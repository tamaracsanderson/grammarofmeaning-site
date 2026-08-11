# Connect v2 — reconciliation (GPT crit + PI direction + the old constellation viz)

**Inputs:** GPT usability crit (2026-08-10, all 3 live figures); PI direction (sonic-on-the-Plate; family→sub-type drill-down); the old off-the-shelf `VIZ_constellation_v3_unified_coffee_2026-07-27.html` (which already solved parts of this); the reading-room / lectio telos.

## ⚠ CORRECTION (from the Connect method drawer — the SSOT, §2.16)

I built the 3 figures on a wrong family scheme. The real edge grammar (`edge_grammar_v1`, drawer PASS/PASS/PASS 2026-08-09) has **FIVE edge-kinds**, not three:

| KIND | scope | sub-types |
|---|---|---|
| **LINKAGE** | in-text logic | FEED · FILLS · NEST_CONTAINS/COMPOSES/REPORTS · LINK_SEQUENCE (cheap default) · LINK_CAUSE/CONTRAST/CONDITION/CORRECTION/SUPPORT/ELABORATES/BACKGROUND/OTHER |
| **LINEAGE** | cross-text reference | CITES · REUSES · BEQUEATHS · RE-READS · INHERITS-ACROSS (this IS Situate's Lineage) |
| **RESONANCE** | both (cross-tradition correspondence) | MATCH (same move) · ANALOGY (A:B::C:D) · COUNTERS · INVERTS — carries NO contact claim |
| **SHAPE** | in-text form | PARALLELISM · JUXTAPOSITION · RING · LEAP |
| **SONIC** | in-text sound (word-level, computed) | RHYME · ASSONANCE · ALLITERATION · CONSONANCE (via `pronouncing`+`panphon`) |

My error (§2.16): I mapped SHAPE→"resonance" (wrong — RESONANCE is its own kind) and dropped LINEAGE. The **drill-down families are these 5 KINDs → their sub-types.** Fixing the figures' `fam()` to the real 5 kinds (hues: linkage=fern · lineage=moss · resonance=gold · shape=olive · sonic=sky; sequence ghosted; terracotta stays reserved for provenance — so 5 kinds fit the house palette, answering the encoding-audit's palette question).

**On SONIC (drawer-confirmed):** it's OUR method (word-level, `pronouncing`+`panphon`), "computed separately at word-level — a different granularity, not this [move-edge] pass." That's exactly why `connect_edges.json` has 0 SONIC and why it belongs on the **Plate**. The old V3 = an early off-the-shelf version of the same libs. So: our-method SONIC and the V3 are the same lineage of computation; the compare-them question is really "our word-level sonic run vs the old artifact."

**More data exists than the WEB feed shows:** the grammar also ran on **MARK-16-GRC (79 edges — the Greek!)** and **TTC-CH1-EN (Daodejing, 17 edges)**, plus **one worked RESONANCE MATCH (Mark↔Daodejing)**. `connect_edges.json` (what's deployed) is only the WEB 78. So the **EN↔GRC comparison** and a **first Facing-Page RESONANCE example** have data — they just aren't exported to the deploy feed yet. Flag to Method SB: export the GRC edges + the RESONANCE edge(s) + (word-level) SONIC.

## Headline (GPT, and it's right)

**The visualizations are stronger than the use-model around them.** The reader is taught *what marks mean* (green = logic) but not *what action to perform*. The fix is a **task model** + making the three a **single coordinated instrument**, not three sibling artworks.

## LOCKS (GPT + PI converge)

1. **CONNECT = one instrument, three coordinated views with functional verbs:**
   - **Trace** (Arc Band) — *follow a relation through the reading* — "what is this move connected to as I read?" — the READING view.
   - **Scan** (Relation Loom) — *see the whole pattern* — "where are the structural hotspots + long reaches?" — meso-analysis.
   - **Map** (Topology Lab) — *hubs & clusters, order removed* — "what's central when sequence is dropped?" — the RESEARCH view.
   Keep the poetic names as subtitles; lead with the verbs. Retain separate deep-linkable URLs for citation.
2. **State survives the switch (GPT's highest-leverage).** Select M12→M17 in Trace → switch to Scan → that row/column/cell is already highlighted → switch to Map → those two nodes + their edge emphasized → "Back to text" returns to those rows. *"This green arc, this green cell, this green line are the same thing"* becomes self-teaching instead of something the reader must reconstruct.
3. **Task-first, not legend-first.** One primary prompt above each view: Trace = "Pick a move that catches you. Where does it reach?"; Scan = "Find a crowded row or a mark far from the diagonal."; Map = "Find a large dot. Why is this move a hub?" Then a reflective prompt after: "What did this make you notice that the plain text didn't?"
4. **Plain-language relation, not just family (GPT + PI's drill-down converge).** On selection show the *typed relation in prose* — "M17 belongs inside the speech begun at M12" — with `NEST_REPORTS` demoted to research/Inspect. "Logic" is a family, not yet an interpretation.
5. **Family → sub-type drill-down (PI + the old viz).** The 3-family clustering (logic/resonance/sonic) hides the sub-types. Review by family, then drill in: logic → cause · contrast · support · nesting · elaborates · sequence; resonance → parallelism · ring · leap · juxtaposition; sonic → rhyme · assonance · alliteration · consonance. Each sub-type isolable, with counts (the old viz's filter bar is the model: per-sub-type buttons with live counts).
6. **Sonic lives on the PLATE, not the moves — but keep TWO SONIC SOURCES distinct (PI, do-not-conflate):**
   - **(a) OUR method's sonic** = the `SONIC` edge-kind in the Connect grammar. It is **defined but NOT computed** for Mark 16 (`connect_edges.json` = 70 LINKAGE + 8 SHAPE + **0 SONIC**). So our-method sonic is *owed*, not done — the edge_grammar run didn't populate it.
   - **(b) OFF-THE-SHELF sonic** = the old `VIZ_constellation_v3` (Poemage approach + `pronouncing` + `panphon`), an OLD artifact, **not our dataset or method**. Its 41 rhyme / 91 assonance / 77 alliteration / 18 consonance are external computation.
   Either way, sonic ties are WORD-level (which words rhyme/alliterate/assonate/consonate), so they highlight on the verbatim **Plate**, not the move-cards. Any sonic layer must **label which source** it's showing (our-method vs off-the-shelf), never blur them.

11. **The point is the COMPARISON — our-method sonic vs off-the-shelf, and Greek vs English (PI).**
   - **Compute our-method sonic** (populate the `SONIC` edge-kind for Mark 16 — a Connect-grammar/coder run), then **compare it against the off-the-shelf** (Poemage) computation: *where do they agree, where do they diverge, and why?* That methodological comparison is itself a finding (does our coded sonic detection match phonological computation?).
   - **Greek vs English:** sound lives in the *original*; the PI recalls an analysis where the **Greek had stronger sonic edges while the English had stronger resonance/logic edges**. So sonic ideally runs on the **Greek**, and the **EN↔GRC gap shows what translation drops** — negative-space (§2.8), thesis-relevant. Tooling caveat: `pronouncing` (CMU) is **English-only**; Greek sonic needs different phonology tooling. Composes with the bilingual EN↔GRC Plate.
7. **Tie CONNECT to the Move Score (GPT).** Clicking a move shows "Connections: 7 · 5 logic · 1 resonance · 1 sequence · Follow →" which opens Trace positioned at that move.
8. **Reading vs Analysis hierarchy (GPT).** `READING: Plate → Move Score → Trace` · `ANALYSIS: Scan → Map (behind a Research door)`. Don't force all three to be equally contemplative — they are different epistemic distances (I am still reading / inspecting my reading / studying the model). Every abstract discovery has a one-click route back to the words.
9. **Demote unavailable sonic move-edges.** In the move-edge views, "sonic — not coded yet" currently gets near-equal status; show it as *disabled/unavailable for this passage* (the real sonic action is on the Plate, per #6).
10. **Onboarding = a 60-second "same relation, three views" worked example** on the real Mark data (M12→M17): trace it → scan it → map it → "now follow M12 yourself." Explain the *translation between views once*, not each page separately.

## Build order

**P1 — buildable NOW on existing data (`connect_edges.json` has the `type` sub-field):**
- Family → sub-type drill-down in all 3 views (2-level legend/filter with counts). [#5]
- Plain-language relation card on selection (a small `type → prose` table; `NEST_REPORTS` → "the speech begun at M12 continues through M17"). [#4]
- Task-first prompt + reflective prompt per view; demote sonic-edges to disabled. [#3, #9]
- Direction visible on selection.

**P2 — the unified instrument (a refactor, the highest-leverage):**
- Merge the 3 pages into one CONNECT shell with a Trace/Scan/Map control + **shared selection state that survives the switch**. [#1, #2]
- The Move Score → CONNECT tie ("N connections · Follow →"). [#7]
- The Reading/Analysis hierarchy + the 60-sec worked example. [#8, #10]

**P3 — the Plate sonic layer (off-the-shelf compute, needs a feed):**
- Bring back the old viz's **sonic ties** (rhyme/assonance/alliteration/consonance via **Poemage-approach + `pronouncing` + `panphon`**) as a **feed** (`sonic_ties.json`: word/token spans + tie sub-type), rendered as a clickable **sound layer on the Plate** (click a sub-type → tied words light up). [#6]
- **English** path is off-the-shelf (pronouncing/CMU) → quickest to re-feed. **Greek** path needs different tooling (Greek phonology, not CMU) → its own build. [#11]
- **The finding to surface:** run both and show the **EN↔GRC sonic gap** — where the Greek's sound-ties have no English counterpart (what translation drops). Negative-space, thesis-relevant.
- **Data need:** the computation is off-the-shelf but isn't a current feed. Flag to Method SB: export `sonic_ties.json` (EN now; GRC as a follow-up), render-from-data, so the Plate sonic layer isn't hardcoded.

## Notes
- The old `VIZ_constellation_v3` is a strong reference for #5 (per-sub-type filter bar with counts) and #6 (sonic on the words) — but it mixed sonic + move edges on one field; GPT's model separates *reading* (Plate sonic + Trace) from *analysis* (Scan/Map), which is the better architecture.
- This composes with the progressive-layering thread (Plate → Moves → Gloss → Situate → Connect): CONNECT itself becomes a layer with its own Trace/Scan/Map internal views.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: design-SB 2026-08-10 — reconciliation of the GPT usability crit (PI-run) + PI direction (sonic-on-Plate; family→
  sub-type drill-down) + the old VIZ_constellation_v3 (which already did per-sub-type filtering + sonic-on-words) into a Connect
  v2 build spec. §2.6 (cohort → reconciliation is the deliverable), §2.15 (diverge→converge), §2.16 (reader never sees raw schema
  labels — plain-language relation, NEST_REPORTS demoted).
SCHOLARLY SOURCES: GPT crit (cites arc-diagram/matrix/node-link viz literature — spot-check before chapter use); the 3 live
  figures; connect_edges.json (the type sub-field enables drill-down NOW); the old constellation artifact (sonic via pronouncing+
  panphon); the lectio/reading-room telos.
WHAT NEEDS VERIFICATION: (1) PI ratifies the Trace/Scan/Map unification + the build order. (2) P3 needs a sonic_ties.json feed
  (flag to Method SB — the computation exists, the feed doesn't). (3) the type→prose table (#4) is a small controlled vocabulary
  to write + validate. (4) P2 is a real refactor (shared state across views) — scope before building. -->
