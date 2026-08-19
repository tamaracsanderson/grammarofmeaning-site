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

  ESC(); window.scrollTo(0, 0);
  var failed = R.filter(function (x) { return x.pass === false; });
  console.table(R);
  var checks = R.filter(function (x) { return x.pass !== '—'; }).length;
  console.log(failed.length ? '✗ ' + failed.length + ' FAILED: ' + failed.map(function (f) { return f.check; }).join(' · ')
                            : '✓ all ' + checks + ' invariants hold across ' + panels + ' panels (' + layout + ')');
  return { panels: panels, failed: failed.length, results: R };
})();
