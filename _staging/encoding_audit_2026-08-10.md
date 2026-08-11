# Encoding audit — do we need to expand the palette? (design-SB, 2026-08-10)

**The question (PI):** "do we need to expand our color palette a bit? I know the brown was added because of the terracotta."

**The method:** list every dimension the figures need to encode, and assign each a *channel*. Colour is reserved for **KIND** (the locked, 3DR-16 grammar). If a dimension is structural (hierarchy, sequence) it should ride a non-colour channel. Only if a genuine *KIND* dimension has no free, legible hue do we expand.

## The audit

| Dimension | What it is | Channel now | Verdict |
|---|---|---|---|
| **Provenance** | original (16:1–8) vs added (16:9–20) text | HUE — fern / terracotta | KIND ✓ |
| **Edge kind** | logic / resonance / sonic | HUE — fern / gold / sky | KIND ✓ |
| **Move hierarchy** | top-level vs nested | INDENT + line-style (solid/dotted) + lightness + "unpacks into" label | structure, not hue ✓ (fixed today) |
| **Sequence** | the weak "and then" edge | de-emphasis (ghosted/dotted/faint) | ✓ |
| **Direction** | source → target | arrow-tip / matrix asymmetry | ✓ |
| **Selection / focus** | the move/section you're on | gold accent + white card | interaction state, not KIND ✓ |
| **Text vs reading** | Mark's words vs our note | typeface (serif vs sans) + weight + the M-label | not hue ✓ (D4) |
| **Move kind** | `move_type` (transaction, perception…) | text value in the axes | not hue ✓ |
| **Claim strength** | edge/coding confidence | *not yet encoded* | reserved: weight / opacity (grammar already says "weight = claim strength") |

## The finding — the one real issue

Per-figure, everything's clean: each figure legends its own colours, and no viewer sees two colour-systems at once. **But across figures, `fern` is doing two jobs:**

- `fern` = **"original text"** (provenance) in the Move Score
- `fern` = **"logic"** (edge-kind) in the Connect figures

Same with the general accent role gold plays. This is a **global** colour=KIND drift — not visible in any single view, but real if someone reads the whole suite. It's exactly the "green/orange means two things" problem you caught earlier, one level up.

## Recommendation

1. **Don't expand ad-hoc.** Adding hues reactively re-creates the overload.
2. **Keep structure off the colour channel** (done today — hierarchy via indent/line-style, not hue). This is what kept us from *needing* more colours for the Move Score.
3. **Do a small, deliberate expansion IF we want strict global consistency** — assign each project-wide KIND its **own** hue and publish **one global colour-key** (a single legend that holds across every figure), so `fern` never means two things. That likely means 1–2 new hues (e.g. a distinct hue for "logic" so it stops borrowing fern), chosen to sit inside the house (warm, botanical, no near-black) and to hold at favicon scale + for colour-blind safety.
4. **Route it through a design-crit** (the grammar is 3DR-locked, so this is a grammar update, not a styling tweak). The crit question: *"here are the N project-wide KINDs that need colour; here's a proposed global key; does it stay legible + house-coherent + colour-blind-safe?"*

**My lean:** worth doing, but as its own small deliberate pass — not tonight. The per-figure views are honest and legible now; the global key is a polish/consistency upgrade before the whole suite goes public (and before Lovable, so they skin against the final key).

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: design-SB 2026-08-10 — answer to the PI's palette-expansion question, as an encoding audit (dimensions × channels).
  Surfaced a global colour=KIND drift (fern = provenance-original AND logic-edge across different figures). Per §2.16 (colour =
  KIND) + §2.15 (declared channels = auditable encoding). Not a decision — a tee-up for a design-crit + the PI's review.
SCHOLARLY SOURCES: the locked visual grammar (viz_principles / 3DR-16); the live figures (Move Score + 3 Connect); the house
  palette (design tokens). Colour-blind safety + favicon-scale legibility are the crit's acceptance tests.
WHAT NEEDS VERIFICATION: (1) PI decides whether strict global consistency is worth a deliberate palette expansion. (2) if yes,
  a design-crit on a proposed global colour-key (1–2 new hues, house-coherent, colour-blind-safe). (3) do it before the suite
  goes public / before Lovable, so the signature look is skinned against the final key. -->
