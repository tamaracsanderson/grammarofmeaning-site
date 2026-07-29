# NICENE-325 — background sheet

> Full coded transcript for **NICENE-325** — read-only snapshot from the DB.

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
| NICENE-325 | 31 | 0 | 0 | 0 |


## NICENE-325

### Sitz — situational conditions (source_grounding)

- **summary:** The Nicene Creed of 325 CE is directly produced by [POL-COUNCIL-NICAEA], the first ecumenical council convened by Constantine, whose [POL-CONSTANTINE-EDICT] of 313 CE made such an imperially-sponsored gathering possible by legalizing Christianity and enabling bishops to assemble under state patronage. The creed's polemical anathemas against 'there was a time when he was not' target the Arian controversy centered in Alexandria, where [FIG-ATHANASIUS-ALEXANDRIA-330] (then deacon accompanying bishop Alexander) was a key anti-Arian voice. The prior North African episcopal tradition of conciliar creedal definition exemplified by [FIG-CYPRIAN-CARTHAGE-250] supplies the institutional template of bishops speaking collectively for 'the holy catholic and apostolic Church.' MODEL-KNOWLEDGE: the specific figure of Arius of Alexandria (~256-336) whose subordinationist Christology is the direct polemical target is not in the supplied substrate list.
- **categories:** ["political_institutional", "interreligious_contact", "communication_media"]
- **layers:** ["polemical", "cultural_intellectual"]

### Paradigm — the scripts the text thinks with (+ its stance toward each)

_(none coded)_

### Frame — the 8-axis morphospace coordinate

_(none coded)_

### Coded moves — each with the context it picked up

**M1** — The assembled 'we' profess trust in the reality of a single God identified as the Father Almighty.
  · agent: we · operation: believe-in · substrate: the proposition that there is one God, the Father Almighty, Maker of all · outcome: that proposition confessed as held · narrator: the assembled bishops, first-person-plural conciliar voice, authority = shared confession
  · **edges:** M1 —CONTAINS→ M3; M1 —REPORTS→ M2

**M2** — There is one God, and this God is the Father, holding all power.
  · agent: not-stated · operation: be-identified-as · substrate: the divine · outcome: identified as one, as Father, and as almighty · narrator: same conciliar 'we', now unfolding what is confessed
  · **edges:** ["M1"] —REPORTS→ M2

**M3** — This same Father is the one who produced everything, both what can be seen and what cannot.
  · agent: the Father · operation: make · substrate: all things visible and invisible · outcome: all things visible and invisible as made · narrator: same conciliar 'we'
  · **edges:** ["M1"] —CONTAINS→ M3

**M4** — The same 'we' profess trust in a second object: one Lord, Jesus Christ, understood in the manifold way to follow.
  · agent: we · operation: believe-in · substrate: the proposition that Jesus Christ is one Lord, Son of the Father, of the Father's essence, of one substance with the Father, and the one through whom all was made · outcome: that proposition confessed as held · narrator: same conciliar 'we'
  · **edges:** M4 —CONTAINS→ M10; M4 —CONTAINS→ M11; M4 —CONTAINS→ M12; M4 —CONTAINS→ M13; M4 —CONTAINS→ M14; M4 —CONTAINS→ M15; M4 —CONTAINS→ M16; M4 —CONTAINS→ M17; M4 —CONTAINS→ M18; M4 —CONTAINS→ M6; M4 —CONTAINS→ M7; M4 —CONTAINS→ M8; M4 —CONTAINS→ M9; M4 —REPORTS→ M5

**M5** — Jesus Christ is the single Lord.
  · agent: not-stated · operation: be-identified-as · substrate: Jesus Christ · outcome: identified as one Lord · narrator: same conciliar 'we'
  · **edges:** ["M4"] —REPORTS→ M5

**M6** — Jesus is the Son that belongs to God.
  · agent: not-stated · operation: be-identified-as · substrate: Jesus Christ · outcome: identified as Son of God · narrator: same conciliar 'we'
  · **edges:** ["M4"] —CONTAINS→ M6

**M7** — The Father generated this Son — uniquely, and out of what the Father himself IS.
  · agent: the Father · operation: beget · substrate: the Son · outcome: the Son as begotten, uniquely, from the Father's own essence · narrator: same conciliar 'we'
  · **edges:** ["M4"] —CONTAINS→ M7

**M8** — Whatever the Father is as divine, as luminous, as truly-divine — the Son is the same, drawn from the Father.
  · agent: not-stated · operation: be-of-same-kind-as · substrate: the Son · outcome: identified as God-from-God, Light-from-Light, very-God-from-very-God · narrator: same conciliar 'we'
  · **edges:** ["M4"] —CONTAINS→ M8

**M9** — The Son's coming-to-be is of the generative kind, and expressly NOT of the crafted kind.
  · agent: not-stated (implicit: the confessing 'we' marking the distinction) · operation: distinguish (assert-and-deny) · substrate: the mode of the Son's origin · outcome: affirmed as begetting, denied as making · narrator: same conciliar 'we', now visibly ruling out an opposing account
  · **edges:** ["M4"] —CONTAINS→ M9

**M10** — The Son and the Father share one and the same underlying reality.
  · agent: not-stated · operation: be-of-one-substance-with · substrate: the Son (in relation to the Father) · outcome: identified as of one substance with the Father · narrator: same conciliar 'we'
  · **edges:** ["M4"] —CONTAINS→ M10

**M11** — It was through this Son that everything, heavenly and earthly, was brought into being.
  · agent: the Son (as the one through whom) · operation: make · substrate: all things, in heaven and on earth · outcome: all things as made through the Son · narrator: same conciliar 'we'
  · **edges:** ["M4"] —CONTAINS→ M11

**M12** — The Son descended, and the purpose of that descent was human beings and their being-saved.
  · agent: the Son · operation: come-down · substrate: not-stated (the from-above) · outcome: descent, for the sake of humans and their salvation · narrator: same conciliar 'we'
  · **edges:** ["M4"] —CONTAINS→ M12

**M13** — The Son took on flesh.
  · agent: the Son (as undergoer of the enfleshing) · operation: be-enfleshed · substrate: not-stated (flesh, implicitly) · outcome: the Son as enfleshed · narrator: same conciliar 'we'
  · **edges:** ["M4"] —CONTAINS→ M13

**M14** — The Son was rendered a human being.
  · agent: the Son (as undergoer) · operation: be-made-human · substrate: not-stated · outcome: the Son as a human being · narrator: same conciliar 'we'
  · **edges:** ["M4"] —CONTAINS→ M14

**M15** — He underwent suffering.
  · agent: he (the Son as undergoer) · operation: suffer · substrate: not-stated · outcome: having-suffered · narrator: same conciliar 'we'
  · **edges:** ["M4"] —CONTAINS→ M15

**M16** — On the third day he came up alive again.
  · agent: he (the Son) · operation: rise · substrate: not-stated (the state of death, implicitly) · outcome: risen, on the third day · narrator: same conciliar 'we'
  · **edges:** ["M4"] —CONTAINS→ M16

**M17** — He went up into heaven.
  · agent: he (the Son) · operation: ascend · substrate: not-stated (from earth) · outcome: in heaven · narrator: same conciliar 'we'
  · **edges:** ["M4"] —CONTAINS→ M17

**M18** — From heaven he will come again — and the purpose of that coming will be to render judgment over the living and the dead.
  · agent: he (the Son) · operation: come (future) · substrate: not-stated (from heaven, toward the world) · outcome: future coming, for the purpose of judging the living and the dead · narrator: same conciliar 'we'
  · **edges:** ["M4"] —CONTAINS→ M18

**M19** — The same 'we' profess trust in a third object: the Holy Spirit — with no further predication given.
  · agent: we · operation: believe-in · substrate: the Holy Ghost · outcome: the Holy Ghost confessed as held-in-trust · narrator: same conciliar 'we'

**M20** — The Church, in its catholic and apostolic character, formally places outside its bounds those who put forward the following claims about the Son.
  · agent: the holy catholic and apostolic Church · operation: condemn · substrate: those who make the following claims about the Son · outcome: those persons ruled outside the Church's confession · narrator: the assembled bishops speaking as the Church, authority = conciliar consensus in anathematic register
  · **edges:** M20 —CONTAINS→ M21; M20 —CONTAINS→ M22; M20 —CONTAINS→ M23; M20 —CONTAINS→ M24

**M21** — These people make the assertion that there was some past moment at which the Son did not exist.
  · agent: those (the condemned parties) · operation: say · substrate: the proposition M6 · outcome: that proposition attributed to them as held · narrator: same conciliar 'we', attributing the claim to opponents
  · **edges:** M21 —REPORTS→ M25; ["M20"] —CONTAINS→ M21

**M22** — They also assert that prior to being brought into being, the Son was not.
  · agent: those (the condemned parties) · operation: say · substrate: the proposition M7 · outcome: that proposition attributed to them as held · narrator: same
  · **edges:** M22 —REPORTS→ M26; ["M20"] —CONTAINS→ M22

**M23** — They further assert that the Son was produced out of nothing at all.
  · agent: those (the condemned parties) · operation: say · substrate: the proposition M8 · outcome: that proposition attributed to them as held · narrator: same
  · **edges:** M23 —REPORTS→ M27; ["M20"] —CONTAINS→ M23

**M24** — They also assert, in a cluster of alternative claims, that the Son belongs to a different underlying reality than the Father, or is a creature, or is subject to change, or is subject to alteration.
  · agent: those (the condemned parties) · operation: say · substrate: the disjunctive proposition-set M9 / M10 / M11 / M12 · outcome: each of those alternative claims attributed to them as held · narrator: same
  · **edges:** M24 —CONTAINS→ M28; M24 —CONTAINS→ M29; M24 —CONTAINS→ M30; M24 —CONTAINS→ M31; ["M20"] —CONTAINS→ M24

**M25** — There was a past interval during which the Son did not exist.
  · agent: not-stated · operation: not-exist (at a time) · substrate: the Son · outcome: predicated as non-existent during some past interval · narrator: same, quoting the opponents' content
  · **edges:** ["M21"] —REPORTS→ M25

**M26** — Before the point of his being produced, the Son did not exist.
  · agent: not-stated · operation: not-exist (prior to being made) · substrate: the Son · outcome: predicated as non-existent prior to his being made · narrator: same
  · **edges:** ["M22"] —REPORTS→ M26

**M27** — The Son was produced, and the material-or-source out of which he was produced was nothing.
  · agent: not-stated · operation: make · substrate: nothing (as the from-which) · outcome: the Son as made out of nothing · narrator: same
  · **edges:** ["M23"] —REPORTS→ M27

**M28** — The Son of God has an underlying reality different from that of the Father.
  · agent: not-stated · operation: be-of-different-substance-than · substrate: the Son of God (in relation to the Father) · outcome: predicated as of another substance or essence · narrator: same
  · **edges:** ["M24"] —CONTAINS→ M28

**M29** — The Son of God is a produced thing.
  · agent: not-stated · operation: be-created · substrate: the Son of God · outcome: predicated as a creature · narrator: same
  · **edges:** ["M24"] —CONTAINS→ M29

**M30** — The Son of God is capable of undergoing change.
  · agent: not-stated · operation: be-changeable · substrate: the Son of God · outcome: predicated as changeable · narrator: same
  · **edges:** ["M24"] —CONTAINS→ M30

**M31** — The Son of God is capable of being altered.
  · agent: not-stated · operation: be-alterable · substrate: the Son of God · outcome: predicated as alterable · narrator: same
  · **edges:** ["M24"] —CONTAINS→ M31
