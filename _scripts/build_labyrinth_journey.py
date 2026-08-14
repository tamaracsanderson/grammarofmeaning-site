#!/usr/bin/env python3
"""build_labyrinth_journey.py — curate the six-signpost gospel labyrinth's image feed (miniature-as-relevance).

The Garden's gospels labyrinth is a pan/zoom MAP (Leaflet CRS.Simple): the unicursal path winds through the six
canonical gospel signposts (Nativity → Wilderness → Teaching → Signs → Passion → Resurrection, the reading-room ToC),
with a CLUSTER of curated miniatures at each. This script IS the curation black box (§2.15):

  input:   six signposts, each with the scene-titles that name it
  filter:  a work is KEPT only if (a) it has a CC0/PD image, AND (b) its TITLE names the scene (not a fuzzy keyword).
           That title-match is the relevance guarantee the PI asked for — no "weird out-of-context images through a filter".
  rank:    prefer the MINIATURE aesthetic — illuminated-manuscript leaves, tempera/gold/parchment, icon/panel — which is
           BOTH the look she wants AND genuinely cross-tradition (Byzantine/Ethiopian/Armenian/Persian illumination share it).
  output:  engine/data/labyrinth/journey_gospels.json — the render-from-data feed the Leaflet kernel + flip-card read.

Source: Cleveland Museum of Art open-access API (CORS '*', CC0, images load cross-origin, rich medieval/Byzantine holdings).
  Met is queried opportunistically with a small budget + graceful fail (it intermittently 403/429s). Seed-agnostic +
  idempotent: re-run any time; same signposts in, refreshed curation out.

Usage:  python3 _scripts/build_labyrinth_journey.py            # curate + write + report
        python3 _scripts/build_labyrinth_journey.py --cap 10   # override per-signpost tile cap
"""
from __future__ import annotations
import argparse, json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

DEPLOY = Path(__file__).resolve().parents[1]
OUT = DEPLOY / "engine" / "data" / "labyrinth" / "journey_gospels.json"

CLE = "https://openaccess-api.clevelandart.org/api/artworks/"

# The six canonical gospel signposts (reading-room house-pattern ToC). Each carries: the scene-title keywords that a work's
# TITLE must contain to be kept (the relevance gate), and the ToC one-liner/refs shown in the walk.
SIGNPOSTS = [
    {"n":"I","key":"nativity","title":"Nativity","latin":"Adventus","refs":"Mt 1–2 · Lk 1–2",
     "line":"A birth reported by two witnesses and passed over in silence by two others.",
     "scenes":["nativity","adoration of the shepherds","adoration of the magi","adoration of the christ child",
               "adoration of the kings","virgin and child","madonna and child","annunciation","holy family"]},
    {"n":"II","key":"wilderness","title":"Wilderness","latin":"Desertum","refs":"Mk 1 · Mt 3–4 · Lk 3–4",
     "line":"Driven into the desert to be tested before the work begins.",
     "scenes":["baptism of christ","baptism of jesus","temptation of christ","john the baptist","christ in the wilderness",
               "saint john the baptist"]},
    {"n":"III","key":"teaching","title":"Teaching","latin":"Doctrina","refs":"the Sermon · the parables",
     "line":"The one who speaks in stories, so that seeing they might not see.",
     "scenes":["christ and the adulteress","sermon on the mount","christ teaching","christ preaching","christ among the doctors",
               "parable","the good shepherd","christ blessing","sermon"]},
    {"n":"IV","key":"signs","title":"Signs","latin":"Signa","refs":"Cana · the healings · Lazarus",
     "line":"Water into wine, sight to the blind, the dead called out by name.",
     "scenes":["marriage at cana","marriage feast at cana","wedding at cana","raising of lazarus","christ healing","the miracle",
               "feeding of the","walking on water","transfiguration","christ and the samaritan","loaves and fishes","miracle of"]},
    {"n":"V","key":"passion","title":"Passion","latin":"Passio","refs":"the Cross",
     "line":"The turning the whole story leans toward.",
     "scenes":["crucifixion","the passion","christ carrying the cross","carrying of the cross","last supper","agony in the garden",
               "flagellation","descent from the cross","lamentation","entombment","ecce homo","betrayal of christ","crown of thorns",
               "pieta","man of sorrows","christ on the cross","deposition"]},
    {"n":"VI","key":"resurrection","title":"Resurrection","latin":"Resurrectio","refs":"Mt 28 · Mk 16 · Lk 24 · Jn 20",
     "line":"The empty tomb told four ways — and one of the four ends in fear and says nothing.",
     "scenes":["resurrection","anastasis","noli me tangere","harrowing of hell","empty tomb","maries at the tomb",
               "holy women at the tomb","doubting thomas","incredulity of thomas","road to emmaus","supper at emmaus",
               "ascension of christ","three marys","women at the sepulchre"]},
]

# miniature-ness rank: illuminated manuscript > icon/tempera-gold panel > embroidery/enamel > print/oil.
MINIATURE_STRONG = re.compile(r"parchment|vellum|tempera|illumin|manuscript|gold ground|gold leaf", re.I)
MINIATURE_MED    = re.compile(r"icon|panel|egg tempera|enamel|embroider|gold thread|miniature", re.I)

# negative guard — a work whose TITLE names a scene can still be off-scene (a landscape titled "…Parable of…",
# a portrait, a study). Drop these so the field stays on-scene (the PI's "no weird out-of-context images" rule).
OFF_SCENE = re.compile(r"view of|landscape|still life|self.?portrait|liber veritatis|study of|academy|"
                       r"design for|ornament|frame|coat of arms|figure study|drapery", re.I)


def get(url: str, tries: int = 3, pause: float = 1.5):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "grammarofmeaning-labyrinth/1.0"})
            with urllib.request.urlopen(req, timeout=25) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            if i == tries - 1:
                print(f"    ! fetch failed ({e})")
                return None
            time.sleep(pause * (i + 1))
    return None


def title_names_scene(title: str, scenes: list[str]) -> str | None:
    t = title.lower()
    for s in scenes:
        if s in t:
            return s
    return None


def rank(medium: str, typ: str) -> int:
    m = f"{medium} {typ}"
    if MINIATURE_STRONG.search(m):
        return 3
    if MINIATURE_MED.search(m):
        return 2
    if re.search(r"paint", m, re.I):
        return 1
    return 0


def cleveland_for(sp: dict) -> list[dict]:
    """query Cleveland per scene-term; keep works whose TITLE names the scene; return normalized tiles."""
    seen, tiles = set(), []
    for term in sp["scenes"]:
        q = urllib.parse.quote(term)
        d = get(f"{CLE}?q={q}&cc0=1&has_image=1&limit=40")
        if not d:
            continue
        for a in d.get("data", []):
            aid = a.get("id")
            if aid in seen:
                continue
            title = (a.get("title") or "").strip()
            if OFF_SCENE.search(title):
                continue
            scene = title_names_scene(title, sp["scenes"])
            if not scene:
                continue
            imgs = a.get("images") or {}
            web = (imgs.get("web") or {}).get("url")
            if not web:
                continue
            seen.add(aid)
            typ = a.get("type") or ""
            medium = (a.get("technique") or "")
            cultures = a.get("culture") or []
            culture = ""
            if cultures:
                c0 = cultures[0]
                culture = (c0.get("culture") if isinstance(c0, dict) else str(c0)) or ""
                culture = re.sub(r",?\s*\d.*$", "", culture).strip()  # drop trailing century/date
            tiles.append({
                "id": f"cle-{aid}",
                "img": web,
                "full": (imgs.get("print") or {}).get("url") or web,
                "title": title,
                "culture": culture,
                "date": a.get("creation_date") or (str(a.get("creation_date_earliest")) if a.get("creation_date_earliest") else ""),
                "museum": "Cleveland Museum of Art",
                "license": "CC0",
                "medium": medium,
                "type": typ,
                "scene": scene,
                "url": a.get("url") or f"https://www.clevelandart.org/art/{aid}",
                "_rank": rank(medium, typ),
            })
    return tiles


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cap", type=int, default=12, help="max tiles per signpost")
    args = ap.parse_args()

    out_signposts, total = [], 0
    for sp in SIGNPOSTS:
        print(f"  {sp['n']}. {sp['title']} …")
        tiles = cleveland_for(sp)
        tiles.sort(key=lambda t: (-t["_rank"], t["date"] or "9999"))  # miniature-first, then oldest
        kept = tiles[: args.cap]
        for t in kept:
            t.pop("_rank", None)
        total += len(kept)
        strong = sum(1 for t in kept if MINIATURE_STRONG.search(f"{t['medium']} {t['type']}"))
        print(f"     kept {len(kept)} (of {len(tiles)} on-scene) · {strong} illuminated-manuscript-grade")
        out_signposts.append({
            "n": sp["n"], "key": sp["key"], "title": sp["title"], "latin": sp["latin"],
            "refs": sp["refs"], "line": sp["line"], "tiles": kept,
        })

    feed = {
        "engine": "labyrinth_gospels_v1",
        "_producing_script": "_scripts/build_labyrinth_journey.py",
        "_method_summary": ("Six-signpost gospel labyrinth. Tiles curated from the Cleveland Museum open-access API "
                            "(CC0). A work is kept ONLY if its TITLE names the scene (the relevance gate — no fuzzy "
                            "keyword filler) AND it carries a CC0 image; ranked miniature-first (illuminated manuscript "
                            "> icon/tempera-gold panel > painting). The Resurrection signpost carries the 4-gospel braid "
                            "as its narrative; per-image sitz/paradigm coding rides on Stage-6 coding progress (Mark 16 today)."),
        "signposts": out_signposts,
        "total_tiles": total,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(feed, indent=2, ensure_ascii=False))
    print(f"\n  wrote {OUT.relative_to(DEPLOY)} · {total} tiles across {len(out_signposts)} signposts")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# ── METHODOLOGY FOOTER ──
# HOW PRODUCED: Design SB S171 (2026-08-14). PI locked the gospels labyrinth as a pan/zoom MAP (Leaflet CRS.Simple) winding
#   through the six reading-room signposts, image-heavy but RELEVANT ("no weird out-of-context images through a filter").
#   This curates the feed with the title-names-the-scene gate as the relevance guarantee + miniature-medium rank as the
#   aesthetic (which is also cross-tradition). Cleveland API = spine (CORS/CC0/rich medieval holdings, images load x-origin).
# SCHOLARLY SOURCES: reading_room_house_pattern.html (the canonical six-signpost gospel ToC); labyrinth_DWS_2026-08-13.md;
#   §2.15 (input→black-box→output; curation as a declared-gate step); §2.16 render-from-data; §2.8 provenance-as-honoring.
# WHAT NEEDS VERIFICATION: (1) final VISUAL QA per tile (does the image clearly show the scene) is a browser pass — the
#   title-match is a strong metadata first-curation, not a substitute for eyes. (2) Met/Wikimedia as secondary sources for
#   thinner signposts (Teaching/Wilderness) — add if Cleveland yield is low. (3) per-image braid/paradigm tags await Stage-6.
