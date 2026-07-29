# TEST-POETIC-ULYSSES — background sheet

> Full coded transcript for **TEST-POETIC-ULYSSES** — read-only snapshot from the DB.

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
| TEST-POETIC-ULYSSES | 38 | 0 | 0 | 0 |


## TEST-POETIC-ULYSSES

### Sitz — situational conditions (source_grounding)

_(no Sitz grounding row)_

### Paradigm — the scripts the text thinks with (+ its stance toward each)

_(none coded)_

### Frame — the 8-axis morphospace coordinate

_(none coded)_

### Coded moves — each with the context it picked up

**M1** — The thinker asserts that the world of what can be seen has an unavoidable manner or structure of appearing.
  · agent: I (the thinker) · operation: posit · substrate: the visible · outcome: an assertion that visibility has an ineluctable modality · narrator: the I of the monologue (first-person interior, own consciousness as authority)

**M2** — He grants, minimally, that at bare minimum his own thinking is channelled through his vision.
  · agent: I (the thinker) · operation: concede (at minimum) · substrate: my thought · outcome: an acknowledgment that thought is visually mediated · narrator: the I of the monologue (first-person interior, own consciousness as authority)

**M3** — He announces his standing purpose in this place: to interpret the marks that things themselves bear.
  · agent: I (the thinker) · operation: declare-task · substrate: signatures of all things · outcome: a self-declared task of reading them · narrator: the I of the monologue (first-person interior, own consciousness as authority)

**M4** — He notes the specific things in front of him — beach-debris, the incoming water, a corroded shoe.
  · agent: I (the thinker) · operation: observe (name-what-is-there) · substrate: seaspawn, seawrack, the nearing tide, that rusty boot · outcome: an inventory of what is present to the eye · narrator: the I of the monologue (first-person interior, own consciousness as authority)

**M5** — He labels the color-qualities of those things and groups them under the heading of colored indicators.
  · agent: I (the thinker) · operation: classify · substrate: snotgreen, bluesilver, rust (the colours of those things) · outcome: the classification 'coloured signs' · narrator: the I of the monologue (first-person interior, own consciousness as authority)

**M6** — He brings to mind an Aristotelian technical phrase about the borders of transparency.
  · agent: I (the thinker) · operation: recall (invoke a phrase) · substrate: the concept of the diaphane and its limits · outcome: the recalled phrase surfacing in mind · narrator: the I of the monologue (first-person interior, own consciousness as authority)
  · **edges:** M6 —REPORTS→ M7

**M7** — He remembers that the philosopher qualified the phrase by locating those borders within physical objects.
  · agent: he (Aristotle) · operation: add (report an addition) · substrate: the previously recalled formulation · outcome: the qualification that the limits are in bodies · narrator: the I of the monologue, quoting the philosopher inwardly
  · **edges:** ["M6"] —REPORTS→ M7

**M8** — He infers that, for the philosopher, awareness of solid objects came before awareness of their colours.
  · agent: he (Aristotle) · operation: be-aware (cognitive priority attributed) · substrate: bodies (prior to colours) · outcome: an awareness of bodies before an awareness of colours · narrator: the I of the monologue, inferring the philosopher's cognitive order

**M9** — He asks himself how such an awareness could have been arrived at.
  · agent: I (the thinker) · operation: question (self) · substrate: the prior claim about the philosopher's awareness · outcome: an open question about its mechanism · narrator: the I of the monologue (first-person interior, own consciousness as authority)

**M10** — He answers his own question by supposing that the philosopher literally bumped his head against the objects.
  · agent: I (the thinker), proposing an action of his (Aristotle) · operation: answer (self); propose a method · substrate: the question in M9 · outcome: the proposed mechanism (a head knocked against bodies) · narrator: the I of the monologue, half-mockingly answering himself

**M11** — He tells himself to pace it — not to push his thinking too hard.
  · agent: I (the thinker), addressed reflexively · operation: direct (self) · substrate: own pace of thinking · outcome: a self-imposed slowing directive · narrator: the I of the monologue (first-person interior, own consciousness as authority)

**M12** — He characterizes the philosopher as bald, wealthy, and (in the Dantean phrase) the master of those who know.
  · agent: he (Aristotle) as bearer of the states · operation: characterize (attribute states) · substrate: the philosopher's person · outcome: a portrait: bald, a millionaire, master of the knowers · narrator: the I of the monologue, sketching the philosopher fondly and mockingly

**M13** — He repeats the technical phrase, trailing off at the qualifier.
  · agent: I (the thinker) · operation: echo (repeat a phrase for reconsideration) · substrate: the recalled Aristotelian phrase, now truncated at its qualifier · outcome: the phrase held in mind, cut off mid-qualification · narrator: the I of the monologue (first-person interior, own consciousness as authority)

**M14** — He asks himself why the qualifier is needed at all.
  · agent: I (the thinker) · operation: question (self) · substrate: the qualifier just echoed · outcome: an open question about its necessity · narrator: the I of the monologue (first-person interior, own consciousness as authority)

**M15** — He sets the two Greek terms for transparent and non-transparent side by side.
  · agent: I (the thinker) · operation: juxtapose (terms) · substrate: the paired terms (transparent / non-transparent) · outcome: a live contrast held in mind · narrator: the I of the monologue (first-person interior, own consciousness as authority)

**M16** — He proposes a whimsical test for telling one kind of opening from another: whether one's hand can pass through it.
  · agent: I (the thinker) · operation: posit-rule (state a heuristic) · substrate: the distinction between passable and impassable openings · outcome: a stated rule of thumb (gate vs. door) · narrator: the I of the monologue, playing with the diaphane/adiaphane pairing

**M17** — He issues himself a paradoxical order — to close his eyes and yet still see.
  · agent: I (the thinker), addressed reflexively · operation: direct (self, paradoxically) · substrate: own eyes and own seeing · outcome: a paradoxical compound directive: close-and-see (a test of whether the visible persists apart from vision) · narrator: the I of the monologue, closing the passage on an experimental self-directive

**M18** — The external narrator reports that the young man shuts his eyes so as to attend to the crunching noise of his soles on the shore-debris.
  · agent: Stephen · operation: close (with a perceptual purpose) · substrate: his eyes · outcome: eyes shut, so that the sound of his soles on the beach-debris comes to the fore (the infinitival purpose folded in per the modifier rule) · narrator: the external third-person narrator of the novel (observing Stephen from outside)

**M19** — An inner voice addresses him in the second person, remarking that he is nonetheless still walking through it.
  · agent: you (the addressed self) · operation: address (you are walking) · substrate: it (the medium being traversed on the strand) · outcome: an assertion that the walking is going on regardless · narrator: the I of the monologue in its second-person self-addressing register

**M20** — He replies in the first person, confirming that he is — one step at a time.
  · agent: I · operation: affirm (I am, step by step) · substrate: the walking just asserted of him · outcome: confirmation that the walking is ongoing, discretised into strides · narrator: the I of the monologue, now answering itself in first person

**M21** — He formulates the walking chiastically as a slim duration passing through slim locations.
  · agent: I (the thinker, implicit) · operation: characterise (chiasmus of time-through-space) · substrate: the walking as a joined time-and-space experience · outcome: a chiastic formulation: a short stretch of time crossing short stretches of space · narrator: the I of the monologue (first-person interior)

**M22** — He counts off a couple of paces and labels the mode as the one-after-the-other of temporal succession.
  · agent: I (the thinker, implicit) · operation: count-and-name (instance yielding classification) · substrate: successive steps as a temporal series · outcome: the classification of the walking-mode as the temporal-succession mode · narrator: the I of the monologue (first-person interior)

**M23** — He affirms the label and posits the parallel principle: what can be heard has its own unavoidable manner of appearing.
  · agent: I (the thinker, implicit) · operation: posit (with an initial self-affirmation) · substrate: the audible · outcome: the assertion that the audible has an ineluctable modality (parallel to the visible) · narrator: the I of the monologue (first-person interior)

**M24** — He orders himself to open his eyes.
  · agent: you (self-addressed) · operation: direct (self) · substrate: own eyes · outcome: a self-directive to open them · narrator: the I of the monologue in its self-addressing register

**M25** — He refuses.
  · agent: I · operation: refuse (the just-issued directive) · substrate: the directive in M7 · outcome: a refusal (the eyes stay shut) · narrator: the I of the monologue (first-person interior)

**M26** — He exclaims in alarm.
  · agent: I · operation: exclaim (alarm) · substrate: not-stated · outcome: an involuntary outburst breaking the reflection · narrator: the I of the monologue (first-person interior)

**M27** — He imagines the counterfactual scene of tumbling from an overhanging cliff and dropping inescapably through the side-by-side mode of space.
  · agent: I (as protagonist of the imagined scenario) · operation: imagine (counterfactual) · substrate: the possibility of a fall from an overhanging cliff · outcome: an imagined plunge through the spatial-juxtaposition mode (nebeneinander), unavoidably · narrator: the I of the monologue, staging a counterfactual to himself (with an audible Hamlet echo)

**M28** — He assesses his sightless progress as going well.
  · agent: I · operation: assess (own progress in the dark) · substrate: own walking with eyes shut · outcome: the characterisation that it is proceeding well · narrator: the I of the monologue (first-person interior)

**M29** — He notes the ashplant hanging at his hip.
  · agent: my ash sword (the object as state-bearer) · operation: hang (state description of an object at his side) · substrate: not-stated · outcome: the state of hanging at his side · narrator: the I of the monologue, noting the object inwardly

**M30** — He tells himself to strike the ground with it.
  · agent: you (self-addressed) · operation: direct (self, to tap with the stick) · substrate: the ashplant (as instrument) · outcome: a self-directive to use it as a probe · narrator: the I of the monologue in its self-addressing register

**M31** — He observes that the sightless as a practice do just that.
  · agent: they (the blind, implicit) · operation: observe (a practice attributed to the blind) · substrate: not-stated (a probing-stick, understood from M13) · outcome: the observation that this is what they habitually do · narrator: the I of the monologue, drawing on cultural knowledge to warrant the directive

**M32** — He observes his feet ending his legs side by side, in the spatial-juxtaposition mode.
  · agent: my two feet in his boots (as state-bearer) · operation: observe-and-name (a spatial state named as the side-by-side mode) · substrate: not-stated · outcome: the state 'at the ends of his legs, side-by-side' — an instance labelled as the spatial mode · narrator: the I of the monologue, applying Lessing's category to his own body

**M33** — He characterises the tapping noise as having a solid quality.
  · agent: the tap-sound (as state-bearer) · operation: characterise (the tap-sound as solid-sounding) · substrate: not-stated · outcome: the auditory quality 'solid' predicated of the sound · narrator: the I of the monologue, judging what the ear returns

**M34** — He mythologises the sound as forged by Blake's demiurge Los with his hammer.
  · agent: the hammer of Los the demiurge · operation: make (the sound, mythically attributed) · substrate: the sounded material of the world · outcome: the tap-sound produced as if by a cosmic smithing · narrator: the I of the monologue, staging a mythic attribution for the auditory quality just heard

**M35** — He asks himself whether his walk along the beach is a walk into eternity.
  · agent: I · operation: question (self, metaphysical) · substrate: own walking along the beach · outcome: an open metaphysical question about eternity as the walk's destination · narrator: the I of the monologue, interrogating its own act

**M36** — He registers a run of crunching sounds onomatopoeically.
  · agent: not-stated (the boot-shell collisions producing the noise) · operation: sound (a crunching sequence registered) · substrate: not-stated · outcome: a sequence of crunches and cricks admitted to the ear · narrator: the I of the monologue, letting the audible arrive as bare sound

**M37** — He renames the shells underfoot as untamed currency of the sea.
  · agent: I (the thinker, implicit) · operation: name (a metaphoric re-labelling) · substrate: the shells underfoot · outcome: the poetic name 'wild sea money' for them · narrator: the I of the monologue, letting a poetic image rise

**M38** — He recalls that his schoolmaster employer is expert in all such money.
  · agent: Dominie Deasy · operation: know (attributed expertise) · substrate: them all (the coins-and-shells of the previous naming) · outcome: the state of being expert in them · narrator: the I of the monologue, drily remembering the schoolmaster
