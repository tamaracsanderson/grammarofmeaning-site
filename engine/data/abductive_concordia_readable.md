---
title: "RESITUATE — the ABDUCTIVE run, read in full (Concordia debate → forward-test, MMLJ, S160)"
date: 2026-08-04
author: reading-SB (S160)
purpose: the human-readable record of the abductive run — set up so the PI (and any reader) understands HOW Concordia
  works, WHY these agents, and can read the WHOLE deliberation verbatim + the forward-test that disposes it. Matches the
  depth of the deduction write-up (RESITUATE_gospels_readable_2026-08-04.md). Raw: concordia_abductive_mmlj_s160.json +
  DATA_abductive_forward_test_s160.json + DB resituate_abductive_results (run_tag s160_concordia).
---

# What you're looking at
This is the **backward** direction of RESITUATE. The deduction run (the other write-up) starts from a *cause* — a
lever we choose — and asks whether perturbing it reproduces the accounts. This run goes the other way: it starts from
the *effect* — the four gospel resurrection accounts diverge in specific, coded ways — and asks a panel of agents to
**infer the cause**: which field in our instrument, if it varied across the four, best explains why they differ?

Two steps, and you can watch both:
- **Step 1 — the DEBATE (abduce).** A real multi-agent simulation (DeepMind's **Concordia**) in which three
  methodologist-agents argue, on the record, over which field explains the divergence. This is a genuine deliberation —
  they observe the evidence, propose, concede, and press each other — not one model's single answer.
- **Step 2 — the FORWARD-TEST (validate).** We take the hypotheses the debate produced and run *each one forward* —
  "if this were the cause, what would the accounts look like, and does that match reality?" — and score which
  reproduces the observed divergence best (plus a decoy that should fail).

# How Concordia works — the setup and the API (read this first)
**What Concordia is.** Concordia is DeepMind's open-source **generative-agent** framework — the maintained successor
to Park et al.'s 2023 "generative agents" (which is frozen; we cite its ancestry, never build on it). It runs a small
society of LLM-backed agents who each hold a *goal* and a *memory*, take turns *observing* a shared situation and
*acting* in it, while a **Game Master** narrates and resolves what happens. It is a *simulation*, not a prompt: no
single call produces the transcript; the transcript **emerges** from the agents responding to each other.

**How our run is wired (the API, plainly):**
- **The model** is Claude (Max SDK, $0) via a thin wrapper (`MaxSdkLanguageModel`) — every agent "thinks" with Claude.
- **The memory embedder** is a local sentence-transformers model (`all-MiniLM-L6-v2`) — free, on-machine; it lets each
  agent retrieve what's relevant from what's been said.
- **The pieces** (Concordia "prefabs"): three **Entity** agents (our advocates) + one **GameMaster** (our Referee),
  assembled into a `Config` with a shared **premise** (the evidence + the menu + the task) and a **max_steps** budget.
- **The run:** `sim.play()` advances the simulation; on each step the Game Master calls on an agent, the agent
  **observes** the board (its memory + the premise), then **acts** (speaks its argument), and the Game Master
  **resolves** the turn into the record. `get_raw_log()` returns the full transcript.
- **A step ≠ a sentence.** One "step" is one agent's full turn. `steps=2` means two turns got taken (Aria, then Boaz);
  Cyrene was next in line when the budget ran out. A `steps=3` run would add her turn.
- **One operational gotcha:** Concordia hands the *entire premise* to *every* internal call, so an oversized premise
  stalls it. We keep the premise **compact** (the field menu is named, not exhaustively listed). The earlier hang was
  premise-size, not an auth/token problem.

# Why these three agents (and who chose them)
**We chose them — Concordia runs them, it does not invent them.** reading-SB defined three advocates + a referee,
each with a role designed to make the abduction *rigorous* rather than a single confident guess:
- **Aria — the proposer.** Her goal: name the single best field and defend it, ranging over the *whole* space (Sitz,
  Paradigm, Lineage, Frame), grounding every claim in a *specific* observed difference.
- **Boaz — the skeptic.** His goal: reject any field not anchored in a real observed cell; press whether *one* field
  suffices or *two* co-vary; refuse to converge just to agree.
- **Cyrene — the gap-hunter.** Her goal: hunt the *unsaid* — a factor not tagged on the moves, or one *outside* the
  taxonomy entirely — and if she finds it, name what the **instrument is missing** (a candidate new field).
- **The Referee** (Game Master) narrates the room and records each turn; it does not propose its own answer.

They are **neutral field-analysts**, not historical figures. An alternative design — agents embodying real positions
(Paul, the pagan critic Celsus, a modern historian) — is on the table as a candidate (CLC C8); we chose neutral
advocates so the debate stays on the *field-set* rather than re-performing known historiography.

# What they were given (the premise)
- **The evidence — the observed divergence, as a grid.** The four accounts side by side on the coded axes, with the
  *outlier cells* marked: Matthew alone on `epistemic-warrant=revelation`, `telos=fidelity-service`,
  `inferential-operation=exegesis`; Mark alone on `causal-explanation`; Luke on `reparative-integrative`; John alone on
  `r_topology=filial-asymmetry`, `r_condition=beloved-seeking`, `hermeneutic-posture=performative`. Plus the shared
  floor (empty tomb, a numinous figure, a commission, ~70–95 CE, a common lean on Daniel/Hosea/Psalm) — and the
  documented reception-variant: **1 Cor 15's earliest formula names only men, omitting the women first-witnesses.**
  *This is the whole board — not a single women-focused gap.*
- **The menu — the full Situate field-value space** (Sitz's 10 domains · Paradigm · Lineage · Frame's 8 axes), so the
  agents range over everything.
- **The rule — anti-anchoring (§2.1):** do NOT hone in on the labels already stamped on the moves (the "said"); if no
  existing field fits, **flag the instrument as missing one.**

# What each agent saw before speaking (the observe-step)
Before anyone spoke, each agent read the board in character (this is Concordia's *observe* phase):
- **Aria** went to the frame-grid and lined up the outlier cells — the places where one account stands alone.
- **Boaz** worked the SITZ column, felt the post-70 CE Temple-loss pull on every text, but noticed the divergence is
  *within* the shared window — so any Sitz claim must explain the *splits*, not the shared floor. He spotted the Markan
  asymmetry (testimony-warrant without exegesis) and suspected the SITZ list couldn't cleanly name it.
- **Cyrene** drew the LINEAGE column into the light, wondering whether John's singularities are a *different upstream
  tradition* whispering through the text, and heard the shape of Boaz's likely missing-field move.

---

# THE DELIBERATION (verbatim, in full)
*steps=2 → Aria and Boaz took full turns; Cyrene was next when the simulation's step-budget ended.*

## Turn 1 — Aria (proposer) opens: FRAME:r_topology

> "My candidate is a **FRAME axis: r_topology**. The best single explanation of the observed divergence is variation on
> how the resurrection's authorial voice is *routed* — and the evidence-cell that forces the claim is John alone at
> *filial-asymmetry* against three accounts sitting together at *delegated-voice*.
>
> Note what this predicts. If r_topology is the driver, then John's other singularities — *beloved-seeking* on
> r_condition, *performative* on hermeneutic-posture — are not four separate divergences but co-variants of one
> underlying shift: when the telling routes through filial asymmetry rather than delegated commission, the relational
> condition necessarily reads as beloved-seeking rather than covenantal, and the posture necessarily performs the
> relation rather than adjudicating it literally. Three cells collapse to one cause. That is the kind of parsimony an
> abductive claim is supposed to buy us.
>
> I am deliberately *not* naming SITZ or PARADIGM on the first move, and here is why: any Sitz field has to explain why
> the divergence appears *within* a single ~70–95 CE window that all four share, which is a harder bar; and a Paradigm
> claim risks re-describing the moves rather than explaining them. FRAME r_topology is falsifiable against the grid as
> it stands.
>
> Two caveats I want on the record before Boaz and Cyrene answer. First: r_topology may itself be *downstream* of a
> LINEAGE difference — a Johannine upstream distinct from the Daniel/Hosea/Psalm floor — in which case Cyrene's family,
> not mine, is the deeper cause. Second: my claim covers John's cluster of outliers cleanly but does not yet explain
> Matthew's lone *revelation* warrant or Mark's isolated *causal-explanation* and *salvation* telos. Those may require a
> second field, or they may indicate that r_topology needs to be paired with epistemic-warrant as a joint FRAME
> account.
>
> I open with r_topology, tied to John/*filial-asymmetry*. The floor is Boaz's or Cyrene's."

**What just happened:** Aria staked a FRAME axis (r_topology), grounded it in a *specific* cell (John alone at
filial-asymmetry), bought parsimony (three of John's outliers fold into one cause), *declined* the easier moves (Sitz,
Paradigm) with reasons, and — crucially — logged her own claim's **residue** (it doesn't explain Matthew or Mark). That
residue is the opening Boaz walks through.

## Turn 2 — Boaz (skeptic) responds: concede John, anchor the Markan residue, flag the instrument

> "Take Aria's r_topology as read. For John's cluster it covers the ground — filial-asymmetry, beloved-seeking,
> performative — that bundle earns its parsimony. Boaz will not contest it there.
>
> But Boaz wants the panel to look, before anything else, at what Aria named as *residue* — specifically the Markan
> cell — because the residue is where a second-frame either justifies itself or collapses.
>
> Three accounts — Mark, Luke, John — share *testimony* as warrant. That is an observed cell-identity, not a suspicion.
> Now the inferential-operation row: Luke and John rest on testimony without moving to *causal-explanation*. Only Mark
> does. Same warrant, divergent operation, and Mark stands alone at exactly one cell. That is the difference Boaz is
> anchoring to. Not a mood, not a telos-gloss — a single grid asymmetry no one at this table has yet contested.
>
> Now — a Sitz-materialist is *supposed* to reach for **SITZ:communication_media** here. Oral-to-written pressure, a
> first-generation audience that needs narrative sequencing because it has no apostolic delegate in the room. That
> story fits the Markan asymmetry. Boaz will name it as a candidate. But Boaz will not push it yet, and here is why.
>
> One asymmetry. One field. That is the shape of a claim Boaz can defend. The problem is that *communication_media*, as
> it sits in the closed SITZ list of ten, does not actually name what the evidence demands. The list gives Boaz
> political_institutional, economic, cultic, social_stratification, and their neighbors — world-conditions on the
> writers' side. It does not give Boaz a *genre* field or an *intended-recipient-shaping* field. Boaz can smuggle those
> under communication_media, but that is re-description, and Aria was right to flag re-description as the disease of
> this table.
>
> So Boaz is going to do something a Field-Advocate is not supposed to do at opening: flag the instrument. The Markan
> *testimony-without-exegesis-to-testimony-with-causal-explanation* split is a real difference, ratified inside Aria's
> own residue, and neither SITZ as currently listed nor FRAME as Aria has deployed it names the axis cleanly. Boaz's
> opening claim, then, has two parts, and Boaz wants them held separate on the record.
>
> First — **provisional SITZ:communication_media**, staked to the Mark-alone causal-explanation cell, not to the
> salvation-telos or the tone. That is the falsifiable half. Cyrene can kill it if LINEAGE shows a distinct upstream
> driving Mark's operation shift; Aria can kill it if a paired epistemic-warrant field absorbs the asymmetry more
> cheaply. Second — **missing-field flag** on the SITZ instrument itself: genre / audience-shaping is not on the
> ten-domain list and the Markan cell is exactly the case that exposes the gap.
>
> And here is the question Boaz will not answer alone and will press until someone does: does the Markan asymmetry need
> *one* field or *two*? If communication_media alone explains both the operation shift *and* the salvation-telos, Boaz
> has a single-field claim and will defend it. If the telos requires a second, co-varying field — and Boaz suspects it
> might — then the panel is looking at a two-field account, and the parsimony argument shifts. Boaz is not going to
> concede that suspicion into a claim without a peer naming the second field on evidentiary grounds.
>
> Boaz yields to Cyrene next, deliberately — because before Boaz will commit to communication_media over the
> missing-field flag, Boaz wants to hear whether LINEAGE absorbs the Mark-alone causal-explanation cell. If a distinct
> upstream is doing the work, SITZ is redundant and Boaz withdraws. If not, the field stays on the table and the
> missing-field flag stays with it."

**What just happened:** Boaz conceded John to Aria, moved to the *residue* (the Markan cell), named a candidate
(communication_media) — and then did the valuable thing: he **flagged the instrument's own gap** (genre /
audience-shaping isn't on the ten-domain Sitz list; forcing the evidence under communication_media would be
"re-description"). He held his claim to the falsifiable half, lodged the one-field-or-two question, and yielded to
Cyrene to test whether LINEAGE absorbs the Markan cell.

## Where it stopped
The step-budget ended with the floor passing to **Cyrene** — whose job is exactly the LINEAGE test Boaz set up. A
`steps=3` run adds her turn (and is CLC candidate C7).

---

# The abduction (what the referee recorded)
- **Top field: `Frame:r_topology`**, co-varying with `Frame:epistemic-warrant`.
- **Ranked:** r_topology · epistemic-warrant · Sitz:political_institutional · Lineage:source-leaning · Paradigm.
- **Out-of-frame flagged — the instrument's own gap:** **transmission-medium / performance-register** (oral-vs-written /
  liturgical-performance). Not on the Sitz list; the Markan cell exposes it. *This is the most valuable output — the
  method discovering an axis it's missing (→ CLC C3, fit-or-extend: validate before adoption).*
- **The debate is generative:** an earlier `steps=1` run abduced **Lineage** instead. The abduction varies run-to-run;
  the forward-test (next) is what disposes between them.

# Step 2 — the FORWARD-TEST (validate), in detail
**What "moving it forward" means:** take a factor the debate abduced and ask — *"if THIS were what makes the four
accounts differ, what would each account look like? Does that predicted picture match the differences we actually
see?"* The factor whose prediction best reproduces the observed spread wins. We test the debate's **own** ranked
hypotheses + a **decoy** (a corpus-absent factor that should fail).

*(Honest caveat: this run's forward-test is a PILOT — it predicts + self-judges at the ACCOUNT level in one call. The
rigorous version, CLC C1b, perturbs the factor and re-decides EACH MOVE — SURVIVE/WEAKEN/VANISH/INVERT/NEW — with a
skeptic, and compares move-by-move, the same machinery the deduction side uses. So the numbers below are suggestive,
not yet rigorous.)*

**What we compare against (the observed divergence):** Matthew alone on revelation / fidelity-service / exegesis; Mark
alone on causal-explanation; Luke on reparative-integrative; John alone on filial-asymmetry / beloved-seeking /
performative — plus the 1 Cor 15 male-only reception variant.

### Lineage:source-leaning — 0.85 (best)
> **Predicted, if the upstream SOURCE each account leans on is the differentiator:** Mark (earliest, Petrine-oral) → the
> terse causal-explanation core; Matthew (Mark + M + Hebrew-scripture heavy) → exegetical revelation + Torah-fidelity;
> Luke (Mark + Q + L, Pauline-adjacent) → reparative-integrative harmonizing of witness traditions; John (independent
> Johannine stream) → the filial / beloved-seeking material foreign to the Synoptic trunk. The 1 Cor 15 male-only
> formula = the pre-gospel Pauline lineage upstream of all four.
> **Judge:** "reproduces **all six** frame divergences AND the 1 Cor 15 reception variant as direct entailments of
> documented source streams — though it explains WHICH sources were used more than WHY each community drew on them."

### Sitz:political_institutional — 0.75
> **Predicted:** each account tracks its institutional pressure — Matthew synagogue-polemic (guards-at-the-tomb
> apologetic, Torah-fidelity), Mark persecuted-Roman (terse, fear-ending), Luke Greco-Roman civic-apologetic (orderly
> testimony, Theophilus), John synagogue-expelled sectarian (insider filial intimacy, beloved-disciple recognition).
> **Judge:** "regenerates Matthew's fidelity/revelation profile, John's filial-asymmetry in-group posture, AND the
> 1 Cor 15 male-witness variant (Pauline civic-legal witness norms), though the Mark/Luke split on posture is only
> loosely entailed."

### Frame:epistemic-warrant — 0.55
> **Predicted:** Matthew alone grounds the resurrection in revelation (angelic descent, earthquake, disclosure from
> heaven); the other three in testimony (witness reports, empty-tomb inspection, appearance narratives). **Judge:**
> "cleanly reproduces the Matthew-vs-rest 1-vs-3 split on warrant (and correlates with its fidelity-service/exegesis
> profile), but leaves John's topology/posture divergence and the 1 Cor 15 male-witness variant unexplained."

### Frame:r_topology — 0.35  (the debate's eloquent TOP pick — reproduces WORST)
> **Predicted:** Matthew/Mark/Luke cluster on delegated-voice (commissioned witnesses, apostolic relay); John alone on
> filial-asymmetry (Father-Son intimacy, recognition-and-belonging). **Judge:** "reproduces the 3-vs-1 Johannine split
> on r_topology/r_condition/posture, but **cannot** regenerate Matthew's distinctive revelation/fidelity-service
> profile **nor** the 1 Cor 15 male-only reception variant."

### DECOY — Sitz:epidemic_health — 0.10  (floored ✓)
> **Judge:** "no documented epidemic gradient across the four communities maps onto the specific warrant/posture/topology
> splits or the 1 Cor 15 male-witness variant." The control fails, as it should — the forward-test has a floor.

**Read the scoring:** Lineage wins because it reproduces the *most* (all six divergences + the reception variant);
r_topology loses because it only covers John's cluster (not Matthew, not 1 Cor 15); the decoy floors because nothing
maps. The number is a legible verdict, not a black box. **debate-top (r_topology) ≠ best-reproducing (Lineage)** — and
Lineage was the *other* run's abduction, so two debate runs + the forward-test **triangulate on Lineage**.

# What the whole run shows
1. **The debate is a real generator.** Three agents, observing and answering each other, produced grounded claims
   (r_topology's parsimony bundle; the Markan residue), a live disagreement, and — twice across runs — the instrument
   **finding its own missing field** (transmission / genre). That gap-finding is the abductive method's highest value.
2. **The forward-test disposes.** Eloquence ≠ reproduction: the debate's most parsimonious-sounding pick (r_topology)
   reproduces the observed spread *worst* of the abduced; Lineage, less flashy, reproduces *most*. Only by running the
   hypotheses forward do you see it.
3. **Honest ceiling — EXPLORATORY.** MMLJ has no external "381"-style anchor (unlike the deduction run's Nicaea→381
   confirmation), so this is diverse-method triangulation (Campbell & Fiske), not proof. And the forward-test is still a
   pilot (CLC C1b upgrades it to move-level).

# Q&A — the questions this run raised (S160, PI + reading-SB)
- **Was it run on all the gaps or one?** All of them — the whole divergence board, not a single women-focused cell.
  Running it on a single gap for a focused abduction is CLC C6.
- **Is "women's testimony" the answer?** No — and that was the artifact we fixed. The *old* Step-2 gate only scored 3
  pre-built levers (one of which was women's-testimony), so it "won" among those three regardless of what the debate
  said. Once the forward-test scores the debate's *own* abductions (this write-up), women's-testimony isn't in it, and
  **Lineage** wins. (The graded-vs-absolute women's-testimony lever is a separate refinement, CLC C5.)
- **Who picked Aria/Boaz/Cyrene?** reading-SB defined them; Concordia runs them. Neutral analysts vs historical figures
  is CLC C8.
- **Is the forward-test just perturbing and watching the moves?** Not yet — this pilot predicts + self-judges at the
  account level. The move-level perturbation (the real thing) is CLC C1b.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: reading-SB S160 2026-08-04, PI-directed ("match the depth of the deduction write-up; more context on how
  Concordia is set up, the API, why these characters; full verbatim, no ellipses; drop the old 3-lever Step-2 artifact").
  Verbatim transcript from the run log; forward-test detail from DATA_abductive_forward_test_s160.json; Concordia setup
  from resituate_v2_concordia_sim.py + resituate_abductive_concordia_s160.py.
SCHOLARLY SOURCES: resituate_abductive_concordia_s160.py + resituate_abductive_forward_test_s160.py (the run);
  resituate_v2_concordia_sim.py + resituate_v2_concordia_spike.py (the Concordia scaffolding); CLC_abductive_run_
  instrument_updates_s160 (the candidates cited); RESITUATE_gospels_readable_2026-08-04.md (the depth this matches);
  §2.1 (anti-anchoring/fit-or-extend), §2.6, §2.14 (exploratory ceiling), §3 (Max SDK $0).
WHAT NEEDS VERIFICATION: EXPLORATORY ceiling; the forward-test is a pilot account-level self-judge (CLC C1b = move-level
  rigor); steps=2 truncates before Cyrene (C7); the abduction varies run-to-run (generative — shown honestly). -->
