---
title: "Is 5-LLM agreement shared bias or signal? A task-dependence test on 307 IRR rounds"
short_title: "IRR consensus is task-dependent"
date: 2026-07-29 (S156)
author: reading-SB (main-Claude), PI-directed
status: FINDING (first-pass, defensible; exact percentages are proxy estimates — see §7)
audience: written for a non-specialist advisor (technical OR theological); all jargon defined inline
source_analysis: pm/50_audits/IRR_consensus_meta_analysis_s156_2026-07-29.md
reflexive_context: research/00_irr/irr224_reflexive_method_freeform_review_reconciliation_2026-07-29.md;
  pm/50_audits/CRT_3agent_method_review_synthesis_2026-07-29.md
---

# Is 5-LLM agreement shared bias, or signal?
### A task-dependence test on 307 inter-rater-reliability rounds

**Abstract.** The project's core validation instrument asks five large language models (LLMs) the
same methodological question and records how much they agree — a "5-LLM IRR round" (IRR =
*inter-rater reliability*, the standard social-science measure of whether independent judges reach
the same verdict). A standing objection says this agreement is worthless: the five models were
trained on overlapping text and tuned by similar human-feedback processes, so when they agree they
are only echoing a *shared bias*, not detecting a *real answer*. We tested that objection against
our own three-month archive of 307 completed rounds. The result: **agreement is not flat — it tracks
task difficulty.** Models agree most when asked to *enumerate what exists* (list the canonical stories
of a tradition: ~42% of findings reach full 5/5 agreement) and least when asked to *code, bound, or
label a specific unit of text* (~25% full agreement, ~29% outright split). If the agreement were pure
shared bias, it would not know which questions are hard. Because it does, the agreement carries signal
— and, more usefully, it tells us *where the instrument can be trusted and where a human expert must
remain the gold standard.*

---

## 1. Hypothesis — the objection we are testing

State the objection at full strength, because a weak version would be easy to knock down.

> **The rebuttal.** "Your 5-LLM IRR is not really five independent judges. All five models are trained
> on heavily overlapping internet-scale corpora and aligned by similar reinforcement-learning-from-
> human-feedback (RLHF) procedures. They share the same priors, the same blind spots, and the same
> culturally dominant readings. So when they agree, that agreement measures a **shared prior**, not
> the truth of the matter. Multi-model consensus is therefore a 'statistical house of cards' —
> reproducibility without validity. You have five copies of one biased rater, not five raters."

This is not a straw man we invented to defeat. It is the single most-agreed critique our own external
reviewers have leveled at the method. In a blind review round (IRR224, 2026-07-29), five frontier
LLMs read a statement of our method and independently converged — at **full 5/5 unanimity** — on
exactly this point: "agreement measures a shared prior, not ground truth." Three independent in-house
review agents landed on it too (CRT synthesis, 2026-07-29). The objection is real, it is sharp, and
the honest reflexive irony is that *five models agreed that five models agreeing proves nothing.* This
paper is our empirical answer.

**What would confirm the objection vs. what would refute it.**
- *If the objection is right* (agreement = shared bias), the agreement rate should be roughly **flat
  across question types.** A shared prior does not care whether a question is easy or hard; it just
  produces the same conventional output. Uniform high agreement everywhere = a house of cards.
- *If the agreement carries signal*, the rate should **vary with the difficulty of the task** — high
  where there is a discoverable right-ish answer, low where the question requires contested judgment.
  A pattern that tracks difficulty is something a mere shared bias cannot fake.

The test, then, is not "do the models agree?" (they often do). It is: **does their agreement know
which questions are hard?**

---

## 2. Method — how we tested it

**The corpus.** Every time the project faces a substantive methodological decision, it fires a 5-LLM
IRR round and writes a *reconciliation document* — a prose write-up that sorts the five models'
answers into consensus tiers. Over roughly three months (2026-04-27 → 2026-07-29) we accumulated a
large archive of these. We enumerated all of them:

- **320** files matched the reconciliation-document pattern under `research/00_irr/`.
- We removed **2** empty templates and **11** single-model self-reviews (not true 5-model rounds),
  leaving **307** genuine reconciliation documents.
- **304 of 307 (99%)** used the disciplined consensus vocabulary and were machine-parsed.
- **3 were excluded, by name, because they used loose qualitative phrasing** instead of the
  vocabulary (`irr77`, `irr126`, `irr127`). We did not guess their contents.

The rounds span numbered rounds IRR42–IRR224 plus ~130 earlier named (pre-numbering) rounds.

**The consensus vocabulary ("Decision-39 buckets").** Each reconciliation sorts findings into five
tiers by how many of the five models agreed:

| Bucket | Meaning |
|---|---|
| **UNANIMOUS** | 5 of 5 models agree |
| **STRONG-MAJORITY** | 4 of 5 |
| **MAJORITY** | 3 of 5 |
| **SPLIT / DIVERGE** | the models genuinely disagree; no clear majority |
| **SOLO** | 1–2 of 5 — a lone model raises something the others did not |

**The two things we counted.**
1. *Per-round headline* — is the round's top-line verdict clean consensus, consensus-with-some-
   divergence, or genuinely contested?
2. *Per-finding bucket* — across all rounds, what share of individual findings landed in each tier
   (≈7,290 tagged findings total)?

**The classification step (the actual experiment).** We labeled each round by **query-type** — the
*kind* of question it asked (defined and illustrated in §3). We then compared the agreement
distribution across types. This is the manipulation: if agreement is task-dependent, the distributions
will differ by type; if it is shared bias, they will not.

**Honesty about the proxy (per project rule §13 — do not overstate precision).** The reconciliation
documents are prose, not a uniform machine-readable table. We counted **occurrences of the bucket
vocabulary** in each document as a *proxy* for its findings. This means a free-floating word like
"diverge" in a sentence ("the cohorts diverge on X") is counted the same as a formal `SPLIT:` finding
header. Consequently:

- **Absolute percentages are approximate — treat them as ±several points.**
- The **relative pattern across query-types** is the trustworthy result, because the same proxy bias
  applies to every type, so *differences between types* are not artifacts of the counting method.
- Query-type labels were assigned by a keyword heuristic on filename + document header, not by reading
  every round in full. The two extreme types (passage-coding, substance-gathering) have the cleanest
  filename signatures; the middle types are softer (see §7).

This is a **first-pass characterization, not a statistic to cite to two decimals.** §6 lists the
follow-up tests that would harden it into a thesis figure.

---

## 3. The six query-types — defined, with a real example each

This section is the hand-holding the PI asked for. For each type we give (a) a one-sentence plain
definition, (b) a **real IRR round we actually ran** (verified to exist on disk — no invented
examples, per §13), and (c) how the models behaved on it.

A note on the naming, for both advisors: religion terms are glossed for the technical reader; ML
terms are glossed for the theological reader.

---

### 3.1 Substance-gathering — *"list what exists across traditions"*

**(a) Definition.** Ask the cohort to *enumerate real things in the world*: which canonical stories,
sources, figures, or observations exist in a given tradition or across traditions. There is a
right-ish answer; the task is coverage, not judgment.

**(b) Real example — `canonical_stories_christianity` (Round 85a, 2026-05-09).** We asked five models
to list the canonical stories of Christianity across its sub-traditions — deliberately including
non-dominant branches (Coptic, Ethiopian Tewahedo, Syriac, Armenian, African-American Methodist
Episcopal, Latin American liberation theology, Korean Minjung, Dalit Christian, Womanist, Caribbean
creolized, and more). The five cohorts together produced ~886 raw entries collapsing to ~597 distinct
stories.

**(c) Consensus behavior — highest agreement of any type (≈42% of findings unanimous).** When the
task is "enumerate what's there," the models heavily overlap: they find the same core stories, and
their lists reinforce each other. (A useful side-finding: one model, DeepSeek, refused certain
politically sensitive *non-Christian* content in sibling rounds, which the enumeration surfaced as a
documented coverage limit rather than hiding it — an instance of the project's bias-visibility
discipline, §2.8.)

---

### 3.2 Passage-coding — *"code / bound / label this specific unit of text"*

**(a) Definition.** Apply the analytical instrument to *one concrete passage* in one tradition:
segment it into moves, mark its negative space (what it leaves unsaid), and judge whether each
element is present and whether it is *obligated*. This is interpretive judgment on a specific unit,
not enumeration.

**(b) Real example — `irr167_beatles_coding_method` (IRR167, coded 2026-07-09, reconciled 2026-07-19).**
Earlier coding of Romans 8 (a dense, ancient, translated theological text) had shown a reliability
split: coders agreed on whether a silence was *present* (Krippendorff's α ≈ 0.59 — α is a chance-
corrected agreement score where 1.0 is perfect and 0 is chance-level) but almost never agreed on
whether that silence was *obligated* (α ≈ 0.03, i.e. essentially chance). The obvious explanation was
"theology is just hard." So we re-ran the *same coding instrument* on the cleanest possible text — a
famous, modern, English, semantically simple pop lyric (*All You Need Is Love*) — to isolate the
variable. Five models each coded six candidate silences independently.

**(c) Consensus behavior — lowest agreement of any type (≈25% unanimous, ≈29% outright split).** All
five models agreed on the *headline*: the split reproduces even on the clean corpus. Presence still
codes reliably; obligation still does not. This is the paper's thesis-critical result, discussed in
§4 — and note it is a *high-value* disagreement: the models converged on the fact that they cannot
converge on obligation, which localizes the exact fragile step in the method.

---

### 3.3 Taxonomy-validation — *"are these the right categories, and where is the boundary?"*

**(a) Definition.** Ask whether a proposed set of categories or axis-values is complete and correctly
cut — i.e., *where do we draw the lines* between types. This is boundary-drawing, which is judgment.

**(b) Real example — `irr179_edge_taxonomy` (IRR179, 2026-07-11).** We proposed a nine-type taxonomy
of "edges" (the relations between negative-space moves — e.g. *presupposes*, *entails*, *fills*) and
asked the cohort to pressure-test it. All five said: codeable *with named changes* — the architecture
holds, but the definitions need tightening, and one change is load-bearing. Specifically, the "RHYME"
edge (two texts making structurally the same move) had to be split into (1) a structural match,
codeable now, and (2) *independent convergence*, a later verdict that must first rule out historical
contact — otherwise Augustine quoting Paul would be miscounted as independent discovery, invalidating
the project's central comparative claim.

**(c) Consensus behavior — second-most contested (≈22% split).** Boundary questions split the models
more than enumeration does. The closer a question gets to *drawing a line*, the more judgment it
requires, and the more the models diverge — but the divergence here was *productive*, converging on a
fix that protects the thesis rather than one that undermines it.

---

### 3.4 Methodology-fork — *"design a new method / choose between method designs"*

**(a) Definition.** Ask the cohort to help invent or choose a genuinely novel analytical procedure —
a new framework, algorithm, or detector. There is no established right answer; the space is open.

**(b) Real example — `irr138_negative_space_framework` (IRR138, 2026-06-20).** We proposed a
four-part scheme for classifying "negative space" (the meaningful silences in a text) and asked
whether it was complete. All five said it was both incomplete *and* mis-cut — and then each model
proposed a *different* recut: GPT offered three axes (locus / mechanism / evidence); Gemini offered
four levels including an "epistemic-meta" tier; DeepSeek offered five ontological sources; Solar and
Haiku offered still other cuts. They converged on "it's wrong" but diverged on "here's the right one,"
each contributing a distinct idea.

**(c) Consensus behavior — the most SOLO signal of any type (≈27%).** New-method rounds are where a
single model most often surfaces a unique, additive idea the others missed — not agreement, not
conflict, but *complementary invention.* This matches the project's §2.8 observation that the cohort
produces *additive* signal, not just convergent signal; method-design is where that shows up most.

---

### 3.5 Architecture — *"how should we build the engineering system?"*

**(a) Definition.** Ask about the technical infrastructure: database design, pipeline structure,
throughput, storage. Engineering questions with real trade-offs but often a defensible middle.

**(b) Real example — `multi_writer_sqlite_resolver_chain_architecture` (Round 43, 2026-05-13).** We
asked whether to stay on a single-file SQLite database or migrate to Postgres, and how to structure
the source-resolver chain. (This round is doubly interesting: we asked the *same* engineering
questions under two different framings — "solo student side-project" vs. "decade-scale open-methodology
product" — and the models flipped their recommendations, which became the project's canonical evidence
that framing shapes answers, §2.8. For the present analysis it is simply a representative architecture
round.)

**(c) Consensus behavior — converged middle (≈36% unanimous, balanced tail).** Infrastructure
questions land in the middle: solid but not extreme agreement, with divergence distributed evenly
rather than concentrated in splits. Sensible engineers agree on a lot and reasonably differ on the
rest.

---

### 3.6 Citation-retrieval — *"verify these facts / find these sources"*

**(a) Definition.** Ask the cohort to check verifiable facts — dates, councils, names, textual loci —
or to retrieve real sources. There is a checkable right answer.

**(b) Real example — `irr141_junctions_reception_factcheck` (IRR141, 2026-06-21).** We asked the
cohort to fact-check seven historical "reception junctions" (claimed lineages like Augustine → Calvin
→ Synod of Dort). Note this round was deliberately run with **four models, not five** — Solar was
excluded because it fabricates citations on sparse-corpus retrieval (project rule, Decision 75). The
models mostly agreed the *facts* check out (dates, councils, primary-text loci) while unanimously
flagging the most dangerous over-compressed chain (Greek Fathers → Arminius → Wesley) as needing to
be split.

**(c) Consensus behavior — highest STRONG-MAJORITY of any type (≈27% at 4/5), on the smallest sample
(only 9 rounds).** On verifiable facts the models mostly-agree, with the occasional lone dissent —
the profile you would expect for checkable claims. **Caveat: N = 9 rounds is too small to lean on
hard;** we report it for completeness, not as a load-bearing result.

---

### 3.7 Summary table of the six examples

| Query-type | One-line definition | Verified real example | Consensus behavior |
|---|---|---|---|
| **substance-gathering** | list what exists across traditions | `canonical_stories_christianity` (R85a) | **highest agreement** — ~42% unanimous |
| **passage-coding** | code/bound/label one specific unit | `irr167_beatles_coding_method` | **lowest agreement** — ~25% unanimous, ~29% split |
| **taxonomy-validation** | are these the right categories / where is the line | `irr179_edge_taxonomy` | 2nd-most contested — ~22% split |
| **methodology-fork** | design/choose a novel method | `irr138_negative_space_framework` | **most SOLO** — ~27% additive lone ideas |
| **architecture** | how to build the engineering system | `multi_writer_sqlite_resolver_chain` (R43) | converged middle — ~36% unanimous |
| **citation-retrieval** | verify facts / retrieve sources | `irr141_junctions_reception_factcheck` | highest 4/5 majority, but N=9 (small) |

All six examples were confirmed to exist on disk. None is fabricated.

---

## 4. Results

**4.1 How often do rounds converge overall?** Two honest readings:

| Reading | Rate | Plain meaning |
|---|---:|---|
| **Strict** (pure 5/5 top-to-bottom, zero divergence) | **80 / 304 ≈ 26%** | ~a quarter of rounds are total consensus |
| **Lenient** (consensus-led, some divergence at margins) | **217 / 304 ≈ 71%** | ~7 in 10 rounds are consensus-dominant |
| **Genuinely contested** (divergence dominates) | **15 / 304 ≈ 5%** | fully contested rounds are rare |

So: a *pure* 5/5 round is the minority (~26%); *consensus-dominant* rounds are the strong majority
(~71%); rounds where the models mostly *disagree* are rare (~5%). When divergence happens, it is
almost always **local** (a specific finding inside an otherwise-converged round), not global.

**4.2 Finding-level distribution** (all ≈7,290 tagged findings): UNANIMOUS 36% · STRONG-MAJORITY 13%
· MAJORITY 14% · SPLIT 19% · SOLO 18%. Roughly half of all findings (49%) are 4/5-or-better; full 5/5
is the single largest bucket; the interesting variation lives in the SPLIT + SOLO tail (37%).

**4.3 The main result — agreement varies systematically by task.** Finding-level bucket share broken
out by query-type, sorted by unanimous share:

| Query type | N docs | UNANIMOUS | STRONG-MAJ | MAJORITY | SPLIT | SOLO |
|---|---:|---:|---:|---:|---:|---:|
| **substance-gathering** | 78 | **42%** | 9% | 13% | 18% | 17% |
| citation-retrieval | 9 | 37% | **27%** | 6% | 19% | 11% |
| architecture | 87 | 36% | 14% | 15% | 18% | 18% |
| taxonomy-validation | 48 | 36% | 12% | 13% | **22%** | 16% |
| methodology-fork | 46 | 34% | 16% | 13% | 11% | **27%** |
| **passage-coding** | 33 | **25%** | 18% | 15% | **29%** | 14% |

**The one-line finding: the models converge on enumeration and diverge on demarcation.** Agreement is
highest when the task is "list what exists" (substance-gathering, 42% unanimous) and lowest when the
task is "code / bound / label a specific unit" (passage-coding, 29% split; taxonomy-validation, 22%
split). Method-invention sits apart: it produces *additive solo* signal (27%) rather than either
convergence or conflict.

**4.4 The thesis-critical link — passage-coding reproduces the IRR167 present-vs-obligated split at
corpus scale.** The single round IRR167 found that coders agree on *whether a silence is present* but
not on *whether it is obligated* — and that this split survives even on a maximally clean text, making
it a property of the **method (the instrument), not the domain (theology).** This meta-analysis shows
that same signal is not a one-round fluke: across all 33 passage-coding rounds, this is the most
divergent task-type in the entire corpus. The instrument-level reliability problem IRR167 identified
in one case is visible as a corpus-wide pattern.

---

## 5. How this answers the rebuttal

Return to the objection: *the models share training and RLHF, so their agreement is shared bias, not
signal.*

**The decisive observation: agreement is task-dependent, and a shared bias cannot be task-dependent.**

- A pure shared prior does not know which questions are hard. It would produce roughly *uniform*
  agreement — high everywhere, because the models would keep echoing the same conventional output
  regardless of task. That is the prediction the objection makes (§1).
- What we observe instead is a **17-point spread in unanimity across task-types** (42% for
  enumeration down to 25% for passage-coding), and the spread lines up with *task difficulty as
  independently understood*: enumeration has a discoverable answer, so agreement is high; interpretive
  coding and boundary-drawing require contested judgment, so agreement is low.
- Crucially, the low-agreement zones are exactly where we **independently know** (from IRR167, and
  from the philosophy of interpretation generally) that the work is genuinely hard. The agreement
  pattern *tracks* a difficulty gradient it was not told about. A house of cards does not do that.

Therefore the honest conclusion is **not** "IRR proves validity" (it does not) and **not** "IRR is
worthless" (the objection's claim). It is the more useful middle:

> **The agreement carries signal, and the signal is a map of where to trust the instrument.**
> Where the models converge on enumeration, the automated cohort is a reasonable coverage tool. Where
> they diverge on coding and demarcation, agreement should *not* be read as validity — those are
> precisely the cells that require a **human-expert gold anchor**, chance-correction, and an
> inter-model error-correlation discount (the fixes our external reviewers named, IRR224 §2).

This reframes the objection from a refutation into a *finding*: the distribution of agreement is
itself diagnostic. It tells the researcher, task by task, whether the LLM cohort is measuring the
world or measuring itself — which is exactly the discrimination the bias-visibility methodology (§2.8)
is built to make visible rather than hide.

---

## 6. Secondary tests — designed, not yet run

The §4 result is a *pattern* consistent with signal. To promote it from "consistent with" to
"demonstrated," three tests are designed but not yet executed. They are listed here so the claim's
current status is honest.

### 6a. Statistical baseline — is 26% / 71% above chance?

The pattern (spread across types) is the load-bearing result, but the *absolute* rates need a null
model to interpret. Two complementary baselines:

- **A permutation null (internal).** Randomly shuffle each model's per-finding verdicts, holding each
  model's marginal label-frequencies fixed, and re-compute the agreement distribution many times. This
  yields the agreement rate expected *if the models were independent raters with the same output
  habits but no shared signal.* Compare observed vs. null. (Intuition for the binary sub-case: if a
  present/absent judgment were a coin-flip per model, chance 5/5 unanimity ≈ 2 × 0.5⁵ ≈ 6%. Observed
  strict unanimity is ~26% — several-fold above that floor. The permutation null generalizes this to
  the real, non-binary, non-uniform label space.)
- **A non-LLM human/reference baseline (external — the more persuasive one).** Take the *same*
  demarcation questions the models split on and ask how much established **reference works** agree.
  For example: where does a given pericope begin and end, across several study Bibles and commentaries?
  Is a given text canonical, across the *Encyclopædia of Religion*, the *SEP*, and standard tradition
  reference works? If human-authored reference works *also* disagree on demarcation at comparable
  rates, then the models' low agreement on those tasks is **appropriate** — they are tracking a
  genuinely contested question, not manufacturing noise. This directly converts the "agreement ≠
  validity" worry into a calibration check: the instrument should agree where experts agree and split
  where experts split.

### 6b. Reliability check — three independent agents re-tally the same corpus

The bucket counts here are a single-pass proxy. Re-run the tally with **three independent agents**
parsing the *same* 307-document corpus with the same instructions, then compute their agreement on
(i) the per-round headline classification and (ii) the query-type labels. Report inter-tallier
reliability. If the three tallies agree, the proxy is trustworthy for the relative pattern; if they
diverge on query-type labels, §7's classifier caveat is the dominant limitation and must be fixed
first. (This is the meta-analysis eating its own dog food — an IRR check on the IRR meta-analysis.)

### 6c. Coverage / proxy caveats to close

- Replace vocabulary-occurrence counting with a **format-aware parser** that extracts each finding's
  explicit bucket from the verdict section, separating formal `SPLIT:` headers from prose "diverge."
- Validate the query-type labels against a human (or single-LLM) pass on a 20-round sample to get a
  classifier-agreement rate.
- Add a **time-series** decomposition: does the unanimous rate drift as the method matures (early
  enumeration harvests vs. late method-forks)? The corpus spans April–July 2026 and the task-mix
  shifts across that window, which could confound the cross-type comparison.

---

## 7. Limitations (stated plainly)

1. **The counts are a proxy, not a structured parse.** We counted bucket-vocabulary occurrences in
   prose. Absolute percentages are ±several points. Only the *relative* cross-type pattern is
   defensible; do not cite the exact numbers as precise statistics.
2. **Query-type labels are unvalidated heuristics.** Filename + header keywords assigned each round.
   The two extremes (passage-coding, substance-gathering) have clean signatures and are trustworthy;
   the middle three (architecture / taxonomy / methodology) have fuzzy boundaries and could shift a
   few points with a careful re-read.
3. **Citation-retrieval is N = 9.** Too small to lean on; reported for completeness only.
4. **Three rounds were excluded, by name**, not silently — they used qualitative phrasing the parser
   could not bucket (`irr77`, `irr126`, `irr127`).
5. **This test defends signal, not validity.** Showing agreement is task-dependent refutes the
   *strong* "pure shared bias" objection. It does **not** prove any individual coding is correct. The
   external reviewers' deeper point stands and is *accepted*: for the low-agreement tasks (coding,
   demarcation), a human-expert gold anchor and chance-correction remain required. This analysis tells
   you *where* that anchor is most needed; it does not remove the need for it.
6. **The reflexive irony is real and worth stating in the defense.** The instrument used to defend the
   method (multi-LLM agreement) is the same instrument the method's critics distrust. We do not
   resolve that by asserting the instrument is fine; we resolve it by showing the instrument's
   agreement is *structured* in a way shared bias cannot produce — and by conceding the human anchor
   exactly where the structure says it is needed.

---

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED. S156 (2026-07-29), reading-SB (main-Claude), PI-directed. Rewrote the first-pass
  meta-analysis (pm/50_audits/IRR_consensus_meta_analysis_s156_2026-07-29.md) into a science-paper
  structure legible to a non-specialist advisor (Saquib / Lamberth): stated the "agreement = shared
  bias" rebuttal at full strength; framed the task-dependence test as the discriminator; defined all
  six query-types with a VERIFIED real IRR example each (grep + head-read of the reconciliation docs
  under research/00_irr/ — no invented examples per §13); carried through the enumeration-converges /
  demarcation-diverges result and the IRR167 passage-coding link; added the designed-not-run secondary
  tests (permutation null + non-LLM reference-work baseline + 3-agent re-tally reliability); stated
  limitations. Numbers are quoted from the source meta-analysis (proxy counts, ±several points).
  Reflexive context read from irr224 reconciliation + CRT_3agent synthesis (the external reviewers'
  U1 "IRR ≠ validity" critique this paper answers). Not committed per brief.
SCHOLARLY SOURCES. CLAUDE.md §2.6 (5-LLM IRR pattern + Decision-39 buckets); §2.8 (bias-visibility;
  cohorts produce additive not just convergent signal; the framing-flip); §2.14 (instrument vs domain
  — IRR167 present-vs-obligated as the canonical worked example reproduced here at corpus scale);
  Decision 75 (4IRR Solar-OUT for citation-retrieval — the irr141 example); feedback_solar_judgment_
  not_retrieval_cohort. The six verified examples: canonical_stories_christianity_reconciliation_
  2026-05-09 (_archived/); irr167_beatles_coding_method_reconciliation_2026-07-19; irr179_edge_taxonomy_
  reconciliation_2026-07-11; irr138_negative_space_framework_reconciliation_2026-06-20; multi_writer_
  sqlite_resolver_chain_architecture_reconciliation_2026-05-13; irr141_junctions_reception_factcheck_
  reconciliation_2026-06-21.
WHAT NEEDS VERIFICATION. (1) All absolute percentages are vocabulary-occurrence proxies — a format-
  aware per-finding parser would replace prose "diverge" false-positives (§6c). (2) Query-type labels
  unvalidated; the architecture/taxonomy/methodology middle is the softest boundary (§7.2). (3) The
  secondary tests (§6) are DESIGNED, NOT RUN — the permutation null, the non-LLM reference-work
  baseline, and the 3-agent re-tally are proposals, not results; do not report their outcomes as if
  obtained. (4) N=9 citation-retrieval is too small to lean on. (5) No time-series decomposition yet.
  Cite the PATTERN (converge-on-enumeration, diverge-on-demarcation; agreement is task-dependent), not
  the exact percentages. -->
