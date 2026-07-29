# MARK-16 — background sheet

> Full coded transcript for **MARK-16** — read-only snapshot from the DB.

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
| MARK-16 | 36 | 9 | 12 | 0 |


## MARK-16

### Full text — Mark 16 (World English Bible, public domain)

**1** When the Sabbath was past, Mary Magdalene, and Mary the mother of James, and Salome, bought spices, that they might come and anoint him.
**2** Very early on the first day of the week, they came to the tomb when the sun had risen.
**3** They were saying among themselves, “Who will roll away the stone from the door of the tomb for us?”
**4** for it was very big. Looking up, they saw that the stone was rolled back.
**5** Entering into the tomb, they saw a young man sitting on the right side, dressed in a white robe, and they were amazed.
**6** He said to them, “Don’t be amazed. You seek Jesus, the Nazarene, who has been crucified. He has risen. He is not here. Behold, the place where they laid him!
**7** But go, tell his disciples and Peter, ‘He goes before you into Galilee. There you will see him, as he said to you.’”
**8** They went out, and fled from the tomb, for trembling and astonishment had come on them. They said nothing to anyone; for they were afraid.
**9** Now when he had risen early on the first day of the week, he appeared first to Mary Magdalene, from whom he had cast out seven demons.
**10** She went and told those who had been with him, as they mourned and wept.
**11** When they heard that he was alive, and had been seen by her, they disbelieved.
**12** After these things he was revealed in another form to two of them, as they walked, on their way into the country.
**13** They went away and told it to the rest. They didn’t believe them, either.
**14** Afterward he was revealed to the eleven themselves as they sat at the table, and he rebuked them for their unbelief and hardness of heart, because they didn’t believe those who had seen him after he had risen.
**15** He said to them,
“Go into all the world, and preach the Good News to the whole creation.
**16** He who believes and is baptized will be saved; but he who disbelieves will be condemned.
**17** These signs will accompany those who believe: in my name they will cast out demons; they will speak with new languages;
**18** they will take up serpents; and if they drink any deadly thing, it will in no way hurt them; they will lay hands on the sick, and they will recover.”
**19** So then the Lord, after he had spoken to them, was received up into heaven, and sat down at the right hand of God.
**20** They went out, and preached everywhere, the Lord working with them, and confirming the word by the signs that followed. Amen.

### Sitz — situational conditions (source_grounding)

- **summary:** Mark 16 is composed in the immediate shadow of the First Jewish-Roman War and the 70 CE destruction of the Second Temple [POL-FIRST-JEWISH-ROMAN-WAR], which reframes the empty-tomb narrative for a community whose Jerusalem cultic center has just been annihilated — the angel's redirection 'he is going ahead of you to Galilee' pulls the risen Jesus AWAY from the destroyed Temple city and back to the Galilean periphery where the movement began [FIG-JESUS-GALILEE-30]. The text is written under Roman imperial administration [POL-PAX-ROMANA, POL-HERODIAN-CLIENT-RULE] — the crucifixion it presupposes is a Roman provincial execution — and circulates in the diaspora house-church network [DEM-JEWGENTILE-ROMAN-CHURCH-54, MIG-CLAUDIUS-EXPULSION-49] that Paul's mission had already seeded [FIG-PAUL-MEDITERRANEAN-50]. The abrupt original ending at v.8 ('they said nothing to anyone, for they were afraid') and the later 'Intermediate Ending' are themselves artifacts of a community in trauma-processing after 70 CE, with the intermediate ending's 'from east to west' language reflecting the already-Mediterranean-wide diaspora reach.
- **categories:** ["political_institutional", "migration_diaspora", "demographic_social", "communication_media"]

### Paradigm — the scripts the text thinks with (+ its stance toward each)

| paradigm | stance | salience |  | relation | evidence |
|---|---|---|---|---|---|
| vindication-of-the-righteous-sufferer | endorsed | 0.95 | DOMINANT | self | 'Jesus of Nazareth, who was crucified. He has been raised' — the announcement fuses the shameful execution and the divine reversal in a single breath, the classic Second-Temple pattern (cf. Wisdom 2–5, Daniel 12, the persecuted-then-exalted prophet) where God overturns the verdict of the powers on the innocent one. |
| empty-tomb / translation-of-the-hero | invoked | 0.85 |  | reinforces | The stone rolled away, the body absent, the interpreting angelic figure ('a young man ... in a white robe'), and the instruction to look at 'the place they laid him' — this is the Greco-Roman/Jewish translation-narrative template (Enoch, Elijah, Romulus, Heracles): a missing body plus a heavenly messenger read as apotheosis/removal, not corpse-theft. |
| angelophany / commissioning-of-the-messenger | invoked | 0.75 |  | reinforces | White-robed figure, the formula 'Do not be alarmed,' the disclosure, the imperative 'go, tell' with a specified addressee and destination — the standard biblical commissioning shape (Judges 6, Luke 1, Tobit) is fully present. |
| failed-disciple / hidden-witness (Markan messianic-secret shape) | invoked | 0.7 |  | ironizes | 'they went out and fled ... they said nothing to anyone, for they were afraid' — the paradoxical ending runs the recurrent Markan script in which the human witnesses to divine disclosure fail to speak, throwing the burden of proclamation onto the hearer. |
| burial-anointing / mourning rite | subverted | 0.7 |  | subverts | The women 'bought spices, so that they might go and anoint him' and worry 'Who will roll away the stone' — the script of proper female mourning-and-anointing is set up in full and then broken open: the corpse that would receive the rite is gone, so the rite cannot complete. |
| prophecy-fulfillment | endorsed | 0.6 |  | reinforces | 'he is going ahead of you to Galilee; there you will see him, just as he told you' — explicit callback to Jesus' own earlier word (Mark 14:28), asserting that the events are running on the prophet's script and thus authenticating him. |
| universal missionary proclamation (Intermediate Ending only) | endorsed | 0.5 |  | competes | 'Jesus himself sent out through them, from east to west, the sacred and imperishable proclamation of eternal salvation' — a fully-formed apostolic-mission-to-the-oikoumene script, with cosmic scope and imperishability language, that is absent from vv.1–8. |
| apocalyptic new-age inauguration | invoked | 0.45 |  | reinforces | 'very early on the first day of the week, when the sun had risen' — first-day/new-creation timing plus the intrusion of a heavenly figure and a world-reversing event fits the apocalyptic template of a new aeon breaking in. |
| shepherd-gathers-scattered-flock (Galilee return) | invoked | 0.4 |  | reinforces | 'going ahead of you to Galilee' echoes Mark 14:27–28's Zechariah citation about the struck shepherd and the scattered sheep; the promised regathering-in-Galilee runs on the pastoral-restoration template. |

### Frame — the 8-axis morphospace coordinate

| axis | value | rank | conf | evidence |
|---|---|---|---|---|
| epistemic-warrant | revelation | 1 | 0.85 | A 'young man dressed in a white robe' (angelophany) announces 'He has been raised' — the claim is grounded in supernatural disclosure, not observation. |
| epistemic-warrant | testimony | 2 | 0.75 | 'go, tell his disciples and Peter' — the truth is transmitted via commissioned witness; the Intermediate Ending frames it as a 'sacred and imperishable proclamation.' |
| evaluative-stance | reverent | 1 | 0.9 | 'terror and amazement had seized them, and they said nothing to anyone, for they were afraid' — awe/numinous dread frames the narration; 'sacred and imperishable proclamation.' |
| ground-world-relation | manifestation | 1 | 0.7 | The ultimate breaks into the world as event — angelic appearance, stone rolled away, promised christophany in Galilee ('there you will see him'). |
| hermeneutic-posture | reparative-integrative | 1 | 0.7 | The crucifixion (apparent defeat) is re-narrated as vindication ('who was crucified. He has been raised'), integrating scandal into a redemptive whole. |
| hermeneutic-posture | literal | 2 | 0.6 | The account is delivered as straightforward historical narrative — named women, spices, day, tomb, stone — asking to be read as what happened. |
| inferential-operation | abduction | 1 | 0.6 | Empty tomb + angelic interpretation → best-explanation inference to resurrection: 'you are looking for Jesus... He has been raised; he is not here. Look, there is the place they laid him.' |
| inferential-operation | exegesis | 2 | 0.55 | 'just as he told you' — the event is read as fulfillment of Jesus' prior word (cf. Mk 14:28), a scripturally/prophetically anchored reading. |
| ontological-commitment | transcendent-personal | 1 | 0.85 | The reality asserted is a personal agent (Jesus of Nazareth) raised by divine passive ('he has been raised'), presupposing a transcendent personal God who acts. |
| ontological-commitment | personal-agentive | 2 | 0.7 | The messenger, the risen Jesus 'going ahead of you to Galilee,' and the women as agents — the world is populated by intentional persons whose acts matter. |
| telos | salvation | 1 | 0.85 | Intermediate Ending: 'the sacred and imperishable proclamation of eternal salvation'; the resurrection secures deliverance from death. |
| telos | communion | 2 | 0.55 | 'he is going ahead of you to Galilee; there you will see him' — the promised end is renewed seeing/being-with the risen one. |

### Coded moves — each with the context it picked up

**M1** — The teller opens by noting that the weekly day of rest has run its course.
  · agent: not-stated · operation: come to an end · substrate: the Sabbath · outcome: the Sabbath is over (time now available for work) · narrator: Markan evangelist, as tradent of received witness

**M2** — Three named women, once trade is again permitted, purchase burial spices.
  · agent: Mary Magdalene, Mary the mother of James, and Salome · operation: buy (spices) · substrate: spices · outcome: spices in the women's possession · narrator: Markan evangelist

**M3** — The teller discloses the women's stated purpose in buying: they mean to go and perform the anointing themselves.
  · agent: the three women · operation: intend (to anoint) · substrate: him (Jesus's corpse) · outcome: an intended, not-yet-performed anointing · narrator: Markan evangelist

**M4** — Very early on the first day of the week, daylight has just come on.
  · agent: the sun · operation: rise (of the sun) · substrate: not-stated (the sky/horizon is implied but not named) · outcome: daylight has begun · narrator: Markan evangelist

**M5** — At that dawn hour the women travel to where the corpse was placed.
  · agent: the three women · operation: go (to the tomb) · substrate: themselves in motion · outcome: the women arrive at the tomb · narrator: Markan evangelist

**M6** — As they walked, the women had been exchanging with each other a worried question about how they would get in.
  · agent: the three women · operation: say (repeatedly, to one another) · substrate: an anxious question they keep voicing · outcome: a shared, verbalized worry · narrator: Markan evangelist
  · **edges:** M6 —REPORTS→ M7

**M7** — The question they keep voicing: who is going to shift the great blocking stone aside for them?
  · agent: not-stated (an as-yet-unknown 'who') · operation: roll away (interrogated, future) · substrate: the great stone at the tomb's entrance · outcome: hoped-for opened access to the tomb · narrator: Markan evangelist
  · **edges:** ["M6"] —REPORTS→ M7

**M8** — The women raise their eyes toward the tomb.
  · agent: the three women · operation: look up · substrate: their own gaze · outcome: their eyes are directed at the tomb · narrator: Markan evangelist

**M9** — They perceive that the stone is no longer where they feared it would be.
  · agent: the three women · operation: see (perceive) that · substrate: the state of the stone as-already-moved · outcome: the women apprehend the stone's altered state · narrator: Markan evangelist
  · **edges:** M9 —REPORTS→ M10

**M10** — The very large stone has, prior to their arrival, been shifted back from the entrance — with no mover named.
  · agent: not-stated (grammatical divine-passive; no mover disclosed) · operation: roll back · substrate: the great stone · outcome: the tomb entrance is unblocked · narrator: Markan evangelist
  · **edges:** ["M9"] —REPORTS→ M10

**M11** — The women step into the tomb chamber.
  · agent: the three women · operation: enter (the tomb) · substrate: themselves and the tomb interior · outcome: the women are inside the burial chamber · narrator: Markan evangelist

**M12** — Inside, the women perceive the presence of a youthful figure.
  · agent: the three women · operation: see (perceive) · substrate: the tableau of the young man · outcome: the women register the figure's presence · narrator: Markan evangelist
  · **edges:** M12 —REPORTS→ M13

**M13** — The figure is seated on the right side, wearing a white robe.
  · agent: the young man · operation: sit (robed in white) · substrate: his posture and attire (right side; white robe) · outcome: a visible, uncanny tableau · narrator: Markan evangelist
  · **edges:** ["M12"] —REPORTS→ M13

**M14** — The sight throws the women into a state of dread.
  · agent: not-stated (the cause of the alarm is left unspoken) · operation: become alarmed / be gripped by dread · substrate: the three women (as experiencers) · outcome: the women stand alarmed · narrator: Markan evangelist

**M15** — The figure addresses the women in speech.
  · agent: the young man in white · operation: say (to them) · substrate: his address (comprising a directive, an identification, an announcement, and a commission) · outcome: a speech is delivered to the women · narrator: Markan evangelist
  · **edges:** M15 —CONTAINS→ M17; M15 —CONTAINS→ M18; M15 —CONTAINS→ M19; M15 —CONTAINS→ M20; M15 —CONTAINS→ M21; M15 —CONTAINS→ M22; M15 —CONTAINS→ M24; M15 —CONTAINS→ M25; M15 —REPORTS→ M16

**M16** — First he instructs them to stop being terrified.
  · agent: the three women (addressees) · operation: cease being alarmed (prohibitive) · substrate: their own state of dread · outcome: the intended cessation of their alarm · narrator: Markan evangelist
  · **edges:** ["M15"] —REPORTS→ M16

**M17** — He then names what the women are doing there: searching for a specific person.
  · agent: the three women · operation: look for / seek · substrate: Jesus of Nazareth (as sought person) · outcome: their unfulfilled search is named for them · narrator: Markan evangelist
  · **edges:** ["M15"] —CONTAINS→ M17

**M18** — He specifies which Jesus by pointing back to his execution on the cross — with no executioner named.
  · agent: not-stated (executioners not named) · operation: crucify (perfect) · substrate: Jesus of Nazareth · outcome: his identification as the one who was killed on a cross · narrator: Markan evangelist
  · **edges:** ["M15"] —CONTAINS→ M18

**M19** — The figure delivers the central announcement: the sought one has been brought back from death, with the raiser unnamed.
  · agent: not-stated (divine-passive; the raiser is deliberately withheld) · operation: raise (from the dead, perfect) · substrate: Jesus (him) · outcome: he stands in the state of the raised · narrator: Markan evangelist
  · **edges:** ["M15"] —CONTAINS→ M19

**M20** — He states, negatively, that Jesus is not present in this place.
  · agent: not-stated · operation: be present (negated) · substrate: Jesus · outcome: his absence from the tomb is declared · narrator: Markan evangelist
  · **edges:** ["M15"] —CONTAINS→ M20

**M21** — He tells them to direct their attention to a specific spot.
  · agent: the three women (addressees) · operation: look (imperative) · substrate: the spot in the tomb · outcome: their intended attention on the burial spot · narrator: Markan evangelist
  · **edges:** ["M15"] —CONTAINS→ M21

**M22** — He identifies the spot as the one where the body had been placed.
  · agent: not-stated · operation: be (demonstrative locative) · substrate: the spot in the tomb · outcome: the spot is identified as the burial place · narrator: Markan evangelist
  · **edges:** M22 —CONTAINS→ M23; ["M15"] —CONTAINS→ M22

**M23** — That spot is the place where an earlier burial party had positioned the body.
  · agent: not-stated ('they' — the earlier burial party) · operation: lay (down) · substrate: him (the corpse of Jesus) · outcome: the body is left in place in the tomb · narrator: Markan evangelist
  · **edges:** ["M22"] —CONTAINS→ M23

**M24** — He then commissions the women to depart from the site.
  · agent: the three women (addressees) · operation: go (imperative) · substrate: themselves in movement · outcome: an intended departure from the tomb · narrator: Markan evangelist
  · **edges:** ["M15"] —CONTAINS→ M24

**M25** — He commissions them to deliver a specific message to the male followers and to Peter in particular.
  · agent: the three women (as commissioned messengers) · operation: tell (imperative) · substrate: an announcement to be delivered (see M26-M28) · outcome: the intended informing of the male disciples and Peter · narrator: Markan evangelist
  · **edges:** M25 —CONTAINS→ M27; M25 —CONTAINS→ M28; M25 —REPORTS→ M26; ["M15"] —CONTAINS→ M25

**M26** — The first piece of the message: Jesus is moving on ahead of them, heading north.
  · agent: Jesus (he) · operation: go ahead (of you, to Galilee) · substrate: himself in movement toward Galilee · outcome: his precedent arrival in Galilee before the disciples · narrator: Markan evangelist
  · **edges:** ["M25"] —REPORTS→ M26

**M27** — The second piece: the male followers will be granted sight of Jesus in that northern region.
  · agent: the male disciples (as addressees of the forwarded message) · operation: see (future) · substrate: him (Jesus) · outcome: a future seeing / reunion in Galilee · narrator: Markan evangelist
  · **edges:** ["M25"] —CONTAINS→ M27

**M28** — The third piece: this fulfils something Jesus himself had already told them earlier (content not spelled out here).
  · agent: Jesus (he) · operation: tell (prior) · substrate: the male disciples (you) — content of the prior telling not made recoverable here · outcome: authorization of the present message by an earlier one · narrator: Markan evangelist
  · **edges:** ["M25"] —CONTAINS→ M28

**M29** — The women bolt from the burial chamber and away from the site.
  · agent: the three women · operation: flee (from the tomb) · substrate: themselves in flight from the tomb · outcome: the women are outside and moving away in flight · narrator: Markan evangelist

**M30** — A wave of trembling and stunned amazement has taken hold of them.
  · agent: terror and amazement (personified affects) · operation: seize / grip · substrate: the three women · outcome: the women are held in the grip of dread-astonishment · narrator: Markan evangelist

**M31** — They speak the message to no one at all.
  · agent: the three women · operation: say (negated) · substrate: no addressee (null hearer) · outcome: the commission is not carried out · narrator: Markan evangelist

**M32** — The reason: they are held in fear (the object of the fear unspoken).
  · agent: not-stated (what they fear is not disclosed) · operation: be afraid · substrate: the three women (experiencers) · outcome: an ongoing state of fear that closes the account · narrator: Markan evangelist

**M33** — In the added coda, the women in fact deliver a brief report to Peter's circle.
  · agent: the three women (implied 'they') · operation: report / tell briefly · substrate: the content they had been commissioned to relay (nested at M34) · outcome: Peter's circle is informed · narrator: Intermediate-Ending scribe (early 2nd-c. addition to Mark)
  · **edges:** M33 —REPORTS→ M34

**M34** — The content they deliver is everything they had been ordered to convey — the ordering itself given passively, no orderer named.
  · agent: not-stated (grammatical passive; the ordering picks up the earlier young-man scene but is now generalized) · operation: command (perfect passive) · substrate: the three women (as those commanded) · outcome: a commission they now carry · narrator: Intermediate-Ending scribe
  · **edges:** ["M33"] —REPORTS→ M34

**M35** — Afterward, Jesus himself, working through the women, dispatches a universal, imperishable proclamation of unending salvation across the world.
  · agent: Jesus himself · operation: send out (a proclamation) · substrate: the sacred and imperishable proclamation of eternal salvation (through the women as instruments) · outcome: the proclamation goes out from east to west · narrator: Intermediate-Ending scribe

**M36** — The teller closes with a liturgical seal affirming what has just been proclaimed.
  · agent: the scribe (as liturgical voice, joined by the reader) · operation: affirm / seal (liturgical) · substrate: the foregoing proclamation · outcome: the proclamation is sealed with assent · narrator: Intermediate-Ending scribe
