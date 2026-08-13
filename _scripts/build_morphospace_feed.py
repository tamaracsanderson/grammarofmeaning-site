#!/usr/bin/env python3
"""build_morphospace_feed.py — derive the compact deploy feed for the morphospace scatter.

Reads the CANONICAL run (twelve-laws pm/40_architecture/DATA_mca_morphospace_living_latest.json,
produced by Atlas Reader / the MCA build) and writes a trimmed, web-sized feed the figure renders from
(engine/data/viz/morphospace_points.json). Re-run whenever the canonical run updates.

Single-store discipline (§2.13): the canonical lives in twelve-laws; this is a convenience dump beside the
figure, regenerable, never hand-edited. Bias-visibility (§2.8): the prevalence curve is embedded so the
caption can SHOW the 85%-Abrahamic skew rather than hide it — the raw silhouette is an artifact, the
balanced one is the honest read.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
from collections import Counter

CANON = Path("/Users/tamarasanderson/Documents/twelve-laws/pm/40_architecture/DATA_mca_morphospace_living_latest.json")
OUT   = Path(__file__).resolve().parents[1] / "engine" / "data" / "viz" / "morphospace_points.json"

# The prevalence curve — NOT a field in the canonical run; sourced from the finding doc
# pm/50_audits/FINDING_mca_repermute_postdim1_balanced_s167_2026-08-11.md (S167, the --cap class-balancing round).
# Shows the raw silhouette collapsing monotonically toward interleave as the Abrahamic majority is capped down.
PREVALENCE_CURVE = {
  "source_doc": "pm/50_audits/FINDING_mca_repermute_postdim1_balanced_s167_2026-08-11.md",
  "rows": [
    {"abrahamic_cap": "none (naive)", "n": 2890, "silhouette": 0.2411, "reading": "\"strong separation\" — prevalence artifact"},
    {"abrahamic_cap": "50",           "n": 332,  "silhouette": -0.0488, "reading": "interleave"},
    {"abrahamic_cap": "34 (balanced)","n": 258,  "silhouette": -0.0525, "reading": "interleave"}
  ],
  "read": ("The raw silhouette (+0.24) is ~90% the Bible-bloc effect on an 85%-Abrahamic set. Balancing the "
           "classes collapses it monotonically to ~0/slightly-negative: the traditions largely INTERLEAVE — "
           "there is no meaningful tradition SEPARATION. The skew is shown, not hidden (§2.8).")
}

AXES = ["epistemic-warrant", "ontological-commitment", "inferential-operation",
        "telos", "evaluative-stance", "hermeneutic-posture", "r_condition", "r_topology"]


def main() -> int:
    d = json.loads(CANON.read_text())
    pts_in = d.get("points", [])
    pts = []
    for p in pts_in:
        if not (isinstance(p.get("x"), (int, float)) and isinstance(p.get("y"), (int, float))):
            continue
        row = {
            "r": p.get("read_id"), "f": p.get("tradition_family") or "Unknown",
            "ti": p.get("tradition_id"), "t": p.get("text_title") or "",
            "x": round(p["x"], 4), "y": round(p["y"], 4),
        }
        if isinstance(p.get("z"), (int, float)):
            row["z"] = round(p["z"], 4)
        row["a"] = [p.get(ax) for ax in AXES]           # the 8 axis values, in AXES order, for hover
        pts.append(row)

    families = Counter(p["f"] for p in pts)
    total = len(pts)
    fam_pct = {f: round(100 * n / total, 1) for f, n in families.most_common()}

    feed = {
        "_source": str(CANON.name),
        "_generated_by": "_scripts/build_morphospace_feed.py",
        "_note": "compact deploy feed for viz_morphospace.html; regenerate when the canonical run updates (§2.13).",
        "axes_order": AXES,
        "n": total,
        "families": fam_pct,                             # tradition_family -> % of coded reads (shows the skew)
        "diagnostics": {
            "adjusted_inertia_pct": d.get("adjusted_inertia_pct", [])[:3],
            "silhouette_normalized": d.get("tradition_silhouette_normalized"),
            "mca_pcoa_distance_agreement": d.get("mca_pcoa_distance_agreement"),
            "dim_top_loadings": d.get("dim_top_loadings", []),
            "n_reads": total,
            "snapshot": (d.get("snapshot") or {}).get("run_label"),
            "single_label_baseline": True,
            "stage6_coded": 0
        },
        "prevalence_curve": PREVALENCE_CURVE,
        "points": pts
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(feed, ensure_ascii=False, separators=(",", ":")))
    kb = OUT.stat().st_size / 1024
    print(f"✓ wrote {OUT.relative_to(Path(__file__).resolve().parents[1])} — {total} points, {len(families)} families, {kb:.0f} KB")
    print(f"  families: " + " · ".join(f"{f} {p}%" for f, p in list(fam_pct.items())[:8]))
    print(f"  silhouette_normalized={feed['diagnostics']['silhouette_normalized']} · adj-inertia={feed['diagnostics']['adjusted_inertia_pct']} · mca/pcoa={feed['diagnostics']['mca_pcoa_distance_agreement']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# ── METHODOLOGY FOOTER ──
# HOW PRODUCED: Design SB S171 (2026-08-13), for the Saquib show. Atlas Reader confirmed build-the-scatter (a) with an
#   honesty-critical caption spec: cite the BALANCED silhouette (interleave=convergence), never the raw +0.24 (a
#   prevalence artifact of an 85%-Abrahamic corpus). This trims the 2.2MB canonical run to a web feed + embeds the
#   prevalence curve so the figure can show the skew.
# SCHOLARLY SOURCES: DATA_mca_morphospace_living_latest.json (the canonical MCA run); FINDING_mca_repermute_postdim1_
#   balanced_s167_2026-08-11.md (the prevalence curve); §2.8 bias-visibility; §2.13 single-store; §2.16 render-from-data.
# WHAT NEEDS VERIFICATION: (1) the prevalence-curve numbers are from the 08-11 finding run; the deployed canonical is the
#   08-13 saquib_prep run (silhouette_normalized -0.213) — both show the same interleave direction, cited together honestly.
#   (2) if Atlas Reader re-runs, re-run this generator. (3) axis English names for dim1/dim2 are intentionally NOT hardcoded
#   (the new run's loadings differ from the old prose page); the figure labels dims by % inertia + top loadings from data.
