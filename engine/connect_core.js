/* ── Connect core — shared render logic for the Connect figures (Trace/Scan/Map) ──
   design-SB, Connect v2 P1 (2026-08-11). Framework-free, CSP-safe (no external libs,
   same-origin fetch only), ES5 to match the figure codebase. ONE place the 5-kind
   grammar lives, so the arc-band, loom, topology — and the eventual P2 unified shell —
   render the SAME taxonomy from engine/data/connect_taxonomy.json (render-from-data,
   §2.16 · single-store, §2.13). See the METHODOLOGY FOOTER at the bottom. */
(function (root) {
  "use strict";

  var TAX_URL = "/engine/data/connect_taxonomy.json";
  var KIND_ORDER = ["LINKAGE", "LINEAGE", "RESONANCE", "SHAPE", "SONIC"];

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }
  function kindOf(e) { return String(e.edge_kind || "").toUpperCase(); }
  function typeOf(e) { return String(e.type || "").toUpperCase(); }

  function load() { return fetch(TAX_URL).then(function (r) { return r.json(); }); }

  function kindDef(tax, id) {
    var ks = tax.kinds || [];
    for (var i = 0; i < ks.length; i++) if (ks[i].id === id) return ks[i];
    return null;
  }
  function hueVar(tax, id) { var k = kindDef(tax, id); return k ? k.hue : "--ink-3"; }

  function subInfo(tax, t) {
    return (tax.subtypes && tax.subtypes[t]) ||
      { kind: "LINKAGE", label: String(t || "").toLowerCase().replace(/_/g, " "), prose: "{src} is linked to {tgt}" };
  }
  function isWeak(tax, e) { var s = tax.subtypes && tax.subtypes[typeOf(e)]; return !!(s && s.weak); }

  /* plain-language relation — the reader never sees NEST_REPORTS (§2.16) */
  function prose(tax, e) {
    var s = subInfo(tax, typeOf(e));
    return String(s.prose)
      .replace(/\{src\}/g, e.source_move_label)
      .replace(/\{tgt\}/g, e.target_move_label);
  }
  function subLabel(tax, e) { return subInfo(tax, typeOf(e)).label; }

  /* counts of an edge list, per kind + per subtype */
  function counts(edges) {
    var byKind = {}, bySub = {};
    for (var i = 0; i < edges.length; i++) {
      var k = kindOf(edges[i]), t = typeOf(edges[i]);
      byKind[k] = (byKind[k] || 0) + 1;
      bySub[t] = (bySub[t] || 0) + 1;
    }
    return { byKind: byKind, bySub: bySub };
  }

  /* ── the shared filter control (5-kind legend + sub-type drill-down) ──
     mounts into `host`, owns the on/off state, calls onChange() on any toggle.
     The figure exposes edges as DOM with data-kind + data-sub and re-applies
     visible(e) in onChange. `edges` is the RENDERED edge list (post-drop). */
  function Filter(host, tax, edges, onChange) {
    var c = counts(edges);
    var offKind = {}, offSub = {}, open = false;

    function visibleKind(id) { return !offKind[id]; }
    function visibleSub(t) { return !offSub[t]; }
    function visible(e) { return visibleKind(kindOf(e)) && visibleSub(typeOf(e)); }

    function render() {
      var html = '<div class="cc-kinds">';
      for (var i = 0; i < KIND_ORDER.length; i++) {
        var id = KIND_ORDER[i], def = kindDef(tax, id) || { label: id, hue: "--ink-3", gloss: "" };
        var n = c.byKind[id] || 0, absent = n === 0;
        var note = absent ? (id === "SONIC" ? "on the Plate" : "none here") : String(n);
        html += '<button type="button" class="cc-k' + (absent ? " cc-absent" : "") + (offKind[id] ? " cc-off" : "") +
          '" data-kind="' + id + '"' + (absent ? " disabled aria-disabled=\"true\"" : "") +
          ' title="' + esc(def.gloss) + '">' +
          '<span class="cc-sw" style="background:var(' + def.hue + ')"></span>' +
          esc(def.label) + ' <span class="cc-ct">' + esc(note) + '</span></button>';
      }
      html += '</div>';
      html += '<button type="button" class="cc-drill" data-drill>' + (open ? "hide detail ▴" : "break down by relation ▾") + '</button>';
      if (open) {
        html += '<div class="cc-subs">';
        for (var j = 0; j < KIND_ORDER.length; j++) {
          var kid = KIND_ORDER[j];
          // subtypes present in THIS feed, in count order
          var subs = [];
          for (var t in c.bySub) if (c.bySub.hasOwnProperty(t) && subInfo(tax, t).kind === kid) subs.push(t);
          if (!subs.length) continue;
          subs.sort(function (a, b) { return (c.bySub[b] || 0) - (c.bySub[a] || 0); });
          var kd = kindDef(tax, kid) || { label: kid, hue: "--ink-3" };
          html += '<div class="cc-subrow"><span class="cc-subk" style="color:var(' + kd.hue + ')">' + esc(kd.label) + '</span>';
          for (var s = 0; s < subs.length; s++) {
            var st = subs[s], si = subInfo(tax, st);
            html += '<button type="button" class="cc-s' + (offSub[st] ? " cc-off" : "") + (si.weak ? " cc-weak" : "") +
              '" data-sub="' + esc(st) + '"><span class="cc-sw sq" style="background:var(' + kd.hue + ')"></span>' +
              esc(si.label) + ' <span class="cc-ct">' + (c.bySub[st] || 0) + '</span></button>';
          }
          html += '</div>';
        }
        html += '</div>';
      }
      host.innerHTML = html;
      wire();
    }

    function wire() {
      var kb = host.querySelectorAll(".cc-k");
      for (var i = 0; i < kb.length; i++) kb[i].addEventListener("click", function () {
        if (this.disabled) return;
        var id = this.getAttribute("data-kind"); offKind[id] = !offKind[id]; render(); onChange();
      });
      var sb = host.querySelectorAll(".cc-s");
      for (var j = 0; j < sb.length; j++) sb[j].addEventListener("click", function () {
        var t = this.getAttribute("data-sub"); offSub[t] = !offSub[t]; render(); onChange();
      });
      var d = host.querySelector("[data-drill]");
      if (d) d.addEventListener("click", function () { open = !open; render(); });
    }

    render();
    return { visible: visible, counts: c };
  }

  /* the relation-card HTML for a single edge (typed relation in prose + direction + kind chip) */
  function relationCardHTML(tax, e) {
    var kid = kindOf(e), kd = kindDef(tax, kid) || { label: kid, hue: "--ink-3" };
    var arrow = e.direction === "backward" ? "←" : (e.direction === "forward" ? "→" : "↔");
    return '<div class="cc-rel">' +
      '<span class="cc-pill" style="border-color:var(' + kd.hue + ');color:var(' + kd.hue + ')">' +
      esc(kd.label) + " · " + esc(subLabel(tax, e)) + '</span>' +
      '<span class="cc-relp">' + esc(prose(tax, e)) + '</span>' +
      '<span class="cc-dir">' + esc(e.source_move_label) + " " + arrow + " " + esc(e.target_move_label) + '</span>' +
      '</div>';
  }

  /* all connections for one move, as a titled block of relation cards */
  function moveConnectionsHTML(tax, edges, label) {
    var mine = [];
    for (var i = 0; i < edges.length; i++)
      if (edges[i].source_move_label === label || edges[i].target_move_label === label) mine.push(edges[i]);
    if (!mine.length) return '<p class="cc-none">' + esc(label) + ' reaches to nothing coded here.</p>';
    // strong (meaning-bearing) first, weak "and then" last
    mine.sort(function (a, b) { return (isWeak(tax, a) ? 1 : 0) - (isWeak(tax, b) ? 1 : 0); });
    var head = '<p class="cc-relhead"><strong>' + esc(label) + '</strong> · ' + mine.length +
      ' connection' + (mine.length === 1 ? "" : "s") + '</p>';
    var body = "";
    for (var j = 0; j < mine.length; j++) body += relationCardHTML(tax, mine[j]);
    return head + body;
  }

  /* the shared CSS for the filter + relation cards (injected once) */
  var CSS =
    '.cc-kinds{display:flex;flex-wrap:wrap;gap:7px;justify-content:center}' +
    '.cc-k,.cc-s,.cc-drill{font-family:var(--sans);font-size:12px;border:1px solid var(--rule);background:transparent;border-radius:999px;padding:4px 11px;cursor:pointer;color:var(--ink-2);display:inline-flex;align-items:center;gap:6px;user-select:none;line-height:1.2}' +
    '.cc-drill{margin:10px auto 0;display:block;color:var(--ink-3);font-size:11px;letter-spacing:.04em}' +
    '.cc-sw{width:15px;height:0;border-top:3px solid transparent;display:inline-block;border-radius:2px}' +
    '.cc-sw.sq{width:9px;height:9px;border-top:0;border-radius:2px}' +
    '.cc-ct{font-family:var(--mono);font-size:10px;color:var(--ink-3)}' +
    '.cc-k .cc-sw{height:3px}' +
    '.cc-off{opacity:.34}' +
    '.cc-absent{opacity:.5;cursor:default;border-style:dashed}' +
    '.cc-absent .cc-ct{font-style:italic}' +
    '.cc-weak{opacity:.72}' +
    '.cc-subs{max-width:52rem;margin:10px auto 0;display:flex;flex-direction:column;gap:7px}' +
    '.cc-subrow{display:flex;flex-wrap:wrap;gap:6px;align-items:center;justify-content:center}' +
    '.cc-subk{font-family:var(--mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;min-width:5.2rem;text-align:right}' +
    '.cc-s{padding:3px 9px;font-size:11.5px}' +
    '.cc-rel{border:1px solid var(--rule);border-radius:9px;padding:8px 11px;margin:7px 0;background:color-mix(in srgb,var(--paper-3) 60%,transparent)}' +
    '.cc-pill{display:inline-block;font-family:var(--mono);font-size:9.5px;letter-spacing:.06em;text-transform:uppercase;border:1px solid;border-radius:999px;padding:1px 8px;margin-right:8px;vertical-align:middle}' +
    '.cc-relp{font-family:var(--serif);font-size:14.5px;color:var(--ink)}' +
    '.cc-dir{display:block;font-family:var(--mono);font-size:10px;color:var(--ink-3);margin-top:4px;letter-spacing:.04em}' +
    '.cc-relhead{font-family:var(--sans);font-size:12px;color:var(--ink-2);margin:0 0 6px}' +
    '.cc-none{font-family:var(--sans);font-size:12px;color:var(--ink-3);font-style:italic}';

  function injectCSS(doc) {
    doc = doc || document;
    if (doc.getElementById("cc-css")) return;
    var st = doc.createElement("style"); st.id = "cc-css"; st.textContent = CSS;
    doc.head.appendChild(st);
  }

  /* drop-note: honest classification of edges that reference labels not in moves.json */
  function dropNote(dropped) {
    if (!dropped.length) return "";
    var comp = [], runmiss = [];
    for (var i = 0; i < dropped.length; i++) {
      (/\+/.test(dropped[i]) ? comp : runmiss).push(dropped[i]);
    }
    var bits = [];
    if (comp.length) bits.push(comp.length + " span several moves at once (parallelism runs the single-move views can’t draw as one arc)");
    if (runmiss.length) bits.push(runmiss.length + " reference " + runmiss.join(", ") + " (the moves.json 55→60 regen is pending — auto-resolves)");
    return " · ⚠ " + dropped.length + " edge" + (dropped.length === 1 ? "" : "s") + " not drawn: " + bits.join("; ");
  }

  root.ConnectCore = {
    TAX_URL: TAX_URL, KIND_ORDER: KIND_ORDER,
    esc: esc, load: load, kindOf: kindOf, typeOf: typeOf,
    kindDef: kindDef, hueVar: hueVar, subInfo: subInfo, isWeak: isWeak,
    prose: prose, subLabel: subLabel, counts: counts,
    Filter: Filter, relationCardHTML: relationCardHTML, moveConnectionsHTML: moveConnectionsHTML,
    injectCSS: injectCSS, dropNote: dropNote
  };
})(this);

/* ── METHODOLOGY FOOTER ──
HOW PRODUCED: design-SB 2026-08-11 (Connect figures v2, P1) — extracted the 5-edge-kind grammar into ONE shared render module so
  the three Connect views (Arc Band / Relation Loom / Topology Lab) and the coming P2 unified shell render the SAME taxonomy from
  engine/data/connect_taxonomy.json, fixing the S168 error where each figure hardcoded an invented 3-family scheme
  (logic/resonance/sonic). Framework-free, CSP-safe (same-origin fetch, no CDN), ES5 to match the figure codebase. Provides: the
  5-kind legend + sub-type drill-down with live counts (the old VIZ_constellation_v3 filter-bar model), the declared-but-absent
  handling (LINEAGE/RESONANCE/SONIC show as declared with 0 in the WEB feed; SONIC → "on the Plate"), the plain-language relation
  card (NEST_REPORTS → "the speech reported inside M3", §2.16), and honest drop-note classification (composite parallelism runs vs
  the M56–M60 regen mismatch).
SCHOLARLY SOURCES: _staging/connect_v2_reconciliation_2026-08-10.md (the v2 build spec — GPT crit + PI direction); the Connect
  method drawer edge_grammar_v1 (the SSOT, §2.16); connect_edges.json (edge_kind + type fields, the real data); the encoding audit
  palette lock (colour = KIND: linkage=fern/lineage=moss/resonance=gold/shape=olive/sonic=sky; terracotta reserved for provenance).
WHAT NEEDS VERIFICATION: (1) the plain-language `prose` templates in connect_taxonomy.json are design-SB-authored — reading-SB/PI
  should validate the wording. (2) when Method SB ships an edge-grammar taxonomy export, switch the STRUCTURE source off this
  interim file (keep only the prose map). (3) P2 (one shell + selection state that survives the view switch) reuses this module. */
