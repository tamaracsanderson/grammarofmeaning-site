# Lovable handoff — batch 1: The Plate + The Move Score

**For:** a Lovable signature-look pass on the first two engine figures.
**From:** design-SB, 2026-08-10.
**Process (established):** functional-first. The interaction, data-binding, and grammar are LOCKED here; Lovable restyles the *look*; design-SB then re-integrates Lovable's output back to render-from-data (Lovable emits React — we re-wire to our static HTML that reads the live feeds). So Lovable works on the **look**, not the logic.

## The two figures (live, functional, v1 draft)

| Figure | Engine | Live | Reads from |
|---|---|---|---|
| **The Plate** | Text | https://grammarofmeaning.org/_staging/viz_plate.html | `checkout.json` |
| **The Move Score** | Decompose | https://grammarofmeaning.org/_staging/viz_move_score_v2.html | `checkout.json` + `moves.json` |

Both default to the **reader view** (clean); append `?mode=audit` (Plate) or click **Inspect** (Move Score) to see the builder/analytic layer. Lovable should skin the **reader view**.

## LOAD-BEARING — do not change (these are the instrument, not the styling)

1. **Render-from-data.** Every word of scripture + every move value comes from the feeds. Never hardcode passage text, move labels, paraphrases, counts, or the apparatus. If a value looks wrong, it's fixed in the generator, never in the page.
2. **The visual grammar** (locked, 3DR-16): position = textual order (never time) · indentation = nesting · **colour = KIND only** · arrow = direction · ○ = tested-absence · weight = claim strength · **the verbatim text is the only pure black.**
3. **Text keeps visual sovereignty.** The verse is the largest, darkest, most stable thing; our reading is clearly secondary. Analysis comes and goes *around* the text.
4. **Reader-first default; strip internal vocabulary.** The reader never sees "bow-tie / node / method-engine / spec / filenames" — those live only in the audit/Inspect layer.
5. **Labels track the real fields.** The Move Score's axes (agent · operation · substrate · outcome · narrator · kind of move · agent's role · place) are the actual coded fields — don't rename or invent.
6. **Provenance encoding.** Fern = earliest text (16:1–8); terracotta = added-by-later-hands (16:9–20) + the TR variant siglum. Terracotta consistently means "contested/later." Keep that consistent.
7. **The zero-token trace stays local** (localStorage; highlight + categorized note). No accounts, no network.
8. **The four checks** (Cold Read · Cold Start · Fidelity · vs-Wild) — the figure must stay self-sufficient + honest about what it does/doesn't claim.

## SKINNABLE — Lovable's playground (make it beautiful)

- Typography: scale, pairing, rhythm, optical sizing (currently Fraunces display / Newsreader serif reading / Inter sans / IBM Plex Mono labels — refine freely within a warm, literary, botanical-restraint feel).
- Spacing, margins, reading measure, vertical rhythm.
- Colour *refinement within the house palette* (below) — never new hue meanings (colour = KIND is locked), but tone/tint/contrast polish is welcome.
- Motion & cadence — the scroll-driven Focus, the arc, transitions (reference: pudding.cool "A Brief History" — text stays, analysis reveals; motion serves reading, never spectacle).
- Card / drawer / margin treatments; the arc's bar styling; the apparatus popover; the "How to read a move" key; the ending/rest treatment at 16:8.
- The overall **signature look** — this is the point of the pass.

## Design tokens (the house palette — light + dark)

```css
/* light */
--paper:#FCFBF7; --paper-2:#EFE7D3; --paper-3:#FFFFFF;
--ink:#0E0E0C; --ink-soft:#24302A; --ink-2:#52605A; --ink-3:#7C8478; --rule:#C9BE9F;
--fern:#3F7D57; --moss:#2C4A38; --gold:#B8924A; --terracotta:#C4602F; --sky:#3f6d7d; --olive:#6E7B3A;
/* dark */
--paper:#1C1813; --paper-2:#26211A; --paper-3:#221D16;
--ink:#F7F1E3; --ink-soft:#ECE6D8; --ink-2:#C3BCAC; --ink-3:#8E877A; --rule:#3D362B;
--fern:#7FB894; --moss:#A9C9B2; --gold:#D8B36A; --terracotta:#E08A54; --sky:#8fb6c4; --olive:#A6B06A;
/* type */
--disp:"Fraunces"; --serif:"Newsreader"; --sans:"Inter"; --mono:"IBM Plex Mono";
```

House rule: warm-white ground, botanical restraint, **no near-black** (use `--ink` for the text only; chrome is softer). Fern/moss/gold/terracotta earn their place by KIND, not decoration.

## The re-integration gotcha (design-SB owns this, not Lovable)

Lovable outputs a React app; our figures are static HTML that fetch the live JSON feeds. So: take Lovable's *visual* treatment (CSS, layout, type, motion) and re-apply it to our render-from-data HTML — do **not** ship Lovable's React with hardcoded content. The content must keep flowing from `checkout.json` / `moves.json`.

## References to study first
- **Sefaria's reader + Resource Panel** — the interaction model (text central; apparatus alongside, never overlaying).
- **The Vilna Talmud page** — text central, commentary demarked, distance-from-centre = authority.
- **pudding.cool "A Brief History"** — the scroll cadence.
- Our grammar + gate + moodboard: https://grammarofmeaning.org/engine/design-principles.html
- Our schema (what each figure is): https://grammarofmeaning.org/engine/design-engine.html

## Not in this batch
Connect (Arc Band / Relation Loom), Facing Page, Ledger of Absences — data-blocked pending Method SB's `connect_edges.json`. They'll be batch 2.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: design-SB 2026-08-10 — Lovable handoff for the first two engine figures (Plate/Text + Move Score/Decompose), both
  at v1 draft + reader-first. Prepared per the PI's "send a few to Lovable at a time" intent while the Connect family is data-
  blocked. Functional-first process: Lovable skins the look; design-SB re-integrates to render-from-data (React→static HTML).
SCHOLARLY SOURCES: the locked visual grammar (3DR-16 / viz_principles); the four-check gate (design-principles); the house
  palette (design tokens above); the reference set (Sefaria, Talmud, pudding.cool). The two live figures are the source of truth
  for behavior; this doc is the skinning brief.
WHAT NEEDS VERIFICATION: (1) PI decides WHEN to send + which Lovable project. (2) after Lovable returns, design-SB re-integrates
  to the live feeds + re-runs the four checks + verifies no hardcoded content crept in. (3) batch 2 (Connect family) waits on
  connect_edges.json. -->
