---
title: "Candidate-graduation analysis — the full 795 fit-or-extend candidates (surface + bundle; nothing graduates cold)"
date: 2026-07-31
session: S156 (reading-SB, PI-asked)
status: RESULT. Reasoning-mode + live DB queries. Applies AXIS_candidate_graduation_MECE_method to all 795
  candidates (774 new-axis + 21 new-value). HEADLINE = NO 9th axis warranted on this analysis alone. It
  SURFACES the pinch-points + BUNDLES per the reader's own dispositions; the single strongest genuine
  graduate-candidate is MEDIATION/MATERIALIZATION (worth the full Cramér's V + 3IRR next), not eschatological
  (already BUNDLED, S156 demo). Read-only on data/project.db (WAL).
method: pm/30_methodology/AXIS_candidate_graduation_MECE_method_s156_2026-07-30.md
demo: pm/50_audits/orthogonality_test_eschatological_temporality_s156_2026-07-30.md
---

# TL;DR

Applying the graduation method (cluster → orthogonality → 3IRR → CLC-lock; default = BUNDLE) to **all 795
candidates**: **nothing graduates to a 9th axis on this analysis.** The candidates are overwhelmingly the
*reader's own bundle signals* — of the 774 new-axis proposals, the coder tagged **481 (62%) `folds_under` an
existing axis**, **250 (32%) `expands` an existing axis's value-set** (i.e. "chose X but the value pinched"),
and only **39 (5%) `separate`** (a genuine new-axis flag). The vocabulary is not badly under-built; it is
*pinching at specific values*.

- **The single clearest 9th-axis GRADUATE-CANDIDATE is MEDIATION/MATERIALIZATION** (semiotic / linguistic /
  technological / institutional mediation): recurs **46×** (8 `separate`), and — unlike eschatological — it is
  **not corpus-confounded** (48% Abrahamic, near the corpus baseline). It is the one cluster that earns the
  full orthogonality test (Cramér's V vs the 8) + 3IRR *before* any real call. Everything else BUNDLES or DEFERS.
- **The clearest NEW-VALUE pinch is `epistemic-warrant`**: it needs `exegesis` (proposed ×5) and `induction`
  (×3) — the top two recurring exact proposals in the whole 795 after "eschatological-temporality" ×3.
- **The already-tested eschatological cluster stays BUNDLED** (demo, 2026-07-30) — and this analysis shows
  *why it was a special case*: at 93% Abrahamic it is the most corpus-confounded cluster of all; the mediation
  cluster is the honest replacement as "strongest new-axis signal."

Nothing here is a graduation. Per §2.1 + the method's gates, graduation needs the full orthogonality + 3IRR;
this doc SURFACES and BUNDLES only.

---

# 0. Ground truth (§13 — every count is a live SQL result on `atlas_frame_read_candidate`)

```
Total candidates:               795   (all review_status='pending')
  candidate_kind='new_axis':    774
  candidate_kind='new_value':    21
Candidates with empty evidence:   0   (all 795 carry a non-empty rationale — §13 clean)
```

The reader's own three-way disposition, extracted from the `[relation=…]` tag in each new-axis rationale —
this is the strong prior the method leans on (§2.1: the coding already did the generation):

| Reader tag | Meaning (maps to method disposition) | Count | Share of 774 |
|---|---|---:|---:|
| `folds_under:<axis>` | **BUNDLE** — a facet/value of an existing axis | **481** | 62% |
| `expands:<axis>` | **NEW VALUE** — axis right, value-set incomplete | **250** | 32% |
| `separate` | **GRADUATE-CANDIDATE** — flagged genuinely orthogonal | **39** | 5% |
| `(no tag)` | untagged | 4 | 0.5% |

`folds_under` breakdown: r_topology 115 · hermeneutic-posture 80 · inferential-operation 77 · epistemic-warrant
74 · telos 67 · ontological-commitment 29 · evaluative-stance 26 · r_condition 13.
`expands` breakdown: epistemic-warrant 89 · r_topology 62 · ontological-commitment 32 · hermeneutic-posture 31 ·
telos 18 · inferential-operation 13 · r_condition 4 · evaluative-stance 1.

The default is **already bundle** — by the coder's own hand, 94% of new-axis proposals fold or expand onto the
existing 8. That raises the bar for the remaining 39 (correctly).

---

# 1. The "chose X but proposed Y" signal — the forced-choice-mismatch map

This is the PI's key question: *where does the current vocabulary pinch?* Two data streams answer it — the 21
`new_value` candidates (the purest form: coder picked the nearest value, flagged a better absent one) and the
250 `expands` new-axis candidates (same signal, filed as new-axis but tagged "axis right, value missing").

## 1a. The 21 `new_value` candidates — per axis

| Axis | # | Proposed values (recurrence) |
|---|---:|---|
| **epistemic-warrant** | **8** | **exegesis ×5**, **induction ×3** |
| **r_condition** | 6 | fidelity-service ×2, reciprocity, ritual-propriety, rivalrous, unilateral-objectification |
| **r_topology** | 4 | filial-asymmetric, hospitality, kinship-continuity, transcendent-personal |
| **ontological-commitment** | 3 | graded-asymmetry ×2, differentiation |

**Two sub-signals hide inside the 21, and they need different treatment:**

- **(A) genuinely-absent value → EXTEND the axis.** `exegesis` (barely present — only 2 reads currently placed
  in it), `induction` (absent from the epistemic-warrant bar entirely), `reciprocity` / `ritual-propriety` /
  `unilateral-objectification` (absent from the r_condition bar). These are real pinch-points.
- **(B) value-exists-on-a-SIBLING-axis → RELOCATE, don't extend.** `graded-asymmetry` (×2, proposed for
  ontological-commitment) and `rivalrous` (proposed for r_condition) and `differentiation` (proposed for
  ontological-commitment) and `kinship-continuity` (proposed for r_topology) **already exist as primary values
  — on `r_topology`** (graded-asymmetry 58, rivalrous 58, differentiation 65) **and `r_condition`**
  (kinship-continuity 62). These are not missing values; they are coders reaching for a value that lives on the
  neighboring relational axis. The fix is a coding-guidance clarification (which relational axis owns which
  value), **not** a new value — a §2.1 anti-bloat catch.

**Caveat (§13).** The 21 `new_value` rationales are terse (28–70 chars — bare phrase-quotes, not the fuller
`[relation=…]` reasoning the new-axis candidates carry). Evidence is present for all 21 but thin; the EXTEND
calls below should be re-confirmed against the actual passages before locking.

## 1b. The broader pinch — recurring semantic clusters across all 774 new-axis candidates

Exact-string recurrence is low (the proposals are verbose near-singletons): top exact repeats are
`exegesis` ×5, `eschatological-temporality` ×3, `induction` ×3, then a tail of ×2s. So the real clustering is
**semantic**. Keyword-family clustering of the 774 (Step 1 of the method — name the cluster after it forms):

| Cluster | Total candidates | `separate` (new-axis flags) | Reader's top bundle-targets |
|---|---:|---:|---|
| **political / legitimacy / institutional** | **112** | 13 | epistemic-warrant 38 · r_topology 37 · telos 15 |
| **mediation / materialization** | **46** | **8** | r_topology 15 · hermeneutic-posture 9 · epistemic-warrant 4 |
| temporal / eschatological *(demo → BUNDLED)* | 37 | 8 | r_topology 18 · telos + epistemic-warrant |
| spatial / cosmo / territory | 24 | 5 | r_topology 8 · epistemic-warrant 3 |
| affect / aesthetic / somatic | 20 | 1 | epistemic-warrant 5 · r_topology 4 |
| developmental / ontogenetic | 18 | 3 | inferential-operation 5 · telos 4 |
| part-whole / mereology / scale | 17 | 0 | r_topology 4 · inferential-operation 3 |
| self / ego-boundary | 8 | 2 | telos 1 · r_topology 1 |
| *(no keyword family — long tail)* | 531 | 5 | scattered folds/expands across all 8 |

**Where the vocabulary pinches, ranked:** the biggest raw pressure is **political/institutional** (112), but
the reader folds ~60 of those under existing axes (epistemic-warrant + r_topology) — it's a *facet-heavy*
cluster, not an orthogonal one. The next, **mediation** (46), carries the **most `separate` flags relative to
its confound** (see §3) — that combination, not raw size, is what makes it the graduate-candidate.

---

# 2. Bar-delta simulation (order-of-magnitude estimate — clearly labeled)

*What would the field-usage bar look like if the top pinch-value were added to its axis?* Rough method: the
count of candidates proposing value V is the floor of reads that move to V; the reads currently sit in some
existing value on that axis (queried live). This is directional, not a forecast.

**`epistemic-warrant` — current primary bar (n=911 reads):** observation 255 · reason 226 · testimony 189 ·
tradition 114 · revelation 64 · practice 28 · noetic-intuition 18 · embodied-practice 11 · mystical-union 2 ·
**exegesis 2** · divination 1.

| Proposed value | Currently | Reads flagging it & where they now sit | Est. bar after add |
|---|---|---|---|
| **exegesis** | 2 (present, tiny) | 5 flag it: 2 already in `exegesis`, 2 in `observation`, 1 in `reason` | **2 → ~5–7** (≈3× lift; a small but real value being under-offered) |
| **induction** | absent (0) | 3 flag it, all currently in `observation` (255) | **0 → ~3** (a new low-frequency value carved from `observation`) |

**Reading.** Neither is a large bar. `exegesis` is a genuine value that was *under-offered* at coding time
(reads that wanted it defaulted into observation/reason); adding/surfacing it is a low-risk EXTEND. `induction`
is a genuine but rare epistemic mode. The bar-delta confirms these are **value-level** fixes, nowhere near
axis-level pressure.

**The (B) relocation cases do NOT move bars** — `graded-asymmetry`/`rivalrous`/`differentiation` already carry
50–65 reads on `r_topology`; the 1–2 candidates proposing them elsewhere are mis-homed, not new demand.

---

# 3. Graduation calls — the top candidates (extends the eschatological demo)

Applying the bundling heuristic (default = BUNDLE; graduate only clears recurrence + orthogonality + coherence)
to the top clusters + top new-value pinch-points. **A load-bearing new finding drives every call: the
corpus-confound is cluster-specific.** Baseline: the full new-axis pool is **30% Abrahamic** (234/774). Per
cluster:

| Cluster | Abrahamic share | vs baseline (30%) | Confound verdict |
|---|---:|---|---|
| temporal / eschatological | **93%** (13/14 core) | massively over | **confounded** (why the demo BUNDLE had a caveat) |
| developmental / ontogenetic | **6%** (1/17) | massively under | skewed (psych/philosophical-driven) |
| political / legitimacy | 41% (39/96) | near baseline | clean |
| **mediation / materialization** | **48%** (12/25) | near baseline | **clean — least confounded** |
| spatial / cosmo / territory | 43% (3/7) | near baseline | clean (but tiny n) |

This reframes the demo: eschatological BUNDLED partly *because* its reads are almost all Abrahamic canon, so
"temporality co-loads with revelation/telos" was partly a which-texts-we-coded artifact (§2.8). **Mediation is
the honest replacement for "strongest new-axis signal"** — it recurs almost as often, carries as many
`separate` flags, and is *not* corpus-confounded, so its eventual orthogonality test will be trustworthy.

### Verdict table (top candidates × call × bundles-under)

| # | Candidate (cluster / value) | Recurrence | Call | Bundles under / home | Needs full orthogonality (Cramér's V) + 3IRR before any real call? |
|---|---|---:|---|---|---|
| 1 | **mediation / materialization** | 46 (8 sep) | **GRADUATE-CANDIDATE** | *tentative* r_topology (mediated-triadic already exists there) OR hermeneutic-posture | **YES — run this next.** Least confounded (48% Abr); the one cluster that earns the test. |
| 2 | political / legitimacy / institutional | 112 (13 sep) | **BUNDLE** (test only if #1 clears) | epistemic-warrant + r_topology (reader folds 60/96 there) | Optional — facet-heavy, low separate-ratio; likely bundles even under test |
| 3 | **epistemic-warrant → `exegesis`** | 5 | **NEW VALUE (EXTEND)** | epistemic-warrant (value already present ×2, under-offered) | No — value-level; confirm against passages, then EXTEND |
| 4 | **epistemic-warrant → `induction`** | 3 | **NEW VALUE (EXTEND)** | epistemic-warrant | No — value-level EXTEND (rare mode) |
| 5 | temporal / eschatological | 37 (8 sep) | **BUNDLE** *(already tested)* | telos (temporal inflection of salvation) | Done — 2026-07-30 demo; DEFER only the "structure-of-historical-time" residue |
| 6 | developmental / ontogenetic | 18 (3 sep) | **DEFER** (candidate new-value) | inferential-operation (diachronic-causation facet) | Re-test with #1 — corpus-skewed (6% Abr, psych-driven); coherent but confounded the other way |
| 7 | spatial / cosmo / territory | 24 (5 sep) | **DEFER** (candidate new-value) | r_topology | Re-test — coherent, clean spread, but small n (7 tradition-tagged) |
| 8 | r_condition → `reciprocity` / `ritual-propriety` / `unilateral-objectification` | 1 each | **NEW VALUE (EXTEND)** | r_condition | No — genuinely-absent relational-condition values |
| 9 | ontological-commitment/r_condition → `graded-asymmetry` / `rivalrous` / `differentiation` / `kinship-continuity` | 2/1/1/1 | **BUNDLE (RELOCATE)** | already exist on r_topology / r_condition | No — coding-guidance fix (sibling-axis leakage), not a new value |
| 10 | affect / aesthetic / somatic | 20 (1 sep) | **BUNDLE** | epistemic-warrant (embodied-practice) + evaluative-stance | No — only 1 separate flag; a facet, not a dimension |

**Nothing in this table is graduated.** #1 (mediation) is the sole cluster promoted to *graduate-candidate*
status — meaning: worth the full orthogonality + 3IRR, not that it becomes an axis. Per §2.1 and the method's
gates, no 9th axis is warranted on this SURFACE-and-BUNDLE pass.

---

# 4. Verdict

**Does anything warrant a 9th axis? NO — not on this analysis.** The 795 are, by the coder's own dispositions,
94% bundle-or-extend signals on the existing 8. The residual `separate` flags (39, 5%) are spread thin across
several small clusters, and the largest of them (mediation, 46) has not been orthogonality-tested yet.

**The three things to carry into the CLC walk (§12):**

1. **Run the full orthogonality test (Cramér's V vs the 8) + 3IRR on the MEDIATION/MATERIALIZATION cluster.**
   It is the strongest *honest* new-axis signal in the 795 — recurs 46×, 8 `separate`, and (critically) it is
   **not corpus-confounded** the way eschatological was. This is the direct successor to the eschatological demo.
2. **EXTEND `epistemic-warrant` with `exegesis` + `induction`** (the clearest value-level pinch; bar-delta ≈
   2→5-7 and 0→3), and **EXTEND `r_condition`** with `reciprocity` / `ritual-propriety` /
   `unilateral-objectification`. Confirm the terse `new_value` rationales against passages first (§13).
3. **BUNDLE / RELOCATE the sibling-axis leakage** (graded-asymmetry, rivalrous, differentiation,
   kinship-continuity → they already exist on r_topology/r_condition) via a coding-guidance note on which
   relational axis owns which value — an anti-bloat catch, not a vocabulary gap.

Everything else BUNDLES (political, affect) or DEFERS-with-reason (developmental — confounded the *other* way,
6% Abrahamic; spatial — clean but tiny n), re-tested alongside mediation.

---

# 5. Render-note for design-SB

The **candidates block** on the field-usage / atlas page should:
- **Link to this doc** (`pm/50_audits/candidate_graduation_analysis_s156_2026-07-31.md`) as "how the 795 open
  candidates are triaged (surface → bundle → graduate-candidate)".
- **Link to the eschatological demo** (`pm/50_audits/orthogonality_test_eschatological_temporality_s156_2026-07-30.md`)
  as "the one worked orthogonality test so far (verdict: BUNDLE)".
- Headline copy: *"795 open candidates → 62% bundle, 32% value-pinch, 5% flagged-separate. Zero new axes
  warranted yet; the next axis to earn a full test is MEDIATION, not eschatology."*
- If the block shows a bar/mini-viz, the honest framing is the **reader-disposition split (481 / 250 / 39)** +
  the **per-cluster Abrahamic-confound column** (it's the §2.8 bias made visible — the reason eschatological
  bundled and why mediation is the cleaner next test). Avoid implying any candidate has *graduated*.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: reading-SB S156 2026-07-31, reasoning-mode + live read-only DB queries (no engine). Applied
  AXIS_candidate_graduation_MECE_method_s156_2026-07-30.md to all 795 rows of atlas_frame_read_candidate
  (774 new_axis + 21 new_value, all pending). Extracted the reader's [relation=…] disposition tags from
  rationale (folds_under=481 / expands=250 / separate=39 / no-tag=4); keyword-clustered the 774 new-axis
  proposed_value strings into semantic families (political 112, mediation 46, temporal 37, spatial 24, affect
  20, developmental 18, part-whole 17, self/ego 8, long-tail 531); tabulated the 21 new_value candidates per
  axis + split them into genuinely-absent (EXTEND) vs sibling-axis-leakage (RELOCATE) by checking each proposed
  value against the live primary-value bars in atlas_frame_read_placement (is_primary=1, is_not_engaged=0, 911
  reads); ran the bar-delta estimate for exegesis (2→~5-7) + induction (0→~3) by joining proposing reads to
  their current epistemic-warrant primary value; computed per-cluster Abrahamic confound via
  atlas_frame_read_envelope → sources.tradition_family. All counts are SQL results, none recalled from memory
  (§13). Extends the eschatological orthogonality demo (2026-07-30) to the full pool.
SCHOLARLY SOURCES: data/project.db (atlas_frame_read_candidate / _placement / _envelope / sources);
  AXIS_candidate_graduation_MECE_method_s156_2026-07-30.md (the 3 gates + default-bundle); the eschatological
  demo (orthogonality_test_eschatological_temporality_s156_2026-07-30.md — the one prior worked test); CLAUDE.md
  §2.1 (anti-pre-anchoring / default-bundle — do NOT graduate cold), §2.8 (bias-visibility — per-cluster
  Abrahamic confound is the load-bearing new finding), §2.15 (black-box gates), §12 (CLC lock — this doc is a
  Step-4 input), §13 (real-data-over-memory; every count grounded).
WHAT NEEDS VERIFICATION: (1) No 9th axis is asserted — this SURFACES + BUNDLES; graduation of the mediation
  cluster requires the full Cramér's V orthogonality test + 3IRR (not run here). (2) Keyword clustering is a
  coarse proxy for the method's embeddings step; a borderline candidate may sit in the wrong family (esp. the
  531 long-tail unassigned). (3) The 21 new_value rationales are terse (28-70 chars) — confirm the EXTEND calls
  (exegesis/induction/reciprocity/ritual-propriety/unilateral-objectification) against actual passages before
  locking. (4) Bar-delta is order-of-magnitude (candidate-count floor + current-placement of proposing reads),
  not a forecast; multi-pick coding could shift shares. (5) The developmental cluster is confounded the OPPOSITE
  way (6% Abrahamic); its DEFER should be re-tested when the corpus balances, same discipline as eschatological. -->
