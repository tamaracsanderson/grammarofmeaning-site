# Lovable brief v2 — "The Method Engine" bow-tie, REVISION crack (S161, 2026-08-07)

**For the PI to paste into the SAME Lovable project** (`method-engine-flow.lovable.app`). This is a **revision** of the
first crack — keep the geometry, cut the density, fix five ontology labels. Synthesizes reading-SB's reduction crit +
ChatGPT's 17-section crit + design-SB's crit + reading-SB's Gate-0 ontology rulings (all PI-approved). Produced by
design-SB; plan at `_staging/_tools/method_engine_crit_synthesis_and_plan_s161.md`.

---
═══════════════════════════════════════════════════════════════
PASTE-START — copy from here to PASTE-END into Lovable
═══════════════════════════════════════════════════════════════

# Revise "The Method Engine" — same bow-tie, far less ink

This revises the diagram you just built. **The bones are right — keep them:** the left→right bow-tie; the two parallel
input branches converging on a central waist; the distinction between outputs that bypass the waist and outputs that need
it; the two output bands ("the instrument speaking" vs "the tradition speaking"); and the Reading Room at the end.

**The one problem: it's trying to be three things at once** — an explanatory figure, an implementation map, and a live
audit dashboard — so every JSON field became visible ink and the topology got buried under cards, badges, sublines, and
crossing arcs. **Fix = change what earns a place in the overview.** The overview shows the *shape*; a click shows the
*detail*. Concretely:

## THE ACCEPTANCE TEST (the objective target — design to this, not to "smaller")
> At **1440 × 900 CSS px, browser zoom 100%**, the whole path **Text → Reading Room is visible with NO horizontal or
> vertical scroll**; all primary labels ≥ 13px. Target: figure body ~650–700px tall; waist ~150px wide; left cone ~28% of
> width · gutter ~12% · right fan ~42% · synthesis/end ~18%. Detail expands only on interaction (click → drawer). Browser
> zoom is never part of the intended reading.

## FIVE ONTOLOGY LABEL FIXES (small text changes, big accuracy gains)

1. **Rename the two edge types.** DIRECT → **WAIST-INDEPENDENT** (the output doesn't need the coded move); COMBINATION →
   **MOVE-CONDITIONED** (needs the coded move). More accurate: Sitz/Paradigm/Witness involve reconstruction (dating,
   grounding, transmission-distance), not raw text — "waist-independent" captures them all; only Constellation is literally
   raw-text.
2. **The waist is an ENRICHED MOVE RECORD, not just "coded move."** Draw it as: the move (produced by DECOMPOSE, which sets
   the boundaries) **with context attached** by SITUATE (which annotates, never segments). So the two branches are
   **"DECOMPOSE segments ∥ SITUATE annotates," meeting at the enriched move** — NOT "both produce it." Label the waist
   **"Enriched move — operation + arguments + attached context."** Make the waist the most visually dominant node (~1.4×
   the type size, strongest border): it is the hinge the whole instrument turns on.
3. **Frame is TEXT-level.** Reword its output from "the 8-axis stance *the move* takes" to **"where the text stands — the
   8-axis frame"** (it reads a text chunk, not moves). So Frame → Morphospace is a **waist-independent** output.
4. **Reception is GAP-DRIVEN — and this is the diagram's centerpiece.** The flow is **enriched move → a named GAP →
   retrieve real historical texts answering THAT gap.** Draw the mirror at the heart of the figure:
   ```
                         GAP  (a named interpretive question)
                         /                         \
              constructed GLOSS              retrieved RECEPTION
           (the instrument's built voices)   (the tradition's real voices)
                    grammar side                    canon side
   ```
   The point the reader must feel: same gap, two kinds of voice — **where they diverge is the finding.** Make this the most
   memorable moment in the diagram.
5. **Reading Room is the terminal DELIVERY surface, NOT "meta."** End the main flow AT the Reading Room (where the reader
   lands and reads). Move **"the instrument reads itself"** (the reflexive audit + provenance + vocab-version +
   SSOT-freshness) into a **thin strip floated below the whole diagram** — it is the method commenting on itself, off to
   the side, not a stage in the flow.

## THE REDUCTION (this is where the size goes)

- **~10 primary objects in the overview, not ~20 cards.** Reserve bordered CARDS for the structural spine only:
  **Text · Decompose · Situate · Enriched move · Reception · Synthesis · Reading Room.** Everything else = plain labels on
  a faint tinted band, NOT its own card.
- **Move ALL node detail into the click-drawer.** A default node shows only: **LABEL · a 3–6-word function gloss · one tiny
  status dot.** Everything else — layer lists (reader-gloss/persona-crit/gap-fill; Braid/Partiture; deductive/abductive),
  long badges, coverage notes ("Mark 16 = 55 moves"), "retired 7-axis," "0 rows," "analysis-only" — lives in the drawer.
- **Collapse the direct-output mirror-doubling.** Right now Sitz/Paradigm/Frame/Witness each appear twice (once in the
  Situate branch, again as a right-side output tile) with crossing arcs between. Don't. The Situate category IS its
  output — tag it "↳ rendered" in place. Remove the duplicate right-side boxes and the arcs they needed.
- **One bypass RAIL, not five arcs.** Replace the individual curves that skip the waist with **one thin "waist-independent"
  bus** that the waist-independent views tap off (think metro trunk / data bus). ~2 long curves total, not 5+ spaghetti.
- **One waist TRUNK → short fan branches.** From the waist, one strong fern trunk fans into short branches to the
  move-conditioned outputs — the literal **pinch (converge) → release (fan)** the "bow-tie" promises.
- **A compact 2-D output FIELD, not a vertical filing cabinet.** The tall single column makes the "fan" look like a *list*.
  Lay the outputs as small tiles (36–48px) in labeled rows so the fan looks like a fan:
  ```
      WAIST-INDEPENDENT   Sitz · Paradigm · Morphospace · Degrees · Constellation
      MOVE-CONDITIONED    Compare · Resituate · Tributary · Gloss · Gap-map · Cross-analysis
      RECEPTION (canon)   Reception
      SYNTHESIS           panel argument-graph · cross-output joins
  ```
- **Remove Fan from the overview** — it's retired; keep it in provenance/history only.
- **Compact header (~100–130px, not ~220–300):** small schema kicker + title + one-line "decompose + situate → shared
  move → recompositions" + the legend on one line. The figure starts almost immediately.

## TWO MODES (same JSON, a toggle) — because implementation ≠ validity

- **METHOD (default):** topology + names + one-line functions + tiny maturity dots. This is what a first-time reader sees.
- **AUDIT (toggle):** adds implementation status, coverage warnings, row-counts, known-limits, dependency metadata.
- Why: "live" = built + has data; a green dot must NOT read as "validated" to a scholarly reader. Keep operational status,
  but don't let it masquerade as epistemic confidence — hence the toggle.

## THE OVERVIEW OBJECTS (what each expands to, in its drawer)

| Overview object (card) | one-line function | drawer / expands to |
|---|---|---|
| **Text** | the passage as it arrives | source / passages |
| **Decompose** *(= the coding stage; "Grammar" = the move-grammar inside)* | segment into moves; find silences | Grammar (moves) · Detect-gaps · Seed-ranking · [known-limit: Mark-16-WEB has a lineage-only run — the multi-locus seer scan hasn't been pointed at it yet; the 7-locus × 6-subtype gap taxonomy is rich; run-coverage, not a taxonomy limit] |
| **Situate** | annotate each move in its world (never segments) | **Annotation grain:** Sitz · Paradigm = text-level (computed once, stamped onto every move); Lineage = move-level (cites a coded move); Frame/Witness attach per-move but render text/source-level outputs. None segments — only Decompose sets boundaries. **Output waist-dependency:** Sitz · Paradigm · Frame→Morphospace · Witness→Degrees = waist-independent; Lineage→Tributary = move-conditioned. Sitz/Paradigm are DB-rendered engine-0 (`source_grounding`), ~2 seed texts so far. |
| **Enriched move** *(the waist — dominant)* | the operation + arguments + attached context | Decompose segments ∥ Situate annotates → converge here; every move-conditioned output fans from here. Worked example: Mark 16 = 55 moves |
| **Waist-independent views** *(labels on a band; tap the bypass rail)* | outputs that don't need the move | Sitz view · Paradigm view · Morphospace (frame) · Degrees-of-separation (witness) · Constellation (sound; off raw text) |
| **Move-conditioned outputs** *(labels on a band; off the waist trunk)* | outputs that need the move | Compare (Braid · Partiture = SHOW·LOCATE·EXPLAIN) · Resituate (deductive · abductive) · Tributary (◄Lineage) · Gloss (reader · persona-crit · gap-fill; renders on a (stance × method) grid — cells PROPOSED) · Gap-map · Cross-analysis (JOINS — also feeds Synthesis; analysis-only, no export yet) |
| **Reception** *(canon band — "the tradition speaking")* | real retrieved texts answering the gap | gap-driven retrieval; the mirror of Gloss's built voices; ⚠ awaiting build (0 rows, S162+) |
| **Synthesis** | the argument across frames | per-gap panel colloquy / argument-graph (edges: AGREES·CONTESTS·REFRAMES·EXTENDS·CONCEPTUALLY-ENABLES·HISTORICALLY-DEVELOPS-FROM) + cross-output joins; ⚠ mostly spec, no store |
| **Reading Room** *(terminal delivery)* | the reader-facing surface | integrated reading (e.g. the gospels) + church/institution map |
| **Reflexive audit** *(thin strip BELOW the diagram, off the flow)* | the instrument on itself | recursive abductive run · provenance · vocab-version · SSOT-freshness |

## HOUSE STYLE (keep the tokens from the first crack)
Same warm botanical palette + Newsreader/Inter/IBM Plex Mono; light + dark. **Encode the two edge types REDUNDANTLY** (not
color-only, so it survives grayscale + is accessible): **waist-independent = thin + lighter + slight dash**;
**move-conditioned = thick + solid**. Use fewer large dashed group-outlines — a pale paper tint + a typographic band
heading is enough to mark a region. One tiny status dot per node in METHOD mode; richer status only in AUDIT.

## THE TEST TO DESIGN AGAINST (say this back to yourself)
> At first glance I see a bow-tie. At second glance I see why some paths bypass its waist. At third glance I understand
> what the instrument does. Only after clicking do I learn how each engine is implemented.

## WHAT I NEED BACK (so I can rebuild this as a STATIC site — no React runtime on our host)

1. **README / HANDOVER.md** — production direction; LOCKED vs BACKUP; key files; "do not change" rules; the INTERACTIONS
   note (drawer behavior, hover-to-highlight-a-path, METHOD/AUDIT toggle, mobile degradation).
2. **`method_flow.json`** — `nodes[]` + `edges[]`, content out of components. Node fields: `id · label · function (3–6 wd)
   · band · kind · status`; plus (even if not shown in METHOD mode) **`grain` (raw_text|source|passage|move|gap|
   cross_output|corpus) · `requires[]` · `produces[]`**, and **`implementation` (specified|built|populated|retired)
   separate from `validation` (untested|internally-tested|benchmarked|externally-reviewed)**. Edge fields: `from · to ·
   type (waist_independent | move_conditioned | flow) · note`.
3. **tokens file** — all colors/fonts/radii/effects in one place.
4. **React → static-HTML porting note + a static export** — what's React-specific and its plain-HTML/vanilla-JS
   equivalent; ideally a **self-contained HTML+CSS+JS build** (or the rendered HTML/SVG + extracted CSS) so I don't
   reverse-engineer JSX; and a list of runtime deps (CDN/fonts) to inline — our static host blocks external requests.
5. **Connector geometry note** — how the bypass rail, waist trunk, fan branches, and the gap-mirror fork are drawn:
   ideally **HTML/CSS-grid nodes + ONE absolute inline-SVG layer** whose `<path>`s are computed from anchor positions
   (`getBoundingClientRect` + `ResizeObserver`). **Do not use a graph-layout library** (Dagre/ELK/Cytoscape/force) — the
   topology is authored, not discovered. Give me the path-generation approach so I can reproduce it statically.

═══════════════════════════════════════════════════════════════
PASTE-END — stop copying here
═══════════════════════════════════════════════════════════════

<!--
HOW PRODUCED: design-SB S161 (2026-08-07). Revision brief for Lovable's 2nd crack, folding reading-SB's reduction crit +
ChatGPT's 17-section crit + design-SB's crit + reading-SB's Gate-0 ontology rulings (all 5, PI-approved). Frames the change
as a reduce-pass on the first crack's correct geometry. Sequenced per the approved plan (Gate 0 → this brief → PI pastes).
SOURCES: method_engine_crit_synthesis_and_plan_s161.md; CRT_method_schema_v2_vs_engine_reality_s161; reading-SB Gate-0
rulings (waist=enriched-move/segment-vs-annotate, edge rename, Frame text-level, Reception gap-driven, Reading-Room
terminal); ChatGPT crit; lovable_brief_method_engine_bowtie_s161.md (v1); CLAUDE.md §2.13/§2.16.
WHAT NEEDS VERIFICATION: whether Lovable hits the 1440x900 acceptance test in one crack; gloss-mode grid cell membership
still PROPOSED (pending CLC); design-SB then does the static rebuild (HTML grid + inline-SVG connectors) on receipt.
-->
