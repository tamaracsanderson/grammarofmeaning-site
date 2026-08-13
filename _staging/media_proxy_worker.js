/* media_proxy_worker.js — a tiny Cloudflare Worker that lets the media picker reach the
   museum collections a static page can't call directly: it (1) injects the API key from the
   Worker's OWN env (never in the public page) and (2) adds the CORS header those APIs omit.

   Deploy (free tier):
     1. dash.cloudflare.com → Workers & Pages → Create → Worker → paste this file → Deploy.
     2. Settings → Variables → add (as *encrypted* secrets), matching the picker's source ids:
          SMITHSONIAN_API_KEY   EUROPEANA_API_KEY   HARVARD_API_KEY
        (Cooper Hewitt needs no key — it's proxied only for CORS.)
     3. Copy the Worker URL (e.g. https://media-proxy.<you>.workers.dev) and give it to me;
        I set it as PROXY in viz_media_picker.html and the four galleries light up.

   The Worker NORMALIZES each source to the picker's common item shape, so the page has ONE
   adapter for all four: {img,title,date,lo,hi,culture,url,src,short,lic}. Only public-domain /
   CC0 / no-known-copyright items are returned; each carries its own license for the card.
   Call shape:  GET /?source=<cooperhewitt|smithsonian|europeana|harvard>&q=<query> */

const CORS = {
  "access-control-allow-origin": "*",
  "access-control-allow-methods": "GET,OPTIONS",
  "access-control-allow-headers": "*",
  "content-type": "application/json; charset=utf-8",
  "cache-control": "public, max-age=600"
};
const json = (obj, status = 200) => new Response(JSON.stringify(obj), { status, headers: CORS });

export default {
  async fetch(request, env) {
    if (request.method === "OPTIONS") return new Response(null, { headers: CORS });
    const url = new URL(request.url);
    const source = (url.searchParams.get("source") || "").toLowerCase();
    const q = (url.searchParams.get("q") || "").trim();
    if (!q) return json({ items: [] });
    try {
      let items;
      if (source === "cooperhewitt") items = await cooperhewitt(q);
      else if (source === "smithsonian") items = await smithsonian(q, env.SMITHSONIAN_API_KEY);
      else if (source === "europeana")   items = await europeana(q, env.EUROPEANA_API_KEY);
      else if (source === "harvard")     items = await harvard(q, env.HARVARD_API_KEY);
      else return json({ error: "unknown source: " + source }, 400);
      return json({ items: (items || []).slice(0, 12) });
    } catch (e) {
      return json({ error: String(e && e.message || e), items: [] }, 502);  // never blank the grid — caller ignores {items:[]}
    }
  }
};

/* ── per-source normalizers (built to the live response shapes, verified 2026-08-13) ── */

// Cooper Hewitt — keyless GraphQL; proxied ONLY for CORS. `general` full-text; cc0 flag per media.
async function cooperhewitt(q) {
  const query = "{ object(general:" + JSON.stringify(q) + ", hasImages:true) { summary multimedia } }";
  const r = await fetch("https://api.cooperhewitt.org/", {
    method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ query })
  });
  const d = await r.json();
  const objs = (d.data && d.data.object) || [];
  const out = [];
  for (const o of objs) {
    const title = (o.summary && o.summary.title) || "Untitled";
    for (const m of (o.multimedia || [])) {
      const u = m.cc0 && ((m.preview && m.preview.url) || (m.large && m.large.url));
      if (u) { out.push(item(u, title, "", null, null, "", "", "Cooper Hewitt", "CH", "CC0")); break; }
    }
  }
  return out;
}

// Smithsonian Open Access — key; filter media to usage.access==="CC0"; image via ids.si.edu.
async function smithsonian(q, key) {
  const u = "https://api.si.edu/openaccess/api/v1.0/search?rows=25&api_key=" + key +
            "&q=" + encodeURIComponent(q + ' AND online_media_type:"Images"');
  const d = await (await fetch(u)).json();
  const rows = (d.response && d.response.rows) || [];
  const out = [];
  for (const o of rows) {
    const c = o.content || {}, dnr = c.descriptiveNonRepeating || {}, idx = c.indexedStructured || {};
    const media = ((dnr.online_media || {}).media) || [];
    const m = media.find(x => x.usage && x.usage.access === "CC0" && (x.thumbnail || x.content));
    if (m) out.push(item(m.thumbnail || m.content, o.title || "Untitled",
      (idx.date && idx.date[0]) || "", null, null, (idx.culture && idx.culture[0]) || "",
      dnr.record_link || (o.id ? "https://www.si.edu/object/" + o.id : ""), "Smithsonian", "SI", "CC0"));
  }
  return out;
}

// Europeana — key; reusability=open then KEEP only public-domain/CC0 (drop CC-BY-SA etc.).
async function europeana(q, key) {
  const u = "https://api.europeana.eu/record/v2/search.json?wskey=" + key +
            "&rows=25&media=true&reusability=open&query=" + encodeURIComponent(q);
  const d = await (await fetch(u)).json();
  const out = [];
  for (const o of (d.items || [])) {
    const rights = (o.rights && o.rights[0]) || "";
    if (!/publicdomain|licenses\/zero|\/zero\/|\/mark\//i.test(rights)) continue;   // PD / CC0 only
    const img = (o.edmPreview && o.edmPreview[0]) || (o.edmIsShownBy && o.edmIsShownBy[0]);
    if (!img) continue;
    out.push(item(img, (o.title && o.title[0]) || "Untitled", (o.year && o.year[0]) || "",
      null, null, (o.dataProvider && o.dataProvider[0]) || "", o.guid || "",
      "Europeana", "EU", /zero/i.test(rights) ? "CC0" : "public domain"));
  }
  return out;
}

// Harvard Art Museums — key; primaryimageurl loads cross-origin; skip anything with a copyright note.
async function harvard(q, key) {
  const u = "https://api.harvardartmuseums.org/object?apikey=" + key +
            "&hasimage=1&size=25&q=" + encodeURIComponent(q);   // default relevance beats sort=rank here
  const d = await (await fetch(u)).json();
  const out = [];
  for (const o of (d.records || [])) {
    if (!o.primaryimageurl || o.copyright) continue;         // no image, or explicitly copyrighted → skip
    out.push(item(o.primaryimageurl, o.title || "Untitled", o.dated || "",
      o.datebegin || null, o.dateend || null, o.culture || "", o.url || "",
      "Harvard Art Museums", "HV", "no known copyright"));
  }
  return out;
}

function item(img, title, date, lo, hi, culture, url, src, short, lic) {
  return { img, title, date, lo, hi, culture, url, src, short, lic };
}

// Named exports so the normalizers can be unit-tested against the live APIs off-Worker.
// Cloudflare uses only the default export above; these are inert there.
export { cooperhewitt, smithsonian, europeana, harvard };
