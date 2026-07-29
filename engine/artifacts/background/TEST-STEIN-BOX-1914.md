# TEST-STEIN-BOX-1914 — background sheet

> Full coded transcript for **TEST-STEIN-BOX-1914** — read-only snapshot from the DB.

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
| TEST-STEIN-BOX-1914 | 10 | 0 | 0 | 0 |


## TEST-STEIN-BOX-1914

### Sitz — situational conditions (source_grounding)

- **summary:** This is Gertrude Stein's 'A Substance in a Cushion' from Tender Buttons (1914), a paradigmatic modernist prose-poem whose parataxis, referential slippage, and refusal of syntactic subordination emerge from the same fin-de-siècle Vienna/Paris intellectual climate that produced psychoanalysis's decentering of the Cartesian subject [DEM-FIN-DE-SIECLE-VIENNA, FIG-NIETZSCHE-1886]. Its style rhymes with the neotechnic sensorium [MUMFORD-NEOTECHNIC, DIS-ELECTRICITY] in which continuous perception is broken into discrete simultaneous fragments. Materially relevant conditions absent from the list: MODEL-KNOWLEDGE: Cubism (Picasso/Braque 1907-1914, Stein's Paris salon at 27 rue de Fleurus), MODEL-KNOWLEDGE: Bergson's durée and the crisis of representation, and MODEL-KNOWLEDGE: the imminent outbreak of WWI (July-August 1914) which frames the volume's June 1914 publication.
- **categories:** ["communication_media", "science_technology", "demographic_social", "cultural_intellectual"]
- **layers:** ["cultural_intellectual", "personal_biography"]

### Paradigm — the scripts the text thinks with (+ its stance toward each)

_(none coded)_

### Frame — the 8-axis morphospace coordinate

_(none coded)_

### Coded moves — each with the context it picked up

**M1** — Something warm-hearted issues in something red.
  · agent: kindness · operation: come-out-of · substrate: kindness · outcome: redness · narrator: anonymous meditative voice contemplating an object, no named teller, no cited authority

**M2** — Something abrasive issues in a fast repeat of the same question.
  · agent: rudeness · operation: come-out-of · substrate: rudeness · outcome: rapid same question · narrator: same anonymous meditative voice

**M3** — An organ of looking issues in inquiry.
  · agent: an eye · operation: come-out-of · substrate: an eye · outcome: research · narrator: same anonymous meditative voice

**M4** — The act of choosing among things issues in livestock that hurt.
  · agent: selection · operation: come-out-of · substrate: selection · outcome: painful cattle · narrator: same anonymous meditative voice

**M5** — The teller draws a summary — the arrangement of things, she declares, is the following proposition (M6).
  · agent: the teller · operation: declare-the-order · substrate: the arrangement just observed · outcome: the proposition stated in M6 · narrator: same meditative voice, now stepping back to summarise ('so then the order is that...')
  · **edges:** M5 —REPORTS→ M6

**M6** — A round white manner of being calls a small pointed fastener to mind.
  · agent: a white way of being round · operation: suggest · substrate: a white way of being round · outcome: something suggesting a pin · narrator: same meditative voice, now inside the declared order
  · **edges:** ["M5"] —REPORTS→ M6

**M7** — The teller puts to herself the question whether this round-white-pin thing lets one down.
  · agent: the teller · operation: ask · substrate: the white-round-thing of M6 · outcome: a question about whether it disappoints · narrator: same meditative voice, now interrogative

**M8** — She answers her own question with a plain no.
  · agent: the teller · operation: deny · substrate: the question posed in M7 · outcome: a negation — it does not disappoint · narrator: same meditative voice, now answering

**M9** — She judges that examining it is elementary enough to let a delicate stuff be seen in an odd light.
  · agent: the teller · operation: deem · substrate: the act of analysing the thing · outcome: a fine substance seen strangely · narrator: same meditative voice, now evaluative

**M10** — She judges too that holding a green tip is a serious matter — its work is not to reach red but to keep on pointing.
  · agent: the teller · operation: deem · substrate: having a green point · outcome: to point again (rather than to arrive at red) · narrator: same meditative voice, closing evaluation
