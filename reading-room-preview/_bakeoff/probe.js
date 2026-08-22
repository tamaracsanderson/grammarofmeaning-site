/* one probe, run per variant, comparing against the no-bakeoff baseline in an iframe */
(async()=>{
  const V=document.documentElement.getAttribute('data-bakeoff')||'baseline';
  const PROPS=['fontFamily','fontSize','lineHeight','fontWeight','color','backgroundColor',
               'letterSpacing','marginTop','marginBottom','paddingTop','paddingLeft',
               'borderTopWidth','borderLeftWidth','width','height','position','display','overflow'];
  const SELS=['.vtext','.vnum','.para .pp','.para .mk','.mcard','.mcard .mc-t','.shelf-in','.shelf-q',
              '.st','.ladder-note','.d2-t','.d2-st','.d2-basis','.d2-row','.arc-h','.text','.marg-h'];
  const snap=(d,w)=>Object.fromEntries(SELS.map(s=>{const e=d.querySelector(s);if(!e)return[s,null];
    const c=w.getComputedStyle(e);const o={};PROPS.forEach(p=>o[p]=c[p]);
    o.__textShadow=c.textShadow;o.__boxShadow=c.boxShadow;return[s,o];}));
  const mine=snap(document,window);

  // baseline in an iframe, same step, no bakeoff param
  const url=location.pathname+location.search.replace(/&?bakeoff=v[234]/,'');
  const html=await (await fetch(url)).text();
  const ifr=document.createElement('iframe');
  ifr.style.cssText='position:fixed;left:-9999px;top:0;width:1440px;height:1250px';
  document.body.appendChild(ifr); ifr.contentDocument.open(); ifr.contentDocument.write(html); ifr.contentDocument.close();
  await new Promise(r=>setTimeout(r,4200));
  /* The iframe inherits the PARENT's location, so the harness inside it saw ?bakeoff=v2 and applied
     the candidate too — making "baseline" identical to "treated" and the probe incapable of showing
     a difference. It reported 0 changes while the shadow was demonstrably on the page. Strip the
     candidate inside the frame and let it settle before snapshotting. */
  const bd=ifr.contentDocument;
  bd.querySelectorAll('link[href*="_bakeoff/"]').forEach(l=>l.remove());
  bd.documentElement.removeAttribute('data-bakeoff');
  await new Promise(r=>setTimeout(r,600));
  if (bd.documentElement.getAttribute('data-bakeoff'))
    return {ERROR:'baseline frame still carries the candidate; the comparison would be vacuous'};
  const base=snap(bd, ifr.contentWindow);

  const intended=[], unintended=[]; let compared=0;
  SELS.forEach(s=>{ if(!mine[s]||!base[s]) return;
    PROPS.concat(['__textShadow','__boxShadow']).forEach(p=>{ compared++;
      if(mine[s][p]===base[s][p]) return;
      const rec={selector:s,property:p,baseline:base[s][p],treated:mine[s][p]};
      (p==='__textShadow'||p==='__boxShadow'||p==='backgroundColor'||p==='borderTopWidth'||p==='borderLeftWidth'||p==='paddingTop'||p==='paddingLeft')
        ? intended.push(rec) : unintended.push(rec);
    });});
  ifr.remove();
  return {variant:V, compared, intended_changes:intended.length, unintended_changes:unintended.length,
          unintended, intended:intended.map(r=>r.selector+'{'+r.property.replace('__','')+'}')};
})()
