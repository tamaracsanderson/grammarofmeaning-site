#!/usr/bin/env python3
"""build_morphospace_suite_feeds.py — derive the 3 morphospace-suite deploy feeds from the twelve-laws canonicals.

The archetype / mixing / prevalence figures render from deploy-repo COPIES
(engine/data/viz/morphospace_{archetypes,mixing,prevalence}.json). The canonicals live in twelve-laws
(pm/40_architecture/DATA_morphospace_*_feed_s167.json, §2.13, produced by the s167 scripts). When Atlas Reader
re-runs those scripts (e.g. after the Qur'an+Tanakh rebalance), the deploy copies do NOT auto-update — run THIS to
re-derive them, then deploy the changed feeds. Reads the canonicals from twelve-laws origin/main (they're committed),
so it works even though this repo is read-only on that tree.

Usage:  python3 _scripts/build_morphospace_suite_feeds.py            # re-derive + report
"""
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

DEPLOY = Path(__file__).resolve().parents[1]
TWELVE = Path("/Users/tamarasanderson/Documents/twelve-laws")
OUT = DEPLOY / "engine" / "data" / "viz"

# deploy-feed name  ->  twelve-laws canonical basename
FEEDS = {
    "morphospace_archetypes.json":       "DATA_morphospace_archetype_feed_s167.json",
    "morphospace_mixing.json":           "DATA_morphospace_mixing_feed_s167.json",
    "morphospace_mixing_tradition_tier.json": "DATA_morphospace_mixing_tradition_tier_feed_s167.json",
    "morphospace_prevalence.json":       "DATA_morphospace_prevalence_curve_feed_s167.json",
    # the findings MANIFEST — every feed it lists is copied DYNAMICALLY below (so Method/Library feeds auto-copy
    # when they append to the manifest; no generator edit needed). Deployed under canonical names so the page's
    # FEED_BASE + entry.feed resolves.
    "DATA_findings_index.json":          "DATA_findings_index.json",
}


def canonical(basename: str) -> str:
    """read the canonical from twelve-laws origin/main (committed; robust to gitignored on-disk coords)."""
    return subprocess.check_output(
        ["git", "-C", str(TWELVE), "show", f"origin/main:pm/40_architecture/{basename}"],
        text=True,
    )


def main() -> int:
    subprocess.run(["git", "-C", str(TWELVE), "fetch", "origin", "-q"], check=False)
    OUT.mkdir(parents=True, exist_ok=True)
    for out_name, canon in FEEDS.items():
        try:
            raw = canonical(canon)
            d = json.loads(raw)                      # validate it parses
        except Exception as e:
            print(f"  ✗ {out_name}: could not read {canon} from twelve-laws origin/main ({e})")
            return 1
        (OUT / out_name).write_text(raw)
        n = len(d.get("points", d.get("curve", d.get("per_family", []))))
        print(f"  ✓ {out_name}  <-  {canon}  ({n} rows · script {d.get('_producing_script')})")

    # DYNAMIC: copy every feed the findings manifest lists (each owner's feed, under its canonical name)
    try:
        manifest = json.loads((OUT / "DATA_findings_index.json").read_text())
        for entry in manifest.get("feeds", []):
            fname = entry.get("feed")
            if not fname or (OUT / fname).exists() and fname in FEEDS.values():
                continue  # already copied above
            try:
                raw = canonical(fname)
                json.loads(raw)
                (OUT / fname).write_text(raw)
                print(f"  ✓ {fname}  <-  (manifest: {entry.get('domain')} / {entry.get('owner')})")
            except Exception as e:
                print(f"  ⚠ manifest feed {fname} ({entry.get('owner')}) not on origin/main yet — skipped ({e})")
    except Exception as e:
        print(f"  ⚠ could not read the findings manifest to resolve owner feeds ({e})")

    print("re-derived. Now deploy the changed feeds (worktree off origin/main → PR).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# ── METHODOLOGY FOOTER ──
# HOW PRODUCED: Design SB S171 (2026-08-14). Atlas Reader flagged a coming Qur'an+Tanakh rebalance that re-runs the s167
#   feed scripts in place; since the suite figures render from deploy COPIES (not the twelve-laws canonicals), they don't
#   auto-update. This makes the re-derive one command (read canonical from origin/main → write deploy copy), §2.13-clean.
# SCHOLARLY SOURCES: the 3 s167 canonicals; §2.13 single-store (canonical in twelve-laws, deploy feed derived);
#   §2.16 render-from-data. Mirrors build_morphospace_feed.py (the scatter's generator).
# WHAT NEEDS VERIFICATION: (1) the canonical basenames stay stable across Atlas Reader's re-runs. (2) if a canonical becomes
#   gitignored (on-disk only, like the coords), switch canonical() to read the filesystem path instead of git show.
