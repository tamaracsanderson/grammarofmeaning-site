# Prevalence curve — crit log

**Figure:** `_staging/viz_morphospace_prevalence.html` · live: https://grammarofmeaning.org/_staging/viz_morphospace_prevalence.html
**PI reaction 2026-08-14:** "I don't know how to read this at all — not enough context about the numbers, chart, source." → a **visual-story** problem, not interaction. GPT concurs: research value 5/5, intuitiveness 1.5/5.

## The finding (should take 5 seconds, not paragraphs)
The corpus is **85% Abrahamic**. A tradition-separation score (silhouette) reads positive on the raw corpus (traditions *look* separated); cap every family to equal size and the score **drops through zero into interleave**. → the separation is **prevalence-sensitive**.

## Readability pass — SHIPPED 2026-08-14 (copy/label, my lane)
- [x] **Renamed around the question:** title + H1 → "What happens when we balance the corpus?" (was "why 'traditions separate' is an artifact…").
- [x] **Three-beat lede:** (1) problem — 85% Abrahamic · (2) test — the separation score + cap-to-equal · (3) finding — drops through zero → prevalence-sensitive. Silhouette explained in plain words ("does each passage sit closer to its own tradition than any other?").
- [x] **Softened "artifact" → "prevalence-sensitive"** (§2.8): one robustness check shows *sensitivity*, not proof of *pure artifact* — added the caveat that the stronger claim needs the full suite (resample bands, weight-vs-cap, metric/dimension sensitivity).
- [x] **"tradition-label silhouette"** + "near ≠ same doctrine" note (it's a repurposed cluster-validation metric fed tradition labels; don't imply MCA *discovered* these clusters).
- (already present) zero-line + region labels ↑ apparent separation / ↓ interleave; x-axis RAW → capped → balanced.

## Still owed for full V2 (needs data / Atlas Reader)
- [ ] **BEFORE→AFTER morphospace thumbnails** beside the curve (raw = ochre/Abrahamic-dense → balanced = colors mix). The single strongest add.
- [ ] **Corpus-composition strip** under the x-axis (85% dominant → equal) — show the manipulated variable.
- [ ] **Uncertainty band** from repeated stratified resamples at each cap (a single line falsely implies determinism; "across balanced resamples the effect consistently collapses" is stronger evidence). Needs the resample feed from Atlas Reader.
- [ ] **Reframe as a "CHECK / robustness" view** in the Atlas IA — not an equal-status visualization. Atlas: Landscape (archetypes) · Neighbors · Path · Mixing (aggregate) · **Check/Prevalence** (does the pattern survive imbalance?). Link from the Morphospace page: "Are these tradition regions real? Test prevalence bias →".
- [ ] Public view: collapse intermediate cap points → RAW · LESS-SKEWED · BALANCED (researcher mode keeps all).

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: Design SB 2026-08-14. PI couldn't read the prevalence curve; GPT diagnosed a visual-story problem + gave a 3-beat
  robustness-story redesign. Shipped the copy/label readability pass (rename to the question, 3-beat lede, plain-language
  silhouette, soften artifact→prevalence-sensitive per §2.8). The data-dependent V2 (thumbnails, composition strip, uncertainty
  band, CHECK-view reframe) is flagged for Atlas Reader / the build session.
SCHOLARLY SOURCES: viz_morphospace_prevalence.html; the prevalence feed; §2.8 bias-visibility (soften over-strong claims);
  silhouette = a cluster-validation metric here fed tradition labels (call it tradition-label silhouette). §2.16 render-from-data.
WHAT NEEDS VERIFICATION: (1) live render of the copy pass. (2) resample-band feed for the uncertainty layer (Atlas Reader).
  (3) whether the broader robustness suite warrants "inflates"/"artifact" language. -->
