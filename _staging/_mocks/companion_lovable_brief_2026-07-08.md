# Lovable brief — "The Companion" reading screen (paste target)

**Purpose:** paste the block below into Lovable to generate a React/Tailwind version of the
companion's slow-read screen. We are **harvesting components + interaction patterns** to bring
into our own build (our site is hand-authored HTML/CSS on `gom.css`), not adopting the whole app.
Evaluate: the lens-selector pattern, the line-reveal interaction, the golden-chain component, and
how cleanly it decomposes. Self-contained, mock content only — no backend/auth/db.

---
PASTE-START — copy from here into Lovable
---

Build a single, calm, reverent **reading screen** called **The Companion** — a "slow-read" of one
scripture passage. It is a reading *practice*, not an app: unhurried, for adults, never gamified.

## The look (match this exactly)
A warm, botanical, print-inspired house style. Use these tokens as Tailwind theme values:
- Colors: paper `#FCFBF7`, paper-white `#FFFFFF`, ink `#24302A`, ink-2 `#52605A`, rule `#C9BE9F`,
  moss `#2C4A38`, fern `#3F7D57`, sage `#8AA88B`, olive `#6E7B3A`, terracotta `#C4602F`, gold `#C9A227`.
- Fonts (Google Fonts): **Newsreader** (serif) for all reading text + headings; **Inter** (sans) for
  UI/labels; **IBM Plex Mono** for small eyebrow/tag labels.
- Feel: generous whitespace, hairline rules, rounded cards, a single small botanical leaf mark.
  Calm and confident. NEVER twee, stained-glass-kitsch, neon, or dark-SaaS.

## The screen (one view)
1. A small monospace eyebrow: "Romans · read as Christian first".
2. A 4-stage progress rail, subtle: **Read → Reflect → Respond → Rest** (Read active).
3. Heading: "Romans 8:28–30".
4. **The golden chain** — a horizontal 5-node diagram of the verbs
   **foreknew → predestined → called → justified → glorified** (small gold/sage dots joined by a line;
   the Greek under each is optional). The chain should be its own reusable component.
5. **The passage, revealed one line at a time** at the reader's pace. Show ~3 lines "read" and the
   next lines faint/waiting; a tap or scroll reveals the next line; a slow "breathing" dot sets tempo.
   Passage (public-domain KJV):
   "And we know that all things work together for good to them that love God, to them who are the
   called according to his purpose. For whom he did foreknow, he also did predestinate… whom he
   called, them he also justified: and whom he justified, them he also glorified."
6. **A held gap** — a faint line where the *reason* God chose would go, that intentionally **stays
   empty** ("…why these? — held, not filled"). It must never resolve or explain.
7. **The lens-selector — the core UI.** A control to pick one "reading lens" from a battery of ten
   families (show these as the options): Staged-discursive (Lectio) · Analytical (close reading) ·
   Symbolic · Apophatic (silence) · Embodied (body-scan) · Recitation · Dialogical (Chavruta) ·
   Imaginative (Ignatian) · Ethical (Naikan) · Meta (the mirror). One is active; picking a different
   lens re-frames the reading. **Design this selector well** — try a clean pattern (a tucked side-tab,
   a command-palette, a segmented dial). This is the piece we most want to see your take on.
8. **A reflect-back prompt** at the end: an italic question ("What caught you?") that mirrors the
   reader's response back — it must **never advise, score, or tell them what it means.**

## Hard rules (non-negotiable)
- **Deposits nothing:** the UI never states an interpretation, never says "this means" or "traditions
  agree." It holds the gap and hands nothing down.
- **No gamification:** no scores, streaks, XP, progress-percentages, badges, or dopamine loops.
- **Accessible + reduced-motion:** every animation has a `prefers-reduced-motion` fallback (finished
  state, no motion); full keyboard + screen-reader support.
- **Self-contained:** mock content only; no backend, auth, database, or external API.

## What to output
A small, cleanly-decomposed React + Tailwind (+ shadcn/ui if useful) component set:
`ReadingSurface`, `GoldenChain`, `LensSelector`, `LineReveal`, `ReflectBack`, `PaceDot`,
`StageRail`. Keep components independent and legible. Prioritize the **LensSelector** and the
**LineReveal** interaction — those are what we're evaluating for reuse.

---
PASTE-END — stop copying here
---

## After Lovable runs — what to bring back
Look at (and tell design-SB about): (1) the **LensSelector** pattern — is it better than our
margin-tab / dial / illuminated-index sketches? (2) the **LineReveal** approach (scroll vs tap,
easing, reduced-motion). (3) any Tailwind token setup we can mirror in `gom.css`. (4) the component
boundaries. We re-implement the winners in our own hand-authored house code (no framework on the
live site) — so we're mining *patterns + interactions*, not shipping Lovable's output.

## HOW PRODUCED
design-SB, 2026-07-08 — the researcher has a Lovable account and wanted a paste-ready brief to
explore whether any components/interactions are worth bringing into our companion. Scoped to the
slow-read screen + the lens-selector (the round-2 differentiator). Guards travel per the companion
spec (deposits-nothing §2.1, no-gamification, reduced-motion, for-adults). Staging reference doc.
