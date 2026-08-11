---
title: "3DR-19 — Connect per-kind visualization (logic vs shape vs sonic, separately, for a reader)"
number: 3DR-19
date: 2026-08-11
author: design-SB
round: 3DR-19 (GPT-5 · Fable · Gemini Deep Research) — SOLVE the per-kind viz question
pairs-with: _staging/connect_v2_reconciliation_2026-08-10.md (item D); the 3 live Connect figures; the old VIZ_constellation_v3
registry-note: next number after 3DR-18 (Move Score redesign) / 3DR-17. Responses land at the twelve-laws root as 3DR19_*.txt (per the 3DR17/18 convention); design-SB reconciles.
status: DRAFT — PASTE-READY (PI runs the 3 cohorts; design-SB reconciles)
companion docs (NOT pasted — for a cohort to reference if asked): the 3 live figures + the old constellation (links inside)
---

═══════════════════════════════════════════════════════════════
PASTE-START — copy from this line to PASTE-END to a cohort (GPT-5 / Fable / Gemini Deep Research)
═══════════════════════════════════════════════════════════════

# Best ways to visualize LOGIC vs SHAPE vs SONIC edges, separately, for a reader

I'm building a close-reading instrument. A passage (Mark 16) is broken into **moves** (one move = one operation the text performs: an agent does an operation on a substrate, producing an outcome). A separate engine then types the **relations between moves** under a fixed grammar. This question is about visualizing three *in-text* relation KINDs — each has a different structure, and I want to show them **separately** (overlaying all of them is a hairball of ~78 lines), so a reader can actually **track what each kind of relation tells them**. Note this is a *different* reading than reading the passage move-by-move — it's reading the *structure*.

## The three kinds, and what each connects (move → move, within one passage)

1. **LOGIC** (in-text discourse logic) — *directed* relations between moves. Sub-types: `SEQUENCE` (and-then, the weak default), `CAUSE` (and so), `CONTRAST` (but), `CONDITION` (if-then), `CORRECTION` (no, rather), `SUPPORT` (evidence for), `ELABORATES`, `BACKGROUND`, `FEED` (A's outcome becomes B's input), `FILLS` (B answers a question A opened), `NEST_REPORTS` / `NEST_COMPOSES` / `NEST_CONTAINS` (one move inside another). Mostly runs *forward* along the reading order; forms a DAG (a move can have several parents). ~70 of the 78 edges in Mark 16 are this kind.
2. **SHAPE** (in-text form) — *non-directional* structural patterns across the passage. Sub-types: `PARALLELISM` (two moves in parallel form), `RING` (an A…A ring/chiasm), `JUXTAPOSITION` (set side-by-side, gap held open), `LEAP` (a non-logical jump). ~8 edges in Mark 16. These are *symmetries and returns*, not causal chains.
3. **SONIC** (word-level sound) — ties between **words** (not moves): `RHYME`, `ASSONANCE`, `ALLITERATION`, `CONSONANCE` (computed phonetically). This is a *field over the verbatim text*, at a finer grain than moves. (Not yet run on this passage in the current engine, but a prior version computed it — see below.)

(There are also two *cross-text* kinds — LINEAGE [what a text cites/stands on] and RESONANCE [correspondence across traditions] — but those are handled on a separate facing-page view and are **out of scope** for this question. Focus on the three in-text kinds above.)

## What exists now (the starting point — critique + improve, don't just endorse)

Three live figures currently render **all kinds overlaid** (colour = kind), which is the hairball problem I'm trying to fix:
- Arc Band — moves in reading order, arcs in the margin: https://grammarofmeaning.org/_staging/viz_connect_arcband.html
- Relation Loom — adjacency matrix (move × move): https://grammarofmeaning.org/_staging/viz_connect_loom.html
- Topology Lab — force-directed graph (order dropped): https://grammarofmeaning.org/_staging/viz_connect_topology.html

An older, off-the-shelf sonic visualization (rhyme/assonance/alliteration/consonance as dotted arcs *on the words*, via the Poemage approach + `pronouncing`+`panphon`): https://grammarofmeaning.org/engine/artifacts/VIZ_constellation_v3_unified_coffee_2026-07-27.html

## What I need from you (be concrete, and specific to these three kinds)

1. **LOGIC** — what is the *best* visual form to read directed discourse relations (cause/contrast/support/sequence/nesting) between moves, so a reader can trace *how the argument holds together* — and see direction, and not drown in the sequence edges (the weak default)? (Arc? flow/tree? matrix? something else?)
2. **SHAPE** — what best shows in-text *symmetries* (parallelism, ring/chiasm, juxtaposition, leap) — patterns and returns across a passage — for a reader? (These are not chains; what form makes a chiasm or a parallel *pop*?)
3. **SONIC** — what best shows the *sound field* at word grain (rhyme/assonance/alliteration/consonance) — on the verbatim text, not the moves? (What does the old constellation get right/wrong; how would you do it?)
4. **Separate vs unified** — three distinct views, or one instrument with a per-kind mode? What's the right default (I lean: one kind at a time)? How would a reader move between them?
5. For each: name the **one comprehension barrier** a first-time reader hits, and the fix.

Draw on information-visualization (arc diagrams, adjacency matrices, node-link, sequence/alignment, phonetic-tie viz) and close-reading/rhetoric where relevant.

At the END, give me: (a) your single best recommendation per kind (LOGIC / SHAPE / SONIC), and (b) one sentence on separate-vs-unified.

═══════════════════════════════════════════════════════════════
PASTE-END — stop copying here
═══════════════════════════════════════════════════════════════

## How to fire 3DR-19 (researcher operational instructions; NOT part of the cohort paste)

- **Cohorts:** GPT-5 (ChatGPT) · Fable · Gemini Deep Research. Paste the PASTE block to each.
- **Save responses at the twelve-laws root** as `3DR19_gpt.txt` · `3DR19_fable.txt` · `3DR19_DR.txt` (matching the 3DR17 / 3DR18 convention).
- **Then design-SB reconciles** to `_staging/connect_perkind_viz_3DR-19_reconciliation_2026-08-11.md` (Decision-39 buckets: UNANIMOUS / MAJORITY / SOLO) → the per-kind viz spec that finalizes connect_v2 item D.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: design-SB 2026-08-11 — paste-ready 3DR query (PI directive) on the best way to visualize the three in-text edge
  KINDs (LOGIC/SHAPE/SONIC) SEPARATELY for a reader, since overlaying all is a hairball and Connect is edge-tracking (a different
  reading than the move-by-move Move Score). Open-framed per §2.1 (ask the cohorts the best form; don't pre-anchor an answer);
  names the edges + what they connect; points to the 3 live figures + the old sonic constellation as the critique baseline.
  §2.6 (3DR → reconciliation is the deliverable), §2.16 (SSOT taxonomy from the Connect drawer).
SCHOLARLY SOURCES: the Connect edge grammar (edge_grammar_v1, the 5 KINDs + sub-types); the 3 live Connect figures; the old
  VIZ_constellation_v3 (Poemage + pronouncing + panphon). Cohorts flag they can't verify their own citations — spot-check.
WHAT NEEDS VERIFICATION: (1) PI runs the 3 cohorts + drops responses. (2) design-SB reconciles → the per-kind viz spec (feeds
  connect_v2 item D: per-kind separate views). (3) SONIC viz depends on the word-level sonic data (Method-SB tooling for GRC;
  the EN sonic exists off-the-shelf) — the viz form can still be specced now. -->
