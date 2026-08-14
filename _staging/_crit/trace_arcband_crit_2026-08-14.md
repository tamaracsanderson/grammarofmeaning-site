# Trace / Arc Band — crit log + working checklist

**Figure:** `_staging/viz_connect_arcband.html` · live: https://grammarofmeaning.org/_staging/viz_connect_arcband.html
**Data:** `engine/data/goldenpath/mark16/{moves,connect_edges}.json` · `engine/data/connect_taxonomy.json` · `engine/connect_core.js`
**Started:** 2026-08-14 (GPT crit, run by PI). Living doc — append new crit rounds below.

## The central problem (PI + GPT agree)
The underlying idea is strong, but the visualization asks the reader to do too much interpretive work to *perceive* it.
The interaction model says "trace connections," but the visual hierarchy reads as "long list of moves with thin lines at the left."
**Fix:** make V2 much more opinionated about ONE question — *"What does this move connect to elsewhere in the passage, and how?"*
Everything that doesn't help answer that disappears or goes secondary. **Keep the Arc Band concept; keep the name "Trace."**

Scores now → potential: Intuitiveness 2.5→4.5 · Usability 2.5→4 · Info-design fit 4→5 · Wayfinding 2.5→4.5 · Distinctiveness 4→5.
"The information design is better than the UI makes it look" — an encouraging problem.

## The real grammar (verified against connect_taxonomy.json + the Mark 16 feed)
- Mark 16 edges: **70 LINKAGE + 8 SHAPE** → scoping Trace to LINKAGE is honest (90%). SHAPE (parallelism/ring/leap/juxtaposition) is a *different phenomenon* → its own figure.
- LINKAGE sub-types present: `and then` (LINK_SEQUENCE ×19) · `reports` (NEST_REPORTS ×19) · `composes` (×7) · `supports` (×6) · `feeds` (FEED ×5) · `because` (LINK_CAUSE ×5) · `but` (LINK_CONTRAST ×5) · `elaborates` (×2) · `fills` (×1) · `linked` (LINK_OTHER ×1).
- Edges carry `source_move_label` → `target_move_label` (directional data already present; taxonomy `directional` flag currently null — render direction from source→target, don't invent semantic reversal; flag to Method).

---

## THE SIX PRIORITIES (do these first — GPT's ranked list)
- [ ] **1. Scope to LINKAGE.** Remove Shape/Sonic/Lineage/Resonance from THIS figure. Title it **TRACE — connections inside the text**; show only the linkage sub-grammar. (Each other kind gets its own viz later — the phenomenon-specific rule.)
- [ ] **2. Explanation BESIDE the selected move.** Kill the eye-commute to the top. Desktop = sticky right-hand inspector alongside the text; narrow = inline expansion beneath the selected move.
- [ ] **3. Arcs get ~2–3× more horizontal space** so **span** becomes visible (M3→M4 must look different from M3→M38). The band's whole point.
- [ ] **4. On selection, dim every unrelated edge; strongly highlight source + targets.** Selection should transform the picture ("pull three strings taut").
- [ ] **5. Relation type extremely visible** — `SUPPORTS → M5`, not a tiny pill. The sub-type IS the intellectual payload.
- [ ] **6. Never truncate the move text** (it's the *datum* in a close-reading instrument). Wrap to 2 lines; full text on select.

## THE V2 — three states (the target shape)
1. **REST** — "see the passage's connective shape": full passage vertical, wide arc gutter, only meaningful linkage shown (sequence off by default), arcs subdued-but-visible, native section markers, no inspector taking space.
2. **TRACE** — "see everything this move touches": click M3 → M3 strong, unrelated edges nearly gone, targets highlighted, 3 arcs strong + directional, sticky inspector beside the text (`M3 · 3 connections` / `SUPPORTS → M5` / `REPORTS → M4` / `SEQUENCE ← M2`).
3. **FOLLOW** — "walk one relation": click `SUPPORTS → M5` → only M3→M5 strong, both passages readable in full, plain-language explanation between them, **Continue tracing from M5 →**. Makes Trace a *verb*.

## The 16 points (secondary — fold in where clean)
- [ ] 6b. **Directional arcs** — solid dot = source, small landing marker/arrowhead = destination; card uses directional grammar ("M5 SUPPORTS M3").
- [ ] 7. **Stronger selection state change** (unrelated fade ~to nothing; distant targets get numbered badges 1/2/3).
- [ ] 8. **"Walk" as an explicit interaction** — inspector `← prev / next →` + numbered connections + **Continue from M5 →** (traverse M3→M5→M6→…).
- [ ] 9. **Demote sequence** — structural links ON, sequence OFF by default, subtle `+ show sequence` (order already encodes it).
- [ ] 10. **Compress the top region** — `# Trace / See how one move reaches into the rest of the text. / [sub-type chips] / Click any move to trace.` Method behind `How to read this ↗`.
- [ ] 11. **Give long-range relations physical drama** — a 30-move arc should *feel* like 30 moves (the reason to keep textual order).
- [ ] 12. **Lanes by span** — route longer edges deeper left (short = shallow arc, long = deep arc); geometry encodes span, learnable, non-arbitrary.
- [ ] 13. **Reader vs researcher** — public card is linguistic ("M5 gives the reason M3 matters" + the two texts); formal edge-ID/schema behind a "researcher details" disclosure.
- [ ] 14. **Redundant line grammar** — don't let color carry full semantics; families differ by line (feeds=solid / supports=weighted landing / contains=bracket / fills=hollow→filled / sequence=dotted). Name on focus.
- [ ] 15. **Section / episode landmarks** — native divisions (verse/paragraph/speaker) as dividers so "M3→M37" reads as *narratively* distant, not just numerically.
- [ ] 16. **"Shape of the passage"** — reserve the strong claim for when higher-order structure is exposed (dense/sparse zones, hubs, bridges, isolated moves). Currently shows *distribution of encoded connections* — still powerful; name it accurately until then.

---
## Round 2 — GPT crit on Trace V2 (2026-08-14): the problem is the IA, not the graphic
Selected-M4 interaction is now **4/5** ("first version I can imagine reading with"); overall page/nav **2/5**, wayfinding **1.5/5**. "Do NOT redraw the graphic — fix the conceptual hierarchy." The "what is this?" comes from naming + nav one level ABOVE the visualization.

**⭐ THE DECIDED IA — five peer instruments (not a view×lens grid):**
> ## CONNECT — five ways to see how the moves hold together.
> **Trace** follow one move · **Scan** all connections at once · **Map** neighborhoods without order · **Logic** the argument's hidden connectives · **Shape** pairings, rings, returns.
- Nav = `Trace · Scan · Map · Logic · Shape` — **task names only**. Design-names ("Arc Band"/"Relation Loom"/"Topology") are internal; they must NOT sit in the nav (that's what made "TraceArc BandScanRelation Loom…" read as six broken things).
- **Kill "All kinds"** — category error (*kind* = the technical 5-edge-kind term). Current scope = **"All Linkage relations."** Strict: **kind ≠ relation ≠ visualization.**
- Logic + Shape are **peer instruments**, not filters inside Trace/Scan/Map (each has its own bespoke geometry + question).

**8 polish priorities:** 1) nav→task-names-only · 2) header "Trace · Follow one move · Showing: All Linkage `Filter▾`" · 3) "All kinds"→"All Linkage" · 4) **standardize inspector direction** `A —REL→ B` grouped **INTO/OUT** (current "M7→FILLS"/"BUT→M6"/"M3→REPORTS" are 3 syntaxes) · 5) **label active arcs** with relation type on focus · 6) **route arcs around text** (connection lane; text wins) · 7) explain/remove the left numbered dots · 8) keep the selected/faded state (the win) + rename "+ show reading sequence".

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: Design SB 2026-08-14. PI ran a GPT design crit on the Trace / Arc Band figure and asked to collect it in an md
  then work through it. This captures the crit's central problem, the six ranked priorities, the three-state V2 (REST/TRACE/
  FOLLOW), and the 16 detailed points, cross-checked against the REAL grammar (connect_taxonomy.json: 70 LINKAGE + 8 SHAPE in
  Mark 16; linkage sub-types verified — no invented grammar per §2.16). Living doc; Round 2+ appended as the crit continues.
SCHOLARLY SOURCES: the GPT crit (PI-run, 2026-08-14); viz_connect_arcband.html (current figure); connect_taxonomy.json (the
  render vocabulary, mirrors edge_grammar_v1 SSOT); connect_edges.json (Mark 16 feed). §2.16 render-from-data; §2.15 black-box.
WHAT NEEDS VERIFICATION: (1) direction semantics per sub-type (taxonomy `directional` is null) — render from source→target,
  flag to Method for a semantic pass. (2) section-landmark field in moves.json (does it carry native divisions?). (3) the
  reader-vs-researcher split may want a Method/reading-SB wording pass on the plain-language templates. -->
