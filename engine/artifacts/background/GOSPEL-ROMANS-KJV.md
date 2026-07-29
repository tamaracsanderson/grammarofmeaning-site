# GOSPEL-ROMANS-KJV — background sheet

> Full coded transcript for **GOSPEL-ROMANS-KJV** — read-only snapshot from the DB.

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
| GOSPEL-ROMANS-KJV | 1109 | 0 | 0 | 0 |


## GOSPEL-ROMANS-KJV

### Sitz — situational conditions (source_grounding)

_(no Sitz grounding row)_

### Paradigm — the scripts the text thinks with (+ its stance toward each)

_(none coded)_

### Frame — the 8-axis morphospace coordinate

_(none coded)_

### Coded moves — each with the context it picked up

**M1** — Paul opens by placing himself in a bond-servant relation to Jesus Christ.
  · agent: Paul · operation: serve (be servant of) · substrate: Jesus Christ · outcome: Paul standing as servant of Jesus Christ · narrator: Paul, first-person epistolary author, self-identifying to the Roman assembly
  · **edges:** M1 —BEQUEATHS→ RECEPTION

**M2** — Paul reports himself as summoned into the office of apostle by an unnamed caller.
  · agent: not-stated (implicit caller) · operation: call · substrate: Paul · outcome: Paul constituted as apostle · narrator: Paul, first-person epistolary author

**M3** — Paul reports himself as set apart, dedicated toward the gospel that belongs to God.
  · agent: not-stated (implicit setter-apart) · operation: separate (set apart unto) · substrate: Paul · outcome: Paul consecrated toward the gospel of God · narrator: Paul, first-person epistolary author

**M4** — The parenthetical says God had beforehand pledged this gospel, doing so through his prophets and lodging the pledge in the holy writings.
  · agent: he (God) · operation: promise (afore, beforehand) · substrate: the gospel of God · outcome: the gospel standing as pre-pledged in scripture through the prophets · narrator: Paul, first-person epistolary author

**M5** — God's Son, on the fleshly side, was brought into being out of David's line.
  · agent: not-stated (implicit maker) · operation: make (bring forth from) · substrate: his Son Jesus Christ our Lord · outcome: Jesus standing as of David's seed according to the flesh · narrator: Paul, first-person epistolary author
  · **edges:** M5 —BEQUEATHS→ RECEPTION

**M6** — On the spirit-of-holiness side, that same Son was publicly marked out as God's Son-in-power, and the marking-out ran through his rising from the dead.
  · agent: not-stated (implicit declarer) · operation: declare (mark out, appoint publicly) · substrate: his Son Jesus Christ our Lord · outcome: Jesus manifested as Son of God with power, according to the spirit of holiness, by way of the resurrection · narrator: Paul, first-person epistolary author
  · **edges:** M6 —BEQUEATHS→ RECEPTION

**M7** — Through this Son, Paul and his circle came into possession of both favor and the office of apostle, and the point of that receiving is to bring the nations into faith's obedience, for the sake of the Son's name.
  · agent: we (Paul with his apostolic circle) · operation: receive · substrate: grace and apostleship (mediated through Jesus) · outcome: we holding grace-and-apostleship, aimed at obedience-of-faith among all the nations, for his name · narrator: Paul, first-person epistolary author

**M8** — Paul directs the letter toward everyone in Rome who belongs to the addressed group.
  · agent: Paul (implicit) · operation: address (direct letter to) · substrate: this letter/greeting · outcome: the letter aimed at all in Rome · narrator: Paul, first-person epistolary author

**M9** — The Romans stand as ones whom God holds dear.
  · agent: God · operation: love (hold dear) · substrate: those in Rome (the addressees) · outcome: the Romans standing as beloved of God · narrator: Paul, first-person epistolary author
  · **edges:** M9 —BEQUEATHS→ RECEPTION

**M10** — The Romans stand as ones summoned into holy standing.
  · agent: not-stated (implicit caller, God) · operation: call (summon into standing) · substrate: those in Rome (the addressees) · outcome: the Romans standing as saints (holy ones) by call · narrator: Paul, first-person epistolary author
  · **edges:** M10 —BEQUEATHS→ RECEPTION

**M11** — Paul performatively wishes favor and peace upon the addressees, sourced from the Father and the Lord Jesus Christ.
  · agent: Paul · operation: bless (wish grace and peace upon) · substrate: the Romans (addressees) · outcome: grace-and-peace pronounced upon them, sourced from God the Father and the Lord Jesus Christ · narrator: Paul, first-person epistolary author

**M12** — Paul turns to the thanksgiving section and offers thanks to his God, routing the thanks through Jesus Christ, on behalf of all of them.
  · agent: I (Paul) · operation: thank · substrate: my God · outcome: thanks rendered to God, through Jesus Christ, concerning all of them · narrator: Paul, first-person epistolary author
  · **edges:** M12 —BEQUEATHS→ RECEPTION

**M13** — Grounding the thanksgiving: the addressees' faith is being talked about all across the known world.
  · agent: not-stated (people throughout the world) · operation: speak of (report, be talked about) · substrate: your faith · outcome: the Romans' faith standing as known and reported worldwide · narrator: Paul, first-person epistolary author

**M14** — Paul invokes God as the one who stands as guarantor of what he is about to say.
  · agent: God · operation: witness (stand as attester) · substrate: Paul's forthcoming claim (implied) · outcome: God standing as witness to Paul · narrator: Paul, first-person epistolary author

**M15** — Paul says he renders service to this same God, and does so from his spirit, in the sphere of [the sentence is cut off here].
  · agent: I (Paul) · operation: serve (render cultic service to) · substrate: God (whom) · outcome: God served by Paul with his spirit, in a sphere the text does not finish specifying · narrator: Paul, first-person epistolary author

**M16** — Paul says he keeps the Romans continuously in his prayers, bringing them up without a break.
  · agent: I (Paul) · operation: make mention (in prayer) · substrate: you (the Romans) · outcome: the Romans held in continual remembrance in Paul's prayers · narrator: Paul, first-person epistolary author

**M17** — In those prayers, Paul is also lodging a specific petition — that somehow, at long last, he might be granted a smooth trip to reach them.
  · agent: I (Paul) · operation: make request (petition in prayer) · substrate: not-stated (the addressee of the request is implicit — God) · outcome: request lodged, whose content is M2a · narrator: Paul, first-person epistolary author
  · **edges:** M17 —REPORTS→ M18

**M18** — The content of the petition: that Paul gets a successful passage, contingent on God's will, so as to arrive to them.
  · agent: I (Paul), enabled by the will of God · operation: have a prosperous journey (be granted safe passage) · substrate: Paul's travel plan toward Rome · outcome: Paul arriving to the Romans by God-willed passage (wished-for, not accomplished) · narrator: Paul, first-person epistolary author
  · **edges:** ["M17"] —REPORTS→ M18

**M19** — Paul says he yearns to see them face to face, and he ties that yearning to a purpose: sharing some pneumatic gift with them so they stand firm.
  · agent: I (Paul) · operation: long (to see) · substrate: seeing you (the Romans) · outcome: Paul's longing-to-see directed toward the Romans, aimed at imparting some spiritual gift, so that they may be established · narrator: Paul, first-person epistolary author

**M20** — Paul immediately walks back the one-way sound of that: he clarifies that what he really means is that he and they will be mutually consoled through the faith the two sides share.
  · agent: I (Paul) together with you (the Romans) · operation: be comforted together (mutually) — clarify · substrate: the mutual faith of both of you and me · outcome: shared consolation between Paul and the Romans through their reciprocal faith · narrator: Paul, first-person epistolary author

**M21** — Paul turns to disclosure mode and addresses them as brothers, saying he does not want them left in the dark about something.
  · agent: I (Paul) · operation: would not have you ignorant (disclose, refuse to leave you unaware) · substrate: you (brethren) · outcome: the brethren being informed, whose content is M5a (and its adversative counterpart M5b) · narrator: Paul, first-person epistolary author
  · **edges:** M21 —CONTAINS→ M23; M21 —REPORTS→ M22

**M22** — The disclosed content: on many occasions Paul had firmly resolved to come to them — and the intent behind that resolution was to reap some fruit among them, matching what he has reaped among other gentile communities.
  · agent: I (Paul) · operation: purpose (repeatedly resolve, intend) · substrate: coming to you · outcome: a standing, repeated intention to travel to Rome, aimed at having some fruit among them just as among other Gentiles · narrator: Paul, first-person epistolary author
  · **edges:** ["M21"] —REPORTS→ M22

**M23** — The parenthetical undercuts M5a: up to now, Paul kept getting blocked from doing it.
  · agent: not-stated (implicit obstacle/hinderer) · operation: be hindered (be prevented, 'let' in the older sense of obstruct) · substrate: I (Paul) · outcome: Paul's coming blocked up to this present moment · narrator: Paul, first-person epistolary author
  · **edges:** M23 —BEQUEATHS→ RECEPTION; ["M21"] —CONTAINS→ M23

**M24** — Paul turns to a self-attribution: he stands under obligation to every category of gentile — Greeks and Barbarians, the cultured and the uncultured alike.
  · agent: I (Paul) · operation: be debtor (stand under obligation to) · substrate: Greeks and Barbarians, wise and unwise · outcome: Paul's standing as under obligation to all these groups · narrator: Paul, first-person epistolary author

**M25** — From that obligation Paul draws a conclusion about his own posture: to the limit of what he is capable of, he is set and eager to announce the gospel — [the object of the preaching is cut off in the source at this point].
  · agent: I (Paul) · operation: be ready (to preach) · substrate: the gospel (as message to be preached) · outcome: Paul standing ready to preach the gospel, up to the measure of what is in him — to a recipient the text does not finish naming · narrator: Paul, first-person epistolary author

**M26** — Paul reports of himself that he feels no shame toward the good-news-message that belongs to the Anointed.
  · agent: I (Paul) · operation: be not ashamed · substrate: the gospel of Christ · outcome: Paul standing unashamed of the gospel of Christ · narrator: Paul, first-person epistolary author, moving from personal-letter frame into theological exposition

**M27** — The reason: that message just IS God's own power operating toward rescue, and it operates that way for anyone at all who trusts — for the Jew as the first recipient and equally for the Greek.
  · agent: the gospel of Christ · operation: be (attribution — the gospel IS) · substrate: not-stated · outcome: the gospel standing as God's power unto salvation for every believer, with priority to the Jew and equally to the Greek · narrator: Paul, first-person epistolary author
  · **edges:** M27 —BEQUEATHS→ RECEPTION

**M28** — In that same message, a rightness-of-God's is uncovered — and the uncovering moves from trust into trust.
  · agent: not-stated (implicit God as revealer) · operation: reveal (uncover, disclose) · substrate: the righteousness of God · outcome: the righteousness of God disclosed within the gospel, on a faith-to-faith trajectory · narrator: Paul, first-person epistolary author

**M29** — Paul invokes scripture as a standing written record and points to what it contains.
  · agent: not-stated (scripture as authoritative source) · operation: be written (stand as inscribed in scripture) · substrate: the cited proposition (M4a) · outcome: the following claim standing under scriptural warrant · narrator: Paul, first-person epistolary author
  · **edges:** M29 —REPORTS→ M30

**M30** — The cited claim: the one who is righteous will draw his life from trust.
  · agent: the just (the righteous one) · operation: live (by faith) · substrate: not-stated · outcome: the righteous one having his life through faith · narrator: Paul, first-person epistolary author, ventriloquizing scripture
  · **edges:** M30 —BEQUEATHS→ RECEPTION; ["M29"] —REPORTS→ M30

**M31** — In parallel, God's anger is being uncovered from the heavenly side, aimed at every kind of impiety and injustice performed by human beings.
  · agent: not-stated (implicit God as revealer) · operation: reveal (uncover, disclose — from heaven) · substrate: the wrath of God · outcome: God's wrath disclosed from heaven, aimed at all ungodliness and unrighteousness of humans · narrator: Paul, first-person epistolary author

**M32** — Those humans, further specified: they take hold of the truth and pin it down inside unrighteousness.
  · agent: men (the humans just named) · operation: hold (down) the truth in unrighteousness · substrate: the truth · outcome: the truth held under and imprisoned within unrighteous conduct · narrator: Paul, first-person epistolary author
  · **edges:** M32 —BEQUEATHS→ RECEPTION

**M33** — The ground for that indictment: whatever can be known about God stands openly present inside them.
  · agent: not-stated (implicit — God as the one who makes it manifest, made explicit in M8) · operation: be manifest (stand openly present) · substrate: that which may be known of God · outcome: the knowable of God standing openly present within them · narrator: Paul, first-person epistolary author

**M34** — The reason that knowable-of-God is present in them: God himself did the showing.
  · agent: God · operation: shew (make apparent, disclose) · substrate: it (that which may be known of God) · outcome: the knowable of God actively shown by God to those humans · narrator: Paul, first-person epistolary author
  · **edges:** M34 —BEQUEATHS→ RECEPTION

**M35** — Elaborating the disclosure: God's own hidden attributes — specifically his everlasting power and his very godhood — have, all the way from the world's making, been plainly seen, taken in through the things God has made.
  · agent: not-stated (implicit humans as perceivers) · operation: be clearly seen (be perceptually taken in) · substrate: the invisible things of God — his eternal power and Godhead · outcome: God's invisible attributes standing as clearly perceived — ever since creation — through the things that are made · narrator: Paul, first-person epistolary author

**M36** — The result Paul draws: those humans stand with no defense to offer.
  · agent: they (the humans) · operation: be without excuse (stand as inexcusable) · substrate: not-stated (their standing before the disclosed God) · outcome: the humans standing as having no defense · narrator: Paul, first-person epistolary author
  · **edges:** M36 —BEQUEATHS→ RECEPTION

**M37** — Reaching backward to name the moment of failure: there was a state in which those humans had come to know God.
  · agent: they (the humans) · operation: know (God) · substrate: God · outcome: the humans standing as ones who had come to know God · narrator: Paul, first-person epistolary author

**M38** — Then the failure: they did not give him the honor owed to what he actually is — [the source cuts off mid-comparison].
  · agent: they (the humans) · operation: not glorify (fail to accord honor) · substrate: him (God) · outcome: God not honored by them as befits what he is (the comparison after 'as' is truncated) · narrator: Paul, first-person epistolary author
  · **edges:** M38 —BEQUEATHS→ RECEPTION

**M39** — Paired with the failure to give him honor: they also failed to render him any thanks.
  · agent: they (the humans) · operation: not be thankful (fail to render thanks) · substrate: not-stated (the tacit addressee of thanks is God) · outcome: the humans standing as ones who rendered no thanks · narrator: Paul, first-person epistolary author, continuing the apocalyptic-diagnostic exposition of gentile wrong
  · **edges:** M39 —BEQUEATHS→ RECEPTION

**M40** — Instead of that, they slid into futility in their own inner reasonings.
  · agent: they (the humans) · operation: become vain (become futile) · substrate: their imaginations (their reasonings) · outcome: their inner reasonings emptied into futility · narrator: Paul, first-person epistolary author

**M41** — The heart at their center — already senseless — was pushed into darkness.
  · agent: not-stated (the darkening comes upon them) · operation: be darkened · substrate: their foolish heart · outcome: their heart standing in darkness · narrator: Paul, first-person epistolary author

**M42** — They also performed a substitution: they swapped out the splendor of the imperishable God and put in its place a made-thing shaped like mortal humanity, and like birds, and four-legged animals, and slithering things.
  · agent: they (the humans) · operation: change (exchange, swap) · substrate: the glory of the uncorruptible God · outcome: God's glory swapped for an image resembling corruptible man, birds, four-footed beasts, and creeping things · narrator: Paul, first-person epistolary author
  · **edges:** M42 —BEQUEATHS→ RECEPTION

**M43** — As the consequent countermove, God handed them over into a state of impurity — through the cravings that lived in their own hearts — with the result that they degraded their own bodies among each other.
  · agent: God · operation: give up (deliver over, hand over) · substrate: them (the humans) · outcome: humans handed over to uncleanness by way of their own heart-lusts, so that they dishonored their own bodies among themselves · narrator: Paul, first-person epistolary author
  · **edges:** M43 —BEQUEATHS→ RECEPTION

**M44** — The relative clause names the same substitution move at a second level: they swapped what is true about God for a falsehood.
  · agent: they (the humans) · operation: change (exchange, swap) · substrate: the truth of God · outcome: the truth of God swapped for a lie · narrator: Paul, first-person epistolary author
  · **edges:** M44 —BEQUEATHS→ RECEPTION

**M45** — And they directed cultic reverence and cultic service at the made-thing rather than at the one who made it.
  · agent: they (the humans) · operation: worship and serve (in preference to) · substrate: the creature · outcome: the creature venerated and served in preference to the Creator · narrator: Paul, first-person epistolary author
  · **edges:** M45 —BEQUEATHS→ RECEPTION

**M46** — Paul breaks the accusation for a moment to pronounce the Creator worthy of praise into the ages, and seals it.
  · agent: the Creator · operation: bless / affirm-as-blessed (with sealing 'Amen') · substrate: not-stated · outcome: the Creator standing as blessed forever, sealed by Paul's Amen · narrator: Paul, first-person epistolary author, briefly stepping out of the diagnostic frame into a liturgical acclamation
  · **edges:** M46 —BEQUEATHS→ RECEPTION

**M47** — Because of all this, God performed a second handing-over: this time into shameful appetites.
  · agent: God · operation: give up (deliver over, hand over — second time) · substrate: them (the humans) · outcome: humans handed over into vile affections · narrator: Paul, first-person epistolary author
  · **edges:** M47 —BEQUEATHS→ RECEPTION

**M48** — Specifying the shameful appetites: their female members swapped out the customary/natural use and took up in its place what runs against nature.
  · agent: their women · operation: change (exchange, swap) · substrate: the natural use · outcome: the natural use swapped for what is against nature · narrator: Paul, first-person epistolary author
  · **edges:** M48 —BEQUEATHS→ RECEPTION

**M49** — In the same way, the male members abandoned the customary/natural use of the female.
  · agent: the men · operation: leave (abandon) · substrate: the natural use of the woman · outcome: the natural use of the woman abandoned by the men · narrator: Paul, first-person epistolary author
  · **edges:** M49 —BEQUEATHS→ RECEPTION

**M50** — And they were consumed by desire directed at each other — [the text is cut off mid-clause, mid-'men with men'].
  · agent: the men · operation: burn (be inflamed with lust) · substrate: their lust (turned one toward another) · outcome: the men standing consumed with mutual lust — 'men with men' begins to specify the resulting act but the source cuts off · narrator: Paul, first-person epistolary author

**M51** — Completing the male-male description: they are engaged in performing what is disgraceful.
  · agent: they (the men) · operation: work (perform, carry out) · substrate: that which is unseemly (the disgraceful deed) · outcome: disgraceful deeds performed by the men · narrator: Paul, first-person epistolary author, closing the male half of the against-nature diagnosis
  · **edges:** M51 —BEQUEATHS→ RECEPTION

**M52** — And, right in their own persons, they are taking back the pay-back that was the fitting match for their going-astray.
  · agent: they (the men) · operation: receive (in themselves) · substrate: the recompense of their error · outcome: the fitting recompense of their error received in their own persons · narrator: Paul, first-person epistolary author
  · **edges:** M52 —BEQUEATHS→ RECEPTION

**M53** — Now Paul steps back and names the underlying cognitive refusal: they did not deem God worth holding onto in their acknowledgment.
  · agent: they (the humans) · operation: not like (not test-as-worthy, not approve) to retain · substrate: God (in their knowledge) · outcome: God judged unworthy of retention in their acknowledgment · narrator: Paul, first-person epistolary author
  · **edges:** M53 —BEQUEATHS→ RECEPTION

**M54** — In tit-for-tat parallel, God handed them over — this time into an untested, unapproved mind — with the result that they do things that do not fit.
  · agent: God · operation: give over (deliver over, hand over — third time) · substrate: them (the humans) · outcome: humans handed over to a reprobate mind, so as to do the things which are not convenient · narrator: Paul, first-person epistolary author
  · **edges:** M54 —BEQUEATHS→ RECEPTION

**M55** — The reprobate mind's contents, laid out in an exhaustive catalogue: they are packed full of every kind of wrong — injustice, sexual disorder, moral wrong, greed, malice — teeming with envy, killing, quarrel, deceit, spite; they are gossips, slanderers, God-haters, insolent, arrogant, braggarts, inventors of new evils, disobedient to parents, without discernment, oath-breakers, without ordinary natural affection, incapable of being reconciled, without mercy.
  · agent: they (the humans) · operation: be filled with / be characterized as (attribution by vice-catalogue) · substrate: not-stated (they themselves stand as substrate of the filling) · outcome: they standing as filled with and characterized by every item in the vice-catalogue: unrighteousness, fornication, wickedness, covetousness, maliciousness, envy, murder, debate, deceit, malignity, whispering, backbiting, God-hatred, despite, pride, boasting, invention of new evils, disobedience to parents, lack of understanding, covenant-breaking, absence of natural affection, implacability, mercilessness · narrator: Paul, first-person epistolary author

**M56** — Paul closes the diagnosis by naming what they in fact know: God's righteous verdict — and specifying its content.
  · agent: they (the humans) · operation: know (have cognitive hold of) · substrate: the judgment of God (whose content is M6a) · outcome: the humans standing as ones who know God's judgment · narrator: Paul, first-person epistolary author
  · **edges:** M56 —REPORTS→ M57

**M57** — The content of that verdict: those who carry out such things stand deserving of death.
  · agent: they which commit such things · operation: be worthy of death (stand as deserving death) · substrate: not-stated · outcome: the doers-of-such-things standing as deserving of death · narrator: Paul, first-person epistolary author, ventriloquizing the content of God's judgment as it is known to them
  · **edges:** ["M56"] —REPORTS→ M57

**M58** — In the face of that known verdict, they not merely go on carrying out the same things themselves — but they also [the text is cut off before the second half arrives, though it begins 'but have...'].
  · agent: they (the humans) · operation: do (the same things) · substrate: the same things (the deeds named as capital-worthy in M6a) · outcome: the humans doing those same deeds — with a second, coordinated action ('but have...') beginning but truncated in the source · narrator: Paul, first-person epistolary author
  · **edges:** M58 —BEQUEATHS→ RECEPTION

**M59** — The final beat of the prior diagnosis: they also take satisfaction in the people who carry such things out.
  · agent: they (the humans of the prior diagnosis) · operation: have pleasure (in) · substrate: them that do such things · outcome: the humans standing as taking satisfaction in the doers of the capital-worthy deeds · narrator: Paul, first-person epistolary author, closing the vice-catalogue with a climactic co-consent beat

**M60** — Paul wheels around and speaks directly to a hypothetical interlocutor — a person, whoever he is, who occupies the seat of judgment on others — and pronounces him without any defense.
  · agent: thou (O man, whosoever thou art that judgest) · operation: be inexcusable (stand as one who has no defense) · substrate: not-stated (the judging-person's standing before God) · outcome: the judging-man standing as having no defense · narrator: Paul, first-person epistolary author, switching into direct second-person address (apostrophe / diatribal turn)

**M61** — The circumstantial ground: in the very act by which you pass judgment on another person...
  · agent: thou · operation: judge (another) · substrate: another (the judged party) · outcome: another passed under your verdict · narrator: Paul, first-person epistolary author, in diatribal apostrophe

**M62** — ...that very same act pronounces the verdict back on yourself.
  · agent: thou · operation: condemn (thyself) · substrate: thyself · outcome: the judge condemned by his own act of judging · narrator: Paul, first-person epistolary author, in diatribal apostrophe

**M63** — The deeper ground for M4: you, the judge, actually perform the very same acts you condemn.
  · agent: thou that judgest · operation: do (the same things) · substrate: the same things (as those you judge) · outcome: the judge doing the very deeds he condemns · narrator: Paul, first-person epistolary author, in diatribal apostrophe
  · **edges:** M63 —BEQUEATHS→ RECEPTION

**M64** — Paul steps back into the plural 'we' and reports a shared, settled cognition of God's verdict.
  · agent: we (Paul and his 'we-know' community) · operation: be sure (know as settled) · substrate: the content of the settled knowledge (M6a) · outcome: we standing as ones who share this settled knowledge · narrator: Paul, first-person epistolary author, briefly stepping from apostrophe to shared 'we know' formula
  · **edges:** M64 —REPORTS→ M65

**M65** — The content of that settled knowledge: God's verdict lines up with the way things truly are, and it lands on the ones who perform such things.
  · agent: the judgment of God · operation: be according to truth (be true-conforming) — against such doers · substrate: not-stated · outcome: God's judgment standing as truth-conforming, directed against those who commit such things · narrator: Paul, first-person epistolary author, ventriloquizing the shared knowledge
  · **edges:** ["M64"] —REPORTS→ M65

**M66** — Paul turns back to the interlocutor with a pointed rhetorical question: do you actually calculate that ...?
  · agent: thou (O man that judgest them which do such things and doest the same) · operation: think (rhetorically ask if the addressee calculates) · substrate: the content of the addressee's calculation (M7a) · outcome: the addressee held to account for what he supposes · narrator: Paul, first-person epistolary author, in diatribal apostrophe
  · **edges:** M66 —BEQUEATHS→ RECEPTION; M66 —REPORTS→ M67

**M67** — The content of that supposition: that you personally will slip out from under God's verdict.
  · agent: thou · operation: escape (the judgment of God) · substrate: the judgment of God · outcome: the addressee (in his own supposition) slipping out from under God's verdict · narrator: Paul, first-person epistolary author, ventriloquizing the addressee's implicit calculation
  · **edges:** M67 —BEQUEATHS→ RECEPTION; ["M66"] —REPORTS→ M67

**M68** — Or, second rhetorical prong: are you holding in contempt the abundance of God's kindness, restraint, and long-suffering?
  · agent: thou · operation: despise (hold in contempt) · substrate: the riches of his goodness and forbearance and longsuffering · outcome: God's kindness-riches held in contempt by the addressee · narrator: Paul, first-person epistolary author, in diatribal apostrophe
  · **edges:** M68 —BEQUEATHS→ RECEPTION

**M69** — The participial diagnosis running under M8: that despising is done in ignorance — you fail to recognize a specific fact.
  · agent: thou · operation: not know (fail to recognize) · substrate: the content of what is not recognized (M9a) · outcome: the addressee standing as one who does not know · narrator: Paul, first-person epistolary author
  · **edges:** M69 —BEQUEATHS→ RECEPTION; M69 —REPORTS→ M70

**M70** — The content the addressee fails to recognize: that God's kindness is leading him toward a turning-around.
  · agent: the goodness of God · operation: lead (guide toward) · substrate: thee (the addressee) · outcome: the addressee being led toward repentance by God's kindness · narrator: Paul, first-person epistolary author, ventriloquizing the content the interlocutor fails to recognize
  · **edges:** M70 —BEQUEATHS→ RECEPTION; ["M69"] —REPORTS→ M70

**M71** — The consequence for the addressee, given his hardness and unrepentant heart: he is stockpiling wrath — for himself — reserved for the day when wrath breaks out and God's righteous verdict is uncovered.
  · agent: thou (with hardness and impenitent heart) · operation: treasure up (stockpile, accumulate — for oneself) · substrate: wrath · outcome: wrath being stored up for the addressee, held against the day of wrath and the disclosure of God's righteous judgment · narrator: Paul, first-person epistolary author, in diatribal apostrophe

**M72** — Paul begins the counter-side of the ledger, naming those who, through patient sticking-with well-doing, are seeking after — [the object of their seeking is cut off in the source, along with the implied main verb of rendering-to-them].
  · agent: them who by patient continuance in well doing · operation: seek (for) · substrate: not-stated (truncated — the object of seeking would name what they seek) · outcome: the well-doers standing as persistent seekers of the (unstated) object; the implied main-clause of rendering-to-them is not supplied by the source · narrator: Paul, first-person epistolary author, opening the counter-cohort in a rendering-to-each construction
  · **edges:** M72 —BEQUEATHS→ RECEPTION

**M73** — Closing the seekers-clause from the prior sentence: to that patient-seeking cohort God pays back the life of the age-to-come.
  · agent: not-stated (God, implicit from the prior 'who will render to every man according to his deeds') · operation: render (repay, give in return — implied from the prior render-verb governing this dative sequence) · substrate: eternal life · outcome: eternal life rendered to the seekers of glory, honour, and immortality · narrator: Paul, first-person epistolary author, continuing the render-to-each-according-to-deeds ledger

**M74** — For the opposite cohort — those set in faction, refusing obedience to truth and instead giving obedience to unrighteousness — God pays back anger, wrath, pressure, and distress; and he does so upon every human person who works evil, on the Jew as first recipient and equally on the Greek.
  · agent: not-stated (God, implicit) · operation: render (repay — negative side) · substrate: indignation and wrath, tribulation and anguish · outcome: indignation, wrath, tribulation, and anguish rendered upon every evil-doing person — the contentious, the disobeyers of truth, the obeyers of unrighteousness — with priority to the Jew and equally to the Gentile · narrator: Paul, first-person epistolary author

**M75** — Flip back to the positive lane and open it universally: to every person who works good God pays back glory, honour, and peace — on the Jew as first recipient and equally on the Greek.
  · agent: not-stated (God, implicit) · operation: render (repay — positive side, universalized) · substrate: glory, honour, and peace · outcome: glory, honour, and peace rendered to every man that works good, with priority to the Jew and equally to the Gentile · narrator: Paul, first-person epistolary author

**M76** — First principle underneath the ledger: all who have gone wrong outside any law will meet their end outside that law as well.
  · agent: as many as have sinned without law · operation: perish (also, without law) · substrate: not-stated (their standing as sinners without law) · outcome: the without-law sinners perishing also without law — sin-mode and fate-mode matched · narrator: Paul, first-person epistolary author

**M77** — Parallel principle for the other side: all who have gone wrong inside the framework of the law will be adjudicated by that same framework.
  · agent: as many as have sinned in the law · operation: be judged (by the law) · substrate: not-stated (their standing as sinners in the law) · outcome: the in-law sinners judged by the law — sin-mode and judgment-mode matched · narrator: Paul, first-person epistolary author

**M78** — Parenthetical rule (negative half): the ones who merely take the law in as hearers are not the ones who stand as righteous before God.
  · agent: the hearers of the law · operation: be just (before God) · substrate: not-stated (their standing before God) · outcome: the hearers of the law standing as NOT just before God · narrator: Paul, first-person epistolary author, in a parenthetical clarifying the M5 principle

**M79** — Parenthetical rule (positive half): rather, it is those who actually perform the law who will be declared righteous.
  · agent: the doers of the law · operation: be justified (be pronounced righteous) · substrate: not-stated (their standing before God) · outcome: the doers of the law being pronounced righteous · narrator: Paul, first-person epistolary author, still inside the parenthesis

**M80** — The case-in-point that makes M7 make sense across the Jew-Gentile divide: whenever gentile persons — who do not possess the law — carry out the contents of the law from their own nature, then these people, without possessing the law, [the main clause naming what such Gentiles then are is cut off in the source].
  · agent: the Gentiles, which have not the law · operation: do (by nature, the things contained in the law) · substrate: the things contained in the law · outcome: law-conforming performance carried out by the Gentiles from their own nature — with the resulting main-clause (what such Gentiles then constitute) truncated in the source · narrator: Paul, first-person epistolary author

**M81** — Completing the prior conditional: those gentile persons, without possessing the given law, function as their own law-source.
  · agent: these (the Gentiles-who-do-by-nature from prior) · operation: be a law (unto themselves) · substrate: themselves · outcome: the gentile doers standing as law-to-themselves · narrator: Paul, first-person epistolary author, completing the natural-law case from the prior passage

**M82** — Those gentile doers display, visibly, the effect-of-the-law inscribed inside them — inside their very hearts.
  · agent: they (the same Gentiles) · operation: shew (display, manifest) · substrate: the work of the law (written in their hearts) · outcome: the law's work exhibited as inscribed in their hearts · narrator: Paul, first-person epistolary author

**M83** — Their own moral witness-organ — their consciousness of right — also stands as a co-witnessing voice.
  · agent: their conscience · operation: bear witness (co-testify) · substrate: not-stated (the fact of interior law-inscription just named) · outcome: conscience adding its testimony to M2's display · narrator: Paul, first-person epistolary author

**M84** — And, in the interval, their reasonings prosecute or defend one another back and forth.
  · agent: their thoughts (dialogismoi) · operation: accuse or else excuse (deliberative alternation) · substrate: one another (the thoughts among themselves) · outcome: an ongoing prosecuting-or-defending debate within their reasonings · narrator: Paul, first-person epistolary author

**M85** — The horizon under which all that interior witnessing takes place: the day when God will bring the hidden interior life of humans under his verdict, doing so by way of Jesus Christ, in accord with the announcement Paul preaches.
  · agent: God · operation: judge (the secrets of men) · substrate: the secrets of men · outcome: the hidden interior of humans brought under God's verdict, through Jesus Christ, according to Paul's gospel · narrator: Paul, first-person epistolary author, naming his own gospel as the standard of the judgment
  · **edges:** M85 —BEQUEATHS→ RECEPTION

**M86** — Attention-pointer: you carry the name 'Jew'.
  · agent: not-stated (the naming community that confers the label) · operation: be called (bear the name) · substrate: thou (the new addressee — the Jewish interlocutor) · outcome: the addressee standing under the name 'Jew' · narrator: Paul, first-person epistolary author, turning apostrophe to a new second-person interlocutor with the attention-marker 'Behold'

**M87** — You settle back and lean on the law as a place of security.
  · agent: thou · operation: rest (upon the law) · substrate: the law · outcome: the addressee taking his rest upon the law · narrator: Paul, first-person epistolary author
  · **edges:** M87 —BEQUEATHS→ RECEPTION

**M88** — And you make God the object of your boasting.
  · agent: thou · operation: boast (of God) · substrate: God · outcome: the addressee boasting of God as his distinguishing possession · narrator: Paul, first-person epistolary author

**M89** — You have cognitive hold of what he wills.
  · agent: thou · operation: know (his will) · substrate: his will (God's will) · outcome: the addressee standing as knower of God's will · narrator: Paul, first-person epistolary author

**M90** — You test and approve which things carry more weight, and you do that from the schooling the law gives you.
  · agent: thou · operation: approve (test-and-approve the more excellent) · substrate: the things that are more excellent · outcome: the addressee discriminating and approving the more-weighty things, out of law-derived instruction · narrator: Paul, first-person epistolary author

**M91** — You carry a settled confidence about what you yourself are.
  · agent: thou · operation: be confident (be persuaded of, hold-as-settled) · substrate: the content of that self-confidence (M11a) · outcome: the addressee holding a settled self-image whose content is M11a · narrator: Paul, first-person epistolary author
  · **edges:** M91 —BEQUEATHS→ RECEPTION; M91 —REPORTS→ M92

**M92** — The content of that self-confidence: you take yourself to occupy a whole set of pedagogic roles — one who guides the blind, one who is a light for those in the dark, one who instructs the foolish, one who teaches infants.
  · agent: thou thyself · operation: be (occupy such a set of pedagogic roles) · substrate: not-stated · outcome: the addressee standing (in his own conviction) as guide of the blind, light of those in darkness, instructor of the foolish, teacher of babes · narrator: Paul, first-person epistolary author, ventriloquizing the addressee's self-image
  · **edges:** M92 —BEQUEATHS→ RECEPTION; ["M91"] —REPORTS→ M92

**M93** — And you possess the outward shape of knowledge and of truth as they take form in the law.
  · agent: thou · operation: have (the form of knowledge and truth) · substrate: the form (morphosis) of knowledge and of the truth in the law · outcome: the addressee possessing the shaped outward form of knowledge and truth as configured in the law · narrator: Paul, first-person epistolary author
  · **edges:** M93 —BEQUEATHS→ RECEPTION

**M94** — So then: the descriptor names you as one who teaches someone else.
  · agent: thou · operation: teach (another) · substrate: another · outcome: the addressee standing as one who teaches another · narrator: Paul, first-person epistolary author
  · **edges:** M94 —BEQUEATHS→ RECEPTION

**M95** — The rhetorical question the descriptor sets up: do you fail to teach — [the source cuts off before the object is named; the syntax opens 'teachest thou not ...?' and pauses there].
  · agent: thou · operation: not teach (?) — do-you-fail-to-teach · substrate: not-stated (the object of the failed-teaching is truncated in the source) · outcome: the addressee put under a question about whom he fails to teach (object unsupplied by the source) · narrator: Paul, first-person epistolary author, in diatribal apostrophe
  · **edges:** M95 —BEQUEATHS→ RECEPTION

**M96** — Completing the prior rhetorical question: [do you fail to teach] your own self?
  · agent: thou · operation: not teach (thyself) · substrate: thyself · outcome: the addressee put under a question about failing to teach his own self · narrator: Paul, first-person epistolary author, in diatribal apostrophe to the Jewish interlocutor
  · **edges:** M96 —BEQUEATHS→ RECEPTION

**M97** — Descriptor of the addressee: you are one who publicly proclaims a specific directive.
  · agent: thou · operation: preach (proclaim publicly) · substrate: the directive content (M2a) · outcome: the addressee standing as public proclaimer of the directive · narrator: Paul, first-person epistolary author
  · **edges:** M97 —REPORTS→ M98

**M98** — The content of that preaching: the directive that a person is not to take what is not his.
  · agent: a man (indefinite subject of the directive) · operation: not steal (directive: refrain from stealing) · substrate: not-stated (the withheld act) · outcome: the directed man standing as one who is to refrain from stealing · narrator: Paul, first-person epistolary author, ventriloquizing the content the addressee preaches
  · **edges:** ["M97"] —REPORTS→ M98

**M99** — The trap-question: do you, yourself, do the very thing you proclaim against?
  · agent: thou · operation: steal (interrogatively pressed) · substrate: not-stated (the taking-of-what-is-not-yours) · outcome: the addressee put under interrogation about whether he performs the very act his preaching prohibits · narrator: Paul, first-person epistolary author, in diatribal apostrophe
  · **edges:** M99 —BEQUEATHS→ RECEPTION

**M100** — Same pattern, second instance: you are one who declares a specific prohibition.
  · agent: thou · operation: say (declare) · substrate: the directive content (M4a) · outcome: the addressee standing as one who declares the directive · narrator: Paul, first-person epistolary author
  · **edges:** M100 —REPORTS→ M101

**M101** — The content of that declaration: the directive that a person is not to violate marriage.
  · agent: a man (indefinite subject of the directive) · operation: not commit adultery (directive) · substrate: not-stated · outcome: the directed man standing as one who is to refrain from adultery · narrator: Paul, first-person epistolary author, ventriloquizing the addressee's declared directive
  · **edges:** ["M100"] —REPORTS→ M101

**M102** — Second trap-question: do you, yourself, perform the very violation you declare against?
  · agent: thou · operation: commit adultery (interrogatively pressed) · substrate: not-stated · outcome: the addressee put under interrogation about whether he performs the prohibited act · narrator: Paul, first-person epistolary author
  · **edges:** M102 —BEQUEATHS→ RECEPTION

**M103** — Third descriptor: you are one who recoils from idols.
  · agent: thou · operation: abhor (recoil from) · substrate: idols · outcome: the addressee standing as one who recoils from idols · narrator: Paul, first-person epistolary author

**M104** — Third trap-question: do you, yourself, plunder sacred things?
  · agent: thou · operation: commit sacrilege (rob temples) · substrate: not-stated (the sacred property that is the object of sacrilege) · outcome: the addressee put under interrogation about whether he plunders sacred things · narrator: Paul, first-person epistolary author
  · **edges:** M104 —BEQUEATHS→ RECEPTION

**M105** — Fourth descriptor: you are one who makes the law the object of your boasting.
  · agent: thou · operation: boast (of the law) · substrate: the law · outcome: the addressee boasting of the law as his distinguishing possession · narrator: Paul, first-person epistolary author

**M106** — The instrument through which the following question operates: you break the law.
  · agent: thou (implicit in the participial 'through breaking the law') · operation: break (transgress) the law · substrate: the law · outcome: the addressee standing as breaker of the law · narrator: Paul, first-person epistolary author
  · **edges:** M106 —BEQUEATHS→ RECEPTION

**M107** — Fourth trap-question: by means of that law-breaking, are you the one who brings God into dishonor?
  · agent: thou · operation: dishonour God · substrate: God · outcome: the addressee put under interrogation about whether he dishonors God through law-breaking · narrator: Paul, first-person epistolary author
  · **edges:** M107 —BEQUEATHS→ RECEPTION

**M108** — Paul turns from question to declaration: God's name is being spoken against, among the nations, on your account.
  · agent: not-stated (the Gentiles among whom the defaming happens, implicit) · operation: be blasphemed (be defamed, spoken against) · substrate: the name of God · outcome: God's name defamed among the Gentiles, on account of the addressee · narrator: Paul, first-person epistolary author
  · **edges:** M108 —BEQUEATHS→ RECEPTION

**M109** — Paul appeals to scripture as a standing record — the just-made claim sits under its warrant.
  · agent: not-stated (scripture as authoritative source) · operation: be written (stand as inscribed in scripture) · substrate: the assertion just made (M11) · outcome: M11's claim standing under scriptural warrant · narrator: Paul, first-person epistolary author

**M110** — New topic — circumcision. Paul concedes: the mark does bring genuine benefit — but only if you actually perform the law.
  · agent: circumcision · operation: profit (be advantageous) · substrate: not-stated (the addressee as beneficiary) · outcome: circumcision counting as advantage under the condition that the addressee keeps the law · narrator: Paul, first-person epistolary author

**M111** — The reversal: if instead you turn out to be a law-transgressor, the mark you carry undergoes a transformation into its opposite — your circumcision becomes uncircumcision.
  · agent: not-stated (the transforming force — the addressee's law-breaking / divine reckoning, implicit) · operation: be made (be transformed into) · substrate: thy circumcision · outcome: the addressee's circumcision transformed into uncircumcision, under the condition that he is a law-breaker · narrator: Paul, first-person epistolary author

**M112** — The mirror-image rhetorical question: if instead an uncircumcised person keeps the law's righteous requirement, is his uncircumcision not going to be reckoned as circumcision?
  · agent: not-stated (the reckoner — God, implicit) · operation: be counted (be reckoned as) · substrate: his uncircumcision · outcome: the uncircumcised person's uncircumcision reckoned for circumcision, under the condition that the uncircumcision keeps the law's righteousness · narrator: Paul, first-person epistolary author

**M113** — And the further mirror-question: is not the uncircumcised-by-birth person — provided he fulfils the law — going to pass verdict on you, who despite having the written text and the bodily mark [the source cuts off before naming what you do]?
  · agent: uncircumcision which is by nature · operation: judge (thee) · substrate: thee (the addressee — 'who by the letter and circumcision dost ...') · outcome: the law-fulfilling natural-uncircumcision passing verdict on the addressee, whose own law-relation-through-letter-and-circumcision is truncated in the source before its verb is delivered · narrator: Paul, first-person epistolary author

**M114** — Completing the rhetorical question from the prior passage: [do you, who possess the text and the bodily mark,] step across the law?
  · agent: thou (the addressee — who by the letter and circumcision) · operation: transgress (the law) · substrate: the law · outcome: the addressee put under interrogation about whether he transgresses the very law he possesses · narrator: Paul, first-person epistolary author, in diatribal apostrophe to the Jewish interlocutor
  · **edges:** M114 —BEQUEATHS→ RECEPTION

**M115** — Paul settles the redefinition negatively: the one whose Jewishness is at the outer, visible level does not count as a Jew.
  · agent: he (the one who is a Jew only outwardly) · operation: not be (a Jew) · substrate: not-stated · outcome: the outward-only person standing as not-a-Jew in the sense Paul is fixing · narrator: Paul, first-person epistolary author
  · **edges:** M115 —BEQUEATHS→ RECEPTION

**M116** — Parallel negative for the mark: the thing visible in the body is not what circumcision actually is.
  · agent: that (which is outward in the flesh) · operation: not be (circumcision) · substrate: not-stated · outcome: the outward-in-flesh mark standing as not-circumcision in the sense Paul is fixing · narrator: Paul, first-person epistolary author

**M117** — The positive counterpart: the one whose Jewishness is at the inner level — that person is the Jew.
  · agent: he (the one who is a Jew inwardly) · operation: be (a Jew) · substrate: not-stated · outcome: the inward person standing as a Jew in Paul's sense · narrator: Paul, first-person epistolary author
  · **edges:** M117 —BEQUEATHS→ RECEPTION

**M118** — The positive counterpart for the mark: circumcision is a matter of the heart, carried in spirit, not in the written text.
  · agent: circumcision · operation: be (of the heart, in the spirit, not in the letter) · substrate: not-stated · outcome: circumcision standing as heart-circumcision, held in the register of spirit rather than of letter · narrator: Paul, first-person epistolary author
  · **edges:** M118 —BEQUEATHS→ RECEPTION

**M119** — Closing the redefinition: the source of praise for that inward-Jew comes not from human quarters but from God.
  · agent: his praise (the true Jew's praise) · operation: be (of God, not of men) · substrate: not-stated · outcome: the true Jew's praise sourced from God rather than from human recognition · narrator: Paul, first-person epistolary author
  · **edges:** M119 —BEQUEATHS→ RECEPTION

**M120** — Paul poses the natural objection: what edge, in that case, does the Jew possess?
  · agent: the Jew · operation: have (advantage) — interrogatively · substrate: advantage (perisson) · outcome: the Jew's advantage put in question · narrator: Paul, first-person epistolary author, briefly voicing the imagined interlocutor's objection

**M121** — Parallel objection-question about the mark: what benefit is there in being circumcised?
  · agent: circumcision · operation: be (profit of circumcision) — interrogatively · substrate: not-stated · outcome: circumcision's profit put in question · narrator: Paul, first-person epistolary author

**M122** — Paul answers his own question with a strong affirmation: the advantage is considerable, on every axis one might name.
  · agent: not-stated (the Jew's advantage / circumcision's profit, held together) · operation: be (much, every way) · substrate: not-stated · outcome: the Jewish advantage affirmed as much-every-way · narrator: Paul, first-person epistolary author, answering his own diatribal question

**M123** — The chief ground of that advantage: God's utterances were placed in their trust.
  · agent: not-stated (God, implicit as entruster) · operation: be committed (entrusted) · substrate: the oracles of God · outcome: God's oracles entrusted to them (the Jews) · narrator: Paul, first-person epistolary author
  · **edges:** M123 —BEQUEATHS→ RECEPTION

**M124** — The counter-move: what does it change if some of them turned out not to trust?
  · agent: some (of them) · operation: not believe (fail to trust) · substrate: not-stated (the entrusted oracles / the promise) · outcome: some standing as ones who did not believe · narrator: Paul, first-person epistolary author
  · **edges:** M124 —BEQUEATHS→ RECEPTION

**M125** — The actual rhetorical question that hangs on M11: is that failure of theirs going to void God's own reliability?
  · agent: their unbelief · operation: make without effect (nullify, cancel) · substrate: the faith of God (God's faithfulness) · outcome: God's faithfulness (interrogatively) put at risk of being nullified by human unbelief · narrator: Paul, first-person epistolary author
  · **edges:** M125 —BEQUEATHS→ RECEPTION

**M126** — Paul dismisses the possibility flatly: absolutely not — may it never come to that.
  · agent: not-stated (Paul himself as speaker) · operation: may-it-not-be (emphatically deny) · substrate: the possibility raised by M12 (that human unbelief could nullify God's faithfulness) · outcome: the possibility emphatically denied · narrator: Paul, first-person epistolary author

**M127** — Paul's positive posture behind the denial: let God stand as the true one.
  · agent: God · operation: be true (jussive — let God be true) · substrate: not-stated · outcome: God affirmed as standing-true (even if it costs every human standing) · narrator: Paul, first-person epistolary author

**M128** — The paired counterpart, held in the same jussive: let every human being stand as a liar.
  · agent: every man · operation: be a liar (jussive — let every man be a liar) · substrate: not-stated · outcome: every human affirmed as standing-as-liar (against the standing of M14) · narrator: Paul, first-person epistolary author

**M129** — Paul brings scripture in as the standing warrant for the M14/M15 pair.
  · agent: not-stated (scripture as authoritative source) · operation: be written (stand as inscribed in scripture) · substrate: the cited content (M16a and M16b) · outcome: the following claims standing under scriptural warrant · narrator: Paul, first-person epistolary author
  · **edges:** M129 —CONTAINS→ M131; M129 —REPORTS→ M130

**M130** — First part of the cited content: that you (God, addressed) would be shown righteous in the words you speak.
  · agent: thou (God, addressed by the psalmist) · operation: be justified (be shown righteous) · substrate: thy sayings · outcome: God shown righteous in his own speech-acts · narrator: Paul, first-person epistolary author, ventriloquizing the psalmist's address to God
  · **edges:** ["M129"] —REPORTS→ M130

**M131** — Second part of the cited content: that you (God) would prevail whenever you are brought under judgment.
  · agent: thou (God, addressed by the psalmist) · operation: overcome (prevail when judged) · substrate: not-stated (the judgment-setting into which God is brought) · outcome: God prevailing whenever placed under judgment · narrator: Paul, first-person epistolary author, ventriloquizing the psalmist's address to God
  · **edges:** ["M129"] —CONTAINS→ M131

**M132** — New objection introduced as a conditional: what if our own going-wrong actually spotlights the rightness that belongs to God — [the main clause completing this hypothesis is cut off in the source].
  · agent: our unrighteousness · operation: commend (bring into view, showcase) · substrate: the righteousness of God · outcome: God's righteousness (hypothetically) shown-forth by human unrighteousness — the main clause exploring the consequence is truncated in the source · narrator: Paul, first-person epistolary author

**M133** — Paul opens with the diatribal deliberation-question: what verdict do we draw from all this?
  · agent: we (Paul with the imagined interlocutor) · operation: say (deliberatively — what shall we say?) · substrate: not-stated (the emerging topic) · outcome: the conclusion put open for question · narrator: Paul, first-person epistolary author, in diatribal mode

**M134** — The specific objection-question: is the God who administers wrath acting outside righteousness in doing so?
  · agent: God (who taketh vengeance) · operation: be unrighteous (interrogatively — of God who inflicts wrath) · substrate: not-stated · outcome: God's righteousness put in question given that he is the one who inflicts wrath · narrator: Paul, first-person epistolary author, ventriloquizing the imagined objection
  · **edges:** M134 —BEQUEATHS→ RECEPTION

**M135** — Paul flags the register of the question: he is speaking in the human, not the properly theological, key.
  · agent: I (Paul) · operation: speak (as a man — in the human register) · substrate: not-stated (this current line of questioning) · outcome: Paul's line of questioning marked as spoken in the human register · narrator: Paul, first-person epistolary author, breaking frame to qualify his own speech
  · **edges:** M135 —BEQUEATHS→ RECEPTION

**M136** — The conditional under which the next question stands: God's truth becomes still more richly on display through the falsehood I put out, and this all runs to his glory.
  · agent: the truth of God · operation: abound more (be amplified) — through my lie, unto his glory · substrate: not-stated (its own extent of display) · outcome: God's truth amplified through the medium of my lie, to God's glory · narrator: Paul, first-person epistolary author
  · **edges:** M136 —BEQUEATHS→ RECEPTION

**M137** — The corresponding question hanging on M4: given that hypothetical, why is verdict still passed on me as if I were an offender?
  · agent: I (Paul, in the objector's voice) · operation: be judged (as a sinner) — interrogatively · substrate: not-stated (Paul as sinner in the objector's construal) · outcome: Paul's continued placement under judgment-as-sinner put in question · narrator: Paul, first-person epistolary author, still voicing the human-register objection
  · **edges:** M137 —BEQUEATHS→ RECEPTION

**M138** — Paul pushes the reductio one step further: on the same logic, should we not instead adopt the directive [content M6a]?
  · agent: we (Paul with the imagined interlocutor) · operation: adopt-directive (interrogatively — why not rather ...?) · substrate: the recommended directive (M6a) · outcome: the do-evil-for-good directive presented as the absurd terminus of the M4-M5 logic · narrator: Paul, first-person epistolary author, in diatribal mode
  · **edges:** M138 —BEQUEATHS→ RECEPTION; M138 —REPORTS→ M139

**M139** — The content of the reductio directive: perform evils so that good things may result from them.
  · agent: we (indefinite first-plural subject of the directive) · operation: do evil (that good may come — directive) · substrate: evil (as what is to be done) · outcome: evil performed so that good may come out of it · narrator: Paul, first-person epistolary author, ventriloquizing the reductio conclusion
  · **edges:** M139 —BEQUEATHS→ RECEPTION; ["M138"] —REPORTS→ M139

**M140** — Parenthetical: we (Paul's circle) are being falsely reported — as if we did teach this.
  · agent: not-stated (the slanderers) · operation: be reported (slanderously) · substrate: we (Paul's apostolic circle) · outcome: Paul's circle defamed with a false report — the reported content is the M6a directive · narrator: Paul, first-person epistolary author, breaking frame parenthetically

**M141** — Parenthetical, second layer: certain people go so far as to actively affirm that we ourselves make this teaching.
  · agent: some (opponents of Paul) · operation: affirm (assert as fact) · substrate: the content of the affirmation (M8a) · outcome: the opponents' affirmation that Paul's circle teaches the directive · narrator: Paul, first-person epistolary author
  · **edges:** M141 —REPORTS→ M142

**M142** — The content of the opponents' affirmation: that we say [the directive].
  · agent: we (Paul's circle, in the opponents' construal) · operation: say (alleged — that we utter the directive) · substrate: the directive-content (M6a) · outcome: Paul's circle allegedly uttering the do-evil-for-good directive · narrator: Paul, first-person epistolary author, at second remove — reporting what opponents report Paul to be reporting
  · **edges:** ["M141"] —REPORTS→ M142

**M143** — Paul turns from the parenthesis to a verdict: the condemnation such people are under is deserved.
  · agent: their damnation (the condemnation on such reporters / promoters) · operation: be just (be deserved) · substrate: not-stated · outcome: their condemnation standing as deserved · narrator: Paul, first-person epistolary author

**M144** — Diatribal pivot into the universal-verdict section: what then follows? Do we (Jews) stand ahead of them (Gentiles)?
  · agent: we (Jews) · operation: be better (than they) — interrogatively · substrate: not-stated (the comparison to them, the Gentiles) · outcome: the Jewish comparative advantage put in question · narrator: Paul, first-person epistolary author

**M145** — Paul's own emphatic denial: not at all, on any reading.
  · agent: not-stated (Paul himself as speaker) · operation: no (emphatically deny) · substrate: the M10 possibility (Jewish comparative advantage in this sense) · outcome: the M10 possibility emphatically denied · narrator: Paul, first-person epistolary author

**M146** — The ground for that denial: Paul cites his own prior argumentation as having already established the point.
  · agent: we (Paul, using the argumentative 'we') · operation: prove (aforehand — establish by prior argument) · substrate: the content demonstrated (M12a) · outcome: the M12a content held as already established by prior argument · narrator: Paul, first-person epistolary author, citing his own prior chapters
  · **edges:** M146 —REPORTS→ M147

**M147** — The content of that prior demonstration: both Jews and Gentiles alike stand in one and the same place — under sin's dominion.
  · agent: both Jews and Gentiles (all of them) · operation: be (all under sin) · substrate: not-stated (their standing before God) · outcome: both cohorts standing all under sin · narrator: Paul, first-person epistolary author
  · **edges:** M147 —BEQUEATHS→ RECEPTION; ["M146"] —REPORTS→ M147

**M148** — Catena opens with a universal negation: no human being possesses genuine understanding.
  · agent: none (no one) · operation: understand (with universal negation — none does) · substrate: not-stated (the object of understanding) · outcome: universal absence of understanders · narrator: Paul, first-person epistolary author, in scriptural catena mode (Ps 14/53 LXX)
  · **edges:** M148 —BEQUEATHS→ RECEPTION

**M149** — Second universal negation: no one goes searching after God.
  · agent: none (no one) · operation: seek (after God — with universal negation) · substrate: God · outcome: universal absence of God-seekers · narrator: Paul, first-person epistolary author, in catena
  · **edges:** M149 —BEQUEATHS→ RECEPTION

**M150** — Universal wandering: all of them have turned off from the road.
  · agent: they (all) · operation: go out of the way (turn aside) · substrate: the way · outcome: all having turned aside from the way · narrator: Paul, first-person epistolary author, in catena
  · **edges:** M150 —BEQUEATHS→ RECEPTION

**M151** — Their state after that turning: they have collectively become useless.
  · agent: they (all together) · operation: become unprofitable (turn useless) · substrate: not-stated · outcome: all of them together standing as become-unprofitable · narrator: Paul, first-person epistolary author, in catena

**M152** — Sealed with universal negation of the good: no one at all — not even one — does what is good.
  · agent: none (no one, not even one) · operation: do good (with universal negation — none does, not one) · substrate: good · outcome: universal absence of good-doers · narrator: Paul, first-person epistolary author, in catena

**M153** — Catena shifts to body-parts. Their throat is a metaphor: it is a grave standing wide open.
  · agent: their throat · operation: be (an open sepulchre — metaphoric attribution) · substrate: not-stated · outcome: their throat standing as an open tomb (image of speech that emits deathliness) · narrator: Paul, first-person epistolary author, in catena (Ps 5:9 LXX)

**M154** — Continuing the body-parts catena: with their tongues they [carry out a specific act — the source cuts off before the verb of the clause arrives, though the KJV continuation is 'have used deceit'].
  · agent: they · operation: (unstated verb) — with their tongues, they do something · substrate: not-stated (the object of the truncated action) · outcome: the addressees performing some tongue-mediated action — the verb the source is heading toward is not delivered · narrator: Paul, first-person epistolary author, in catena (mid-clause of Ps 5:9 continuation)

**M155** — Completing the prior catena clause: their tongues have been the instrument by which they have practiced deceit.
  · agent: they · operation: use (deceit — with tongues as instrument) · substrate: deceit · outcome: deceit employed by them through their tongues · narrator: Paul, first-person epistolary author, in the closing lines of the scriptural catena

**M156** — Next body-part in the catena: what lies beneath their lips is the venom of asps.
  · agent: the poison of asps · operation: be (under their lips — as venom-under-lips) · substrate: not-stated · outcome: asp-venom standing as what is lodged under their lips · narrator: Paul, first-person epistolary author, in catena (Ps 140:3 LXX)

**M157** — Paul turns from catena to reflection with a shared-cognition claim: we all recognize a certain fact about the law's scope of address.
  · agent: we (Paul with his shared 'we-know' community) · operation: know (share as settled recognition) · substrate: the content of the settled recognition (M3a) · outcome: we standing as ones who share this recognition about the law's addressees · narrator: Paul, first-person epistolary author
  · **edges:** M157 —REPORTS→ M158

**M158** — The content of that recognition: whatever the law utters, it utters to the ones who stand inside the law.
  · agent: the law (as speaking-agent) · operation: say (address — the law speaks to those under it) · substrate: them who are under the law · outcome: the law's speech targeted specifically at those inside its jurisdiction · narrator: Paul, first-person epistolary author, ventriloquizing the shared recognition
  · **edges:** ["M157"] —REPORTS→ M158

**M159** — The first end that this speaking-under-the-law is aimed at: every mouth is silenced.
  · agent: every mouth · operation: be stopped (be silenced — of every mouth) · substrate: not-stated · outcome: every mouth brought to silence (no defense left to be spoken) · narrator: Paul, first-person epistolary author

**M160** — The second end: the entire world comes to stand as liable before God.
  · agent: all the world · operation: become guilty (become liable — before God) · substrate: not-stated (the world's standing before God) · outcome: the whole world brought to stand as liable before God · narrator: Paul, first-person epistolary author

**M161** — Paul draws the conclusion: no flesh at all will be pronounced righteous in God's sight, on the basis of law-performances.
  · agent: no flesh · operation: be justified (be pronounced righteous — with universal negation, by law-deeds, in his sight) · substrate: not-stated (their standing before God) · outcome: universal absence of law-deed justification — no human at all pronounced righteous in God's sight on that basis · narrator: Paul, first-person epistolary author

**M162** — The reason: what the law actually does is generate cognitive recognition of sin.
  · agent: not-stated (knowledge-of-sin, as what arises through the law) · operation: be (knowledge of sin — by/through the law) · substrate: not-stated · outcome: knowledge-of-sin standing as what the law produces · narrator: Paul, first-person epistolary author

**M163** — The turn — the letter's pivot: apart from the law, God's own rightness has now been brought into the open.
  · agent: not-stated (implicit God as revealer) · operation: be manifested (be openly disclosed) · substrate: the righteousness of God (without the law) · outcome: God's righteousness openly disclosed, apart from the law, in the present time · narrator: Paul, first-person epistolary author, at the letter's programmatic pivot ('but now')

**M164** — That same disclosure is at the same time attested by the older witnesses — the law itself and the prophets stand as its testifiers.
  · agent: the law and the prophets (as attesters) · operation: be witnessed (be attested) · substrate: the righteousness of God (from M8) · outcome: God's righteousness attested by law and prophets · narrator: Paul, first-person epistolary author

**M165** — Further specification of that disclosed righteousness: it comes into effect through the faith of Jesus Christ, and it reaches to all who trust — landing upon them.
  · agent: the righteousness of God · operation: be (by faith of Jesus Christ — unto all and upon all them that believe) · substrate: not-stated · outcome: the disclosed righteousness standing as by-faith-of-Jesus-Christ, extending to and coming upon all who believe · narrator: Paul, first-person epistolary author
  · **edges:** M165 —BEQUEATHS→ RECEPTION

**M166** — Because there stands no distinction between people at this point.
  · agent: not-stated (the class of humans facing M10) · operation: be (no difference — no distinction among humans in this respect) · substrate: not-stated · outcome: the human class standing as undifferentiated before this disclosed righteousness · narrator: Paul, first-person epistolary author

**M167** — Continuing the specification of how believers stand: they are being pronounced righteous as a free gift, on the basis of God's favor, through the buying-back that lodges in Christ Jesus.
  · agent: not-stated (believers, from M10-M11) · operation: be justified (freely — by his grace, through the redemption in Christ Jesus) · substrate: not-stated (their standing before God) · outcome: believers pronounced righteous as a free gift, grounded in God's grace, mediated through the redemption in Christ Jesus · narrator: Paul, first-person epistolary author
  · **edges:** M167 —BEQUEATHS→ RECEPTION

**M168** — That same Christ — God publicly placed him forward as a mercy-place, and this operates through trust in his blood.
  · agent: God · operation: set forth (place publicly, ordain as) · substrate: whom (Christ Jesus) · outcome: Christ Jesus publicly placed as propitiation, operative through faith in his blood · narrator: Paul, first-person epistolary author
  · **edges:** M168 —BEQUEATHS→ RECEPTION

**M169** — The purpose of that public placement: to publicly display God's own rightness, aimed at the passing-over of [the source cuts off before naming which sins].
  · agent: not-stated (implicitly God as the one whose righteousness is displayed through Christ's public placement) · operation: declare (his righteousness — for the remission of ...) · substrate: his righteousness · outcome: God's righteousness publicly displayed, aimed at the remission of [truncated — presumably the sins of the past, per the KJV continuation] · narrator: Paul, first-person epistolary author

**M170** — Completing the prior clause: past offenses are passed over, and the means of that passing-over is God's holding-back.
  · agent: not-stated (God as the implicit forbearer) · operation: remit (pass over — past sins, through forbearance) · substrate: sins that are past · outcome: past sins passed over, mediated through God's forbearance · narrator: Paul, first-person epistolary author, closing the propitiation-purpose clause from the prior passage

**M171** — Paul re-emphasizes with a marker ('I say'): the aim of the propitiation-setting is to publicly show God's own righteousness, and to do so precisely in this present season.
  · agent: not-stated (God as the one whose righteousness is displayed) · operation: declare (publicly show — his righteousness, at this time) · substrate: his righteousness · outcome: God's righteousness publicly displayed in the present time (nun-kairos) · narrator: Paul, first-person epistolary author, using 'I say' as an epistolary re-emphasis marker

**M172** — First side of the paradox the display secures: God stands as just.
  · agent: he (God) · operation: be just (stand as righteous) · substrate: not-stated · outcome: God standing as just, secured by the M2 display · narrator: Paul, first-person epistolary author

**M173** — Second side of the paradox: at the same time God stands as the one who pronounces righteous the person who trusts in Jesus.
  · agent: he (God) · operation: be (justifier — of him who believes in Jesus) · substrate: him which believeth in Jesus · outcome: God standing as justifier of the Jesus-believer · narrator: Paul, first-person epistolary author

**M174** — Paul turns to a diatribal question: given all this, where does boasting go?
  · agent: boasting · operation: be (where — boasting) — interrogatively · substrate: not-stated · outcome: the location of boasting put in question · narrator: Paul, first-person epistolary author, in diatribal mode

**M175** — The blunt answer: it is shut out.
  · agent: it (boasting) · operation: be excluded (be shut out) · substrate: not-stated · outcome: boasting shut out · narrator: Paul, first-person epistolary author

**M176** — Follow-up question about the mechanism: by which principle — the one that runs on performances?
  · agent: not-stated (the M6 exclusion mechanism) · operation: be excluded (by what law — of works?) — interrogatively · substrate: not-stated · outcome: the mode of exclusion put in question, with 'works-law' proposed as a candidate · narrator: Paul, first-person epistolary author

**M177** — Paul rejects the works-answer and supplies the correct one: not by that principle; rather, by the principle-of-faith.
  · agent: not-stated (the M6 exclusion mechanism) · operation: be excluded (by the law of faith — not by works) · substrate: not-stated · outcome: the exclusion mechanism identified as the law of faith, and the works-answer rejected · narrator: Paul, first-person epistolary author

**M178** — Paul draws the conclusion of the argument, using a reckoning verb ('we conclude') that flags the following as inference.
  · agent: we (Paul with the argumentative 'we') · operation: conclude (reckon — draw an inference) · substrate: the content of the concluded inference (M9a) · outcome: the following thesis held as inferred from the M1-M8 argument · narrator: Paul, first-person epistolary author
  · **edges:** M178 —REPORTS→ M179

**M179** — The concluded content — the thesis-statement of the whole argument: a human being is pronounced righteous through trust, standing apart from law-performances.
  · agent: a man (indefinite subject) · operation: be justified (by faith, without the deeds of the law) · substrate: not-stated (the man's standing before God) · outcome: a human pronounced righteous by faith, apart from the deeds of the law · narrator: Paul, first-person epistolary author, ventriloquizing his own concluded thesis
  · **edges:** ["M178"] —REPORTS→ M179

**M180** — Next diatribal question: is God's Godhood confined to Jews as the only cohort in view?
  · agent: he (God) · operation: be (God of the Jews only) — interrogatively · substrate: not-stated · outcome: God's confinement-to-Jews put in question · narrator: Paul, first-person epistolary author

**M181** — The negative reformulation as its own question: is he not equally of the gentile cohort as well?
  · agent: he (God) · operation: be (God of the Gentiles also) — interrogatively · substrate: not-stated · outcome: God's inclusion-of-Gentiles proposed via question · narrator: Paul, first-person epistolary author

**M182** — Paul supplies the answer: yes — of the gentile cohort too.
  · agent: he (God) · operation: be (God of the Gentiles also — affirmed) · substrate: not-stated · outcome: God affirmed as belonging equally to the Gentiles · narrator: Paul, first-person epistolary author

**M183** — The ground of that answer: God is one.
  · agent: not-stated (God as substrate of the oneness-attribution) · operation: be (one God) · substrate: not-stated · outcome: God standing as one · narrator: Paul, first-person epistolary author

**M184** — First arm of what the one God will do: he will pronounce righteous the circumcised cohort — on the basis of trust.
  · agent: one God (from M13) · operation: justify (pronounce righteous — the circumcision, by faith) · substrate: the circumcision (the circumcised cohort) · outcome: the circumcision pronounced righteous by faith · narrator: Paul, first-person epistolary author

**M185** — Second arm, held in parallel: and he will pronounce righteous the uncircumcised — through trust.
  · agent: one God (from M13) · operation: justify (pronounce righteous — the uncircumcision, through faith) · substrate: the uncircumcision (the uncircumcised cohort) · outcome: the uncircumcision pronounced righteous through faith · narrator: Paul, first-person epistolary author

**M186** — Anticipated objection as a question: does that faith-move mean we are cancelling the law?
  · agent: we (Paul with the imagined interlocutor) · operation: make void (nullify — the law through faith) — interrogatively · substrate: the law · outcome: the law's nullification put in question as a possible consequence of the faith-move · narrator: Paul, first-person epistolary author

**M187** — Paul flatly denies it: absolutely not.
  · agent: not-stated (Paul himself as speaker) · operation: may-it-not-be (emphatically deny) · substrate: the M16 possibility (that faith nullifies the law) · outcome: the M16 possibility emphatically denied · narrator: Paul, first-person epistolary author

**M188** — Positive counterpart of the denial: on the contrary, we prop the law up.
  · agent: we · operation: establish (uphold, set-in-place — the law) · substrate: the law · outcome: the law upheld by the faith-move · narrator: Paul, first-person epistolary author

**M189** — Paul opens the next section with a deliberative question about a specific test-case: what should we say Abraham (our ancestor on the fleshly line) has come by?
  · agent: we (Paul with the imagined interlocutor) · operation: say (deliberatively — what shall we say ... hath found?) · substrate: the content of the deliberation (M19a) · outcome: the Abrahamic case-content put open for question · narrator: Paul, first-person epistolary author, pivoting to Abraham
  · **edges:** M189 —REPORTS→ M190

**M190** — The content of the deliberation: Abraham — the forefather on the fleshly-line side — has come upon [some finding whose object Paul is about to spring].
  · agent: Abraham our father (as pertaining to the flesh) · operation: find (come upon — with unspecified object) · substrate: not-stated (the object of finding is what the deliberation-question interrogates) · outcome: Abraham held as the subject of a finding whose object M19 asks us to name · narrator: Paul, first-person epistolary author, ventriloquizing the Abrahamic case-content
  · **edges:** ["M189"] —REPORTS→ M190

**M191** — Paul entertains the hypothetical: suppose Abraham WAS pronounced righteous on the basis of what he performed.
  · agent: Abraham · operation: be justified (by works — hypothetically) · substrate: not-stated · outcome: Abraham (hypothetically) pronounced righteous on the basis of works · narrator: Paul, first-person epistolary author

**M192** — The consequent of the hypothetical: he would then have grounds for something — [the source cuts off before the object arrives, though the KJV continuation is 'to glory'].
  · agent: he (Abraham, in the hypothetical) · operation: have (whereof to ... — object truncated) · substrate: not-stated (grounds for the truncated object) · outcome: Abraham holding, in the hypothetical, grounds for [truncated] — the object of 'whereof to ...' is not delivered by the source · narrator: Paul, first-person epistolary author

**M193** — Completing the hypothetical consequent from the prior passage: [Abraham then would have grounds] for boasting.
  · agent: he (Abraham, still in the ei-Abraam-ex-ergon hypothetical) · operation: have (grounds to boast / glory) · substrate: not-stated (his grounds for boasting) · outcome: Abraham holding, in the hypothetical, grounds for boasting · narrator: Paul, first-person epistolary author, closing the ch 4 opening hypothetical

**M194** — Paul cuts the hypothetical short by naming the location where the boast does not stand: in God's presence.
  · agent: the M1 boast (as substrate whose God-facing standing is denied) · operation: be (not — before God — with respect to the M1 boast) · substrate: not-stated · outcome: the M1 boast standing as not-holding before God · narrator: Paul, first-person epistolary author

**M195** — Paul turns to scripture as the settling voice with a diatribal question: what does scripture actually say?
  · agent: the scripture · operation: say (interrogatively — what does the scripture say?) · substrate: the content of what scripture says (M4 and M5) · outcome: scripture's utterance called out for citation, whose content follows · narrator: Paul, first-person epistolary author, invoking scripture as a speaking authority
  · **edges:** M195 —CONTAINS→ M197; M195 —REPORTS→ M196

**M196** — First half of scripture's answer: Abraham gave trust to God.
  · agent: Abraham · operation: believe (God — give trust to) · substrate: God · outcome: Abraham standing as one who trusted God · narrator: Paul, first-person epistolary author, ventriloquizing Gen 15:6 as scripture's answer
  · **edges:** M196 —BEQUEATHS→ RECEPTION; ["M195"] —REPORTS→ M196

**M197** — Second half of scripture's answer: that trust of his was entered into the ledger, credited to him under the heading of righteousness.
  · agent: not-stated (God as reckoner, implicit) · operation: be counted (be reckoned — for righteousness) · substrate: it (Abraham's believing, from M4) · outcome: Abraham's believing entered into the ledger and credited to him as righteousness · narrator: Paul, first-person epistolary author, ventriloquizing the second clause of Gen 15:6
  · **edges:** ["M195"] —CONTAINS→ M197

**M198** — Paul supplies the accounting-principle underlying M5: for the person whose relation is one of performing, the pay-out is not entered as a gift but as an owed sum.
  · agent: not-stated (the reward, as substrate booked one way or the other) · operation: not be reckoned (of grace) — but of debt · substrate: the reward · outcome: the worker's reward booked as owed-debt rather than as grace-gift · narrator: Paul, first-person epistolary author

**M199** — Descriptor of the God the non-worker trusts: he is the one who pronounces righteous the person who stands as ungodly.
  · agent: him (God, characterized here) · operation: justify (pronounce righteous — the ungodly) · substrate: the ungodly (asebes) · outcome: the ungodly person pronounced righteous by God · narrator: Paul, first-person epistolary author, providing the substantive characterization of the God the non-worker believes on

**M200** — Contrast to M6: for the person who does NOT work, but who trusts in that ungodly-justifying God, the trust itself is what gets entered into the ledger — credited as righteousness.
  · agent: not-stated (God as reckoner, implicit) · operation: be counted (be reckoned — his faith for righteousness) · substrate: his faith (the non-worker's trust) · outcome: the non-worker's faith entered into the ledger and credited to him as righteousness · narrator: Paul, first-person epistolary author

**M201** — Paul brings in a second scriptural witness: David also gives an account of the same happy standing of the man to whom God credits righteousness apart from performances.
  · agent: David · operation: describe (give an account of — the blessedness of the man) · substrate: the blessedness of the man (whose content is M9a) · outcome: David giving verbal shape to the blessedness of the M9a-characterized man · narrator: Paul, first-person epistolary author, invoking David as a second scriptural voice
  · **edges:** M201 —REPORTS→ M202

**M202** — The content of David's description: God credits righteousness — and does so apart from performances — to the man in view.
  · agent: God · operation: impute (credit — righteousness, without works) · substrate: righteousness · outcome: righteousness credited by God to the man, apart from works · narrator: Paul, first-person epistolary author, ventriloquizing the M9 description
  · **edges:** ["M201"] —REPORTS→ M202

**M203** — Continuing David's testimony with a further reporting-participle: he goes on to say the following.
  · agent: David (implied continuation from M9) · operation: say (utter — with recoverable quotation-content) · substrate: the content of the utterance (M10a) · outcome: David's makarism delivered as quotation-content · narrator: Paul, first-person epistolary author
  · **edges:** M203 —REPORTS→ M204

**M204** — The quoted content of David's makarism: the ones whose lawless acts have been let-off and whose offenses have been draped-over — those people stand as blessed.
  · agent: they (whose iniquities are forgiven, and whose sins are covered) · operation: be blessed (attribution of makarism-standing on a characterized cohort) · substrate: not-stated · outcome: the characterized cohort standing as blessed · narrator: Paul, first-person epistolary author, ventriloquizing Ps 32:1 (LXX)
  · **edges:** ["M203"] —REPORTS→ M204

**M205** — Paul opens the next question about scope: does this happy-standing arrive only on the circumcised cohort, or does it come upon the uncircumcised as well?
  · agent: this blessedness · operation: come upon (arrive on — this blessedness) — interrogatively · substrate: the circumcision (only) — or the uncircumcision (also) · outcome: the scope of the M9-M10 blessedness put in question · narrator: Paul, first-person epistolary author

**M206** — The ground for reopening the question: our own settled saying is that trust was entered into the ledger for Abraham as righteousness.
  · agent: we (Paul with his 'we-say' community) · operation: say (assert — as a settled claim) · substrate: the settled claim being said (M12a) · outcome: the M12a reckoning-claim held as our settled saying · narrator: Paul, first-person epistolary author, citing his own settled formulation
  · **edges:** M206 —REPORTS→ M207

**M207** — The content of our saying: trust was entered into the ledger for Abraham, credited to him as righteousness.
  · agent: not-stated (God as reckoner, implicit) · operation: be reckoned (be entered into the ledger — faith to Abraham for righteousness) · substrate: faith (Abraham's trust) · outcome: Abraham's faith entered into the ledger and credited to him as righteousness · narrator: Paul, first-person epistolary author, ventriloquizing his own settled claim
  · **edges:** M207 —BEQUEATHS→ RECEPTION; ["M206"] —REPORTS→ M207

**M208** — Paul sharpens the question with a next rhetorical follow-up: how, under what circumstance, was that reckoning done?
  · agent: not-stated (the M12a reckoning-act, as substrate whose circumstance is queried) · operation: be reckoned (interrogatively — how, under what circumstance?) · substrate: it (Abraham's faith, from M12a) · outcome: the circumstance-of-the-reckoning put in question · narrator: Paul, first-person epistolary author

**M209** — The specific circumstance-alternatives Paul poses to answer M13: was Abraham in the state of being circumcised at that time, or was he in the state of [being uncircumcised — the source cuts off before the second disjunct arrives].
  · agent: he (Abraham) · operation: be (in circumcision — or in [uncircumcision]) — interrogatively · substrate: not-stated (his state at the time of the M12a reckoning) · outcome: Abraham's state at the time of reckoning put in question — circumcision or the truncated alternative · narrator: Paul, first-person epistolary author

**M210** — Completing the second disjunct of the prior rhetorical question: [or was he in the state of] being uncircumcised?
  · agent: he (Abraham) · operation: be (in uncircumcision — as second interrogative disjunct) · substrate: not-stated (his state at the time of the M12a-prior reckoning) · outcome: the uncircumcision-alternative for Abraham's state put in question, completing the disjunction · narrator: Paul, first-person epistolary author, closing the prior rhetorical Q about Abraham's state at the time of the reckoning

**M211** — Paul supplies the answer to the disjunction: not in the state of being circumcised — rather, in the state of being uncircumcised.
  · agent: he (Abraham) · operation: be (not in circumcision, but in uncircumcision — as contrastive answer) · substrate: not-stated · outcome: Abraham's state at the time of reckoning identified as uncircumcised, with the circumcision-alternative rejected · narrator: Paul, first-person epistolary author

**M212** — The sequel event: he took onto himself the sign that is circumcision.
  · agent: he (Abraham) · operation: receive (take onto oneself — the sign of circumcision) · substrate: the sign of circumcision · outcome: Abraham having received the sign of circumcision (subsequent to his already-reckoned faith) · narrator: Paul, first-person epistolary author

**M213** — Attribution about what that sign actually is: it is a stamped seal on the righteousness that came from the trust.
  · agent: the sign of circumcision (from M3) · operation: be (a seal — of the righteousness of the faith) · substrate: not-stated · outcome: the sign standing as a seal-stamp on the righteousness-of-faith · narrator: Paul, first-person epistolary author

**M214** — Further attribution qualifying the M4 faith: this trust of his was in his possession already, at a time when he still stood uncircumcised.
  · agent: he (Abraham) · operation: have (hold in possession — the faith, while yet being uncircumcised) · substrate: the faith (from M4) · outcome: Abraham's faith held in possession by him during the time of his uncircumcision · narrator: Paul, first-person epistolary author

**M215** — First purpose of that reception-of-sign-after-faith sequence: that he might occupy fatherhood over all who trust, even those who lack circumcision.
  · agent: he (Abraham) · operation: be father (of all them that believe, though not circumcised) · substrate: all them that believe (though they be not circumcised) · outcome: Abraham standing as father over all uncircumcised believers · narrator: Paul, first-person epistolary author

**M216** — Second purpose, coordinate with M6: that righteousness might be entered into the ledger for those uncircumcised believers as well.
  · agent: not-stated (God as reckoner, implicit) · operation: be imputed (be credited — righteousness, unto them also) · substrate: righteousness · outcome: righteousness credited to the uncircumcised believers as well · narrator: Paul, first-person epistolary author
  · **edges:** M216 —BEQUEATHS→ RECEPTION

**M217** — The parallel fatherhood over the circumcised cohort, held with a qualification: father to those who are not merely of the circumcision but who ALSO follow the trust-steps of Abraham.
  · agent: he (Abraham) · operation: be father (of circumcision — to a qualified cohort) · substrate: them who are not of the circumcision only, but who also walk in the steps of Abraham's faith · outcome: Abraham standing as father over the qualified circumcised-and-also-faith-walking cohort · narrator: Paul, first-person epistolary author

**M218** — Attribution about that qualifying condition: they take their steps along the same trust-path our forefather Abraham held while he was still uncircumcised.
  · agent: they (the qualified circumcision-cohort of M8) · operation: walk (take steps in — the faith-steps of Abraham, held pre-circumcision) · substrate: the steps of that faith of our father Abraham (which he had being yet uncircumcised) · outcome: the cohort walking in Abraham's pre-circumcision faith-steps · narrator: Paul, first-person epistolary author

**M219** — Paul draws the promise into the same frame: the promise made to Abraham and his line was not conveyed by the law-channel — it was conveyed through faith-righteousness.
  · agent: the promise · operation: be (not through the law — but through the righteousness of faith — of the promise) · substrate: not-stated (its mediating channel) · outcome: the promise standing as mediated through faith-righteousness rather than through the law, to Abraham and his seed · narrator: Paul, first-person epistolary author
  · **edges:** M219 —CONTAINS→ M220

**M220** — The content of that promise: that Abraham would stand as heir of the whole world.
  · agent: he (Abraham) · operation: be (heir of the world) · substrate: the world · outcome: Abraham standing as heir over the world (the promise's content) · narrator: Paul, first-person epistolary author, ventriloquizing the promise's content
  · **edges:** ["M219"] —CONTAINS→ M220

**M221** — Paul opens the reductio: suppose that the ones who belong to the law-cohort are the heirs.
  · agent: they which are of the law · operation: be (heirs — of the law-cohort, hypothetically) · substrate: not-stated (the inheritance) · outcome: the law-cohort (hypothetically) standing as heirs · narrator: Paul, first-person epistolary author
  · **edges:** M221 —BEQUEATHS→ RECEPTION

**M222** — The consequent of M11: then trust is emptied out — [the source cuts off before the parallel 'and the promise made of none effect' arrives].
  · agent: not-stated (the M11 hypothetical, as force emptying the faith) · operation: be made void (be emptied — of faith) · substrate: faith · outcome: faith emptied of content, as consequent of the M11 hypothetical — the source truncates before the parallel-clause about the promise arrives · narrator: Paul, first-person epistolary author
  · **edges:** M222 —BEQUEATHS→ RECEPTION

**M223** — Completing the M12-prior consequent: and in the same stroke the promise is drained of its force.
  · agent: not-stated (the M11-prior law-heirs hypothetical, as the emptying force) · operation: be made of none effect (be voided of force) · substrate: the promise · outcome: the promise drained of its force, held in parallel with the M12-prior faith-emptying · narrator: Paul, first-person epistolary author, closing the reductio-consequent from the prior passage

**M224** — The reason both go together: what the law is actually productive of is wrath.
  · agent: the law · operation: work (produce, generate — wrath) · substrate: wrath · outcome: wrath produced as the law's yield · narrator: Paul, first-person epistolary author

**M225** — The underlying general rule: at any location where there is no law in place, there is nothing to count as transgression.
  · agent: not-stated (the general principle-frame) · operation: be (no law → no transgression — general principle) · substrate: not-stated (the correlation between law-presence and transgression-existence) · outcome: no-law and no-transgression standing as co-varying: where the first is absent, the second is absent · narrator: Paul, first-person epistolary author

**M226** — Given all this, the ground is now named: the inheritance rests on trust.
  · agent: it (the promise/inheritance, from M1 and prior) · operation: be (of faith — attribution about the ground of the inheritance/promise) · substrate: not-stated · outcome: the promise/inheritance grounded in faith · narrator: Paul, first-person epistolary author

**M227** — First purpose of the M4 grounding: that the inheritance might come by favor rather than by owed-pay.
  · agent: it (the promise/inheritance) · operation: be (by grace — purpose) · substrate: not-stated · outcome: the promise mediated by grace rather than by owed-pay · narrator: Paul, first-person epistolary author

**M228** — Second purpose: so that the promise might stand as certain, and stand so for the whole line of descendants.
  · agent: the promise · operation: be sure (be certain — the promise, to all the seed) · substrate: not-stated · outcome: the promise standing as secure to all the seed (universally) · narrator: Paul, first-person epistolary author

**M229** — Specifying who 'all the seed' means: not restricted to the descendants who belong to the law, but also including those who share Abraham's trust.
  · agent: the seed (from M6) · operation: be (of the seed — scope-specification: not only law-seed, but also Abraham-faith-seed) · substrate: not-stated · outcome: the seed-scope specified as both the law-cohort AND the faith-of-Abraham cohort · narrator: Paul, first-person epistolary author

**M230** — Descriptor of the Abraham anchoring both arms: he stands as father over all of us.
  · agent: he (Abraham) · operation: be (father of us all) · substrate: us all · outcome: Abraham standing as father over all-of-us (both cohorts) · narrator: Paul, first-person epistolary author

**M231** — Paul brings scripture in to attest that fatherhood: it stands written that God addressed him in these words.
  · agent: not-stated (scripture as authoritative source) · operation: be written (stand as inscribed in scripture — parenthetical attestation) · substrate: the cited content (M9a) · outcome: the following divine address standing under scriptural warrant · narrator: Paul, first-person epistolary author
  · **edges:** M231 —REPORTS→ M232

**M232** — The cited divine address: I have placed you in the position of being father over a multitude of nations.
  · agent: I (God, in direct address) · operation: make (appoint as — father of many nations) · substrate: thee (Abraham) · outcome: Abraham appointed as father of many nations by God's own act · narrator: Paul, first-person epistolary author, ventriloquizing Gen 17:5
  · **edges:** ["M231"] —REPORTS→ M232

**M233** — The relative clause on the God-in-whose-sight Abraham stands as father: the one whom he trusted.
  · agent: he (Abraham) · operation: believe (trust — God) · substrate: him (God, characterized as the one believed) · outcome: Abraham having trusted this God — locating the M8 fatherhood before that God · narrator: Paul, first-person epistolary author
  · **edges:** M233 —BEQUEATHS→ RECEPTION

**M234** — First divine attribute in the who-clause chain: he is the one who brings the dead back to life.
  · agent: God (the one Abraham believed, from M10) · operation: quicken (make alive — the dead) · substrate: the dead · outcome: the dead brought to life by God · narrator: Paul, first-person epistolary author
  · **edges:** M234 —BEQUEATHS→ RECEPTION

**M235** — Second divine attribute in the chain: he addresses non-existing things by name, as though they already existed.
  · agent: God (from M10-M11) · operation: call (name-summon — those things which be not, as though they were) · substrate: those things which be not · outcome: the non-existent things summoned by name as if they existed · narrator: Paul, first-person epistolary author

**M236** — Returning to Abraham: contrary to every natural expectation, he still gave trust — resting his trust on hope itself.
  · agent: he (Abraham) · operation: believe (trust — against hope, in hope) · substrate: not-stated (God's promise from M9a) · outcome: Abraham trusting in defiance of natural-hope-evidence, held within hope itself · narrator: Paul, first-person epistolary author
  · **edges:** M236 —BEQUEATHS→ RECEPTION

**M237** — The purpose held out through that against-hope trust: that he might come to occupy the position of father over a multitude of nations.
  · agent: he (Abraham) · operation: become (father of many nations — purpose-outcome of the M13 trust) · substrate: many nations · outcome: Abraham coming to occupy fatherhood over many nations, as the purpose held under the M13 believing · narrator: Paul, first-person epistolary author

**M238** — Paul appeals to a further scriptural word as the standard: as the utterance ran.
  · agent: not-stated (God as the divine speaker, implicit) · operation: be spoken (be uttered — of an authoritative divine word) · substrate: the uttered content (M15a) · outcome: the following divine utterance standing as the standard against which M14 is measured · narrator: Paul, first-person epistolary author
  · **edges:** M238 —REPORTS→ M239

**M239** — The uttered content: in this way — like [the stars, understood from Gen 15:5] — your descendants will be.
  · agent: thy seed (Abraham's descendants) · operation: be (thy seed shall be — so, thus) · substrate: not-stated · outcome: Abraham's descendants standing (in the future) as innumerable — the comparison-referent implied but not spelled out in the quoted words themselves · narrator: Paul, first-person epistolary author, ventriloquizing Gen 15:5
  · **edges:** ["M238"] —REPORTS→ M239

**M240** — Further attribution about Abraham's trust-condition: he did not go slack in his trust.
  · agent: he (Abraham) · operation: be (not weak — in faith) · substrate: not-stated · outcome: Abraham standing as not-weak in the register of faith · narrator: Paul, first-person epistolary author

**M241** — The specific act of the M16 not-weakness: he refused to fix his attention on his own body, dead as it now was — his age being around a hundred years.
  · agent: he (Abraham) · operation: consider (not — his own body, dead) · substrate: his own body (now dead, when he was about an hundred years old) · outcome: Abraham refusing to fix his attention on his own age-and-death-marked body · narrator: Paul, first-person epistolary author

**M242** — Parallel refusal in a second direction: nor yet [did he fix his attention on — the second object, the deadness of Sarah's womb, is truncated at 'neither yet'].
  · agent: he (Abraham) · operation: (not consider — second, truncated substrate) · substrate: not-stated (truncated — the second object of the refused attention; the KJV continuation is 'the deadness of Sarah's womb') · outcome: Abraham refusing to fix his attention on a second death-marker whose specific substrate the source does not deliver · narrator: Paul, first-person epistolary author

**M243** — Completing the second refused-attention object from the prior passage: [nor yet did Abraham fix his attention on] the barrenness-like death of Sarah's womb.
  · agent: he (Abraham, from the prior 'neither yet') · operation: (not consider — second substrate arrives: the deadness of Sarah's womb) · substrate: the deadness of Sarah's womb · outcome: Abraham refusing to fix his attention on the second death-marker — Sarah's barren womb — alongside his own age-marked body · narrator: Paul, first-person epistolary author, closing the not-considering pair from the prior passage

**M244** — Positive attribution about Abraham's response to the promise: he did not waver at God's promise, and he did not do so through disbelief either.
  · agent: he (Abraham) · operation: not stagger (not waver, not be divided — at the promise, through unbelief) · substrate: the promise of God · outcome: Abraham standing as one who did not waver at the promise through unbelief · narrator: Paul, first-person epistolary author

**M245** — The positive-flip attribution: rather, he was made strong in the register of trust.
  · agent: he (Abraham) · operation: be strong (be strengthened — in faith) · substrate: not-stated · outcome: Abraham strengthened in the register of faith · narrator: Paul, first-person epistolary author

**M246** — The concurrent act: he gave over glory to God.
  · agent: he (Abraham) · operation: give (glory — to God) · substrate: glory · outcome: glory rendered by Abraham to God · narrator: Paul, first-person epistolary author

**M247** — The cognitive-state undergirding the trust: he had been fully brought over to a settled conviction.
  · agent: he (Abraham) · operation: be fully persuaded (be fully brought over to settled conviction) · substrate: the content of the conviction (M5a) · outcome: Abraham brought over to settled conviction about M5a · narrator: Paul, first-person epistolary author
  · **edges:** M247 —REPORTS→ M248

**M248** — The content of that settled conviction: God has the power to bring to completion what he pledged.
  · agent: he (God) · operation: be able (have power — to perform what he had promised) · substrate: what he had promised (the pledge to be performed) · outcome: God standing as able to carry out what he had pledged · narrator: Paul, first-person epistolary author, ventriloquizing the content of Abraham's conviction
  · **edges:** M248 —BEQUEATHS→ RECEPTION; ["M247"] —REPORTS→ M248

**M249** — Paul pivots the whole Abraham-passage forward: the record was not put into writing solely on Abraham's behalf.
  · agent: not-stated (the implicit inscriber — scripture as authoritative source) · operation: be written (be put into scripture — not for his sake alone) · substrate: the content of the writing (M6a) · outcome: the reckoning-passage put into writing not for Abraham's sake alone · narrator: Paul, first-person epistolary author, pivoting from historical-Abraham to hermeneutical extension
  · **edges:** M249 —REPORTS→ M250

**M250** — The content of that written record: Abraham's trust was entered into the ledger and credited to him.
  · agent: not-stated (God as reckoner, implicit) · operation: be imputed (be entered into the ledger — to him) · substrate: it (Abraham's faith) · outcome: Abraham's faith entered into the ledger and credited to him · narrator: Paul, first-person epistolary author, ventriloquizing the written record's content
  · **edges:** ["M249"] —REPORTS→ M250

**M251** — The extension of the M6 scope-claim to Paul's addressees: rather, the record was written for us as well — us to whom the same reckoning is to be credited in the future.
  · agent: not-stated (God as reckoner, implicit) · operation: be imputed (be entered into the ledger — future, to us also) · substrate: it (the M6a reckoning-content) · outcome: the same reckoning to be credited to us, under the condition specified in M8 · narrator: Paul, first-person epistolary author

**M252** — The condition under which the M7 future-reckoning holds: our own trusting is directed toward the same God — the one who raised Jesus.
  · agent: we · operation: believe (trust — on him who raised Jesus) · substrate: him (the God-who-raised-Jesus, from M9) · outcome: we trusting the Jesus-raising God, as the condition-of-membership in the M7 future-reckoning · narrator: Paul, first-person epistolary author

**M253** — Descriptor of the God trusted: he is the one who lifted up Jesus, our Lord, out of death.
  · agent: him (God, characterized here) · operation: raise up (lift out of death — Jesus our Lord, from the dead) · substrate: Jesus our Lord · outcome: Jesus lifted up from the dead by God · narrator: Paul, first-person epistolary author
  · **edges:** M253 —BEQUEATHS→ RECEPTION

**M254** — Relative clause on that raised Jesus: he was handed over on account of our slips.
  · agent: not-stated (God as the implicit hander-over, echoing the paradosis-chain of Rom 1) · operation: be delivered (be handed over — for our offences) · substrate: Jesus (from M9) · outcome: Jesus handed over on account of our offences · narrator: Paul, first-person epistolary author
  · **edges:** M254 —BEQUEATHS→ RECEPTION

**M255** — Second beat of the Jesus-relative: he was lifted up again, and this happened for the sake of our being declared righteous.
  · agent: not-stated (God as the implicit raiser, from M9) · operation: be raised again (be lifted up again — for our justification) · substrate: Jesus (from M9) · outcome: Jesus lifted up again for the sake of our justification · narrator: Paul, first-person epistolary author
  · **edges:** M255 —BEQUEATHS→ RECEPTION

**M256** — Drawing the conclusion out of the M8-M11 configuration: given that we stand pronounced righteous through trust.
  · agent: not-stated (God as reckoner, implicit) · operation: be justified (be pronounced righteous — by faith) · substrate: we · outcome: we standing pronounced righteous through faith · narrator: Paul, first-person epistolary author, opening ch 5

**M257** — The main upshot: we hold peace with God, and hold it through our Lord Jesus Christ as the mediator.
  · agent: we · operation: have (hold — peace with God, through our Lord Jesus Christ) · substrate: peace with God · outcome: we holding peace with God, mediated through our Lord Jesus Christ · narrator: Paul, first-person epistolary author

**M258** — Through that same Christ, we have entry — by trust — into this favor-realm.
  · agent: we · operation: have (hold — access, by faith, into this grace) · substrate: access (into this grace, by faith, through Christ) · outcome: we holding access into the grace-realm, by faith, mediated through Christ · narrator: Paul, first-person epistolary author

**M259** — Descriptor of that grace-realm: it is where we now stand.
  · agent: we · operation: stand (in this grace) · substrate: this grace · outcome: we standing in the grace-realm accessed in M14 · narrator: Paul, first-person epistolary author

**M260** — We also do this: we exult in the hope of God's glory.
  · agent: we · operation: rejoice (exult, boast — in hope of the glory of God) · substrate: the hope of the glory of God · outcome: we exulting in the hope of the glory of God · narrator: Paul, first-person epistolary author

**M261** — And beyond that too — we exult even inside pressures.
  · agent: we · operation: glory (exult, boast — in tribulations also) · substrate: tribulations · outcome: we exulting even in tribulations · narrator: Paul, first-person epistolary author

**M262** — The cognitive-state undergirding the M17 exultation-in-pressure: we know [the following content — the source cuts off before the content is delivered, though the KJV continuation is 'that tribulation worketh patience'].
  · agent: we · operation: know (with recoverable content — truncated) · substrate: not-stated (the content of what we know is truncated in the source) · outcome: we standing as knowers of a content whose specification the source does not deliver · narrator: Paul, first-person epistolary author

**M263** — Completing the content of the M18-prior 'knowing': pressure produces stayed-under endurance.
  · agent: tribulation · operation: work (produce, generate — patience) · substrate: patience · outcome: patience produced by tribulation · narrator: Paul, first-person epistolary author, closing the eidotes-content that opened at the end of the prior passage

**M264** — The terminus of the chain, arrived-at abruptly: that hope does not put us to shame.
  · agent: hope · operation: make not ashamed (not put to shame — of hope) · substrate: not-stated (us, as those held under the hope) · outcome: hope not putting us to shame · narrator: Paul, first-person epistolary author

**M265** — The ground for that non-disappointment: God's affection has been poured out into the interior of us, and the pouring runs through the Holy Spirit.
  · agent: not-stated (implicit God as pourer, via the Holy Spirit as instrument) · operation: shed abroad (pour out — the love of God, in our hearts, by the Holy Spirit) · substrate: the love of God · outcome: God's love poured out in our hearts, mediated through the Holy Spirit · narrator: Paul, first-person epistolary author
  · **edges:** M265 —BEQUEATHS→ RECEPTION

**M266** — Descriptor of that Holy Spirit: he is the one who has been given to us.
  · agent: not-stated (God as giver, implicit) · operation: be given (be handed as gift — the Holy Spirit, to us) · substrate: the Holy Spirit · outcome: the Holy Spirit given as gift to us · narrator: Paul, first-person epistolary author

**M267** — Temporal-state setup for the next move: back when we were still without any strength of our own.
  · agent: we · operation: be (yet without strength — of us, past-state) · substrate: not-stated · outcome: we standing (past) as without strength · narrator: Paul, first-person epistolary author
  · **edges:** M267 —BEQUEATHS→ RECEPTION

**M268** — The main event that happened over against that state: at the rightly-appointed time, Christ died on behalf of the ungodly.
  · agent: Christ · operation: die (on behalf of — the ungodly, at the appointed time) · substrate: not-stated (the ungodly as beneficiaries, folded into outcome) · outcome: Christ dying on behalf of the ungodly, at the appointed time (kata kairon) · narrator: Paul, first-person epistolary author
  · **edges:** M268 —BEQUEATHS→ RECEPTION

**M269** — A comparative human-analogy consideration: even for a person who stands as righteous, someone will barely die.
  · agent: one (anyone, indefinite) · operation: die (for a righteous man — scarcely) · substrate: not-stated (self as sacrificed) · outcome: rare-scarcely dying on behalf of a righteous man · narrator: Paul, first-person epistolary author

**M270** — The concession-side of that observation: it is possible that some might rise even to daring the dying, when it is for a genuinely good person.
  · agent: some · operation: dare (to die — for a good man, hypothetically) · substrate: not-stated (self as sacrificed) · outcome: some possibly daring-to-die on behalf of a good man (hypothetical) · narrator: Paul, first-person epistolary author

**M271** — Sharp contrast: God, meanwhile, actively puts his own love-for-us on display.
  · agent: God · operation: commend (put on display, demonstrate — his love toward us) · substrate: his love (toward us) · outcome: God's love toward us put on demonstrative display · narrator: Paul, first-person epistolary author

**M272** — Temporal-state setup for the demonstration act: at the time when we still stood as offenders.
  · agent: we · operation: be (yet sinners — of us, past-state) · substrate: not-stated · outcome: we standing (past) as still sinners at the time of M11 · narrator: Paul, first-person epistolary author

**M273** — The demonstrating act itself: Christ died for us.
  · agent: Christ · operation: die (on behalf of us) · substrate: not-stated (us as beneficiaries, folded into outcome) · outcome: Christ dying on our behalf, done while we were still sinners · narrator: Paul, first-person epistolary author

**M274** — Given all that, the participial ground for what follows: since we now stand pronounced righteous, and stand so by his blood.
  · agent: not-stated (God as reckoner, implicit) · operation: be justified (be pronounced righteous — by his blood, now) · substrate: we · outcome: we standing now pronounced righteous by Christ's blood · narrator: Paul, first-person epistolary author

**M275** — The a-fortiori conclusion drawn from M12: how much more will we be rescued from wrath, mediated through him.
  · agent: not-stated (God as saver, implicit) · operation: be saved (be rescued — from wrath, through him) · substrate: we · outcome: we (future) to be rescued from wrath, mediated through Christ · narrator: Paul, first-person epistolary author

**M276** — Restating the a-fortiori with sharper past-condition wording: at a time when we stood as enemies.
  · agent: we · operation: be (enemies — of us, past-state) · substrate: not-stated · outcome: we standing (past) as enemies at the time of M15 · narrator: Paul, first-person epistolary author

**M277** — The reconciliation act: we were brought over to God, and this was done through the death of his Son.
  · agent: not-stated (God as reconciler, implicit) · operation: be reconciled (be brought over — to God, through the death of his Son) · substrate: we · outcome: we brought over to God, mediated through the death of his Son · narrator: Paul, first-person epistolary author

**M278** — A-fortiori conclusion parallel to M13: how much more, given that reconciliation is done, will we be rescued — and rescued by his life.
  · agent: not-stated (God as saver, implicit) · operation: be saved (be rescued — by his life, future) · substrate: we · outcome: we (future) to be rescued by Christ's life, given that we stand reconciled · narrator: Paul, first-person epistolary author

**M279** — And beyond even that: we exult in God himself, mediated through our Lord Jesus — [the source cuts off at 'Jesus', before 'Christ' arrives].
  · agent: we · operation: joy (exult, boast — in God, through our Lord Jesus [Christ, truncated]) · substrate: God · outcome: we exulting in God as our substrate of exultation, mediated through our Lord Jesus [Christ, truncated] · narrator: Paul, first-person epistolary author
  · **edges:** M279 —BEQUEATHS→ RECEPTION

**M280** — The trailing word that completes the prior clause: [our Lord Jesus] Christ — through whom we have now taken hold of the reconciliation.
  · agent: we · operation: receive (take hold of — the atonement/reconciliation, now) · substrate: the atonement (the reconciliation, katallagē) · outcome: we having now received the reconciliation, mediated through Christ · narrator: Paul, first-person epistolary author, closing the joy-in-God clause from the prior passage

**M281** — Paul opens the Adam-typology: as through one particular human being, sin came into the world as a newly-present force.
  · agent: sin · operation: enter (come into — the world) · substrate: the world · outcome: sin having entered into the world, mediated through one man · narrator: Paul, first-person epistolary author, pivoting to the Adam-Christ typology

**M282** — Coordinate second entry, with the verb elided from M2: and death [came in] through sin.
  · agent: death · operation: enter (come into — the world, through sin — verb elided from M2) · substrate: not-stated (the world, elided from M2) · outcome: death having entered by way of sin · narrator: Paul, first-person epistolary author

**M283** — And in that way death spread out and came over the whole human population.
  · agent: death · operation: pass upon (spread over — all men) · substrate: all men · outcome: death spreading over all men (universally) · narrator: Paul, first-person epistolary author

**M284** — The ground that makes M4 hold: all humans have done the sinning themselves.
  · agent: all (all humans) · operation: sin (all — have sinned) · substrate: not-stated · outcome: all humans standing as having-sinned · narrator: Paul, first-person epistolary author
  · **edges:** M284 —BEQUEATHS→ RECEPTION

**M285** — Parenthetical clarification: before-law-arrived, sin was already an active presence in the world.
  · agent: sin · operation: be (in the world — of sin, until the law) · substrate: not-stated · outcome: sin standing as present-in-the-world during the pre-law era · narrator: Paul, first-person epistolary author, breaking frame into parenthesis

**M286** — The qualifying principle: when no law is on the scene, sin is not entered into the ledger.
  · agent: not-stated (God as implicit reckoner) · operation: not be imputed (not be reckoned — of sin, absent law) · substrate: sin · outcome: sin not being entered into the ledger under conditions of no-law-present · narrator: Paul, first-person epistolary author

**M287** — The paradoxical persistence: yet death ruled as king across the whole span from Adam through Moses, and its rule extended even over those whose sinning did not match Adam's kind of transgression.
  · agent: death · operation: reign (rule as king — from Adam to Moses, even over non-Adam-style sinners) · substrate: not-stated (its dominion-range) · outcome: death exercising kingship across the Adam-to-Moses span, extending even over those who had not sinned in Adam's transgression-mode · narrator: Paul, first-person epistolary author
  · **edges:** M287 —BEQUEATHS→ RECEPTION

**M288** — Attribution about Adam that pivots into the typology: he stands as the figure of the coming one.
  · agent: who (Adam) · operation: be (the figure — of him that was to come) · substrate: not-stated · outcome: Adam standing as typos of the coming-one (Christ) · narrator: Paul, first-person epistolary author
  · **edges:** M288 —BEQUEATHS→ RECEPTION

**M289** — But — the correspondence is not straight: the gift-side is not held in exactly the same shape as the offence-side.
  · agent: the free gift · operation: be (not-as-the-offence — of the free gift, contrastively) · substrate: not-stated (the comparison-frame with the offence) · outcome: the free gift standing as not-in-the-same-shape as the offence · narrator: Paul, first-person epistolary author

**M290** — The hypothetical setup: suppose that through the one figure's misstep, the many stand dead.
  · agent: many · operation: be dead (die — of many, through the offence of one) · substrate: not-stated · outcome: many standing dead through the offence of one (hypothetically, as ground for the a-fortiori) · narrator: Paul, first-person epistolary author
  · **edges:** M290 —BEQUEATHS→ RECEPTION

**M291** — The a-fortiori consequent: how much more strongly does God's favor, and the gift that runs on that favor, overflow to the many — the mediator here being the one man Jesus Christ.
  · agent: the grace of God, and the gift by grace (mediated by one man, Jesus Christ) · operation: abound (overflow — to many, of God's grace and the gift by grace, through Jesus Christ) · substrate: not-stated (many as recipients, folded into outcome) · outcome: grace and gift overflowing to many, mediated through the one man Jesus Christ · narrator: Paul, first-person epistolary author
  · **edges:** M291 —BEQUEATHS→ RECEPTION

**M292** — A second dissimilarity statement: what happened through one who sinned is not the shape the gift takes either.
  · agent: the gift · operation: be (not-as-by-one-who-sinned — so the gift, contrastively) · substrate: not-stated (comparison-frame with what came by one-who-sinned) · outcome: the gift standing as not-in-the-same-shape as what came by one-who-sinned · narrator: Paul, first-person epistolary author

**M293** — The reason for that dissimilarity, judgment-side: the verdict, taking its origin from one, ran toward condemnation.
  · agent: the judgment · operation: be (the judgment — by one, to condemnation) · substrate: not-stated · outcome: the judgment standing as originating from one and terminating in condemnation · narrator: Paul, first-person epistolary author
  · **edges:** M293 —BEQUEATHS→ RECEPTION

**M294** — The contrast, gift-side: but the free gift takes its origin from [many offences — the source cuts off before the terminus (unto justification) arrives].
  · agent: the free gift · operation: be (the free gift — of [many offences unto justification, truncated]) · substrate: not-stated · outcome: the free gift standing as originating from [many offences] and terminating in [justification] — the specific terminus arrives beyond the source-cutoff · narrator: Paul, first-person epistolary author
  · **edges:** M294 —BEQUEATHS→ RECEPTION

**M295** — Completing the prior contrast: [the free gift originates] from many offences and terminates in a righteousness-verdict.
  · agent: the free gift (from the prior passage) · operation: be (the free gift — of many offences unto justification, completion) · substrate: many offences (as origin) — unto justification (as terminus) · outcome: the free gift standing as originating from many offences and terminating in a righteousness-verdict (dikaiōma) · narrator: Paul, first-person epistolary author, closing the Adam-Christ contrast opened in the prior passage

**M296** — The hypothetical setup: suppose that through the one figure's misstep, death took kingship — and did so by way of that one.
  · agent: death · operation: reign (rule as king — through one man's offence, by one) · substrate: not-stated (its dominion-range) · outcome: death (hypothetically) exercising kingship through one man's offence, mediated by that one · narrator: Paul, first-person epistolary author
  · **edges:** M296 —BEQUEATHS→ RECEPTION

**M297** — Descriptor of the a-fortiori subject: those persons who take onto themselves an over-and-above measure of favor along with the gift that is righteousness.
  · agent: they (the a-fortiori subject cohort) · operation: receive (take onto themselves — abundance of grace and of the gift of righteousness) · substrate: abundance of grace, and of the gift of righteousness · outcome: the cohort standing as receivers of grace-abundance and the gift-of-righteousness · narrator: Paul, first-person epistolary author
  · **edges:** M297 —BEQUEATHS→ RECEPTION

**M298** — The a-fortiori consequent: how much more will those receivers themselves take up kingship in life — and take it up through one, namely Jesus Christ.
  · agent: they (the M3 cohort) · operation: reign (rule as king — in life, by one, Jesus Christ) · substrate: not-stated (life as domain of their reign) · outcome: the receivers exercising kingship in life, mediated through the one — Jesus Christ · narrator: Paul, first-person epistolary author
  · **edges:** M298 —BEQUEATHS→ RECEPTION

**M299** — Restating the comparison, Adam-side: as through the misstep of the one, a verdict came upon the whole human population, and it ran to condemnation.
  · agent: judgment · operation: come upon (arrive on — all men, through the offence of one, to condemnation) · substrate: all men · outcome: judgment arriving upon all men, originating from one's offence and terminating in condemnation · narrator: Paul, first-person epistolary author
  · **edges:** M299 —BEQUEATHS→ RECEPTION

**M300** — The parallel Christ-side of the comparison: in the same way, through the righteousness of the one, the gift came upon the whole population, and it ran to a life-shaped righteousness-verdict.
  · agent: the free gift · operation: come upon (arrive on — all men, through the righteousness of one, unto justification of life) · substrate: all men · outcome: the free gift arriving upon all men, originating from one's righteousness and terminating in justification-of-life · narrator: Paul, first-person epistolary author
  · **edges:** M300 —BEQUEATHS→ RECEPTION

**M301** — A further restatement of the Adam-side, now in constituting-terms: as through the not-listening of the one human being, many were placed into the standing of sinners.
  · agent: not-stated (the implicit constituting force — Adam's disobedience acting through/on the many) · operation: be made (be constituted — sinners, through one man's disobedience) · substrate: many · outcome: many constituted sinners, mediated through the one man's disobedience · narrator: Paul, first-person epistolary author
  · **edges:** M301 —BEQUEATHS→ RECEPTION

**M302** — The parallel Christ-side, still in constituting-terms: in the same way, through the listening-obedience of the one, many will be placed into the standing of righteous.
  · agent: not-stated (the implicit constituting force — Christ's obedience acting on the many) · operation: be made (be constituted — righteous, through the obedience of one, future) · substrate: many · outcome: many (future) constituted righteous, mediated through the obedience of one · narrator: Paul, first-person epistolary author
  · **edges:** M302 —BEQUEATHS→ RECEPTION

**M303** — Paul introduces the law's part in this story: the law came alongside as a second entry.
  · agent: the law · operation: enter (come alongside — of the law) · substrate: not-stated (its entry-into the scene) · outcome: the law having entered alongside (parenteisēlthen — as a secondary or paralleling entry) · narrator: Paul, first-person epistolary author

**M304** — The intended-effect of that law-entry: that the misstep might become overflowingly plentiful.
  · agent: the offence · operation: abound (become plentiful — of the offence, as purpose) · substrate: not-stated · outcome: the offence becoming plentiful (as intended-effect of the law's entry) · narrator: Paul, first-person epistolary author

**M305** — The paradoxical turn: at the very location where sin became plentiful.
  · agent: sin · operation: abound (become plentiful — of sin) · substrate: not-stated · outcome: sin having become plentiful (as the location-condition for M12) · narrator: Paul, first-person epistolary author

**M306** — The paradoxical apodosis: at that same site, favor went overwhelmingly beyond that plentiful measure.
  · agent: grace · operation: much more abound (super-abound, hyper-exceed — of grace) · substrate: not-stated · outcome: grace hyper-abounding, exceeding the M11 sin-abundance · narrator: Paul, first-person epistolary author
  · **edges:** M306 —BEQUEATHS→ RECEPTION

**M307** — The purpose that governs both dominions, first side: just as sin has held kingship, and its kingship ran toward death.
  · agent: sin · operation: reign (rule as king — of sin, unto death) · substrate: not-stated (its dominion) · outcome: sin having exercised kingship, terminating in death · narrator: Paul, first-person epistolary author

**M308** — The parallel purpose, second side: so also might favor exercise kingship — running through righteousness, terminating in the age-to-come life, mediated by Jesus Christ our Lord.
  · agent: grace · operation: reign (rule as king — of grace, through righteousness, unto eternal life, by Jesus Christ our Lord) · substrate: not-stated (its dominion) · outcome: grace exercising kingship, mediated through righteousness, terminating in eternal life, through Jesus Christ our Lord · narrator: Paul, first-person epistolary author

**M309** — Paul opens ch 6 with a diatribal deliberation-question: what conclusion are we to draw from all of that?
  · agent: we (Paul with the imagined interlocutor) · operation: say (deliberatively — what shall we say?) · substrate: not-stated (the emerging conclusion) · outcome: the conclusion opened for question · narrator: Paul, first-person epistolary author, opening the ch 6 diatribe

**M310** — The proposed conclusion that Paul sets up to demolish: are we to remain within sin, in order that [favor might overflow — the purpose-clause is cut off at 'grace' before the verb arrives].
  · agent: we · operation: continue (remain — in sin, interrogatively, that grace [may abound — truncated]) · substrate: sin · outcome: we (interrogatively) remaining within sin, with the purpose-clause 'that grace [may abound]' opened but truncated · narrator: Paul, first-person epistolary author
  · **edges:** M310 —BEQUEATHS→ RECEPTION

**M311** — Completing the prior rhetorical question's purpose-tail: [so that favor] might overflow?
  · agent: grace · operation: abound (become plentiful — of grace, as purpose) · substrate: not-stated · outcome: grace's abounding held out as the (proposed) purpose of remaining-in-sin · narrator: Paul, first-person epistolary author, closing the diatribal question from the prior passage

**M312** — Paul denies flatly: absolutely not — may it not come to that.
  · agent: not-stated (Paul himself as speaker) · operation: may-it-not-be (emphatically deny) · substrate: the proposed M1 purpose (continuing in sin so grace may abound) · outcome: the M1 possibility emphatically denied · narrator: Paul, first-person epistolary author

**M313** — Descriptor of the addressees: we stand in the condition of having died to sin.
  · agent: we · operation: be dead (be in a state of death — to sin) · substrate: sin (as the sphere to which we have died) · outcome: we standing in the condition of having died with respect to sin · narrator: Paul, first-person epistolary author
  · **edges:** M313 —BEQUEATHS→ RECEPTION

**M314** — The corresponding rhetorical question: how could we still keep going on living within sin?
  · agent: we · operation: live (still — in sin, interrogatively) · substrate: sin (the sphere) · outcome: we put under an impossibility-question about further living-within-sin · narrator: Paul, first-person epistolary author
  · **edges:** M314 —BEQUEATHS→ RECEPTION

**M315** — Paul appeals to what the addressees ought already to know: don't you have cognitive hold of the following fact?
  · agent: ye (the addressees) · operation: know (interrogatively — with recoverable content) · substrate: the content of the knowing (M5a and M5b) · outcome: the addressees challenged to recognize the M5a-M5b content · narrator: Paul, first-person epistolary author
  · **edges:** M315 —CONTAINS→ M316; M315 —REPORTS→ M317

**M316** — First half of the recoverable content: those of us who underwent baptism did so into Christ Jesus.
  · agent: not-stated (the baptizer as implicit agent, ecclesial or divine) · operation: be baptized (be immersed — into Jesus Christ) · substrate: so many of us as (the baptized cohort) · outcome: the cohort baptized into Jesus Christ (immersed into his person as the sphere) · narrator: Paul, first-person epistolary author, ventriloquizing the shared baptismal knowledge
  · **edges:** M316 —BEQUEATHS→ RECEPTION; ["M315"] —CONTAINS→ M316

**M317** — Second half of the content — the main claim: that same immersion was also an immersion into his death.
  · agent: not-stated · operation: be baptized (be immersed — into his death) · substrate: we (the baptized cohort from M5a) · outcome: we baptized into Christ's death (immersed into the death-event as the sphere) · narrator: Paul, first-person epistolary author, ventriloquizing the shared baptismal knowledge
  · **edges:** M317 —BEQUEATHS→ RECEPTION; ["M315"] —REPORTS→ M317

**M318** — Drawing the inference from M5b: we accordingly stand co-buried with him — the burial-medium being baptism, and the terminus being death.
  · agent: not-stated (God as the implicit co-burying agent, or the ritual as agent) · operation: be buried with (be co-buried — with him, by baptism, into death) · substrate: we · outcome: we standing co-buried with Christ, by baptism, into death · narrator: Paul, first-person epistolary author
  · **edges:** M318 —BEQUEATHS→ RECEPTION

**M319** — The purpose-comparison first half: just as Christ was lifted up from the dead — and lifted up by the Father's glory.
  · agent: not-stated (God as raiser, mediated through the glory of the Father) · operation: be raised up (be lifted — from the dead, by the glory of the Father) · substrate: Christ · outcome: Christ lifted up from the dead, by the glory of the Father · narrator: Paul, first-person epistolary author

**M320** — The corresponding second half of the purpose-comparison: so also we, for our part, should walk our path in a newness that belongs to life.
  · agent: we · operation: walk (take steps — in newness of life) · substrate: not-stated (the walk-mode itself) · outcome: we walking in the newness that belongs to life (as intended-purpose-outcome of the M6-M7 configuration) · narrator: Paul, first-person epistolary author

**M321** — The conditional restatement: suppose we have been grafted-together with him — grafted, that is, in a form-and-manner that matches his death.
  · agent: not-stated (God as the implicit co-grafting agent) · operation: be planted together (be grafted-together — in the likeness of his death) · substrate: we · outcome: we (hypothetically) grafted together with Christ in the form-and-manner of his death · narrator: Paul, first-person epistolary author
  · **edges:** M321 —BEQUEATHS→ RECEPTION

**M322** — The consequent that follows: then we will likewise stand in a form-and-manner that matches his resurrection.
  · agent: not-stated (the same implicit co-grafting agent, from M9) · operation: be (also — in the likeness of his resurrection, future) · substrate: we · outcome: we (future) grafted together with Christ in the form-and-manner of his resurrection · narrator: Paul, first-person epistolary author
  · **edges:** M322 —BEQUEATHS→ RECEPTION

**M323** — The knowing-participle undergirding all this: we have cognitive hold of the following.
  · agent: we (implied from the M11a subject) · operation: know (with recoverable content) · substrate: the content of the knowing (M11a) · outcome: we standing as ones who know the M11a content · narrator: Paul, first-person epistolary author
  · **edges:** M323 —REPORTS→ M324

**M324** — The recoverable content: our old-humanity self has been crucified together with him.
  · agent: not-stated (the implicit divine or event-agent of the crucifixion) · operation: be crucified with (be co-crucified — of our old man, with him) · substrate: our old man (ho palaios anthropos hēmōn) · outcome: the old-humanity self co-crucified with Christ · narrator: Paul, first-person epistolary author, ventriloquizing the recognized content
  · **edges:** M324 —BEQUEATHS→ RECEPTION; ["M323"] —REPORTS→ M324

**M325** — First purpose of that co-crucifixion: that the sin-shaped body might be brought to nothing.
  · agent: not-stated (the implicit divine or event-agent) · operation: be destroyed (be brought to nothing — of the body of sin, as purpose) · substrate: the body of sin · outcome: the body of sin brought to nothing (as intended-effect of M11a) · narrator: Paul, first-person epistolary author

**M326** — Second purpose: that we, from this point on, no longer function as slave to sin.
  · agent: we · operation: not serve (not be enslaved to — sin, henceforth) · substrate: sin · outcome: we (henceforth) not enslaved to sin · narrator: Paul, first-person epistolary author

**M327** — New conditional restatement: suppose we have died together with Christ.
  · agent: not-stated (the implicit co-dying event) · operation: be dead with (be co-dead — with Christ, hypothetically) · substrate: we · outcome: we (hypothetically) standing dead together with Christ · narrator: Paul, first-person epistolary author

**M328** — The consequent: we hold as our conviction that we will also live together with him.
  · agent: we · operation: believe (hold as settled conviction — with recoverable content) · substrate: the content of the belief (M15a) · outcome: we standing as ones who hold M15a as settled conviction · narrator: Paul, first-person epistolary author
  · **edges:** M328 —BEQUEATHS→ RECEPTION; M328 —REPORTS→ M329

**M329** — The content of the belief: that we too will live together with him.
  · agent: we · operation: live with (co-live — with him, future) · substrate: him (Christ) · outcome: we (future) living together with Christ · narrator: Paul, first-person epistolary author, ventriloquizing the belief-content
  · **edges:** ["M328"] —REPORTS→ M329

**M330** — The further knowing-participle: we have cognitive hold of this next fact.
  · agent: we (implied from the M16a subject) · operation: know (with recoverable content) · substrate: the content of the knowing (M16a) · outcome: we standing as ones who know the M16a content · narrator: Paul, first-person epistolary author
  · **edges:** M330 —REPORTS→ M331

**M331** — The content of that knowing: Christ, standing now as the one who has been lifted from the dead, dies no more — [the source cuts off before 'death has no more dominion over him' arrives].
  · agent: Christ (characterized as 'being raised from the dead') · operation: die no more (never-die-again — of Christ, once raised) · substrate: not-stated · outcome: Christ standing as one who never dies again — with the parallel 'death has no more dominion over him' truncated in the source · narrator: Paul, first-person epistolary author, ventriloquizing the knowing-content
  · **edges:** M331 —BEQUEATHS→ RECEPTION; ["M330"] —REPORTS→ M331

**M332** — Completing the prior parallel-clause: death has no continuing mastery over him.
  · agent: death · operation: have dominion (exercise mastery — over him, of death, no more) · substrate: him (Christ) · outcome: death no longer exercising mastery over Christ · narrator: Paul, first-person epistolary author, closing the parallel-clause from the prior passage
  · **edges:** M332 —BEQUEATHS→ RECEPTION

**M333** — Paul unpacks Christ's death-side: when he died, that dying was one-time-and-for-all, and it was a dying with respect to sin.
  · agent: he (Christ) · operation: die (unto sin, once — for all) · substrate: sin (as the sphere with respect to which he died) · outcome: Christ having died once-for-all with respect to sin · narrator: Paul, first-person epistolary author
  · **edges:** M333 —BEQUEATHS→ RECEPTION

**M334** — The paired life-side: when he lives, that living is a living with respect to God.
  · agent: he (Christ) · operation: live (unto God) · substrate: God (as the sphere with respect to which he lives) · outcome: Christ living with respect to God · narrator: Paul, first-person epistolary author
  · **edges:** M334 —BEQUEATHS→ RECEPTION

**M335** — Directive to the addressees: in the same way, do the reckoning on yourselves — enter yourselves into the ledger as [content].
  · agent: ye (the addressees) · operation: reckon (imperative — with recoverable content) · substrate: the content of the reckoning (M4a and M4b) · outcome: the addressees directed to reckon themselves under the M4a-M4b two-side attribution · narrator: Paul, first-person epistolary author
  · **edges:** M335 —BEQUEATHS→ RECEPTION; M335 —CONTAINS→ M337; M335 —REPORTS→ M336

**M336** — First side of the reckoning-content: that you yourselves stand as dead with respect to sin.
  · agent: yourselves (the addressees) · operation: be dead (with respect to sin — of the addressees) · substrate: sin · outcome: the addressees standing dead with respect to sin · narrator: Paul, first-person epistolary author, ventriloquizing the reckoning-content
  · **edges:** M336 —BEQUEATHS→ RECEPTION; ["M335"] —REPORTS→ M336

**M337** — Second side of the reckoning-content: but at the same time, alive with respect to God — and alive through Jesus Christ our Lord.
  · agent: yourselves (the addressees) · operation: be alive (with respect to God — through Jesus Christ our Lord) · substrate: God (as sphere) · outcome: the addressees standing alive with respect to God, mediated through Christ · narrator: Paul, first-person epistolary author, ventriloquizing the reckoning-content
  · **edges:** ["M335"] —CONTAINS→ M337

**M338** — Behavioral directive: do not permit sin to take up kingship inside your death-liable body.
  · agent: sin · operation: reign (rule as king — of sin, in your mortal body, jussive-negated) · substrate: not-stated (its dominion-space, folded into 'in your mortal body') · outcome: sin directed not to exercise kingship in the addressees' mortal body · narrator: Paul, first-person epistolary author

**M339** — The intended-consequence of sin's would-be reign: that you should end up obeying it, and doing so on the ground of its cravings.
  · agent: ye (the addressees) · operation: obey (comply with — sin, in the lusts thereof) · substrate: it (sin, via its lusts) · outcome: the addressees (would be) obeying sin under the direction of its lusts, if M5 were allowed · narrator: Paul, first-person epistolary author

**M340** — Second behavioral directive, negative side: do not go on handing over your body-parts to sin as tools by which unrighteousness gets done.
  · agent: ye · operation: yield (present, hand over — your members as instruments of unrighteousness unto sin, imperative-negated) · substrate: your members · outcome: the addressees directed to withhold their members from being presented to sin as unrighteousness-tools · narrator: Paul, first-person epistolary author

**M341** — The positive counterpart: rather, hand yourselves over to God — and hand yourselves as ones who have crossed over from death to life.
  · agent: ye · operation: yield (present, hand over — yourselves unto God, as those alive from the dead) · substrate: yourselves · outcome: the addressees directed to present themselves to God as those alive from the dead · narrator: Paul, first-person epistolary author

**M342** — And in parallel: hand over your body-parts to God as tools by which righteousness gets done.
  · agent: ye · operation: yield (present, hand over — your members as instruments of righteousness unto God) · substrate: your members · outcome: the addressees directed to present their members to God as righteousness-tools · narrator: Paul, first-person epistolary author

**M343** — The promise/ground under the imperatives: sin will not exercise mastery over you.
  · agent: sin · operation: have dominion (exercise mastery — over you, of sin, future-negated) · substrate: you · outcome: sin (future) not exercising mastery over the addressees · narrator: Paul, first-person epistolary author

**M344** — The reason for that promise: you don't stand located under the law's regime — you stand located under favor's regime.
  · agent: ye · operation: be (not under the law, but under grace — of the addressees, as location) · substrate: not-stated (your-regime-of-standing) · outcome: the addressees standing not under law but under grace · narrator: Paul, first-person epistolary author

**M345** — Paul poses the next rhetorical trap: what then? are we to commit sin on the ground that we stand under grace's regime rather than the law's?
  · agent: we · operation: sin (interrogatively — because we are under grace, not law) · substrate: not-stated · outcome: the antinomian conclusion opened for question · narrator: Paul, first-person epistolary author

**M346** — Paul dismisses it flatly: absolutely not.
  · agent: not-stated (Paul himself as speaker) · operation: may-it-not-be (emphatically deny) · substrate: the M12 possibility · outcome: the M12 possibility emphatically denied · narrator: Paul, first-person epistolary author

**M347** — Paul appeals again to what the addressees ought already to recognize: don't you have cognitive hold of the following principle?
  · agent: ye (the addressees) · operation: know (interrogatively — with recoverable content, truncated) · substrate: the content of the knowing (M14a) · outcome: the addressees challenged to recognize the principle whose statement M14a begins · narrator: Paul, first-person epistolary author
  · **edges:** M347 —REPORTS→ M348

**M348** — The content of what the addressees ought to know — the principle begins: that to whichever party you hand yourselves over as slaves for [obeying — the source cuts off before the terminus of the principle arrives].
  · agent: ye · operation: yield (present yourselves — as servants, to whom [to obey, truncated]) · substrate: yourselves (as offered slaves) · outcome: the addressees presenting themselves as slaves to whichever party they hand over to — with the completing principle-statement ('to whom you obey, his slaves you are') truncated in the source · narrator: Paul, first-person epistolary author, ventriloquizing the principle-content
  · **edges:** ["M347"] —REPORTS→ M348

**M349** — Completing the principle-content from the prior passage: the party you obey is the party whose slaves you actually are.
  · agent: ye · operation: be (his servants — of the one to whom you obey, principle-completion) · substrate: not-stated · outcome: the addressees standing as servants of whichever party they obey · narrator: Paul, first-person epistolary author, closing the ouk-oidate-hoti principle from the prior passage
  · **edges:** M349 —BEQUEATHS→ RECEPTION

**M350** — The bilateral scope-specification of that principle: whether the master you obey is sin (whose end-terminus is death) or obedience (whose end-terminus is righteousness).
  · agent: ye · operation: be (servants — of either sin unto death, or of obedience unto righteousness — scope-specification) · substrate: either sin (leading to death) or obedience (leading to righteousness) · outcome: the M1 slave-standing specified as running along one of two paths: sin→death or obedience→righteousness · narrator: Paul, first-person epistolary author

**M351** — Paul offers thanks to God — thanks whose specific ground follows.
  · agent: not-stated (Paul as speaker, formula-form) · operation: thank (be given thanks — of God, with recoverable content) · substrate: the content of the thanks (M4 and M5) · outcome: thanks rendered to God for the M4→M5 transition · narrator: Paul, first-person epistolary author
  · **edges:** M351 —BEQUEATHS→ RECEPTION; M351 —CONTAINS→ M353; M351 —REPORTS→ M352

**M352** — First part of the thanksgiving-content: that you used to be slaves belonging to sin.
  · agent: ye · operation: be (servants of sin — past-state) · substrate: sin (as master) · outcome: the addressees standing (past) as sin's servants · narrator: Paul, first-person epistolary author, ventriloquizing the thanksgiving-content
  · **edges:** M352 —BEQUEATHS→ RECEPTION; ["M351"] —REPORTS→ M352

**M353** — The transition-side of the thanksgiving-content: but you gave over your obedience — from a heart-level place — to that pattern of teaching that was handed on to you.
  · agent: ye · operation: obey (comply — from the heart, that form of doctrine) · substrate: that form of doctrine (typos didachēs) · outcome: the addressees having complied — from the heart — with the delivered form-of-doctrine · narrator: Paul, first-person epistolary author, ventriloquizing the transition-side of the thanksgiving
  · **edges:** ["M351"] —CONTAINS→ M353

**M354** — Descriptor of that pattern-of-teaching: it was passed on to you.
  · agent: not-stated (the handers-on, ecclesial/catechetical) · operation: be delivered (be handed on — that form of doctrine, to you) · substrate: that form of doctrine · outcome: the doctrinal pattern handed on to the addressees · narrator: Paul, first-person epistolary author

**M355** — The participial ground for M8: since you had been released from sin's ownership.
  · agent: not-stated (the implicit divine or event-agent of the release) · operation: be made free (be released — from sin) · substrate: ye · outcome: the addressees released from sin's ownership · narrator: Paul, first-person epistolary author

**M356** — The main-verb outcome: you came into a new servitude — you became slaves belonging to righteousness.
  · agent: not-stated (the implicit divine or event-agent of the transfer) · operation: become (be made — servants of righteousness) · substrate: ye · outcome: the addressees transferred into slavery-to-righteousness · narrator: Paul, first-person epistolary author

**M357** — Paul flags the register of the argument: he is speaking in human-fashion, and doing so on account of the weakness that belongs to their flesh.
  · agent: I (Paul) · operation: speak (in human-manner — because of the infirmity of your flesh) · substrate: not-stated (this current mode of speech — the slave-metaphor argument) · outcome: Paul's argument marked as spoken in human-manner because of the addressees' flesh-weakness · narrator: Paul, first-person epistolary author, breaking frame to qualify his own metaphor-use

**M358** — The comparison first half: for just as you presented your body-parts as slaves at the disposal of impurity and lawlessness — and did so unto ever-more lawlessness.
  · agent: ye · operation: yield (present, hand over — your members as servants to uncleanness and to iniquity, unto iniquity) · substrate: your members · outcome: the addressees having presented their members as slaves to uncleanness and iniquity, terminating in iniquity · narrator: Paul, first-person epistolary author

**M359** — The comparison second half — as a directive: in exactly the same way, right now, present your body-parts as slaves at the disposal of righteousness — and do so unto holiness.
  · agent: ye · operation: yield (present, hand over — your members as servants to righteousness, unto holiness, imperative) · substrate: your members · outcome: the addressees directed to present their members as slaves to righteousness, terminating in holiness · narrator: Paul, first-person epistolary author

**M360** — Temporal-state descriptor of the past-condition: at the time when you were slaves belonging to sin.
  · agent: ye · operation: be (servants of sin — past-temporal-state) · substrate: sin (as master) · outcome: the addressees standing (past) as sin's servants · narrator: Paul, first-person epistolary author

**M361** — The paradoxical corollary of that past-state: in that condition, you stood free — free from righteousness's claim.
  · agent: ye · operation: be (free from righteousness — past-state) · substrate: righteousness (as the sphere from which they were free) · outcome: the addressees standing (past) free from righteousness's claim · narrator: Paul, first-person epistolary author

**M362** — Paul poses the honest question about the yield of that past-condition: what harvest did you actually reap back then from those things?
  · agent: ye · operation: have (harvest, produce — fruit, in those things, interrogatively) · substrate: not-stated (the fruit-yield) · outcome: the past-fruit put in question (with the implied answer: none of any worth) · narrator: Paul, first-person epistolary author

**M363** — Descriptor of the those-things in question: they are the very things you are now feeling shame over.
  · agent: ye · operation: be ashamed (feel shame — of those things, now) · substrate: those things (the M14 past-substrate) · outcome: the addressees standing now as ones ashamed of those past-things · narrator: Paul, first-person epistolary author

**M364** — The ground for the M15 shame: those things' terminus is death.
  · agent: the end of those things (as substrate of the terminus-attribution) · operation: be (the end / terminus — of those things, death) · substrate: not-stated · outcome: those things' terminus standing as death · narrator: Paul, first-person epistolary author

**M365** — But contrast the present: since you now stand released from sin's ownership.
  · agent: not-stated (the implicit releaser) · operation: be made free (be released — from sin, present-state) · substrate: ye · outcome: the addressees standing now released from sin's ownership · narrator: Paul, first-person epistolary author

**M366** — And the paired present-state — enslaved to God — [the main-verb outcome about your present fruit and its terminus in eternal life is cut off in the source].
  · agent: not-stated (the implicit divine transfer-agent) · operation: become (be made — servants to God, present-state) · substrate: ye · outcome: the addressees standing now as servants of God — with the main-clause about the present-fruit and its holiness-and-eternal-life terminus truncated in the source · narrator: Paul, first-person epistolary author

**M367** — Completing the main-clause outcome from the prior passage: you have the harvest you now carry, and that harvest runs toward holiness.
  · agent: ye · operation: have (harvest — your fruit unto holiness) · substrate: your fruit · outcome: the addressees possessing fruit that runs toward holiness · narrator: Paul, first-person epistolary author, closing the M17-M18-prior participial-grounds

**M368** — And the terminus of that harvest: an eternal-and-ongoing life.
  · agent: the end (of the M1 fruit) · operation: be (the end — everlasting life) · substrate: not-stated · outcome: the terminus of the M1 fruit standing as everlasting life · narrator: Paul, first-person epistolary author

**M369** — The soldier-pay side of the picture: what sin pays out as wages is death.
  · agent: the wages of sin · operation: be (the wages of sin — death) · substrate: not-stated · outcome: sin's wages standing as death · narrator: Paul, first-person epistolary author

**M370** — The contrasting gift-side: what God gives — as gift, not as wages — is life for the age-to-come, mediated through our Lord Jesus Christ.
  · agent: the gift of God · operation: be (the gift of God — eternal life through Jesus Christ our Lord) · substrate: not-stated · outcome: God's gift standing as eternal life, mediated through our Lord Jesus Christ · narrator: Paul, first-person epistolary author
  · **edges:** M370 —BEQUEATHS→ RECEPTION

**M371** — Paul opens the ch 7 argument with an appeal to shared knowledge: don't you already have cognitive hold of the following principle, brothers?
  · agent: ye (brethren, the addressees) · operation: know (interrogatively — with recoverable content) · substrate: the content of the knowing (M5a) · outcome: the addressees challenged to recognize the M5a principle · narrator: Paul, first-person epistolary author
  · **edges:** M371 —REPORTS→ M372

**M372** — The content of that knowing — the general principle: the law exercises mastery over a person for as long as that person keeps living.
  · agent: the law · operation: have dominion (exercise mastery — over a man, as long as he liveth) · substrate: a man (as long as he liveth) · outcome: the law exercising mastery over a person during that person's lifetime · narrator: Paul, first-person epistolary author, ventriloquizing the shared knowledge
  · **edges:** ["M371"] —REPORTS→ M372

**M373** — Parenthetical marker of who the audience is: Paul explains he is addressing those who have cognitive hold of the law.
  · agent: I (Paul) · operation: speak (address — to them that know the law) · substrate: them that know the law (the specified audience) · outcome: Paul's argument addressed to the law-knowing subset of the audience · narrator: Paul, first-person epistolary author, breaking frame into parenthesis

**M374** — Descriptor for the marriage-analogy subject: the wife stands as a woman who has a husband.
  · agent: the woman · operation: have (a husband — of the woman) · substrate: a husband · outcome: the woman standing as one who has a husband · narrator: Paul, first-person epistolary author

**M375** — The legal-binding attribution: that woman is held bound, by the law, to her husband — bound for the whole duration of his life.
  · agent: not-stated (the law as binding force) · operation: be bound (be legally-held — to her husband, by the law, so long as he liveth) · substrate: the woman · outcome: the wife legally-held to her husband during the whole span of his life · narrator: Paul, first-person epistolary author

**M376** — First conditional-state clause: if the husband, on the other hand, is in the state of having died.
  · agent: the husband · operation: be dead (be in the state of having died — of the husband, first conditional) · substrate: not-stated · outcome: the husband standing (hypothetically) as having died · narrator: Paul, first-person epistolary author
  · **edges:** M376 —BEQUEATHS→ RECEPTION

**M377** — The consequent: she has been released from the law that bound her to her husband.
  · agent: not-stated (the husband's death as releasing event) · operation: be loosed (be released — from the law of her husband) · substrate: she (the wife) · outcome: the wife released from the law that had bound her to her husband · narrator: Paul, first-person epistolary author
  · **edges:** M377 —BEQUEATHS→ RECEPTION

**M378** — Second conditional, first-state clause: while the husband is in the ongoing state of being alive.
  · agent: her husband · operation: be alive (be in the state of living — of the husband, second conditional-state) · substrate: not-stated · outcome: the husband standing (in the conditional) as still living · narrator: Paul, first-person epistolary author

**M379** — Second conditional, act-clause: if she should get married to a different man during that time.
  · agent: not-stated (the marriage-event/officiator) · operation: be married (be joined in marriage — to another man) · substrate: she (the wife) · outcome: the wife (hypothetically) married to a different man while her husband still lives · narrator: Paul, first-person epistolary author

**M380** — The verdict-consequent: she will get named 'adulteress'.
  · agent: not-stated (the naming-community, socio-legal) · operation: be called (be named, receive verdict-name — an adulteress) · substrate: she (the wife) · outcome: the wife (future) receiving the verdict-name of adulteress, as consequent of M11 (husband alive) plus M12 (remarriage) · narrator: Paul, first-person epistolary author

**M381** — Third conditional-state clause (parallel to M9): but if instead her husband is in the state of having died.
  · agent: her husband · operation: be dead (be in the state of having died — of the husband, second conditional-instance) · substrate: not-stated · outcome: the husband standing (hypothetically) as having died — reprised for the M15-M17 case · narrator: Paul, first-person epistolary author

**M382** — The consequent for that death-condition: she stands free from that particular law.
  · agent: she (the wife) · operation: be (free — from that law) · substrate: that law (the husband-law) · outcome: the wife standing free from the husband-law once he has died · narrator: Paul, first-person epistolary author

**M383** — The further consequent: with the result that she is not an adulteress.
  · agent: she (the wife) · operation: be (no adulteress — of the wife) · substrate: not-stated · outcome: the wife standing as no-adulteress (the M13 verdict-name negated) · narrator: Paul, first-person epistolary author

**M384** — The concessive-condition: even in the case where she is married to a different man.
  · agent: not-stated (the marriage-event) · operation: be married (be joined in marriage — to another man, concessive) · substrate: she (the wife) · outcome: the wife married to a different man — a marriage-condition that under M14's death-state does not incur the M13 verdict · narrator: Paul, first-person epistolary author

**M385** — Paul draws the application, using the kinship-address 'my brothers': you also, in the same way, have come into the state of being dead with respect to the law — the mediating means being [the body of Christ, truncated in the source].
  · agent: not-stated (the implicit divine or event-agent, mediated through the truncated 'by the body of Christ') · operation: become (be made — dead to the law, by [the body of Christ, truncated]) · substrate: ye (the addressees, my brethren) · outcome: the addressees standing dead with respect to the law, mediated through [the body of Christ, truncated] — the M9/M14 death-transition applied to the addressees on the law-side rather than the husband-side · narrator: Paul, first-person epistolary author, drawing the application from marriage-analogy to law-relation

**M386** — Completing the mediating instrument from the prior clause: [by way of] the body of Christ.
  · agent: not-stated (the implicit transfer-agent from M18-prior) · operation: (mediating substrate arrives — the body of Christ, as the by-what of the M18-prior dying-to-the-law) · substrate: the body of Christ · outcome: the addressees' dying-to-the-law mediated through the body of Christ · narrator: Paul, first-person epistolary author, closing the mediation-clause from the prior passage
  · **edges:** M386 —BEQUEATHS→ RECEPTION

**M387** — First purpose of that dying-to-the-law: that you should be joined-in-marriage to a different party.
  · agent: not-stated (the implicit joining-agent) · operation: be married (be joined in marriage — to another) · substrate: ye · outcome: the addressees joined in marriage to a different party (than the law-husband) · narrator: Paul, first-person epistolary author

**M388** — Descriptor of that other-party you are being joined to: he is the one who was lifted from among the dead.
  · agent: not-stated (God as the implicit raiser) · operation: be raised (be lifted — from the dead, of the joined-to party) · substrate: him (the joined-to party, Christ) · outcome: the joined-to party (Christ) standing as one raised from the dead · narrator: Paul, first-person epistolary author

**M389** — Further purpose held out over the whole configuration: that we might yield up harvest for God.
  · agent: we · operation: bring forth (yield — fruit unto God) · substrate: fruit · outcome: we bringing forth fruit that runs toward God · narrator: Paul, first-person epistolary author

**M390** — Temporal-state setup for the contrast: back at the time when we were located in the flesh.
  · agent: we · operation: be (in the flesh — past-state) · substrate: not-stated · outcome: we standing (past) as located in the flesh · narrator: Paul, first-person epistolary author

**M391** — The main-clause happening in that past-state: the sin-impulses actively worked inside our body-parts.
  · agent: the motions of sins · operation: work (be active — in our members) · substrate: our members (as the space where the impulses operate) · outcome: sin-impulses actively working in the addressees' members · narrator: Paul, first-person epistolary author

**M392** — Descriptor of those sin-impulses: they came into operation by way of the law.
  · agent: the motions of sins (from M6) · operation: be (by the law — of the sin-impulses) · substrate: not-stated · outcome: the sin-impulses standing as arising by way of the law · narrator: Paul, first-person epistolary author

**M393** — The purpose-outcome of that sin-impulses-at-work: to yield up harvest that runs toward death.
  · agent: not-stated (the sin-impulses as force, via the members as instrumentality) · operation: bring forth (yield — fruit unto death, purpose) · substrate: fruit (as what is brought forth) · outcome: fruit brought forth that runs toward death — the outcome of the M6 sin-impulses-at-work · narrator: Paul, first-person epistolary author

**M394** — The now-turn: at the present moment, we stand released from the law.
  · agent: not-stated (the implicit divine or event-agent of the release) · operation: be delivered (be released — from the law, now) · substrate: we · outcome: the addressees standing now released from the law · narrator: Paul, first-person epistolary author

**M395** — The participial-ground for the release: having died to that in which we were previously held.
  · agent: we · operation: be dead (be in the state of having died — to that which held us) · substrate: that (which held us — the law-relation from M5-M8) · outcome: the addressees standing dead to that which held them in the M5-M8 past-state · narrator: Paul, first-person epistolary author

**M396** — Descriptor of that which held us: we were held in it (i.e., the law).
  · agent: not-stated (the law as holding force, implicit) · operation: be held (be kept-in-grip — of the addressees, in the law) · substrate: we · outcome: the addressees having been held (past) in the law-relation · narrator: Paul, first-person epistolary author

**M397** — The purpose held over the release: that we should render service in a new, spirit-register mode, and not in the old, letter-register mode.
  · agent: we · operation: serve (render service — in newness of spirit, not in oldness of letter) · substrate: not-stated (God as the served party, implicit) · outcome: we serving in the newness of spirit rather than the oldness of the letter · narrator: Paul, first-person epistolary author

**M398** — Paul opens the next diatribal turn: what conclusion, then, do we draw?
  · agent: we (Paul with the imagined interlocutor) · operation: say (deliberatively — what shall we say?) · substrate: not-stated (the emerging conclusion) · outcome: the conclusion opened for question · narrator: Paul, first-person epistolary author

**M399** — The proposed objection posed as a question: is the law itself to be identified with sin?
  · agent: the law · operation: be (sin — of the law, interrogatively) · substrate: not-stated · outcome: the law's identity-with-sin put in question · narrator: Paul, first-person epistolary author

**M400** — Paul denies flatly: absolutely not.
  · agent: not-stated (Paul himself as speaker) · operation: may-it-not-be (emphatically deny) · substrate: the M14 identity-proposition (that the law is sin) · outcome: the M14 identity emphatically denied · narrator: Paul, first-person epistolary author

**M401** — Paul's positive attribution about the law's diagnostic function: except through the law, I would not have gained cognitive recognition of sin.
  · agent: I (Paul, in first-person diagnostic voice) · operation: not know (would-not-have-had-cognitive-recognition — sin, except through the law) · substrate: sin · outcome: I standing as one who would not have recognized sin apart from the law · narrator: Paul, first-person epistolary author, in the first-person diagnostic ego of Rom 7

**M402** — Sharper specific instance: I would not have gained recognition of coveting-desire either.
  · agent: I · operation: not know (would-not-have-had-cognitive-recognition — lust/coveting-desire) · substrate: lust (coveting-desire) · outcome: I standing as one who would not have recognized lust (apart from the law's Do-Not-Covet) · narrator: Paul, first-person epistolary author

**M403** — The exception-clause naming the diagnostic-source: except the law had spoken a specific utterance.
  · agent: the law · operation: say (utter — of the law, with recoverable directive content) · substrate: the content of the law's utterance (M18a) · outcome: the law having spoken the directive that M18a names · narrator: Paul, first-person epistolary author
  · **edges:** M403 —REPORTS→ M404

**M404** — The content of the law's utterance: you are not to covet.
  · agent: thou (indefinite second-person subject of the directive) · operation: not covet (directive: refrain from coveting) · substrate: not-stated (the withheld coveting-act) · outcome: the directed subject standing as one who is to refrain from coveting · narrator: Paul, first-person epistolary author, ventriloquizing the law's directive (Deut 5:21 / Exod 20:17)
  · **edges:** ["M403"] —REPORTS→ M404

**M405** — The participial-ground for M20: sin, using the commandment as its foothold-opportunity.
  · agent: sin · operation: take (seize — occasion, by the commandment) · substrate: occasion (the foothold-opportunity, aphormē) · outcome: sin having seized the foothold-opportunity by way of the commandment · narrator: Paul, first-person epistolary author
  · **edges:** M405 —BEQUEATHS→ RECEPTION

**M406** — The main-clause happening: sin actively worked up inside me every sort of coveting-desire.
  · agent: sin · operation: work (produce, generate, be active — in me, all manner of concupiscence) · substrate: in me (as the location of operation) · outcome: sin having actively generated every sort of concupiscence in me · narrator: Paul, first-person epistolary author
  · **edges:** M406 —BEQUEATHS→ RECEPTION

**M407** — The counter-principle showing why the law is the diagnostic-lens: without the law in place, sin lies dead.
  · agent: sin · operation: be (dead — of sin, without the law) · substrate: not-stated · outcome: sin standing dead (inert, inoperative) apart from the law · narrator: Paul, first-person epistolary author
  · **edges:** M407 —BEQUEATHS→ RECEPTION

**M408** — The autobiographical parallel: as for me, there was a time when I stood alive, apart from the law.
  · agent: I · operation: be alive (be in the state of living — without the law, once) · substrate: not-stated · outcome: I standing (past, once) alive apart from the law · narrator: Paul, first-person epistolary author, in the diagnostic first-person voice
  · **edges:** M408 —BEQUEATHS→ RECEPTION

**M409** — The pivot-clause introducing the inversion: but at the moment when the commandment [came, sin revived and I died — the completing verb-chain is truncated in the source].
  · agent: the commandment · operation: come (arrive — of the commandment; verb truncated in the source) · substrate: not-stated (the moment/scene into which it arrives) · outcome: the commandment's arrival — with the completing consequent (sin's revival and the ego's dying) truncated in the source · narrator: Paul, first-person epistolary author

**M410** — The verb-completion of the prior temporal clause: [the commandment] arrived.
  · agent: the commandment (from the prior clause) · operation: come (arrive — of the commandment, verb-completion) · substrate: not-stated · outcome: the commandment having arrived (the pivot-event of the M22-prior autobiography) · narrator: Paul, first-person epistolary author, closing the temporal clause from the prior passage

**M411** — The first consequent of the commandment's arrival: sin sprang back into activity.
  · agent: sin · operation: revive (spring back into life) · substrate: not-stated · outcome: sin having sprung back into active life · narrator: Paul, first-person epistolary author
  · **edges:** M411 —BEQUEATHS→ RECEPTION

**M412** — The second consequent, on the I-side: I underwent dying.
  · agent: I · operation: die (undergo death) · substrate: not-stated · outcome: the diagnostic-I having died · narrator: Paul, first-person epistolary author

**M413** — Descriptor of the commandment as originally intended: it was set-in-place aimed toward life.
  · agent: not-stated (the implicit ordainer, God) · operation: be ordained (be established, be set-in-place — unto life) · substrate: the commandment · outcome: the commandment set-in-place aimed at life · narrator: Paul, first-person epistolary author
  · **edges:** M413 —BEQUEATHS→ RECEPTION

**M414** — The cognitive-discovery reversal: I made a finding about the commandment.
  · agent: I · operation: find (discover, come to recognize — with recoverable content) · substrate: the content of the finding (M5a) · outcome: the diagnostic-I coming to recognize the M5a content · narrator: Paul, first-person epistolary author
  · **edges:** M414 —REPORTS→ M415

**M415** — The content of the discovery: that the same commandment — aimed at life — ran, for me, toward death.
  · agent: the commandment (this same one from M4) · operation: be (unto death — of the commandment, for me) · substrate: not-stated (its terminus for me) · outcome: the commandment terminating (for me) in death, contrary to its M4 life-destination · narrator: Paul, first-person epistolary author, ventriloquizing the discovery-content
  · **edges:** ["M414"] —REPORTS→ M415

**M416** — The participial-ground for what actually happened: sin, seizing the commandment as its foothold-opportunity.
  · agent: sin · operation: take (seize — occasion, by the commandment) · substrate: occasion (aphormē, foothold-opportunity) · outcome: sin having seized the foothold-opportunity by way of the commandment · narrator: Paul, first-person epistolary author

**M417** — First main-verb: sin thoroughly deceived me.
  · agent: sin · operation: deceive (thoroughly mislead — me) · substrate: me · outcome: the diagnostic-I having been thoroughly deceived by sin · narrator: Paul, first-person epistolary author
  · **edges:** M417 —BEQUEATHS→ RECEPTION

**M418** — Second main-verb: and by way of the same commandment, sin killed me.
  · agent: sin · operation: slay (kill — me, by it/the commandment) · substrate: me · outcome: the diagnostic-I having been killed by sin, mediated through the commandment · narrator: Paul, first-person epistolary author
  · **edges:** M418 —BEQUEATHS→ RECEPTION

**M419** — Paul draws the exculpating conclusion for the law: the law itself, as such, is holy.
  · agent: the law · operation: be (holy — of the law) · substrate: not-stated · outcome: the law standing as holy · narrator: Paul, first-person epistolary author

**M420** — And the commandment specifically: it also stands as holy, and it also stands as right, and it also stands as good.
  · agent: the commandment · operation: be (holy and just and good — of the commandment) · substrate: not-stated · outcome: the commandment standing as holy, and just, and good · narrator: Paul, first-person epistolary author

**M421** — Paul poses the follow-up diatribal question: did the thing that stands as good then get turned into death for me?
  · agent: that which is good · operation: be made (be turned — death unto me, of that which is good, interrogatively) · substrate: not-stated (its transformation-into-death for me) · outcome: the good's transformation into death-for-me put in question · narrator: Paul, first-person epistolary author

**M422** — Paul dismisses it: absolutely not.
  · agent: not-stated (Paul himself as speaker) · operation: may-it-not-be (emphatically deny) · substrate: the M11 possibility · outcome: the M11 possibility emphatically denied · narrator: Paul, first-person epistolary author

**M423** — The corrective placement of responsibility: it was sin — sin doing its death-work in me, using the good as its instrument.
  · agent: sin · operation: work (produce, generate — death in me, by that which is good) · substrate: in me (as location of death-generation) · outcome: sin having generated death in me, using that-which-is-good as instrument · narrator: Paul, first-person epistolary author

**M424** — First purpose of sin's death-work: that sin might get shown up as sin.
  · agent: sin · operation: appear (be shown up — as sin, purpose) · substrate: not-stated (its manifest character) · outcome: sin exposed and shown for what it is · narrator: Paul, first-person epistolary author

**M425** — Second purpose, coordinate: that sin, mediated by the commandment, might come to stand as beyond-measure-sinful.
  · agent: sin · operation: become (be made — exceeding sinful, through the commandment) · substrate: not-stated (its own sinfulness-intensity) · outcome: sin coming to stand as beyond-measure-sinful, through the commandment as intensifying instrument · narrator: Paul, first-person epistolary author

**M426** — Paul appeals to shared knowledge: we have cognitive hold of the fact that follows.
  · agent: we (Paul with the 'we-know' community) · operation: know (with recoverable content) · substrate: the content of the knowing (M16a) · outcome: we standing as ones who know the M16a content · narrator: Paul, first-person epistolary author
  · **edges:** M426 —REPORTS→ M427

**M427** — The content of that knowing: the law is spirit-register, spirit-formed.
  · agent: the law · operation: be (spiritual — of the law) · substrate: not-stated · outcome: the law standing as spiritual · narrator: Paul, first-person epistolary author, ventriloquizing the shared knowledge
  · **edges:** ["M426"] —REPORTS→ M427

**M428** — But the contrasting attribution about the diagnostic-I: I stand in the flesh-register.
  · agent: I · operation: be (carnal — of the diagnostic-I) · substrate: not-stated · outcome: the diagnostic-I standing as carnal (flesh-register) · narrator: Paul, first-person epistolary author, in the diagnostic first-person voice

**M429** — Further attribution about the diagnostic-I: sold over into the ownership of sin.
  · agent: not-stated (the implicit selling-agent) · operation: be sold (be transferred under ownership — sold under sin) · substrate: I · outcome: the diagnostic-I standing as sold-under sin's ownership · narrator: Paul, first-person epistolary author
  · **edges:** M429 —BEQUEATHS→ RECEPTION

**M430** — The specific inner-conflict pattern begins: as for what I actually carry out, I do not recognize/approve it as mine.
  · agent: I · operation: not allow (not approve, not recognize as one's own — that which I do) · substrate: that which I do · outcome: the diagnostic-I not approving what he actually carries out · narrator: Paul, first-person epistolary author

**M431** — The second beat: what my will wishes for, that is what I precisely do not carry out.
  · agent: I · operation: not do (not carry out — what I would/will) · substrate: what I would (what I will/wish) · outcome: the diagnostic-I not doing what his will wishes · narrator: Paul, first-person epistolary author

**M432** — The third beat: what I actually detest, that is what I in fact do.
  · agent: I · operation: do (carry out — what I hate) · substrate: what I hate · outcome: the diagnostic-I doing what he detests · narrator: Paul, first-person epistolary author

**M433** — The conditional setup for the diagnostic conclusion: if I actually do the thing my will refuses.
  · agent: I · operation: do (carry out — that which I would not, conditional) · substrate: that which I would not (what my will refuses) · outcome: the diagnostic-I (conditionally) doing what his will refuses · narrator: Paul, first-person epistolary author
  · **edges:** M433 —BEQUEATHS→ RECEPTION

**M434** — The conclusion drawn from that conditional: I am agreeing with the law — agreeing that it stands as good.
  · agent: I · operation: consent (agree with — the law, with recoverable content) · substrate: the law (with recoverable content M23a) · outcome: the diagnostic-I agreeing with the law about the M23a content · narrator: Paul, first-person epistolary author
  · **edges:** M434 —BEQUEATHS→ RECEPTION; M434 —REPORTS→ M435

**M435** — The content of that agreement: that the law stands as good.
  · agent: the law · operation: be (good — of the law) · substrate: not-stated · outcome: the law standing as good (as the content of the M23 consent) · narrator: Paul, first-person epistolary author, ventriloquizing the consent-content
  · **edges:** M435 —BEQUEATHS→ RECEPTION; ["M434"] —REPORTS→ M435

**M436** — The identity-conclusion drawn, negative half: it is no longer I myself who am the one doing the doing.
  · agent: not-stated (the diagnostic-I is disowned as agent here) · operation: do (interrogatively-negated — the it, of I) · substrate: it (the deed in question) · outcome: the deed's doing not attributed to the diagnostic-I · narrator: Paul, first-person epistolary author
  · **edges:** M436 —BEQUEATHS→ RECEPTION

**M437** — The identity-conclusion, positive half: instead, it is sin that is the actual doer.
  · agent: sin · operation: do (carry out — the it, of sin) · substrate: it (the deed in question) · outcome: the deed's doing attributed to sin as its actual agent · narrator: Paul, first-person epistolary author
  · **edges:** M437 —BEQUEATHS→ RECEPTION

**M438** — Descriptor of the M25 sin: it is the sin that resides — [inside me, per the truncated continuation].
  · agent: sin · operation: dwell (reside — of sin, in [me — truncated]) · substrate: not-stated (the location — 'in me' — is truncated at 'in') · outcome: sin standing as resident-within [me, per the truncated continuation] · narrator: Paul, first-person epistolary author
  · **edges:** M438 —BEQUEATHS→ RECEPTION

**M439** — Completing the location-clause from the prior passage: [sin that dwells] in me.
  · agent: sin (from the prior clause) · operation: (location arrives — 'in me', substrate-completion of the M26-prior indwelling) · substrate: me (as the location of indwelling) · outcome: sin standing as resident within the diagnostic-I · narrator: Paul, first-person epistolary author, closing the indwelling-location from the prior passage

**M440** — Paul reports his own cognitive hold of the following: he has come to know a particular thing about himself.
  · agent: I · operation: know (with recoverable content) · substrate: the content of the knowing (M2a) · outcome: the diagnostic-I standing as one who knows the M2a content · narrator: Paul, first-person epistolary author
  · **edges:** M440 —BEQUEATHS→ RECEPTION; M440 —REPORTS→ M441

**M441** — The content of that knowing: no good thing takes up residence inside me — the parenthetical clarifies: inside my fleshly-register.
  · agent: no good thing (negated existential subject) · operation: dwell (reside — of no good thing, in me / in my flesh) · substrate: in me — that is, in my flesh (as location) · outcome: no good thing standing as resident within me / within my flesh · narrator: Paul, first-person epistolary author, ventriloquizing the knowing-content
  · **edges:** ["M440"] —REPORTS→ M441

**M442** — The paired self-report: the willing IS at hand for me.
  · agent: to will (the willing-faculty) · operation: be present (be at-hand — with me, of the willing) · substrate: not-stated (its being-with-me) · outcome: the willing standing as present-with-me · narrator: Paul, first-person epistolary author

**M443** — The contrast: but as for how to perform the good thing, I do not find that.
  · agent: I · operation: not find (not discover — how to perform that which is good) · substrate: how to perform that which is good · outcome: the diagnostic-I not finding the how-to-perform the good · narrator: Paul, first-person epistolary author

**M444** — Restating the inner-conflict pattern: as for the good my will wishes, I do not do it.
  · agent: I · operation: not do (not carry out — the good that I would) · substrate: the good that I would · outcome: the diagnostic-I not doing the good that his will wishes · narrator: Paul, first-person epistolary author

**M445** — The mirror-inverse: but the evil my will refuses — that is what I actually do.
  · agent: I · operation: do (carry out — the evil which I would not) · substrate: the evil which I would not · outcome: the diagnostic-I doing the evil his will refuses · narrator: Paul, first-person epistolary author

**M446** — The conditional setup for the identity-transfer: if I actually do what my will refuses.
  · agent: I · operation: do (carry out — that I would not, conditional) · substrate: that I would not · outcome: the diagnostic-I (conditionally) doing what his will refuses · narrator: Paul, first-person epistolary author

**M447** — The identity-conclusion, negative half: it is no longer I myself who am the one doing the doing.
  · agent: not-stated (the diagnostic-I disowned as agent) · operation: do (interrogatively-negated — the it, of I as agent) · substrate: it (the deed) · outcome: the deed's doing not attributed to the diagnostic-I · narrator: Paul, first-person epistolary author
  · **edges:** M447 —BEQUEATHS→ RECEPTION

**M448** — The identity-conclusion, positive half: instead, it is sin — sin that keeps residing in me — who does the doing.
  · agent: sin (that dwelleth in me) · operation: do (carry out — the it, of sin that dwells in me) · substrate: it (the deed) · outcome: the deed's doing attributed to indwelling-sin as its actual agent · narrator: Paul, first-person epistolary author
  · **edges:** M448 —BEQUEATHS→ RECEPTION

**M449** — Paul draws the inference into a pattern-observation: I make a finding about a certain pattern/principle at work.
  · agent: I · operation: find (discover — a law/pattern, with recoverable content) · substrate: the content of the found-pattern (M10a) · outcome: the diagnostic-I coming to recognize the M10a pattern · narrator: Paul, first-person epistolary author
  · **edges:** M449 —BEQUEATHS→ RECEPTION; M449 —REPORTS→ M450

**M450** — The content of the found-pattern: at those very moments when I set my will on doing good, evil is right there at hand with me.
  · agent: evil · operation: be present (be at-hand — with me, of evil, at the moment I would do good) · substrate: not-stated (its being-with-me at the willing-good moments) · outcome: evil standing at-hand with me at the very moments when I would do good · narrator: Paul, first-person epistolary author, ventriloquizing the found-pattern
  · **edges:** ["M449"] —REPORTS→ M450

**M451** — Escalating the diagnosis further: I actually observe a different law/pattern at work in my body-parts.
  · agent: I · operation: see (observe — with recoverable content) · substrate: the content of the observation (M11a) · outcome: the diagnostic-I coming to observe the M11a another-law · narrator: Paul, first-person epistolary author
  · **edges:** M451 —REPORTS→ M452

**M452** — The content of the observation: there stands another law, and it is at work in my body-parts.
  · agent: another law · operation: be (another law — in my members) · substrate: in my members (as location of operation) · outcome: a further law standing at work in the addressee's body-parts · narrator: Paul, first-person epistolary author, ventriloquizing the observation-content
  · **edges:** M452 —BEQUEATHS→ RECEPTION; ["M451"] —REPORTS→ M452

**M453** — First participial descriptor of that another-law: it is waging war against the law that governs my mind.
  · agent: another law (from M11a) · operation: war (wage war — against the law of my mind) · substrate: the law of my mind · outcome: the another-law waging war against the mind-law · narrator: Paul, first-person epistolary author
  · **edges:** M453 —BEQUEATHS→ RECEPTION

**M454** — Second participial descriptor: and it is dragging me into captivity, and the master into whose captivity I am dragged is the law-of-sin.
  · agent: another law (from M11a) · operation: bring into captivity (take captive — me, to the law of sin) · substrate: me · outcome: the diagnostic-I brought into captivity to the law-of-sin, by the another-law · narrator: Paul, first-person epistolary author

**M455** — Descriptor of that law-of-sin the M13 captivity is toward: it is the one located in my body-parts.
  · agent: the law of sin · operation: be (in my members — of the law of sin) · substrate: in my members (as location) · outcome: the law-of-sin standing as located in the members — making it (perhaps) identical with the M11a another-law · narrator: Paul, first-person epistolary author
  · **edges:** M455 —BEQUEATHS→ RECEPTION

**M456** — The exclamatory-diagnosis breaks out: what a wretched-under-toil human I am!
  · agent: I (self-exclaiming) · operation: be (wretched — of the diagnostic-I, exclamatory) · substrate: not-stated · outcome: the diagnostic-I exclaiming himself as a wretched-under-toil human · narrator: Paul, first-person epistolary author, in exclamatory-diagnostic voice

**M457** — The rescue-question follows: who is going to pull me out of this body characterized by death?
  · agent: who (interrogated — the potential rescuer) · operation: deliver (rescue — me, from the body of this death) · substrate: me · outcome: the diagnostic-I put under the question of who could rescue him from the body-of-this-death · narrator: Paul, first-person epistolary author

**M458** — The answer bursts through: I render thanks to God — thanks routed through our Lord Jesus Christ.
  · agent: I · operation: thank (render thanks — to God, through Jesus Christ our Lord) · substrate: God · outcome: thanks rendered by the diagnostic-I to God, mediated through our Lord Jesus Christ · narrator: Paul, first-person epistolary author

**M459** — Paul closes the ch 7 diagnosis with a summary attribution: on the mind-side, I myself render service to the law that belongs to God.
  · agent: I myself (with the mind) · operation: serve (render service — the law of God, with the mind) · substrate: the law of God · outcome: the diagnostic-I serving God's law with his mind · narrator: Paul, first-person epistolary author
  · **edges:** M459 —BEQUEATHS→ RECEPTION

**M460** — The flesh-side of the summary: but with the flesh, [I serve] the law — [the source cuts off at 'the law' before the substrate 'of sin' arrives].
  · agent: I (with the flesh, implicit from parallel with M18) · operation: serve (render service — the law [of sin, truncated], with the flesh) · substrate: the law [of sin, truncated] · outcome: the diagnostic-I serving [the law of sin] with his flesh — the substrate-specification 'of sin' is truncated at 'the law' in the source · narrator: Paul, first-person epistolary author
  · **edges:** M460 —BEQUEATHS→ RECEPTION

**M461** — Completing the substrate from the prior clause: [I serve] the law of sin [with the flesh].
  · agent: I (from the prior clause, with the flesh) · operation: (substrate-completion — 'of sin', completing the serve-law substrate from prior M19) · substrate: the law of sin (substrate arrived) · outcome: the diagnostic-I serving the law-of-sin with his flesh, completing the M19-prior dual-service · narrator: Paul, first-person epistolary author, closing the flesh-side of the dual-service from the prior passage

**M462** — The great turn: on this account, at the present moment, there stands no adverse verdict at all against those who are located in Christ Jesus.
  · agent: not-stated (the condemnation, existentially negated) · operation: be (no condemnation — now, to them which are in Christ Jesus) · substrate: them which are in Christ Jesus · outcome: the in-Christ cohort standing under no adverse verdict, at the present time · narrator: Paul, first-person epistolary author, opening the ch 8 pneumatological climax
  · **edges:** M462 —BEQUEATHS→ RECEPTION

**M463** — Descriptor of the in-Christ cohort: they take their steps not by the flesh's direction, but by the Spirit's direction.
  · agent: they (the in-Christ cohort of M2) · operation: walk (take steps — not after the flesh, but after the Spirit) · substrate: not-stated (the walking-mode itself) · outcome: the in-Christ cohort walking after the Spirit rather than after the flesh · narrator: Paul, first-person epistolary author

**M464** — The mechanism behind that no-condemnation: the Spirit-of-life-law-in-Christ-Jesus took me out of the domain of the sin-and-death-law.
  · agent: the law of the Spirit of life in Christ Jesus · operation: make free (release — me, from the law of sin and death) · substrate: me · outcome: me released from the law-of-sin-and-death by the Spirit-of-life-law · narrator: Paul, first-person epistolary author

**M465** — Paul locates what the law was structurally incapable of accomplishing: there is something the law could not do.
  · agent: the law · operation: not be able (be structurally incapable — of the law, to do something) · substrate: not-stated (the thing the law could not do) · outcome: the law standing as unable to do (the thing at issue — condemn sin in the flesh) · narrator: Paul, first-person epistolary author

**M466** — The reason for that structural impossibility: the law was weakened, and the weakening ran through the flesh.
  · agent: it (the law) · operation: be weak (be weakened — through the flesh) · substrate: not-stated (its weakened-condition through the flesh) · outcome: the law standing weakened, the weakening mediated through the flesh · narrator: Paul, first-person epistolary author

**M467** — The participial-mediation for what God did instead: God sent his own Son — sent him in the shape-of-sinful-flesh, and did so with reference to sin.
  · agent: God · operation: send (dispatch — his own Son, in the likeness of sinful flesh, for sin) · substrate: his own Son · outcome: God's own Son dispatched in the likeness of sinful flesh, for sin (as instrument of the M8 condemnation) · narrator: Paul, first-person epistolary author
  · **edges:** M467 —BEQUEATHS→ RECEPTION

**M468** — The main-verb outcome of that sending: God pronounced adverse verdict on sin, and did so in the flesh itself.
  · agent: God (implicit from M7) · operation: condemn (pronounce adverse verdict on — sin, in the flesh) · substrate: sin · outcome: sin pronounced-under-adverse-verdict, and pronounced so in the flesh itself · narrator: Paul, first-person epistolary author

**M469** — The purpose held over the M8 condemnation: that the law's righteous requirement should get completed in us.
  · agent: not-stated (the implicit divine-fulfilling agency) · operation: be fulfilled (be completed — the righteousness of the law, in us) · substrate: the righteousness of the law (dikaiōma tou nomou) · outcome: the law's righteous-requirement completed in us as its location · narrator: Paul, first-person epistolary author

**M470** — Descriptor of the 'us' the requirement is fulfilled in: we, in parallel with the M3 cohort, take our steps not by the flesh's direction but by the Spirit's direction.
  · agent: us (the 'we' in whom the requirement is fulfilled) · operation: walk (take steps — not after the flesh, but after the Spirit) · substrate: not-stated (the walking-mode) · outcome: the M9 'us' walking after the Spirit rather than after the flesh · narrator: Paul, first-person epistolary author

**M471** — Sharpening the flesh-vs-Spirit distinction: those persons whose location is with-respect-to-the-flesh set their minds on the things of the flesh.
  · agent: they that are after the flesh · operation: mind (set-the-mind-on, be occupied with — the things of the flesh) · substrate: the things of the flesh · outcome: the flesh-cohort's mindedness set on the flesh-things · narrator: Paul, first-person epistolary author

**M472** — The parallel Spirit-side, with the verb elided: those whose location is with-respect-to-the-Spirit [set their minds on] the things of the Spirit.
  · agent: they that are after the Spirit · operation: mind (set-the-mind-on — the things of the Spirit, verb elided from M11) · substrate: the things of the Spirit · outcome: the Spirit-cohort's mindedness set on the Spirit-things · narrator: Paul, first-person epistolary author

**M473** — The verdict on the flesh-mindedness: that mode of being minded IS death.
  · agent: to be carnally minded (the flesh-mindset itself) · operation: be (death — of carnal-mindedness) · substrate: not-stated · outcome: flesh-mindedness standing as death · narrator: Paul, first-person epistolary author

**M474** — The paired verdict on Spirit-mindedness: that mode of being minded IS life and peace.
  · agent: to be spiritually minded (the Spirit-mindset itself) · operation: be (life and peace — of spiritual-mindedness) · substrate: not-stated · outcome: Spirit-mindedness standing as life and peace · narrator: Paul, first-person epistolary author

**M475** — The ground for M13's verdict: the flesh-mindset stands as active hostility directed against God.
  · agent: the carnal mind · operation: be (enmity — against God, of the carnal mind) · substrate: not-stated · outcome: the carnal mind standing as hostility directed against God · narrator: Paul, first-person epistolary author

**M476** — Further ground for M15's hostility: because it — the carnal mind — is not [under the law of God's authority — the substrate-completion is truncated in the source at 'for it is not'].
  · agent: it (the carnal mind) · operation: not be (subject / not be under — [the law of God, truncated]) · substrate: not-stated (the truncated 'to the law of God' completes it per Rom 8:7b) · outcome: the carnal mind standing as not-subject-to [the law of God, truncated] — the substrate-specification is cut off at 'for it is not' · narrator: Paul, first-person epistolary author

**M477** — Completing the prior clause: [the carnal mind is not] under the authority of God's law.
  · agent: it (the carnal mind) · operation: not be subject (not be under authority — to the law of God) · substrate: the law of God · outcome: the carnal mind standing as not under the law-of-God's authority · narrator: Paul, first-person epistolary author, closing the not-subject attribution from the prior passage

**M478** — Sharpening M1: nor, indeed, is it actually capable of being subject.
  · agent: it (the carnal mind) · operation: not be able (be incapable — of being subject) · substrate: not-stated (the being-subject state) · outcome: the carnal mind standing as structurally unable to be subject · narrator: Paul, first-person epistolary author
  · **edges:** M478 —BEQUEATHS→ RECEPTION

**M479** — But you, in contrast to that carnal-mind cohort, stand located not in the flesh-region but in the Spirit-region.
  · agent: ye · operation: be (not in the flesh, but in the Spirit — of the addressees, contrastive location) · substrate: not-stated (the region-of-location itself) · outcome: the addressees standing located in the Spirit-region rather than the flesh-region · narrator: Paul, first-person epistolary author

**M480** — The condition under which that in-Spirit location holds: God's Spirit takes up residence within you.
  · agent: the Spirit of God · operation: dwell (reside — of the Spirit of God, in you, conditional) · substrate: in you · outcome: God's Spirit residing in the addressees (as condition for M3) · narrator: Paul, first-person epistolary author
  · **edges:** M480 —BEQUEATHS→ RECEPTION

**M481** — The negative conditional: if any person does not have the Spirit that belongs to Christ.
  · agent: any man · operation: not have (not possess — the Spirit of Christ, conditional) · substrate: the Spirit of Christ · outcome: the person (conditionally) standing as not possessing the Christ-Spirit · narrator: Paul, first-person epistolary author
  · **edges:** M481 —BEQUEATHS→ RECEPTION

**M482** — The consequent-verdict: that person does not belong to him at all.
  · agent: he (the Spirit-lacking man) · operation: be (none of his — of the Spirit-lacking person) · substrate: not-stated (Christ, whose belonging the person lacks) · outcome: the Spirit-lacking person standing as not-belonging to Christ · narrator: Paul, first-person epistolary author
  · **edges:** M482 —BEQUEATHS→ RECEPTION

**M483** — The positive conditional: if Christ, on the other hand, is in you.
  · agent: Christ · operation: be (in you — of Christ, conditional) · substrate: in you · outcome: Christ (conditionally) standing as located in the addressees · narrator: Paul, first-person epistolary author
  · **edges:** M483 —BEQUEATHS→ RECEPTION

**M484** — First consequent-side: the body is dead — and the cause is sin.
  · agent: the body · operation: be (dead — of the body, because of sin) · substrate: not-stated · outcome: the body standing as dead, with sin named as the cause · narrator: Paul, first-person epistolary author
  · **edges:** M484 —BEQUEATHS→ RECEPTION

**M485** — The paired second consequent-side: but the Spirit is life — and the cause is righteousness.
  · agent: the Spirit · operation: be (life — of the Spirit, because of righteousness) · substrate: not-stated · outcome: the Spirit standing as life, with righteousness named as the cause · narrator: Paul, first-person epistolary author
  · **edges:** M485 —BEQUEATHS→ RECEPTION

**M486** — The further conditional, with a heavier characterization of the Spirit: if the Spirit — the Spirit of the one who raised Jesus from among the dead — takes up residence in you.
  · agent: the Spirit of him that raised up Jesus from the dead · operation: dwell (reside — of the Spirit of him who raised Jesus, in you, conditional) · substrate: in you · outcome: the Spirit of the Jesus-raiser residing in the addressees · narrator: Paul, first-person epistolary author
  · **edges:** M486 —BEQUEATHS→ RECEPTION

**M487** — Descriptor of that Spirit's source: he lifted Jesus up out of death.
  · agent: him (God, characterized as raiser) · operation: raise up (lift out of death — Jesus, from the dead) · substrate: Jesus · outcome: Jesus lifted up from among the dead by God · narrator: Paul, first-person epistolary author

**M488** — Restatement of the raiser-descriptor as subject of the main verb: he (the same one who raised the Anointed from among the dead).
  · agent: he (God, as subject of the M13 promise) · operation: raise up (lift out of death — Christ, from the dead, subject-descriptor) · substrate: Christ · outcome: Christ lifted up from among the dead by God, this raiser being the M13 promise-agent · narrator: Paul, first-person epistolary author

**M489** — The main-promise: that same raiser will also bring to life your death-liable bodies — and he will do so through his Spirit.
  · agent: he that raised up Christ from the dead (from M12) · operation: quicken (bring to life — your mortal bodies, by his Spirit) · substrate: your mortal bodies · outcome: the addressees' mortal bodies (future) brought to life by God, mediated through his Spirit · narrator: Paul, first-person epistolary author
  · **edges:** M489 —BEQUEATHS→ RECEPTION

**M490** — Descriptor of the mediating-Spirit in that promise: it is the Spirit that resides in you.
  · agent: his Spirit (that dwelleth in you) · operation: dwell (reside — of his Spirit, in you) · substrate: in you · outcome: God's Spirit residing in the addressees, as the mediating-instrument of M13 · narrator: Paul, first-person epistolary author
  · **edges:** M490 —BEQUEATHS→ RECEPTION

**M491** — Paul draws the practical inference with a kinship-address: therefore, brothers, we stand under obligation — but the obligation is not to the flesh, not to conduct our lives after the flesh.
  · agent: we (brethren) · operation: be debtors (be under obligation — not to the flesh, not to live after the flesh) · substrate: not-stated (the obligation-target) · outcome: we standing under obligation, but not to the flesh — thus not to live after the flesh · narrator: Paul, first-person epistolary author

**M492** — The conditional test on the flesh-side: if you actually conduct your lives according to the flesh's direction.
  · agent: ye · operation: live (conduct life — after the flesh, conditional) · substrate: not-stated (life-mode) · outcome: the addressees (conditionally) living after the flesh's direction · narrator: Paul, first-person epistolary author
  · **edges:** M492 —BEQUEATHS→ RECEPTION

**M493** — The consequent of that flesh-side condition: you are about to die.
  · agent: ye · operation: die (undergo death — future) · substrate: not-stated · outcome: the addressees (future) undergoing death, as consequent of flesh-life · narrator: Paul, first-person epistolary author

**M494** — The alternative conditional on the Spirit-side: if instead you, through the Spirit as your instrument, actively put to death the body's deeds.
  · agent: ye (through the Spirit as instrument) · operation: mortify (put to death — the deeds of the body, through the Spirit, conditional) · substrate: the deeds of the body · outcome: the addressees (conditionally) putting the body's deeds to death, mediated through the Spirit · narrator: Paul, first-person epistolary author

**M495** — The consequent of the Spirit-side condition: you are going to live.
  · agent: ye · operation: live (undergo life — future) · substrate: not-stated · outcome: the addressees (future) living, as consequent of Spirit-mediated putting-to-death of body-deeds · narrator: Paul, first-person epistolary author

**M496** — Descriptor of the cohort being characterized: as many as are being led by God's Spirit.
  · agent: not-stated (the Spirit of God as leader) · operation: be led (be guided — by the Spirit of God) · substrate: as many as (the Spirit-led cohort) · outcome: the cohort standing as those being led by God's Spirit · narrator: Paul, first-person epistolary author

**M497** — The identity-attribution: those persons are — [the substrate 'sons of God' is truncated at 'sons' in the source, missing the of-God specification].
  · agent: they (the Spirit-led cohort of M20) · operation: be (the sons [of God, truncated] — of the Spirit-led cohort) · substrate: not-stated (the of-God specification is truncated) · outcome: the Spirit-led cohort standing as the sons [of God — the specifying-genitive is truncated at 'sons'] · narrator: Paul, first-person epistolary author

**M498** — Completing the identity-attribution from the prior clause: [they are the sons] of God.
  · agent: they (the Spirit-led cohort from prior M20) · operation: (substrate-completion — 'of God', completing the M21-prior sons-of attribution) · substrate: God (as the specifying genitive) · outcome: the Spirit-led cohort standing as the sons of God · narrator: Paul, first-person epistolary author, closing the sons-of-God identity from the prior passage

**M499** — The negative attribution about what you received: not a spirit of slavery, one that would bring you back once more into fear.
  · agent: ye · operation: not receive (not take on — the spirit of bondage, again unto fear) · substrate: the spirit of bondage · outcome: the addressees not receiving a slave-spirit that would return them to fear · narrator: Paul, first-person epistolary author

**M500** — The positive counterpart: instead you took onto yourselves the Spirit of being made-a-child — an adoption-Spirit.
  · agent: ye · operation: receive (take onto oneself — the Spirit of adoption) · substrate: the Spirit of adoption · outcome: the addressees receiving the Spirit-of-adoption (pneuma huiothesias) · narrator: Paul, first-person epistolary author

**M501** — The consequence enabled by that adoption-Spirit: through it we cry out an address — 'Abba, Father'.
  · agent: we · operation: cry (cry out an address — 'Abba, Father', through the adoption-Spirit as instrument) · substrate: not-stated (God, as the vocative-addressee named by the Abba-Father cry) · outcome: we crying out to God with the vocative-name 'Abba, Father', mediated through the adoption-Spirit · narrator: Paul, first-person epistolary author

**M502** — The Spirit itself acts as co-witness, adding its testimony alongside our own spirit's testimony — to a specific fact about us.
  · agent: the Spirit itself · operation: bear witness with (co-testify — with our spirit, with recoverable content) · substrate: the content of the witness (M5a) — with our spirit as co-witness · outcome: the Spirit joint-testifying with our spirit to the M5a content · narrator: Paul, first-person epistolary author
  · **edges:** M502 —BEQUEATHS→ RECEPTION; M502 —REPORTS→ M503

**M503** — The content of that joint-witness: that we stand as the children of God.
  · agent: we · operation: be (children of God — of us) · substrate: not-stated · outcome: the addressees standing as the children of God · narrator: Paul, first-person epistolary author, ventriloquizing the joint-witness content
  · **edges:** ["M502"] —REPORTS→ M503

**M504** — The conditional syllogism-setup: and if children.
  · agent: we (as substrate of the children-state) · operation: be (children — conditional/hypothetical) · substrate: not-stated · outcome: the addressees (conditionally) standing as children · narrator: Paul, first-person epistolary author

**M505** — The consequent of the syllogism, with an escalating chain of specifiers: then heirs — heirs whose inheritance-source is God, and heirs standing joint with Christ.
  · agent: we · operation: be (heirs — of God, joint-heirs with Christ) · substrate: not-stated (the inheritance) · outcome: the addressees standing as heirs — specifically, heirs of God, and joint-heirs with Christ · narrator: Paul, first-person epistolary author

**M506** — A further condition attached to the heir-consequent: provided that we undergo suffering together with him.
  · agent: we · operation: suffer with (co-suffer — with him, conditional) · substrate: not-stated (the suffering-event, with Christ as co-sufferer) · outcome: the addressees (conditionally) suffering together with Christ · narrator: Paul, first-person epistolary author

**M507** — The purpose held out over that co-suffering: that we may also be glorified together (with him).
  · agent: not-stated (the implicit divine glorifier) · operation: be glorified together (be co-glorified — with him, purpose) · substrate: we · outcome: the addressees (future) glorified together with Christ, as intended-outcome of the M8 co-suffering · narrator: Paul, first-person epistolary author

**M508** — Paul offers a considered judgment: my accounting brings me to conclude the following.
  · agent: I (Paul) · operation: reckon (draw an inferred assessment — with recoverable content) · substrate: the content of the reckoned judgment (M10a) · outcome: Paul standing as one who holds the M10a assessment · narrator: Paul, first-person epistolary author
  · **edges:** M508 —REPORTS→ M509

**M509** — The content of the reckoning: the suffering-experiences of this current time do not stand as of weight to be balanced against the coming glory.
  · agent: the sufferings of this present time · operation: not be worthy (not be of weight — to be compared with the glory) · substrate: not-stated (the comparison-scale) · outcome: the present-sufferings standing as not-weight-comparable to the coming glory · narrator: Paul, first-person epistolary author, ventriloquizing the reckoned judgment
  · **edges:** ["M508"] —REPORTS→ M509

**M510** — Descriptor of that glory: it is what is going to be uncovered — uncovered into our sphere.
  · agent: not-stated (the implicit divine revealer) · operation: be revealed (be uncovered, disclosed — the glory, in us, future) · substrate: the glory (from M10a) · outcome: the glory (future) uncovered into the addressees as the location of its manifestation · narrator: Paul, first-person epistolary author

**M511** — Now paul introduces creation-side of the picture: the whole created order, with its stretched-out expectation, sits in the posture of waiting — waiting for the unveiling of God's sons.
  · agent: the earnest expectation of the creature · operation: wait (be in the posture of expectant-waiting — for the manifestation of the sons of God) · substrate: the manifestation of the sons of God · outcome: creation's stretched-out expectation waiting for the manifestation of the sons of God · narrator: Paul, first-person epistolary author

**M512** — The explanation of why creation is in that waiting-posture: creation was placed under futility, and it was not by creation's own will.
  · agent: not-stated (the implicit subjector, named in M14) · operation: be made subject (be placed under — the creature, to vanity, not willingly) · substrate: the creature · outcome: creation subjected to vanity/futility, and against creation's own will · narrator: Paul, first-person epistolary author

**M513** — Descriptor of that implicit subjector: he is the one who did the subjecting, and he did it holding out hope.
  · agent: him (God, characterized as subjector) · operation: subject (place-under — the creation, in hope) · substrate: the same (the creation, from M13) · outcome: creation subjected by God, with hope held out over the subjection · narrator: Paul, first-person epistolary author

**M514** — The content of that hope, introduced as reason-clause: because the creation itself will also be released from [the slavery of decay — the substrate-specification is truncated in the source at 'from the'].
  · agent: not-stated (the implicit divine deliverer) · operation: be delivered (be released — of the creature itself, from [the bondage of corruption, truncated]) · substrate: the creature itself · outcome: creation (future) released from [the bondage of corruption, per the KJV continuation, truncated in the source at 'from the'] · narrator: Paul, first-person epistolary author

**M515** — Completing the from-and-into pair from the prior clause: [creation will be released] out of the slavery to decay, and into the glory-marked liberty that belongs to the children of God.
  · agent: not-stated (the implicit divine deliverer from prior M15) · operation: (substrate-completion — 'bondage of corruption' as source, 'glorious liberty of the children of God' as terminus) · substrate: bondage of corruption (source) — into glorious liberty of the children of God (terminus) · outcome: creation released out of the slavery-to-decay and into the glory-marked liberty of the children of God · narrator: Paul, first-person epistolary author, closing the release-substrate and terminus from the prior passage

**M516** — Paul appeals to shared cognition: we have hold of the following fact about the creation.
  · agent: we (Paul with the 'we-know' community) · operation: know (with recoverable content) · substrate: the content of the knowing (M2a) · outcome: we standing as ones who know the M2a content · narrator: Paul, first-person epistolary author
  · **edges:** M516 —REPORTS→ M517

**M517** — The content of what we know: the entire created order joins in groaning and in labor-pain, groaning together and laboring together, and this has been going on right up to the present.
  · agent: the whole creation · operation: groan and travail together (join-groan and join-labor-in-pain — until now) · substrate: not-stated (its own pained condition) · outcome: the whole creation joined in groaning and labor-pain, up to the present · narrator: Paul, first-person epistolary author, ventriloquizing the shared knowledge
  · **edges:** M517 —BEQUEATHS→ RECEPTION; ["M516"] —REPORTS→ M517

**M518** — Descriptor of the us-cohort about to be added to the groaning: we are the ones who possess the Spirit's first-portion.
  · agent: ourselves (the addressees + Paul) · operation: have (possess — the firstfruits of the Spirit) · substrate: the firstfruits of the Spirit · outcome: we standing as possessors of the Spirit's first-portion · narrator: Paul, first-person epistolary author

**M519** — And in fact, not just creation, but we too — we ourselves — do the groaning, and we groan on the inside.
  · agent: we ourselves · operation: groan (groan within — of us ourselves, inwardly) · substrate: not-stated (within ourselves — the location of the groaning) · outcome: the Spirit-firstfruits cohort groaning inwardly, joining creation's groaning · narrator: Paul, first-person epistolary author

**M520** — The participial specifying what that inward groaning is directed toward: we are in the posture of waiting — waiting for the son-making, that is, the release of our body.
  · agent: we (from M4) · operation: wait (be in the posture of waiting — for the adoption / the redemption of our body) · substrate: the adoption — that is, the redemption of our body · outcome: the Spirit-firstfruits cohort waiting for the adoption, glossed as the redemption-of-our-body · narrator: Paul, first-person epistolary author

**M521** — The grounding-attribution: we have been rescued — the register in which the rescue holds is hope.
  · agent: not-stated (the implicit divine rescuer) · operation: be saved (be rescued — by hope, as register) · substrate: we · outcome: we standing as rescued, and rescued in the hope-register · narrator: Paul, first-person epistolary author

**M522** — The definitional-principle behind hope: a hope-object that is actually seen is not really hope in the true sense.
  · agent: hope that is seen · operation: not be (hope — of hope-that-is-seen) · substrate: not-stated · outcome: hope-that-is-seen standing as not-hope (in the true sense) · narrator: Paul, first-person epistolary author

**M523** — Ground for the M7 definition: consider what a person actually sees.
  · agent: a man · operation: see (perceive — of a man, indefinite object) · substrate: not-stated (what a man sees, indefinite) · outcome: a person's actual seeing (as premise for the M9 rhetorical question) · narrator: Paul, first-person epistolary author

**M524** — The rhetorical question that follows: why then does that person still hope for it?
  · agent: he (the man from M8) · operation: hope (for — interrogatively, why still) · substrate: not-stated (the seen-object, from M8) · outcome: the person put under an impossibility-question about still-hoping for what is already seen · narrator: Paul, first-person epistolary author
  · **edges:** M524 —BEQUEATHS→ RECEPTION

**M525** — The alternative conditional: but if we in fact hope for that which we do not see.
  · agent: we · operation: hope (for — that we see not, conditional) · substrate: that we see not (the unseen substrate of hope) · outcome: we (conditionally) hoping for what we do not see · narrator: Paul, first-person epistolary author

**M526** — The consequent of the alternative: in that case, we make it our practice to wait for it — waiting with staying-under endurance.
  · agent: we · operation: wait (wait for — with patience/staying-under-endurance) · substrate: it (the unseen substrate from M10) · outcome: we waiting-with-patience for the unseen substrate · narrator: Paul, first-person epistolary author

**M527** — Paul pivots to a parallel act by the Spirit: likewise, the Spirit takes hold alongside our weakness and helps.
  · agent: the Spirit · operation: help (take-hold-alongside — our infirmities) · substrate: our infirmities · outcome: the Spirit taking-hold-alongside our weakness and helping · narrator: Paul, first-person epistolary author
  · **edges:** M527 —BEQUEATHS→ RECEPTION

**M528** — Naming the weakness the Spirit helps: we do not have cognitive hold of what we should be praying for, in the way we ought.
  · agent: we · operation: not know (not have cognitive hold — with recoverable content) · substrate: the content of the not-knowing (M13a) · outcome: we standing as ones who do not know the M13a content · narrator: Paul, first-person epistolary author
  · **edges:** M528 —BEQUEATHS→ RECEPTION; M528 —REPORTS→ M529

**M529** — The content of the not-knowing: what we ought to be praying for, in the manner in which we ought.
  · agent: we · operation: pray (should-pray — for what, in what manner) · substrate: not-stated (the object and manner of praying) · outcome: the deliberative-open of what we should pray for and how — left unresolved from our side · narrator: Paul, first-person epistolary author, ventriloquizing the not-known deliberation
  · **edges:** ["M528"] —REPORTS→ M529

**M530** — The Spirit's response: the Spirit himself steps in on our behalf, and does so with groans that are not put into words.
  · agent: the Spirit itself · operation: make intercession (step in for — for us, with unutterable groanings) · substrate: not-stated (us as beneficiaries, folded into for-us) · outcome: the Spirit interceding on our behalf, with groanings that are not put into words · narrator: Paul, first-person epistolary author

**M531** — Descriptor of those Spirit-groanings: they are of a kind that cannot be put into speech.
  · agent: not-stated (the potential utterer) · operation: not be uttered (not be spoken — of the groanings) · substrate: the groanings (from M14) · outcome: the Spirit-groanings standing as unable-to-be-spoken · narrator: Paul, first-person epistolary author

**M532** — Descriptor of a new subject entering the picture: the one whose action is searching hearts.
  · agent: he (the heart-searcher, God) · operation: search (examine — the hearts) · substrate: the hearts · outcome: God-as-heart-searcher examining the hearts · narrator: Paul, first-person epistolary author

**M533** — The main claim about that heart-searcher: he has cognitive hold of a specific something.
  · agent: he (the heart-searcher, God) · operation: know (have cognitive hold — with recoverable content) · substrate: the content of the knowing (M17a) · outcome: the heart-searcher standing as one who knows the M17a content · narrator: Paul, first-person epistolary author
  · **edges:** M533 —REPORTS→ M534

**M534** — The content of the heart-searcher's knowing: what the mind of [the Spirit — the specifying genitive is truncated in the source at 'of'] actually is.
  · agent: the mind of [the Spirit, truncated] · operation: be (the mind — of [the Spirit, truncated]) · substrate: not-stated · outcome: the Spirit's mind standing as a knowable something to the heart-searcher — the specifying-genitive 'of the Spirit' is truncated in the source at 'of' · narrator: Paul, first-person epistolary author, ventriloquizing the knowing-content
  · **edges:** M534 —BEQUEATHS→ RECEPTION; ["M533"] —REPORTS→ M534

**M535** — Completing the specifying-genitive from the prior clause: [what the mind of] the Spirit [is].
  · agent: the mind (from prior M17a) · operation: (specifying-genitive completion — 'of the Spirit', identifying whose mind M17a-prior asked about) · substrate: the Spirit (as specifying-genitive) · outcome: the M17a-prior mind identified specifically as the Spirit's mind · narrator: Paul, first-person epistolary author, closing the specifying-genitive from the prior passage

**M536** — The ground for the heart-searcher's knowing of the Spirit's mind: because the Spirit is stepping in for the holy-ones, and stepping in in accord with God's own will.
  · agent: he (the Spirit) · operation: make intercession (step in for — the saints, according to the will of God) · substrate: not-stated (the saints as beneficiaries, folded into for-them) · outcome: the Spirit interceding for the saints, aligned with God's will · narrator: Paul, first-person epistolary author
  · **edges:** M536 —BEQUEATHS→ RECEPTION

**M537** — Paul turns to shared cognition: we have cognitive hold of a further fact.
  · agent: we (Paul with the 'we-know' community) · operation: know (with recoverable content) · substrate: the content of the knowing (M3a) · outcome: we standing as ones who know the M3a content · narrator: Paul, first-person epistolary author
  · **edges:** M537 —BEQUEATHS→ RECEPTION; M537 —REPORTS→ M538

**M538** — The content of the knowing: all things collaborate — working together — toward good for those who love God.
  · agent: all things · operation: work together (collaborate — for good, for those who love God) · substrate: not-stated (the good-outcome) · outcome: all things collaborating toward good for those who love God (or, in an alternative reading, God is co-working all things with them for good) · narrator: Paul, first-person epistolary author, ventriloquizing the shared knowledge
  · **edges:** M538 —BEQUEATHS→ RECEPTION; ["M537"] —REPORTS→ M538

**M539** — First descriptor of the beneficiaries: they are the ones who love God.
  · agent: them (the beneficiary-cohort) · operation: love (God — of the beneficiary-cohort) · substrate: God · outcome: the beneficiary-cohort standing as those who love God · narrator: Paul, first-person epistolary author

**M540** — Second descriptor of the beneficiaries: they stand as the summoned-ones, and their summons is according to his purpose.
  · agent: not-stated (God as caller) · operation: be called (be summoned — according to his purpose) · substrate: them (the beneficiary-cohort) · outcome: the beneficiary-cohort standing as called, in accord with God's purpose · narrator: Paul, first-person epistolary author
  · **edges:** M540 —BEQUEATHS→ RECEPTION

**M541** — The first link in the divine action-chain: those whom God had cognitive hold of beforehand.
  · agent: he (God) · operation: foreknow (have advance-knowledge-of) · substrate: whom (the ones foreknown) · outcome: God having advance-cognition of the foreknown-ones · narrator: Paul, first-person epistolary author
  · **edges:** M541 —BEQUEATHS→ RECEPTION

**M542** — The second link: God also fixed their destiny in advance, and fixed it toward becoming shaped-to-match the image of his Son.
  · agent: he (God) · operation: predestinate (fix-destiny-in-advance — to be conformed to the image of his Son) · substrate: the same foreknown-ones (from M6) · outcome: the foreknown-ones fixed by God toward becoming shape-conformed to the image of his Son · narrator: Paul, first-person epistolary author

**M543** — The intended-purpose over the Son-conformity outcome: that the Son himself might stand as firstborn — firstborn among a whole cohort of brothers.
  · agent: he (the Son) · operation: be (firstborn — of the Son, among many brethren) · substrate: not-stated (his standing among the brethren) · outcome: the Son standing as firstborn among many brethren · narrator: Paul, first-person epistolary author

**M544** — The third link: those very ones God had predestined, God also summoned.
  · agent: he (God) · operation: call (summon) · substrate: them (whom he predestinated) · outcome: the predestinated-ones summoned by God · narrator: Paul, first-person epistolary author

**M545** — The fourth link: those whom God had summoned, God also pronounced righteous.
  · agent: he (God) · operation: justify (pronounce righteous) · substrate: them (whom he called) · outcome: the called-ones pronounced righteous by God · narrator: Paul, first-person epistolary author

**M546** — The fifth and terminal link: those whom God had pronounced righteous, God also brought into glory.
  · agent: he (God) · operation: glorify (bring into glory) · substrate: them (whom he justified) · outcome: the justified-ones glorified by God — the eschatological outcome named in the past-tense aorist as if already accomplished · narrator: Paul, first-person epistolary author
  · **edges:** M546 —BEQUEATHS→ RECEPTION

**M547** — Paul opens the triumphal diatribal turn: what response, then, shall we make to all of that?
  · agent: we (Paul with the imagined interlocutor) · operation: say (deliberatively — what shall we say to these things?) · substrate: these things (the M6-M11 chain) · outcome: the deliberation opened · narrator: Paul, first-person epistolary author

**M548** — The first triumphal conditional: given that God stands on our side.
  · agent: God · operation: be (for us — of God, conditional) · substrate: not-stated (our situation) · outcome: God (conditionally) standing for-us / on-our-side · narrator: Paul, first-person epistolary author

**M549** — The rhetorical impossibility-question that follows: who then could possibly be against us?
  · agent: who (interrogated) · operation: be (against us — interrogatively, who can be) · substrate: not-stated (our position) · outcome: the possibility of anyone being against-us put under an impossibility-question · narrator: Paul, first-person epistolary author

**M550** — First descriptor of the God the a-fortiori is about to draw from: he is the one who did not withhold his own Son.
  · agent: he (God) · operation: not spare (not withhold — his own Son) · substrate: his own Son · outcome: God not-having-withheld his own Son · narrator: Paul, first-person epistolary author
  · **edges:** M550 —BEQUEATHS→ RECEPTION

**M551** — The positive counterpart: rather, he handed the Son over — and did so on behalf of all of us.
  · agent: he (God) · operation: deliver up (hand over — for us all) · substrate: him (the Son) · outcome: God having handed the Son over on behalf of all of us · narrator: Paul, first-person epistolary author
  · **edges:** M551 —BEQUEATHS→ RECEPTION

**M552** — The a-fortiori rhetorical question: how then will he possibly not, along with the Son himself, also gift-give us the totality of everything else?
  · agent: he (God) · operation: freely give (gift-give — us all things, together with him, interrogatively) · substrate: us (as beneficiaries) — all things (as substrate given) · outcome: God (interrogatively) not-freely-giving-all-things-with-him — the rhetorical form implying the certainty of the gift · narrator: Paul, first-person epistolary author

**M553** — The second triumphal-question, forensic in shape: who is going to bring a legal-charge against those whom God has chosen?
  · agent: who (interrogated challenger) · operation: lay to the charge (bring-a-legal-charge against — God's elect, interrogatively) · substrate: God's elect · outcome: the possibility of any charge-against-God's-elect put under a rhetorical impossibility · narrator: Paul, first-person epistolary author

**M554** — The answer begins to arrive: it is — [the answer's full form ('God that justifieth') is truncated in the source at 'It is'].
  · agent: not-stated (the answer's subject is truncated at 'it is') · operation: be (— the answer to M18, subject-substrate truncated) · substrate: not-stated (the answer-content is truncated) · outcome: an answer beginning — the source cuts off at 'It is' before the answer-content ('God that justifieth') arrives · narrator: Paul, first-person epistolary author

**M555** — Completing the answer to the prior challenge: it is God — the one who pronounces righteous.
  · agent: God (as the answer's subject) · operation: justify (pronounce righteous — of God, as answer-content) · substrate: not-stated (God's elect from prior M18) · outcome: God identified as the one who pronounces God's elect righteous — the answer to who-shall-lay-charge · narrator: Paul, first-person epistolary author, closing the answer from the prior passage

**M556** — The next triumphal-question in the forensic sequence: who is the one who could pronounce adverse verdict?
  · agent: who (interrogated condemner) · operation: condemn (pronounce adverse verdict — interrogatively, who?) · substrate: not-stated (God's elect as implied would-be substrate of condemnation) · outcome: the possibility of any condemner put under a rhetorical impossibility · narrator: Paul, first-person epistolary author

**M557** — The answer's first characterization: it is the Anointed — the one whose act was dying.
  · agent: Christ (as the answer's subject) · operation: die (of Christ, as answer-descriptor) · substrate: not-stated · outcome: Christ identified as the one who died · narrator: Paul, first-person epistolary author

**M558** — The corrective escalation: or rather — one who has been raised from death.
  · agent: not-stated (God as implicit raiser) · operation: be risen again (be raised from death — as corrective descriptor) · substrate: Christ (implicit) · outcome: Christ standing as raised from death · narrator: Paul, first-person epistolary author

**M559** — Third characterization: the one who is now located at God's right hand.
  · agent: he (Christ) · operation: be (at the right hand of God — of Christ, third descriptor) · substrate: not-stated · outcome: Christ standing at God's right hand · narrator: Paul, first-person epistolary author

**M560** — Fourth characterization: the one who is also stepping in on our behalf.
  · agent: he (Christ) · operation: make intercession (step in — for us) · substrate: not-stated (us as beneficiaries, folded into for-us) · outcome: Christ interceding on our behalf · narrator: Paul, first-person epistolary author
  · **edges:** M560 —BEQUEATHS→ RECEPTION

**M561** — The next triumphal-question: who is going to cut us off from the love that belongs to the Anointed?
  · agent: who (interrogated separator) · operation: separate (cut off — us, from the love of Christ, interrogatively) · substrate: us · outcome: the possibility of any separator-from-Christ's-love put under a rhetorical impossibility · narrator: Paul, first-person epistolary author
  · **edges:** M561 —BEQUEATHS→ RECEPTION

**M562** — The specification-question, listing candidate-separators: shall it be pressure, or narrowness-of-space, or hostile-pursuit, or hunger, or being-stripped, or danger, or the sword?
  · agent: tribulation OR distress OR persecution OR famine OR nakedness OR peril OR sword (the candidate-set) · operation: separate (cut off — us, interrogatively, of a listed set of candidate-forces) · substrate: us (from M7) · outcome: the seven-candidate-list put under the M7 impossibility-question · narrator: Paul, first-person epistolary author

**M563** — Paul appeals to scriptural attestation: as stands written in scripture.
  · agent: not-stated (scripture as authoritative source) · operation: be written (stand as inscribed in scripture — with recoverable content) · substrate: the cited content (M9a and M9b) · outcome: the following claims standing under scriptural warrant · narrator: Paul, first-person epistolary author
  · **edges:** M563 —CONTAINS→ M565; M563 —REPORTS→ M564

**M564** — First part of the cited content: for your sake we undergo being killed — and this goes on all through every day.
  · agent: not-stated (the implicit killers) · operation: be killed (undergo killing — for thy sake, all the day long) · substrate: we (Paul with the psalmic voice) · outcome: we undergoing killing continuously (day-long), for God's sake · narrator: Paul, first-person epistolary author, ventriloquizing Ps 44:22 (LXX 43:23)
  · **edges:** M564 —BEQUEATHS→ RECEPTION; ["M563"] —REPORTS→ M564

**M565** — Second part of the cited content: we are placed into the ledger as sheep destined for slaughter.
  · agent: not-stated (the reckoner) · operation: be accounted (be reckoned — as sheep for the slaughter) · substrate: we (Paul with the psalmic voice) · outcome: we entered into the ledger as sheep-for-slaughter · narrator: Paul, first-person epistolary author, ventriloquizing the second half of the psalmic verse
  · **edges:** ["M563"] —CONTAINS→ M565

**M566** — The triumphal answer: no — in the middle of every one of those things, we come out as more-than-victors, and we do so through the one who has loved us.
  · agent: we · operation: be more than conquerors (super-conquer — in all these things, through him that loved us) · substrate: all these things (the M8-M9b catalogue of sufferings) · outcome: we standing as super-conquerors even in the middle of all these sufferings, mediated through him-who-loved-us · narrator: Paul, first-person epistolary author
  · **edges:** M566 —BEQUEATHS→ RECEPTION

**M567** — Descriptor of the mediator: it is the one whose act toward us was loving us.
  · agent: him (Christ, characterized as loving us) · operation: love (of him — us) · substrate: us · outcome: Christ standing as the one who loved us · narrator: Paul, first-person epistolary author
  · **edges:** M567 —BEQUEATHS→ RECEPTION

**M568** — Paul closes with a settled personal conviction: I have been fully brought over to conviction about the following.
  · agent: I (Paul) · operation: be persuaded (be brought over to settled conviction — with recoverable content) · substrate: the content of the conviction (M12a) · outcome: Paul standing as brought-over to the M12a conviction · narrator: Paul, first-person epistolary author
  · **edges:** M568 —REPORTS→ M569

**M569** — The content of that conviction: neither death, nor life, nor angel-powers, nor principality-powers, nor other powers, nor present-time-things, nor coming-time-things, nor height-region, nor depth-region, nor any other created thing — none of them will be capable of cutting us off from God's love.
  · agent: the ten-fold list: neither death, nor life, nor angels, nor principalities, nor powers, nor things present, nor things to come, nor height, nor depth, nor any other creature · operation: not be able to separate (be incapable — of separating us from the love of God, of the ten-fold cosmic-list) · substrate: us (as substrate of would-be separation) — from the love of God (as source-separator would try to break) · outcome: no member of the cosmic-list capable of separating us from God's love · narrator: Paul, first-person epistolary author, ventriloquizing the settled conviction
  · **edges:** ["M568"] —REPORTS→ M569

**M570** — Descriptor of that love-of-God: it is the love that finds its location in Christ Jesus — [the source cuts off before 'our Lord' arrives to close the letter's climactic sentence].
  · agent: the love of God (from M12a) · operation: be (in Christ Jesus — of the love of God) · substrate: not-stated · outcome: God's love standing as located in Christ Jesus — with the vocative-completion 'our Lord' truncated in the source · narrator: Paul, first-person epistolary author
  · **edges:** M570 —BEQUEATHS→ RECEPTION

**M571** — Completing the closing-vocative from the prior clause: [in Christ Jesus] our Lord.
  · agent: Christ Jesus (from prior clause) · operation: (vocative-completion — 'our Lord', closing the Christ-Jesus name from the ch 8 climax) · substrate: not-stated · outcome: Christ Jesus named as 'our Lord', closing the M13-prior love-of-God-in-Christ-Jesus attribution · narrator: Paul, first-person epistolary author, closing the Christ-Jesus vocative from the prior passage

**M572** — Paul opens the new section with a solemn truth-assertion: I speak truth, and I do so in Christ.
  · agent: I (Paul) · operation: say (assert — the truth, in Christ) · substrate: the truth · outcome: Paul asserting truth, in the register of Christ · narrator: Paul, first-person epistolary author, opening ch 9 with a solemn attestation

**M573** — The negative pair to that assertion: I am not uttering falsehood.
  · agent: I (Paul) · operation: not lie (not utter falsehood) · substrate: not-stated · outcome: Paul standing as not-lying · narrator: Paul, first-person epistolary author

**M574** — The third witness in the oath: my inner moral-witness testifies alongside me, and does so in the Holy Spirit.
  · agent: my conscience · operation: bear witness (co-testify with — me, in the Holy Ghost) · substrate: me (Paul) · outcome: conscience adding its testimony to Paul's assertion, in the Holy Spirit-register · narrator: Paul, first-person epistolary author

**M575** — Paul reports the shocking wish behind the oath: I could bring myself to want the following.
  · agent: I (Paul) · operation: wish (could-wish — with recoverable content) · substrate: the content of the wish (M5a) · outcome: Paul reporting his ability-to-wish the M5a content · narrator: Paul, first-person epistolary author
  · **edges:** M575 —REPORTS→ M576

**M576** — The content of the wish: that I myself would stand under the anathema-curse, cut off from Christ — and that on behalf of my brothers, who are my blood-kin on the fleshly side.
  · agent: not-stated (the implicit curse-imposer) · operation: be accursed (stand under anathema-curse — myself, from Christ, for my brethren) · substrate: myself (Paul) · outcome: Paul (in the wish) standing under anathema-curse, cut off from Christ, done on behalf of his kinsmen-according-to-flesh · narrator: Paul, first-person epistolary author, ventriloquizing the wish-content
  · **edges:** M576 —BEQUEATHS→ RECEPTION; ["M575"] —REPORTS→ M576

**M577** — Descriptor of those kinsmen: they carry the identity 'Israelites'.
  · agent: they (the kinsmen from M5a) · operation: be (Israelites) · substrate: not-stated · outcome: the kinsmen standing as Israelites · narrator: Paul, first-person epistolary author

**M578** — Attribution of the Israel-privileges: to them belongs the son-making, and the glory, and the covenants, and the giving-of-the-torah, and the temple-service, and the promises.
  · agent: the six-fold list: the adoption, and the glory, and the covenants, and the giving of the law, and the service of God, and the promises · operation: pertain (belong to — the adoption, and the glory, and the covenants, and the giving of the law, and the service of God, and the promises) · substrate: not-stated (them as recipients of the belonging) · outcome: the six-fold Israel-privilege-set belonging to the kinsmen-of-M6 · narrator: Paul, first-person epistolary author

**M579** — Further attribution about the kinsmen: whose the fathers are.
  · agent: the fathers (the patriarchs) · operation: be (whose — the fathers, of them) · substrate: not-stated (them as ancestral-line) · outcome: the patriarchs standing as belonging to the kinsmen-of-M6 · narrator: Paul, first-person epistolary author

**M580** — The climactic-privilege attribution: and out of them, on the fleshly-line side, the Anointed himself came into being.
  · agent: Christ · operation: come (originate — of Christ, from them, as concerning the flesh) · substrate: not-stated (his lineage-origin from the kinsmen) · outcome: Christ having originated from the M6-M8 kinsmen, on the fleshly-line · narrator: Paul, first-person epistolary author

**M581** — Descriptor of that Christ: he is the one who is over all things.
  · agent: who (Christ) · operation: be (over all — of Christ) · substrate: all · outcome: Christ standing as over all · narrator: Paul, first-person epistolary author

**M582** — Second descriptor of that Christ (or, in an alternative reading, a separate doxology): God, praised forever.
  · agent: he (Christ, per one KJV reading) OR God (per an alternative reading with different punctuation) · operation: be (God blessed for ever — of Christ, or, as separate doxology, God-standing-as-blessed) · substrate: not-stated · outcome: Christ (or God, depending on punctuation) standing as God, blessed forever · narrator: Paul, first-person epistolary author

**M583** — The sealing-affirmation on the doxological ascription: so-be-it.
  · agent: not-stated (Paul as speaker) · operation: affirm (seal — Amen) · substrate: the M11 doxology (as sealed) · outcome: the M11 ascription sealed with Amen · narrator: Paul, first-person epistolary author

**M584** — Paul denies a possible inference from the Israel-grief: it is not as though God's word has become inoperative.
  · agent: the word of God · operation: not have fallen (not have become inoperative — of the word of God) · substrate: not-stated · outcome: God's word standing as NOT having become-inoperative (denial-form) · narrator: Paul, first-person epistolary author

**M585** — The distinction that grounds the M13 denial: those who are out-of Israel are not, as a body, Israel.
  · agent: they (which are of Israel — the ethnic-Israel cohort) · operation: not be (all Israel — of those which are of Israel) · substrate: not-stated · outcome: the ethnic-Israel cohort NOT identical with all-Israel (in the true sense) · narrator: Paul, first-person epistolary author

**M586** — The parallel distinction on the Abraham-descent axis: they stand as the seed-line of Abraham.
  · agent: they · operation: be (the seed of Abraham — of the ethnic descendants) · substrate: not-stated · outcome: the ethnic descendants standing as the seed-line of Abraham · narrator: Paul, first-person epistolary author

**M587** — The paired negative claim: they are not, on that basis, all children.
  · agent: they (the M15 Abraham-seed cohort) · operation: not be (all children — of the Abraham-seed cohort) · substrate: not-stated · outcome: the Abraham-seed cohort standing as NOT-all-children-of-Abraham (in the promise-sense) · narrator: Paul, first-person epistolary author

**M588** — The corrective scriptural directive that names the true-child-line: in Isaac shall thy seed-line be reckoned.
  · agent: not-stated (God as the caller/reckoner) · operation: be called (be reckoned — thy seed, in Isaac) · substrate: thy seed (Abraham's seed, addressed) · outcome: Abraham's seed reckoned/named in Isaac (rather than in Ishmael or other lines) · narrator: Paul, first-person epistolary author, ventriloquizing Gen 21:12 (LXX)

**M589** — Paul offers his own explanatory paraphrase of the M17 scripture: 'that is' — i.e., here's what it means.
  · agent: not-stated (Paul as speaker) · operation: explain (paraphrase — with recoverable content) · substrate: the M17 scripture (as being paraphrased) · outcome: an exegetical paraphrase of M17 opened, whose content is M18a · narrator: Paul, first-person epistolary author
  · **edges:** M589 —REPORTS→ M590

**M590** — The content of the paraphrase: those persons who are children on the fleshly-line side, these are — [the completing negation, 'not the children of God', is truncated in the source at 'these are'].
  · agent: they which are the children of the flesh (as substrate of the truncated attribution) · operation: not be (the children of God — of the flesh-children, truncated) · substrate: not-stated · outcome: the flesh-children NOT-being-the-children-of-God — the completing predicate ('not the children of God, but the children of the promise are counted for the seed') is truncated in the source at 'these are' · narrator: Paul, first-person epistolary author, ventriloquizing the exegetical content
  · **edges:** ["M589"] —REPORTS→ M590

**M591** — Completing the predicate from the prior clause: [these are] not the children who belong to God.
  · agent: they which are the children of the flesh (from prior clause) · operation: not be (the children of God — of the flesh-children, predicate-completion) · substrate: not-stated · outcome: the flesh-children standing as not-the-children-of-God · narrator: Paul, first-person epistolary author, closing the M18a-prior predicate

**M592** — The contrast: it is the children who are of the promise-line who get placed in the ledger as the seed.
  · agent: not-stated (God as reckoner) · operation: be counted (be reckoned — for the seed, of the promise-children) · substrate: the children of the promise · outcome: the promise-children entered into the ledger as the seed (the true seed-line) · narrator: Paul, first-person epistolary author

**M593** — Paul introduces the scriptural word that shows this promise-line at work: for this next quotation stands as the promise-word.
  · agent: this (the quoted content that follows) · operation: be (the word of promise — of this, quotation-introducer) · substrate: the recoverable content (M4 and M5) · outcome: the following words identified as the promise-word · narrator: Paul, first-person epistolary author
  · **edges:** M593 —CONTAINS→ M595; M593 —REPORTS→ M594

**M594** — First half of the quoted promise-word: at the appointed time I will come.
  · agent: I (God, in direct speech) · operation: come (arrive — at this time, of God, future direct-speech) · substrate: not-stated · outcome: God (in the quoted promise) coming at the appointed time · narrator: Paul, first-person epistolary author, ventriloquizing Gen 18:10 (LXX)
  · **edges:** ["M593"] —REPORTS→ M594

**M595** — Second half of the quoted promise-word: and Sarah will have a son.
  · agent: Sarah · operation: have (bear — a son, of Sarah, future) · substrate: a son · outcome: Sarah (in the quoted promise) having a son (future) · narrator: Paul, first-person epistolary author, ventriloquizing the second half of Gen 18:10
  · **edges:** ["M593"] —CONTAINS→ M595

**M596** — The second case-instance in the argument-sequence: and it is not just that case — but the case where Rebecca too had gotten pregnant, and the pregnancy came about by a single father, namely Isaac.
  · agent: Rebecca · operation: conceive (be pregnant with — by one, of Rebecca, by our father Isaac) · substrate: not-stated (the twins, folded into the pregnancy) · outcome: Rebecca having conceived by a single father (Isaac our father), setting up the twins-case · narrator: Paul, first-person epistolary author

**M597** — First parenthetical-state clause: with the children still standing in the pre-birth condition.
  · agent: not-stated (the not-yet-birth process) · operation: be (not yet born — of the children, past state) · substrate: the children · outcome: the twins standing (past) as not-yet-born, at the moment of the M9 divine purpose · narrator: Paul, first-person epistolary author, in parenthesis

**M598** — Second parenthetical-state clause: nor with the children having yet performed any good or bad act.
  · agent: the children (the twins) · operation: not do (not have performed — any good or evil, of the children, past state) · substrate: any good or evil · outcome: the twins standing (past) as not-having-done any good or evil, at the moment of the M9 divine purpose · narrator: Paul, first-person epistolary author, in parenthesis

**M599** — The purpose that governs the M7-M8 pre-conditions: so that God's plan-according-to-election might remain in force — not on the basis of what one performs, but on the basis of the one who does the calling.
  · agent: the purpose of God (according to election) · operation: stand (remain in force — the purpose of God according to election, not of works, but of him that calleth) · substrate: not-stated · outcome: God's election-purpose standing in force, grounded not in works but in the calling-agent · narrator: Paul, first-person epistolary author
  · **edges:** M599 —BEQUEATHS→ RECEPTION

**M600** — Paul opens the next diatribal-question: what conclusion, then, do we draw?
  · agent: we (Paul with the imagined interlocutor) · operation: say (deliberatively — what shall we say?) · substrate: not-stated (the emerging conclusion) · outcome: the conclusion opened for question · narrator: Paul, first-person epistolary author

**M601** — The theodicy-question that presses on the M9 not-based-on-works election: is there wrongness with God?
  · agent: unrighteousness · operation: be (unrighteousness — with God, interrogatively) · substrate: with God (God's own standing as substrate of the question) · outcome: the possibility of God's unrighteousness put under a rhetorical impossibility · narrator: Paul, first-person epistolary author

**M602** — Paul denies flatly: absolutely not.
  · agent: not-stated (Paul himself as speaker) · operation: may-it-not-be (emphatically deny) · substrate: the M11 possibility · outcome: the M11 unrighteousness-with-God possibility emphatically denied · narrator: Paul, first-person epistolary author

**M603** — The ground for the denial: God addresses a specific utterance to Moses.
  · agent: he (God) · operation: say (utter — to Moses, with recoverable content) · substrate: the content of the utterance (M13a and M13b) · outcome: God having spoken the mercy-formula to Moses · narrator: Paul, first-person epistolary author
  · **edges:** M603 —CONTAINS→ M605; M603 —REPORTS→ M604

**M604** — First half of the quoted divine speech: I will hold mercy toward whomever I hold mercy toward.
  · agent: I (God, in direct speech) · operation: have mercy (show mercy — on whom I will have mercy) · substrate: whom I will have mercy (God's own self-designated recipients) · outcome: God's mercy landing on those God will show mercy to — a tautological-recursive form asserting divine self-sovereignty in mercy · narrator: Paul, first-person epistolary author, ventriloquizing Exod 33:19
  · **edges:** M604 —BEQUEATHS→ RECEPTION; ["M603"] —REPORTS→ M604

**M605** — Paired second half of the quoted divine speech: I will feel compassion toward whomever I feel compassion toward.
  · agent: I (God, in direct speech) · operation: have compassion (show compassion — on whom I will have compassion) · substrate: whom I will have compassion (God's own self-designated recipients) · outcome: God's compassion landing on those God will show compassion to — the parallel tautological-recursive form for oiktirmos alongside eleos · narrator: Paul, first-person epistolary author, ventriloquizing the second clause of Exod 33:19
  · **edges:** M605 —BEQUEATHS→ RECEPTION; ["M603"] —CONTAINS→ M605

**M606** — The conclusion Paul draws from the mercy-formula: therefore the outcome-in-question rests not on the one who wills, and not on the one who runs, but on God — the one who is showing mercy.
  · agent: it (the outcome-in-question, from the M9 election-purpose) · operation: be (of God that showeth mercy — not of him that willeth, nor of him that runneth, of the outcome-in-question) · substrate: not-stated · outcome: the outcome sourced in God-who-shows-mercy, not in the will-agent or the run-agent · narrator: Paul, first-person epistolary author

**M607** — Paul brings in a second scriptural voice: the scripture makes an utterance addressed to Pharaoh.
  · agent: the scripture · operation: say (utter — to Pharaoh, with recoverable content) · substrate: the content of the utterance (M15a, truncated) · outcome: scripture's utterance addressed to Pharaoh — with the content M15a beginning but truncated · narrator: Paul, first-person epistolary author
  · **edges:** M607 —REPORTS→ M608

**M608** — The content of the scripture's utterance begins: 'for this very [purpose I have raised you up — the completing verb-and-object is truncated in the source at 'even for this same'].
  · agent: I (God, in direct speech, per Exod 9:16 continuation) · operation: (unstated verb — 'for this very [purpose I have raised thee up]', truncated at 'even for this same') · substrate: thee (Pharaoh) — 'for this very purpose', truncated before verb arrives · outcome: the divine address to Pharaoh 'even for this same [purpose have I raised thee up]' — the completing verb-and-object is truncated in the source · narrator: Paul, first-person epistolary author, ventriloquizing Exod 9:16
  · **edges:** ["M607"] —REPORTS→ M608

**M609** — Completing the divine address from the prior clause: [for this very] purpose I have brought you up onto the stage.
  · agent: I (God, in direct speech) · operation: raise up (bring onto the stage — thee, for this same purpose) · substrate: thee (Pharaoh) · outcome: Pharaoh brought onto the stage by God, for the very purpose the following clauses will name · narrator: Paul, first-person epistolary author, closing the Exod 9:16 quotation from the prior passage
  · **edges:** M609 —BEQUEATHS→ RECEPTION

**M610** — First purpose of that raising: so that I might exhibit my power inside you.
  · agent: I (God, in direct speech) · operation: shew (exhibit, display — my power, in thee) · substrate: my power · outcome: God's power exhibited in Pharaoh · narrator: Paul, first-person epistolary author, ventriloquizing Exod 9:16
  · **edges:** M610 —BEQUEATHS→ RECEPTION

**M611** — Second purpose: and so that my name might be proclaimed across the whole earth.
  · agent: not-stated (the implicit proclaimers) · operation: be declared (be proclaimed — my name, throughout all the earth) · substrate: my name · outcome: God's name proclaimed across the whole earth · narrator: Paul, first-person epistolary author, ventriloquizing Exod 9:16

**M612** — Paul draws the inference from the Moses-mercy and Pharaoh-purpose passages: therefore God shows mercy toward whichever party he wills to show mercy toward.
  · agent: he (God) · operation: have mercy (show mercy — on whom he will have mercy) · substrate: whom he will have mercy (God's self-designated recipients) · outcome: God showing mercy sovereignly, according to his own will · narrator: Paul, first-person epistolary author
  · **edges:** M612 —BEQUEATHS→ RECEPTION

**M613** — The paired inference on the hardening-side: and whichever party he wills, he makes hard.
  · agent: he (God) · operation: harden (make hard — whom he will) · substrate: whom he will (God's self-designated hardening-recipients) · outcome: God hardening sovereignly, according to his own will · narrator: Paul, first-person epistolary author
  · **edges:** M613 —BEQUEATHS→ RECEPTION

**M614** — Paul anticipates the interlocutor's objection: you will address me with the following question.
  · agent: thou (the anticipated interlocutor) · operation: say (address me — with recoverable content) · substrate: the content of the interlocutor's question (M6a and M6b) · outcome: the interlocutor's objection anticipated and quoted · narrator: Paul, first-person epistolary author, ventriloquizing the imagined objector
  · **edges:** M614 —CONTAINS→ M616; M614 —REPORTS→ M615

**M615** — The interlocutor's first question: why then does he still find fault?
  · agent: he (God, as interrogated fault-finder) · operation: find fault (bring blame — interrogatively, why yet) · substrate: not-stated (the fault-substrate) · outcome: God's continuing to find-fault put in question by the objector · narrator: Paul, first-person epistolary author, ventriloquizing the objector's first question
  · **edges:** ["M614"] —REPORTS→ M615

**M616** — The interlocutor's second question, supporting the first: for who has ever stood-against his will?
  · agent: who (interrogated as would-be resister) · operation: resist (stand-against — his will, interrogatively, who) · substrate: his will (God's will) · outcome: the possibility of anyone having-resisted-God's-will put under impossibility-question · narrator: Paul, first-person epistolary author, ventriloquizing the objector's supporting question
  · **edges:** M616 —BEQUEATHS→ RECEPTION; ["M614"] —CONTAINS→ M616

**M617** — Paul's sharp rebuke to the objector, with apostrophe: no, rather — O human, who exactly are you to talk back to God?
  · agent: thou (O man, the objector) · operation: be (who — of thou, interrogatively, identity-challenge) · substrate: not-stated (thy standing to talk back) · outcome: the objector's standing to talk back to God put under identity-challenge · narrator: Paul, first-person epistolary author, in diatribal apostrophe
  · **edges:** M617 —BEQUEATHS→ RECEPTION

**M618** — Descriptor of that O-man: the one who talks back against God.
  · agent: thou (the objector) · operation: reply against (talk back to — God) · substrate: God · outcome: the objector standing as one who talks back against God · narrator: Paul, first-person epistolary author
  · **edges:** M618 —BEQUEATHS→ RECEPTION

**M619** — The potter-clay rhetorical question, matrix-form: shall the thing that has been shaped speak back to the one who shaped it — with a certain question?
  · agent: the thing formed · operation: say (speak back — to him that formed it, interrogatively, with recoverable content) · substrate: him that formed it (the former, God-figure) · outcome: the possibility of the formed-thing speaking back to the former put in question · narrator: Paul, first-person epistolary author
  · **edges:** M619 —BEQUEATHS→ RECEPTION; M619 —REPORTS→ M620

**M620** — The content of the formed-thing's would-be speech: why have you made me in this specific way?
  · agent: thou (the former, addressed by the formed thing) · operation: make (of thou, the former — me, thus, interrogatively) · substrate: me (the formed thing) · outcome: the former's shaping-of-me put in question by the formed thing · narrator: Paul, first-person epistolary author, ventriloquizing the formed-thing's would-be question
  · **edges:** M620 —BEQUEATHS→ RECEPTION; ["M619"] —REPORTS→ M620

**M621** — Descriptor of the former: the one whose act was to shape it.
  · agent: he (the former, God-figure) · operation: form (shape — of him, it) · substrate: it (the thing formed) · outcome: the former having shaped the formed thing · narrator: Paul, first-person epistolary author
  · **edges:** M621 —BEQUEATHS→ RECEPTION

**M622** — The next rhetorical question in the potter-analogy chain: does not the potter have jurisdiction over the clay?
  · agent: the potter · operation: have (hold — power over the clay, interrogatively) · substrate: the clay · outcome: the potter's jurisdiction over clay put as rhetorically-affirmed · narrator: Paul, first-person epistolary author
  · **edges:** M622 —BEQUEATHS→ RECEPTION

**M623** — The purpose that fills the potter-jurisdiction: to shape, from the very same lump of clay, one container aimed at honored-use and another aimed at dishonored-use.
  · agent: the potter (from M11) · operation: make (shape — from the same lump, one vessel unto honour and another unto dishonour) · substrate: the same lump (of clay) · outcome: one vessel shaped for honored-use, and another vessel shaped for dishonored-use, from a single lump · narrator: Paul, first-person epistolary author
  · **edges:** M623 —BEQUEATHS→ RECEPTION

**M624** — First conditional-premise the analogy applies to God: given that God wills to display his anger.
  · agent: God · operation: be willing (want — to show his wrath, conditional) · substrate: not-stated (the willing-object is the shew-wrath infinitival) · outcome: God (in the hypothetical) willing to display his wrath · narrator: Paul, first-person epistolary author
  · **edges:** M624 —BEQUEATHS→ RECEPTION

**M625** — Second coordinate will-clause: and given that God wills also to make his power something known.
  · agent: God · operation: be willing (want — to make his power known, conditional) · substrate: not-stated (the willing-object is the make-power-known infinitival) · outcome: God (in the hypothetical) willing to make his power known · narrator: Paul, first-person epistolary author
  · **edges:** M625 —BEQUEATHS→ RECEPTION

**M626** — The main-clause consequent of the hypothetical: [God] put up with the vessels destined for wrath — put up with them, and did so with abundant staying-under-endurance.
  · agent: God (implicit from M13-M14) · operation: endure (put up with — with much longsuffering, the vessels of wrath) · substrate: the vessels of wrath · outcome: God bearing with the wrath-vessels through much longsuffering · narrator: Paul, first-person epistolary author
  · **edges:** M626 —BEQUEATHS→ RECEPTION

**M627** — Descriptor of the wrath-vessels: they are the ones prepared-for-destruction.
  · agent: not-stated (the implicit preparer, whose identity is deliberately left open) · operation: be fitted (be prepared — for destruction, of the wrath-vessels) · substrate: the vessels of wrath · outcome: the wrath-vessels standing as prepared-for-destruction (katērtismena — perfect-participle continuing-state) · narrator: Paul, first-person epistolary author
  · **edges:** M627 —BEQUEATHS→ RECEPTION

**M628** — The further purpose held out over the M15 forbearance: and that he might make the wealth of his glory something known — on the [vessels of mercy, per the truncated continuation of Rom 9:23].
  · agent: he (God) · operation: make known (make known — the riches of his glory, on the [vessels of mercy, truncated]) · substrate: the riches of his glory · outcome: God (in the purpose) making his glory-riches known on the [vessels of mercy, per Rom 9:23 continuation — the specifying substrate-completion is truncated at 'on the'] · narrator: Paul, first-person epistolary author

**M629** — Completing the substrate from the prior clause: [on the] vessels of mercy.
  · agent: not-stated (God as glory-revealer, from prior) · operation: (substrate-completion — 'vessels of mercy', identifying the M17-prior recipients of the glory-display) · substrate: vessels of mercy (as substrate on which the glory is displayed) · outcome: the M17-prior glory-display locating on the vessels-of-mercy specifically · narrator: Paul, first-person epistolary author, closing the substrate-completion from the prior passage

**M630** — Descriptor of those mercy-vessels: they are the ones God pre-prepared, and the direction of the preparation was glory.
  · agent: he (God) · operation: prepare afore (pre-prepare — unto glory) · substrate: the vessels of mercy (from M1) · outcome: the mercy-vessels pre-prepared by God, aimed at glory · narrator: Paul, first-person epistolary author
  · **edges:** M630 —BEQUEATHS→ RECEPTION

**M631** — The identification that lands the whole potter-and-vessels argument on the addressees: even us — that's who those mercy-vessels turn out to be.
  · agent: the mercy-vessels (from M1-M2) · operation: be (identical with — us, of the mercy-vessels) · substrate: us (Paul with the addressees) · outcome: the mercy-vessels identified with the first-person cohort ('us') · narrator: Paul, first-person epistolary author

**M632** — Descriptor of that us-cohort: we are the ones God has summoned.
  · agent: he (God) · operation: call (summon — us) · substrate: us (whom) · outcome: the us-cohort standing as those God has summoned · narrator: Paul, first-person epistolary author

**M633** — The scope-specification of who counts among that called-us: not from the Jew-cohort alone, but also from the gentile-cohort.
  · agent: he (God, implicit from M4) · operation: call (summon — us, scope-specification: not only of Jews, but also of Gentiles) · substrate: not of the Jews only, but also of the Gentiles (as scope-set) · outcome: the M4 calling scoped to include both Jews and Gentiles · narrator: Paul, first-person epistolary author

**M634** — Paul cites Hosea as scriptural attestation: he also speaks the following in Hosea.
  · agent: he (God, as speaker through Hosea) · operation: say (utter — in Hosea, with recoverable content) · substrate: the content of the utterance (M6a-M6d nested) · outcome: God (through Hosea) uttering the M6a-M6d content · narrator: Paul, first-person epistolary author
  · **edges:** M634 —CONTAINS→ M636; M634 —CONTAINS→ M637; M634 —CONTAINS→ M638; M634 —REPORTS→ M635

**M635** — First quoted line: I will name them — as my people.
  · agent: I (God, in direct speech) · operation: call (name — them, as my people, future) · substrate: them (the not-my-people who become my-people) · outcome: God (future) naming them as his people · narrator: Paul, first-person epistolary author, ventriloquizing Hos 2:23
  · **edges:** M635 —BEQUEATHS→ RECEPTION; ["M634"] —REPORTS→ M635

**M636** — Descriptor of that same 'them': they used to stand as not-my-people.
  · agent: them (the same 'them' from M6a) · operation: not be (my people — of them, past-state descriptor) · substrate: not-stated · outcome: the same 'them' having (past) not been my-people · narrator: Paul, first-person epistolary author, ventriloquizing Hosea
  · **edges:** M636 —BEQUEATHS→ RECEPTION; ["M634"] —CONTAINS→ M636

**M637** — Second parallel quoted line: and I will name her — as beloved.
  · agent: I (God, in direct speech, implicit from M6a) · operation: call (name — her, as beloved, future, elided verb from M6a) · substrate: her (the not-beloved who becomes beloved) · outcome: God (future) naming her as beloved · narrator: Paul, first-person epistolary author, ventriloquizing the second half of Hos 2:23
  · **edges:** M637 —BEQUEATHS→ RECEPTION; ["M634"] —CONTAINS→ M637

**M638** — Descriptor of that same 'her': she used to stand as not-beloved.
  · agent: not-stated · operation: not be (beloved — of her, past-state descriptor) · substrate: her (the same 'her' from M6c) · outcome: the same 'her' having (past) not been beloved · narrator: Paul, first-person epistolary author, ventriloquizing Hosea
  · **edges:** M638 —BEQUEATHS→ RECEPTION; ["M634"] —CONTAINS→ M638

**M639** — Second Hosea citation-introducer: and it will come about, that in a specific place — [namely the place where the following was said, then this will happen].
  · agent: it (the coming-about event) · operation: come to pass (be, come-about — with recoverable content) · substrate: the content of what will come to pass (M9) · outcome: the following M9 event coming to pass · narrator: Paul, first-person epistolary author, ventriloquizing Hos 1:10 LXX
  · **edges:** M639 —CONTAINS→ M640; M639 —REPORTS→ M642

**M640** — The location-marker embedded in the eventuation: the place where the past-saying went out to them saying 'you are not my people'.
  · agent: not-stated (the past-sayer, God through prophets) · operation: say (be said — unto them, past, with recoverable content) · substrate: them (the sayer's addressees) — the content of the saying (M8a) · outcome: the past-saying located in a specific place · narrator: Paul, first-person epistolary author, ventriloquizing the past-saying-clause within the Hos 1:10 quotation
  · **edges:** M640 —REPORTS→ M641; ["M639"] —CONTAINS→ M640

**M641** — The content of that past-saying: you are not my people.
  · agent: ye (them, addressed) · operation: not be (my people — of them, past-attribution) · substrate: not-stated · outcome: the addressees (in the past-saying) attributed as not-my-people · narrator: Paul, first-person epistolary author, doubly-ventriloquizing the past divine saying
  · **edges:** M641 —BEQUEATHS→ RECEPTION; ["M640"] —REPORTS→ M641

**M642** — The main future-eventuation content: right there, in that same place, they will be called by name as sons of the living God.
  · agent: not-stated (God as caller-namer) · operation: be called (be named — the children of the living God, in that place, future) · substrate: they (the same 'them' from M8) · outcome: the addressees (future) named as children of the living God, in the same place where the M8a rejection was spoken · narrator: Paul, first-person epistolary author, ventriloquizing the main clause of Hos 1:10 LXX
  · **edges:** M642 —BEQUEATHS→ RECEPTION; ["M639"] —REPORTS→ M642

**M643** — Paul brings in Isaiah as a second scriptural witness: Isaiah also raises his voice concerning Israel with the following.
  · agent: Isaiah · operation: cry (raise one's voice — concerning Israel, with recoverable content) · substrate: the content of the crying (M11 and following) · outcome: Isaiah raising his voice about Israel with the M11-following content · narrator: Paul, first-person epistolary author
  · **edges:** M643 —CONTAINS→ M644; M643 —CONTAINS→ M646; M643 —CONTAINS→ M647; M643 —CONTAINS→ M648; M643 —REPORTS→ M645

**M644** — First half of the Isaiah citation, concessive: even though the count of Israel's children reaches the size of sea-sand.
  · agent: the number of the children of Israel · operation: be (as the sand of the sea — of the number of Israel's children, concessive) · substrate: not-stated (the comparison-substrate) · outcome: Israel's-children-count standing as sea-sand-numerous (the abundance-descriptor against which the M12 remnant registers) · narrator: Paul, first-person epistolary author, ventriloquizing Isa 10:22 LXX
  · **edges:** ["M643"] —CONTAINS→ M644

**M645** — The main-clause of the Isaiah citation: a remnant-portion is the one that will be rescued.
  · agent: not-stated (God as saver) · operation: be saved (be rescued — a remnant, future) · substrate: a remnant (kataleimma / hypoleimma) · outcome: a remnant-portion (future) rescued from the M11 abundance · narrator: Paul, first-person epistolary author, ventriloquizing Isa 10:22 LXX
  · **edges:** M645 —BEQUEATHS→ RECEPTION; ["M643"] —REPORTS→ M645

**M646** — The ground for the remnant-saving: for he will bring the plan to completion.
  · agent: he (the Lord, from Isaiah) · operation: finish (bring to completion — the work) · substrate: the work · outcome: the Lord bringing the plan-work to completion · narrator: Paul, first-person epistolary author, ventriloquizing the continuation of Isa 10:22-23
  · **edges:** ["M643"] —CONTAINS→ M646

**M647** — Coordinate ground: and he will cut it short — and do so in the register of righteousness.
  · agent: he (the Lord) · operation: cut short (curtail — in righteousness) · substrate: it (the work, implicit from M13) · outcome: the Lord curtailing the work in the righteousness-register · narrator: Paul, first-person epistolary author, ventriloquizing the continuation of Isaiah
  · **edges:** M647 —BEQUEATHS→ RECEPTION; ["M643"] —CONTAINS→ M647

**M648** — Further ground: because it is a short, cut-off work that the Lord is going to make happen on the earth.
  · agent: the Lord · operation: make (bring about — a short work, upon the earth) · substrate: a short work · outcome: the Lord bringing about a short/decisive work upon the earth · narrator: Paul, first-person epistolary author, ventriloquizing the continuation of Isa 10:23
  · **edges:** M648 —BEQUEATHS→ RECEPTION; ["M643"] —CONTAINS→ M648

**M649** — Paul cites Isaiah a second time, from an earlier place: and as Isaiah has said in an earlier passage.
  · agent: Isaiah · operation: say (speak — in an earlier passage, with recoverable content) · substrate: the content of the earlier-said (M16a-M16c) · outcome: Isaiah's earlier-passage utterance quoted · narrator: Paul, first-person epistolary author
  · **edges:** M649 —CONTAINS→ M651; M649 —CONTAINS→ M652; M649 —REPORTS→ M650

**M650** — First half of the earlier Isaiah quotation, contrary-to-fact conditional: if not for the fact that the Lord of Armies had reserved us a seed-remnant.
  · agent: the Lord of Sabaoth (the Lord of Armies) · operation: leave (reserve — us, a seed, contrary-to-fact conditional) · substrate: us (the addressees / community) — a seed (as reserved-portion) · outcome: the Lord of Armies having (in the counter-factual) reserved a seed for us · narrator: Paul, first-person epistolary author, ventriloquizing Isa 1:9 LXX
  · **edges:** M650 —BEQUEATHS→ RECEPTION; ["M649"] —REPORTS→ M650

**M651** — First apodosis-clause: we would have ended up as Sodom.
  · agent: we · operation: be (as Sodom — of us, counter-factual apodosis) · substrate: as Sodom (the comparison-substrate) · outcome: we (in the counter-factual) standing as Sodom · narrator: Paul, first-person epistolary author, ventriloquizing the second half of Isa 1:9 LXX
  · **edges:** ["M649"] —CONTAINS→ M651

**M652** — Second apodosis-clause: and would have been made resembling [Gomorrah — the second comparison-city is truncated in the source at 'like unto'].
  · agent: not-stated (the implicit renderer in the counter-factual) · operation: be made (be rendered — like unto [Gomorrah, truncated], counter-factual) · substrate: we · outcome: we (in the counter-factual) rendered like unto [Gomorrah, per Isa 1:9 continuation — the second comparison-city is truncated in the source at 'like unto'] · narrator: Paul, first-person epistolary author, ventriloquizing the third clause of Isa 1:9
  · **edges:** ["M649"] —CONTAINS→ M652

**M653** — Completing the second comparison-city from the prior clause: [like unto] Gomorrah.
  · agent: not-stated (the counter-factual renderer, from prior) · operation: (substrate-completion — 'Gomorrah', identifying the second twin-city of the M16c-prior counter-factual) · substrate: Gomorrah (as second comparison-city) · outcome: we (in the counter-factual) rendered like Gomorrah, completing the Sodom-and-Gomorrah pair · narrator: Paul, first-person epistolary author, closing the Gomorrah-completion from the prior passage

**M654** — Paul opens the next diatribal turn: what conclusion, then, are we to draw?
  · agent: we (Paul with the imagined interlocutor) · operation: say (deliberatively — what shall we say?) · substrate: not-stated (the emerging conclusion) · outcome: the conclusion opened for question · narrator: Paul, first-person epistolary author

**M655** — The paradoxical answer, main-claim: the Gentiles have caught up with righteousness — attained it.
  · agent: the Gentiles · operation: attain (catch up with, reach — righteousness) · substrate: righteousness · outcome: the Gentiles having caught up with righteousness · narrator: Paul, first-person epistolary author

**M656** — Descriptor of the Gentiles that sharpens the paradox: they are the ones who did not pursue after righteousness.
  · agent: the Gentiles · operation: not follow after (not pursue — righteousness) · substrate: righteousness · outcome: the Gentiles standing as ones who did not pursue righteousness · narrator: Paul, first-person epistolary author

**M657** — Specification of the righteousness the Gentiles attained: namely the righteousness that has trust as its ground.
  · agent: the righteousness (from M3) · operation: be (of faith — of the attained-righteousness, specification) · substrate: not-stated (the mode-of-grounding) · outcome: the attained-righteousness identified specifically as the faith-mode righteousness · narrator: Paul, first-person epistolary author

**M658** — Descriptor of Israel: they are the ones who did pursue the law of righteousness.
  · agent: Israel · operation: follow after (pursue — the law of righteousness) · substrate: the law of righteousness · outcome: Israel standing as ones who pursued the law-of-righteousness · narrator: Paul, first-person epistolary author

**M659** — The paradoxical result on Israel's side: they have not caught up with the law of righteousness.
  · agent: Israel · operation: not attain (not reach — the law of righteousness) · substrate: the law of righteousness · outcome: Israel standing as ones who did not attain the law-of-righteousness despite pursuing it · narrator: Paul, first-person epistolary author

**M660** — The follow-up question: why?
  · agent: we (Paul with the interlocutor, implicit) · operation: say (deliberatively — why?) · substrate: not-stated (the reason for M7) · outcome: the M7 reason opened for question · narrator: Paul, first-person epistolary author

**M661** — The answer, contrastive: because they sought it not on the ground of trust, but as though on the ground of law-performances.
  · agent: they (Israel from M7) · operation: seek (pursue — it, not by faith, but as by works of the law) · substrate: it (the law-of-righteousness, from M7) · outcome: Israel's seeking the law-of-righteousness not by-faith but as-if by-works · narrator: Paul, first-person epistolary author
  · **edges:** M661 —BEQUEATHS→ RECEPTION

**M662** — The specific event underlying that failure: they tripped against the stumbling-stone.
  · agent: they (Israel) · operation: stumble (trip against — the stumblingstone) · substrate: that stumblingstone · outcome: Israel having tripped against the stumbling-stone · narrator: Paul, first-person epistolary author
  · **edges:** M662 —BEQUEATHS→ RECEPTION

**M663** — Paul appeals to scriptural warrant: as it is written in scripture.
  · agent: not-stated (scripture as authoritative source) · operation: be written (stand as inscribed in scripture — with recoverable content) · substrate: the cited content (M11a and M13) · outcome: the following claims standing under scriptural warrant · narrator: Paul, first-person epistolary author
  · **edges:** M663 —BEQUEATHS→ RECEPTION; M663 —CONTAINS→ M665; M663 —CONTAINS→ M666; M663 —REPORTS→ M664

**M664** — First quoted content: attention — I am placing in Zion something that trips people and a rock that offends.
  · agent: I (God, in direct speech) · operation: lay (place — in Sion, a stumblingstone and a rock of offence) · substrate: a stumblingstone and rock of offence · outcome: God placing in Zion a stone-of-stumbling that is also a rock-of-offence · narrator: Paul, first-person epistolary author, ventriloquizing the mixed Isaiah quotation
  · **edges:** ["M663"] —REPORTS→ M664

**M665** — Descriptor of the subject of the M13 promise: anyone at all who places trust in him.
  · agent: whosoever (whoever) · operation: believe (place trust — on him) · substrate: him (the stone / Christ) · outcome: the believer-on-him standing as the subject-cohort for the M13 promise · narrator: Paul, first-person epistolary author, ventriloquizing the continuation of Isa 28:16
  · **edges:** M665 —BEQUEATHS→ RECEPTION; ["M663"] —CONTAINS→ M665

**M666** — The promise-content: that person will not undergo shaming.
  · agent: not-stated (the implicit shame-source, negated) · operation: not be ashamed (not be put to shame — the believer, future) · substrate: he (the believer from M12) · outcome: the believer (future) not being put to shame · narrator: Paul, first-person epistolary author, ventriloquizing Isa 28:16 LXX
  · **edges:** M666 —BEQUEATHS→ RECEPTION; ["M663"] —CONTAINS→ M666

**M667** — Paul addresses his readers with a kinship-vocative and reports the shape of his own heart-and-prayer: brothers, what my heart most-wants and my prayer to God is directed at is a specific goal — this one.
  · agent: my heart's desire and prayer to God (for Israel) · operation: be (of my heart's desire and prayer — for Israel, with recoverable content) · substrate: the content of the desire-and-prayer (M14a) · outcome: Paul's heart's-desire and prayer to God directed at the M14a content, on behalf of Israel · narrator: Paul, first-person epistolary author, opening ch 10 with kinship-address and personal-report
  · **edges:** M667 —REPORTS→ M668

**M668** — The content of the heart's-desire and the prayer: that they should undergo being rescued.
  · agent: not-stated (God as implicit saver) · operation: be saved (be rescued — of them / Israel) · substrate: they (Israel) · outcome: Israel (in the intended-content) rescued · narrator: Paul, first-person epistolary author, ventriloquizing his own desire-and-prayer-content
  · **edges:** ["M667"] —REPORTS→ M668

**M669** — Paul offers his own testimony about Israel: I stand as witness for the following about them.
  · agent: I (Paul) · operation: bear record (testify — concerning them, with recoverable content) · substrate: the content of the testimony (M15a) · outcome: Paul giving testimony about Israel's zeal-and-knowledge-condition · narrator: Paul, first-person epistolary author
  · **edges:** M669 —REPORTS→ M670

**M670** — The content of that testimony: they hold a burning-zeal directed at God — but the zeal does not run according to the register of knowledge.
  · agent: they (Israel) · operation: have (possess — a zeal of God, but not according to knowledge) · substrate: a zeal of God (a burning-zeal directed at God) · outcome: Israel possessing zeal-for-God, but the zeal-mode failing to accord with knowledge-mode · narrator: Paul, first-person epistolary author, ventriloquizing his testimony
  · **edges:** ["M669"] —REPORTS→ M670

**M671** — First participial-ground explaining that mismatch: they stand in a state of not-recognizing God's own righteousness.
  · agent: they (Israel) · operation: be ignorant (not-recognize — of God's righteousness) · substrate: God's righteousness · outcome: Israel standing as ones who do not recognize God's righteousness · narrator: Paul, first-person epistolary author
  · **edges:** M671 —BEQUEATHS→ RECEPTION

**M672** — Second participial-ground: and they stand going about [to establish their own righteousness — the completing verb-and-object is truncated in the source at 'going'].
  · agent: they (Israel) · operation: go about (be-in-the-act-of — with truncated verb-and-object) · substrate: not-stated (the truncated verb's object — 'their own righteousness' per Rom 10:3 continuation) · outcome: Israel (in the on-going state) doing something the source truncates at 'going' — per the KJV continuation, going-about-to-establish-their-own-righteousness · narrator: Paul, first-person epistolary author

**M673** — Completing the verb-and-object from the prior clause: [going] about to set up their own righteousness.
  · agent: they (Israel, from prior) · operation: establish (set up — their own righteousness, completion of on-going-action) · substrate: their own righteousness · outcome: Israel setting up their own righteousness (as opposed to receiving God's) · narrator: Paul, first-person epistolary author, closing the going-about-to-establish from the prior passage

**M674** — The main-verb consequent: they have refused to place themselves under God's righteousness.
  · agent: they (Israel) · operation: not submit (not place-oneself-under — the righteousness of God) · substrate: themselves — to the righteousness of God · outcome: Israel standing as ones who did not place themselves under God's righteousness · narrator: Paul, first-person epistolary author

**M675** — The Christological correction: because the Anointed is the terminus of the law — with respect to righteousness, and for every person who trusts.
  · agent: Christ · operation: be (the end of the law — of Christ, for righteousness, to every believer) · substrate: not-stated (the law-relation) · outcome: Christ standing as the telos of the law, for righteousness, extended to every believer · narrator: Paul, first-person epistolary author

**M676** — Descriptor of the beneficiary-cohort: it is every person who exercises trust.
  · agent: every one (the beneficiary-cohort) · operation: believe (exercise trust) · substrate: not-stated (Christ / the gospel as object of trust, implicit) · outcome: every-believer standing as the beneficiary-cohort for M3's Christ-terminus-of-law · narrator: Paul, first-person epistolary author

**M677** — Paul brings in Moses's characterization of the law-side of righteousness: Moses describes it in the following way.
  · agent: Moses · operation: describe (give an account of — the righteousness which is of the law, with recoverable content) · substrate: the righteousness which is of the law (as topic) — the content of the description (M5a and M5b) · outcome: Moses giving verbal shape to the law-side of righteousness · narrator: Paul, first-person epistolary author
  · **edges:** M677 —CONTAINS→ M679; M677 —REPORTS→ M678

**M678** — First half of the described content: the person who performs those very things.
  · agent: the man (indefinite subject) · operation: do (perform — those things) · substrate: those things (the law's requirements) · outcome: the person standing as one who performs the law's requirements · narrator: Paul, first-person epistolary author, ventriloquizing Lev 18:5 LXX
  · **edges:** ["M677"] —REPORTS→ M678

**M679** — The apodosis-promise: that person will find his life through those things.
  · agent: the man (from M5a) · operation: live (find life — by them, future) · substrate: not-stated (his life-source) · outcome: the law-performer (future) living by those things (the law's requirements) · narrator: Paul, first-person epistolary author, ventriloquizing Lev 18:5 LXX
  · **edges:** ["M677"] —CONTAINS→ M679

**M680** — Paul now personifies the alternative-side and reports how it speaks: the righteousness that operates by trust speaks in the following manner.
  · agent: the righteousness which is of faith (personified as speaker) · operation: speak (utter — on this wise, with recoverable content) · substrate: the content of its speech (M7-M12a nested) · outcome: the righteousness-of-faith speaking the M7-M12a Deut-30-with-gloss content · narrator: Paul, first-person epistolary author
  · **edges:** M680 —BEQUEATHS→ RECEPTION; M680 —CONTAINS→ M685; M680 —REPORTS→ M681

**M681** — First quoted directive-content: don't utter in your own heart the following question.
  · agent: thou (addressed) · operation: not say (imperative-negation — in thine heart, with recoverable content) · substrate: the content of the forbidden saying (M7a) — in thine heart · outcome: the addressee directed not to utter the M7a content in the heart · narrator: Paul, first-person epistolary author, ventriloquizing Deut 30:12-14 (LXX)
  · **edges:** M681 —REPORTS→ M682; ["M680"] —REPORTS→ M681

**M682** — The content of the forbidden saying: who will go up into heaven?
  · agent: who (interrogated ascender) · operation: ascend (go up — into heaven, interrogatively) · substrate: not-stated (heaven as destination) · outcome: the ascending-into-heaven question posed within the forbidden speech · narrator: Paul, first-person epistolary author, doubly-ventriloquizing
  · **edges:** M682 —BEQUEATHS→ RECEPTION; ["M681"] —REPORTS→ M682

**M683** — Paul offers his own exegetical gloss on that ascend-question: that is — in explanation — here's what it would come to.
  · agent: not-stated (Paul as speaker) · operation: explain (paraphrase — with recoverable content) · substrate: the M7a question (as being glossed) — the content of the gloss (M8a) · outcome: Paul's exegetical gloss on the ascend-question delivered · narrator: Paul, first-person epistolary author, in exegetical mode
  · **edges:** M683 —REPORTS→ M684

**M684** — The content of Paul's gloss: [asking that would amount] to bringing the Anointed down from up-above.
  · agent: the-implied-ascender (from M7a's question) · operation: bring down (bring — Christ down from above) · substrate: Christ · outcome: the imagined ascend-action equated with bringing Christ down from above · narrator: Paul, first-person epistolary author, ventriloquizing his own gloss-content
  · **edges:** M684 —BEQUEATHS→ RECEPTION; ["M683"] —REPORTS→ M684

**M685** — The second forbidden-question in the paired formulation: or [don't utter in the heart] the following question.
  · agent: thou (addressed) · operation: not say (elided imperative-negation — with recoverable content, second forbidden question) · substrate: the content of the second forbidden saying (M9a) — in thine heart, elided · outcome: the addressee directed not to utter the second forbidden question either · narrator: Paul, first-person epistolary author, ventriloquizing the paired Deut 30:13 forbidden question
  · **edges:** M685 —REPORTS→ M686; ["M680"] —CONTAINS→ M685

**M686** — The content of the second forbidden saying: who will descend into the depth?
  · agent: who (interrogated descender) · operation: descend (go down — into the deep, interrogatively) · substrate: not-stated (the deep as destination) · outcome: the descending-into-the-deep question posed within the second forbidden speech · narrator: Paul, first-person epistolary author, doubly-ventriloquizing
  · **edges:** ["M685"] —REPORTS→ M686

**M687** — Paul's exegetical gloss on the descend-question: that is — [asking that would amount to] the following.
  · agent: not-stated (Paul as speaker) · operation: explain (paraphrase — with recoverable content, second gloss) · substrate: the M9a question (as being glossed) — the content of the gloss (M10a) · outcome: Paul's exegetical gloss on the descend-question delivered · narrator: Paul, first-person epistolary author, in exegetical mode
  · **edges:** M687 —REPORTS→ M688

**M688** — The content of Paul's second gloss: [asking that would amount] to bringing the Anointed back up out of the dead.
  · agent: the-implied-descender (from M9a's question) · operation: bring up (raise — Christ again, from the dead) · substrate: Christ · outcome: the imagined descend-action equated with bringing Christ up from the dead · narrator: Paul, first-person epistolary author, ventriloquizing his own gloss-content
  · **edges:** M688 —BEQUEATHS→ RECEPTION; ["M687"] —REPORTS→ M688

**M689** — Paul poses the positive-question: but what does it (the righteousness-of-faith) actually say?
  · agent: it (the righteousness-of-faith from M6) · operation: say (interrogatively — what does it say, with recoverable content) · substrate: the content of what it says (M11a) · outcome: the actual positive-saying opened for citation · narrator: Paul, first-person epistolary author
  · **edges:** M689 —REPORTS→ M690

**M690** — The positive-content: the word is nearby to you — it is in your mouth, and it is in your heart.
  · agent: the word · operation: be (near thee — of the word, in thy mouth and in thy heart) · substrate: thee (in thy mouth and in thy heart, as location) · outcome: the word standing as near-to-thee, in thy mouth and in thy heart · narrator: Paul, first-person epistolary author, ventriloquizing Deut 30:14 LXX
  · **edges:** ["M689"] —REPORTS→ M690

**M691** — Paul's third exegetical gloss: that is — [what the word here actually names is] the following.
  · agent: not-stated (Paul as speaker) · operation: explain (paraphrase — with recoverable content, third gloss) · substrate: the M11a 'word' (as being glossed) — the content of the gloss (M12a) · outcome: Paul's exegetical gloss identifying the M11a 'word' with the M12a specific · narrator: Paul, first-person epistolary author, in exegetical mode
  · **edges:** M691 —REPORTS→ M692

**M692** — The identification-content of the third gloss: it is the word that belongs to trust — the very word we announce.
  · agent: the word (from M11a) · operation: be (the word of faith — of the word, identification) · substrate: not-stated · outcome: the near-word identified as the word-of-faith · narrator: Paul, first-person epistolary author, ventriloquizing his own gloss-content
  · **edges:** ["M691"] —REPORTS→ M692

**M693** — Descriptor of that word-of-faith: it is the one we make our public announcement about.
  · agent: we (Paul and the apostolic circle) · operation: preach (make public announcement about — the word-of-faith) · substrate: the word of faith (from M12a) · outcome: the word-of-faith standing as the object of we-preach · narrator: Paul, first-person epistolary author

**M694** — The first conditional-clause of the confession-formula: if you carry out the confession — with your mouth — that Jesus is Lord.
  · agent: thou (addressed) · operation: confess (make confession — with thy mouth, the Lord Jesus, conditional) · substrate: the Lord Jesus (as content of the confession) · outcome: the addressee (in the conditional) confessing with the mouth 'the Lord Jesus' · narrator: Paul, first-person epistolary author

**M695** — The second conditional-clause of the confession-formula: and if you place trust in your heart concerning the following.
  · agent: thou (addressed) · operation: believe (place trust — in thine heart, with recoverable content, conditional) · substrate: the content of the heart-belief (M14a) · outcome: the addressee (in the conditional) placing heart-trust in the M14a content · narrator: Paul, first-person epistolary author
  · **edges:** M695 —REPORTS→ M696

**M696** — The content of the heart-belief: that God has lifted him up out of the [dead — the substrate-completion is truncated in the source at 'from the'].
  · agent: God · operation: raise (lift up — him, from the [dead, truncated]) · substrate: him (Christ) · outcome: God having raised him (Christ) from the [dead, per the KJV continuation — the substrate is truncated in the source at 'from the'] · narrator: Paul, first-person epistolary author, ventriloquizing the heart-belief content
  · **edges:** ["M695"] —REPORTS→ M696

**M697** — Completing the substrate from the prior clause: [God raised him] from among the dead.
  · agent: God (from prior) · operation: (substrate-completion — 'dead', identifying the M14a-prior raising-source) · substrate: the dead (as source from which Christ was raised) · outcome: the M14a-prior raising specified as from-among-the-dead · narrator: Paul, first-person epistolary author, closing the substrate-completion from the prior passage

**M698** — The main-consequent of the confession-formula: you will be rescued.
  · agent: not-stated (God as saver) · operation: be saved (be rescued — thou, future) · substrate: thou · outcome: the addressee (future) rescued, as consequent of the M13-M14-prior confession-and-belief conditionals · narrator: Paul, first-person epistolary author
  · **edges:** M698 —BEQUEATHS→ RECEPTION

**M699** — The heart-side principle underlying the formula: with the heart as its organ, the human trusts, and the terminus of the trusting is righteousness.
  · agent: man (indefinite subject) · operation: believe (trust — with the heart, unto righteousness) · substrate: not-stated (the object of trust) · outcome: the human trusting with the heart, with righteousness as terminus · narrator: Paul, first-person epistolary author

**M700** — The paired mouth-side principle: with the mouth as its organ, the confession is uttered, and the terminus of the confessing is salvation.
  · agent: not-stated (the confessing subject) · operation: be made (be uttered — of confession, with the mouth, unto salvation) · substrate: confession · outcome: confession uttered with the mouth, with salvation as terminus · narrator: Paul, first-person epistolary author

**M701** — Paul cites scriptural attestation for the formula: the scripture makes the following utterance.
  · agent: the scripture · operation: say (utter — with recoverable content) · substrate: the content of the scripture's utterance (M5a) · outcome: scripture uttering the M5a content · narrator: Paul, first-person epistolary author
  · **edges:** M701 —REPORTS→ M702

**M702** — The content of the scripture's saying: any person at all who places trust on him will not undergo shaming.
  · agent: not-stated (the implicit shame-source, negated) · operation: not be ashamed (not be put to shame — of every believer on him, future) · substrate: whosoever believeth on him (the every-believer cohort) · outcome: every believer-on-him (future) not put to shame · narrator: Paul, first-person epistolary author, ventriloquizing Isa 28:16 LXX
  · **edges:** M702 —BEQUEATHS→ RECEPTION; ["M701"] —REPORTS→ M702

**M703** — The universalizing ground: there stands no distinction between the Jew and the Greek.
  · agent: not-stated (the distinction, existentially negated) · operation: be (no difference — between the Jew and the Greek) · substrate: the Jew and the Greek · outcome: no distinction standing between Jew and Greek · narrator: Paul, first-person epistolary author
  · **edges:** M703 —BEQUEATHS→ RECEPTION

**M704** — The reason for that non-distinction: the very same Lord — Lord over all — stands as lavish toward everyone who calls on him.
  · agent: the same Lord over all · operation: be rich (be lavish — the same Lord over all, unto all that call upon him) · substrate: not-stated (all that call upon him) · outcome: the same Lord-over-all standing as lavish toward all who call upon him · narrator: Paul, first-person epistolary author

**M705** — Descriptor of that all-cohort: those who call upon him.
  · agent: all (that call upon him) · operation: call upon (invoke — him) · substrate: him (the Lord) · outcome: the beneficiary-cohort standing as those who invoke the Lord · narrator: Paul, first-person epistolary author
  · **edges:** M705 —BEQUEATHS→ RECEPTION

**M706** — The universal-scope formula, descriptor-half: anyone at all who will call upon the name of the Lord.
  · agent: whosoever · operation: call upon (invoke — the name of the Lord, universal) · substrate: the name of the Lord · outcome: any invoker of the Lord's name standing as the beneficiary-cohort of the M10 promise · narrator: Paul, first-person epistolary author, ventriloquizing Joel 2:32 (LXX 3:5)

**M707** — The main-promise of the formula: that person will undergo being rescued.
  · agent: not-stated (God as saver) · operation: be saved (be rescued — every invoker, future) · substrate: every invoker (from M9) · outcome: every invoker (future) rescued · narrator: Paul, first-person epistolary author, ventriloquizing Joel 2:32
  · **edges:** M707 —BEQUEATHS→ RECEPTION

**M708** — The first link of the preach-chain: how then are they going to invoke someone in whom they have not exercised trust?
  · agent: they (potential invokers) · operation: call upon (invoke — him, interrogatively, how) · substrate: him (the Lord, in whom they have not believed) · outcome: the impossibility of invoking someone not-believed-in put in question · narrator: Paul, first-person epistolary author
  · **edges:** M708 —BEQUEATHS→ RECEPTION

**M709** — Descriptor of the object of the M11 question: they have not exercised trust in him.
  · agent: they · operation: not believe (not trust — in him) · substrate: him (the Lord) · outcome: they standing as ones who have not believed in him · narrator: Paul, first-person epistolary author

**M710** — Second preach-chain link: and how are they going to trust in someone about whom they have not heard?
  · agent: they · operation: believe (trust — in him, interrogatively, how) · substrate: him (the Lord, of whom they have not heard) · outcome: the impossibility of believing in someone not-heard-of put in question · narrator: Paul, first-person epistolary author

**M711** — Descriptor of the object of the M13 question: they have not heard about him.
  · agent: they · operation: not hear (not have heard — of him) · substrate: him (the Lord — hou 'of whom') · outcome: they standing as ones who have not heard of him · narrator: Paul, first-person epistolary author

**M712** — Third preach-chain link: and how are they going to hear without someone doing the announcing?
  · agent: they · operation: hear (interrogatively, how, without a preacher) · substrate: not-stated (the object of hearing) · outcome: the impossibility of hearing-without-a-preacher put in question · narrator: Paul, first-person epistolary author

**M713** — Fourth preach-chain link: and how are they going to announce, if they are not commissioned to do so?
  · agent: they (potential preachers) · operation: preach (make public announcement — interrogatively, how) · substrate: not-stated · outcome: the impossibility of preaching-without-commission put in question · narrator: Paul, first-person epistolary author

**M714** — The precondition-conditional for the preachers: unless they have been sent by commission.
  · agent: not-stated (God as commissioner) · operation: be sent (be commissioned — of the preachers, conditional) · substrate: they (the preachers) · outcome: the preachers standing as commissioned (as necessary precondition for preaching) · narrator: Paul, first-person epistolary author
  · **edges:** M714 —BEQUEATHS→ RECEPTION

**M715** — Paul appeals to scriptural warrant for the beauty of the preaching-mission: as it stands written in scripture.
  · agent: not-stated (scripture as authoritative source) · operation: be written (stand as inscribed in scripture — with recoverable content) · substrate: the cited content (M18a and following) · outcome: the following claim standing under scriptural warrant · narrator: Paul, first-person epistolary author
  · **edges:** M715 —CONTAINS→ M717; M715 —CONTAINS→ M718; M715 —REPORTS→ M716

**M716** — The cited content: how beautiful are the feet of those who announce — [descriptors follow].
  · agent: the feet of them (the gospel-preachers) · operation: be (beautiful — of the feet of the gospel-preachers) · substrate: not-stated · outcome: the feet-of-gospel-preachers standing as beautiful · narrator: Paul, first-person epistolary author, ventriloquizing Isa 52:7 LXX
  · **edges:** ["M715"] —REPORTS→ M716

**M717** — First descriptor of the beautiful-footed cohort: they are the ones announcing the message of peace.
  · agent: them (the preachers, from M18a) · operation: preach (make public announcement — of the gospel of peace) · substrate: the gospel of peace · outcome: the preachers standing as those who preach the gospel-of-peace · narrator: Paul, first-person epistolary author, ventriloquizing Isaiah
  · **edges:** ["M715"] —CONTAINS→ M717

**M718** — Paired second descriptor: and they bring glad-tidings about good things.
  · agent: them (the preachers, from M18a) · operation: bring glad tidings (announce good news — of good things) · substrate: good things (the substrate of the glad-tidings) · outcome: the preachers standing as those who bring glad-tidings-of-good-things · narrator: Paul, first-person epistolary author, ventriloquizing Isa 52:7
  · **edges:** ["M715"] —CONTAINS→ M718

**M719** — Paul returns from the preach-chain to the diagnosis: but they have not — not all — given assent to the gospel.
  · agent: they · operation: not obey (not give assent — the gospel, universal-partial) · substrate: the gospel · outcome: not all of them having obeyed the gospel · narrator: Paul, first-person epistolary author
  · **edges:** M719 —BEQUEATHS→ RECEPTION

**M720** — Paul cites Isaiah to attest that non-universal-obedience: Isaiah says the following — [the actual quoted content is truncated in the source at 'For Esaias saith'].
  · agent: Isaiah · operation: say (utter — with recoverable content, truncated) · substrate: the content of Isaiah's utterance (truncated in the source) · outcome: Isaiah's citation opened — with the actual quoted content ('Lord, who hath believed our report?' per Isa 53:1) truncated in the source at 'For Esaias saith' · narrator: Paul, first-person epistolary author

**M721** — Completing the Isaiah citation-content from the prior clause: Lord — who has actually placed trust in the report we brought?
  · agent: who (interrogated as would-be-believer) · operation: believe (place trust — our report, interrogatively, who — with vocative-address to Lord) · substrate: our report · outcome: the near-impossibility of anyone having-believed-our-report put in question, addressed to the Lord · narrator: Paul, first-person epistolary author, closing the Isa 53:1 citation from the prior passage
  · **edges:** M721 —BEQUEATHS→ RECEPTION

**M722** — The consequence Paul draws from the report-hearing thematic: therefore trust comes into being through the act of hearing.
  · agent: faith · operation: come (arise — by hearing, of faith) · substrate: not-stated · outcome: faith arising by way of hearing · narrator: Paul, first-person epistolary author

**M723** — The second derivational-link: and hearing itself comes into being through the word of God.
  · agent: hearing · operation: come (arise — by the word of God, of hearing, verb elided from M2) · substrate: not-stated · outcome: hearing arising by way of God's word · narrator: Paul, first-person epistolary author

**M724** — Paul opens the next diatribal question: but I go on to raise a point — have they in fact not heard?
  · agent: I (Paul) · operation: say (raise — the following, with recoverable content) · substrate: the content of what Paul raises (M4a) · outcome: Paul opening the M4a question · narrator: Paul, first-person epistolary author
  · **edges:** M724 —REPORTS→ M725

**M725** — The content Paul raises: is it really the case that they have not heard?
  · agent: they · operation: not hear (interrogatively — have they not heard, negated-question) · substrate: not-stated (the object of hearing) · outcome: the have-they-not-heard question posed, leading toward affirmation of hearing · narrator: Paul, first-person epistolary author, ventriloquizing his own question
  · **edges:** M725 —BEQUEATHS→ RECEPTION; ["M724"] —REPORTS→ M725

**M726** — The emphatic affirmation, with Ps 19:4 imagery: yes indeed — their voice went out into all the earth.
  · agent: their sound (phthongos) · operation: go (extend, go out — into all the earth, of their sound) · substrate: not-stated (the earth as destination) · outcome: their sound extending into all the earth · narrator: Paul, first-person epistolary author, ventriloquizing Ps 19:4 (LXX 18:5)
  · **edges:** M726 —BEQUEATHS→ RECEPTION

**M727** — The paired parallel: and their utterances reached to the very ends of the inhabited world.
  · agent: their words (rhēmata) · operation: go (extend — unto the ends of the world, of their words, verb elided from M5) · substrate: not-stated (the world's-ends as destination) · outcome: their words extending to the ends of the world · narrator: Paul, first-person epistolary author, ventriloquizing the second half of Ps 19:4

**M728** — Paul raises the next diatribal question: but I raise a further point — was it really the case that Israel did not know?
  · agent: I (Paul) · operation: say (raise — the following, with recoverable content) · substrate: the content of what Paul raises (M7a) · outcome: Paul opening the M7a question · narrator: Paul, first-person epistolary author
  · **edges:** M728 —REPORTS→ M729

**M729** — The content Paul raises: did Israel truly fail to know?
  · agent: Israel · operation: not know (interrogatively — did Israel not know, negated-question) · substrate: not-stated (the object of knowledge) · outcome: the did-Israel-not-know question posed, leading toward affirmation of Israel's knowledge · narrator: Paul, first-person epistolary author, ventriloquizing his own question
  · **edges:** ["M728"] —REPORTS→ M729

**M730** — Paul introduces the first scriptural witness: firstly, Moses makes the following utterance.
  · agent: Moses · operation: say (utter — first, with recoverable content) · substrate: the content of Moses's utterance (M8a and M8b) · outcome: Moses's Deut 32:21 utterance quoted as first witness · narrator: Paul, first-person epistolary author
  · **edges:** M730 —CONTAINS→ M732; M730 —REPORTS→ M731

**M731** — First quoted line of Moses's utterance: I will provoke you to jealousy — using those who are not a people to do it.
  · agent: I (God, in direct speech) · operation: provoke to jealousy (make jealous — you, by them that are no people, future) · substrate: you (Israel, addressed) · outcome: God (future) provoking Israel to jealousy, mediated through no-people · narrator: Paul, first-person epistolary author, ventriloquizing Deut 32:21 LXX
  · **edges:** ["M730"] —REPORTS→ M731

**M732** — Paired second line: and by a nation that lacks understanding, I will make you angry.
  · agent: I (God, in direct speech) · operation: anger (make angry — you, by a foolish nation, future) · substrate: you (Israel, addressed) · outcome: God (future) making Israel angry, mediated through a foolish nation · narrator: Paul, first-person epistolary author, ventriloquizing the second half of Deut 32:21
  · **edges:** ["M730"] —CONTAINS→ M732

**M733** — Paul characterizes Isaiah's boldness: Isaiah dares — he stands as very bold.
  · agent: Isaiah · operation: be very bold (dare, be daring — of Isaiah) · substrate: not-stated · outcome: Isaiah standing as very bold, in Paul's estimation · narrator: Paul, first-person epistolary author

**M734** — Isaiah's utterance itself: and he speaks the following.
  · agent: Isaiah · operation: say (utter — with recoverable content) · substrate: the content of Isaiah's utterance (M10a-M10d nested) · outcome: Isaiah uttering the Isa 65:1 sought/found-by-non-seekers formula · narrator: Paul, first-person epistolary author
  · **edges:** M734 —CONTAINS→ M736; M734 —CONTAINS→ M737; M734 —CONTAINS→ M738; M734 —REPORTS→ M735

**M735** — First line of Isaiah's citation: I underwent being-found by people who were not seeking me.
  · agent: not-stated (the finders — them-that-sought-me-not) · operation: be found (be discovered — of I / God, by them, past) · substrate: I (God, in direct speech) · outcome: God found by those who were not seeking him · narrator: Paul, first-person epistolary author, ventriloquizing Isa 65:1 LXX
  · **edges:** ["M734"] —REPORTS→ M735

**M736** — Descriptor of those finders: they were the ones who were not seeking me.
  · agent: them (the finders, from M10a) · operation: not seek (not pursue — me, of the finders) · substrate: me (God) · outcome: the finders standing as those who did not seek God · narrator: Paul, first-person epistolary author, ventriloquizing Isaiah
  · **edges:** ["M734"] —CONTAINS→ M736

**M737** — Paired second half: I was made openly-visible to people who were not making inquiry about me.
  · agent: not-stated (God, as self-manifesting agent, implicit) · operation: be made manifest (be made-openly-visible — of I / God, unto them, past) · substrate: I (God, in direct speech) · outcome: God made openly-visible to those who were not inquiring after him · narrator: Paul, first-person epistolary author, ventriloquizing the second half of Isa 65:1
  · **edges:** ["M734"] —CONTAINS→ M737

**M738** — Descriptor of the recipients of M10c: they were the ones not making inquiry after me.
  · agent: them (the recipients, from M10c) · operation: not ask after (not inquire about — me, of the recipients) · substrate: me (God) · outcome: the recipients standing as those who did not inquire after God · narrator: Paul, first-person epistolary author, ventriloquizing Isaiah
  · **edges:** ["M734"] —CONTAINS→ M738

**M739** — But turning specifically to Israel, Isaiah has a different word: to Israel he speaks the following.
  · agent: he (Isaiah) · operation: say (address — to Israel, with recoverable content) · substrate: Israel (as addressee) — the content of the address (M11a) · outcome: Isaiah speaking specifically to Israel with the Isa 65:2 content · narrator: Paul, first-person epistolary author
  · **edges:** M739 —REPORTS→ M740

**M740** — The content of that Israel-directed word: throughout the entire day I have kept my hands stretched out — reaching toward a people that refuses to hear and answers back.
  · agent: I (God, in direct speech) · operation: stretch forth (reach out — my hands, all day long, unto a disobedient and gainsaying people) · substrate: my hands (as extended toward the people) · outcome: God's hands stretched out continuously toward a disobedient-and-gainsaying people · narrator: Paul, first-person epistolary author, ventriloquizing Isa 65:2 LXX
  · **edges:** M740 —BEQUEATHS→ RECEPTION; ["M739"] —REPORTS→ M740

**M741** — Paul opens ch 11 with the anticipated grief-question: I raise then the following.
  · agent: I (Paul) · operation: say (raise then — with recoverable content) · substrate: the content of what Paul raises (M12a) · outcome: Paul opening the M12a question · narrator: Paul, first-person epistolary author, opening ch 11
  · **edges:** M741 —REPORTS→ M742

**M742** — The content Paul raises: has God flung his people away from himself?
  · agent: God · operation: cast away (fling away, reject — his people, interrogatively) · substrate: his people · outcome: the possibility of God-rejecting-his-people put under interrogation · narrator: Paul, first-person epistolary author, ventriloquizing his own opening question
  · **edges:** M742 —BEQUEATHS→ RECEPTION; ["M741"] —REPORTS→ M742

**M743** — Paul denies flatly: absolutely not.
  · agent: not-stated (Paul himself as speaker) · operation: may-it-not-be (emphatically deny) · substrate: the M12a possibility · outcome: the M12a possibility (God-rejected-his-people) emphatically denied · narrator: Paul, first-person epistolary author
  · **edges:** M743 —BEQUEATHS→ RECEPTION

**M744** — Paul offers himself as proof: for I too stand as an Israelite, and as one of Abraham's seed-line, and as belonging to the tribe of [Benjamin — the tribe-name is truncated in the source at 'of the tribe of'].
  · agent: I (Paul) · operation: be (an Israelite, of the seed of Abraham, of the tribe of [Benjamin, truncated] — of I / Paul, merged self-identification) · substrate: not-stated · outcome: Paul standing as Israelite, as of Abraham's seed, and as of the tribe of [Benjamin, per the KJV continuation — the tribe-name is truncated in the source] · narrator: Paul, first-person epistolary author
  · **edges:** M744 —BEQUEATHS→ RECEPTION

**M745** — Completing the tribe-name from the prior clause: [of the tribe of] Benjamin.
  · agent: I (Paul, from prior) · operation: (substrate-completion — 'Benjamin', identifying the tribe-substrate of Paul's self-identification) · substrate: Benjamin (as tribe-substrate) · outcome: Paul's tribe identified as Benjamin, completing his three-fold Jewish self-identification · narrator: Paul, first-person epistolary author, closing the tribe-completion from the prior passage

**M746** — The main claim of the section: God has not thrown-away his people.
  · agent: God · operation: not cast away (not reject, not throw away — his people) · substrate: his people · outcome: God standing as one who has not cast his people away · narrator: Paul, first-person epistolary author

**M747** — Descriptor of that people: they are the ones God had cognitive-recognition of in advance.
  · agent: he (God) · operation: foreknow (have advance-cognition of) · substrate: whom (his people) · outcome: God's advance-cognition of his people (as ground for the M2 non-rejection) · narrator: Paul, first-person epistolary author
  · **edges:** M747 —BEQUEATHS→ RECEPTION

**M748** — Paul appeals to shared knowledge with a diatribal question: don't you have cognitive hold of what scripture says about Elijah?
  · agent: ye · operation: know (interrogatively — with recoverable content, about scripture-on-Elias) · substrate: the content of the knowing (M4a — what scripture says of Elias) · outcome: the addressees challenged to recognize the M4a scriptural-content · narrator: Paul, first-person epistolary author
  · **edges:** M748 —REPORTS→ M749

**M749** — The content of the knowing — what scripture says of Elijah: how he takes his complaint to God, and takes it against Israel.
  · agent: he (Elias) · operation: make intercession (bring complaint — to God, against Israel) · substrate: God (as recipient) — against Israel (as substrate-target) · outcome: Elias bringing complaint to God, directed against Israel · narrator: Paul, first-person epistolary author, ventriloquizing the scripture-about-Elias
  · **edges:** M749 —REPORTS→ M750; ["M748"] —REPORTS→ M749

**M750** — The saying-verb attaching Elijah's actual speech: saying the following.
  · agent: he (Elias, from M4a) · operation: say (utter — with recoverable content) · substrate: the content of Elias's speech (M5a-M5d) · outcome: Elias uttering his four-part complaint · narrator: Paul, first-person epistolary author
  · **edges:** M750 —CONTAINS→ M752; M750 —CONTAINS→ M753; M750 —CONTAINS→ M754; M750 —REPORTS→ M751; ["M749"] —REPORTS→ M750

**M751** — First line of Elijah's complaint: Lord, they have killed the prophets that belong to you.
  · agent: they · operation: kill (put to death — thy prophets) · substrate: thy prophets · outcome: the prophets killed by them · narrator: Paul, first-person epistolary author, doubly-ventriloquizing (through scripture, through Elias)
  · **edges:** ["M750"] —REPORTS→ M751

**M752** — Second line of the complaint: and they have dug down your altars.
  · agent: they · operation: dig down (demolish, tear down — thine altars) · substrate: thine altars · outcome: the altars demolished by them · narrator: Paul, first-person epistolary author, doubly-ventriloquizing
  · **edges:** ["M750"] —CONTAINS→ M752

**M753** — Third line — the self-isolation complaint: and I have been left alone, standing on my own.
  · agent: not-stated (the implicit leaver) · operation: be left (be left behind — alone, of I / Elias) · substrate: I (Elias) · outcome: Elias standing as left-alone (the only Yahweh-loyalist remaining, in his perception) · narrator: Paul, first-person epistolary author, doubly-ventriloquizing
  · **edges:** ["M750"] —CONTAINS→ M753

**M754** — Fourth line — the threat-complaint: and they are pursuing my life to take it.
  · agent: they · operation: seek (pursue — my life) · substrate: my life · outcome: them pursuing Elias's life (with intent to take it) · narrator: Paul, first-person epistolary author, doubly-ventriloquizing
  · **edges:** ["M750"] —CONTAINS→ M754

**M755** — Paul poses the counter-question: but what does the divine reply say back to him?
  · agent: the answer of God (chrēmatismos, oracular-response) · operation: say (interrogatively — of the divine-answer to him, with recoverable content) · substrate: him (Elias, as addressee) — the content of the reply (M6a and M6b) · outcome: the divine oracular-reply to Elias delivered as scriptural content · narrator: Paul, first-person epistolary author
  · **edges:** M755 —CONTAINS→ M757; M755 —REPORTS→ M756

**M756** — First line of the divine reply: I have set aside for myself a group of seven thousand men.
  · agent: I (God, in direct speech) · operation: reserve (keep back, set aside — seven thousand men, to myself) · substrate: seven thousand men (as reserved-substrate) · outcome: God having reserved seven thousand men for himself (as remnant-cohort) · narrator: Paul, first-person epistolary author, ventriloquizing 1 Kgs 19:18 LXX
  · **edges:** ["M755"] —REPORTS→ M756

**M757** — Descriptor of that seven thousand: they are the ones who have refused to bend the knee before Baal's cult-image.
  · agent: they (the seven thousand) · operation: not bow the knee (not have knelt — to the image of Baal) · substrate: the image of Baal (as substrate not-knelt-to) · outcome: the seven thousand standing as ones who have not knelt to Baal · narrator: Paul, first-person epistolary author, ventriloquizing the continuation of 1 Kgs 19:18
  · **edges:** ["M755"] —CONTAINS→ M757

**M758** — Paul applies the Elijah-remnant precedent to the present: in the same way then, and at the current time as well, a remnant-portion exists — one that stands there according to grace-based election.
  · agent: a remnant (as existential subject) · operation: be (a remnant — at this present time, according to the election of grace) · substrate: not-stated · outcome: a remnant existing at the present time, grounded in election-by-grace · narrator: Paul, first-person epistolary author
  · **edges:** M758 —BEQUEATHS→ RECEPTION

**M759** — The first conditional of a two-part deductive-couplet: and given that it comes by grace.
  · agent: it (the remnant-status from M7) · operation: be (by grace — of it / the remnant-status, conditional) · substrate: not-stated · outcome: the remnant-status (conditionally) grounded in grace · narrator: Paul, first-person epistolary author
  · **edges:** M759 —BEQUEATHS→ RECEPTION

**M760** — The consequent of M8: then no longer is it of works.
  · agent: it (the remnant-status) · operation: not be (of works — of it, consequent) · substrate: not-stated · outcome: the remnant-status standing as no-longer-of-works, as consequent of M8 · narrator: Paul, first-person epistolary author
  · **edges:** M760 —BEQUEATHS→ RECEPTION

**M761** — The otherwise-clause: else, grace ceases to be grace.
  · agent: grace · operation: not be (grace — of grace, negated-identity, otherwise-clause) · substrate: not-stated · outcome: grace standing as no-longer-grace (in the otherwise-case) · narrator: Paul, first-person epistolary author
  · **edges:** M761 —BEQUEATHS→ RECEPTION

**M762** — The paired second conditional: but if instead it comes by works.
  · agent: it (the remnant-status) · operation: be (of works — of it / the remnant-status, second conditional) · substrate: not-stated · outcome: the remnant-status (conditionally) grounded in works · narrator: Paul, first-person epistolary author
  · **edges:** M762 —BEQUEATHS→ RECEPTION

**M763** — The consequent of M11: then it is no longer grace.
  · agent: it (the remnant-status) · operation: not be (grace — of it, consequent) · substrate: not-stated · outcome: the remnant-status standing as no-longer-grace, as consequent of M11 · narrator: Paul, first-person epistolary author

**M764** — The paired otherwise-clause: else, work ceases to be work.
  · agent: work · operation: not be (work — of work, negated-identity, otherwise-clause) · substrate: not-stated · outcome: work standing as no-longer-work (in the otherwise-case) · narrator: Paul, first-person epistolary author
  · **edges:** M764 —BEQUEATHS→ RECEPTION

**M765** — Paul opens the next question: what then?
  · agent: not-stated (Paul with the imagined interlocutor) · operation: say (deliberatively — what then?) · substrate: not-stated (the emerging conclusion) · outcome: the conclusion opened for question · narrator: Paul, first-person epistolary author

**M766** — The answer, main-claim about Israel: Israel did not reach hold of the thing he was going after.
  · agent: Israel · operation: not obtain (not reach hold of — that which he seeks) · substrate: that which he seeks (the sought-after) · outcome: Israel standing as one who did not obtain what he was seeking · narrator: Paul, first-person epistolary author

**M767** — Descriptor of what Israel was after: it is the thing he is going after — [the source cuts off at 'that which he seeketh for' before the continuing clause about the election-obtaining and the-rest-being-blinded arrives].
  · agent: he (Israel) · operation: seek (pursue — that which) · substrate: that which (the sought-after) · outcome: Israel standing as one who seeks the object he does not obtain — with the continuation (about the election-obtaining and the-rest-being-blinded) truncated in the source at 'that which he seeketh for' · narrator: Paul, first-person epistolary author

**M768** — Completing the answer from the prior clause: but the election-cohort managed to reach hold of it.
  · agent: the election (the election-cohort) · operation: obtain (reach hold of — it, the sought-after) · substrate: it (the sought-after, from M16-prior) · outcome: the election-cohort having reached hold of the sought-after (in contrast to Israel-as-a-whole) · narrator: Paul, first-person epistolary author, closing the answer from the prior passage

**M769** — The paired second consequent: and the remaining portion of Israel underwent being hardened.
  · agent: not-stated (the implicit hardener — God, per the M3a citation) · operation: be blinded (be hardened — of the rest) · substrate: the rest (of Israel) · outcome: the non-election-portion of Israel hardened · narrator: Paul, first-person epistolary author
  · **edges:** M769 —BEQUEATHS→ RECEPTION

**M770** — Paul brings scriptural attestation for the hardening: as it stands written in scripture.
  · agent: not-stated (scripture as authoritative source) · operation: be written (stand as inscribed in scripture — with recoverable content) · substrate: the cited content (M3a) · outcome: the following claim standing under scriptural warrant · narrator: Paul, first-person epistolary author
  · **edges:** M770 —REPORTS→ M771

**M771** — The content of the citation: God has handed over to them a slumber-spirit, along with eyes that do not see and ears that do not hear — and this state runs on to the present day.
  · agent: God · operation: give (hand over — to them, the spirit of slumber, and eyes that should not see, and ears that should not hear, unto this day) · substrate: the spirit of slumber, and eyes that should not see, and ears that should not hear (merged three-fold gift) · outcome: God having given them a three-fold slumber-and-blindness-and-deafness gift, a state persisting unto the present day · narrator: Paul, first-person epistolary author, ventriloquizing the composite Isa 29:10 / Deut 29:4 citation
  · **edges:** M771 —BEQUEATHS→ RECEPTION; ["M770"] —REPORTS→ M771

**M772** — Paul brings in David as a second witness: and David speaks the following.
  · agent: David · operation: say (utter — with recoverable content) · substrate: the content of David's utterance (M4a-M4c nested) · outcome: David's Ps 69:22-23 imprecation delivered as scriptural content · narrator: Paul, first-person epistolary author
  · **edges:** M772 —CONTAINS→ M774; M772 —CONTAINS→ M775; M772 —REPORTS→ M773

**M773** — First imprecation of David: let their table become — for them — a trap, a snare, a stumblingstone, and a pay-back.
  · agent: not-stated (the implicit transforming-agent, God-invoked) · operation: be made (be turned into — a snare, and a trap, and a stumblingblock, and a recompence unto them — of their table) · substrate: their table · outcome: their table (imprecated to be) turned into snare/trap/stumblingstone/recompence for them · narrator: Paul, first-person epistolary author, ventriloquizing Ps 69:22 LXX
  · **edges:** M773 —BEQUEATHS→ RECEPTION; ["M772"] —REPORTS→ M773

**M774** — Second imprecation: let their eyes undergo darkening — so that they may not see.
  · agent: not-stated (the implicit darkening-agent) · operation: be darkened (be made-dark — their eyes, with purpose that they may not see) · substrate: their eyes · outcome: their eyes (imprecated to be) darkened, with the purpose that they may not see · narrator: Paul, first-person epistolary author, ventriloquizing Ps 69:23 LXX
  · **edges:** M774 —BEQUEATHS→ RECEPTION; ["M772"] —CONTAINS→ M774

**M775** — Third imprecation: and bend down their back — perpetually.
  · agent: not-stated (the addressee of the imprecation — God, implicit) · operation: bow down (bend down — their back, alway) · substrate: their back · outcome: their back (imprecated to be) bent down, perpetually · narrator: Paul, first-person epistolary author, ventriloquizing Ps 69:23 LXX
  · **edges:** M775 —BEQUEATHS→ RECEPTION; ["M772"] —CONTAINS→ M775

**M776** — Paul opens the next diatribal question: I raise then the following.
  · agent: I (Paul) · operation: say (raise then — with recoverable content) · substrate: the content of what Paul raises (M5a) · outcome: Paul opening the M5a question · narrator: Paul, first-person epistolary author
  · **edges:** M776 —REPORTS→ M777

**M777** — The content Paul raises: is it the case that they stumbled with the intent that they should fall?
  · agent: they (Israel-as-hardened) · operation: stumble (trip — with intent that they should fall, interrogatively) · substrate: not-stated (their state-of-fall as intended-outcome, folded into the purpose-clause) · outcome: the possibility that Israel stumbled with fall-purpose put in question — leading to the M6 denial · narrator: Paul, first-person epistolary author, ventriloquizing his own question
  · **edges:** M777 —BEQUEATHS→ RECEPTION; ["M776"] —REPORTS→ M777

**M778** — Paul denies flatly: absolutely not.
  · agent: not-stated (Paul himself as speaker) · operation: may-it-not-be (emphatically deny) · substrate: the M5a possibility · outcome: the M5a stumble-to-fall possibility emphatically denied · narrator: Paul, first-person epistolary author
  · **edges:** M778 —BEQUEATHS→ RECEPTION

**M779** — The positive counter-account: on the contrary, mediated by their fall, rescue has arrived onto the Gentiles.
  · agent: salvation · operation: come (arrive — of salvation, unto the Gentiles, through their fall) · substrate: the Gentiles (as recipients) · outcome: salvation having arrived unto the Gentiles, mediated through Israel's fall · narrator: Paul, first-person epistolary author

**M780** — The purpose held over that Gentile-salvation-arrival: for the sake of provoking them (Israel) to jealousy.
  · agent: not-stated (God as implicit provoker) · operation: provoke to jealousy (make jealous — them / Israel, purpose) · substrate: them (Israel) · outcome: Israel (in the purpose) provoked to jealousy, by the Gentile-salvation of M7 · narrator: Paul, first-person epistolary author
  · **edges:** M780 —BEQUEATHS→ RECEPTION

**M781** — First conditional-premise of the a-fortiori: given that their fall stands as the world's wealth.
  · agent: the fall of them · operation: be (the riches of the world — of their fall, conditional) · substrate: not-stated · outcome: their fall (in the hypothetical) standing as the world's wealth · narrator: Paul, first-person epistolary author

**M782** — Coordinate second premise: and given that the shrinking of their number stands as the Gentiles' wealth.
  · agent: the diminishing of them (their number-shrinkage) · operation: be (the riches of the Gentiles — of the diminishing of them, conditional) · substrate: not-stated · outcome: their diminishing (in the hypothetical) standing as the Gentiles' wealth · narrator: Paul, first-person epistolary author

**M783** — The a-fortiori rhetorical question: how much more will their fulness be?
  · agent: their fulness (their full-restoration) · operation: be (how much more — of their fulness, a-fortiori interrogatively) · substrate: not-stated · outcome: the how-much-more-value of their fulness put in rhetorical question (implying: much greater than M9-M10 fall/diminishing) · narrator: Paul, first-person epistolary author
  · **edges:** M783 —BEQUEATHS→ RECEPTION

**M784** — Paul turns directly to address the Gentile addressees: I make my speaking-of-this to you Gentiles.
  · agent: I (Paul) · operation: speak (address — to you Gentiles) · substrate: you Gentiles · outcome: Paul addressing the Gentile addressees · narrator: Paul, first-person epistolary author, turning directly to Gentile addressees

**M785** — The ground for that direct-address to the Gentiles: to the extent that I stand as the apostle of [the Gentiles — the specifying-substrate is truncated in the source at 'the apostle of'].
  · agent: I (Paul) · operation: be (the apostle of [the Gentiles, truncated] — of I / Paul) · substrate: not-stated (the specifying-substrate 'of the Gentiles' is truncated at 'the apostle of') · outcome: Paul standing as the apostle of [the Gentiles — per the KJV continuation, truncated in the source] · narrator: Paul, first-person epistolary author

**M786** — Completing the specifying-substrate from the prior clause: [I am the apostle of] the Gentiles.
  · agent: I (Paul, from prior) · operation: (substrate-completion — 'the Gentiles', identifying the apostolic-domain of Paul's office) · substrate: the Gentiles (as apostolic-domain) · outcome: Paul's apostleship identified as directed-to-Gentiles, completing his M13-prior office-attribution · narrator: Paul, first-person epistolary author, closing the apostle-of-Gentiles from the prior passage

**M787** — The consequent stance: I make much of my apostolic-office — I glorify it.
  · agent: I (Paul) · operation: magnify (glorify, make much of — mine office) · substrate: mine office (Paul's apostolic diakonia) · outcome: Paul glorifying his apostolic office · narrator: Paul, first-person epistolary author

**M788** — The conditional-hope explaining that glorification: if in some way I might succeed in stirring up my own flesh-kin to jealous imitation.
  · agent: I (Paul) · operation: provoke to emulation (stir to jealous-imitation — them which are my flesh, hopefully) · substrate: them which are my flesh (Israel-as-fleshly-kin) · outcome: Paul (in the hopeful conditional) provoking his flesh-kin to jealous-imitation · narrator: Paul, first-person epistolary author
  · **edges:** M788 —BEQUEATHS→ RECEPTION

**M789** — Coordinate second hope: and that I might succeed in rescuing at least some of them.
  · agent: I (Paul) · operation: save (rescue — some of them) · substrate: some of them (some of Israel) · outcome: Paul (in the hopeful conditional) rescuing some of his flesh-kin · narrator: Paul, first-person epistolary author
  · **edges:** M789 —BEQUEATHS→ RECEPTION

**M790** — First premise of the a-fortiori: given that their being thrown-out counts as the reconciliation of the world.
  · agent: the casting away of them · operation: be (the reconciling of the world — of the casting-away of them, conditional) · substrate: not-stated · outcome: their casting-away (in the hypothetical) standing as world's reconciliation · narrator: Paul, first-person epistolary author
  · **edges:** M790 —BEQUEATHS→ RECEPTION

**M791** — The a-fortiori consequent: what will their acceptance-back be — if not life from among the dead?
  · agent: the receiving of them · operation: be (life from the dead — of the receiving of them, a-fortiori interrogatively) · substrate: not-stated · outcome: their receiving-back put in rhetorical question that expects the answer 'life from the dead' · narrator: Paul, first-person epistolary author
  · **edges:** M791 —BEQUEATHS→ RECEPTION

**M792** — First conditional of the second a-fortiori: given that the first-portion offering stands as holy.
  · agent: the firstfruit · operation: be (holy — of the firstfruit, conditional) · substrate: not-stated · outcome: the firstfruit (in the hypothetical) standing as holy · narrator: Paul, first-person epistolary author

**M793** — The consequent: then the whole batch of dough is also holy.
  · agent: the lump · operation: be (holy also — of the lump, consequent) · substrate: not-stated · outcome: the lump standing as also-holy, as consequent of the M7 firstfruit-holiness · narrator: Paul, first-person epistolary author

**M794** — Parallel conditional in the olive-tree register: and given that the root stands as holy.
  · agent: the root · operation: be (holy — of the root, parallel conditional) · substrate: not-stated · outcome: the root (in the hypothetical) standing as holy · narrator: Paul, first-person epistolary author

**M795** — The parallel consequent: so also are the branches — holy.
  · agent: the branches · operation: be (holy also — of the branches, consequent) · substrate: not-stated · outcome: the branches standing as also-holy, as consequent of the M9 root-holiness · narrator: Paul, first-person epistolary author

**M796** — The scenario the olive-metaphor now develops: given that some of the branches were broken off.
  · agent: not-stated (the implicit breaker) · operation: be broken off (be snapped away — some of the branches, conditional) · substrate: some of the branches · outcome: some of the branches (in the hypothetical) broken off from the tree · narrator: Paul, first-person epistolary author
  · **edges:** M796 —BEQUEATHS→ RECEPTION

**M797** — Descriptor of the addressee within the scenario: you, being a wild-olive-tree.
  · agent: thou (the addressee) · operation: be (a wild olive tree — of thou) · substrate: not-stated · outcome: the addressee standing as a wild-olive-tree · narrator: Paul, first-person epistolary author

**M798** — The main-conditional-consequent: and you were grafted in among them.
  · agent: not-stated (the implicit grafter, God) · operation: be graffed in (be grafted, be inserted — among them) · substrate: thou (the addressee) · outcome: the addressee (in the hypothetical) grafted in among the remaining branches · narrator: Paul, first-person epistolary author

**M799** — The continuing state that follows: and with them you become sharer in the root and the sap-richness of the olive tree.
  · agent: thou · operation: partake (be joint-sharer — with them, of the root and fatness of the olive tree) · substrate: the root and fatness of the olive tree · outcome: the addressee sharing with them in the root-and-sap of the olive tree · narrator: Paul, first-person epistolary author
  · **edges:** M799 —BEQUEATHS→ RECEPTION

**M800** — The directive that follows from that grafted-in status: do not boast over-against the branches.
  · agent: thou (the addressee) · operation: not boast (not exult — against the branches, imperative-negated) · substrate: the branches (against them) · outcome: the addressee directed not to boast over-against the branches · narrator: Paul, first-person epistolary author
  · **edges:** M800 —BEQUEATHS→ RECEPTION

**M801** — The counter-conditional if the directive is ignored: but suppose you do boast.
  · agent: thou · operation: boast (exult — conditional) · substrate: not-stated · outcome: the addressee (conditionally) boasting despite the M15 directive · narrator: Paul, first-person epistolary author
  · **edges:** M801 —BEQUEATHS→ RECEPTION

**M802** — The corrective on the boasting-side: [remember that] you are not the one bearing the root.
  · agent: thou · operation: not bear (not carry — the root, of thou) · substrate: the root · outcome: the addressee standing as one who does not bear the root · narrator: Paul, first-person epistolary author

**M803** — The paired flip: rather, the root is the one bearing you.
  · agent: the root · operation: bear (carry — thee, of the root) · substrate: thee (the addressee) · outcome: the root bearing the addressee · narrator: Paul, first-person epistolary author
  · **edges:** M803 —BEQUEATHS→ RECEPTION

**M804** — Paul anticipates the addressee's rejoinder: you will therefore address me with the following.
  · agent: thou (the anticipated addressee) · operation: say (address — with recoverable content) · substrate: the content of the rejoinder (M19a and M19b) · outcome: the addressee's rejoinder anticipated and quoted · narrator: Paul, first-person epistolary author
  · **edges:** M804 —BEQUEATHS→ RECEPTION; M804 —CONTAINS→ M806; M804 —REPORTS→ M805

**M805** — First part of the anticipated rejoinder: the branches were broken off.
  · agent: not-stated (the implicit breaker) · operation: be broken off (be snapped away — of the branches) · substrate: the branches · outcome: the branches broken off (as premise in the anticipated rejoinder) · narrator: Paul, first-person epistolary author, ventriloquizing the addressee's rejoinder
  · **edges:** M805 —BEQUEATHS→ RECEPTION; ["M804"] —REPORTS→ M805

**M806** — The purpose the addressee reads into it: [and this happened] so that I might get grafted in.
  · agent: not-stated (the implicit grafter) · operation: be graffed in (be grafted — I / the addressee, purpose) · substrate: I (the addressee, first-person in the rejoinder) · outcome: the addressee (in his construal) grafted in as the intended-purpose of the branch-breaking-off · narrator: Paul, first-person epistolary author, ventriloquizing the addressee's rejoinder
  · **edges:** ["M804"] —CONTAINS→ M806

**M807** — Paul's concessive-correction: well — [the fact is] because of unbelief they were broken off.
  · agent: not-stated (the implicit breaker) · operation: be broken off (be snapped away — of them, because of unbelief) · substrate: they (the branches) · outcome: the branches broken off, correctly-attributed to their unbelief as cause · narrator: Paul, first-person epistolary author
  · **edges:** M807 —BEQUEATHS→ RECEPTION

**M808** — The paired contrast begins to arrive: and you — [the completing verb-and-object 'stand by faith' is truncated in the source at 'and thou'].
  · agent: thou (the addressee) · operation: (unstated verb — and thou, truncated at 'and thou') · substrate: not-stated (the completing verb and substrate are truncated) · outcome: the corrective about the addressee ('and thou standest by faith' per Rom 11:20 continuation) opened — the completing verb-and-object is truncated in the source at 'and thou' · narrator: Paul, first-person epistolary author

**M809** — Completing the paired parallel from the prior clause: [but you, on the other hand,] stand by way of trust.
  · agent: thou (the addressee) · operation: stand (be positioned — by faith) · substrate: not-stated (the position of standing) · outcome: the addressee standing by faith (as opposed to the M20-prior branches broken off by unbelief) · narrator: Paul, first-person epistolary author, closing the paired parallel from the prior passage

**M810** — First directive that follows: don't hold yourself in high thoughts.
  · agent: thou (the addressee) · operation: not be highminded (not hold high-thoughts, imperative-negated) · substrate: not-stated · outcome: the addressee directed not to hold high-thoughts of himself · narrator: Paul, first-person epistolary author

**M811** — Paired second directive: rather, hold reverent fear.
  · agent: thou (the addressee) · operation: fear (hold reverent-fear — imperative) · substrate: not-stated · outcome: the addressee directed to hold reverent-fear · narrator: Paul, first-person epistolary author

**M812** — The reason for the fear-directive: given that God did not spare the natural branches [when they lost trust].
  · agent: God · operation: not spare (not spare — of God, the natural branches, conditional) · substrate: the natural branches · outcome: God (in the hypothetical) not having spared the natural branches · narrator: Paul, first-person epistolary author
  · **edges:** M812 —BEQUEATHS→ RECEPTION

**M813** — The main directive drawing from M4: watch out, in case he also fails to spare you.
  · agent: thou (the addressee) · operation: take heed (be careful — lest he also spare not thee) · substrate: not-stated (the potential-non-sparing of the addressee, folded into the lest-clause) · outcome: the addressee directed to be careful, given the possibility of God not sparing him also · narrator: Paul, first-person epistolary author

**M814** — Fresh directive: therefore fix your attention on the goodness and the severity that belong to God.
  · agent: thou (the addressee) · operation: behold (fix attention on, consider — the goodness and severity of God) · substrate: the goodness and severity of God · outcome: the addressee directed to consider God's two-sided character (goodness and severity) · narrator: Paul, first-person epistolary author

**M815** — First half of the differentiated-attribution: on the ones who fell — severity.
  · agent: severity · operation: be (severity — on them which fell) · substrate: them which fell (as location-of-landing) · outcome: severity landing on those who fell · narrator: Paul, first-person epistolary author
  · **edges:** M815 —BEQUEATHS→ RECEPTION

**M816** — Paired second half: but toward you — goodness.
  · agent: goodness · operation: be (goodness — toward thee) · substrate: thee (as recipient of goodness) · outcome: goodness landing toward the addressee · narrator: Paul, first-person epistolary author

**M817** — The condition on that goodness: provided you keep on in the goodness that is his.
  · agent: thou (the addressee) · operation: continue (remain — in his goodness, conditional) · substrate: his goodness · outcome: the addressee (conditionally) remaining in God's goodness (as condition for the M8 goodness continuing) · narrator: Paul, first-person epistolary author

**M818** — The otherwise-warning: else you also will end up cut off.
  · agent: not-stated (the implicit cutter, God) · operation: be cut off (be excised — thou also) · substrate: thou (the addressee) · outcome: the addressee (in the otherwise-case) cut off from the tree · narrator: Paul, first-person epistolary author

**M819** — Turning to the paired positive side about them (Israel): and as for those persons, provided they do not stay put in unbelief.
  · agent: they (the fallen branches / Israel) · operation: not abide (not remain — in unbelief, conditional) · substrate: unbelief (the sphere-of-remaining) · outcome: them (conditionally) not remaining in unbelief · narrator: Paul, first-person epistolary author

**M820** — The consequent: they will be grafted back in.
  · agent: not-stated (the implicit grafter, God) · operation: be graffed in (be re-grafted — they also, future) · substrate: they (the fallen branches) · outcome: them (future) grafted back in, as consequent of M11's non-remaining in unbelief · narrator: Paul, first-person epistolary author

**M821** — The ground for the M12 promise: for God has power to graft them in again.
  · agent: God · operation: be able (have power — to graff them in again, of God) · substrate: not-stated (the grafting-again-operation) · outcome: God standing as able to re-graft them · narrator: Paul, first-person epistolary author

**M822** — The next a-fortiori conditional-premise: given that you underwent being cut out of the olive-tree which by its very nature is wild.
  · agent: not-stated (the implicit cutter) · operation: be cut out (be excised — thou, of the wild olive tree, conditional) · substrate: thou (the addressee) · outcome: the addressee (in the hypothetical) cut out of the wild-by-nature olive tree · narrator: Paul, first-person epistolary author

**M823** — And coordinate second conditional: and were then grafted, contrary to nature, into a cultivated olive-tree.
  · agent: not-stated (the implicit grafter) · operation: be graffed (be grafted — contrary to nature, into a good olive tree, conditional) · substrate: thou (the addressee) · outcome: the addressee (in the hypothetical) grafted contra-natura into a cultivated olive tree · narrator: Paul, first-person epistolary author

**M824** — The a-fortiori rhetorical consequent: how much more will these persons — the ones who are, in fact, the natural branches — be grafted into what is properly their own olive-tree?
  · agent: not-stated (the implicit grafter, God) · operation: be graffed (be grafted — into their own olive tree, a-fortiori interrogatively) · substrate: these (the natural branches) · outcome: the natural branches (much-more-easily) grafted into their own olive tree — asserted-via-question · narrator: Paul, first-person epistolary author
  · **edges:** M824 —BEQUEATHS→ RECEPTION

**M825** — Paul opens a fresh disclosure with kinship-address: brothers, I do not want you left in the dark about the following.
  · agent: I (Paul) · operation: not have you ignorant (refuse to leave you unaware — with recoverable content) · substrate: ye (brethren) — the content of the non-ignorance (M17a) · outcome: the brethren directed to recognize the M17a content · narrator: Paul, first-person epistolary author
  · **edges:** M825 —BEQUEATHS→ RECEPTION; M825 —REPORTS→ M826

**M826** — The content Paul is disclosing: this particular hidden-thing.
  · agent: this mystery · operation: be (this mystery — the substrate of the disclosure) · substrate: not-stated (its content, which the truncated M20 begins to unfold) · outcome: this mystery identified as the substantive substrate of the M17 disclosure · narrator: Paul, first-person epistolary author, ventriloquizing his own disclosure-object
  · **edges:** ["M825"] —REPORTS→ M826

**M827** — The purpose that governs the M17 disclosure: so that you might not end up being wise-in-your-own-estimation.
  · agent: ye · operation: be wise (be prudent — in your own conceits, purpose-negated) · substrate: not-stated (own-conceits as location of the wise-status) · outcome: the addressees (to be prevented from) becoming wise-in-own-conceits · narrator: Paul, first-person epistolary author

**M828** — The mystery-content-clause begins: that — [the completing hoti-clause content is truncated in the source at 'that'].
  · agent: not-stated (per truncation) · operation: (unstated content — 'that ___', truncated at 'that') · substrate: not-stated (per truncation) · outcome: the mystery-content-clause opened by 'that' — the specific content (per Rom 11:25b-26 continuation: 'that blindness in part is happened to Israel, until the fulness of the Gentiles be come in; and so all Israel shall be saved') is truncated in the source at 'that' · narrator: Paul, first-person epistolary author
  · **edges:** M828 —BEQUEATHS→ RECEPTION

**M829** — Completing the mystery-content-clause from the prior 'that': a partial-hardening has befallen Israel.
  · agent: not-stated (the implicit divine hardening-source) · operation: happen (befall — blindness in part, to Israel) · substrate: Israel · outcome: partial-blindness having befallen Israel · narrator: Paul, first-person epistolary author, closing the mystery-content that opened at the end of the prior passage
  · **edges:** M829 —BEQUEATHS→ RECEPTION

**M830** — The temporal-limit on that hardening: until the full-measure of the Gentiles has come in.
  · agent: the fulness of the Gentiles · operation: come in (arrive-in — the fulness of the Gentiles) · substrate: not-stated (the coming-into-the-in-group) · outcome: the Gentile-fulness (in the temporal-limit) arriving into the in-group · narrator: Paul, first-person epistolary author

**M831** — The main-consequent of the mystery: and in that way all Israel shall be rescued.
  · agent: not-stated (God as saver) · operation: be saved (be rescued — all Israel, future) · substrate: all Israel · outcome: all Israel (future) rescued · narrator: Paul, first-person epistolary author
  · **edges:** M831 —BEQUEATHS→ RECEPTION

**M832** — Paul supports the mystery-content with scripture: as it stands written.
  · agent: not-stated (scripture as authoritative source) · operation: be written (stand as inscribed in scripture — with recoverable content) · substrate: the cited content (M4a-M4b, and M5-M6 as further citation-continuation) · outcome: the following claims standing under scriptural warrant · narrator: Paul, first-person epistolary author
  · **edges:** M832 —CONTAINS→ M834; M832 —REPORTS→ M833

**M833** — First quoted line: the Rescuer will come out from Zion.
  · agent: the Deliverer · operation: come (issue forth — of the Deliverer, out of Sion, future) · substrate: not-stated (Sion as source-location, folded) · outcome: the Deliverer emerging from Zion (future) · narrator: Paul, first-person epistolary author, ventriloquizing Isa 59:20 LXX (with Paul's substitution 'out of' for 'to')
  · **edges:** ["M832"] —REPORTS→ M833

**M834** — Paired second line: and he will remove impieties away from Jacob.
  · agent: he (the Deliverer) · operation: turn away (remove — ungodliness, from Jacob) · substrate: ungodliness (as substrate to be removed) · outcome: ungodliness (future) turned away from Jacob by the Deliverer · narrator: Paul, first-person epistolary author, ventriloquizing the continuation of Isa 59:20 LXX
  · **edges:** M834 —BEQUEATHS→ RECEPTION; ["M832"] —CONTAINS→ M834

**M835** — The covenant-formula continuing the quotation: because this is my covenant to them.
  · agent: this (the following covenant-content) · operation: be (my covenant — of this, unto them) · substrate: not-stated (them as recipients) · outcome: the following identified as God's covenant-with-them · narrator: Paul, first-person epistolary author, ventriloquizing Isa 59:21 (opening) / Jer 31:33-echoes

**M836** — The covenant-content, in temporal-clause form: at the time when I remove their offenses.
  · agent: I (God, in direct speech) · operation: take away (remove — their sins, future) · substrate: their sins · outcome: God (future) removing their sins · narrator: Paul, first-person epistolary author, ventriloquizing Isa 27:9 LXX

**M837** — The two-sided attribution about Israel, first side: with respect to the gospel-relation, they stand as enemies — and this is for your sakes.
  · agent: they (Israel) · operation: be (enemies — as concerning the gospel, for your sakes) · substrate: not-stated (their standing-relation) · outcome: Israel standing as enemies with respect to the gospel, for the addressees' sakes · narrator: Paul, first-person epistolary author
  · **edges:** M837 —BEQUEATHS→ RECEPTION

**M838** — The paired second side: but with respect to the election-relation, they stand as beloved — and this is for the fathers' sakes.
  · agent: they (Israel) · operation: be (beloved — as touching the election, for the father's sakes) · substrate: not-stated (their standing-relation) · outcome: Israel standing as beloved with respect to election, for the fathers' sakes · narrator: Paul, first-person epistolary author
  · **edges:** M838 —BEQUEATHS→ RECEPTION

**M839** — The comparison-first-half: for as you, in the times before, did not exercise trust toward God.
  · agent: ye (the Gentile addressees) · operation: not believe (not trust — God, in times past) · substrate: God · outcome: the addressees (in the past) having not trusted God · narrator: Paul, first-person epistolary author
  · **edges:** M839 —BEQUEATHS→ RECEPTION

**M840** — The present-corollary of that past-non-believing: yet in the current time you have taken hold of mercy — and it has come to you through their unbelief.
  · agent: ye (the Gentile addressees) · operation: obtain mercy (be shown mercy — now, through their unbelief) · substrate: not-stated (mercy as received) · outcome: the addressees now having received mercy, mediated through Israel's unbelief · narrator: Paul, first-person epistolary author

**M841** — The comparison-second-half: in the same way, these persons (Israel) have now also failed to exercise trust.
  · agent: these (Israel) · operation: not believe (not trust — now, of these / Israel) · substrate: not-stated (God, implicit as object of non-belief) · outcome: Israel (now) having not trusted · narrator: Paul, first-person epistolary author
  · **edges:** M841 —BEQUEATHS→ RECEPTION

**M842** — The purpose held over M11: that through the mercy shown to you, they too might come to receive mercy.
  · agent: they also (Israel) · operation: obtain mercy (be shown mercy — through your mercy, of them also, purpose) · substrate: not-stated (mercy as intended) · outcome: Israel (in the intended purpose) receiving mercy, mediated through the Gentile mercy-reception · narrator: Paul, first-person epistolary author
  · **edges:** M842 —BEQUEATHS→ RECEPTION

**M843** — The ground for the whole mercy-loop: God has shut them all up — locked them in — inside disobedience.
  · agent: God · operation: conclude (shut up, lock in — them all, in unbelief) · substrate: them all (all humans) · outcome: God having shut all up in unbelief · narrator: Paul, first-person epistolary author
  · **edges:** M843 —BEQUEATHS→ RECEPTION

**M844** — The purpose that governs the shutting-up: so that he might show mercy — upon all.
  · agent: he (God) · operation: have mercy (show mercy — upon all, purpose) · substrate: all · outcome: God (in the purpose) showing mercy upon all · narrator: Paul, first-person epistolary author
  · **edges:** M844 —BEQUEATHS→ RECEPTION

**M845** — Paul bursts into doxological exclamation: oh, the depth — of the wealth, of both the wisdom and the knowledge, of [God — the specifying-genitive is truncated in the source at 'of'].
  · agent: the depth of the riches (of God's wisdom and knowledge) · operation: be (depth of riches — of the wisdom and knowledge of [God, truncated], doxological exclamation) · substrate: not-stated (the specifying 'of God' is truncated at 'of') · outcome: doxological exclamation of the depth-of-riches-of-God's-wisdom-and-knowledge — the substrate-completion is truncated in the source at 'of' · narrator: Paul, first-person epistolary author, breaking into doxological exclamation

**M846** — Completing the specifying-genitive from the prior clause: [of the wisdom and knowledge of] God.
  · agent: the depth of the riches of wisdom and knowledge (from prior) · operation: (specifying-genitive completion — 'God', identifying whose wisdom-and-knowledge M15-prior exclaimed) · substrate: God (as specifying-genitive) · outcome: the M15-prior depth-of-riches specified as God's wisdom-and-knowledge · narrator: Paul, first-person epistolary author, closing the doxological specifying-genitive from the prior passage

**M847** — The doxological exclamation continues: how impossible to search-out his verdict-decisions are!
  · agent: his judgments · operation: be unsearchable (be unfathomable — his judgments, exclamatory) · substrate: not-stated · outcome: God's judgments standing as unsearchable · narrator: Paul, first-person epistolary author, in doxological mode
  · **edges:** M847 —BEQUEATHS→ RECEPTION

**M848** — Paired exclamation: and his paths are beyond tracing out!
  · agent: his ways · operation: be past finding out (be untraceable — his ways, exclamatory) · substrate: not-stated · outcome: God's ways standing as untraceable · narrator: Paul, first-person epistolary author, in doxological mode
  · **edges:** M848 —BEQUEATHS→ RECEPTION

**M849** — First scripturally-attested rhetorical question: who has ever gotten cognitive hold of the Lord's mind?
  · agent: who (interrogated knower) · operation: know (have cognitive hold — the mind of the Lord, interrogatively, who) · substrate: the mind of the Lord · outcome: the impossibility of anyone knowing the Lord's mind put in question · narrator: Paul, first-person epistolary author, ventriloquizing Isa 40:13 LXX
  · **edges:** M849 —BEQUEATHS→ RECEPTION

**M850** — Paired second impossibility-question: or who has ever served him as advisor?
  · agent: who (interrogated advisor) · operation: be counsellor (be advisor — of him, interrogatively, who) · substrate: him (God) · outcome: the impossibility of anyone being God's advisor put in question · narrator: Paul, first-person epistolary author, ventriloquizing the continuation of Isa 40:13
  · **edges:** M850 —BEQUEATHS→ RECEPTION

**M851** — Third impossibility-question: or who has given anything to him first — first, so as to put him in debt?
  · agent: who (interrogated first-giver) · operation: first give (be-first-donor — to him, interrogatively, who) · substrate: to him (God as recipient) · outcome: the impossibility of anyone first-giving to God put in question · narrator: Paul, first-person epistolary author, ventriloquizing Job 41:11 or similar
  · **edges:** M851 —BEQUEATHS→ RECEPTION

**M852** — The consequent-clause of M6: with the result that it would have to be paid back to him again.
  · agent: not-stated (the implicit repayer) · operation: be recompensed (be paid back — to him again) · substrate: it (whatever was given, from M6) · outcome: the given-thing (in the hypothetical) paid back to God — a scenario the M6 impossibility rules out · narrator: Paul, first-person epistolary author
  · **edges:** M852 —BEQUEATHS→ RECEPTION

**M853** — The theological ground the doxology rests on: because from him, and through him, and unto him — everything that is exists.
  · agent: all things · operation: be (all things — of him, through him, to him) · substrate: not-stated (the of-him / through-him / to-him relation-set) · outcome: all-things standing as sourced-in, mediated-by, and directed-toward God (three-fold merged) · narrator: Paul, first-person epistolary author

**M854** — The doxological jussive: to him — let glory be, into the ages.
  · agent: glory · operation: be (glory — to him, for ever, jussive) · substrate: to him (God) · outcome: glory rendered to God, forever (jussive-attribution) · narrator: Paul, first-person epistolary author, in doxological mode

**M855** — Sealed with the affirmation: so-be-it.
  · agent: not-stated (Paul as speaker) · operation: affirm (seal — Amen) · substrate: the M9 doxology (as sealed) · outcome: the M9 doxology sealed with Amen · narrator: Paul, first-person epistolary author

**M856** — Paul opens the ethical section with a kinship-address and appeal-formula: brothers, I earnestly urge you — by the mercies that belong to God — to the following.
  · agent: I (Paul) · operation: beseech (earnestly urge — with recoverable content, by the mercies of God) · substrate: you (brethren) — the content of the appeal (M11a) · outcome: the addressees earnestly urged to the M11a content, on the basis of God's mercies · narrator: Paul, first-person epistolary author, opening the ch 12 ethical-appeal section
  · **edges:** M856 —REPORTS→ M857

**M857** — The content of the appeal: that you place your bodies-yourselves as an offering — a living one, one that is holy and welcome to God.
  · agent: ye (the addressees) · operation: present (place-alongside — your bodies as a living sacrifice, holy, acceptable unto God) · substrate: your bodies (as substrate of the sacrifice-presentation) · outcome: the addressees presenting their bodies as a living, holy, God-welcome sacrifice · narrator: Paul, first-person epistolary author, ventriloquizing the appeal-content
  · **edges:** ["M856"] —REPORTS→ M857

**M858** — Descriptor of that presentation: this is your reasoned-and-appropriate service.
  · agent: the presenting (from M11a) · operation: be (your reasonable service — of the presentation) · substrate: not-stated · outcome: the M11a presentation identified as the addressees' reasonable (logical, spiritual, appropriate) service · narrator: Paul, first-person epistolary author

**M859** — First paired-directive of the ethical formation: do not undergo being shape-conformed to this present age.
  · agent: ye (the addressees) · operation: not be conformed (not be shape-conformed — to this world, imperative-negated) · substrate: this world (the age as substrate of conformity) · outcome: the addressees directed not to undergo shape-conformity to this age · narrator: Paul, first-person epistolary author

**M860** — The paired positive counterpart: rather, undergo metamorphic-transformation, the transformation running through the mind's re-newing.
  · agent: ye (the addressees) · operation: be transformed (be metamorphosed — by the renewing of your mind, imperative) · substrate: not-stated (the mind as location of the renewing-mediation, folded) · outcome: the addressees directed to undergo metamorphic-transformation, mediated through mind-renewing · narrator: Paul, first-person epistolary author

**M861** — The purpose held over the M14 transformation: so that you may test-and-approve what constitutes the good, welcome, and complete will of God.
  · agent: ye (the addressees) · operation: prove (test-and-approve — what is that good, and acceptable, and perfect, will of God, purpose) · substrate: what is that good, and acceptable, and perfect, will of God · outcome: the addressees (in the purpose) testing-and-approving God's three-fold-qualified will · narrator: Paul, first-person epistolary author

**M862** — Paul opens a directive to every individual, mediated by his apostolic grace: for I say, through the favor granted to me, to every person among you — the following.
  · agent: I (Paul, mediated through the grace given to him) · operation: say (address — to every man among you, through the grace given unto me, with recoverable content) · substrate: every man that is among you — the content of the directive (M16a) · outcome: Paul addressing every-individual-among-you with the M16a directive, on the basis of his apostolic grace · narrator: Paul, first-person epistolary author
  · **edges:** M862 —REPORTS→ M863

**M863** — The directive: [each person is] not to reckon-of himself in a way that goes higher than what he [should reckon-of himself — the completing 'ought to think' is truncated in the source at 'than he'].
  · agent: every man (indefinite subject of the directive) · operation: not think of himself more highly (not over-reckon self — than one [ought, truncated]) · substrate: himself (as substrate of the reckoning) · outcome: the person directed not to reckon-of-himself in a way exceeding [what he ought to reckon — per the KJV continuation 'than he ought to think', truncated in the source at 'than he'] · narrator: Paul, first-person epistolary author, ventriloquizing the directive-content
  · **edges:** ["M862"] —REPORTS→ M863

**M864** — Completing the comparative from the prior clause: [more highly than he] ought to reckon-of-himself.
  · agent: he (the indefinite individual from prior M16a) · operation: think (ought to reckon-of-himself — the standard-of-appropriate-thinking) · substrate: not-stated (himself as substrate of the appropriate-reckoning) · outcome: the person's ought-to-reckon standard as the comparative-reference-point for the M16a-prior 'more highly' · narrator: Paul, first-person epistolary author, closing the comparative from the prior passage

**M865** — The positive counterpart-directive: rather, to reckon-of-oneself in the register of sound-mindedness.
  · agent: he (the indefinite individual) · operation: think soberly (reckon-of-oneself in sober-register) · substrate: not-stated · outcome: the person reckoning of himself in the sober-minded register · narrator: Paul, first-person epistolary author

**M866** — The measure-clause that guides the sober self-reckoning: according as God has parceled out a trust-measure to each individual.
  · agent: God · operation: deal (apportion, parcel out — the measure of faith, to every man) · substrate: the measure of faith (as apportioned-portion) · outcome: God having apportioned a faith-measure to each individual · narrator: Paul, first-person epistolary author
  · **edges:** M866 —BEQUEATHS→ RECEPTION

**M867** — First side of the body-analogy: in the same way as we possess many members within a single body.
  · agent: we (as substrate of the body-analogy) · operation: have (possess — many members, in one body) · substrate: many members (in one body) · outcome: we having many members within one body · narrator: Paul, first-person epistolary author

**M868** — The continuing observation about the body-analogy: and the members-all do not carry out the same function.
  · agent: all members · operation: not have (not perform — the same office, of all members) · substrate: the same office (praxis, function) · outcome: the many members not-having identical functions · narrator: Paul, first-person epistolary author

**M869** — The application: in exactly that way, we — although many in number — stand as one body inside the Anointed.
  · agent: we (being many) · operation: be (one body in Christ — of we, being many) · substrate: not-stated (the body-in-Christ location) · outcome: we-many standing as one body located-in-Christ · narrator: Paul, first-person epistolary author

**M870** — The individual-side of that: and every one of us stands as members belonging one to another.
  · agent: every one · operation: be (members one of another — of every one) · substrate: one of another (mutual-membership relation) · outcome: every-individual standing as members-mutually-of-one-another · narrator: Paul, first-person epistolary author

**M871** — The participial-ground for the following gift-directives: since we hold gifts that differ, differing in accord with the favor that has been granted to us.
  · agent: not-stated (we, implicit from M6-M7) · operation: have (possess — gifts differing according to the grace given to us) · substrate: gifts differing (according to the grace given to us) · outcome: we possessing differentiated gifts, each according to the grace given · narrator: Paul, first-person epistolary author

**M872** — The seven-fold gift-directive list, merged: prophesy according to faith-proportion if prophecy is your gift; attend to your service if ministry is your gift; if you are the teacher, attend to teaching; if you are the exhorter, attend to exhortation; the giver — do it with sincerity; the ruler — do it with diligence; the one who shows mercy — do it with cheerfulness.
  · agent: each individual (bearing the specific gift) · operation: exercise-your-gift (each one — in the mode appropriate to it, seven-fold merged directive) · substrate: the seven-fold gift-set: prophecy, ministry, teaching, exhortation, giving, ruling, showing-mercy — each with its appropriate mode (proportion of faith, waiting-on-ministering, on-teaching, on-exhortation, with-simplicity, with-diligence, with-cheerfulness) · outcome: each individual exercising their specific gift in its appropriate mode · narrator: Paul, first-person epistolary author

**M873** — Directive on love: let love stand as unfeigned, without any acting.
  · agent: love · operation: be (without dissimulation — of love, jussive) · substrate: not-stated · outcome: love (in the jussive-directive) standing as unfeigned · narrator: Paul, first-person epistolary author

**M874** — Directive: recoil-from what is evil.
  · agent: ye (addressees, implicit) · operation: abhor (recoil from — that which is evil) · substrate: that which is evil · outcome: the addressees directed to recoil-from-evil · narrator: Paul, first-person epistolary author

**M875** — Paired positive directive: stick-fast-to what is good.
  · agent: ye (addressees) · operation: cleave (adhere-fast to — that which is good) · substrate: that which is good · outcome: the addressees directed to adhere-fast-to-good · narrator: Paul, first-person epistolary author

**M876** — Directive on mutual affection: be tenderly-affectionate to one another — in the sibling-love register.
  · agent: ye (addressees) · operation: be kindly affectioned (be tenderly-affectionate — one to another, with brotherly love) · substrate: one another (as mutual-affection substrate) · outcome: the addressees mutually-tenderly-affectionate in the brotherly-love register · narrator: Paul, first-person epistolary author

**M877** — The next directive opens: in [honour, out-doing-one-another — the completing 'honour preferring one another' is truncated in the source at 'in'].
  · agent: ye (addressees, implicit) · operation: (unstated operation — in [honour preferring one another, truncated at 'in']) · substrate: not-stated (per truncation) · outcome: the imperative directive begun by 'in' — with the completing phrase ('honour preferring one another' per Rom 12:10b) truncated in the source at 'in' · narrator: Paul, first-person epistolary author

**M878** — Completing the directive from the prior clause: [in honour] out-doing one another in preference.
  · agent: ye (addressees, implicit) · operation: prefer (out-do-in-preference — one another, in honour) · substrate: one another · outcome: the addressees mutually out-doing-one-another in honour-preference · narrator: Paul, first-person epistolary author, closing the honour-directive from the prior passage

**M879** — Directive: rejoicing in the hope-register.
  · agent: ye · operation: rejoice (be joyful — in hope) · substrate: hope · outcome: the addressees rejoicing in the hope-register · narrator: Paul, first-person epistolary author

**M880** — Directive: enduring under pressure.
  · agent: ye · operation: be patient (endure — in tribulation) · substrate: tribulation · outcome: the addressees enduring in tribulation · narrator: Paul, first-person epistolary author

**M881** — Directive: staying steadfastly-attentive in prayer.
  · agent: ye · operation: continue instant (persist steadfastly — in prayer) · substrate: prayer · outcome: the addressees continuing steadfastly in prayer · narrator: Paul, first-person epistolary author

**M882** — Directive: rejoicing together with those who are rejoicing.
  · agent: ye · operation: rejoice with (co-rejoice — with them that rejoice) · substrate: them that do rejoice · outcome: the addressees co-rejoicing with rejoicers · narrator: Paul, first-person epistolary author

**M883** — Paired directive: weeping together with those who are weeping.
  · agent: ye · operation: weep with (co-weep — with them that weep) · substrate: them that weep · outcome: the addressees co-weeping with weepers · narrator: Paul, first-person epistolary author

**M884** — Directive: holding the same-mindedness toward one another.
  · agent: ye · operation: be of the same mind (be like-minded — one toward another) · substrate: one toward another (mutual-relation) · outcome: the addressees standing in same-mindedness with one another · narrator: Paul, first-person epistolary author

**M885** — Directive: do not set your mind on high-status things.
  · agent: ye · operation: not mind (not set-the-mind-on — high things) · substrate: high things · outcome: the addressees directed not-to-mind high things · narrator: Paul, first-person epistolary author

**M886** — Paired positive directive: rather, be drawn-along with the low-position people.
  · agent: ye · operation: condescend (be drawn-along with — men of low estate) · substrate: men of low estate · outcome: the addressees drawn-along with the lowly · narrator: Paul, first-person epistolary author

**M887** — Directive: don't be wise-in-your-own-estimation.
  · agent: ye · operation: not be wise (not be — wise in your own conceits) · substrate: not-stated (own-conceits as location of the wise-status) · outcome: the addressees directed not-to-be-wise-in-own-conceits · narrator: Paul, first-person epistolary author

**M888** — Directive: don't pay back to any person harm-for-harm.
  · agent: ye · operation: not recompense (not repay — evil, for evil, to any man) · substrate: evil (as substrate of the non-repayment) · outcome: the addressees directed not-to-repay-evil-for-evil to anyone · narrator: Paul, first-person epistolary author

**M889** — Directive: take-forethought for the things that are honorable in the sight of all people.
  · agent: ye · operation: provide (take-forethought for — things honest, in the sight of all men) · substrate: things honest (in the sight of all men) · outcome: the addressees taking-forethought for what is publicly-honorable · narrator: Paul, first-person epistolary author

**M890** — The conditioning-clause on the peace-directive: if it is possible at all — as far as depends on your side.
  · agent: it (the possibility, and 'lieth in you' — your capacity) · operation: be possible (lie in you — conditional-scope for M14) · substrate: not-stated · outcome: the peace-directive scoped to what is possible and what depends on the addressee · narrator: Paul, first-person epistolary author

**M891** — The main directive under that scope: live in the mode-of-peace with everyone.
  · agent: ye · operation: live peaceably (be at peace — with all men) · substrate: all men · outcome: the addressees living peaceably with all people, within the M13 scope · narrator: Paul, first-person epistolary author
  · **edges:** M891 —BEQUEATHS→ RECEPTION

**M892** — Warm kinship-address: dearly-beloved — do not take-vengeance on your own account.
  · agent: ye (dearly beloved) · operation: not avenge (not take vengeance — yourselves) · substrate: yourselves · outcome: the addressees directed not-to-avenge-themselves · narrator: Paul, first-person epistolary author, using affectionate address (agapētoi)

**M893** — The positive counterpart: rather, give-way-to the wrath (leaving room for God's wrath to act).
  · agent: ye · operation: give place (yield ground — unto wrath) · substrate: wrath (God's wrath, per M17 warrant) · outcome: the addressees yielding ground to (God's) wrath · narrator: Paul, first-person epistolary author

**M894** — Paul brings scriptural warrant: it stands written in scripture.
  · agent: not-stated (scripture as authoritative source) · operation: be written (stand as inscribed in scripture — with recoverable content) · substrate: the cited content (M17a) · outcome: the following claim standing under scriptural warrant · narrator: Paul, first-person epistolary author
  · **edges:** M894 —REPORTS→ M895

**M895** — The cited content, in composite form: 'the vengeance belongs to me — I will make the repayment,' the Lord says.
  · agent: I (the Lord, in direct speech, identified by 'saith the Lord') · operation: be (mine — of vengeance) / repay (of I / God — future) — merged direct-speech content with reporter-identification · substrate: vengeance / the repayment · outcome: the Lord claiming vengeance as his own and promising future-repayment · narrator: Paul, first-person epistolary author, ventriloquizing Deut 32:35 LXX with the 'saith the Lord' reporter-identifier
  · **edges:** ["M894"] —REPORTS→ M895

**M896** — The consequent-directive: therefore if your enemy is going hungry.
  · agent: thine enemy · operation: hunger (be hungry — of thine enemy, conditional) · substrate: not-stated · outcome: the enemy (conditionally) being hungry · narrator: Paul, first-person epistolary author

**M897** — The main directive under that hunger-condition: feed him.
  · agent: thou (addressee, second-person singular) · operation: feed (give food to — him) · substrate: him (thine enemy) · outcome: the addressee directed to feed the hungry enemy · narrator: Paul, first-person epistolary author
  · **edges:** M897 —BEQUEATHS→ RECEPTION

**M898** — Second paired conditional: if he is thirsting.
  · agent: he (thine enemy) · operation: thirst (be thirsty — of he/enemy, conditional) · substrate: not-stated · outcome: the enemy (conditionally) thirsting · narrator: Paul, first-person epistolary author

**M899** — The paired main directive: give him a drink.
  · agent: thou · operation: give (give — drink to him) · substrate: him (drink to him) · outcome: the addressee directed to give-drink to the thirsty enemy · narrator: Paul, first-person epistolary author
  · **edges:** M899 —BEQUEATHS→ RECEPTION

**M900** — The rationale for the enemy-provisions: for by doing that you will pile up burning-coals on his head.
  · agent: thou · operation: heap (pile up — coals of fire, on his head) · substrate: coals of fire · outcome: the addressee (future) heaping coals-of-fire on the enemy's head, by-doing-so · narrator: Paul, first-person epistolary author, ventriloquizing Prov 25:22 LXX
  · **edges:** M900 —BEQUEATHS→ RECEPTION

**M901** — Opening the ch 13 governance-directive: let every human-soul place-oneself-under the authorities that stand above.
  · agent: every soul · operation: be subject (place-oneself-under — the higher powers, jussive) · substrate: the higher powers (authorities standing above) · outcome: every soul (in the jussive) placed-under the higher powers · narrator: Paul, first-person epistolary author, opening ch 13

**M902** — The ground for that directive begins: for there is — [the completing 'no power but of God' is truncated in the source at 'For there is'].
  · agent: not-stated (per truncation) · operation: be (there is — with recoverable content, truncated) · substrate: not-stated (the completing 'no power but of God' is truncated in the source at 'For there is') · outcome: the existential-ground for the M23 directive opened by 'there is' — with the specific content (per Rom 13:1b: 'no power but of God: the powers that be are ordained of God') truncated in the source · narrator: Paul, first-person epistolary author

**M903** — Completing the existential-ground from the prior clause: [no power exists] except through God as source.
  · agent: not-stated (power, existentially and universally negated except through God) · operation: be (no power — but of God, source, existential-ground completion) · substrate: not-stated · outcome: no power standing as existing except through God · narrator: Paul, first-person epistolary author, closing the ground from the prior passage

**M904** — The paired specification: and the powers that presently exist have been set-in-order — set by God.
  · agent: not-stated (God as ordainer) · operation: be ordained (be set-in-order — of God, of the powers-that-be) · substrate: the powers that be · outcome: the existing powers set-in-order by God · narrator: Paul, first-person epistolary author

**M905** — Descriptor of the person the next claim is about: anyone at all who takes a stand against the power.
  · agent: whosoever (indefinite subject) · operation: resist (stand against — the power) · substrate: the power · outcome: the person standing as one who resists the power · narrator: Paul, first-person epistolary author

**M906** — The main claim: that same resisting act is a resisting-against the divine ordering itself.
  · agent: whosoever (from M3, the power-resister) · operation: resist (stand against — the ordinance of God) · substrate: the ordinance of God · outcome: the power-resister standing as one who resists God's ordinance-itself · narrator: Paul, first-person epistolary author

**M907** — The consequence for the resisters: those persons who resist will bring on themselves adverse verdict.
  · agent: they that resist · operation: receive (bring on oneself — damnation, of they that resist) · substrate: damnation (as substrate self-received) · outcome: the resisters bringing damnation upon themselves · narrator: Paul, first-person epistolary author

**M908** — The reason for the M5 consequence: the rulers do not function as a source-of-fear to good works — but rather to the evil.
  · agent: rulers · operation: be (not a terror to good works — but to the evil — of rulers, merged contrastive attribution) · substrate: not-stated · outcome: rulers standing as not-a-terror-to-good-works but as terror-to-the-evil · narrator: Paul, first-person epistolary author

**M909** — Paul turns to the addressee with a rhetorical question: do you want to be non-afraid of the power?
  · agent: thou (addressee) · operation: not be afraid (not fear — of the power, interrogatively) · substrate: the power · outcome: the addressee's willed-non-fear-of-power opened for question · narrator: Paul, first-person epistolary author

**M910** — The answering directive: do that which is good.
  · agent: thou · operation: do (perform — that which is good, imperative) · substrate: that which is good · outcome: the addressee directed to do-good · narrator: Paul, first-person epistolary author

**M911** — The promised consequence: and you will get commendation from the same power.
  · agent: thou · operation: have (receive — praise, from the same, future) · substrate: praise (from the same power) · outcome: the addressee (future) receiving praise from the power · narrator: Paul, first-person epistolary author

**M912** — The theological ground for M9: because he is God's servant, directed toward you for good.
  · agent: he (the ruler) · operation: be (the minister of God to thee for good — of he/the ruler) · substrate: not-stated · outcome: the ruler standing as God's servant, directed-to-thee for good · narrator: Paul, first-person epistolary author

**M913** — The alternative conditional: but if you go and perform that which is evil.
  · agent: thou · operation: do (perform — that which is evil, conditional) · substrate: that which is evil · outcome: the addressee (conditionally) doing evil · narrator: Paul, first-person epistolary author

**M914** — The consequent directive: be afraid.
  · agent: thou · operation: be afraid (fear — imperative) · substrate: not-stated · outcome: the addressee directed to be afraid · narrator: Paul, first-person epistolary author
  · **edges:** M914 —BEQUEATHS→ RECEPTION

**M915** — The reason for the fear: because he does not carry the sword-of-office as a mere empty display.
  · agent: he (the ruler) · operation: not bear (not carry — the sword, in vain, of the ruler) · substrate: the sword · outcome: the ruler standing as one who carries the sword not-in-vain · narrator: Paul, first-person epistolary author

**M916** — Further ground about the ruler: because he stands as God's servant — one who executes vengeance, in order to bring wrath down on the person who does evil.
  · agent: he (the ruler) · operation: be (the minister of God, a revenger to execute wrath — of the ruler, upon him that doeth evil) · substrate: not-stated · outcome: the ruler standing as God's servant and revenger, executing wrath upon the evil-doer · narrator: Paul, first-person epistolary author
  · **edges:** M916 —BEQUEATHS→ RECEPTION

**M917** — The main-summary directive: therefore it is necessary that you be placed-under — and this not only because of the wrath, but also because of conscience.
  · agent: ye (addressees) · operation: be subject (of necessity — place-oneself-under, not only for wrath, but also for conscience sake) · substrate: not-stated (the higher powers) · outcome: the addressees necessarily placing themselves under the higher powers, for the two-fold reason (wrath + conscience) · narrator: Paul, first-person epistolary author

**M918** — The extension to tribute-payment: for this same reason, pay out taxes-tribute also.
  · agent: ye · operation: pay (render — tribute) · substrate: tribute · outcome: the addressees paying tribute · narrator: Paul, first-person epistolary author

**M919** — The ground for the tribute-directive: for they stand as God's [ministers — the completing substantive is truncated in the source at 'they are God's'].
  · agent: they (the rulers) · operation: be (God's [ministers, truncated] — of they/the rulers, ground) · substrate: not-stated (the specifying-substantive 'ministers' is truncated at 'God's') · outcome: the rulers standing as God's [ministers — per the KJV continuation, truncated in the source at 'God's'] · narrator: Paul, first-person epistolary author

**M920** — The civil authorities are described as God's officials whose steady work is exactly the governing/collecting just discussed.
  · agent: they (the authorities of the prior verses) · operation: minister/attend-continually · substrate: this very thing (governance/tribute) · outcome: standing characterization as continually-attending ministers · narrator: Paul, apostolic voice writing to Roman believers

**M921** — The addressees are commanded to pay everyone the specific obligation owed them — the four named kinds together.
  · agent: the addressees (Roman believers) · operation: render · substrate: the set of dues owed to each recipient — tribute, custom, fear, honour · outcome: each due discharged to the party it belongs to · narrator: Paul, apostolic voice

**M922** — The addressees are told to carry no outstanding debt to anyone except the standing debt of mutual love.
  · agent: the addressees · operation: owe (prohibited except for love) · substrate: any debt between persons · outcome: no debt outstanding except the ongoing debt of loving one another · narrator: Paul, apostolic voice
  · **edges:** M922 —BEQUEATHS→ RECEPTION

**M923** — The one who loves the other person is declared to have already met what the law requires.
  · agent: the one who loves another · operation: fulfil (the law) · substrate: the law · outcome: the law fulfilled · narrator: Paul, apostolic voice

**M924** — Paul brings the specific prohibitions of the Decalogue into his text as a set to be reasoned over.
  · agent: Paul · operation: cite · substrate: the set of Decalogue prohibitions (and any other commandment) · outcome: the commandments installed as the set that the next move will subsume · narrator: Paul, apostolic voice
  · **edges:** M924 —CONTAINS→ M925; M924 —CONTAINS→ M926; M924 —CONTAINS→ M927; M924 —CONTAINS→ M928; M924 —CONTAINS→ M929

**M925** — The Torah forbids the act of adultery to the one addressed.
  · agent: the Torah-giver (God, in the voice of the Decalogue) · operation: forbid · substrate: adultery · outcome: adultery prohibited to the addressee · narrator: Paul, citing Torah
  · **edges:** ["M924"] —CONTAINS→ M925

**M926** — The Torah forbids killing to the one addressed.
  · agent: the Torah-giver · operation: forbid · substrate: killing · outcome: killing prohibited · narrator: Paul, citing Torah
  · **edges:** ["M924"] —CONTAINS→ M926

**M927** — The Torah forbids stealing to the one addressed.
  · agent: the Torah-giver · operation: forbid · substrate: stealing · outcome: stealing prohibited · narrator: Paul, citing Torah
  · **edges:** ["M924"] —CONTAINS→ M927

**M928** — The Torah forbids bearing false witness to the one addressed.
  · agent: the Torah-giver · operation: forbid · substrate: bearing false witness · outcome: false witness prohibited · narrator: Paul, citing Torah
  · **edges:** ["M924"] —CONTAINS→ M928

**M929** — The Torah forbids coveting to the one addressed.
  · agent: the Torah-giver · operation: forbid · substrate: coveting · outcome: coveting prohibited · narrator: Paul, citing Torah
  · **edges:** ["M924"] —CONTAINS→ M929

**M930** — Paul claims that any commandment whatsoever is summed up briefly in one particular saying.
  · agent: not-stated (the commandment 'is comprehended' — the agent of the summing is left unnamed) · operation: comprehend/sum-up · substrate: any commandment (the ones just cited, and any other) · outcome: all commandments subsumed into one summarizing saying · narrator: Paul, apostolic voice
  · **edges:** M930 —REPORTS→ M931

**M931** — The saying itself commands the addressee to love the neighbour to the same degree as the self.
  · agent: the addressee of the commandment ('thou') · operation: love (commanded) · substrate: thy neighbour · outcome: neighbour loved as self · narrator: Torah (Lev 19:18), voiced via Paul
  · **edges:** ["M930"] —REPORTS→ M931

**M932** — Love, treated as an agent in its own right, is said never to do harm to the one next to it.
  · agent: love (personified as agent) · operation: do-no-ill · substrate: his neighbour · outcome: no ill/harm produced · narrator: Paul, apostolic voice

**M933** — The passage concludes by equating love itself with the completion of what the law asks.
  · agent: love · operation: fulfil (equative identification) · substrate: the law · outcome: the law identified as fulfilled in love · narrator: Paul, apostolic voice

**M934** — The addressees are told to grasp what moment they are in — a moment whose content is spelled out in a nested claim.
  · agent: the addressees ('you/we') · operation: know (the time) · substrate: the eschatological time · outcome: the time recognized (grounding the nested proposition) · narrator: Paul, apostolic voice
  · **edges:** M934 —REPORTS→ M935

**M935** — The nested content is that the present is the overdue hour at which those addressed must rouse themselves out of a sleeping state.
  · agent: we / the addressees · operation: awake (from sleep) · substrate: sleep (a state of spiritual dormancy) · outcome: awakened at the overdue hour · narrator: Paul, apostolic voice
  · **edges:** ["M934"] —REPORTS→ M935

**M936** — A reason is offered for the urgency: our deliverance now stands closer than it did at some earlier reference point.
  · agent: our salvation · operation: be-nearer (temporal proximity of salvation) · substrate: not-stated (the temporal reference point is truncated in the source: 'than when we ...') · outcome: salvation now stands closer than at the earlier point · narrator: Paul, apostolic voice

**M937** — The addressees' community is recalled to an earlier moment when they first came to trust — the reference point for how much closer things now stand.
  · agent: we (the addressee community, in retrospect) · operation: believe (past coming-to-faith) · substrate: not-stated (the content of the initial believing is left implicit in this fragment) · outcome: having-first-believed, serving as the temporal baseline · narrator: Paul, apostolic voice

**M938** — The stretch of darkness is said to be nearly used up.
  · agent: the night · operation: be-far-spent · substrate: not-stated (the time-container itself is the state-bearer) · outcome: the night characterized as almost over · narrator: Paul, apostolic voice

**M939** — The stretch of light is said to be right up close.
  · agent: the day · operation: be-at-hand · substrate: not-stated · outcome: the day characterized as imminent · narrator: Paul, apostolic voice

**M940** — The addressees are exhorted to strip off the practices that belong to the dark stretch.
  · agent: we (the addressees, including the speaker) · operation: cast-off · substrate: the works of darkness · outcome: the dark-time practices removed · narrator: Paul, apostolic voice

**M941** — The addressees are exhorted to clothe themselves with the equipment that belongs to the light stretch.
  · agent: we (the addressees) · operation: put-on · substrate: the armour of light · outcome: the light-time equipment worn · narrator: Paul, apostolic voice

**M942** — The addressees are urged to conduct themselves openly and decently, as one behaves when it is daylight — with a list of the excesses that must be absent.
  · agent: we (the addressees) · operation: walk (conduct oneself) · substrate: our conduct, specified negatively as absent of rioting, drunkenness, chambering, wantonness, strife, envying · outcome: conduct that stands up in daylight · narrator: Paul, apostolic voice

**M943** — The addressees are commanded — now with a direct 'you' — to clothe themselves specifically with the person of the Lord Jesus Christ.
  · agent: you (the addressees) · operation: put-on · substrate: the Lord Jesus Christ (as garment/person to be put on) · outcome: Christ worn as the covering-person · narrator: Paul, apostolic voice

**M944** — The addressees are told not to make advance arrangements for the body's cravings, since such arrangement would end up feeding them.
  · agent: you (the addressees) · operation: make-provision (prohibited) · substrate: the flesh · outcome: no provisioning of the flesh, so its lusts go unfed · narrator: Paul, apostolic voice

**M945** — The addressees are commanded to welcome the one whose trust is not strong — but not for the purpose of drawing him into contested arguments.
  · agent: you (the addressees, understood as the stronger) · operation: receive · substrate: the one who is weak in the faith · outcome: the weak one welcomed into the community, without being drawn into disputes · narrator: Paul, apostolic voice
  · **edges:** M945 —BEQUEATHS→ RECEPTION

**M946** — One kind of person, Paul reports, is convinced that everything is permissible food.
  · agent: one (a person of the first type) · operation: believe · substrate: the proposition that he is free to eat anything · outcome: that person holds the eating-freedom conviction · narrator: Paul, apostolic voice
  · **edges:** M946 —REPORTS→ M947

**M947** — The nested content is that this person takes himself to be allowed to eat every kind of thing.
  · agent: he (the believing eater) · operation: be-permitted-to-eat · substrate: all things (as food) · outcome: eating of all things stands as permitted for him · narrator: Paul, embedding within the reported belief
  · **edges:** ["M946"] —REPORTS→ M947

**M948** — Another kind of person — the one whose trust is not strong — is described as eating only plant food.
  · agent: another (the person whose faith is weak) · operation: eat · substrate: herbs · outcome: herbs eaten (as the whole diet) · narrator: Paul, apostolic voice

**M949** — The one who does eat is commanded not to look down on the one who abstains.
  · agent: him that eateth · operation: despise (prohibited) · substrate: him that eateth not (the abstainer) · outcome: no contempt directed at the abstainer · narrator: Paul, apostolic voice

**M950** — The one who abstains is commanded not to pass sentence on the one who does eat.
  · agent: him which eateth not (the abstainer) · operation: judge (prohibited) · substrate: him that eateth · outcome: no verdict passed against the eater · narrator: Paul, apostolic voice

**M951** — The reason offered for both prohibitions is that God himself has already welcomed the person in question.
  · agent: God · operation: receive · substrate: him (the disputed person, whether eater or abstainer) · outcome: the person already stands as welcomed by God · narrator: Paul, apostolic voice
  · **edges:** M951 —BEQUEATHS→ RECEPTION

**M952** — The judging addressee is directly challenged: what standing has he to pronounce on someone else's household servant?
  · agent: Paul (the challenger) · operation: challenge/rebuke (rhetorical question) · substrate: you (the one judging another's servant) · outcome: the judging addressee's standing to judge exposed as null · narrator: Paul, apostolic voice
  · **edges:** M952 —BEQUEATHS→ RECEPTION

**M953** — It is claimed that whether the servant keeps his feet or falls is a matter between him and his own master.
  · agent: he (the servant / disputed person) · operation: stand-or-fall (with-respect-to-master) · substrate: not-stated (the standing-or-falling is his own state; the relational anchor is his own master) · outcome: his standing or falling accountable only to his own master · narrator: Paul, apostolic voice

**M954** — The passage insists — before the reason arrives — that the servant will in fact be kept upright.
  · agent: he (the servant / disputed person) · operation: hold-up (be upheld) · substrate: not-stated (the upholder is left unnamed at this point; the warrant that follows is truncated in the source with 'for') · outcome: he will be kept upright rather than falling · narrator: Paul, apostolic voice

**M955** — The warrant is completed: the divine power itself is what has the capacity to keep the disputed person on his feet.
  · agent: God · operation: make-stand (able-to) · substrate: him (the disputed person / servant of the prior verse) · outcome: the divine capacity to uphold him established as the ground of the earlier assurance · narrator: Paul, apostolic voice

**M956** — One kind of person is described as ranking one day higher in worth than another.
  · agent: one man · operation: esteem (differentially, one day above another) · substrate: days (compared against one another) · outcome: one day valued higher than another · narrator: Paul, apostolic voice

**M957** — Another kind of person is described as treating every day as of equal worth.
  · agent: another (man) · operation: esteem (undifferentially, every day alike) · substrate: every day · outcome: all days valued equally · narrator: Paul, apostolic voice

**M958** — Each person is exhorted to reach full personal conviction within his own inner reasoning.
  · agent: every man · operation: be-persuaded (fully) · substrate: his own mind · outcome: full inner conviction attained · narrator: Paul, apostolic voice

**M959** — The one who marks a day as special is characterized as doing so with the Lord as its orientation.
  · agent: he that regardeth the day · operation: regard (the day, oriented to the Lord) · substrate: the day · outcome: the day-regarding oriented to/for the Lord · narrator: Paul, apostolic voice

**M960** — The one who does not mark a day as special is likewise characterized as having the Lord as the orientation of that non-observance.
  · agent: he that regardeth not the day · operation: regard-not (the day, oriented to the Lord) · substrate: the day · outcome: the not-regarding oriented to/for the Lord · narrator: Paul, apostolic voice

**M961** — The one who does eat is characterized as eating with the Lord as the orientation of that eating.
  · agent: he that eateth · operation: eat (oriented to the Lord) · substrate: food (implicit) · outcome: eating oriented to/for the Lord · narrator: Paul, apostolic voice

**M962** — The evidence Paul supplies is that the eater is one who offers thanks to God.
  · agent: he (the eater) · operation: give-thanks (to God) · substrate: God · outcome: thanks addressed to God, evidencing the Lord-orientation of the eating · narrator: Paul, apostolic voice

**M963** — The one who does not eat is likewise characterized as making the abstention oriented to the Lord.
  · agent: he that eateth not · operation: eat-not (oriented to the Lord) · substrate: food (implicit) · outcome: abstention oriented to/for the Lord · narrator: Paul, apostolic voice

**M964** — The abstainer, too, is characterized as one who offers thanks to God.
  · agent: he (the abstainer) · operation: give-thanks (to God) · substrate: God · outcome: thanks addressed to God, evidencing the Lord-orientation of the abstention · narrator: Paul, apostolic voice

**M965** — If the collective is in the state of living, that living is oriented to the Lord.
  · agent: we · operation: live (oriented to the Lord) · substrate: not-stated (our life as the ongoing state) · outcome: living oriented to/for the Lord · narrator: Paul, apostolic voice

**M966** — If the collective is in the state of dying, that dying too is oriented to the Lord.
  · agent: we · operation: die (oriented to the Lord) · substrate: not-stated (our death as the terminal state) · outcome: dying oriented to/for the Lord · narrator: Paul, apostolic voice

**M967** — The conclusion drawn is that across either state — living or dying — the collective belongs to the Lord.
  · agent: we · operation: be-the-Lord's (belong-to) · substrate: not-stated (belonging is a relational state, not directed at a substrate) · outcome: identity as the Lord's people established across the life/death alternation · narrator: Paul, apostolic voice

**M968** — The warrant offered is that Christ underwent death for the purpose of holding the lordship over both the dead and the living.
  · agent: Christ · operation: die · substrate: himself (his own life) · outcome: Christ dead — folded purpose modifier: aimed at his lordship over both dead and living · narrator: Paul, apostolic voice
  · **edges:** M968 —BEQUEATHS→ RECEPTION

**M969** — The warrant continues: Christ then came back up from that death and stood alive again — with the same lordship-purpose in view.
  · agent: Christ · operation: rise/revive (come alive again) · substrate: himself (his dead state) · outcome: Christ risen and alive again — folded purpose modifier: aimed at his lordship over both dead and living · narrator: Paul, apostolic voice
  · **edges:** M969 —BEQUEATHS→ RECEPTION

**M970** — The addressee is challenged: on what basis does he pass sentence on the fellow-member?
  · agent: Paul (the challenger) · operation: judge (challenged rhetorically) · substrate: you (the addressee's judging stance toward the brother) · outcome: the judging exposed as unjustified given M13-M15 · narrator: Paul, apostolic voice

**M971** — A parallel challenge: on what basis does the addressee treat the fellow-member as of no account?
  · agent: Paul (the challenger) · operation: set-at-nought (challenged rhetorically) · substrate: you (the addressee's contempt-stance toward the brother) · outcome: the contempt exposed as unjustified · narrator: Paul, apostolic voice

**M972** — The reason offered for the rebukes is that the whole collective is destined to be positioned before the coming tribunal.
  · agent: we all · operation: stand-before (the judgment) · substrate: the judgment (seat — truncated at 'judgment' in the source) · outcome: all members positioned before the coming tribunal (bracketing peer-judgment in this life) · narrator: Paul, apostolic voice
  · **edges:** M972 —BEQUEATHS→ RECEPTION

**M973** — The seat before which the community will be positioned is identified as belonging to the risen one — completing the substrate of the truncated prior claim.
  · agent: the judgment seat · operation: be-of / belong-to (attribution of the seat) · substrate: not-stated · outcome: the seat identified as Christ's · narrator: Paul, apostolic voice

**M974** — Paul warrants what follows by bringing a written scripture into his text.
  · agent: Paul (via the it-is-written formula) · operation: cite (scripture) · substrate: the scripture-move being introduced · outcome: scriptural saying installed as the warranting text · narrator: Paul, apostolic voice
  · **edges:** M974 —REPORTS→ M975

**M975** — The scripture reports that the Lord himself is the speaker of what follows, on the strength of his own life as oath.
  · agent: the Lord · operation: say (with oath-formula) · substrate: the set of sworn futurities (M4, M5) · outcome: the Lord's sworn declaration installed as the content of the citation · narrator: Scripture (Isa 45:23-style oracle), embedded within Paul's citation
  · **edges:** M975 —CONTAINS→ M976; M975 —CONTAINS→ M977; ["M974"] —REPORTS→ M975

**M976** — The nested oath predicts that every knee will bend before the Lord.
  · agent: every knee · operation: bow (future) · substrate: the Lord (me) · outcome: universal bowing before the Lord · narrator: Scripture, voiced by God through Paul
  · **edges:** M976 —BEQUEATHS→ RECEPTION; ["M975"] —CONTAINS→ M976

**M977** — The nested oath predicts that every tongue will make acknowledgement to God.
  · agent: every tongue · operation: confess (future) · substrate: God · outcome: universal confessing/acknowledgement to God · narrator: Scripture, voiced by God through Paul
  · **edges:** M977 —BEQUEATHS→ RECEPTION; ["M975"] —CONTAINS→ M977

**M978** — Drawing the inference from the sworn universal reckoning, Paul urges the community to stop passing sentence on each other.
  · agent: we (the addressee community, including the speaker) · operation: judge (prohibited, cessation) · substrate: one another · outcome: peer-judgment ceased henceforth · narrator: Paul, apostolic voice

**M979** — In the positive place of that prohibition, Paul redirects the community's decision-making onto a specific communal resolve.
  · agent: we / you (the addressee community) · operation: decide/determine (this rather) · substrate: the decision-content nested as M8 · outcome: the community's judging redirected onto the M8 resolve · narrator: Paul, apostolic voice
  · **edges:** M979 —REPORTS→ M980

**M980** — The decided-upon resolve is that no member place anything in the fellow-member's path that would trip him or occasion his falling.
  · agent: no man (any member of the community, as should-not-do) · operation: put (a stumbling-cause, prohibited) · substrate: stumblingblock / occasion-to-fall (near-synonymous pair merged) in his brother's way · outcome: no member causes another to trip or fall in his path · narrator: Paul, apostolic voice (as content of the community's resolve)
  · **edges:** ["M979"] —REPORTS→ M980

**M981** — Paul reports his own settled conviction — held both as personal knowledge and as a conviction he attributes to the Lord's persuading — that something further is the case.
  · agent: I (Paul) · operation: know / be-persuaded (composite cognition) · substrate: the proposition nested as M10 · outcome: Paul's settled conviction installed, with the Lord Jesus named as the source of the persuading · narrator: Paul, apostolic voice
  · **edges:** M981 —REPORTS→ M982

**M982** — The nested conviction is that no thing carries uncleanness as a property intrinsic to itself.
  · agent: no thing (universal negative quantifier over things) · operation: be-unclean (intrinsically, negated) · substrate: not-stated · outcome: the property of intrinsic uncleanness attributed to nothing · narrator: Paul (as the content of his known/persuaded conviction)
  · **edges:** ["M981"] —REPORTS→ M982

**M983** — In counterbalance: for the specific person who takes something to be unclean, uncleanness does hold with respect to him.
  · agent: it (the thing in question) · operation: be-unclean (relationally, to a specific person) · substrate: him that esteemeth it to be unclean (the reckoner as the frame-of-reference) · outcome: uncleanness holds relative to that person · narrator: Paul, apostolic voice

**M984** — It is claimed that if a fellow-member is pained by what the addressee eats, then the addressee is no longer conducting himself in a way that shows love.
  · agent: you (the addressee) · operation: walk (charitably, negated) · substrate: not-stated (your conduct as it stands under the folded condition) · outcome: the conduct disqualified from walking-charitably · narrator: Paul, apostolic voice

**M985** — The addressee is commanded not to use his eating to bring ruin upon the fellow-member on whose behalf Christ underwent death.
  · agent: you (the addressee) · operation: destroy (prohibited) · substrate: him (thy brother, for whom Christ died) · outcome: the brother not destroyed by the addressee's eating · narrator: Paul, apostolic voice

**M986** — The warrant is that the divine reign is not identified with food and drink at all, but with rightness, peace, and joy — the last of these rooted in the Holy Spirit.
  · agent: the kingdom of God · operation: be (identification) · substrate: not-stated · outcome: the kingdom's identity fixed on righteousness, peace, and joy in the Holy Ghost — with the food/drink identification negated · narrator: Paul, apostolic voice

**M987** — A further warrant is offered: the person whose service of Christ takes place in these very things — righteousness, peace, joy — stands as one welcomed by the unnamed addressee (truncated).
  · agent: he that in these things serveth Christ · operation: be-acceptable · substrate: not-stated (the recipient of the acceptability is truncated in the source at 'acceptable to') · outcome: the Christ-server's acceptable status established · narrator: Paul, apostolic voice

**M988** — The Christ-server whose acceptability was left mid-sentence in the prior segment is completed as one whose acceptability is before the divine addressee.
  · agent: he that serveth Christ (the subject inherited from the truncated prior move) · operation: be-acceptable · substrate: God · outcome: the Christ-server's acceptable status before God established · narrator: Paul, apostolic voice

**M989** — The same server is characterized on a second axis as one who is signed off on by the human community.
  · agent: he that serveth Christ · operation: be-approved-of · substrate: men (the human community as the approving frame) · outcome: approved-status established on the human axis · narrator: Paul, apostolic voice

**M990** — The community is urged to pursue whatever contributes to peace and to mutual building-up.
  · agent: we (the addressee community, including the speaker) · operation: follow-after (pursue) · substrate: the things which make for peace and the things by which one may build another up · outcome: peace-conducing and mutually-edifying things pursued · narrator: Paul, apostolic voice

**M991** — For the sake of food, the addressee is commanded not to tear down what the divine agent has built.
  · agent: you (the addressee) · operation: destroy (prohibited) · substrate: the work of God · outcome: God's work not torn down for the sake of food · narrator: Paul, apostolic voice

**M992** — It is granted as a general truth that everything is unpolluted.
  · agent: all things · operation: be-pure · substrate: not-stated · outcome: purity holds for all things without exception · narrator: Paul, apostolic voice

**M993** — In counterbalance: for the specific person whose eating causes offense, the eating is bad.
  · agent: it (the eating) · operation: be-evil (relationally, to the offense-causing eater) · substrate: that man who eateth with offence · outcome: an evil evaluation holds relative to that eater · narrator: Paul, apostolic voice

**M994** — The good course is characterized as refraining from meat, from wine, and from anything at all that trips, offends, or weakens the fellow-member.
  · agent: not-stated (the abstention-course is the state-bearer) · operation: be-good (of abstention-set) · substrate: the set of abstentions: not eating flesh, not drinking wine, not doing anything by which the brother trips / is offended / is made weak · outcome: the goodness-evaluation applied to this abstention-set · narrator: Paul, apostolic voice

**M995** — The addressee is put to a direct question about whether he holds conviction.
  · agent: Paul (the querier) · operation: have-faith (queried) · substrate: the addressee's faith-state · outcome: the addressee's holding of faith put on the table as the premise of what follows · narrator: Paul, apostolic voice

**M996** — The addressee is commanded to keep that conviction between himself and the divine addressee.
  · agent: you (the addressee) · operation: have (privately, before God) · substrate: it (the faith) · outcome: the faith held privately, in the presence of God rather than imposed on the brother · narrator: Paul, apostolic voice

**M997** — A blessing is pronounced upon the person who does not turn a verdict against himself for what he in fact permits himself.
  · agent: he that condemneth not himself in what he alloweth · operation: be-happy (blessed) · substrate: not-stated · outcome: happy/blessed status pronounced on this person · narrator: Paul, apostolic voice

**M998** — In counter to that blessing: the wavering one, if he goes ahead and eats, stands condemned — because that eating does not proceed from conviction.
  · agent: he that doubteth · operation: be-damned (condemned) · substrate: not-stated · outcome: condemnation-status holds for the doubter when he eats · narrator: Paul, apostolic voice

**M999** — The universal principle is stated: anything at all that does not proceed from conviction counts as missing-the-mark.
  · agent: whatsoever is not of faith · operation: be-sin (identification) · substrate: not-stated · outcome: sin-status identified with all not-of-faith action · narrator: Paul, apostolic voice
  · **edges:** M999 —BEQUEATHS→ RECEPTION

**M1000** — The stronger-in-faith are told they are obliged to carry the not-strong points of the weaker-in-faith.
  · agent: we that are strong · operation: bear (an obligation) · substrate: the infirmities of the weak · outcome: the weaker's infirmities carried by the stronger · narrator: Paul, apostolic voice
  · **edges:** M1000 —BEQUEATHS→ RECEPTION

**M1001** — The paired obligation is that the strong not make themselves the object of their own pleasing.
  · agent: we (the strong) · operation: please (self, prohibited) · substrate: ourselves · outcome: self-pleasing avoided as an aim · narrator: Paul, apostolic voice

**M1002** — Each member is exhorted to make the fellow-member the object of his pleasing, for the fellow-member's own good — with a purpose-modifier truncated in the source.
  · agent: every one of us · operation: please (neighbour) · substrate: his neighbour · outcome: the neighbour pleased for his own good (purpose-clause truncated in source at 'to') · narrator: Paul, apostolic voice

**M1003** — The truncated purpose slot from the prior segment is filled in: the aim named is the building-up of the fellow-member.
  · agent: not-stated (the neighbour, understood as the one being built up) · operation: build-up (edify) · substrate: not-stated · outcome: building-up identified as the aim of the pleasing-the-neighbour directive of the prior segment · narrator: Paul, apostolic voice

**M1004** — The warrant is that Christ, of all people, did not act to please himself.
  · agent: Christ · operation: please (self, negated) · substrate: himself · outcome: self-pleasing not done by Christ, established as the pattern-example · narrator: Paul, apostolic voice

**M1005** — Paul supplies a written scripture as the further ground for the Christ-example.
  · agent: Paul (via the it-is-written formula) · operation: cite (scripture) · substrate: the scripture-move nested as M4 · outcome: the scriptural saying installed as warranting text for M2 · narrator: Paul, apostolic voice
  · **edges:** M1005 —REPORTS→ M1006

**M1006** — The nested scripture has an 'I' speaker (read by Paul as Christ) saying that the insults directed against a 'thee' (God) came down on him instead.
  · agent: the reproaches (of those who reproached thee) · operation: fall (upon me) · substrate: me (the psalm-speaker, read by Paul as Christ) · outcome: reproaches landing on the me-speaker, not on the addressed 'thee' · narrator: Scripture (psalm-voice), embedded within Paul's citation
  · **edges:** ["M1005"] —REPORTS→ M1006

**M1007** — The universal principle is stated: everything written back then was in fact set down for the addressees' learning, with the aim that they might hold hope through what those scriptures teach about endurance and comfort.
  · agent: not-stated (the writing-agent is left unnamed in the passive) · operation: be-written (for our learning) · substrate: whatsoever things were written aforetime · outcome: written for our learning, folded purpose: that we through patience and comfort of the scriptures might have hope · narrator: Paul, apostolic voice

**M1008** — Paul directs a prayer-form at the divine addressee, asking that the source of endurance and comfort bestow a particular state on the community.
  · agent: the God of patience and consolation · operation: grant (wish/optative form) · substrate: the granted state, nested as M7 · outcome: the wished-for state placed under divine granting · narrator: Paul, apostolic voice
  · **edges:** M1008 —REPORTS→ M1009

**M1009** — The nested wished-for state is that the addressees hold one shared mind toward one another, in a way patterned on Christ, with the further aim of shared-voice praise-giving to God.
  · agent: you (the addressee community) · operation: be-likeminded (one toward another) · substrate: one another (reciprocal target) · outcome: mutual likemindedness held, folded purpose: that ye may with one mind and one mouth glorify God, even the Father of our Lord Jesus Christ · narrator: Paul, embedded as the content of his wish-move
  · **edges:** ["M1008"] —REPORTS→ M1009

**M1010** — Drawing the conclusion, the addressees are commanded to welcome each other into the community.
  · agent: you (the addressees) · operation: receive · substrate: one another · outcome: mutual reception into the community established as the required practice · narrator: Paul, apostolic voice

**M1011** — The pattern for that reception is given: Christ, on his part, welcomed the addressees, and did so for the sake of the divine glory.
  · agent: Christ · operation: receive · substrate: us · outcome: us received to the glory of God (the 'to the glory of God' modifier folded as purpose of the receiving) · narrator: Paul, apostolic voice
  · **edges:** M1011 —BEQUEATHS→ RECEPTION

**M1012** — Paul now makes an explicit first-person assertion, introducing a substantial theological claim.
  · agent: I (Paul) · operation: say (assert) · substrate: the proposition nested as M11 · outcome: the assertion made on Paul's own authority · narrator: Paul, apostolic voice
  · **edges:** M1012 —REPORTS→ M1013

**M1013** — The nested content is that Jesus Christ took on a ministering role directed at the circumcised — a role oriented to the divine truth, aimed at making good the promises previously made to the ancestral fathers, and also aimed at giving the non-Jewish nations a ground for praising God for his kindness.
  · agent: Jesus Christ · operation: be-minister-of (the circumcision) · substrate: the circumcision · outcome: minister-role held toward the circumcised — with three folded purpose-modifiers: (1) 'for the truth of God' as ground; (2) 'to confirm the promises made unto the fathers' as aim 1; (3) 'and that the Gentiles might glorify God for his mercy' as aim 2 · narrator: Paul (as the content of his said-move)
  · **edges:** M1013 —BEQUEATHS→ RECEPTION; ["M1012"] —REPORTS→ M1013

**M1014** — A further scripture-citation is initiated but truncated in the source.
  · agent: Paul (via the as-it-is-written formula) · operation: cite (initiated, truncated) · substrate: not-stated (the scriptural content is truncated in the source at 'as it') · outcome: citation formula begun; content-move not coded due to truncation · narrator: Paul, apostolic voice

**M1015** — The truncated citation formula from the prior segment is completed: Paul frames what follows as a scriptural writing.
  · agent: Paul (via the it-is-written formula) · operation: cite (scripture) · substrate: the scripture-moves nested as M2 and M3 · outcome: the first scriptural saying installed as warranting text for the Gentile-glorification claim of the prior segment · narrator: Paul, apostolic voice
  · **edges:** M1015 —CONTAINS→ M1016; M1015 —CONTAINS→ M1017

**M1016** — The cited psalm has an 'I' speaker who declares he will publicly acknowledge the addressed 'thee' while standing among the non-Jewish peoples.
  · agent: I (the psalm-speaker, read by Paul as one whose praise reaches Gentile ears) · operation: confess (to thee, among the Gentiles) · substrate: thee (the addressed divine 'you') · outcome: public acknowledgement given to God in the presence of Gentile hearers · narrator: Psalm-speaker, embedded within Paul's citation
  · **edges:** ["M1015"] —CONTAINS→ M1016

**M1017** — The same speaker further declares he will offer song to the addressed one's name.
  · agent: I (the psalm-speaker) · operation: sing (to thy name) · substrate: thy name · outcome: song given to the divine name · narrator: Psalm-speaker, embedded within Paul's citation
  · **edges:** ["M1015"] —CONTAINS→ M1017

**M1018** — Paul brings a further scriptural saying into his text as additional warrant.
  · agent: Paul (via the and-again formula) · operation: cite (scripture, again) · substrate: the scripture-move nested as M5 · outcome: a second scriptural saying installed as further warrant · narrator: Paul, apostolic voice
  · **edges:** M1018 —REPORTS→ M1019

**M1019** — The second scripture directly summons the non-Jewish peoples — and the whole set of peoples — to raise praise to the Lord.
  · agent: all ye Gentiles / all ye people (paired addressee-agent) · operation: praise / laud · substrate: the Lord (him) · outcome: praise raised to the Lord by all peoples · narrator: Scripture-voice (psalter), embedded within Paul's citation
  · **edges:** ["M1018"] —REPORTS→ M1019

**M1020** — Paul brings a third scriptural saying, this time explicitly attributed to Isaiah.
  · agent: Paul (via the and-again formula) · operation: cite (scripture, again — with named prophet) · substrate: the Isaiah-saying move nested as M7 · outcome: a third scriptural saying installed as further warrant, with the prophet named · narrator: Paul, apostolic voice
  · **edges:** M1020 —REPORTS→ M1021

**M1021** — The nested layer has Isaiah as the speaker who says what follows.
  · agent: Esaias (Isaiah) · operation: say · substrate: the set of prophetic claims nested as M8, M9, M10 · outcome: Isaiah's saying installed as the content of Paul's citation · narrator: Paul, embedding Isaiah as the speaker within his citation
  · **edges:** M1021 —CONTAINS→ M1022; M1021 —CONTAINS→ M1023; M1021 —CONTAINS→ M1024; ["M1020"] —REPORTS→ M1021

**M1022** — The first sub-claim within Isaiah's saying is that a root growing from Jesse will come into being.
  · agent: a root of Jesse · operation: be (future existence) · substrate: not-stated · outcome: the future existence of the Jesse-root established as prophesied · narrator: Isaiah, embedded within Paul's citation
  · **edges:** ["M1021"] —CONTAINS→ M1022

**M1023** — The second sub-claim, appositionally identifying the same being, is that he will come up to rule over the non-Jewish nations.
  · agent: he (the Jesse-root, coreferential with M8) · operation: rise (to reign over the Gentiles) · substrate: the Gentiles (as the reigned-over) · outcome: arisen to reign over the Gentiles · narrator: Isaiah, embedded within Paul's citation
  · **edges:** ["M1021"] —CONTAINS→ M1023

**M1024** — The third sub-claim is that the non-Jewish peoples will place their trust in him.
  · agent: the Gentiles · operation: trust (in him) · substrate: him (the Jesse-root) · outcome: Gentile trust placed in him · narrator: Isaiah, embedded within Paul's citation
  · **edges:** ["M1021"] —CONTAINS→ M1024

**M1025** — Paul turns to a prayer-form: he asks that the source of hope pour a fullness into the addressees.
  · agent: the God of hope · operation: fill (wish/optative form) · substrate: the filled-state nested as M12 · outcome: the wished-for filling placed under divine granting · narrator: Paul, apostolic voice
  · **edges:** M1025 —REPORTS→ M1026

**M1026** — The nested wished-for state is that the addressees find themselves saturated with joy and peace as they exercise their trust — so that their hope may overflow, powered by the Holy Spirit.
  · agent: you (the addressee community) · operation: be-filled (with all joy and peace, in believing) · substrate: all joy and peace (as the filling content) · outcome: filled state realized in the act of believing, folded purpose: that ye may abound in hope, folded instrument: through the power of the Holy Ghost · narrator: Paul, embedded as the content of his wish-move
  · **edges:** ["M1025"] —REPORTS→ M1026

**M1027** — Paul reports his own settled conviction about the addressees, addressing them warmly as siblings.
  · agent: I myself also (Paul) · operation: be-persuaded (of you) · substrate: the proposition about the addressees, nested as M14 and M15 · outcome: Paul's own conviction about the addressees installed alongside the prayer · narrator: Paul, apostolic voice
  · **edges:** M1027 —CONTAINS→ M1028; M1027 —CONTAINS→ M1029

**M1028** — The nested conviction is that the addressees are already carrying an inner fullness — full of goodness and equally full of the whole scope of knowledge.
  · agent: ye (the addressees) · operation: be-full-of / be-filled-with · substrate: goodness and all knowledge (paired filling-content) · outcome: fullness held on both the goodness-axis and the knowledge-axis · narrator: Paul (as the content of his persuaded-move)
  · **edges:** ["M1027"] —CONTAINS→ M1028

**M1029** — The further nested conviction is that the addressees are equipped to correct and counsel one another.
  · agent: ye (the addressees) · operation: be-able (to admonish one another) · substrate: one another (the reciprocal target of the potential admonishing) · outcome: capability to admonish one another established as held · narrator: Paul (as the content of his persuaded-move)
  · **edges:** ["M1027"] —CONTAINS→ M1029

**M1030** — Paul offers a meta-comment on the letter itself: he has written more forwardly than he might have, in a certain measure, functioning as a reminder, and prompted by the gift previously given to him — the reason-slot truncated in the source.
  · agent: I (Paul) · operation: write (boldly, in part, as a reminder, because of the grace) · substrate: you (the addressees) · outcome: the letter written with heightened boldness, in some measure, functioning as reminder, folded reason: 'because of the grace [given to me]' (truncated at 'the grace') · narrator: Paul, apostolic voice

**M1031** — The truncated causal slot from the prior segment is completed: the grace in question is one placed on Paul by the divine source.
  · agent: God · operation: give (grace) · substrate: me (Paul, as recipient) · outcome: grace given to Paul by God — the reason-source of the letter's boldness · narrator: Paul, apostolic voice

**M1032** — The aim named for that gift is that Paul stand as an official-minister figure for Christ Jesus, oriented toward the non-Jewish nations.
  · agent: I (Paul) · operation: be-minister-of (Christ Jesus, to the Gentiles) · substrate: the Gentiles (as the recipient-set of the ministering) · outcome: official minister-role held toward the Gentiles under Christ · narrator: Paul, apostolic voice

**M1033** — The concrete form of that ministering is Paul's priestly-style handling of the divine good-news.
  · agent: I (Paul) · operation: priestly-minister (the gospel) · substrate: the gospel of God · outcome: the gospel of God handled in priestly-ministering mode by Paul · narrator: Paul, apostolic voice
  · **edges:** M1033 —BEQUEATHS→ RECEPTION

**M1034** — The further aim is that the offering-up of the non-Jewish peoples themselves stand as acceptable — an offering the Holy Spirit has made sacred.
  · agent: the offering-up of the Gentiles · operation: be-acceptable · substrate: not-stated (God as implicit recipient) · outcome: acceptable-status established for the Gentile-offering — folded participial modifier: 'being sanctified by the Holy Ghost' identifies the Holy Ghost as the sanctifying agent that makes the offering acceptable · narrator: Paul, apostolic voice
  · **edges:** M1034 —BEQUEATHS→ RECEPTION

**M1035** — Paul draws the inference that he holds a legitimate ground to boast — but that boast is routed through Christ and confined to the God-facing dimension of things.
  · agent: I (Paul) · operation: have (a ground for glorying) · substrate: not-stated (the possessed ground itself) · outcome: possession of a ground-for-glorying established, folded instrument 'through Jesus Christ' and folded domain 'in those things which pertain to God' restricting the mode and scope of the glorying · narrator: Paul, apostolic voice

**M1036** — The self-restraint on that boast is that Paul refuses to bring up anything falling outside the range of what Christ has actually accomplished through him — that range being directed at Gentile obedience and realized in speech, action, remarkable signs, and the Spirit's power.
  · agent: I (Paul) · operation: dare-to-speak (negated, of anything outside Christ's actual work through Paul) · substrate: any of those things which Christ hath not wrought by me (the negated-scope substrate) · outcome: Paul commits not to speak beyond the scope of Christ's actual working through him; folded modifiers describe that working — purpose 'to make the Gentiles obedient', manner 'by word and deed', instrument 'through mighty signs and wonders, by the power of the Spirit of God' · narrator: Paul, apostolic voice
  · **edges:** M1036 —BEQUEATHS→ RECEPTION

**M1037** — The consequent claim is that Paul's actual preaching-arc, running from Jerusalem out through the surrounding regions as far as Illyricum, has covered the whole announced good-news of Christ.
  · agent: I (Paul) · operation: preach (fully, geographically-completed) · substrate: the gospel of Christ · outcome: the gospel of Christ fully preached across the arc, folded geographical-modifier: 'from Jerusalem, and round about unto Illyricum' · narrator: Paul, apostolic voice
  · **edges:** M1037 —BEQUEATHS→ RECEPTION

**M1038** — Paul emphatically restates the manner: his aim in the preaching-effort has been to work in places where Christ has not yet been named — the where-clause truncated in the source.
  · agent: I (Paul) · operation: strive (to preach) · substrate: the gospel · outcome: preaching-effort undertaken in the specified where-condition, truncated at 'not where Christ ...' — the location-restriction ('not where Christ [was already named]') is cut off in the source · narrator: Paul, apostolic voice
  · **edges:** M1038 —BEQUEATHS→ RECEPTION

**M1039** — The truncated location-restrictor from the prior segment is completed: the excluded territory is where the name of Christ has already been made known.
  · agent: Christ · operation: be-named (Christ, in specific places) · substrate: not-stated (the human namers are left unnamed in the passive) · outcome: Christ's name installed in specific places — the negated preaching-scope from the prior segment · narrator: Paul, apostolic voice

**M1040** — The reason for that avoidance is that Paul refuses to raise his own work on top of the groundwork already laid by someone else.
  · agent: I (Paul) · operation: build-upon (negated) · substrate: another man's foundation · outcome: no building placed on another's already-laid foundation · narrator: Paul, apostolic voice

**M1041** — Paul brings a written scripture into his text to warrant the pioneer-preaching principle.
  · agent: Paul (via the it-is-written formula) · operation: cite (scripture) · substrate: the scripture-moves nested as M4 and M5 · outcome: the scriptural saying installed as warrant for the pioneer-preaching principle · narrator: Paul, apostolic voice
  · **edges:** M1041 —CONTAINS→ M1042; M1041 —CONTAINS→ M1043

**M1042** — The first cited line has those who were never told about him future-tense-seeing.
  · agent: they to whom he was not spoken of · operation: see (future) · substrate: not-stated (what they will see is left implicit in the citation) · outcome: future seeing by those previously un-told · narrator: Isaiah (via LXX), embedded within Paul's citation
  · **edges:** ["M1041"] —CONTAINS→ M1042

**M1043** — The parallel cited line has those who have never heard future-tense-understanding.
  · agent: they that have not heard · operation: understand (future) · substrate: not-stated · outcome: future understanding by those previously un-hearing · narrator: Isaiah (via LXX), embedded within Paul's citation
  · **edges:** ["M1041"] —CONTAINS→ M1043

**M1044** — Paul reports that this same principle has been the very thing repeatedly blocking his travel to the addressees.
  · agent: I (Paul) · operation: be-hindered (from coming to you) · substrate: not-stated (the hindering source is left unnamed in the passive) · outcome: Paul repeatedly blocked from coming to the Rome addressees · narrator: Paul, apostolic voice

**M1045** — Paul reports his present state: the field in this region no longer offers him room to work.
  · agent: I (Paul) · operation: have (place, negated) · substrate: place (in these parts) · outcome: Paul without further working-place in the current region · narrator: Paul, apostolic voice

**M1046** — Paul reports the second piece of his present state: over many years he has been carrying a strong wanting to reach the addressees.
  · agent: I (Paul) · operation: have (a great desire, over many years) · substrate: a great desire (to come unto you) · outcome: Paul holding a long-standing desire to visit Rome · narrator: Paul, apostolic voice

**M1047** — Paul lays out his intended travel: at some future point he will set out on the journey to Spain.
  · agent: I (Paul) · operation: take-journey (into Spain, future) · substrate: Spain (as destination) · outcome: Paul's future Spain-journey named as the trigger-event for the Rome-visit · narrator: Paul, apostolic voice

**M1048** — Paired with that: Paul commits to actually arriving where the addressees are.
  · agent: I (Paul) · operation: come (to you) · substrate: you (the Rome addressees) · outcome: Paul's future arrival in Rome established as promised · narrator: Paul, apostolic voice

**M1049** — Paul reports his own hope-holding about that Rome-stop: two specific things he expects from the visit, contingent on his being first satisfied by their company.
  · agent: I (Paul) · operation: trust (hope) · substrate: the set of hoped-for actions nested as M12 and M13 · outcome: Paul's hope-holding installed as the affective frame of the visit-plan · narrator: Paul, apostolic voice
  · **edges:** M1049 —CONTAINS→ M1050; M1049 —CONTAINS→ M1051

**M1050** — The first hoped-for action is that Paul lays eyes on the addressees during his passing-through.
  · agent: I (Paul) · operation: see (you, in the journey) · substrate: you (the Rome addressees) · outcome: Paul's future seeing of the addressees, positioned within the ongoing journey · narrator: Paul (as content of his trusting-move)
  · **edges:** ["M1049"] —CONTAINS→ M1050

**M1051** — The second hoped-for action is that the addressees themselves send Paul forward on the next leg of his journey.
  · agent: I (Paul, as the one sent onward) · operation: be-brought-on-way (thitherward, by you) · substrate: you (as the sending-party) · outcome: Paul being sent onward from Rome toward the next destination by the addressee community · narrator: Paul (as content of his trusting-move)
  · **edges:** ["M1049"] —CONTAINS→ M1051

**M1052** — Paul reports the decision reached by the assemblies in Macedonia and Achaia — a decision they took with satisfaction — to raise a specific contribution.
  · agent: them of Macedonia and Achaia · operation: be-pleased (to make contribution) · substrate: the decision-content nested as M15 · outcome: Macedonia/Achaia's decision installed as an accomplished choice · narrator: Paul, apostolic voice
  · **edges:** M1052 —REPORTS→ M1053

**M1053** — The nested content of that decision is that they gather up a specific contribution for the poverty-stricken believers who live in Jerusalem.
  · agent: they (Macedonia and Achaia) · operation: make (a contribution) · substrate: a certain contribution, for the poor saints at Jerusalem · outcome: the contribution assembled for the Jerusalem poor · narrator: Paul (as content of the reported decision)
  · **edges:** ["M1052"] —REPORTS→ M1053

**M1054** — Paul underlines the point: the Gentile assemblies stand as ones who owe something to the Jerusalem group.
  · agent: they (Macedonia and Achaia) · operation: be-debtors (of them) · substrate: the Jerusalem saints (implicit as the creditor-party via 'their' back-reference) · outcome: debtor-status of the Gentile-assemblies established with respect to the Jerusalem community · narrator: Paul, apostolic voice

**M1055** — The warrant for that debt-status is stated as a conditional whose protasis is that the non-Jewish peoples have been brought into sharing the Jewish community's spiritually-derived goods — the noun that specifies those goods is cut off in the source.
  · agent: the Gentiles · operation: be-made-partakers-of (their spiritual [things]) · substrate: their spiritual [things — truncated in the source at 'spiritual'] · outcome: partaker-status established for the Gentiles in the Jewish community's spiritually-derived goods · narrator: Paul, apostolic voice

**M1056** — The consequent of the prior conditional is completed: the Gentile assemblies stand under an obligation to do a matching material ministering for the Jerusalem group.
  · agent: they (the Gentiles, inherited from the prior conditional's protasis) · operation: owe-to-minister (in carnal things) · substrate: them (the Jerusalem saints, as recipients of the material ministering) · outcome: material ministering owed as duty on the carnal axis · narrator: Paul, apostolic voice

**M1057** — Paul frames a future-perfect: the collection task will have been completed at his own hand.
  · agent: I (Paul) · operation: perform (this) · substrate: this (the collection-delivery task) · outcome: the collection-task completed as a future accomplished fact · narrator: Paul, apostolic voice

**M1058** — Paul also frames a second future-perfect: he will have formally set his seal on the yielded return of the collection, delivered to the Jerusalem group.
  · agent: I (Paul) · operation: seal (this fruit, to them) · substrate: this fruit (the yielded return of the collection) · outcome: the fruit sealed and delivered to the Jerusalem community as a future accomplished fact · narrator: Paul, apostolic voice

**M1059** — The consequent-clause is the promised travel-event: Paul will pass through where the addressees are, on his way to Spain.
  · agent: I (Paul) · operation: come (into Spain, via you) · substrate: Spain (as destination) · outcome: Paul's future arrival in Spain, folded via-modifier: 'by you' identifying Rome as the pass-through waypoint · narrator: Paul, apostolic voice

**M1060** — Paul reports his own settled confidence about the character of that Rome-visit.
  · agent: I (Paul) · operation: be-sure · substrate: the proposition nested as M6 · outcome: Paul's confidence installed as his own settled conviction about the visit · narrator: Paul, apostolic voice
  · **edges:** M1060 —REPORTS→ M1061

**M1061** — The nested content of that confidence is that when Paul does arrive at Rome, the arrival will carry the whole weight of the Christ-good-news's blessing.
  · agent: I (Paul) · operation: come (in the fulness of blessing) · substrate: you (Rome) · outcome: Paul's arrival at Rome carrying the fulness of the blessing of the gospel of Christ; the temporal 'when I come unto you' folded per IRR205 as circumstance · narrator: Paul (as the content of his sure-move)
  · **edges:** ["M1060"] —REPORTS→ M1061

**M1062** — Paul turns to a direct request to the addressees, addressing them warmly and appealing on two motivational grounds.
  · agent: I (Paul) · operation: beseech (you) · substrate: the requested action nested as M8 · outcome: Paul's request installed on Christ-authority and Spirit-love grounds · narrator: Paul, apostolic voice
  · **edges:** M1062 —REPORTS→ M1063

**M1063** — The requested action is that the addressees join Paul as fellow-strugglers in their prayer-work directed to God on his behalf.
  · agent: ye (the addressees) · operation: strive-together (with me, in prayers) · substrate: me (Paul, as the beneficiary of the joint prayer-struggle) · outcome: joint prayer-striving on Paul's behalf; folded domain-modifier: 'in your prayers to God for me' · narrator: Paul (as content of the beseech-move)
  · **edges:** ["M1062"] —REPORTS→ M1063

**M1064** — The first aim of that prayer-struggle is that Paul be rescued from the non-trusting people in Judaea.
  · agent: I (Paul) · operation: be-delivered (from them that do not believe in Judaea) · substrate: not-stated (the deliverer is left unnamed in the passive) · outcome: Paul's rescue from the Judean unbelievers; the substantival participle 'them that do not believe in Judaea' folded per IRR205 as source-modifier · narrator: Paul, apostolic voice

**M1065** — The second aim is that the collection-service Paul is carrying to Jerusalem meet with the sign-off of the Jerusalem community.
  · agent: my service (which I have for Jerusalem) · operation: be-accepted (of the saints) · substrate: the saints (as the accepting party) · outcome: acceptance-status established for Paul's collection-service by the Jerusalem saints · narrator: Paul, apostolic voice

**M1066** — The third aim is that Paul actually reach the addressees, in a mood of joy, with God's will as the enabling ground.
  · agent: I (Paul) · operation: come (with joy, by the will of God) · substrate: you (the Rome addressees) · outcome: Paul's future arrival at Rome in the mode of joy; folded agency-modifier 'by the will of God' as the enabling ground · narrator: Paul, apostolic voice

**M1067** — Paired with that: Paul may find restoration in the company of the addressees themselves.
  · agent: I (Paul) · operation: be-refreshed (with you) · substrate: you (the Rome addressees, as the co-refreshing companions) · outcome: Paul restored/refreshed in the company of the addressees · narrator: Paul, apostolic voice

**M1068** — Paul introduces and vouches for a specific person by name — his sister Phoebe, who holds a servant-role in a particular assembly, the church-name truncated in the source.
  · agent: I (Paul) · operation: commend (Phebe, to you) · substrate: Phebe our sister (folded relative-modifier: 'which is a servant of the [church at ... — truncated]') · outcome: Phebe installed to the addressees as a commended person; the specifying church-name is cut off in the source · narrator: Paul, apostolic voice

**M1069** — The truncated church-name from the prior segment is completed: the assembly Phoebe serves is the one located at Cenchrea.
  · agent: the church (that Phoebe serves) · operation: be-at (Cenchrea) · substrate: not-stated (Cenchrea as the location-frame) · outcome: the church located and identified as the Cenchrea assembly · narrator: Paul, apostolic voice

**M1070** — The first aim of the commendation is that the addressees welcome Phoebe in a Lord-oriented manner, matching what fits set-apart persons.
  · agent: ye (the addressees) · operation: receive (her, in the Lord) · substrate: her (Phoebe) · outcome: Phoebe welcomed in the Lord; comparative-modifier 'as becometh saints' folded per IRR205 as manner-restrictor · narrator: Paul, apostolic voice

**M1071** — The second aim of the commendation is that the addressees actually stand by Phoebe in whatever matter she may require them for.
  · agent: ye (the addressees) · operation: assist (her) · substrate: her (Phoebe) · outcome: Phoebe practically assisted in whatever business she has need of the addressees; relative 'in whatsoever business she hath need of you' folded per IRR205 as scope-modifier · narrator: Paul, apostolic voice

**M1072** — The warrant Paul offers is that Phoebe has, in fact, been a supporting-figure for many people — including Paul himself.
  · agent: she (Phoebe) · operation: be-succourer (of many, and of myself also) · substrate: many (and myself, Paul, also) — paired recipient-substrate · outcome: Phoebe's succouring-record established as ground for the requested reception and assistance · narrator: Paul, apostolic voice

**M1073** — Turning to another matter, Paul reports about certain persons that they put their own necks on the line for the sake of his own life — the antecedent name is missing from this text segment.
  · agent: who (referent not-stated in this segment; the antecedent is absent from the text) · operation: lay-down (their own necks, for my life) · substrate: their own necks · outcome: risk of life undertaken on Paul's behalf · narrator: Paul, apostolic voice

**M1074** — Paul reports that thanks-giving is directed to those same persons — and not only by himself but by the whole set of non-Jewish assemblies.
  · agent: not only I (Paul), but also all the churches of the Gentiles · operation: give-thanks (unto whom) · substrate: unto whom (the same referent as M5) · outcome: thanks-giving addressed to them by Paul and by all Gentile assemblies · narrator: Paul, apostolic voice

**M1075** — Paul commands a greeting also to the assembly gathering in the house of those same persons.
  · agent: ye (the addressees, implicit imperative addressee) · operation: greet (the church in their house) · substrate: the church that is in their house · outcome: greeting extended to the house-church of the M5/M6 referents · narrator: Paul, apostolic voice

**M1076** — Paul commands a personal greeting to Epaenetus, a specially-loved figure, characterized as the first-yielded harvest of Achaia into Christ.
  · agent: ye (the addressees, implicit) · operation: salute (Epaenetus) · substrate: Epaenetus (my well-beloved, firstfruits of Achaia unto Christ) · outcome: greeting extended to Epaenetus · narrator: Paul, apostolic voice

**M1077** — Paul commands a greeting to Andronicus and Junia, characterized as fellow-Jews of Paul, fellow-prisoners with him, distinguished within the apostle-set, and Christ-adherents earlier than Paul himself.
  · agent: ye (the addressees, implicit) · operation: salute (Andronicus and Junia) · substrate: Andronicus and Junia (my kinsmen, my fellow-prisoners, of note among the apostles, in Christ before me) · outcome: greeting extended to Andronicus and Junia · narrator: Paul, apostolic voice

**M1078** — Paul commands a greeting to Apelles, characterized as one who has stood the test in Christ.
  · agent: ye (the addressees, implicit) · operation: salute (Apelles) · substrate: Apelles (approved in Christ) · outcome: greeting extended to Apelles · narrator: Paul, apostolic voice

**M1079** — Paul commands a greeting to the members who belong to the household of Aristobulus.
  · agent: ye (the addressees, implicit) · operation: salute (those of Aristobulus' household) · substrate: them which are of Aristobulus' household · outcome: greeting extended to the Aristobulus-household group · narrator: Paul, apostolic voice

**M1080** — Paul commands a greeting to Herodion, characterized as a fellow-Jew.
  · agent: ye (the addressees, implicit) · operation: salute (Herodion) · substrate: Herodion (my kinsman) · outcome: greeting extended to Herodion · narrator: Paul, apostolic voice

**M1081** — Paul commands a greeting to the members who belong to a further-named household — with the household-name truncated in the source.
  · agent: ye (the addressees, implicit) · operation: greet (those of the [household — truncated]) · substrate: them that be of the [household-name truncated at 'the'] · outcome: greeting extended to a further household-group; the specifying household-name is cut off in the source · narrator: Paul, apostolic voice

**M1082** — The truncated household-name from the prior segment is completed as the household of Narcissus, and the greeted subset is restricted to those within it who stand in the Lord.
  · agent: they (those of Narcissus's household) · operation: be-in-the-Lord (with household-of-Narcissus scope) · substrate: not-stated · outcome: in-the-Lord status established as the qualifier restricting the greeted subset of the Narcissus household · narrator: Paul, apostolic voice

**M1083** — Paul commands a greeting to two named women, characterized as ones whose labour is done in the Lord.
  · agent: ye (the addressees, implicit) · operation: salute (Tryphena and Tryphosa) · substrate: Tryphena and Tryphosa (who labour in the Lord) · outcome: greeting extended to Tryphena and Tryphosa · narrator: Paul, apostolic voice

**M1084** — Paul commands a greeting to Persis, called beloved, characterized as one whose past-tense labour in the Lord was extensive.
  · agent: ye (the addressees, implicit) · operation: salute (Persis) · substrate: the beloved Persis (which laboured much in the Lord) · outcome: greeting extended to Persis · narrator: Paul, apostolic voice

**M1085** — Paul commands a greeting to a further set of five named men and the sibling-set that gathers with them.
  · agent: ye (the addressees, implicit) · operation: salute (Asyncritus, Phlegon, Hermas, Patrobas, Hermes, and their brethren) · substrate: Asyncritus, Phlegon, Hermas, Patrobas, Hermes, and the brethren which are with them · outcome: greeting extended to the five named men and their associated brethren-group · narrator: Paul, apostolic voice

**M1086** — Paul commands a greeting to a further set of named persons — including a sister of one and Olympas — and to the wider set-apart persons who gather with them.
  · agent: ye (the addressees, implicit) · operation: salute (Philologus, Julia, Nereus and his sister, Olympas, and all the saints with them) · substrate: Philologus, Julia, Nereus and his sister, Olympas, and all the saints which are with them · outcome: greeting extended to the named cluster and the wider saint-group with them · narrator: Paul, apostolic voice

**M1087** — Paul commands the addressees to exchange the greeting reciprocally, in the manner of a set-apart kiss.
  · agent: ye (the addressees, in reciprocal role) · operation: salute (one another, with an holy kiss) · substrate: one another (reciprocal target) · outcome: mutual greeting exchanged in the holy-kiss form · narrator: Paul, apostolic voice

**M1088** — Paul reports that greetings run the other direction as well: the Christ-assemblies themselves send their greeting to the addressees.
  · agent: the churches of Christ · operation: salute (you) · substrate: you (the addressees) · outcome: greeting from the wider Christ-assembly network delivered to the addressees · narrator: Paul, apostolic voice

**M1089** — Paul turns to a direct request to the addressees, addressing them warmly as siblings.
  · agent: I (Paul) · operation: beseech (you) · substrate: the requested actions nested as M9 and M10 · outcome: Paul's request installed on the addressees for a two-part response to divisive persons · narrator: Paul, apostolic voice
  · **edges:** M1089 —CONTAINS→ M1090; M1089 —CONTAINS→ M1091

**M1090** — The first requested action is that the addressees keep their eye out for those particular persons whose activity produces splits and trip-ups in the community, running against the teaching the addressees have been given.
  · agent: ye (the addressees) · operation: mark (them who cause divisions and offences) · substrate: them which cause divisions and offences contrary to the doctrine which ye have learned · outcome: the divisive/offence-causing persons watched-for and identified · narrator: Paul (as content of the beseech-move)
  · **edges:** ["M1089"] —CONTAINS→ M1090

**M1091** — The second requested action is that the addressees turn aside from those same persons.
  · agent: ye (the addressees) · operation: avoid (them) · substrate: them (the divisive persons of M9) · outcome: the divisive persons distanced from · narrator: Paul (as content of the beseech-move)
  · **edges:** ["M1089"] —CONTAINS→ M1091

**M1092** — The warrant for the warning is that persons of this kind, in place of serving the community's Lord Jesus Christ, are in fact serving their own appetitive lower part.
  · agent: they that are such (the divisive persons) · operation: serve (contrastive: not Christ, but own belly) · substrate: not our Lord Jesus Christ, but their own belly (contrastive-paired substrate) · outcome: mis-directed service established — service withheld from Christ and redirected to the belly · narrator: Paul, apostolic voice

**M1093** — A parallel warrant: through smooth talk and flattering rhetoric, they mislead the inner disposition of unsuspecting people.
  · agent: they (the divisive persons) · operation: deceive (the hearts of the simple) · substrate: the hearts of the simple · outcome: the inner-disposition of the unsuspecting misled; folded instrument-modifier 'by good words and fair speeches' · narrator: Paul, apostolic voice

**M1094** — Paul then reports that the actual compliant response of the addressees has become widely-known-of, reaching everyone.
  · agent: your obedience · operation: come-abroad (unto all men) · substrate: unto all men (as the reach-target) · outcome: the addressees' obedience made known to everyone · narrator: Paul, apostolic voice

**M1095** — Paul reports his own affective response — gladness — with the content of the gladness cut off in the source.
  · agent: I (Paul) · operation: be-glad · substrate: not-stated (the object/reason for the gladness is truncated in the source at 'I am glad') · outcome: Paul's gladness state installed as his response · narrator: Paul, apostolic voice

**M1096** — The truncated scope of Paul's gladness from the prior segment is completed: the gladness is inferentially drawn and directed on the addressees' account.
  · agent: I (Paul) · operation: be-glad (scoped on-behalf-of you) · substrate: you (the addressees, as the beneficiary of the gladness) · outcome: Paul's gladness anchored inferentially (therefore) on the addressees' account · narrator: Paul, apostolic voice

**M1097** — Paul now qualifies with a wish-directive: he wants the addressees to hold a specific double-posture toward the good and the evil.
  · agent: I (Paul) · operation: would-have (want) you · substrate: the double-posture nested as M3 and M4 · outcome: Paul's wish installed as the corrective supplement to his gladness · narrator: Paul, apostolic voice
  · **edges:** M1097 —CONTAINS→ M1098; M1097 —CONTAINS→ M1099

**M1098** — The first side of the wished-for posture is that the addressees be shrewd with respect to what is good.
  · agent: you (the addressees) · operation: be-wise (unto that which is good) · substrate: that which is good · outcome: wisdom-orientation held toward the good · narrator: Paul (as content of the would-have-move)
  · **edges:** ["M1097"] —CONTAINS→ M1098

**M1099** — The paired side of the wished-for posture is that the addressees remain unmixed and inexperienced with respect to what is evil.
  · agent: you (the addressees) · operation: be-simple (concerning evil) · substrate: evil · outcome: simplicity/unmixedness held toward evil · narrator: Paul (as content of the would-have-move)
  · **edges:** ["M1097"] —CONTAINS→ M1099

**M1100** — Paul then announces a future-tense promise: the peace-God will crush the adversary under the community's own feet, and soon.
  · agent: the God of peace · operation: bruise (Satan, under your feet) · substrate: Satan · outcome: Satan crushed under the addressees' feet; folded temporal 'shortly' · narrator: Paul, apostolic voice

**M1101** — Paul closes with a benediction-wish: that the favor issuing from the community's Lord Jesus Christ remain with them, confirmed with the amen-affirmation.
  · agent: the grace of our Lord Jesus Christ · operation: be-with (wish/optative) · substrate: you (the addressees) · outcome: grace-with-you state wished; affirmation 'Amen' folded as confirmation-modifier · narrator: Paul, apostolic voice

**M1102** — Paul relays greetings from his associates on the sender-side: Timothy, described as workfellow, and three named Jewish kinsmen — Lucius, Jason, Sosipater.
  · agent: Timotheus (my workfellow), Lucius, Jason, and Sosipater (my kinsmen) — paired-cluster agent · operation: salute (you) · substrate: you (the addressees) · outcome: greeting from Paul's associate-cluster delivered · narrator: Paul, apostolic voice

**M1103** — Paul relays a separate greeting from Gaius, characterized as the host of Paul himself and of the whole assembly.
  · agent: Gaius (mine host, and of the whole church) · operation: salute (you) · substrate: you (the addressees) · outcome: greeting from Gaius delivered · narrator: Paul, apostolic voice

**M1104** — Paul relays a further greeting from Erastus, described as the city's civic-treasurer, and adds Quartus, a fellow-member.
  · agent: Erastus (the chamberlain of the city) and Quartus (a brother) — paired agent · operation: salute (you) · substrate: you (the addressees) · outcome: greeting from Erastus and Quartus delivered · narrator: Paul, apostolic voice

**M1105** — Paul begins his closing doxology by addressing the recipient of the coming glory-ascription: the one whose capacity is to make the addressees stand firm — a capacity matched to Paul's gospel and to the announcement of Jesus Christ, itself matched to the disclosure of the long-held-back mystery.
  · agent: him (the one addressed in the doxology, understood as God) · operation: be-of-power-to-establish (you) · substrate: you (the addressees, as the ones to be established) · outcome: establishing-power attributed to God as the doxology's addressee; folded norm-modifiers: 'according to my gospel', 'and the preaching of Jesus Christ', 'according to the revelation of the mystery' · narrator: Paul, apostolic voice

**M1106** — The past state of the mystery is that it had been held back in silence for the whole time reaching from the world's beginning up to now.
  · agent: the mystery · operation: be-kept-secret (since the world began) · substrate: not-stated (God as the keeper-in-silence is left unnamed in the passive) · outcome: mystery held in silence from world-beginning up to the pre-now period · narrator: Paul, apostolic voice
  · **edges:** M1106 —BEQUEATHS→ RECEPTION

**M1107** — The present state of the same mystery is that it has now been brought out into the open — through the prophets' writings, on the authorization of the age-lasting God, the fuller mission-clause truncated in the source.
  · agent: the mystery · operation: be-made-manifest (now) · substrate: not-stated (God as the revealer is left unnamed in the passive) · outcome: mystery brought into the open in the present period; folded instrument-modifier 'by the scriptures of the prophets'; folded authorization-modifier 'according to the commandment of the everlasting God'; further clause truncated in the source at 'the everlasting God,' · narrator: Paul, apostolic voice

**M1108** — The truncated doxology-clause from the prior segment is completed: the mystery has been brought into the awareness of every people-group, with the aim that trust-shaped obedience follow.
  · agent: the mystery (inherited from the prior segment's subject) · operation: be-made-known (to all nations) · substrate: all nations (as the recipients of the making-known) · outcome: mystery installed as known-to-all-nations; folded purpose-modifier 'for the obedience of faith' · narrator: Paul, apostolic voice

**M1109** — The doxology-ascription itself is now spoken: glory belongs, ongoingly and without endpoint, to the sole-wise God — routed through Jesus Christ — sealed with the amen-affirmation.
  · agent: glory (as the ascribed content) · operation: be-glory (wish/ascription) · substrate: God only wise (as the recipient of the ascription) · outcome: glory ascribed to God for ever; folded mediator-modifier 'through Jesus Christ'; folded duration-modifier 'for ever'; folded affirmation 'Amen'; folded epithet 'only wise' as agent-attribute of the recipient · narrator: Paul, apostolic voice
