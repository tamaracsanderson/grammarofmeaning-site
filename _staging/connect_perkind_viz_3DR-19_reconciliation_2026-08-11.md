# 3DR-19 reconciliation — Connect per-kind visualization (LOGIC vs SHAPE vs SONIC)

**Round:** 3DR-19 (GPT-5 · Fable · Gemini Deep Research) · **reconciled by:** design-SB · **2026-08-11**
**Query:** `_staging/connect_perkind_viz_3DR-19_query_2026-08-11.md` · **Responses:** `3DR19_{gpt,fable,DR}.txt` (twelve-laws root)
**Finalizes:** connect_v2 item D (per-kind separate views) — the roadmap `[3]` gate.

## Headline

**Unusually strong convergence — 3/3 on every load-bearing point.** The one-line verdict all three reached independently: *stop filtering a hairball by colour; give each kind the visual grammar native to its topology, on one never-moving text spine, one kind at a time.* This is a deeper reframe than "promote the drill-down filter to primary mode" (the roadmap's original framing of D): the cohorts agree the per-kind views need **different render idioms**, not just a default filter.

Fable's framing captures why: the three kinds differ in **topology** — LOGIC is a *directed sparse DAG over an ordered sequence*, SHAPE is a *small set of symmetries over that same sequence*, SONIC is a *dense equivalence-class field at a finer grain*. One edge-drawing idiom (coloured lines) for three topologies is the root error.

---

## UNANIMOUS (3/3)

1. **One instrument · mode-switching · ONE kind at a time by default.** design-SB's lean is confirmed by all three. Overlay serves the *analyst* checking co-occurrence, not the *reader* learning a structure (a reader asks one question at a time).
2. **A shared, never-moving text spine (object constancy).** The verbatim text/moves stay in the same screen position across modes; switching is a *change of lens, not of place*; selection + reading position survive the switch. (DR: "persistent verbatim anchor"; Fable: "the substrate never moves"; GPT: "shared spatial substrate.") This is the same principle as our P2 state-carry — extend it across the per-kind modes.
3. **Different visual GRAMMARS per kind, not different colours.** Switching modes must change the *representation*, not just toggle which edges are lit.
4. **LOGIC — STOP DRAWING SEQUENCE.** Reading order already encodes "and-then"; drawing sequence edges is the single largest noise source (~40+ of the ~70 LOGIC edges). Demote SEQUENCE to the layout itself. *(We already ghost `LINK_SEQUENCE` in P1 — this promotes that instinct to a hard rule and extends it.)* Reserve drawn edges for the high-value operators (CAUSE · CONTRAST · CORRECTION · CONDITION · SUPPORT · FEED · FILLS · ELABORATES · BACKGROUND).
5. **LOGIC — nesting is ENCLOSURE, not an edge.** `NEST_REPORTS/COMPOSES/CONTAINS` → indentation / bracketing on the spine (Gestalt enclosure). In Mark 16 the young man's announcement + the longer-ending commissions become visible *as structure* before any arc is read.
6. **LOGIC — a vertical move-spine + marginal directed arcs** for the remaining informative relations (keeps every move in reading order; routes edges in the margin so the text stays pristine).
7. **SHAPE — symmetry as GEOMETRY, not arcs.** Crossed arcs for a chiasm read as a tangle of wires, not a mirror. Rings → concentric/nested arcs with an **explicitly marked pivot** (or mirrored indentation); parallelism → alignment/ribbon; juxtaposition → a **held-open gap with NO connector** (the withheld connective *is* the content); leap → a **broken/discontinuous** mark.
8. **SHAPE — annotate at the PATTERN level, not per-edge** (one label per whole structure: "ring: A–B–pivot–B′–A′"), with hover highlighting the echoed members.
9. **SONIC — stay ON the words; it is a FIELD, not an edge-set.** Never displace the verbatim text (the constellation's fatal error was extracting words off-text + rendering a field as pairwise arcs — a 5-word chord becomes 10 arcs, exactly the richest moments least readable).
10. **SONIC — mark sound families IN the text** (tint/underline the sound-bearing grapheme span) + a **per-family density strip / heat-map** in the margin for the field reading; connecting threads only **on-demand (hover)**, never persistent.
11. **Separate-vs-unified — unified, one-at-a-time, shared spine.** (The explicit (b) answer from all three.)

## STRONG-MAJORITY / MAJORITY

- **Keep the matrix (Loom) as a RESEARCH/diagnostic view; retire the force-graph (Topology) for LOGIC.** (GPT + Fable explicit; DR concurs the matrix is analyst-only + force-layout destroys the linear order that makes discourse legible.) → maps cleanly onto our **Trace = reading / Scan = meso / Map = research** verbs: per-kind primary applies to the *reading* views; matrix/topology stay as research lenses behind them.
- **Relation labels in natural-language connective, not taxonomy jargon** ("but-rather," "and so" — not `NEST_REPORTS`). (GPT + Fable.) *We already ship this as P1's plain-language relation cards — extend it to arc-apex labels.*
- **Chiasm FOLD is an opt-in interaction, not the default layout.** DR would physically re-indent text blocks to form the shape by default; GPT + Fable warn that re-layout "disturbs the shared coordinate system" (breaks object constancy, itself unanimous) → **reconciled: keep the straight spine stable + draw the geometry; offer "fold this ring" as a per-structure interaction.** (Majority over DR's default-refold.)

## SOLO (worth adopting — additive, not contested)

- **Fable — directional margins:** forward relations arc in the **right** margin, retrospective relations (BACKGROUND, FILLS answering an earlier opening, backward SUPPORT) in the **left**. Direction becomes a glance; the left margin becomes "where the text answers itself" (in Mark 16: the absent body, the promised Galilee appearance). *Strong — adopt.*
- **Fable — FEED drawn slot-to-slot:** from A's *outcome* slot to B's *substrate* slot, so the viz literally shows the handoff the grammar claims (our move cards already carry agent/operation/substrate/outcome). *Adopt as enhancement.*
- **Fable — mode switcher as small-multiple thumbnails** (each button a miniature of that kind's actual structure in this passage) that doubles as an overview. *Strong — adopt for the nav.*
- **Fable — cross-kind pinning** at low opacity ("does the CONTRAST fall at the ring's pivot?"). *Adopt as an option, never default.*
- **GPT — "Trace this move"**: click a move → fade all but its logical ancestry + consequences (answers "why are we here?"). *We already have per-move selection + the P1 relation card + the new Move-Score→Connect tie — this is the same affordance; make fade-to-lineage the LOGIC-mode selection behaviour.*
- **Fable/DR — audio-on-hover** for a sonic family (play the family's words). *Nice-to-have; defer.*
- **Fable — legend shows the shared phoneme itself** ("-one / -own / -oll"). *Adopt when SONIC lands.*

## Citation-veracity note (§13)

Cohorts flagged they can't verify their own citations (GPT + Fable couldn't open the staging URLs; DR carries a long academic bibliography — Poemage/Meyer, Wattenberg arc diagrams, Ghoniem matrix-vs-node-link, RST/SDRT, SPARSAR). The design recommendations stand on their own reasoning; the *named studies* (esp. DR's numbered refs) are **spot-check-before-citing** if any reach the methodology chapter. The one I'd trust without checking: **Poemage (Meyer et al.) on keeping sound in "poem space"** — it's the direct precedent for our SONIC=on-the-words rule and is real.

---

## The finalized per-kind viz spec (feeds the D build)

**Architecture:** one Connect instrument, **shared vertical move-spine** (verbatim text in reading order, same position across modes), **one kind visible at a time** (LOGIC / SHAPE / SONIC), mode switcher = small-multiple thumbnails; selection + position survive the switch (extend P2 state-carry). Matrix (Scan) + force-graph (Map) demote to research lenses reachable from each reading view.

| Kind | Default render (reading view) | Do NOT | Selection behaviour |
|---|---|---|---|
| **LOGIC** | Vertical spine; SEQUENCE implicit in order (no line); NEST → indentation; remaining typed relations as **marginal directed arcs** — forward right, retrospective left; colour = relation *family* (additive/causal/adversative/evidential), adversative hottest; connective spelled in words at the arc apex; FEED slot→slot. | draw sequence; draw nesting as an arc; 12 colours for 12 types | click a move → fade to its lineage (ancestry+consequences) |
| **SHAPE** | Same spine; geometry per type — ring = concentric arcs + **marked pivot axis**; parallelism = alignment **ribbon** with member rungs; juxtaposition = **held-open seam, no connector**; leap = **broken** mark. Label per *structure*. | crossed arcs; per-edge labels | hover a structure → highlight echoed members; "fold this ring" opt-in |
| **SONIC** | Verbatim text locked; sound **families as sets** — tint/underline the sound-bearing grapheme span in each word; per-family **density strip** in margin; threads **on hover only**. Legend shows the shared phoneme. | off-text extraction; persistent pairwise arcs | hover family/word → isolate that family + transient slurs |

**Data readiness:** LOGIC + SHAPE render from the **existing** `connect_edges.json` (70 LINKAGE + 8 SHAPE on main) — **buildable now**. SONIC is **data-blocked** (0 SONIC edges in the feed; word-level sonic owed from Method SB — but the EN off-the-shelf run exists and the Greek sonic tooling exists per the roadmap §0). So the SONIC mode is *specced now, built when the word-level sonic feed lands.*

## Recommended build sequence (surface to PI)

This is a **redesign of 3 shipped figures**, not a filter toggle — so it's a deliverable-shape decision. My recommendation:

1. **Now (buildable, no new data):** rebuild the **LOGIC reading view** to the spec (drop-sequence + nest-as-indent + family-coloured margin arcs + directional margins) — it's the highest-yield (~70 edges, the actual hairball) and needs only the current feed. Ship it as the new Connect **Trace = LOGIC** default; keep Scan (matrix) + Map (topology) as the research lenses behind it.
2. **Now:** **SHAPE reading view** (only ~8 edges; geometry idiom) — small, high-clarity.
3. **When the word-level sonic feed lands:** **SONIC reading view** (typographic families + density strips).
4. Fold the small-multiple thumbnail nav + cross-kind pinning across all three.

**Alternative (if the PI wants to see it before a full redesign):** I build the LOGIC view alone as a **staging prototype** on Mark 16, the PI reacts to the drop-sequence + margin-arc idiom live, then I roll it to SHAPE/SONIC. I lean **prototype-LOGIC-first** — it's the biggest change to a shipped figure, so one reactable prototype de-risks the whole redesign.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: design-SB 2026-08-11 — reconciliation of 3DR-19 (GPT-5 · Fable · Gemini Deep Research) on visualizing the three
  in-text edge KINDs (LOGIC/SHAPE/SONIC) separately for a reader. Decision-39 buckets (UNANIMOUS / STRONG-MAJORITY / MAJORITY /
  SOLO) per §2.6; the reconciliation is the deliverable (§2.6 — chat-only summaries don't count). Finalizes connect_v2 item D.
SCHOLARLY SOURCES: the 3 response files (3DR19_{gpt,fable,DR}.txt); the Connect edge_grammar_v1 drawer (5 KINDs); the 3 live
  figures (arc band / loom / topology); VIZ_constellation_v3 (Poemage + pronouncing + panphon). §2.16 (SSOT taxonomy), §13
  (citation-veracity flag — cohorts can't verify own citations; DR's academic refs spot-check-before-citing).
WHAT NEEDS VERIFICATION: (1) PI direction on the build sequence (full redesign vs prototype-LOGIC-first — I lean prototype-first).
  (2) SONIC mode is data-blocked on the word-level sonic feed (Method SB). (3) DR's numbered citations spot-check before any
  reach the methodology chapter (Poemage/Meyer is the one safe to cite). -->
