# Design Crit — Method-Engine Bow-Tie Schema (COMPLETENESS + FIDELITY CRT)

**Artifact:** `https://grammarofmeaning.org/engine/method-engine.html` (new bow-tie schema)
**Cross-checked against:** live flagship `method-schema.html` · built `reading-room-preview/` · FINAL 11-stage spec (`MASTER_gap_gloss_engine_FINAL_spec_s161`) · `method_flow.json`
**Reviewers:** 8 personas · **Mode:** staged review, no deploy · **Date:** 2026-08-07

---

## 1. Scores

| Persona | Score (/5) |
|---|---|
| Lamberth (HDS, philosophy of religion) | 4 |
| Saquib (MIT Media Lab, knowledge-graph eng.) | 3 |
| IDEO senior designer | 3 |
| Lidwell (Universal Principles of Design) | 3 |
| HDS MDiv peer (non-engineer) | 3 |
| Lay readers (the "mom test") | 3 |
| Web/UX designer | 3 |
| Info/comms designer (Tufte school) | 3 |

**Mean: 3.13 · Range: 3–4.**

**Who it is currently built for:** an *initiated reader who reads the lede/legend* — someone who already holds the domain (the theologically-literate peer found the human-named nodes land: Sitz, Reception, Gloss, the gap-mirror) or who reads the caption before the canvas. It is **not yet built** for a cold first-timer or a defense committee: every reviewer reports the bow-tie silhouette and the gap-mirror read, but the panel/chairs machinery that the spec calls "the finding" is invisible, so a viewer trusting the diagram alone will confidently misread what the instrument does.

---

## 2. Loved (keep) — praised by 3+ reviewers

- **The bow-tie silhouette is honest, not decorative** — a genuine pinch-and-release (left decompose∥situate cone → dark waist → right fan). *(Lamberth, Saquib, IDEO, Lidwell, parents, web, infoviz — 7)*
- **The Gloss/Reception gap mirror is the strongest, most memorable idea** — "the instrument's built voices vs the tradition's real voices," explainable at dinner and the truest third-glance story. *(all 8)*
- **Color restraint is correct: color ONLY the mirror pair** — reserve hue for the one sharpest semantic contrast; keep everything else neutral. *(Saquib, IDEO, Lidwell, HDS, parents, infoviz — with web's caveat that it isn't yet fully implemented; ~7)*
- **The dark waist earns dominance by VALUE, not hue** — weighting the hinge by darkness+size instead of a third color is the right instinct. *(IDEO, Lidwell, HDS, parents, web, infoviz — 6)*
- **Honesty badges + METHOD/AUDIT toggle** separate implementation-maturity from methodological validity, so "built" doesn't masquerade as "validated." *(Lamberth, Saquib, Lidwell, HDS, parents, web, infoviz — 7)*
- **Most FINAL-spec outputs DO map to a home** — S1 8-loci → Gap findings; S9 six colloquy edges → Synthesis; Fan retired; duplicate Sitz/Paradigm tiles already reduced. *(Lamberth, Saquib, HDS, parents, web, infoviz — 6)*

---

## 3. Convergent fixes

### UNANIMOUS (≥6 of 8)

**U1 — ORPHAN, most severe: the panel/chairs apparatus has no home.** S3 nominate (42 agents → `panel_nomination`) + S4/S8 two-chair **CONVERGENCE vs DIVERGENCE** select (`chair_selection`, whose **symmetric-difference the spec names "the finding"**) render as zero pixels — three DB tables between Gap and Gloss/Synthesis. The diagram jumps Selected-gap → {Gloss|Reception} → Synthesis with "the panel is the invention" erased; it looks complete while hiding its thesis-step. *Flagged by all 8.*
→ **Fix:** give the panel a visible home — a node/subgraph or rich drawer on the Selected-gap→Synthesis path ("Panel: nominate 42 → 2 chairs (converge | diverge) → pick-top"), and surface the symmetric-difference AS a first-class finding.

**U2 — ORPHAN: the S6 fidelity gate has no home.** `gloss_fidelity` ("no-grounded-gloss is an allowable verdict") is drawn as a plain flow arrow; the diagram implies every gloss survives to Synthesis. For a thesis whose AUDIT mode argues implementation≠validity, an honesty gate that can return null is the most defense-relevant node — and it's missing. *Flagged by all 8.*
→ **Fix:** a gate glyph on the Gloss→Synthesis edge carrying the allowable-null verdict.

**U3 — ORPHAN: `move_gloss` (per-move running gloss) is unrepresented and conflated with gap-fill Gloss.** The spec KEEPS it DISTINCT (§5); the diagram's single "Gloss" word silently absorbs it. *Flagged by all 8.*
→ **Fix:** home `move_gloss` as a Decompose / Enriched-move drawer layer, explicitly distinct-named from the gap-fill Gloss node.

**U4 — CONFLATION: "lineage" (and "cross-source") wear 3–4 hats with no signal they differ.** Lineage = a Situate leaf (→Tributary), a gap-locus inside Gap findings, AND a Cross-analysis join dimension; "cross-source" (a gap-locus) near-collides with "Cross-analysis" (an output). One token, multiple grains — reads as a duplication bug, not a deliberate two-views-of-one-dimension. *Flagged by all 8.*
→ **Fix:** role-qualified labels or a shared icon linking the appearances; mark loci as pointers ("lineage ↗ / cross-source ↗") to the leaf/output rather than independent things.

**U5 — FIDELITY CONTRADICTION: "Fan" is retired here but LIVE in the built reading room** ("The fan — Mark's abrupt ending and its alternative worlds"). The SSOT schema and the shipped surface disagree. *Flagged by Lamberth, Saquib, IDEO, Lidwell, parents, web — 6.*
→ **Fix:** either relabel the reading-room item as Resituate-abductive, or un-retire Fan — pick one before either page ships; if genuinely retired, don't draw it at all.

**U6 — COLOR: do NOT give the Enriched move a third hue.** Keep it dark/tonal-dominant (value contrast); a third hue dilutes the two-color mirror signal. *Flagged by Saquib, IDEO, Lidwell, HDS, parents, infoviz — 6 (web concurs on keeping it dominant, via fill/accent not just border).*
→ **Fix:** lock the waist as neutral-but-dark; reserve the only two hues for the mirror.

**U7 — COLOR: bind the two colors to meaning with a legend/label at the fork.** With only 2 of 24 nodes colored, an unlabeled pair reads as arbitrary highlighting instead of the built-vs-retrieved mirror it is. *Flagged by Saquib, IDEO, Lidwell, HDS, parents, infoviz (web via fix) — ~7.*
→ **Fix:** a 2-word self-explaining legend at the mirror ("built" under Gloss, "retrieved" under Reception) — not only in the far legend.

**U8 — COMPREHENSIBILITY: "waist-independent / move-conditioned" is opaque jargon carrying the load-bearing 2nd-glance distinction.** A viewer cannot intuit these mean "reads the text directly / needs the coded move" — the deepest methodological point is behind the most opaque labels. *Flagged by all 8 (every persona lists both terms as opaque).*
→ **Fix:** plain-language gloss on the band headings; also inline-define "move" and "enriched move" (never defined on the canvas).

### MAJORITY (4–5 of 8)

**M1 — Missing selection edge Gap-findings (`gap_map`) → Selected gap (`gap`).** The JSON draws `enriched_move → gap` directly but no `gap_map → gap` edge, so "the gap is chosen FROM the 8-locus scan" is invisible — they read as two unrelated tiles. *(Saquib, parents, web, infoviz — 4.)*
→ **Fix:** add the light selection edge Gap-findings→Selected-gap; keep the heavy `enriched_move ⇒ Selected-gap` dependency, so detect→findings→selected reads as a chain.

**M2 — Rename the Reception band "canon."** `canon` (band id) ≠ Reception; reception history is mostly extra-canonical, and node/function/side-label drift ("Reception" / "the tradition's real voices" / "canon side · retrieved"). *(Lamberth, IDEO, parents, web; HDS lists "canon" as opaque — 4–5.)*
→ **Fix:** publicly pick one word — "Reception / the tradition's voices."

**M3 — Make the waist-independent bypass visibly ORIGINATE before the waist (spatial, not only color).** Three crossing arcs that skip the middle read as errors/clutter; one deliberate bus tapping Text/Situate before the pinch reads as intentional. *(IDEO, Lidwell, infoviz; web notes the rail-bus already exists — 3–4.)*
→ **Fix:** route the bypass as one thin labeled bus that starts before the dark waist.

**M4 — Add a "blocked / awaiting-corpus" maturity state distinct from "specified," and apply it to Reception (0 rows, S162+).** AUDIT mode currently buckets a data-wall with never-built. *(Saquib strongly; Lidwell "badge Reception as pilot/awaiting-build"; web notes the badge — 3–4.)*
→ **Fix:** new status value; also consider bumping `gap_map` "specified"→"thin" (it has a lineage-only run).

### SOLO-but-sharp

- **Mirror renders as ONE color, not two (implementation bug).** Web: only Reception is tinted (`--me-tint-canon`); the Gloss arm uses the generic neutral band tint, identical to Morphospace/Compare — the symmetric mirror is visually asymmetric (one side marked, one generic). *(Web; infoviz flags the adjacent "ship JSON behavior, delete the 'all instrument outputs → fern' line from the brief" — 2.)* → Give Gloss its own cool fern/moss fill so the fork is a matched pair; keep hue exclusively on the pair.
- **LIVE DEFECT: the deployed page still exposes the retired 7-axis frame,** violating the engine's own S0 gate ("fail-loud if 7-axis exposed"). *(Saquib "Frame drawer admits stale"; web — 2.)* → Fix on rebuild.
- **Gloss drawer layers contradict the spec.** Diagram shows reader-gloss / persona-crit / gap-fill; FINAL spec's 3 layers are hook / argued / raw. *(Lamberth "delete the retired layer-tree, render the stance×method grid"; infoviz — 2.)* → Align the drawer to the spec or it reads as a fourth, contradictory taxonomy.
- **Rewrite the waist definition without CS jargon** — "operation + arguments + attached context" reads as debate-arguments to a theologian; means function-arguments. *(HDS.)* → "one interpretive move (what the text does + to what) with its context attached."

### CONFLATION adjudications — CONFIRMED by reviewers (no split)

- **(i) Reception = the retrieved reception HISTORY = ONE thing.** The glossing-of-retrieved-voices happens downstream at **Synthesis** (S9 colloquy consumes gloss + reception); the gap-FILL gloss is instrument-side under **Gloss** (S5). "Reception gloss" vs "reception history" are NOT two things. **Do NOT split Reception** — but its drawer must say "retrieved, not generated." *(Explicitly confirmed by Saquib, IDEO, HDS, web, infoviz; PI read upheld.)*
- **(ii) lineage / cross-source double-life (locus inside Gap-findings AND output Tributary/Cross-analysis) IS confusing** — see U4. *(Confirmed by all who addressed it.)*

### REVERSE-ORPHANS (decorations without a real engine home)

- **No pure decorations found** — HDS explicitly reports none; nearly every node traces to a real engine/table.
- **Constellation** (sonic Text→IPA, "specified," no data) is the thinnest — closest to decoration; interrogate its home before it earns equal waist-independent real estate. *(IDEO, Lidwell, HDS "thin," infoviz, web "thin" — MAJORITY note.)*
- **Cross-analysis** ("analysis-only, no export yet") sits at the same visual weight as populated outputs — borderline, but honestly AUDIT-flagged. *(Web, infoviz — 2.)*
- **Retired Fan should not be drawn at all** if it stays retired. *(IDEO, Lidwell.)*

---

## 4. Opaque-term leaderboard (most-flagged first)

| Term | # personas |
|---|---|
| waist-independent / move-conditioned | 8 |
| enriched move (vs coded move) | 8 |
| Morphospace | 8 |
| Partiture (/ Braid) | 8 |
| Tributary | 7 |
| witness-seam | 7 |
| Constellation (reads as star-map, means sound-field/IPA) | 6 |
| Resituate | 6 |
| Sitz | 6 |
| Paradigm | 6 |
| Braid | 6 |
| Degrees of separation (reads as the party game) | 6 |
| JOINS / Cross-analysis | 6 |
| Reflexive audit | 5 |
| incongruity (as a scan-locus) | 5 |
| wild-catch | 4 |
| 8-locus scan | 4 |
| colloquy | 3 |
| canon (band label) | 2 |

*(Runner-up structural note: several reviewers add that "move" itself is never defined in plain English on the canvas though it carries the whole diagram.)*

---

## 5. Recommended fix order

### P1 — before ANY audience
1. **Home the panel/chairs apparatus** (S3 nominate + S4/S8 CONVERGENCE-vs-DIVERGENCE chairs + symmetric-difference = the finding). *U1 — the #1 orphan; restores the method's crown jewel.*
2. **Draw the S6 fidelity gate** on Gloss→Synthesis with "no-grounded-gloss is allowable." *U2.*
3. **Plain-gloss "waist-independent / move-conditioned"** on the band headings; inline-define "move" and "enriched move" (drop CS "arguments"). *U8.*
4. **Fix the mirror to actually be two colors** (give Gloss its own cool hue; only Reception is tinted today) AND add the built/retrieved legend at the fork. *U7 + web SOLO.*
5. **Reconcile Fan** retired-here vs live-in-reading-room. *U5.*
6. **Disambiguate "lineage" / "cross-source"** (locus vs output vs leaf). *U4.*

### P2 — next pass
7. **Home `move_gloss`** as a distinct object/drawer, separate name from gap-fill Gloss. *U3.*
8. **Add the Gap-findings → Selected-gap selection edge** (light), keep the heavy `enriched_move` dependency. *M1.*
9. **Rename the Reception band "canon" → "Reception / the tradition's voices."** *M2.*
10. **Add a "blocked / awaiting-corpus" maturity state** distinct from "specified"; apply to Reception. *M4.*
11. **Make the bypass bus visibly originate before the waist.** *M3.*
12. **Lock the two correct calls:** NO third hue on the Enriched move (*U6*); do NOT split Reception (*conflation-i*).

### P3 — polish / rebuild
13. **Gloss all coined/engineering terms in METHOD mode** (Morphospace, Partiture, JOINS, IPA, witness-seam, wild-catch, 8-locus, Degrees, Constellation); reserve raw table names for AUDIT mode.
14. **Show a one-word function under each Situate leaf** in METHOD (not only AUDIT).
15. **Align the Gloss drawer layers to the spec** (hook / argued / raw) or reconcile the taxonomy.
16. **Fix the live S0-gate defect** — the deployed page still exposes the retired 7-axis frame.
17. **Interrogate reverse-orphans** — confirm Constellation / Cross-analysis have real homes before equal visual weight; don't draw the retired Fan.
18. **Responsive check** — the 4-column absolute-SVG bow-tie is desktop-only; verify a mobile stacked breakpoint and the 13px text floor; reserve terracotta (currently reused for the page kicker).

---

*Synthesized IRR-style from 8 independent persona crits. Findings use reviewers' own claims only; UNANIMOUS = ≥6 of 8, MAJORITY = 4–5, SOLO = 1–3-but-sharp.*
