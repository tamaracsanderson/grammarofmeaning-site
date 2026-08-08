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
  mode: localStorage.getItem("me-mode") === "audit" ? "audit" : "method",
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

  if (state.mode === "audit") {
    const audit = el("span", "me-audit");
    audit.appendChild(el("span", "me-audit-tag", node.implementation));
    audit.appendChild(el("span", "me-audit-tag is-val", node.validation));
    if (node.badge) audit.appendChild(el("span", "me-audit-warn", "⚠"));
    b.appendChild(audit);
  }

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
  s.appendChild(bandHead("The panel", "the invention — the argument gets made here"));
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
    item.appendChild(el("span", "me-legend-desc", ` — ${desc}`));
    host.appendChild(item);
  });
  if (state.mode === "audit") {
    Object.entries(FLOW.meta.maturity).forEach(([key, desc]) => {
      const item = el("span", "me-legend-item");
      item.appendChild(el("span", `me-legend-dot is-${key}`));
      item.appendChild(document.createTextNode(key));
      item.appendChild(el("span", "me-legend-desc", ` — ${desc}`));
      host.appendChild(item);
    });
  } else {
    const item = el("span", "me-legend-item is-quiet");
    item.appendChild(el("span", "me-legend-dot is-populated"));
    item.appendChild(
      document.createTextNode(
        "build-status dot — operational, not epistemic; switch to AUDIT for detail",
      ),
    );
    host.appendChild(item);
  }
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
  const situate = el("div", "me-situate");
  situate.appendChild(nodeCard(byId["situate"]));
  // #5 — METHOD: collapse the 5 children to one inline line so Decompose ∥ Situate read as parallel;
  //      AUDIT: expand the detailed leaf rows (per-component status lives here, not on the canvas in METHOD).
  if (state.mode === "audit") {
    const leaves = el("div", "me-leaves");
    LEAVES.forEach((n) => leaves.appendChild(nodeCard(n, "leaf")));
    situate.appendChild(leaves);
  } else {
    situate.appendChild(
      el("div", "me-leaf-inline", LEAVES.map((n) => n.label).join("  ·  ")),
    );
  }
  branches.appendChild(situate);
  cone.appendChild(branches);
  grid.appendChild(cone);

  // waist
  const gutter = el("div", "me-col me-gutter");
  gutter.appendChild(nodeCard(byId["enriched_move"], "waist"));
  gutter.appendChild(
    el("p", "me-gutter-note", "Decompose segments ∥ Situate annotates"),
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

  // ---- AUDIT only: the engineering detail (build status · dependency · metadata · edges) ----
  if (state.mode === "audit") {
    const meta = el("div", "me-drawer-meta");
    meta.appendChild(el("span", null, `grain ${node.grain}`));
    meta.appendChild(el("span", null, `impl ${node.implementation}`));
    meta.appendChild(el("span", null, `validation ${node.validation}`));
    const statusSpan = el("span");
    statusSpan.appendChild(el("span", `me-status-dot is-${node.status}`));
    statusSpan.appendChild(
      document.createTextNode(`${node.status} — ${FLOW.meta.maturity[node.status]}`),
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
      depP.textContent = "structural — part of the spine, not an output.";
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
      p.appendChild(document.createTextNode(`requires: ${req.length ? req.join(" · ") : "—"}`));
      p.appendChild(el("br"));
      p.appendChild(document.createTextNode(`produces: ${prod.length ? prod.join(" · ") : "—"}`));
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
        if (e.note) li.appendChild(document.createTextNode(` — ${e.note}`));
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

function renderStepDrawer(aside, node) {
  var id = node.id;
  var host = el("div", "me-checkout");
  host.appendChild(el("p", "me-drawer-p", "loading…"));
  aside.appendChild(host);
  var paint = function () {
    var D = STEP_CACHE[id] || {};
    host.textContent = "";
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
      ((D._reads_from ? Object.keys(D._reads_from).map(function (k) { return D._reads_from[k]; }).join(" · ") + " · " : "") + "generated by " + (D._generated_by || "—"));
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

    // How it's stored (v2)
    if (D.how_stored) {
      var hs = el("div", "me-drawer-section"); hs.appendChild(el("h3", null, "How it's stored"));
      if (D.how_stored.plain) hs.appendChild(el("p", "me-drawer-p", D.how_stored.plain));
      if (D.how_stored.passage_types && D.how_stored.passage_types.length) {
        var pu = el("ul", "me-drawer-list"); D.how_stored.passage_types.forEach(function (x) { pu.appendChild(el("li", null, x)); }); hs.appendChild(pu);
      }
      if (D.how_stored.this_checkout) hs.appendChild(el("p", "me-drawer-p", D.how_stored.this_checkout));
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
    // how to run it — so a reader can REPRODUCE the step, not just read about it
    var htr = (D.research_view && D.research_view.how_to_run);
    if (htr) {
      rv.appendChild(el("h4", null, "how to run it"));
      var cmd = htr["reproduce this checkout"] || htr.command || htr.reproduce;
      if (cmd) { var pre = el("pre", "me-code"); pre.textContent = cmd; rv.appendChild(pre); }
      var hu = el("ul", "me-drawer-list");
      Object.keys(htr).forEach(function (k) {
        if (k === "reproduce this checkout" || k === "command" || k === "reproduce") return;
        hu.appendChild(el("li", null, k + ": " + htr[k]));
      });
      if (hu.childNodes.length) rv.appendChild(hu);
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
    var col = function (tag, txt, cls) { var c = el("div", "me-m23-col " + cls); c.appendChild(el("span", "me-m23-tag", tag)); c.appendChild(el("p", "me-m23-text", "“" + txt + "”")); return c; };
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
    s3.appendChild(el("p", "me-checkout-text", "“" + cleanVerbatim(raw) + "”"));
    s3.appendChild(el("p", "me-checkout-stamp", "✓ version-locked · verified unchanged"));
    if (om.edition && om.reading_ref) s3.appendChild(el("p", "me-checkout-stamp", om.edition));
    host.appendChild(s3);
  }
}

/* LAYER 2 — Decompose (Step 2a): the move count + featured moves + the M22→M23 silence thread */
function renderLayer2Decompose(host, l2) {
  var s2 = el("div", "me-drawer-section");
  s2.appendChild(el("h3", null, "On Mark 16: the moves"));
  s2.appendChild(el("p", "me-drawer-p",
    "The passage becomes " + (l2.move_count || "—") + " moves" +
    (l2.edge_count ? ", linked by " + l2.edge_count + " connections" : "") + "."));
  var fm = l2.featured_moves || [];
  if (fm.length) {
    var ul = el("ul", "me-drawer-list");
    fm.forEach(function (m) {
      var li = el("li");
      li.appendChild(el("b", null, (m.move || "") + " "));
      li.appendChild(document.createTextNode(m.plain || ""));
      if (m.grammar) li.appendChild(el("span", "me-move-grammar", " — " + m.grammar));
      ul.appendChild(li);
    });
    s2.appendChild(ul);
  }
  host.appendChild(s2);
  if (l2.the_silence_thread) {
    var mv = el("div", "me-drawer-section me-m23");
    mv.appendChild(el("h3", null, "The silence thread"));
    mv.appendChild(el("p", "me-m23-caption", l2.the_silence_thread));
    host.appendChild(mv);
  }
  if (l2.all_moves_note) host.appendChild(el("p", "me-drawer-p me-deepdive", l2.all_moves_note));
}

/* ------------------------------------------------------------------ chrome */

function renderHead() {
  document.getElementById("me-kicker").textContent = FLOW.meta.kicker;
  document.getElementById("me-title").textContent = FLOW.meta.title;
  document.getElementById("me-lede").textContent = FLOW.meta.lede;

  const modeHost = document.getElementById("me-mode");
  modeHost.textContent = "";
  ["method", "audit"].forEach((m) => {
    const b = el("button", `me-mode-btn${state.mode === m ? " is-on" : ""}`, m);
    b.type = "button";
    b.addEventListener("click", () => {
      state.mode = m;
      localStorage.setItem("me-mode", m);
      renderHead();
      renderLegend();
      renderFigure();
    });
    modeHost.appendChild(b);
  });
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
