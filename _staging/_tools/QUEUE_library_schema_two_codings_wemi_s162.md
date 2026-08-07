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
