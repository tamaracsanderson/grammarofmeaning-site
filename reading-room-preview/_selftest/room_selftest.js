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
  var R = [], V = function (id) { return document.querySelector('.verse[data-verse="' + id + '"]'); };
  var lensBtns = function () { return [].slice.call(document.querySelectorAll('.lens')); };
  var esc = function (k, ok, detail) { R.push({ check: k, pass: !!ok, detail: detail || '' }); };
  /* A third state, deliberately. Coverage facts are not failures, and a check that is red on every run
     teaches people to ignore red — which would undo the point of the file. */
  var note = function (k, detail) { R.push({ check: k, pass: '—', detail: detail }); };
  var ESC = function () { document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape' })); };

  /* An early return sends back `undefined`, which reads the same as a pass to anything checking
     `.failed`. This suite exited here silently for a whole release after the markup was renamed
     .v -> .verse, so it verified nothing while appearing to. Refusals are now shaped so a caller
     must notice, same as the degenerate-viewport case below. */
  if (!document.querySelector('.verse')) {
    console.error('no .verse on the page — the text has not loaded, or the markup was renamed again');
    return { refused: 'no .verse found', failed: null, results: [] };
  }
  /* A degenerate viewport makes every width-based check nonsense — a 0px-wide window reported 495 panels
     overflowing by 180px, which is a confident failure about nothing. Refuse rather than report: a check
     that cries wolf is the mirror of one that cannot go red, and both end in being ignored. */
  if (window.innerWidth < 320 || window.innerHeight < 320) {
    console.error('viewport is ' + window.innerWidth + 'x' + window.innerHeight +
      ' — too small to measure. Resize to a real window and run again; width-based checks would be noise here.');
    /* `failed: 0` here would be a lie of shape: a refusal that returns the same fields as a clean
       run reads as green to anything that checks `.failed`, which is how a suite that ran NOTHING
       reports success.  So a refusal returns `failed: null` and no `panels` key at all -- the caller
       has to notice.  (Found by using it: a 0x0 headless viewport returned {panels:0, failed:0} and
       looked exactly like a pass.) */
    return { refused: 'degenerate viewport', failed: null, results: [] };
  }

  /* ── 1 · walk EVERY panel: 20 verses x every move x every lens ────────────────────────────── */
  var panels = 0, thrown = 0, blanks = 0, overflow = 0, worstOver = 0, states = {}, leaks = {};
  /* the terms that actually leaked during the build. Read from RENDERED text, because that is the only
     place the question "does the reader see this?" can be answered — a regex over source cannot. */
  var BUILDER = ['verse_id', 'move_handle', 'edge_id', 'source_move', 'seam item', 'beat-index',
                 'carried_by', 'plane A', 'plane B', 'ontology', 'krippendorff', 'silence_obligated',
                 'LINSEAM', 'XSRC', '\\bSitz\\b', 'metaxy', 'morphospace'];
  /* The ladder gates which lenses exist, so a sweep run at READ sees none and a sweep run at
     UNPACK sees five. Step to the last rung first: the suite's job is to walk every panel that can
     exist, and only RESPOND has earned them all. */
  (function () { var last = document.querySelector('.st[data-step="respond"]'); if (last) last.click(); })();
  document.querySelector('.verse').click();
  var lensIds = lensBtns().map(function (e) { return e.getAttribute('data-lens'); });
  [].forEach.call(document.querySelectorAll('.verse'), function (vEl) {
    vEl.click();
    /* the chips are gone; the moves are on the page, so walk those */
    var mvs = [].map.call(document.querySelectorAll('.mv'), function (c) { return c.getAttribute('data-mv'); });
    (mvs.length ? mvs.slice(0, 3) : [null]).forEach(function (mh) {
      if (mh) { var c = document.querySelector('.mv[data-mv="' + mh + '"] > .para'); if (c) c.click(); }
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
  esc('20 verses', document.querySelectorAll('.verse').length === 20, document.querySelectorAll('.verse').length + '');
  esc('16:8 keeps the silence clause',
      /said nothing to anyone; for they were afraid/.test(V('016:008').innerText), '');
  esc('translator apparatus is marked, not stripped', !!V('016:008').querySelector('.app'), '');

  /* ── 7 · the method's own word survives beside the plain gloss ────────────────────────────── */
  V('016:001').click();
  var terms = [].map.call(document.querySelectorAll('.ax .an .term'), function (e) { return e.textContent; });
  if (terms.length) {
    esc('the frame shows the method’s term, not only a gloss',
        terms.indexOf('epistemic-warrant') >= 0, terms.slice(0, 3).join(' · '));
  } else {
    /* The 8-axis ribbon left the page with the SEE lens — the move's anatomy is in the centre now.
       Its per-axis values are also the ones the S167 path-dependence finding measured as unstable
       (8 of 16 changed on re-code), so its absence is not a gap to close in a hurry. Recorded as
       coverage, not as a failure: a check that is red every run teaches people to ignore red. */
    note('the frame ribbon is not on this page', 'no .ax — the axis view is not rendered here');
  }

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
  /* The panel fades in over .45s with a .1s delay, so computed opacity is still 0 immediately after
     the click and every panel element gets skipped as invisible — a green that measured 6 of 19
     styles and let a deliberately-broken colour through. Kill transitions for the measurement so
     computed style is the FINAL style, then restore. */
  var _noAnim=document.createElement('style');
  _noAnim.textContent='*,*::before,*::after{transition:none!important;animation:none!important}';
  document.head.appendChild(_noAnim);
  V('016:001').click();
  void document.body.offsetWidth;   // force layout so the settled styles are readable
  var TEXT=['.verse','.vnum','.app','.lens .q','.lens .n','.h','.p','.ax .term','.ax .gl','.a-anchor',
            '.chip','.gloss','.foot','.row .rt','.row .rm','.lane .lt','.st','.st .why','.ed'];
  var bad=[];
  /* One lens does not render every style — rows live in INHERITS/CONNECT, lanes in COMPARE, the
     typed states in OPEN. Measuring only the SEE panel left 7 of 19 unmeasured, so walk the lenses
     on a verse rich enough to populate them and accumulate. Coverage is asserted below, so a lens
     that stops rendering something turns this red rather than quietly shrinking the sample. */
  var measured=0, seen={};
  [['016:009','inherits'],['016:008','connect'],['016:008','compare'],['016:008','open'],
   ['016:008','afterlives'],['016:001','see'],['016:008','evidence']].forEach(function(pair){
    V(pair[0]).click();
    var b=lensBtns().filter(function(e){return e.getAttribute('data-lens')===pair[1];})[0];
    if(b) b.click();
    void document.body.offsetWidth;
    TEXT.forEach(function(sel){
      if(seen[sel]) return;
      var el=document.querySelector(sel);
      if(!_visible(el)) return;
      seen[sel]=true; measured++;
      var c=_contrast(el);
      if(c.r < c.need) bad.push(sel+' '+c.r.toFixed(2)+':1 (need '+c.need+')');
    });
  });
  var skipped=TEXT.filter(function(sel){return !seen[sel];});
  _noAnim.remove();
  /* A green must not be able to mean "measured almost nothing", so coverage is asserted too. */
  esc('text meets WCAG AA contrast', bad.length===0 && measured >= TEXT.length - 1,
      (bad.length ? 'FAILS: '+bad.join(' · ')+' — ' : '')
      + measured+'/'+TEXT.length+' text styles measured'
      + (skipped.length ? ' · not rendered here: '+skipped.join(', ') : ''));

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

  /* .chip is gone -- the move is on the page now, so a pill that opened a panel about it was a
     second copy. The check follows the controls that actually exist rather than asserting on a
     deleted one, which is how this whole file threw and reported nothing. */
  (function () {
    var want = { '.lens': 'BUTTON', '.st': 'BUTTON' };
    var bad = Object.keys(want).filter(function (sel) {
      var e = document.querySelector(sel);
      if (!e && sel === '.lens') return false;    /* READ has earned no lens; that is the design */
      return !e || e.tagName !== want[sel]; });
    esc('every control is a real control (not a div)', bad.length === 0,
        bad.length ? 'wrong or missing: ' + bad.join(' ')
                   : Object.keys(want).map(function (s2) { var e2 = document.querySelector(s2);
                       return s2 + '=' + (e2 ? e2.tagName : 'not at this step'); }).join(' '));
  })();
  esc('the page announces its language and landmarks',
      document.documentElement.lang==='en' && !!document.querySelector('main') && !!document.querySelector('[aria-live]'),
      'lang=' + (document.documentElement.lang||'unset') +
      ' landmarks=' + document.querySelectorAll('main,nav,aside,header,footer').length +
      ' aria-live=' + !!document.querySelector('[aria-live]'));

  /* ── 10 · SOURCE SENSITIVITY — change the input, the displayed proposition must change ──────── */
  /* Open the lens this check actually reads. It looks for a gloss, which only SEE renders — and it
     silently began failing the moment the contrast walk started leaving a different lens open.
     A check that depends on state another check happens to leave behind is not a check. */
  /* There is no SEE panel any more — "what is it doing?" is answered by the move in the CENTRE and
     its gloss by the right margin. So the render-from-data property is tested where the data now
     surfaces: mutate the feed, re-render, and look for the sentinel on the page. The old version
     asked a deleted panel and got '' every time, which reads as "the sentinel never arrived" —
     i.e. it reported the page as BAKED, the exact opposite of the truth, and stayed red for a
     reason that had nothing to do with the property. */
  (function () {
    var step = document.querySelector('.st[data-step="respond"]'); if (step) step.click();
    var before = document.body.innerText;
    var saved = D.moves.items[0].gloss;
    D.moves.items[0].gloss = '__SENTINEL__';
    if (typeof paintMargins === 'function') paintMargins();
    var after = document.body.innerText;
    D.moves.items[0].gloss = saved;
    if (typeof paintMargins === 'function') paintMargins();
    esc('the page is sensitive to its source (change the feed, the page changes)',
        /__SENTINEL__/.test(after) && !/__SENTINEL__/.test(before),
        /__SENTINEL__/.test(after) ? 'a mutated feed value reached the page — not a baked copy'
                                   : 'the mutation did NOT reach the page — something is baked');
  })();

  /* ── 11 · PROVENANCE ROUNDTRIP — a visible claim traces to a declared source ─────────────────── */
  var evTxt=(function(){
    var st=document.querySelector('.st[data-step="respond"]'); if(st) st.click();
    var b=lensBtns().filter(function(e){return /^EVIDENCE/.test(e.innerText);})[0];
    if(!b) return ''; b.click();
    var box=document.querySelector('.aside-in'); return box ? box.innerText : '';})();
  esc('every lens names the file its claims came from',
      lensIds.filter(function(L){return L!=='evidence';}).every(function(L){
        return new RegExp(L==='see'?'SEE':L.toUpperCase()).test(evTxt);}) && /\.json/.test(evTxt),
      'EVIDENCE lists a source file per lens');

  /* ── 12 · ABSENCE SEMANTICS — a comparative omission must not render as a textual absence ────── */
  esc('16:8 is not listed as an absence (Method S180 RULING 3)',
      !(D.absence.typed_now||[]).some(function(t){return /obligated|textual/i.test(t.kind||'');}) &&
      !!D.absence.not_an_absence,
      'textual silence is rendered as a coded move, not as a gap');


  /* ── 13 · REDUCED MOTION — the setting must actually reach the page ──────────────────────────
   * The stylesheet has a prefers-reduced-motion block, which is the easy half. The half that
   * matters is whether every animated property is inside it: a transition declared after the
   * media block, or on a property the block does not name, keeps moving for a reader who asked
   * everything to stop. So enumerate what is actually animated and check the rule covers it. */
  var rmRule = false, rmText = '';
  [].forEach.call(document.styleSheets, function(sh){
    try { [].forEach.call(sh.cssRules, function(r){
      if(r.media && /prefers-reduced-motion/.test(r.media.mediaText)){
        rmRule = true;
        rmText += [].map.call(r.cssRules, function(x){return x.cssText;}).join(' ');
      }});} catch(e){}
  });
  var killsBoth = /transition-duration|transition\s*:/.test(rmText) && /animation-duration|animation\s*:/.test(rmText);
  esc('a reader who asked for no motion gets none', rmRule && killsBoth,
      rmRule ? (killsBoth ? 'the reduced-motion rule neutralises both transition and animation'
                          : 'a reduced-motion rule exists but does not cover both transition AND animation')
             : 'NO prefers-reduced-motion rule');

  /* ── 14 · A READABLE ALTERNATIVE — the text survives without CSS or JS ───────────────────────
   * The reading is the product. If it depends on the lens machinery to be legible, then a reader
   * on a screen reader, a text browser, or a failed stylesheet gets nothing. Check the text is in
   * the document as ordered prose with its verse numbers — not assembled by layout. */
  /* Read the TEXT elements, not the verse containers. The daf nests each verse's moves inside its
     .verse block (that is what puts them inside the verse's own left rule), so a container's
     innerText now interleaves scripture with apparatus. The property worth protecting is that the
     SCRIPTURE is continuous and in order, which is a claim about .vtext. */
  var plain = [].map.call(document.querySelectorAll('.verse'), function(el){
    var n = el.querySelector('.vnum'), t = el.querySelector('.vtext');
    return ((n ? n.innerText.replace(/^\d+:/, '') : '') + ' ' + (t ? t.innerText : '')).trim(); });
  var ordered = plain.length===20 && /^1\b/.test(plain[0]) && /^20\b/.test(plain[19]);
  var readableWithoutCSS = ordered && plain.every(function(t){ return t.length > 20; });
  esc('the text reads as ordered prose without the interface',
      readableWithoutCSS, plain.length+' verses in document order, each carrying its number and text');

  /* ── 15 · VISUAL REGRESSION — the reading interaction survives implementation change ──────────
   * Not a screenshot diff: a pixel baseline on a page that is deliberately being redesigned would
   * fail on every intended change and teach everyone to ignore it. What must not regress is the
   * STRUCTURE the reader depends on — the text centred and continuous, the rail present, the
   * panel anchored beside it, and the text wider than the panel so it stays the subject. */
  /* The shape being protected is now the DAF: the text in the centre, a margin either side, one
     menu above, and the panel — when a lens is opened — as an overlay rather than a resident of
     the right margin. The previous version asserted the old shape and read `.aside-in`
     unconditionally, so it threw the moment selecting a verse stopped auto-opening a drawer, and
     took the whole suite down with it: every check after it never ran, and the run reported
     `undefined` rather than a failure. Hence the guards. */
  V('016:005').click();
  var textEl = document.querySelector('.text').getBoundingClientRect();
  var menuEl = (document.querySelector('.ladder-r') || {}).getBoundingClientRect
             ? document.querySelector('.ladder-r').getBoundingClientRect() : null;
  var mL = document.getElementById('margL'), mR = document.getElementById('margR');
  var wide = window.innerWidth > 1180;
  var shape = wide ? {
    marginsFlankTheText: !!mL && !!mR
      && mL.getBoundingClientRect().right <= textEl.left + 2
      && mR.getBoundingClientRect().left  >= textEl.right - 2,
    textNotSqueezed: textEl.width > 400,
    oneMenuAboveTheText: !!menuEl && menuEl.bottom <= textEl.top + 2,
    noHorizontalScroll: document.documentElement.scrollWidth <= window.innerWidth + 1
  } : {
    textNotSqueezed: textEl.width > 260,
    oneMenuAboveTheText: !!menuEl && menuEl.bottom <= textEl.top + 2,
    noHorizontalScroll: document.documentElement.scrollWidth <= window.innerWidth + 1
  };
  var ok = Object.keys(shape).every(function (k) { return shape[k]; });
  esc('the reading layout still has the shape a reader depends on', ok,
      (wide ? 'wide' : 'narrow') + ' · ' + Object.keys(shape).map(function (k) { return k + '=' + shape[k]; }).join(' '));

  /* a lens, when one is opened, overlays rather than displacing the reading */
  (function () {
    var b2 = lensBtns()[0]; if (!b2) { note('a lens can be opened at this step', 'none earned here'); return; }
    var t0 = document.querySelector('.text').getBoundingClientRect();
    b2.click();
    var box = document.querySelector('.aside-in');
    var t1 = document.querySelector('.text').getBoundingClientRect();
    esc('opening a lens overlays the reading rather than displacing it',
        !!box && Math.abs(t1.left - t0.left) < 1 && Math.abs(t1.width - t0.width) < 1,
        box ? 'text held at ' + Math.round(t1.left) + 'px, width ' + Math.round(t1.width)
            : 'the panel did not open');
    ESC();
  })();

  /* ── disclosure: the anatomy must actually BECOME VISIBLE, not merely gain a class ─────────
     Added after shipping a page where "see how" expanded nothing for a whole release. The copied
     component's rule is `.anat.open`; I was toggling `.mv.open`, so the anatomy stayed
     display:none. Every check I ran passed -- because they asked whether the CONTENT was in the
     DOM and whether the CLASS was set, and both were true. Presence is not visibility, and a
     disclosure that renders into a hidden node is worse than one that is absent, because it looks
     discharged. Measured in pixels for that reason. */
  (function () {
    var mv = document.querySelector('.mv'), para = mv && mv.querySelector('.para');
    if (!para) { note('the move component is present', 'no .mv on the page'); return; }
    var an = mv.querySelector('.anat');
    var h0 = an ? an.getBoundingClientRect().height : -1;
    para.click();
    var h1 = an ? an.getBoundingClientRect().height : -1;
    esc('opening a move actually reveals its anatomy', h0 === 0 && h1 > 20,
        'height ' + h0 + 'px -> ' + h1 + 'px (a class alone is not a reveal)');
    var parts = ['.roleline', '.axes', '.conn'].filter(function (sel) {
      var e = mv.querySelector(sel); return !e || e.getBoundingClientRect().height === 0; });
    esc('every part of the opened anatomy is visible', parts.length === 0,
        parts.length ? 'zero-height: ' + parts.join(' ') : 'roleline + axes + connections all render');
    var rep = mv.querySelector('.repro');
    esc('the reproducibility caveat renders with the move', !!rep && rep.getBoundingClientRect().height > 0,
        rep ? 'visible' : 'ABSENT — a per-move reading is on screen with no caveat beside it');
    para.click();
  })();

  ESC(); window.scrollTo(0, 0);
  var failed = R.filter(function (x) { return x.pass === false; });
  console.table(R);
  var checks = R.filter(function (x) { return x.pass !== '—'; }).length;
  console.log(failed.length ? '✗ ' + failed.length + ' FAILED: ' + failed.map(function (f) { return f.check; }).join(' · ')
                            : '✓ all ' + checks + ' invariants hold across ' + panels + ' panels (' + layout + ')');
  return { panels: panels, failed: failed.length, results: R };
})();
