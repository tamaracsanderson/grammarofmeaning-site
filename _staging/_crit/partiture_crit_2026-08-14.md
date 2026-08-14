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

## Q4 — real, open, off-the-shelf tools (verify embeddability — browser was blocked at write time)
- **Alpheios** (alpheios.net, open-source) — click a Greek OR Latin word → morphology + lexicon (LSJ for Greek, Lewis & Short for Latin). Closest to "click a word, unpack it." Embeddable as a reading tool.
- **Scaife Viewer** (scaife.perseus.org, `scaife-viewer` on GitHub, open-source) — Perseus reader; Greek + Latin with word-level lexicon/morphology links. Forkable.
- **STEP Bible** (stepbible.org, Tyndale House, free) — interlinear Greek/Hebrew ↔ English + Strong's; the interlinear/click-highlight is native.
- **Alignment DATA for the click-highlight** (open): MACULA Greek, Nestle 1904 + Strong's, Berean interlinear — word-level Greek↔English alignment you can build the Pudding-"Plain" highlight on directly. (Greek↔English is the tractable core; Latin/KJV/WEB 4-way alignment is harder — needs per-pair alignment.)
- **Etymology/lexicon sources** (open): LSJ (Greek), Lewis & Short (Latin), Strong's — all in Perseus/STEP data.

**Recommendation:** build the parallel reader on **open interlinear/alignment data** (STEP/MACULA/Nestle1904+Strong's) for the click-word-highlight + lexicon, and consider **embedding/forking Alpheios or Scaife** for the Greek/Latin morphology-on-click rather than building a morphology engine. Reader view first (4-up + click-highlight + lexicon); variance chart stays as the research sibling.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: Design SB 2026-08-14. PI couldn't read the Partiture variance chart + asked what the bars/variance mean, for a
  4-up translation reader with click-word-highlight (Pudding "Plain"), off-the-shelf tools, and etymology. Captures the read-
  confusion, the redirect to a reader-facing parallel reader, and real open tools (Alpheios/Scaife/STEP/MACULA/LSJ/Lewis-Short).
SCHOLARLY SOURCES: viz_partiture.html (variance/segmentation chart, reads Greek SBLGNT + Latin Vulgate + KJV + WEB); Pudding
  "Plain" (pudding.cool/2022/02/plain/); Alpheios / Scaife-Perseus / STEP Bible / MACULA / Nestle1904+Strong's (open tools + data).
WHAT NEEDS VERIFICATION: (1) embeddability/licensing of Alpheios/Scaife/STEP (browser blocked at write — verify live). (2) which
  alignment dataset covers Greek↔English cleanly for Mark 16. (3) 4-way (Gk/La/KJV/WEB) word alignment is the hard part — scope
  the reader view to Greek↔English click-highlight first, add Latin/KJV as parallel columns without full word-alignment initially. -->
