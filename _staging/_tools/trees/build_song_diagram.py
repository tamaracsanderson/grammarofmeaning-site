#!/usr/bin/env python3
"""'She Loves You' as a what-happened / what-could-have-been docent-diagram (bakeoff #2b).

Researcher feedback on trailmap #2: (1) make the NEGATIVE SPACE the star — show the moves that
could have happened but didn't, not just the two actual outcomes; (2) needs a docent voice /
hand-holding; (3) do She-Loves-You first (easier than the theology); (4) show the chain as its
MOVES + what-could-have-been, not zoomed to one word.

This: the song's actual argument is the SOLID spine (what happened); at each move, DASHED
branches fan out — the roads not taken (what could have been) + the song's own silences. A
DOCENT TOUR (prev/next) walks one beat at a time, narrating plainly, so it's never a wall.

Candidate counterfactuals are design-illustration, flagged for reading-SB to bless (negative-
space content is her lane). Self-contained; no lyric text beyond the factual title/refrain.

Usage: build_song_diagram.py <OUTPUT.html>
"""
import sys, json

# the song's actual argument — the SOLID spine (what happened), left→right
BEATS = [
 dict(id="frame", x=150, star=False,
      move="A friend brings the news",
      plain="Before anything else: the whole song is one person telling <i>you</i> about someone else. A messenger. That framing choice shapes everything after it.",
      couldbe=[("she tells you herself", "a first-person “I love you” — a different song entirely"),
               ("a rival warns you off", "the messenger could have had a stake"),
               ("no one tells you", "you never find out — the news never arrives")]),
 dict(id="hurt", x=370, star=False,
      move="“You hurt her”",
      plain="The friend sets the backstory: there was a wound, and it was yours to answer for. The song opens in the aftermath of something that already went wrong.",
      couldbe=[("she hurt you", "the blame could have run the other way"),
               ("it was a mistake", "a misunderstanding, no one at fault"),
               ("nothing happened", "no wound at all — no reason for the song")]),
 dict(id="loves", x=590, star=True,
      move="“She loves you”",
      plain="The core move — the whole reason for the song. And notice its <b>form</b>: it is a <i>report about a third person</i> (“she loves you”), not an avowal (“I love you”). That grammatical choice is the move.",
      couldbe=[("“she doesn't anymore”", "the same messenger, the opposite news"),
               ("“she might”", "hedged, uncertain — a maybe instead of a fact"),
               ("“does she love you?”", "a question, not a report")],
      silence=("Does HE love her back?", "The song never says. It presses you to return to her — but your side of the feeling is left blank. A road the song refuses to walk.")),
 dict(id="glad", x=810, star=False,
      move="“So be glad”",
      plain="Having delivered the news, the friend tells you how to <i>feel</i> about it — glad. An instruction on your emotion, not just a fact.",
      couldbe=[("“be careful”", "the same news, a warning instead of joy"),
               ("“grieve it”", "treat the love as already lost"),
               ("“doubt it”", "don't trust the messenger")],
      silence=("Why does the friend care?", "The messenger's own stake is never given. Why are they doing this? The song's biggest silence sits right at its warmest moment.")),
 dict(id="back", x=1010, star=False,
      move="“Go back to her”",
      plain="The resolution: not just feel glad — <i>act</i>. Apologize, return. The song ends by pushing you off its own stage and back toward her.",
      couldbe=[("“let her go”", "accept it and move on"),
               ("“wait”", "do nothing yet"),
               ("“she should come to you”", "put the next move on her")],
      silence=("What does SHE want?", "She is talked about for the entire song and never speaks. The person at the center is the one voice we never hear.")),
]

def build(out):
    W,H=1160,560
    spine_y=150
    # spine segments (solid, what-happened)
    svg=[]
    for i in range(len(BEATS)-1):
        a,b=BEATS[i],BEATS[i+1]
        svg.append(f'<line class="spine" x1="{a["x"]+70}" y1="{spine_y}" x2="{b["x"]-70}" y2="{spine_y}"/>')
    # could-have-been branches (dashed) + silences, per beat
    for bi,bt in enumerate(BEATS):
        cx=bt["x"]
        # three could-be stubs fanning down
        n=len(bt["couldbe"])
        for j,(lab,why) in enumerate(bt["couldbe"]):
            bx=cx-70+(140*(j/(max(1,n-1)))) if n>1 else cx
            by=300+ (j%2)*54
            svg.append(f'<path class="cbedge b-{bt["id"]}" data-beat="{bt["id"]}" d="M {cx} {spine_y+20} C {cx} {spine_y+90}, {bx} {by-70}, {bx} {by-26}" fill="none"/>')
            svg.append(f'<g class="cbnode b-{bt["id"]}" data-beat="{bt["id"]}"><rect x="{bx-72}" y="{by-24}" width="144" height="46" rx="9"/>'
                       f'<text class="cbl" x="{bx}" y="{by-4}" text-anchor="middle">{lab}</text>'
                       f'<text class="cbw" x="{bx}" y="{by+13}" text-anchor="middle">{why[:34]}</text></g>')
        # silence marker (above the spine)
        if bt.get("silence"):
            sx=cx
            svg.append(f'<path class="siledge b-{bt["id"]}" data-beat="{bt["id"]}" d="M {cx} {spine_y-20} L {cx} {spine_y-64}" fill="none"/>')
            svg.append(f'<g class="silnode b-{bt["id"]}" data-beat="{bt["id"]}"><rect x="{sx-90}" y="{spine_y-108}" width="180" height="44" rx="9"/>'
                       f'<text class="silq" x="{sx}" y="{spine_y-88}" text-anchor="middle">the song never says:</text>'
                       f'<text class="sill" x="{sx}" y="{spine_y-72}" text-anchor="middle">{bt["silence"][0]}</text></g>')
    # spine nodes (the moves)
    for bt in BEATS:
        cx=bt["x"]; star="★ " if bt["star"] else ""
        cls="move"+(" star" if bt["star"] else "")
        svg.append(f'<g class="{cls}" data-beat="{bt["id"]}" tabindex="0"><rect x="{cx-70}" y="{spine_y-24}" width="140" height="48" rx="11"/>'
                   f'<text class="ml" x="{cx}" y="{spine_y+5}" text-anchor="middle">{star}{bt["move"]}</text></g>')
    svg_s="".join(svg)

    STEPS=json.dumps([{"id":b["id"],"move":b["move"],"plain":b["plain"],
                       "couldbe":b["couldbe"],"silence":b.get("silence")} for b in BEATS], ensure_ascii=False)

    HTML=f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>She Loves You — what happened, and what could have been</title>
<style>
  :root{{--paper:#f7f2e7;--paper2:#fffdf7;--card:#fffefa;--ink:#26221a;--ink2:#5b5346;--ink3:#8a8172;--line:#e4dcc9;--line2:#d0c6ae;--moss:#4b6b46;--moss-d:#33502f;--gold:#b8892f;--gold-bg:#f6ecd4;--myst:#5b53a6;--myst-bg:#eae7f6;--terra:#9c3f37;--terra-bg:#f7e7e4;--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;--sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,sans-serif;--serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;}}
  @media (prefers-color-scheme:dark){{:root{{--paper:#14130f;--paper2:#1a1813;--card:#1e1b15;--ink:#ece7dc;--ink2:#b3aa98;--ink3:#847c6c;--line:#332f27;--line2:#423d31;--moss:#8fb884;--moss-d:#6c9a62;--gold:#e0b45f;--gold-bg:#2c2410;--myst:#a99ee6;--myst-bg:#221d38;--terra:#d98b80;--terra-bg:#301b18;}}}}
  *{{box-sizing:border-box}} body{{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:15.5px;line-height:1.6}}
  .wrap{{max-width:1120px;margin:0 auto;padding:0 22px 80px}}
  a{{color:var(--moss-d)}}
  header{{padding:38px 0 12px}}
  .banner{{display:inline-block;font-family:var(--mono);font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#fff;background:var(--terra);padding:4px 10px;border-radius:5px;margin-bottom:13px}}
  .eyebrow{{font-family:var(--mono);font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);margin:0 0 9px}}
  h1{{font-family:var(--serif);font-weight:500;font-size:30px;line-height:1.12;margin:0 0 10px}}
  .orient{{background:var(--card);border:1px solid var(--line2);border-left:3px solid var(--moss);border-radius:0 12px 12px 0;padding:14px 18px;margin:6px 0 8px;font-size:15px;color:var(--ink2);max-width:84ch}}
  .orient b{{color:var(--ink)}} .orient .sol{{color:var(--moss-d);font-weight:600}} .orient .dsh{{color:var(--myst);font-weight:600}}
  .legend{{display:flex;gap:18px;flex-wrap:wrap;font-family:var(--mono);font-size:11px;color:var(--ink3);margin:6px 2px 4px}}
  .legend .sw{{display:inline-block;width:24px;height:0;border-top:3px solid var(--moss);vertical-align:middle;margin-right:6px}}
  .legend .sw.d{{border-top:2.5px dashed var(--myst)}} .legend .sw.s{{border-top:2.5px dashed var(--terra)}}
  .mapwrap{{overflow-x:auto;border:1px solid var(--line2);border-radius:14px;background:var(--paper2);margin-top:8px}}
  svg.diag{{display:block;width:100%;min-width:980px;height:auto}}
  .spine{{stroke:var(--moss);stroke-width:3.5;stroke-linecap:round}}
  .move rect{{fill:var(--card);stroke:var(--moss);stroke-width:2;transition:.16s;cursor:pointer}}
  .move.star rect{{fill:var(--gold-bg);stroke:var(--gold);stroke-width:2.6}}
  .move .ml{{font-family:var(--serif);font-size:14px;font-weight:600;fill:var(--ink);pointer-events:none}}
  .move.active rect{{filter:drop-shadow(0 3px 8px rgba(0,0,0,.16));stroke-width:3.2}}
  .cbedge{{stroke:var(--myst);stroke-width:1.8;stroke-dasharray:3 6;opacity:.35;transition:.18s}}
  .cbnode rect{{fill:var(--myst-bg);stroke:var(--myst);stroke-width:1.3;stroke-dasharray:3 4;opacity:.4;transition:.18s}}
  .cbnode .cbl{{font-family:var(--serif);font-size:12.5px;fill:var(--myst);font-weight:600;opacity:.5;transition:.18s}}
  .cbnode .cbw{{font-family:var(--sans);font-size:8.5px;fill:var(--ink3);opacity:.5;transition:.18s}}
  .siledge{{stroke:var(--terra);stroke-width:1.8;stroke-dasharray:2 5;opacity:.35;transition:.18s}}
  .silnode rect{{fill:var(--terra-bg);stroke:var(--terra);stroke-width:1.3;stroke-dasharray:2 4;opacity:.4;transition:.18s}}
  .silnode .silq{{font-family:var(--mono);font-size:8px;letter-spacing:.04em;text-transform:uppercase;fill:var(--terra);opacity:.55;transition:.18s}}
  .silnode .sill{{font-family:var(--serif);font-size:12.5px;font-weight:600;fill:var(--terra);opacity:.55;transition:.18s}}
  .lit .cbedge.on,.lit .siledge.on{{opacity:.95}}
  .cbedge.on,.siledge.on{{opacity:.95;stroke-width:2.4}}
  .cbnode.on rect,.silnode.on rect{{opacity:1}} .cbnode.on .cbl,.cbnode.on .cbw,.silnode.on .silq,.silnode.on .sill{{opacity:1}}
  .faded{{opacity:.16!important}}
  /* docent */
  .docent{{display:grid;grid-template-columns:1fr;gap:0;margin-top:16px;background:var(--card);border:1px solid var(--line2);border-radius:14px;overflow:hidden}}
  .dhead{{display:flex;align-items:center;gap:12px;padding:13px 18px;background:var(--gold-bg);border-bottom:1px solid var(--line2)}}
  .dstep{{font-family:var(--mono);font-size:11px;font-weight:700;color:var(--gold);white-space:nowrap}}
  .dmove{{font-family:var(--serif);font-weight:600;font-size:18px}}
  .dbody{{padding:16px 20px}}
  .dplain{{font-size:15.5px;line-height:1.6;color:var(--ink);margin:0 0 12px}} .dplain b{{color:var(--ink)}}
  .droads{{font-family:var(--mono);font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:var(--myst);margin:10px 0 6px}}
  .road{{display:flex;gap:9px;padding:6px 0;border-top:1px solid var(--line);font-size:14px}}
  .road .rl{{font-family:var(--serif);font-weight:600;color:var(--myst);flex:none;min-width:150px}}
  .road .rw{{color:var(--ink2);font-size:13.5px}}
  .dsil{{margin-top:12px;background:var(--terra-bg);border:1px solid var(--terra);border-radius:9px;padding:10px 14px;font-size:14px;color:var(--terra)}}
  .dsil b{{color:var(--terra);font-weight:700}}
  .dnav{{display:flex;gap:10px;align-items:center;padding:12px 18px;border-top:1px solid var(--line2)}}
  .navbtn{{font-family:var(--sans);font-size:14px;font-weight:600;padding:9px 18px;border-radius:10px;border:1.5px solid var(--line2);background:var(--paper2);color:var(--ink);cursor:pointer}}
  .navbtn.primary{{background:var(--moss);color:#fff;border-color:var(--moss)}}
  .navbtn:disabled{{opacity:.4;cursor:default}}
  .dots{{display:flex;gap:6px;margin-left:auto}} .dot{{width:9px;height:9px;border-radius:50%;background:var(--line2);cursor:pointer}} .dot.on{{background:var(--moss)}}
  .backlink{{display:inline-block;margin:22px 0 0;font-family:var(--mono);font-size:12px}}
  .foot{{margin-top:32px;padding-top:14px;border-top:1px solid var(--line);font-family:var(--mono);font-size:11.5px;color:var(--ink3);line-height:1.7}}
</style>
</head>
<body>
<div class="wrap">
<header>
  <span class="banner">candidate · interaction bakeoff · #2b · negative space as the star</span>
  <p class="eyebrow">the coding lab · reading a song for the roads not taken</p>
  <h1>“She Loves You” — what happened, and what could have been</h1>
  <div class="orient"><b>What you’re looking at.</b> The <span class="sol">solid green line</span> is the song’s actual argument, left to right — the moves it really makes. Hanging off each move are the <span class="dsh">dashed branches</span>: the moves it <i>could</i> have made but didn’t — the roads not taken. Above the line, in red, sit the song’s <b>silences</b> — the questions it raises and never answers. <b>Use the docent below</b> to walk it one beat at a time; it’ll light up each move and its could-have-beens as you go.</div>
  <div class="legend">
    <span><span class="sw"></span>what happened — the move the song makes</span>
    <span><span class="sw d"></span>what could have been — a road not taken</span>
    <span><span class="sw s"></span>a silence — raised, never answered</span>
  </div>
</header>

<div class="mapwrap">
  <svg class="diag" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="She Loves You — what happened and what could have been">
    {svg_s}
  </svg>
</div>

<div class="docent">
  <div class="dhead"><span class="dstep" id="dstep">Step 1 / {len(BEATS)}</span><span class="dmove" id="dmove"></span></div>
  <div class="dbody">
    <p class="dplain" id="dplain"></p>
    <div class="droads">the roads not taken →</div>
    <div id="droads"></div>
    <div class="dsil" id="dsil" style="display:none"></div>
  </div>
  <div class="dnav">
    <button class="navbtn" id="prev">◀ back</button>
    <button class="navbtn primary" id="next">next beat ▶</button>
    <span style="font-family:var(--mono);font-size:11.5px;color:var(--ink3)">or click any move on the map</span>
    <span class="dots" id="dots"></span>
  </div>
</div>

<a class="backlink" href="coding-lab.html">← back to the coding lab</a>
<p class="foot">HOW PRODUCED · design-SB — bakeoff entry #2b (negative-space docent-diagram) on “She Loves You,” per the researcher’s S150 feedback (make the could-have-beens the star; add a docent voice; song before theology). Structure + docent copy are design-SB’s; the <b>could-have-been branches + silences are candidate illustrations for reading-SB to bless/expand</b> (negative-space content is reading-SB’s lane). No lyric text beyond the factual title/refrain. WHAT NEEDS VERIFICATION · candidate interaction concept for review; the specific roads-not-taken await reading-SB’s negative-space set per move; Stage 6 = 0; nothing written to the DB.</p>
</div>
<script>
var STEPS=__STEPS__;
(function(){{
  var svg=document.querySelector('svg.diag'), i=0;
  var dstep=document.getElementById('dstep'),dmove=document.getElementById('dmove'),dplain=document.getElementById('dplain'),
      droads=document.getElementById('droads'),dsil=document.getElementById('dsil'),dots=document.getElementById('dots');
  STEPS.forEach(function(s,k){{ var d=document.createElement('span'); d.className='dot'; d.onclick=function(){{go(k);}}; dots.appendChild(d); }});
  function setLit(id){{
    // fade non-active moves; light this beat's could-be + silence
    document.querySelectorAll('.move').forEach(function(m){{ m.classList.toggle('active',m.getAttribute('data-beat')===id); m.classList.toggle('faded',m.getAttribute('data-beat')!==id); }});
    document.querySelectorAll('.cbedge,.cbnode,.siledge,.silnode').forEach(function(e){{
      var on=e.classList.contains('b-'+id); e.classList.toggle('on',on); e.classList.toggle('faded',!on);
    }});
  }}
  function go(k){{
    i=Math.max(0,Math.min(STEPS.length-1,k)); var s=STEPS[i];
    dstep.textContent='Step '+(i+1)+' / '+STEPS.length; dmove.innerHTML=s.move; dplain.innerHTML=s.plain;
    droads.innerHTML=s.couldbe.map(function(c){{return '<div class="road"><span class="rl">'+c[0]+'</span><span class="rw">'+c[1]+'</span></div>';}}).join('');
    if(s.silence){{ dsil.style.display='block'; dsil.innerHTML='<b>The silence here — '+s.silence[0]+'</b> '+s.silence[1]; }} else {{ dsil.style.display='none'; }}
    document.getElementById('prev').disabled=(i===0); document.getElementById('next').disabled=(i===STEPS.length-1);
    dots.querySelectorAll('.dot').forEach(function(d,j){{d.classList.toggle('on',j===i);}});
    setLit(s.id);
  }}
  document.getElementById('next').onclick=function(){{go(i+1);}};
  document.getElementById('prev').onclick=function(){{go(i-1);}};
  document.querySelectorAll('.move').forEach(function(m){{ var id=m.getAttribute('data-beat');
    m.addEventListener('click',function(){{ var k=STEPS.findIndex(function(s){{return s.id===id;}}); go(k); }});
    m.addEventListener('keydown',function(e){{if(e.key==='Enter'||e.key===' '){{e.preventDefault();m.click();}}}});
  }});
  go(0);
}})();
</script>
</body>
</html>"""
    HTML=HTML.replace("__STEPS__",STEPS)
    open(out,"w").write(HTML)
    print(f"wrote {out} — {len(BEATS)} beats, {sum(len(b['couldbe']) for b in BEATS)} could-have-beens, {sum(1 for b in BEATS if b.get('silence'))} silences")

if __name__=="__main__":
    build(sys.argv[1])
