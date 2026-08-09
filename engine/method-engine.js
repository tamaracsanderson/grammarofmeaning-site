/* ===========================================================================
   THE METHOD ENGINE — static renderer. Vanilla JS, no dependencies, no build.

   Reads window.METHOD_FLOW (inlined in method-engine.html so the file opens
   over file://). On a server you can instead do:
       window.METHOD_FLOW = await (await fetch('./method_flow.json')).json();

   The DOM it emits is identical to the React tree in
   src/components/method-engine/*, and the geometry below is a straight
   transliteration of src/components/method-engine/geometry.ts — same anchor
   map, same d-strings.
   =========================================================================== */

const FLOW = window.METHOD_FLOW;
const byId = Object.fromEntries(FLOW.nodes.map((n) => [n.id, n]));
const inBand = (b) => FLOW.nodes.filter((n) => n.band === b);
const LEAVES = inBand("situate");
const CONNECT_PILLS = inBand("connect"); // the 3 edge-kind pills (Linkage / Resonance / Constellation)
const WI = inBand("band_wi");
const MC = inBand("band_mc");

/* ---------------------------------------------------------------- geometry */

function anchorFrom(el, base) {
  const r = el.getBoundingClientRect();
  return {
    left: r.left - base.left,
    right: r.right - base.left,
    top: r.top - base.top,
    bottom: r.bottom - base.top,
    cx: r.left - base.left + r.width / 2,
    cy: r.top - base.top + r.height / 2,
  };
}

function flowPath(a, b) {
  const x1 = a.right, y1 = a.cy, x2 = b.left - 5, y2 = b.cy;
  const k = Math.max(28, (x2 - x1) * 0.45);
  return `M ${x1} ${y1} C ${x1 + k} ${y1}, ${x2 - k} ${y2}, ${x2} ${y2}`;
}

function railPath(src, tiles, railY) {
  const x1 = src.right, y1 = src.cy;
  const xClimb = x1 + 56;
  const xEnd = tiles.length ? Math.max(...tiles.map((t) => t.left)) - 14 : xClimb + 200;
  const trunk =
    `M ${x1} ${y1} C ${x1 + 26} ${y1}, ${xClimb - 16} ${railY}, ${xClimb} ${railY}` +
    ` L ${xEnd} ${railY}`;
  const taps = tiles.map((t, i) => {
    const tx = Math.max(xClimb + 24, t.left - 16 - i * 9);
    const my = (railY + t.cy) / 2;
    return `M ${tx} ${railY} C ${tx} ${my}, ${tx} ${t.top - 8}, ${t.cx} ${t.top - 4}`;
  });
  return { trunk, taps };
}

function trunkPath(waist, tiles) {
  const x1 = waist.right, y1 = waist.cy;
  const stemX = tiles.length ? Math.min(...tiles.map((t) => t.left)) - 34 : x1 + 60;
  const trunk = `M ${x1} ${y1} L ${stemX} ${y1}`;
  const branches = tiles.map((t) => {
    const x2 = t.left - 5;
    const k = Math.max(14, (x2 - stemX) * 0.5);
    return `M ${stemX} ${y1} C ${stemX + k} ${y1}, ${x2 - k} ${t.cy}, ${x2} ${t.cy}`;
  });
  return { trunk, branches };
}

function mirrorPath(gap, target) {
  const x1 = gap.cx, y1 = gap.bottom, x2 = target.cx, y2 = target.top - 4;
  const k = Math.max(16, (y2 - y1) * 0.6);
  return `M ${x1} ${y1} C ${x1} ${y1 + k}, ${x2} ${y2 - k}, ${x2} ${y2}`;
}

/* ------------------------------------------------------------------- state */

const state = {
  mode: "method", // one view; the METHOD/AUDIT toggle was retired per PI S162 (status → inline dot + drawer + the Reflexive-audit node)
  focused: null,
  open: null,
};

/* -------------------------------------------------------------------- util */

function el(tag, cls, text) {
  const n = document.createElement(tag);
  if (cls) n.className = cls;
  if (text != null) n.textContent = text;
  return n;
}
const svgEl = (tag) => document.createElementNS("http://www.w3.org/2000/svg", tag);

/* ------------------------------------------------------------- node button */

function nodeCard(node, variant) {
  const b = el("button", `me-node is-${variant || "card"} is-${node.status}`);
  b.type = "button";
  b.dataset.id = node.id;

  const label = el("span", "me-node-label");
  label.appendChild(el("span", `me-status-dot is-${node.status}`));
  label.appendChild(document.createTextNode(node.label));
  if (node.rendered) label.appendChild(el("span", "me-rendered", "↳ rendered"));
  b.appendChild(label);
  b.appendChild(el("span", "me-node-fn", node.function));
  // one view: the status dot above is the lightweight canvas signal; full detail lives one click into the drawer

  b.addEventListener("click", () => openDrawer(node.id));
  b.addEventListener("mouseenter", () => setFocus(node.id));
  b.addEventListener("mouseleave", () => setFocus(null));
  b.addEventListener("focus", () => setFocus(node.id));
  b.addEventListener("blur", () => setFocus(null));
  return b;
}

function bandHead(label, note) {
  const h = el("header", "me-band-head");
  h.appendChild(el("span", "me-band-label", label));
  h.appendChild(el("span", "me-band-note", note));
  return h;
}

function bandRow(band, tiles) {
  const s = el("section", `me-band is-${band.tone}`);
  s.dataset.band = band.id;
  s.appendChild(bandHead(band.label, band.note));
  const row = el("div", "me-band-tiles");
  tiles.forEach((n) => row.appendChild(nodeCard(n, "tile")));
  s.appendChild(row);
  return s;
}

function gapMirror() {
  const s = el("section", "me-mirror");
  s.dataset.band = "mirror";
  s.appendChild(bandHead("The gap mirror", "same gap · two kinds of voice"));
  const gapWrap = el("div", "me-mirror-gap");
  gapWrap.appendChild(nodeCard(byId["gap"]));
  s.appendChild(gapWrap);

  const arms = el("div", "me-mirror-arms");
  [["gloss", "the instrument's voices · constructed", " is-grammar"],
   ["reception", "the tradition's voices · retrieved", " is-canon"]].forEach(([id, side, extra]) => {
    const arm = el("div", `me-mirror-arm${extra}`);
    arm.appendChild(nodeCard(byId[id]));
    arm.appendChild(el("span", "me-mirror-side", side));
    arms.appendChild(arm);
  });
  s.appendChild(arms);
  s.appendChild(el("p", "me-mirror-caption", "where they diverge is the finding"));
  return s;
}

/* --------------------------------------------------------- the panel (U1) */
/* The panel is the invention — it must have pixels. A visible cluster on the
   Selected-gap → Synthesis path: nominate 42 → two CHAIRS as parallel tracks
   (convergence ∥ divergence) → pick-top → the symmetric-difference FINDING. */
function panelCluster() {
  const s = el("section", "me-panel");
  s.dataset.band = "panel";
  s.appendChild(bandHead("The panel", "the invention: the argument gets made here"));
  const nom = el("div", "me-panel-beat");
  nom.appendChild(nodeCard(byId["nominate"]));
  s.appendChild(nom);
  s.appendChild(el("div", "me-panel-conn", "▾"));
  const tracks = el("div", "me-panel-tracks");
  [["chair_convergence", "develops-with"], ["chair_divergence", "reads-against"]].forEach(([id, tag]) => {
    const t = el("div", "me-panel-track");
    t.appendChild(nodeCard(byId[id]));
    t.appendChild(el("span", "me-panel-track-tag", tag));
    tracks.appendChild(t);
  });
  s.appendChild(tracks);
  s.appendChild(el("div", "me-panel-conn", "▾"));
  // U2 — the fidelity gate: a small standalone glyph on the glosses' path into pick-top;
  //      glosses can DIE here (S6 / DP-5) — "no-grounded-gloss" is an allowable verdict.
  const gate = el("div", "me-panel-gate");
  gate.appendChild(nodeCard(byId["fidelity_gate"]));
  s.appendChild(gate);
  const pk = el("div", "me-panel-beat");
  pk.appendChild(nodeCard(byId["pick_top"]));
  s.appendChild(pk);
  s.appendChild(el("div", "me-panel-conn", "▾"));
  const fnd = el("div", "me-panel-beat");
  fnd.appendChild(nodeCard(byId["the_finding"]));
  s.appendChild(fnd);
  return s;
}

/* ----------------------------------------------------------------- legend */

function renderLegend() {
  const host = document.getElementById("me-legend");
  host.textContent = "";
  Object.entries(FLOW.meta.edgeTypes).forEach(([key, desc]) => {
    const item = el("span", "me-legend-item");
    item.appendChild(el("span", `me-legend-rule is-${key}`));
    item.appendChild(document.createTextNode(key.replace("_", "-")));
    item.appendChild(el("span", "me-legend-desc", `${desc}`));
    host.appendChild(item);
  });
  const item = el("span", "me-legend-item is-quiet");
  item.appendChild(el("span", "me-legend-dot is-populated"));
  item.appendChild(
    document.createTextNode(
      "build-status dot: operational, not epistemic; click a node for detail",
    ),
  );
  host.appendChild(item);
}

/* ----------------------------------------------------------------- figure */

function renderFigure() {
  const fig = document.getElementById("me-figure");
  fig.textContent = "";
  fig.dataset.mode = state.mode;

  const svg = svgEl("svg");
  svg.setAttribute("class", "me-edges");
  svg.setAttribute("aria-hidden", "true");
  const defs = svgEl("defs");
  [["waist_independent", "--me-moss", 8, 6],
   ["move_conditioned", "--me-fern", 7, 4.5],
   ["flow", "--me-olive", 8, 6]].forEach(([type, token, refX, size]) => {
    const m = svgEl("marker");
    m.setAttribute("id", `me-arrow-${type}`);
    m.setAttribute("viewBox", "0 0 10 10");
    m.setAttribute("refX", String(refX));
    m.setAttribute("refY", "5");
    m.setAttribute("markerWidth", String(size));
    m.setAttribute("markerHeight", String(size));
    m.setAttribute("orient", "auto-start-reverse");
    const p = svgEl("path");
    p.setAttribute("d", "M 0 1 L 9 5 L 0 9 z");
    p.setAttribute("fill", `var(${token})`);
    m.appendChild(p);
    defs.appendChild(m);
  });
  svg.appendChild(defs);
  fig.appendChild(svg);

  const lane = el("div", "me-rail-lane");
  lane.dataset.band = "rail";
  // #8 — the band heading carries the name; the rail is not labelled separately
  fig.appendChild(lane);

  const grid = el("div", "me-grid");

  // cone
  const cone = el("div", "me-col me-cone");
  cone.appendChild(nodeCard(byId["text"]));
  const branches = el("div", "me-branches");
  branches.appendChild(nodeCard(byId["decompose"]));
  // Connect — the reconstruction half (wire the moves back together); pairs with Decompose, sits between it and Situate.
  // Guarded: a missing node (e.g. a stale cached method_flow.json) must not blank the whole figure.
  if (byId["connect"]) {
    const connectBox = el("div", "me-situate");
    connectBox.appendChild(nodeCard(byId["connect"]));
    const cpills = el("div", "me-situate-pills");
    CONNECT_PILLS.forEach((n) => {
      const pill = el("button", `me-situate-pill is-${n.status}`);
      pill.type = "button";
      pill.dataset.id = n.id;
      pill.appendChild(el("span", `me-status-dot is-${n.status}`));
      pill.appendChild(document.createTextNode(n.label));
      pill.addEventListener("click", (e) => { e.stopPropagation(); openDrawer(n.id); });
      cpills.appendChild(pill);
    });
    connectBox.appendChild(cpills);
    branches.appendChild(connectBox);
  }
  const situate = el("div", "me-situate");
  situate.appendChild(nodeCard(byId["situate"]));
  // the 5 aspects are parallel lenses, not a sequence: a compact clickable pill row, each opening its own drawer
  const pills = el("div", "me-situate-pills");
  LEAVES.forEach((n) => {
    const pill = el("button", `me-situate-pill is-${n.status}`);
    pill.type = "button";
    pill.dataset.id = n.id;
    pill.appendChild(el("span", `me-status-dot is-${n.status}`));
    pill.appendChild(document.createTextNode(n.label));
    pill.addEventListener("click", (e) => { e.stopPropagation(); openDrawer(n.id); });
    pills.appendChild(pill);
  });
  situate.appendChild(pills);
  branches.appendChild(situate);
  cone.appendChild(branches);
  grid.appendChild(cone);

  // waist
  const gutter = el("div", "me-col me-gutter");
  gutter.appendChild(nodeCard(byId["enriched_move"], "waist"));
  gutter.appendChild(
    el("p", "me-gutter-note", "Decompose segments · Connect wires · Situate annotates"),
  );
  grid.appendChild(gutter);

  // fan
  const fan = el("div", "me-col me-fan");
  const bandWi = FLOW.meta.bands.find((b) => b.id === "band_wi");
  const bandMc = FLOW.meta.bands.find((b) => b.id === "band_mc");
  fan.appendChild(bandRow(bandWi, WI));
  fan.appendChild(bandRow(bandMc, MC));
  fan.appendChild(gapMirror());
  fan.appendChild(panelCluster());
  grid.appendChild(fan);

  // end
  const end = el("div", "me-col me-end");
  end.appendChild(nodeCard(byId["synthesis"]));
  end.appendChild(nodeCard(byId["reading_room"]));
  end.appendChild(el("p", "me-end-note", "terminal delivery"));
  grid.appendChild(end);

  fig.appendChild(grid);

  const strip = document.getElementById("me-strip");
  strip.textContent = "";
  strip.appendChild(el("span", "me-strip-label", "off the flow"));
  strip.appendChild(nodeCard(byId["reflexive"], "strip"));
  strip.appendChild(
    el("span", "me-strip-note", (byId["reflexive"].layers || []).join(" · ")),
  );

  drawEdges();
}

/* ------------------------------------------------------------------ edges */

let EDGE_PATHS = [];

function drawEdges() {
  const fig = document.getElementById("me-figure");
  const svg = fig.querySelector(".me-edges");
  if (!svg) return;
  const base = fig.getBoundingClientRect();
  const anchors = {};
  fig.querySelectorAll("[data-id]").forEach((n) => {
    anchors[n.dataset.id] = anchorFrom(n, base);
  });
  fig.querySelectorAll("[data-band]").forEach((n) => {
    anchors[`band:${n.dataset.band}`] = anchorFrom(n, base);
  });

  svg.setAttribute("width", String(Math.max(1, base.width)));
  svg.setAttribute("height", String(Math.max(1, base.height)));
  svg.querySelectorAll("path.me-edge").forEach((p) => p.remove());

  const a = (id) => anchors[id];
  const out = [];

  FLOW.edges.filter((e) => e.type === "flow").forEach((e) => {
    const from = a(e.from), to = a(e.to);
    if (!from || !to) return;
    out.push({
      key: `flow-${e.from}-${e.to}`,
      d: flowPath(from, to),
      type: "flow",
      nodes: [e.from, e.to],
      status: byId[e.to].status,
    });
  });

  const railLane = a("band:rail");
  const src = a("text");
  const wiTiles = WI.map((n) => a(n.id)).filter(Boolean);
  if (railLane && src && wiTiles.length === WI.length) {
    const rail = railPath(src, wiTiles, railLane.cy);
    out.push({
      key: "rail-trunk",
      d: rail.trunk,
      type: "waist_independent",
      nodes: ["text", ...WI.map((n) => n.id), ...LEAVES.map((n) => n.id)],
      status: "specified",
      noArrow: true,
    });
    rail.taps.forEach((d, i) => {
      const tile = WI[i];
      const source = FLOW.edges.find(
        (e) => e.to === tile.id && e.type === "waist_independent",
      );
      out.push({
        key: `rail-tap-${tile.id}`,
        d,
        type: "waist_independent",
        nodes: [tile.id, source ? source.from : "text"],
        status: tile.status,
      });
    });
  }

  const waist = a("enriched_move");
  const mcTiles = MC.map((n) => a(n.id)).filter(Boolean);
  if (waist && mcTiles.length === MC.length) {
    const t = trunkPath(waist, mcTiles);
    out.push({
      key: "waist-trunk",
      d: t.trunk,
      type: "move_conditioned",
      nodes: ["enriched_move", ...MC.map((n) => n.id)],
      status: "populated",
      noArrow: true,
    });
    t.branches.forEach((d, i) => {
      out.push({
        key: `waist-branch-${MC[i].id}`,
        d,
        type: "move_conditioned",
        nodes: ["enriched_move", MC[i].id],
        status: MC[i].status,
      });
    });
  }

  const gap = a("gap");
  if (waist && gap) {
    out.push({
      key: "waist-gap",
      d: flowPath(waist, gap),
      type: "move_conditioned",
      nodes: ["enriched_move", "gap"],
      status: byId["gap"].status,
    });
    ["gloss", "reception"].forEach((id) => {
      const target = a(id);
      if (!target) return;
      out.push({
        key: `mirror-${id}`,
        d: mirrorPath(gap, target),
        type: "move_conditioned",
        nodes: ["gap", id],
        status: byId[id].status,
      });
    });
  }

  EDGE_PATHS = out;
  out.forEach((p) => {
    const path = svgEl("path");
    path.setAttribute("class", `me-edge is-${p.type} is-${p.status}`);
    path.setAttribute("d", p.d);
    path.dataset.nodes = p.nodes.join(" ");
    if (!p.noArrow) path.setAttribute("marker-end", `url(#me-arrow-${p.type})`);
    svg.appendChild(path);
  });

  applyFocus();
}

/* ------------------------------------------------------------------ focus */

function setFocus(id) {
  state.focused = id;
  applyFocus();
}

function applyFocus() {
  const fig = document.getElementById("me-figure");
  const id = state.focused;
  fig.classList.toggle("is-focused", Boolean(id));

  const neighbours = new Set();
  if (id) {
    neighbours.add(id);
    FLOW.edges.forEach((e) => {
      if (e.from === id) neighbours.add(e.to);
      if (e.to === id) neighbours.add(e.from);
    });
  }
  fig.querySelectorAll("[data-id]").forEach((n) => {
    n.classList.toggle("is-traced", Boolean(id) && neighbours.has(n.dataset.id));
  });
  fig.querySelectorAll("path.me-edge").forEach((p) => {
    const nodes = (p.dataset.nodes || "").split(" ");
    p.classList.toggle("is-traced", Boolean(id) && nodes.includes(id));
  });
}

/* ----------------------------------------------------------------- drawer */

function openDrawer(id) {
  state.open = id;
  const node = byId[id];
  const host = document.getElementById("me-drawer-host");
  host.textContent = "";

  const scrim = el("button", "me-scrim");
  scrim.setAttribute("aria-label", "Close");
  scrim.addEventListener("click", closeDrawer);
  host.appendChild(scrim);

  const aside = el("aside", "me-drawer");
  aside.setAttribute("role", "dialog");
  aside.setAttribute("aria-label", node.label);

  const close = el("button", "me-drawer-close", "×");
  close.setAttribute("aria-label", "Close");
  close.addEventListener("click", closeDrawer);
  aside.appendChild(close);

  // a sequence step + the stage — tells you WHERE you are in the walk; never the internal "kind"
  const STAGE = {
    input: "INPUT", grammar: "ANALYZE", situate: "SITUATE", waist: "THE WAIST",
    band_wi: "OUTPUT · doesn’t need the move", band_mc: "OUTPUT · needs the move",
    mirror: "THE GAP MIRROR", canon: "THE GAP MIRROR", panel: "THE PANEL",
    end: "SYNTHESIS → READING ROOM", strip: "OFF THE FLOW", history: "RETIRED",
  };
  const stage = node.stage || STAGE[node.band] || String(node.band || "").toUpperCase();
  const kicker = el("p", "me-kicker", node.step ? ("STEP " + node.step + " · " + stage) : stage);
  kicker.style.margin = "0";
  aside.appendChild(kicker);
  aside.appendChild(el("h2", null, node.label));
  aside.appendChild(el("p", "me-drawer-fn", node.function));

  // Golden-path step drawers: fully custom, rendered from each step's generated file (the neutral feed)
  if (STEP_DATA[id]) { renderStepDrawer(aside, node); host.appendChild(aside); return; }

  if (node.sub) aside.appendChild(el("p", "me-drawer-sub", node.sub));

  // honest status pill — never claim built-what-isn't (§13)
  if (node.status_pill) aside.appendChild(el("p", "me-drawer-pill", node.status_pill));

  // Layer 1 — plain "what it is / why it matters / how it works" (any node may carry these)
  [["What it is", node.what_it_is], ["Why it matters", node.why_it_matters], ["How it works", node.logic]]
    .forEach(function (row) {
      if (!row[1]) return;
      var s = el("div", "me-drawer-section");
      s.appendChild(el("h3", null, row[0]));
      s.appendChild(el("p", "me-drawer-p", row[1]));
      aside.appendChild(s);
    });


  const incoming = FLOW.edges.filter((e) => e.to === node.id);
  const outgoing = FLOW.edges.filter((e) => e.from === node.id);
  const labelOf = (nid) => (byId[nid] ? byId[nid].label : nid);

  // "What's inside" — the step's parts / sub-outputs, in plain view
  if (node.layers && node.layers.length) {
    const s = el("div", "me-drawer-section");
    s.appendChild(el("h3", null, "What’s inside"));
    const ul = el("ul", "me-drawer-list");
    node.layers.forEach((l) => ul.appendChild(el("li", null, l)));
    s.appendChild(ul);
    aside.appendChild(s);
  }

  // "Leads to" — where this step goes next, in plain words
  if (outgoing.length) {
    const s = el("div", "me-drawer-section");
    s.appendChild(el("h3", null, "Leads to"));
    s.appendChild(el("p", "me-drawer-p", outgoing.map((e) => labelOf(e.to)).join("  ·  ")));
    aside.appendChild(s);
  }

  // the engineering detail (build status, dependency, metadata, edges): always available, one click into the drawer
  {
    const meta = el("div", "me-drawer-meta");
    meta.appendChild(el("span", null, `grain ${node.grain}`));
    meta.appendChild(el("span", null, `impl ${node.implementation}`));
    meta.appendChild(el("span", null, `validation ${node.validation}`));
    const statusSpan = el("span");
    statusSpan.appendChild(el("span", `me-status-dot is-${node.status}`));
    statusSpan.appendChild(
      document.createTextNode(`${node.status}: ${FLOW.meta.maturity[node.status]}`),
    );
    meta.appendChild(statusSpan);
    aside.appendChild(meta);

    const dep = incoming.find(
      (e) => e.type === "waist_independent" || e.type === "move_conditioned",
    );
    const depSection = el("div", "me-drawer-section");
    depSection.appendChild(el("h3", null, "Waist dependency"));
    const depP = el("p", "me-drawer-p");
    if (dep) {
      depP.appendChild(el("span", `me-kind-tag is-${dep.type}`, dep.type.replace("_", "-")));
      depP.appendChild(el("br"));
      depP.appendChild(document.createTextNode(FLOW.meta.edgeTypes[dep.type]));
    } else {
      depP.textContent = "structural: part of the spine, not an output.";
    }
    depSection.appendChild(depP);
    aside.appendChild(depSection);

    if (node.badge) {
      const s = el("div", "me-drawer-section");
      s.appendChild(el("h3", null, "Implementation note"));
      s.appendChild(el("span", "me-badge is-block", node.badge));
      aside.appendChild(s);
    }
    const req = node.requires || [];
    const prod = node.produces || [];
    if (req.length + prod.length > 0) {
      const s = el("div", "me-drawer-section");
      s.appendChild(el("h3", null, "Dependency metadata"));
      const p = el("p", "me-drawer-p");
      p.appendChild(document.createTextNode(`requires: ${req.length ? req.join(" · ") : "none"}`));
      p.appendChild(el("br"));
      p.appendChild(document.createTextNode(`produces: ${prod.length ? prod.join(" · ") : "none"}`));
      s.appendChild(p);
      aside.appendChild(s);
    }
    if (incoming.length + outgoing.length > 0) {
      const s = el("div", "me-drawer-section");
      s.appendChild(el("h3", null, "Edges"));
      const ul = el("ul", "me-drawer-list");
      const row = (arrow, other, e) => {
        const li = el("li");
        li.appendChild(document.createTextNode(`${arrow} ${labelOf(other)} · `));
        li.appendChild(el("span", `me-kind-tag is-${e.type}`, e.type.replace("_", "-")));
        if (e.note) li.appendChild(document.createTextNode(`: ${e.note}`));
        return li;
      };
      incoming.forEach((e) => ul.appendChild(row("◄", e.from, e)));
      outgoing.forEach((e) => ul.appendChild(row("►", e.to, e)));
      s.appendChild(ul);
      aside.appendChild(s);
    }
  }

  host.appendChild(aside);
}

function closeDrawer() {
  state.open = null;
  document.getElementById("me-drawer-host").textContent = "";
}

/* ---- Golden-path step drawers: render from each step's single generated file (the neutral feed) ---- */
var STEP_DATA = { text: "text_node_drawer.json", decompose: "decompose_node_drawer.json" };
var STEP_CACHE = {}, CHECKOUT = null;
function cleanVerbatim(t) {
  if (!t) return "";
  var s = String(t)
    .replace(/\r?\n\s*/g, " ")
    .replace(/\d{3}:\d{3}\s*/g, "") // strip chunk-internal verse markers (015:044 …) for readability
    .replace(/\s+/g, " ")
    .trim();
  if (s.length > 2000) s = s.slice(0, 2000).replace(/\s+\S*$/, "") + " …"; // cap only huge text, always at a word boundary
  return s;
}
function verseRange(ids) {
  if (!ids || !ids.length) return "";
  var f = ids[0].split(":").map(function (x) { return parseInt(x, 10); });
  var l = ids[ids.length - 1].split(":").map(function (x) { return parseInt(x, 10); });
  return f[0] + ":" + f[1] + "–" + (l[0] === f[0] ? l[1] : l[0] + ":" + l[1]);
}
/* one shell for every golden-path step drawer; per-step layer-2 renderers below */
/* the golden-path forward chain (for the "What's next" arrows) + a loud-red WIP badge (standard element) */
var GP_ORDER = ["text", "decompose", "situate", "enriched_move"];
var GP_LABEL = { text: "Text", decompose: "Decompose", situate: "Situate", enriched_move: "Enriched move" };
function nextChain(id) {
  var i = GP_ORDER.indexOf(id);
  if (i < 0) return "";
  return GP_ORDER.slice(i, i + 3).map(function (k) { return GP_LABEL[k]; }).join(" → ");
}
function wipBadge(text) { return el("p", "me-wip-badge", text); }

/* status pills near the title — render whichever of fidelity / crt (Cold Read) / vs_wild the card carries.
   PASS = green; PENDING = amber (honest: not yet re-run, never a false green); PARTIAL/FAIL = terracotta. */
function renderStatusPills(host, D) {
  var order = [["fidelity", "Fidelity"], ["crt", "Cold Read"], ["vs_wild", "vs-Wild"]];
  var wrap = el("div", "me-crt"), any = false;
  order.forEach(function (pair) {
    var p = D[pair[0]];
    if (!p || !p.status) return;
    any = true;
    var s = String(p.status).toUpperCase();
    var pill = el("span", "me-crt-pill is-" + s.toLowerCase(),
      pair[1] + ": " + s + (p.date ? " · " + p.date : ""));
    if (p.meta_line) pill.setAttribute("title", p.meta_line);
    wrap.appendChild(pill);
  });
  if (!any) return;
  if (D.crt && D.crt.checks) wrap.appendChild(el("span", "me-crt-checks", "checked: " + D.crt.checks));
  host.appendChild(wrap);
  // the run doc is a repo path (not web-served), so surface it as a visible path, not a 404-ing link
  if (D.crt && D.crt.run_doc) host.appendChild(el("p", "me-crt-run", "run: " + D.crt.run_doc));
}

/* Foundation (template section 11): the established scholarship each part of the method stands on, stated openly.
   Serves both cards (frameworks[].grounds is an array on Decompose, a string on Text — handle both). */
function renderFoundation(host, f) {
  if (!f || !(f.note || (f.frameworks && f.frameworks.length) || (f.prior_work && f.prior_work.length))) return;
  var s = el("div", "me-drawer-section me-foundation");
  s.appendChild(el("h3", null, "Foundation"));
  if (f.note) s.appendChild(el("p", "me-drawer-p", f.note));
  if (f.frameworks && f.frameworks.length) {
    var ul = el("ul", "me-drawer-list");
    f.frameworks.forEach(function (fw) {
      var li = el("li");
      li.appendChild(el("b", "me-fw-name", fw.framework || ""));
      var grounds = Array.isArray(fw.grounds) ? fw.grounds.join(", ") : fw.grounds;
      if (grounds) li.appendChild(document.createTextNode(": " + grounds));
      ul.appendChild(li);
    });
    s.appendChild(ul);
  }
  if (f.prior_work && f.prior_work.length) {
    s.appendChild(el("p", "me-drawer-caption", "Prior work"));
    var pw = el("ul", "me-drawer-list");
    f.prior_work.forEach(function (x) { pw.appendChild(el("li", null, x)); });
    s.appendChild(pw);
  }
  host.appendChild(s);
}

/* §2.14 out-of-domain validation: the same grammar re-coded on other texts (a different language, a different
   genre), each catching a category Mark 16 barely uses — evidence it's an instrument, not an English-narrative tool */
function renderValidatedOn(host, vo) {
  if (!vo || !(vo.texts && vo.texts.length)) return;
  var s = el("div", "me-drawer-section me-validated");
  s.appendChild(el("h3", null, "Validated out-of-domain"));
  if (vo.note) s.appendChild(el("p", "me-drawer-p", vo.note));
  var list = el("div", "me-val-list");
  vo.texts.forEach(function (t) {
    var row = el("div", "me-val-row");
    var head = el("p", "me-val-head");
    head.appendChild(el("b", null, t.label || t.source_key || ""));
    if (t.axis) head.appendChild(el("span", "me-val-axis", " (" + t.axis + ")"));
    row.appendChild(head);
    var bits = [];
    if (t.moves != null) bits.push(t.moves + " moves");
    if (t.signal_field) bits.push(t.signal_field + "=" + t.signal_value + (t.signal_count != null ? " ×" + t.signal_count : ""));
    if (bits.length) row.appendChild(el("p", "me-val-signal", bits.join(" · ")));
    if (t.note) row.appendChild(el("p", "me-val-note", t.note));
    list.appendChild(row);
  });
  s.appendChild(list);
  host.appendChild(s);
}

/* THE MOVE-GRAMMAR v2 (Decision 223): a funnel (process_type, asked FIRST) + 5 core parts
   (narrator/agent/operation/substrate/outcome) + 12 modifiers grouped under their part.
   Anatomy = the clean contract (renderGrammar); worked list = the grammar applied (moveBlock). */

// the applied grammar per move: which modifiers hang off each core part (drives moveBlock)
var MOVE_PARTS = [
  { core: "narrator", mods: [["evidentiality", "narrator_evidentiality"], ["stance", "narrator_stance"], ["tone", "narrator_tone"]] },
  { core: "agent", mods: [["animacy", "agent_animacy"]] },
  { core: "operation", mods: [["type", "operation_type"], ["voice", "operation_voice"], ["modality", "operation_modality"], ["polarity", "operation_polarity"], ["force", "operation_force"]] },
  { core: "substrate", mods: [["kind", "substrate_kind"]] }, // case-roles handled specially below
  { core: "outcome", mods: [["realis", "outcome_realis"]] },
];
var SUBSTRATE_ROLES = [["on", "substrate_on"], ["to", "substrate_to"], ["of", "substrate_of"], ["with", "substrate_with"], ["in", "substrate_in"]];
function stated(v) { return v && v !== "not stated"; }

/* one move block: badge + plain + the funnel + the 5 core parts (orange) with their modifiers (green) */
function moveBlock(m) {
  var b = el("div", "me-move-block");
  var head = el("p", "me-move-head");
  head.appendChild(el("span", "me-move-badge", m.move || ""));
  head.appendChild(document.createTextNode(" " + (m.plain || "")));
  b.appendChild(head);
  if (m.process_type) {
    var f = el("p", "me-move-funnel");
    f.appendChild(el("b", null, "process ")); f.appendChild(document.createTextNode(m.process_type));
    b.appendChild(f);
  }
  var g = el("div", "me-move-grammar");
  MOVE_PARTS.forEach(function (p) {
    var value = p.core === "substrate"
      ? SUBSTRATE_ROLES.filter(function (r) { return stated(m[r[1]]); }).map(function (r) { return m[r[1]] + " (" + r[0] + ")"; }).join(", ")
      : m[p.core];
    var mods = p.mods.filter(function (md) { return stated(m[md[1]]); });
    if (!stated(value) && !mods.length) return;
    var row = el("div", "me-move-part");
    row.appendChild(el("b", "me-mp-core", p.core));
    if (stated(value)) row.appendChild(document.createTextNode(" " + value));
    mods.forEach(function (md) { row.appendChild(el("span", "me-mp-mod", md[0] + ": " + m[md[1]])); });
    g.appendChild(row);
  });
  if (g.children.length) b.appendChild(g);
  return b;
}
/* the grammar defined on the card (the clean contract): funnel first, then each core part (orange) with its
   modifiers grouped under it (green), each modifier showing its controlled-value contract (vocab · single/multi · candidate) */
/* the controlled-value contract for one field: show the full closed SET with the values THIS text used marked,
   the rest as legal-but-unused (muted); an open field shows its used values + an "open set" marker; candidates
   flagged as proposals. Returns a <p> element (mixed styling) or null. */
function vocabDisplay(m) {
  var v = m.vocab;
  if (!v) return null;
  var p = el("p", "me-gram-vocab");
  var addVals = function (vals, cls) {
    vals.forEach(function (val, i) {
      if (i) p.appendChild(document.createTextNode(" · "));
      p.appendChild(el("span", cls, val));
    });
  };
  if (Array.isArray(v)) {                    // legacy flat list (fallback)
    addVals(v, "me-vocab-used");
  } else {
    var used = v.used_here || [], usedSet = {};
    used.forEach(function (u) { usedSet[u] = true; });
    if (Array.isArray(v.set)) {               // closed set: used bold, unused muted
      v.set.forEach(function (val, i) {
        if (i) p.appendChild(document.createTextNode(" · "));
        p.appendChild(el("span", usedSet[val] ? "me-vocab-used" : "me-vocab-unused", val));
      });
    } else {                                  // open field: used values + open marker
      addVals(used, "me-vocab-used");
      p.appendChild(el("span", "me-vocab-open", (used.length ? " · " : "") + "open set"));
    }
    if (v.candidates_seen && v.candidates_seen.length) {
      p.appendChild(el("span", "me-vocab-cand", " · proposed: " + v.candidates_seen.join(", ")));
    }
  }
  var tag = [];
  if (m.single_or_multi) tag.push(m.single_or_multi);
  if (m.candidate) tag.push("candidate: " + m.candidate);
  if (tag.length) p.appendChild(el("span", "me-vocab-policy", "  (" + tag.join(" · ") + ")"));
  return p;
}
function renderGrammar(g) {
  var wrap = el("div", "me-grammar");
  if (g.funnel) {
    var fn = el("div", "me-gram-funnel");
    var fr = el("p", "me-gram-row");
    fr.appendChild(el("b", "me-def-part", g.funnel.handle));
    fr.appendChild(document.createTextNode(" " + (g.funnel.definition || "")));
    fn.appendChild(fr);
    var fv = vocabDisplay(g.funnel); if (fv) fn.appendChild(fv);
    wrap.appendChild(fn);
  }
  (g.core || []).forEach(function (c) {
    var cr = el("p", "me-gram-row");
    cr.appendChild(el("b", "me-def-part", c.handle));
    cr.appendChild(document.createTextNode(" " + (c.definition || "")));
    wrap.appendChild(cr);
    (g.modifiers || []).filter(function (md) { return md.part === c.handle; }).forEach(function (md) {
      var block = el("div", "me-gram-mod");
      var mr = el("p", "me-gram-mod-row");
      mr.appendChild(el("b", "me-def-mod", md.handle));
      mr.appendChild(document.createTextNode(" " + (md.definition || "")));
      block.appendChild(mr);
      var vd = vocabDisplay(md); if (vd) block.appendChild(vd);
      wrap.appendChild(block);
    });
  });
  return wrap;
}

function renderStepDrawer(aside, node) {
  var id = node.id;
  var host = el("div", "me-checkout");
  host.appendChild(el("p", "me-drawer-p", "loading…"));
  aside.appendChild(host);
  var paint = function () {
    var D = STEP_CACHE[id] || {};
    host.textContent = "";
    renderStatusPills(host, D); // fidelity / cold-read / vs-wild pills near the title
    // normalize v2-flat / v1-nested so one shell serves both shapes
    var card = D.card || {}, L1 = D.layer_1_what_it_is || {}, L3 = D.layer_3_evidence || {};
    var whatItIs = D.what_it_is || L1.what_it_is;
    var whyItMatters = D.why_it_matters || L1.why_it_matters;
    var howItWorks = D.how_it_works || L1.the_process;
    var onMark = D.on_mark_16 || D.layer_2_on_mark_16 || {};
    var limits = D.honest_limits || L3.honest_limits || [];
    var madeBy = D.made_by || L3.made_by;
    var whatsNext = D.whats_next || D.whats_next_plain;
    var receipt = (D.research_view && D.research_view.receipt) || null;
    var dataSource = (D.research_view && D.research_view.data_source) ||
      ((D._reads_from ? Object.keys(D._reads_from).map(function (k) { return D._reads_from[k]; }).join(" · ") + " · " : "") + "generated by " + (D._generated_by || "unknown"));
    var sect = function (h, p) { if (!p) return; var s = el("div", "me-drawer-section"); s.appendChild(el("h3", null, h)); s.appendChild(el("p", "me-drawer-p", p)); host.appendChild(s); };

    // WIP badge only for genuinely-pending items (loud red); else the plain status line
    if (D.wip) host.appendChild(wipBadge(typeof D.wip === "string" ? D.wip : "work in progress"));
    else if (card.status_tag) host.appendChild(el("p", "me-drawer-pill", card.status_tag));
    if (card.status_plain) host.appendChild(el("p", "me-drawer-sub", card.status_plain));

    // What it is / Why it matters / How it works
    sect("What it is", whatItIs);
    sect("Why it matters", whyItMatters);
    if (howItWorks && typeof howItWorks === "object") {
      var sp = el("div", "me-drawer-section"); sp.appendChild(el("h3", null, "How it works"));
      var up = el("ul", "me-drawer-list");
      Object.keys(howItWorks).forEach(function (k) { up.appendChild(el("li", null, k + ": " + howItWorks[k])); });
      sp.appendChild(up); host.appendChild(sp);
    } else if (howItWorks) sect("How it works", howItWorks);

    // the worked result on Mark 16 (per step)
    if (id === "text") renderLayer2Text(host, onMark);
    else if (id === "decompose") renderLayer2Decompose(host, onMark);

    // §2.14 out-of-domain validation (top-level; currently Decompose) — the instrument tested on other texts
    if (D.validated_on) renderValidatedOn(host, D.validated_on);

    // How it's stored (v2)
    if (D.how_stored) {
      var hs = el("div", "me-drawer-section"); hs.appendChild(el("h3", null, "How it's stored"));
      if (D.how_stored.plain) hs.appendChild(el("p", "me-drawer-p", D.how_stored.plain));
      if (D.how_stored.passage_types && D.how_stored.passage_types.length) {
        var pu = el("ul", "me-drawer-list"); D.how_stored.passage_types.forEach(function (x) { pu.appendChild(el("li", null, x)); }); hs.appendChild(pu);
      }
      if (D.how_stored.how_chapter_16_is_stored) hs.appendChild(el("p", "me-drawer-p", D.how_stored.how_chapter_16_is_stored));
      if (D.how_stored.this_checkout) hs.appendChild(el("p", "me-drawer-p", D.how_stored.this_checkout));
      if (D.how_stored.level_legend) hs.appendChild(el("p", "me-drawer-caption", D.how_stored.level_legend));
      host.appendChild(hs);
    }

    // Where the work is saved (v2) — the registered home (both sides); no WIP badge since it's live
    if (D.where_saved) {
      var ws = el("div", "me-drawer-section"); ws.appendChild(el("h3", null, "Where the work is saved"));
      if (D.where_saved.plain) ws.appendChild(el("p", "me-drawer-p", D.where_saved.plain));
      var home = D.where_saved.home || {};
      if (home.table) {
        var hb = el("div", "me-home");
        hb.appendChild(el("span", "me-home-tag", (home.registered ? "✓ registered · " : "") + home.table + (home.checkout_id ? " · " + home.checkout_id : "")));
        var hg = el("div", "me-home-grid");
        var side = function (label, s) {
          if (!s) return null;
          var c = el("div", "me-home-side");
          c.appendChild(el("span", "me-home-side-t", label));
          c.appendChild(el("p", "me-home-side-b", (s.source_id || s.method_source_key || "") + (s.reads ? " → " + s.reads : "")));
          return c;
        };
        var a = side("library side", home.library_side); if (a) hg.appendChild(a);
        var b = side("method side", home.method_side); if (b) hg.appendChild(b);
        hb.appendChild(hg); ws.appendChild(hb);
      }
      host.appendChild(ws);
    }

    // The contract — what the checkout guarantees now (locked) + what's future scope
    if (D.the_contract) {
      var tc = D.the_contract;
      var cs = el("div", "me-drawer-section me-contract");
      cs.appendChild(el("h3", null, "The contract"));
      if (tc.note) cs.appendChild(el("p", "me-drawer-p", tc.note));
      if (tc.locked && tc.locked.length) {
        cs.appendChild(el("p", "me-contract-label is-locked", "✓ locked"));
        var lu = el("ul", "me-drawer-list"); tc.locked.forEach(function (x) { lu.appendChild(el("li", null, x)); }); cs.appendChild(lu);
      }
      if (tc.future && tc.future.length) {
        cs.appendChild(el("p", "me-contract-label is-future", "○ future scope"));
        var fu = el("ul", "me-drawer-list"); tc.future.forEach(function (x) { fu.appendChild(el("li", null, x)); }); cs.appendChild(fu);
      }
      host.appendChild(cs);
    }

    // Honest limits (strings v2 / {plain} v1)
    if (limits.length) {
      var hl = el("div", "me-drawer-section me-limits"); hl.appendChild(el("h3", null, "Honest limits"));
      var hul = el("ul", "me-drawer-list");
      limits.forEach(function (x) { hul.appendChild(el("li", null, typeof x === "string" ? x : (x.plain || x.field || ""))); });
      hl.appendChild(hul); host.appendChild(hl);
    }

    // Made by (array v2 / string v1)
    if (madeBy) {
      var mb = el("div", "me-drawer-section"); mb.appendChild(el("h3", null, "Made by"));
      if (Array.isArray(madeBy)) { var mu = el("ul", "me-drawer-list"); madeBy.forEach(function (x) { mu.appendChild(el("li", null, x)); }); mb.appendChild(mu); }
      else mb.appendChild(el("p", "me-drawer-p", madeBy));
      host.appendChild(mb);
    }

    // What's next — the arrow chain + the prose
    if (whatsNext) {
      var wn = el("div", "me-drawer-section"); wn.appendChild(el("h3", null, "What's next"));
      var chain = nextChain(id); if (chain) wn.appendChild(el("p", "me-whatsnext-chain", chain));
      wn.appendChild(el("p", "me-drawer-p", whatsNext));
      host.appendChild(wn);
    }

    // Foundation (template section 11) — the established scholarship the method visibly stands on
    if (D.foundation) renderFoundation(host, D.foundation);

    // Research view (nested) — the raw receipt lives HERE, not in METHOD (Content SB principle)
    var det = el("details", "me-research");
    det.appendChild(el("summary", null, "show the research view"));
    var rv = el("div", "me-research-body");
    if (receipt) {
      rv.appendChild(el("h4", null, "the receipt (raw fields)"));
      var r3 = el("ul", "me-drawer-list");
      if (receipt.checkout_version) r3.appendChild(el("li", null, "checkout_version: " + receipt.checkout_version));
      if (receipt.package_hash) r3.appendChild(el("li", null, "package_hash: " + String(receipt.package_hash).slice(0, 16) + "…"));
      if (receipt.fidelity) r3.appendChild(el("li", null, "fidelity: " + receipt.fidelity));
      (receipt.units || []).forEach(function (u) { r3.appendChild(el("li", null, (u.passage_id || "") + " · hash " + String(u.content_hash || "").slice(0, 12) + "…")); });
      rv.appendChild(r3);
    }
    // copyright basis (auditable) — the raw field + verify link live in the research tier, not METHOD
    if (onMark.rights_basis) {
      var rb = onMark.rights_basis;
      rv.appendChild(el("h4", null, "copyright basis (auditable)"));
      if (rb.plain) rv.appendChild(el("p", "me-drawer-p", rb.plain));
      var rbl = el("ul", "me-drawer-list");
      if (rb.field) rbl.appendChild(el("li", null, rb.field + " = " + (rb.value || "")));
      if (rb.source_id) rbl.appendChild(el("li", null, "source_id: " + rb.source_id));
      rv.appendChild(rbl);
      if (rb.verify_at) {
        var va = el("a", "me-verify-link", "verify at the source →");
        va.href = rb.verify_at; va.target = "_blank"; va.rel = "noopener";
        rv.appendChild(va);
      }
    }
    // how to run it — so a reader can REPRODUCE the step, not just read about it
    var htr = (D.research_view && D.research_view.how_to_run);
    if (htr) {
      rv.appendChild(el("h4", null, "how to run it"));
      Object.keys(htr).forEach(function (k) {
        var v = htr[k];
        if (typeof v !== "string") return;
        var isCmd = /^\.\//.test(v.trim()); // only the actual invocation (a command starts with ./); prose that merely names a script stays prose
        if (isCmd) {
          rv.appendChild(el("p", "me-htr-step", k));
          var pre = el("pre", "me-code"); pre.textContent = v; rv.appendChild(pre);
        } else {
          var p = el("p", "me-htr-step");
          p.appendChild(el("b", null, k + ": "));
          p.appendChild(document.createTextNode(v));
          rv.appendChild(p);
        }
      });
    }
    rv.appendChild(el("h4", null, "data source"));
    rv.appendChild(el("p", "me-drawer-p", dataSource));
    det.appendChild(rv);
    host.appendChild(det);
  };
  if (STEP_CACHE[id]) { paint(); } else {
    fetch("./data/goldenpath/mark16/" + (STEP_DATA[id] || ""))
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (x) { STEP_CACHE[id] = x; paint(); })
      .catch(function () { STEP_CACHE[id] = {}; paint(); });
  }
}

/* the worked result — Text (Step 1): the checkout gate + the M23 money shot + the verbatim passage.
   Handles v2 (gate = plain-key object, verbatim_text inline) and v1 (gate_result + checkout package). */
function renderLayer2Text(host, om) {
  var gate = om.gate || {}, ct = om.the_contrast || {};
  var s2 = el("div", "me-drawer-section");
  s2.appendChild(el("h3", null, "On Mark 16: the checkout"));
  var ul2 = el("ul", "me-checkout-checks");
  var li = function (ok, label) { return el("li", ok ? "is-ok" : "is-pending", (ok ? "✓ " : "◦ ") + label); };
  if (gate["in our collection"] !== undefined || gate["permission to share"] !== undefined) {
    Object.keys(gate).forEach(function (k) { ul2.appendChild(li(gate[k], k)); });
  } else {
    ul2.appendChild(li(gate.in_corpus, "in our collection"));
    ul2.appendChild(li(gate.chunked, "split into pieces"));
    ul2.appendChild(li(gate.verbatim_integrity, "exact wording"));
    ul2.appendChild(li(gate.rights_cleared, "permission to share"));
  }
  s2.appendChild(ul2);
  host.appendChild(s2);
  if (ct.coder_saw_paraphrase || ct.corpus_verbatim) {
    var mv = el("div", "me-drawer-section me-m23");
    mv.appendChild(el("h3", null, ct.heading || "What the coder saw vs. what the passage says (Mark 16:8)"));
    var grid = el("div", "me-m23-grid");
    var col = function (tag, txt, cls) { var c = el("div", "me-m23-col " + cls); c.appendChild(el("span", "me-m23-tag", tag)); c.appendChild(el("p", "me-m23-text", '"' + txt + '"')); return c; };
    grid.appendChild(col("the coder's paraphrase", ct.coder_saw_paraphrase || "", "is-paraphrase"));
    grid.appendChild(col("the corpus verbatim", ct.corpus_verbatim || "", "is-verbatim"));
    mv.appendChild(grid);
    if (ct.plain || ct.plain_caption) mv.appendChild(el("p", "me-m23-caption", ct.plain || ct.plain_caption));
    host.appendChild(mv);
  }
  var raw = om.verbatim_text || (CHECKOUT && CHECKOUT.units && CHECKOUT.units[0] && CHECKOUT.units[0].text) || "";
  if (raw) {
    var ix = raw.indexOf("016:001"); if (ix > 0) raw = raw.slice(ix);
    var s3 = el("div", "me-drawer-section");
    s3.appendChild(el("h3", null, "What we're reading"));
    if (om.reading_ref || om.edition) s3.appendChild(el("p", "me-checkout-ref", om.reading_ref || om.edition));
    var gs = om.goal_span;
    if (gs && (gs.ref || gs.note)) s3.appendChild(el("p", "me-drawer-caption", "Reading focus: " + (gs.ref || "") + (gs.note ? ". " + gs.note : "")));
    // rendered from the checkout package's own bytes: straight quotes + the translator's {…} apparatus preserved, not curled or stripped
    s3.appendChild(el("p", "me-checkout-text", '"' + cleanVerbatim(raw) + '"'));
    s3.appendChild(el("p", "me-checkout-stamp", "✓ version-locked · verified unchanged"));
    if (om.edition && om.reading_ref) s3.appendChild(el("p", "me-checkout-stamp", om.edition));
    if (om.reading_source) s3.appendChild(el("p", "me-drawer-caption", om.reading_source));
    if (om.apparatus_note) s3.appendChild(el("p", "me-drawer-caption", om.apparatus_note));
    host.appendChild(s3);
  }
}

/* LAYER 2 — Decompose (Step 2a): count + what-a-move-is teaching box + the full worked example + connections + silence.
   Every move is a FLAT object {move, plain, who, operation, on, result}; rendered via moveBlock (never the raw object). */
function renderLayer2Decompose(host, l2) {
  var s2 = el("div", "me-drawer-section");
  s2.appendChild(el("h3", null, "On Mark 16: the moves"));
  s2.appendChild(el("p", "me-drawer-p",
    "The passage becomes " + (l2.move_count || "several") + " moves" +
    (l2.edge_count ? ", linked by " + l2.edge_count + " connections" : "") + "."));
  if (l2.what_counts_as_one_move) s2.appendChild(el("p", "me-drawer-caption", l2.what_counts_as_one_move));
  host.appendChild(s2);

  // teaching box: what a move IS — the clean grammar contract (v2: funnel + core[orange] + modifiers[green])
  var an = l2.the_anatomy_of_a_move;
  // gate on any renderable key (grammar/note/example); dropping a gated key would blank the box (S162 lesson)
  if (an && (an.note || an.grammar || an.definitions || an.example)) {
    var ab = el("div", "me-drawer-section me-anatomy");
    ab.appendChild(el("h3", null, "What a move is"));
    if (an.note) ab.appendChild(el("p", "me-drawer-p", an.note));
    if (an.grammar) ab.appendChild(renderGrammar(an.grammar));  // v2 (Decision 223): funnel + core + modifiers
    if (an.example) ab.appendChild(moveBlock(an.example));      // gone in v2 (clean/applied split); render if present
    host.appendChild(ab);
  }

  // the thorough worked example: every move as a labeled block (falls back to featured_moves)
  var we = l2.worked_example, isFull = !!(we && we.moves && we.moves.length);
  var moves = isFull ? we.moves : (l2.featured_moves || []);
  if (moves.length) {
    var wb = el("div", "me-drawer-section");
    wb.appendChild(el("h3", null, isFull ? "The moves of Mark 16" : "Featured moves"));
    if (we && we.note) wb.appendChild(el("p", "me-drawer-caption", we.note));
    var list = el("div", "me-move-list");
    moves.forEach(function (m) { list.appendChild(moveBlock(m)); });
    wb.appendChild(list);
    host.appendChild(wb);
  }

  // the silence thread — the finding (M22 flee / M23 say nothing)
  if (l2.the_silence_thread) {
    var mv = el("div", "me-drawer-section me-m23");
    mv.appendChild(el("h3", null, "The silence thread"));
    mv.appendChild(el("p", "me-m23-caption", l2.the_silence_thread));
    host.appendChild(mv);
  }

  // how the moves connect (nesting vs reporting)
  if (l2.connections && (l2.connections.plain || l2.connections.count)) {
    var cx = el("div", "me-drawer-section");
    cx.appendChild(el("h3", null, "How the moves connect"));
    cx.appendChild(el("p", "me-drawer-p", l2.connections.plain || (l2.connections.count + " connections")));
    host.appendChild(cx);
  }
  if (l2.all_moves_note) host.appendChild(el("p", "me-drawer-p me-deepdive", l2.all_moves_note));
}

/* ------------------------------------------------------------------ chrome */

function renderHead() {
  document.getElementById("me-kicker").textContent = FLOW.meta.kicker;
  document.getElementById("me-title").textContent = FLOW.meta.title;
  document.getElementById("me-lede").textContent = FLOW.meta.lede;

  // one view (METHOD): the METHOD/AUDIT toggle was retired per PI S162; hide the now-empty toggle host
  const modeHost = document.getElementById("me-mode");
  if (modeHost) { modeHost.textContent = ""; modeHost.style.display = "none"; }
}

function initTheme() {
  const btn = document.getElementById("me-theme");
  const stored = localStorage.getItem("me-theme");
  if (stored) document.documentElement.setAttribute("data-theme", stored);
  const label = () => {
    const cur =
      document.documentElement.getAttribute("data-theme") ||
      (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    btn.textContent = cur === "dark" ? "light" : "dark";
  };
  label();
  btn.addEventListener("click", () => {
    const cur =
      document.documentElement.getAttribute("data-theme") ||
      (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    const next = cur === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    localStorage.setItem("me-theme", next);
    label();
  });
}

/* -------------------------------------------------------------------- boot */

renderHead();
renderLegend();
renderFigure();
initTheme();

window.addEventListener("resize", () => drawEdges());
if (window.ResizeObserver) {
  const fig = document.getElementById("me-figure");
  const ro = new ResizeObserver(() => drawEdges());
  ro.observe(fig);
}
if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => drawEdges());
window.addEventListener("keydown", (e) => {
  if (e.key === "Escape") closeDrawer();
});
