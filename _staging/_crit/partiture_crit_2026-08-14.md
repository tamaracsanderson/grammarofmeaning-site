# Partiture — crit log (the translation comparison)

**Figure:** `_staging/viz_partiture.html` · live: https://grammarofmeaning.org/_staging/viz_partiture.html
**PI reaction 2026-08-14:** "I want to like this, but I don't think I know how to read it." → the abstract variance chart doesn't teach itself; the PI wants a **reader-centered translation experience**.

## What it currently shows (needs explaining IN the figure)
- **The little bars per cell = SEGMENTATION BLOCKS** — how many units that translation cuts the verse into (Greek 16:8 = 8 blocks, Latin 4, KJV 4, WEB 2). "Same scene, different segmentation."
- **The top VARIANCE bar = cross-translation *disagreement* on segmentation** per verse. 16:8 = variance 1.00 (a hotspot — the four translations carve it very differently); low bars = they agree. Neither is labeled clearly enough → the reader can't decode it.

## PI's 5 questions → the answers + the redirect
1. **What do the bars mean?** → segmentation blocks (above). Must be said on the figure.
2. **What does variance mean?** → how much the 4 translations *disagree on how to cut the verse*. High = a translation hotspot. Must be said.
3. **⭐ Wants all 4 translations TOGETHER + click-a-word → see it highlighted across the others** (ref: Pudding "Plain" — pudding.cool/2022/02/plain/). This is a **word-alignment parallel reader**, not an abstract chart. This is the real ask.
4. **Off-the-shelf / API / git for unpacking Greek vs Latin vs Old-English vs WEB?** → yes, real + open (see below).
5. **⭐ More etymology** — what a word means in Greek vs Latin, how translation decisions shift meaning. The lexicon/morphology layer.

## The redirect: Partiture V2 = a reader-facing parallel reader (not a variance dashboard)
The variance chart is a *research* view (where do translations diverge structurally). What the PI wants is the *reader* view: **4 translations side by side, click an English word → it highlights across Greek/Latin/KJV/WEB, with lexicon + etymology on click** (how the Greek/Latin word means, how the translation choice shifts sense). This is her "experience Greek vs Latin vs Old English vs WEB" + on-telos with interactive lectio divina. Keep the variance chart as the *research* sibling; build the parallel reader as the *reader* one.

## Round 2 — GPT crit (2026-08-14): demote the Partiture to a MINIMAP; the four texts are the experience
Verdict: keep the Partiture but **demote it from "the translation experience" to "the overview/minimap of translation divergence."** Intuitiveness 2→5 once the four actual texts are the primary object. Connection-to-translation 1.5/5 now.
- **"One stripe = one coded move"** (from DECOMPOSE), not word-density — must be taught. 16:8 = Greek 8 · Latin 4 · KJV 4 · WEB 2 moves.
- **"Variance" is too opaque** — rename to **"segmentation difference"** (or split: segmentation / wording / sound). Don't collapse several measures into one mystery number.
- **Reverse the order:** reader asks "what changed in the WORDS?" first → then "did it change shape/moves/sound/meaning?" Begin with **"One scene, four versions"** showing all four aligned; the Partiture becomes the bird's-eye map of *where to look*.
- **Hero interaction = click-a-word → highlight aligned phrase(s) across all versions** (Pudding "Plain"); handle 1→1, 1→many, many→1, reorder, omission (alignment itself is the finding).
- **Word inspector:** FORM → LEMMA → MORPHOLOGY → RANGE → HERE (contextual sense) → each version's CHOICE → **what the choice changes** (voice/aspect/agency/register/ambiguity). Call it "word history & range," not just etymology.
- **Translation taxonomy** a selected phrase can carry: EXPANDS · COMPRESSES · REORDERS · EXPLICITATES · OMITS · SHIFTS-SENSE/GRAMMAR/REGISTER/SOUND.
- **Toggle WORDS · MOVES · SOUND** (three phenomena currently mixed). Keep the seismograph bars as **navigation** (sparkline → hotspots 16:6/16:8 → click opens the four-text reader), not the finding.
- **Methodology warnings:** "more moves ≠ more meaning" (label "segmented into 8 moves", not "high granularity" — readers read stripe-count normatively); "one textual scene, four renderings", not "same events".
- **The distinctive contribution** (nobody else has it): connecting a translation choice to **what happens to the meaning-making OPERATION** — the lexical/morphology infrastructure is all off-the-shelf; the move-consequence layer is ours.

## Q4 — CONFIRMED off-the-shelf tools (GPT verified with links, 2026-08-14; still confirm licensing before committing)
- **⭐ Alpheios Embedded (`alpheios-project/embed-lib`)** — clickable Ancient Greek/Latin → morphology + short definitions + grammar; its embedded lib **already highlights aligned words/phrases across translations (incl. 1→many) on hover, pin on click** — i.e. the exact interaction the PI described, almost verbatim. CDN or npm. **GPT's #1 UI shortcut** — put it under the Greek/Latin lanes rather than rebuilding lexical popovers.
- **Alpheios Alignment Editor (`alpheios-project/alignment-editor-new`)** — build/fix word-by-word alignments across texts, JSON/HTML out.
- **⭐ Clear Bible Alignments (`Clear-Bible/Alignments`)** — pre-existing Bible word alignments (auto + manually corrected); **data CC BY 4.0, code MIT**. First place to look before generating our own.
- **MACULA Greek (`Clear-Bible/macula-greek`)** — word-level morphology, lemmas, English glosses, word senses, semantic roles; trees + TSV. Backend for "click Greek word → what's it doing."
- **STEPBible-Data (`STEPBible/STEPBible-Data`)** — open Greek datasets, morphology, lexical tagging, context-sensitive translations, LSJ material (CC BY 4.0). For semantic range / lexicon / contextual gloss.
- **PROIEL / Syntacticus** — morphosyntactic Greek + Latin (incl. NT) for Greek↔Vulgate **grammatical** comparison.
- Scaife/Perseus (UX reference) · CollateX (same-language variant collation) · API.Bible (many modern translations, later).

**Recommended stack (GPT, modest — not machine-translation-first):** texts we control (Gk/Vulgate/KJV/WEB) + **Clear Bible alignments** (auto + manual-correct the hotspot verses via Alpheios editor) + **MACULA + STEPBible** lexical layer + a custom React 4-lane reader with **Alpheios embedded** lookup/alignment. MT (Google/DeepL) is a different research object — use language tech only for alignment/lemmatization/morphology/lexical retrieval; keep the *meaning-consequence* analysis ours. Reader view first (4-up + click-highlight + word inspector); the variance chart demotes to the navigational minimap.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: Design SB 2026-08-14. PI couldn't read the Partiture variance chart + asked what the bars/variance mean, for a
  4-up translation reader with click-word-highlight (Pudding "Plain"), off-the-shelf tools, and etymology. Captures the read-
  confusion, the redirect to a reader-facing parallel reader, and real open tools (Alpheios/Scaife/STEP/MACULA/LSJ/Lewis-Short).
SCHOLARLY SOURCES: viz_partiture.html (variance/segmentation chart, reads Greek SBLGNT + Latin Vulgate + KJV + WEB); Pudding
  "Plain" (pudding.cool/2022/02/plain/); Alpheios / Scaife-Perseus / STEP Bible / MACULA / Nestle1904+Strong's (open tools + data).
WHAT NEEDS VERIFICATION: (1) embeddability/licensing of Alpheios/Scaife/STEP (browser blocked at write — verify live). (2) which
  alignment dataset covers Greek↔English cleanly for Mark 16. (3) 4-way (Gk/La/KJV/WEB) word alignment is the hard part — scope
  the reader view to Greek↔English click-highlight first, add Latin/KJV as parallel columns without full word-alignment initially. -->
