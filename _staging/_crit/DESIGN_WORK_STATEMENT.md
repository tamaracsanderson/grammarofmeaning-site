---
title: "Design Work Statement — the figure suite + the build plan (post-crit-walk)"
date: 2026-08-14
author: Design SB
status: LIVING — the Design build plan; update as builds ship / blocks clear
owner: 🧀 Design SB
pairs_with: the design-engine dashboard (engine/design-engine.html — the live per-figure review pills) · _staging/_crit/*.md (the 13 crit logs)
---

# Design Work Statement — the figure suite + the build plan

## What this is
The durable build plan for the Grammar of Meaning figure suite, after the PI's full crit-walk (2026-08-14) of every figure (Connect · Lineage · Partiture · Morphospace · Plate · Facing Page · Ledger · Position · Reading Room). It pairs with:
- **The live tracker:** `engine/design-engine.html` — every figure has a **review pill** (PI notes / GPT crit / status), render-from-data from `design_engine.json`. This DWS is the *plan*; the dashboard is the *state*.
- **The 13 crit logs:** `_staging/_crit/*.md` — each figure's PI + GPT crit rounds + priorities.

## The synthesis (the architecture everything resolves into)
The crit-walk resolved into ONE unifying architecture — **the Reading Room** (`reading_room_synthesis_2026-08-14.md`): the **text is the sequence**, a digital critical edition. **CENTER = the Move Score** (permanent spine, verbatim verse). **LEFT margin = structural-change lenses** (Position braid · Logic · Shape · Sound). **RIGHT margin = contextual cards** (World=Sitz+Paradigm · Inherits=Lineage · Afterlives=Reception+Gloss · Open=Gap/Seam), anchored per move. **Every reviewed figure becomes a margin lens/card here.** "The text is the road; everything else is the landscape beside it." → Each new figure is built to *double* as a Reading-Room lens so it drops into the synthesis rather than being rebuilt.

## The shared V2 contract (recurred across all 13 crits)
1. **Show the real text, never just IDs.** 2. **Detail beside the field** (sticky inspector, not a scroll-away chart). 3. **Explain + interpret** (say what a connection MEANS, not just that/how-many). 4. **Encoding matches the phenomenon** (kind ≠ degree; near ≠ same doctrine; "prevalence-sensitive" not "artifact"; MCA-interpreted not MCA-discovered). 5. **Render-from-data** (§2.16) — no hardcoded status/counts. 6. **Honest about built vs blocked.**

## THE BUILD QUEUE (prioritized · status)
| # | build | status | notes |
|---|---|---|---|
| ✅ | **Logic V2** — the annotated reading (word-substitution: M4 [BUT] M6 + definitions + directional arrowheads + participation dots + reads-as honesty + 5-instrument nav) | **SHIPPED 2026-08-14** | PR #441. Doubles as the Reading-Room LOGIC left-lens. |
| ✅ | **Media picker** — multi-select words (OR/coverage) + populated default + catch-all + clear semantics | **SHIPPED 2026-08-14** | PR #442. Proxied sources gated on the Worker. |
| ✅ | **Position** as its own peer card on the bow-tie (text → decompose → [position·connect·situate] → enriched move) | **SHIPPED 2026-08-14** | PR #438/#439. Provisional placement — Atlas Reader owns the deeper decompose→trio flow rewire. |
| **1** | **Shape V2** — keep the brackets; MOVE/SOURCE toggle (Greek at `mark16_grc/`); ring as higher-order structure; evidence-basis; apophenia-honest | **NEXT — unblocked** | Roll the annotated-reading idiom to Shape. |
| 2 | **Connect IA cleanup** on Scan/Map/Loom (5-instrument nav, kill "all kinds" everywhere) | unblocked | Trace/Scan/Map get their own hero + beside-inspector. |
| 3 | **Scan V2** (teach-the-diagonal, Hubs/Clusters/Long-reaches, marginal degree, crosshair) · **Map V2** (beside-inspector, interpret-degree, decompose REPORTS) | unblocked | |
| 4 | **Archetype walkthrough render** — cards (definition → faces → examples) on the archetypes page + **findings.html** (the pullable version) | ⏳ Atlas Reader feed-shape (PR #3234 shipped the data; asked for field names + verse-level exemplars) | The PI's "somewhere easy I can pull it up". |
| 5 | **Legend → tradition tier** + restore quadrant colors on the archetypes viz | ⏳ Atlas Reader tradition→color key (Abrahamic now unpacked in the feed) | |
| 6 | **Neighbors** — morphospace kNN local constellation (radial=real distance, NOT force layout; 8-axis why-near fingerprint; Mark rail) | ⏳ Atlas Reader kNN feed | The thesis view: rhyme = nearest neighbor. |
| 7 | **Prevalence V2** — before/after morphospace thumbnails + composition strip + uncertainty band; reframe as a CHECK view | ⏳ Atlas Reader resample-band feed (readability pass already shipped) | |
| 8 | **Reading Room shell** — the synthesis frame (Move Score center + the two margins; lenses drop in) | after the lenses exist | The culmination. |

## The 4-scale Atlas IA (morphospace family)
**Landscape** (archetypes — broad regions) · **Neighbors** (who's next door to this text) · **Path** (M1→M55 trajectory through the space) · **Mixing** (aggregate interleave stat — kept as evidence) · **Check/Prevalence** (does the pattern survive imbalance?).

## Open items owned by Atlas Reader (all flagged, coordinated)
Neighbors kNN feed · the archetype walkthrough feed-shape (+ verse-level exemplars) · tradition-tier color key · MCA-derived-vs-constructed axes (the defensibility question) · tradition FAMILY→TRADITION→SUBTRADITION hierarchy · archetype names ("Prophet's Fire" → stance names, PI's call) · Facing Page + Ledger coding · the "candidate" term + value-count in the Position drawer · the bow-tie right-side reconceptualization + the decompose→trio flow rewire.

## Cross-references
- **Live tracker:** `engine/design-engine.html` (review pills) · **crit logs:** `_staging/_crit/*.md`
- **The synthesis:** `_staging/_crit/reading_room_synthesis_2026-08-14.md`
- **Labyrinth DWS:** `labyrinth_DWS_v2_2026-08-14.md` (the Garden's map-paradigm labyrinth — a separate Design workstream)

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: Design SB 2026-08-14. PI asked for the post-crit-walk build plan captured in the Design Work Statement (durable +
  findable, not lost in chat). Consolidates the 13-figure crit-walk into the Reading-Room synthesis + the shared V2 contract +
  the prioritized build queue (2 shipped, Shape V2 next, several ⏳ Atlas Reader feeds). Living doc — update as builds ship.
SCHOLARLY SOURCES: the 13 crit logs (_staging/_crit/*.md); reading_room_synthesis_2026-08-14.md; design_engine.json (the live
  review-pill tracker); the PI's crit-walk 2026-08-14; §2.16 render-from-data; §2.13 single-store (this DWS + the dashboard are
  the two stores of the plan/state, not scattered chat).
WHAT NEEDS VERIFICATION: (1) keep in sync with the design-engine dashboard pills as builds ship. (2) the ⏳ items unblock as
  Atlas Reader lands feeds — move them up when they do. (3) the Reading-Room shell (item 8) is the culmination once lenses exist. -->
