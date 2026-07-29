# TEST-STEIN-GLAZED-GLITTER-1914 — background sheet

> Full coded transcript for **TEST-STEIN-GLAZED-GLITTER-1914** — read-only snapshot from the DB.

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
| TEST-STEIN-GLAZED-GLITTER-1914 | 20 | 0 | 0 | 0 |


## TEST-STEIN-GLAZED-GLITTER-1914

### Sitz — situational conditions (source_grounding)

- **summary:** This is Gertrude Stein's 'Glazed Glitter,' the opening piece of Tender Buttons (1914), and its conditions are squarely those of pre-war Anglo-European modernism. The MUMFORD-NEOTECHNIC substrate (electricity + new industrial materials ~1900) directly grounds the poem's object-world — 'nickel' is the neotechnic metal par excellence (electroplating, cutlery, coinage, hygienic surfaces), and 'clean and cleansing / glittering... handsome and convincing' is the neotechnic bourgeois-hygiene aesthetic Mumford diagnoses; DIS-ELECTRICITY underwrites the same substrate. FIG-NIETZSCHE-1886 and DEM-FIN-DE-SIECLE-VIENNA bear on the de-centred grammar ('Nickel, what is nickel, it is originally rid of a cover') and on the psychoanalytic-adjacent vocabulary of 'hope and... interpretation,' 'no search,' 'breakages,' 'obligation' — Stein trained under William James and shared psychoanalysis's dazzling-surface / repressed-interior milieu. MODEL-KNOWLEDGE: Parisian Cubism (Picasso/Braque 1907-14, Stein's rue de Fleurus salon) is the immediate stylistic sitz — cubist still-life transposed to prose; MODEL-KNOWLEDGE: Japonisme / late-Victorian consumer-goods culture ('breakages in Japanese,' porcelain, polishing) is the material referent; MODEL-KNOWLEDGE: 1914 as the eve of WWI hovers around 'the change has come.'
- **categories:** ["science_technology", "communication_media", "economic_material", "demographic_social"]
- **layers:** ["cultural_intellectual", "ecological_material_geographical", "personal_biography"]

### Paradigm — the scripts the text thinks with (+ its stance toward each)

_(none coded)_

### Frame — the 8-axis morphospace coordinate

_(none coded)_

### Coded moves — each with the context it picked up

**M1** — The teller puts the question of what nickel is on the table.
  · agent: narrator · operation: ask · substrate: nickel · outcome: an open question about nickel · narrator: an unnamed teller, first-person meditative, warrants the question by posing it

**M2** — The teller answers by attributing to nickel an original condition of being stripped of a cover.
  · agent: not-stated · operation: be (originally rid of a cover) · substrate: nickel · outcome: nickel characterized as originally uncovered · narrator: same teller, warranting by assertion

**M3** — The teller identifies what the change in that condition consists of.
  · agent: not-stated · operation: identify (the change is X) · substrate: the change in that · outcome: the change equated with an embedded happening · narrator: same teller, warranting by equative assertion
  · **edges:** M3 —REPORTS→ M4

**M4** — Red weakens an hour.
  · agent: red · operation: weaken · substrate: an hour · outcome: the hour rendered weaker · narrator: same teller, reporting the content of the change
  · **edges:** ["M3"] —REPORTS→ M4

**M5** — The change has arrived.
  · agent: the change · operation: come · substrate: not-stated · outcome: the change now present · narrator: same teller, warranting the arrival by announcement

**M6** — The teller denies that any searching is happening.
  · agent: not-stated · operation: exist (negated) · substrate: search · outcome: no search on the scene · narrator: same teller, warranting by direct denial

**M7** — The teller asserts, against that denial, that hope and interpretation are present.
  · agent: not-stated · operation: exist (asserted, adversative) · substrate: that hope and that interpretation · outcome: hope and interpretation posited as present · narrator: same teller, warranting by insistent 'there is, there is'

**M8** — The teller judges that, at times, anything at all is unwelcome.
  · agent: not-stated · operation: deem unwelcome · substrate: any (anything whatever), sometime · outcome: 'any' rated as unwelcome · narrator: same teller, warranting by 'surely'

**M9** — The teller asserts that at times breath is present.
  · agent: not-stated · operation: exist (asserted, temporal) · substrate: breath, sometime · outcome: breath posited as intermittently present · narrator: same teller

**M10** — The teller predicts a sinecure will come to exist.
  · agent: not-stated · operation: exist (future) · substrate: a sinecure · outcome: a sinecure projected into future presence · narrator: same teller, warranting by future assertion

**M11** — The teller judges the clean-and-cleansing thing very charming.
  · agent: not-stated · operation: deem charming · substrate: that clean and cleansing · outcome: the clean/cleansing thing rated highly charming · narrator: same teller, warranting by emphatic repetition ('charming, very charming')

**M12** — The teller judges glittering itself handsome and convincing.
  · agent: not-stated · operation: deem handsome and convincing · substrate: glittering · outcome: glittering rated handsome and persuasive · narrator: same teller, warranting by 'certainly'

**M13** — The teller denies that any gratitude lives inside mercy or medicine.
  · agent: not-stated · operation: exist (negated, located-in) · substrate: gratitude, located in mercy and in medicine · outcome: gratitude ruled absent from those two domains · narrator: same teller, warranting by direct denial

**M14** — The teller allows the possibility of breakages in Japanese things.
  · agent: not-stated · operation: exist (possible) · substrate: breakages, in Japanese (ware) · outcome: breakages granted as possible in that domain · narrator: same teller, warranting by modal 'can'

**M15** — The teller denies that that is any programme.
  · agent: not-stated · operation: identify (negated) · substrate: that (the foregoing) · outcome: 'that' ruled out as a programme · narrator: same teller, warranting by flat denial

**M16** — The teller denies that that is a chosen color either.
  · agent: not-stated · operation: identify (negated) · substrate: that (the foregoing) · outcome: 'that' ruled out as a chosen color · narrator: same teller

**M17** — It was in fact chosen the day before.
  · agent: not-stated · operation: choose · substrate: it (the color/thing) · outcome: the thing standing as chosen, dated to yesterday · narrator: same teller, warranting the past act

**M18** — That choosing disclosed spitting and, perhaps, washing and polishing.
  · agent: that (the choosing) · operation: show / disclose · substrate: a set of cleaning-like activities: spitting, washing, polishing · outcome: those activities made visible through the choice · narrator: same teller, warranting the disclosure with a hedge ('perhaps')

**M19** — That same choosing disclosed no obligation whatever.
  · agent: that (the choosing) · operation: show / disclose (negated) · substrate: obligation · outcome: obligation registered as visibly absent · narrator: same teller, warranting by 'certainly'

**M20** — If borrowing is not the natural mode, then giving has some use — offered tentatively.
  · agent: not-stated · operation: posit conditional value · substrate: giving, conditioned on borrowing being unnatural · outcome: giving credited with some use in that case · narrator: same teller, warranting with 'perhaps'
