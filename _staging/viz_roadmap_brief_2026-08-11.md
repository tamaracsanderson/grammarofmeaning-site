# Forward visualization roadmap — brief (for the v2 design-SB)

**Why now (PI directive 2026-08-11):** Situate + the MCA/morphospace data are finalizing, so this is the window to develop the FORWARD roadmap — the visualizations *beyond* the sections we already have — by synthesizing everything we've already explored. This is a PLANNING + light-mock task (mostly unblocked); it produces the prioritized build queue for when the data lands.

## The task
Develop a prioritized roadmap of FURTHER visualizations, organized by three axes (PI's framing):
1. **With additional ANALYSIS** — a new analysis unlocks a new viz (e.g. Greek sonic/shape; cross-tradition RESONANCE at scale; gap-shape audits; degrees-of-separation).
2. **With additional MATERIALS** — new sources/texts unlock a new viz (e.g. more traditions; real reception texts; other-language runs).
3. **COMBOS** — combining existing engines/outputs into new composite views (the reading-sequence below; Compare×Lineage "JOINS"; sonic×move; move×frame).

For each candidate: one line on *what it shows*, *what it needs* (analysis / material / combo), and a flag — **buildable-now / data-blocked (on-whom) / cross-SB**.

## Review these FIRST — don't reinvent (design-SB is read-only on twelve-laws; `git show origin/main:<path>`)
- **The DRs** — `research/10_dr/` in twelve-laws: `viz_methods_reconciliation_2026-08-06` (the adopt-vs-build map: partiture=BUILD [CollateX+D3], seismograph=ADOPT [horizon/ridgeline], lineage=ADOPT [d3-sankey]); `translation_change_viz_reconciliation_2026-08-05` (the partiture greenlight); the sonic / lineage / witness DR reconciliations; the 3DRs.
- **The reconciliations + backlogs** — `_staging/connect_v2_reconciliation_2026-08-10` (Trace/Scan/Map + sonic-on-Plate + EN↔GRC), `_staging/move_score_v2_backlog_2026-08-10` (the **progressive-layering** thread — Plate→Moves→Gloss→Situate→Connect as a stack).
- **The reading-SB S161 DESIGN_BRIEFs** already in the DWS `conventions` FIGURE QUEUE: Witness/transmission, lineage/tributary, sonic-constellation, translation-partiture — each with render-craft flags. These are half the roadmap already; fold them in.
- **Past tests** — the 3 built Connect figures, the Move Score, and the old `VIZ_constellation_v3` (off-the-shelf sonic via **Poemage + pronouncing + panphon**).

## The headline COMBO — present the READING SEQUENCE (PI wants this designed)
A designed *sequence* through the engines — a reading FLOW, not separate figures:

**move score → situate (the added context) → gaps (the top questions) → gloss (the responses that could-have-been, from our agents) → reception history (what was actually received)**

This is the progressive-layering thread made concrete. The design challenge the PI named: **be thoughtful about showing all this without overload.** Propose the flow — progressive disclosure, one layer at a time, the reader deepens (lectio: draw→linger→respond→reflect); the *gap* is where "the responses that could-have-been" (Gloss, our agents) sit beside "what was actually received" (Reception) — *where they diverge is the finding*. The DESIGN can be developed now (mock against the shape); the live wiring is data-dependent (Situate/Gaps/Gloss/Reception feeds). Surface the sequence to the PI early.

## Two near-term items the PI flagged — assess + queue with HONEST caveats
### A. The Partiture (translation) — buildable NOW?
PI: we have BOTH Greek + English **moves** for Mark 16 → build the translation Partiture + "add *between*" (the comparison). **First verify the data** (don't assume): is there a GRC moves.json alongside the WEB one, and — critically — is there a **cross-version move ALIGNMENT** (which GRC move ↔ which EN move)? *Moves existing ≠ alignment existing.* Per the DWS FIGURE QUEUE, the partiture's L2 hero "waits on reading-SB's aligned move-families." So likely: **L1 chapter heatmap** (granularity/variance) is buildable now from the two move sets; the **L2 partiture hero** (4 lanes over a shared semantic sequence) needs the alignment export — request from reading-SB. Build L1 if its data is on main; flag L2's alignment need.

### B. Greek sonic + shape — the EN↔GRC comparison "outside of just words"
PI: run the Greek sonic + shape (same as English) and see what changes with translation — *beyond lexical* (structure, not just words). Caveats: (1) **Greek SHAPE** edges EXIST (the GRC connect run = 79 edges) but aren't exported to the deploy feed — request from Method SB. (2) **Greek SONIC** needs *different tooling* — `pronouncing` (CMU dict) is **English-only**; Greek phonology needs `panphon` + a Greek pronunciation source (a Method-SB / tooling task — flag it, don't fake it). So: the EN↔GRC **SHAPE** comparison is near-term (needs the GRC edge export); the EN↔GRC **SONIC** comparison needs the Greek-sonic tooling first. The FINDING — *what translation drops/re-shapes structurally, not just lexically* — is the §2.8 negative-space payoff and is thesis-gold.

## C. Multi-media gallery-picker (per passage + Situate) — cross-SB
A **media gallery** that, per passage, surfaces *candidate* images/media the PI picks + places as she builds the reading room. Two source streams (PI): (1) **our library** (the Librarian's media holdings); (2) **the SEVERAL open-access museum APIs the Lovable mock wired up quickly** — **MET Open Access + the Art Institute of Chicago (AIC) + others** (PI: "a few Lovable used… chicago, etc"). **FIRST STEP: extract the full API list from the mock** (its code/config + `IMAGE-CREDITS.md` carry the endpoints + provenance rules; likely also Smithsonian OA / Rijksmuseum / Cleveland / Harvard-class CC0 sources — confirm from the mock, don't guess). The **Night Gallery** work is the working precedent (`reading-room-preview/data/gospels_room_config.json` = 34 candidate plates w/ credit + crop; open thread in this file). **ELEVATION (PI):** drive the query from **Situate, not just the scripture** — paradigm · location · time period (Mark 16 → 1st-c. Jerusalem · empty-tomb tradition · corpse-care/anointing paradigm → candidates of period tombs / anointing / the place), so media is grounded in the *Sitz*, not a generic illustration. **OWNERSHIP:** Librarian owns media SOURCING (library + API acquisition + the Situate-driven queries — their acquisition lane; they hold the MET architecture); **design-SB builds the gallery-PICKER UI**; provenance §2.4 (CC0/credits) per the Night Gallery pattern. **Flag to the Librarian.** Buildable-shell-now (a picker over the existing gospels_room_config candidates); the Situate-driven query needs the Situate data + a Librarian acquisition query.

## D. Reconsider the Connect figures — per-kind SEPARATE views (not all overlaid) — PI correction
Now that the 5 `edge_kind`s are known: overlaying ALL kinds on one graph is **too many lines** (78 now; worse when LINEAGE/RESONANCE/SONIC populate). **PI:** look at **LOGIC · SHAPE · SONIC separately** — but still be able to actually **TRACK what the edges tell us**, which is a **DIFFERENT reading than the Move Score** (move-by-move spine) — Connect is for reading the *structure*. **SO:** default the Connect v2 to **one-kind-at-a-time** (a clean Logic view · Shape view · Sonic view, per Trace/Scan/Map form), with compare/combine as the *option* — NOT the current all-kinds-overlaid default. We already built the drill-down (filter to one kind); this **promotes "one kind" from a filter to the primary mode**. Optimize Connect for edge-reading, not a second decorated move-list. This is a design reconsideration of the 3 shipped figures — fold into the connect_v2 design (elevates reconciliation #5 drill-down to per-kind-primary). **Buildable now** (the taxonomy + filter already exist; it's a default-mode + nav change).

## Output
A **roadmap doc** in `_staging/`: the 3-axis candidate list + the reading-sequence design + the Partiture/Greek assessments, every item flagged **buildable-now / data-blocked (on-whom) / cross-SB** — so it's the ready-to-prioritize build queue the moment the Situate + MCA data lands. Surface (i) the reading-sequence design and (ii) the Partiture-now question to the PI.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: design-SB 2026-08-11 — brief for the v2 design-SB to develop the forward visualization roadmap during the
  Situate/MCA data-finalization window, per PI directive: (1) further viz by additional-analysis / additional-materials / combos;
  (2) review ALL the DRs + past tests; (3) design the panel READING SEQUENCE (move score→situate→gaps→gloss→reception); (4) the
  translation Partiture (Greek+English moves for Mark 16); (5) Greek sonic+shape vs English (translation change beyond words).
  §2.15 (diverge→converge; roadmap = the converge), §2.16 (render-from-data; flag data-blocked honestly), §2.8 (the EN↔GRC gap
  as negative-space finding), §2.9 (synthesize discovered inventory — the DRs — don't let it rot).
SCHOLARLY SOURCES: research/10_dr/ (the DR reconciliations); the connect_v2 + move_score reconciliations; the reading-SB S161
  design briefs; VIZ_constellation_v3 (Poemage+pronouncing+panphon). Cross-SB: reading-SB (move alignment, partiture data),
  Method SB (GRC edge export, Greek-sonic tooling).
WHAT NEEDS VERIFICATION: (1) whether a GRC moves.json + a cross-version move alignment exist on main (gates the Partiture hero).
  (2) whether the GRC connect edges are exportable to deploy (gates EN↔GRC shape). (3) Greek-sonic tooling (Method SB). (4) the
  Situate/Gaps/Gloss/Reception feeds (gate the reading-sequence live wiring; the design is developable now). -->
