/* room_selftest.js — the Reading Room's INTERACTION invariants.
 * ---------------------------------------------------------------------------------------------
 * Run: open reading-room-preview/room.html, paste this whole file into the console, read the table.
 * (The other half — feed shape, hardcoded counts, the derive() contract — is
 *  scripts/analysis/check_reading_room_shell.py in twelve-laws. Neither half is sufficient.)
 *
 * WHY IT EXISTS. Every check below was added only after the defect it catches had shipped or nearly
 * shipped, and each one passed the previous sweep:
 *   throws / blanks     — caught nothing, and looked like proof the page was fine
 *   position            — caught a real drift on every re-selection, and a 132px push in the narrow layout
 *   overflow            — caught a 44px spill on 17 of 440 panels, past THREE green sweeps
 *   reader language     — caught internal method terms sitting in reader panels
 * The lesson is the reason this file is committed rather than retyped: a check that asks a narrower
 * question than the one you care about passes, and the evidence of passing is what hides the gap.
 * So when you find a new defect here, ADD ITS CHECK — and then break the thing on purpose and confirm the
 * check goes red. A green that cannot go red is decoration, and check 5 below was exactly that until a
 * mutation test showed the round trip cancelled the very drift it was supposed to catch.
 * ------------------------------------------------------------------------------------------- */
(function () {
  var R = [], V = function (id) { return document.querySelector('.v[data-verse="' + id + '"]'); };
  var lensBtns = function () { return [].slice.call(document.querySelectorAll('.lens')); };
  var esc = function (k, ok, detail) { R.push({ check: k, pass: !!ok, detail: detail || '' }); };
  /* A third state, deliberately. Coverage facts are not failures, and a check that is red on every run
     teaches people to ignore red — which would undo the point of the file. */
  var note = function (k, detail) { R.push({ check: k, pass: '—', detail: detail }); };
  var ESC = function () { document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape' })); };

  if (!document.querySelector('.v')) { console.error('the text has not loaded — is the feed reachable?'); return; }
  /* A degenerate viewport makes every width-based check nonsense — a 0px-wide window reported 495 panels
     overflowing by 180px, which is a confident failure about nothing. Refuse rather than report: a check
     that cries wolf is the mirror of one that cannot go red, and both end in being ignored. */
  if (window.innerWidth < 320 || window.innerHeight < 320) {
    console.error('viewport is ' + window.innerWidth + 'x' + window.innerHeight +
      ' — too small to measure. Resize to a real window and run again; width-based checks would be noise here.');
    return { panels: 0, failed: 0, results: [], aborted: 'degenerate viewport' };
  }

  /* ── 1 · walk EVERY panel: 20 verses x every move x every lens ────────────────────────────── */
  var panels = 0, thrown = 0, blanks = 0, overflow = 0, worstOver = 0, states = {}, leaks = {};
  /* the terms that actually leaked during the build. Read from RENDERED text, because that is the only
     place the question "does the reader see this?" can be answered — a regex over source cannot. */
  var BUILDER = ['verse_id', 'move_handle', 'edge_id', 'source_move', 'seam item', 'beat-index',
                 'carried_by', 'plane A', 'plane B', 'ontology', 'krippendorff', 'silence_obligated',
                 'LINSEAM', 'XSRC', '\\bSitz\\b', 'metaxy', 'morphospace'];
  document.querySelector('.v').click();
  var lensIds = lensBtns().map(function (e) { return e.getAttribute('data-lens'); });
  [].forEach.call(document.querySelectorAll('.v'), function (vEl) {
    vEl.click();
    var chips = [].map.call(document.querySelectorAll('.chip'), function (c) { return c.getAttribute('data-move'); });
    (chips.length ? chips : [null]).forEach(function (mh) {
      if (mh) { var c = document.querySelector('.chip[data-move="' + mh + '"]'); if (c) c.click(); }
      lensIds.forEach(function (L) {
        panels++;
        try {
          lensBtns().filter(function (e) { return e.getAttribute('data-lens') === L; })[0].click();
          var b = document.querySelector('.aside-in'), t = b.innerText;
          if (t.replace(/\s+/g, ' ').trim().length < 60) blanks++;
          var o = b.scrollWidth - b.clientWidth;
          if (o > 1) { overflow++; worstOver = Math.max(worstOver, o); }
          [].forEach.call(b.querySelectorAll('.st'), function (s) {
            var k = s.className.replace('st st-', ''); states[k] = (states[k] || 0) + 1;
          });
          /* EVIDENCE is the audit receipt — it names files and ids on purpose, so it is exempt */
          if (L !== 'evidence') BUILDER.forEach(function (j) {
            if (new RegExp(j).test(t)) leaks[j.replace(/\\b/g, '')] = (leaks[j] || 0) + 1;
          });
        } catch (e) { thrown++; }
      });
    });
  });
  esc('every panel renders', thrown === 0, panels + ' panels, ' + thrown + ' threw');
  esc('no silent blank', blanks === 0, blanks + ' panels under 60 chars');
  esc('no panel overflows', overflow === 0, overflow + ' panels, worst ' + worstOver + 'px');
  esc('no builder language in a reader panel', Object.keys(leaks).length === 0, JSON.stringify(leaks));
  esc('every typed state is reachable', Object.keys(states).length >= 5, JSON.stringify(states));

  /* ── 2 · the verse you click does not move ────────────────────────────────────────────────── */
  ESC();
  V('016:012').scrollIntoView({ block: 'center' });
  var worstClick = 0;
  ['016:012', '016:003', '016:018', '016:001', '016:020', '016:008'].forEach(function (id) {
    var el = V(id), before = el.getBoundingClientRect().top;
    el.click();
    worstClick = Math.max(worstClick, Math.abs(el.getBoundingClientRect().top - before));
  });
  esc('the clicked verse holds its place', worstClick < 1, 'max drift ' + worstClick.toFixed(2) + 'px');

  /* ── 3 · switching lenses moves nothing ───────────────────────────────────────────────────── */
  var cur = V('016:008'), b3 = cur.getBoundingClientRect().top;
  lensBtns().forEach(function (b) { b.click(); });
  esc('switching lenses moves nothing',
      Math.abs(cur.getBoundingClientRect().top - b3) < 1,
      Math.abs(cur.getBoundingClientRect().top - b3).toFixed(2) + 'px');

  /* ── 4 · OPENING does not move the text ───────────────────────────────────────────────────────
   * Measured while the lens is still OPEN, deliberately. The round-trip check below cannot catch an
   * uncompensated push: opening shoves the text down and closing pulls it back by the same amount, so
   * the two cancel and the trip reads clean. That is how the 132px narrow-layout push survived — found
   * by mutation-testing these checks, not by using the page. Both checks stay; they fail differently.
   *
   * AND THE LAYOUT MATTERS, so it is reported rather than assumed. Above 1180px the rail and the panel
   * are absolutely positioned and opening one costs no layout at all — so these checks CANNOT fail here
   * even with the compensation removed. It is the narrow layout, where the rail joins the flow, that has
   * something to catch. A green at one width says nothing about the other; run this at both. */
  ESC();
  var o = V('016:014'); o.scrollIntoView({ block: 'center' });
  var oT = o.getBoundingClientRect().top;
  o.click();
  var openDrift = Math.abs(o.getBoundingClientRect().top - oT);
  lensBtns().forEach(function (b) { b.click(); });
  openDrift = Math.max(openDrift, Math.abs(o.getBoundingClientRect().top - oT));
  var narrow = window.innerWidth <= 1180;
  var layout = (narrow ? 'narrow' : 'wide') + ' layout @' + window.innerWidth + 'px';
  esc('opening a lens does not move the text (as the reader has it)', openDrift < 1,
      'drift while open ' + openDrift.toFixed(2) + 'px · ' + layout);

  /* And the same measurement with the BROWSER's own scroll anchoring switched off, because otherwise this
   * is not a check of our code at all. Measured: opening the narrow layout grows the document 139px, and
   * native anchoring alone holds the verse to 0.29px — so with anchoring on, the check passes even with
   * keepingPlace() entirely removed. Two mechanisms are protecting the reader and only one is ours.
   * Native anchoring is not guaranteed (a browser setting or an inherited overflow-anchor:none turns it
   * off), so the line below is the one that says whether WE hold position. */
  ESC();
  var root = document.documentElement, prevAnchor = root.style.overflowAnchor;
  root.style.overflowAnchor = 'none';
  var o2 = V('016:014'); o2.scrollIntoView({ block: 'center' });
  var o2T = o2.getBoundingClientRect().top;
  o2.click();
  var ownDrift = Math.abs(o2.getBoundingClientRect().top - o2T);
  lensBtns().forEach(function (b) { b.click(); });
  ownDrift = Math.max(ownDrift, Math.abs(o2.getBoundingClientRect().top - o2T));
  root.style.overflowAnchor = prevAnchor;
  esc('…and without the browser’s scroll anchoring, so it is OUR compensation being measured',
      ownDrift < 1, 'drift ' + ownDrift.toFixed(2) + 'px · ' + layout);

  /* ── 5 · and closing returns you to exactly where you were reading ────────────────────────── */
  ESC();
  var r = V('016:010'); r.scrollIntoView({ block: 'center' });
  var y0 = window.scrollY, t0 = r.getBoundingClientRect().top;
  r.click(); lensBtns().forEach(function (b) { b.click(); }); ESC();
  esc('close returns you in place',
      window.scrollY === y0 && Math.abs(r.getBoundingClientRect().top - t0) < 1,
      'scroll ' + (window.scrollY - y0) + ' · verse ' + (r.getBoundingClientRect().top - t0).toFixed(2)
      + 'px · ' + layout);

  /* ── 5b · say plainly which layouts this run actually covered ──────────────────────────────── */
  note('layout coverage',
       'this run covered the ' + (narrow ? 'NARROW' : 'WIDE') + ' layout only — resize past 1180px and run '
       + 'again. Reported rather than asserted: a green here would otherwise imply coverage it does not have.');

  /* ── 6 · the text is whole, and 16:8 keeps its silence ────────────────────────────────────── */
  esc('20 verses', document.querySelectorAll('.v').length === 20, document.querySelectorAll('.v').length + '');
  esc('16:8 keeps the silence clause',
      /said nothing to anyone; for they were afraid/.test(V('016:008').innerText), '');
  esc('translator apparatus is marked, not stripped', !!V('016:008').querySelector('.app'), '');

  /* ── 7 · the method's own word survives beside the plain gloss ────────────────────────────── */
  V('016:001').click();
  var terms = [].map.call(document.querySelectorAll('.ax .an .term'), function (e) { return e.textContent; });
  esc('the frame shows the method’s term, not only a gloss',
      terms.indexOf('epistemic-warrant') >= 0, terms.slice(0, 3).join(' · '));

  /* ── 8 · the page never presents a reliability number as a verdict ────────────────────────── */
  esc('no agreement figure on the page', !/0\.415/.test(document.body.innerText), '');


  /* ── 9 · ACCESSIBILITY — Design owns this outright, and it had only had the minimum ───────────
   * Contrast is measured against the nearest element that actually PAINTS a background, and after
   * compositing the element's own opacity. A first pass compared everything to the body ground and
   * scored the selected chip at 1.00:1 — meaningless. The real finding underneath was systematic:
   * opacity stacked on an already-muted colour. Each layer reasonable, the composition failing. */
  /* Parse rgb() / rgba() / color(srgb r g b / a). The srgb form gives 0-1 floats; reading them as
     0-255 turns a near-white masthead into near-black and invents a failure. */
  function _rgba(c){
    if(/^color\(srgb/i.test(c)){
      var n=c.match(/[\d.]+/g).map(Number);
      return [n[0]*255,n[1]*255,n[2]*255, n.length>3?n[3]:1];
    }
    var m=c.match(/[\d.]+/g).map(Number);
    return [m[0],m[1],m[2], m.length>3?m[3]:1];
  }
  function _over(fg,bg){ // composite fg (with alpha) onto an opaque bg
    var a=fg[3];
    return [fg[0]*a+bg[0]*(1-a), fg[1]*a+bg[1]*(1-a), fg[2]*a+bg[2]*(1-a), 1];
  }
  function _lum(c){var f=[c[0],c[1],c[2]].map(function(v){v/=255;
    return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4);});
    return .2126*f[0]+.7152*f[1]+.0722*f[2];}
  /* The real ground is every translucent background between the element and the page, composited
     down — not "the first background that isn't fully transparent". A 15%-alpha highlight read as
     an opaque colour is what made a correct lens label look like a 1.63:1 failure. */
  function _groundOf(el){
    var stack=[];
    for(var n=el; n && n!==document.documentElement; n=n.parentElement){
      var c=_rgba(getComputedStyle(n).backgroundColor);
      if(c[3]>0) stack.push(c);
    }
    stack.push(_rgba(getComputedStyle(document.documentElement).backgroundColor||'rgb(255,255,255)'));
    var ground=stack.pop(); if(ground[3]<1) ground=[255,255,255,1];
    while(stack.length) ground=_over(stack.pop(), ground);
    return ground;
  }
  /* opacity is inherited multiplicatively — the element's own is not the whole story */
  function _effAlpha(el){
    var a=1;
    for(var n=el; n && n!==document.documentElement; n=n.parentElement) a*=parseFloat(getComputedStyle(n).opacity);
    return a;
  }
  function _contrast(el){
    var cs=getComputedStyle(el), ground=_groundOf(el);
    var fg=_rgba(cs.color); fg[3]=(fg[3]===undefined?1:fg[3])*_effAlpha(el);
    var composited=_over(fg, ground);
    var a=_lum(composited), b=_lum(ground);
    var r=(Math.max(a,b)+.05)/(Math.min(a,b)+.05);
    var px=parseFloat(cs.fontSize), large=(px>=24)||(px>=18.66&&+cs.fontWeight>=700);
    return {r:r, need:large?3:4.5, px:px};
  }
  /* Only measure what a reader can actually SEE. A closed panel's children composite to exactly
     1.00:1 — which is the maths being right about something invisible — and `.lens .n` is
     display:none in the narrow layout. Measuring either is noise dressed as a failure. */
  function _visible(el){
    if(!el) return false;
    var r=el.getBoundingClientRect();
    if(r.width<1 || r.height<1) return false;
    if(getComputedStyle(el).visibility==='hidden') return false;
    return _effAlpha(el) > 0.05;
  }
  V('016:001').click();
  var TEXT=['.v','.v .vn','.app','.lens .q','.lens .n','.h','.p','.ax .term','.ax .gl','.a-anchor',
            '.chip','.gloss','.foot','.row .rt','.row .rm','.lane .lt','.st','.st .why','.ed'];
  var bad=[];
  var measured=0, skipped=[];
  TEXT.forEach(function(sel){
    var el=document.querySelector(sel);
    if(!_visible(el)){ skipped.push(sel); return; }
    measured++;
    var c=_contrast(el);
    if(c.r < c.need) bad.push(sel+' '+c.r.toFixed(2)+':1 (need '+c.need+')');
  });
  esc('text meets WCAG AA contrast', bad.length===0,
      bad.length ? bad.join(' · ')
                 : measured+' visible text styles pass'+(skipped.length?' ('+skipped.length+' not rendered here: '+skipped.join(', ')+')':''));

  /* A scripted .focus() does not satisfy :focus-visible in Chrome — it requires keyboard intent — so
     asserting on the matched state would fail on a correct page. Verify the RULE exists and is
     well-formed, which is the thing that can actually regress. */
  var fvRule = [].some.call(document.styleSheets, function(sh){
    try { return [].some.call(sh.cssRules, function(r){
      return /:focus-visible/.test(r.selectorText||'') && /outline/.test(r.style && r.style.cssText || ''); }); }
    catch(e){ return false; }
  });
  var srcHasRule = /:focus-visible\s*\{[^}]*outline:\s*2px solid/.test(document.documentElement.outerHTML);
  esc('a keyboard reader can see where they are (focus ring defined)', fvRule || srcHasRule,
      fvRule ? 'a :focus-visible rule with an outline is in the stylesheet'
             : (srcHasRule ? 'found in page source' : 'NO :focus-visible outline rule'));

  esc('every control is a real control (not a div)',
      document.querySelector('.lens').tagName==='BUTTON' && document.querySelector('.chip').tagName==='BUTTON',
      'lens=' + document.querySelector('.lens').tagName + ' chip=' + document.querySelector('.chip').tagName);
  esc('the page announces its language and landmarks',
      document.documentElement.lang==='en' && !!document.querySelector('main') && !!document.querySelector('[aria-live]'),
      'lang=' + (document.documentElement.lang||'unset') +
      ' landmarks=' + document.querySelectorAll('main,nav,aside,header,footer').length +
      ' aria-live=' + !!document.querySelector('[aria-live]'));

  /* ── 10 · SOURCE SENSITIVITY — change the input, the displayed proposition must change ──────── */
  var beforeTxt = (function(){V('016:001').click();
    return document.querySelector('.aside-in').innerText;})();
  var savedGloss = D.moves.items[0].gloss;
  D.moves.items[0].gloss = '__SENTINEL__';
  V('016:002').click(); V('016:001').click();
  var afterTxt = document.querySelector('.aside-in').innerText;
  D.moves.items[0].gloss = savedGloss;
  V('016:002').click(); V('016:001').click();
  esc('the page is sensitive to its source (change the feed, the panel changes)',
      /__SENTINEL__/.test(afterTxt) && !/__SENTINEL__/.test(beforeTxt),
      'a mutated feed value reached the panel — the page is not showing a baked copy');

  /* ── 11 · PROVENANCE ROUNDTRIP — a visible claim traces to a declared source ─────────────────── */
  var evTxt=(function(){lensBtns().filter(function(e){return /^EVIDENCE/.test(e.innerText);})[0].click();
    return document.querySelector('.aside-in').innerText;})();
  esc('every lens names the file its claims came from',
      lensIds.filter(function(L){return L!=='evidence';}).every(function(L){
        return new RegExp(L==='see'?'SEE':L.toUpperCase()).test(evTxt);}) && /\.json/.test(evTxt),
      'EVIDENCE lists a source file per lens');

  /* ── 12 · ABSENCE SEMANTICS — a comparative omission must not render as a textual absence ────── */
  esc('16:8 is not listed as an absence (Method S180 RULING 3)',
      !(D.absence.typed_now||[]).some(function(t){return /obligated|textual/i.test(t.kind||'');}) &&
      !!D.absence.not_an_absence,
      'textual silence is rendered as a coded move, not as a gap');

  ESC(); window.scrollTo(0, 0);
  var failed = R.filter(function (x) { return x.pass === false; });
  console.table(R);
  var checks = R.filter(function (x) { return x.pass !== '—'; }).length;
  console.log(failed.length ? '✗ ' + failed.length + ' FAILED: ' + failed.map(function (f) { return f.check; }).join(' · ')
                            : '✓ all ' + checks + ' invariants hold across ' + panels + ' panels (' + layout + ')');
  return { panels: panels, failed: failed.length, results: R };
})();
