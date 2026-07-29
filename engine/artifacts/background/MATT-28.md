# MATT-28 — background sheet

> Full coded transcript for **MATT-28** — read-only snapshot from the DB.

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
| MATT-28 | 29 | 10 | 11 | 11 |


## MATT-28

### Full text — Matthew 28 (World English Bible, public domain)

**1** Now after the Sabbath, as it began to dawn on the first day of the week, Mary Magdalene and the other Mary came to see the tomb.
**2** Behold, there was a great earthquake, for an angel of the Lord descended from the sky, and came and rolled away the stone from the door, and sat on it.
**3** His appearance was like lightning, and his clothing white as snow.
**4** For fear of him, the guards shook, and became like dead men.
**5** The angel answered the women, “Don’t be afraid, for I know that you seek Jesus, who has been crucified.
**6** He is not here, for he has risen, just like he said. Come, see the place where the Lord was lying.
**7** Go quickly and tell his disciples, ‘He has risen from the dead, and behold, he goes before you into Galilee; there you will see him.’ Behold, I have told you.”
**8** They departed quickly from the tomb with fear and great joy, and ran to bring his disciples word.
**9** As they went to tell his disciples, behold, Jesus met them, saying,
“Rejoice!”
They came and took hold of his feet, and worshiped him.
**10** Then Jesus said to them,
“Don’t be afraid. Go tell my brothers

that they should go into Galilee, and there they will see me.”
**11** Now while they were going, behold, some of the guards came into the city, and told the chief priests all the things that had happened.
**12** When they were assembled with the elders, and had taken counsel, they gave a large amount of silver to the soldiers,
**13** saying, “Say that his disciples came by night, and stole him away while we slept.
**14** If this comes to the governor’s ears, we will persuade him and make you free of worry.”
**15** So they took the money and did as they were told. This saying was spread abroad among the Jews, and continues until today.
**16** But the eleven disciples went into Galilee, to the mountain where Jesus had sent them.
**17** When they saw him, they bowed down to him, but some doubted.
**18** Jesus came to them and spoke to them, saying,
“All authority has been given to me in heaven and on earth.
**19** Go
and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit,
**20** teaching them to observe all things that I commanded you. Behold, I am with you always, even to the end of the age.” Amen.

### Sitz — situational conditions (source_grounding)

- **summary:** Matthew 28 (composed ~80 CE) is written in the shadow of the First Jewish-Roman War and the destruction of the Second Temple [POL-FIRST-JEWISH-ROMAN-WAR], which had shattered Temple-centered Judaism a decade earlier and forced both rabbinic Judaism and the Jesus-movement to relocate authority — here, to the risen Jesus commissioning disciples in Galilee rather than Jerusalem. The narrative presupposes Roman judicial power [POL-HERODIAN-CLIENT-RULE, POL-PAX-ROMANA] (the crucifixion under a Roman prefecture, the posted guard) and the earlier ministry of Jesus in Galilee [FIG-JESUS-GALILEE-30]. The empty-tomb pericope also reflects MODEL-KNOWLEDGE: the post-70 CE Jewish-Christian polemical context (the 'stolen body' counter-narrative Matthew explicitly rebuts in 28:11-15) and intra-Jewish contestation over resurrection between Pharisaic and Sadducean parties.
- **categories:** ["political_institutional", "demographic_social", "interreligious_contact", "communication_media"]

### Paradigm — the scripts the text thinks with (+ its stance toward each)

| paradigm | stance | salience |  | relation | evidence |
|---|---|---|---|---|---|
| eschatological-vindication of the righteous sufferer | endorsed | 0.95 |  | self | 'Jesus who was crucified' (the shameful verdict of the powers) set against 'he has been raised, as he said' (God's counter-verdict); the empty tomb as the resolution of the passion; the guards — agents of the executing authority — reduced to 'like dead men' while the executed one is vindicated |
| angelic-messenger commissioning (mal'ak announcement) | endorsed | 0.9 |  | reinforces | the angel's fixed sequence — reassurance ('Do not be afraid'), disclosure ('he has been raised'), ostension ('Come, see the place'), sending ('go quickly and tell'), and a message to relay verbatim ('This is my message for you'); women cast as commissioned heralds who then 'ran to tell' |
| theophany / Sinai-style divine descent | endorsed | 0.85 |  | reinforces | 'a great earthquake,' 'an angel of the Lord, descending from heaven,' 'his appearance was like lightning and his clothing white as snow,' the paralyzing fear of the bystanders, the opening command 'Do not be afraid' — the standard grammar of biblical theophany (Exod 19, Dan 10, Ezek 1) |
| prophecy-fulfillment / word-and-event | endorsed | 0.75 |  | reinforces | 'he has been raised, AS HE SAID'; 'he is going ahead of you to Galilee; there you will see him' — the event is legible because it matches a prior word (both Jesus' own predictions and, in Matthew's frame, scriptural pattern) |
| empty-tomb / missing-body recognition scene | invoked | 0.7 |  | reinforces | seekers arrive at a burial site, the stone is displaced, an interpreter is present, the seekers are invited to inspect the vacated place ('Come, see the place where he lay'); the absence is read AS presence-elsewhere ('he is going ahead of you to Galilee') |
| honor-shame reversal | endorsed | 0.7 |  | reinforces | the crucified one (maximally shamed by Rome) is publicly honored by heaven's own herald; the imperial guards (bearers of coercive honor) are shamed into corpse-likeness; women (low-status witnesses in that world) are elevated as first commissioned proclaimers |
| resurrection of the righteous (Danielic / martyrological) | endorsed | 0.65 |  | reinforces | 'he has been raised from the dead' read against the 2nd-Temple expectation (Dan 12:2; 2 Macc 7) that God vindicates the faithful martyr by bodily raising — here compressed onto a single figure ahead of the general resurrection |
| holy-war / divine-warrior reversal | endorsed | 0.6 |  | reinforces | earthquake as YHWH's battle-sign, the armed Roman guards struck down and 'became like dead men' without a blow — the classic script in which God's appearing routs the hostile watchers (cf. Exod 14, Josh 10, 2 Kgs 19) |
| Sabbath-and-first-day / new-creation dawn | invoked | 0.55 |  | reinforces | 'After the Sabbath, as the first day of the week was dawning' — deliberate temporal marking that positions the event on the eighth day / re-creation morning, activating the Genesis-week script |
| pilgrimage / visitation to the honored dead | subverted | 0.4 |  | subverts | the women 'went to see the tomb' — the expected script is mourning-visitation to a grave, but the script is broken open: the tomb is not the locus, the dead is not there, and the visit converts into commissioning |

### Frame — the 8-axis morphospace coordinate

| axis | value | rank | conf | evidence |
|---|---|---|---|---|
| epistemic-warrant | revelation | 1 | 0.92 | 'an angel of the Lord, descending from heaven' announces 'he has been raised' — the claim is grounded in angelic disclosure |
| epistemic-warrant | testimony | 2 | 0.85 | 'go quickly and tell his disciples' + 'ran to tell his disciples' — knowledge propagates by eyewitness report |
| evaluative-stance | reverent | 1 | 0.95 | 'fear and great joy'; guards 'became like dead men'; luminous imagery ('like lightning', 'white as snow') — awe-saturated register |
| ground-world-relation | manifestation | 1 | 0.85 | the ultimate irrupts into the world — angel descends, stone rolled back, empty tomb 'manifested' to the women as sign |
| hermeneutic-posture | literal | 1 | 0.8 | narrated as event-report: dawn, earthquake, stone, empty place — presented as what happened, not as allegory |
| hermeneutic-posture | reparative-integrative | 2 | 0.6 | 'he has been raised, AS HE SAID' — the event is read as fulfilling and integrating Jesus' prior word |
| inferential-operation | causal-explanation | 1 | 0.65 | 'suddenly there was a great earthquake, FOR an angel of the Lord... came and rolled back the stone' — event explained by agent-cause |
| ontological-commitment | transcendent-personal | 1 | 0.9 | 'an angel of the Lord, descending from heaven' — a personal transcendent order breaks in with earthquake, lightning-appearance |
| ontological-commitment | personal-agentive | 2 | 0.8 | named agents (Mary Magdalene, the other Mary, the angel, Jesus) act intentionally; 'he is going ahead of you to Galilee' |
| telos | salvation | 1 | 0.85 | 'he has been raised' — resurrection as the decisive saving event the passage is oriented to proclaim |
| telos | communion | 2 | 0.7 | 'he is going ahead of you to Galilee; there you will see him' — telos includes reunion/seeing-again with the risen one |

### Coded moves — each with the context it picked up

**M1** — At first light after the sabbath, the two women named Mary travel to the burial site with the intent of viewing it
  · agent: Mary Magdalene and the other Mary · operation: go · substrate: the tomb · outcome: arrival at the tomb (viewing-purpose) · narrator: the evangelist, anonymous third-person, authority = received passion-tradition

**M2** — A large seismic disturbance abruptly happens
  · agent: not-stated · operation: occur · substrate: not-stated · outcome: a great earthquake · narrator: the evangelist, anonymous third-person
  · **gaps:** *cause* — The earthquake simply occurs; whether it is produced by the angel's descent or by the resurrection itself — or is a cosmic marker independent of either — is not stated. (residual); *temporal-sequence* — The earthquake is narrated first in the sequence, but whether the resurrection precedes it, coincides with it, or follows the angel's arrival is not fixed. (residual)

**M3** — A messenger of the Lord travels down out of the sky and arrives at the scene
  · agent: an angel of the Lord · operation: descend-and-come · substrate: heaven (origin) → the tomb (destination) · outcome: angelic presence at the tomb · narrator: the evangelist, anonymous third-person

**M4** — The messenger removes the sealing stone from its position
  · agent: the angel · operation: roll-back · substrate: the stone · outcome: the stone displaced; the tomb opened · narrator: the evangelist, anonymous third-person
  · **gaps:** *purpose* — The stone is rolled away, but whether this action serves to release the risen Jesus from the tomb or to open the tomb so the women can verify its vacancy is not stated. (residual)

**M5** — The messenger takes up a seated position on top of the moved stone
  · agent: the angel · operation: sit · substrate: the stone (now as platform) · outcome: the angel enthroned upon the displaced seal · narrator: the evangelist, anonymous third-person

**M6** — The visible aspect of the messenger resembles lightning
  · agent: not-stated · operation: resemble (visual) · substrate: the angel's appearance · outcome: appearance likened to lightning · narrator: the evangelist, anonymous third-person, using a stock apocalyptic simile

**M7** — The garments of the messenger are of snow-white color
  · agent: not-stated · operation: be-colored (white) · substrate: the angel's clothing · outcome: whiteness likened to snow · narrator: the evangelist, anonymous third-person

**M8** — The guards tremble under the effect of terror at the messenger
  · agent: the guards · operation: tremble · substrate: the guards themselves (as fear-bearer) · outcome: trembling · narrator: the evangelist, anonymous third-person

**M9** — The guards enter a state resembling the dead
  · agent: the guards · operation: become-like-dead · substrate: the guards themselves · outcome: death-like immobility · narrator: the evangelist, anonymous third-person
  · **gaps:** *outcome* — The guards are last described as death-like and immobile; when they recover, what they do next, and whether they speak to anyone within the scene is entirely absent. (residual)

**M10** — The messenger addresses speech to the women
  · agent: the angel · operation: say · substrate: the compound message that follows (to the women as addressees) · outcome: the message uttered to the women · narrator: the evangelist, anonymous third-person, framing the angel's speech
  · **gaps:** *addressee-exclusion* — The guards are present throughout and witness the same theophanic events as the women, yet they receive no angelic word whatsoever. (barred)
  · **edges:** M10 —CONTAINS→ M11; M10 —CONTAINS→ M12; M10 —CONTAINS→ M15; M10 —CONTAINS→ M16; M10 —CONTAINS→ M17; M10 —CONTAINS→ M18; M10 —CONTAINS→ M19; M10 —CONTAINS→ M21; M10 —CONTAINS→ M22; M10 —CONTAINS→ M26

**M11** — The women are directed to stop being afraid
  · agent: the women (as directed addressees) · operation: not-fear (directive) · substrate: fear · outcome: cessation of fear (as commanded) · narrator: the angel, as the internal speaker within M10's report
  · **edges:** ["M10"] —CONTAINS→ M11

**M12** — The messenger declares that he has knowledge of the women's purpose
  · agent: the angel ('I') · operation: know · substrate: the fact that the women are seeking Jesus · outcome: propositional knowledge asserted · narrator: the angel, within M10
  · **edges:** M12 —REPORTS→ M13; ["M10"] —CONTAINS→ M12

**M13** — The women are engaged in seeking Jesus
  · agent: the women ('you') · operation: seek · substrate: Jesus · outcome: the seeking, ongoing · narrator: the angel, within M10 — reporting the women's action back to them
  · **edges:** M13 —CONTAINS→ M14; ["M12"] —REPORTS→ M13

**M14** — Jesus is identified by the fact that he underwent crucifixion
  · agent: not-stated · operation: crucify · substrate: Jesus · outcome: having-been-crucified (as identifying mark) · narrator: the angel, within M10
  · **edges:** ["M13"] —CONTAINS→ M14

**M15** — The messenger declares Jesus to be absent from this place
  · agent: not-stated · operation: be-absent (negated presence) · substrate: Jesus at the tomb · outcome: negation: Jesus is not here · narrator: the angel, within M10
  · **edges:** ["M10"] —CONTAINS→ M15

**M16** — Jesus has been brought up from death by an unnamed agent
  · agent: not-stated · operation: raise · substrate: Jesus ('he') · outcome: raised-status (completed) · narrator: the angel, within M10; authority-source = the prior word of Jesus (grounded by M17)
  · **gaps:** *witness* — No party occupies a witnessing position at the moment the rising itself occurs; the text arrives at the empty tomb and the angel's report without anyone having seen the event it exists to proclaim. (barred); *agent* — The raising is stated in a passive construction; who performs it is not named. (residual)
  · **edges:** ["M10"] —CONTAINS→ M16

**M17** — Jesus previously stated this outcome, and the messenger cites that prior word as ground
  · agent: Jesus ('he') · operation: say (prior) · substrate: the raising-content later borne out · outcome: prior speech-act by Jesus, now cited · narrator: the angel, within M10, citing Jesus
  · **gaps:** *content* — Jesus' prior speech is cited as the epistemic anchor for the angel's entire claim, but its actual wording is not reproduced; the reader must retrieve it from elsewhere in the gospel. (residual)
  · **edges:** ["M10"] —CONTAINS→ M17

**M18** — The women are directed to approach
  · agent: the women (as directed addressees) · operation: come (directive) · substrate: the place of Jesus' laying (implicit destination) · outcome: approach as commanded · narrator: the angel, within M10
  · **edges:** ["M10"] —CONTAINS→ M18

**M19** — The women are directed to look at the specific spot of the laying
  · agent: the women · operation: see (directive) · substrate: the place where Jesus lay · outcome: perception as commanded (verification) · narrator: the angel, within M10
  · **edges:** M19 —CONTAINS→ M20; ["M10"] —CONTAINS→ M19

**M20** — Jesus previously occupied this specific spot in a lying position
  · agent: Jesus ('he') · operation: lie (posture) · substrate: the place inside the tomb · outcome: past position of the body at this spot · narrator: the angel, within M10
  · **edges:** ["M19"] —CONTAINS→ M20

**M21** — The women are directed to depart without delay
  · agent: the women · operation: go (directive, urgent) · substrate: not-stated (departure-path) · outcome: quick departure as commanded · narrator: the angel, within M10
  · **edges:** ["M10"] —CONTAINS→ M21

**M22** — The women are directed to convey a message to Jesus' disciples
  · agent: the women · operation: tell (directive-reporting) · substrate: the message (compound, embedded) · outcome: message conveyed to the disciples (as commanded) · narrator: the angel, within M10
  · **gaps:** *warrant-for-messenger-selection* — The women are chosen as bearers of the resurrection testimony to the disciples; why they rather than the guards who also witnessed the theophany is not supplied. (residual)
  · **edges:** M22 —CONTAINS→ M23; M22 —CONTAINS→ M24; M22 —CONTAINS→ M25; ["M10"] —CONTAINS→ M22

**M23** — Jesus has been brought up from among the dead by an unnamed agent
  · agent: not-stated · operation: raise (from the dead) · substrate: Jesus · outcome: raised-from-the-dead status · narrator: the angel (as message-author), to be re-narrated by the women
  · **edges:** ["M22"] —CONTAINS→ M23

**M24** — Jesus is now moving in advance of the women toward the region of Galilee
  · agent: Jesus · operation: go-ahead (precede) · substrate: Galilee (destination), the women (those preceded) · outcome: Jesus preceding them toward Galilee · narrator: the angel (as message-author), to be re-narrated by the women
  · **gaps:** *present-location* — The angel promises a future appearance in Galilee, but where the risen Jesus is located at the moment of this scene is nowhere stated. (residual)
  · **edges:** ["M22"] —CONTAINS→ M24

**M25** — The women will visually encounter Jesus in that region
  · agent: the women ('you') · operation: see (future) · substrate: Jesus, in Galilee · outcome: future perception of Jesus · narrator: the angel (as message-author), to be re-narrated by the women
  · **edges:** ["M22"] —CONTAINS→ M25

**M26** — The messenger closes by attributing the preceding message to himself as his own
  · agent: the angel ('my') · operation: attribute (self-marking of message) · substrate: the entire message just given · outcome: the message marked as coming from this angelic authority · narrator: the angel, within M10
  · **edges:** ["M10"] —CONTAINS→ M26

**M27** — The women depart from the burial site without delay
  · agent: Mary Magdalene and the other Mary · operation: leave · substrate: the tomb · outcome: quick departure from the tomb · narrator: the evangelist, anonymous third-person

**M28** — The women are simultaneously in a state of terror and of great gladness
  · agent: the women · operation: have (compound affect) · substrate: fear and great joy (as the affective content they bear) · outcome: held in a doubled affective state · narrator: the evangelist, anonymous third-person
  · **gaps:** *interior* — The women are said to hold fear and great joy simultaneously, but what binds these contrary states — and which governs their action — is not stated. (residual)

**M29** — The women move at a run in order to convey the news to Jesus' disciples
  · agent: Mary Magdalene and the other Mary · operation: run (purpose-embedded) · substrate: not-stated (path toward the disciples) · outcome: hastened motion toward the disciples to deliver the message · narrator: the evangelist, anonymous third-person
