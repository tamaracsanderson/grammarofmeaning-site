# QUEUE — library-schema.html SSOT: two-codings framing + WEMI restructure direction

**From:** 🍑 Librarian SB (S162), 2026-08-07 → design-SB (owns site + deploy; library-schema source isn't in main tree).
**Status:** QUEUED — non-blocking, "when you next touch the library SSOT." NOT a blocker. Currently mid-thread on the
method-engine bow-tie (awaiting PI eyeball) — pick this up after that settles or on the next library-SSOT touch.
**Target page:** `engine/library-schema.html` (the LIBRARY SSOT — Librarian owns its CONTENT; design-SB owns the render/deploy).
**Full detail (READ FIRST when picking up):** `research/10_dr/catalogue_coding_schema_reconciliation_2026-08-07.md` (twelve-laws; read via `git show origin/main:…`).

## Two things to reflect

### 1. THE TWO CODINGS (PI-locked framing) — make explicit on the library SSOT
- **CATALOGUE coding (Type-1)** = the "librarian-card": fields a librarian records per holding (type, significance,
  edition, language, citation/provenance, rights). This is the **LIBRARY engine's job** (part of CORPUS → SERVE).
- **METHOD coding (Type-2)** = the analytical atlas-frame (8 axes) + moves. **DOWNSTREAM in the method instrument** —
  *reference* it from the library SSOT, do NOT own it there (it lives on the method-schema SSOT).
- **NAMING (hard rule):** use **"catalogue coding"**, NOT "reference coding" — "reference" is already a
  `significance_tier` value and would collide.

### 2. CATALOGUE SCHEMA UNDER RESTRUCTURE (3DR-10, 2026-08-07) — document the DIRECTION only
- 3-frontier DR (GPT-5 + Gemini-DR + Fable), **UNANIMOUS**: the flat 6-field card conflates FRBR levels → restructure to
  **WEMI-lite BEFORE backfilling.**
- Direction to document: **row = one Manifestation**, with **`work_id` above** (clusters translations/editions; dedup key)
  and **passage locators below**.
- **Phase-1 slice:** work_id + significance-split (centrality + branch-relative canonicity) + genre/format split.
- **Phase-2 deferred:** agents/authority-IDs, CTS-URNs, TK-labels.

### 3. ADD under ① OUTPUT — "the coding-input package" / the library CHECKOUT (Librarian S162, PI-directed)
- New output item on library-schema.html under **① OUTPUT**:
  - **Title:** "the coding-input package — what we hold to gloss it" (a.k.a. the library CHECKOUT / the instrument's INPUT node)
  - **Link:** "Method & Instrument →" (to the method-schema SSOT — this is the seam to the method-engine INPUT node)
  - **Framing:** one of the LIBRARY's OUTPUTs *is* the anchored coding-input package the method instrument glosses. Library
    **RESOLVE** (work+edition) → **GATE** (in-corpus / chunked / rights) → **EXTRACT** a **verbatim · anchored · versioned**
    package (text + {source_id, passage_id, verse_ids} + provenance + content_hash) → method codes it offline → results
    ingest back joined on the anchors. Three words: **verbatim · anchored · versioned.**
- **Render-from-data (§2.16):** a working **v0 exemplar is on main** — `pm/40_architecture/DATA_checkout_mark16_web_v1.json`
  (Mark-16, from `scripts/analysis/build_checkout_package_s162.py`). Render the drawer from that package shape (mirror it
  into `engine/data/` via `git show origin/main:…`).
- **Status caveat:** mark the checkout "v0 exemplar; full RESOLVE-by-work_id + registry table = WEMI Phase-1" — don't imply
  the general engine is built.
- **CROSS-LANE NOTE:** this is ALSO the method-engine INPUT node's true left edge. The method-engine `Text`/INPUT node
  (currently badged "corpus seam = TBD") should flip to "← from the library checkout (verbatim · anchored · versioned)"
  and can render its golden-path Step-0 worked example FROM `DATA_checkout_mark16_web_v1.json`. Coordinate the flip with
  reading/method SB (it owns the method lane; it said it'd flag when to wire the seam).

### 4. Librarian S162 EXTENSION (full spec, checked against the live page) — render-from-data, honesty-badged
**(a) Two coding types — currently ABSENT; add prominently** (top of CORPUS or a framing band):
- **Catalogue coding (Type-1)** = the librarian-card — descriptive fields the library records per source (type · significance ·
  edition · language · rights · provenance). The LIBRARY's job (CORPUS→SERVE). **Frame the CORPUS data-contract fields AS
  "catalogue coding."**
- **Method coding (Type-2)** = the 8-axis atlas frames + moves. DOWNSTREAM in the method instrument — link "Method & Instrument →";
  the library SERVEs text to it, doesn't own it.
- "catalogue coding," NOT "reference coding" (collides with significance_tier value 'reference').

**(b) Complete the CORPUS catalogue field list** (missing; add each with fill-% + the controlled-not-enforced honesty style already on the page — **render fill-% from the live DB, not hardcoded**):
- `source_artifact_type` — "what kind of thing" (~40 CHECK values) — filled **6.5%**
- `significance_tier` — already shown ✓ (6 values) — filled **3%** non-default
- `edition_info` — edition/translation/printing — filled **0.1%** (essentially empty — honest flag)
- `language_code` — ISO language — filled **25%**
- `rights_status` — copyright/access — filled **54%**
- `citation_source` — citation/where-from (distinct from `extraction_provenance` = how-harvested) — filled **34%**
- **Banner on the catalogue block:** "⚠ catalogue schema UNDER RESTRUCTURE (3DR-10, 2026-08-07): moving to WEMI-lite —
  row=Manifestation, work_id above + significance-split (centrality + branch-relative canonicity) + genre/format split.
  Field names pending CLC + migration (Phase-1). Current flat fields shown honestly; do NOT read them as final."

**(c) LWS reference (PI-flagged discoverability; META/footer):** "This library engine is run by the **LWS — the Library
WorkStream** (charter: `pm/40_architecture/LWS_library_workstream_charter_s157`; plans: `pm/40_architecture/LWS_next_plan_*`).
Its sibling is the **IWS — the Instrument/Method WorkStream** (reading-SB), which runs the method side (schema.html)." The SSOT
is the engine spec; the LWS is the workstream that builds+runs it.

**(d) Reconfirm** the ① OUTPUT checkout item + "Method & Instrument →" link (§3 above; v0 exemplar `DATA_checkout_mark16_web_v1.json`).

**OPEN Q for the Librarian (before build):** the fill-% must render-from-data (§2.16) — is there a data file with the live
catalogue fill-% (like the method-engine's generated drawer files), or should design-SB query `project.db`? design-SB renders
from files, not the DB directly — need a fill-% JSON to render honestly.

## ⚠ CAUTIONS (from the Librarian) — honor these when implementing
1. **The new WEMI field-NAMES are IN FLUX** (pending a CLC + migration next session). Document the **DIRECTION + the
   two-coding-types framing**, but **do NOT hard-type the new WEMI field-names** — they will change.
2. **Render catalogue fields from the live schema/data where possible** (§2.16 / §2.13), not hardcoded.
3. This is the LIBRARY SSOT — keep it subordinate to / pointing at the deployed library-schema page; the method-coding
   reference points to the method-schema SSOT.

## When picking up
1. Read the reconciliation doc (path above) + the current `engine/library-schema.html`.
2. Add the two-codings framing (catalogue Type-1 owned here / method Type-2 referenced).
3. Add the WEMI restructure DIRECTION as a status/roadmap note — NOT hard-typed field names; mark it "under restructure,
   names pending CLC."
4. Render existing catalogue fields from live data where the page already does; flag the in-flight bits honestly.
5. Deploy + tell the Librarian.

<!-- HOW PRODUCED: design-SB S161 (2026-08-07), capturing the Librarian S162 cross-session request so it doesn't rot
(§2.9) while design-SB finishes the method-engine bow-tie. SOURCES: Librarian SB message; catalogue_coding_schema
_reconciliation_2026-08-07.md; CLAUDE.md §2.16 (SSOT pages) §2.13 (single store) §2.9 (discovered-inventory triage). -->
