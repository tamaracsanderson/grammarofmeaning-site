# HANDOVER — The Method Engine (bow-tie schema, v2 "less ink")

One explanatory figure, not an audit dashboard. Reads left → right: two parallel branches
(DECOMPOSE ∥ SITUATE) converge on one waist (the **enriched move**), and recompositions fan out
of it into two tinted bands, then the **gap mirror**, then synthesis → Reading Room.

## LOCKED (production direction)

- **Fits without scroll at 1440 × 900, 100% zoom.** Figure body ~625px; the whole path
  Text → Reading Room is on one screen. Any edit that breaks this is a regression.
- **Ontology / labels.** `waist_independent` (the output does not need the coded move) and
  `move_conditioned` (needs the enriched move). Never "direct" / "combination" again.
- **Two edge languages + a quiet spine.** waist-independent = thin dashed moss;
  move-conditioned = thick fern; `flow` = dotted olive for the structural spine only.
- **One rail, one trunk.** A *single* bypass RAIL climbs out of Text, runs flat in its own lane
  above the figure, and each waist-independent view taps off it with a short drop. A *single*
  TRUNK leaves the waist, and short branches peel to each move-conditioned tile. No per-node
  over-arcs, no spaghetti fan.
- **~10 bordered cards carry the spine** (Text, Decompose, Situate, enriched move, Gap, Gloss,
  Reception, Synthesis, Reading Room, Reflexive audit). Everything else is a plain label tile on
  a tinted band, or a leaf line under Situate.
- **The gap mirror is the centrepiece.** One named GAP forks symmetrically into GLOSS (grammar
  side · constructed) and RECEPTION (canon side · retrieved). Caption: *where they diverge is the
  finding*. The two-sided split is load-bearing even while Reception has no rows.
- **Reflexive audit lives off the flow** — a thin strip below the figure, never a node in it.
- **Two modes.** METHOD (default): topology, names, functions, one maturity dot. AUDIT: adds
  implementation / validation tags and a ⚠ where a known limit exists. Stored in `me-mode`.
- **All detail is in the drawer** — layers, badges, requires/produces, edges, status gloss.
  Nothing long is drawn on the canvas.
- **House tokens.** Warm ground, hairline rules, small radii, Newsreader / Inter / IBM Plex Mono,
  no near-black, no drop shadows.

## BACKUP alternate (not built)

If the rail still reads as busy: drop the taps and label the rail once, letting the band heading
carry the meaning ("outputs that don't need the move"). Only `railPath()` changes.

## Files — what each holds

| File | Holds | Rule |
| --- | --- | --- |
| `public/data/method_flow.json` | **ALL content**: `meta` (modes, edgeTypes, maturity, bands) + `nodes[]` + `edges[]` | Single source of truth. Never hardcode a label in a component. |
| `public/data/tokens.json` | every colour / font / radius / stroke width, light + dark | Mirrors the `:root` block; keep in sync. |
| `src/styles/method-engine.css` | all presentation, incl. the mobile notation swap | Copied verbatim to `public/static/method-engine.css`. |
| `src/components/method-engine/geometry.ts` | `flowPath` · `railPath` · `trunkPath` · `mirrorPath` · `anchorFrom` | Pure functions of the anchor map. No DOM beyond one `getBoundingClientRect`. |
| `src/components/method-engine/MethodEngine.tsx` | grid assembly, `useAnchors` measure pass, hover/drawer/mode state | |
| `NodeCard · BandRow · GapMirror · Legend · NodeDrawer` | one concern each | |
| `public/static/method-engine.{html,css,js}` | the self-contained static build | Opens over `file://`; data inlined into `window.METHOD_FLOW`. |

### DO NOT CHANGE

1. Adding a node = editing JSON only (plus, if it is a tile, the band it belongs to).
2. No colour literals in components. Tokens only (`var(--me-*)`).
3. `waist_independent` and `move_conditioned` must never share a weight, colour or dash.
4. Do not restore per-node arcs. One rail, one trunk.
5. Do not fill the canon side with placeholders to make Reception look finished.
6. Do not move drawer detail back onto the canvas.

## LAYOUT — no coordinates any more

v1 stored `x/y/w/h` per node. v2 does not: the figure is a **CSS grid** (cone · waist gutter · fan ·
end) and the SVG edge layer is drawn from anchors measured off the DOM, relative to the figure box:

```js
const anchorFrom = (el, base) => { const r = el.getBoundingClientRect(); return {
  left:r.left-base.left, right:r.right-base.left, top:r.top-base.top,
  bottom:r.bottom-base.top, cx:r.left-base.left+r.width/2, cy:r.top-base.top+r.height/2 }; };
```

A `ResizeObserver` on the figure re-measures on layout change, mode switch and font load. Editing
copy therefore cannot break the geometry — there is no height to re-fit.

**The rail** (two curves total): climb out of Text into the lane, then one flat run; taps are short
staggered drops (`t.left - 16 - i*9`) into each tile's top edge.

**The trunk**: one straight stem to `min(tile.left) - 34`, then flat-shouldered cubics to each tile.

**The mirror**: vertical cubics from the gap's bottom edge to each arm's top edge.

## INTERACTIONS

- **Click a node** → the one drawer: function, grain, impl, validation, status gloss, waist
  dependency, expands-to, implementation note, requires/produces, full edge list. Close via ×,
  scrim or Escape.
- **Hover a node** → `.me-figure.is-focused` dims everything; the node, its neighbours and its
  edges get `.is-traced`. Pure class toggling, no re-layout.
- **Mode toggle** → METHOD / AUDIT, persisted in `localStorage` (`me-mode`).
- **Theme** → `data-theme="light|dark"` on `<html>`, defaults to `prefers-color-scheme`, manual
  choice stored under `me-theme`.

## MOBILE

Below 900px the SVG and the rail lane are hidden and the grid collapses to one column. The
edge distinction moves from curve weight to a **left border** on each tile (moss = waist-independent,
fern = move-conditioned). No arc math runs at mobile.

## QA after an edit

- 1440 × 900: `document.documentElement.scrollHeight` must stay ≤ 900 with the figure ≈ 600–700px.
- No card may clip: `[...document.querySelectorAll('.me-node')].filter(n => n.scrollWidth > n.clientWidth + 1)`
  must be `[]`.
- Static parity: open `public/static/method-engine.html` over `file://` — same node count, same
  `path.me-edge` count (23), no console errors, drawer + AUDIT toggle working.
- After a CSS edit, re-copy: `cp src/styles/method-engine.css public/static/method-engine.css`.
