# TEST-POETIC-ZHUANGZI — background sheet

> Full coded transcript for **TEST-POETIC-ZHUANGZI** — read-only snapshot from the DB.

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
| TEST-POETIC-ZHUANGZI | 24 | 0 | 0 | 0 |


## TEST-POETIC-ZHUANGZI

### Sitz — situational conditions (source_grounding)

_(no Sitz grounding row)_

### Paradigm — the scripts the text thinks with (+ its stance toward each)

_(none coded)_

### Frame — the 8-axis morphospace coordinate

_(none coded)_

### Coded moves — each with the context it picked up

**M1** — The half-shadow puts a question to the shadow, addressing the shadow's changing behavior.
  · agent: the Penumbra (the half-shadow) · operation: ask (put a question to) · substrate: the question posed to the Shadow (nested content) · outcome: the Shadow addressed; an inquiry into the Shadow's instability opened · narrator: the parable's anonymous Zhuangist teller (third-person; authority = fable-tradition, not eyewitness)
  · **edges:** M1 —CONTAINS→ M2; M1 —REPORTS→ M3

**M2** — The half-shadow points out that the shadow keeps switching between motion and rest — going, then halting; sitting, then standing.
  · agent: the Penumbra · operation: point-out / describe (attribute a pattern of transitions) · substrate: the Shadow's alternations between walking-and-stopping, sitting-and-rising · outcome: inconsistency of the Shadow's conduct noted · narrator: the parable's anonymous Zhuangist teller
  · **edges:** ["M1"] —CONTAINS→ M2

**M3** — The half-shadow demands to know why the shadow has no fixed way of its own.
  · agent: the Penumbra · operation: ask-why (inquire after a cause) · substrate: the Shadow's lack of a stable pattern · outcome: an explanation of the Shadow's want-of-stability demanded · narrator: the parable's anonymous Zhuangist teller
  · **edges:** ["M1"] —REPORTS→ M3

**M4** — The shadow answers the half-shadow.
  · agent: the Shadow · operation: reply (respond to a question) · substrate: the Shadow's response (nested content) · outcome: the Penumbra's question receives an answer · narrator: the parable's anonymous Zhuangist teller
  · **edges:** M4 —CONTAINS→ M6; M4 —CONTAINS→ M7; M4 —CONTAINS→ M8; M4 —REPORTS→ M5

**M5** — The shadow avows that its own doing hangs on the movements of some other thing.
  · agent: I (the Shadow) · operation: wait-on / depend-on (avow one's own contingency) · substrate: what I do (my action) · outcome: my doing is contingent on the movements of something else · narrator: the parable's anonymous Zhuangist teller (the Shadow speaks; the teller reports)
  · **edges:** ["M4"] —REPORTS→ M5

**M6** — The shadow extends the point: the very thing it hangs on itself hangs on something further.
  · agent: that something-else on which I wait · operation: wait-on / depend-on (predicate the same contingency of another agent) · substrate: its action (as it does) · outcome: its doing is contingent on yet another — the dependency-chain iterates · narrator: the parable's anonymous Zhuangist teller
  · **edges:** ["M4"] —CONTAINS→ M6

**M7** — The shadow rhetorically wonders whether what it hangs on is something as slight as a snake's underside or an insect's wing.
  · agent: I (the Shadow) · operation: ask (rhetorical wondering about the specific object of dependence) · substrate: the object of my waiting (whatever it may be) · outcome: the specific object of the dependence is foregrounded as unknowable / indeterminable · narrator: the parable's anonymous Zhuangist teller
  · **edges:** ["M4"] —CONTAINS→ M7

**M8** — The shadow disavows any knowledge of the reason behind its acting or its refraining.
  · agent: I (the Shadow) · operation: disavow-knowledge (declare inability to know) · substrate: the reasons for my doing one thing or not-doing another · outcome: the causal ground of my action is declared beyond my knowing · narrator: the parable's anonymous Zhuangist teller
  · **edges:** ["M4"] —CONTAINS→ M8

**M9** — The teller reports that his past self, some while ago, underwent a dream-episode.
  · agent: I / Zhuang Zhou (past self) · operation: dream (cognition-perception) · substrate: the dream-content (nested) · outcome: past-self occupies a dream-state · narrator: Zhuang Zhou telling his own experience in first-person retrospective; authority-source = personal dream-memory
  · **edges:** M9 —CONTAINS→ M11; M9 —CONTAINS→ M12; M9 —CONTAINS→ M14; M9 —REPORTS→ M10

**M10** — Inside that dream, the dreamer took on butterfly-being.
  · agent: I (the dreamer, in the dream) · operation: be (identity in the dream-content) · substrate: butterfly-form · outcome: butterfly-identity assumed within the dream · narrator: Zhuang Zhou telling his own experience in first-person retrospective
  · **edges:** ["M9"] —REPORTS→ M10

**M11** — The dream-butterfly moved about in flight.
  · agent: the butterfly (= I within the dream) · operation: fly-about (motion) · substrate: not-stated · outcome: flight underway · narrator: Zhuang Zhou telling his own experience in first-person retrospective
  · **edges:** ["M9"] —CONTAINS→ M11

**M12** — The dream-butterfly registered a sense of its own enjoyment.
  · agent: it (the butterfly) · operation: feel-that (cognition / self-perception) · substrate: the self-enjoyment proposition (nested) · outcome: self-enjoyment registered / felt · narrator: Zhuang Zhou telling his own experience in first-person retrospective
  · **edges:** M12 —REPORTS→ M13; ["M9"] —CONTAINS→ M12

**M13** — The dream-butterfly was in a state of taking pleasure in itself.
  · agent: it (the butterfly) · operation: enjoy-oneself (reflexive affect) · substrate: itself (as object of enjoyment) · outcome: self-enjoyment obtaining · narrator: Zhuang Zhou telling his own experience in first-person retrospective
  · **edges:** ["M12"] —REPORTS→ M13

**M14** — Within that dream, the dreamer had no awareness that its identity was that of the teller.
  · agent: I (the dreamer, in the dream-state) · operation: not-know (disavowal of cognition / absence of awareness) · substrate: the proposition about the dreamer's identity (nested) · outcome: self-identification with the teller absent · narrator: Zhuang Zhou telling his own experience in first-person retrospective
  · **edges:** M14 —REPORTS→ M15; ["M9"] —CONTAINS→ M14

**M15** — In fact the dreamer's identity was that of the teller.
  · agent: it (the dreamer) · operation: be (identity) · substrate: the teller's identity · outcome: the dreamer identifies with the teller in fact · narrator: Zhuang Zhou telling his own experience in first-person retrospective
  · **edges:** ["M14"] —REPORTS→ M15

**M16** — The teller's past self came out of the dream abruptly.
  · agent: I (the teller, at the transition-moment) · operation: awake (transition out of dream) · substrate: the dream-state · outcome: waking-state entered · narrator: Zhuang Zhou telling his own experience in first-person retrospective

**M17** — The teller's past self returned to being his settled self, unambiguously himself.
  · agent: I (the teller) · operation: be-oneself-again (identity re-inhabited) · substrate: the teller's own identity · outcome: the teller's identity restored, felt as unambiguous · narrator: Zhuang Zhou telling his own experience in first-person retrospective

**M18** — The teller cannot decide which of two possibilities describes what actually happened.
  · agent: I (the teller, present-time-of-telling) · operation: not-know (disavow-knowledge of which alternative holds) · substrate: the disjunction of two dream-directions (nested set) · outcome: the direction of dreaming declared undecidable · narrator: Zhuang Zhou telling his own experience in first-person retrospective
  · **edges:** M18 —CONTAINS→ M19; M18 —CONTAINS→ M21

**M19** — Alternative one: the teller (in the past) had a dream in which he took butterfly-form.
  · agent: the teller (formerly) · operation: dream (cognition-perception) · substrate: the butterfly-content (nested) · outcome: past-teller occupies a dream-state whose content is butterfly-being · narrator: Zhuang Zhou telling his own experience in first-person retrospective
  · **edges:** M19 —REPORTS→ M20; ["M18"] —CONTAINS→ M19

**M20** — In that hypothesis-dream, he took butterfly-form.
  · agent: he (the past-teller, in the hypothesis-dream) · operation: be (identity) · substrate: butterfly-form · outcome: butterfly-identity assumed within the hypothesis-dream · narrator: Zhuang Zhou telling his own experience in first-person retrospective
  · **edges:** ["M19"] —REPORTS→ M20

**M21** — Alternative two: a butterfly is presently dreaming, and in its dream it takes the teller's form.
  · agent: a butterfly (in the present) · operation: dream (cognition-perception) · substrate: the teller-content (nested) · outcome: present-butterfly occupies a dream-state whose content is teller-being · narrator: Zhuang Zhou telling his own experience in first-person retrospective
  · **edges:** M21 —REPORTS→ M22; ["M18"] —CONTAINS→ M21

**M22** — In that hypothesis-dream, it takes the teller's form.
  · agent: it (the butterfly, in the hypothesis-dream) · operation: be (identity) · substrate: the teller's form · outcome: teller-identity assumed within the hypothesis-dream · narrator: Zhuang Zhou telling his own experience in first-person retrospective
  · **edges:** ["M21"] —REPORTS→ M22

**M23** — The teller affirms that some distinction has to obtain between his own form and the butterfly-form.
  · agent: I (the teller, as declarant) · operation: assert-necessity (a distinction must hold) · substrate: the relation between the teller's form and the butterfly-form · outcome: a distinction affirmed as obligatory / necessary · narrator: Zhuang Zhou telling his own experience in first-person retrospective

**M24** — The teller classifies this whole scenario as an instance of the category the tradition names as the transformation-of-things.
  · agent: I (the teller, as classifier) · operation: classify-as / name-as (labeling under a received category) · substrate: this (the whole preceding dream-and-reflection scenario) · outcome: the scenario tagged as an instance of the Transformation-of-Things (wu hua 物化); the label attributed to received usage · narrator: Zhuang Zhou telling his own experience in first-person retrospective; authority for the label = received tradition (‘what is called’)
