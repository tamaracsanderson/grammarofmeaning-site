# LUKE-24 — background sheet

> Full coded transcript for **LUKE-24** — read-only snapshot from the DB.

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
| LUKE-24 | 29 | 13 | 12 | 0 |


## LUKE-24

### Full text — Luke 24 (World English Bible, public domain)

**1** But on the first day of the week, at early dawn, they and some others came to the tomb, bringing the spices which they had prepared.
**2** They found the stone rolled away from the tomb.
**3** They entered in, and didn’t find the Lord Jesus’ body.
**4** While they were greatly perplexed about this, behold, two men stood by them in dazzling clothing.
**5** Becoming terrified, they bowed their faces down to the earth.
They said to them, “Why do you seek the living among the dead?
**6** He isn’t here, but is risen. Remember what he told you when he was still in Galilee,
**7** saying that the Son of Man must be delivered up into the hands of sinful men, and be crucified, and the third day rise again?”
**8** They remembered his words,
**9** returned from the tomb, and told all these things to the eleven, and to all the rest.
**10** Now they were Mary Magdalene, Joanna, and Mary the mother of James. The other women with them told these things to the apostles.
**11** These words seemed to them to be nonsense, and they didn’t believe them.
**12** But Peter got up and ran to the tomb. Stooping and looking in, he saw the strips of linen lying by themselves, and he departed to his home, wondering what had happened.
**13** Behold, two of them were going that very day to a village named Emmaus, which was sixty stadia from Jerusalem.
**14** They talked with each other about all of these things which had happened.
**15** While they talked and questioned together, Jesus himself came near, and went with them.
**16** But their eyes were kept from recognizing him.
**17** He said to them,
“What are you talking about as you walk, and are sad?”
**18** One of them, named Cleopas, answered him, “Are you the only stranger in Jerusalem who doesn’t know the things which have happened there in these days?”
**19** He said to them,
“What things?”
They said to him, “The things concerning Jesus, the Nazarene, who was a prophet mighty in deed and word before God and all the people;
**20** and how the chief priests and our rulers delivered him up to be condemned to death, and crucified him.
**21** But we were hoping that it was he who would redeem Israel. Yes, and besides all this, it is now the third day since these things happened.
**22** Also, certain women of our company amazed us, having arrived early at the tomb;
**23** and when they didn’t find his body, they came saying that they had also seen a vision of angels, who said that he was alive.
**24** Some of us went to the tomb, and found it just like the women had said, but they didn’t see him.”
**25** He said to them,
“Foolish men, and slow of heart to believe in all that the prophets have spoken!
**26** Didn’t the Christ have to suffer these things and to enter into his glory?”
**27** Beginning from Moses and from all the prophets, he explained to them in all the Scriptures the things concerning himself.
**28** They came near to the village, where they were going, and he acted like he would go further.
**29** They urged him, saying, “Stay with us, for it is almost evening, and the day is almost over.”
He went in to stay with them.
**30** When he had sat down at the table with them, he took the bread and gave thanks. Breaking it, he gave it to them.
**31** Their eyes were opened, and they recognized him, and he vanished out of their sight.
**32** They said to one another, “Weren’t our hearts burning within us, while he spoke to us along the way, and while he opened the Scriptures to us?”
**33** They rose up that very hour, returned to Jerusalem, and found the eleven gathered together, and those who were with them,
**34** saying, “The Lord is risen indeed, and has appeared to Simon!”
**35** They related the things that happened along the way, and how he was recognized by them in the breaking of the bread.
**36** As they said these things, Jesus himself stood among them, and said to them,
“Peace be to you.”
**37** But they were terrified and filled with fear, and supposed that they had seen a spirit.
**38** He said to them,
“Why are you troubled? Why do doubts arise in your hearts?
**39** See my hands and my feet, that it is truly me. Touch me and see, for a spirit doesn’t have flesh and bones, as you see that I have.”
**40** When he had said this, he showed them his hands and his feet.
**41** While they still didn’t believe for joy, and wondered, he said to them,
“Do you have anything here to eat?”
**42** They gave him a piece of a broiled fish and some honeycomb.
**43** He took them, and ate in front of them.
**44** He said to them,
“This is what I told you, while I was still with you, that all things which are written in the law of Moses, the prophets, and the psalms, concerning me must be fulfilled.”
**45** Then he opened their minds, that they might understand the Scriptures.
**46** He said to them,
“Thus it is written, and thus it was necessary for the Christ to suffer and to rise from the dead the third day,
**47** and that repentance and remission of sins should be preached in his name to all the nations, beginning at Jerusalem.
**48** You are witnesses of these things.
**49** Behold, I send out the promise of my Father on you. But wait in the city of Jerusalem until you are clothed with power from on high.”
**50** He led them out as far as Bethany, and he lifted up his hands, and blessed them.
**51** While he blessed them, he withdrew from them, and was carried up into heaven.
**52** They worshiped him, and returned to Jerusalem with great joy,
**53** and were continually in the temple, praising and blessing God. Amen.

### Sitz — situational conditions (source_grounding)

- **summary:** Luke 24's empty-tomb narrative is composed ~85 CE in the aftermath of [POL-FIRST-JEWISH-ROMAN-WAR] — the 70 CE destruction of the Second Temple has removed the sacrificial cult that anchored Jewish practice, and nascent Christian communities are reorganizing their identity around the risen Christ rather than Temple worship. The text presupposes the Galilean ministry of [FIG-JESUS-GALILEE-30] (explicitly named in v.6 'while he was still in Galilee') and the Pauline missionary expansion [FIG-PAUL-MEDITERRANEAN-50] that had by the 80s established Gentile-inclusive house-churches across the Mediterranean under [POL-PAX-ROMANA] conditions that enabled the text's circulation. MODEL-KNOWLEDGE: the post-70 Jewish-Christian separation (birkat ha-minim ~85-90 CE) and the emergence of Lukan two-volume historiographical form addressed to a Hellenistic patron (Theophilus) also condition this passage's apologetic framing of women-as-witnesses (v.11 'idle tale') within Greco-Roman evidentiary conventions.
- **categories:** ["political_institutional", "demographic_social", "migration_diaspora", "communication_media", "interreligious_contact"]

### Paradigm — the scripts the text thinks with (+ its stance toward each)

| paradigm | stance | salience |  | relation | evidence |
|---|---|---|---|---|---|
| prophetic vindication of the righteous sufferer | endorsed | 0.95 | DOMINANT | self | 'the Son of Man must be handed over to the hands of sinners and be crucified and on the third day rise again' (v.7) — the divine-necessity ('must') pattern in which the righteous one is delivered up, killed, and vindicated by God on the third day; the empty tomb is legible as vindication, not disappearance |
| prophecy-fulfillment (predictive word → event → remembering) | endorsed | 0.9 |  | reinforces | 'Remember how he told you, while he was still in Galilee…' → 'Then they remembered his words' (v.6–8) — the empty tomb is not self-interpreting; it becomes resurrection only when routed back through Jesus's earlier prediction, which the angels enforce as the correct interpretive frame |
| prophecy-fulfillment (divine dei / Son-of-Man must-pattern) | endorsed | 0.9 |  | self | The angelic speech is structured entirely as retrospective fulfillment: 'Remember how he told you, while he was still in Galilee, that the Son of Man MUST be handed over... and on the third day rise again' (vv.6-7); the disciples' pivot is 'Then they remembered his words' (v.8). The empty tomb is not interpreted as itself — it is interpreted as the predicted third-day rising. |
| angelophany / divine announcement at a threshold | invoked | 0.85 |  | reinforces | 'Two men in dazzling clothes stood beside them' (v.4); the women are 'terrified and bowed their faces to the ground' (v.5); the messengers deliver an oracle that reframes the scene. The full Daniel/Tobit/transfiguration pattern — sudden appearance, dazzling garments, human terror, prostration, message — is present. |
| angelophany / Second Temple messenger-vision | invoked | 0.8 |  | reinforces | 'suddenly two men in dazzling clothes stood beside them. The women were terrified and bowed their faces to the ground' (v.4–5) — canonical roles+sequence of a Danielic/apocalyptic revelation scene: dazzling figures, terror, prostration, authoritative reproach-and-message ('Why do you look for the living among the dead?') |
| burial / anointing ritual | subverted | 0.75 |  | subverts | Women come 'at early dawn... taking the spices that they had prepared' (v.1) — the full script of post-mortem anointing is set up. It is then explicitly cancelled: 'they did not find the body' (v.3), and the angels rebuke the script itself — 'Why do you look for the living among the dead?' (v.5). The rite has no object. |
| vindication of the righteous sufferer (Wis 2-5 / Dan 12 / 2 Macc 7 apocalyptic script) | endorsed | 0.75 |  | reinforces | 'Handed over to the hands of sinners and be crucified' (v.7) frames Jesus in the unjustly-killed-righteous slot; resurrection functions as God's reversal of that verdict. Son-of-Man language ties the vindication to the Daniel 7 apocalyptic register. |
| legal witness-report | subverted | 0.7 |  | reinforces | the women give a formal deposition — named individually (Mary Magdalene, Joanna, Mary the mother of James, 'and the other women with them') — 'they told all this to the eleven and to all the rest' (v.9–10); the eleven's response invokes the culturally standard dismissal of women's testimony — 'these words seemed to them an idle tale, and they did not believe them' (v.11) — but the narrator overturns that verdict: he names the witnesses, and Peter's independent verification (v.12) implicitly ratifies them |
| mourning-visit / corpse-tending | subverted | 0.65 |  | subverts | 'on the first day of the week, at early dawn, they went to the tomb, taking the spices that they had prepared' (v.1) — the standard female-mourner script (dawn, tomb, aromatics, body-care) is set up in full and then structurally broken: the stone is rolled, 'they did not find the body' (v.3); the script is invoked precisely so it can fail |
| legal witness / testimony credibility (gendered) | subverted | 0.65 |  | competes | The women are named as a formal witness list (v.10: Mary Magdalene, Joanna, Mary of James, the others), then their report is dismissed as 'an idle tale' (leros, v.11) — the technical register for unreliable testimony. Peter's confirming run (v.12) tacitly vindicates them, inverting the ambient honor-shame default that discounts female witness. |
| anagnorisis / delayed recognition | invoked | 0.55 |  | reinforces | 'Then they remembered his words' (v.8) and Peter 'amazed at what had happened' (v.12) — the recognition beat: prior knowledge or evidence is suddenly re-cognized under a new key; the paradigm carries the reader from puzzle ('perplexed', v.4) to disclosure |
| anamnesis / covenant remembrance | endorsed | 0.5 |  | reinforces | The interpretive turn of the passage is not sight but recall: 'Then they remembered his words' (v.8). The women's status shifts from perplexed mourners to authorized proclaimers via an act of remembering — a script drawn from covenant / Passover anamnesis where remembering is itself a mode of participation. |
| empty-tomb-as-translation/assumption (Elijah, Enoch, Moses-legends) | denied | 0.35 |  | incompatible | The bare datum — missing body, no corpse to anoint — would naturally invoke the assumption/rapture script available in the Second Temple repertoire. The angels pre-empt this reading: not 'he has been taken' but 'he is not here, but has risen' (v.5). The text refuses the translation frame in favor of resurrection. |

### Frame — the 8-axis morphospace coordinate

| axis | value | rank | conf | evidence |
|---|---|---|---|---|
| epistemic-warrant | testimony | 1 | 0.92 | the women 'told all this to the eleven and to all the rest' — the text's mode of knowing is eyewitness report passed on |
| epistemic-warrant | revelation | 2 | 0.78 | 'two men in dazzling clothes' announce 'He is not here but has risen' — angelic disclosure grounds the claim |
| evaluative-stance | reverent | 1 | 0.9 | 'terrified and bowed their faces to the ground'; Peter 'amazed at what had happened' — the narrator holds the object in awe |
| ground-world-relation | manifestation | 1 | 0.75 | the resurrected one and the dazzling messengers appear within the world (tomb, dawn, spices) — the transcendent shows itself in ordinary space |
| ground-world-relation | creation | 2 | 0.5 | the ambient Lukan cosmology assumes a creator God whose promise is being kept, though not stated in this pericope |
| hermeneutic-posture | reparative-integrative | 1 | 0.82 | the empty tomb + remembered prophecy + angelic word are woven into a single coherent vindication narrative that repairs the scandal of the cross |
| hermeneutic-posture | literal | 2 | 0.6 | the report is offered as factual account (stone rolled away, linen cloths, named women) — not allegorized |
| inferential-operation | exegesis | 1 | 0.85 | 'Remember how he told you, while he was still in Galilee...' 'Then they remembered his words' — the empty tomb is read by recalling and interpreting prior prophecy |
| inferential-operation | abduction | 2 | 0.6 | Peter sees 'the linen cloths by themselves' and goes home 'amazed' — inference to a best explanation from physical trace |
| ontological-commitment | personal-agentive | 1 | 0.9 | 'the Son of Man must be handed over... and on the third day rise again' — reality is populated by named agents (Jesus, the Son of Man, the messengers) who act |
| telos | salvation | 1 | 0.88 | 'Why do you look for the living among the dead? He is not here but has risen' — the orienting end is God's vindicating deliverance from death |
| telos | fidelity-service | 2 | 0.55 | the women 'returning from the tomb they told all this to the eleven' — remembering and reporting as faithful discipleship |

### Coded moves — each with the context it picked up

**M1** — At daybreak on the week's first day the women set out for the tomb, carrying the burial-spices they had already readied.
  · agent: they (the women who had followed from Galilee) · operation: go-to (with accompanying carry) · substrate: the tomb (as destination); the prepared spices (as what is carried) · outcome: arrival at the tomb, spices in hand · narrator: third-person Lukan narrator, community/eyewitness-tradition authority

**M2a** — The stone at the tomb-mouth had already been moved aside — by no named doer.
  · agent: not-stated · operation: roll-away (of the stone) · substrate: the stone (of the tomb-entrance) · outcome: stone displaced from the tomb-mouth; tomb standing open · narrator: third-person Lukan narrator, reporting the prior state the women encounter
  · **edges:** ["M2"] —REPORTS→ M2a

**M2** — They discovered that state of the stone.
  · agent: they (the women) · operation: find (as discover) · substrate: the state of the stone having been rolled away · outcome: the women register that the tomb has been opened · narrator: third-person Lukan narrator
  · **edges:** M2 —REPORTS→ M2a

**M3** — They went inside the tomb.
  · agent: they (the women) · operation: enter · substrate: the interior of the tomb · outcome: the women are inside the burial chamber · narrator: third-person Lukan narrator

**M4** — Inside, they failed to find the body.
  · agent: they (the women) · operation: find-not (negated discovery) · substrate: the body (the object expected to be there) · outcome: the women register the body's absence · narrator: third-person Lukan narrator

**M5** — The absence left them at a loss.
  · agent: they (the women, as experiencer — no doer) · operation: be-perplexed · substrate: the discovered absence (the event of M4) · outcome: a state of bewilderment · narrator: third-person Lukan narrator, reporting inner state

**M6** — All at once, two figures in gleaming garments were suddenly there beside them.
  · agent: two men (in dazzling clothes) · operation: appear/stand-beside · substrate: the space beside the women (as location) · outcome: the two figures are present alongside the women · narrator: third-person Lukan narrator; the 'dazzling clothes' detail signals angelophany without labelling it

**M7** — The women were struck with terror.
  · agent: the women (as experiencer — no doer) · operation: be-terrified · substrate: the appearance of the two figures (M6) · outcome: a state of terror · narrator: third-person Lukan narrator, reporting inner state

**M8** — They lowered their faces toward the ground.
  · agent: the women · operation: bow (faces to the ground) · substrate: their own faces · outcome: faces lowered to the earth (posture of reverence/dread) · narrator: third-person Lukan narrator

**M9** — The two figures spoke to the women, delivering the following as a single utterance.
  · agent: the two men (in dazzling clothes) · operation: say-to (reporting-speech) · substrate: the composite utterance carrying moves M10–M13 · outcome: the utterance is delivered to the women · narrator: third-person Lukan narrator, quoting the speech
  · **edges:** M9 —CONTAINS→ M10; M9 —CONTAINS→ M11; M9 —CONTAINS→ M12; M9 —CONTAINS→ M13

**M10** — As a rebuke-shaped question, they challenge the women's category-choice: seeking one who lives in the place of the dead.
  · agent: the two men · operation: challenge-by-question (rhetorical) · substrate: the women's act of seeking a living one in a location of the dead · outcome: the women's search is reframed as category-mistaken · narrator: as M9 (quoted within the narrator's report)
  · **edges:** ["M9"] —CONTAINS→ M10

**M11** — They assert his absence from this place.
  · agent: he (as subject of a state; no doer) · operation: assert-absence (state-declaration) · substrate: this place (the tomb) · outcome: the state 'not here' is declared of him · narrator: as M9
  · **edges:** ["M9"] —CONTAINS→ M11

**M12** — They declare that he has been raised (or has arisen).
  · agent: not-stated (English 'has risen' is intransitive; the underlying passive leaves the raiser unnamed) · operation: raise/rise (event of resurrection) · substrate: he (his prior dead body/person) · outcome: he is alive again · narrator: as M9 (the narrator does not warrant this directly here; the two figures do)
  · **edges:** ["M9"] —CONTAINS→ M12

**M13** — They direct the women to bring to mind his earlier teaching, referenced as follows.
  · agent: the two men · operation: command-to-remember (directive) · substrate: the women's memory of his earlier speech (M14) · outcome: the women are enjoined to recall · narrator: as M9
  · **edges:** M13 —REPORTS→ M14; ["M9"] —CONTAINS→ M13

**M14** — The referenced earlier event: while still in Galilee, he had told the women the following.
  · agent: he · operation: tell (reporting-speech, past) · substrate: the content that follows (M15–M17) · outcome: the passion-and-resurrection prediction was delivered to the women · narrator: as M9 (quoted within the two figures' speech, itself within the Lukan narrator's report)
  · **edges:** M14 —CONTAINS→ M15; M14 —CONTAINS→ M16; M14 —CONTAINS→ M17; ["M13"] —REPORTS→ M14

**M15** — The Son of Man is fated to be delivered into sinful human hands.
  · agent: not-stated (the 'must' signals divine passive; no doer named) · operation: hand-over (with divine necessity) · substrate: the Son of Man · outcome: he is in the power of sinners · narrator: as M14 (quoted within the two figures' speech, within the Lukan report)
  · **edges:** ["M14"] —CONTAINS→ M15

**M16** — He is fated to be executed by crucifixion.
  · agent: not-stated (the 'must' preserves the divine-passive; the executioners are unnamed here) · operation: crucify · substrate: the Son of Man · outcome: he is dead by crucifixion · narrator: as M14
  · **edges:** ["M14"] —CONTAINS→ M16

**M17** — On the third day he is fated to rise again.
  · agent: not-stated (grammatical subject 'Son of Man', but the 'must' again marks divine necessity; the raiser is unnamed) · operation: rise-again (on the third day) · substrate: the Son of Man (in his post-crucifixion dead state) · outcome: he is alive again on the third day · narrator: as M14
  · **edges:** ["M14"] —CONTAINS→ M17

**M18** — The women then brought his earlier words back to mind.
  · agent: they (the women) · operation: remember (cognition) · substrate: his earlier words (M14 as recovered content) · outcome: the passion-prediction is now present to them as remembered · narrator: third-person Lukan narrator, reporting inner cognition

**M19** — They came back away from the tomb.
  · agent: they (the women) · operation: return (motion) · substrate: the tomb (as departure-point) · outcome: the women are moving back toward where the disciples are · narrator: third-person Lukan narrator

**M20** — They reported the whole tomb-experience to the eleven and to everyone else with them.
  · agent: they (the women) · operation: tell (reporting-speech) · substrate: the entire prior sequence at the tomb (references M1–M17 as recovered content) · outcome: the eleven and the rest have received the testimony · narrator: third-person Lukan narrator

**M21** — The narrator names the tellers: Mary Magdalene, Joanna, Mary the mother of James, and the other women with them.
  · agent: the Lukan narrator (naming, not acting inside the story) · operation: identify/attribute (narrator-level naming) · substrate: the collective 'they' who performed M20 · outcome: the tellers of M20 are given proper names in the record · narrator: third-person Lukan narrator, community/tradition authority; here surfacing to name

**M22** — To the apostles, the women's report registered as a piece of nonsense.
  · agent: the apostles (as experiencer of the seeming; no doer) · operation: seem-as / deem-as (evaluative-perception) · substrate: the women's words (M20 as testimony-content) · outcome: the testimony is classed as an idle tale · narrator: third-person Lukan narrator, reporting apostolic reception

**M23** — The apostles withheld belief from the women.
  · agent: the apostles (they) · operation: believe-not (negated credence) · substrate: the women / their words · outcome: credence is refused · narrator: third-person Lukan narrator

**M24** — Peter, however, rose to his feet.
  · agent: Peter · operation: get-up (rise from seat/rest) · substrate: himself (his own body/posture) · outcome: Peter is on his feet · narrator: third-person Lukan narrator

**M25** — He ran to the tomb.
  · agent: Peter · operation: run-to (motion) · substrate: the tomb (destination) · outcome: Peter arrives at the tomb · narrator: third-person Lukan narrator

**M26** — Bending down to look inside, he saw the burial-linens lying by themselves.
  · agent: Peter · operation: see (perception, with stoop-and-look-in as manner) · substrate: the linen cloths (lying by themselves inside the tomb) · outcome: Peter registers the linens' presence and the body's absence around them · narrator: third-person Lukan narrator

**M27** — He went back to his own place.
  · agent: Peter · operation: go-home (motion) · substrate: his home (destination) · outcome: Peter departs from the tomb toward home · narrator: third-person Lukan narrator

**M28** — He was left in a state of astonishment at what had taken place.
  · agent: Peter (as experiencer — no doer) · operation: be-amazed · substrate: what had happened (the whole tomb-scene as an event-complex) · outcome: a state of amazement, unresolved into belief or disbelief here · narrator: third-person Lukan narrator, reporting inner state; the closing note is deliberately open (neither confirming nor denying credence)
