#!/usr/bin/env python3
"""
animate_static.py — an implementation of Willett et al., UIST 2018,
"A Mixed-Initiative Interface for Animating Static Pictures".

Seed-agnostic: takes ANY raster image + a few "circle" gestures + a motion path,
and produces a looping animation of the repeating elements.

Pipeline (mirrors the paper's Figures 5, 7, 8):
  Stage A  EXEMPLAR   — user circles objects; LAB k-means (k=15) seeds GrabCut       (§ Finding Exemplar Objects)
  Stage B  SIMILAR    — whole-image GrabCut seeded from exemplars; connected
                        components filtered by area/aspect quartile outliers        (§ Finding Similar Objects)
  Stage C  INPAINT    — fill object holes to produce a clean background plate        (§ Inpainting)
  Stage D  LAYERS     — k-means on object area → depth layers, speed ∝ area          (§ Depth Ordering with Layers)
  Stage E  ANIMATE    — emitter line from motion path; stochastic emission with the
                        paper's P_e controller; auto-scale along path; loop search   (§ Animation Optimization)

Usage:
  python animate_static.py --image X.jpg \
      --circles "0.42,0.55,0.05; 0.61,0.34,0.04" \
      --motion "0.15,0.85 0.85,0.15" \
      --out ./out

Circles and motion points are NORMALISED (0-1) so gestures are resolution-independent.
"""
from __future__ import annotations

import argparse
import json
import math
import random
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

import cv2
import numpy as np

# ----------------------------------------------------------------------------
# Config
# ----------------------------------------------------------------------------

WORK_MAX_DIM = 1400        # process at this scale for speed; paper ran on iPad
LAB_K_EXEMPLAR = 15        # paper: "split the pixels inside the circle into 15 groups"
LAB_K_LAYERS = 30          # paper: "separated into 30 groups" for depth ordering
GRABCUT_ITERS = 5          # paper: "GrabCut with five iterations"


# ----------------------------------------------------------------------------
# Stage A — Finding Exemplar Objects
# ----------------------------------------------------------------------------

def load_image(path: Path) -> tuple[np.ndarray, float]:
    """Load and downscale for processing. Returns (bgr, scale_applied)."""
    img = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if img is None:
        raise SystemExit(f"could not read image: {path}")
    h, w = img.shape[:2]
    scale = min(1.0, WORK_MAX_DIM / max(h, w))
    if scale < 1.0:
        img = cv2.resize(img, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_AREA)
    return img, scale


def extract_exemplars(img: np.ndarray, circles: list[tuple[float, float, float]]) -> np.ndarray:
    """Stage A. For each circled area, LAB k-means picks the foreground group, then GrabCut.

    Paper: "we split the pixels inside the circle into 15 groups using k-means on the
    pixel color in the LAB color space. Next, all groups that are underneath the circles
    are marked as background. For the foreground, we select the group with the furthest
    average distance from all the background groups."
    """
    h, w = img.shape[:2]
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    out = np.zeros((h, w), np.uint8)

    for (cx, cy, cr) in circles:
        px, py, pr = int(cx * w), int(cy * h), int(cr * max(h, w))

        inside = np.zeros((h, w), np.uint8)
        cv2.circle(inside, (px, py), pr, 255, -1)
        # paper: "a circled area is defined by having an inside and outside contour".
        # The ring just OUTSIDE the circle samples the local ground — far more robust
        # than sampling the stroke itself, which may clip the object.
        outer = np.zeros((h, w), np.uint8)
        cv2.circle(outer, (px, py), int(pr * 1.45), 255, -1)
        annulus = cv2.subtract(outer, inside)

        idx = np.where(inside > 0)
        if len(idx[0]) < 50:
            continue
        samples = lab[idx].astype(np.float32)

        k = min(LAB_K_EXEMPLAR, max(2, len(samples) // 20))
        crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
        _, labels, centers = cv2.kmeans(samples, k, None, crit, 3, cv2.KMEANS_PP_CENTERS)
        labels = labels.ravel()

        # cluster the surrounding ground separately; those centres are the background
        a_idx = np.where(annulus > 0)
        if len(a_idx[0]) < 30:
            continue
        a_samples = lab[a_idx].astype(np.float32)
        ak = min(8, max(2, len(a_samples) // 30))
        _, _, bg_centers = cv2.kmeans(a_samples, ak, None, crit, 3, cv2.KMEANS_PP_CENTERS)

        # distance of each in-circle group to the nearest ground colour
        dists = np.array([float(np.min(np.linalg.norm(bg_centers - centers[g], axis=1)))
                          for g in range(k)])
        best_d = float(dists.max())
        if best_d < 8.0:                       # object indistinguishable from its ground
            continue
        # keep the furthest group AND any group nearly as far — lets a bird whose body
        # spans two tones (white body / dark wing) survive as one object
        fg_groups = {g for g in range(k) if dists[g] >= 0.72 * best_d}

        # seed GrabCut: definite FG = chosen groups, definite BG = outside the circle,
        # everything else probably-background (paper's default)
        gc = np.full((h, w), cv2.GC_PR_BGD, np.uint8)
        gc[inside == 0] = cv2.GC_BGD
        sel = np.isin(labels, list(fg_groups))
        fg_pixels = (np.array(idx[0])[sel], np.array(idx[1])[sel])
        gc[fg_pixels] = cv2.GC_FGD

        bgd, fgd = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
        try:
            cv2.grabCut(img, gc, None, bgd, fgd, GRABCUT_ITERS, cv2.GC_INIT_WITH_MASK)
        except cv2.error:
            continue
        out |= np.where((gc == cv2.GC_FGD) | (gc == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)

    return out


# ----------------------------------------------------------------------------
# Stage B — Finding Similar Objects
# ----------------------------------------------------------------------------

@dataclass
class Obj:
    mask: np.ndarray            # full-frame binary mask
    bbox: tuple[int, int, int, int]
    area: float
    aspect: float
    centroid: tuple[float, float]
    is_exemplar: bool = False
    layer: int = 0


def _components(mask: np.ndarray, min_area: int) -> list[Obj]:
    n, lbl, stats, cents = cv2.connectedComponentsWithStats(mask, 8)
    objs: list[Obj] = []
    for i in range(1, n):
        area = float(stats[i, cv2.CC_STAT_AREA])
        if area < min_area:
            continue
        x, y, bw, bh = (stats[i, cv2.CC_STAT_LEFT], stats[i, cv2.CC_STAT_TOP],
                        stats[i, cv2.CC_STAT_WIDTH], stats[i, cv2.CC_STAT_HEIGHT])
        objs.append(Obj(mask=(lbl == i).astype(np.uint8) * 255, bbox=(x, y, bw, bh),
                        area=area, aspect=bw / max(1, bh),
                        centroid=(float(cents[i][0]), float(cents[i][1]))))
    return objs


def find_similar(img: np.ndarray, exemplar_mask: np.ndarray,
                 bg_marks: list[tuple[float, float, float]] | None = None
                 ) -> tuple[list[Obj], list[Obj]]:
    """Stage B. GrabCut over the whole image seeded by the exemplars, then filter
    connected components on area + aspect ratio using the exemplars as ground truth
    with iterative quartile outlier rejection (paper's method).

    `bg_marks` are the paper's "Background" brush strokes. On busy, non-photographic
    grounds (illuminated manuscript, woodblock print) these are not optional — without
    them GrabCut's global GMM cannot separate the objects from a multi-modal ground.
    """
    h, w = img.shape[:2]
    min_area = max(20, (h * w) // 20000)
    exemplars = _components(exemplar_mask, min_area)
    for e in exemplars:
        e.is_exemplar = True
    if not exemplars:
        return [], []

    gc = np.full((h, w), cv2.GC_PR_BGD, np.uint8)   # unknown → probably background
    gc[exemplar_mask > 0] = cv2.GC_FGD
    # image border rows are reliable background seeds
    gc[:2, :] = cv2.GC_BGD
    gc[-2:, :] = cv2.GC_BGD
    for (bx, by, br) in (bg_marks or []):
        cv2.circle(gc, (int(bx * w), int(by * h)), int(br * max(h, w)),
                   int(cv2.GC_BGD), -1)
    gc[exemplar_mask > 0] = cv2.GC_FGD              # foreground always wins
    bgd, fgd = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
    try:
        cv2.grabCut(img, gc, None, bgd, fgd, GRABCUT_ITERS, cv2.GC_INIT_WITH_MASK)
    except cv2.error:
        return exemplars, exemplars

    fg = np.where((gc == cv2.GC_FGD) | (gc == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
    fg = cv2.morphologyEx(fg, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    candidates = _components(fg, min_area)

    # iterative quartile filtering, seeded from the exemplars' area/aspect
    truth = list(exemplars)
    for _ in range(6):
        areas = np.array([o.area for o in truth])
        aspects = np.array([o.aspect for o in truth])
        aq1, aq3 = np.percentile(areas, [25, 75])
        air = max(aq3 - aq1, areas.mean() * 0.5)
        sq1, sq3 = np.percentile(aspects, [25, 75])
        sir = max(sq3 - sq1, 0.25)
        keep = [o for o in candidates
                if (aq1 - 1.5 * air) <= o.area <= (aq3 + 1.5 * air)
                and (sq1 - 1.5 * sir) <= o.aspect <= (sq3 + 1.5 * sir)]
        if len(keep) == len(truth):
            break
        truth = keep if keep else truth

    # exemplars are ground truth — always retained
    found = list(truth)
    for e in exemplars:
        if not any(abs(e.centroid[0] - o.centroid[0]) < 3 and abs(e.centroid[1] - o.centroid[1]) < 3
                   for o in found):
            found.append(e)
    return found, exemplars


# ----------------------------------------------------------------------------
# Stage C — Inpainting
# ----------------------------------------------------------------------------

def inpaint_background(img: np.ndarray, objs: list[Obj]) -> np.ndarray:
    """Stage C. Paper uses PatchMatch; cv2.inpaint (Telea) is the stand-in here —
    good enough on smooth grounds, visibly weaker on textured ones."""
    mask = np.zeros(img.shape[:2], np.uint8)
    for o in objs:
        mask |= (o.mask > 0).astype(np.uint8) * 255
    mask = cv2.dilate(mask, np.ones((7, 7), np.uint8), iterations=2)
    return cv2.inpaint(img, mask, 5, cv2.INPAINT_TELEA)


# ----------------------------------------------------------------------------
# Stage D — Depth Ordering with Layers
# ----------------------------------------------------------------------------

def assign_layers(objs: list[Obj], n_layers: int) -> None:
    """k-means on object area → layers. Paper: 'each subsequent layer speed is
    proportional to that layer's average object area divided by the original
    layer's average object area.'"""
    if n_layers <= 1 or len(objs) < n_layers:
        return
    areas = np.array([[o.area] for o in objs], np.float32)
    crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    _, labels, centers = cv2.kmeans(areas, n_layers, None, crit, 5, cv2.KMEANS_PP_CENTERS)
    order = np.argsort(centers.ravel())            # smallest area = furthest back
    remap = {int(old): new for new, old in enumerate(order)}
    for o, l in zip(objs, labels.ravel()):
        o.layer = remap[int(l)]


# ----------------------------------------------------------------------------
# Stage E — Animation Optimization
# ----------------------------------------------------------------------------

@dataclass
class Sprite:
    """A cut-out exemplar object, ready to be emitted as a particle."""
    rgb: np.ndarray
    alpha: np.ndarray
    base_area: float


@dataclass
class Particle:
    sprite: int
    t0: float
    emit_idx: int
    offset: np.ndarray
    speed: float
    layer: int
    rot: float


def cut_sprites(img: np.ndarray, objs: list[Obj]) -> list[Sprite]:
    sprites = []
    for o in objs:
        x, y, bw, bh = o.bbox
        pad = 2
        x0, y0 = max(0, x - pad), max(0, y - pad)
        x1, y1 = min(img.shape[1], x + bw + pad), min(img.shape[0], y + bh + pad)
        rgb = img[y0:y1, x0:x1].copy()
        a = (o.mask[y0:y1, x0:x1] > 0).astype(np.float32)
        a = cv2.GaussianBlur(a, (3, 3), 0)          # feather the cut edge
        if rgb.size == 0:
            continue
        sprites.append(Sprite(rgb=rgb, alpha=a, base_area=o.area))
    return sprites


def build_emitter(objs: list[Obj], motion: np.ndarray, shape) -> tuple[np.ndarray, np.ndarray]:
    """Emitter line: perpendicular to the motion path's start, pushed outside the
    objects' convex hull, then extended to cover the object region (paper Fig. 10)."""
    h, w = shape[:2]
    pts = np.array([o.centroid for o in objs], np.float32)
    d = motion[1] - motion[0]
    d = d / (np.linalg.norm(d) + 1e-6)
    perp = np.array([-d[1], d[0]], np.float32)

    # project all object centroids onto the perpendicular to size the emitter
    proj = (pts - motion[0]) @ perp
    lo, hi = float(proj.min()), float(proj.max())
    span = max(hi - lo, 0.15 * max(h, w))
    mid = (hi + lo) / 2.0

    # push the line back along the motion direction, outside the object hull
    along = (pts - motion[0]) @ d
    back = motion[0] + d * (float(along.min()) - 0.10 * max(h, w))

    a = back + perp * (mid - span * 0.62)
    b = back + perp * (mid + span * 0.62)
    return a.astype(np.float32), b.astype(np.float32)


def fit_scale_over_path(objs: list[Obj], motion: np.ndarray) -> tuple[float, float]:
    """Paper Fig. 11b: fit a line through (path fraction, area / mean exemplar area)
    so emitted objects scale the way the source image's objects do."""
    d = motion[1] - motion[0]
    L = float(np.linalg.norm(d)) + 1e-6
    d = d / L
    xs, ys = [], []
    mean_area = float(np.mean([o.area for o in objs]))
    for o in objs:
        t = float(np.clip((np.array(o.centroid) - motion[0]) @ d / L, 0.0, 1.0))
        xs.append(t)
        ys.append(o.area / max(mean_area, 1e-6))
    if len(xs) < 3:
        return 1.0, 0.0
    slope, intercept = np.polyfit(np.array(xs), np.array(ys), 1)
    return float(intercept), float(slope)


def schedule_emissions(n_target: int, duration: float, dt: float, lifetime: float,
                       n_emit_points: int, rng: random.Random) -> list[tuple[float, int]]:
    """The paper's stochastic emission controller.

        P_e(t_i) = P_d(t_i - t_{i-1})                if t_i < D/v      (fill phase)
                 = P_d(t_i - t_{i-1}) * C(n)         otherwise         (steady state)
        P_d(delta) = N*v*delta / D
        C(n) = 2e^x/(e^x+1), x = N - n

    Emit points are weighted by distance to the most recently used point, so
    particles spread rather than clump.
    """
    D = 1.0
    v = 1.0 / max(lifetime, 1e-6)         # normalised: travel the path in `lifetime`
    fill_until = D / v
    Pd = (n_target * v * dt) / D

    emissions: list[tuple[float, int]] = []
    live: list[float] = []                # birth times of on-screen particles
    last_pt = None
    t = 0.0
    while t < duration:
        live = [b for b in live if t - b < lifetime]
        n = len(live)
        if t < fill_until:
            p = Pd
        else:
            x = float(np.clip(n_target - n, -30, 30))
            p = Pd * (2.0 * math.exp(x) / (math.exp(x) + 1.0))
        if rng.random() < min(p, 1.0):
            if last_pt is None:
                pt = rng.randrange(n_emit_points)
            else:
                # weight each candidate point by its distance from the last emission
                w = np.array([abs(i - last_pt) + 0.5 for i in range(n_emit_points)], np.float64)
                pt = int(rng.choices(range(n_emit_points), weights=w / w.sum())[0])
            emissions.append((t, pt))
            live.append(t)
            last_pt = pt
        t += dt
    return emissions


def find_loop(emissions: list[tuple[float, int]], lifetime: float, K: int = 12
              ) -> tuple[float, float]:
    """Paper's loop search. Minimise

        D_ij = sum_{k=0}^{K-1} (K-k)/K * ( |(t_{i+k}-t_i) - (t_{j+k}-t_j)| + |e_{i+k}-e_{j+k}| )

    over emission-window pairs, with the interval between 2x and 4x particle lifetime.
    """
    ts = np.array([e[0] for e in emissions], np.float64)
    es = np.array([e[1] for e in emissions], np.float64)
    n = len(ts)
    if n < 2 * K + 4:
        return 0.0, float(lifetime * 3)

    lo, hi = 2.0 * lifetime, 4.0 * lifetime
    best, best_pair = float("inf"), (0, n - 1)
    wk = np.array([(K - k) / K for k in range(K)], np.float64)
    for i in range(0, n - K):
        for j in range(i + 1, n - K):
            dur = ts[j] - ts[i]
            if dur < lo:
                continue
            if dur > hi:
                break
            dt_i = ts[i:i + K] - ts[i]
            dt_j = ts[j:j + K] - ts[j]
            d = float(np.sum(wk * (np.abs(dt_i - dt_j) + np.abs(es[i:i + K] - es[j:j + K]))))
            if d < best:
                best, best_pair = d, (i, j)
    return float(ts[best_pair[0]]), float(ts[best_pair[1]])


def composite(bg: np.ndarray, sprite: Sprite, cx: float, cy: float,
              scale: float, alpha: float, rot: float) -> None:
    """Alpha-composite one scaled/rotated sprite into the background, in place."""
    if scale <= 0.02 or alpha <= 0.01:
        return
    sh, sw = sprite.rgb.shape[:2]
    nw, nh = max(1, int(sw * scale)), max(1, int(sh * scale))
    if nw < 2 or nh < 2 or nw > bg.shape[1] * 2 or nh > bg.shape[0] * 2:
        return
    rgb = cv2.resize(sprite.rgb, (nw, nh), interpolation=cv2.INTER_AREA)
    a = cv2.resize(sprite.alpha, (nw, nh), interpolation=cv2.INTER_AREA)

    if abs(rot) > 0.5:
        M = cv2.getRotationMatrix2D((nw / 2, nh / 2), rot, 1.0)
        rgb = cv2.warpAffine(rgb, M, (nw, nh), flags=cv2.INTER_LINEAR,
                             borderMode=cv2.BORDER_REPLICATE)
        a = cv2.warpAffine(a, M, (nw, nh), flags=cv2.INTER_LINEAR, borderValue=0)

    x0, y0 = int(cx - nw / 2), int(cy - nh / 2)
    x1, y1 = x0 + nw, y0 + nh
    bx0, by0 = max(0, x0), max(0, y0)
    bx1, by1 = min(bg.shape[1], x1), min(bg.shape[0], y1)
    if bx0 >= bx1 or by0 >= by1:
        return
    sx0, sy0 = bx0 - x0, by0 - y0
    sx1, sy1 = sx0 + (bx1 - bx0), sy0 + (by1 - by0)

    aa = (a[sy0:sy1, sx0:sx1] * alpha)[..., None]
    roi = bg[by0:by1, bx0:bx1].astype(np.float32)
    src = rgb[sy0:sy1, sx0:sx1].astype(np.float32)
    bg[by0:by1, bx0:bx1] = (roi * (1 - aa) + src * aa).astype(np.uint8)


def render(bg: np.ndarray, sprites: list[Sprite], objs: list[Obj], motion: np.ndarray,
           emitter: tuple[np.ndarray, np.ndarray], out_dir: Path, fps: int,
           n_layers: int, seed: int, granular: float) -> int:
    rng = random.Random(seed)
    n_target = len(objs)
    lifetime = 4.0
    dt = 1.0 / fps
    n_emit_points = 24

    emissions = schedule_emissions(n_target, duration=40.0, dt=dt, lifetime=lifetime,
                                   n_emit_points=n_emit_points, rng=rng)
    t_start, t_end = find_loop(emissions, lifetime)
    period = t_end - t_start

    s0, s1 = fit_scale_over_path(objs, motion)
    a, b = emitter
    path_vec = motion[1] - motion[0]

    # layer speed ∝ mean layer area / mean overall area  (paper, Depth Ordering)
    mean_all = float(np.mean([o.area for o in objs]))
    layer_speed = {}
    for l in range(n_layers):
        ms = [o.area for o in objs if o.layer == l]
        layer_speed[l] = (float(np.mean(ms)) / mean_all) if ms else 1.0

    parts: list[Particle] = []
    for (t, ei) in emissions:
        layer = rng.randrange(n_layers)
        parts.append(Particle(
            sprite=rng.randrange(len(sprites)), t0=t, emit_idx=ei,
            offset=(a + (b - a) * (ei / (n_emit_points - 1))).astype(np.float32),
            speed=layer_speed[layer] * rng.uniform(0.9, 1.1),
            layer=layer, rot=rng.uniform(-1, 1) * granular * 25.0))

    frames_dir = out_dir / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    n_frames = int(round(period * fps))
    mean_sprite_area = float(np.mean([s.base_area for s in sprites]))

    for f in range(n_frames):
        t = t_start + f * dt
        canvas = bg.copy()
        # draw back-to-front for depth ordering
        for layer in range(n_layers):
            for p in parts:
                if p.layer != layer:
                    continue
                # a particle also appears one loop-period earlier/later, so the
                # seam is continuous (paper: duplicate particles across the seam)
                for shift in (-period, 0.0, period):
                    age = (t - (p.t0 + shift)) * p.speed
                    if age < 0 or age > lifetime:
                        continue
                    u = age / lifetime
                    pos = p.offset + path_vec * u
                    rel = (s0 + s1 * u) * (mean_sprite_area / max(sprites[p.sprite].base_area, 1))
                    scale = float(np.clip(rel, 0.05, 4.0))
                    fade = float(np.clip(min(u, 1 - u) / 0.12, 0.0, 1.0))
                    composite(canvas, sprites[p.sprite], float(pos[0]), float(pos[1]),
                              scale, fade, p.rot * math.sin(u * math.pi * 2))
        cv2.imwrite(str(frames_dir / f"f{f:04d}.png"), canvas)

    return n_frames


# ----------------------------------------------------------------------------

def parse_circles(s: str) -> list[tuple[float, float, float]]:
    out = []
    for part in s.split(";"):
        part = part.strip()
        if not part:
            continue
        x, y, r = (float(v) for v in part.split(","))
        out.append((x, y, r))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--image", required=True, type=Path)
    ap.add_argument("--circles", required=True, help="normalised 'cx,cy,r; cx,cy,r'")
    ap.add_argument("--bg", default="", help="background-brush marks, 'cx,cy,r; ...'")
    ap.add_argument("--motion", required=True, help="normalised 'x0,y0 x1,y1'")
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--layers", type=int, default=3)
    ap.add_argument("--fps", type=int, default=20)
    ap.add_argument("--granular", type=float, default=0.5, help="rotation jitter 0-1")
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    img, scale = load_image(args.image)
    h, w = img.shape[:2]
    print(f"[load] {args.image.name} → working at {w}x{h} (scale {scale:.3f})")

    circles = parse_circles(args.circles)
    p0, p1 = args.motion.split()
    motion = np.array([[float(v) for v in p0.split(",")],
                       [float(v) for v in p1.split(",")]], np.float32)
    motion[:, 0] *= w
    motion[:, 1] *= h

    print(f"[A] exemplars from {len(circles)} circle gesture(s)…")
    ex_mask = extract_exemplars(img, circles)
    cv2.imwrite(str(args.out / "a_exemplars.png"),
                cv2.bitwise_and(img, img, mask=ex_mask))

    bg_marks = parse_circles(args.bg) if args.bg else []
    print(f"[B] searching for similar objects ({len(bg_marks)} bg mark(s))…")
    objs, exemplars = find_similar(img, ex_mask, bg_marks)
    print(f"    exemplars={len(exemplars)}  similar found={len(objs)}")
    if not objs:
        raise SystemExit("no objects found — try different circles")

    vis = img.copy()
    for o in objs:
        colour = (255, 0, 255) if not o.is_exemplar else (0, 255, 0)
        cv2.drawContours(vis, cv2.findContours(o.mask, cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_SIMPLE)[0], -1, colour, 2)
    cv2.imwrite(str(args.out / "b_similar.png"), vis)

    print("[C] inpainting background…")
    bg = inpaint_background(img, objs)
    cv2.imwrite(str(args.out / "c_background.png"), bg)

    print(f"[D] assigning {args.layers} depth layers…")
    assign_layers(objs, args.layers)

    print("[E] animating…")
    sprites = cut_sprites(img, objs)
    emitter = build_emitter(objs, motion, img.shape)
    n = render(bg, sprites, objs, motion, emitter, args.out, args.fps,
               args.layers, args.seed, args.granular)
    print(f"    rendered {n} frames")

    gif = args.out / "animation.gif"
    mp4 = args.out / "animation.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(args.fps),
                    "-i", str(args.out / "frames" / "f%04d.png"),
                    "-vf", "scale=720:-2:flags=lanczos,split[s0][s1];"
                           "[s0]palettegen[p];[s1][p]paletteuse",
                    "-loop", "0", str(gif)], check=False)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(args.fps),
                    "-i", str(args.out / "frames" / "f%04d.png"),
                    "-c:v", "libx264", "-pix_fmt", "yuv420p",
                    "-vf", "scale=720:-2", str(mp4)], check=False)

    (args.out / "run.json").write_text(json.dumps({
        "image": str(args.image), "circles": circles,
        "motion": motion.tolist(), "objects_found": len(objs),
        "exemplars": len(exemplars), "layers": args.layers,
        "frames": n, "fps": args.fps,
    }, indent=2))
    print(f"[done] {gif}")


if __name__ == "__main__":
    main()
