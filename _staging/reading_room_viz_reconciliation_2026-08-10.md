---
title: "3DR-16 reconciliation — how to visualize Text · Decompose · Connect (the reading-room viz)"
date: 2026-08-10
author: design-SB
round: 3DR-16 (reading-room visualization / right side of the bow-tie)
cohorts: GPT-5 · Fable · Gemini Deep Research
query: research/10_dr/queries/reading_room_viz_3DR-16_2026-08-10.md (drafted in deploy _staging/, to mirror)
responses: 3DR16_gpt.txt · 3DR16_fable.txt · 3DR16_DR.txt (dropped at twelve-laws root, to mirror to research/10_dr/reading_room_viz_responses/)
status: RECONCILED — the deliverable (§2.6). Buckets per Decision 39 (UNANIMOUS / STRONG-MAJORITY / SOLO).
---

# 3DR-16 reconciliation — the reading-room visualization

## Headline: strong 3-way convergence; the approach is validated and the visual grammar is now lockable

All three cohorts — independently grounding their critiques in the Talmud daf, the Glossa Ordinaria, the critical apparatus
(TEI/Nestle-Aland), Bertin/Tufte, Wattenberg's arc diagrams, Drucker's *Graphesis*, and annotation-graph theory — converged on
the SAME architecture: a **family of synchronized views over one immutable textual spine**, two audiences served by **one grammar
in two disclosure modes**, a **Talmud-daf reading room**, and **negative space rendered as a positive mark**. The convergence is
strong enough to LOCK the encoding grammar (below). There is exactly ONE genuine design divergence (the Connect form), and it
resolves not by picking but by **building variants and testing** (per the PI's diverge-then-converge direction). Two of the
cohorts' "crucial questions" turned out to be METHOD-side, not design-side, and are routed to Method SB.

## UNANIMOUS (3/3) — LOCK these

| # | Finding (3/3) |
|---|---|
| 1 | **Text is the coordinate system.** Decompose annotates it, Connect relates objects anchored to it; nothing downstream reflows the text. A modular SERIES of views, never a mega-chart or one giant network. |
| 2 | **Two audiences = one grammar/data, two disclosure modes** (dense audit vs scrollytelling/progressive disclosure) — NOT two codebases. The moves-view is the bridging visual that serves both. |
| 3 | **Reading room = the Talmud daf + Glossa Ordinaria.** Center text (largest module) as anchor; margins radiate; brushing-and-linking on ONE shared coordinate (verse + move id); cross-text revealed on demand. Distance-from-center = epistemic distance. |
| 4 | **Negative space = a positive mark for a negative result** (hollow node / ghost edge with a null terminus / orphan glyph). Distinguish "sought-and-absent" from "not-assessed" — a blank alone reads as missing data. |
| 5 | **Generalization: abstract geometric primitives only; NO domain iconography** (no crosses/dharma-wheels/columns — "it should look like an instrument"). Colour = semantic only; indentation = nesting; text-anchored. Vary: locator system, script/RTL, baseline-meaning. |
| 6 | **The encoding grammar** (see the locked key below): colour carries KIND only (a small fixed categorical palette, NOT one-colour-per-type); the boring majority (LINK_SEQUENCE) is suppressed; motion only for state-change/object-constancy; two typefaces (serif text + sans/mono machinery); the text is the primary/only-pure-black voice. |
| 7 | **Where it breaks (Daodejing / legal / ritual):** a Gospel-trained baseline silently asserts NARRATIVE TIME. The axis must be declarable "discourse order," not timeline; support non-directional/cyclic containment; SHAPE must be promotable to primary; apophatic negation needs its own affordance; legal needs collapsible scope-brackets + the matrix view. |
| 8 | **Off-the-shelf, don't build:** D3 (d3-hierarchy for the moves-view; arcs), Observable Plot (matrices/small-multiples), Cytoscape.js (secondary topology/graph), Scrollama (scroll-driven reading), W3C Web Annotation + a stand-off anchoring layer, TEI apparatus tooling (EVT / TEI Publisher / ProseMirror+Annotorious) for the text+apparatus. CSS grid for the daf geometry. |
| 9 | **References (shared core):** the Vilna Talmud page · the Glossa Ordinaria / glossed scripture · the critical apparatus (TEI/Nestle-Aland). The `{TR adds 'quickly'}` apparatus belongs to the scholarly-text layer, typographically distinct from an analytical edge. |

## STRONG-MAJORITY (2/3) — adopt, with the minority noted

| Finding | Cohorts | Disposition |
|---|---|---|
| **Connect preserves textual order — arcs in GUTTERS**, not a re-laid-out graph. Fable + GPT both explicitly warn against the node-link "hairball" as the PRIMARY view. | Fable + GPT | ADOPT for the primary Connect view. (DR's edge-bundling — SOLO — sacrifices textual order, contradicting the 3/3 "text is the coordinate system" rule; it belongs to the SECONDARY topology/research view, where GPT already placed a node-link graph.) |
| **The Vilna Talmud page is THE first reference** to study (as information architecture, not aesthetic). | Fable + GPT | ADOPT as the "study first" reference. DR's *Graphesis* (SOLO) is adopted too, as the EPISTEMOLOGY reference (humanistic capta vs data) — not in conflict; different job. |
| **Bertin (Semiology) + Tufte (Envisioning) + Wattenberg (Arc Diagrams)** as the encoding/layering/connection canon. | Fable + GPT | ADOPT into the reading list. |

## SOLO (1/3) — kept as options / routed, not adopted as primary

| Finding | Cohort | Disposition |
|---|---|---|
| **Hierarchical Edge Bundling** (Holten) for Connect | DR | Not the primary view (breaks text-order). Keep as a candidate for the SECONDARY topology view. |
| **Drucker, *Graphesis*** as THE first reference | DR | Adopt as the epistemology reference (capta vs data); Talmud page remains "study first." |
| **z-axis depth overlay** for cross-text resonance | DR | A good interaction idea for the Facing Page / cross-text reveal; hold as an implementation option. |
| **Poemage** (sonic topology close-reading) | GPT | Adopt as the SONIC reference when SONIC is built. |
| **Bird & Liberman, Annotation Graphs** | GPT | Adopt as the data-architecture reference (overlapping annotations over one signal) — bears on the anchoring layer. |

## The one variant-decision (per the PI's diverge-then-converge)

The Connect (in-text) form has TWO good, text-order-preserving, NON-reconcilable candidates. Do not pick on paper — **build both,
run through the design-crit gate, converge (or split by audience) on the evidence:**
- **The Arc Band** (Fable): one text baseline; LINKAGE arcs above, SHAPE/SONIC below; hue = KIND; LINK_SEQUENCE ghosted.
- **The Relation Loom** (GPT): the move spine with FIVE parallel relation gutters (one per KIND); an edge curves between positions.
The **Decompose moves-view** likewise has two candidates worth testing — the **Move Score** (bars aligned to exact spans) vs the
**Indented Tree** (outline). Note: variants apply to the FORMS, never to the grammar (which is locked, §UNANIMOUS #6).

## The locked visual grammar (the move-grammar-equivalent for the right side)

> **position = textual/discourse order (never time) · indentation/containment = nesting · colour = KIND only (small fixed
> categorical palette; edge TYPE is a text/glyph label, not a colour) · arrow = direction · ○ = tested-and-absent (· = not
> assessed, — = not applicable) · visual weight = claim strength (LINK_SEQUENCE ghosted) · the verbatim text is the only pure
> black / the primary typographic voice · motion only to explain a state change (object constancy preserved) · no domain
> iconography.**

## Action items

1. **LOCK the grammar** above into `viz_principles` (a `the_grammar` block, render-from-data), cited to this reconciliation — it is now validated against Bertin/Tufte/Wattenberg/Talmud/Glossa/apparatus, not ad hoc.
2. **Build the design-engine schema** (mirrors method-engine.html): the six visuals as NODES, each holding 1–N candidate forms, each with a spec-drawer + the four-check gate.
3. **Build the Move Score first** (unanimous), on Mark 16:1–8 only, through the gate. Then build BOTH Connect variants (Arc Band + Relation Loom) and let the design-crit pick.
4. **Method-side questions routed to Method SB (165):** (a) ANCHORING GRAIN — moves anchor at verse grain (`verse_refs`), not exact char/token spans; v1 aligns at verse grain, full Move-Score fidelity needs spans (incl. discontinuous/nested). (b) DECOMPOSITION STATUS — single authoritative decomposition vs competing/overlapping (a §2.1 data-model call). Not blocking v1.
5. **Reading list** (for the studio wall): Talmud daf (first) · Glossa Ordinaria · critical apparatus (TEI) · Bertin · Tufte · Wattenberg · Drucker *Graphesis* · Poemage (SONIC) · Bird & Liberman (annotation graphs) · the Pudding (practitioner, for explaining progressively — not for encoding).
6. **Mirror the artifact set** to `research/10_dr/` (query → queries/; the 3 responses → reading_room_viz_responses/; this doc → reconciliation) — 🐥 Method SB owns the twelve-laws write.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: design-SB 2026-08-10 — reconciliation of 3DR-16 (reading-room visualization DR; GPT-5 / Fable / Gemini-DR). The
  cohorts critiqued how to VISUALIZE the finalized output of the first three engines (Text/Decompose/Connect) for two audiences
  composing into a reading room. Buckets per Decision 39. The finding: strong 3-way convergence on the architecture + the
  encoding grammar (lockable), ONE design divergence (Connect form) resolved by building variants and testing (PI diverge-then-
  converge), and two method-side questions routed to Method SB. §2.6 (3DR/IRR always yields a reconciliation), §2.8 (negative
  space as a finding), §2.14 (generalization/out-of-domain), §2.15 (go wide then consolidate — variants before convergence).
SCHOLARLY SOURCES: 3DR16_{gpt,fable,DR}.txt (the three responses); the 3 finalized feeds (checkout.json / moves.json /
  connect_node_drawer.json); the references the cohorts supply (Talmud daf, Glossa Ordinaria, TEI/Nestle-Aland apparatus,
  Bertin, Tufte, Wattenberg, Drucker Graphesis, Poemage, Bird & Liberman annotation graphs, the Pudding).
WHAT NEEDS VERIFICATION: (1) 🐥 Method SB to mirror the artifact set (query + 3 responses + this doc) to research/10_dr/. (2)
  spot-check any cohort-supplied citation before it enters the thesis chapter (cohorts flag they can't verify their own cites).
  (3) the grammar-lock lands in viz_principles; the design-engine schema + Move Score are built THROUGH the four-check gate. -->
