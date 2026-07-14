#!/usr/bin/env python3
"""Build the seven-figure transmission-structure case-study page from reading-SB's coordinate feed.

Seed-agnostic + idempotent (per feedback_systematic_seed_agnostic_idempotent): reads ANY
DATA_*_coordinates feed of the same shape and emits the case-study HTML. reading-SB will
re-emit full 6-axis coords per portrayal on request; re-run this to regenerate.

Usage: build_transmission.py <coords.json> <OUTPUT.html>
"""
import json, sys, html

def esc(s): return html.escape(str(s), quote=True)

def build(feed_path, out_path):
    d = json.load(open(feed_path))
    meta = d["_meta"]
    figs = sorted(d["figures"], key=lambda f: f.get("base_spread", 0))

    # ---- spectrum hero: 7 dots on a protected(green)→contested(red) track ----
    dots = []
    for i, f in enumerate(figs):
        spread = f.get("base_spread", 0.0)
        left = 3.5 + spread * 93.0            # inset so 0.0 and 1.0 aren't clipped
        above = (i % 2 == 1)                  # stagger labels to avoid collision
        cls = "cd " + ("green" if f["color"] == "green" else "red")
        lbl = ("lab above" if above else "lab below")
        dots.append(
            f'<div class="{cls}" style="left:{left:.1f}%">'
            f'<span class="{lbl}"><b>{esc(f["figure"])}</b><i>{spread:.2f}</i></span></div>'
        )
    spectrum = "".join(dots)

    # ---- one card per figure (ordered by spread) ----
    ESS = meta.get("essence_axis", "ontological-commitment")
    cards = []
    for f in figs:
        green = f["color"] == "green"
        ccls = "fig green" if green else "fig red"
        status = esc(f["essence_status"])
        stcls = "st-prot" if green else "st-cont"
        spread = f.get("base_spread", 0.0)

        # per-portrayal: essence value + out-of-custody flag
        def is_out(p): return any(k in p.get("custody", "").lower() for k in ("outside", "out-of-custody", "gnostic"))
        def is_myst(p): return bool(p.get("mystical", False))
        ess_vals = [p.get(ESS, "—") for p in f["portrayals"]]
        core_vals = [p.get(ESS, "—") for p in f["portrayals"] if not is_myst(p)]  # the non-mystical CORE
        myst_vals = [p.get(ESS, "—") for p in f["portrayals"] if is_myst(p)]      # the mystical breakers
        uniq = list(dict.fromkeys(ess_vals))                 # all distinct essence values (for verdict)
        mode = core_vals[0] if core_vals else (ess_vals[0] if ess_vals else "—")
        essence_agrees = (len(set(core_vals)) == 1)          # the non-mystical CORE agrees (mystical breakers excluded)

        chips = []
        for p in f["portrayals"]:
            ev = p.get(ESS, "—")
            chcls = "chip"
            if is_myst(p):          chcls += " mystical" # the essence-shifter → metaxy-indigo halo (Thomas/Isaiah/Sufi/Zhuangzi)
            elif is_out(p):         chcls += " out"      # out-of-custody but not mystical → amber (rare)
            elif essence_agrees:    chcls += " held"     # non-mystical core agrees → green
            else:                   chcls += " rival"    # rival cores, no shared essence → red (Confucius/Freud)
            # secondary domain-axis variance (transcendent/immanent, prophetic/divine…)
            dom = ""
            for k, v in p.items():
                if k.startswith("domain_axis"):
                    axname = k.replace("domain_axis_", "").replace("_", " ")
                    dom = f'<span class="dom">{esc(axname)}: {esc(v)}</span>'
            chips.append(
                f'<div class="{chcls}"><div class="cl">{esc(p["label"])}</div>'
                f'<div class="cu">{esc(p.get("custody","—"))}</div>'
                f'<div class="ce">{esc(ev)}{dom}</div></div>'
            )
        chips_html = "".join(chips)

        # verdict line — driven by the feed's own status/color, not recomputed
        myst_names = [esc(p["label"].replace(" (out-of-custody)", "")) for p in f["portrayals"] if is_myst(p)]
        myst_ess = " / ".join(dict.fromkeys(esc(v) for v in myst_vals))
        if green:
            if not myst_vals and len(set(core_vals)) == 1:
                verdict = f'<b>essence invariant</b> — every framer holds <em>{esc(mode)}</em>. Variance, where it exists, lives in a <em>domain</em> axis, not the essence.'
            elif myst_vals:
                verdict = f'<b>the custodial core holds</b> <em>{esc(mode)}</em>; the <span class="myst-word">mystical strand</span> ({", ".join(myst_names)}) breaks toward <em>{myst_ess}</em>. Custody protects the core — the mystical turn is what shifts it.'
            else:
                verdict = f'<b>essence protected in custody</b> — the canonical framers hold <em>{esc(mode)}</em>; the out-of-custody reading deviates. <em>Custody, not sacredness, does the protecting.</em>'
        else:
            core_uniq = list(dict.fromkeys(core_vals))
            if len(set(core_vals)) == 1 and not myst_vals:
                verdict = f'ontology <em>agreed</em> (<em>{esc(mode)}</em>) — but the contest is real elsewhere: {status.lower()}.'
            else:
                parts = " vs ".join(esc(u) for u in core_uniq)
                mtail = f' — the <span class="myst-word">mystical strand</span> ({", ".join(myst_names)}) sits at <em>{myst_ess}</em>' if myst_vals else ''
                verdict = f'<b>essence rewritten</b> — rival custody, no shared core: <em>{parts}</em>{mtail}.'

        cards.append(f"""
  <div class="{ccls}">
    <div class="fh">
      <div class="fname">{esc(f['figure'])} <span class="fdom">{esc(f['domain'])}</span></div>
      <span class="stat {stcls}">{status}</span>
    </div>
    <div class="fmeta"><span class="tx">{esc(f['transmission_structure'])}</span><span class="spread"><i style="width:{spread*100:.0f}%"></i></span><span class="sv">spread {spread:.2f}</span></div>
    <div class="chips">{chips_html}</div>
    <div class="verdict {'v-green' if green else 'v-red'}">{verdict}</div>
    <p class="note">{esc(f['note'])}</p>
  </div>""")
    cards_html = "".join(cards)

    # ---- JS-friendly data for the interactive stage ----
    def _is_out(p): return any(k in p.get("custody", "").lower() for k in ("outside", "out-of-custody", "gnostic"))
    js_figs = []
    for f in figs:
        ports = []
        for p in f["portrayals"]:
            ev = p.get(ESS, "—")
            dom = next((f'{k.replace("domain_axis_","").replace("_"," ")}: {v}'
                        for k, v in p.items() if k.startswith("domain_axis")), "")
            ports.append({"label": p["label"], "custody": p.get("custody", "—"),
                          "ess": ev, "out": _is_out(p), "myst": bool(p.get("mystical", False)), "dom": dom})
        core = [pp["ess"] for pp in ports if not pp["myst"]]  # non-mystical core
        all_ess = [pp["ess"] for pp in ports]
        js_figs.append({"figure": f["figure"], "color": f["color"],
                        "tx": f["transmission_structure"], "spread": f.get("base_spread", 0.0),
                        "status": f["essence_status"],
                        "all_agree": len(set(all_ess)) == 1,   # every framer shares one essence (Buddha, Socrates)
                        "icv": core[0] if core else "—", "ports": ports})
    FIGS_JSON = json.dumps(js_figs, ensure_ascii=False)

    STAGE_JS = """<script>
(function(){
  var FIGS = __FIGS_JSON__;
  var picker=document.getElementById('picker'), stage=document.getElementById('stage'),
      cap=document.getElementById('scap'), vtog=document.getElementById('vtog');
  var VIEW='A', CUR=0;                                  // A = core only; B = + mystical outliers
  function xFor(val, uv){ return uv.length<2 ? 50 : 16 + 68*(uv.indexOf(val)/(uv.length-1)); }
  function esc(s){ return String(s).replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c];}); }
  function uniqEss(ports){ var uv=[]; ports.forEach(function(p){ if(uv.indexOf(p.ess)<0) uv.push(p.ess); }); return uv; }
  function render(){
    var f=FIGS[CUR];
    var shown = f.ports.filter(function(p){ return VIEW==='B' || !p.myst; });  // View A hides mystical outliers
    var uv=uniqEss(shown);
    Array.prototype.slice.call(stage.querySelectorAll('.sc')).forEach(function(el){ el.remove(); });
    var isDiverge = (f.color==='red' && !f.all_agree);   // Confucius/Freud: rival custody, no shared core
    // dynamic vertical spacing so a tall stack of core framers always fits the stage
    var col={}; shown.forEach(function(p){ var kk=xFor(p.ess,uv).toFixed(1); col[kk]=(col[kk]||0)+1; });
    var maxStack=1; for(var kk in col){ if(col[kk]>maxStack) maxStack=col[kk]; }
    var gap = maxStack<2 ? 54 : Math.min(54, Math.floor(176/(maxStack-1)));
    var atX={};
    shown.forEach(function(p){
      var x=xFor(p.ess, uv), key=x.toFixed(1);
      atX[key]=(atX[key]||0); var yoff=atX[key]*gap; atX[key]++;
      // non-mystical chips: held (green) unless this is a rival-custody diverge → rival (red)
      var cls = p.myst ? 'mystical' : (p.out ? 'out' : (isDiverge ? 'rival' : 'held'));
      var el=document.createElement('div');
      el.className='sc '+cls;
      el.innerHTML='<b>'+esc(p.label)+'</b><i>'+esc(p.ess)+'</i>'+(p.dom?'<u>'+esc(p.dom)+'</u>':'')+(p.myst?'<u class="mtag">mystical strand</u>':'');
      el.style.left='50%'; el.style.top=(42+yoff)+'px'; el.style.opacity='0';
      stage.appendChild(el);
      void el.offsetWidth;                 // force reflow so the transition triggers reliably
      el.style.left=x+'%'; el.style.opacity='1';
    });
    // caption
    var mysts = shown.filter(function(p){return p.myst;});
    var domNote = shown.some(function(p){return p.dom;}) ? ' The visible difference among the core sits in a domain axis, not the essence.' : '';
    var sp='  <span style="opacity:.7">spread '+f.spread.toFixed(2)+'</span>';
    if(isDiverge){
      cap.className='scap div';
      var mn2 = mysts.length ? '  The <b class="mw">mystical strand</b> ('+mysts.map(function(p){return esc(p.label.replace(' (Daoist)','').replace(' (out-of-custody)',''));}).join(', ')+') is the apophatic pole.' : '';
      cap.innerHTML='<b>Diverges.</b> Rival custody, no shared core \\u2014 <em>'+uv.map(esc).join(' vs ')+'</em>.'+mn2+sp;
    } else if(mysts.length){
      var mn = mysts.map(function(p){return esc(p.label.replace(' (out-of-custody)',''));}).join(', ');
      var me = mysts.map(function(p){return esc(p.ess);}).filter(function(v,i,a){return a.indexOf(v)===i;}).join(' / ');
      cap.className='scap myst';
      cap.innerHTML='<b>The core holds.</b> The custodial framers cluster on one essence \\u2014 <em>'+esc(f.icv)+'</em> \\u2014 and the <b class="mw">mystical strand</b> ('+mn+') breaks away toward <em>'+me+'</em>. Custody protects the core; the mystical turn is what shifts it.'+sp;
    } else if(f.color==='red' && f.all_agree){
      cap.className='scap conv';
      cap.innerHTML='<b>Converges on the essence.</b> Every framer holds <em>'+esc(f.icv)+'</em> \\u2014 the contest is real, but it lives elsewhere ('+esc(f.status).toLowerCase()+'), not in the ontology.'+sp;
    } else {
      cap.className='scap conv';
      cap.innerHTML='<b>Converges.</b> The custodial framers hold one essence \\u2014 <em>'+esc(f.icv)+'</em>.'+domNote+sp;
    }
  }
  function select(i){ CUR=i; Array.prototype.forEach.call(picker.children,function(b,j){ b.classList.toggle('on', j===i); }); render(); }
  function setView(v){ VIEW=v; Array.prototype.forEach.call(vtog.querySelectorAll('.vbtn'),function(b){ b.classList.toggle('on', b.getAttribute('data-v')===v); }); render(); }
  FIGS.forEach(function(f,i){
    var b=document.createElement('button');
    b.className='pbtn '+(f.color==='green'?'green':'red');
    b.textContent=f.figure; b.onclick=function(){ select(i); };
    picker.appendChild(b);
  });
  Array.prototype.forEach.call(vtog.querySelectorAll('.vbtn'),function(b){
    if(!b.classList.contains('disabled')) b.onclick=function(){ setView(b.getAttribute('data-v')); };
  });
  setView('A'); select(0);
})();
</script>"""

    HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>What protects a founder's essence — custody, not sacredness — Grammar of Meaning</title>
<style>
  :root{{--paper:#f7f2e7;--paper2:#fffdf7;--card:#fffefa;--ink:#26221a;--ink2:#5b5346;--ink3:#8a8172;--line:#e4dcc9;--line2:#d0c6ae;--moss:#4b6b46;--moss-d:#33502f;--gold:#b8892f;--gold-bg:#f6ecd4;--green:#4b6b46;--green-bg:#e8efe2;--red:#9c3f37;--red-bg:#f4e3e0;--amber:#ba7517;--amber-bg:#faeeda;--myst:#5b53a6;--myst-bg:#eae7f6;--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;--sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,sans-serif;--serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;}}
  @media (prefers-color-scheme:dark){{:root{{--paper:#14130f;--paper2:#1a1813;--card:#1e1b15;--ink:#ece7dc;--ink2:#b3aa98;--ink3:#847c6c;--line:#332f27;--line2:#423d31;--moss:#8fb884;--moss-d:#6c9a62;--gold:#e0b45f;--gold-bg:#2c2410;--green:#8fb884;--green-bg:#1c2a18;--red:#d98b80;--red-bg:#301b18;--amber:#e0b45f;--amber-bg:#3a2a0a;--myst:#a99ee6;--myst-bg:#221d38;}}}}
  *{{box-sizing:border-box}}
  body{{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:15.5px;line-height:1.62;-webkit-font-smoothing:antialiased}}
  .wrap{{max-width:860px;margin:0 auto;padding:0 22px 90px}}
  a{{color:var(--moss-d)}}@media(prefers-color-scheme:dark){{a{{color:var(--moss)}}}}
  header{{padding:44px 0 20px;border-bottom:2px solid var(--line2)}}
  .eyebrow{{font-family:var(--mono);font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);margin:0 0 10px}}
  h1{{font-family:var(--serif);font-weight:500;font-size:32px;line-height:1.13;margin:0 0 8px;letter-spacing:-.015em}}
  .sub{{color:var(--ink2);font-size:16.5px;max-width:64ch;margin:0}}
  h2{{font-family:var(--serif);font-weight:500;font-size:21px;margin:40px 0 6px;letter-spacing:-.01em}}
  p{{margin:10px 0}}.lead{{color:var(--ink2)}}
  .callout{{background:var(--card);border:1px solid var(--line2);border-left:3px solid var(--moss);border-radius:0 10px 10px 0;padding:14px 18px;margin:18px 0;font-size:14.5px;color:var(--ink2)}}
  .callout b{{color:var(--ink)}}
  .backlink{{display:inline-block;margin:30px 0 0;font-family:var(--mono);font-size:12px}}
  .foot{{margin-top:44px;padding-top:16px;border-top:1px solid var(--line);font-family:var(--mono);font-size:12px;color:var(--ink3);line-height:1.7}}
  .sr-only{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)}}
  /* spectrum hero */
  .spec-wrap{{margin:26px 0 60px;padding:0 6px}}
  .spec-ends{{display:flex;justify-content:space-between;font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;margin:0 0 8px}}
  .spec-ends .l{{color:var(--green)}}.spec-ends .r{{color:var(--red)}}
  .track{{position:relative;height:8px;border-radius:99px;background:linear-gradient(90deg,var(--green) 0%,var(--gold) 46%,var(--red) 100%);margin:44px 0}}
  .cd{{position:absolute;top:50%;width:15px;height:15px;border-radius:50%;transform:translate(-50%,-50%);border:2.5px solid var(--paper);box-shadow:0 0 0 1.5px var(--ink3)}}
  .cd.green{{background:var(--green)}}.cd.red{{background:var(--red)}}
  .cd .lab{{position:absolute;left:50%;transform:translateX(-50%);white-space:nowrap;font-family:var(--mono);font-size:10px;text-align:center;line-height:1.3}}
  .cd .lab b{{display:block;font-weight:600;color:var(--ink);font-size:11px}}
  .cd .lab i{{font-style:normal;color:var(--ink3)}}
  .cd .lab.above{{bottom:22px}}.cd .lab.below{{top:22px}}
  /* figure cards */
  .fig{{background:var(--card);border:1px solid var(--line2);border-radius:14px;padding:16px 18px;margin:14px 0}}
  .fig.green{{border-left:4px solid var(--green)}}.fig.red{{border-left:4px solid var(--red)}}
  .fh{{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap}}
  .fname{{font-family:var(--serif);font-size:21px;color:var(--ink)}}
  .fdom{{font-family:var(--sans);font-size:12.5px;color:var(--ink3);margin-left:4px}}
  .stat{{font-family:var(--mono);font-size:10.5px;letter-spacing:.05em;text-transform:uppercase;padding:3px 10px;border-radius:6px;font-weight:600;white-space:nowrap}}
  .st-prot{{background:var(--green-bg);color:var(--green)}}.st-cont{{background:var(--red-bg);color:var(--red)}}
  .fmeta{{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin:8px 0 12px}}
  .fmeta .tx{{font-family:var(--mono);font-size:11px;color:var(--ink2)}}
  .fmeta .spread{{flex:1;min-width:80px;height:5px;border-radius:99px;background:var(--line);overflow:hidden}}
  .fmeta .spread i{{display:block;height:100%;background:linear-gradient(90deg,var(--green),var(--red))}}
  .fmeta .sv{{font-family:var(--mono);font-size:10.5px;color:var(--ink3)}}
  .chips{{display:flex;gap:9px;flex-wrap:wrap;margin:4px 0 2px}}
  .chip{{flex:1;min-width:150px;border-radius:10px;padding:9px 11px;border:1px solid var(--line2);background:var(--paper2)}}
  .chip .cl{{font-family:var(--serif);font-size:14.5px;color:var(--ink);line-height:1.25}}
  .chip .cu{{font-family:var(--mono);font-size:9.5px;letter-spacing:.04em;text-transform:uppercase;color:var(--ink3);margin:3px 0 6px}}
  .chip .ce{{font-family:var(--mono);font-size:11px;color:var(--ink2)}}
  .chip .ce .dom{{display:block;color:var(--ink3);margin-top:3px}}
  .chip.held{{border-color:var(--green);background:var(--green-bg)}}
  .chip.held .ce{{color:var(--green);font-weight:600}}
  .chip.dev,.chip.out{{border-color:var(--amber);background:var(--amber-bg)}}
  .chip.dev .ce,.chip.out .ce{{color:var(--amber);font-weight:600}}
  .chip.rival{{border-color:var(--red);background:var(--red-bg)}}
  .chip.rival .ce{{color:var(--red);font-weight:600}}
  .chip.mystical{{border-color:var(--myst);background:var(--myst-bg);box-shadow:0 0 0 3px var(--myst-bg),0 0 0 4px var(--myst)}}
  .chip.mystical .ce{{color:var(--myst);font-weight:600}}
  .myst-word,.mw{{color:var(--myst);font-weight:600;font-style:normal}}
  .verdict{{margin:12px 0 0;font-size:14px;padding:9px 13px;border-radius:8px}}
  .verdict.v-green{{background:var(--green-bg);color:var(--green)}}
  .verdict.v-red{{background:var(--red-bg);color:var(--red)}}
  .verdict b{{font-weight:700}}.verdict em{{font-style:normal;font-family:var(--mono);font-size:12.5px}}
  .note{{margin:10px 0 0;font-size:13.5px;color:var(--ink2)}}
  .legend{{display:flex;gap:16px;flex-wrap:wrap;font-family:var(--mono);font-size:11px;color:var(--ink3);margin:14px 0 0}}
  .legend span{{display:inline-flex;align-items:center;gap:6px}}
  .legend i{{width:11px;height:11px;border-radius:3px;display:inline-block}}
  .sw-held{{background:var(--green-bg);border:1px solid var(--green)}}
  .sw-dev{{background:var(--amber-bg);border:1px solid var(--amber)}}
  .sw-rival{{background:var(--red-bg);border:1px solid var(--red)}}
  .sw-myst{{background:var(--myst-bg);border:1px solid var(--myst);box-shadow:0 0 0 1.5px var(--myst)}}
  /* interactive stage — pick a figure → watch it hold or split */
  .picker{{display:flex;gap:8px;flex-wrap:wrap;margin:16px 0 18px}}
  .pbtn{{font-family:var(--sans);font-size:14px;padding:7px 14px;border-radius:99px;border:1.5px solid var(--line2);background:var(--paper2);color:var(--ink2);cursor:pointer;transition:all .18s}}
  .pbtn.green.on{{border-color:var(--green);background:var(--green-bg);color:var(--green);font-weight:600}}
  .pbtn.red.on{{border-color:var(--red);background:var(--red-bg);color:var(--red);font-weight:600}}
  .pbtn:hover{{border-color:var(--ink3)}}
  .stagewrap{{position:relative;height:304px;background:var(--paper2);border:1px solid var(--line2);border-radius:14px;margin:0 0 4px;overflow:hidden}}
  .axisline{{position:absolute;left:6%;right:6%;top:26px;height:2px;background:var(--line2)}}
  .axistick{{position:absolute;top:14px;font-family:var(--mono);font-size:9.5px;letter-spacing:.05em;text-transform:uppercase;color:var(--ink3);transform:translateX(-50%)}}
  .converge-pt{{position:absolute;left:50%;top:20px;width:14px;height:14px;border-radius:50%;transform:translate(-50%,-50%);border:2px dashed var(--ink3);opacity:.5}}
  .sc{{position:absolute;transform:translateX(-50%);width:150px;border-radius:10px;padding:8px 10px;border:1.5px solid var(--line2);background:var(--card);left:50%;opacity:0;transition:left .72s cubic-bezier(.34,.02,.24,1),top .72s cubic-bezier(.34,.02,.24,1),opacity .5s}}
  .sc b{{display:block;font-family:var(--serif);font-size:13.5px;color:var(--ink);line-height:1.2}}
  .sc i{{font-style:normal;font-family:var(--mono);font-size:10.5px;display:block;margin-top:3px}}
  .sc u{{text-decoration:none;display:block;font-family:var(--mono);font-size:9px;color:var(--ink3);margin-top:3px}}
  .sc.held{{border-color:var(--green);background:var(--green-bg);box-shadow:0 1px 6px rgba(75,107,70,.14)}}.sc.held i{{color:var(--green);font-weight:600}}
  .sc.out{{border-color:var(--amber);background:var(--amber-bg);box-shadow:0 1px 6px rgba(186,117,23,.16)}}.sc.out i{{color:var(--amber);font-weight:600}}
  .sc.rival{{border-color:var(--red);background:var(--red-bg);box-shadow:0 1px 6px rgba(156,63,55,.16)}}.sc.rival i{{color:var(--red);font-weight:600}}
  .sc.mystical{{border-color:var(--myst);background:var(--myst-bg);box-shadow:0 0 0 4px var(--paper2),0 0 0 6px var(--myst),0 2px 10px rgba(91,83,166,.28)}}.sc.mystical i{{color:var(--myst);font-weight:600}}
  .sc .mtag{{color:var(--myst);font-weight:600;letter-spacing:.03em;text-transform:uppercase;font-size:8px}}
  .scap{{font-size:14.5px;padding:11px 15px;border-radius:9px;margin:0 0 8px}}
  .scap.conv{{background:var(--green-bg);color:var(--green)}}
  .scap.div{{background:var(--red-bg);color:var(--red)}}
  .scap.myst{{background:var(--myst-bg);color:var(--myst)}}
  .scap b{{font-weight:700}}.scap em{{font-style:normal;font-family:var(--mono);font-size:13px}}
  /* A/B/C view toggle */
  .vtog{{display:inline-flex;gap:0;border:1.5px solid var(--line2);border-radius:99px;padding:3px;margin:2px 0 10px;flex-wrap:wrap}}
  .vbtn{{font-family:var(--sans);font-size:13px;padding:6px 13px;border-radius:99px;border:0;background:transparent;color:var(--ink2);cursor:pointer;transition:all .18s}}
  .vbtn.on{{background:var(--ink);color:var(--paper);font-weight:600}}
  .vbtn.disabled{{color:var(--ink3);cursor:not-allowed;opacity:.6}}
  .vbtn:not(.on):not(.disabled):hover{{color:var(--ink)}}
</style>
</head>
<body>
<div class="wrap">
<h2 class="sr-only">A case study: run the instrument on seven founders across their rival portrayals and the essence axis stays invariant exactly when a single custodian or a shared core holds it, and splits when rival custodians hold no shared core — so custody, not sacredness, is what protects a founder's essence.</h2>
<header>
  <p class="eyebrow">the coding lab · case study · what protects an essence</p>
  <h1>Custody, not sacredness, protects a founder's essence</h1>
  <p class="sub">Take seven founders — Jesus, God, Muhammad, the Buddha, Confucius, Socrates, Freud — and read each one across the rival portrayals history left behind. On one axis, the <em>essence</em> ({esc(ESS)}), a pattern appears: the essence holds when a single custodian, or a genuinely shared core, keeps it; it splits when rival custodians share no core. What does the protecting is the <em>custody</em> — not the reverence.</p>
</header>

<h2>Pick a figure — watch it hold or split</h2>
<p class="lead">Choose a founder. The instrument places each surviving <em>framer</em> — "Matthew's Jesus", "Isaiah's God" — on the <em>essence</em> axis ({esc(ESS)}) and lets it move: framers that share the essence <strong>converge</strong>; framers whose custodians rewrote it <strong>diverge</strong>. Green = a custody protects the essence; red = rival custody splits it; <span class="myst-word">metaxy-indigo</span> = the <span class="myst-word">mystical strand</span>, the framer that breaks the essence toward the apophatic.</p>
<div class="vtog" id="vtog">
  <button class="vbtn on" data-v="A">View A · primary source</button>
  <button class="vbtn" data-v="B">View B · + mystical outliers</button>
  <button class="vbtn disabled" data-v="C" title="Gated on reading-SB's per-tradition periodizations (IRR192: not a single Küng line)">View C · reception over time · coming</button>
</div>
<p class="lead" style="font-size:14px;margin-top:2px">Toggle <b>A → B</b> and watch the mystical framer appear and break away. View A shows the in-custody core; View B adds the out-of-custody / mystical readings. View C (the framers on a reception era-axis) is held until the per-tradition periodizations land — it will be a multi-clock model, not a single timeline.</p>
<div class="picker" id="picker"></div>
<div class="stagewrap" id="stage">
  <div class="axisline"></div>
  <div class="axistick" style="left:50%">essence axis · {esc(ESS)}</div>
  <div class="converge-pt"></div>
</div>
<div class="scap" id="scap"></div>

<h2>The spectrum</h2>
<p class="lead">Seven figures, ordered by how far their portrayals spread apart on the essence axis. Green = the essence is protected (a single or shared-core custody). Red = the essence is contested (rival custody, no shared core). The number is the base spread, 0 (identical) to 1 (every axis differs).</p>
<div class="spec-wrap">
  <div class="spec-ends"><span class="l">◀ protected · shared custody</span><span class="r">contested · rival custody ▶</span></div>
  <div class="track">{spectrum}</div>
</div>

<h2>Read each one</h2>
<p class="lead">Each card holds the founder's rival portrayals as chips. A <span style="color:var(--green);font-weight:600">green</span> chip holds the shared essence; an <span style="color:var(--amber);font-weight:600">amber</span> chip is the one that leaves custody and deviates; <span style="color:var(--red);font-weight:600">red</span> chips are rival cores with nothing shared. Where a difference is real but lives in a <em>domain</em> axis rather than the essence, the chip names it underneath.</p>
<div class="legend"><span><i class="sw-held"></i>holds the shared essence</span><span><i class="sw-myst"></i>mystical strand · breaks the essence</span><span><i class="sw-dev"></i>out of custody · deviates</span><span><i class="sw-rival"></i>rival core · no shared essence</span></div>
<div class="callout" style="border-left-color:var(--myst)"><b class="myst-word">The mystical strand.</b> One pattern runs through every break: the framer that shifts the essence is always the <span class="myst-word">mystical / apophatic</span> one — Thomas among the gospels, Isaiah in the Tanakh, the Sufi Light in Islam, the Zhuangzi against the Analects. Each is marked in metaxy-indigo so you can see the breaks cluster at the mystical turn. The custody protects the core; the mystical strand is where it moves.</div>
{cards_html}

<div class="callout">
  <b>The exception that reveals the mechanism.</b> The Buddha's custody is <em>fragmented</em> — Theravāda and Mahāyāna are rival schools — yet the essence is <em>preserved</em>: both hold the void-ontology; only the epistemic warrant varies. Fragmentation alone doesn't break an essence. A <em>shared core</em> can protect it even without a single custodian. And Jesus shows the converse from the inside: the canonical portrayals stay invariant, and it is precisely the <em>out-of-custody</em> Gnostic reading that deviates. Custody, not sacredness, is the load-bearing thing.
</div>

<a class="backlink" href="coding-lab.html">← back to the coding lab</a>
<!--STAGEJS-->
<p class="foot">HOW PRODUCED · design-SB, built by build_transmission.py from reading-SB's feed {esc(meta.get('date',''))} ({esc(meta.get('source',''))}). Seed-agnostic + idempotent — regenerates when the feed updates. SCHOLARLY SOURCES · {esc(meta.get('source',''))}; the FINDINGS ledger V2–V12; the E×O×M×telos×stance×ground coordinate instrument. WHAT NEEDS VERIFICATION · N=1 matched pair per figure (demonstrator-grade); Confucius + Freud carry full 6-axis Sonnet-hardened coords, the others give the essence axis + the domain axis where the finding lives (full 6-axis re-run available on request). Stage 6 = 0.</p>
</div>
</body>
</html>"""
    HTML = HTML.replace("<!--STAGEJS-->", STAGE_JS.replace("__FIGS_JSON__", FIGS_JSON))
    open(out_path, "w").write(HTML)
    print(f"wrote {out_path} — {len(figs)} figures, {sum(len(f['portrayals']) for f in figs)} portrayals; interactive stage wired")

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
