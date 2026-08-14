# Map / Topology — crit log + working checklist

**Figure:** `_staging/viz_connect_topology.html` · live: https://grammarofmeaning.org/_staging/viz_connect_topology.html
**Data:** `engine/data/goldenpath/mark16/{moves,connect_edges}.json` · `connect_taxonomy.json` · `engine/connect_core.js`
**Started:** 2026-08-14 (PI reactions; GPT crit round TBD — append when it comes).

## PI's reactions
1. **"I can't see the moves while I play with the chart."** Clicking the largest hub jumps me UP to a text list of moves — the detail is elsewhere, not beside the graph. → same detail-placement problem as Trace + Scan.
2. **"I'm not sure why I should care about 7 links, and I should be able to explore those connections more clearly WITHIN the map."** → raw degree count is meaningless without interpretation; exploration should happen IN the graph (click a hub → neighbors light in place, walkable), not by leaving for a list.
3. **"What does it mean that these two things are connected?"** (screenshot: two linked nodes) → the edges carry no explained meaning in the graph. Hover/click an edge should say the relation ("M42 REPORTS M43 = M43 is the speech reported inside M42").

## Working direction (pre-GPT-crit; consistent with Trace + Scan V2)
- [ ] **1. Own proposition (per-view identity):** Map = "See the passage as a web — who anchors it, what stands apart." (Trace=follow one move · Scan=architecture of the whole · Map=the web/its shape.) Own hero + own primary affordances; drop the shared boilerplate top + disabled other-kind controls.
- [ ] **2. Detail BESIDE the graph** — sticky side inspector; clicking a node never scrolls the graph out of view. The graph stays put; you explore within it.
- [ ] **3. Explain the edge** — hover an edge → the relation in plain language ("M42 —REPORTS→ M43: M43 is the speech reported inside M42"); hover/click a node → its neighbors highlight IN the graph + the inspector lists them (linguistic, directional), each clickable to walk.
- [ ] **4. Interpret degree, don't just count** — not "7 links" but "M42 anchors 7 moves (a hub)"; size/label hubs meaningfully; surface isolated moves + the few bridges. (The Scan auto-findings idea applies: "M42 is the strongest hub; M7 stands nearly alone.")
- [ ] **5. Explore in-place / walk** — click a node → focus it, dim the rest, neighbors strong; click a neighbor → re-center on it (walk the web). Never dump to an external ordered list.
- [ ] **6. Keep the force-graph aesthetic** (the PI likes the visual) — the fix is interpretation + in-place interaction + beside-inspector, not a new chart.

## Notes
- The 8 SHAPE echoes belong here (Map is where cross-view "shape" was pointed from Trace). Consider showing LINKAGE (structure) + SHAPE (echoes) as two edge families here, since Map is the "whole web" view — but avoid confetti (one family emphasized at a time).
- Force graphs handle 55 nodes but can spaghetti; keep labels legible, let selection prune.

## Round 2 — GPT crit (append when PI runs it)
<!-- next round -->

---
## ⟐ CROSS-CUTTING (now confirmed across ALL THREE Connect views)
The PI felt the SAME three things on Trace, Scan, and Map:
1. **Per-view identity** — each lens gets its own hero proposition + primary controls; kill the shared boilerplate top ("the top stays the same as I switch tabs").
2. **Detail BESIDE the field** — a sticky side inspector, never a scroll-away card above/below that pushes the visual out of view.
3. **Explain + interpret** — say what a connection MEANS (not just that it exists / how many), and let the reader explore/walk IN the visual.
These three are the shared V2 contract for the whole Connect suite. Trace V2 (shipped 2026-08-14) is the first worked example; Scan + Map follow the same contract with their own hero propositions.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: Design SB 2026-08-14. Third of the Connect crit-walk (Trace → Scan → Map). Captures the PI's Map reactions +
  records that the same three issues recurred across all three views → the shared V2 contract (per-view identity · beside-
  inspector · explain-and-interpret). GPT crit round for Map to be appended when run, matching the Trace/Scan pattern.
SCHOLARLY SOURCES: PI reactions 2026-08-14; viz_connect_topology.html (current force-graph); trace_arcband_crit + scan_loom_crit
  (siblings); connect_taxonomy.json; connect_edges.json (70 LINKAGE + 8 SHAPE). §2.16 render-from-data.
WHAT NEEDS VERIFICATION: (1) GPT crit round for Map (pending). (2) whether Map shows LINKAGE only or LINKAGE+SHAPE families.
  (3) edge-meaning-on-hover needs the same CC.prose plain-language templates Trace uses. -->
