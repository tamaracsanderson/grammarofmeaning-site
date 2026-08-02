---
title: "Best practice — running a Clean-Room Triangulation (CRT) with a design brief (for future reading SBs)"
date: 2026-08-02
session: S157 (reading-SB), PI-asked ("the 3-CRT process is working — write it up as a best practice future reading SBs
  can use"). Builds on Decision 200 (Clean-Room Triangulation) — this is the OPERATIONAL playbook, not a new term.
status: BEST PRACTICE (reusable). Proven across 3 S157 instances: lineage-detector CRT, engineering-speed CRT, church-map CRT.
---

# What CRT is (Decision 200 — don't re-coin)
**Clean-Room Triangulation (CRT):** N *independent* parties (reviewers or builders) with **no contact**, each given the
**same** input, whose outputs you then reconcile. The independence is the whole value — divergence is signal, and a lone
reviewer ships plausible-but-wrong. (Contrast RESITUATE's *runs* = the same world re-perturbed N times; CRT's
*clean-rooms* = N different eyes on the same thing. Never conflate.) This doc = **how to run a CRT well for a BUILD or
REVIEW, using a design brief.**

# When to reach for a CRT (and when NOT)
**Use it when:**
- A **genuinely uncertain build** with multiple valid approaches (church-map: Overpass vs QLever vs planet-PBF; render:
  deck.gl vs MapLibre) — anchoring on the first design risks missing a better one.
- A **review where a single pass would miss things** (engineering-speed: 3 reviewers on the same hot-path code).
- A build where **you're the weak link** — you'd anchor on your own first instinct (§2.1 anti-pre-anchoring at the
  engineering level).

**Don't use it when:**
- The choice is an engineering detail you should just make (§6 — pick and proceed).
- It's a **methodology-consensus** question → that's a **5-LLM IRR** (§2.6), a different tool (see the distinction below).
- The task is mechanical/known — CRT's cost (3× agents) isn't earned.

# CRT vs IRR — the distinction (don't confuse)
| | **CRT** (Decision 200) | **IRR** (§2.6) |
|---|---|---|
| Question type | *build/design approach* — "how would you build this?" | *methodology truth* — "is this right?" |
| Parties | ~3 independent agents (builders/reviewers) | 5 LLM cohorts (judges) |
| Goal | **diverge** for coverage → synthesize the **hybrid** | **converge** on consensus (UNANIMOUS/MAJORITY) |
| Output | the hybrid best build | the reconciliation doc (the citable consensus) |
| Composes | CRT proposes → IRR can validate the proposal | IRR reconciliation can seed a CRT brief |

# The playbook — 5 steps
### 1. Write the design brief (the shared input — this is the craft)
The brief is the single most important artifact. Anatomy that worked (3/3 across S157):
- **Goal in ONE sentence.** ("A reusable, off-the-shelf-sourced global map of religious buildings, filterable by tradition.")
- **Scope: IN vs PARKED, explicit.** State what v1 covers AND what to *not* design for (church-map: temporal +
  satellite imagery PARKED). Prevents agents solving the wrong (bigger) problem.
- **The N specific sections each agent MUST address** — enumerate them (church-map: acquisition / storage / render /
  normalization / bias-visibility / reusability). This makes the three outputs *comparable* — they answer the same
  questions, so reconciliation is apples-to-apples. Without this, three essays on different aspects → no synthesis.
- **The anti-anchoring instruction, verbatim:** "You are ONE of three independent proposers. Do not converge on a
  standard answer — propose what YOU think is best. Divergence is the point."
- **§13 verify-tools clause:** "verify every tool/library you name actually exists — do not fabricate." (DR/LLM agents
  hallucinate library names; this catches it.)
- **Prior research, already grepped, handed to them** — so they don't re-find it (and so they know what's net-new).
- **What to return:** a single proposal covering all N sections + build-effort estimate + the single biggest risk +
  the ONE thing to prototype first + confidence-per-section.

### 2. Spawn N independent agents with the SAME brief (no cross-talk)
- N=3 is the sweet spot (enough for divergence, cheap enough to reconcile). Send them in ONE message so they run
  concurrently. Each gets the identical brief path.
- For a **review** (read-only): plain agents. For a **build** (mutates files): `isolation: worktree` so they hand back
  a branch, per §2.12.
- Do NOT let them see each other's work — the independence is the value.

### 3. Reconcile into Decision-39 buckets → the hybrid
- **UNANIMOUS (N/N):** the load-bearing agreements — adopt.
- **Divergences:** the signal. Two kinds: (a) a **reality-check** one agent found that others missed (church-map:
  1.6M-not-5M via taginfo — decisive, shrank the whole build); (b) a **trap** the majority caught in the minority's
  plan (lineage: reviewer B's "remove recycle_every=1" would re-introduce context contamination — A+C caught it). Both
  are exactly what a lone reviewer misses.
- Write the synthesis doc (the deliverable): buckets + the hybrid build + biggest risk + prototype-first.

### 4. Build the hybrid (you, or a delegated build SB)
- The hybrid is usually NOT any single proposal — it's the UNANIMOUS core + the best divergent insight (church-map:
  C's static-artifact architecture + B's denomination-sparsity-is-a-finding + A's QLever-probe).
- Start with the **prototype-first** step all agents converged on (the de-risk), then the full build.

### 5. Capture provenance
- The brief, the 3 raw outputs, the synthesis doc — all on disk (like an IRR's 3 artifacts). The synthesis is the
  deliverable; chat-only summaries die at session end (same discipline as §2.6).

# The three proven S157 instances (evidence it works)
- **Lineage-detector CRT** — 3 agents *built* independently; hybrid took the best of each; the trap (recycle_every=1)
  caught by 2/3.
- **Engineering-speed CRT** — 3 reviewers on the same hot-path; 3/3 converged on effort=low + max_tokens-is-dead; the
  trap (removing recycle_every=1) caught by 2/3.
- **Church-map CRT** — 3 *design proposals*; 3/3 converged on the architecture; the reality-check (1.6M) from 2/3
  shrank the build from "server-side tile API" to "one static file."

# The one-line rule
**When a build has more than one right answer and you'd anchor on your first instinct: write a tight, section-structured
design brief, hand it to three independent agents, and synthesize the hybrid from where they agree + where they diverge.**

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: reading-SB S157 2026-08-02, PI-asked to codify the 3-agent-CRT-with-design-brief pattern as a reusable
  best practice for future reading SBs. Builds on Decision 200 (Clean-Room Triangulation) — operational playbook, not a
  new term. Distilled from 3 proven S157 instances (lineage / engineering-speed / church-map CRTs).
SCHOLARLY SOURCES: Decision 200 (CRT = Clean-Room Triangulation; MASTER_LEXICON); §2.6 (IRR — the sister pattern, the
  distinction table); §2.1 (anti-anchoring — the epistemic root); §2.12 (worktree isolation for build agents); §2.15
  (input→black-box→output — the brief's section structure); §13 (verify-tools clause; divergence-as-ghost-protection);
  the 3 S157 synthesis docs (church_map_CRT_synthesis, engineering_crt_engine_speed_synthesis, the lineage CRT).
WHAT NEEDS VERIFICATION: N=3 is the tested size (N=5 untested here — likely over-cost for most builds); the brief's
  section-structure is the load-bearing craft (a brief without enumerated comparable sections yields non-synthesizable
  outputs); CRT is for build/design, IRR for methodology-truth — mixing them is the misuse to watch for. -->
