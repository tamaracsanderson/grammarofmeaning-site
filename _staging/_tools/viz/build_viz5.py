#!/usr/bin/env python3
"""VIZ-5 — seven figures, the custody ladder. Replaces the VIZ-5 vizslot (§D4, #d-cloud).

Every datum from the real feed (R1): DATA_seven_figures_coordinates_for_designSB_2026-07-14.json
(its own _meta: "N=1 matched pair/figure (demonstrator-grade)"). Ordering, spreads, essence-status,
transmission structures, colours: the feed + the §D4 arbiter table.

★ The N=1 caveat is ON THE FACE (R4), not a footnote: N=1 matched pair per figure · single-coder
(Sonnet) · reliability moderate-pending · Socrates on a small local model that flattens irony. A
demonstrator — and the picture says so while still showing why it is the most interesting thing
in the drawer.

Ink: this is a CANDIDATE demonstrator; within it the ATTESTED portrayals (real texts/readers) are
plotted, with out-of-custody marked distinctly. No GENERATED content is present to mix.
"""
import sys, re, json

def build(feed_path, page_path):
    d = json.load(open(feed_path, encoding="utf-8"))
    figs = sorted(d["figures"], key=lambda f: f["base_spread"])
    ESS = d["_meta"]["essence_axis"]  # ontological-commitment

    # transmission-structure family (4), keyed for the legend
    def fam(ts):
        t = ts.lower()
        if "single-custodian" in t: return ("single", "single-custodian")
        if "fragmented" in t or "shared core" in t: return ("shared", "fragmented, but shared core")
        if "rival" in t: return ("rival", "rival-custodian, no shared core")
        if "no-custodian" in t or "no custodian" in t: return ("none", "no custodian")
        return ("other", ts)

    # the shared essence axis: distinct ontological-commitment values across all figures, ordered personal→negative
    order = ["personal-agentive", "dual-aspect-monism", "not-asserted", "impersonal-order", "void", "apophatic"]
    present = []
    for f in figs:
        for p in f["portrayals"]:
            v = p.get(ESS)
            if v and v not in present: present.append(v)
    axis = [v for v in order if v in present] + [v for v in present if v not in order]

    F = []
    for f in figs:
        famk, faml = fam(f["transmission_structure"])
        ports = []
        for p in f["portrayals"]:
            out = any(k in p.get("custody", "").lower() for k in ("outside", "out-of-custody", "gnostic"))
            # where non-essence variance lives (domain / telos / epistemic)
            ports.append({"label": p["label"], "custody": p.get("custody", ""), "ess": p.get(ESS, "—"), "out": out})
        core_vals = [p.get(ESS) for p in f["portrayals"]
                     if not any(k in p.get("custody", "").lower() for k in ("outside", "out-of-custody", "gnostic"))]
        essence_holds = len(set(core_vals)) == 1
        # variance-location: what differs if the essence axis agrees?
        note = f.get("note", "")
        F.append({"figure": f["figure"], "domain": f.get("domain", ""), "ts": f["transmission_structure"],
                  "fam": famk, "faml": faml, "status": f["essence_status"], "spread": f["base_spread"],
                  "color": f["color"], "ports": ports, "essence_holds": essence_holds, "note": note})
    DATA = json.dumps({"F": F, "axis": axis, "essName": ESS,
                       "meta": {"source": d["_meta"].get("source", ""), "date": d["_meta"].get("date", "")}}, ensure_ascii=False)

    BLOCK = '''<div class="viz viz-5" id="viz-5">
<style>
.viz-5{border:1px solid var(--rule);border-radius:12px;background:var(--paper-3);padding:18px 18px 14px;margin:22px 0}
.viz-5 .viz-h{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap;margin-bottom:6px}
.viz-5 .viz-id{font-family:var(--mono);font-size:11px;font-weight:600;letter-spacing:.06em;color:var(--paper);background:var(--moss);padding:2px 8px;border-radius:5px}
.viz-5 .viz-t{font-family:var(--serif);font-size:19px;color:var(--ink)}
.viz-5 .chip{font-family:var(--mono);font-size:9.5px;letter-spacing:.05em;text-transform:uppercase;padding:2px 8px;border-radius:20px;border:1px solid currentColor}
.viz-5 .chip-cand{color:var(--terracotta)}
.viz-5 .viz-lede{font-size:14.5px;color:var(--ink-2);margin:6px 0 10px;max-width:82ch;line-height:1.6}
/* the caveat — ON THE FACE */
.viz-5 .v5-caveat{border:1.5px solid var(--terracotta);border-radius:9px;background:var(--paper-2);padding:10px 13px;margin:0 0 14px;font-size:12.5px;color:var(--ink-2);line-height:1.55}
.viz-5 .v5-caveat b{color:var(--terracotta);font-family:var(--mono);font-size:11px;letter-spacing:.04em}
/* legend */
.viz-5 .v5-legend{display:flex;gap:16px;flex-wrap:wrap;font-size:11.5px;color:var(--ink-2);margin:0 0 12px;align-items:center}
.viz-5 .v5-legend .k{display:inline-flex;align-items:center;gap:6px}
.viz-5 .dot{width:11px;height:11px;border-radius:50%;flex:none}
.viz-5 .dot.single{background:var(--fern)}.viz-5 .dot.shared{background:var(--olive)}
.viz-5 .dot.rival{background:var(--terracotta)}.viz-5 .dot.none{background:var(--honey)}
.viz-5 .oc{width:11px;height:11px;border-radius:50%;border:1.5px solid var(--ink-3);background:transparent;flex:none}
/* the ladder */
.viz-5 .v5-scroll{overflow-x:auto}
.viz-5 .v5-ladder{min-width:640px}
.viz-5 .rung{display:grid;grid-template-columns:150px 1fr 150px;gap:12px;align-items:center;padding:9px 0;border-top:1px solid var(--rule-soft)}
.viz-5 .rung:first-child{border-top:0}
.viz-5 .fig{}
.viz-5 .fig .fn{font-family:var(--serif);font-size:15px;color:var(--ink)}
.viz-5 .fig .ft{display:flex;align-items:center;gap:6px;font-family:var(--mono);font-size:9.5px;color:var(--ink-3);margin-top:2px}
.viz-5 .strip{position:relative;height:44px;border:1px solid var(--rule-soft);border-radius:7px;background:var(--paper)}
.viz-5 .strip .tick{position:absolute;top:0;bottom:0;width:0;border-left:1px dashed var(--rule-soft)}
.viz-5 .strip .pt{position:absolute;top:50%;width:14px;height:14px;border-radius:50%;transform:translate(-50%,-50%)}
.viz-5 .strip .pt.in{border:0}
.viz-5 .strip .pt.out{background:transparent!important;border:2px solid var(--ink-3)}
.viz-5 .pt.single{background:var(--fern)}.viz-5 .pt.shared{background:var(--olive)}
.viz-5 .pt.rival{background:var(--terracotta)}.viz-5 .pt.none{background:var(--honey)}
.viz-5 .strip .plab{position:absolute;bottom:2px;font-family:var(--mono);font-size:7.5px;color:var(--ink-3);transform:translateX(-50%);white-space:nowrap}
.viz-5 .meta{text-align:right}
.viz-5 .meta .sp{font-family:var(--serif);font-size:20px;color:var(--ink)}
.viz-5 .meta .spbar{height:5px;border-radius:99px;background:var(--rule);overflow:hidden;margin:3px 0}
.viz-5 .meta .spbar i{display:block;height:100%;background:linear-gradient(90deg,var(--fern),var(--terracotta))}
.viz-5 .meta .st{font-family:var(--mono);font-size:9px;letter-spacing:.03em;padding:1px 7px;border-radius:20px}
.viz-5 .st.prot{color:var(--fern);border:1px solid var(--fern)}
.viz-5 .st.cont{color:var(--terracotta);border:1px solid var(--terracotta)}
.viz-5 .vnote{grid-column:1 / -1;font-size:11px;color:var(--ink-3);padding:0 0 2px 152px;line-height:1.4}
.viz-5 .vnote b{color:var(--ink-2)}
.viz-5 .axhead{font-family:var(--mono);font-size:9px;color:var(--ink-3);text-align:center;margin:2px 0 0;grid-column:2}
.viz-5 .reading{margin:14px 0 0;border-left:3px solid var(--moss);background:var(--paper-2);border-radius:0 9px 9px 0;padding:11px 14px;font-size:13px;color:var(--ink-2);line-height:1.6}
.viz-5 .reading b{color:var(--ink)}
.viz-5 .viz-src{font-family:var(--mono);font-size:10.5px;color:var(--ink-3);margin:12px 0 0;line-height:1.65}
@media(prefers-reduced-motion:reduce){.viz-5 *{transition:none!important}}
</style>
  <div class="viz-h">
    <span class="viz-id">VIZ-5</span>
    <span class="viz-t">Seven figures — the custody ladder</span>
    <span class="chip chip-cand">candidate · demonstrator</span>
  </div>
  <div class="v5-caveat"><b>⚠ Demonstrator — read the shape, not the numbers.</b> N=1 matched pair per figure. Single-coder (Sonnet), reliability moderate-pending (gated by TG-1). Socrates was run on a small local model that flattens exactly the Socratic irony it needed to read. Every spread below is one run, not a measurement. It is on the page because the <i>ordering</i> — Jesus 0.06 → Freud 1.00 — is one no one designed, and it tracks a structural fact about custody rather than about theology.</div>
  <p class="viz-lede">Seven central figures, ordered top-to-bottom by how far their portrayals spread. The claim in one sentence: <b>the depth of the variance is set by who controls the telling.</b> Each figure’s dots are its portrayals plotted on the <b>essence axis</b> (ontological-commitment). Where they <b>cluster</b>, the essence holds; where they <b>scatter</b>, the essence itself is contested. A hollow ring = a portrayal <b>outside custody</b>.</p>

  <div class="v5-legend">
    <span class="k"><span class="dot single"></span>single-custodian</span>
    <span class="k"><span class="dot shared"></span>fragmented, shared core</span>
    <span class="k"><span class="dot rival"></span>rival, no shared core</span>
    <span class="k"><span class="dot none"></span>no custodian</span>
    <span class="k"><span class="oc"></span>outside custody</span>
  </div>

  <div class="v5-scroll"><div class="v5-ladder" id="v5-ladder"></div></div>

  <div class="reading">
    <b>Read the shape.</b> Where one custodian controls the telling (Jesus · God · Muhammad), the essence-axis is protected no matter how much peripheral variation exists — God’s portrayals differ on <i>transcendent vs immanent</i>, but not on the essence. <b>Buddhism is the interesting middle:</b> custody is fragmented across rival schools, yet a shared core (śūnyatā) preserves the essence anyway — so it is <b>not custody-count</b> that does the work, it is whether the custodians agree on what the essence <i>is</i>. <b>Socrates is the subtle one:</b> his essence-axis actually holds (both readings refuse to assert a metaphysics) — his spread comes from a contested <i>telos and method</i>, not a contested essence. And <b>Freud/Jung is the limit case:</b> rival schools, no shared core, and every axis differs.
  </div>

  <p class="viz-src">Source — <code>DATA_seven_figures_coordinates_for_designSB_2026-07-14.json</code>, whose own <code>_meta</code> reads “N=1 matched pair/figure (demonstrator-grade).” Full 6-axis coords exist only for Confucius + Freud; the others carry the essence axis + the domain axis where the finding lives, so the cloud is plotted on the essence axis (shared by all). Ordering + structures + the reading: §D4. Case study: <code>CASE_STUDY_transmission_structure_seven_figures_2026-07-14.md</code>. Stage&nbsp;6&nbsp;=&nbsp;0.</p>
<script>
(function(){
  var D=__DATA__;
  function esc(s){return String(s).replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c];});}
  var axis=D.axis, n=axis.length;
  function xFor(v){ var i=axis.indexOf(v); return n<2?50:(8+ (i/(n-1))*84); }
  var lad=document.getElementById('v5-ladder');
  // shared axis header row
  var ticks=axis.map(function(v){ return '<span class="plab" style="left:'+xFor(v)+'%">'+esc(v)+'</span><span class="tick" style="left:'+xFor(v)+'%"></span>'; }).join('');
  var html='';
  D.F.forEach(function(f){
    // stack dots that share an x
    var atX={};
    var dots=f.ports.map(function(p){
      var x=xFor(p.ess), key=x.toFixed(0); atX[key]=(atX[key]||0); var dy=(atX[key]-0)*7 - 0; atX[key]++;
      var cls='pt '+f.fam+' '+(p.out?'out':'in');
      return '<span class="'+cls+'" style="left:'+x+'%;top:calc(50% + '+(dy)+'px)" title="'+esc(p.label)+' · '+esc(p.ess)+'"></span>';
    }).join('');
    var st=f.status.indexOf('CONTEST')>=0 ? 'cont':'prot';
    var variance = f.essence_holds
      ? 'essence <b>holds</b> — the variance lives elsewhere (domain · telos · method)'
      : 'essence <b>scatters</b> — the portrayals disagree on what it fundamentally is';
    html+='<div class="rung">'
      +'<div class="fig"><div class="fn">'+esc(f.figure)+'</div><div class="ft"><span class="dot '+f.fam+'" style="width:9px;height:9px"></span>'+esc(f.faml)+'</div></div>'
      +'<div class="strip">'+ticks+dots+'</div>'
      +'<div class="meta"><div class="sp">'+f.spread.toFixed(2)+'</div><div class="spbar"><i style="width:'+(f.spread*100).toFixed(0)+'%"></i></div><span class="st '+st+'">'+esc(f.status)+'</span></div>'
      +'<div class="vnote">'+variance+'</div>'
      +'</div>';
  });
  lad.innerHTML='<div class="rung" style="border:0;padding-bottom:0"><div></div><div class="axhead">the essence axis — '+esc(D.essName)+' → portrayals cluster (held) or scatter (contested)</div><div></div></div>'+html;
})();
</script>
</div>'''
    block = BLOCK.replace("__DATA__", DATA)
    h = open(page_path, encoding="utf-8").read()
    slot = re.compile(r'<div class="vizslot"[^>]*>\s*<div class="vs-h"><span class="vs-id">VIZ-5</span>.*?</div>\s*</div>', re.S)
    built = re.compile(r'<div class="viz viz-5" id="viz-5">.*?</script>\s*</div>', re.S)
    if slot.search(h):
        h2 = slot.sub(lambda _: block, h, count=1)
    elif built.search(h):
        h2 = built.sub(lambda _: block, h, count=1)
    else:
        raise AssertionError("neither VIZ-5 vizslot nor built block matched")
    open(page_path, "w", encoding="utf-8").write(h2)
    left = h2.count('class="vizslot"')
    print(f"VIZ-5 installed · {len(F)} figures · essence axis {len(axis)} values · slots left: {left}")

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
