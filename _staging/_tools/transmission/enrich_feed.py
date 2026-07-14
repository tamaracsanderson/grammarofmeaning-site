#!/usr/bin/env python3
"""Enrich the v1 seven-figure feed with reading-SB's V13-V15 framer data (HANDOFF 2026-07-14).

Transcribed faithfully from the handoff table (reading-SB owns the content). Jesus/God/Muhammad
get their full framer sets + a `mystical` flag per framer; the 4 other figures pass through from
v1 unchanged (mystical=false). reading-SB will emit a clean per-framer JSON on request — swap it in
and re-run build_transmission.py; this file is the interim transcription.

Usage: enrich_feed.py <v1_feed.json> <OUTPUT_enriched.json>
"""
import json, sys

def enrich(v1_path, out_path):
    d = json.load(open(v1_path))
    d["_meta"]["enriched"] = "V13-V15 framer data (HANDOFF_designSB_enriched_framer_data_2026-07-14); design-SB transcription of reading-SB's table; awaiting official per-framer JSON"
    d["_meta"]["views"] = {"A": "primary source — in-custody core (non-mystical)",
                            "B": "+ out-of-custody / mystical outliers (metaxy-indigo)",
                            "C": "reception era-axis — HELD (gated on reading-SB per-tradition periodizations; IRR192 5/5: NOT a single Küng line)"}
    d["_meta"]["mystical_note"] = "V15 meta-finding: every essence-break is the mystical/apophatic strand (Thomas, Isaiah, Sufi Nūr Muḥammadī, Zhuangzi, Schleiermacher). Marked metaxy-indigo."

    # framer sets transcribed from the handoff table (essence = ontological-commitment)
    ENRICH = {
        "Jesus": [
            {"label": "Matthew", "custody": "canonical", "ontological-commitment": "personal-agentive", "mystical": False},
            {"label": "Mark",    "custody": "canonical", "ontological-commitment": "personal-agentive", "mystical": False},
            {"label": "Luke",    "custody": "canonical", "ontological-commitment": "personal-agentive", "mystical": False},
            {"label": "John",    "custody": "canonical", "ontological-commitment": "personal-agentive", "mystical": False, "framer_note": "high-Christology, holds essence"},
            {"label": "Paul",    "custody": "canonical", "ontological-commitment": "personal-agentive", "mystical": False, "framer_note": "the IRR190 counter-case — holds"},
            {"label": "Thomas (out-of-custody)", "custody": "Gnostic (outside Church)", "ontological-commitment": "consciousness-first", "mystical": True, "framer_note": "mystical outlier"},
        ],
        "God": [
            {"label": "Genesis P", "custody": "canonical", "ontological-commitment": "personal-agentive", "mystical": False, "domain_axis_divine_mode": "TRANSCENDENT"},
            {"label": "Genesis J", "custody": "canonical", "ontological-commitment": "personal-agentive", "mystical": False, "domain_axis_divine_mode": "IMMANENT"},
            {"label": "Job",       "custody": "canonical", "ontological-commitment": "personal-agentive", "mystical": False},
            {"label": "Moses",     "custody": "canonical", "ontological-commitment": "personal-agentive", "mystical": False},
            {"label": "Psalms",    "custody": "canonical", "ontological-commitment": "personal-agentive", "mystical": False},
            {"label": "Isaiah",    "custody": "canonical", "ontological-commitment": "apophatic", "mystical": True, "framer_note": "mystical outlier (deus absconditus)"},
        ],
        "Muhammad": [
            {"label": "Sunni", "custody": "canonical", "ontological-commitment": "personal-agentive", "mystical": False},
            {"label": "Shia",  "custody": "canonical", "ontological-commitment": "personal-agentive", "mystical": False},
            {"label": "Sufi (Nūr Muḥammadī)", "custody": "canonical (Sufi)", "ontological-commitment": "consciousness-first", "mystical": True, "framer_note": "mystical outlier"},
        ],
    }
    # notes to refresh (the framer-unit reframe)
    NOTE = {
        "Jesus": "V13: six framers — the five canonical (Matthew/Mark/Luke/John/Paul) hold personal-agentive; Thomas, out of custody, breaks toward consciousness-first. Paul matching the gospels answered IRR190's hardest counter-case. The break is the mystical strand.",
        "God": "V15: the Tanakh framers (Genesis-P/J, Job, Moses, Psalms) hold personal-agentive; Isaiah — in custody — breaks toward apophatic (deus absconditus). The essence-shifter is the mystical strand, even within the canon.",
        "Muhammad": "V15: Sunni and Shia share personal-agentive; the Sufi Nūr Muḥammadī (in custody) breaks toward consciousness-first. Again the mystical strand is the shifter.",
    }

    for f in d["figures"]:
        fig = f["figure"]
        if fig in ENRICH:
            f["portrayals"] = ENRICH[fig]
            f["note"] = NOTE[fig]
        else:
            # pass-through v1 figures: tag every portrayal non-mystical, except the named Zhuangzi break
            for p in f["portrayals"]:
                lab = p.get("label", "").lower()
                p["mystical"] = ("zhuangzi" in lab)  # V15 names the Zhuangzi as a mystical essence-shifter
    json.dump(d, open(out_path, "w"), ensure_ascii=False, indent=2)
    n_myst = sum(1 for f in d["figures"] for p in f["portrayals"] if p.get("mystical"))
    n_fr = sum(len(f["portrayals"]) for f in d["figures"])
    print(f"wrote {out_path} — {len(d['figures'])} figures, {n_fr} framers, {n_myst} mystical outliers")

if __name__ == "__main__":
    enrich(sys.argv[1], sys.argv[2])
