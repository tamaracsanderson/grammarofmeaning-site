# Method-engine diagram — crit synthesis + plan (S161, 2026-08-07)

**Inputs synthesized:** Lovable's first crack (`method-engine-flow.lovable.app`) · reading-SB's reduction crit · ChatGPT's
17-section crit · design-SB's own crit. **Deliverable the PI asked for:** synthesize the crits + a sequenced plan.
**Decision baked in:** another Lovable crack (with a synthesized revision brief) → design-SB static rebuild — NOT in-house
takeover yet (the ontology must resolve first; Lovable's geometry is the asset; the fixes are mostly reduction).

---

## A. WHERE ALL THREE CRITS AGREE (high confidence — just do these)

1. **It's a reduce-pass, not a redo.** The bones are right: the bow-tie reads, both bands are there, the waist is central,
   direct-vs-combination is distinguished. Keep them.
2. **Hero skeleton + drill-down.** ~7–10 primary objects tell the whole story at a glance; all node detail (sublines,
   layers, badges, status prose) moves into the click-drawer the brief already specified. Lovable inlined the drawer
   content — that's ~70% of the density.
3. **Collapse the direct-output mirror-doubling** (reading-SB). Sitz/Paradigm/Frame/Witness appear twice (left category +
   right output tile). The category IS its output — tag it in place; kill the right-side boxes and their crossing arcs.
4. **Preserve + amplify "the instrument speaking" vs "the tradition speaking."** All three call this the strongest idea in
   the diagram — it does real methodological work (generated constructions vs retrieved historical voices). Make it MORE
   prominent as detail recedes.
5. **Keep the honesty statuses** (live/pilot/awaiting/paused) — but move their explanatory burden off the primary canvas.

## B. WHAT ChatGPT ADDS (net-new beyond reading-SB + me)

### B1. ONTOLOGY tightening — resolve BEFORE the artwork (Gate 0; reading-SB's domain)
- **Rename the two edge types:** DIRECT → **WAIST-INDEPENDENT**; COMBINATION → **MOVE-CONDITIONED**. More accurate —
  Sitz/Paradigm/Witness aren't "straight from raw text," they involve contextual reconstruction; the true distinction is
  "needs the coded-move representation or not."
- **The waist: "coded move" vs "enriched move record."** The DB truth (CRT) is that `source_move` *carries* sitz+paradigm
  columns — so the shared object is the move **with context attached**. ChatGPT's fix: draw **Grammar → move (produces)**
  and **Situate → move (attaches)**, not both "producing" it. This answers the committee question "does Sitz determine the
  segmentation?" → **no** (Grammar sets boundaries; Situate annotates). Aligns with engine truth; strong improvement.
- **Frame's label is misleading.** CRT engine truth: Frame → Morphospace is text-level (atlas_frame_reader reads a *chunk*,
  not moves) → genuinely waist-independent. But the label "the 8-axis stance *the move* takes" implies move-level. **Fix =
  reword the label** (engine truth wins; ChatGPT's concern is real but resolves to a labeling fix). Confirm w/ reading-SB.
- **Reception is gap-driven.** Not "move → Reception" but **move → gap/question → Reception retrieval** (real texts
  answering *this named gap*). This unlocks the strongest possible visual: **GAP → { constructed Gloss | retrieved
  Reception }** — the instrument's voices vs the tradition's voices, mirrored on one fork. Potentially the most memorable
  element in the whole diagram. Confirm the dependency w/ reading-SB.

### B2. METHOD vs AUDIT dual-mode (big for the thesis)
Two *presentations of the same JSON*, a toggle — not two datasets:
- **METHOD (default):** topology + node names + one-line functions + tiny maturity dots.
- **AUDIT (toggle):** adds implementation status, coverage warnings, row-counts, known-limits, dependency metadata.
Why it matters: **implementation maturity ≠ methodological validity.** "Live = built + has data" can read as "validated" to
a committee. Keep operational status, but don't let it masquerade as epistemic confidence. (Extend the JSON:
`implementation: specified|built|populated|retired` separate from `validation: untested|internally-tested|benchmarked|
externally-reviewed`.)

### B3. Visual engineering (the size fixes)
- **Bypass RAIL, not 5 arcs.** One thin "waist-independent" bus/trunk that the direct views tap off — ~2 long curves, not
  5 crossing spaghetti arcs. Converse on the right: **one thick fern trunk out of the waist → short fan branches** = the
  literal pinch-and-release the "bow-tie" promises.
- **2-D output FIELD, not a vertical filing cabinet.** The right side is the biggest vertical explosion — a tall single
  column makes the "fan" look like a *list*. Lay outputs in a compact grid (WAIST-INDEPENDENT row · MOVE-CONDITIONED grid ·
  RECEPTION · SYNTHESIS) so the fan looks like a fan. Small 36–48px tiles, not 160×90 cards.
- **~10 primary objects, fewer rectangles.** Reserve bordered cards for the 7 structural stages (Text · Decompose ·
  Situate · Coded move · Reception · Synthesis · Reading Room); output leaves = plain labels on a faint band wash.
- **Compact header** (~100–130px, not ~220–300px) — the figure starts almost immediately.

### B4. Explicit acceptance test (give Lovable an objective target, not "smaller")
> At **1440×900 CSS px, browser zoom 100%**, the whole path Text → Reading Room is visible with **no horizontal or
> vertical scroll**; all primary labels ≥13px. Figure body ~650–700px; waist ~150px; left cone ~28% · gutter ~12% ·
> right fan ~42% · synthesis/end ~18%. Detail expands only on interaction.

### B5. Naming fixes
- **"Grammar" is overloaded** (the decompose branch AND the whole upper output band). Rename branch → **DECOMPOSE**; band →
  **RECOMPOSITIONS / ANALYTIC OUTPUTS — the instrument speaking**. Keep "grammar" for the move-grammar *inside* Decompose.
  Recovers the old method page's **decompose → recompose** vocabulary.
- **Gaps:** "Detect gaps" (inside Decompose) vs "Gap map / published gaps" (output).
- **JOINS vs Cross-output joins:** make operation-vs-view explicit, or collapse to one.
- **Reading Room is NOT meta** — it's the reader-facing *delivery* surface; only "instrument reads itself" is meta. End the
  main flow at **Reading Room**; put **Reflexive audit** in a thin strip below the whole diagram.

### B6. Engineering (matches design-SB's rebuild plan)
HTML/CSS-grid nodes + **one absolute inline SVG layer** for connectors; JS measures anchors (`getBoundingClientRect` +
`ResizeObserver`) and draws the bus/trunk/fan paths. **No graph-layout lib** (Dagre/ELK/Cytoscape/force) — the topology is
*authored, not discovered*. Add `grain / requires / produces` to the JSON so the data can validate the method (e.g. exposes
any "independent branch but move-level" tension automatically).

## C. DIVERGENCES to put to the PI / reading-SB

1. **Reading Room: META (CRT) vs delivery-surface (ChatGPT). → RESOLVED (PI, 2026-08-07): NOT meta.** The main flow ENDS
   at **Reading Room** (the reader-facing delivery surface); **"instrument reads itself" drops to a thin reflexive-audit
   strip below the whole diagram.** This becomes ontology-addendum item 5 (LOCKED by PI); reading-SB item 5 = FYI, not a
   ruling. Fold into the Lovable revision brief.
2. **Frame text-level vs move-level.** Resolves to engine-truth (text-level) + a label reword — but reading-SB confirms.
3. **How many modes to ship now.** METHOD-only first, or METHOD+AUDIT toggle in the first rebuild? *Lean: build the JSON to
   support both; ship METHOD default + AUDIT toggle if cheap, else METHOD first.*

---

## D. THE PLAN (sequenced)

**Gate 0 — ONTOLOGY LOCK ✅ CLEAR (2026-08-07)** — reading-SB ruled all 5, no engine-spec change; PI locked #5. Folded
into the revision brief `_staging/_tools/lovable_brief_method_engine_bowtie_v2_s161.md` (Step 2 DONE, ready for PI paste).
*(reading-SB + PI; blocked the redraw).* Resolve: (1) waist = enriched-move-record; Situate
*attaches* not produces; (2) direct/combination → waist-independent/move-conditioned rename; (3) Frame label reword
(text-level confirmed); (4) Reception = gap-driven (move→gap→retrieval); (5) Reading Room = delivery, reflexive-audit =
thin strip. Output: a 1-paragraph ontology addendum design-SB folds into the brief.

**Step 1 — design-SB writes ONE synthesized Lovable revision brief** (all of §A+§B+resolved §C). Reduction + ontology +
the B4 acceptance test + METHOD/AUDIT modes + renames + the grain/requires/produces schema + "bypass rail / waist trunk /
2-D field / ~10 objects / compact header." Paste-ready, on the DWS.

**Step 2 — PI: paste → Lovable second crack.**

**Step 3 — design-SB: ingest Lovable's 2nd output → static rebuild** (HTML grid + inline-SVG connector layer per B6;
render-from-`method_flow.json`; drawers carry the detail; AUDIT toggle) → **staging**.

**Step 4 — PI eyeball vs Lovable → flip `method-schema.html` → the rebuilt page.**

**Parallel track (independent):** PI + reading-SB finalize the master engine (7 DPs; DP-3 `gap_gloss` + the name are the
PI's). The diagram track above needs no PI real-time except Gate 0 + Step 2 + Step 4.

---

## E. ChatGPT crit of the 2nd Lovable crack (2026-08-07) — "close to thesis-ready," ~8 changes then STOP

Verdict: the reduce-pass worked — governing idea first, machinery second. Landed: enriched-move waist as the hinge; the
GAP MIRROR as the centerpiece; METHOD/AUDIT (implementation ≠ epistemic); reflexive-audit off the flow; readable at
ordinary scale. **8 priorities for one LAST pass, then stop (removing more would delete real methodological distinctions).**

**Semantic/accuracy (all ALIGN with our locked ontology — render/label fixes, not new ontology; quick reading-SB confirm):**
1. **Selected Gap originates from the ENRICHED MOVE, not Cross-analysis.** The 2nd crack's heavy curve into Gap appears to
   come from Cross-analysis → implies the wrong method. Give Gap its OWN thick branch off the waist. (Matches locked item
   4: Reception is gap-driven, move → gap → retrieval.) The waist should split into two destinations: **recompositions** +
   **interpretive Gap** ("recompose the move" ∥ "interrogate its silence").
2. **The mirror must visibly REJOIN at Synthesis** — a little bow-tie nested in the big one: Gap → {Gloss | Reception} →
   **Synthesis** → Reading Room. Gives Synthesis an unmistakable job (relate the two voices). Reword its gloss "the argument
   across frames" → **"relates claims across frames + voices."** (Aligns with CRT: Synthesis = per-gap colloquy + joins.)
3. **Three gap LEVELS, currently blurred:** Gap detection (in Decompose) → **Gap findings** (the mapped set; rename the
   "Gap-map" card) → **Selected gap** (one named QUD; rename the centerpiece "Gap" → "Selected gap"). Light selection edge
   Gap-findings ⇢ Selected-gap; heavy dependency edge Enriched-move ⇒ Selected-gap. (Matches `source_move_gap` store +
   S7 "top selected gaps.")

**Reduction/labels (design-SB's lane — fold directly):**
4. **Drop the duplicate Sitz-view / Paradigm-view cards** (they only say "rendered" — no transform). Keep only genuinely
   transformed views as output objects: **Morphospace · Degrees · Constellation.** Sitz/Paradigm stay in Situate tagged
   "↳ rendered." (Frame→Morphospace and Witness→Degrees dup IS meaningful — keep.)
5. **Collapse Situate's 5 children in METHOD mode** so Decompose ∥ Situate look genuinely parallel (equal size); the 5 rows
   move to the drawer / AUDIT. (Right now Situate towers over Decompose.)
6. **De-border the output leaves** (plain labels on the tinted band, still `<button>` full-hit-area); reserve bordered
   cards for the structural spine.
7. **Rename "maturity dot" → "build/implementation status"; fix legend "coded move" → "enriched move"** (symmetry: "does
   not require / requires the enriched move").
8. **Integrate the waist-independent RAIL into the band heading** (concept currently named 3×: legend + rail label + band
   heading — drop the rail's separate label; make the rail the band's upper edge).
+ Textual: subtitle "one shared enriched move" → **"shared enriched-move record"** (a data type, not a count); Situate
  "annotate each move in its world" → **"attach context to each move"**; AUDIT shows state on PRIMARY nodes only, the
  per-component Situate table lives in its DRAWER (inline sub-node pills break legibility). + design-SB color rec:
  **Reception (canon/tradition voice) → warm terracotta; all instrument outputs → cool fern** (the gap mirror = two colors).

**Engineering caveat (ChatGPT):** the DEPLOYED Lovable URL still serves the OLD build (direct/combination/coded-move) —
deployment/crawl lag. Don't treat that URL as canonical; the crit is from the new screenshots. ⇒ argues for NOT depending
on Lovable's export.

## F. THE FORK (2026-08-07) — take it in-house now vs one more Lovable pass
Design is proven + only refinements remain (ChatGPT: stop after these). The 8 are exactly connector-accuracy (#1/#2 =
precise SVG geometry design-SB draws anyway), reduction (#4-6), and labels (#7/8) — design-SB's lane + the react→html
rebuild is design-SB's regardless. Lovable's deployed export is stale (caveat above). **Recommendation: take it in-house —
design-SB rebuilds the canonical static page from scratch** (own method_flow.json extended to the final structure + house
tokens + the 2nd-crack screenshots as the visual target), folding all 8 + Reception-warm → staging. One step, becomes the
canonical page, no stale-export dependency. Alternative: one more Lovable v3 pass, then rebuild (slower; keeps Lovable in
the loop). The calculus flipped since the PI's earlier "another crack vs takeover" — that was right when the design was
rough; now it's proven. PI's call.

<!--
HOW PRODUCED: design-SB S161 (2026-08-07). Synthesis of Lovable's first method-engine crack + reading-SB's reduction crit
+ ChatGPT's 17-section crit + design-SB's crit, at the PI's request ("synthesize and develop a plan"). Decision: another
Lovable crack with a synthesized revision brief, then design-SB static rebuild — per the PI's "another crack vs takeover"
steer. Ontology-before-artwork sequencing per ChatGPT §17 priority order.
SOURCES: method-engine-flow.lovable.app (1st crack); CRT_method_schema_v2_vs_engine_reality_s161 (edge-types, waist,
Lineage move-level, Frame text-level via atlas_frame_reader, Reception gap-answering); ChatGPT crit (ontology rename,
METHOD/AUDIT modes, bypass rail, 2-D field, acceptance test, naming, grain/requires/produces); lovable_brief_method_engine
_bowtie_s161.md; CLAUDE.md §2.13/§2.16.
WHAT NEEDS VERIFICATION: Gate-0 ontology calls are reading-SB's + the PI's; §C divergences unresolved until then; whether
Lovable can hit the 1440×900 acceptance test in one more crack or needs two.
-->
