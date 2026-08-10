---
title: "3DR-18 — solve the design crit: how would you redesign the three Move Score mocks for the reader?"
date: 2026-08-10
author: design-SB
round_type: 3DR (GPT-5 / Fable / Gemini Deep Research) — a PROBLEM-SOLVING / redesign DR (not a validation round)
status: READY-TO-FIRE (PI runs; design-SB reconciles). Follows the 8-persona design-crit; asks the cohorts to SOLVE what the crit found, with concrete examples.
pairs_with: the 3 live mocks (viz_move_mockA_flow.html · viz_move_mockB_table.html · viz_move_mockC_diagram.html); the crit record field_ed/design_crit_move_score_mocks_2026-08-10.md; 3DR-16 (reading-room viz) reconciliation
note: "This is the SOLVE half. An 8-persona design-crit critiqued three ways of showing the Decompose 'moves'; this DR hands the cohorts the mocks + the critique and asks them to REDESIGN — with concrete examples (copy, layouts, references), not just principles. The finalized-only scope holds (Situate/Gloss are a 'coming' holding slot). Cross-tradition idea is 'rhyme' only."
---

# 3DR-18 — solve the design crit: redesign the "Move Score" for the reader

**Purpose.** We built three directions for one figure (the "Move Score" — a Bible passage broken into MOVES), then ran an
8-persona design-crit on the live trio. The crit's headline: all three are *built for the insider builder, not the reader.*
This DR asks three cohorts to SOLVE that — to redesign the figure so it serves a seeker AND a scholar — and, crucially, to
give CONCRETE EXAMPLES (real copy, real layouts, real references), not just design principles.

**Companion (not pasted — reference if useful):** the three live mocks (URLs in the paste block); the full crit record at
field_ed/design_crit_move_score_mocks_2026-08-10.md.

═══════════════════════════════════════════════════════════════
PASTE-START — copy from this line to PASTE-END into each 3DR cohort (GPT-5 · Fable · Gemini Deep Research)
═══════════════════════════════════════════════════════════════

# Redesign a "Move Score" figure to fix a design critique — with concrete examples

We are building an instrument that makes the structure of meaning in a text visible. One step, DECOMPOSE, breaks a passage
into MOVES — each move is one operation the text makes (an agent doing an operation on a substrate, with an outcome; moves
can nest inside other moves). We built three ways to show this for Mark 16:1–8, then ran an 8-persona design critique. We
want you to SOLVE what the critique found, with concrete examples.

## The three live mocks (open and use each — click a move, scroll, and append ?mode=reading to strip the "research" chrome)
- Mock A "The Reading Flow": a scroll-through — each move a big readable line with the verbatim verse beneath, a sticky
  anatomy card that follows, with a small agent→operation→outcome mini-diagram. https://grammarofmeaning.org/_staging/viz_move_mockA_flow.html
- Mock B "The Move Table": all 23 moves at a glance in one dense table; scan a whole column top to bottom. https://grammarofmeaning.org/_staging/viz_move_mockB_table.html
- Mock C "The Move Diagram": each move a small agent→operation→outcome visual unit, nesting drawn as containment, the
  passage as a vertical spine. https://grammarofmeaning.org/_staging/viz_move_mockC_diagram.html

Two audiences from ONE figure, via a mode toggle: a READER (a seeker; wants a slow, attentive, "lectio divina" reading of
what the text is doing) and a RESEARCHER (wants the coding made auditable). This is a CONTEMPLATIVE reading instrument —
it should be consonant with slow, close-reading traditions (lectio divina, Talmudic chevruta, literary close reading), not
a dashboard. Note: some fields are still being finalized (the "Situate" layers — a text's context), so they appear only as
a designated "coming from Situate" holding slot; do not design around them yet.

## What the 8-persona critique found (the problem you're solving)
- **Headline:** all three are built for the insider BUILDER, not either audience. The DEFAULT view greets the least-informed
  viewer with the most internal chrome, and the move's tags ship UN-KEYED.
- **Unanimous (8/8) fixes:** (1) decode the cryptic tag triad `transaction / active / top-level` — they are three different
  axes (kind-of-move · voice · nesting) but read as undifferentiated jargon; (2) add a "lay of the land" key that defines
  each part of a move; (3) strip pipeline chrome (internal words like "the bow-tie", "node 2", "DECOMPOSE", data filenames);
  (4) gloss grammar jargon like `null-stative` / `middle-passive`; (5) the empty "coming from Situate" placeholder reads as
  broken rather than as an honest not-yet.
- **Direction the crit recommends (react to it):** develop Mock A (Flow) as the reader spine; fold Mock C's legend +
  agent→operation→outcome unit into A's anatomy card; keep Mock B behind the research toggle as the auditor's export.

## Please solve — WITH CONCRETE EXAMPLES for each (real words, a sketch/ASCII layout, or a named reference — not just principles)

1. **Decode the tags.** How would you present a move's `type · voice · nesting` so a zero-context reader instantly gets it?
   Give the exact labels/words and the layout. (Example move: operation "buy", type "transaction", voice "active",
   top-level.)

2. **The "lay of the land" key.** Design the annotated example that onboards a reader — take one move and label every part
   (agent · operation · substrate · outcome · narrator · paraphrase + the tags) with a plain definition. Show it.

3. **Reader vs researcher default.** What should the DEFAULT view show, and how does the toggle to the auditable view read
   (what does the reader see vs the researcher)? What do you strip for the reader, and what MUST survive into the reading
   view (e.g. the textual-variant apparatus)? Name the toggle.

4. **Compose the three into one.** Do you agree with the crit's A-spine + fold-in-C + B-behind-toggle? Or propose a better
   synthesis. Sketch the composed figure (the reading view AND the research view) — where the text, the moves, the anatomy,
   and the nesting each live.

5. **Invite the practice.** The goal is an attentive, slow reading — the reader should LINGER on each operation, not skim.
   What concrete design moves make the figure invite that (pacing, reveal, focus, motion, whitespace)? Not "add animation" —
   specific, with an example.

6. **The honest "coming" layer.** How do you show a not-yet-finalized layer ("Situate: sitz · paradigm · frame — coming")
   so it reads as an honest, anticipated absence rather than a bug or an empty box? Give the visual treatment.

7. **Borrow from how OTHER disciplines slow a reader down.** Close reading is not new: literary close reading / New
   Criticism, lectio divina, Talmudic chevruta, the annotated legal opinion, the musical score, psychoanalytic listening,
   and computational / distant-vs-close "data" reading all have techniques for making a reader ATTEND and making structure
   visible. Draw on these AND on research on attention / meaning-making (how do people actually make meaning from a text —
   what focuses attention, what invites re-reading, what makes an insight land?). For 2–3 of these disciplines: name the
   TECHNIQUE, say what it does to the reader, and map it concretely onto a move-by-move reading of a passage, with an example.

At the END please give: (a) your single highest-leverage change; (b) the one reference (a page, tool, or artifact) we should
copy the solution from; and (c) one question you would ask us before we build.

═══════════════════════════════════════════════════════════════
PASTE-END — stop copying here
═══════════════════════════════════════════════════════════════

## How to fire this 3DR (researcher operational instructions; NOT part of the cohort paste)
- **Cohorts:** GPT-5 (ChatGPT) · Fable · Gemini Deep Research. Paste the block above into each. (They can open the three live
  URLs; if a cohort cannot browse, it can still solve from the description + the crit findings.)
- **Save responses to** `research/10_dr/move_score_redesign_responses/move_score_redesign_<cohort>_<DATE>.md` with provenance frontmatter.
- **Then design-SB reconciles** to `research/10_dr/move_score_redesign_reconciliation_<DATE>.md` (Decision-39 buckets), merged
  with the 8-persona crit AND our EXISTING reading-practices research into ONE build spec for the converged figure (the P1
  fixes: decode tags + key + strip chrome + gloss jargon + fix the held apparatus).
- **Existing internal research to fold in (do NOT reinvent — orient first):** the S138 reading-practices package —
  `_staging/_moodboards/moodboard_web_mechanics_S138_2026-07-05.html` (the ~28 reading mechanics + treatments),
  `the_four_layers_index_2026-07-05.html` (reading · ritual · interactivity · treatment),
  `practices_by_tradition_2026-07-05.html` (128 contemplative practices × 14 traditions),
  `enactment_matrix_2026-07-05.html`; the companion-Romans mocks (`_staging/_mocks/companion_romans_*_2026-07-08.html`);
  and reading-SB's prior reading-practice DRs. The 3DR + the crit + THIS existing synthesis merge into the one build spec.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: design-SB 2026-08-10 — 3DR-18, the SOLVE/redesign DR that follows the 8-persona design-crit on the three Move
  Score mocks (A flow / B table / C diagram). Hands the cohorts the live mocks + the crit's findings and asks them to
  redesign WITH concrete examples (copy/layout/references), not principles. Drafted paste-ready per the PI (Gemini-DR =
  draft-don't-run; §feedback_gemini_dr_means_draft_not_run). Format mirrors 3DR-16/3DR-15. Finalized-only scope holds
  (Situate/Gloss = a 'coming' holding slot). §2.6 (3DR/IRR), §2.8 (honest absence / the held layer), §2.15 (diverge then
  converge — crit found the problems, this solves them), §2.16 (the reader must not see the SSOT's internal vocabulary).
SCHOLARLY SOURCES: the 3 live mocks + the crit record (field_ed/design_crit_move_score_mocks_2026-08-10.md); the feeds behind
  the mocks (checkout.json + moves.json); the references the cohorts are asked to supply (the Talmud page, the critical
  apparatus, the Pudding, annotation tools).
WHAT NEEDS VERIFICATION: (1) 🐌 Method SB (168) to mirror this file to research/10_dr/queries/move_score_redesign_3DR-18_2026-08-10.md
  (design-SB is read-only on twelve-laws; drafted here in the deploy repo). (2) PI fires on all three cohorts. (3) design-SB
  reconciles the 3 responses + the crit into ONE build spec for the converged figure, then builds through the gate. -->
