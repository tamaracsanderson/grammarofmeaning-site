# Scan / Relation Loom — crit log + working checklist

**Figure:** `_staging/viz_connect_loom.html` · live: https://grammarofmeaning.org/_staging/viz_connect_loom.html
**Data:** `engine/data/goldenpath/mark16/{moves,connect_edges}.json` · `connect_taxonomy.json` · `engine/connect_core.js`
**Started:** 2026-08-14 (PI reactions + GPT crit). Living doc.

## PI's two reactions
1. **"I don't love how the top part stays the same as I switch tabs."** → the SHARED-header problem (see cross-cutting below).
2. **"I love the visual of the chart, the cross-word, but I have no idea what it tells me."** → right chart, under-interpreted.

## The central problem (GPT agrees)
Not "wrong chart" — **"right chart, insufficiently interpreted."** The matrix is a strong research view; keep it.
Scores now→potential: Intuitiveness 2→4.5 · Usability 3→4 · Info-fit 4.5→5 · Wayfinding 2→4.5 · "So what?" 1.5→5 · Appeal 4→4.5.

## What Scan is FOR (vs Trace) — the identity distinction
- **TRACE:** *Where does THIS move connect?* (start with one move, follow its edges; click→inspect.)
- **SCAN:** *What is the connective architecture of the WHOLE passage?* (stand back; hubs, dense neighborhoods, long reaches, local-vs-long-range, forward-vs-backward; **look→notice→inspect**.)
Lead with the analytical question, not "how to operate the instrument."

---
## THE SIX PRIORITIES (Scan)
- [ ] **1. Different top-level proposition from Trace:** "See the architecture of the whole passage." (own hero + own primary controls.)
- [ ] **2. Matrix much higher; remove the permanent detail card above it.** The grid is the hero; details appear only after selection (sticky right inspector, doesn't push the grid down).
- [ ] **3. Teach the diagonal explicitly:** diagonal = reading order; near = local, far = long-range; **forward vs backward** (the two triangles: rows=source, cols=target → upper/lower triangle = reaches forward / reaches backward through textual time).
- [ ] **4. `Hubs · Clusters · Long reaches` as interpretive lenses** — press Hubs → marginal degree summaries; Long reaches → far cells stay strong, local fade; Clusters → dense blocks emphasized.
- [ ] **5. Marginal summaries** — tiny outgoing-degree bar at each row end, incoming-degree bar per column → sender-hubs + receiver-hubs legible without reading cells.
- [ ] **6. Hover = strong row×column crosshair + the two actual move texts** ("M13 → M21 · SUPPORTS", both microtexts, "8 moves apart").

## THE V2 — four perceptual stages
1. **GLANCE** — matrix almost immediately after title; strong labeled diagonal spine; faint section boundaries; tiny key (near=local · far=long reach · crowded line=hub); no big detail panel.
2. **NOTICE** — `Hubs · Clusters · Long reaches` lenses + 2–3 **auto-generated findings** ("M13 reaches unusually widely" / "M42–M48 a dense neighborhood" / "M12→M41 one of the longest links") each with `show me →`. **The single most valuable change** (#6): compute + surface salient structure; don't just display the matrix.
3. **INSPECT** — hover crosshair; click → sticky side inspector (M7→M6 · REPORTS · source text · target text · plain-language · distance/direction).
4. **FILTER** — promote "break down by relation" from a weak dropdown to a real analytical affordance: `ALL · FEEDS · SUPPORTS · FILLS · REPORTS · …` with counts → "what is the topology of SUPPORT in this passage?"

## Secondary points
- [ ] Remove disabled Lineage/Resonance/Shape/Sonic controls here too (unless it genuinely becomes multi-kind).
- [ ] Reinforce the **Loom** metaphor lightly: rows=warp, cols=weft, crossing=connection, open cloth=**negative space** (aligned with the method — where it ISN'T woven).
- [ ] One visual family for all Linkage; isolate a type on filter (avoid confetti; spatial position is the superpower, not per-cell color).
- [ ] Density/hub modes as "look-for" buttons, not permanent tabs.
- [ ] Row/col label microtext on hover; row-label click = "M13 reaches 9 moves", col-label click = "M13 is reached by 4 moves" (directed).
- [ ] Section boundaries in the grid (native divisions — verse/paragraph/speaker, not Christian-specific), so within-episode vs cross-episode density shows.
- [ ] Wording: not "find a crowded row" but **"crowded row = a move that organizes many others; crowded column = a move many converge on; far-from-diagonal = a relationship bridging distant parts."**
- [ ] LONG-TERM: **compare matrices** (small multiples: Mark 16 vs Matthew 28; Greek vs WEB; original vs reception) — each passage a structural *fingerprint*. The instrument's larger claim.

---
## ⟐ CROSS-CUTTING (both Trace + Scan; PI felt it directly)
**Per-view identity — kill the shared boilerplate top.** The three Connect views (Trace/Scan/Map) currently share one top region (kick, title, task, how, 5-kind legend, relation card) → "same app, different chart renderer." Each must become a distinct **lens** with its OWN hero proposition + OWN primary affordances (nav framework stays constant):
- **TRACE** → "Follow one move's connections." primary: *choose/click a move*.
- **SCAN** → "See the architecture of the whole passage." primary: *Hubs · Clusters · Long reaches*.
- **MAP** → (its own proposition — TBD when crit-walked).
Also shared: drop the disabled other-kind controls per view; move detail into a sticky side inspector (not above the field); teach the reader vs researcher split; use native section landmarks.

---
## Round 2 crit (append below)
<!-- next round -->

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: Design SB 2026-08-14. PI crit-walked the Scan/Loom view (her two reactions + a GPT crit) right after Trace.
  Captured per the collect-in-md-then-work-through workflow. The through-line she felt ("top stays same across tabs") = GPT's
  per-view-identity point; recorded as the #1 cross-cutting fix for the whole Connect suite.
SCHOLARLY SOURCES: the GPT crit (PI-run 2026-08-14); viz_connect_loom.html (current figure); trace_arcband_crit_2026-08-14.md
  (sibling); connect_taxonomy.json (render vocabulary); connect_edges.json (Mark 16 feed: 70 LINKAGE + 8 SHAPE). §2.16 render-from-data.
WHAT NEEDS VERIFICATION: (1) forward/backward triangle orientation depends on the render's row=source/col=target convention —
  confirm against connect_loom's actual axes. (2) auto-findings (hub/cluster/long-reach detection) = a small graph pass on the
  edges; thresholds want a sanity check. (3) section-boundary field = verse_start in moves.json (native division, cross-tradition-safe). -->
