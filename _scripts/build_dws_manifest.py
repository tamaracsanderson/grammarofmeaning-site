#!/usr/bin/env python3
"""
build_dws_manifest.py — the DWS (Design Work-State) render-manifest generator.

WHAT: scans every reading-room-preview/*.html + engine/*.html page for its fetch()
calls (the data it renders from), and emits engine/data/dws_manifest.json:
  page -> fetches[]   (AUTO-derived — render-from-data; cannot drift)
  data-file -> {fetched_by[], owner-SB, twelve-laws source, status}  (owner/source
               from the maintained MIRROR_MAP below — the human-knowledge layer)
Any fetched data file with no MIRROR_MAP entry is flagged under "unmapped" — a
drift-detector: if design-SB adds a new fetch without recording its owner, it shows.

WHY: design-SB renders every drawer/page from other SBs' DATA exports but had no
SSOT for the render layer. This manifest + DWS_STATE.md are that SSOT, so a fresh
design-SB can pick up the whole render layer without archaeology. Powers the
watchable design-state.html page (parallel to IWS schema.html / LWS library-schema.html).

Run:  python3 _scripts/build_dws_manifest.py   (from repo root)
Re-run whenever a page's fetch() set changes OR a new data file is mirrored.
"""
import os, re, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── MIRROR_MAP (maintained by design-SB) ─────────────────────────────────────
# deployed data path -> which SB owns the source + where it lives in twelve-laws.
# This is the ONE hand-kept lookup; everything else is auto-scanned.
MIRROR_MAP = {
  "/engine/data/library_engine_schema.json": ("Librarian", "twelve-laws:pm/40_architecture/DATA_library_engine_schema_s159_2026-08-03.json", "CORPUS held/registered (GAPMAP)"),
  "/engine/data/library_schema_stages.json": ("Librarian", "twelve-laws:pm/40_architecture/DATA_library_schema_stages_s159_2026-08-04.json", "the 6 library stages + closure_modes"),
  "/engine/data/library_principles.json":    ("Librarian", "twelve-laws:pm/40_architecture/DATA_library_principles_*.json", "principles.html — silence taxonomy + copyright ladder"),
  "/engine/data/library_insights.json":      ("Librarian", "twelve-laws:pm/40_architecture/DATA_library_insights_s160_2026-08-04.json", "Field-findings insight strip (LACUNA drawer)"),
  "/engine/data/voices_web.json":            ("Librarian", "twelve-laws:pm/40_architecture/DATA_voices_web_s160.json", "WEB text of the 4 resurrection chapters"),
  "/engine/data/resituate_gospels_export.json": ("reading-SB", "twelve-laws:pm/40_architecture/resituate_3room/RESITUATE_gospels_readable_2026-08-04.md (export)", "RESITUATE gospels sensitivity strip"),
  "/engine/data/resituation_drawer.json":    ("reading-SB", "twelve-laws:pm/40_architecture/DATA_resituation_drawer_s160.json", "Resituation drawer: both directions + CLC backlog"),
  "/engine/data/coded_move_state_MATT-28.json": ("reading-SB", "twelve-laws:pm/50_audits/DATA_coded_move_state_MATT-28_s160.json", "coded-move heatmap + moves-list"),
  "/engine/data/coded_move_state_MARK-16.json": ("reading-SB", "twelve-laws:pm/50_audits/DATA_coded_move_state_MARK-16_s160.json", "coded-move heatmap + moves-list"),
  "/engine/data/coded_move_state_LUKE-24.json": ("reading-SB", "twelve-laws:pm/50_audits/DATA_coded_move_state_LUKE-24_s160.json", "coded-move heatmap + moves-list"),
  "/engine/data/coded_move_state_JOHN-20.json": ("reading-SB", "twelve-laws:pm/50_audits/DATA_coded_move_state_JOHN-20_s160.json", "coded-move heatmap + moves-list"),
  "/engine/data/reception_endgap.json":      ("reading-SB", "twelve-laws:(reception export — verify path)", "reception.html end-gap graph"),
  "/engine/artifacts/coded_ledger.json":     ("reading-SB / Main", "twelve-laws:(coded_ledger export)", "schema.html Coded Object ledger"),
  "/engine/artifacts/reflexive_gloss.md":    ("reading-SB / Main", "twelve-laws:(reflexive gloss)", "schema.html reflexive gloss"),
  "/engine/artifacts/faq_comprehension.md":  ("reading-SB / Main", "twelve-laws:(faq)", "schema.html FAQ"),
  "/engine/artifacts/method_rebuttals_faq.md": ("reading-SB / Main", "twelve-laws:(rebuttals faq)", "schema.html objections/answers"),
  "/engine/artifacts/morphospace_findings_companion_s156_2026-07-31.md": ("Librarian", "twelve-laws:(morphospace findings)", "morphospace companion"),
  "/reading-room-preview/data/reception_endgap.json": ("reading-SB", "twelve-laws:(reception end-gap export — verify path)", "reception.html end-gap graph"),
  "/engine/data/abductive_forward_test.json": ("reading-SB", "twelve-laws:pm/40_architecture/resituate_3room/DATA_abductive_forward_test_s160.json", "abduction.html Panel B — forward-test bars"),
  "/engine/data/abductive_concordia_readable.md": ("reading-SB", "twelve-laws:pm/40_architecture/resituate_3room/RESITUATE_abductive_concordia_readable_s160.md", "abduction.html Panel A — the verbatim deliberation"),
  "/engine/data/library_gapmap.json": ("Librarian", "twelve-laws:pm/40_architecture/DATA_library_gapmap_librarywide_s161_2026-08-05.json", "OUTPUT ② gap-map drawer — 348 bibliographic silences"),
  "/engine/data/dws_manifest.json": ("design-SB", "(this file — self-generated)", "the DWS render-manifest itself"),
  "/engine/data/dws_status.json": ("design-SB", "(hand-maintained)", "the DWS open-threads + conventions"),
  "/engine/data/essay_workstream.json": ("Essay SB", "twelve-laws:field_ed/_essay_workstream/essay_workstream.json", "essay-schema.html (EWS) — METRICS + NODES; via export_essay_workstream.py"),
  "/engine/data/value_gloss.json": ("Content SB (store) / reading-SB (fills values)", "twelve-laws:pm/40_architecture/DATA_value_gloss_s161.json", "reading.html Phase-2 axis-name + value → reader-words map (retired the interim frame_axis_reader_words.json; §2.13 one store)"),
}

# DYNAMIC_MAP — fetches whose path is built at runtime (`base+key+'.json'`); the scanner
# catches only the literal PREFIX. Mapped here as families, not flagged as unmapped.
DYNAMIC_MAP = {
  "/engine/data/coded_move_state_": ("reading-SB", "twelve-laws:pm/50_audits/DATA_coded_move_state_<gospel>_s160.json", "moves.html — 4 files: MATT-28 / MARK-16 / LUKE-24 / JOHN-20 (dynamic by ?g)"),
  "/engine/artifacts/provenance/PROVENANCE_": ("reading-SB / Main", "twelve-laws:(per-source provenance export)", "schema.html + schema-review.html provenance panel — per-source coded objects (dynamic by key)"),
  "/engine/artifacts/background/": ("reading-SB / Main", "twelve-laws:(background md family)", "background.html — dynamic md loader (?p=)"),
}
def is_dynamic_prefix(p):
    return p.endswith("_") or p.endswith("/")

def normalize(fetch_path, page_rel):
    """Resolve a fetch() target to an absolute site path."""
    if fetch_path.startswith("http"):
        return fetch_path
    if fetch_path.startswith("/"):
        return fetch_path
    page_dir = "/" + os.path.dirname(page_rel)          # e.g. /engine
    return os.path.normpath(os.path.join(page_dir, fetch_path))

def scan():
    pages, data_index = [], {}
    for page_abs in sorted(glob.glob(os.path.join(ROOT, "reading-room-preview", "*.html")) +
                           glob.glob(os.path.join(ROOT, "engine", "*.html"))):
        rel = os.path.relpath(page_abs, ROOT)
        html = open(page_abs, encoding="utf-8").read()
        raw = re.findall(r"fetch\(\s*['\"]([^'\"]+)['\"]", html)
        # skip template-literal / dynamic fetches (contain ${ or +), keep static ones
        fetches = sorted(set(normalize(f, rel) for f in raw if "${" not in f and "+" not in f))
        pages.append({"page": rel, "fetches": fetches, "n_fetches": len(fetches)})
        for f in fetches:
            data_index.setdefault(f, []).append(rel)
    return pages, data_index

def build():
    pages, data_index = scan()
    data_sources, dynamic_families, unmapped = [], [], []
    for f in sorted(data_index):
        by = sorted(data_index[f])
        if is_dynamic_prefix(f):
            if f in DYNAMIC_MAP:
                owner, src, note = DYNAMIC_MAP[f]
                dynamic_families.append({"prefix": f, "fetched_by": by, "owner": owner, "source": src, "note": note})
            else:
                unmapped.append({"file": f, "fetched_by": by})
        elif f in MIRROR_MAP:
            owner, src, note = MIRROR_MAP[f]
            data_sources.append({"file": f, "fetched_by": by, "owner": owner, "source": src, "note": note, "status": "mapped"})
        else:
            unmapped.append({"file": f, "fetched_by": by})
    return {
        "generated_by": "_scripts/build_dws_manifest.py",
        "what": "DWS render-manifest: page->fetches auto-scanned; owner/source from the maintained MIRROR_MAP; unmapped fetches flagged as a drift-detector.",
        "ownership_model": {
            "reading-SB (IWS · method-schema.html)": "Resituate + method + coded-move data — exports the SSOT-accurate DATA",
            "Librarian (LWS · library-schema.html)": "Frame / atlas / morphospace + library data — exports the SSOT-accurate DATA",
            "Content SB (🐞 · language-sharpening)": "turns coded material into reader-facing prose — gloss / frame_delta / sharpened descriptions / the prose gap-finder; produces DATA fields, design-SB renders; managed by design-SB",
            "Essay SB (✍️ · essays)": "long-form essays only (handed its sharpening scope to Content SB)",
            "design-SB (DWS · this manifest)": "renders EVERY page from those exports; owns the deploy repo; read-only on twelve-laws; manages Content SB's render targets",
        },
        "pages": pages,
        "data_sources": data_sources,
        "dynamic_families": dynamic_families,
        "unmapped_fetches": unmapped,
        "counts": {"pages": len(pages), "mapped_sources": len(data_sources), "dynamic_families": len(dynamic_families), "unmapped": len(unmapped)},
    }

if __name__ == "__main__":
    manifest = build()
    out = os.path.join(ROOT, "engine", "data", "dws_manifest.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)
    c = manifest["counts"]
    print("wrote", os.path.relpath(out, ROOT))
    print("  pages: %d · mapped sources: %d · unmapped: %d" % (c["pages"], c["mapped_sources"], c["unmapped"]))
    if manifest["unmapped_fetches"]:
        print("  UNMAPPED (add to MIRROR_MAP):")
        for u in manifest["unmapped_fetches"]:
            print("    -", u["file"], "<-", ", ".join(u["fetched_by"]))
