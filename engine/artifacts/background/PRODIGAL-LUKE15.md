# PRODIGAL-LUKE15 — background sheet

> Full coded transcript for **PRODIGAL-LUKE15** — read-only snapshot from the DB.

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
| PRODIGAL-LUKE15 | 70 | 18 | 28 | 0 |


## PRODIGAL-LUKE15

### Sitz — situational conditions (source_grounding)

- **summary:** Luke 15:11-32 reaches us in a Greek Gospel composed ~85 CE, so its material substrate is doubled: the parable's Galilean-Jewish agrarian world (partible inheritance, famine, unclean pig-herding for a Gentile employer) and Luke's post-70 Mediterranean audience. [POL-PAX-ROMANA] underwrites the plausibility of the younger son traveling 'to a distant region' and hiring out across ethnic lines; [FIG-JESUS-GALILEE-30] anchors the saying's attributed origin in Galilean parabolic teaching under Herodian client-rule ([POL-HERODIAN-CLIENT-RULE]); and [POL-FIRST-JEWISH-ROMAN-WAR] decisively conditions the hearing — Luke and his audience read the elder-brother/younger-son reconciliation after the Temple's destruction, when the [DEM-JEWGENTILE-ROMAN-CHURCH-54] question of who counts as 'always with me' vs. 'dead and alive again' is live. MODEL-KNOWLEDGE: Mediterranean partible-inheritance custom and patria-potestas honor-shame kinship (the son's 'give me my share' is a socially scandalous premortem demand) and the recurrent Levantine agrarian famine cycle are the immediate material substrate for the plot.
- **categories:** ["political_institutional", "economic_material", "climate_ecology", "demographic_social", "interreligious_contact", "kinship_residence"]
- **layers:** ["cultural_intellectual", "polemical", "ecological_material_geographical"]

### Paradigm — the scripts the text thinks with (+ its stance toward each)

| paradigm | stance | salience |  | relation | evidence |
|---|---|---|---|---|---|
| kinship-restoration (patriarchal household reincorporation) | endorsed | 0.98 | DOMINANT | self | Father/son roles throughout; premature inheritance division ([12] 'the portion of goods that falleth to me'); the son's self-disqualification from sonship ([19] 'no more worthy to be called thy son'); the father's restoration of filial status via robe, ring, and shoes ([22]) — insignia of household standing, not hired-servant status; the telos declared twice as reincorporation into the living household ([24], [32] 'was dead, and is alive again; was lost, and is found'). |
| kinship-restoration (patriarchal household honor) | endorsed | 0.98 | DOMINANT | self | 'father'/'son'/'brother' saturate the text; the telos is reincorporation into the household ('this son of mine was dead and is alive again'); restoration is enacted through kinship-status regalia (best robe, ring, sandals) and a household feast (fatted calf); the elder is told 'you are always with me, and all that is mine is yours' — sonship, not merit, defines standing. |
| honor-shame (public disgrace and public rehabilitation) | subverted | 0.88 |  | reinforces | The son's shame is maximal in a Second-Temple Jewish frame: demanding inheritance while father lives, squandering it among Gentiles, attaching himself to a Gentile ('joined himself to a citizen of that country' [15]), and feeding swine ([15]-[16]) — ritually unclean labor. Honor-script expects the shamed son to be met with rebuke, penance, or refusal at the village gate; instead the father runs ([20] — itself undignified for a patriarch), embraces, and publicly rehabilitates him with the fatted calf feast. The script is invoked precisely to be overturned by the father's action. |
| honor-shame / patronal reception | subverted | 0.85 |  | reinforces | The son's demand for inheritance while the father lives, dissipation among Gentiles, and pig-feeding are maximal shame markers; the father's public running to meet him, embrace, and kiss inverts patriarchal decorum (a village patriarch does not run); robe/ring/sandals are honor-restoration signs bestowed without the expected shaming ritual or probation. |
| repentance-and-return (teshuvah / prophetic 'return to the father') | endorsed | 0.82 |  | reinforces | The interior turn ([17] 'when he came to himself'), the rehearsed confession using the classic formula ([18] 'sinned against heaven, and before thee'), and the physical 'arise and go' ([18], [20]) map onto Second-Temple teshuvah — the sinner returns, confesses, seeks reduced status. The father's response, however, short-circuits the transactional side of the script (the 'make me as one of thy hired servants' request is never granted); repentance is accepted but is not the mechanism of restoration. |
| repentance-and-return (prophetic teshuvah / turning to YHWH) | invoked | 0.8 |  | reinforces | 'when he came to his senses'; the rehearsed confession 'I have sinned against heaven and before you'; 'I will get up and go to my father' echoes prophetic call-to-return language; 'heaven' as circumlocution for God frames the domestic return as also a return to God. |
| two-brothers / elder-younger reversal (Genesis typology: Cain-Abel, Ishmael-Isaac, Esau-Jacob, Joseph) | invoked | 0.75 |  | reinforces | 'A certain man had two sons' ([11]) is a signal opening in the Hebrew Bible repertoire, and the pattern of the younger displacing or being favored over the elder is a stock script. The elder's field-labor and resentment ([25], [28]-[30]) versus the younger's celebrated return activates the typology; the parable ends unresolved ([31]-[32] with the father entreating the elder outside), leaving the reversal partial and the elder's response open. |
| death-and-resurrection (lost-and-found) | endorsed | 0.75 |  | reinforces | Repeated refrain 'was dead and is alive again; was lost and is found' — a two-beat template that supplies the celebration's warrant and closes both halves of the parable, framing return as resurrection. |
| death-and-resurrection (lost-and-found / return-to-life) | endorsed | 0.7 |  | reinforces | The telos is declared not as reconciliation or forgiveness but as ontological reversal, twice: [24] 'this my son was dead, and is alive again; he was lost, and is found,' and [32] repeated to the elder. The banquet ([23] fatted calf, music and dancing [25]) functions as a resurrection-feast, not merely a welcome. This paradigm names WHY the kinship restoration warrants a feast rather than probation. |
| inheritance-and-stewardship (patrimony/estate law) | invoked | 0.7 |  | competes | The mechanics that set the plot in motion are legal-economic: division of the estate ([12] 'he divided unto them his living'), the younger son's liquidation and dissipation ([13]), and the elder's grievance framed in ledger terms ([29]-[30] years of service, never a kid, contrasted with 'devoured thy living'). The father's closing line to the elder ([31] 'all that I have is thine') settles the estate question, but the paradigm is displaced rather than resolved on its own terms — legal entitlement is not what the feast celebrates. |
| two-sons / younger-favored (Israelite patriarchal narrative) | invoked | 0.7 |  | reinforces | 'a man who had two sons' directly cues the Genesis pattern (Cain/Abel, Ishmael/Isaac, Esau/Jacob, Joseph and brothers, Ephraim/Manasseh) in which the younger is unexpectedly received or elevated and the elder resents; the plea-scene with the elder ('his father came out and began to plead with him') fits this template. |
| festal banquet / covenant meal | endorsed | 0.7 |  | reinforces | Fatted calf slaughtered, music and dancing, a household feast celebrating reincorporation; the elder's refusal to 'go in' marks the meal as the site where belonging is publicly ratified — a recognizable script of covenantal/eschatological banquet in Second Temple and Jesus-tradition idiom. |
| merit / wage-labor economy (hired-hand reckoning) | subverted | 0.65 |  | competes | The younger son plans to downgrade to 'hired hand' status — a merit/wage frame — but the father short-circuits the transaction and reinstates him as son; the elder explicitly frames his relation as 'working like a slave' expecting proportional reward. The father's reply refuses the ledger. |
| Gentile-inclusion / insider–outsider reversal (Lukan) | endorsed | 0.6 |  | reinforces | The younger goes to 'a distant region' and feeds pigs (unclean, Gentile-coded); his welcome without probation, paired with the elder's exclusion-by-choice, maps onto Luke's larger script of outsiders received and insiders scandalized (cf. the tax-collector/sinner context of Luke 15). The parable is left open — the elder's response is not resolved — pressing the audience into the elder's seat. |
| inheritance / patrimony division (legal-household) | invoked | 0.6 |  | competes | 'give me the share of the wealth that will belong to me'; 'he divided his assets between them'; the elder's grievance is framed in property terms ('you have never given me even a young goat'; 'devoured your assets'); the father's reply reasserts undivided patrimony: 'all that is mine is yours.' |
| purity/clean-unclean boundary | subverted | 0.55 |  | subverts | The son's degradation is coded in purity terms — Gentile land, swine ([15]-[16]), longing for their food — the maximally unclean state for a Jewish hearer. The father's embrace ([20] 'fell on his neck, and kissed him') before any washing, confession completion, or ritual reintegration ignores the purity script; contact precedes purification. The paradigm is present as the measure of scandal, then bypassed. |
| patron-client / hired-servant contract | denied | 0.45 |  | competes | The son's plan ([17]-[19]) is to renegotiate the relationship contractually — downgrade from son to 'hired servant' (misthios), a wage-labor role with defined terms and no kinship claim. The father never lets the request be spoken as a request; the robe/ring/shoes ([22]) are refused-substitution — sonship is restored, not a lesser contract offered. The elder son's speech ([29] 'Lo, these many years do I serve thee') reveals he has been living the household AS IF it were a patron-client contract, and the father's reply ([31]) denies that framing too. |
| banquet / messianic feast | invoked | 0.4 |  | reinforces | Fatted calf ([23]), music and dancing ([25]), collective merriment, and the imperative 'let us eat, and be merry' ([23]) evoke the eschatological/celebratory banquet common in Second-Temple Jewish imagination (Isaiah 25, wedding-feast imagery). Within Luke's larger frame this resonates with kingdom-banquet motifs, though inside the parable itself it functions primarily as the sign that restoration is complete. |

### Frame — the 8-axis morphospace coordinate

| axis | value | rank | conf | evidence |
|---|---|---|---|---|
| epistemic-warrant | revelation | 1 | 0.85 | 'Then Jesus said...' — the parable's authority rests on the disclosive speech of Jesus, functioning as revelatory teaching within the Lukan Gospel frame. |
| epistemic-warrant | testimony | 1 | 0.9 | 'And he said...' — a parable-narrative delivered as reported speech of Jesus, grounding its claim in authoritative story-telling |
| epistemic-warrant | testimony | 2 | 0.7 | The text is transmitted as reported speech within a Gospel narrative ('Then Jesus said'), embedding the teaching in witnessed tradition. |
| epistemic-warrant | revelation | 2 | 0.6 | the story functions as disclosure of the father's disposition ('had compassion, and ran, and fell on his neck') — a revealing of divine-paternal character through narrative |
| evaluative-stance | reverent | 1 | 0.85 | The text delivers Jesus' words as authoritative teaching, treating the father-figure (transparently God) with unqualified positive regard ('filled with compassion; he ran and put his arms around him and kissed him'). |
| evaluative-stance | tender | 1 | 0.9 | 'when he was yet a great way off, his father saw him, and had compassion, and ran, and fell on his neck, and kissed him' — the narrator's stance toward the returning son and the father's response is unmistakably tender |
| evaluative-stance | charitable | 2 | 0.65 | Even the resentful elder brother is addressed tenderly ('Son, you are always with me') rather than condemned — the narrator's stance extends charity to both sons. |
| evaluative-stance | reverent | 2 | 0.55 | the father-figure is treated with implicit reverence as the moral center whose judgment ('it was meet that we should make merry') closes the parable |
| ground-world-relation | creation | 1 | 0.7 | The implied father-God stands as originary source over an ordered household/world ('all that is mine is yours'), a creator-owner relation rather than emanation or identity. |
| ground-world-relation | participation | 1 | 0.7 | 'Son, thou art ever with me, and all that I have is thine' — the son's proper mode of being is shared-life-with the father; belonging is participatory |
| ground-world-relation | participation | 2 | 0.65 | 'Son, you are always with me, and all that is mine is yours' — the elder's belonging figures the world-relation as shared participation in the father's estate. |
| ground-world-relation | manifestation | 2 | 0.55 | the father's character is DISCLOSED / made visible through his running-and-embracing act — the ground shows itself in the encounter |
| hermeneutic-posture | reparative-integrative | 1 | 0.85 | The parable enacts repair: the broken son is reintegrated ('this brother of yours was dead and has come to life; he was lost and has been found'), and the father pleads to include the elder as well. |
| hermeneutic-posture | performative | 1 | 0.85 | the parable ENACTS what it teaches — the reader is drawn into the scene (elder-brother's grievance, father's reply) rather than told a doctrine; it works by doing |
| hermeneutic-posture | literal | 2 | 0.4 | On its narrative surface the story is told as a straightforward household episode, with the allegorical dimension left implicit for the hearer to unfold. |
| hermeneutic-posture | reparative-integrative | 2 | 0.7 | the whole arc is repair — 'was lost, and is found' — and the father's closing speech reintegrates the elder brother into the joy rather than expelling him |
| inferential-operation | analogical-mapping | 1 | 0.9 | The parable form itself maps a household drama onto the divine-human relation; the earthly father's welcome analogically discloses the character of God/heaven ('I have sinned against heaven and before you'). |
| inferential-operation | analogical-mapping | 1 | 0.88 | the household drama is offered as an analog for a larger (unstated) reality; the parable-form maps a domestic scene onto a theological claim about welcome |
| inferential-operation | abduction | 2 | 0.6 | The father's response ('we HAD to celebrate') invites the hearer to infer the best explanation for such extravagant welcome — the logic of restoration over accounting. |
| inferential-operation | exegesis | 2 | 0.4 | the elder-brother exchange ('Son, thou art ever with me...') reads as an internal exposition/gloss on what the father's action MEANS |
| ontological-commitment | personal-agentive | 1 | 0.9 | The father is a personal agent whose compassion, running, embracing, and speech carry the parable's ontology: reality is constituted by personal relations and agentive love ('his father saw him and was filled with compassion; he ran and put his arms around him'). |
| ontological-commitment | personal-agentive | 1 | 0.92 | the ultimate figure is a father who sees, runs, embraces, speaks, commands the servants — an agentive person, not an impersonal order |
| ontological-commitment | relational | 2 | 0.75 | Being is figured through kinship-bonds — sonship, brotherhood, household — such that to be 'lost' or 'found,' 'dead' or 'alive,' is a relational status ('this son of mine was dead and is alive again'). |
| ontological-commitment | relational | 2 | 0.75 | reality is constituted by kinship-bonds — son/father/brother/servant — and the drama turns on their rupture and repair |
| telos | communion | 1 | 0.88 | The end is restored table-fellowship: robe, ring, sandals, fatted calf, celebration — reunion of persons within the household ('let us eat and celebrate ... he was lost and is found'). |
| telos | communion | 1 | 0.88 | 'this my son was dead, and is alive again; he was lost, and is found' — the fulfillment is restored table-fellowship, the celebratory meal, reunion |
| telos | salvation | 2 | 0.75 | 'This son of mine was dead and is alive again' — the framing of rescue-from-death names a salvific arc alongside the relational communion. |
| telos | belonging | 2 | 0.82 | the son's crisis is loss of sonship ('am no more worthy to be called thy son') and the resolution is restoration of place (robe, ring, shoes — marks of household standing) |

### Coded moves — each with the context it picked up

**M1** — The evangelist opens by reporting that Jesus commences a further piece of speech.
  · agent: he (Jesus, the teller within the gospel) · operation: said · substrate: the parable that follows · outcome: the parable is delivered to Jesus's hearers (and to the gospel's audience) · narrator: Luke, evangelist; third-person report; authority = gospel tradition
  · **edges:** M1 —CONTAINS→ M10; M1 —CONTAINS→ M11; M1 —CONTAINS→ M12; M1 —CONTAINS→ M13; M1 —CONTAINS→ M14; M1 —CONTAINS→ M3; M1 —CONTAINS→ M5; M1 —CONTAINS→ M6; M1 —CONTAINS→ M7; M1 —CONTAINS→ M8; M1 —CONTAINS→ M9; M1 —REPORTS→ M2

**M2** — The parable's opening premise: a certain man stands in a paternal relation to a pair of sons.
  · agent: a certain man · operation: had (two sons) · substrate: two sons · outcome: paternal relation obtains (a father with two sons) · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** ["M1"] —REPORTS→ M2

**M3** — The junior son addresses his father in speech.
  · agent: the younger of them (the junior son) · operation: said (to his father) · substrate: the request uttered to the father · outcome: the request is placed before the father · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** M3 —REPORTS→ M4; ["M1"] —CONTAINS→ M3

**M4** — The junior son directs the father to release to him now the share of the estate that would eventually be his.
  · agent: father (the addressee whom the imperative names as the one to act) · operation: give (imperative — hand over) · substrate: the portion of goods that falleth to me (the son's due share) · outcome: the son receives his portion (an ante-mortem release of inheritance) · narrator: Jesus, ventriloquising the son's speech within the parable
  · **edges:** ["M3"] —REPORTS→ M4

**M5** — The father parcels out his estate between the two sons.
  · agent: he (the father) · operation: divided (unto them his living) · substrate: his living (his whole estate / means of life) · outcome: the living is divided between the two sons · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** ["M1"] —CONTAINS→ M5

**M6** — After a short interval the junior son consolidates the whole of what is now his.
  · agent: the younger son · operation: gathered all together · substrate: all (the divided portion, now his) · outcome: the portion is consolidated (implicitly convertible to portable wealth) · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** ["M1"] —CONTAINS→ M6

**M7** — He removes himself far from home into a distant land.
  · agent: the younger son · operation: took his journey (into a far country) · substrate: himself (his person) · outcome: he is in a far country · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** ["M1"] —CONTAINS→ M7

**M8** — In the distant land he dissipates his wealth in extravagant living, exhausting it entirely.
  · agent: the younger son · operation: wasted his substance (with riotous living); spent all · substrate: his substance (the wealth carried from home) · outcome: the substance is depleted; nothing remains · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** ["M1"] —CONTAINS→ M8

**M9** — A severe famine sets in across that land.
  · agent: not-stated (no doer named; the famine arises impersonally) · operation: there arose (a mighty famine) · substrate: that land (the far country) · outcome: a mighty famine is present in the land · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** ["M1"] —CONTAINS→ M9

**M10** — He passes into a condition of destitution.
  · agent: he (the younger son, as experiencer rather than doer) · operation: began to be in want · substrate: himself (his own condition) · outcome: he is in a state of want / lack · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** ["M1"] —CONTAINS→ M10

**M11** — He attaches himself as a hired hand to a local resident of that country.
  · agent: he (the younger son) · operation: went and joined himself (to a citizen of that country) · substrate: himself · outcome: he is attached to a citizen of that country (a dependent / client relation) · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** ["M1"] —CONTAINS→ M11

**M12** — That local dispatches him out to his fields to feed pigs.
  · agent: he (the citizen of that country) · operation: sent (him into his fields) · substrate: him (the younger son, now the one being sent) · outcome: the son is placed in the citizen's fields (purpose: to feed swine) · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** ["M1"] —CONTAINS→ M12

**M13** — He longs to appease his hunger even with the pods that the pigs are eating.
  · agent: he (the younger son, as experiencer of longing) · operation: would fain have filled (his belly with the husks) · substrate: his belly (his hunger) · outcome: wished-for satiation with the husks — the wish is left unfulfilled by the surrounding narration · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** ["M1"] —CONTAINS→ M13

**M14** — No one in that land extends anything to him.
  · agent: no man (universal negation of any giver) · operation: gave (unto him) — negated: no man gave · substrate: not-stated (implicitly: food, aid, or anything at all) · outcome: he receives nothing; his want continues · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** ["M1"] —CONTAINS→ M14

**M15** — The son returns to lucidity — his right mind is restored to him.
  · agent: he (the younger son, as experiencer of his own return-to-self) · operation: came to himself · substrate: himself (his own mind / condition) · outcome: he is in his right mind, self-possessed · narrator: Jesus, telling a parable — as reported by Luke

**M16** — The son begins to speak — a soliloquy delivered aloud.
  · agent: he (the younger son) · operation: he said · substrate: the soliloquy that follows · outcome: the reflection is uttered aloud · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** M16 —CONTAINS→ M18; M16 —CONTAINS→ M19; M16 —CONTAINS→ M20; M16 —REPORTS→ M17

**M17** — In the soliloquy: the father's paid workers have more than enough food.
  · agent: hired servants of my father's · operation: have bread enough and to spare (the hired servants) · substrate: bread (enough and to spare) · outcome: the hired servants stand in a state of surplus food · narrator: Jesus, via the son's soliloquy
  · **edges:** ["M16"] —REPORTS→ M17

**M18** — Meanwhile, the son is dying of hunger.
  · agent: I (the son, as one undergoing perishing) · operation: perish (with hunger) · substrate: myself (my own life) · outcome: life ebbs / one is perishing from hunger · narrator: Jesus, via the son's soliloquy
  · **edges:** ["M16"] —CONTAINS→ M18

**M19** — The son resolves to get up and travel back to his father.
  · agent: I (the son) · operation: will arise and go (to my father) · substrate: myself · outcome: resolved course of action — depart the pigs, go to the father · narrator: Jesus, via the son's soliloquy
  · **edges:** ["M16"] —CONTAINS→ M19

**M20** — He plans that, once arrived, he will deliver a piece of speech to the father.
  · agent: I (the son, as planned speaker) · operation: will say (unto him) · substrate: the planned speech that follows · outcome: the speech would be uttered before the father · narrator: Jesus, via the son's soliloquy
  · **edges:** M20 —CONTAINS→ M22; M20 —CONTAINS→ M23; M20 —REPORTS→ M21; ["M16"] —CONTAINS→ M20

**M21** — In the planned speech: a confession — he has wronged God and the father.
  · agent: I (the son) · operation: have sinned (against heaven, and before thee) · substrate: heaven (God, by periphrasis), and thee (the father) — the parties offended · outcome: sin stands committed (and, in the utterance, acknowledged) · narrator: Jesus, via the son's planned confession
  · **edges:** ["M20"] —REPORTS→ M21

**M22** — In the planned speech: he disclaims any right to still be counted a son.
  · agent: I (the son, as the one being evaluated) · operation: am no more worthy (to be called thy son) · substrate: myself (as candidate for being called thy son) · outcome: unworthy of the title 'son' · narrator: Jesus, via the son's planned confession
  · **edges:** ["M20"] —CONTAINS→ M22

**M23** — In the planned speech: he plans to ask the father to reassign him to the status of a paid worker.
  · agent: father (the addressee of the imperative, whom the request names as the one to act) · operation: make me (as one of thy hired servants) · substrate: me (the son, as the one to be re-assigned) · outcome: son treated as one of the hired servants (reinstated into the household at a lowered rank) · narrator: Jesus, via the son's planned confession
  · **edges:** ["M20"] —CONTAINS→ M23

**M24** — The son enacts the resolution — he gets up and travels back, arriving in the father's vicinity.
  · agent: he (the son) · operation: arose and came (to his father) · substrate: himself · outcome: he is at his father / in the father's vicinity · narrator: Jesus, telling a parable — as reported by Luke

**M25** — While the son is still at a distance, the father catches sight of him.
  · agent: his father · operation: saw him · substrate: him (the returning son, at a distance) · outcome: the father has seen the son · narrator: Jesus, telling a parable — as reported by Luke

**M26** — The father is inwardly moved with pity.
  · agent: his father (as experiencer of the affect) · operation: had compassion · substrate: his own inward part (the seat of feeling); implicit object = the son · outcome: the father is moved with compassion · narrator: Jesus, telling a parable — as reported by Luke

**M27** — The father runs (an unusual, undignified sprint for a patriarch).
  · agent: his father · operation: ran · substrate: himself (as self-mover) · outcome: the father is in motion toward the son · narrator: Jesus, telling a parable — as reported by Luke

**M28** — The father throws his arms around the son's neck in embrace.
  · agent: his father · operation: fell on his neck · substrate: his (the son's) neck · outcome: the son is embraced · narrator: Jesus, telling a parable — as reported by Luke

**M29** — The father kisses him.
  · agent: his father · operation: kissed him · substrate: him (the son) · outcome: a kiss is delivered to the son · narrator: Jesus, telling a parable — as reported by Luke

**M30** — The son delivers a piece of speech to the father.
  · agent: the son · operation: said (unto him) · substrate: the utterance that follows · outcome: the confession is spoken to the father · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** M30 —CONTAINS→ M32; M30 —REPORTS→ M31

**M31** — As delivered: the son confesses that he has wronged God and the father in the father's own presence.
  · agent: I (the son) · operation: have sinned (against heaven, and in thy sight) · substrate: heaven (God, by periphrasis), and thy sight (the father's very presence) — the parties/venue of the offence · outcome: sin stands acknowledged before the father · narrator: Jesus, via the son's actually delivered confession
  · **edges:** ["M30"] —REPORTS→ M31

**M32** — As delivered: he disclaims any right to still be counted a son — and then stops, without arriving at the planned petition to be reassigned as a paid worker.
  · agent: I (the son, as the one being evaluated) · operation: am no more worthy (to be called thy son) · substrate: myself (as candidate for being called thy son) · outcome: unworthy of the title 'son' — and the delivered speech ends here · narrator: Jesus, via the son's actually delivered confession
  · **edges:** ["M30"] —CONTAINS→ M32

**M33** — The father, in contrast to the son's confession, addresses his household workers with a rapid string of instructions.
  · agent: the father · operation: said (to his servants) · substrate: the string of instructions that follows · outcome: the household is issued a set of orders · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** M33 —CONTAINS→ M35; M33 —CONTAINS→ M36; M33 —CONTAINS→ M37; M33 —REPORTS→ M34

**M34** — First order: fetch the finest ceremonial garment.
  · agent: servants (the addressees of the imperative) · operation: bring forth (the best robe) · substrate: the best robe · outcome: the finest robe is brought forth · narrator: Jesus, via the father's command
  · **edges:** ["M33"] —REPORTS→ M34

**M35** — Second order: clothe him in it.
  · agent: servants · operation: put it (on him) · substrate: it (the robe) — to be placed on him (the son) · outcome: the son is clothed in the best robe · narrator: Jesus, via the father's command
  · **edges:** ["M33"] —CONTAINS→ M35

**M36** — Third order: place a signet-style ring on his hand.
  · agent: servants · operation: put a ring (on his hand) · substrate: a ring (on his hand) · outcome: a ring is on the son's hand · narrator: Jesus, via the father's command
  · **edges:** ["M33"] —CONTAINS→ M36

**M37** — Fourth order: put footwear on his feet.
  · agent: servants · operation: [put] shoes (on his feet) · substrate: shoes (on his feet) · outcome: shoes are on the son's feet · narrator: Jesus, via the father's command
  · **edges:** ["M33"] —CONTAINS→ M37

**M38** — Continuing the father's orders to his household staff: fetch the calf reserved for special occasions.
  · agent: servants (the addressees, carried over from the previous verse's 'the father said to his servants') · operation: bring hither (the fatted calf) · substrate: the fatted calf · outcome: the fatted calf is brought to the house · narrator: Jesus, via the father's continuing command to his servants

**M39** — Slaughter that calf.
  · agent: servants · operation: kill (it) · substrate: it (the fatted calf) · outcome: the calf is slaughtered (readied as feast-meat) · narrator: Jesus, via the father's continuing command

**M40** — The father calls for a communal feast, drawing himself in with the household.
  · agent: us (the father together with the household) · operation: let us eat · substrate: not-stated (implicitly, the feast-meat of the slaughtered calf) · outcome: the household eats together · narrator: Jesus, via the father's continuing command

**M41** — The father calls the household into a festive mood.
  · agent: us (the father with the household) · operation: be merry · substrate: ourselves (our disposition) · outcome: the household is in a state of merriment · narrator: Jesus, via the father's continuing command

**M42** — The father supplies the warrant for the feast: the son had been effectively dead and gone but is now restored and back in the household's keeping.
  · agent: this my son · operation: was dead, and is alive again; was lost, and is found · substrate: his prior state (dead / lost) · outcome: his present state (alive again / found) · narrator: Jesus, via the father's own justification, spoken to the household

**M43** — The household enters into the celebration.
  · agent: they (the household) · operation: began to be merry · substrate: themselves (their collective disposition) · outcome: the household is in the state of celebration · narrator: Jesus, telling a parable — as reported by Luke

**M44** — Meanwhile the older son had been out doing his customary work.
  · agent: his elder son · operation: was (in the field) · substrate: himself (his person) · outcome: the elder son is in the field (at his labour) · narrator: Jesus, telling a parable — as reported by Luke

**M45** — On his way back, he approaches the house.
  · agent: he (the elder son) · operation: came and drew nigh (to the house) · substrate: himself (as self-mover) · outcome: he is near the house · narrator: Jesus, telling a parable — as reported by Luke

**M46** — He picks up on the sounds of festivity — music and dancing.
  · agent: he (the elder son) · operation: heard (musick and dancing) · substrate: musick and dancing (the sounds of festivity) · outcome: he has perceived the festivity-sounds · narrator: Jesus, telling a parable — as reported by Luke

**M47** — He hails one of the household staff.
  · agent: he (the elder son) · operation: called (one of the servants) · substrate: one of the servants · outcome: a servant is summoned to him · narrator: Jesus, telling a parable — as reported by Luke

**M48** — He puts a question to the summoned staff-member.
  · agent: he (the elder son) · operation: asked · substrate: the question that follows · outcome: a question is put to the servant · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** M48 —REPORTS→ M49

**M49** — The question: what does all this festivity signify?
  · agent: these things (the observed festivity — music, dancing, the whole commotion) · operation: meant / signified (these things) · substrate: not-stated (the meaning-content is precisely what is being queried) · outcome: some meaning (queried, not asserted) · narrator: Jesus, via the elder son's question
  · **edges:** ["M48"] —REPORTS→ M49

**M50** — The staff-member gives him an account.
  · agent: he (the servant) · operation: said (unto him) · substrate: the account that follows · outcome: the elder son is told what has happened · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** M50 —CONTAINS→ M52; M50 —CONTAINS→ M53; M50 —REPORTS→ M51

**M51** — In the report: your younger sibling has arrived.
  · agent: thy brother (the younger son) · operation: is come (thy brother) · substrate: himself (as arriver) · outcome: the younger brother is here / has arrived · narrator: Jesus, via the servant's report
  · **edges:** ["M50"] —REPORTS→ M51

**M52** — In the report: your father has slaughtered the special-occasion calf.
  · agent: thy father · operation: hath killed (the fatted calf) · substrate: the fatted calf · outcome: the fatted calf is slaughtered (for the feast) · narrator: Jesus, via the servant's report
  · **edges:** ["M50"] —CONTAINS→ M52

**M53** — In the report — as gloss on the killing: the father took him back in one piece.
  · agent: he (thy father) · operation: hath received (him safe and sound) · substrate: him (thy brother, the younger son) · outcome: the younger son is received back safe and sound (in a whole / healthy state) · narrator: Jesus, via the servant's report — the servant's own interpretive gloss on the father's motive
  · **edges:** ["M50"] —CONTAINS→ M53

**M54** — The older son flares into anger.
  · agent: he (the elder son, as experiencer) · operation: was angry · substrate: himself (his own inward condition) · outcome: he is in a state of anger · narrator: Jesus, telling a parable — as reported by Luke

**M55** — He refuses to cross the threshold into the house.
  · agent: he (the elder son) · operation: would not go in · substrate: himself (as agent of not-entering) · outcome: he remains outside; the household festival goes on without him · narrator: Jesus, telling a parable — as reported by Luke

**M56** — His father comes outside to him.
  · agent: his father · operation: came out (his father) · substrate: himself (as self-mover) · outcome: the father is outside, with the elder son · narrator: Jesus, telling a parable — as reported by Luke

**M57** — The father pleads with him.
  · agent: his father · operation: intreated (him) · substrate: him (the elder son, as addressee of the pleading) · outcome: the elder son has been entreated (whether he yields is not stated here) · narrator: Jesus, telling a parable — as reported by Luke

**M58** — In reply, the older son speaks back to his father.
  · agent: he (the elder son) · operation: answering said (to his father) · substrate: the reply that follows · outcome: the elder son's reply is uttered to the father · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** M58 —CONTAINS→ M60; M58 —CONTAINS→ M61; M58 —CONTAINS→ M62; M58 —CONTAINS→ M63; M58 —CONTAINS→ M64; M58 —REPORTS→ M59

**M59** — He points out that for a great stretch of years he has served the father.
  · agent: I (the elder son) · operation: do I serve thee (these many years) · substrate: thee (the father, as the one served) · outcome: an unbroken record of service, running many years · narrator: Jesus, via the elder son's reply
  · **edges:** ["M58"] —REPORTS→ M59

**M60** — He claims he has never once broken one of the father's commands.
  · agent: I (the elder son) · operation: neither transgressed I (at any time thy commandment) · substrate: thy commandment (the father's directives) · outcome: no transgression on record (obedience maintained throughout) · narrator: Jesus, via the elder son's reply
  · **edges:** ["M58"] —CONTAINS→ M60

**M61** — Yet, he charges, the father has never so much as given him a young goat so he could throw a small party with his own circle.
  · agent: thou (the father, as agent of the not-giving) · operation: thou never gavest me a kid (that I might make merry with my friends) · substrate: a kid (a young goat — the modest gift never given) · outcome: no gift at any point; the intended purpose (a modest celebration with the son's own circle) never realised · narrator: Jesus, via the elder son's reply
  · **edges:** ["M58"] —CONTAINS→ M61

**M62** — But now — the very moment the one the father claims as his own turns up back home —
  · agent: this thy son (the younger brother, named as the father's — not the elder's) · operation: was come (this thy son) · substrate: himself (as arriver) · outcome: the younger has arrived home · narrator: Jesus, via the elder son's reply
  · **edges:** ["M58"] —CONTAINS→ M62

**M63** — — the one, he adds, who ran through the family estate with prostitutes —
  · agent: which (referring to 'this thy son' — the younger brother) · operation: hath devoured thy living (with harlots) · substrate: thy living (the father's estate / patrimony) · outcome: the estate has been consumed / squandered, in the specified company (harlots) · narrator: Jesus, via the elder son's reply — the 'with harlots' is the elder's own characterisation, not part of the narrator's earlier description (v.13 said 'riotous living' without naming harlots)
  · **edges:** ["M58"] —CONTAINS→ M63

**M64** — — the father has slaughtered the specially-fed calf on his account.
  · agent: thou (the father) · operation: thou hast killed (for him the fatted calf) · substrate: the fatted calf · outcome: the fatted calf has been slaughtered, on the returned brother's behalf · narrator: Jesus, via the elder son's reply
  · **edges:** ["M58"] —CONTAINS→ M64

**M65** — The father speaks back to him.
  · agent: he (the father) · operation: he said (unto him) · substrate: the response that follows · outcome: the father's response is uttered to the elder son · narrator: Jesus, telling a parable — as reported by Luke
  · **edges:** M65 —CONTAINS→ M67; M65 —CONTAINS→ M68; M65 —CONTAINS→ M70; M65 —REPORTS→ M66

**M66** — The elder is continuously in the father's company.
  · agent: thou (the elder son) · operation: thou art ever (with me) · substrate: himself (his ongoing presence) · outcome: the elder stands in unbroken presence with the father · narrator: Jesus, via the father's reply
  · **edges:** ["M65"] —REPORTS→ M66

**M67** — Everything the father owns already belongs to him.
  · agent: all that I have (the father's holdings) · operation: all that I have is thine · substrate: the holdings themselves · outcome: the holdings are already the elder's · narrator: Jesus, via the father's reply
  · **edges:** ["M65"] —CONTAINS→ M67

**M68** — The father evaluates the celebration as the fitting — even the necessary — response.
  · agent: not-stated (impersonal 'it') · operation: it was meet · substrate: the fitting action (a recoverable embedded operation — the making-merry) · outcome: fittingness / rightness attaches to the celebration · narrator: Jesus, via the father's reply
  · **edges:** M68 —REPORTS→ M69; ["M65"] —CONTAINS→ M68

**M69** — The fitting action was that the household should celebrate together in joy.
  · agent: we (the father with the household) · operation: we should make merry, and be glad · substrate: ourselves (our collective disposition) · outcome: the household is in celebration and gladness · narrator: Jesus, via the father's reply
  · **edges:** ["M68"] —REPORTS→ M69

**M70** — The father grounds the fittingness on the warrant: the elder's own sibling had been effectively dead and gone but is now restored and back in the household's keeping.
  · agent: this thy brother (the younger — deliberately named to the elder in fraternal, not paternal, language) · operation: was dead, and is alive again; and was lost, and is found (this thy brother) · substrate: his prior state (dead / lost) · outcome: his present state (alive again / found) · narrator: Jesus, via the father's reply — a near-verbatim recapitulation of the warrant the father gave the servants (v.24), now redirected at the elder son
  · **edges:** ["M65"] —CONTAINS→ M70
