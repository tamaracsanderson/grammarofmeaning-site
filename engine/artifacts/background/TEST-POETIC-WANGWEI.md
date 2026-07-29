# TEST-POETIC-WANGWEI — background sheet

> Full coded transcript for **TEST-POETIC-WANGWEI** — read-only snapshot from the DB.

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
| TEST-POETIC-WANGWEI | 25 | 0 | 0 | 0 |


## TEST-POETIC-WANGWEI

### Sitz — situational conditions (source_grounding)

_(no Sitz grounding row)_

### Paradigm — the scripts the text thinks with (+ its stance toward each)

_(none coded)_

### Frame — the 8-axis morphospace coordinate

_(none coded)_

### Coded moves — each with the context it picked up

**M1** — The teller reports that, to view, the mountain shows no human presence — a hedged claim of absence.
  · agent: mountain · operation: seem-empty · substrate: presence of any person · outcome: apparent human-absence · narrator: first-person mountain-dweller reporting his own perception as eyewitness

**M2** — The teller concedes a cognitive impression that cuts against M1 — he takes himself to be catching a human sound.
  · agent: first-person speaker · operation: think · substrate: the embedded perceptual claim M3 · outcome: held impression, hedged by 'I think' · narrator: first-person mountain-dweller reporting his own inner cognition
  · **edges:** M2 —REPORTS→ M3

**M3** — Inside the cognition of M2: the speaker's hearing takes in a voice.
  · agent: first-person speaker · operation: hear · substrate: a voice · outcome: auditory intake of a human sound · narrator: same first-person speaker; here the reported (inner) content, not the frame
  · **edges:** ["M2"] —REPORTS→ M3

**M4** — Sunlight that has passed into the grove is thrown back off the moss and finds the speaker.
  · agent: sunlight · operation: reflect-back · substrate: the green moss · outcome: reflected light returning to the speaker · narrator: first-person mountain-dweller as receiving eye

**M5** — The speaker holds a solitary posture within the close-set bamboos.
  · agent: first-person speaker · operation: lean-alone · substrate: his own posture (in the bamboo grove) · outcome: solitary held-position among the stalks · narrator: first-person recluse describing his own bodily situation

**M6** — The speaker sounds his lute.
  · agent: first-person speaker · operation: play · substrate: his lute · outcome: music produced from the instrument · narrator: first-person recluse reporting his own action

**M7** — The speaker voices a song under breath.
  · agent: first-person speaker · operation: hum · substrate: a song · outcome: quiet vocalization of a tune · narrator: first-person recluse reporting his own action

**M8** — The sound stays under any human ear — nobody catches it.
  · agent: no human listener · operation: fail-to-hear · substrate: the lute-and-song of M6/M7 · outcome: inaudibility to any person · narrator: first-person recluse claiming the reception-side of his own making

**M9** — The exception to that unhearing: the moon is a listener.
  · agent: the bright moon · operation: hear · substrate: the lute-and-song of M6/M7 · outcome: presence of a single listener · narrator: first-person recluse crediting the moon as reception

**M10** — The speaker names the moon a companion of his own.
  · agent: first-person speaker · operation: deem-companion · substrate: the bright moon · outcome: the moon-as-comrade construed · narrator: first-person recluse making an attributive claim

**M11** — The speaker kept his eye on his friend the whole way down the slope.
  · agent: first-person speaker · operation: watch-until-gone · substrate: the departing friend · outcome: the friend followed by gaze until beyond sight · narrator: first-person host reporting his own past attention

**M12** — Now, in darkness, the speaker shuts up his hut.
  · agent: first-person speaker · operation: close · substrate: the door of his thatched hut · outcome: the hut sealed for the night · narrator: first-person host reporting his present, post-farewell action

**M13** — The grasses will, as they always do, come back green with the season.
  · agent: the grasses · operation: return-green · substrate: not-stated · outcome: their annual reappearance in spring · narrator: first-person host invoking a stock natural regularity

**M14** — The speaker addresses the departed with an intimate title of honor.
  · agent: first-person speaker · operation: address-with-title · substrate: the departed friend · outcome: the friend named 'Prince of Friends' · narrator: first-person host addressing the absent friend directly

**M15** — The speaker puts to the friend the open question of whether he, too, will come again — playing on the grasses of M13.
  · agent: first-person speaker · operation: question-return · substrate: the friend's possible return · outcome: unanswered question hanging in the air · narrator: first-person host putting a question to the absent friend

**M16** — With the rain over, the empty mountain wears its autumn evening.
  · agent: the empty mountain · operation: stand-autumnal · substrate: not-stated · outcome: post-rain autumnal appearance in the evening · narrator: first-person mountain-dweller framing the whole scene for a visitor

**M17** — Moonlight sits inside the pine groves.
  · agent: moonlight · operation: rest-upon · substrate: the pine groves · outcome: the groves inhabited by light · narrator: first-person eye scanning across the scene

**M18** — In the brooks, the stones show as crystalline.
  · agent: the stones · operation: appear-crystal · substrate: the brooks (as their setting) · outcome: crystalline appearance of the stones in water · narrator: first-person eye moving across the scene

**M19** — The bamboos make a sound that reads as the passing of women coming back from washing — a reporting through personification.
  · agent: the bamboos · operation: whisper · substrate: the embedded scene M20 · outcome: audible presence of what M20 describes · narrator: first-person listener reading meaning out of natural sound
  · **edges:** M19 —REPORTS→ M20

**M20** — Inside what the bamboos convey: the women who have been washing are on their way back.
  · agent: the washer-girls · operation: return-home · substrate: not-stated (their homeward path) · outcome: them heading home · narrator: same first-person listener; here the reported content, not the frame
  · **edges:** ["M19"] —REPORTS→ M20

**M21** — Lotus-leaves part as a fishing-boat passes among them.
  · agent: the lotus-leaves · operation: yield · substrate: the passing fisher-boat · outcome: cleared way through the water for the boat · narrator: first-person eye reading a second sign of nearby human life

**M22** — The season of spring is no longer here.
  · agent: springtime · operation: depart · substrate: not-stated · outcome: the spring's absence in the present · narrator: first-person host stating a temporal fact

**M23** — The friend himself is present in this place.
  · agent: the friend · operation: be-present · substrate: here, with the speaker · outcome: the friend's presence in the scene · narrator: first-person host stating a fact about the guest

**M24** — The speaker dismisses the loss of spring as of no consequence, given the friend's presence.
  · agent: first-person speaker · operation: dismiss-as-inconsequential · substrate: the two states M22 and M23 held together · outcome: the seasonal loss set aside as trivial · narrator: first-person host putting a rhetorical question whose burden is a positive claim

**M25** — As before in poem 3, the speaker addresses the friend with the same intimate title of honor.
  · agent: first-person speaker · operation: address-with-title · substrate: the friend present with him · outcome: the friend named 'Prince of Friends' at the close · narrator: first-person host addressing the guest directly
