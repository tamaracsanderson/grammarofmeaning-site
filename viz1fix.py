#!/usr/bin/env python3
"""viz1fix.py — make the edge families visible and findable in VIZ-1.

Researcher: "right now, in the diagram, I only easily see 'fills' but there are other edges,
and the yellow lines are confusing. I need to be able to see 'feeds' vs 'fills' vs
'composes' — and know where they are — by not having the number clickable, I can not see
between what 7 moves I can find feeds, or the 4 fills, or the 8 composes."

Three real defects behind that:
  1. COMPOSES had NO edges drawn at all — "8 — all of them" pointed at a dotted container
     box, so the eight were literally invisible. Now drawn as eight ticks to the meta-move.
  2. The counts were inert text. Now they are buttons: click one and the diagram isolates
     that family, and a caption spells out WHICH moves it connects, in words.
  3. The two BEQUEATHS curves (yellow) sat at full strength at rest, so they read as the
     loudest thing on a diagram where they are the rarest. Calmed at rest, full when picked.
"""
import re, sys, pathlib
p = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "method-canonical.html")
h = p.read_text()
# VIZ-1 predates the closing-marker convention, so find its matching </div> by depth.
i = h.find('<div class="viz viz-1" id="viz-1">')
assert i != -1, "viz-1 not found"
_d = 0
for _m in re.finditer(r'<div\b|</div>', h[i:]):
    _d += 1 if _m.group(0).startswith('<div') else -1
    if _d == 0:
        j = i + _m.end(); break
else:
    raise AssertionError("unbalanced viz-1 block")
blk = h[i:j]; orig = blk

# ── 1 · draw the eight COMPOSES edges (move → the whole that holds it) ──
CENTRES = [90, 222, 354, 486, 618, 750, 882, 1014]
comp = "".join(
    f'<line class="e-composes" x1="{c}" y1="250" x2="{c}" y2="224" marker-end="url(#ah-comp)"/>'
    for c in CENTRES)
anchor = '<rect class="metabox" x="40" y="192" width="1050" height="158" rx="14"/>'
assert anchor in blk, "metabox not found"
blk = blk.replace(anchor, anchor + comp, 1)

# marker for composes — reuse the feeds arrowhead shape
mk = re.search(r'<marker id="ah-feeds".*?</marker>', blk, re.S)
assert mk, "feeds marker not found"
blk = blk.replace(mk.group(0), mk.group(0) + mk.group(0).replace('id="ah-feeds"', 'id="ah-comp"').replace('mk-a', 'mk-c'), 1)

# ── 2 · make the legend counts into family buttons ──
LEG = [('FEEDS', 'feeds'), ('FILLS', 'fills'), ('COMPOSES', 'composes'), ('BEQUEATHS', 'res')]
for name, fam in LEG:
    m = re.search(rf'(<b>{name}</b>(?:\s*<span[^>]*>\(was RESIDUAL\)</span>)?)(<span class="ct yes">)([^<]+)(</span>)', blk)
    if not m:
        print(f"  ! legend count for {name} not matched — skipped"); continue
    blk = blk.replace(m.group(0),
        f'{m.group(1)}<button type="button" class="ct yes v1-pick" data-fam="{fam}" '
        f'aria-pressed="false" title="Show only these edges in the diagram">{m.group(3)}</button>', 1)

# ── 3 · CSS: isolation + calmer bequeaths at rest ──
css = '''
.viz-1 .v1-pick{font:inherit;cursor:pointer;border:1px solid transparent;border-radius:20px;padding:1px 8px;background:rgba(63,125,87,.10);transition:background .12s,border-color .12s}
.viz-1 .v1-pick:hover{border-color:var(--fern)}
.viz-1 .v1-pick[aria-pressed="true"]{background:var(--moss);color:var(--paper);border-color:var(--moss)}
.viz-1 .e-composes{stroke:var(--sage);stroke-width:1.4;stroke-dasharray:1 3;opacity:.5}
.viz-1 .mk-c{fill:var(--sage)}
.viz-1 .v1-svg.iso-composes .mk-c{fill:var(--moss)}
.viz-1 .e-res{opacity:.45}
.viz-1 .v1-svg.iso .e-feeds,.viz-1 .v1-svg.iso .e-fills,.viz-1 .v1-svg.iso .e-composes,.viz-1 .v1-svg.iso .e-res{opacity:.06}
.viz-1 .v1-svg.iso-feeds .e-feeds{opacity:1;stroke-width:3.2}
.viz-1 .v1-svg.iso-fills .e-fills{opacity:1;stroke-width:2.6}
.viz-1 .v1-svg.iso-composes .e-composes{opacity:1;stroke-width:2.6;stroke-dasharray:none}
.viz-1 .v1-svg.iso-res .e-res{opacity:1;stroke-width:2.6}
.viz-1 .v1-where{font-size:12.5px;color:var(--ink-2);background:var(--paper-2);border-left:3px solid var(--rule);border-radius:0 7px 7px 0;padding:9px 12px;margin:10px 0 0;line-height:1.6;min-height:22px}
.viz-1 .v1-where b{color:var(--moss)}
.viz-1 .v1-where .wm{font-family:var(--mono);font-size:11.5px}
'''
sm = re.search(r'(\.viz-1 \.v1-scroll\{[^}]*\})', blk)
blk = blk.replace(sm.group(1), sm.group(1) + css, 1) if sm else blk.replace('</style>', css + '</style>', 1)

# ── 4 · the "where" caption + reset, right under the svg ──
sv = blk.find('</svg>') + 6
close = blk.find('</div>', sv)
where = ('\n  <div class="v1-where" id="v1-where"><b>Click a count in the legend above</b> — '
         '<span class="wm">7</span> feeds, <span class="wm">4</span> fills, <span class="wm">8</span> composes, '
         '<span class="wm">2</span> bequeaths — to isolate that family in the diagram and see exactly which moves it joins.</div>')
blk = blk[:close] + where + blk[close:]

# ── 5 · the script: isolate + name the connections ──
js = '''
<script>
(function(){
  var root=document.getElementById('viz-1'); if(!root) return;
  var svg=root.querySelector('.v1-svg'), out=root.querySelector('#v1-where');
  if(!svg||!out) return;
  var TXT={
    feeds:'<b>FEEDS · 7</b> — the forward spine, each move handing to the next: '+
      '<span class="wm">M1→M2 · M2→M3 · M3→M4 · M4→M5 · M5→M6 · M6→M7 · M7→M8</span>. '+
      'Seven edges for eight moves — that is what a chain looks like.',
    fills:'<b>FILLS · 4</b> — later moves answering an earlier gap, running <i>backward</i>, and '+
      '<b>all four land on M4</b>: <span class="wm">M1+M3→M4 (reason) · M2→M4 (degree) · '+
      'M5+M8→M4 (reciprocity) · M6→M4 (warrant)</span>. This is why M4 is the money-move.',
    composes:'<b>COMPOSES · 8</b> — <span class="wm">every move → the META-MOVE that holds it</span> '+
      '(M1…M8, all eight). Not a link between moves: a link from each move up to the whole, '+
      'which is why they run vertically into the box.',
    res:'<b>BEQUEATHS · 2</b> — the two gaps the song cannot close from inside, pointing '+
      '<i>out</i> to reception: <span class="wm">M4 → the addressee\\'s foreclosed reciprocity</span> '+
      'and <span class="wm">the meta-move → the friend\\'s motive</span>. Rare, and pointing off-diagram — '+
      'which is the point.'
  };
  var DEF=out.innerHTML;
  root.querySelectorAll('.v1-pick').forEach(function(b){
    b.addEventListener('click', function(){
      var fam=b.getAttribute('data-fam'), on=b.getAttribute('aria-pressed')==='true';
      root.querySelectorAll('.v1-pick').forEach(function(x){x.setAttribute('aria-pressed','false');});
      svg.className.baseVal=svg.className.baseVal.replace(/\\s*iso[\\w-]*/g,'');
      if(on){ out.innerHTML=DEF; return; }
      b.setAttribute('aria-pressed','true');
      svg.className.baseVal+=' iso iso-'+fam;
      out.innerHTML=TXT[fam]||DEF;
    });
  });
})();
</script>
'''
blk = blk.rstrip() + js

h = h[:i] + blk + h[j:]
p.write_text(h)
print("composes edges drawn:", blk.count('e-composes') - blk.count('.e-composes'))
print("legend buttons:", blk.count('v1-pick') - blk.count('.v1-pick'))
print("changed:", len(blk) - len(orig), "chars")
