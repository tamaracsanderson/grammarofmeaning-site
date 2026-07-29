# NICENE-381 — background sheet

> Full coded transcript for **NICENE-381** — read-only snapshot from the DB.

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
| NICENE-381 | 33 | 0 | 0 | 0 |


## NICENE-381

### Sitz — situational conditions (source_grounding)

- **summary:** The Nicene-Constantinopolitan Creed of 381 CE is the direct product of the Trinitarian controversy set in motion by [POL-COUNCIL-NICAEA] in 325 CE and carried forward by [FIG-ATHANASIUS-ALEXANDRIA-330] and the [FIG-CAPPADOCIAN-FATHERS-370], whose pro-Nicene theology of the Son's homoousion and the Spirit's full divinity is what the creed's expanded third article ratifies. Its promulgation is inseparable from [POL-CONSTANTINE-EDICT] (313 CE), which made conciliar Christianity legally possible, and above all from [POL-THEODOSIUS-CHRISTIAN-STATE] (380 CE), whose Edict of Thessalonica made Nicene Christianity the Roman state religion and directly occasioned the Council of Constantinople (381) that issued this text. MODEL-KNOWLEDGE: the specific convening event is the First Council of Constantinople (381 CE) under Theodosius I, called to settle Pneumatomachian ('Macedonian') and residual Homoian-Arian disputes; the text is also shaped by imperial postal/road infrastructure enabling ecumenical bishop-gatherings and by Greek-language koine-plus-philosophical vocabulary (ousia, hypostasis) as the shared medium of the eastern episcopate.
- **categories:** ["political_institutional", "interreligious_contact", "communication_media", "demographic_social"]
- **layers:** ["cultural_intellectual", "polemical", "ecological_material_geographical"]

### Paradigm — the scripts the text thinks with (+ its stance toward each)

_(none coded)_

### Frame — the 8-axis morphospace coordinate

_(none coded)_

### Coded moves — each with the context it picked up

**M1** — The confessing 'we' declare their trust in a single God who is Father and Almighty.
  · agent: we · operation: believe · substrate: one God, the Father Almighty · outcome: not-stated · narrator: the confessing 'we' of the council, speaking as authorised church-voice
  · **edges:** M1 —CONTAINS→ M3; M1 —REPORTS→ M2

**M2** — God is titled as one, as Father, and as Almighty.
  · agent: not-stated · operation: title-as · substrate: God · outcome: one / Father / Almighty · narrator: the confessing 'we'
  · **edges:** ["M1"] —REPORTS→ M2

**M3** — That same God is the one who made the sky, the earth, and everything seen and unseen.
  · agent: God the Father Almighty · operation: make · substrate: heaven and earth, and all things visible and invisible · outcome: heaven, earth, and all things (as made) · narrator: the confessing 'we'
  · **edges:** ["M1"] —CONTAINS→ M3

**M4** — The confessing 'we' extend their trust to one Lord, Jesus Christ.
  · agent: we · operation: believe · substrate: one Lord Jesus Christ (as unpacked in M5ff) · outcome: not-stated · narrator: the confessing 'we'
  · **edges:** M4 —CONTAINS→ M10; M4 —CONTAINS→ M11; M4 —CONTAINS→ M12; M4 —CONTAINS→ M13; M4 —CONTAINS→ M14; M4 —CONTAINS→ M15; M4 —CONTAINS→ M16; M4 —CONTAINS→ M17; M4 —CONTAINS→ M18; M4 —CONTAINS→ M19; M4 —CONTAINS→ M20; M4 —CONTAINS→ M21; M4 —CONTAINS→ M6; M4 —CONTAINS→ M7; M4 —CONTAINS→ M8; M4 —CONTAINS→ M9; M4 —REPORTS→ M5

**M5** — Jesus Christ is titled the only-begotten Son of God.
  · agent: not-stated · operation: title-as · substrate: Jesus Christ · outcome: only-begotten Son of God · narrator: the confessing 'we'
  · **edges:** ["M4"] —REPORTS→ M5

**M6** — The Father begets the Son before any world exists.
  · agent: the Father · operation: beget · substrate: the Son · outcome: the Son as begotten, prior to all worlds · narrator: the confessing 'we'
  · **edges:** ["M4"] —CONTAINS→ M6

**M7** — The Son is titled Light-from-Light and true-God-from-true-God.
  · agent: not-stated · operation: title-as · substrate: the Son · outcome: Light of Light, very God of very God · narrator: the confessing 'we'
  · **edges:** ["M4"] —CONTAINS→ M7

**M8** — The Son is affirmed as begotten and specifically denied as made.
  · agent: not-stated · operation: affirm-and-deny · substrate: the Son · outcome: begotten (yes) / made (no) · narrator: the confessing 'we'
  · **edges:** ["M4"] —CONTAINS→ M8

**M9** — The Son is declared to share one and the same substance with the Father.
  · agent: not-stated · operation: predicate-same-substance · substrate: the Son (in relation to the Father) · outcome: of one substance with the Father (homoousios) · narrator: the confessing 'we'
  · **edges:** ["M4"] —CONTAINS→ M9

**M10** — All things came into being through him as the one through whom they were made.
  · agent: God, acting through the Son · operation: make-through · substrate: all things · outcome: all things (as made through him) · narrator: the confessing 'we'
  · **edges:** ["M4"] —CONTAINS→ M10

**M11** — For the sake of human beings and their rescue, he descended from heaven.
  · agent: the Son · operation: descend · substrate: heaven (as point of departure) · outcome: descent into the human sphere, for us and for our salvation · narrator: the confessing 'we'
  · **edges:** ["M4"] —CONTAINS→ M11

**M12** — By means of the Holy Spirit, and from the Virgin Mary, he took on flesh.
  · agent: the Holy Spirit (as through-agent), with the Virgin Mary (as of-whom) · operation: incarnate · substrate: the descended Son · outcome: the Son as enfleshed · narrator: the confessing 'we'
  · **edges:** ["M4"] —CONTAINS→ M12

**M13** — He became a human being.
  · agent: not-stated (implied divine action) · operation: become-human · substrate: the incarnate Son · outcome: the Son as man · narrator: the confessing 'we'
  · **edges:** ["M4"] —CONTAINS→ M13

**M14** — Under Pontius Pilate's authority, and for our sake, he was crucified.
  · agent: Pontius Pilate (as historical warrant), for us (as beneficiary) · operation: crucify · substrate: the incarnate Son · outcome: the Son as crucified · narrator: the confessing 'we'
  · **edges:** ["M4"] —CONTAINS→ M14

**M15** — He underwent suffering.
  · agent: not-stated · operation: suffer · substrate: the Son · outcome: the Son as one who suffered · narrator: the confessing 'we'
  · **edges:** ["M4"] —CONTAINS→ M15

**M16** — He was placed in a tomb.
  · agent: not-stated (those who buried him) · operation: bury · substrate: the dead Son · outcome: the Son as buried · narrator: the confessing 'we'
  · **edges:** ["M4"] —CONTAINS→ M16

**M17** — On the third day, in agreement with the scriptures, he rose.
  · agent: the Son · operation: rise · substrate: the state of being dead/buried · outcome: the Son as risen on the third day · narrator: the confessing 'we', warranted by 'the Scriptures'
  · **edges:** ["M4"] —CONTAINS→ M17

**M18** — He went up into heaven.
  · agent: the Son · operation: ascend · substrate: the earthly sphere (as point of departure) · outcome: the Son as ascended into heaven · narrator: the confessing 'we'
  · **edges:** ["M4"] —CONTAINS→ M18

**M19** — He is seated at the Father's right hand.
  · agent: not-stated · operation: sit-enthroned · substrate: the ascended Son · outcome: the Son as seated at the right hand of the Father · narrator: the confessing 'we'
  · **edges:** ["M4"] —CONTAINS→ M19

**M20** — He will come back, in glory, in order to judge the living and the dead.
  · agent: the Son · operation: come-again · substrate: the human world (implied) · outcome: a glorious return that judges the living and the dead · narrator: the confessing 'we'
  · **edges:** ["M4"] —CONTAINS→ M20

**M21** — The reign that belongs to him will never end.
  · agent: not-stated · operation: predicate-endlessness · substrate: his kingdom · outcome: no end (unending duration) · narrator: the confessing 'we'
  · **edges:** ["M4"] —CONTAINS→ M21

**M22** — The confessing 'we' extend their trust to the Holy Spirit as well.
  · agent: we · operation: believe · substrate: the Holy Ghost (as unpacked in M2ff) · outcome: not-stated · narrator: the confessing 'we' of the council, speaking as authorised church-voice
  · **edges:** M22 —CONTAINS→ M24; M22 —CONTAINS→ M25; M22 —CONTAINS→ M26; M22 —REPORTS→ M23

**M23** — The Spirit is titled Lord and the one who gives life.
  · agent: not-stated · operation: title-as · substrate: the Holy Ghost · outcome: the Lord and Giver of life · narrator: the confessing 'we'
  · **edges:** ["M22"] —REPORTS→ M23

**M24** — The Spirit issues forth from the Father.
  · agent: the Holy Ghost · operation: proceed-from · substrate: the Father (as source) · outcome: the Spirit as one who proceeds from the Father · narrator: the confessing 'we'
  · **edges:** ["M22"] —CONTAINS→ M24

**M25** — The Spirit receives worship and glorification jointly with the Father and the Son.
  · agent: not-stated (the worshipping community, implied) · operation: co-worship-and-glorify · substrate: the Spirit, alongside the Father and the Son · outcome: the Spirit as co-worshipped and co-glorified with the Father and the Son · narrator: the confessing 'we'
  · **edges:** ["M22"] —CONTAINS→ M25

**M26** — The Spirit is the one who spoke through the prophets.
  · agent: the Holy Ghost · operation: speak-through · substrate: the prophets (as mouthpieces) · outcome: prophetic speech as Spirit-uttered · narrator: the confessing 'we'
  · **edges:** ["M22"] —CONTAINS→ M26

**M27** — The confessing 'we' extend their trust onto the Church.
  · agent: we · operation: believe · substrate: one holy catholic and apostolic Church (as unpacked in M7) · outcome: not-stated · narrator: the confessing 'we'
  · **edges:** M27 —REPORTS→ M28

**M28** — The Church is titled as one, holy, universal, and apostolic.
  · agent: not-stated · operation: title-as · substrate: the Church · outcome: one / holy / catholic / apostolic · narrator: the confessing 'we'
  · **edges:** ["M27"] —REPORTS→ M28

**M29** — The confessing 'we' avow a single baptism whose purpose is the wiping away of sins.
  · agent: we · operation: acknowledge · substrate: one baptism, for the remission of sins · outcome: not-stated · narrator: the confessing 'we'

**M30** — The confessing 'we' expectantly await the raising of the dead.
  · agent: we · operation: look-for · substrate: the resurrection of the dead (as unpacked in M10) · outcome: not-stated · narrator: the confessing 'we'
  · **edges:** M30 —CONTAINS→ M32; M30 —REPORTS→ M31

**M31** — The dead will be raised.
  · agent: not-stated (God, implied) · operation: raise · substrate: the dead · outcome: the dead as raised · narrator: the confessing 'we'
  · **edges:** ["M30"] —REPORTS→ M31

**M32** — There will be a life belonging to the age that is coming.
  · agent: not-stated · operation: predicate-future-life · substrate: the world/age to come · outcome: life proper to that coming world · narrator: the confessing 'we'
  · **edges:** ["M30"] —CONTAINS→ M32

**M33** — The confessing 'we' set their seal of assent to the whole preceding confession.
  · agent: we · operation: assent · substrate: the entire preceding confession · outcome: the confession as ratified / said-so · narrator: the confessing 'we'
