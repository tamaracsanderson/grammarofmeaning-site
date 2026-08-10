---
title: "3DR-16 — how should we visualize the instrument's first three FINALIZED steps (Text · Decompose · Connect), for an academic and a reading audience, composing into a reading room?"
date: 2026-08-10
author: design-SB
round_type: 3DR (GPT-5 / Fable / Gemini Deep Research) — a RIGHT-SIDE-of-the-bow-tie visualization/design DR
status: READY-TO-FIRE (PI runs; design-SB reconciles). Same paste-format as 3DR-15 (situate) / 3DR-14 (edge grammar).
pairs_with: the 3 finalized feeds (checkout.json = TEXT · moves.json = DECOMPOSE · connect_node_drawer.json = CONNECT);
  the live WIP staging figures (viz_decompose.html · viz_connect.html · viz_house_pattern.html); the method-engine SSOT
  (grammarofmeaning.org/engine/method-engine.html)
note: "This is a RIGHT-SIDE DR — not about the coding METHOD (3DR-13/14/15 tested that) but about how to VISUALIZE its
  finalized OUTPUT. Scope is strictly the three FINALIZED engines: TEXT, DECOMPOSE, CONNECT. Un-finalized layers
  (Situate/Frame/Gloss) are deliberately OUT of scope. Two audiences (academic/pragmatic-theology + reading/meaning-making);
  the visuals compose into a 'reading room' (a modern Talmudic reading experience). Proof-of-concept on the Gospels (Mark 16);
  the visual grammar must GENERALIZE to other religious traditions and to philosophy + psychology."
---

# 3DR-16 — how should we visualize an instrument's first three steps (Text · Decompose · Connect)?

**Purpose.** We have a method that makes the STRUCTURE OF MEANING in a text visible, and three of its steps are finalized:
TEXT (the verbatim passage), DECOMPOSE (the passage broken into "moves"), and CONNECT (typed edges between the moves, plus
the edges that are absent). We are designing the RIGHT SIDE of the bow-tie — the visualizations of that output — and want to
do the design thinking BEFORE we build. We ask three cohorts: given this exact data, how would you visualize it as a SERIES
of visuals, for two very different audiences, composing into a "reading room"? Plus: what off-the-shelf tools, what canonical
references, and what design principles should we use? This is a fit-for-purpose / how-best-to-show-it round, not a defense of
any current figure (our current figures are deliberately WIP).

**Companion (not pasted — reference if useful):** the method-engine SSOT (grammarofmeaning.org/engine/method-engine.html);
the current WIP staging figures (grammarofmeaning.org/_staging/viz_decompose.html and /viz_connect.html) — shown only so a
cohort can react to a first attempt, NOT as a target to match.

═══════════════════════════════════════════════════════════════
PASTE-START — copy from this line to PASTE-END to each 3DR cohort (GPT-5 · Fable · Gemini Deep Research)
═══════════════════════════════════════════════════════════════

# Design a series of visualizations for the first three steps of a meaning-analysis instrument

We are building a method that makes the STRUCTURE OF MEANING in a text visible. Three steps are finalized, and we want to
visualize their output well. Help us design the visuals BEFORE we build them.

## What the instrument does (three finalized steps)
1. **TEXT** — a verbatim passage, exact words, with verse/line markers and textual-variant apparatus preserved.
2. **DECOMPOSE** — the passage broken into MOVES. A move = one agent doing one operation on a substrate, producing an
   outcome. Moves can nest inside other moves. Each move also carries a plain-language paraphrase.
3. **CONNECT** — typed EDGES between the moves (how they hold together), under five KINDs, PLUS the edges that are ABSENT
   (negative space is a first-class result, not missing data).

Proof-of-concept is the Gospels (Mark 16). It will extend to other religious traditions, and to philosophy and psychology —
so the visual grammar must GENERALIZE, not depend on Christian-specific iconography.

## The actual data (real, from Mark 16, World English Bible)

**Step 1 — TEXT (verbatim; apparatus preserved):**
"16:1 When the Sabbath was past, Mary Magdalene, and Mary the mother of James, and Salome, bought spices, that they might
come and anoint him. 16:2 Very early on the first day of the week, they came to the tomb when the sun had risen. 16:3 They
were saying among themselves, 'Who will roll away the stone from the door of the tomb for us?' … 16:6 'Don't be amazed. You
seek Jesus, the Nazarene, who has been crucified. He has risen. He is not here.' … 16:8 They went out, {TR adds 'quickly'}
and fled from the tomb, for trembling and astonishment had come on them."
(The {TR adds 'quickly'} is a textual-variant apparatus mark, kept verbatim — a place the manuscripts disagree.)

**Step 2 — DECOMPOSE (the moves).** Per-move fields: label · operation · agent · substrate · outcome · move_type · voice ·
narrator · nested_under · verse_refs · paraphrase. On Mark 16: 60 moves; 25 nested inside others; 16 carry an outside
citation. Samples:
- M1 (16:1) — operation: buy · agent: the three named women · substrate: spices · outcome: spices in hand, intending to
  anoint the body · top-level · paraphrase: "Once the rest-day had ended, the three named women purchased aromatic spices
  intending to go and dress the body."
- M3 (16:3) — operation: say · outcome: the question uttered aloud among them · with a NESTED move M4 (operation: ask —
  "who will roll the stone?") · paraphrase: "As they walked they were voicing a worry to one another."
- M-negate (16:6) — operation: negate ("he is not here") — a negation that redirects attention beyond the tomb.

**Step 3 — CONNECT (the edges).** Five KINDs: LINKAGE (in-text logic — how the moves in one passage hold together), LINEAGE
(cross-text reference — what a text cites/stands on), RESONANCE (cross-tradition correspondence — the same move in a
different voice), SHAPE (in-text form — parallelism/ring/juxtaposition), SONIC (in-text sound). On Mark 16: 78 edges across
14 types; almost all LINKAGE (70) + SHAPE (8), the two biggest being NEST_REPORTS (19) and LINK_SEQUENCE (19, the weak
default). The cross-text kinds are a frontier.
- A worked edge: M42 —NEST_REPORTS→ M43 ("he addresses commissioning speech to the eleven" reports "he orders them to travel
  out across the whole world").
- The ONE worked cross-text RESONANCE so far: Mark's "he is not here" (a negation that redirects) ⟷ the Daodejing's opening
  "a way that can be walked is not the abiding way." Same MOVE (negation-as-redirection); where it BREAKS: Mark's is a
  singular event, the Daodejing's a permanent condition.
- NEGATIVE SPACE: a move with no edge into it is unmotivated; a claim with no support-edge is ungrounded; a move with no
  cross-text partner is a rhyme that isn't there. These absences are the point.
- A governing rule: an edge is a PROPOSAL, not proof of dependence; "no edge" is a legitimate answer.

## Please answer

1. **The series.** How would you visualize this as a SERIES of distinct visuals (not one mega-chart)? Propose the set. For
   each visual: a name · what it shows · which step (text/decompose/connect) · the visual encoding (what each mark, colour,
   position means) · an off-the-shelf tool that could build it · one reference it draws on.

2. **Two audiences.** Design for (a) an ACADEMIC audience whose purpose is contextualizing / pragmatic theology — values
   rigor, auditability, the encoding made legible, honesty about what is and is not claimed; and (b) a READING audience whose
   purpose is meaning-making — values invitation, the contemplative read, moving through the text and its structure. Same
   visuals in two framings, or different visuals per audience? Which single visuals serve both well?

3. **The reading room.** These compose into a READING ROOM — a modern Talmudic reading experience: the verbatim text at the
   centre with layers of structure, commentary, and cross-text resonance around it, the reader navigating between them (the
   way a Talmud page holds Mishnah at the centre with Gemara, Rashi, Tosafot around it). How should the series be arranged so
   it composes into that whole rather than scattering into separate charts?

4. **Negative space.** A first-class result is what is ABSENT — the edges not there, the moves nothing motivates, the
   cross-text rhyme that fails. How do you visualize an absence so it reads as a finding, not as missing data or a blank?

5. **Generalization.** The same visual grammar must later carry other religious traditions AND philosophy + psychology. What
   in the design should stay CONSTANT across domains, and what should be allowed to vary, so it never becomes Gospel-specific?

6. **Off-the-shelf.** What existing tools, libraries, or frameworks would render these well, so we USE rather than build?
   Name specific ones and what each is best for (e.g. text-with-annotation, typed graphs, scrollytelling, side-by-side).

7. **Eternal references.** The canonical, timeless works and artifacts on visualizing text-structure, annotation, commentary,
   and scripture that we should study (e.g. the Talmud page, the critical apparatus, manuscript glossing, Bertin, Tufte, the
   Pudding). What are the few we cannot skip, and what does each teach?

8. **Visual design tips.** Concrete principles for making these super crisp, clear, and visually appealing — type, colour,
   density, negative space, motion, restraint. What are the highest-leverage rules for THIS kind of text-structure visual?

9. **Where it breaks.** Apply the series in your head to a very different unit — a short apophatic aphorism (Daodejing ch.1),
   or a dense legal/ritual passage. Where does a visual designed on a Gospel narrative silently mislead, and what would it
   need to hold up?

At the END please give: (a) your single strongest recommendation for the FIRST visual we should build; (b) the one canonical
reference we should study before anything else; and (c) one question you would ask us before we start.

═══════════════════════════════════════════════════════════════
PASTE-END — stop copying here
═══════════════════════════════════════════════════════════════

## How to fire this 3DR (researcher operational instructions; NOT part of the cohort paste)
- **Cohorts:** GPT-5 (ChatGPT) · Fable · Gemini Deep Research. Paste the block above into each.
- **Save responses to** `research/10_dr/reading_room_viz_responses/reading_room_viz_<cohort>_<DATE>.md` with provenance frontmatter.
- **Then design-SB reconciles** to `research/10_dr/reading_room_viz_reconciliation_<DATE>.md` → a proposed visual SERIES
  (buckets: UNANIMOUS / MAJORITY / SOLO), with the off-the-shelf tools, the reference reading list, and a build order — which
  each then passes the viz Fidelity + Cold-Read gate before it ships.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: design-SB 2026-08-10 — 3DR-16, a RIGHT-SIDE-of-the-bow-tie visualization DR: given the FINALIZED output of the
  first three engines (Text/Decompose/Connect), how to visualize it as a series for two audiences (academic/pragmatic-theology
  + reading/meaning-making), composing into a reading room (a modern Talmudic experience). Drafted paste-ready per the PI
  (Gemini-DR = draft-don't-run; §feedback_gemini_dr_means_draft_not_run). Format mirrors 3DR-15 (situate). Scope is strictly
  the three finalized engines — un-finalized layers (Situate/Frame/Gloss) held out per the PI ("if it's not there, don't use
  it"). Prompted by a run of design errors this session that a step-back-and-DR (rather than build-first) is meant to correct.
  §2.6 (3DR/IRR), §2.8 (bias-visibility / negative space as a finding), §2.14 (generalization / out-of-domain), §2.15 (go
  wide then consolidate — this is the go-wide step before converging on a design).
SCHOLARLY SOURCES: the 3 finalized feeds (checkout.json = TEXT verbatim; moves.json = DECOMPOSE; connect_node_drawer.json =
  CONNECT, the edge grammar validated by 3DR-14); the method-engine SSOT page; the design/viz references the cohorts are asked
  to supply (the Talmud page, the critical apparatus, Bertin, Tufte, the Pudding, manuscript glossing).
WHAT NEEDS VERIFICATION: (1) 🐥 Method SB (165) to mirror this file to research/10_dr/queries/reading_room_viz_3DR-16_2026-08-10.md
  (design-SB is read-only on twelve-laws; drafted here in the deploy repo). (2) PI fires on all three cohorts. (3) design-SB
  reconciles → a proposed visual series + build order, each gated (Fidelity + Cold Read) before it ships. -->
