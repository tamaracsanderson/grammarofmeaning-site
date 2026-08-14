# Connect · Logic view — crit log (the PI-preferred reading view)

**Figure:** `_staging/viz_connect_logic.html` · live: https://grammarofmeaning.org/_staging/viz_connect_logic.html
**Built:** design-SB S170 to the 3DR-19 per-kind LOGIC spec. **PI reaction 2026-08-14: "I do like this, and it feels like what the arc band was trying to do."**

## Why it clicks (the editorial stance)
It's OPINIONATED where the arc band was generic: sequence (19 edges) isn't drawn (reading order already says *and-then*); nesting (26 edges) is shown as **indentation**, not an arc; what's left in the margins are the **~21 relations that carry the argument** — **forward on the right, answering-back on the left**. Colour = relation FAMILY; the connective is spelled in WORDS at the arc apex (and-so / but / because / answers), never the taxonomy label. → This is the strong candidate for the **primary Trace / reading view**, absorbing the arc-band V2's interaction wins.

## The family ↔ word map (render-from-data; §2.16-clean)
4 families (toggles), each holding sub-types spelled as words:
- **causal · and-so** ← LINK_CAUSE "and so" · FEED "feeds into" · LINK_CONDITION "if—then"
- **adversative · but** ← LINK_CONTRAST "but" · LINK_CORRECTION "no, rather"
- **evidential · because** ← LINK_SUPPORT "because" · **FILLS "answers"**  ← the M4↔M7 case the PI caught
- **additive · expanding** ← LINK_ELABORATES "expanding" · LINK_BACKGROUND "against" · LINK_OTHER "relates to"

## PI notes (2026-08-14)
- [ ] **1. Directional arrows** — show which way a relation runs (does M4 answer M7, or M7 answer M4). Same for BUT. (Edges carry source→target; add arrowheads. The view already spatializes forward-right/back-left; make it explicit.)
- [ ] **2. ⭐ Word-substitution reading** — let the reader substitute the connective INTO the moves to read them as one sentence: *"They ask who will move the sealing-stone aside for them. **BUT** Raising their eyes, they perceived the stone had already been shifted aside."* Makes the relation legible as language. High-value + on-telos (reading instrument).
- [ ] **3. A dot/mark on moves that participate in a relation** — some moves have no arrow; mark which do. ALSO clarify: **M8→M9 nesting IS a relation** (REPORTS/COMPOSES) — shown as indentation, not an arc, by design. It's not "no relation"; give it a cue so it doesn't read as unrelated.
- [ ] **4. Legibility — the line sometimes crosses the text** so it's hard to read. Route arcs clear into the margin gutter / dim on non-focus.
- [ ] **5. "There are more edges than these — logic-specific?"** — YES: this view filters to the discourse-logic families; sequence + nesting are pulled out on purpose. State it more visibly (the "19 sequence + 26 nesting taken out → 21 that carry the argument" line exists but was missed).
- [ ] **6. Define the edges + make family↔word visible** — what does "BUT" mean; which of the 4 toggles is it. (Answer: BUT = adversative family. "answers" = FILLS in the evidential family — that seam confused at first.) Add a small definition/legend grouping words under their family.

## Round 2 — GPT crit (2026-08-14): Logic is the strongest reader-facing view
Verdict: **"this may have the clearest public-facing why"** of all Connect views. Trace=follow · Scan=architecture · Map=topology · **Logic="Read the passage with its hidden conjunctions restored."** Scores: Intuitiveness 3→**5** · Wayfinding 2.5→5 · Reader-usefulness 3.5→**5**. Target identity: a **logical annotated reading**.

**The 8 priorities:**
1. ⭐ **Word-substitution / read-the-relation** — click an edge → read the two moves joined by the connective as one sentence: *"They ask who will move the stone **[BUT]** they perceive it already moved."* Then the definition beneath: *"Contrast: M7 overturns the expectation M4 opens."* Three levels: **text → connective → analytical definition.** THE identity.
2. **Per-relation natural-language templates** (not all edges are conjunctions): BUT/BECAUSE/SO/THEN slot between clauses; ANSWERS/SUPPORTS/FILLS need a frame ("B answers the question opened by A"). Table of reader-templates per relation.
3. **Arrowheads on every directed relation** (source dot → target arrowhead) — margin position alone isn't perceptually strong enough (the PI read the prose explanation and still didn't notice forward/back).
4. **Direction written out on select** — "M7 → M4 · ANSWERS", never "M4 — M7 / ANSWERS".
5. **Participation port/dot beside every move** in a Logic edge — distinguish the 5 states: no line spotted / truly no logic edge / sequence-only (suppressed) / nesting (indentation) / genuinely disconnected.
6. **Distinguish "no relation" from "relation exists but not drawn"** (the M8/M9 nesting case) — negative space is analytically meaningful; never conflate absent with suppressed. Tiny marks: `↳ nested · → argument link · · sequence only`.
7. **"What is hidden?" indicator** under the title — *"Showing: argument relations · Not drawn: sequence · nesting"* + counts (answers "are these logic-specific?" before you have to infer it).
8. **Family↔label hierarchy explicit** — the 4 toggles are FAMILIES; BUT/ANSWERS are edge labels. Show "RESPONSE · ANSWERS", nest the controls. Reader mode = BUT/BECAUSE/ANSWERS words; research mode = family/type/edge_id.

**Two methodological gifts (not UI) — flag to Method/Atlas Reader:**
- **⭐ The "sentence test" is a coding-adjudication check.** For each relation define a canonical frame ("B runs against the expectation created by A"); then test: *can the two paraphrases plug into the frame without distortion?* If `M4 BUT M7` reads cleanly → good; if it needs a paragraph of explanation → the relation type is probably wrong/too abstract. A validity check on the coding grammar itself.
- **⭐ Don't pretend the connective is in the source text.** The original may not contain "but"; showing `M4 BUT M7` must read as *"our coding says this reads as contrast,"* not *"the text contains 'but.'"* Mark it as an analytical gloss (`reads as: BUT` / distinct color). Critical for translation-sensitive work + honesty (§2.8) — and it's the same axis as the Shape paraphrase-vs-original finding.

Legibility (hard rule): **arcs around the prose, never through it**; strict stack (text > selected > relevant > inactive > guides); mask any line behind a text block. Keep sequence suppressed (optionally a thin reading-spine backbone). Gentle span depth (shallow=near, deep=far) but the WORD is what the eye notices first, not geometry.

## ⟐ Recommendation
Make the **Logic view the primary Trace / reading view** (retire or demote the all-linkage arc band), and fold in the arc-band V2 wins: beside-inspector (not scroll-away), no truncation, click-to-walk. Then build the SHAPE + SONIC per-kind views to the same idiom (the 3DR-19 plan). PI intent needed: Logic-as-Trace, yes?

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: Design SB 2026-08-14. PI's crit-walk reached viz_connect_logic.html and preferred it to the arc band ("what the
  arc band was trying to do"). Captures why (editorial stance: strip mechanical edges, show argument-carrying relations,
  forward/back margins), the family↔word map (render-from-data), and the 6 PI notes. Recommends Logic-as-primary-Trace.
SCHOLARLY SOURCES: viz_connect_logic.html (built to connect_perkind_viz_3DR-19_reconciliation_2026-08-11 LOGIC verdict);
  connect_taxonomy.json (the sub-types the family map consumes); trace_arcband_crit (the V2 interaction wins to fold in). §2.16.
WHAT NEEDS VERIFICATION: (1) PI intent — Logic replaces the arc band as Trace, or both kept? (2) word-substitution reading =
  the joined-sentence render (new, small). (3) nesting-relation cue (indentation reads as "unrelated" today). -->
