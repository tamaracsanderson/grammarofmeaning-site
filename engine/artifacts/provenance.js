/* Provenance render-contract (PI-directed, S156, trust-critical).
 *
 * THE RULE: every displayed reading must trace to real engine data — and the badge must certify
 * THE CONTENT, not merely that a dataset exists somewhere.
 *
 * R-10 (Thesis+Program, 2026-08-19) found that it did the second while claiming the first. The
 * check resolved data-prov-source against coded_ledger.json and, on a hit, printed a green
 * "source: coded_ledger". But a key existing in a ledger says NOTHING about whether the prose on
 * the page came from that data. resurrection.html makes zero fetches, bakes every word, declares
 * BRAID-RESURRECTION, and was certified grounded. The docstring's own promise — "a hand-authored
 * reading can NOT silently render as coded" — was therefore not met for exactly the case it named.
 *
 * THE FIX: stop trusting the declaration and verify it. A page that renders from a feed HAS TO
 * HAVE FETCHED IT, and the browser already knows what was fetched — performance.getEntriesByType
 * ('resource'). So a reading now declares the feed it rendered from, and the badge is only green
 * if this document actually loaded it. A declaration nobody can check is not provenance.
 *
 *   data-prov-source="<source_key>"     the ledger key the reading is about        (required)
 *   data-prov-feed="/engine/data/x.json" the feed its content was rendered from     (for grounded)
 *   data-prov-need="gaps|gloss_rows|moves"  require that count > 0                  (optional)
 *
 * THREE HONEST STATES, replacing two:
 *   key in ledger  +  declared feed WAS fetched   → GROUNDED (green)
 *   key in ledger  +  no feed, or feed not fetched → HAND-AUTHORED (amber) — the R-10 case: the
 *                                                    dataset is real, this page did not render
 *                                                    from it, and the reader is told so
 *   key not in ledger  /  ledger unreachable      → DRAFT (amber, fail-safe)
 *
 * Dynamically-rendered readings: call window.Provenance.rescan() after injecting them.
 * See PROVENANCE_CONTRACT.md.
 */
(function(){
  var IDX=null;
  var CSS='.prov-badge{display:inline-flex;align-items:center;gap:5px;font-family:ui-monospace,Menlo,monospace;'
    +'font-size:10px;border-radius:6px;padding:2px 8px;letter-spacing:.02em;line-height:1.4;vertical-align:middle}'
    +'.prov-grounded{color:#2e7d47;background:rgba(46,125,71,.10);border:1px solid rgba(46,125,71,.32)}'
    +'.prov-draft{color:#8A2B0F;background:#F5E6C8;border:1px solid #C4602F;font-weight:700}'
    +'.prov-hand{color:#7A4A12;background:#F7EEDA;border:1px solid #B4551F;font-weight:700}'
    +'@media(prefers-color-scheme:dark){.prov-grounded{color:#7fd39b;background:rgba(127,211,155,.12);border-color:rgba(127,211,155,.34)}}';
  function injectCSS(){ if(document.getElementById('prov-css'))return; var s=document.createElement('style'); s.id='prov-css'; s.textContent=CSS; document.head.appendChild(s); }
  function esc(s){ return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;'); }
  /* Did THIS document actually load that feed? The browser knows; we do not have to take the
     page's word for it. This is the whole difference between a declaration and a check. */
  function fetched(feed){
    if(!feed) return false;
    try{
      var want=new URL(feed, location.origin).pathname;
      return performance.getEntriesByType('resource').some(function(r){
        try { return new URL(r.name).pathname === want; } catch(e){ return false; }
      });
    }catch(e){ return false; }
  }
  function badge(key,need,feed){
    var e=IDX?IDX[key]:null;
    var inLedger = !!e && (!need || (+e[need]>0));
    if(!inLedger){
      return '<span class="prov-badge prov-draft" title="not found in coded_ledger.json — not engine-grounded, rendered as draft">DRAFT · not engine-grounded'+(key?' · '+esc(key):'')+'</span>';
    }
    if(!fetched(feed)){
      /* The dataset is real. This page did not render from it. Both halves are true and the
         reader is entitled to both — saying only the first is what R-10 caught. */
      return '<span class="prov-badge prov-hand" title="'+esc(key)+' exists in coded_ledger.json, but this page did not load '
        +(feed?esc(feed):'any feed')+' — the words here are hand-authored, not rendered from that data">'
        +'HAND-AUTHORED · '+esc(key)+' is coded, this reading is not rendered from it</span>';
    }
    var bits=['rendered from '+esc(feed.split('/').pop()), 'source: coded_ledger', esc(key)];
    if(e.moves) bits.push(e.moves+' moves');
    if(need && e[need]!=null) bits.push(e[need]+' '+need.replace(/_/g,' '));
    return '<span class="prov-badge prov-grounded" title="this document loaded '+esc(feed)+' and '+esc(key)+' is verified in coded_ledger.json">'+bits.join(' · ')+'</span>';
  }
  function render(el){
    if(el.getAttribute('data-prov-done')) return;
    var html=badge(el.getAttribute('data-prov-source'), el.getAttribute('data-prov-need'), el.getAttribute('data-prov-feed'));
    var wrap=document.createElement('span'); wrap.innerHTML=html;
    var slot=el.querySelector('[data-prov-slot]');
    (slot||el).appendChild(wrap.firstChild);
    el.setAttribute('data-prov-done','1');
  }
  function scan(){ [].forEach.call(document.querySelectorAll('[data-prov-source]'), render); }
  function boot(d){
    IDX={}; if(d && d.ledger) d.ledger.forEach(function(e){ IDX[e.source_key]=e; });
    injectCSS(); scan();
    window.Provenance={ check:function(k){return IDX[k]||null;}, badge:badge, rescan:scan,
      fetched:fetched, count:function(){return Object.keys(IDX).length;} };
  }
  fetch('/engine/artifacts/coded_ledger.json')
    .then(function(r){ return r.ok?r.json():null; })
    .then(boot)
    .catch(function(){ boot(null); });  // ledger unreachable → all declared readings render DRAFT (fail-safe)
})();
