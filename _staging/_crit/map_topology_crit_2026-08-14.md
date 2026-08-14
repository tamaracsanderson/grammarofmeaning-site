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

## Round 2 — GPT crit (2026-08-14)
Verdict: "right object, wrong claim." Keep the force graph (appeal 4.5/5); change what Map *claims to show*. Scores: Intuitiveness 2.5→4 · Usability 2→4.5 · Info-fit 3→4.5 · Wayfinding 2→4 · **Analytical payoff 2.5→5**.

**THE METHODOLOGICAL FINDING (biggest point — not UI):** raw degree is a **grammar artifact**, not importance. M42's "7 links" are mostly **REPORTS** (a 7-move speech container), so "7 links ≠ 7 independent ways it organizes meaning." **Do NOT size nodes by raw degree.** Affordance that exposes it: **hide REPORTS → watch M42 shrink** → teaches "M42 looked central because it contains reported speech." This is the instrument revealing something about the METHOD (§2.8) → flag to Method/Atlas Reader.

Seven priorities:
- [ ] **1. Never scroll away on selection** — persistent side/bottom inspector (same as Trace/Scan).
- [ ] **2. Selected move's actual TEXT stays visible** continuously, not just its M-number.
- [ ] **3. On selection, label every immediate edge with sub-type + direction** (M42 —REPORTS→ M43).
- [ ] **4. Replace "7 links = hub" with a decomposition** — `7 links · 5 REPORTS · 2 other · reaches 2 regions`.
- [ ] **5. Teach that graph distance ≠ semantic/textual distance** — "Position shows network structure, not reading order or similarity; exact distances have no independent meaning" (force layout, D3). In the viz, not buried.
- [ ] **6. Make bridges / communities / isolates the payoff**, not big dots. Bridge (removal fragments the graph) = the close-reading question Map can pose that Scan can't. Isolate ("M31 · no coded linkage") = a negative-space result.
- [ ] **7. Relation-type toggle central** — turn REPORTS off, watch topology change (exposes taxonomy artifacts).
- Own proposition (#1/#20): **"See what groups together when reading order is removed."** REST → SELECT (neighborhood) → FOLLOW (recenter + breadcrumb M42→M47→M53) → ANALYZE (Bridges·Communities·Isolates·Hide-REPORTS). "Topology Lab."
- Bundle repetitive REPORTS fans (one "REPORTS fan" node, click to expand) so a speech-container reads as one thing, not 7 hubs.

**The trio, made complementary (use in the top copy):**
| View | Keeps reading order? | Best question |
|---|---|---|
| Trace | yes | Where does THIS move reach? |
| Scan | yes (matrix) | Where is the passage densely / distantly connected? |
| Map | **no** | What neighborhoods emerge when order is removed? |

## ⟐ NEW DIRECTION — Map = POSITION, nearest-neighbor across the atlas (PI, 2026-08-14)
> "Map would be very interesting connected to **position** — each Mark 16 move's **8-coordinate**, mapped against the morphospace, and see its **nearest neighbors**. The 10 closest positions, then explore those, and eventually across the entire atlas reader. Ask the atlas reader about the 'nearest neighbor' idea."

This is a **second, thesis-aligned Map** distinct from the within-passage Topology Lab:
- **Map-A (Topology Lab):** within-passage LINKAGE graph (the crit above) — "what groups in THIS passage."
- **Map-B (Position Map):** each move plotted by its **8-coordinate frame position** in the morphospace; **k-nearest-neighbors** across ALL coded moves/traditions → the cross-tradition **rhyme** view (Q2 convergence). "What rhymes with this move, anywhere in the atlas?"
Map-B is the stronger "Map" for the thesis (rhyme = nearest neighbor in position-space). **Depends on Atlas Reader:** (a) per-move 8-coordinate present in the atlas, (b) a k-NN feed (10 closest, expandable). Asked Atlas Reader 2026-08-14.

<!-- appended round -->

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
