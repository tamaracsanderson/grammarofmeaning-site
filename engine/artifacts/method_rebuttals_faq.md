<!--
═══════════════════════════════════════════════════════════════════════════════
RENDERER NOTE FOR DESIGN-SB — this rework changes the document STRUCTURE, so the
current renderer (grammarofmeaning-site/engine/rebuttals.html) will need updating
before this file can go live. What the renderer must now handle:

  1. THEMED SECTIONS. Questions used to be flat, headed `## R\d · "objection"`.
     They are now grouped under seven THEME headers (`## Theme name`), each with a
     one-line italic intro, and each question is a `### ` sub-heading. The parser
     that does `mainMd.split(/\n##\s+(?=R\d)/)` must change to: walk `## ` theme
     sections, then split each on `### ` for the question units.

  2. QUESTION IDs NOW INCLUDE S-CODES. Entries are `### R4 · question?` (the 16
     originals, R1–R16, IDs preserved for traceability) AND `### S1 · question?`
     (seven NEW schema questions, S1–S7). The current `(head.match(/^R\d+/))`
     regex must widen to `/^[RS]\d+/` or it will drop every S-entry.

  3. MARKDOWN LINKS IN EVIDENCE + TESTS QUEUE. Evidence used to be raw path
     strings; every citation is now a real Markdown link `[label](path)`. The
     renderer already runs `marked.parse`, so links will render — BUT the Evidence
     hrefs point at twelve-laws REPO paths (research/00_irr/…, pm/50_audits/…) that
     are NOT deployed to the site. Design-SB must decide the final href target:
     (a) point at a repo browser, (b) host the audit docs, or (c) keep the readable
     label and drop the href. Site-relative links (research-gap-smallville.html)
     already resolve.

  4. STATUS + EVIDENCE ARE NOW SINGLE CONSISTENT LABELS. The old parser looked for
     `**Response.**`, `**Status.**`, `**Evidence.**`. There is no more `**Response.**`
     label — the answer prose simply follows the question heading. Each entry ends
     with exactly one `**Status —**` line and one `**Evidence —**` line. Update the
     three body regexes (resp/status/evid) accordingly; the answer is
     "everything between the heading and the `**Status —**` line."

  5. COHORT-STRENGTH TAGS MOVED OUT OF THE HEADING. Strength markers (e.g.
     "IRR224 5/5 U2", "3-agent CRT 3/3 #1") used to live in the `## R\d ·` heading;
     they now live in the answer prose. If the renderer scraped them from the
     heading, it must read them from the body (or ignore them).

  The section names `# How to read this` and `# TESTS QUEUE` are UNCHANGED (still
  H1) so those two anchors survive.
═══════════════════════════════════════════════════════════════════════════════
-->
---
title: "Method FAQ — the hard questions about the instrument, our answers, and the test behind each"
date: 2026-08-01
session: "S156 origin (reading-SB, PI-directed); S157 rework — re-themed into a Q&A FAQ, plain-language rewrite, seven schema questions added, citations turned into links (reading-SB)"
status: LIVING defense artifact. For every question an advisor or crit-group member (Lamberth, Saquib, the CRT
  group) is likely to ask, this gives (1) the question in plain form, (2) a direct answer, and (3) a link to the
  actual run that backs it. Honesty is the whole point — each answer carries its real status (ANSWERED / PARTIAL /
  OPEN) and never inflates one into another. The TESTS QUEUE at the bottom holds the experiments still to run.
---

# How to read this

These are the hardest questions people ask about the instrument — from us, from the five-LLM review cohorts, from the twenty-agent meta-critique of our own process, from advisors (Lamberth, Saquib), and from the frontier engines when we probe how novel the method is. Each entry is a plain **question**, a plain **answer**, and a **link to the run** that backs it. The answers are not assertions — they point at experiments.

Every answer carries an honest status:

- **ANSWERED** — a real run backs this, not just an argument.
- **PARTIAL** — part of it is answered by a run; part is still open, and we say which.
- **OPEN** — a fair hit. We can name the fix precisely, but we have not built or run it yet.

Where the backing test is *designed but not yet run*, it lives in the [TESTS QUEUE](#tests-queue) at the bottom, not in the answered column above.

The questions are grouped by **theme**, not by the order we discovered them. Seven themes, roughly following the instrument itself: how it cuts a text into moves; what it says about the unsaid; the eight-axis map; whether the numbers mean anything; the reader's place in all this; whether it generalizes or just fits anything; and the critic panels. Question IDs (R1–R16, and the newer schema questions S1–S7) are kept only so each answer stays traceable to its evidence.

---

## 1 · The move-grammar — how we cut a text into "moves"

*The instrument's first act is to break a text into moves (one operation with its parts: who does what, to what, with what result) and draw typed edges between them. These questions ask whether that cut is principled or imposed.*

### R3 · Your move-grammar looks Western and action-oriented. Does it even fit non-agentive or apophatic traditions?

It fits without needing a different grammar — by using different values, explicit nulls, and per-domain axis-weights in the *same* slots, not by rebuilding the ontology. This was designed in when the slots were chosen: a non-agentive or apophatic text fills the same slots with different fillers (or marks them empty), and the per-domain importance prior weights them differently. The grammar bends rather than breaks. The confirming run — the built instrument taken end-to-end through a representative non-Western text — is the piece still owed.

**Status —** Answered in principle; confirming run OPEN (see [TESTS QUEUE #5](#tests-queue)).
**Evidence —** [irr157 — negative-space grammar grounding](research/00_irr) · [irr218 — per-domain axis importance](research/00_irr) · irr139 / irr142 / irr158.

### R5 · What exactly are your edge types? "presupposes, entails, fills, …" — is that set complete, exclusive, and rule-governed, or is the "…" hiding the hard part?

This one we do **not** yet have a strong answer to, and all five review cohorts caught it. We do not publish a closed edge-type set with formal assignment rules, nor a rigorous graph-theoretic description of the model underneath. The ellipsis in our own method statement is doing real concealment. The honest position: the edge inventory grew bottom-up ("fit or extend"), and has not been frozen, sorted by theoretical register (logical vs. semantic-pragmatic vs. method-defined), or tested for whether two coders type the same edge the same way. The fix is a formalization pass — enumerate the set, sort by register, state the rules, then measure agreement on edge-typing.

**Status —** OPEN. No strong answer yet.
**Evidence —** [IRR224 reconciliation — U3, unanimous 5/5](research/00_irr/irr224_reflexive_method_freeform_review_reconciliation_2026-07-29.md). No test exists yet → [TESTS QUEUE #7](#tests-queue).

### R6 · When does a move stop? Is "the kingdom of heaven is like a mustard seed" one move or three? Without a stopping rule, the grain of every downstream coordinate is arbitrary.

We accept there is no justified atomicity rule today, and the sharpest version of the objection bites: forcing one-operation-per-move may raise reliability while *lowering* validity — the grammar risks "discovering" the discreteness it imposed. Our partial answer is the fix the in-house critique named: **report segmentation reliability separately from label reliability**. That way an inter-rater number stops silently mixing two different disagreements — "we disagree on where the move boundary is" versus "we disagree on how to code the same unit." That separation makes the problem visible and measurable. It does not yet supply the stopping rule itself.

**Status —** PARTIAL — the two reliabilities can be separated; OPEN on the atomicity rule.
**Evidence —** [IRR224 reconciliation — SM4, 4/5](research/00_irr/irr224_reflexive_method_freeform_review_reconciliation_2026-07-29.md) · [3-agent CRT synthesis — #5, the separated-reliability fix](pm/50_audits/CRT_3agent_method_review_synthesis_2026-07-29.md). Test: [TESTS QUEUE #8](#tests-queue).

### R11 · Isn't the five-slot grammar (agent → operation → substrate → outcome) itself a Western, action-first metaphysics? If so, it might *manufacture* the cross-tradition convergence it claims to discover — and that contradicts your claim that the categories are validated by inter-rater reliability, not chosen in advance.

This is the deepest objection in both reviews, and it is different from R3. R3 asks whether the grammar *fits* a non-agentive text. R11 asks whether, even where it fits, it *pre-decides* the answer — the instrument "can only see the meaning its grammar is shaped to catch." We concede the frame-versus-filler point: inter-rater reliability validates the *fillers* we put in the slots, not the *slot-ontology* itself, so the claim "categories validated, not a priori" overreaches as stated and needs narrowing. Two answers, both currently designed rather than proven. First, the **Fan-as-validity-probe** (see R9): if perturbing one slot changes the coding *coherently*, the coder is tracking the text, not re-imposing the frame. Second, the structural fix — **pluralize into a "grammar of grammars":** allow tradition-native (non-agentive, apophatic) frames, log a per-move "does-not-fit" residual, and collect those residuals into an atlas. Then the places where the frame *breaks* become the finding, not a hidden defect — which is both the strongest novelty claim and the honest response to the manufacturing charge.

**Status —** OPEN. The concession is stated precisely; the falsification (Fan-probe) and the structural fix (grammar-of-grammars + residual atlas) are designed, not run.
**Evidence —** [3-agent CRT synthesis — #1 "the deepest," grammar-of-grammars](pm/50_audits/CRT_3agent_method_review_synthesis_2026-07-29.md) · [IRR224 reconciliation — SM2, 4/5](research/00_irr/irr224_reflexive_method_freeform_review_reconciliation_2026-07-29.md). Cross-refs R3 (the fit question) and R9 (the shared Fan-probe test). Test: [TESTS QUEUE #9](#tests-queue).

### S1 · Engine 1 says it returns "a graph of typed edges between moves." Do you actually analyze that graph as a network — centrality, motifs, cross-text structure — or just store it?

Right now, mostly store it, with one exception. The move-graph exists in the data (`source_move_edge`), and the Seed-Ranking stage already uses one edge relation seriously: it ranks moves by "ripple" — the transitive closure of a move's dependents — to find the move whose flip reorganizes the most, which then feeds the Fan output. So there is genuine graph computation, but it is narrow (one dependency relation, one ranking use). The broader network analysis a citation-network methodologist would expect — node centrality, recurring motif subgraphs, structure *across* texts — is not built. It is a natural and cheap extension once the edge typology (R5) is frozen, because motif-finding is only meaningful over a closed, reliably-typed edge set.

**Status —** PARTIAL — dependency-ripple ranking is built and in use; general network analysis is not. Gated on R5's edge formalization.
**Evidence —** the Seed-Ranking stage (move-seed = ripple over the DEPENDS graph) in the [engine schema](https://grammarofmeaning.org/engine/schema.html) · cross-ref R5. Relates to [TESTS QUEUE #7](#tests-queue).

---

## 2 · Said vs. unsaid — gaps and seams

*The instrument names not only what a text says but what it leaves unsaid-yet-in-play. A "gap" is a question the text's own words open at the move layer and don't close; a "seam" is a tension between layers. The worry is obvious: everything leaves infinitely much unsaid.*

### R4 · Every sentence leaves infinitely many things unsaid. Doesn't "gap-scoring" just measure the model's own associations, not the text?

We accept the charge exactly as stated: an *open* notion of "gap" measures the coder's imagination, not the text. Our answer is the fix both review cohorts independently converged on — make gaps **closed and contrastive**. A gap is no longer "anything you could conceive as missing." It is "a role that *is* filled in a parallel text or the tagged paradigm, and is empty *here*." The contrast set supplies an *obligation*, which is what turns an infinite absence into a single scored, falsifiable one. This is not a bolt-on: it is the same present-versus-obligated distinction an earlier study (IRR167) already surfaced — coders readily agree a silence is *present* (α ≈ 0.59) but not that it is *obligated* (α ≈ 0.03), and the contrast set is precisely what supplies the missing obligation. The frontier cohort also sharpened the target: some silence *functions* (apophatic protection, trauma, esoteric reticence), so the fix must carry a **silence typology** (presupposed / taboo / ineffable / genre-convention) rather than treating every absence as a defect.

**Status —** ANSWERED IN PRINCIPLE, OPEN IN IMPLEMENTATION. The contrast-set fix is named, converged on 3/3, and reproduced 5/5, but is not yet operationalized at scale; the silence typology is proposed, not built.
**Evidence —** [IRR224 reconciliation — U2, unanimous 5/5](research/00_irr/irr224_reflexive_method_freeform_review_reconciliation_2026-07-29.md) · [3-agent CRT synthesis — #2, the contrast-set fix](pm/50_audits/CRT_3agent_method_review_synthesis_2026-07-29.md) · [IRR167 — present-vs-obligated split](research/00_irr/irr167_beatles_coding_method_reconciliation_2026-07-19.md) (project invariant §2.14). Test: [TESTS QUEUE #12](#tests-queue).

### R13 · What if the instrument just *over-generates* gaps? Give it four layers and a dozen loci and it will always find plausible-sounding "gaps." Haven't you built a generator, not an instrument?

We tested this with a **negative control** — a text engineered to *close* interpretive space, where a well-calibrated instrument should find almost nothing. The MIT License is the ideal trap: legal boilerplate is the opposite of scripture, and a competent reuser needs almost nothing from between its lines. If the instrument finds twenty "gaps" in a software license, it is a generator. The result: 12 candidates went in, roughly **81% were discarded by the eligibility gates, leaving 2 clean survivors (plus one marginal).** And the survivors are exactly the MIT License's two genuinely famous silences — the scope of **patent rights** (the very silence Apache 2.0 exists to fix) and the undefined **"substantial portions"** threshold (its only affirmative obligation, left unbounded). The gates killed every candidate whose content was *stated* (the "AS IS" / no-liability clauses — said, not withheld) and every omission with *no textual hook* (governing law, severability — the text is silent, but nothing in its own words forks on them). This crystallized the rule that operationalizes R4: **a gap is not "anything the text doesn't say" (that list is infinite) — it is "something the text's own words open but don't close."** Boundedness falls out of tying every gap to a textual hook, so the same instrument finds ~10 gaps in Jonah and ~2 in a license.

**Status —** ANSWERED (a run) — the negative control PASSES. This is the first control run; the confirming scale-up (a diverse non-canonical corpus: legal / technical / expository) is the same battery [TESTS QUEUE #2](#tests-queue) uses.
**Evidence —** [MIT-License over-generation probe — the run, ~81% discard, the 2 famous survivors](pm/50_audits/v3_overgeneration_probe_mit_license_s156_2026-07-30.md) · [IRR225 reconciliation — U9, unanimous 5/5](research/00_irr/irr225_layered_gap_taxonomy_reconciliation_2026-07-30.md) · [Instrument v3 spec — the gates + textual_anchor that deliver the restraint](pm/40_architecture/INSTRUMENT_v3_spec_s156_2026-07-30.md). Cross-ref R4. Test: [TESTS QUEUE #13](#tests-queue).

### S5 · Your schema splits the unsaid into GAP (in-text) and SEAM (between layers). Can coders actually agree which is which — and doesn't a "seam" between, say, Sitz and Move risk being an artifact of your own layering rather than something in the text?

Fair, and untested. The distinction is real and load-bearing in the schema: a GAP lives inside the move layer (the text's own words open a question and don't close it), while a SEAM is a tension *between* layers the instrument itself imposes (setting vs. move, paradigm vs. move). The honest risk is exactly the one you name — because the layers are ours, a "seam" could be an artifact of how we sliced the text, not a feature of the text. We have not measured whether two coders (or two models) agree on GAP-versus-SEAM labeling, and until we do, the seam category is more vulnerable to the R4 associative-priors charge than the (now closed-and-contrastive) gap category is. It should be folded into the same present-versus-obligated reliability test, with SEAM held to the stricter bar since it depends on our layering.

**Status —** OPEN. The distinction is defined; inter-coder reliability on GAP-vs-SEAM is not measured.
**Evidence —** the Gaps stage (GAP vs. SEAM definition, the salience × visibility 2×2) in the [engine schema](https://grammarofmeaning.org/engine/schema.html) · cross-refs R4 and R6. Relates to [TESTS QUEUE #12](#tests-queue).

---

## 3 · The morphospace — the eight axes

*We place each text on eight "frame" axes (its angle on its subject: how it knows, what it commits to, where it's headed, and so on). The worry is that a coordinate can launder a judgment call beneath false geometric precision.*

### R8 · Are the axes chosen in advance or discovered from data? How many axes count as "enough"? And doesn't a "coordinate" dress up a judgment as geometry — couldn't two coders land a text in completely different places?

Partly answered, honestly. On the false-precision half we do have a real handling: keep the **declared** categorical values (the eight-row fingerprint) visibly separate from any **derived** 2-D geometry (a projection over an explicitly documented distance model), and never let a smooth interface make the ontology look more metric than it is — we refuse radial or spectrum encodings wherever the values are not genuinely ordered. On the "points vs. clouds" charge we have empirical backing: **78% of texts pick multiple values on the axes**, so a text is already represented as a *region*, not a single point — the data and the critique agree. What remains unanswered is the *derivation* question (a-priori vs. induced, and how many axes constitute adequacy) and coder-to-coder coordinate reliability. R16 answers the derivation half; the reliability half is still owed.

**Status —** PARTIAL — false precision handled (declared/derived split + 78% multi-pick); OPEN on axis derivation, adequacy-N, and inter-coder coordinate reliability.
**Evidence —** [IRR224 reconciliation — SM5, 4/5](research/00_irr/irr224_reflexive_method_freeform_review_reconciliation_2026-07-29.md) · [3-agent CRT synthesis — #7, the 78%-multi-pick finding](pm/50_audits/CRT_3agent_method_review_synthesis_2026-07-29.md) · [GPT tooling survey — §5 declared-vs-derived geometry](researchsurvey_gpt.txt). Test: [TESTS QUEUE #11](#tests-queue).

### R16 · How do you know these are the *right* axes — and doesn't a fixed axis-set launder judgment?

The axes are **empirically graduated**, not asserted. A proposed new axis has to clear three gates — **recurrence** (does it keep showing up?), **orthogonality** (does it spread independently of the existing axes, or just correlate with them?), and **coherence** (is it one dimension, not several lumped together?) — and then a researcher lock. The default is to **bundle** a candidate into an existing axis; the bar for minting a new one is deliberately high. The first live test: the single strongest new-axis candidate out of 795 proposals, *eschatological-temporality*, still got **bundled** — it co-loads with revelation and telos rather than spreading on its own, so the eight axes are conservative and earned, not padded. Honest caveat: that orthogonality test is corpus-limited (13 of 14 cluster reads Abrahamic, n=14), so the narrow *structure-of-historical-time* residue is **deferred** for re-test as more non-Abrahamic and cyclic-time material is coded — deferred, not dropped. This answers the derivation half of R8.

**Status —** ANSWERED (a run) — with an honest corpus caveat.
**Evidence —** the Frame drawer in the [engine schema](https://grammarofmeaning.org/engine/schema.html) · the axis-graduation method (recurrence / orthogonality / coherence gates) · project invariant §2.8 (bias-visibility, the n=14 caveat).

### S4 · Your Frame stage says "eight frame axes" but then names only seven letters, and notes that three axis letters don't even match their own names. Which is it — seven or eight? And doesn't a live naming drift undercut "the axes are earned"?

You are reading the schema honestly, and yes, there is a documented inconsistency: the field description says *eight* axes, enumerates *seven* letter-codes (E / O / I / T / S1 / S2 / G), and flags that three of those letters are mid-migration to new names (for example, ground-world-relation → relational-topology). This is housekeeping debt — an un-migrated rename tracked as a lock item — not a claim about which axes are valid. The graduation argument in R16 is about *whether* a dimension earns its place; this is about *what we've finished calling* the dimensions we kept. It is a fair ding on the schema's polish, and it is exactly the kind of drift the instrument's own reflexive scan is meant to surface. It should be reconciled before defense so the count and the labels stop contradicting each other on the page.

**Status —** OPEN (housekeeping). A naming/migration debt, self-flagged in the schema; it does not touch axis validity (R16).
**Evidence —** the `axis_name` field description in the [engine schema](https://grammarofmeaning.org/engine/schema.html) (the self-flagged seven-vs-eight and letter-mismatch note).

---

## 4 · Do the numbers mean anything — reliability & validity

*We use a five-LLM inter-rater panel and an auditable trail instead of human raters. Two questions cut deepest: are five models really independent judges, and does a well-formed audit trail actually mean the coding is true?*

### R1 · Your five-LLM inter-rater panel isn't five independent judges — they share training data and RLHF, so their agreement is *shared bias*, not signal.

We agree it isn't five independent humans — and instead of denying it, we measured it. Across **307 inter-rater reconciliation documents**, agreement is **task-dependent**: the models converge when the task is *enumeration* (gathering substance — about 42% unanimous) and diverge when the task is *demarcation* (drawing coding boundaries — the lowest unanimity, splitting around 29%). If the agreement were pure shared bias, it would *not* track task difficulty like that — so the *pattern itself* is signal. Practically, it tells us where to trust the instrument (enumeration) and where a human gold-anchor is required (coding and judgment). The null result ("they share training") becomes a finding ("and here is the *shape* of when that matters"). As a bonus, the passage-coding divergence independently reproduces, at corpus scale, the present-versus-obligated reliability split we saw in IRR167.

**Status —** ANSWERED (measured). Secondary tests (a statistical chance-baseline; a reliability re-tally) are queued.
**Evidence —** [IRR consensus meta-analysis](pm/50_audits/IRR_consensus_meta_analysis_s156_2026-07-29.md) · [the finding write-up — consensus task-dependence](pm/50_audits/FINDING_irr_consensus_task_dependence_s156_2026-07-29.md). Follow-ups: [TESTS QUEUE #2](#tests-queue) and [#3](#tests-queue).

### R12 · Auditability isn't validity. A fully traceable, well-formed coding can still be systematically wrong — you emphasize traceability more than construct validity, and you never expose the grammar-to-LLM mapping.

We agree, and we do not want to conflate the two. A well-formed but wrong coding passes the audit, so auditability buys *reproducibility and inspectability*, not *truth*. Construct validity has to come from *outside* the audit trail, and the two reviews named the two mechanisms for it: a small **human-expert / tradition-bearer gold anchor** that critiques the *categories* themselves (not just individual codings), plus an **inter-model error-correlation discount** on the reliability numbers (so shared-prior agreement is not read as validity — the R1 point). We also concede the second half: the concrete mapping between the grammar and the LLM prompt is not currently published, so "auditability" is, for now, still partly a promise.

**Status —** OPEN. Acknowledged squarely; the human gold-anchor, the error-correlation discount, and the exposed grammar-to-prompt mapping are named fixes, none yet built.
**Evidence —** [IRR224 reconciliation — M1, 3/5, plus the human-anchor proposal](research/00_irr/irr224_reflexive_method_freeform_review_reconciliation_2026-07-29.md) · [3-agent CRT synthesis — #8, human-anchored independence-aware reliability](pm/50_audits/CRT_3agent_method_review_synthesis_2026-07-29.md). Cross-ref R1. Relates to [TESTS QUEUE #2](#tests-queue) and [#10](#tests-queue) (the ledger carries the human anchor).

### S3 · Several schema fields are declared but never filled — year_estimate is always NULL, cohort_support and retraction_note are 0 of 306 rows, closure_type is populated for one text only. Is the published schema partly aspirational — structure you show but don't compute?

Yes, in places, and the schema says so on its own face — those fields carry ⚠ / caveat markers rather than pretending to be live. The honest picture: `year_estimate` stays NULL because the model response has no field to catch an estimated date, so it's discarded; `cohort_support` and `retraction_note` on moves have no writer yet (0 of 306); `closure_type` is populated for one text (SLY-1963) and NULL everywhere else. This is disclosed, not hidden — but it does mean the published schema currently overstates what is *computed* versus what is *scaffolded*. The right reading is that the schema is the target shape and the caveats are the honest delta; a defense-grade version should either wire these fields or visibly demote them, so a reader can't mistake a declared column for a filled one. This is the same discipline as R12: traceability includes being explicit about what the trail does *not* yet contain.

**Status —** PARTIAL — honest self-disclosure. Some fields are declared-but-unwritten and marked as such; wiring-or-demoting them is owed before defense.
**Evidence —** the ⚠ / caveat annotations on `year_estimate`, `cohort_support`, `retraction_note`, `closure_type` in the [engine schema](https://grammarofmeaning.org/engine/schema.html) · project invariant §2.13 (single store of record).

### S6 · The schema says each of the six recompositions (Fan, Resituation, Gloss, Reception, Comparison, Constellation) "changes what it means." How do you know a recomposition is a valid reading of the text and not a plausible hypothetical the text can't actually support?

We don't yet score it, and we shouldn't pretend otherwise. The six outputs are **generative by design** — they produce alternatives (Fan), the text under a changed world (Resituation), commentary on its silences (Gloss), its history of readings (Reception), its variants across tellings (Comparison), and its non-linear field of recurrences (Constellation). Each is a hypothesis-*producing* move, and each currently stands on worked examples (the Stein Constellation, the Beatles and Romans runs), not on a validity score. Validity of a recomposition is exactly what the **Fan-as-validity-probe** (R9 / TESTS QUEUE #9) is meant to establish: perturb one slot and check the recomposition changes *coherently and only where predicted*. Until that runs, the outputs are demonstrated and inspectable but not validity-graded — which is the honest status to give a reader before they lean on a Resituation as if it were a reading the text licenses.

**Status —** OPEN. Outputs are demonstrated, not validity-scored; the Fan-probe is the intended test.
**Evidence —** the six OUTPUT stages in the [engine schema](https://grammarofmeaning.org/engine/schema.html) · cross-ref R9. Test: [TESTS QUEUE #9](#tests-queue).

---

## 5 · The reader — positionality and the coded object

*The method models what happens inside the text. These questions ask about what it leaves out: the reader who completes the meaning, and the coder whose choices the finished object quietly hides.*

### R7 · There's no reader, no reception, no interpreter in the method. Meaning is completed in uptake — but your coder's own role is invisible, so the coded object presents a false neutrality.

This is a real hole, and it is one the instrument caught *about itself*. When we ran the method on its own method-statement, the top gap its forebears selected was exactly this: requiring every output to be read "from the coded object, not the original" silently installs the coded layer as scripture — with no stated justification, and against a whole tradition of thinking about reading (Genette's palimpsest, Kugel's targum, Iser's gap-in-the-text). Our coding models text-internal *production*; even the reception-flavored outputs stay text-to-text and never model a situated reader taking the text up. The designed answer is a **Representation Ledger** — a versioned object with a positionality preamble, calibrated confidence, and alternative codings — which was the review's single strongest generative convergence. But it is designed, not built.

**Status —** OPEN. We can name the miss precisely — the instrument surfaced it reflexively — but there is no built mechanism that models reception or exposes coder positionality.
**Evidence —** [IRR224 reconciliation — SM3, 4/5, the Representation Ledger](research/00_irr/irr224_reflexive_method_freeform_review_reconciliation_2026-07-29.md) · [reflexive output — the "coded object as scripture" gap](pm/50_audits/REFLEXIVE_OUTPUT_instrument_reads_itself_2026-07-29.md) · [3-agent CRT synthesis — #4, reader-is-a-system](pm/50_audits/CRT_3agent_method_review_synthesis_2026-07-29.md). Test: [TESTS QUEUE #10](#tests-queue).

### R10 · The coded object looks neutral and settled, but it should preserve disagreement, alternatives, provenance, and versioning. It's really a *versioned argument about the text*, not a finished graph.

We take this as a design mandate, not a defeater — and we note a genuine tension with our own rule that canonical data lives in one queryable place. That rule exists so we don't hunt across scattered files for the authoritative version; but a *single canonical coding* would erase the history of interpretation. These reconcile if the single store of record *is* the **Representation Ledger**: one authoritative table whose every row carries its evidence span, an annotation status (explicit / inferred / historically-reconstructed / generated / disputed), calibrated confidence, provenance, **alternative codings**, and a loss note. That preserves disagreement *inside* the one store — so a morphospace point becomes a confidence region, and a Compare spine becomes a set of possible alignments. It is the review's #1 generative convergence and buildable on the store we already have — but not yet built.

**Status —** OPEN. The reconciliation (a versioned ledger inside the single store) is designed and resolves the tension in principle; no implementation yet.
**Evidence —** [IRR224 reconciliation — SM6, 4/5, the Representation Ledger](research/00_irr/irr224_reflexive_method_freeform_review_reconciliation_2026-07-29.md) · [reflexive output — "coded object installed as scripture"](pm/50_audits/REFLEXIVE_OUTPUT_instrument_reads_itself_2026-07-29.md) · project invariant §2.13 (single store of record — the tension). Test: [TESTS QUEUE #10](#tests-queue).

---

## 6 · Does it generalize, or just fit anything?

*We claim the method is domain-general — it works on scripture, lyrics, licenses, papers. The critic's worry is the Barnum effect: a method loose enough to "work" everywhere may be finding generic structure, not the text's own.*

### R2 · Your instrument seems built for linear, Western, agentive narrative. What about non-linear or non-agentive texts?

Two parts. On **non-linear texts:** we built a sixth output, **Constellation**, in direct response to this exact question — a non-linear text rendered as a field of moves and edges rather than a single spine, worked on Gertrude Stein's *Tender Buttons*. The objection *generated an output*. On **non-agentive / apophatic texts:** the move-grammar was designed to fit them via different values, explicit nulls, and per-domain axis-weights — a different *filling* of the same slots, not a different grammar (this is R3). What is still owed is the confirming end-to-end run on a representative non-Western text.

**Status —** PARTIAL — one output was built in answer to the non-linear half; the confirming non-Western run is OPEN.
**Evidence —** the Constellation output (Stein's *Tender Buttons*) in the [engine schema](https://grammarofmeaning.org/engine/schema.html) · the grammar-grounding runs under R3. Open run: [TESTS QUEUE #5](#tests-queue).

### R9 · Domain-generality is asserted, untested, and unfalsifiable. Running the method on its own statement proves consistency, not generality; showing it works on two domains doesn't prove the structure belongs to the *method* rather than being generic (the Barnum effect).

This is the objection we have the *strongest live answer* to, and it is a real falsification program, not a flourish. The discriminating move the cohorts demand is exactly our replication rule: *is a result a property of the INSTRUMENT or of the DOMAIN?* The worked example: the Romans-8 present-versus-obligated reliability split looked like it might just mean "theology is hard," so we ran the *same instrument* on a confound-free out-of-domain corpus — a modern pop lyric — and **the split reproduced, 5/5**, converting a suspected domain problem into a demonstrated property of the instrument. That is a replication *result*, not a self-application. We also concede the sharper test still to run: **intervention-based validation** (the Fan-as-validity-probe) — perturb one slot (flip an agent, remove a warrant) and check the coding changes *coherently in the predicted slot* — which gives the generality claim a real per-move falsification instead of a domain-count argument.

**Status —** SUBSTANTIALLY ANSWERED via out-of-domain replication (a run, not a claim); OPEN on the per-move intervention test.
**Evidence —** [IRR167 reconciliation — the out-of-domain Beatles replication](research/00_irr/irr167_beatles_coding_method_reconciliation_2026-07-19.md) (project invariant §2.14) · [IRR224 reconciliation — SM1, 4/5, plus the Fan-as-validity-probe](research/00_irr/irr224_reflexive_method_freeform_review_reconciliation_2026-07-29.md) · [3-agent CRT synthesis — #9](pm/50_audits/CRT_3agent_method_review_synthesis_2026-07-29.md). Test: [TESTS QUEUE #9](#tests-queue).

### S2 · Your own schema flags the first engine — Situate, which grounds a text in its historical world — as "reliability-tested on 2 texts only (Romans 8:28–30, Mark 16), both biblical, never tested out-of-domain." How can the pipeline claim generality when its first stage is validated on two texts from one tradition?

It can't, yet — and the schema is right to flag it. Situate (Sitz-grounding) is the *least* out-of-domain-tested engine in the pipeline: it matches a text's date and setting against a catalogue of substrate events and Sitz-im-Leben layers, and that matching has only been reliability-checked on two biblical passages. Everything downstream inherits that narrowness at the grounding step, even where later stages have been run more widely. This is the same shape as R9 (property-of-instrument vs. property-of-domain) but aimed at the *first* stage rather than the coding: the out-of-domain replication we have is on the reliability split, not on Situate's grounding accuracy. The honest position is that Situate's generality is asserted on n=2, and the confirming run is a representative non-biblical text taken through grounding end-to-end — the same run R2(b) and TESTS QUEUE #5 owe.

**Status —** OPEN on out-of-domain Situate. The limitation is self-flagged in the schema; the confirming run is owed.
**Evidence —** the Situate (Engine 0.A) status line "reliability-tested on 2 texts only … never tested out-of-domain" in the [engine schema](https://grammarofmeaning.org/engine/schema.html) · cross-ref R9 (project invariant §2.14). Test: [TESTS QUEUE #5](#tests-queue).

### S7 · Your live schema shows the whole instrument has been run on about 32 texts, gaps on 8, constellation on 3 — most of them biblical. Isn't every reliability and generality claim in this FAQ built on a handful of texts?

Yes, and we'd rather say so plainly than let the interface imply otherwise. The live counts are real and small: moves on ~32 sources, the gap scan on ~8, the constellation output on ~3. Every status marked ANSWERED in this document is a *first run / proof-of-concept* — the negative control (R13), the seeded-critic A/B (R14), the out-of-domain replication (R9) — not a result at scale, and the corpus skews Abrahamic (the n=14 caveat in R16 is the same story). We treat this as a disclosed scope limit, consistent with our bias-visibility commitment: name the skew rather than hide it behind curatorial selection. The right way to read this FAQ is that it reports what each run *showed*, and that the confirming scale-ups — a diverse non-canonical corpus (TESTS QUEUE #2, #13) and the non-Western end-to-end run (#5) — are exactly what would move these from proof-of-concept to established.

**Status —** PARTIAL — an honest scope caveat. The claims are real runs but small-N and corpus-skewed; the scale-ups are queued.
**Evidence —** the live run-counts in the [engine schema](https://grammarofmeaning.org/engine/schema.html) · project invariant §2.8 (bias-visibility). Scale-ups: [TESTS QUEUE #2](#tests-queue), [#5](#tests-queue), [#13](#tests-queue).

---

## 7 · The critic panels — seeded voices and glosses

*One output glosses a text's silences through named critics (William James, Augustine, and others). The obvious suspicion: these are just the generic "act like Socrates" personas anyone can prompt an LLM into.*

### R14 · Aren't your critic panels just the generic "act like William James" personas everyone role-plays with an LLM?

No — and the difference is auditable. Our critics are **seeded with real, fetched text** and must critique *from that document*, not from the model's averaged impression of a name. We proved it with a bare-versus-seeded A/B on one named critic, William James, glossing the same gap. **Bare-James (from memory)** regressed to the mean of the name — "believability is *merely* subjective, discount it." **Seeded-James** — given his actual text, *Varieties of Religious Experience*, Lecture III, "The Reality of the Unseen" — said the *opposite* and rerouted the critique: the "sense of reality" is a *real, primary faculty* that fires hardest where nothing is present (his hallucination case: "real in the most emphatic sense… neither seen, heard, touched"), so the metric under scrutiny measures a faculty *decoupled from actual presence* — making it *worse*, not softer. The real text **overruled the persona's instinct** — the same shape as when Gelman and Loken's actual paper overruled a stats-skeptic's reflexive "that effect is too big, it must be p-hacking." The *difference between the two arms is itself the evidence that seeding works*: a bare named-persona is a prior-driven guess (flagged as such), a seeded critic is the thinker's *text*. And the panel *composition* is a declared, reusable instrument parameter — a named registry of panels — so running two or more panels shows the critique is composition-dependent, not arbitrary.

**Status —** ANSWERED (a run) — bare-versus-seeded demonstrated on William James; the seed reversed the conclusion. Repeatable on any named critic (Augustine, Socrates, …).
**Evidence —** [bare-vs-seeded A/B — William James, the two arms + the fetched quotes](pm/50_audits/AB_bare_vs_seeded_william_james_s156_2026-07-30.md) · [Smallville 20-critic rooms — the seeded Gelman overrule](pm/50_audits/smallville_20critic_rooms_s156_2026-07-30.md) · [the seeding step](pm/30_methodology/GLOSS_process_steps_with_seeding_s156_2026-07-30.md) · [the named-panel registry](pm/30_methodology/CRIT_PANEL_REGISTRY_s156_2026-07-30.md) · [MASTER LEXICON — the SEEDING lock](docs/methodology/MASTER_LEXICON.md).

### R15 · Could this be used outside meaning-making — can it actually find real *research* gaps?

Yes, and honestly bounded. We ran the instrument blind on a foundational tech paper (Park et al., "Smallville," arXiv 2304.03442). The honest finding, against our fair baseline: on a *tech* paper — the LLM's home turf — a strong cold read finds the gap-list on its own, so gap-*finding* is not where a structured instrument earns its keep. What the **seeded** instrument adds, and a cold read cannot, is threefold: the **rival model** (an ACT-R critic showing that Smallville's exponential recency-decay is the *wrong functional form* against fifty years of validated human-memory data — "the knob is the wrong shape," not "tune the knob"); the **paradigm-exit critics** (Suchman, Weizenbaum, Turing, Blake); and **auditable multi-panel disagreement**. The full write-up, with the gap-list honestly labeled, is the [Research-Gap Demo — Smallville](research-gap-smallville.html).

**Status —** ANSWERED (a run) — honestly bounded: gap-finding on the LLM's home turf is not the win; the rival model and paradigm-exit critics are.
**Evidence —** [Research-Gap Demo — Smallville](research-gap-smallville.html) · the seeded-critic runs under R14.

---

# TESTS QUEUE

*The experiments that back future entries — designed or partially run. Item #13 is the one exception: it has a result already.*

1. **A/B — raw text vs. decomposed process** *(the cleanest value-of-the-instrument test the PI wants).* Same text (Romans 8:28–30), same critic panel: Arm A gets the *raw text* + "where is the unsaid? give commentary"; Arm B gets our *decomposed* object (moves · gaps · the compatible questions). Compare the gap/commentary sets. Most-scientific shape: hold the panel and text fixed, vary only the instrument; pre-register what "better" means (does B surface text-specific, historically-attested gaps A misses; does A produce more associative-prior noise). The controlled version of the IRR224 critique.
2. **Statistical baseline for R1** — is 26% strict / 71% lenient unanimity *higher than chance*? Null models: (a) random bucket assignment; (b) a non-LLM reference baseline — do encyclopedias / standard reference works "agree" at what rate on the same demarcation questions? Establishes whether the LLM consensus rate is elevated versus a non-LLM knowledge source. (The other ~3–5% = rounds where the models mostly disagree.) Backs [R1](#r1--your-five-llm-inter-rater-panel-isnt-five-independent-judges--they-share-training-data-and-rlhf-so-their-agreement-is-shared-bias-not-signal) and [R12](#4--do-the-numbers-mean-anything--reliability--validity).
3. **Reliability re-tally on the meta-analysis itself** — three independent agents re-tally the same 307-document corpus; compare their counts. Tests that R1's numbers are reproducible, not one parse's artifact.
4. **Gap → reception overlay (Romans 8:29)** — show that our *gaps* (the unsaid slots) sit where interpreters *historically divided* (Augustinian / Arminian / Orthodox on 8:29). Needs a visualization: our gap-map overlaid on the documented dispute record. See [gap-seed ranking / type-compatibility](pm/30_methodology/gap_seed_ranking_type_compatibility_2026-07-29.md).
5. **Non-Western grammar-fit** — run the built instrument on a representative non-agentive / apophatic text; confirm it codes via different values / nulls (not breakage). Backs [R2](#r2--your-instrument-seems-built-for-linear-western-agentive-narrative-what-about-non-linear-or-non-agentive-texts), [R3](#r3--your-move-grammar-looks-western-and-action-oriented-does-it-even-fit-non-agentive-or-apophatic-traditions), and [S2](#s2--your-own-schema-flags-the-first-engine--situate-which-grounds-a-text-in-its-historical-world--as-reliability-tested-on-2-texts-only-romans-828-30-mark-16-both-biblical-never-tested-out-of-domain-how-can-the-pipeline-claim-generality-when-its-first-stage-is-validated-on-two-texts-from-one-tradition).
6. **Free-form vs. process — side by side** (not a summary) — lay the five-LLM free-form gap-lists next to our systematic output, actual output vs. actual output, so the PI can see each one's strengths directly. (Partly in the IRR224 reconciliation; the PI wants the raw side-by-side.)
7. **Edge-typology formalization + assignment-agreement** *(backs [R5](#r5--what-exactly-are-your-edge-types-presupposes-entails-fills--is-that-set-complete-exclusive-and-rule-governed-or-is-the--hiding-the-hard-part), currently OPEN; also gates [S1](#s1--engine-1-says-it-returns-a-graph-of-typed-edges-between-moves-do-you-actually-analyze-that-graph-as-a-network--centrality-motifs-cross-text-structure--or-just-store-it)).* Enumerate the complete edge-type set, sort by register (logical / semantic-pragmatic / method-defined), state assignment rules and whether the set is exhaustive / mutually exclusive, then measure inter-coder (and inter-model) agreement on *edge-typing* specifically. Turns the "…" all five cohorts flagged into a closed, testable inventory.
8. **Segmentation stopping-rule + separated reliability** *(backs [R6](#r6--when-does-a-move-stop-is-the-kingdom-of-heaven-is-like-a-mustard-seed-one-move-or-three-without-a-stopping-rule-the-grain-of-every-downstream-coordinate-is-arbitrary), OPEN on the rule).* (a) State an atomicity rule (when is a move atomic vs. a composition — the mustard-seed case); (b) measure *segmentation* reliability separately from *label* reliability on the same passages, so a reliability number stops conflating boundary-disagreement with coding-disagreement. Pre-register the atomicity rule before measuring.
9. **Fan-as-validity-probe / intervention-based validation** *(backs [R9](#r9--domain-generality-is-asserted-untested-and-unfalsifiable-running-the-method-on-its-own-statement-proves-consistency-not-generality-showing-it-works-on-two-domains-doesnt-prove-the-structure-belongs-to-the-method-rather-than-being-generic-the-barnum-effect), [R11](#r11--isnt-the-five-slot-grammar-agent--operation--substrate--outcome-itself-a-western-action-first-metaphysics-if-so-it-might-manufacture-the-cross-tradition-convergence-it-claims-to-discover--and-that-contradicts-your-claim-that-the-categories-are-validated-by-inter-rater-reliability-not-chosen-in-advance), and [S6](#s6--the-schema-says-each-of-the-six-recompositions-fan-resituation-gloss-reception-comparison-constellation-changes-what-it-means-how-do-you-know-a-recomposition-is-a-valid-reading-of-the-text-and-not-a-plausible-hypothetical-the-text-cant-actually-support) — the per-move falsification).* Perturb one slot of a coded move (flip agent, remove a warrant, reverse polarity) and test whether the coding changes *coherently in the predicted slot* and not elsewhere. Confirms the coder tracks the text, not its priors — and gives the domain-generality claim (R9), the grammar-manufactures-convergence charge (R11), and the recomposition-validity question (S6) a real falsification. High leverage, low cost (re-purposes the Fan output the instrument already produces).
10. **Representation Ledger build + false-neutrality test** *(backs [R7](#r7--theres-no-reader-no-reception-no-interpreter-in-the-method-meaning-is-completed-in-uptake--but-your-coders-own-role-is-invisible-so-the-coded-object-presents-a-false-neutrality), [R10](#r10--the-coded-object-looks-neutral-and-settled-but-it-should-preserve-disagreement-alternatives-provenance-and-versioning-its-really-a-versioned-argument-about-the-text-not-a-finished-graph), and [R12](#r12--auditability-isnt-validity-a-fully-traceable-well-formed-coding-can-still-be-systematically-wrong-you-emphasize-traceability-more-than-construct-validity-and-you-never-expose-the-grammar-to-llm-mapping) — all OPEN).* Build the versioned lattice *inside* the single store of record: each annotation carries evidence-span · status (explicit / inferred / reconstructed / generated / disputed) · calibrated confidence · provenance · **alternative codings** · loss note, plus a slot for the human-expert / tradition-bearer gold anchor. Test: does preserving disagreement change downstream outputs (does a morphospace point become a region, a Compare spine a set of alignments)? Resolves the tension between the single-store rule and preserving interpretive history.
11. **Morphospace axis-derivation audit + coordinate reliability** *(backs [R8](#r8--are-the-axes-chosen-in-advance-or-discovered-from-data-how-many-axes-count-as-enough-and-doesnt-a-coordinate-dress-up-a-judgment-as-geometry--couldnt-two-coders-land-a-text-in-completely-different-places), OPEN half).* (a) State whether each axis is a-priori or induced and what constitutes adequacy-N (the "ninth axis" test: does a candidate axis add discriminative information after conditioning on the existing eight); (b) measure inter-coder *coordinate* reliability (do different coders place the same text near the same coordinates); (c) enforce the declared-profile-vs-derived-geometry separation as an audit invariant so geometry never over-claims metric structure the ontology lacks.
12. **Gap salience / contrast-set operationalization + silence typology** *(backs [R4](#r4--every-sentence-leaves-infinitely-many-things-unsaid-doesnt-gap-scoring-just-measure-the-models-own-associations-not-the-text), OPEN implementation; also [S5](#s5--your-schema-splits-the-unsaid-into-gap-in-text-and-seam-between-layers-can-coders-actually-agree-which-is-which--and-doesnt-a-seam-between-say-sitz-and-move-risk-being-an-artifact-of-your-own-layering-rather-than-something-in-the-text)).* Operationalize closed + contrastive gaps at scale: a gap must cite the parallel text / tagged paradigm where the role IS filled (the obligation), per the present-vs-obligated finding. Then test that scored gaps track the contrast set, not the model's associative priors (swap the coding model; do the high-salience gaps stay put?). Add the silence typology (presupposed / taboo / ineffable / genre-convention) so "productive silence" is not miscounted as a defect. Fold the GAP-vs-SEAM reliability question (S5) into the same measurement, holding SEAM to the stricter bar.
13. **Over-generation negative control — ✅ RUN (not designed)** *(backs [R13](#r13--what-if-the-instrument-just-over-generates-gaps-give-it-four-layers-and-a-dozen-loci-and-it-will-always-find-plausible-sounding-gaps-havent-you-built-a-generator-not-an-instrument); IRR225 U9).* Run the instrument on a text engineered to *close* interpretive space (legal / expository boilerplate), where a well-calibrated instrument should find almost nothing. **First run: MIT License → ~81% of candidates discarded by the gates; 2 clean survivors (patent scope; "substantial portions") = the license's real famous silences.** The control PASSES — the instrument restrains, it does not generate. Unlike #1–#12, this test has a result already. Confirming scale-up: a diverse non-canonical corpus (legal / technical / expository), shared with the #2 baseline battery. Evidence: [MIT-License over-generation probe](pm/50_audits/v3_overgeneration_probe_mit_license_s156_2026-07-30.md).

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: reading-SB S157 (2026-08-01) reworked the S156 method-rebuttals doc per PI direction. The S156
  original (reading-SB, 2026-07-29→30) collected objections R1–R16 as objection→response→evidence entries in
  discovery order. This S157 pass (1) rewrote every entry in plain question→answer form, term-first with plain
  glosses; (2) re-grouped the 16 entries into SEVEN THEMES (move-grammar; gaps & seams; the eight axes;
  reliability & validity; the reader / positionality; domain-generality & over-generation; the critic panels)
  rather than discovery order; (3) added SEVEN NEW schema questions (S1–S7) aimed at the engine schema itself —
  the move-edge graph as a network (S1), Engine-0 Situate tested on only 2 biblical texts (S2), declared-but-
  unwritten schema fields (S3), the eight-axes-vs-seven-letters naming drift (S4), GAP-vs-SEAM reliability (S5),
  recomposition validity of the six outputs (S6), and the small-N / Abrahamic-skewed corpus (S7) — each with an
  honest answer marking OPEN / PARTIAL where nothing is built yet; (4) converted every raw evidence-path string
  into a real Markdown link; and (5) removed the ad-hoc bold-label soup, standardizing to one Status line and one
  Evidence line per entry. No claim, status, or cohort-strength marker was inflated: every ANSWERED / PARTIAL /
  OPEN is carried over verbatim from the S156 source. New S-question answers were written only from the visible
  schema (schema.html: the move quadruple, the eight Frame axes, the GAP/SEAM 2×2, the six outputs, the LIVE
  run-counts) and existing project invariants — no new evidence files or test results were invented.
SCHOLARLY SOURCES: the S156 source doc (method_rebuttals_faq.md, 2026-07-29/30) and every file it cites —
  IRR_consensus_meta_analysis + FINDING_irr_consensus_task_dependence (R1); irr224 reflexive-method reconciliation
  (R4–R12, S3-adjacent); CRT_3agent_method_review_synthesis (the 3/3 convergent critiques); REFLEXIVE_OUTPUT
  instrument_reads_itself (R7/R10); researchsurvey_gpt.txt §4–§5 (R8 declared-vs-derived geometry); irr167 Beatles
  reconciliation + §2.14 (R9 out-of-domain replication); irr225 layered-gap reconciliation + v3 over-generation
  probe + INSTRUMENT_v3_spec (R13); AB_bare_vs_seeded_william_james + smallville_20critic_rooms +
  GLOSS_process_steps_with_seeding + CRIT_PANEL_REGISTRY + MASTER_LEXICON (R14); §2.8 / §2.13 (the bias-visibility
  and single-store invariants the S-questions lean on). The seven S-questions are grounded in the live engine
  schema at grammarofmeaning-site/engine/schema.html (the const P stage/field definitions read S157).
WHAT NEEDS VERIFICATION: (1) The renderer (rebuttals.html) will NOT parse this file as-is — see the HTML comment
  at the top of this document for the exact changes Design-SB must make (themed sections, S-IDs, Markdown-link
  evidence, single Status/Evidence labels, cohort tags moved to prose). (2) The Evidence links point at twelve-laws
  REPO paths that are not deployed to the site; Design-SB must decide the final href target. (3) The intra-doc
  anchor links in the TESTS QUEUE (to #r1, #s2, etc.) assume GitHub-style heading-slug anchors; verify the site's
  Markdown renderer generates matching slugs, or Design-SB should swap them for explicit anchors. (4) Statuses
  carried from S156 inherit its caveats: six of nine original appended entries (R5/R6/R7/R10/R11/R12) remain OPEN
  on their core fix; SM2 (R11) was scored 4/5 with Solar ADJACENT. (5) All new S-questions except none are marked
  OPEN or PARTIAL — none claims a run that has not happened. (6) The engine schema's own self-flagged bugs
  (year_estimate NULL, 8-vs-7 axes, closure_type on one text) that S3/S4 report should be fixed in schema.html
  independently of this FAQ. -->
