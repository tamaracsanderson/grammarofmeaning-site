#!/usr/bin/env python3
"""VIZ-3 — the 3D morphospace, rotatable. Replaces the VIZ-3 vizslot (§D6, #d-mca).

Every datum from the real file (R1): DATA_mca_morphospace_coords_2026-07-14.json — the computed
geometry that has never been rendered. Axis English names + loadings: SPA §D6 (the file's loadings
corroborate them). Self-contained SVG 3D projector, no CDN (R7). Drag to rotate; click a point → its
figure + six coordinates. Diagnostics on the face; the two flags §D6 requires (dim3 is NOT independent
corroboration; occupancy is 31%-coded) preserved verbatim in spirit.

★ SHOWS THE LOOSENESS: no hulls, no blobs, no tidy cluster colours. Points are one ink by default;
highlighting a single value scatters — that IS the silhouette being weak. A picture of clean clumps
here would report our wishes.

⚑ The file's numbers differ from the SPA prose — rendered from the FILE, flagged (see report).
"""
import sys, re, json

def build(coords_path, page_path):
    d = json.load(open(coords_path, encoding="utf-8"))
    pts = d["points"]
    # frame index per figure (288 distinct across 483 → some repeat = multiple frames)
    from collections import Counter, defaultdict
    fc = Counter(p["figure"] for p in pts)
    seen = defaultdict(int)
    P = []
    for p in pts:
        f = p["figure"]; seen[f] += 1
        P.append({"f": f, "x": p["x"], "y": p["y"], "z": p["z"],
                  "E": p["epistemic"], "O": p["ontological"], "M": p["inferential"],
                  "T": p["telos"], "S": p["stance"], "G": p["ground"],
                  "fi": seen[f], "fn": fc[f]})
    AXES = [
        ("O", "ontological-commitment"), ("E", "epistemic-warrant"), ("M", "inferential-operation"),
        ("T", "telos"), ("S", "stance"), ("G", "ground-world-relation"),
    ]
    axis_values = {k: sorted({p[k] for p in P}) for k, _ in AXES}
    DIMS = [
        ("dim1", d["adjusted_inertia_pct"][0], "Secular ↔ Religious", "material · observation · reductive · epoche"),
        ("dim2", d["adjusted_inertia_pct"][1], "Personal-theist ↔ Impersonal / Void", "void · dependent-arising · noetic-intuition · identity"),
        ("dim3", d["adjusted_inertia_pct"][2], "Kataphatic ↔ Apophatic", "apophatic · mystical-union · contemplation"),
    ]
    inertia3 = round(sum(d["adjusted_inertia_pct"][:3]), 1)
    DATA = json.dumps({"P": P, "axes": [{"k": k, "name": n} for k, n in AXES],
                       "axisValues": axis_values, "sil": d["O_silhouette"],
                       "agree": d["mca_pcoa_distance_agreement"], "inertia3": inertia3,
                       "dims": [{"k": k, "pct": pct, "name": n, "loads": l} for k, pct, n, l in DIMS]},
                      ensure_ascii=False)

    BLOCK = '''<div class="viz viz-3" id="viz-3">
<style>
.viz-3{border:1px solid var(--rule);border-radius:12px;background:var(--paper-3);padding:18px 18px 14px;margin:22px 0}
.viz-3 .viz-h{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap;margin-bottom:6px}
.viz-3 .viz-id{font-family:var(--mono);font-size:11px;font-weight:600;letter-spacing:.06em;color:var(--paper);background:var(--moss);padding:2px 8px;border-radius:5px}
.viz-3 .viz-t{font-family:var(--serif);font-size:19px;color:var(--ink)}
.viz-3 .chip{font-family:var(--mono);font-size:9.5px;letter-spacing:.05em;text-transform:uppercase;padding:2px 8px;border-radius:20px;border:1px solid currentColor}
.viz-3 .chip-cand{color:var(--terracotta)}.viz-3 .chip-actual{color:var(--fern)}
.viz-3 .viz-lede{font-size:14.5px;color:var(--ink-2);margin:6px 0 12px;max-width:82ch;line-height:1.6}
.viz-3 .v3-main{display:grid;grid-template-columns:1fr 260px;gap:14px}
@media(max-width:780px){.viz-3 .v3-main{grid-template-columns:1fr}}
.viz-3 .v3-stage{position:relative;border:1px solid var(--rule);border-radius:9px;background:var(--paper);overflow:hidden;min-height:420px;touch-action:none;cursor:grab}
.viz-3 .v3-stage.drag{cursor:grabbing}
.viz-3 .v3-svg{display:block;width:100%;height:auto}
.viz-3 .pt{cursor:pointer}
.viz-3 .axline{stroke:var(--rule);stroke-width:1}
.viz-3 .axcap{font-family:var(--mono);font-size:9px;fill:var(--ink-3)}
.viz-3 .hint{position:absolute;left:10px;bottom:8px;font-family:var(--mono);font-size:10px;color:var(--ink-3)}
/* side panel */
.viz-3 .v3-side{display:flex;flex-direction:column;gap:10px}
.viz-3 .v3-read{border:1px solid var(--rule);border-radius:9px;padding:11px 12px;background:var(--paper);min-height:150px}
.viz-3 .v3-read .rf{font-family:var(--serif);font-size:16px;color:var(--ink);line-height:1.2}
.viz-3 .v3-read .rfr{font-family:var(--mono);font-size:9.5px;color:var(--ink-3);margin:2px 0 8px}
.viz-3 .v3-read .rc{display:flex;justify-content:space-between;gap:8px;font-size:11.5px;padding:2px 0;border-top:1px solid var(--rule-soft)}
.viz-3 .v3-read .rk{font-family:var(--mono);font-size:9px;color:var(--ink-3);white-space:nowrap}
.viz-3 .v3-read .rv{color:var(--ink);text-align:right}
.viz-3 .v3-read .empty{font-size:12px;color:var(--ink-3);line-height:1.5}
.viz-3 .v3-hl{border:1px solid var(--rule);border-radius:9px;padding:10px 12px;background:var(--paper)}
.viz-3 .v3-hl-h{font-size:11.5px;color:var(--ink-2);margin-bottom:6px}
.viz-3 .v3-hl select{font-family:var(--mono);font-size:11px;padding:3px 6px;border:1px solid var(--rule);border-radius:5px;background:var(--paper-3);color:var(--ink);width:100%}
.viz-3 .v3-vals{display:flex;flex-wrap:wrap;gap:4px;margin-top:8px}
.viz-3 .vchip{font-family:var(--mono);font-size:9.5px;padding:2px 7px;border-radius:20px;border:1px solid var(--rule);background:var(--paper-3);color:var(--ink-2);cursor:pointer}
.viz-3 .vchip .n{color:var(--ink-3)}
.viz-3 .vchip.on{background:var(--fern);border-color:var(--fern);color:var(--paper)}
.viz-3 .vchip.on .n{color:var(--paper)}
/* diagnostics */
.viz-3 .v3-diag{margin:14px 0 0;display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
@media(max-width:680px){.viz-3 .v3-diag{grid-template-columns:1fr}}
.viz-3 .diag{border:1px solid var(--rule);border-radius:9px;padding:10px 12px;background:var(--paper)}
.viz-3 .diag .dv{font-family:var(--serif);font-size:22px;color:var(--ink)}
.viz-3 .diag .dk{font-family:var(--mono);font-size:9.5px;color:var(--ink-3);letter-spacing:.03em}
.viz-3 .diag .dg{font-size:11px;color:var(--ink-2);margin-top:5px;line-height:1.45}
.viz-3 .diag.weak{border-color:var(--terracotta)}
.viz-3 .diag.weak .dv{color:var(--terracotta)}
.viz-3 .dims{margin:12px 0 0;display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
@media(max-width:680px){.viz-3 .dims{grid-template-columns:1fr}}
.viz-3 .dim{border:1px solid var(--rule-soft);border-radius:8px;padding:8px 10px;background:var(--paper)}
.viz-3 .dim .dn{font-size:12.5px;color:var(--ink);font-weight:600}
.viz-3 .dim .dp{font-family:var(--mono);font-size:9.5px;color:var(--fern)}
.viz-3 .dim .dl{font-family:var(--mono);font-size:9px;color:var(--ink-3);margin-top:3px;line-height:1.4}
.viz-3 .v3-flag{margin:12px 0 0;border-left:3px solid var(--terracotta);background:var(--paper-2);border-radius:0 9px 9px 0;padding:10px 13px;font-size:12.5px;color:var(--ink-2);line-height:1.55}
.viz-3 .v3-flag b{color:var(--terracotta)}
.viz-3 .v3-flag+.v3-flag{margin-top:8px}
.viz-3 .viz-src{font-family:var(--mono);font-size:10.5px;color:var(--ink-3);margin:12px 0 0;line-height:1.65}
@media(prefers-reduced-motion:reduce){.viz-3 *{transition:none!important}}
</style>
  <div class="viz-h">
    <span class="viz-id">VIZ-3</span>
    <span class="viz-t">The 3D morphospace — every point a real coded figure</span>
    <span class="chip chip-cand">candidate</span>
    <span class="chip chip-actual">ACTUAL · unsupervised · from our data</span>
  </div>
  <p class="viz-lede">The computed geometry, rendered for the first time. <b id="v3-n"></b> real coded points on the three axes the space <b>found by itself</b> — we did not tell it what to look for. <b>Drag to rotate; click any point</b> for its figure and its six coordinates (that is the answer to “is this from our data?”). The clusters are <b>loose on purpose</b>: the silhouette is weak, the space is a continuum that bleeds — so there are no hulls, no blobs, no tidy cluster colours. Highlight a value and watch it <i>scatter</i>, not clump.</p>

  <div class="v3-main">
    <div class="v3-stage" id="v3-stage"><div class="hint">drag to rotate · click a point</div></div>
    <div class="v3-side">
      <div class="v3-read" id="v3-read"><div class="empty">Click a point to read the figure and its six coordinates. Clicking <b>Thich Nhat Hanh</b> shows <i>embodied-practice · process-becoming · analogical-mapping · liberation · reparative · dependent-arising</i> — proof the map is our data, not random.</div></div>
      <div class="v3-hl">
        <div class="v3-hl-h">Highlight a value — see whether it clumps</div>
        <select id="v3-axis"></select>
        <div class="v3-vals" id="v3-vals"></div>
      </div>
    </div>
  </div>

  <div class="v3-diag" id="v3-diag"></div>
  <div class="dims" id="v3-dims"></div>

  <div class="v3-flag"><b>The claim we do NOT make:</b> dim-3 matching the apophatic/kataphatic distinction our reading surfaced is a <b>coherence check, not independent discovery</b> — the axis menu the geometry runs on already contains the value “apophatic,” and coding + reading came from the same emitter with the same vocabulary. A space built from a menu including “apophatic” recovering an apophatic axis says the coding is internally consistent, not that it corroborates itself. Settling discovery-vs-consistency needs a rater outside the pipeline (TG-1b).</div>
  <div class="v3-flag"><b>Occupancy:</b> this is the geometry of what has been <b>coded (~31% of the roster)</b>, not of what we hold. And the first run of this analysis was <b>wrong in a beautiful way</b>: a coder-fallback value (“insufficient-context”) hijacked the largest axis via mass-correction; 13 shrugging figures formed a spurious outlier cluster. Dropping them (keeping the legitimate “not-asserted” / “unspecified”) produced this clean result — the specimen of the failure this method most needs to fear.</div>

  <p class="viz-src">Source — the 483 points and their coordinates: <code>DATA_mca_morphospace_coords_2026-07-14.json</code> (method: MCA, indicator matrix, Greenacre-adjusted). Axis English names + loadings: §D6 (the file's own loadings corroborate them). <b>Numbers are the file's</b>, not the SPA prose — see the delivery report's flag. No source-passage field exists in the data, so the readout shows the six coordinates, not a passage. Stage&nbsp;6&nbsp;=&nbsp;0.</p>
<script>
(function(){
  var D=__DATA__;
  document.getElementById('v3-n').textContent=D.P.length+' figures';
  var stage=document.getElementById('v3-stage'), read=document.getElementById('v3-read');
  var W=640,H=440,cx=W/2,cy=H/2;
  // center + fit-scale from raw coords
  var mx=0,my=0,mz=0; D.P.forEach(function(p){mx+=p.x;my+=p.y;mz+=p.z;}); mx/=D.P.length;my/=D.P.length;mz/=D.P.length;
  var maxr=0; D.P.forEach(function(p){var r=Math.max(Math.abs(p.x-mx),Math.abs(p.y-my),Math.abs(p.z-mz)); if(r>maxr)maxr=r;});
  var scale=(Math.min(W,H)*0.40)/maxr;
  var yaw=-0.5, pitch=0.35, hlAxis='O', hlVal=null;
  var NS='http://www.w3.org/2000/svg';
  var svg=document.createElementNS(NS,'svg'); svg.setAttribute('class','v3-svg'); svg.setAttribute('viewBox','0 0 '+W+' '+H);
  stage.insertBefore(svg,stage.firstChild);
  function esc(s){return String(s).replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c];});}
  function project(p){
    var X=p.x-mx,Y=p.y-my,Z=p.z-mz;
    var ca=Math.cos(yaw),sa=Math.sin(yaw), x1=X*ca-Z*sa, z1=X*sa+Z*ca;
    var cb=Math.cos(pitch),sb=Math.sin(pitch), y1=Y*cb-z1*sb, z2=Y*sb+z1*cb;
    return {sx:cx+x1*scale, sy:cy-y1*scale, d:z2};
  }
  var els=[];
  function build(){
    while(svg.firstChild) svg.removeChild(svg.firstChild);
    // axis triad (drawn from centre)
    var axes=[[1,0,0,'dim1 · secular↔religious'],[0,1,0,'dim2 · personal↔void'],[0,0,1,'dim3 · kataphatic↔apophatic']];
    axes.forEach(function(a){
      var p0=project({x:mx,y:my,z:mz}), p1=project({x:mx+a[0]*maxr*1.15,y:my+a[1]*maxr*1.15,z:mz+a[2]*maxr*1.15});
      var ln=document.createElementNS(NS,'line'); ln.setAttribute('class','axline');
      ln.setAttribute('x1',p0.sx.toFixed(1));ln.setAttribute('y1',p0.sy.toFixed(1));ln.setAttribute('x2',p1.sx.toFixed(1));ln.setAttribute('y2',p1.sy.toFixed(1));
      svg.appendChild(ln);
      var tx=document.createElementNS(NS,'text'); tx.setAttribute('class','axcap'); tx.setAttribute('x',p1.sx.toFixed(1)); tx.setAttribute('y',p1.sy.toFixed(1)); tx.textContent=a[3]; svg.appendChild(tx);
    });
    els=D.P.map(function(p,i){ return {p:p, pr:project(p)}; });
    els.sort(function(a,b){return a.pr.d-b.pr.d;}); // far first
    els.forEach(function(o){
      var p=o.p, pr=o.pr;
      var dn=(pr.d+maxr)/(2*maxr); // 0 far .. 1 near
      var r=(2.2+dn*2.4).toFixed(1);
      var hit = hlVal===null || p[hlAxis]===hlVal;
      var c=document.createElementNS(NS,'circle'); c.setAttribute('class','pt');
      c.setAttribute('cx',pr.sx.toFixed(1)); c.setAttribute('cy',pr.sy.toFixed(1)); c.setAttribute('r',r);
      if(hlVal!==null){ c.setAttribute('fill', hit?'var(--fern)':'var(--ink-3)'); c.setAttribute('fill-opacity', hit?(0.55+dn*0.4):0.12); }
      else { c.setAttribute('fill','var(--moss)'); c.setAttribute('fill-opacity',(0.30+dn*0.45).toFixed(2)); }
      c.addEventListener('click',function(ev){ ev.stopPropagation(); showPt(p, c); });
      svg.appendChild(c); o.c=c;
    });
  }
  function showPt(p, c){
    svg.querySelectorAll('.pt').forEach(function(e){e.setAttribute('stroke','none');});
    if(c){c.setAttribute('stroke','var(--terracotta)');c.setAttribute('stroke-width','1.6');}
    var frame = p.fn>1 ? ' · frame '+p.fi+' of '+p.fn : '';
    read.innerHTML='<div class="rf">'+esc(p.f)+'</div><div class="rfr">a coded figure'+frame+'</div>'
      +[['epistemic-warrant',p.E],['ontological-commitment',p.O],['inferential-operation',p.M],['telos',p.T],['stance',p.S],['ground-world-relation',p.G]]
        .map(function(r){return '<div class="rc"><span class="rk">'+r[0]+'</span><span class="rv">'+esc(r[1])+'</span></div>';}).join('');
  }
  // drag-rotate (pointer = mouse + touch)
  var dragging=false,lx=0,ly=0,raf=null;
  function schedule(){ if(raf) return; raf=requestAnimationFrame(function(){raf=null;build();}); }
  stage.addEventListener('pointerdown',function(e){dragging=true;lx=e.clientX;ly=e.clientY;stage.classList.add('drag');stage.setPointerCapture(e.pointerId);});
  stage.addEventListener('pointermove',function(e){ if(!dragging)return; yaw+=(e.clientX-lx)*0.01; pitch+=(e.clientY-ly)*0.01; pitch=Math.max(-1.4,Math.min(1.4,pitch)); lx=e.clientX;ly=e.clientY; schedule(); });
  stage.addEventListener('pointerup',function(e){dragging=false;stage.classList.remove('drag');});
  stage.addEventListener('pointercancel',function(){dragging=false;stage.classList.remove('drag');});
  // highlight controls
  var axSel=document.getElementById('v3-axis'), valsEl=document.getElementById('v3-vals');
  D.axes.forEach(function(a){var o=document.createElement('option');o.value=a.k;o.textContent=a.name;axSel.appendChild(o);});
  axSel.value='O';
  function renderVals(){
    hlAxis=axSel.value; hlVal=null;
    valsEl.innerHTML=D.axisValues[hlAxis].map(function(v){
      var n=D.P.filter(function(p){return p[hlAxis]===v;}).length;
      return '<button type="button" class="vchip" data-v="'+esc(v)+'">'+esc(v)+' <span class="n">'+n+'</span></button>';
    }).join('');
    valsEl.querySelectorAll('.vchip').forEach(function(b){ b.addEventListener('click',function(){
      var v=b.getAttribute('data-v');
      if(hlVal===v){hlVal=null;b.classList.remove('on');} else {hlVal=v; valsEl.querySelectorAll('.vchip').forEach(function(x){x.classList.toggle('on',x===b);});}
      build();
    });});
  }
  axSel.addEventListener('change',function(){renderVals();build();});
  // diagnostics
  var dg=document.getElementById('v3-diag');
  dg.innerHTML=''
   +'<div class="diag"><div class="dv">'+D.inertia3+'%</div><div class="dk">adjusted inertia (3D)</div><div class="dg">Good — most of the structure fits in three dimensions, so a 3D picture isn\\'t hiding much.</div></div>'
   +'<div class="diag"><div class="dv">'+D.agree+'</div><div class="dk">MCA vs Gower/PCoA</div><div class="dg">Moderate — two independent methods broadly agree about distances, but this is not a tight lock. Not a strong claim.</div></div>'
   +'<div class="diag weak"><div class="dv">'+D.sil+'</div><div class="dk">held-out silhouette (O)</div><div class="dg">Weak-positive — 1 = tidy clusters, 0 = none. The traditions do <b>not</b> sit in neat clumps; the space is a continuum. If someone wants to attack this work, aim here — which is why it\\'s on the page.</div></div>';
  var dm=document.getElementById('v3-dims');
  dm.innerHTML=D.dims.map(function(x){return '<div class="dim"><div class="dn">'+x.name+'</div><div class="dp">'+x.pct+'% of structure</div><div class="dl">loads on '+esc(x.loads)+'</div></div>';}).join('');
  renderVals(); build();
})();
</script>
</div>'''
    block = BLOCK.replace("__DATA__", DATA)
    h = open(page_path, encoding="utf-8").read()
    pat = re.compile(r'<div class="vizslot"[^>]*>\s*<div class="vs-h"><span class="vs-id">VIZ-3</span>.*?</div>\s*</div>', re.S)
    assert pat.search(h), "VIZ-3 vizslot not matched"
    h2 = pat.sub(lambda _: block, h, count=1)
    open(page_path, "w", encoding="utf-8").write(h2)
    left = h2.count('class="vizslot"')
    print(f"VIZ-3 installed · {len(P)} points · {len(fc)} distinct figures · sil {d['O_silhouette']} · slots left: {left}")

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
