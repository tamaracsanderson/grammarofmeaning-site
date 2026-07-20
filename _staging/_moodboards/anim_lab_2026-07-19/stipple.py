#!/usr/bin/env python3
"""
stipple.py — weighted Voronoi stippling.

A port of Mike Bostock's "Voronoi Stippling" notebook
(https://observablehq.com/@mbostock/voronoi-stippling), which implements the
weighted variant of Lloyd's algorithm from:

    Adrian Secord, "Weighted Voronoi Stippling", NPAR 2002.

The idea: scatter n points over an image, then repeatedly move each point to the
*luminance-weighted centroid* of its Voronoi cell. Dark regions pull harder, so the
points settle at a density proportional to image darkness — reproducing the tonal
range with nothing but uniform dots, the way a 19th-century engraver would.

Faithful to Bostock's constants:
  * rejection-sampled initialisation, max 30 tries per point
  * 80 relaxation iterations
  * over-relaxation factor 1.8 (moves PAST the centroid — converges much faster)
  * annealed jitter  w = (k+1)^-0.8 * 10,  uniform in ±w/2, to escape local minima

Substitution: Bostock uses d3-delaunay's `find()` with a hint for nearest-point
lookup. Here a scipy cKDTree does the same job — same assignment, different index.

Usage:
  python stipple.py --image portrait.jpg --points 8000 --out ./out
"""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
from scipy.spatial import cKDTree

# Bostock's constants
ITERATIONS = 80
OVER_RELAX = 1.8
JITTER_SCALE = 10.0
JITTER_DECAY = -0.8
MAX_REJECT_TRIES = 30


def load_density(path: Path, width: int, gamma: float, invert: bool,
                 stretch: tuple[float, float] | None = None,
                 floor: float = 0.0) -> np.ndarray:
    """Image -> density field in [0,1]. Darker = denser (more dots).

    `stretch` applies a percentile tone curve BEFORE gamma. This is not cosmetic:
    stippling reproduces tone faithfully, so a low-contrast source yields a
    low-contrast — i.e. illegible — stipple. A 19th-century engraver working from the
    same photograph would likewise re-map the tonal range rather than transcribe it.
    Doing it here makes that interpretive step explicit and reportable instead of
    hiding it inside a "nicer" result.
    """
    im = Image.open(path).convert("L")
    h = max(1, round(im.height * width / im.width))
    im = im.resize((width, h), Image.LANCZOS)
    v = np.asarray(im, dtype=np.float64) / 255.0
    d = v if invert else 1.0 - v          # default: darkness drives density

    if stretch is not None:
        lo, hi = np.percentile(d, stretch)
        if hi > lo:
            d = np.clip((d - lo) / (hi - lo), 0.0, 1.0)

    d = np.clip(d, 0.0, 1.0) ** gamma
    if d.max() > 0:
        d = d / d.max()
    # a floor keeps the lightest regions from going completely bare
    return np.clip(d, floor, 1.0) if floor > 0 else d


def rejection_sample(density: np.ndarray, n: int, rng: np.random.Generator) -> np.ndarray:
    """Bostock's init: try up to 30 random positions per point, accept with p=density."""
    h, w = density.shape
    pts = np.empty((n, 2))
    xs = rng.integers(0, w, size=(n, MAX_REJECT_TRIES))
    ys = rng.integers(0, h, size=(n, MAX_REJECT_TRIES))
    us = rng.random((n, MAX_REJECT_TRIES))
    accept = us < density[ys, xs]
    # first accepted try per point; fall back to the last try if none accepted
    first = np.where(accept.any(axis=1), accept.argmax(axis=1), MAX_REJECT_TRIES - 1)
    rows = np.arange(n)
    pts[:, 0] = xs[rows, first]
    pts[:, 1] = ys[rows, first]
    return pts


def stipple(density: np.ndarray, n: int, iterations: int, rng: np.random.Generator,
            snapshot_at: set[int] | None = None, out_dir: Path | None = None,
            dot: float = 1.0) -> tuple[np.ndarray, list[int]]:
    """Weighted Lloyd's relaxation. Returns (points, iterations_snapshotted)."""
    h, w = density.shape
    pts = rejection_sample(density, n, rng)

    # pixel centres and their weights, flattened once
    yy, xx = np.mgrid[0:h, 0:w]
    px = (xx + 0.5).ravel()
    py = (yy + 0.5).ravel()
    wt = density.ravel()
    # pixels with zero weight contribute nothing to any centroid — drop them
    keep = wt > 1e-6
    px, py, wt = px[keep], py[keep], wt[keep]
    coords = np.column_stack([px, py])

    snaps: list[int] = []
    for k in range(iterations):
        # assign every weighted pixel to its nearest point (= its Voronoi cell)
        idx = cKDTree(pts).query(coords, workers=-1)[1]

        # weighted centroid per cell
        s = np.bincount(idx, weights=wt, minlength=n)
        cx = np.bincount(idx, weights=wt * px, minlength=n)
        cy = np.bincount(idx, weights=wt * py, minlength=n)
        nonzero = s > 0
        tx = np.where(nonzero, cx / np.maximum(s, 1e-12), pts[:, 0])
        ty = np.where(nonzero, cy / np.maximum(s, 1e-12), pts[:, 1])

        # over-relax past the centroid, plus annealed jitter so points don't stick
        jw = ((k + 1) ** JITTER_DECAY) * JITTER_SCALE
        pts[:, 0] = pts[:, 0] + (tx - pts[:, 0]) * OVER_RELAX + (rng.random(n) - 0.5) * jw
        pts[:, 1] = pts[:, 1] + (ty - pts[:, 1]) * OVER_RELAX + (rng.random(n) - 0.5) * jw
        np.clip(pts[:, 0], 0, w - 1, out=pts[:, 0])
        np.clip(pts[:, 1], 0, h - 1, out=pts[:, 1])

        if snapshot_at and (k + 1) in snapshot_at and out_dir is not None:
            render(pts, (h, w), dot).save(out_dir / f"iter_{k+1:03d}.png")
            snaps.append(k + 1)

    return pts, snaps


def render(pts: np.ndarray, shape: tuple[int, int], dot: float, scale: int = 3,
           weights: np.ndarray | None = None) -> Image.Image:
    """Draw the stipple. Supersampled then downsampled for clean anti-aliased dots."""
    from PIL import ImageDraw
    h, w = shape
    im = Image.new("L", (w * scale, h * scale), 255)
    dr = ImageDraw.Draw(im)
    for i, (x, y) in enumerate(pts):
        r = dot * scale * (0.5 + weights[i]) if weights is not None else dot * scale
        dr.ellipse([x * scale - r, y * scale - r, x * scale + r, y * scale + r], fill=0)
    return im.resize((w, h), Image.LANCZOS)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--image", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--points", type=int, default=8000)
    ap.add_argument("--width", type=int, default=600, help="density-field width in px")
    ap.add_argument("--iterations", type=int, default=ITERATIONS)
    ap.add_argument("--gamma", type=float, default=1.0, help=">1 lightens, <1 darkens")
    ap.add_argument("--stretch", default="", help="percentile tone curve, e.g. '5,95'")
    ap.add_argument("--floor", type=float, default=0.0, help="min density (keeps lights populated)")
    ap.add_argument("--dot", type=float, default=1.0, help="dot radius, density px")
    ap.add_argument("--invert", action="store_true", help="dots in LIGHT regions instead")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--gif", action="store_true", help="also render a convergence GIF")
    args = ap.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(args.seed)

    stretch = None
    if args.stretch:
        lo, hi = (float(v) for v in args.stretch.split(","))
        stretch = (lo, hi)
    density = load_density(args.image, args.width, args.gamma, args.invert,
                           stretch, args.floor)
    h, w = density.shape
    print(f"[load] {args.image.name} → density field {w}x{h}, "
          f"mean darkness {density.mean():.3f}, tone curve "
          f"{'p%g–p%g γ%g' % (stretch[0], stretch[1], args.gamma) if stretch else 'none'}")

    Image.fromarray((density * 255).astype(np.uint8)).save(args.out / "a_density.png")

    snapshot_at = {1, 2, 3, 5, 8, 12, 18, 25, 35, 50, 65, args.iterations} if args.gif else None
    print(f"[relax] {args.points} points × {args.iterations} iterations "
          f"(over-relax {OVER_RELAX}, annealed jitter)…")
    pts, snaps = stipple(density, args.points, args.iterations, rng,
                         snapshot_at, args.out, args.dot)

    render(pts, (h, w), args.dot).save(args.out / "b_stipple.png")
    print(f"[done] {args.out/'b_stipple.png'}")

    if args.gif and snaps:
        frames = [args.out / f"iter_{k:03d}.png" for k in snaps]
        # hold the final frame so the loop reads as "settling"
        listfile = args.out / "frames.txt"
        listfile.write_text("".join(
            f"file '{f.name}'\nduration {0.55 if i < len(frames)-1 else 2.2}\n"
            for i, f in enumerate(frames)))
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat",
                        "-i", listfile.name, "-vf",
                        "scale=420:-2:flags=lanczos,split[a][b];"
                        "[a]palettegen=max_colors=32[p];[b][p]paletteuse",
                        "-loop", "0", "convergence.gif"],
                       cwd=args.out, check=False)   # paths are relative to cwd
        print(f"[done] {args.out/'convergence.gif'} ({len(snaps)} snapshots)")

    (args.out / "run.json").write_text(json.dumps({
        "image": str(args.image), "points": args.points, "iterations": args.iterations,
        "density_field": [w, h], "gamma": args.gamma, "dot": args.dot,
        "stretch": args.stretch or None, "floor": args.floor,
        "over_relaxation": OVER_RELAX, "seed": args.seed,
    }, indent=2))


if __name__ == "__main__":
    main()
