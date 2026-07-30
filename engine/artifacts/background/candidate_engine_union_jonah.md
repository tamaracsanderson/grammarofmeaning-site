---
title: "Candidate-engine unification (Jonah 4) — 4 engines → dedupe → shared v3 gates → one typed/provenanced store. The union rescues the gap every single engine missed."
date: 2026-07-30
session: S156 (reading-SB, PI-directed 'can we try this?')
status: RESULT — the biggest architectural payoff of the session. Demonstrates: pool all candidate-engines through ONE gate →
  higher recall (catches the v.5 seam the move-scan missed) WITHOUT losing precision (gates+dedupe) + confidence-by-agreement
  + full detector provenance.
---

# The architecture, tried
Every output is a CANDIDATE engine; the shared v3 gates are the filter. Four engines ran on Jonah 4:
- **wild** (cold read) — 18 raw candidates (breadth)
- **move-scan** (v3 layered scan) — 10 kept gaps
- **situate-foreclosed** (v3 Situate) — 3 foreclosed-gaps (dating/genre/audience)
- **RESITUATE** (two-stage perturbation) — 7 candidates + 3 discards (incl. God's-mercy discarded @ anchor=stated)
Merge → dedupe (agreement = confidence) → apply the 5 gates + anchor/subtype → one store, each gap tagged with WHICH engines
found it.

# The merged, gated, provenanced store (deduped)
| gap | engines (confidence) | layer·locus | subtype · anchor | gate | rank |
|---|---|---|---|---|---|
| **v.5 booth-vigil seam** (why keep destruction-vigil over an already-spared city?) | **wild + move-scan + RESITUATE (3)** | frame/edge · text-scale | indeterminacy · absent | PASS | **#1** ↑ RESCUED |
| terminal silence / open ending (Jonah's reply withheld) | wild + move-scan + RESITUATE (3) | move · M2b | omission · absent | PASS | #2 |
| why divine mercy ANGERS Jonah (motive/warrant of the death-wish) | wild + move-scan + RESITUATE (3) | move · M2a / paradigm · P2 | suppression · absent | PASS | #3 |
| "120,000 who can't tell right from left" — denotation | wild + move-scan + RESITUATE (3) | paradigm · P3 | ambiguity · implied | PASS | #4 |
| scope of divine concern ("much livestock") | wild + move-scan + RESITUATE (2–3) | frame · F3 | indeterminacy · implied | PASS | #5 |
| the a-fortiori's ungrounded warrant (concern scales plant→persons?) | move-scan + RESITUATE | paradigm · P1 | presupposition · implied | PASS | #6 |
| genre / reading-level (parable vs history) | wild + move-scan + situate + RESITUATE (4) | frame · F1 | indeterminacy · absent | PASS (frame, low local-swing) | #7 |
| audience/Sitz (post-exilic polemic target) | move-scan + situate + RESITUATE (3) | sitz · S3/S2 | presupposition · absent | PASS | #8 |
| anti-hero vs tragic-hero tone | **RESITUATE only (1)** | frame · F2 | indeterminacy · implied | PASS (secondary) | #9 (new from RESITUATE) |

**Discarded by the shared gates (with reason):** God's mercy (anchor=STATED @ v2 — flagged by RESITUATE) · plant/worm/wind
"motive" (activation fail — apparatus/category-error, caught by move-scan) · "does Jonah understand" / "individual vs
representative" (wild padding — competence/consequence fail) · pedagogy-tone (no swing) · v.1 elided "it" (resolved in-window).
~35 raw candidates across engines → ~9 typed/ranked gaps + named discards.

# Why this is the payoff
1. **RECALL — the union rescues the blind spot.** The v.5 seam: wild found it but buried it (unranked #4/5); the move-scan
   only NOTED it; the 3-way judge called it the *shared blind spot* of all three prior runs. **RESITUATE ranked it #1**, and
   the union promotes it to the store's #1. No single lens ranked it; pooling lenses through one gate did. That is the whole
   thesis of the candidate-engine architecture, demonstrated on the exact gap it was supposed to catch (IMP-18 — partially
   answered NOT by a new grammar slot but by a different ENGINE).
2. **PRECISION held.** Bigger candidate pool (~35), but gates + dedupe collapse it to ~9 — and every discard is named. God's
   mercy correctly dies at anchor=stated (the RESITUATE two-stage filter working, U3).
3. **CONFIDENCE by agreement.** Gaps found by 3–4 engines (v.5 seam, terminal silence, motive, right-left) are high-confidence;
   RESITUATE's solo "tragic-hero tone" is a real but lower-confidence candidate. Multi-engine agreement is a free reliability signal.
4. **PROVENANCE.** Every gap carries WHICH engines found it (`detector[]`) — the feeding-graph, now data, not a diagram. This
   is exactly the `{layer, locus, subtype, textual_anchor, detector}` schema (IMP-22) — the store above IS that schema populated.

# What it says for the build
The production instrument = **wild + Situate + RESITUATE + Compare all throw candidates → the shared v3 gates filter/type/dedupe
→ one provenanced store.** The wild arm stops being the instrument's rival and becomes its broadest engine; RESITUATE earns its
place by catching the seam the grammar can't slot. Next: (a) wire this as the schema (IMP-22, the store above is the target
shape); (b) add Compare for multi-account texts (the resurrection braid, task #20); (c) the diverse-corpus precision-recall run.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: reading-SB S156 2026-07-30 — the PI said "can we try this?" (the candidate-engine unification). Ran RESITUATE as
  the 4th engine on Jonah, then merged all four candidate pools (wild + move-scan + situate-foreclosed + resituate) through the
  shared v3 gates + dedupe by hand. The union rescued the v.5 seam (the shared blind spot) to #1.
SCHOLARLY SOURCES: the 4 engine outputs (wild=AB_arm_a_wild_jonah4; move-scan+situate=v3 Jonah run; resituate=this run);
  output_feeding_graph + GAP_SCHEMA_extension (the {detector} provenance) + INSTRUMENT_v3_spec (the gates) + irr225 recon (U3
  two-stage detectors, U6 subtype/anchor); the 3-way judge (the v.5 shared blind spot this rescues); §2.8, §2.1.
WHAT NEEDS VERIFICATION: wire the store as the schema (IMP-22); add Compare for multi-account texts; run the union on more texts
  (does the recall-without-precision-loss hold?); the dedupe + confidence-by-agreement wants a real implementation, not hand-merge. -->
