# JOHN-20 — background sheet

> Full coded transcript for **JOHN-20** — read-only snapshot from the DB.

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
| JOHN-20 | 36 | 9 | 12 | 14 |


## JOHN-20

### Full text — John 20 (World English Bible, public domain)

**1** Now on the first day of the week, Mary Magdalene went early, while it was still dark, to the tomb, and saw the stone taken away from the tomb.
**2** Therefore she ran and came to Simon Peter, and to the other disciple whom Jesus loved, and said to them, “They have taken away the Lord out of the tomb, and we don’t know where they have laid him!”
**3** Therefore Peter and the other disciple went out, and they went toward the tomb.
**4** They both ran together. The other disciple outran Peter, and came to the tomb first.
**5** Stooping and looking in, he saw the linen cloths lying, yet he didn’t enter in.
**6** Then Simon Peter came, following him, and entered into the tomb. He saw the linen cloths lying,
**7** and the cloth that had been on his head, not lying with the linen cloths, but rolled up in a place by itself.
**8** So then the other disciple who came first to the tomb also entered in, and he saw and believed.
**9** For as yet they didn’t know the Scripture, that he must rise from the dead.
**10** So the disciples went away again to their own homes.
**11** But Mary was standing outside at the tomb weeping. So, as she wept, she stooped and looked into the tomb,
**12** and she saw two angels in white sitting, one at the head, and one at the feet, where the body of Jesus had lain.
**13** They told her, “Woman, why are you weeping?”
She said to them, “Because they have taken away my Lord, and I don’t know where they have laid him.”
**14** When she had said this, she turned around and saw Jesus standing, and didn’t know that it was Jesus.
**15** Jesus said to her,
“Woman, why are you weeping? Who are you looking for?”
She, supposing him to be the gardener, said to him, “Sir, if you have carried him away, tell me where you have laid him, and I will take him away.”
**16** Jesus said to her,
“Mary.”
She turned and said to him, “Rabboni!” which is to say, “Teacher!”
**17** Jesus said to her,
“Don’t hold me, for I haven’t yet ascended to my Father; but go to my brothers, and tell them, ‘I am ascending to my Father and your Father, to my God and your God.’”
**18** Mary Magdalene came and told the disciples that she had seen the Lord, and that he had said these things to her.
**19** When therefore it was evening, on that day, the first day of the week, and when the doors were locked where the disciples were assembled, for fear of the Jews, Jesus came and stood in the middle, and said to them,
“Peace be to you.”
**20** When he had said this, he showed them his hands and his side. The disciples therefore were glad when they saw the Lord.
**21** Jesus therefore said to them again,
“Peace be to you. As the Father has sent me, even so I send you.”
**22** When he had said this, he breathed on them, and said to them,
“Receive the Holy Spirit!
**23** If you forgive anyone’s sins, they have been forgiven them. If you retain anyone’s sins, they have been retained.”
**24** But Thomas, one of the twelve, called Didymus, wasn’t with them when Jesus came.
**25** The other disciples therefore said to him, “We have seen the Lord!”
But he said to them, “Unless I see in his hands the print of the nails, put my finger into the print of the nails, and put my hand into his side, I will not believe.”
**26** After eight days again his disciples were inside, and Thomas was with them. Jesus came, the doors being locked, and stood in the middle, and said,
“Peace be to you.”
**27** Then he said to Thomas,
“Reach here your finger, and see my hands. Reach here your hand, and put it into my side. Don’t be unbelieving, but believing.”
**28** Thomas answered him, “My Lord and my God!”
**29** Jesus said to him,
“Because you have seen me,
you have believed. Blessed are those who have not seen, and have believed.”
**30** Therefore Jesus did many other signs in the presence of his disciples, which are not written in this book;
**31** but these are written, that you may believe that Jesus is the Christ, the Son of God, and that believing you may have life in his name.

### Sitz — situational conditions (source_grounding)

- **summary:** John 20's empty-tomb narrative is composed ~95 CE in the aftermath of [POL-FIRST-JEWISH-ROMAN-WAR] (66-73 CE) and the destruction of the Second Temple, which had dislocated Jewish sacred geography and forced early Jesus-followers to relocate resurrection-hope onto a bodily absence (empty tomb) rather than a functioning cultic site. The text builds on the earlier Jesus-movement seeded by [FIG-JESUS-GALILEE-30] and the diaspora-network expansion of [FIG-PAUL-MEDITERRANEAN-50], while [DEM-JEWGENTILE-ROMAN-CHURCH-54] tensions have by now hardened into the Johannine community's sharper Jewish/Christian boundary-formation (the 'other disciple' vs. Peter subtly indexing intra-community authority). MODEL-KNOWLEDGE: the Johannine community's likely expulsion from synagogue contexts (birkat ha-minim / aposynagogos, ~85-95 CE) directly conditions the resurrection-witness polemic here.
- **categories:** ["political_institutional", "demographic_social", "migration_diaspora", "interreligious_contact", "communication_media"]

### Paradigm — the scripts the text thinks with (+ its stance toward each)

| paradigm | stance | salience |  | relation | evidence |
|---|---|---|---|---|---|
| resurrection-vindication of the righteous sufferer | endorsed | 0.95 | DOMINANT | self | 'the stone had been removed from the tomb'; empty tomb with grave-cloths left behind; 'he saw and believed'; narrator's gloss 'that he must rise from the dead' invoking scriptural necessity (δεῖ) — the telos is God's reversal of an unjust death, made legible by the tomb-vacancy topos of Second Temple vindication narratives |
| recognition-scene (anagnorisis) / discipleship-as-seeing-and-believing | endorsed | 0.85 |  | reinforces | the running-race to the tomb; the graded looking ('bent down to look... saw the linen wrappings'; 'went in... saw'; 'also went in, and he saw and believed'); the linen wrappings and separately-rolled head-cloth function as tokens of recognition; Mary's non-recognition ('they have taken away my Lord') sets up her later anagnorisis |
| scriptural fulfillment / prophetic necessity | endorsed | 0.7 |  | reinforces | 'for as yet they did not understand the scripture, that he must rise from the dead' — the narrator installs a template in which events are the enactment of a pre-written script (roles: prophesied-one, God-as-author, disciples-as-belated-readers; sequence: prediction → event → recognition; telos: the scripture is shown true) |
| lament / mourning-at-the-tomb | invoked | 0.65 |  | competes | 'Mary stood weeping outside the tomb. As she wept, she bent over...'; the angels' formulaic address 'Woman, why are you weeping?' — the female mourner keeping vigil at the grave is a recognizable Mediterranean ritual role, which the narrative sets up in order to redirect |
| angelophany / theophanic burial-chamber encounter | endorsed | 0.6 |  | reinforces | 'two angels in white sitting where the body of Jesus had been lying, one at the head and the other at the feet' — two-figure heavenly attendants flanking a sacred locus (echoing the cherubim over the ark / mercy seat), the white garb, and the formulaic question all mark a divine-messenger encounter |
| grave-robbery / missing-body inquest | subverted | 0.6 |  | subverts | Mary's twice-stated hypothesis 'they have taken the Lord out of the tomb, and we do not know where they have laid him' invokes a mundane crime-script (roles: thieves, victim's kin, missing corpse; sequence: discovery → report → search); the neatly folded head-cloth is the anti-clue that undoes the theft reading |
| beloved-disciple vs. Peter authority contest | endorsed | 0.55 |  | competes | 'the other disciple, the one whom Jesus loved' outruns Peter, arrives first, defers entry, then 'saw and believed' — a status-and-precedence script (roles: rival authoritative witnesses; sequence: race → yielding → belief) that ranks insight-through-love above institutional primacy |
| first-day-of-the-week / new-creation dawn | invoked | 0.45 |  | reinforces | 'Early on the first day of the week, while it was still dark' — the Genesis-1 cadence of darkness giving way on day one, staging the event as the inauguration of a new creational order rather than merely a private miracle |
| witness-testimony / legal deposition | invoked | 0.35 |  | reinforces | the careful sequencing of who saw what and in what order (Mary sees stone → reports; beloved disciple sees wrappings from outside; Peter enters and sees; beloved disciple enters, sees, believes) reads as a deposition establishing a chain of eyewitnesses — a forensic script the Fourth Gospel elsewhere thematizes as μαρτυρία |

### Frame — the 8-axis morphospace coordinate

| axis | value | rank | conf | evidence |
|---|---|---|---|---|
| epistemic-warrant | testimony | 1 | 0.92 | First-person eyewitness reports: Mary 'saw that the stone had been removed'; the beloved disciple 'saw and believed'; narrative of what witnesses observed at the tomb. |
| epistemic-warrant | revelation | 2 | 0.6 | 'as yet they did not understand the scripture, that he must rise from the dead' — knowledge is grounded in scripture that must be disclosed; two angels appear as heavenly messengers. |
| evaluative-stance | reverent | 1 | 0.9 | 'the Lord', 'the disciple whom Jesus loved', angelic figures in white, solemn narration of the resurrection — the object is treated as holy. |
| ground-world-relation | manifestation | 1 | 0.7 | The divine breaks into the world through the empty tomb, angelic appearance, and the risen Lord's presence — ultimate reality manifests within ordinary space (a garden tomb at dawn). |
| hermeneutic-posture | reparative-integrative | 1 | 0.75 | Narrative integrates confusion, grief, and scripture-not-yet-understood into a coherent redemptive event; loss ('they have taken away my Lord') is being repaired into recognition and belief. |
| hermeneutic-posture | literal | 2 | 0.6 | Concrete physical reportage — precise details of stone, linen wrappings, head-cloth's position, running-order of the disciples — presented as straightforward historical account. |
| inferential-operation | abduction | 1 | 0.75 | The beloved disciple 'saw and believed' — inference to the best explanation from the arrangement of grave-cloths (empty tomb + orderly wrappings → resurrection, not theft). |
| inferential-operation | exegesis | 2 | 0.65 | 'for as yet they did not understand the scripture, that he must rise from the dead' — event is read against and fulfills prior scriptural text. |
| ontological-commitment | transcendent-personal | 1 | 0.85 | 'the Lord'; angels in white; a personal risen Jesus who transcends death yet remains agentive; God as personal actor implied through resurrection. |
| ontological-commitment | material | 2 | 0.6 | Concrete physical details: stone, tomb, linen wrappings, the head-cloth 'rolled up in a place by itself', body absent — the material world matters and bears the evidence. |
| telos | salvation | 1 | 0.8 | Resurrection of Jesus as the vindication that grounds salvation for believers; 'he must rise from the dead' frames a redemptive necessity. |
| telos | communion | 2 | 0.65 | Mary's weeping search for 'my Lord' and the intimate 'the disciple whom Jesus loved' frame the end as restored personal presence with the risen one. |

### Coded moves — each with the context it picked up

**M1** — Mary Magdalene comes to the tomb at first-light on day one of the week, while it is still dark.
  · agent: Mary Magdalene · operation: come-to · substrate: the tomb · outcome: Mary is at the tomb at pre-dawn · narrator: the Fourth Evangelist, telling received tomb-tradition from an omniscient tracking POV
  · **gaps:** *reason* — No motive is stated for why Mary comes to the tomb at pre-dawn — whether she intends to mourn, to anoint the body, or something else is left entirely open. (residual)

**M2** — Mary sees that the burial-stone is no longer sealing the tomb.
  · agent: Mary Magdalene · operation: see-that · substrate: the state of the tomb (i.e. the embedded state-of-affairs M3) · outcome: Mary comes to know the tomb is open · narrator: the Fourth Evangelist, tracking Mary's POV at the tomb
  · **edges:** M2 —REPORTS→ M3

**M3** — The stone that sealed the tomb has been taken away.
  · agent: not-stated · operation: remove · substrate: the sealing-stone · outcome: the tomb is unsealed / open · narrator: Mary's perception as reported by the Fourth Evangelist
  · **gaps:** *agent* — The unsealing of the tomb has no named actor — the passage never identifies who or what removed the stone. (residual)
  · **edges:** ["M2"] —REPORTS→ M3

**M4** — Mary runs from the tomb and goes to Simon Peter and the disciple whom Jesus loved.
  · agent: Mary Magdalene · operation: run-to · substrate: her own body / the path to the two disciples · outcome: Mary reaches Peter and the beloved disciple · narrator: the Fourth Evangelist

**M5** — Mary tells the two disciples the following.
  · agent: Mary Magdalene · operation: say-to · substrate: the utterance-content she conveys (embedded moves M6 and M7) · outcome: Peter and the beloved disciple receive her report · narrator: the Fourth Evangelist
  · **edges:** M5 —CONTAINS→ M6; M5 —CONTAINS→ M7

**M6** — Some unspecified 'they' have taken the Lord out of the tomb.
  · agent: 'they' (unspecified) · operation: take-away · substrate: 'the Lord' (Jesus's body, as Mary names him) · outcome: the Lord is no longer in the tomb · narrator: Mary (as reported by the Fourth Evangelist); Mary's own construal, not the narrator's warrant
  · **edges:** ["M5"] —CONTAINS→ M6

**M7** — Mary and her group do not know the place where the Lord's body has been put.
  · agent: 'we' (Mary and her group) · operation: not-know-where · substrate: the location of the Lord's body (the embedded LAY-move M8) · outcome: the location is opaque to them · narrator: Mary (as reported by the Fourth Evangelist)
  · **gaps:** *agent (interior of 'we')* — Mary reports that 'we do not know where they laid him,' but no move identifies who was with her at the tomb before she ran to the disciples — the 'we' implies at least one other witness who remains unnamed. (residual)
  · **edges:** M7 —REPORTS→ M8; ["M5"] —CONTAINS→ M7

**M8** — The unspecified 'they' have laid the Lord's body in some place.
  · agent: 'they' (unspecified) · operation: lay-somewhere · substrate: the Lord's body ('him') · outcome: the body is at some location unknown to Mary · narrator: Mary (as reported by the Fourth Evangelist)
  · **edges:** ["M7"] —REPORTS→ M8

**M9** — Peter and the beloved disciple leave and head toward the tomb together.
  · agent: Peter and the beloved disciple (joint) · operation: set-out-toward · substrate: themselves / the road to the tomb · outcome: the two are on the way to the tomb, running together · narrator: the Fourth Evangelist, tracking the two-disciple pair

**M10** — The beloved disciple outpaces Peter on the way.
  · agent: the beloved disciple · operation: outrun · substrate: Peter (the one outpaced) · outcome: the beloved disciple is ahead of Peter · narrator: the Fourth Evangelist, marking the Petrine/beloved-disciple rivalry that is a Johannine signature

**M11** — The beloved disciple arrives at the tomb before Peter does.
  · agent: the beloved disciple · operation: arrive-first · substrate: the tomb · outcome: the beloved disciple is at the tomb before Peter · narrator: the Fourth Evangelist

**M12** — The beloved disciple stoops down at the entrance in order to look inside.
  · agent: the beloved disciple · operation: bend-down-to-look · substrate: his own body / the tomb-entrance · outcome: he is positioned to see into the tomb · narrator: the Fourth Evangelist

**M13** — From that stooped position he sees the linen wrappings inside.
  · agent: the beloved disciple · operation: see · substrate: the state inside the tomb (the embedded state M14) · outcome: the beloved disciple perceives the wrappings-as-lying · narrator: the Fourth Evangelist tracking the beloved disciple's POV
  · **edges:** M13 —REPORTS→ M14

**M14** — The linen burial-wrappings are lying inside the tomb.
  · agent: not-stated · operation: lie-there · substrate: the linen wrappings · outcome: the wrappings persist in their in-tomb position · narrator: the beloved disciple's perception as reported by the Fourth Evangelist
  · **edges:** ["M13"] —REPORTS→ M14

**M15** — The beloved disciple, however, does not enter the tomb.
  · agent: the beloved disciple · operation: not-enter · substrate: the tomb interior (declined) · outcome: the beloved disciple stays outside · narrator: the Fourth Evangelist, marking the hesitation
  · **gaps:** *reason* — The beloved disciple arrives first (M11), positions himself to look in (M12), perceives the wrappings (M13/M14), and then stops short — no reason for his restraint is given. (residual)

**M16** — Simon Peter arrives after him at the tomb.
  · agent: Simon Peter · operation: come-following · substrate: his own path / the tomb-approach · outcome: Peter reaches the tomb, second · narrator: the Fourth Evangelist

**M17** — Peter goes on into the tomb.
  · agent: Simon Peter · operation: enter · substrate: the tomb interior · outcome: Peter is inside the tomb · narrator: the Fourth Evangelist, marking that Peter is the first to cross the threshold

**M18** — From inside, Peter sees the burial-wrappings and, separately, the head-cloth.
  · agent: Simon Peter · operation: see · substrate: the state inside the tomb (the embedded states M19 and M20) · outcome: Peter perceives the two distinct textile arrangements · narrator: the Fourth Evangelist, tracking Peter's POV inside the tomb
  · **edges:** M18 —CONTAINS→ M19; M18 —CONTAINS→ M20

**M19** — The linen burial-wrappings are lying inside the tomb.
  · agent: not-stated · operation: lie-there · substrate: the linen wrappings · outcome: the wrappings remain in position · narrator: Peter's perception as reported by the Fourth Evangelist
  · **edges:** ["M18"] —CONTAINS→ M19

**M20** — The cloth that had covered Jesus's head is not with the other wrappings; it has been rolled up and set apart in its own spot.
  · agent: not-stated (the rolling and setting-apart imply an unspecified agent) · operation: be-rolled-up-apart · substrate: the head-cloth · outcome: the head-cloth is in a rolled, separated arrangement · narrator: Peter's perception as reported by the Fourth Evangelist
  · **gaps:** *significance* — The head-cloth is noted as rolled up and lying apart from the linen wrappings, but the passage assigns no meaning to this distinct arrangement — the detail is observed but not interpreted. (residual)
  · **edges:** ["M18"] —CONTAINS→ M20

**M21** — The beloved disciple now also enters the tomb.
  · agent: the beloved disciple · operation: enter · substrate: the tomb interior · outcome: the beloved disciple is inside · narrator: the Fourth Evangelist, noting that his earlier reticence (M15) now yields

**M22** — Once inside, the beloved disciple sees.
  · agent: the beloved disciple · operation: see (absolute) · substrate: not-stated (the seeing is used absolutely, without a named object) · outcome: the beloved disciple takes in what is there · narrator: the Fourth Evangelist, deliberately leaving the object of seeing open
  · **gaps:** *content* — When the beloved disciple enters and 'sees,' the object of his seeing is left unnamed — the verb is used absolutely, without specifying what he takes in that differs from what he and Peter have already observed. (residual)

**M23** — And he came to trust / hold-as-true.
  · agent: the beloved disciple · operation: believe (absolute) · substrate: not-stated (the belief is used absolutely, without a named content) · outcome: a state of faith / trust is established in him · narrator: the Fourth Evangelist, marking the Johannine faith-verb as the pivot of the scene
  · **gaps:** *content* — The beloved disciple's belief is stated with no complement — the verb carries no named object. What he believes (the resurrection, Mary's report, something even larger) is not specified. (residual); *warrant* — No path of reasoning or inference connects what the beloved disciple sees (M22) to his arriving at belief (M23) — the move from material perception to faith has no supplied mechanism. (residual)

**M24** — The narrator adds an aside: as of that moment the disciples had not yet grasped the scripture-testimony bearing on this event.
  · agent: the disciples (as a group) · operation: not-yet-understand · substrate: the scripture (whose content is the embedded proposition M25) · outcome: the interpretive frame is missing for them at that time · narrator: the Fourth Evangelist speaking in his own editorial voice, warranting a state-of-understanding claim about the characters
  · **gaps:** *tension with M23* — M23 reports the beloved disciple believes; M24 immediately reports that neither disciple yet understood the scripture about resurrection. The passage leaves entirely unresolved how belief can exist without the scriptural framework that would give it content. (residual)
  · **edges:** M24 —REPORTS→ M25

**M25** — According to that scripture, it is necessary for Jesus to rise from among the dead.
  · agent: he (Jesus) · operation: must-rise-from-dead · substrate: the state of being dead · outcome: he rises out of the dead · narrator: the scripture as invoked by the Fourth Evangelist's gloss
  · **gaps:** *reference* — The scripture that establishes the necessity of Jesus' rising is invoked but never named, quoted, or pointed at — it is treated as known without being identified. (residual)
  · **edges:** ["M24"] —REPORTS→ M25

**M26** — The two male disciples then head back to where they are staying.
  · agent: the disciples (Peter and the beloved disciple) · operation: return-home · substrate: themselves / the road back · outcome: they are back at their lodgings · narrator: the Fourth Evangelist, closing the male-witness episode before returning focus to Mary
  · **gaps:** *outcome (attestation to others)* — After the beloved disciple believes, both disciples return to their lodgings — no move shows them telling anyone what they found or believed; their discovery produces no outward attestation within the passage. (residual)

**M27** — Mary, unlike them, remains outside the tomb, on her feet, weeping.
  · agent: Mary Magdalene · operation: stand-weeping-outside · substrate: her own body-in-grief at the tomb-mouth · outcome: Mary persists at the site in a standing-and-weeping posture · narrator: the Fourth Evangelist, deliberately contrasting Mary's stay-behind with the disciples' departure
  · **gaps:** *edge — continuity between M26 and M27* — The disciples depart (M26) while Mary remains weeping at the tomb (M27). Whether they encountered her, spoke to her, or passed in silence on their way out is entirely unaddressed. (residual)

**M28** — In the middle of her weeping, Mary stoops down at the entrance to look inside the tomb.
  · agent: Mary Magdalene · operation: bend-down-to-look-in · substrate: her own body / the tomb-mouth · outcome: Mary is positioned to see into the tomb · narrator: the Fourth Evangelist, echoing the beloved disciple's earlier stooping (M12)

**M29** — From that stooped position she sees two white-robed angels inside the tomb.
  · agent: Mary Magdalene · operation: see · substrate: the interior scene of the tomb (the embedded state M30) · outcome: Mary perceives the two angelic figures at the body's former place · narrator: the Fourth Evangelist, tracking Mary's POV and introducing the angelic messengers
  · **edges:** M29 —REPORTS→ M30

**M30** — Two angels dressed in white are seated at the exact spot where the body had lain, one where the head had been, the other where the feet had been.
  · agent: not-stated (their seated presence is described, not their sitting-down act) · operation: be-sitting-at-the-body's-former-place · substrate: the two angels in white / the head-and-foot positions of the former body-site · outcome: the angels occupy the head and foot positions of the vacated body-place · narrator: Mary's perception as reported by the Fourth Evangelist
  · **edges:** ["M29"] —REPORTS→ M30

**M31** — The two angels address Mary with the following.
  · agent: the two angels · operation: say-to · substrate: the utterance-content they convey to Mary (embedded move M32) · outcome: Mary is addressed by the angelic pair · narrator: the Fourth Evangelist
  · **edges:** M31 —REPORTS→ M32

**M32** — The angels ask Mary — addressing her as 'woman' — why she is weeping.
  · agent: the two angels · operation: ask-why · substrate: Mary (as addressee) and her weeping-state (as the presupposition being interrogated) · outcome: an explanation of her weeping is elicited from Mary · narrator: the angels' speech as reported by the Fourth Evangelist
  · **gaps:** *reason (for angelic indirection)* — The angels address Mary with an interrogative ('why are you weeping?') rather than a proclamation about the resurrection or the empty tomb — the text never explains why their speech takes an eliciting rather than declarative form. (residual)
  · **edges:** ["M31"] —REPORTS→ M32

**M33** — Mary responds to the angels with the following.
  · agent: Mary Magdalene · operation: say-to · substrate: the utterance-content she conveys to the angels (embedded moves M34 and M35) · outcome: the angels receive Mary's reply · narrator: the Fourth Evangelist
  · **edges:** M33 —CONTAINS→ M34; M33 —CONTAINS→ M35

**M34** — Some unspecified 'they' have taken Mary's Lord away.
  · agent: 'they' (unspecified) · operation: take-away · substrate: 'my Lord' (Jesus's body, re-personalized in Mary's own voice) · outcome: the Lord is no longer where he was laid · narrator: Mary (as reported by the Fourth Evangelist)
  · **edges:** ["M33"] —CONTAINS→ M34

**M35** — Mary herself does not know where the Lord's body has been put.
  · agent: Mary ('I') · operation: not-know-where · substrate: the location of the Lord's body (the embedded LAY-move M36) · outcome: the location remains opaque to Mary · narrator: Mary (as reported by the Fourth Evangelist)
  · **edges:** M35 —REPORTS→ M36; ["M33"] —CONTAINS→ M35

**M36** — The unspecified 'they' have laid the Lord's body in some place.
  · agent: 'they' (unspecified) · operation: lay-somewhere · substrate: the Lord's body ('him') · outcome: the body is at some location unknown to Mary · narrator: Mary (as reported by the Fourth Evangelist)
  · **edges:** ["M35"] —REPORTS→ M36
