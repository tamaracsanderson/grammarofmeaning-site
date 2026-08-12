#!/usr/bin/env python3
"""build_design_engine.py — the design-engine catalog GENERATOR.

Stops the design-engine gallery (design_engine.json → design-engine.html) from going stale by
DERIVING the volatile fields from the actual figure files instead of hand-typing them:

  - built.file  (the link)          -> resolved to a figure that ACTUALLY EXISTS in the repo
  - built.live  (the "live" pill)   -> true iff every built file resolves 200-on-disk; broken flagged LOUD
  - reads_from.feeds                 -> parsed from each figure's own fetch()/BASE+"…" calls (what it really reads)
  - _title                           -> the figure's <title> (cross-check against the authored name)

The AUTHORED design intent (name / one_line / step / encoding / audience / reference / gate) stays hand-
authored in design_engine.json — the generator PRESERVES those and only refreshes the derived state. Re-run it
whenever a figure is added / moved / deleted; a dead link then shows as ⚠ broken automatically instead of lying.

Usage:  python3 _scripts/build_design_engine.py            # regenerate + report
        python3 _scripts/build_design_engine.py --check    # report only, non-zero exit if any link is broken
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]                      # the deploy repo root
CATALOG = ROOT / "engine" / "data" / "viz" / "design_engine.json"

FETCH_LIT = re.compile(r"""fetch\(\s*['"]([^'"]+)['"]""")        # fetch('…') / fetch("…")
BASE_DEF  = re.compile(r"""(?:var|const|let)\s+BASE\s*=\s*['"]([^'"]+)['"]""")
FETCH_BASE= re.compile(r"""fetch\(\s*BASE\s*\+\s*['"]([^'"]+)['"]""")
TITLE     = re.compile(r"<title>([^<]*)</title>", re.I)


def repo_path(url: str) -> Path:
    """map a site path (/_staging/x.html or /engine/data/y.json) to a repo file."""
    return ROOT / url.lstrip("/")


def figure_files(built) -> list[str]:
    """every figure-file path a node points at (single `file` OR the multi-view keys)."""
    if not isinstance(built, dict):
        return []
    out = []
    for k, v in built.items():
        if isinstance(v, str) and (v.startswith("/_staging/") or v.startswith("/engine/")) and v.endswith(".html"):
            out.append(v)
    return out


def derive_feeds(html: str) -> list[str]:
    """what data feeds this figure actually reads, from its own fetch() calls."""
    base = (BASE_DEF.search(html) or [None, ""])[1]
    feeds = set()
    for m in FETCH_LIT.findall(html):
        if m.endswith(".json"):
            feeds.add(m.lstrip("/").replace("engine/data/", ""))
    for m in FETCH_BASE.findall(html):
        feeds.add((base + m).lstrip("/").replace("engine/data/", ""))
    return sorted(feeds)


def main() -> int:
    check_only = "--check" in sys.argv
    d = json.loads(CATALOG.read_text())
    report, broken = [], []

    for n in d.get("nodes", []):
        files = figure_files(n.get("built"))
        if not files:
            # no built figure -> planned; leave authored status, clear any live flag
            if isinstance(n.get("built"), dict):
                n["built"]["live"] = False
            continue

        # resolve existence of every file; the primary (for the link) is the first
        exists = {f: repo_path(f).is_file() for f in files}
        primary = files[0]
        live = all(exists.values())
        missing = [f for f, ok in exists.items() if not ok]

        b = n["built"]
        b["file"] = primary                     # guarantee the render's link target resolves
        b["live"] = live
        if missing:
            b["missing"] = missing
            broken.append((n["id"], missing))
        else:
            b.pop("missing", None)

        # derive the feeds from the primary figure's own fetches (what it really reads)
        try:
            html = repo_path(primary).read_text()
            feeds = derive_feeds(html)
            if feeds:
                n.setdefault("reads_from", {})["feeds"] = feeds
            t = TITLE.search(html)
            if t:
                b["_title"] = t.group(1).strip()
        except FileNotFoundError:
            pass

        report.append(f"  {n['id']:<20} live={live!s:<5} feeds={n.get('reads_from',{}).get('feeds')}")

    # provenance stamp (derived, not authored)
    d["_generated_note"] = ("VOLATILE FIELDS (built.file / built.live / reads_from.feeds / built._title) are "
                            "DERIVED by _scripts/build_design_engine.py from the actual figure files — re-run it "
                            "to refresh; a dead link shows as built.live=false. Authored fields are preserved.")

    print("design-engine catalog — derived state:")
    print("\n".join(report))
    if broken:
        print("\n⚠ BROKEN LINKS (built.file points at a figure that does not exist):")
        for nid, miss in broken:
            print(f"  {nid}: {miss}")

    if check_only:
        return 1 if broken else 0

    CATALOG.write_text(json.dumps(d, ensure_ascii=False, indent=1))
    print(f"\n✓ wrote {CATALOG.relative_to(ROOT)} ({len(d['nodes'])} nodes; {len(broken)} broken)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# ── METHODOLOGY FOOTER ──
# HOW PRODUCED: design-SB S170 (2026-08-11), PI-directed ("don't hardcode info — pull from the underlying
#   data/architecture so it's up-to-date vs stale links/texts/completion pills"). Closes the S170 discoverability
#   incident (7 figures shipped to _staging but hand-registered → links/pills would drift). The design-engine
#   gallery is the last hand-maintained feed; this generator makes its VOLATILE fields render-from-reality.
# SCHOLARLY SOURCES: DWS_STATE.md §4 (render-from-data; the S170 "done=findable" convention); the same
#   fix-the-engine-not-the-output move as the Librarian's corpus-count-in-the-generator + Method SB's feed-contract.
# WHAT NEEDS VERIFICATION: (1) the feed-derivation regex covers fetch('…') / fetch(BASE+"…"); a figure using a
#   non-BASE var for its data path won't be auto-detected (falls back to the authored reads_from.feeds — safe).
#   (2) multi-view nodes (connect_intext) link to the first view; a per-view link list is a later refinement.
