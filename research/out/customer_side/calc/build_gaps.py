#!/usr/bin/env python3
"""Collect every NOT DISCLOSED / NOT RETRIEVED line from the module notes (parts/*_notes.md), the
main-session list below and the evidence/table files, one line each, de-duplicated, into gaps.md.
Usage: python3 -I research/out/customer_side/calc/build_gaps.py
"""
import csv, glob, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
OUT = os.path.join(ROOT, "research", "out", "customer_side")
MAIN = [
    "NOT RETRIEVED (tried: Crossref container-title listing on 2026-11-21, 0 records) - IITC 2026 proceedings in Crossref; programme page read instead (sources/customer_side/2026-11-21_iitc_IITC2026-program-page.html)",
    "NOT RETRIEVED (tried: Crossref container-title listing on 2026-11-21, 0 records) - IPFA 2026 proceedings",
    "NOT DISCLOSED (read: 2026-11-21_iitc_IITC2026-program-page.html, full programme) - any IITC 2026 paper by the seven on inspecting or measuring HBM or hybrid bonds",
    "NOT RETRIEVED (tried: fetch.py, Incapsula / 'Pardon Our Interruption' challenge on spiedigitallibrary.org and spie.org) - SPIE paper pages, author affiliations and full texts for all SPIE AL+P 2025/2026 papers",
    "NOT RETRIEVED (tried: api.openalex.org, HTTP 429, network's free daily budget exhausted; an API key would require the user's email) - OpenAlex records",
    "NOT RETRIEVED (tried: ieeexplore.ieee.org, HTTP 202 bot challenge) - full texts of all IEEE conference papers (ECTC, IEDM, IRPS, VLSI, IITC, ASMC, EPTC, IPFA, ITC, IMW)",
    "NOT RETRIEVED (tried: https://www.ectc.net/, HTTP 403) - ECTC 2025/2026 programmes and special-session slides",
    "NOT RETRIEVED (tried: tsmc.com, pr.tsmc.com, esg.tsmc.com, investor.tsmc.com; Cloudflare challenge) - all TSMC-hosted documents (releases, technology symposium, annual report, ESG report)",
    "NOT RETRIEVED (tried: www.semi.org, www.semicontaiwan.org, www.semiconkorea.org; Cloudflare challenge) - SEMICON forum agendas and talk abstracts",
    "NOT RETRIEVED (tried: www.intel.com and newsroom.intel.com, HTTP 403) - Intel newsroom, Foundry Direct Connect material, Foveros Direct brief",
    "NOT RETRIEVED (tried: www.aseglobal.com and ir.aseglobal.com, HTTP 403) - ASE releases and IR material",
    "NOT RETRIEVED (tried: ir.amkor.com, HTTP 403) - Amkor IR material",
    "NOT RETRIEVED (tried: investors.micron.com, HTTP 403) - Micron IR releases and prepared remarks hosted there",
    "NOT DISCLOSED (read: Crossref records of 85 of 3,378 IEEE/ASM records in the volume listings) - author affiliations (those papers are invisible to the affiliation scan)",
]


def norm(s):
    return re.sub(r"\s+", " ", s.strip().lstrip("-*0123456789. ").strip())


items = []
for f in sorted(glob.glob(os.path.join(OUT, "parts", "*_notes.md"))):
    mod = os.path.basename(f).replace("_notes.md", "")
    for line in open(f, encoding="utf-8"):
        if re.search(r"NOT (RETRIEVED|DISCLOSED) \(", line):
            items.append((mod, norm(line)))
for m in MAIN:
    items.append(("MAIN", m))
seen, out = set(), []
for mod, t in items:
    k = re.sub(r"[^a-z0-9]", "", t.lower())[:220]
    if k in seen:
        continue
    seen.add(k); out.append((mod, t))
nr = [x for x in out if "NOT RETRIEVED (" in x[1]]
nd = [x for x in out if "NOT RETRIEVED (" not in x[1]]
lines = ["# Gap log - customer_side (one line per item)", "",
         "Source of each line in brackets: the module that recorded it (PAPM, PAPL, TALK, XR, SMP, AW) or MAIN (main session). "
         "Lines are copied from the module notes; near-duplicates across modules are kept when they name different documents.", "",
         f"## NOT RETRIEVED ({len(nr)})", ""]
lines += [f"- [{m}] {t}" for m, t in nr]
lines += ["", f"## NOT DISCLOSED ({len(nd)})", ""]
lines += [f"- [{m}] {t}" for m, t in nd]
open(os.path.join(OUT, "gaps_body.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("NOT RETRIEVED", len(nr), "NOT DISCLOSED", len(nd))
