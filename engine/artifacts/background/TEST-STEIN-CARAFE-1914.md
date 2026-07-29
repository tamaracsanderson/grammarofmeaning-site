# TEST-STEIN-CARAFE-1914 — background sheet

> Full coded transcript for **TEST-STEIN-CARAFE-1914** — read-only snapshot from the DB.

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
| TEST-STEIN-CARAFE-1914 | 13 | 0 | 0 | 0 |


## TEST-STEIN-CARAFE-1914

### Sitz — situational conditions (source_grounding)

- **summary:** Stein's 'A Carafe, That Is a Blind Glass' (from Tender Buttons, 1914) sits inside the Neotechnic moment [MUMFORD-NEOTECHNIC] and the fin-de-siècle Vienna/psychoanalytic climate [DEM-FIN-DE-SIECLE-VIENNA] whose decentering of the unified subject [FIG-NIETZSCHE-1886] made a language of dispersed perception legible. MODEL-KNOWLEDGE: the immediate material substrate is Parisian avant-garde Cubism (Picasso/Braque analytic cubism c.1908-1914, Stein's salon at 27 rue de Fleurus) and the 1913 Armory Show — Stein is writing a verbal analogue to Cubist still-life, fracturing the domestic object (carafe) into simultaneous facets. MODEL-KNOWLEDGE: publication in June 1914 also sits on the eve of WWI, at the tail of the Second Industrial Revolution's mass-produced glassware and department-store display culture that made 'a spectacle' and 'an arrangement in a system' vernacular. The 'difference is spreading' registers the Neotechnic dissolution of stable reference under electricity, photography, and psychoanalytic interiority.
- **categories:** ["communication_media", "science_technology", "demographic_social", "economic_material"]
- **layers:** ["cultural_intellectual", "personal_biography"]

### Paradigm — the scripts the text thinks with (+ its stance toward each)

_(none coded)_

### Frame — the 8-axis morphospace coordinate

_(none coded)_

### Coded moves — each with the context it picked up

**M1** — The teller stacks a list of attributes onto the object: a kind held in glass, a cousin, a spectacle, an unremarkable thing, a single wounded color, an arrangement inside a system that points.
  · agent: not-stated · operation: attribute · substrate: the object (implied) · outcome: a bundle of attributes: kind-in-glass, cousin, spectacle, single hurt color, arrangement-in-a-system-to-pointing, and 'nothing strange' · narrator: unnamed teller, third-person descriptive, authority = perceptual composition

**M2** — The teller then evaluates that whole prior bundle: it is not ordinary, not unordered, and it does not resemble.
  · agent: not-stated · operation: evaluate-by-negation · substrate: the prior attribute-bundle ('all this') · outcome: three negative qualifications: not-ordinary, not-unordered, not-resembling · narrator: same teller, now reflecting back on what was just said

**M3** — The teller reports a process: the difference is enlarging.
  · agent: not-stated · operation: spread · substrate: the difference · outcome: an ongoing widening · narrator: same teller, stating a process without a doer

**M4** — From kindness, redness emerges.
  · agent: not-stated (redness comes) · operation: issue-from · substrate: kindness · outcome: redness · narrator: teller stating a generative relation

**M5** — From rudeness, a fast recurring question emerges.
  · agent: not-stated · operation: issue-from · substrate: rudeness · outcome: the rapid same question · narrator: same teller

**M6** — From an eye, research emerges.
  · agent: not-stated · operation: issue-from · substrate: an eye · outcome: research · narrator: same teller

**M7** — From selection, painful cattle emerge.
  · agent: not-stated · operation: issue-from · substrate: selection · outcome: painful cattle · narrator: same teller

**M8** — The teller now announces the ordering principle behind all that: 'the order is that X' — a framing act that scopes over the proposition to follow.
  · agent: not-stated (implicit teller) · operation: declare-the-order · substrate: the preceding series of emergences · outcome: an announced ordering, whose content is M9 · narrator: same teller, now speaking as one who states the pattern
  · **edges:** M8 —REPORTS→ M9

**M9** — A white manner of being round suggests a pin.
  · agent: a white way of being round · operation: suggest · substrate: a pin (as what is suggested) · outcome: suggestion-of-a-pin · narrator: same teller
  · **edges:** ["M8"] —REPORTS→ M9

**M10** — The teller poses a question about the prior claim: is it disappointing?
  · agent: the teller · operation: ask · substrate: the M9 suggestion · outcome: an open question about disappointingness · narrator: same teller turning briefly self-interrogative

**M11** — The teller answers her own question in the negative: no, it is not disappointing.
  · agent: the teller · operation: deny · substrate: the question in M10 · outcome: a denial of disappointingness · narrator: same teller

**M12** — The teller predicates of the object that it is elementary enough to be analysed and to yield a fine substance seen oddly.
  · agent: not-stated · operation: attribute · substrate: the object ('it') · outcome: rudimentary-enough-to-be-analysed-and-to-show-a-fine-substance-strangely · narrator: same teller resuming attributive description

**M13** — The teller predicates further: it is earnestly suggestive of being a green point that does not point to red but points again.
  · agent: not-stated · operation: attribute · substrate: the object ('it') · outcome: earnestly-suggestive-of-being-a-green-point-that-points-again-rather-than-to-red · narrator: same teller closing the portrait
