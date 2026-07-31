---
title: "Method rebuttals / FAQ — anticipated objections, our response, and the test that backs it"
date: 2026-07-29
session: S156 (reading-SB, PI-directed)
status: LIVING defense artifact. For each objection an advisor / crit-group member (Lamberth, Saquib, the CRT group)
  is likely to raise: (1) the objection stated fairly, (2) our response, (3) a LINK to the actual test/finding that
  backs it. Grows over time. The TESTS QUEUE at the bottom holds the experiments still to run.
---

# How to read this
Questions come from every direction — **our own**, the **IRR cohorts**, the **20-agent meta-crit / CRT on our process**,
**advisors** (Lamberth, Saquib), and the **DR / GPT / Fable engines** when we probe our uniqueness (the MCA questions,
"how novel is this," etc.). Each entry is **Objection → Response → Evidence (the test we ran)**. The point is that our
answers are not assertions — each links to a run. Where the test is *designed but not yet run*, it sits in the TESTS
QUEUE, not the answered list.

---

## R1 · "Your 5-LLM IRR isn't really 5 independent judges — they're trained on overlapping corpora + RLHF, so agreement is *shared bias*, not signal."
**Response.** We agree it isn't 5 independent humans — and instead of denying it, we *measured* it. Across **307 IRR
reconciliation docs**, agreement is **task-dependent**: the models **converge on enumeration** (substance-gathering ~42%
unanimous) and **diverge on demarcation** (passage-coding lowest-unanimous, ~29% split). If consensus were pure shared
bias it would *not* track task-difficulty like that — so the *pattern* is signal. Operationally it tells us **where to
trust the instrument (enumeration) and where the human gold-anchor is required (coding/judgment).** The null ("they share
training") becomes a finding ("and here's the *shape* of when that matters"). Bonus: the passage-coding divergence
independently reproduces IRR167's present-vs-obligated reliability split at corpus scale (§2.14).
**Evidence.** `pm/50_audits/IRR_consensus_meta_analysis_s156_2026-07-29.md` + the science-paper writeup
`pm/50_audits/FINDING_irr_consensus_task_dependence_s156_2026-07-29.md`. Secondary tests (statistical baseline;
reliability CRT) in the queue.

## R2 · "Your instrument is built for linear, Western, agentive narrative — what about non-linear or non-agentive texts?"
**Response (two parts).** (a) **Non-linear:** we built a *sixth output, Constellation*, in direct response to exactly this
question — a nonlinear text rendered as a field of moves + edges rather than a spine (worked on Gertrude Stein's
*Tender Buttons*). The objection *generated an output*. (b) **Non-agentive/apophatic:** the move-grammar was designed to
fit non-Western traditions via *different values / nulls / per-domain axis-weights*, not a different grammar
(irr157 negative-space-grammar-grounded; irr218 per-domain-axis-importance; irr139/142/158).
**Evidence.** The Constellation output (Stein) + the grammar-grounding IRRs above. *Open:* run the built instrument on a
*representative* non-Western text end-to-end (queued).

## R3 · "Your move-grammar is Western/agentive — does it even *fit* non-agentive or apophatic traditions?" *(raised by the 20-agent meta-crit on our process)*
**Response.** It fits *without* a different grammar — via **different axis-values, nulls, and per-domain axis-weights**,
not a re-built ontology. This was designed in when the grammar-slots were chosen: a non-agentive or apophatic text codes
with different fillers (or explicit nulls) in the *same* slots, and the per-domain axis-importance prior weights them
differently. So the grammar bends rather than breaks.
**Evidence.** irr157 (negative-space-grammar-grounded) · irr218 (per-domain-axis-importance) · irr139/142/158. *Open:*
run the built instrument on a representative non-Western text end-to-end (TESTS QUEUE #5) — the confirming run.

---

## R4 · "Your gaps / negative-space are unbounded — every utterance leaves infinitely many things unsaid, so 'gap-scoring' measures the model's associative priors, not the text." *(IRR224 5-LLM: UNANIMOUS 5/5 U2; 3-agent CRT: 3/3 #2 — the two heaviest blows of the round)*
**Response.** We accept the charge as stated — an *open* gap-frame does measure the coder's completion, not the text. Our answer is the fix both cohorts independently converged on: make gaps **CLOSED + CONTRASTIVE**. A gap is not "conceivably fillable" but "role X is filled in a parallel text / the tagged paradigm and is empty *here*." A contrast set supplies the *obligation* that turns an infinite absence into a scored, falsifiable one. This is not a new idea bolted on — it is the same present-vs-obligated distinction IRR167 already surfaced (§2.14): coders agree a silence is *present* (α≈0.59) but not that it is *obligated* (α≈0.03), and the contrast set is exactly what supplies the missing obligation. The frontier cohort also sharpened the target — GPT's positive-silence point (some silence *functions*: apophatic protection, trauma, esoteric reticence), so the fix must also carry a **silence typology** (presupposed / taboo / ineffable / generic-convention) rather than treating every absence as a defect.
**Status.** ANSWERED-IN-PRINCIPLE, OPEN-IN-IMPLEMENTATION. The contrast-set fix is named + 3/3-converged + 5/5-reproduced, but not yet operationalized at scale; the silence typology is a proposed output, not built. See TESTS QUEUE #12.
**Evidence.** `research/00_irr/irr224_reflexive_method_freeform_review_reconciliation_2026-07-29.md` (U2) · `pm/50_audits/CRT_3agent_method_review_synthesis_2026-07-29.md` (#2 + the contrast-set fix) · §2.14 / IRR167 (present-vs-obligated). Test: TESTS QUEUE #12 (gap salience / contrast-set operationalization).

## R5 · "Your edge typology is under-specified — 'presupposes, entails, fills, …' belong to different theoretical registers (logical / semantic-pragmatic / method-defined), and the '…' hides the hardest part of the grammar. Is the set exhaustive? mutually exclusive? by what assignment rules?" *(IRR224 5-LLM: UNANIMOUS 5/5 U3)*
**Response.** This one we do **not** yet have a strong answer to. We do not currently publish a complete, closed edge-type set with formal assignment rules, nor a rigorous graph-theoretic description of the underlying model — the ellipsis in the method-statement is doing real concealment, as all five cohorts caught. The honest position is that the edge inventory grew bottom-up (fit-or-extend) and has not been frozen, typed by register, or tested for inter-coder assignment agreement.
**Status.** **OPEN.** No strong answer yet. The fix is a formalization pass (enumerate the edge set, sort by register, state assignment rules, then measure agreement on edge-typing), tracked as a new test.
**Evidence.** `research/00_irr/irr224_..._reconciliation_2026-07-29.md` (U3, 5/5). No test exists yet → added as TESTS QUEUE #7.

## R6 · "Move segmentation / granularity has no principled stopping rule — is 'the kingdom of heaven is like a mustard seed' one move or three? IRR on divergent segmentations conflates two error sources, and the grain changes every downstream coordinate." *(IRR224 5-LLM: STRONG-MAJORITY 4/5 SM4; 3-agent CRT: 3/3 #5)*
**Response.** We accept there is no justified atomicity axiom today, and that GPT's sharpest version bites — one-operation-per-move "may improve reliability while reducing validity… the grammar risks discovering the discreteness it imposed." Our partial answer is the fix the CRT named (3/3): **report segmentation reliability separately from label reliability**, so an IRR number stops conflating "we disagree on where the move boundary is" with "we disagree on how to code the same unit." That separation makes the problem visible and measurable; it does not yet supply the stopping rule itself.
**Status.** PARTIALLY ANSWERED (separate the two reliabilities), **OPEN on the stopping rule** (what makes a move atomic vs. a composition). See TESTS QUEUE #8.
**Evidence.** `research/00_irr/irr224_..._reconciliation_2026-07-29.md` (SM4) · `pm/50_audits/CRT_3agent_method_review_synthesis_2026-07-29.md` (#5 + the separated-reliability fix). Test: TESTS QUEUE #8.

## R7 · "There is no reader / reception / interpreter-positionality in the method — meaning is completed in uptake, and the coder's own constitutive role is rendered invisible, so the coded object presents a false neutrality." *(IRR224 5-LLM: STRONG-MAJORITY 4/5 SM3 — the single most important miss for 3 of them; 3-agent CRT: 2/3 #4)*
**Response.** This is a real hole, and one the instrument caught *about itself*: the reflexive run's top forebear-selected gap (`f382fae9bc`) is precisely that mandating outputs read "from the coded object, not the original" silently installs the coded layer as scripture (Genette's palimpsest, Kugel's targum, Iser's Leerstelle) with no stated justification. Our coding models text-internal *production*; even the reception outputs remain text-to-text and do not model uptake in a situated reader. The designed answer is the **Representation Ledger** (a versioned lattice with a positionality preamble + calibrated confidence + alternative codings), the round's top generative convergence — but it is designed, not built.
**Status.** **OPEN.** We can *name* the miss precisely (the instrument surfaced it reflexively) but have no built mechanism that models reception or exposes coder positionality. See TESTS QUEUE #10.
**Evidence.** `research/00_irr/irr224_..._reconciliation_2026-07-29.md` (SM3 + Representation Ledger §3) · `pm/50_audits/REFLEXIVE_OUTPUT_instrument_reads_itself_2026-07-29.md` (gap `f382fae9bc`) · `pm/50_audits/CRT_3agent_method_review_synthesis_2026-07-29.md` (#4, reader-is-a-system). Test: TESTS QUEUE #10.

## R8 · "Your morphospace axes are under-specified — are they a-priori or induced, how many axes constitute adequacy, and doesn't a 'coordinate' launder judgment beneath false geometric precision? Different coders could produce radically different coordinates." *(IRR224 5-LLM: STRONG-MAJORITY 4/5 SM5; 3-agent CRT: 3/3 #7; independently flagged in the GPT tooling survey §5)*
**Response.** Partly answered, honestly. Our real handling of the false-precision half is the **declared-profile-vs-derived-geometry separation** the GPT tooling survey independently recommends: keep the *declared* categorical values (the eight-row fingerprint) visibly distinct from any *derived* 2-D geometry (an MCA/MDS projection over an explicitly documented distance model), and never let the smooth interface make the ontology look more metric than it is — radial/spectrum encodings are refused where the value set is not genuinely ordered. On the "clouds not points" charge we have empirical backing: **78% of texts multi-pick** on the axes, so a text is already represented as a region, not a single point (matches the CRT's dialectical-cloud critique — the data and the critique agree). What remains unanswered is the *derivation* question (a-priori vs induced, and adequacy-N) and coder-to-coder coordinate reliability.
**Status.** PARTIALLY ANSWERED (false-precision → declared/derived split + 78% multi-pick), **OPEN on axis derivation + adequacy-N + inter-coder coordinate reliability.** See TESTS QUEUE #11.
**Evidence.** `research/00_irr/irr224_..._reconciliation_2026-07-29.md` (SM5) · `pm/50_audits/CRT_3agent_method_review_synthesis_2026-07-29.md` (#7 + the 78%-multi-pick empirical finding) · `researchsurvey_gpt.txt` §5 "declared profile vs derived geometry" + §4 cross-check. Test: TESTS QUEUE #11.

## R9 · "Domain-generality is asserted, untested, and non-falsifiable — running the method on its own statement proves consistency, not generality; showing it works on two domains doesn't establish the structure belongs to the method rather than being generic (Barnum effect)." *(IRR224 5-LLM: STRONG-MAJORITY 4/5 SM1; 3-agent CRT: 3/3 #9)*
**Response.** This is the objection we have the *strongest* live answer to — and it is a genuine falsification programme, not a rhetorical flourish. §2.14 (Replication — test the instrument out of domain) is exactly the discriminating move the cohorts demand: is a result a property of the INSTRUMENT or of the DOMAIN? The worked example is IRR167 — the Romans-8 present-vs-obligated reliability split was suspected to be "theology is hard," so we ran the same instrument on a confound-free out-of-domain corpus (a modern pop lyric) and **the split reproduced 5/5**, converting a suspected domain problem into a demonstrated instrument property. That is a replication *result*, not a self-application. We also concede the sharper test still to run: **Fan-as-validity-probe / intervention-based validation** (perturb one slot — flip an agent, remove a warrant — and check the coding changes *coherently in the predicted slot*), which gives the generality claim a real per-move falsification rather than a domain-count argument.
**Status.** SUBSTANTIALLY ANSWERED via out-of-domain replication (§2.14 / IRR167 is a run, not a claim); **OPEN on the per-move intervention test** (Fan-as-validity-probe). See TESTS QUEUE #9.
**Evidence.** §2.14 + IRR167 reconciliation (out-of-domain Beatles replication) · `research/00_irr/irr224_..._reconciliation_2026-07-29.md` (SM1 + Fan-as-validity-probe §3 Top-3 #2) · `pm/50_audits/CRT_3agent_method_review_synthesis_2026-07-29.md` (#9 + Fan-as-validity-probe). Test: TESTS QUEUE #9.

## R10 · "The coded object presents a misleading neutrality — it should preserve disagreement, alternative codings, provenance, and versioning rather than presenting one canonical analysis; it is better understood as a *versioned argument about the text* than a settled graph." *(IRR224 5-LLM: STRONG-MAJORITY 4/5 SM6; reflexive self-critique gap `f382fae9bc`)*
**Response.** We take this as a design mandate rather than a defeater, and note a real tension with our own §2.13 (single store of record): §2.13 exists so canonical data lives in one queryable place, but SM6 warns that a single canonical *coding* erases the history of interpretation. These are reconcilable — the store of record should be the **Representation Ledger**: one authoritative table whose rows each carry evidence-span · annotation status (explicit / inferred / historically-reconstructed / generated / disputed) · calibrated confidence · provenance · **alternative codings** · loss note. That preserves disagreement *inside* the single store, so a morphospace point becomes a confidence region and a Compare spine becomes a set of possible alignments. It is the round's #1 generative convergence and buildable on the existing store — but not yet built.
**Status.** **OPEN.** The reconciliation (versioned ledger inside the single store) is designed and answers the SM6 + §2.13 tension in principle; no implementation yet. See TESTS QUEUE #10.
**Evidence.** `research/00_irr/irr224_..._reconciliation_2026-07-29.md` (SM6 + Representation Ledger §3 Top-3 #1) · `pm/50_audits/REFLEXIVE_OUTPUT_instrument_reads_itself_2026-07-29.md` (gap `f382fae9bc`, "coded object installed as scripture") · §2.13 (single store of record — the tension). Test: TESTS QUEUE #10.

## R11 · "The 5-slot move-grammar is an a-priori ontology, not neutral scaffolding — agent→operation→substrate→outcome encodes an agentive/transitive/propositional (Western) metaphysics, so the grammar may *manufacture the cross-tradition convergence it claims to discover*. And this contradicts claim 11 ('categories validated by IRR, not a priori'): only the *fillers* are IRR-validated; the *frame* is fixed in advance." *(3-agent CRT: 3/3 #1 — "the deepest"; IRR224 5-LLM: STRONG-MAJORITY 4/5 SM2)*
**Response.** This is the sharpest blade in both reviews and it is distinct from R3 (which asks whether the grammar *fits* non-agentive texts). R11 asks whether, even where it fits, it *pre-decides* the Q2 convergence finding — the instrument "can only see the meaning its grammar is shaped to catch." We concede the frame/filler point: IRR validates the fillers, not the slot-ontology itself, so claim 11 overreaches as stated. Two answers, both currently designed rather than proven: (1) **Fan-as-validity-probe** (R9) is also the test *here* — if perturbing a slot changes the coding coherently, the coder is tracking the text, not re-imposing the frame; (2) the structural answer is to **pluralize the grammar into a "grammar of grammars"** — allow tradition-native (non-agentive, apophatic) frames, log a per-move "does-not-fit" **residual channel** → a *residual atlas*, and make the mapping-failure between grammars the object of study. Where the frame breaks is then a finding, not a hidden defect — which is the strongest available novelty claim and the honest response to the manufacturing charge.
**Status.** **OPEN.** We can state the concession precisely (frame ≠ fillers; claim 11 needs narrowing) but the falsification (Fan-probe) and the structural fix (grammar-of-grammars + residual atlas) are designed, not run. See TESTS QUEUE #9.
**Evidence.** `pm/50_audits/CRT_3agent_method_review_synthesis_2026-07-29.md` (#1 + grammar-of-grammars/residual atlas §3) · `research/00_irr/irr224_..._reconciliation_2026-07-29.md` (SM2 + §3 Top-3 #3) · cross-ref R3 (the fit question) + R9 (shared Fan-probe test). Test: TESTS QUEUE #9.

## R12 · "Neuro-symbolic *auditability* is not *validity* — a fully auditable, well-formed coding can be systematically wrong; the method emphasizes traceability more than construct validity, and the grammar↔LLM mapping is never exposed." *(IRR224 5-LLM: MAJORITY 3/5 M1; 3-agent CRT: 2/3 #8)*
**Response.** We agree and do not want to conflate the two. A well-formed but wrong coding passes the audit, so auditability buys *reproducibility and inspectability*, not *truth*. Our honest position is that construct validity has to come from *outside* the audit trail — the two mechanisms the reviews name (3/3 and 5/5 respectively): a small **human-expert / tradition-bearer gold anchor** that critiques the *categories*, not just the codings, plus an **inter-model error-correlation discount** on the IRR numbers (so shared-prior agreement is not read as validity — the R1 point). We also concede M1's second half: the concrete mapping between the grammar and the LLM prompt is not currently exposed, so "auditability" is still partly a promise.
**Status.** **OPEN.** Acknowledged squarely; the human-gold-anchor + error-correlation discount + exposed grammar↔prompt mapping are named fixes, none yet built.
**Evidence.** `research/00_irr/irr224_..._reconciliation_2026-07-29.md` (M1 + the reflexive-sting reading + human-anchor §3) · `pm/50_audits/CRT_3agent_method_review_synthesis_2026-07-29.md` (#8 + human-anchored independence-aware IRR) · cross-ref R1 (IRR ≠ validity). Test: relates to TESTS QUEUE #2 (statistical baseline / non-LLM reference) + a human-gold-anchor run (TESTS QUEUE #10 ledger carries the anchor).

## R13 · "What if your instrument just OVER-GENERATES gaps? Give a reader four layers and a dozen loci and it will always find plausible-sounding 'gaps' — you've built a generator, not an instrument." *(IRR225 5-LLM: UNANIMOUS 5/5 U9 — the over-fitting/over-generation worry every cohort raised)*
**Response.** We tested it with a **negative control** — a text *engineered to close* interpretive space, where a well-calibrated instrument should find almost nothing. The MIT License is the ideal trap: legal boilerplate is the opposite of scripture; a competent reuser needs almost nothing. If the instrument finds twenty "gaps" in a software license, the method is a generator. **Result: 12 candidates → ~81% DISCARDED by the eligibility gates; 2 clean survivors (+1 marginal).** And the survivors are precisely the MIT License's two genuinely famous silences — **patent-rights scope** (the silence Apache 2.0 exists to fix) and the undefined **"substantial portions"** threshold (its only affirmative obligation, unbounded). The gates killed every `anchor=stated` candidate (the "AS IS"/no-liability clauses — said, not withheld) and every *hookless* omission (governing-law, severability — the text is silent, but nothing in its words forks on them). The rule this crystallized, and it is R4's answer operationalized: **a gap is not "anything the text doesn't say" (that list is infinite) — it is "something the text's own words open but don't close."** Boundedness falls out of tying every gap to a textual hook (the `activation` gate + `textual_anchor`), so the same instrument finds ~10 gaps in Jonah and ~2 in a license.
**Status.** **ANSWERED (a run, not a claim) — the negative control PASSES.** First control run; the confirming scale-up is a diverse non-canonical corpus (legal / technical / expository), the same battery TESTS QUEUE #2 uses.
**Evidence.** `pm/50_audits/v3_overgeneration_probe_mit_license_s156_2026-07-30.md` (the run: ~81% discard, the 2 famous survivors, every discard named) · `research/00_irr/irr225_layered_gap_taxonomy_reconciliation_2026-07-30.md` (U9, 5/5) · `pm/40_architecture/INSTRUMENT_v3_spec_s156_2026-07-30.md` (the gates + `textual_anchor` that deliver the restraint) · cross-ref R4 (this is R4's unbounded critique, answered as a control). Test: TESTS QUEUE #13.

## R14 · "Aren't your critic panels just the generic 'act like Socrates / William James' personas everyone role-plays with an LLM?"
**Response.** No — and the difference is auditable. Our critics are **seeded with real, fetched text** and must critique *from that document*, not from the model's averaged impression of a name. We proved it with a bare-vs-seeded A/B on **one named critic (William James)**, glossing the same gap (Smallville's believability-metric confound). **Bare-James (from memory)** regressed to the mean of the name — "believability is *merely* subjective, discount it." **Seeded-James** (his actual text — *Varieties of Religious Experience*, Lect. III "The Reality of the Unseen") said the *opposite* and rerouted the critique: the "sense of reality" is a **real, primary faculty** that fires *hardest where nothing is present* (his hallucination case, "real in the most emphatic sense… neither seen, heard, touched") — so the believability metric measures a faculty **decoupled from actual presence**, making it *worse, not softer*. The real text **overruled the persona's instinct** — the same shape as when Gelman & Loken's actual paper overruled a stats-skeptic's "d=8.16 is too big = p-hacking" reflex. **The diff between the two arms IS the evidence that seeding works;** a bare named-persona is a prior-driven guess (flagged §13), a seeded critic is the thinker's *text*. And the panel COMPOSITION is itself a declared, reusable instrument-parameter (a named registry of panels; running ≥2 shows the critique is composition-dependent).
**Status.** **ANSWERED (a run) — bare-vs-seeded demonstrated on William James; the seed reversed the conclusion.** Repeatable on any named critic (Augustine, Socrates, …).
**Evidence.** `pm/50_audits/AB_bare_vs_seeded_william_james_s156_2026-07-30.md` (the two arms + the fetched quotes) · `pm/50_audits/smallville_20critic_rooms_s156_2026-07-30.md` (Panel C seeded critics — the Gelman overrule) · `pm/30_methodology/GLOSS_process_steps_with_seeding_s156_2026-07-30.md` + `CRIT_PANEL_REGISTRY_s156_2026-07-30.md` (the seeding step + the named-panel registry) · MASTER_LEXICON Gloss entry (SEEDING lock).

## R15 · "Could this be used outside meaning-making — can it find real research gaps?"
**Status.** **ANSWERED (a run) — honestly bounded.** We ran the instrument blind on a foundational tech paper (Park et al., "Smallville," arXiv 2304.03442). The honest finding, per our fair-baseline (T3) test: on a *tech* paper — the LLM's home turf — a strong wild read finds the gap-list on its own, so gap-*finding* is not where a structured instrument wins. What the **seeded** instrument adds, and a cold read cannot, is the **rival model** (the ACT-R critic: Smallville's exponential recency-decay is the *wrong functional form* against 50 years of validated human-memory data — "the knob is the wrong shape," not "tune the knob"), the **paradigm-exit critics** (Suchman / Weizenbaum / Turing / Blake), and **auditable multi-panel disagreement**. Full write-up (the exec summary + the gap-list, honestly labeled): [Research-Gap Demo — Smallville &rarr;](research-gap-smallville.html).

## R16 · "How do you know these are the *right* axes — are they a-priori or induced, and doesn't a fixed axis-set launder judgment?"
**Status.** **ANSWERED (a run) — with an honest corpus caveat.** The axes are **empirically graduated**, not asserted. A proposed new axis must clear three gates — **recurrence** (does it recur?), **orthogonality** (does it spread independently of the existing axes, or just correlate?), and **coherence** (one dimension, not several lumped?) — then a researcher CLC lock; the default is **bundle** and the bar for a new axis is high. First live test: the single strongest new-axis candidate in the 795 proposals, **eschatological-temporality**, still **BUNDLED** — it co-loads with revelation + telos rather than spreading independently, so the eight are conservative and earned. Honest caveat (§2.8): that orthogonality test is corpus-limited (13/14 cluster reads Abrahamic, n=14), so the narrow *structure-of-historical-time* residue is **deferred** for re-test as more non-Abrahamic / cyclic-time material is coded, not dropped. This answers the axis-derivation half of R8. See the **Frame** drawer + `AXIS_candidate_graduation_MECE_method`.

---

# TESTS QUEUE (designed / partially-run — the experiments that back future entries)
1. **A/B — raw text vs. decomposed process** *(the cleanest value-of-the-instrument test the PI wants).* Same text
   (Romans 8:28-30), same critic panel: Arm A gets the *raw text* + "where is the unsaid? give commentary." Arm B gets
   our *decomposed* object (moves · gaps · the compatible questions). Compare the gap/commentary sets. Most-scientific
   shape: hold the panel + text fixed, vary ONLY the instrument; pre-register what "better" means (does B surface
   text-specific, historically-attested gaps that A misses / does A produce more associative-prior noise). This is the
   controlled version of the IRR224 CRT.
2. **Statistical baseline for R1** — is 26% strict / 71% lenient unanimity *higher than chance*? Null models to compare:
   (a) random bucket assignment; (b) a NON-LLM reference baseline — do encyclopedias / standard reference works "agree"
   at what rate on the same demarcation questions? Establishes whether the LLM consensus rate is elevated vs. a
   non-LLM knowledge source. (The "other ~3–5%" = rounds where the models *mostly disagree*.)
3. **Reliability CRT on the meta-analysis itself** — 3 independent agents re-tally the same 307-doc IRR corpus; compare
   their counts. Tests that R1's numbers are reproducible, not one parse's artifact.
4. **Gap → reception overlay (Romans 8:29)** — show that our *gaps* (the unsaid slots) sit where interpreters
   *historically divided* (Augustinian/Arminian/Orthodox on 8:29). This is R-for-"our gaps are the seeds of the later
   disputes" — needs a viz (our gap-map overlaid on the documented dispute record). See gap_seed_ranking_type_compat.
5. **Non-Western grammar-fit** — run the built instrument on a representative non-agentive/apophatic text; confirm it
   codes via different values/nulls (not breakage). Backs R2(b).
6. **Free-form vs. process — SIDE BY SIDE** (not a summary) — lay the 5-LLM free-form gap-lists next to our systematic
   151, actual output vs. actual output, so the PI can see the strengths of each directly. (Partly in the IRR224
   reconciliation; the PI wants the raw side-by-side.)
7. **Edge-typology formalization + assignment-agreement** *(backs R5 — currently OPEN).* Enumerate the complete edge-type
   set, sort by theoretical register (logical / semantic-pragmatic / method-defined), state assignment rules + whether the
   set is exhaustive / mutually exclusive, then measure inter-coder (and inter-model) agreement on *edge-typing* specifically.
   Turns the "…" that all 5 IRR224 cohorts flagged into a closed, testable inventory.
8. **Segmentation stopping-rule + separated reliability** *(backs R6 — OPEN on the rule).* (a) State an atomicity rule
   (when is a move atomic vs. a composition — the mustard-seed case); (b) measure *segmentation* reliability separately
   from *label* reliability on the same passages, so an IRR number stops conflating boundary-disagreement with
   coding-disagreement. Pre-register the atomicity rule before measuring.
9. **Fan-as-validity-probe / intervention-based validation** *(backs R9 + R11 — the per-move falsification).* Perturb ONE
   slot of a coded move (flip agent, remove a warrant, reverse polarity) and test whether the coding changes *coherently
   in the predicted slot* and not elsewhere. Confirms the coder tracks the TEXT, not its priors — gives the
   domain-generality claim (R9) and the grammar-manufactures-convergence charge (R11) a real falsification. High leverage,
   low cost (re-purposes the Fan output the instrument already has).
10. **Representation Ledger build + false-neutrality test** *(backs R7 / R10 / R12 — OPEN).* Build the versioned lattice
    INSIDE the single store of record (§2.13): each annotation carries evidence-span · status (explicit / inferred /
    reconstructed / generated / disputed) · calibrated confidence · provenance · **alternative codings** · loss note, plus a
    slot for the human-expert / tradition-bearer gold anchor. Test: does preserving disagreement change downstream outputs
    (does a morphospace point become a region, a Compare spine a set of alignments)? Resolves the SM6 ↔ §2.13 tension.
11. **Morphospace axis-derivation audit + coordinate reliability** *(backs R8 — OPEN half).* (a) State whether each axis is
    a-priori or induced and what constitutes adequacy-N (the "ninth axis" model-selection test: does a candidate axis add
    discriminative information after conditioning on the existing eight); (b) measure inter-coder *coordinate* reliability
    (do different coders place the same text near the same coordinates); (c) enforce the declared-profile-vs-derived-geometry
    separation (survey §5) as an audit invariant so geometry never over-claims metric structure the ontology lacks.
12. **Gap salience / contrast-set operationalization + silence typology** *(backs R4 — OPEN implementation).* Operationalize
    CLOSED + CONTRASTIVE gaps at scale: a gap must cite the parallel text / tagged paradigm where the role IS filled (the
    obligation), per IRR167 present-vs-obligated. Then test that scored gaps track the contrast set, not the model's
    associative priors (e.g., swap the coding model; do the high-salience gaps stay put?). Add the silence typology
    (presupposed / taboo / ineffable / generic-convention) so "productive silence" is not miscounted as a defect.
13. **Over-generation NEGATIVE CONTROL — ✅ RUN (not designed).** *(backs R13; IRR225 U9.)* Run the instrument on a text
    ENGINEERED to close interpretive space (a legal/expository boilerplate), where a well-calibrated instrument should find
    almost nothing. **First run: MIT License → ~81% of candidates DISCARDED by the gates; 2 clean survivors (patent scope,
    "substantial portions") = the license's real famous silences.** The control PASSES — the instrument restrains, it does
    not generate. Unlike #1-#12, this test has a RESULT already. Confirming scale-up: a diverse non-canonical corpus (legal /
    technical / expository), shared with the #2 baseline battery. Evidence: `pm/50_audits/v3_overgeneration_probe_mit_license_s156_2026-07-30.md`.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: reading-SB S156 2026-07-29 — the PI asked for a running FAQ/rebuttals list (Lamberth/Saquib/crit-group
  objections → our response → links to the tests). R1-R3 = the original entries (5-IRR-isn't-5; non-linear text /
  Constellation; grammar-fit). R4-R12 appended 2026-07-30 (reading-SB, no nested agents) by harvesting the recent
  reflexive/CRT/5-LLM method reviews: IRR224 (frontier 5-LLM free-form critique) + the in-house 3-agent CRT synthesis +
  the instrument's own reflexive self-scan + the GPT tooling survey. Each new entry = objection (with source + cohort
  strength) → our response (from our own materials) → Status (honest ANSWERED / PARTIAL / OPEN per §13) → Evidence + test.
  Six new tests (7-12) added to the TESTS QUEUE for the OPEN entries. R1-R3 not rewritten.
SCHOLARLY SOURCES: IRR_consensus_meta_analysis + FINDING_irr_consensus_task_dependence (R1); the Constellation output +
  irr157/218/139/142/158 (R2/R3); `research/00_irr/irr224_reflexive_method_freeform_review_reconciliation_2026-07-29.md`
  (R4-R12 — U2/U3/SM1-SM6/M1 buckets + the generative Representation-Ledger / Fan-probe / grammar-of-grammars fixes);
  `pm/50_audits/CRT_3agent_method_review_synthesis_2026-07-29.md` (the 3/3 convergent critiques); `pm/50_audits/
  REFLEXIVE_OUTPUT_instrument_reads_itself_2026-07-29.md` (gap f382fae9bc — coded-object-as-scripture, backs R7/R10);
  `researchsurvey_gpt.txt` §4-§5 (declared-vs-derived geometry, backs R8); §2.14 + IRR167 (present-vs-obligated, backs
  R4/R9); §2.13 (single store of record — the R10 tension); §2.8 (bias-visibility — the reflexive-sting reading).
WHAT NEEDS VERIFICATION: six of the nine new entries are marked OPEN (no strong answer yet) — R5 (edge typology) is fully
  OPEN; R6/R7/R10/R11/R12 are OPEN on their core fix; R4/R8/R9 are partially answered. All 12 TESTS QUEUE items are
  designed, not all run; tests 7-12 need pre-registration of their success criteria before running. SM2 was scored 4/5
  with Solar ADJACENT in the IRR224 reconciliation — R11's "4/5" inherits that caveat. -->
