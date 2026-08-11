# Forward visualization roadmap (design-SB · S170 · 2026-08-11)

**What this is.** The prioritized build queue for the visualizations *beyond* what's shipped, produced by synthesizing everything already explored (the DRs, the reading-SB S161 design briefs, the connect/move-score reconciliations, the built figures) — so it's ready to prioritize the moment the Situate/MCA data lands. Per the PI's 3-axis framing: **additional ANALYSIS · additional MATERIALS · COMBOS**. Every item is flagged **🟢 buildable-now / 🟡 data-blocked (on-whom) / 🔵 cross-SB**.

> Design-SB is read-only on twelve-laws; all "on main" claims verified via `git show origin/main:<path>` on 2026-08-11.

---

## 0. Fact-check payoff — three corrections to the brief (verified on main)

The brief carried three assumptions that the source-of-record contradicts. Getting these right *moves items from blocked to near-term*:

1. **Greek SONIC is NOT a "needs-new-tooling / Method-SB" task — the tooling exists and has already RUN.** `scripts/analysis/greek_sonic_constellation_s161.py` builds a reconstructed-Koine→IPA layer (panphon) and computes the same 4 sonic-edge families as the English `constellation_v3_unified.py`. Both have been run: `pm/50_audits/VIZ_greek_sonic_mark16_grc_s161.html` + `VIZ_constellation_v3_unified_mark16_{kjv,web}_s161.html` are all on main. **The only gap is a tiny profile-JSON export** (the script writes an HTML viz + prints a `counts` dict; it doesn't emit a structured feed). So EN↔GRC **sonic** moves from *"blocked on tooling"* → *"near-term, needs a small export."*
2. **The Partiture v1 data is already on main.** `pm/40_architecture/DATA_partiture_mark16_v1_s161.json` — 4 lanes (Greek·Latin·KJV·WEB), 20 verse-moments, operation-tagged blocks, lane-level sonic profile, per-verse variance vector, glossa rich@16:6. It renders to design-SB's locked schema. So a **Partiture v1 render is buildable now** (it's been queued behind Night Gallery + the schema rebuild, not blocked). What's genuinely v2/blocked is the **move-level** block alignment (see §A).
3. **The media-source list is now precise** (PI handed the mock's `IMAGE-CREDITS.md` §Image APIs): MET is the only one *used*; ten more OA APIs are *available* (see §C). Item C's sourcing is de-risked.

---

## Axis 1 — with additional ANALYSIS (a new analysis unlocks a new viz)

| # | Viz | What it shows | Needs (analysis) | Flag |
|---|---|---|---|---|
| A1 | **EN↔GRC sonic profile compare** | What sound-work each language does (assonance/alliteration/consonance/rhyme density) — and that they *don't echo each other* (the §2.8 negative-space finding). Per-language profiles side-by-side, never cross-language edges. | Profile-JSON export from the two already-run runs (GRC + EN). Analysis DONE. | 🟡 → 🟢 (Method SB: tiny export) |
| A2 | **EN↔GRC SHAPE compare** | What form/structure translation drops or re-shapes (parallelism/ring/leap/juxtaposition), beyond lexis. | GRC SHAPE edges exist (Mark-16-GRC connect run = **79 edges**) but aren't in the deploy feed. | 🟡 (Method SB: export GRC edges) |
| A3 | **Gap-shape audit strip** | Whether the gap-grammar's silences are *shaped* or monotone. reading-SB's ⚑: gap-grammar is currently monotone ("is X on source Y?") and missed M23 (the women's silence, the Markan crux). | A gap-typing pass on the GRAMMAR band. | 🟡 (reading-SB) |
| A4 | **Degrees-of-separation (witness)** | Proximity-is-not-fullness: how far each witness sits from the event, as *ranges* not bare ints, with epistemic asymmetry (isnad/stemma) made visually unavoidable. | `DATA_witness_transmission_v2_s161.json` is **on main** (IRR231-corrected). | 🟢 (render the S161 brief) |
| A5 | **Cross-tradition RESONANCE at scale** | MATCH/ANALOGY/COUNTERS/INVERTS across traditions (A:B::C:D rhymes) — no contact claim. | Only 1 worked RESONANCE edge (Mark↔Daodejing) exists today; needs the resonance run at scale + export. | 🟡 (Method SB) |

## Axis 2 — with additional MATERIALS (new sources unlock a new viz)

| # | Viz | What it shows | Needs (material) | Flag |
|---|---|---|---|---|
| M1 | **Reception (real retrieved texts)** | What was *actually* received — real provenance-labelled texts beside the generated frames (the generated-vs-real pairing is itself thesis content). | Reception export, gated on the Librarian's Acquire-SB chunk-index. | 🟡 (Librarian) |
| M2 | **Lineage / tributary (by MOVE)** | How sources flow *into* the text — source-family × MOVE matrix, one fixed watershed trunk per family, **absences as hollow nodes** (moves with no coded upstream = negative space at move scale). | `DATA_lineage_matrix` + source-family map + 2 metrics (data mostly move-keyed already). | 🟡 (reading-SB data ready-ish) |
| M3 | **Multi-tradition morphospace / atlas** | The frame-coordinate cloud across traditions (8-axis MCA). | Librarian 8-axis MCA export + the honest-status contract (see §STALE-VOCAB thread — coordinate with atlas-SB 🔥). | 🔵 (Librarian/atlas-SB) |
| M4 | **Other-language runs (beyond GRC)** | Latin/Syriac/etc. sonic+shape, extending the translation-change finding. | New connect + sonic runs per language. | 🟡 (Method SB) |
| M5 | **More seed texts across the corpus** | The reading room beyond Mark 16 / Romans 8 (the ~2-seed coverage today). | Coding coverage on more curated seeds. | 🟡 (reading-SB coding) |

## Axis 3 — COMBOS (combine existing engines into a composite view)

| # | Viz | What it shows | Combines | Flag |
|---|---|---|---|---|
| C1 | **THE READING SEQUENCE** (headline — §RS below) | move score → situate → gaps → gloss → reception, as one progressive-disclosure flow; the gloss-vs-reception *divergence* is the finding. | all engines | 🟢 design now / 🟡 live-wire (Situate/Gaps/Gloss/Reception feeds) |
| C2 | **JOINS: Variance × Lineage** | Where translation-variance and source-lineage co-occur (load-bearing first-class family per the 08-05 lock). | Compare × Lineage | 🟡 (needs both exports) |
| C3 | **sonic × move** | Which moves carry the sound-work (sonic score as a heat-strip *under* the move spine). | Constellation × Move Score | 🟡 (per-block sonic = partiture v2) |
| C4 | **move × frame** | How frame-coordinate shifts track the move sequence (the ribbon already lives in the reading). | Frame × Move Score | 🟢 (largely shipped in reading.html) |
| C5 | **Move Score → Connect tie** | "this move has N connections · follow →" jumps into Connect Trace at that move. | Move Score × Connect | 🟢 (WORK-QUEUE [1]) |

---

## RS — The READING SEQUENCE (the headline the PI wants designed)

**The claim.** Not five figures — one *reading flow* that deepens a single passage layer by layer, in the lectio rhythm (**draw → linger → respond → reflect**). The design problem the PI named: *show all of this without overload.* The answer is **progressive disclosure** — each layer is opt-in, the reader is never shown everything at once, and the passage stays on screen throughout as the spine.

### The five layers (one passage, deepening)

```
  ┌─ THE TEXT (always present — the spine) ─────────────────────────┐
  │  Mark 16:1–8, verse by verse                                    │
  └────────────────────────────────────────────────────────────────┘
     ▼ draw
  1. MOVE SCORE      what the text DOES, move by move (the grammar)
     ▼ linger                        · already built (viz_move_score)
  2. SITUATE         the added context: sitz · paradigm · frame · lineage · witness
     ▼                                · "why this move, here, then"
  3. GAPS            the top questions the text raises but doesn't answer
     ▼ respond                        · the silences (LACUNA), move-anchored
  4. GLOSS           the responses that could-have-been — our agents' frames
     ▼ reflect                        · what *a* reader (Augustine-frame, etc.) would say
  5. RECEPTION       what was ACTUALLY received — real provenance-labelled texts
  ────────────────────────────────────────────────────────────────────
     ✦ THE FINDING = the DIVERGENCE between 4 and 5
       (what could-have-been-said vs what history did say)
```

### The design mechanics (how it avoids overload)

- **One layer visible at a time; the reader chooses depth.** A left-margin "depth rail" (1→5) with the current layer lit; scrolling or clicking the next affordance reveals the next layer *in place*, beneath the same verse — not a new page, not everything stacked.
- **The text never leaves.** Every layer renders *against* the verse it belongs to (move-anchored, per-clause where we have spans). Situate/Gaps/Gloss attach to specific moves, not the whole chapter — so the reader is always reading, never studying a dashboard.
- **Layers 1–2 are "linger" (what IS); layers 3–5 are "respond/reflect" (what it opens).** The lectio break sits between Situate and Gaps: first you receive the text + its context, *then* you're invited into its questions.
- **The gap between 4 and 5 is the payoff, and it's designed as a explicit facing-pair.** Gloss (left: "a reader *could* have said…") beside Reception (right: "history *did* say…"). Where the generated frame is a high thinker-fit but the real passage-fit is indirect (GPT's generated-Calvin finding), *that visible gap is the thesis content* — surface it, don't smooth it.
- **Progressive across passages too.** The same rail works on any coded seed; on a thin seed (no Reception yet) layer 5 shows an honest "not yet retrieved" state rather than a blank — render-from-data honesty (§2.16).

### Build status of the sequence

| Layer | Design | Live data on main? |
|---|---|---|
| Text (spine) | ✅ shipped (reading.html) | ✅ |
| 1 Move Score | ✅ shipped | ✅ WEB (55 moves; regen 55→60 owed) |
| 2 Situate | designable now | 🟡 partial (sitz/paradigm ~2-seed via source_grounding; frame ribbon live; witness data on main) |
| 3 Gaps | designable now | 🟡 LACUNA gap-map live (bibliographic); move-anchored gaps owed |
| 4 Gloss | designable now | 🟡 move_gloss live (reader-gloss); persona-frame "could-have-been" owed |
| 5 Reception | designable now | 🟡 blocked on Librarian Reception export |

**So: the whole sequence is designable NOW (mock against the shape); the live wiring fills in layer-by-layer as the Situate/Gaps/Gloss/Reception feeds land.** This is the right thing to mock next after the roadmap, because it's the frame every other output plugs into — it turns the scattered engines into one reading.

---

## A. The Partiture (translation) — buildable now?

**Verified.** `DATA_partiture_mark16_v1_s161.json` **is on main**, to design-SB's locked schema: `moments` (20 verses) × 4 `lanes` (greek/latin/kjv/web) × operation-tagged `blocks`, `variance` vector per moment, `links` (verse-level fan, typed by count-change), `glossa` rich@16:6 / thin elsewhere. Its own `_v1_scope` states the honest boundary:

- **moments = verses** (semantic-moment sub-alignment is v2)
- **sonic = lane-level whole-chapter profile** (per-block sonic is v2)
- **links = VERSE-level fan** (**move-level block alignment is v2**)

**Answer:** a **Partiture v1 hero is buildable now** — 4 lanes over the shared verse spine, operation-coloured blocks, lane-level sonic texture, a variance seismograph margin, glossa-on-hover gated by variance/confidence. This is the L1-heatmap + a real v1 partiture, not a mock. **What genuinely waits on reading-SB** is the **L2 move-level alignment** (which GRC move ↔ which EN move → braiding ribbons at move granularity) — that's the `_v1_scope` "move-level block alignment is v2." Design render-craft flags from the S161 brief hold: **stacked parallel lanes** (not descent-ribbons — ribbons imply genealogy), **colour = kind-of-change** (not version; version = lane position). Fable's mockup is the visual target; DR adopt-map says partiture = **BUILD** (CollateX align + D3).

**Flag:** 🟢 v1 render now (data on main) · 🟡 L2 move-alignment on reading-SB.

## B. Greek sonic + shape — the EN↔GRC comparison "beyond words"

**Corrected (see §0).** The Greek-sonic *analysis is done* — reconstructed-Koine IPA via panphon, same 4 edge-families as English, already run on Mark-16-GRC. The honest method (from the script itself): **run per-language, compare the PROFILES, never cross-language** — sound is language-bound; Koine assonance has no English echo and English builds its own. So the viz is two profile fields side-by-side + a delta, and *the finding is the non-overlap* (§2.8).

- **EN↔GRC SONIC (A1):** 🟡→🟢. Needs only a small profile-JSON export from the two existing runs (Method SB) — *not* new tooling.
- **EN↔GRC SHAPE (A2):** 🟡. GRC SHAPE edges exist (79-edge GRC connect run) but aren't in the deploy feed — needs the GRC edge export (Method SB), same ask as Connect P3's EN↔GRC comparison.

The FINDING both unlock — *what translation drops/re-shapes structurally, not just lexically* — is the negative-space payoff and is thesis-gold. **Consolidated ask to Method SB:** one export bundle = GRC connect edges (79) + GRC & EN sonic profile JSON + the worked RESONANCE edge. That single export unblocks A1, A2, A5-seed, and Connect P3 at once.

## C. Multi-media gallery-picker (per passage + Situate) — cross-SB

**Sources now precise** (PI handed `IMAGE-CREDITS.md` §Image APIs):

- **Used in the mock:** MET Collection API (`collectionapi.metmuseum.org`) + MET image CDN (`images.metmuseum.org`) — CC0.
- **Available (could-use), each CC0/PD with docs in the credits file:** Art Institute of Chicago · Harvard Art Museums (key) · Cleveland Museum of Art OA · Smithsonian OA · Rijksmuseum (key) · Europeana · Wikimedia Commons/Wikidata · British Museum · V&A · Cooper Hewitt (key).

**The design.** A per-passage picker that surfaces *candidate* images the PI selects + places (the Night Gallery `gospels_room_config.json` = 34 candidate plates w/ credit + crop is the working precedent). **PI's elevation:** drive the query from **Situate, not just the scripture** — paradigm · location · time-period (Mark 16 → 1st-c. Jerusalem · empty-tomb tradition · corpse-care/anointing paradigm → candidate period tombs / anointing scenes / the place), so media is grounded in the *Sitz*. Provenance §2.4 per entry (`{url, credit, alt, crop}` = caption + PD-source record).

**Ownership (seam):** Librarian owns media **sourcing** (library holdings + OA-API acquisition + the Situate-driven queries — their acquisition lane; they hold the MET architecture). **design-SB builds the picker UI.** → **Flag to the Librarian.**

**Flag:** 🔵 cross-SB · 🟢 picker-shell now (over existing gospels_room_config candidates) · 🟡 Situate-driven query needs Situate data + a Librarian acquisition query.

## D. Reconsider Connect → per-kind SEPARATE views

**PI correction.** Overlaying all 5 `edge_kind`s on one graph is too many lines (78 now; worse when LINEAGE/RESONANCE/SONIC populate). Default Connect to **one-kind-at-a-time** — a clean **Logic** view · **Shape** view · **Sonic** view (per Trace/Scan/Map form) — with compare/combine as the *option*, not the default. This **promotes the drill-down filter from a filter to the primary mode** (reconciliation #5 → per-kind-primary), because Connect is for reading *structure* (edge-tracking), a different reading than the Move Score's move-by-move spine. Buildable now (taxonomy + filter already exist; it's a default-mode + nav change).

**Flag:** 🟢 buildable now, but **gated on 3DR-19** — the per-kind-viz query is PASTE-READY at `_staging/connect_perkind_viz_3DR-19_query_2026-08-11.md`; PI runs GPT/Fable/Gemini-DR → responses land as `3DR19_{gpt,fable,DR}.txt` at the twelve-laws root → design-SB reconciles → per-kind viz spec finalizes the build. **Status 2026-08-11: not yet run** (root has 3DR17 + 3DR18 only).

---

## Consolidated priority queue (the ready-to-prioritize output)

**Buildable now (🟢) — no new data:**
1. **The Reading Sequence mock** (RS/C1) — the frame everything plugs into; design now, live-wire as feeds land. *Surface to PI.*
2. **Partiture v1 hero** (A) — data on main; render to the locked schema.
3. **Move Score → Connect tie** (C5) — WORK-QUEUE [1].
4. **Per-kind Connect default-mode** (D) — *after 3DR-19 reconciles.*
5. **Degrees-of-separation / witness** (A4) — `DATA_witness_transmission_v2` on main; render the S161 brief.

**Near-term (🟡, small export) — one Method-SB bundle unblocks four:**
6. **GRC bundle** = GRC connect edges (79) + GRC&EN sonic profile JSON + worked RESONANCE edge → unblocks EN↔GRC sonic (A1) + EN↔GRC shape (A2) + Connect P3 + first RESONANCE example (A5-seed).

**Data-blocked (🟡) — on named owners:**
7. Lineage/tributary by move (M2) — reading-SB.
8. Reception real-texts (M1) — Librarian (Acquire-SB chunk-index).
9. Partiture L2 move-alignment (A/v2) — reading-SB.
10. Gap-shape audit (A3) — reading-SB.
11. JOINS Variance×Lineage (C2) — both exports.
12. RESONANCE-at-scale (A5) — Method SB.

**Cross-SB (🔵):**
13. Media gallery-picker (C) — Librarian sources / design-SB builds. *Flag to Librarian.*
14. Multi-tradition morphospace (M3) — Librarian/atlas-SB (coordinate honest-status with 🔥).

**DR adopt-vs-build map (from `research/10_dr/viz_methods_reconciliation_2026-08-06`):** partiture = **BUILD** (CollateX + D3); seismograph = **ADOPT** (horizon/ridgeline); lineage = **ADOPT** (d3-sankey). Note: "adopt d3-sankey" = vendoring a JS lib into the static site — decide inline-vendor vs hand-roll per §2.16 (CSP: self-contained, no CDN).

## Surface to the PI (two items, per the brief)
1. **The Reading Sequence design** (§RS) — the progressive-disclosure flow + the gloss-vs-reception divergence as the finding. Is the depth-rail / one-layer-at-a-time / facing-pair-at-the-gap the right shape before I mock it?
2. **Partiture-now** — v1 data is on main; I can render the v1 hero now (verse-level, 4 lanes). Build it now, or hold behind the method-schema rebuild? (L2 move-alignment stays a reading-SB dependency either way.)

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: design-SB (S170, 2026-08-11), WORK-QUEUE item [0] per _staging/viz_roadmap_brief_2026-08-11.md + PI directive.
  Synthesized from: the DRs (research/10_dr/ viz_methods + translation_change reconciliations, the 3DRs), the reading-SB S161
  DESIGN_BRIEFs (witness/lineage/sonic/partiture), the connect_v2 + move_score reconciliations, the built figures, and
  direct verification on twelve-laws origin/main (partiture data, greek_sonic script + VIZ outputs, GRC ls-tree, mock IMAGE-CREDITS).
  §2.15 (diverge→converge — this is the converge/roadmap), §2.16 (render-from-data; every item flagged data-blocked honestly),
  §2.8 (EN↔GRC non-overlap = negative-space finding), §2.9 (synthesize discovered inventory rather than let the DRs rot).
SCHOLARLY SOURCES: DATA_partiture_mark16_v1_s161.json; greek_sonic_constellation_s161.py (reconstructed Koine/panphon);
  constellation_v3_unified.py; VIZ_greek_sonic_mark16_grc_s161.html + VIZ_constellation_v3_unified_mark16_{kjv,web}; the
  connect edge_grammar_v1 drawer (5 edge_kinds); IMAGE-CREDITS.md §Image APIs (MET used; 10 OA APIs available).
WHAT NEEDS VERIFICATION: (1) exact contents of the owed Method-SB GRC/sonic export bundle (item 6) — confirm the profile-JSON
  shape with Method SB. (2) whether reading-SB's move-level alignment (partiture L2) is in progress. (3) the live-wire feed
  paths for the Reading Sequence layers 3–5 (Gaps/Gloss/Reception) as they land. (4) 3DR-19 responses (not yet run at authoring). -->
