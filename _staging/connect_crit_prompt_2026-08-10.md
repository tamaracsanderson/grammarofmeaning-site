# Connect figures — usability crit prompt (paste into GPT / a cohort)

Focus: **how a reader USES these + how they relate**, not the aesthetics (those are settled). Paste everything between the markers.

═══════════════════════════════════════════════════════════════
PASTE-START
═══════════════════════════════════════════════════════════════

I'm designing part of an instrument that reads a scripture passage **move by move** — a "move" is one operation the text performs (an agent does an operation on a substrate, producing an outcome). The base figure ("the Move Score") shows a passage's verses with each move read off the text. This crit is about the **CONNECT** layer: three figures that show *how the moves in one passage hold together* — the links between moves (logic, resonance, sonic). All three render the same data: 78 typed edges between the moves of Mark 16, each edge tagged by kind (logic = cause/contrast/support/nesting; resonance = parallelism/ring/leap; sonic = sound — not yet coded here).

The three figures:
1. **Arc Band** — https://grammarofmeaning.org/_staging/viz_connect_arcband.html — the moves in reading order (top to bottom); an arc in the left margin joins two linked moves; colour = kind of link.
2. **Relation Loom** — https://grammarofmeaning.org/_staging/viz_connect_loom.html — the same links as an adjacency matrix (row = a move reaching out, column = a move reached to); a woven cell = a link; near the diagonal = neighbours, far off = long reach.
3. **Topology Lab** — https://grammarofmeaning.org/_staging/viz_connect_topology.html — the same links as a force-directed graph with reading order set aside; dot size = how many links a move has (hubs); clusters pull together.

The eventual context is a contemplative reading practice (interactive lectio divina: draw → linger → respond → reflect) plus a scholarly research use. The reader can also toggle a plain "Plate" (verbatim text only) and a move-by-move "Move Score."

**The problem I'm feeling, and what I need from you:** I can tell there's missing *use-intuition*. I don't yet have a clear sense of how a reader would actually pick these up, when to use which, or how to move between them to make sense of the passage. It feels like the gap between a first draft and a mature edition. Please answer concretely:

1. **How would a reader actually USE each of the three?** Give 2–3 personas (e.g. a curious first-time reader, a preacher preparing a text, a graduate student, a contemplative). For each figure, what question does it answer, and who is it for?
2. **Is each intuitive on first encounter?** Walk through what a newcomer sees and where they'd get confused or stuck. What's the single biggest comprehension barrier per figure?
3. **How should a reader JUMP BETWEEN the three?** Right now they're three separate pages. Is the *relationship* between them clear? Should they be one instrument with a toggle/zoom (like moving from a wide overview to a close reading), or stay separate? What's the natural sequence — which do you open first, and what makes you switch?
4. **Does this help you read the passage DIFFERENTLY** than plain reading — and if so, how would you name the payoff in one sentence a reader would feel? If it doesn't, say so plainly.
5. **What onboarding / use-intuition is MISSING?** What one or two additions (a first-run walkthrough, a "start here", a worked example, a bridge between the views, a legend rework, a task prompt) would most close the gap between "beautiful diagram" and "I know how to read with this"?

Draw on close-reading pedagogy, information-visualization (arc diagrams / adjacency matrices / node-link graphs and their known trade-offs), and reading-practice / annotation tools you know. Be concrete and specific to these three figures — I don't need generic advice.

At the END, give me: (a) your single highest-leverage recommendation for closing the use-intuition gap, and (b) one sentence on whether these should be three separate figures or one instrument with views.

═══════════════════════════════════════════════════════════════
PASTE-END
═══════════════════════════════════════════════════════════════

## How to run it
Paste the block above into GPT-5 (and optionally Fable + Gemini for a 3-cohort read). Drop the responses back and I'll reconcile them into a Connect use-intuition spec — the "how to use + how they relate" layer these are currently missing.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: design-SB 2026-08-10 — a paste-ready usability crit prompt for the 3 Connect figures, per the PI's request ("give
  me something to paste into gpt"), centered on her stated gap: use-intuition + how to jump between the views + the reading
  payoff, NOT aesthetics (those are settled). Mirrors the 3DR/design-crit pattern; PI runs the cohort, design-SB reconciles.
SCHOLARLY SOURCES: the 3 live figures; the move-grammar; the reading-room / lectio telos; info-viz trade-offs (arc vs matrix vs
  node-link). The prompt asks the cohort to solve the crit concretely, not just critique.
WHAT NEEDS VERIFICATION: (1) PI runs it (GPT ± Fable/Gemini); (2) design-SB reconciles responses into a Connect use-intuition
  spec (onboarding + the jump-between-views model: separate pages vs one instrument with a zoom/toggle). -->
