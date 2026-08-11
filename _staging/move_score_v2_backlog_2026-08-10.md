# The Move Score — v2 backlog (post-Situate-data)

**Status:** captured, NOT building. v1 draft is frozen (PI, 2026-08-10) until the coded Situate data lands. This file holds the GPT feedback (2026-08-10) so it doesn't rot (§2.9), synthesized into the next iteration's work.

## The reframe (GPT's core, and it's right)

The current v1 is strong at **Attend** (what's happening here) + **Understand** (how the move is built). It's weak at **Orient** (where am I in the whole) + **Remember** (can I carry it away). GPT's principle:

> **See the whole → enter the moment → inspect the move → reconstruct the whole.**

Four cognitive jobs the instrument should serve:

| Job | Reader's question | Response | v1 status |
|---|---|---|---|
| **Orient** | Where am I in the story? | scene spine · cast/place state · schematic map | the arc is a first seed; scene layer + cast/place missing |
| **Attend** | What exactly is happening here? | focus text · evidence highlight | v1 does this (Focus, verse-foreground) |
| **Understand** | How is this move built? | labeled line · nesting · before→after | v1 does this (keyed axes, recursive nesting) |
| **Remember** | Can I reconstruct it without looking? | icons · retrieval · retelling · audio | missing entirely |

## Top 5 to prototype when we resume (GPT's shortlist, my ordering)

1. **Story spine / scene layer** — `PASSAGE > SCENE > MOVE > nested`. Mark 16:1–8 as 4 scenes (Preparation 1–2 · Obstacle 3–4 · Encounter 5–7 · Exit 8); the active scene follows scroll. Answers the perpetual "where am I?" **← highest value; depends on a scene-grouping in the data (method), not Situate.**
2. **Evidence highlighting (source ↔ move alignment)** — click a move, the verse temporarily marks the exact words it's read off (agent underlined, operation stronger, substrate bracketed, inferred-outcome dotted). This continuously *demonstrates* "the move is read off the text." **← depends on the move→char-span map (already flagged as v1's fidelity ceiling; method roadmap).**
3. **Parent containers for multi-move utterances** — 16:7's M17–M21 are ONE messenger's message, not 5 parallel observations; 16:3 similarly. Show the utterance whole, the beats attached beneath. *Decomposition must never visually erase the unit it decomposed.* **← buildable now on existing data; a real v1 weakness GPT + the PI both flagged.**
4. **Open threads** — questions/promises/commands raised and (un)resolved: `stone? → rolled back`, `where is Jesus? → Galilee`, `tell the disciples → they said nothing`. The last is electrifying: an instructed action visibly failing to resolve — the negative-space finding, shown not told. **← bridges to CONNECT/negative-space; needs a thread-tracking layer (method).**
5. **Recall mode** — at scene boundaries, replace passive "read again" with one tiny retrieval task ("what changed since they set out?"); at the end, an 8-landmark storyboard. Retrieval > rereading for durable memory. **← buildable; pairs with the recompose bookend v1 already has.**

## The rest, bucketed

**Buildable on current data (no new method layer):**
- Parent containers (#3 above); the labeled-line already exists — extend to reported-speech nesting.
- Cast + location sticky strip (WHO/WHERE/TIME/SPEAKER) — a "story-state debugger for humans." *Needs a per-verse cast/place field (small method add).*
- "What changed? (before → after)" line per move — our grammar already describes state change; surface outcome as a before→after. *Derivable from substrate/outcome.*
- Close-reading **lenses** (`Notice… speech · seeing · place · negation · repetition`) — one at a time; the computer signals without permanently marking the page. This is the "read it again, circle every word about seeing" move. *Derivable from move_type/operation + text.*
- Reader's paraphrase **before** ours (Study mode): TEXT → YOU → INSTRUMENT, then "what did you add? what did we add?" — methodological literacy as UI.
- Highlight categories on the trace (! surprising · ? question · ↔ connection · ★ remember) — extends the v1 annotation layer.

**Depends on the Situate data (the freeze reason):**
- **Date the longer-ending interpolation** (PI, 2026-08-10). The "added by later hands" note on 16:9–20 should carry *when* it was added — a transmission/lineage fact — and render FROM the Situate/transmission data (`transmission_node_drawer` / `lineage`), not hardcoded editorial. Same as the disputed-ending provenance flag requested from Method SB. Until then the note stays qualitative ("absent from the earliest manuscripts").
- The inline typed glosses (paradigm/sitz/position markers, colour = KIND, click → panel) — the PI's own gloss idea; reuses the apparatus pattern. **This is the main thing the freeze is waiting on.**
- The left/right margins (Sefaria Resource-Panel model): center = passage, left = story spine, right (on demand) = Situate depth.

**Bigger / later:**
- The **score** metaphor made literal (noteheads by move-kind; Distant view = the full score of Mark 16). The arc is the seed.
- Mnemonic landmarks (8 non-figurative glyphs; concrete for reading/memory, abstract for inspect — never mixed). *Cross-tradition: default non-figurative (no prophet/deity portraits).*
- Audio as a **controlled mode** (Listen / Follow / Loop / Listen-without-text), move-by-move temporal highlighting (not word-karaoke); beware redundancy (spoken+printed identical can hurt). Tradition-appropriate affordances (recitation/chant/cantillation) as plug-ins around one core object.
- Prediction gates ("continue →" before a reversal) for a Slow Read mode.
- Story memory-palace walk (only textually-attested concrete elements; monochrome strip, not AI fantasy).

## Invariants GPT's feedback confirms (already our discipline)

- **Text keeps visual sovereignty** — darkest, largest, most stable; analysis comes and goes around it. Use opacity → underline → temporary halo → connecting line *before* permanent semantic color. Color should say "look here now," not "memorize my legend." (This tempers a full colour-by-role scheme — matches our locked grammar: colour = KIND, sparingly.)
- **Correspondence over category** — color earns its place more for source↔move correspondence (signaling/cueing) than for permanent role-coding.
- **One lens at a time.**

## Architecture thread — progressive layering (PI, 2026-08-10; not yet decided)

The PI noticed the shape: **Plate (text) → toggle on the Moves → …** — and asked whether that's how the reader goes step by step, with each engine (Gloss, Situate, Connect) becoming another toggle that *stacks*. My read: yes, this is the unifying reading-room architecture. The **text (Plate) is the permanent base**; each engine's output is a **toggle-able layer** the reader adds as they go deeper:

`Plate (Text) → Moves (Decompose) → Gloss → Situate (margins/typed inline) → Connect (arcs/loom)`

Two things it maps onto cleanly: (a) the **engine structure itself** — one layer per engine; (b) the **lectio reading-practice telos** (draw → linger → respond → reflect) — the layers roughly ARE the stages of attention. Design implication: the current controls (Plate toggle, Read/Inspect, Focus) are a first cut; the mature form is a small **layer stack** (each layer on/off, composing on the text), not a pile of unrelated buttons. Not all layers on at once (that's a hairball) — the reader deepens progressively. **Decide when the Gloss + Situate data land** (the layers need their feeds first). This is the reading-room / Luminous-archive form the figures are converging toward.

## Cross-refs
- The build spec: `move_score_redesign_reconciliation_2026-08-10.md`
- The live v1 draft: `/_staging/viz_move_score_v2.html`
- The SSOT node: `engine/data/viz/design_engine.json` → `move_score` (status: v1 draft, frozen)
- Situate feeds (what the freeze waits on): `engine/data/goldenpath/mark16/{sitz,paradigm,form,transmission,lineage}_node_drawer.json`

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: design-SB 2026-08-10 — captured GPT's 25-point Move Score feedback (pasted by PI) into a synthesized v2 backlog,
  per §2.9 (discovered inventory must be triaged, not left to rot) and the PI's v1-draft freeze (don't refine until Situate data
  lands). Organized by GPT's 4-jobs frame (Orient/Attend/Understand/Remember) + top-5 prototypes + buildable-now vs Situate-
  dependent vs later. NOT a build order — a backlog to prioritize when the freeze lifts.
SCHOLARLY SOURCES: GPT feedback 2026-08-10 (cites event-cognition/segmentation PMC5734104; signaling meta-analysis; retrieval-
  practice/spacing Nature Rev Psych; multimedia redundancy; Sefaria Resource Panel; Scaife Viewer; Quran.com Study Mode;
  BibleProject; Genius annotation). Cohort could not verify its own citations — spot-check before any chapter use.
WHAT NEEDS VERIFICATION: (1) which items need new method-side data (scene grouping, move→char-span map, thread-tracking, cast/
  place fields) vs render-only — flagged inline but not confirmed with Method SB. (2) the Situate-dependent items gate on the
  coded Situate layer landing. (3) prioritize with the PI when the v1 freeze lifts. -->
