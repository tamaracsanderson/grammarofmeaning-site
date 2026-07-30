---
title: "R&D gap-find demo — the instrument on Park et al. 'Generative Agents / Smallville' (arXiv 2304.03442). For Saquib."
date: 2026-07-30
session: S156 (reading-SB)
status: RESULT — the instrument run on a real R&D paper, framed as a research gap-finder. Grounded in fetched arXiv text.
provenance: coded from the ar5iv HTML of 2304.03442; reasoned ONLY from the text; no later literature consulted or leaked.
  ✅ VERIFIED (2026-07-30) — all 8 load-bearing quotes/constants confirmed against the AUTHORITATIVE PDF
  (`/Users/tamarasanderson/Documents/twelve-laws/smallville.pdf`) with page citations: 0.995 · α=1 · the 1–10 importance
  prompt · min-max → p.9 §4.1; reflection-threshold 150 → p.10 §4.2; d=8.16 & μ=29.89/σ=0.72 → p.14 §6.5.1; the "without
  access to anything" baseline (μ=21.21) → p.13 §6.2; the limitations (overly-cooperative/embellishment/overly-formal-from-
  instruction-tuning/short-timescale) → p.17 §8.2. No corrections. **Safe to circulate.**
---

# Why this demo
Saquib emailed the PI the Simile ($2B synthetic-users startup) news + this paper (Park's "Smallville," the generative-agents
work Simile is built on) — his own realm. Running our gap-finder on it shows the instrument as an **R&D gap-finder**: it
surfaces genuine research gaps from a paper's OWN words (claim-vs-limitation tensions, asserted-but-underived constants, a
metric measuring appearance while claiming architectural merit) — NOT hindsight about what later work found.

# What was coded (real, fetched passages)
Two passages: (A) the architecture — memory-stream retrieval (recency 0.995 · LLM 1–10 importance · cosine relevance · score
= sum with all α=1 · min-max normalize · reflection fires when Σ importance > 150); (B) evaluation + limitations
(believability as the metric; 100 crowdworkers; ablations; d=8.16; admitted "overly cooperative," "embellishment,"
"overly formal … due to instruction tuning," "short timescale").

# SITUATE
- **Paradigm = believability-as-metric** — success is judged by *rated appearance* ("illusion of life," "facade of realism,"
  "appear to make decisions"), not correctness/veridicality. Explanation is by ablation.
- **Foreclosed-seams:** (FS-1) believability-as-success forecloses correctness/coherence/task-utility as rival criteria;
  (FS-2) "in our implementation … α=1 / 0.995 / 150" frames version-constants as incidental, foreclosing design-vs-tuning;
  (FS-3) believability = raters' perception forecloses models-cognition vs renders-its-appearance.

# TOP-5 GAPS (each cites the activating phrase; all pass the 5 gates)
1. **G1 · metric-validity confound (PARADIGM).** The headline d=8.16 is a *rated-believability* delta — and the paper's OWN
   limitations name surface confounds ("overly cooperative," "embellishment") the metric can't separate from architectural
   merit. Touches the central claim. (Activated by "most believable **behavior**" vs the limitations list.)
2. **G2 · scope/timescale (FRAME).** Planning is claimed for a "**longer time horizon**"; evidenced on a "**short
   timescale**" by the paper's own admission. The load-bearing claim is under-bounded.
3. **G7 · floor-effect / stacked baseline (adversarial).** ~8 SD is measured against a condition "**without access to
   anything**" — a near-empty baseline invites a floor-effect reading independent of architecture quality.
4. **G3 · reflection-trigger indeterminacy (MOVE).** "Σ importance scores for **the latest events** > 150" — event count N
   is unstated, so the threshold conflates memory *intensity* with *volume*.
5. **G4 · magic-constant provenance (SITZ/FRAME).** 0.995 / 150 / α=1 carry the system with no derivation or robustness range.

Plus 3 more kept gaps (G5 construct-validity of "importance"; G6 min-max reference population; G8 sufficiency of the 3-term
retrieval decomposition) + 3 SEAMS (constants "in our implementation" don't-transfer; believability inherited from the
sub-field; instruction-tuning artifacts bound to the base model). **4 DISCARDS** with the gate named (in-window-resolved or
nitpick — shows the filter rejecting, not just finding).

# CRIT-PANEL (divergence preserved) — the demo's punch
- **ML-systems:** min-max is stateful — without its reference population the ranking isn't reproducible; α=1 + min-max
  interact. Wants an ablation on the *constants*, not just the components.
- **Cognitive scientist:** "importance" is one-shot LLM poignancy but narrated as what the agent "believes" — construct
  validity is the whole game.
- **Adversarial skeptic:** the giant d is the tell — 8 SD comes from a stacked comparison, not a real architecture-vs-baseline.
- **HCI-product:** crowdworker believability over a short window ≠ retention over weeks; wants a longitudinal in-situ study.
The four seats *disagree on which gap matters most* — that divergence is itself the signal (a real crit panel, not consensus).

# The demo claim (honest)
The instrument surfaced genuine, defensible research gaps in a foundational paper — each anchored to the paper's own words,
each a place the text opens a question it doesn't close — with the gates rejecting nitpicks + in-window-resolved items. This
is the R&D application: a gap-finder for the research frontier, shown on Saquib's own realm. Next: a section of Saquib's
dissertation ("Embodied Mathematics by Interactive Sketching", the PDF IS on disk) for an even-more-personal run.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: reading-SB S156 2026-07-30 — the PI directed running the instrument on the generative-agents paper as a Saquib
  R&D demo. The local smallville.pdf never downloaded, so the SB fetched the ar5iv HTML of 2304.03442 (provenance flagged) and
  coded from the fetched text; reasoned only from the text, no future-leakage. Full instrument (situate→analyze→layered scan→
  gates→rank→crit panel).
SCHOLARLY SOURCES: Park et al. 2304.03442 (fetched ar5iv HTML); INSTRUMENT_v3_spec (the stages + gates); the naming lock
  (gap/seam); §13 (no fabrication + the spot-verify flag on exact constants); §2.14 (out-of-domain R&D application).
WHAT NEEDS VERIFICATION: spot-verify the exact quoted constants (0.995 / 150 / α=1 / d=8.16 / μ=29.89) against the published
  PDF before circulating; optional follow-on = Saquib's dissertation section (`~/Downloads/nazmus-saquib-phd-thesis-2020_compressed.pdf`). -->
