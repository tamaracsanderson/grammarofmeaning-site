/* component_diff.js — does the shell's Move Score render as the canonical reference does?
 * ---------------------------------------------------------------------------------------------
 * Run: open reading-room-preview/room.html, paste this whole file into the console, read the table.
 *
 * WHY IT EXISTS.  `viz_move_score_v2.html` owns the move component (DESIGN_LOCKS L3); `room.html`
 * owns the shell and RENDERS that component.  Three review rounds went to differences nobody could
 * see reliably by eye — a display face doing body-text work, a beige card, a gold label turned
 * terracotta, bars a few points off.  Each was found by looking harder, which is not a method.
 *
 * WHAT IT DOES.  Loads the canonical reference in an offscreen iframe, brings both to the same
 * state, and compares getComputedStyle across governed properties on governed selectors.  It
 * compares RENDERED RESULT, not source: two stylesheets can differ and render identically, and —
 * the case that actually bit — identical CSS can render differently under different tokens, because
 * these rules resolve through color-mix().
 *
 * WHAT IT CANNOT DO.  It compares the properties in GOVERNED below and nothing else, so a
 * difference in an ungoverned property is invisible to it.  The list is a judgement about what
 * carries the component's identity, and it is short on purpose: a diff that reports every property
 * reports mostly noise and gets ignored.  Extend it when something slips through — that is how it
 * is meant to grow.
 *
 * INTENTIONAL DEVIATIONS are declared below and reported separately from failures.  A deviation
 * that is not declared is a failure; a declared one still gets printed, so the list cannot quietly
 * become a place where drift is parked. */
(function () {
  var GOVERNED = ['fontFamily','fontSize','lineHeight','fontWeight','color','backgroundColor',
                  'letterSpacing','opacity','borderLeftColor','borderLeftWidth','borderRadius'];

  var SELECTORS = ['.vtext','.vnum','.verse.orig','.verse.added','.mv','.mv.child',
                   '.para .mk','.para .pp','.para .exp','.mv.open .para .exp',
                   '.anat','.axes dt','.axes dd','.roleline .rl','.conn','.conn .rl',
                   '.subgroup','.sublabel','.conttag',
                   '.arc-bars .ab','.arc-bars .ab.c2','.arc-h','.arc-how','.arc-beats','.arc-key'];

  /* Declared, with a reason and an authority. Anything not here is drift. */
  var INTENTIONAL = [
    { selector: '.vnum', property: 'color',
      reason: 'the shell marks the SELECTED verse by recolouring its number; the reference has no ' +
              'selection state because it has no ladder. Only differs while a verse is selected.',
      authority: 'shell-owned reader state (plane D) — DESIGN_LOCKS L3: the shell owns page-level state' },
    { selector: '.vnum', property: 'borderLeftColor',
      reason: 'inherits from the same selection recolour above; borderLeftColor is unset here so it ' +
              'follows currentColor',
      authority: 'same as above' }
    /* INTENTIONAL_ACCESSIBILITY_DEVIATION — WCAG AA is the floor and pixel-exactness to the
       predecessor does not override it (DESIGN_LOCKS L6). Same hue, minimum darkening to clear
       4.5:1, computed rather than eyeballed. */
    { selector: '.arc-h', property: 'color',
      reason: 'INTENTIONAL_ACCESSIBILITY_DEVIATION — --ink-3 #7C8478 (3.74:1) darkened to #6F766C (4.52:1)',
      authority: 'DESIGN_LOCKS L6 / PM §10' },
    { selector: '.arc-how', property: 'color',
      reason: 'INTENTIONAL_ACCESSIBILITY_DEVIATION — same --ink-3 darkening', authority: 'DESIGN_LOCKS L6' },
    { selector: '.arc-beats', property: 'color',
      reason: 'INTENTIONAL_ACCESSIBILITY_DEVIATION — same --ink-3 darkening', authority: 'DESIGN_LOCKS L6' },
    { selector: '.arc-key', property: 'color',
      reason: 'INTENTIONAL_ACCESSIBILITY_DEVIATION — same --ink-3 darkening', authority: 'DESIGN_LOCKS L6' },
    { selector: '.sublabel', property: 'color',
      reason: 'INTENTIONAL_ACCESSIBILITY_DEVIATION — same --ink-3 darkening', authority: 'DESIGN_LOCKS L6' },
    { selector: '.axes dt', property: 'color',
      reason: 'INTENTIONAL_ACCESSIBILITY_DEVIATION — same --ink-3 darkening', authority: 'DESIGN_LOCKS L6' },
    { selector: '.roleline .rl', property: 'color',
      reason: 'INTENTIONAL_ACCESSIBILITY_DEVIATION — same --ink-3 darkening', authority: 'DESIGN_LOCKS L6' },
    { selector: '.conn .rl', property: 'color',
      reason: 'INTENTIONAL_ACCESSIBILITY_DEVIATION — same --ink-3 darkening', authority: 'DESIGN_LOCKS L6' },
    { selector: '.para .mk', property: 'color',
      reason: 'INTENTIONAL_ACCESSIBILITY_DEVIATION — --gold #B8924A (2.80:1) darkened to #8D7037 (4.50:1)',
      authority: 'DESIGN_LOCKS L6' },
    { selector: '.vnum', property: 'color',
      reason: 'selection state (above) AND --gold AA darkening', authority: 'DESIGN_LOCKS L3 + L6' },
    { selector: '.conttag', property: 'color',
      reason: 'INTENTIONAL_ACCESSIBILITY_DEVIATION — same --gold darkening', authority: 'DESIGN_LOCKS L6' },
    { selector: '.verse.added', property: 'borderLeftColor',
      reason: 'no provenance segmentation in the feed, so no colour is asserted (D1 item 9); the ' +
              'reference infers it from a verse number',
      authority: 'WORK ORDER D1 item 9' },
    { selector: '.verse.orig', property: 'borderLeftColor',
      reason: 'same as .verse.added — the shell makes no provenance claim',
      authority: 'WORK ORDER D1 item 9' },
    { selector: '.arc-bars .ab', property: 'backgroundColor',
      reason: 'bars carry no provenance colour without a segmentation feed (D1 item 9)',
      authority: 'WORK ORDER D1 item 9' },
    { selector: '.arc-bars .ab.c2', property: 'backgroundColor',
      reason: 'same — .c2 is never applied without segments', authority: 'WORK ORDER D1 item 9' },
  ];

  function declared(sel, prop) {
    return INTENTIONAL.some(function (d) { return d.selector === sel && d.property === prop; });
  }

  function snap(doc, win) {
    var out = {};
    SELECTORS.forEach(function (sel) {
      var el = doc.querySelector(sel);
      if (!el) { out[sel] = null; return; }
      var cs = win.getComputedStyle(el), o = {};
      GOVERNED.forEach(function (p) { o[p] = cs[p]; });
      out[sel] = o;
    });
    return out;
  }

  return new Promise(function (resolve) {
    /* Same state on both sides, or the diff reports state differences as style differences — which
       is how three of these once looked like failures against a page that was behaving correctly. */
    var st = document.querySelector('.st[data-step="unpack"]'); if (st) st.click();
    setTimeout(function () {
      var pa = document.querySelector('.mv .para'); if (pa) pa.click();
      var mine = snap(document, window);

      fetch('/_staging/viz_move_score_v2.html').then(function (r) { return r.text(); }).then(function (html) {
        var ifr = document.createElement('iframe');
        ifr.style.cssText = 'position:fixed;left:-9999px;top:0;width:1440px;height:900px';
        document.body.appendChild(ifr);
        ifr.contentDocument.open(); ifr.contentDocument.write(html); ifr.contentDocument.close();

        setTimeout(function () {
          var d = ifr.contentDocument, w = ifr.contentWindow;
          var rpa = d.querySelector('.mv .para'); if (rpa) rpa.click();

          setTimeout(function () {
            var ref = snap(d, w);
            var rows = [], drift = 0, dev = 0, absent = [], compared = 0;

            SELECTORS.forEach(function (sel) {
              if (!mine[sel]) { absent.push('shell: ' + sel); return; }
              if (!ref[sel])  { absent.push('reference: ' + sel); return; }
              GOVERNED.forEach(function (p) {
                compared++;
                if (mine[sel][p] === ref[sel][p]) return;
                var ok = declared(sel, p);
                if (ok) dev++; else drift++;
                rows.push({ selector: sel, property: p, shell: mine[sel][p], reference: ref[sel][p],
                            verdict: ok ? 'INTENTIONAL' : 'DRIFT' });
              });
            });

            ifr.remove();
            var pass = drift === 0;
            console.log('%c' + (pass ? '✓ PASS' : '✗ FAIL') + '  component diff vs viz_move_score_v2.html',
                        'font-weight:bold');
            console.log('  ' + compared + ' properties compared · ' + SELECTORS.length + ' selectors · ' +
                        GOVERNED.length + ' governed properties');
            console.log('  ' + drift + ' drift · ' + dev + ' declared intentional · ' + absent.length + ' absent');
            if (rows.length) console.table(rows);
            if (absent.length) console.log('  not present on one side (not counted): ' + absent.join(' · '));
            INTENTIONAL.forEach(function (d) {
              console.log('  INTENTIONAL ' + d.selector + '{' + d.property + '} — ' + d.reason);
            });

            resolve({ pass: pass, compared: compared, drift: drift, intentional: dev,
                      absent: absent, rows: rows,
                      governed_properties: GOVERNED, selectors: SELECTORS,
                      declared_deviations: INTENTIONAL });
          }, 400);
        }, 4500);
      });
    }, 500);
  });
})();
