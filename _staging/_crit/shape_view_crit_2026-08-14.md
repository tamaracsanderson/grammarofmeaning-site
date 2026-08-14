# Connect · Shape view — crit log

**Figure:** `_staging/viz_connect_shape.html` · live: https://grammarofmeaning.org/_staging/viz_connect_shape.html
**PI reaction 2026-08-14:** "I do like how clean this is with the brackets." → the bracket idiom for parallelism is a KEEPER.

## The coded SHAPE edges (from connect_edges.json; §2.16)
- **SHAPE_RING** M2 ↔ M23 (the big concentric arc, "pivot at centre")
- **SHAPE_PARALLELISM** M6↔M9 · M15↔M16 · M20↔M21 · M45↔M46 · M34↔M38 (the brackets)
- **SHAPE_LEAP** M26↔M27 · **SHAPE_JUXTAPOSITION** M25+M26↔M44
- **None carry a `note`/rationale field** → the viz can *assert* the shape but can't yet *explain* it render-from-data. Same "define the edges" gap as the Logic view (#6) + the Ledger-of-Absences principle: the rationale must be logged AT coding time.

## PI Q1 — "why is M2↔M23 a concentric + pivot?"
A **ring composition**: the end mirrors the beginning. M2 *"they arrived at the burial place"* ↔ M23 *"they kept silent, telling no one anything"* — the frame (arrival → silent departure) brackets the scene, with the resurrection announcement at the **pivot/centre** (~M14). A recognized feature of Mark 16:1–8. **But** the viz places the pivot geometrically (midpoint), and the rationale isn't coded — so it can't say WHY without the coder logging it. → same edge-definition need.

## PI Q2 — ⭐ "with the paraphrase, can we see the shape? or does shape require the original language?" (methodological)
The sharp catch. Honest split:
- **Discourse-level shape SURVIVES paraphrase:** the ring (arrival↔silence frame), narrative parallelism (parallel *promises* M45↔M46), large-scale concentric structure — these are about narrative/semantic units, visible in English.
- **Word-level / sonic shape does NOT survive paraphrase:** verbal repetition, syntactic mirroring, sound patterns, meter, word-level chiasmus — these live in the Greek and are lost/distorted in paraphrase. (This is exactly why SONIC is a separate view "on the Plate," and why the checkout keeps the verbatim/anchored/versioned original.)
- **The finding (for Method/Atlas Reader):** SHAPE sub-types are not all paraphrase-safe. Each shape edge should be tagged with the LAYER it operates on — **discourse** (paraphrase-safe) vs **verbal/sonic** (requires the original) — and the verbal/sonic ones coded from the Greek, not the paraphrase. Otherwise the Shape view on paraphrase risks claiming word-level parallelism it can't support (§2.8 bias-visibility). The Shape view currently reads `paraphrase`.

## Round 2 — GPT crit (2026-08-14): keep the geometry, spend V2 on "provable from the text"
Verdict: **the strongest of the Connect views in one sense — "representation and phenomenon finally speak the same language"** (parallel→bracket, ring→nested geometry, juxtaposition→seam, leap→broken jump). Info-fit 5/5, elegance 5/5. **Design law: never use color to distinguish a structure geometry can distinguish.** BUT clarity/evidentiary-transparency 2.5→5 — spend V2 making shapes *provable*.

Seven priorities:
1. **Keep the brackets + bespoke geometry.**
2. **Stop labeling M2↔M23 "concentric + pivot."** A ring is a **higher-order structure**, not an edge. Model it as: **RING R1** → correspondences (A: M2↔M23, B: M5↔M20, C: M8↔M17) → **pivot** (M12). Ontology: "7 detected *structures* (2 parallels · 1 ring · 2 juxtapositions · 2 leaps)", not "7 shape edges." Pairings (parallel/juxtaposition/leap) vs Formations (ring/pivot) are different kinds of object.
3. **Every bracket answers "why are these paired?"** on click/hover.
4. **⭐ MOVE / SOURCE-TEXT toggle** — show the shape on the paraphrase (operational) vs the actual words (textual/formal), matching elements highlighted.
5. **⭐ Evidence basis per shape:** `MOVE · SEMANTIC · LEXICAL · SYNTACTIC · SONIC` — what kind of claim it is.
6. **Define "pivot" exactly; midpoint ≠ pivot** (never auto-privilege the geometric center — layout would manufacture a false discovery). "Why pivot?" expandable.
7. **⭐ Unusual evidence-transparency** — Shape is the most vulnerable to **apophenia** (chiasm-hunting); a pretty bracket makes over-reading look inevitable. Show strength: `explicit · strong · proposed`.
- Juxtaposition = a **marked gap** (not no-line, which reads as missing data — the negative-space problem again). Leap + juxtaposition need one-line definitions (a tiny legend).
- A shape-at-a-glance **mini-map** (musical-score overview) so the shape doesn't disappear inside long prose. Ring drill-down: whole shape → member pair → textual evidence.

**The V2 sentence (= the answer to the PI's paraphrase question):** *"The paraphrase shows the proposed structure; the text lets you test it."* → **Paraphrase reveals operational shape; the original verifies textual shape.**

## ⟐ THE UNIFIED FINDING of the crit-walk (Logic + Shape + Sonic) — for Method/Atlas Reader
Every relation claim has an **evidence basis** on a translation-sensitivity gradient, and the basis decides whether paraphrase suffices or the original is required:
- **MOVE / SEMANTIC** → paraphrase-safe (Logic's discourse relations; move-level shape like the arrival↔flight ring).
- **LEXICAL / SYNTACTIC** → needs the original (verbal parallelism, chiasm).
- **SONIC** → original-only (sound doesn't survive translation at all).
→ **Coding-schema addition:** tag every Connect edge with `evidence_basis` + `strength`. Then: Logic marks its connective as "reads as" (analytical gloss, semantic); Shape gets MOVE/SOURCE + basis; Sonic is gated on the original. **Blocker — CORRECTED (PI 2026-08-14):** the Greek DOES exist — there's a full `goldenpath/mark16_grc/` run (moves + connect_edges), and many drawers carry greek/grc/SBLGNT. My earlier "no Greek" was wrong (I checked only `mark16/checkout.json`, the English WEB/Gutenberg feed, and overgeneralized — the check-one-file trap). So the unblock is NOT "acquire the Greek" but **"point the SOURCE view at the Greek that already exists"** (`mark16_grc/`) — a MOVE/SOURCE toggle can read the English `mark16/` and the Greek `mark16_grc/` side by side. Buildable now; no upstream acquisition needed.

## Keep / build
- [ ] KEEP the bracket idiom (PI likes it).
- [ ] Explain each shape edge (needs coder rationale — Method) — what "ring/parallel/leap" means + why these moves.
- [ ] Tag shape edges by layer (discourse vs verbal/sonic); show paraphrase-safe ones as solid, original-dependent ones as flagged. (Method coding + my render.)

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: Design SB 2026-08-14. PI's crit-walk reached viz_connect_shape.html; liked the bracket idiom, asked why the ring
  is coded + whether shape is visible on paraphrase. Captures the coded shape edges (no rationale field), the ring explanation,
  and the paraphrase-vs-original finding (discourse-shape survives, verbal/sonic shape needs the Greek) for Method/Atlas Reader.
SCHOLARLY SOURCES: connect_edges.json (SHAPE edges); viz_connect_shape.html (reads paraphrase); §2.8 bias-visibility;
  the SONIC/Plate view (why the original is kept). The ring-composition reading of Mark 16:1–8.
WHAT NEEDS VERIFICATION: (1) per-shape-edge rationale must be logged at coding time (Method). (2) layer-tag (discourse vs
  verbal/sonic) per shape edge — a coding-schema addition. (3) verbal/sonic shape should be coded from the Greek checkout, not paraphrase. -->
