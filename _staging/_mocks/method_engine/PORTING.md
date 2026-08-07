# PORTING — React figure → static HTML

The static build is already done: **`public/static/method-engine.html` + `method-engine.css` +
`method-engine.js`**. Open the HTML file directly (`file://`) — no server, no build step, no
bundler, no React. Copy those three files (plus `method_flow.json` / `tokens.json` if you switch to
a fetch) into the site and you are finished.

This note exists so you can see exactly which React idea maps to which vanilla one.

## Runtime dependencies

| Thing | Status |
| --- | --- |
| React / TanStack Router / Vite | **Not present in the static build.** Only used by the app. |
| shadcn / Radix / lucide / Tailwind | **Never used in the figure at all.** Every class is a hand-written `me-*` class in one stylesheet. Arrowheads are SVG `<path>`s; ⚠ and × are text characters. |
| CDN scripts | **None.** |
| Web fonts | One `<link>` to `fonts.googleapis.com` for Newsreader / Inter / IBM Plex Mono. If your host blocks external requests, delete that line and either self-host the three families as woff2 with `@font-face` at the top of `method-engine.css`, or drop it: the stacks fall back to `Georgia, serif` / `system-ui` / `ui-monospace`, which still holds the design. |
| Content JSON | Inlined as `window.METHOD_FLOW = {...}` so it works over `file://`. On a server, replace that block with `window.METHOD_FLOW = await (await fetch('./method_flow.json')).json();` before loading the script. |

## The swap table

| In the React app | React-specific because | Plain equivalent (as shipped in `method-engine.js`) |
| --- | --- | --- |
| `createFileRoute("/")` + `head()` | router-owned document head | the `<title>` / `<meta>` tags in `method-engine.html` |
| `import flow from ".../method_flow.json"` | bundler JSON import | inlined `window.METHOD_FLOW` (or `fetch`) |
| `<NodeCard />` | component | `nodeCard(node, variant)` — builds the same `<button class="me-node">` with `createElement` |
| `<BandRow />`, `<GapMirror />`, `<Legend />` | components | `bandRow()`, `gapMirror()`, `renderLegend()` — same DOM, same class names |
| `<NodeDrawer />` + `openId` state | component + state | `openDrawer(id)` builds the `<aside class="me-drawer">` into `#me-drawer-host`; `closeDrawer()` empties it. Scrim click and Escape both close |
| `useState(focused)` + `isTraced()` | React state | `setFocus(id)` → `applyFocus()` toggles `.is-focused` on the figure and `.is-traced` on `[data-id]` / `path.me-edge` via `classList.toggle` |
| `useState(mode)` + re-render | React state | `state.mode` plus a re-run of `renderHead/renderLegend/renderFigure`; persisted in `localStorage` under `me-mode` |
| `useLayoutEffect` + `ResizeObserver` measure pass | hooks | the same `ResizeObserver` on `#me-figure`, plus `window.resize` and `document.fonts.ready`, all calling `drawEdges()` |
| `useMemo` for the path list | memoisation | `drawEdges()` recomputes the array on each measure — same inputs, same `d` strings |
| `useEffect` theme restore | hydration-safe storage read | `initTheme()`: read `localStorage`, set `data-theme` on `<html>` |
| `geometry.ts` (typed) | TypeScript | the same `flowPath` / `railPath` / `trunkPath` / `mirrorPath` / `anchorFrom`, verbatim, minus the type annotations |
| `var(--me-*)` tokens | — | **unchanged.** `method-engine.css` is a byte-for-byte copy of `src/styles/method-engine.css` |

## The one thing to know

Both builds measure the DOM. v2 has no coordinates in the JSON: the layout is a CSS grid, and the
SVG edge layer is drawn from anchors relative to the figure box. So the port had to carry the
measure pass across — that is `drawEdges()` plus the `ResizeObserver`. Everything else is a direct
transliteration.

## Deliberately avoided so the port stayed trivial

- No portal/dialog primitive for the drawer — a plain `position: fixed` `<aside>` plus a scrim button.
- No CSS-in-JS, no Tailwind class soup, no `clsx` — semantic `me-*` classes with `is-*` state
  modifiers, which is what vanilla `classList.toggle` wants.
- No animation library — a few CSS `transition`s.
- No template literals for node markup — `createElement` keeps text content escape-safe.

## Keeping the two in sync

```bash
cp src/styles/method-engine.css public/static/method-engine.css
cp public/data/method_flow.json public/static/method_flow.json   # and re-inline into the HTML
cp public/data/tokens.json      public/static/tokens.json
```

Then open `public/static/method-engine.html` over `file://` and check: same node count, 23
`path.me-edge` elements, no console errors, drawer opens, AUDIT toggle reveals the tags.
