# Morphospace / Archetypes — crit log

**Figures:** `_staging/viz_morphospace_archetypes.html` (+ `viz_morphospace.html` scatter) · live: https://grammarofmeaning.org/_staging/viz_morphospace_archetypes.html
**PI + GPT crit 2026-08-14.** "A strong research result trapped inside a scatterplot + legend." Research value 5/5; ability-to-inspect-evidence 1.5/5. The plot's worth keeping; **redesign everything around the dots.** The shift: from "our MCA scatterplot with four named quadrants" → **"an Atlas: pick any text → where it stands + why; pick a region → meet its texts; pick a tradition → see where it travels."**

## PI notes (2026-08-14)
- [x] **"click to isolate" was backwards** — SHIPPED: solo-on-click + reset (click a family to isolate, click again to show all).
- [ ] **Hierarchy inconsistent** — "Abrahamic 78%" as one color while tiny families (Americas: Native, Africa: Diaspora, Pacific) are split individually. "Abrahamic" ≠ analogous to "Christianity". → **Atlas Reader.**
- [ ] **Archetypes need explanation + examples**, not poetic names floating over dots — the PI prefers the earlier walk-through with an example or two + more on each category.
- [ ] **"Prophet's Fire" feels off** — are these final names? → **Atlas Reader + PI.**
- [ ] **Didn't we unpack Abrahamic?** — the annotation unpacks it (Christianity/Islam/Judaism by name) but the LEGEND still groups it. Inconsistent.

## ⭐ THE METHODOLOGY QUESTION (Atlas Reader — rigor ahead of elegance)
Is **Receive↔Interrogate / Rupture↔Belonging** = the actual **MCA Dimension 1 / Dimension 2** (interpreted), or **two axes constructed independently** from selected coded variables? These are NOT the same claim. If MCA-derived: label "MCA Dimension 1 — interpreted as RECEIVE↔INTERROGATE" + a "why we call it this →" showing the contributing categories (MCA coords must be interpreted via category contributions, not assumed to carry intrinsic labels). If constructed: say so — else a reader infers "the algorithm discovered two psychological questions." Defensibility issue.

## GPT — the 8 priorities
1. **⭐ Make every dot inspectable** (priority #1). Hover = *text + identity* (Mark 16:4 · Christianity · Gospel · paraphrase · archetype); click = **persistent inspector**: text → provenance → **all 8 position coordinates** (each defined *in place*: epistemic-warrant / ontology / inferential-operation / telos / evaluation / hermeneutic-posture / relational-topology / relational-condition) → "why here" (toward Receive because…, toward Rupture because…) → **"see 10 nearest neighbors →"** (ties to Neighbors).
2. **Fix click-to-isolate** — single click = SOLO; add `Show all / None / Compare +`. ✓ SHIPPED (solo + reset; Compare is a follow-up).
3. **Unpack macrofamilies** — strict **FAMILY → TRADITION → SUBTRADITION** hierarchy; **"Color by: tradition / family"** toggle, default *tradition*. Reveals whether the ochre continent is all-Christianity or Chr+Jud+Isl in distinct regions. → Atlas Reader (taxonomy).
4. **Archetype explanations OUT of the plot** — 4 cards beside/below: descriptive title + definition + **1–2 representative passages from different traditions** (algorithmically near-centroid, not hand-picked) + "why they share this region". Remove the giant quadrant labels covering the dots (chart shows geometry; cards explain meaning).
5. **Revisit names, esp. "Prophet's Fire"** — Abrahamic-resonant (bad on a cross-tradition claim), charged, doesn't transparently say "receive+rupture". Make **descriptive names primary, evocative secondary**: Critical–Deconstructive (*Unmasker*) · Prophetic–Reforming (*was Prophet's Fire*) · Emergent–Relational (*Weaver*) · Devotional–Covenantal (*Sanctuary*). **Validate against the 20 centroid-nearest texts** — if the label isn't obvious there, rename from the data.
6. **Expose all 8 coordinates + define each at point of use** (progressive disclosure).
7. **Clarify MCA-derived vs constructed axes** (the methodology question above) + a "why this axis?" disclosure showing contributing categories (research mode).
8. **Connect to Neighbors** — any selected dot → "see closest counterparts →".
- Corpus imbalance: **Actual corpus | Balanced** toggle (ties to the prevalence check). Compare mode (Christianity + Buddhism …). **Search** ("find a text" → zoom to dot). Density toggle (POINTS | DENSITY hexbin) for the overplotted Abrahamic mass. Archetypes = **continuous directions/regions, not hard boxes**; center = legitimate MIXED position (don't over-read); optional archetype-strength = distance-to-corner (strong exemplar vs border case).

## The V2 IA — one right rail that changes with selection
Nothing selected → the 4 archetypal directions (definition + 2 examples each). Tradition selected → N reads + distribution across archetypes + corpus caveat. Point selected → text + metadata + 8 coordinates + why-here + nearest neighbors. Controls: `Find a text… · Explore archetype ▾ · Compare traditions ▾ · Actual | Balanced`. This is the same **Atlas** as Neighbors/Path/Mixing/Check — the morphospace scatter is its Landscape.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: Design SB 2026-08-14. PI + a deep GPT crit on the morphospace/archetypes figure. Captures: make dots inspectable
  (8-coordinate panel), unpack the Abrahamic macrofamily (FAMILY→TRADITION→SUBTRADITION + color-by toggle), archetype cards with
  centroid-representative examples, the "Prophet's Fire" name concern, and THE methodology question (MCA-derived vs constructed
  axes). Most items are Atlas Reader's (taxonomy/names/MCA); the render (inspectable dots, cards, search, compare) is mine.
SCHOLARLY SOURCES: viz_morphospace_archetypes.html; the PI + GPT crits; §2.8 (corpus-imbalance honesty; soften over-reading);
  MCA interpretation via category contributions (FactoMineR); ties to the Neighbors spec (map_topology_crit) + prevalence crit.
WHAT NEEDS VERIFICATION: (1) MCA-derived vs constructed axes — Atlas Reader. (2) archetype names validated against centroid-nearest
  texts — Atlas Reader. (3) the per-dot 8-coordinate + provenance feed for the inspector — Atlas Reader (same substrate as Neighbors). -->
