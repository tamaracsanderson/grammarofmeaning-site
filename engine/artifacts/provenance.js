/* Provenance render-contract (PI-directed, S156, trust-critical).
 *
 * The rule: every displayed reading must trace to real engine data. A reading DECLARES its
 * DB source with data-prov-source="<source_key>"; this script derives the badge from
 * coded_ledger.json (the ground-truth) — so a hand-authored reading can NOT silently render
 * as coded.
 *
 *   - source_key IS in coded_ledger (and, if data-prov-need="gaps|gloss_rows|moves" is set,
 *     that count > 0)  →  a green PROVENANCE line: "source: coded_ledger · KEY · N moves"
 *   - source_key is NOT in the ledger                         →  an amber DRAFT badge.
 *   - ledger unreachable                                      →  DRAFT (fail-safe: never
 *                                                                 render as grounded unverified).
 *
 * Declare on any element:
 *   <div data-prov-source="MATT-28">…</div>                      (badge appended to the element)
 *   <div data-prov-source="MATT-28"><span data-prov-slot></span>…</div>   (badge into the slot)
 *   add data-prov-need="gaps" to require a non-zero gap count for "grounded".
 *
 * Dynamically-rendered readings: call window.Provenance.rescan() after you inject them.
 * See PROVENANCE_CONTRACT.md.
 */
(function(){
  var IDX=null;
  var CSS='.prov-badge{display:inline-flex;align-items:center;gap:5px;font-family:ui-monospace,Menlo,monospace;'
    +'font-size:10px;border-radius:6px;padding:2px 8px;letter-spacing:.02em;line-height:1.4;vertical-align:middle}'
    +'.prov-grounded{color:#2e7d47;background:rgba(46,125,71,.10);border:1px solid rgba(46,125,71,.32)}'
    +'.prov-draft{color:#8A2B0F;background:#F5E6C8;border:1px solid #C4602F;font-weight:700}'
    +'@media(prefers-color-scheme:dark){.prov-grounded{color:#7fd39b;background:rgba(127,211,155,.12);border-color:rgba(127,211,155,.34)}}';
  function injectCSS(){ if(document.getElementById('prov-css'))return; var s=document.createElement('style'); s.id='prov-css'; s.textContent=CSS; document.head.appendChild(s); }
  function esc(s){ return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;'); }
  function badge(key,need){
    var e=IDX?IDX[key]:null;
    var grounded=e && (!need || (+e[need]>0));
    if(grounded){
      var bits=['source: coded_ledger', esc(key)];
      if(e.moves) bits.push(e.moves+' moves');
      if(need && e[need]!=null) bits.push(e[need]+' '+need.replace(/_/g,' '));
      return '<span class="prov-badge prov-grounded" title="verified in coded_ledger.json">'+bits.join(' · ')+'</span>';
    }
    return '<span class="prov-badge prov-draft" title="not found in coded_ledger.json — not engine-grounded, rendered as draft">DRAFT · not engine-grounded'+(key?' · '+esc(key):'')+'</span>';
  }
  function render(el){
    if(el.getAttribute('data-prov-done')) return;
    var html=badge(el.getAttribute('data-prov-source'), el.getAttribute('data-prov-need'));
    var wrap=document.createElement('span'); wrap.innerHTML=html;
    var slot=el.querySelector('[data-prov-slot]');
    (slot||el).appendChild(wrap.firstChild);
    el.setAttribute('data-prov-done','1');
  }
  function scan(){ [].forEach.call(document.querySelectorAll('[data-prov-source]'), render); }
  function boot(d){
    IDX={}; if(d && d.ledger) d.ledger.forEach(function(e){ IDX[e.source_key]=e; });
    injectCSS(); scan();
    window.Provenance={ check:function(k){return IDX[k]||null;}, badge:badge, rescan:scan, count:function(){return Object.keys(IDX).length;} };
  }
  fetch('/engine/artifacts/coded_ledger.json')
    .then(function(r){ return r.ok?r.json():null; })
    .then(boot)
    .catch(function(){ boot(null); });  // ledger unreachable → all declared readings render DRAFT (fail-safe)
})();
