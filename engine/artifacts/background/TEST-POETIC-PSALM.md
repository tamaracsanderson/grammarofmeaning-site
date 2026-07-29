# TEST-POETIC-PSALM — background sheet

> Full coded transcript for **TEST-POETIC-PSALM** — read-only snapshot from the DB.

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
| TEST-POETIC-PSALM | 12 | 0 | 0 | 0 |


## TEST-POETIC-PSALM

### Sitz — situational conditions (source_grounding)

_(no Sitz grounding row)_

### Paradigm — the scripts the text thinks with (+ its stance toward each)

_(none coded)_

### Frame — the 8-axis morphospace coordinate

_(none coded)_

### Coded moves — each with the context it picked up

**M1** — The speaker resolves to raise his gaze toward the hills.
  · agent: I (the pilgrim-speaker) · operation: lift-up (eyes toward the hills) · substrate: mine eyes · outcome: the speaker's gaze is directed toward the hills · narrator: the pilgrim, speaking in the first person; teller as the one who is himself the agent

**M2** — The speaker raises the question of where his help originates.
  · agent: I (the pilgrim-speaker) · operation: ask / wonder (the origin of help) · substrate: the source of my help · outcome: the question of the source is opened — the QUD is placed on the table · narrator: the pilgrim, first person; teller warrants only his own asking, not yet any answer

**M3** — The speaker names the LORD, maker of heaven and earth, as the origin of his help.
  · agent: the LORD, maker of heaven and earth (the source, from which help issues) · operation: come-from / originate-with (source-attribution) · substrate: my help · outcome: help is located as originating with the LORD — the QUD is answered · narrator: the pilgrim, first person; the teller warrants a confessional claim about the source

**M4** — A responding voice tells the pilgrim that the LORD will not let his foot slip.
  · agent: He (the LORD, now as active keeper rather than as named source) · operation: suffer-not / not-allow (negated permit) · substrate: thy foot — its being moved / its slipping · outcome: thy foot is kept firm; the slipping is not permitted · narrator: a second voice addressing the pilgrim ('thee') — plausibly a priest, companion, or blessing-liturgist; the first-person 'my' of M1–M3 has given way to a second-person address

**M5** — The responding voice adds that the one who keeps thee will not doze.
  · agent: he that keepeth thee (the keeper-of-thee — the relative clause identifies which 'he') · operation: slumber (negated) · substrate: not-stated (the state under negation belongs to the agent himself) · outcome: the keeper's wakefulness is unbroken; the guard is not dropped · narrator: the same second voice addressing the pilgrim

**M6** — The responding voice calls the hearer's attention to what follows.
  · agent: the second voice (the speaker addressing the pilgrim) · operation: behold / call-to-attend · substrate: the hearer's attention · outcome: the hearer's attention is turned toward the strengthened claim (M7) · narrator: the same second voice
  · **edges:** M6 —REPORTS→ M7

**M7** — The keeper of Israel neither dozes nor sleeps.
  · agent: he that keepeth Israel (the keeper-of-Israel) · operation: slumber-and-sleep (negated, intensified) · substrate: not-stated (the state under negation belongs to the agent himself) · outcome: the keeper's vigilance over Israel is unbroken and total · narrator: the same second voice
  · **edges:** ["M6"] —REPORTS→ M7

**M8** — The responding voice identifies the LORD in the role of thy keeper.
  · agent: the LORD · operation: be / is (identity-predication in the role of keeper) · substrate: the LORD (self, as the entity being placed in a role) · outcome: the LORD is identified as thy keeper — the role-assignment is made explicit · narrator: the same second voice

**M9** — The responding voice identifies the LORD in the role of thy shade at thy right hand.
  · agent: the LORD · operation: be / is (identity-predication in the role of shade at the right hand) · substrate: the LORD (self, as the entity being placed in a role) · outcome: the LORD is identified as thy shade upon thy right hand — a distinct role from M8, adding shelter-and-companion imagery · narrator: the same second voice

**M10** — Neither the daytime sun nor the nighttime moon will strike thee.
  · agent: the sun by day, the moon by night — the day-and-night celestial totality (merism) · operation: smite (negated) · substrate: thee · outcome: thou art unstruck at all hours · narrator: the same second voice

**M11** — The LORD will guard thee from every evil — will guard thy very inmost self.
  · agent: the LORD · operation: preserve / guard · substrate: thee — and, specified more deeply, thy soul — against all evil · outcome: thou art guarded whole, outwardly against every evil and inwardly at the soul · narrator: the same second voice

**M12** — The LORD will guard thy every departure and every return, from now on and without end.
  · agent: the LORD · operation: preserve / guard · substrate: thy going out and thy coming in (merism for the whole of thy activity) · outcome: every departure and every return is kept, and the keeping runs from now on into a horizon without end · narrator: the same second voice — closing the liturgical exchange
