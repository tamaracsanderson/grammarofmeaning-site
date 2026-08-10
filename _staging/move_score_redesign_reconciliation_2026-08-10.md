---
title: "3DR-18 reconciliation → the Move Score build spec (crit + GPT + Fable + Gemini-DR + S138 research)"
date: 2026-08-10
author: design-SB
round: 3DR-18 (Move Score redesign / SOLVE) — reconciled WITH the 8-persona design-crit AND the S138 reading-practices research
cohorts: GPT-5 · Fable · Gemini Deep Research
inputs: 3DR18_gpt.txt · 3DR18_fable.txt · 3DR18_DR.txt (twelve-laws root); field_ed/design_crit_move_score_mocks_2026-08-10.md; the S138 package (moodboard_web_mechanics · the_four_layers_index · practices_by_tradition · enactment_matrix); the 3 live mocks
status: RECONCILED — the build spec. One decision for the PI (below) gates the ending + what "Inspect/Workbench" stores.
---

# The Move Score — build spec (the converge)

## Headline: near-total convergence

Three DR cohorts (GPT / Fable / Gemini-DR) solved the crit independently and landed on the **same instrument**, and it matches the
8-persona crit's direction and the S138 reading-practices research. The one-sentence spec (GPT's, and all three assent):
**"Make the Move Score an annotated TEXT that can become a database — not a database that can masquerade as a reading."**

The figure is no longer "Flow / Table / Diagram." It is ONE figure — **the Move Score** — with two lenses: **Read** (default) and
**Inspect**. A = the reading spine (time); C = the syntax, folded in as *phrasing*; B = the audit surface, behind the toggle.
"The text supplies space" (GPT).

## UNANIMOUS build decisions (3/3 cohorts + crit) — LOCK

1. **Default = Read. The verbatim TEXT is the foreground; the move is an attached aid.** Invert Mock A's hierarchy. (Crit headline: built-for-the-builder; all 3 DR: text-first.)
2. **Toggle = Read | Inspect** — an ACTION toggle, never "Reader / Researcher" (don't make a user self-identify; a scholar may read contemplatively, a seeker may audit a claim). **Mode-switch preserves selection/location** (the same move stays selected across both) — this is what makes it one instrument, not three pages. (GPT + DR explicit; Fable "Reading | Workbench".)
3. **Decode the tags into keyed axes, not identical pills.** Three axes, plain-language FIRST, taxonomic value demoted: *Kind of move → Transaction (an exchange) · Agent's role → Acts (active) · Place in structure → Main move (top-level)*. Each axis its own channel (a word + a small glyph; voice encoded as the arrow's behavior). Gloss the jargon inline: `middle-passive → Undergoes / acted-upon`; `null-stative → a state, no acting agent`. Pills-as-siblings is exactly what caused the confusion. (All 3 + crit's #1.)
4. **The key = ONE worked move, not a glossary or modal.** A collapsible "How to read a move" before the first verse: move 1 (or 16:8) fully annotated with hairline leader lines + interrogative labels ("who acts? · what happens? · what's acted on? · what becomes true?"), then small-type definitions. Collapses to `ⓘ How to read a move` after first pass. This is *pre-training* (multimedia-learning). (All 3 + crit's #2.)
5. **Strip pipeline chrome from Read** (node IDs · filenames · DECOMPOSE / bow-tie / stage names · coder/owner notes · schema field names · export). **KEEP in Read: the textual-variant apparatus** — the 16:8 ending is *the* reading question in the NT, not a pipeline fact; siglum beside the word, plain-language gloss on tap. (All 3 emphatic + crit's #3/#5.)
6. **Compose A + C + B — draw nesting as PHRASING, never boxes-in-boxes.** C's agent→operation→outcome unit folds into the anatomy; nesting shows as indentation / a score bracket / an accordion (`↳ 3 sub-moves`), NOT literal nested boxes (they make the card "massively tall" and shatter the flow). B is the Inspect table. (All 3 warn against boxes; DR most explicit.)
7. **Cadence, not animation.** ~half-a-viewport per move (deliberately inefficient to scan — Inspect is for scanning); reveal in attention order (verse → operation → paraphrase → anatomy); the **verbatim phrase lights up (40%→100%) as its move takes focus**; no autoplay, no scroll-hijack, no progress bar / "17 of 23" / gamified completion (attention is the task, not finishing). (All 3.)
8. **Give the passage back — the recomposition beat.** After a verse's moves, show the verse again, clean, "Read the verse again ↺". Decompose must not only atomize; it must recompose. (GPT + Fable.)
9. **The held Situate layer = a declared horizon, not an empty box.** Dashed/hatched boundary, half-ink "pencilled-in" type, one sentence of promise, status "In development" (not "Coming soon"), NEVER an empty `sitz: —`, shown ONCE per passage. Model: a museum "on loan" label / a critical edition's *desunt cetera* / an architect's underdrawing (pentimento). (All 3.)
10. **The reference to copy: Sefaria's reader + Resource Panel** — center text stays put; selecting a segment opens its apparatus alongside without navigating away. Copy the *interaction grammar*, not the styling. UNANIMOUS across all three. (It already solves our exact tension: an authoritative base text + a dense relational apparatus available without the apparatus becoming the text.)
11. **Borrow the deep-reading traditions** (all 3): the **Talmud daf / chevruta** (verse always largest + center, commentary in the margin, never overlaying; the paraphrase phrased as "we read this as…", one voice at the table); **lectio divina** as a recursive reveal — but name it plainly **Read → Notice → Read again**, NOT Latin/Christian labels (cross-tradition); the **musical score** (nesting as a phrase-bracket/slur; and a **rest glyph** for silence).

## Distinctive additions worth adopting (SOLO but strong)

- **Fable — the silence at 16:8 rendered positively:** the final move's outcome slot is *empty* (a long dash / a rest glyph) — "the instrument's last gesture is the text's own withholding." The one notation that can render *said nothing* as a positive event.
- **GPT — encounter the passage intact FIRST:** show Mark 16:1–8 whole, no decomposition, before the first move — so the Move Score begins as an act of reading, not analysis.
- **Gemini-DR — a zoom/scale slider (close ↔ distant):** 100% = every move; 10% = a Tufte sparkline of the passage's arc (Anticipation → Discovery → Fear/Silence). Distant-reading (Moretti) as a peer of close reading; a "grasp the whole in a glance, then zoom in" affordance.

## The 16:8 ending decision — DECIDED (PI, 2026-08-10): (c) the trace, ZERO-TOKEN tier

At the silence of **16:8**, the reader may leave a **trace** — but not only at the end: the trace is a **reader-annotation
layer** over the whole reading (highlight a phrase or a move, add a comment, save it) in the **Readwise / Hypothesis / Kindle-
highlights / Genius** idiom — the reader builds their own marks on the text. **Zero-token** (storage + UI, no LLM). Crucial
alignment: annotations anchor to text SPANS via the **W3C Web Annotation model** — the SAME anchoring layer GPT + the DR
flagged for anchoring the coded moves — so a reader's highlight and a coded move attach to the text identically (Hypothesis.is
is the open-source implementation of that standard). The 16:8 silence is simply where the trace-invitation is most pointed
(the empty outcome-slot; "what does this ending leave you holding?"). The **AI "mirroring"** (an instrument that reflects /
responds to the reader's note — the psychoanalytic mirror) is a deliberate, budgeted **v2 opt-in** that slots into the SAME
annotation store later without rework. So: immersive reader-annotation now (free); the mirror when the budget says so.
(Options: (a) nothing/receptive, (b) return/reread, (c) trace — PI chose (c), Readwise-style annotation.)

**Scope note (verified 2026-08-10):** Mark 16 is TWO chunks and the checkout splits them at 16:8 — chunk 0 = 16:1–8 (23 moves,
the short ending), chunk 1 = 16:9–20 (32 moves, the disputed longer ending). moves.json + checkout.json carry both; v1 builds
chunk 1 (16:1–8) but the layout is both-chunks-ready, because the 16:8 boundary IS the drama: the reading reaches "for they
were afraid" → the apparatus marks "the earliest manuscripts end here" → chunk 2 is visibly the *added* ending. The empty
outcome-slot / rest-glyph at 16:8 (Fable) + the trace invitation land exactly on that fracture.

(GPT frames the sibling question — "encounter the text intact first?" — and Gemini-DR the deeper one — does the data model allow *competing* Move Scores for the same verse? Method SB already answered the last: the model is plural-capable; render the single canonical run for v1.)

## The build order (P1 → P3)

- **P1 (the highest-leverage change, unanimous):** flip the default to **Read** with the verbatim text as foreground + **move-1 as the annotated key** + the **never-a-tag-without-its-axis** rule. One decision that discharges audience, jargon, provenance, pacing, and tone at once. + keep the 16:8 apparatus + strip the pipeline chrome.
- **P2:** the Read|Inspect toggle with **preserved selection**; the sticky-verse + phrase-lights-up cadence; nesting as phrasing (accordion), not boxes; the recomposition beat; the held-layer-as-horizon; reconcile the nested-count (the generator bug the crit caught, 13 vs 12).
- **P3:** the Sefaria-style margin apparatus; the distant-reading zoom slider; the 16:8 empty-outcome / rest-glyph ending (per the PI's (a)/(b)/(c) choice).

## Consonance with the S138 reading-practices research

The lectio / contemplative framing is already ours: the S138 package (the reading **mechanics** catalogue, the **128 contemplative practices × 14 traditions**, the four-layer reading·ritual·interactivity·treatment index, the companion-Romans mocks) is the substrate. The converged Move Score is the **reading** layer's first figure; the recomposition beat + the "Notice" reveal are its **mechanics**; the practices layer is where a later "respond/enact" (option (c)) would draw.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: design-SB 2026-08-10 — reconciliation of 3DR-18 (Move Score redesign/SOLVE; GPT/Fable/Gemini-DR) MERGED with the
  8-persona design-crit (field_ed/design_crit_move_score_mocks_2026-08-10.md) AND the S138 reading-practices research, into one
  build spec for the converged Move Score. Near-total convergence; Decision-39 buckets (all core findings UNANIMOUS 3/3 + crit).
  One decision surfaced to the PI (the 16:8 ending: receptive / return / trace). §2.6 (3DR yields a reconciliation), §2.8 (the
  held layer as an honest declared absence), §2.15 (diverge→converge), §2.16 (the reader never sees the SSOT's internal vocab).
SCHOLARLY SOURCES: 3DR18_{gpt,fable,DR}.txt; the crit record; the S138 moodboards; the feeds (checkout.json + moves.json); the
  references the cohorts converged on (Sefaria's reader/Resource-Panel — the one to copy; the Talmud daf; lectio divina; the
  musical score; critical apparatus / ECM; Moretti distant reading; multimedia-learning segmenting/pre-training; Craik &
  Lockhart levels-of-processing). Cohorts flagged they could not verify their own citations — spot-check before the chapter.
WHAT NEEDS VERIFICATION: (1) PI answers the 16:8 ending decision (gates P3 + what Inspect stores). (2) 🐌 Method SB S168 to
  mirror the 3DR-18 artifact set (query + 3 responses + this reconciliation) to research/10_dr/. (3) build P1 through the gate
  (Fidelity + Cold Read) as the converged Move Score, replacing the 3 mocks. (4) reconcile the nested-count generator bug. -->
