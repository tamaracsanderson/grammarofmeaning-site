# TEST-STEIN-COFFEE-1914 — background sheet

> Full coded transcript for **TEST-STEIN-COFFEE-1914** — read-only snapshot from the DB.

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
| TEST-STEIN-COFFEE-1914 | 32 | 6 | 14 | 12 |


## TEST-STEIN-COFFEE-1914

### Sitz — situational conditions (source_grounding)

- **summary:** This is Gertrude Stein's 'A Piece of Coffee' from Tender Buttons (1914), a still-life prose-poem written in Paris at the height of pre-WWI modernist experiment. The text's conditions rhyme most directly with MODEL-KNOWLEDGE: CUBISM-PARIS-1907-1914 (Picasso/Braque's analytic-then-synthetic cubism, which Stein collected and translated into prose) and MODEL-KNOWLEDGE: TENDER-BUTTONS-1914 (the book's own domestic-object program: Objects/Food/Rooms). The de-centred subject visible in [FIG-NIETZSCHE-1886]'s 'es denkt' and [DEM-FIN-DE-SIECLE-VIENNA]'s psychoanalytic milieu is the same intellectual weather that lets a piece of coffee be described without a describing 'I'; [MUMFORD-NEOTECHNIC] and [DIS-ELECTRICITY] name the material substrate (electric-lit interiors, mass-produced domestic goods — 'soap and silk,' 'rose-wood,' 'lining,' 'ribbon') that Stein is cataloguing.
- **categories:** ["cultural_intellectual", "communication_media", "science_technology", "economic_material", "demographic_social"]
- **layers:** ["personal_biography", "cultural_intellectual", "ecological_material_geographical"]

### Paradigm — the scripts the text thinks with (+ its stance toward each)

| paradigm | stance | salience |  | relation | evidence |
|---|---|---|---|---|---|
| cubist-analytic decomposition of a still-life object | endorsed | 0.9 | DOMINANT | self | 'A single image is not splendor' reads as a near-manifesto against single-viewpoint representation; the object (coffee/its 'piece') is refracted across color-facets ('yellow', 'coal color', 'whiter', 'rose-wood color'), tactile facets ('soap and silk', 'lining', 'ribbon', 'solid'), and negations ('not a detainer', 'not torn', 'not coal color'), the same procedure Picasso/Braque apply to a guitar or bottle on a table; the title-object frame ('A place in no new table') explicitly stages the still-life setup only to refuse its unified image. |
| domestic housekeeping / order-of-the-household | subverted | 0.75 |  | reinforces | The whole central paragraph runs on the housekeeping script — 'the settling of stationing cleaning', 'use soap and silk for cleaning', 'a lining and the shape of a ribbon', 'to be solid, quite solid in standing', 'to use heaviness in morning' — but the telos of the script (an ordered room, a clean object in its place) is denied: cleaning is redefined as 'one way not to shatter scatter and scattering', 'dirty' is folded into the object's identity ('The resemblance to yellow is dirtier and distincter'), and 'custom' is displaced onto soap-and-silk rather than onto conduct. |
| logical-propositional demonstration ('suppose … therefore necessary') | invoked | 0.6 |  | reinforces | 'Supposing that the case contained rose-wood and a color. Supposing that there was no reason for a distress … is it not necessary to mingle astonishment' mimes the syllogism / geometric-proof frame (premises → necessity), and 'the more certain is the necessity dwindled' explicitly hollows out the necessity-conclusion the frame promises. |
| aphoristic conduct-book / 'the one way is …' maxim | invoked | 0.55 |  | reinforces | 'The one way to use custom is to use soap and silk for cleaning. The one way to see cotton is to have a design concentrating the illusion and the illustration. The perfect way is to accustom the thing …' invokes the maxim-book / how-to script (a rule of right practice), but the rules govern seeing and accustoming rather than conduct, and the closing 'May not be strange in everything. May not be strange to.' refuses the closing epigrammatic snap. |
| riddle / hidden-referent disclosure | denied | 0.5 |  | competes | Title-frame ('A Piece of Coffee') sets up the riddle script — name the thing being described — and the text plays along ('A piece of coffee is not a detainer', 'not coal color, never more coal color than altogether') only to withhold the aha: no disclosure, no referent settles, the color-set (yellow, rose-wood, whiter) actively disperses the promised object. |
| sacramental/eucharistic disclosure ('a piece of X, a sign of more') | invoked | 0.25 |  | competes | 'A sign of more in not mentioned', 'A piece of coffee is not a detainer', and the recurrent 'more … more … splendor' faintly rhyme on the eucharistic paradigm (a piece stands for more; a sign carries a presence) — but the paradigm is only glancingly touched; it is not driving roles or sequence. |

### Frame — the 8-axis morphospace coordinate

| axis | value | rank | conf | evidence |
|---|---|---|---|---|
| epistemic-warrant | observation | 1 | 0.55 | 'A single image is not splendor. Dirty is yellow.' — grounds itself in perceptual/sensory report of surfaces, colors, objects (coffee, rose-wood, cotton, soap). |
| epistemic-warrant | embodied-practice | 2 | 0.45 | 'The one way to use custom is to use soap and silk for cleaning... to use heaviness in morning' — knowing through domestic handling and habitual use. |
| evaluative-stance | neutral-descriptive | 1 | 0.55 | Predicative flatness ('Dirty is yellow.' 'It has that shape nicely.') without praise or censure of the object. |
| evaluative-stance | tender | 2 | 0.35 | 'nicely,' 'sincerely,' 'flattering,' 'not strange' — a low-heat affection toward domestic surfaces (Tender Buttons register). |
| ground-world-relation | fitting-attunement | 1 | 0.45 | 'The perfect way is to accustom the thing to have a lining and the shape of a ribbon and to be solid… to use heaviness in morning. It is light enough in that. It has that shape nicely.' — right relation is a matter of fit, custom, and accommodation. |
| ground-world-relation | mutual-constitution | 2 | 0.4 | Objects, colors, and qualities co-define one another ('dirtier and distincter,' 'whiter and not coal color') — no ground stands apart from the field it conditions. |
| hermeneutic-posture | performative | 1 | 0.75 | The text does not describe an object so much as enact it through rhythm, repetition, and near-syntax ('May be strangely flattering. May not be strange in everything. May not be strange to.') — meaning is produced by the utterance. |
| hermeneutic-posture | reductive-deconstructive | 2 | 0.45 | Grammar, reference, and predication are disassembled ('A place in no new table.'; 'the intention to wishing, the same splendor, the same furniture') — a taking-apart of ordinary sense. |
| inferential-operation | analogical-mapping | 1 | 0.55 | 'The resemblance to yellow…', 'the same sight slighter, the sight of a simpler negative answer, the same sore sounder' — reasoning by resemblance-chains and sonic/semantic parallelism. |
| inferential-operation | dialectical-negation | 2 | 0.5 | 'not a detainer', 'never more coal color', 'not cheaper', 'not strange', 'no fewer' — advance by iterated negation and qualification. |
| ontological-commitment | material | 1 | 0.7 | Coffee, table, rose-wood, cotton, soap, silk, ribbon, furniture — the real is a field of things, colors, and textures with no appeal to a beyond. |
| ontological-commitment | relational | 2 | 0.5 | 'The resemblance to yellow is dirtier and distincter' — being is constituted in comparisons, resemblances, and differentials rather than substances. |
| telos | harmony | 1 | 0.45 | 'The settling of stationing cleaning is one way not to shatter scatter and scattering' — orientation toward composure, arrangement, non-scattering; 'It has that shape nicely.' |
| telos | agency-mastery | 2 | 0.4 | 'The one way to use custom is to…', 'The perfect way is to accustom the thing…' — a craft-poetics of the right way to handle, arrange, accustom. |

### Coded moves — each with the context it picked up

**M1** — The teller labels an unnamed something as being of a doubled kind — more, in the doubled register.
  · agent: not-stated · operation: predicate · substrate: an unnamed topic · outcome: characterized as 'more of double' · narrator: unnamed teller giving still-life predications in fragment form
  · **gaps:** *identity* — The topic receiving every predication, comparison, and care instruction is never named. All agents throughout the entire move sequence are marked not-stated, so the grammatical subject of the poem is structurally withheld from first move to last. (barred)

**M2** — The teller locates a place as sitting inside no fresh table.
  · agent: not-stated · operation: locate · substrate: a place · outcome: situated within no new table · narrator: unnamed teller giving still-life predications in fragment form

**M3** — The teller denies of a lone picture that it counts as splendor.
  · agent: not-stated · operation: predicate-negation · substrate: a single image · outcome: excluded from the category 'splendor' · narrator: unnamed teller giving still-life predications in fragment form

**M4** — The teller equates the dirty with the yellow.
  · agent: not-stated · operation: equate · substrate: the property 'dirty' · outcome: identified with 'yellow' · narrator: unnamed teller giving still-life predications in fragment form
  · **gaps:** *warrant* — Dirty is simply equated with yellow without any supplied ground — perceptual, cultural, or linguistic — that would explain why these two properties are interchangeable rather than merely co-occurring. (residual)

**M5** — The teller places a sign-of-more within what is not mentioned.
  · agent: not-stated · operation: locate · substrate: a sign of more · outcome: situated inside the not-mentioned · narrator: unnamed teller giving still-life predications in fragment form
  · **gaps:** *referent* — A sign of more is located inside what the text calls 'the not-mentioned.' What the not-mentioned is cannot be recovered from within the text by definition — the poem names its own silence as a spatial container. (barred)

**M6** — The teller denies that a portion of coffee is something that holds one back.
  · agent: not-stated · operation: predicate-negation · substrate: a piece of coffee · outcome: excluded from the category 'detainer' · narrator: unnamed teller giving still-life predications in fragment form

**M7** — The teller ranks the likeness-to-yellow as more soiled and more sharply set-off.
  · agent: not-stated · operation: compare · substrate: the resemblance to yellow · outcome: graded as dirtier and more distinct · narrator: unnamed teller giving still-life predications in fragment form

**M8** — The teller ranks the clean mixture as whiter, not coal-colored, and never more coal-colored than as a whole.
  · agent: not-stated · operation: compare · substrate: the clean mixture · outcome: graded as whiter, kept out of coal-color, and never exceeding its own overall coal-color · narrator: unnamed teller giving still-life predications in fragment form

**M9** — The teller sets out a series of parallel items — a reason's sight, that sight lessened, a simpler no's sight, the same sore made sounder, the leaning-toward-wishing, the same splendor, the same furnishings — as a juxtaposed inventory.
  · agent: not-stated · operation: enumerate · substrate: a series of parallel items (a sight-of-reason, its slighter twin, a sight-of-a-simpler-no, the same sore made sounder, an intention toward wishing, the same splendor, the same furniture) · outcome: presented as a juxtaposed inventory of same-and-slightly-different items · narrator: unnamed teller giving still-life predications in fragment form
  · **gaps:** *principle-of-assembly* — Seven items are placed in parallel inventory — a sight-of-reason, its slighter twin, a sight-of-a-simpler-no, the same sore made sounder, an intention toward wishing, the same splendor, the same furniture. What logic selects and joins these as a coherent set is never given: whether it is typological, associative, temporal, or purely sonic remains open. (residual)

**M10** — The teller says the right moment to deliver a message is at the point of too-late, and that afterward there is no lingering inside a withering.
  · agent: not-stated · operation: predicate · substrate: the time to show a message · outcome: identified with the moment of too-late, coupled with the absence of any lingering in a blight thereafter · narrator: unnamed teller giving still-life predications in fragment form
  · **gaps:** *reason* — The moment of showing a message is identified with too-late, paired with an absence of any lingering in a blight afterward. What has been missed, what the blight was, and why the moment of showing coincides with the moment of having-missed-it are all left open. (residual)

**M11** — The teller names an unnamed something as a rose-wood shade that has not been torn.
  · agent: not-stated · operation: predicate · substrate: an unnamed topic · outcome: characterized as a rose-wood color that is not torn · narrator: unnamed teller giving still-life predications in fragment form

**M12** — The teller conditions: if the thing carries no danger, then it counts as a pleasure — and more so than any other case.
  · agent: not-stated · operation: predicate-conditional · substrate: it (the topic) · outcome: under the condition of not-dangerous, ranked as a pleasure surpassing any other · narrator: unnamed teller giving still-life predications in fragment form
  · **gaps:** *warrant* — Under the single condition of being not-dangerous, the thing is ranked as a pleasure surpassing any other. Why danger is the pivotal threshold — what risk the object carries or once carried that makes its absence the ground for a superlative — is not supplied. (residual)

**M13** — The teller conditions: if the thing comes cheap, then it is not thereby made any cheaper.
  · agent: not-stated · operation: predicate-conditional · substrate: it (the topic), taken as cheap · outcome: denied any further reduction in cheapness · narrator: unnamed teller giving still-life predications in fragment form

**M14** — The teller predicates of the amusing side that as soon as no items are fewer, the dwindling of the necessity becomes the more certain.
  · agent: not-stated · operation: predicate · substrate: the amusing side (of the matter) · outcome: characterized by a scaling relation in which sooner-no-fewer yields more-certain-dwindled-necessity · narrator: unnamed teller giving still-life predications in fragment form
  · **gaps:** *subject-of-amusement* — The amusing side of the matter is characterized by a scaling relation but neither the subject who finds it amusing nor the specific object of the amusement — the thing itself, its cheapness, the logic of dwindled necessity, or some social situation — is identified. (residual)

**M15** — The teller performs a supposing — entertaining as a hypothesis the case referenced below.
  · agent: the teller (implicit supposer) · operation: suppose · substrate: the supposed proposition M6 · outcome: the proposition is entertained as hypothesis · narrator: unnamed teller giving still-life predications in fragment form
  · **gaps:** *reason* — Three earlier moves — M6, M8, and M10 — are re-entertained as hypotheses (in M15, M17, M19) while the other moves are not. What makes these three the candidates for hypothetical re-framing, and what the re-hypothesizing is meant to accomplish relative to the assertions that preceded them, is nowhere stated. (residual)
  · **edges:** M15 —REPORTS→ M16

**M16** — Inside the supposition: the container held rose-wood together with a color.
  · agent: not-stated · operation: contain · substrate: the case · outcome: held to include rose-wood and a color · narrator: unnamed teller giving still-life predications in fragment form
  · **edges:** ["M15"] —REPORTS→ M16

**M17** — The teller performs a further supposing — entertaining as a hypothesis the proposition below.
  · agent: the teller (implicit supposer) · operation: suppose · substrate: the supposed proposition M8 · outcome: the proposition is entertained as hypothesis · narrator: unnamed teller giving still-life predications in fragment form
  · **edges:** M17 —REPORTS→ M18

**M18** — Inside that supposition: there was no ground calling for distress, and the ground more likely called for a count.
  · agent: not-stated · operation: predicate-negation · substrate: reason (for distress vs. for a number) · outcome: no reason for distress; more likely a reason for a number · narrator: unnamed teller giving still-life predications in fragment form
  · **edges:** ["M17"] —REPORTS→ M18

**M19** — The teller performs a further supposing — entertaining as a hypothesis the proposition below.
  · agent: the teller (implicit supposer) · operation: suppose · substrate: the supposed proposition M10 · outcome: the proposition is entertained as hypothesis · narrator: unnamed teller giving still-life predications in fragment form
  · **edges:** M19 —REPORTS→ M20

**M20** — Inside that supposition: astonishment was absent.
  · agent: not-stated · operation: predicate-negation · substrate: astonishment · outcome: denied any presence · narrator: unnamed teller giving still-life predications in fragment form
  · **edges:** ["M19"] —REPORTS→ M20

**M21** — The teller poses as a rhetorical question whether, given those suppositions, one is not obliged to fold astonishment back in.
  · agent: the teller (posing the question) · operation: question-directive · substrate: the requirement to mingle astonishment (into the situation set up by the prior supposings) · outcome: put forward as a rhetorical necessity by way of a negatively phrased question · narrator: unnamed teller giving still-life predications in fragment form
  · **gaps:** *interior* — The teller is the most structurally present party — they suppose (M15, M17, M19), question (M21), and direct — but their own orientation toward the object is entirely absent. Whether they are amused, estranged, affectionate, or ironic can only be inferred from the speech acts; their felt relation to the thing is never given. (barred)

**M22** — The teller predicates that the settling-down of putting cleaning in its station is one way of avoiding shatter, scatter, and scattering.
  · agent: not-stated · operation: predicate · substrate: the settling of stationing cleaning · outcome: identified as one way not to shatter, scatter, and scattering · narrator: unnamed teller giving still-life predications in fragment form
  · **gaps:** *edge-gap* — A structural seam runs between the comparative-and-attributive half of the poem (color, dirtiness, resemblance, enumeration, temporality) and the procedural-care half (how to clean, hold, line, accustom the thing). No move bridges the two halves or explains why describing what the thing is gives way to instructing how to handle it. (residual); *mechanism* — The settling of stationing cleaning is identified as one way not to shatter, scatter, and scattering, but how the settling prevents those outcomes — the causal mechanism linking the action to the averted consequences — is unstated. (residual)

**M23** — The teller predicates that the single way to put custom to work is to employ soap and silk for cleaning.
  · agent: not-stated · operation: predicate · substrate: the one way to use custom · outcome: identified with the use of soap and silk for cleaning · narrator: unnamed teller giving still-life predications in fragment form

**M24** — The teller predicates that the single way to see cotton is to hold a design that draws the illusion and the illustration into one focus.
  · agent: not-stated · operation: predicate · substrate: the one way to see cotton · outcome: identified with holding a design that concentrates the illusion and the illustration · narrator: unnamed teller giving still-life predications in fragment form

**M25** — The teller predicates that the perfect way is to train the thing into a lining, a ribbon-shape, firm solidity in its standing, and the use of heaviness in the morning.
  · agent: not-stated · operation: predicate · substrate: the perfect way · outcome: identified with accustoming the thing to a lining, a ribbon-shape, being quite solid in standing, and using heaviness in morning · narrator: unnamed teller giving still-life predications in fragment form

**M26** — The teller predicates of the thing that in that respect its lightness suffices.
  · agent: not-stated · operation: predicate · substrate: it (the thing) · outcome: graded as light enough within that respect · narrator: unnamed teller giving still-life predications in fragment form

**M27** — The teller predicates of the thing that its holding of that shape is done nicely.
  · agent: not-stated · operation: predicate · substrate: it (the thing) · outcome: credited with holding that shape nicely · narrator: unnamed teller giving still-life predications in fragment form

**M28** — The teller predicates, in modal register, that a very-nicely quality may not amount to exaggeration.
  · agent: not-stated · operation: predicate-modal · substrate: very nicely (as a manner) · outcome: possibly not exaggerating · narrator: unnamed teller giving still-life predications in fragment form
  · **gaps:** *reason* — After the relatively assertive care instructions of M22–M27, a chain of five modal predicates (M28–M32) retrospectively hedges the same manner of acting with a string of 'possibly.' Why the poem withdraws into epistemic tentativeness at the close — whether from sonic necessity, tonal irony, or a genuine limit on knowledge about the object — is not given. (residual)

**M29** — The teller predicates, in modal register, that a very-strongly quality may be a case of sincere fainting.
  · agent: not-stated · operation: predicate-modal · substrate: very strongly (as a manner) · outcome: possibly a sincere fainting · narrator: unnamed teller giving still-life predications in fragment form

**M30** — The teller predicates, in modal register, that the same manner may amount to a strange kind of flattering.
  · agent: not-stated · operation: predicate-modal · substrate: the same manner (elided subject carrying from 'very strongly') · outcome: possibly a strangely flattering effect · narrator: unnamed teller giving still-life predications in fragment form

**M31** — The teller predicates, in modal register and via negation, that the same manner may fail to be strange with respect to everything.
  · agent: not-stated · operation: predicate-modal · substrate: the same manner (elided subject continuing) · outcome: possibly not strange across the whole range ('in everything') · narrator: unnamed teller giving still-life predications in fragment form

**M32** — The teller predicates, in a truncated modal register, that the same manner may fail to be strange toward something left unnamed.
  · agent: not-stated · operation: predicate-modal · substrate: the same manner (elided subject continuing) · outcome: possibly not strange with respect to an unnamed object of the preposition 'to' · narrator: unnamed teller giving still-life predications in fragment form
