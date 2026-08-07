# Meaning Engine

Build me a schema diagram: "The method engine" — a BOW-TIE flow

I need a single, elegant, information-dense schema diagram (not a landing page) called "The method engine." It visualizes a text-analysis pipeline whose true shape is a bow-tie: two parallel input branches converge on one central hinge, and every output fans out from that hinge. The whole diagram reads left → right. It must be beautiful, legible, and scholarly — think a well-designed systems diagram in a good science journal, not a flashy product page.

Non-negotiable: keep content (the nodes + edges) in a JSON data file, presentation in components, and design tokens in a theme file — all separate. I will rebuild this as static HTML that reads the JSON, so nothing about the diagram's content may be hardcoded inside components.

THE SHAPE — a bow-tie, left to right

  LEFT third = converging cone          CENTER = the waist          RIGHT two-thirds = the fan

  ───────────────────────────           ──────────────────         ─────────────────────────────

  INPUT: Text

    │  splits into TWO PARALLEL branches (they do NOT read each other)

    ├───────────────────────────┐

    ▼                           ▼

  ┌───────────────────────┐  ┌────────────────────────────┐

  │ GRAMMAR / ANALYZE     │  │ SITUATE (text-level)       │

  │ (stage + outputs, TOP)│  │  Sitz · Paradigm · Frame · │        ┌────────────────────────────┐

  │ Code → moves          │  │  Witness   (+ Lineage▼)    │        │ OUTPUTS (two stacked bands) │

  │ + Gaps, Seed-ranking  │  │                            │        │  ── GRAMMAR band ────────── │

  └───────────┬───────────┘  └──────────────┬─────────────┘        │  Compare · Resituate ·      │

              │      converge on the shared coded object            │  Tributary · Gloss · Gaps · │

              └───────────────┬───────────────┘                     │  JOINS · [Fan—paused]       │

                              ▼                                      │  ── CANON band ──────────── │

                   ┌──────────────────────┐                         │  Reception  ⚠ awaiting build│

                   │  CODED MOVE (waist)  │──── thick edges ───────▶ └──────────────┬─────────────┘

                   │  "one operation +    │     (from the waist)                    ▼

                   │   its arguments"     │                              SYNTHESIS: panel colloquy /

                   └──────────────────────┘                              argument-graph + JOINS

                     ▲ Constellation forks off RAW TEXT → IPA,                       │

                       bypassing the waist entirely                                  ▼

                                                                          META: Reading Room + church map ·

                                                                          instrument-reads-itself

Left (converging cone): INPUT (Text) splits into two parallel branches — GRAMMAR/ANALYZE on top, SITUATE on the bottom. They run independently (neither reads the other) and converge on the waist.

Center (the waist): the CODED MOVE — the single shared object the whole instrument turns on. Draw it as the visual pinch-point of the bow-tie.

Right (the fan): from the waist, outputs fan out into two stacked bands (GRAMMAR band above, CANON band below), then flow to SYNTHESIS, then META.

THE TWO EDGE TYPES — this is the crux; it's why I want your visual expertise

The diagram must visibly distinguish two kinds of connection:

THIN / DIRECT edges — a text-level box produces an output without passing through the waist. These edges arc from the left branch PAST the waist to their output tile on the right. This graceful over-arc is the hardest and most important visual detail — please make it elegant (a smooth curved path, clearly "skipping" the center). Direct edges: Sitz → Sitz-output · Paradigm → Paradigm-output · Frame → Morphospace/MCA · Witness → Degrees-of-separation, and Constellation, which forks off raw Text → IPA and bypasses everything.

THICK / COMBINATION edges — outputs that originate at the CODED-MOVE waist (they need the coded move + the situate context). Draw these as heavier lines fanning out from the waist: Compare · Resituate · Tributary · Gloss · Gaps-as-output · Reception · Fan.

The reader must be able to tell at a glance: "this output comes straight from the text" vs "this output needs the full coded move." Weight, color, or texture — your call, but the distinction must be immediate.

THE NODES (the content — put ALL of this in the JSON, none hardcoded)

Each node has: id, label, level, band (grammar / canon / — ), kind, status, an optional badge (an honest "not-built-yet" flag), a short sub (one-line description), and optional layers (sub-outputs). Statuses: live (built + has data), pilot (built, thin data), awaiting (real but no data export yet — show dimmed/dashed), paused (retired). Badges are honesty flags — the diagram must NOT pretend un-built things are done.

Level 1 — INPUT

Text — the chunked, move-bearing passage. live.

Level 2a — GRAMMAR / ANALYZE (top branch; a STAGE that is also an output family, drawn UP here — never mirrored lower)

Analyze — awaiting. sub: "the moves, the silences, what ranks." layers: Grammar (moves) · Gaps · Seed ranking. badge: "monotone gap-grammar — a known limit (missed the women's silence at Mark 16)."

Level 2b — SITUATE (bottom branch; text-level)

Sitz — awaiting. sub: "the world the text was made in." produces DIRECT output. badge: "DB-rendered engine-0 output (source_grounding); ~2 seed texts so far."

Paradigm — awaiting. sub: "the frame it argues within." produces DIRECT output. same source_grounding note.

Frame — awaiting. sub: "the 8-axis stance the move takes." produces DIRECT → Morphospace/MCA. badge: "renders from the atlas reader (shared engine); deployed drawer still shows the retired 7-axis — fix on rebuild."

Witness — pilot. sub: "transmission distance from the event / autograph." produces DIRECT → Degrees-of-separation.

Lineage — awaiting. sub: "the sources standing behind the move." NOTE: Lineage is MOVE-LEVEL, not a direct Situate output — its output (Tributary) hangs off the WAIST, not off Situate. Draw Lineage in the Situate branch but route its output edge from the waist.

Level 3 — CODED MOVE (the waist)

Coded move — live. sub: "the analytic atom: one operation + its arguments (source_move). GRAMMAR ∥ SITUATE converge here; every combination-output fans from here." (Worked example: Mark 16 = 55 coded moves.)

Level 4 — OUTPUTS, GRAMMAR band (the instrument speaking)

Compare — awaiting. COMBINATION. layers: Braid (narrative — moves across the gospels) · Partiture (translation — SHOW · LOCATE · EXPLAIN).

Resituate — live. COMBINATION. layers: deductive · abductive.

Tributary — awaiting. COMBINATION (off the waist; ◄ Lineage, move-level). sub: "how sources flow into the text."

Gloss — awaiting. COMBINATION. layers: reader-gloss · persona-crit · gap-fill. badge: "its mode menu renders as a (stance × method) GRID — not a tree; cells marked PROPOSED."

Gaps-as-output — awaiting. COMBINATION. badge: "monotone gap-grammar known-limit."

JOINS — awaiting. COMBINATION, and also feeds SYNTHESIS (draw a second edge to the synthesis band). layers: Variance × Lineage · Lineage-headwaters · Frame-veer × Variance · Sonic × Lineage · Panel-verdict × variance-type. badge: "analysis-only, no export yet."

Constellation — awaiting. DIRECT (thin edge off raw text, bypassing the waist). sub: "the sound-field — sonic / phonetic recurrence."

Fan — paused. sub: "many voices at once." Draw struck-through / dimmed.

(Also drawn as DIRECT outputs landing in this band from the left arcs: Sitz-output · Paradigm-output · Morphospace · Degrees-of-separation — the four thin-edge tiles.)

Level 4 — OUTPUTS, CANON band (the tradition speaking) — label it "Reception — the tradition speaking"

Reception — awaiting. COMBINATION. sub: "the real retrieved historical texts answering the gap (Calvin's actual words off the shelf) — the mirror of Gloss's built voices." badge: "AWAITING BUILD — 0 rows (S162+)." Draw the whole band as a reserved, honestly-empty slot — the two-band split is the load-bearing idea even while empty.

Level 5 — SYNTHESIS (across outputs)

Panel colloquy / argument-graph — awaiting. sub: "per gap: nodes = frame-claims, edges LABELED." layers (the edge vocabulary): AGREES · CONTESTS · REFRAMES · EXTENDS · CONCEPTUALLY-ENABLES · HISTORICALLY-DEVELOPS-FROM. badge: "mostly spec, no store."

Cross-output joins — awaiting. sub: "Variance × Lineage · Braid × Situate (fed by JOINS)."

Level 6 — META (the instrument on itself)

Reading Room — live. sub: "the integrated reader-facing surface (e.g. the gospels) where several outputs land per move; + the church/institution map."

Instrument reads itself — awaiting. sub: "the recursive abductive run + provenance / vocab-version / SSOT-freshness."

HOUSE STYLE (use these tokens exactly — this diagram must sit inside an existing warm, editorial, botanical site)

Palette (light): ground #F6F1E4, paper #EFE7D3, ink #24302A, muted #6E7669, hairline #C9BE9F, card #FFFDF6; accents — deep fern #2C4A38, moss #3F7D57, terracotta #C4602F, honey #E0A93B, olive #6E7B3A.

Palette (dark): ground #1B211D, paper #232A25, ink #EDE7D8, muted #A6AEA3, hairline #3A423C; fern #4A7A5C, moss #5C9A72, terracotta #D9793F. Support BOTH light and dark (prefers-color-scheme + a manual toggle).

Type: serif = Newsreader (headings, node labels); sans = Inter (body, sub-lines); mono = IBM Plex Mono (kickers, badges, level tags — uppercase, letter-spaced). Node labels in Newsreader 600; badges in mono ~9px uppercase.

Feel: botanical restraint, hairline borders, generous whitespace, rounded ~11px cards, no near-black, no drop-shadow drama. The two edge types differentiated by weight + a subtle color shift (moss for direct, fern for combination is a fine start). Honesty badges: awaiting = dashed border + dimmed; paused = struck-through; a small terracotta pill for "awaiting build" / "known-limit."

INTERACTIONS (write these into the HANDOVER so a static rebuild keeps them)

Click a node → a drawer (right-side panel or centered modal) with that node's full detail: its sub-line, its layers, its badge, and its dependency type (direct vs combination). One drawer component, driven by the node's JSON.

Hover a node → highlight its edges (dim the rest) so the reader can trace one path through the bow-tie.

Responsive: the bow-tie is a desktop-first figure. On narrow screens, degrade gracefully — it's fine to stack the flow vertically (INPUT → the two branches → waist → outputs → synthesis → meta) rather than force the horizontal bow-tie. Tell me how you handled the arcs at mobile.

WHAT I NEED BACK (the handover — so I can rebuild this as static HTML fast)

Read this first — the target is a STATIC SITE, not a React app. grammarofmeaning.org is plain static HTML + CSS + vanilla JS on GitHub Pages — there is no React runtime, no build step, no npm at serve time. So the most useful thing you can give me is a design that ports cleanly out of React. Please provide:

README / HANDOVER.md — the production direction; what's LOCKED vs a BACKUP alternate; the key files + what each holds; any "do not change" rules; and the INTERACTIONS note (above).

Content as DATA — a single method_flow.json holding nodes[] and edges[] in the schema I described (id · label · level · band · kind · status · badge · sub · layers[] for nodes; from · to · type:"direct|combination" · note for edges). This is the most important deliverable — I render the real site from a file exactly like it, so please use these field names.

A theme / tokens file — every color / font / radius / effect in one place (tokens.json or a CSS :root block).

A "React → static HTML" porting note + a static export. This is the bridge I care most about:

a short note listing what in the mock is React-specific (state, hooks, JSX, any component library / shadcn / Tailwind classes) and its plain HTML + vanilla-JS equivalent — so I know exactly what to swap;

if at all possible, a self-contained static build of the diagram: one HTML file + CSS + vanilla JS (or, at minimum, the rendered HTML/SVG markup + the extracted CSS) that runs by opening the file — no React, no bundler. That lets me drop it in without reverse-engineering JSX;

a list of any runtime dependencies (CDN scripts, web-font URLs, icon libs) so I can inline or replace them — the static host blocks external requests, so everything must be self-contained.

The connector geometry — a short note (in the README) on how the edges are drawn: are the thin arcs and thick waist-fans SVG <path>s (give me the path-generation approach / the d-string logic), or a layout library? Since the arc-past-the-waist is the trickiest bit to reproduce statically, I need to know exactly how you built it — ideally as plain inline SVG I can lift directly.

(No image-credits needed — this is a diagram, no curated media.)

The guiding principle again: content · presentation · tokens in separate files. That separation is what lets me drop your design straight into a static, data-driven rebuild.

+++

As a reference:

1. here is our house style moodboard: https://grammarofmeaning.org/_staging/_bakeoff/HOUSE_PATTERN.html
2. here are two previous websites you designed for similar parts of this project, for look and feel: https://corpus-flywheel-guide.lovable.app/
https://pleasing-page-forge.lovable.app/

This project was built with [Lovable](https://lovable.dev).

**Live app**: https://method-engine-flow.lovable.app

## Build with Lovable

Continue developing this project in the [Lovable editor](https://lovable.dev/projects/1480c0af-73ae-4abe-a35b-d372de9b8380).

- **Ship faster**: describe what you want to build and Lovable handles the code.
- **Stay in sync**: every change made in Lovable is committed straight to this repository.
- **Full ownership**: this code is yours. Push to `main` on GitHub and your changes sync back into Lovable, ready for your next prompt.

## Development

Prefer working locally? You need Node.js and npm — [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating).

```sh
git clone <this-repository-url>
cd <repository-name>
npm i
npm run dev
```
