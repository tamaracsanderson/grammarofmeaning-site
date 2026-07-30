---
title: "20-critic R&D crit rooms on the Smallville gaps — Panel A (theory) + Panel B (tech/innovation). The panel is a knob."
date: 2026-07-30
session: S156 (reading-SB)
status: Panel A (theory-leaning) DONE; Panel B (tech/innovation) running. The demo is the CONTRAST — same 8 instrument-found
  gaps, two panel compositions, what each surfaces. For Saquib.
---

# Why two panels
The Gloss engine (commentary-constellation) scaled to 20 seats, run on the instrument's own 8-gap find of Park et al.
"Generative Agents / Smallville" (2304.03442). PI's insight: the crit panel's COMPOSITION changes the critique — so we run
two: **Panel A = theory/academic** (psychometrician, philosopher-of-mind, anthropologist, STS…) and **Panel B =
tech/innovation** (research-engineer, founder-who-shipped, eval-engineer, MLOps, VC, game-AI…). The contrast IS the finding.

# PANEL A — theory-leaning (DONE)
**Convergence map:** G1 believability-confound **12/20** (modal) · G7 floor-effect **8/20** · G5 construct-validity **7/20**.
Mid-band: G4 constants 5 · G8 decomposition 4 · G6 min-max 4 · G2 timescale 4.
**The SLEEPER (minority signal):** **G3 (reflection-trigger N) — only 2 seats** (reproducibility + ML-systems). The
architecture's *control flow is un-reconstructable from the paper*, and only the two seats who'd actually re-run the code
noticed. A believability-focused reader never hits it.
**The sharpest divergence — the panel's true fault line:** Philosopher-of-mind ⟷ Product-founder on **G5**. Philosopher:
narrating a 1–10 poignancy score as what the agent "believes" is a *category error, fatal and prior to everything*. Founder:
construct validity is an academic luxury, *irrelevant* — only the deployment horizon (G2) matters. **The paper's core object
("importance" narrated as belief) is simultaneously the fatal flaw AND a non-issue depending on the seat — and the paper
never declares which discourse it's accountable to.**
**Same-gap-opposite-reason:** statistician (G7 baseline "too weak" → nearest-neighbor ablation) vs game-designer (G7 baseline
"wrong kind" → the real floor is a competent scripted NPC). A converging panel would have erased this as "G7: consensus."
**Safety inversion:** the "overly-cooperative/embellishment" confound everyone treats as *noise to partial out* is, to the
safety seat, *the actual finding* (sycophancy is a known failure mode the believability metric rewards).
**Panel A verdict:** *consensus on WHICH gap is not consensus on WHAT the gap means — and only a divergent panel keeps that
visible.* (A 4-persona panel converges on the obvious two — G1, G7 — and calls it agreement.)

# PANEL B — tech/innovation (DONE)
**Convergence:** G1 believability-confound **11/20** · **G8 retrieval-decomposition 10/20** (the "positive-signal inverted" —
G8 is the part they'd actually SHIP, which is exactly why its lack of justification bothers them) · G7 floor-effect **7/20**.
Mid-band splits by FUNCTION: G4 constants (MLOps/infra/enterprise — audit) · G3 trigger-N (implementers/sim/cost — spec-hole
+ cost-modeling) · G6 min-max (data-platform/DX/sim — stateful-purity + lineage).
**Minority / sharpest catch:** G5 flagged by only 4 seats — and the **red-team seat alone reframed G1+G5 as an EXPLOIT**
("optimize the believability metric = steer the whole memory/reflection stack via injected high-poignancy, high-cooperation
events"). The room's rarest + most consequential catch.
**Sharpest divergence:** ★statistician vs ★founder — both agree the believability number is broken, disagree on the fix:
statistician = **measurement rigor** (report ablation deltas w/ CIs vs a real baseline — the result is *rescuable*); founder
= **wrong dependent variable** (even a perfectly-measured believability score doesn't predict retention/coherence — *drop
the DV*). "Is the flaw in the measurement, or in choosing 'believability' as the thing to measure?"

# THE A-vs-B CONTRAST (the demo — the panel is a knob)
Same 8 gaps, two panels, structurally different critiques:
- **Both** converge on G1 (confound) + G7 (floor). But **B elevates G8** (the shippable primitive is under-justified) — a
  gap A barely touched; and **A elevates G5** (the construct/epistemics of "belief") — which B mostly reduced to a
  variance/exploit problem.
- **The verdict, verbatim from B:** *the paper "markets its least-portable claim (believability, G1/G7) and under-justifies
  its most-portable primitive (retrieval decomposition, G8)"* — reproducibility/cost/gameability/does-it-ship concerns a
  theory panel never raises; conversely A interrogates the *construct* of belief/importance a tech panel reduces away.
- **So: who you seat decides whether the paper's flaw reads as an engineering-reproducibility failure or a
  conceptual-construct failure.** The crit apparatus is itself a declared, tunable instrument-parameter — and only running
  ≥2 compositions makes that visible. That reflexivity is the honest, R&D-legible point for Saquib.

# PANEL C — SEEDED grounded critics (DONE) — the seeding PROVED itself
5 critics, each grounded in a REAL fetched OA work (not memory): Zheng et al. *LLM-as-a-Judge* (2306.05685) · Pineau et al.
*ML Reproducibility checklist* (2003.12206) · Gelman & Loken *Garden of Forking Paths* (Columbia PDF) · Henderson et al.
*Deep RL That Matters* (1709.06560) · Park's OWN §6/§7 (self-seed). All fetched + OA-verified; 2 honest flags (a Pineau
figure-image couldn't be transcribed; a Gelman HTML mirror redirect-looped → used the primary PDF).
**The killer result — grounding OVERRULED the persona (real-data-over-memory, demonstrated):**
- **Gelman & Loken:** a bare "stats-skeptic" persona would attack the d=8.16 as p-hacking. The *actual text* says multiplicity
  is "not a huge problem" for large, low-variance effects — exactly Smallville's regime (d=8.16, σ=0.72). So the fetched text
  **removed a WRONG critique** (the magnitude) and relocated the valid one to the *parameter/condition choices* (G4). The
  persona would have been confidently wrong; the seed made it correct.
- **Zheng:** forced the concession that G1's believability was *human*-rated, so the LLM-judge-bias argument had to retreat
  from G1 to G5 (which IS LLM-scored) — again, less aggressive + more correct than a persona.
- **Park self-seed:** G2 (short-timescale) + G7 (floor baseline) are corroborated *by the paper's own limitations text* — the
  strongest reflexivity (the critique rests on the authors' concessions, not our inference).
**Reusable:** these 5 seeded critics ARE the grounded set for our own reflexive method-review (Zheng→our LLM-coded scores;
Pineau→our thresholds; Gelman→§2.1 anti-pre-anchoring's citable backing; Henderson→§2.14 baselines; Park-self-seed→grounding
a critic on our own limitations). = the "Seeded methodology-grounded critics" panel in the registry.

# The demo claim (for Saquib)
The instrument found the gaps; the Gloss engine works them; and running TWO panel compositions on the identical gaps shows
the panel is an explicit, tunable instrument-parameter — theory-panel and tech-panel surface *different* critiques and
*disagree for structurally opposite reasons*, which a small consensus panel would hide. That reflexivity (the crit apparatus
is itself a declared variable) is the honest, R&D-legible point.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: reading-SB S156 2026-07-30 — the PI asked whether the crit panel was tech/innovation-oriented (the first was
  theory-heavy). Rather than discard it, kept it as Panel A (theory) and fired Panel B (tech/innovation, 5 grounded seats
  reusable for the reflexive). Both run on the instrument's 8 Smallville gaps; the A-vs-B contrast is the demo.
SCHOLARLY SOURCES: smallville_rd_gapfind_demo (the 8 gaps); the Gloss / commentary_constellation engine; the naming lock
  (gap/seam); §2.6 IRR (convergence/divergence); §2.8 (the panel-is-a-knob honesty).
WHAT NEEDS VERIFICATION: Panel B result + the A-vs-B contrast to be folded in; the 5 grounded tech seats to be reused as the
  reflexive method-review panel (WS-E); citations inside Panel A (Cronbach&Meehl, Simmons/Nelson/Simonsohn, ACT-R, Wixted)
  are the seats' own references — verify before any enter a write-up (§13). -->
