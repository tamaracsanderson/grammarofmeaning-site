# REFLEXIVE-METHOD — background sheet

> Full coded transcript for **REFLEXIVE-METHOD** — read-only snapshot from the DB.

## What you're looking at
This is the **full coded output of the instrument** — the raw materials behind every visualization. The instrument reads a text through one fixed pipeline:

> **text → SITUATE ∥ ANALYZE → coded object → outputs**

- **SITUATE** places the text in its world: **Sitz** (situational conditions) · **Paradigm** (the scripts it thinks with + its stance) · **Frame** (its coordinate in the 8-axis morphospace).
- **ANALYZE** decomposes its meaning-making: **moves** (agent · operation · substrate · outcome · narrator) · **edges** (typed relations between moves) · **gaps** (what each move foregrounds but leaves unanswered).
- The **coded object** is what every output (Compare · Gloss · Fan · Reception · Constellation · Morphospace) reads from — so each visual can be **cross-checked against the coding below**.

## How this was coded (rigor)
- **Neuro-symbolic:** a symbolic **move-grammar** (the fixed agent/operation/substrate/outcome/narrator slots) scaffolds the generative LLM coder — the structure makes the generation **auditable**, every slot fillable from the text and checkable against it.
- **IRR-validated axes:** the morphospace axes + coding categories were locked via multi-LLM inter-rater-reliability rounds, not authored a priori.
- **Single store of record (§2.13):** every field here is read live from the database, not transcribed — so this is the coding *of record*.
- **Provenance-flagged:** anything an LLM *generates about* a text (e.g. a domain-context primer) is marked **"LLM-generated — not instrument output"**, kept separate from the instrument's own coded fields.

## Definitions — how to read this
| term | what it means |
|---|---|
| **move** | one coded operation + its parts: **agent** (who acts) · **operation** (the verb/what's done) · **substrate** (what it's done to) · **outcome** (the result) · **narrator** (the teller). A text = a sequence of moves. |
| **edge** | a typed relation between moves (presupposes, entails, fills, …) — the connective tissue. |
| **gap** | what a move *foregrounds but leaves unanswered* — the negative space (scored per move × role). |
| **Sitz** | the situational conditions (when/where/how-the-world-was) that condition the text. |
| **Paradigm** | a cultural *script* the text thinks with, tagged with the text's **stance** toward it: *endorsed · invoked · subverted · denied*. |
| **Frame** | the text's coordinate in the 8-axis morphospace (epistemic-warrant, telos, …) with evidence. |
| **spine** (Compare) | the **lowest-common-denominator shared move** across the accounts. |
| **specification** (Compare) | the *same* shared move rendered with different detail (2 vs 3 women — both "at the tomb"). |
| **unique move** (Compare) | a move *in its own right* present in only some accounts — not a retelling of a shared beat. |

## What the coding surfaced (snapshot)

_Counts from the coding — not an interpretation. The reading is yours to make from the material below._

| text | moves | paradigms | frame axes | gaps |
|---|---|---|---|---|
| REFLEXIVE-METHOD | 38 | 0 | 0 | 151 |


## REFLEXIVE-METHOD

### Sitz — situational conditions (source_grounding)

_(no Sitz grounding row)_

### Paradigm — the scripts the text thinks with (+ its stance toward each)

_(none coded)_

### Frame — the 8-axis morphospace coordinate

_(none coded)_

### Coded moves — each with the context it picked up

**M1** — The instrument's purpose is to investigate how meaning is produced within and across traditions.
  · agent: the instrument · operation: studies · substrate: how meaning gets made across traditions · outcome: not-stated · narrator: the methodology's authors
  · **gaps:** *instrument* — the means of studying is supplied by M2: treating texts as decomposable, comparable acts of meaning-making (filled-internally); *reason* — why the instrument studies cross-tradition meaning-making is never given — the telos (comparison, taxonomy, formation?) is withheld (residual)

**M2** — The instrument frames every text it encounters as a meaning-making act that is available for decomposition and comparison.
  · agent: the instrument · operation: treats [as] · substrate: a text · outcome: a text classified as an act of meaning-making that can be decomposed and compared · narrator: the methodology's authors
  · **gaps:** *reason* — why treat a text as a decomposable act of meaning-making is answered by M1: the instrument exists to study how meaning gets made across traditions (filled-internally); *instrument* — the means by which the instrument classifies/treats a text is supplied by M6: identifying the Sitz (situational conditions) that condition the text (filled-internally); *warrant* — on whose authority a text counts as an act of meaning-making — the theoretical commitment grounding that claim — is never named (residual)

**M3** — The instrument accepts one text at a time as its starting material.
  · agent: the instrument · operation: takes [as input] · substrate: a single text · outcome: the text positioned as the instrument's input · narrator: the methodology's authors
  · **gaps:** *reason* — why the instrument takes exactly one text at a time (rather than a corpus or pair) is not given — the unit-of-analysis rationale is withheld (residual)

**M4** — The category 'text' is defined as any delimited expressive unit, illustrated by scripture, poetry, song, and a methodology statement.
  · agent: not-stated · operation: is [definitional] · substrate: a text (the category) · outcome: any bounded unit of expression — scripture passage, poem, song lyric, or methodology statement · narrator: the methodology's authors
  · **gaps:** *reason* — why the definition of 'text' is stretched to include methodology statements alongside scripture is not stated — the theoretical rationale for the broad category is withheld (residual); *warrant* — says who that any bounded unit of expression qualifies as a text — the authority behind collapsing scripture, lyric, and methodology into one category is never supplied (residual)

**M5** — The instrument places the text in its situation as a step that comes before any analysis of the text.
  · agent: the instrument · operation: situates · substrate: the text · outcome: not-stated · narrator: the methodology's authors
  · **gaps:** *reason* — why the instrument situates the text is supplied by M6: situating is in order to identify the Sitz — the conditions that condition the text (filled-internally); *instrument* — the means by which the instrument situates is supplied by M6: identifying the when/where/how-the-world-was conditions constitutes the situating operation (filled-internally)

**M6** — The instrument locates and names the situational conditions — historical, geographical, and worldly — under which the text was produced.
  · agent: the instrument · operation: identifies · substrate: the text's Sitz · outcome: the Sitz specified as situational conditions (when, where, and how the world was) that condition the text · narrator: the methodology's authors
  · **gaps:** *reason* — why the instrument identifies the Sitz is answered by M1: identifying situational conditions is the mechanism for studying how meaning gets made across traditions (filled-internally); *instrument* — by what means the instrument identifies the Sitz (close reading? formal schema? comparative lookup?) is never given — the analytic procedure is withheld (residual); *warrant* — says who that situational conditions (when/where/how-the-world-was) constitute the Sitz — the form-critical or theoretical authority licensing that framing is never named (residual)

**M7** — The instrument locates and names the conceptual frameworks the text draws on, tagging each one with the text's posture toward it.
  · agent: the instrument · operation: identifies · substrate: the paradigms the text thinks with · outcome: paradigms specified as cultural scripts the text runs, each tagged with the text's stance — endorsed, invoked, subverted, or denied · narrator: the methodology's authors
  · **gaps:** *reason* — why the instrument identifies paradigms is unsaid here; M8's frame-assignment is the downstream purpose that implicitly supplies it (filled-internally); *warrant* — authority for the paradigm identifications is unsaid in M7; M9's evidence-from-text backing supplies the warrant structure (filled-internally); *instrument* — by what means the instrument detects and tags cultural scripts (endorsed/invoked/subverted/denied) is never stated (residual)

**M8** — The instrument gives the text a positional location — a coordinate within an eight-axis morphospace.
  · agent: the instrument · operation: assigns · substrate: the text · outcome: a frame: a coordinate in an eight-axis morphospace · narrator: the methodology's authors
  · **gaps:** *instrument* — by what means the frame is assigned is not stated in M8; M9 names text-evidence per axis as the mechanism (filled-internally); *warrant* — on whose authority a coordinate is valid is unsaid in M8; M9's evidentiary support is what authorises each axis value (filled-internally); *reason* — why the instrument assigns a morphospace coordinate rather than some other representational output is never stated (residual)

**M9** — The instrument grounds each axis of that coordinate with textual evidence.
  · agent: the instrument · operation: supports · substrate: each axis · outcome: each axis backed by evidence drawn from the text · narrator: the methodology's authors
  · **gaps:** *reason* — why the instrument evidences each axis is not stated in M9; M8's need for a justified frame assignment supplies the reason (filled-internally); *warrant* — what counts as sufficient evidence, and who adjudicates adequacy, is nowhere stated across all six moves (residual)

**M10** — The instrument breaks the text down into its constituent moves.
  · agent: the instrument · operation: analyzes [into] · substrate: the text · outcome: moves · narrator: the methodology's authors
  · **gaps:** *reason* — why the instrument decomposes texts into moves is unsaid in M10; M11's definition of a move as a meaning-making operation supplies the rationale (filled-internally); *warrant* — authority for any particular move-segmentation is unsaid in M10; M11's definitional status (the five-slot schema) is the implicit warrant (filled-internally); *instrument* — by what procedure the instrument identifies and segments moves within a text is never stated (residual)

**M11** — The category 'move' is defined as a single meaning-making operation carrying five slots: agent, operation, substrate, outcome, and narrator.
  · agent: not-stated · operation: is [definitional] · substrate: a move · outcome: one operation of meaning-making with five slots — agent, operation, substrate, outcome, narrator · narrator: the methodology's authors
  · **gaps:** *reason* — why exactly five slots (agent, operation, substrate, outcome, narrator) constitute a move — and not more or fewer — is never stated (residual); *degree* — whether the five-slot schema is claimed to be exhaustive of all meaning-making operations or merely sufficient is left open (residual); *instrument* — by what method the five-slot definition was derived or operationalised is not stated (residual); *warrant* — on whose authority this particular ontology of meaning-making (five slots) is valid — theoretical tradition, empirical derivation, stipulation — is never stated (residual)

**M12** — The category 'text' is defined as an ordered series of moves.
  · agent: not-stated · operation: is [definitional] · substrate: a text · outcome: a sequence of moves · narrator: the methodology's authors
  · **gaps:** *instrument* — by what means a text is decomposed into its sequence is unsaid in M12; M10's analysis operation is the supplying move (filled-internally); *warrant* — authority for treating a text as a move-sequence is unsaid in M12; M11's definition of a move as the atomic meaning unit provides the foundation (filled-internally); *reason* — why a text is defined as a sequence of moves rather than a network, hierarchy, or other structure is never stated (residual); *degree* — whether the sequence is ordered, exhaustive, or merely a partial enumeration of moves is left open (residual)

**M13** — The instrument locates and names the connections between moves, treating them as typed relations.
  · agent: the instrument · operation: identifies · substrate: edges between moves · outcome: edges specified as typed relations — presupposes, entails, or fills · narrator: the methodology's authors
  · **gaps:** *reason* — why the instrument identifies typed edges at all — the epistemic motive is withheld (residual); *instrument* — by what mechanism the instrument resolves an edge as presupposes vs. entails vs. fills is not stated (residual); *warrant* — on whose authority the three relation-types (presupposes / entails / fills) are the correct and complete taxonomy (residual)

**M14** — The instrument locates and names what each move brings to the foreground but does not fill in — the silences each move carries.
  · agent: the instrument · operation: identifies · substrate: gaps · outcome: gaps specified as what each move foregrounds but leaves unsaid — its negative space · narrator: the methodology's authors
  · **gaps:** *reason* — why identifying a move's negative space serves the instrument's analytic purpose is not given (residual); *instrument* — by what procedure the boundary between foregrounded content and its negative space is drawn (residual); *warrant* — on whose authority a particular silence counts as the gap (not merely incidental omission) (residual)

**M15** — The instrument assigns a score to each gap, calibrated at the level of the move and at the level of each slot.
  · agent: the instrument · operation: scores · substrate: each gap · outcome: not-stated · narrator: the methodology's authors
  · **gaps:** *reason* — why gaps are scored rather than only catalogued — the goal of quantification is withheld (residual); *degree* — the scoring output is explicitly marked 'not-stated'; scale, range, and units are fully withheld (residual); *instrument* — by what criteria or algorithm the instrument assigns a score to each gap (residual); *warrant* — on whose authority the scoring rubric is valid — no grounding source is named (residual)

**M16** — Once situated and analyzed, the text has become a formal artifact available for further use.
  · agent: not-stated · operation: is [resultative state] · substrate: the situated and analyzed text · outcome: a coded object · narrator: the methodology's authors
  · **gaps:** *reason* — why 'not-stated' is the actor that produces the coded object — the ontological logic of the resultative state is withheld (residual); *interior* — what the source text undergoes — what is altered in it by being coded — its 'experience' of the transformation (residual); *instrument* — by what procedure 'not-stated' is converted into a coded object rather than remaining an absence (residual); *warrant* — on whose authority the resultative state qualifies as a legitimate 'coded object' (residual)

**M17** — Each output draws its content directly from the coded object.
  · agent: every output · operation: reads from · substrate: the coded object · outcome: not-stated · narrator: the methodology's authors
  · **gaps:** *warrant* — M16 establishes the coded object as the authoritative resultative state, implicitly warranting M17's dependency on it (filled-internally); *reason* — why every output must read from the coded object rather than from the original source text (residual); *instrument* — by what mechanism an output reads from the coded object — the read interface is unspecified (residual)

**M18** — Because every output derives from the coded object, any output is available for verification against that coding.
  · agent: not-stated · operation: can be cross-checked against · substrate: every output · outcome: not-stated · narrator: the methodology's authors
  · **gaps:** *reason* — why cross-checking against every output is possible — what structural property makes the coded object falsifiable (residual); *instrument* — by what procedure the cross-check is performed — what counts as a match or mismatch (residual); *warrant* — on whose authority a successful cross-check is conclusive — the verification standard is withheld (residual)

**M19** — The instrument transforms the coded object back outward, producing the suite of named outputs.
  · agent: the instrument · operation: recomposes [into] · substrate: the coded object · outcome: outputs · narrator: the methodology's authors
  · **gaps:** *reason* — why the instrument recomposes at all — the telos of the operation — is unstated (residual); *degree* — how completely / how many dimensions of the coded object are recomposed is unspecified (residual); *instrument* — by what mechanism the instrument performs the recomposition — the how of meaning-making — is not stated (residual); *warrant* — on whose authority the instrument is licensed to recompose the coded object is unstated (residual)

**M20** — The Compare output fuses multiple accounts of the same event into one shared backbone with variant branches.
  · agent: the Compare output · operation: merges [into] · substrate: parallel tellings of one event · outcome: a shared consensus spine plus branches · narrator: the methodology's authors
  · **gaps:** *reason* — why merge rather than adjudicate; M21's no-baseline rule supplies the governing rationale (filled-internally); *instrument* — by what procedure Compare identifies the shared spine versus the branch material is not stated (residual); *warrant* — on whose authority the consensus spine is designated as such — who adjudicates convergence — is unstated (residual)

**M21** — The Compare output withholds privileged status from every individual account, treating none as the authoritative ground.
  · agent: the Compare output · operation: treats [as] · substrate: no single telling · outcome: none designated as the baseline · narrator: the methodology's authors
  · **gaps:** *reason* — why no telling is privileged; M20's merge-into-shared-spine enacts the answer implicitly (filled-internally); *instrument* — by what mechanism the Compare output operationally enforces the no-baseline condition is unstated (residual); *warrant* — the authority or principle grounding the claim that no telling should be the baseline is not stated (residual)

**M22** — The Gloss output convenes a panel of critical voices positioned to supply what the text left open, each voice working from its own interpretive frame.
  · agent: the Gloss output · operation: seats · substrate: a crit panel of commentators · outcome: not-stated · narrator: the methodology's authors
  · **gaps:** *reason* — why the Gloss output takes the form of a seated crit panel rather than a single gloss is unstated (residual); *instrument* — by what means the Gloss output constitutes and seats the panel — selection criteria, process — is unstated (residual); *warrant* — on whose authority the panel members are chosen and their readings given standing is unstated (residual)

**M23** — The Fan output substitutes a single move within the text for a different one.
  · agent: the Fan output · operation: swaps · substrate: one move · outcome: not-stated · narrator: the methodology's authors
  · **gaps:** *reason* — why the Fan swaps; M24's tracing of ripple-consequences supplies the purpose — to reveal counterfactual structure (filled-internally); *instrument* — by what means the Fan selects which move to swap and executes the substitution is unstated (residual); *warrant* — on whose authority any particular move is chosen as the swap candidate is unstated (residual)

**M24** — The Fan output follows the chain of downstream effects that the substitution sets in motion.
  · agent: the Fan output · operation: traces · substrate: the counterfactual consequences that ripple from the swap · outcome: not-stated · narrator: the methodology's authors
  · **gaps:** *reason* — why trace consequences; M23's swap is the premise — tracing is the logical completion of the counterfactual (filled-internally); *degree* — how far the ripple is traced — which downstream effects count, where the chain terminates — is unstated (residual); *instrument* — by what method the Fan identifies and traces ripple-consequences from the swap is unstated (residual); *warrant* — on whose authority the traced consequences are identified as the right counterfactual outcomes is unstated (residual)

**M25** — The Reception output puts to the test the question of whether a later text fills in what the first text left unspoken.
  · agent: the Reception output · operation: tests · substrate: whether a second text answers the first text's unsaid gaps · outcome: not-stated · narrator: the methodology's authors
  · **gaps:** *reason* — why unsaid gaps are the operative test criterion is not stated (residual); *degree* — how fully or partially a second text must answer the first's gaps is unspecified (residual); *warrant* — authority for treating unsaid gaps as the right test frame is not given (residual)

**M26** — The Constellation output recast a nonlinear text as a spatial field of moves and their connections, abandoning sequential order.
  · agent: the Constellation output · operation: renders [as] · substrate: a nonlinear text · outcome: a field of moves and edges rather than a line · narrator: the methodology's authors
  · **gaps:** *reason* — why a field of moves and edges is the preferred rendering over a linear form is not stated (residual); *warrant* — on whose authority or by what evidence the nonlinear field rendering is valid is not stated (residual)

**M27** — The Morphospace output situates the text as a single coordinate within the eight-axis space, alongside other texts.
  · agent: the Morphospace output · operation: places [as a point among] · substrate: the text · outcome: a point among other texts in the eight-axis coordinate space · narrator: the methodology's authors
  · **gaps:** *reason* — why placing a text as a coordinate point is the right mode of meaning-location is not stated (residual); *degree* — how precisely or approximately the coordinate placement is made is unspecified (residual); *warrant* — what grounds the choice and calibration of the eight axes is not stated (residual)

**M28** — The method is classified as neuro-symbolic in character.
  · agent: not-stated · operation: is [neuro-symbolic] · substrate: the method · outcome: neuro-symbolic · narrator: the methodology's authors
  · **gaps:** *reason* — M29 supplies the structural answer: a fixed symbolic grammar scaffolds the generative model, giving the neuro-symbolic character its reason (filled-internally); *instrument* — M29 names the fixed symbolic move-grammar as the mechanism that makes the method neuro-symbolic (filled-internally); *degree* — the ratio or balance of neural vs symbolic components is not quantified (residual); *warrant* — on what basis the method qualifies as neuro-symbolic rather than merely hybrid is not argued (residual)

**M29** — A fixed symbolic move-grammar props up and structures a generative language-model coder.
  · agent: a fixed symbolic move-grammar · operation: scaffolds · substrate: a generative language-model coder · outcome: not-stated · narrator: the methodology's authors
  · **gaps:** *reason* — why a fixed symbolic grammar is the right scaffolding choice for an LLM coder is not stated (residual); *degree* — how tightly or loosely the grammar constrains the LLM's generation is unspecified (residual); *reciprocity* — whether the LLM's outputs in turn refine or alter the grammar is left open (residual); *warrant* — what evidence or theory warrants that a fixed grammar reliably scaffolds a generative model is not given (residual)

**M30** — As a consequence of that scaffolding, the generation can be audited and each slot can be checked back against the text.
  · agent: not-stated · operation: is [auditable / checkable against] · substrate: the generation and every slot · outcome: auditable; every slot checkable against the text · narrator: the methodology's authors
  · **gaps:** *reason* — why auditability / slot-level checkability is a design goal rather than an incidental property is not stated (residual); *instrument* — the specific mechanism by which every slot is made checkable against the text is not named (residual); *warrant* — who or what certifies that every slot is in fact checkable is not stated (residual)

**M31** — The method puts its categories through an inter-rater reliability process run across multiple independent language models.
  · agent: the method · operation: validates · substrate: its categories · outcome: categories validated by inter-rater reliability across multiple independent language models · narrator: the methodology's authors
  · **gaps:** *reason* — why the method validates at all — the epistemic motivation for IRR is not stated (residual); *degree* — how many rounds, what agreement threshold constitutes 'validated' (residual); *reciprocity* — whether a failed IRR round revises or discards the category — validation's feedback direction (residual); *warrant* — on whose authority IRR-across-LLMs counts as validity — no methodological grounding is offered (residual)

**M32** — The method refrains from inventing its categories in advance of the data.
  · agent: the method · operation: does not author [a priori] · substrate: its categories · outcome: categories not pre-authored · narrator: the methodology's authors
  · **gaps:** *reason* — why avoid a priori authoring; M34's bias-visibility move implies the same anti-prejudgment motive (filled-internally); *degree* — how fully categories are withheld a priori — whether any seed schema is permitted (residual); *instrument* — by what procedural means authoring is prevented — the bottom-up mechanism is unnamed (residual); *warrant* — who authorizes the claim that non-pre-authoring produces less-biased categories (residual)

**M33** — The method keeps all coded data in one authoritative location rather than dispersing it across multiple files.
  · agent: the method · operation: stores [in a single store of record] / does not scatter [across files] · substrate: its coded data · outcome: data held in a single store of record · narrator: the methodology's authors
  · **gaps:** *reason* — why a single store of record rather than distributed files — the integrity rationale is unstated (residual); *instrument* — what technical system constitutes the single store — database type/schema not identified (residual); *warrant* — on whose authority consolidation into one store is the correct data-governance choice (residual)

**M34** — The method surfaces its biases rather than concealing them.
  · agent: the method · operation: makes [its biases] visible · substrate: its biases · outcome: biases visible · narrator: the methodology's authors
  · **gaps:** *reason* — why make biases visible; M35 (retain rather than filter) implies the same 'surface-don't-suppress' principle (filled-internally); *degree* — which biases, and how completely — whether visibility is exhaustive or selective (residual); *reciprocity* — whether surfaced biases feed back to alter categories or remain merely documented (residual); *interior* — what the reader or analyst experiences when bias is made visible — interpretive effect not described (residual); *instrument* — by what mechanism biases are surfaced — no disclosure protocol or audit procedure named (residual); *warrant* — says who which biases count as methodologically relevant and must be disclosed (residual)

**M35** — The method refrains from removing its biases from the data before analysis is conducted.
  · agent: the method · operation: does not filter [out before analysis] · substrate: its biases · outcome: biases retained in analysis · narrator: the methodology's authors
  · **gaps:** *reason* — why retain rather than filter; M34's visibility move supplies the anti-suppression rationale (filled-internally); *degree* — how fully biases are retained — whether any filtering threshold exists before analysis begins (residual); *reciprocity* — whether retained biases actively shape analytic outputs or merely coexist with them (residual); *instrument* — by what procedural means the method prevents pre-analysis filtering — no gate or checkpoint described (residual); *warrant* — on whose authority retention-over-filtering is the epistemically correct posture (residual)

**M36** — The method asserts that it can operate across different domains.
  · agent: the method · operation: claims · substrate: M11 · outcome: not-stated · narrator: the methodology's authors
  · **gaps:** *reason* — why the method claims on M11 at all — both the target (M11) and the motive are not-stated (residual); *degree* — how strong the claim on M11 is — strength, scope, and conditionality all absent (residual); *warrant* — says who authorizes a claim whose content is itself not-stated — warrant and claim content are jointly absent (residual)
  · **edges:** M36 —REPORTS→ M37

**M37** — A structural feature that holds steady across different domains belongs to the method itself, not to the particular text being analyzed.
  · agent: not-stated · operation: is [a property of] · substrate: a structure that survives a change of domain · outcome: a property of the method, not of the text · narrator: the methodology's authors
  · **gaps:** *reason* — why the property survives domain change is not stated — the structural invariance is asserted, not explained (residual); *degree* — how fully or reliably the property holds across domain changes is not quantified (residual); *instrument* — by what mechanism the method detects or preserves the property across domains is not stated (residual); *warrant* — on whose authority or by what evidence the property is declared domain-invariant is left entirely unsaid (residual)
  · **edges:** ["M36"] —REPORTS→ M37

**M38** — The method is capable of being applied to the very statement that describes it.
  · agent: not-stated · operation: can be run on · substrate: its own method-statement · outcome: not-stated · narrator: the methodology's authors
  · **gaps:** *reason* — why the method should or can be run on its own method-statement is not given (residual); *degree* — how completely the method applies to itself — full recursion or partial — is not specified (residual); *reciprocity* — whether the self-application yields a symmetrical result (method validates itself) or is one-directional is not stated (residual); *instrument* — the specific procedural means by which the method would process its own statement is not described (residual); *warrant* — no authority or demonstration is offered that self-application is coherent or has been tested (residual)
