# JONAH — background sheet

> Full coded transcript for **JONAH** — read-only snapshot from the DB.

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
| JONAH | 125 | 0 | 0 | 0 |


## JONAH

### Sitz — situational conditions (source_grounding)

- **summary:** The Book of Jonah (post-exilic Judah, ~430 BCE) is a Second Temple Judahite prose satire whose conditions are almost entirely OUTSIDE the supplied substrate list — none of Confucius, Buddha, or Sophocles bear directly on it. MODEL-KNOWLEDGE: the operative substrate is (a) the post-586 BCE Neo-Babylonian destruction of Jerusalem and the return under Persian (Achaemenid) imperial rule after 538 BCE, which makes 'Nineveh' (fallen 612 BCE) a safely-dead imperial cipher for reflecting on gentile empire; (b) Ezra–Nehemiah-era boundary politics around intermarriage and Judahite ethnic purity, which Jonah's universalist punchline ('shouldn't I be concerned for Nineveh?') directly polemicizes against; (c) Phoenician-dominated eastern-Mediterranean maritime trade (Joppa→Tarshish) as the realistic economic backdrop for the flight narrative; and (d) a Judahite scribal-prophetic literary culture recycling older prophetic figures (the 8th-c. Jonah ben Amittai of 2 Kgs 14:25) as vehicles for new theological argument.
- **categories:** ["political_institutional", "interreligious_contact", "migration_diaspora", "demographic_social", "economic_material"]
- **layers:** ["cultural_intellectual", "polemical", "ecological_material_geographical"]

### Paradigm — the scripts the text thinks with (+ its stance toward each)

_(none coded)_

### Frame — the 8-axis morphospace coordinate

_(none coded)_

### Coded moves — each with the context it picked up

**M1** — The narrator reports that a divine communication reached the prophet.
  · agent: Yahweh's word · operation: come-to · substrate: Jonah son of Amittai · outcome: a speech-event addressed to Jonah · narrator: third-person Hebrew narrator, prophetic-book authority
  · **edges:** M1 —CONTAINS→ M2

**M2** — Yahweh commands the prophet to get up and travel to the great city.
  · agent: Yahweh · operation: command-to-go · substrate: Jonah · outcome: obligation on Jonah to go to Nineveh · narrator: third-person Hebrew narrator
  · **edges:** M2 —CONTAINS→ M4; M2 —REPORTS→ M3; ["M1"] —CONTAINS→ M2

**M3** — Yahweh commands the prophet to preach against the city.
  · agent: Yahweh · operation: command-to-preach-against · substrate: Nineveh · outcome: obligation to proclaim against it · narrator: third-person Hebrew narrator
  · **edges:** ["M2"] —REPORTS→ M3

**M4** — Yahweh justifies the command by declaring the city's wickedness has risen before him.
  · agent: Nineveh's wickedness · operation: declare-grounds · substrate: Yahweh's attention · outcome: warrant for the sending · narrator: third-person Hebrew narrator
  · **edges:** ["M2"] —CONTAINS→ M4

**M5** — Instead of obeying, the prophet gets up in order to flee toward a far port, away from the divine presence.
  · agent: Jonah · operation: rise-to-flee · substrate: the commission / Yahweh's presence · outcome: a flight underway toward Tarshish · narrator: third-person Hebrew narrator

**M6** — He descends to the port city.
  · agent: Jonah · operation: go-down-to · substrate: his location · outcome: Jonah at Joppa · narrator: third-person Hebrew narrator

**M7** — He finds a ship bound for the far port.
  · agent: Jonah · operation: find · substrate: available shipping · outcome: a Tarshish-bound ship located · narrator: third-person Hebrew narrator

**M8** — He pays the fare.
  · agent: Jonah · operation: pay-fare · substrate: the fare · outcome: passage secured · narrator: third-person Hebrew narrator

**M9** — He descends into the vessel to travel with them away from the divine presence.
  · agent: Jonah · operation: go-down-into · substrate: the ship · outcome: Jonah aboard, en route away from Yahweh's presence · narrator: third-person Hebrew narrator

**M10** — Yahweh hurls a great wind onto the sea.
  · agent: Yahweh · operation: hurl-wind · substrate: the sea · outcome: a great wind on the sea · narrator: third-person Hebrew narrator

**M11** — A mighty storm arises on the sea such that the ship nearly breaks up.
  · agent: not-stated · operation: storm-arise · substrate: the sea and ship · outcome: ship on the verge of breaking · narrator: third-person Hebrew narrator

**M12** — The sailors become afraid.
  · agent: the mariners · operation: become-afraid · substrate: themselves · outcome: fearful crew · narrator: third-person Hebrew narrator

**M13** — Each sailor cries out to his own god.
  · agent: each mariner · operation: cry-to-god · substrate: his own god · outcome: polytheistic appeals for rescue · narrator: third-person Hebrew narrator

**M14** — They jettison the cargo to lighten the ship.
  · agent: the mariners · operation: jettison · substrate: the cargo · outcome: a lightened ship · narrator: third-person Hebrew narrator

**M15** — Meanwhile, the prophet had gone down into the ship's innermost part.
  · agent: Jonah · operation: go-down-into-hold · substrate: the ship's interior · outcome: Jonah in the hold · narrator: third-person Hebrew narrator

**M16** — He lay down and fell into deep sleep.
  · agent: Jonah · operation: sleep-deeply · substrate: himself · outcome: Jonah fast asleep · narrator: third-person Hebrew narrator

**M17** — The captain approaches the sleeper.
  · agent: ship master · operation: approach · substrate: Jonah · outcome: captain at Jonah's side · narrator: third-person Hebrew narrator

**M18** — The captain rebukes him for sleeping.
  · agent: ship master · operation: rebuke · substrate: Jonah · outcome: a reproach delivered · narrator: third-person Hebrew narrator
  · **edges:** M18 —CONTAINS→ M20; M18 —REPORTS→ M19

**M19** — The captain commands him to get up and call on his god.
  · agent: ship master · operation: command-to-pray · substrate: Jonah · outcome: obligation to invoke Jonah's god · narrator: third-person Hebrew narrator
  · **edges:** ["M18"] —REPORTS→ M19

**M20** — The captain voices the hope that Jonah's god will take notice and spare them.
  · agent: ship master · operation: hope-for-notice · substrate: Jonah's god's possible attention · outcome: a stated hope of rescue · narrator: third-person Hebrew narrator
  · **edges:** ["M18"] —CONTAINS→ M20

**M21** — The sailors propose to one another that they cast lots to identify the guilty party.
  · agent: the mariners · operation: propose-lot-casting · substrate: themselves · outcome: a plan to cast lots · narrator: third-person Hebrew narrator

**M22** — They perform the casting of lots.
  · agent: the mariners · operation: cast-lots · substrate: the lots · outcome: a divinatory result · narrator: third-person Hebrew narrator

**M23** — The lot falls on the prophet.
  · agent: not-stated · operation: lot-falls-on · substrate: Jonah · outcome: Jonah singled out as culpable · narrator: third-person Hebrew narrator

**M24** — They interrogate him about the cause of the calamity and his identity.
  · agent: the mariners · operation: interrogate · substrate: Jonah · outcome: a battery of identifying questions posed · narrator: third-person Hebrew narrator

**M25** — He declares his ethnic identity to them.
  · agent: Jonah · operation: self-identify · substrate: the sailors · outcome: 'I am a Hebrew' spoken · narrator: third-person Hebrew narrator

**M26** — He professes reverence for the sky-god who made sea and land.
  · agent: Jonah · operation: profess-fear-of-Yahweh · substrate: the sailors · outcome: a theological self-declaration · narrator: third-person Hebrew narrator
  · **edges:** M26 —REPORTS→ M27

**M27** — He reveres Yahweh, the god of the sky.
  · agent: Jonah · operation: fear/revere · substrate: Yahweh · outcome: a stance of reverence · narrator: Jonah (embedded), reported by the narrator
  · **edges:** ["M26"] —REPORTS→ M27

**M28** — The men become exceedingly afraid.
  · agent: the mariners · operation: become-more-afraid · substrate: themselves · outcome: heightened terror · narrator: third-person Hebrew narrator

**M29** — They exclaim to him a horrified reproach.
  · agent: the mariners · operation: exclaim-reproach · substrate: Jonah · outcome: 'What have you done?' voiced · narrator: third-person Hebrew narrator

**M30** — The narrator explains that the men now knew he was fleeing the divine presence.
  · agent: the mariners · operation: know · substrate: the fact of Jonah's flight · outcome: crew's knowledge state · narrator: third-person Hebrew narrator, aside

**M31** — The narrator notes that Jonah himself had earlier disclosed this to them.
  · agent: Jonah · operation: had-told · substrate: the mariners · outcome: prior disclosure that grounds M30 · narrator: third-person Hebrew narrator

**M32** — They ask him what to do to calm the sea.
  · agent: the mariners · operation: ask-remedy · substrate: Jonah · outcome: a question about the remedy · narrator: third-person Hebrew narrator

**M33** — The narrator notes that the sea was growing steadily more violent.
  · agent: not-stated · operation: grow-stormier · substrate: the sea · outcome: escalating storm · narrator: third-person Hebrew narrator, aside

**M34** — He instructs them to lift him and throw him overboard.
  · agent: Jonah · operation: instruct-to-throw-overboard · substrate: the mariners · outcome: instruction to jettison him · narrator: third-person Hebrew narrator
  · **edges:** M34 —CONTAINS→ M35; M34 —CONTAINS→ M36

**M35** — He predicts the sea will then become calm for them.
  · agent: Jonah · operation: predict-calm · substrate: the sea's future state · outcome: a stated prediction of calm · narrator: third-person Hebrew narrator
  · **edges:** ["M34"] —CONTAINS→ M35

**M36** — He confesses he knows this storm is on account of him.
  · agent: Jonah · operation: acknowledge-cause · substrate: his own culpability · outcome: confessed knowledge · narrator: third-person Hebrew narrator
  · **edges:** ["M34"] —CONTAINS→ M36

**M37** — Nevertheless the sailors rowed hard to bring the ship back to shore.
  · agent: the mariners · operation: row-hard-to-return · substrate: the ship / sea · outcome: strenuous rowing toward land · narrator: third-person Hebrew narrator

**M38** — They could not succeed, because the sea kept growing more violent against them.
  · agent: not-stated · operation: fail-to-return · substrate: their effort · outcome: failed return; storm intensifying · narrator: third-person Hebrew narrator

**M39** — They cry out to Yahweh in pleading prayer.
  · agent: the mariners · operation: cry-to-Yahweh · substrate: Yahweh · outcome: a prayer of appeal · narrator: third-person Hebrew narrator
  · **edges:** M39 —CONTAINS→ M41; M39 —REPORTS→ M40

**M40** — They beg him not to let them die on account of this man and not to hold them guilty of innocent blood.
  · agent: the mariners · operation: petition-for-innocence · substrate: Yahweh · outcome: a petition against blood-guilt · narrator: the mariners (embedded), reported by narrator
  · **edges:** ["M39"] —REPORTS→ M40

**M41** — They acknowledge that Yahweh has done as he pleased.
  · agent: the mariners · operation: acknowledge-sovereignty · substrate: Yahweh's action · outcome: stated acknowledgment of divine sovereignty · narrator: the mariners (embedded), reported by narrator
  · **edges:** ["M39"] —CONTAINS→ M41

**M42** — They lift Jonah and cast him into the sea.
  · agent: the mariners · operation: throw-overboard · substrate: Jonah · outcome: Jonah in the sea · narrator: third-person Hebrew narrator

**M43** — The sea stops its raging.
  · agent: not-stated · operation: cease-raging · substrate: the sea · outcome: calm sea · narrator: third-person Hebrew narrator

**M44** — The men come to revere Yahweh intensely.
  · agent: the mariners · operation: fear-Yahweh · substrate: Yahweh · outcome: reverent stance toward Yahweh · narrator: third-person Hebrew narrator

**M45** — They offer a sacrifice to Yahweh.
  · agent: the mariners · operation: offer-sacrifice · substrate: a sacrifice · outcome: sacrifice given to Yahweh · narrator: third-person Hebrew narrator

**M46** — They make vows.
  · agent: the mariners · operation: make-vows · substrate: themselves · outcome: vows binding them to Yahweh · narrator: third-person Hebrew narrator

**M47** — Yahweh appoints a great fish to swallow the prophet.
  · agent: Yahweh · operation: appoint-fish · substrate: a great fish · outcome: fish designated to swallow Jonah · narrator: third-person Hebrew narrator

**M48** — The fish swallows the prophet.
  · agent: the great fish · operation: swallow · substrate: Jonah · outcome: Jonah inside the fish · narrator: third-person Hebrew narrator

**M49** — The prophet remained in the fish's belly for three days and three nights.
  · agent: not-stated · operation: remain-inside · substrate: Jonah · outcome: Jonah in the belly for three days and nights · narrator: third-person Hebrew narrator

**M50** — The narrator reports that the prophet offered prayer to his god from inside the fish.
  · agent: Jonah · operation: pray-to · substrate: Yahweh · outcome: a prayer directed to Yahweh from the fish's belly · narrator: third-person Hebrew narrator, prophetic-book authority
  · **edges:** M50 —REPORTS→ M51

**M51** — The narrator marks that the following words are Jonah's own speech.
  · agent: Jonah · operation: say · substrate: not-stated · outcome: introduced direct speech · narrator: third-person Hebrew narrator
  · **edges:** M51 —CONTAINS→ M53; M51 —CONTAINS→ M54; M51 —CONTAINS→ M55; M51 —CONTAINS→ M56; M51 —CONTAINS→ M57; M51 —CONTAINS→ M58; M51 —CONTAINS→ M61; M51 —CONTAINS→ M62; M51 —CONTAINS→ M63; M51 —CONTAINS→ M64; M51 —CONTAINS→ M65; M51 —CONTAINS→ M66; M51 —CONTAINS→ M67; M51 —CONTAINS→ M68; M51 —CONTAINS→ M69; M51 —CONTAINS→ M70; M51 —CONTAINS→ M71; M51 —CONTAINS→ M72; M51 —REPORTS→ M52; ["M50"] —REPORTS→ M51

**M52** — Jonah recalls that in his distress he cried out to Yahweh.
  · agent: Jonah · operation: call-out-from-distress · substrate: Yahweh · outcome: a cry raised to Yahweh · narrator: Jonah (first person), embedded in narrator's frame
  · **edges:** ["M51"] —REPORTS→ M52

**M53** — He recounts that Yahweh answered him.
  · agent: Yahweh · operation: answer · substrate: Jonah · outcome: a response given · narrator: Jonah, embedded
  · **edges:** ["M51"] —CONTAINS→ M53

**M54** — He recalls crying out from the realm of the dead.
  · agent: Jonah · operation: cry-from-Sheol · substrate: Yahweh (implied addressee) · outcome: a cry from Sheol · narrator: Jonah, embedded
  · **edges:** ["M51"] —CONTAINS→ M54

**M55** — He tells Yahweh that Yahweh heard his voice.
  · agent: Yahweh · operation: hear · substrate: Jonah's voice · outcome: the cry received · narrator: Jonah, embedded
  · **edges:** ["M51"] —CONTAINS→ M55

**M56** — He attributes the casting into the deep to Yahweh himself.
  · agent: Yahweh · operation: cast-into-deep · substrate: Jonah · outcome: Jonah in the depths at the heart of the seas · narrator: Jonah, embedded
  · **edges:** ["M51"] —CONTAINS→ M56

**M57** — He describes floodwater enveloping him and waves and breakers sweeping over him.
  · agent: the flood / Yahweh's waves and billows · operation: engulf · substrate: Jonah · outcome: Jonah surrounded and overwhelmed · narrator: Jonah, embedded
  · **edges:** ["M51"] —CONTAINS→ M57

**M58** — He reports that he had said, thinking he was expelled from the deity's sight.
  · agent: Jonah · operation: say-inward · substrate: himself · outcome: an inner speech uttered · narrator: Jonah, embedded
  · **edges:** M58 —CONTAINS→ M60; M58 —REPORTS→ M59; ["M51"] —CONTAINS→ M58

**M59** — He judges himself expelled from Yahweh's presence.
  · agent: Jonah · operation: deem-banished · substrate: his standing before Yahweh · outcome: a stated sense of banishment · narrator: Jonah, embedded
  · **edges:** ["M58"] —REPORTS→ M59

**M60** — He resolves nonetheless to gaze again toward the deity's holy sanctuary.
  · agent: Jonah · operation: resolve-to-look-toward-temple · substrate: Yahweh's holy temple · outcome: a stated intention to orient toward the sanctuary · narrator: Jonah, embedded
  · **edges:** ["M58"] —CONTAINS→ M60

**M61** — He describes waters closing around him to the point of his life.
  · agent: the waters · operation: encircle · substrate: Jonah (to his soul) · outcome: Jonah encircled to the point of his life · narrator: Jonah, embedded
  · **edges:** ["M51"] —CONTAINS→ M61

**M62** — He says the deep encircled him.
  · agent: the deep · operation: encircle · substrate: Jonah · outcome: Jonah enclosed by the deep · narrator: Jonah, embedded
  · **edges:** ["M51"] —CONTAINS→ M62

**M63** — He reports seaweed wrapping around his head.
  · agent: weeds · operation: wrap-around · substrate: Jonah's head · outcome: weeds bound about his head · narrator: Jonah, embedded
  · **edges:** ["M51"] —CONTAINS→ M63

**M64** — He recalls descending to the roots of the mountains.
  · agent: Jonah · operation: go-down-to · substrate: the mountain-roots · outcome: Jonah at the base of the mountains · narrator: Jonah, embedded
  · **edges:** ["M51"] —CONTAINS→ M64

**M65** — He says the earth shut its bars against him forever.
  · agent: the earth · operation: bar-in · substrate: Jonah · outcome: Jonah shut in as if permanently · narrator: Jonah, embedded
  · **edges:** ["M51"] —CONTAINS→ M65

**M66** — He praises Yahweh for hauling his life back up from the pit.
  · agent: Yahweh · operation: bring-up-from-pit · substrate: Jonah's life · outcome: life raised out of the pit · narrator: Jonah, embedded
  · **edges:** ["M51"] —CONTAINS→ M66

**M67** — He recounts that when his life was ebbing away, he called Yahweh to mind.
  · agent: Jonah · operation: remember · substrate: Yahweh · outcome: Yahweh brought to mind at the point of collapse · narrator: Jonah, embedded
  · **edges:** ["M51"] —CONTAINS→ M67

**M68** — He says his prayer reached the deity in the holy sanctuary.
  · agent: Jonah's prayer · operation: come-in-to · substrate: Yahweh's holy temple · outcome: prayer arrived before Yahweh · narrator: Jonah, embedded
  · **edges:** ["M51"] —CONTAINS→ M68

**M69** — He passes a general verdict that those who cling to empty idols forsake the loyal-love that would have been theirs.
  · agent: those who regard lying vanities · operation: deem-idolaters-forsake-mercy · substrate: their own mercy · outcome: the idolaters relinquishing their loyal-love · narrator: Jonah, embedded
  · **edges:** ["M51"] —CONTAINS→ M69

**M70** — He vows to offer sacrifice with a voice of thanksgiving.
  · agent: Jonah · operation: pledge-sacrifice · substrate: Yahweh · outcome: a stated pledge to sacrifice with thanksgiving · narrator: Jonah, embedded
  · **edges:** ["M51"] —CONTAINS→ M70

**M71** — He pledges to fulfill what he has vowed.
  · agent: Jonah · operation: pledge-payment-of-vow · substrate: his vow · outcome: a stated commitment to pay the vow · narrator: Jonah, embedded
  · **edges:** ["M51"] —CONTAINS→ M71

**M72** — He confesses that rescue belongs to Yahweh.
  · agent: Jonah · operation: ascribe-salvation · substrate: Yahweh · outcome: a stated confession that deliverance is Yahweh's · narrator: Jonah, embedded
  · **edges:** ["M51"] —CONTAINS→ M72

**M73** — The narrator reports that Yahweh addressed the fish.
  · agent: Yahweh · operation: speak-to · substrate: the fish · outcome: a command directed to the fish · narrator: third-person Hebrew narrator

**M74** — The fish disgorged the prophet onto the shore.
  · agent: the fish · operation: vomit-out · substrate: Jonah · outcome: Jonah on dry land · narrator: third-person Hebrew narrator

**M75** — The narrator reports that a divine communication came to the prophet a second time.
  · agent: Yahweh's word · operation: come-to · substrate: Jonah · outcome: a second speech-event addressed to Jonah · narrator: third-person Hebrew narrator, prophetic-book authority
  · **edges:** M75 —CONTAINS→ M76

**M76** — Yahweh commands the prophet to get up and travel to the great city.
  · agent: Yahweh · operation: command-to-go · substrate: Jonah · outcome: obligation on Jonah to go to Nineveh · narrator: third-person Hebrew narrator
  · **edges:** M76 —REPORTS→ M77; ["M75"] —CONTAINS→ M76

**M77** — Yahweh commands the prophet to proclaim to the city the message Yahweh will give him.
  · agent: Yahweh · operation: command-to-preach · substrate: Nineveh · outcome: obligation to deliver Yahweh's message to the city · narrator: third-person Hebrew narrator
  · **edges:** ["M76"] —REPORTS→ M77

**M78** — The prophet gets up and goes to the city in accordance with the divine word.
  · agent: Jonah · operation: rise-and-go · substrate: the commission · outcome: Jonah arrived at Nineveh · narrator: third-person Hebrew narrator

**M79** — The narrator notes parenthetically that the city was enormously large, a three-day traverse.
  · agent: not-stated · operation: characterize-city-size · substrate: Nineveh · outcome: stated size/scale of the city · narrator: third-person Hebrew narrator, aside

**M80** — He begins to penetrate the city, going a day's journey in.
  · agent: Jonah · operation: enter-into · substrate: the city · outcome: Jonah one day's walk inside Nineveh · narrator: third-person Hebrew narrator

**M81** — He cries out publicly with a proclamation.
  · agent: Jonah · operation: cry-out · substrate: Nineveh (hearers) · outcome: a public proclamation delivered · narrator: third-person Hebrew narrator
  · **edges:** M81 —REPORTS→ M82

**M82** — He announces that in forty days the city will be overturned.
  · agent: Nineveh · operation: announce-overthrow · substrate: Nineveh's future · outcome: a stated forty-day threat of overthrow · narrator: Jonah (embedded), reported by narrator
  · **edges:** ["M81"] —REPORTS→ M82

**M83** — The city's inhabitants put trust in the deity.
  · agent: the people of Nineveh · operation: believe · substrate: God · outcome: a stance of trust in God · narrator: third-person Hebrew narrator

**M84** — They proclaim a fast.
  · agent: the people of Nineveh · operation: proclaim-fast · substrate: themselves · outcome: a fast declared · narrator: third-person Hebrew narrator

**M85** — They don sackcloth, from greatest to least.
  · agent: the people of Nineveh · operation: put-on-sackcloth · substrate: themselves · outcome: the whole populace clothed in sackcloth · narrator: third-person Hebrew narrator

**M86** — The report reaches the king of the city.
  · agent: the news · operation: reach · substrate: the king · outcome: the king informed · narrator: third-person Hebrew narrator

**M87** — The king rises from his throne.
  · agent: the king of Nineveh · operation: rise-from-throne · substrate: his throne · outcome: the king off his throne · narrator: third-person Hebrew narrator

**M88** — He removes his royal robe.
  · agent: the king · operation: remove-robe · substrate: his royal robe · outcome: robe set aside · narrator: third-person Hebrew narrator

**M89** — He covers himself with sackcloth.
  · agent: the king · operation: cover-with-sackcloth · substrate: himself · outcome: king clothed in sackcloth · narrator: third-person Hebrew narrator

**M90** — He sits down in ashes.
  · agent: the king · operation: sit-in-ashes · substrate: ashes · outcome: king seated in ashes · narrator: third-person Hebrew narrator

**M91** — He issues a proclamation throughout the city under royal-and-noble decree.
  · agent: the king (with his nobles) · operation: issue-proclamation · substrate: Nineveh · outcome: a decree published city-wide · narrator: third-person Hebrew narrator
  · **edges:** M91 —CONTAINS→ M93; M91 —CONTAINS→ M94; M91 —CONTAINS→ M95; M91 —CONTAINS→ M96; M91 —CONTAINS→ M97; M91 —REPORTS→ M92

**M92** — The decree forbids any person or animal — herd or flock — to taste anything.
  · agent: the king (with his nobles) · operation: forbid-tasting · substrate: humans and animals of Nineveh · outcome: a ban on tasting food · narrator: the king (embedded), reported by narrator
  · **edges:** ["M91"] —REPORTS→ M92

**M93** — It forbids grazing and drinking water.
  · agent: the king (with his nobles) · operation: forbid-eating-and-drinking · substrate: humans and animals of Nineveh · outcome: a ban on feeding and drinking · narrator: the king (embedded)
  · **edges:** ["M91"] —CONTAINS→ M93

**M94** — It orders humans and beasts alike to be clothed in sackcloth.
  · agent: the king (with his nobles) · operation: order-sackcloth · substrate: humans and animals of Nineveh · outcome: mandated sackcloth-wearing · narrator: the king (embedded)
  · **edges:** ["M91"] —CONTAINS→ M94

**M95** — It commands them to cry out mightily to the deity.
  · agent: the king (with his nobles) · operation: order-cry-to-god · substrate: humans and animals of Nineveh · outcome: mandated urgent cry to God · narrator: the king (embedded)
  · **edges:** ["M91"] —CONTAINS→ M95

**M96** — It commands each one to turn back from his evil way and from the violence in his hands.
  · agent: the king (with his nobles) · operation: order-turn-from-evil · substrate: each person of Nineveh · outcome: mandated turning from evil and violence · narrator: the king (embedded)
  · **edges:** ["M91"] —CONTAINS→ M96

**M97** — It voices the hope that the deity may perhaps relent and spare them.
  · agent: the king (with his nobles) · operation: hope-for-relenting · substrate: God's possible relenting · outcome: a stated hope that God might turn from fierce anger and they not perish · narrator: the king (embedded)
  · **edges:** ["M91"] —CONTAINS→ M97

**M98** — The deity observes their deeds, namely that they turned from their evil way.
  · agent: God · operation: see · substrate: their works / their turning · outcome: God cognizant of their turning · narrator: third-person Hebrew narrator

**M99** — The deity relents of the disaster he had said he would inflict and does not carry it out.
  · agent: God · operation: relent-of-disaster · substrate: the announced disaster · outcome: disaster withheld; not enacted · narrator: third-person Hebrew narrator

**M100** — The narrator reports that the outcome greatly displeased the prophet.
  · agent: the situation (God's relenting) · operation: displease · substrate: Jonah · outcome: Jonah greatly displeased · narrator: third-person Hebrew narrator, prophetic-book authority

**M101** — The prophet became angry.
  · agent: Jonah · operation: become-angry · substrate: himself · outcome: Jonah angry · narrator: third-person Hebrew narrator

**M102** — He prayed to Yahweh.
  · agent: Jonah · operation: pray-to · substrate: Yahweh · outcome: a prayer directed to Yahweh · narrator: third-person Hebrew narrator
  · **edges:** M102 —CONTAINS→ M105; M102 —CONTAINS→ M106; M102 —CONTAINS→ M107; M102 —CONTAINS→ M108; M102 —REPORTS→ M103

**M103** — He appeals to Yahweh, asking whether this outcome was not exactly what he had said back home.
  · agent: Jonah · operation: appeal-recall · substrate: Yahweh · outcome: a rhetorical appeal to his prior words · narrator: Jonah (embedded), reported by narrator
  · **edges:** M103 —REPORTS→ M104; ["M102"] —REPORTS→ M103

**M104** — He recalls that back in his homeland he had already said this would happen.
  · agent: Jonah (past) · operation: had-said · substrate: not-stated (his own hearers/self) · outcome: a prior anticipatory statement · narrator: Jonah (embedded)
  · **edges:** ["M103"] —REPORTS→ M104

**M105** — He explains that this is why he had hastened to flee toward the far port.
  · agent: Jonah · operation: explain-flight · substrate: his prior flight · outcome: a stated rationale for the Tarshish flight · narrator: Jonah (embedded)
  · **edges:** ["M102"] —CONTAINS→ M105

**M106** — He grounds the flight in his prior knowledge of Yahweh's merciful character.
  · agent: Jonah · operation: know · substrate: Yahweh's character · outcome: a stated knowledge that Yahweh is gracious, merciful, slow to anger, abounding in loyal-love, and relents from harm · narrator: Jonah (embedded)
  · **edges:** ["M102"] —CONTAINS→ M106

**M107** — He begs Yahweh to take his life from him.
  · agent: Jonah · operation: beg-for-death · substrate: Yahweh · outcome: a petition that his life be taken · narrator: Jonah (embedded)
  · **edges:** ["M102"] —CONTAINS→ M107

**M108** — He judges that dying would be better for him than living.
  · agent: Jonah · operation: deem-death-better · substrate: his life vs. death · outcome: a stated evaluation that death is preferable · narrator: Jonah (embedded)
  · **edges:** ["M102"] —CONTAINS→ M108

**M109** — Yahweh responds with a question, asking whether Jonah is right to be angry.
  · agent: Yahweh · operation: question-anger · substrate: Jonah · outcome: a challenging question posed · narrator: third-person Hebrew narrator

**M110** — The prophet leaves the city.
  · agent: Jonah · operation: go-out-of · substrate: the city · outcome: Jonah outside Nineveh · narrator: third-person Hebrew narrator

**M111** — He sits down on the east side of the city.
  · agent: Jonah · operation: sit-east-of-city · substrate: a spot east of the city · outcome: Jonah seated east of Nineveh · narrator: third-person Hebrew narrator

**M112** — He makes himself a shelter there.
  · agent: Jonah · operation: make-booth · substrate: materials at hand · outcome: a booth built for himself · narrator: third-person Hebrew narrator

**M113** — He sits under it in the shade to see what would become of the city.
  · agent: Jonah · operation: sit-and-wait · substrate: the booth's shade · outcome: Jonah waiting to see the city's fate · narrator: third-person Hebrew narrator

**M114** — Yahweh appoints a plant and causes it to grow up over the prophet as shade to relieve his distress.
  · agent: Yahweh God · operation: appoint-plant · substrate: a vine · outcome: a vine grown up over Jonah as shade to deliver him from discomfort · narrator: third-person Hebrew narrator

**M115** — The prophet became exceedingly glad because of the plant.
  · agent: Jonah · operation: become-glad · substrate: himself · outcome: Jonah greatly glad on account of the vine · narrator: third-person Hebrew narrator

**M116** — At dawn the next day the deity appoints a worm.
  · agent: God · operation: appoint-worm · substrate: a worm · outcome: a worm designated to attack the vine · narrator: third-person Hebrew narrator

**M117** — The worm chewed the plant so that it withered.
  · agent: the worm · operation: chew-to-wither · substrate: the vine · outcome: the vine withered · narrator: third-person Hebrew narrator

**M118** — When the sun rose, the deity appointed a scorching east wind.
  · agent: God · operation: appoint-east-wind · substrate: a sultry east wind · outcome: a hot east wind set in motion · narrator: third-person Hebrew narrator

**M119** — The sun beat down on the prophet's head so that he grew faint.
  · agent: the sun · operation: beat-down-on · substrate: Jonah's head · outcome: Jonah faint from the heat · narrator: third-person Hebrew narrator

**M120** — He requested for himself that he might die.
  · agent: Jonah · operation: request-death · substrate: himself (as addressee/self) · outcome: a stated request for death · narrator: third-person Hebrew narrator
  · **edges:** M120 —REPORTS→ M121

**M121** — He judges that dying would be better for him than living.
  · agent: Jonah · operation: deem-death-better · substrate: his life vs. death · outcome: a stated evaluation that death is preferable · narrator: Jonah (embedded)
  · **edges:** ["M120"] —REPORTS→ M121

**M122** — The deity asks Jonah whether he is right to be angry about the plant.
  · agent: God · operation: question-anger-about-vine · substrate: Jonah · outcome: a challenging question posed regarding the vine · narrator: third-person Hebrew narrator

**M123** — The prophet asserts that he is right to be angry, even to the point of death.
  · agent: Jonah · operation: assert-right-to-anger · substrate: his own anger · outcome: a stated self-justification of anger unto death · narrator: third-person Hebrew narrator (with embedded Jonah speech)

**M124** — Yahweh points out that Jonah has been concerned for a plant he did not work for, that sprang up overnight and perished overnight.
  · agent: Yahweh · operation: observe-concern-for-vine · substrate: Jonah's concern for the vine · outcome: a stated observation of the disproportion of that concern · narrator: third-person Hebrew narrator (with embedded divine speech)

**M125** — Yahweh asks whether he himself ought not to be concerned for the great city with its vast population who cannot tell right hand from left, and its many animals.
  · agent: Yahweh · operation: question-own-concern-for-Nineveh · substrate: Nineveh (its people and livestock) · outcome: a rhetorical question asserting divine concern for the city · narrator: third-person Hebrew narrator (with embedded divine speech)
