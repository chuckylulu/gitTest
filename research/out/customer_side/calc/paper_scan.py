#!/usr/bin/env python3
"""Scan saved Crossref volume listings for papers with an author affiliated to one of the
seven chipmakers, and flag inspection / metrology topics by title keywords.

Usage: python3 -I research/out/customer_side/calc/paper_scan.py
Inputs : research/sources/customer_side/*_crossref_*-volume-list.json
Outputs: research/out/customer_side/calc/paper_candidates.csv (all chipmaker-affiliated papers,
         with a topic flag) and a coverage table printed to stdout.
"""
import csv, glob, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
SRC = os.path.join(ROOT, "research", "sources", "customer_side")
OUT = os.path.join(ROOT, "research", "out", "customer_side", "calc", "paper_candidates.csv")
CO = {
    "SK hynix": re.compile(r"hynix", re.I),
    "Samsung": re.compile(r"Samsung(?!\s*Electro-?\s*Mechanics)", re.I),
    "Micron": re.compile(r"Micron\b(?!\s*(scale|size))"),
    "TSMC": re.compile(r"TSMC|Taiwan Semiconductor Manufacturing", re.I),
    "Intel": re.compile(r"\bIntel\b(?!ligen)"),
    "ASE": re.compile(r"\bASE\b|Advanced Semiconductor Engineering|\bSPIL\b|Siliconware", re.I if False else 0),
    "Amkor": re.compile(r"Amkor", re.I),
}
SEMCO = re.compile(r"Samsung\s*Electro-?\s*Mechanics", re.I)
TOPIC = re.compile(r"inspect|metrolog|measur|void|x-?ray|\bCT\b|tomograph|laminograph|acoustic|ultrason|"
                   r"infrared|\bIR\b|overlay|misalign|alignment|warpage|warp|bow|wafer shape|flatness|"
                   r"\bAFM\b|atomic force|topograph|roughness|dishing|recess|e-?beam|electron beam|\bSEM\b|"
                   r"voltage contrast|defect|non-?destructive|characteriz|failure analysis|fault isolation|"
                   r"\bKGD\b|known good|probe|probing|test|monitor|imaging|scatterometr|SAXS|XRF|XRD|"
                   r"ellipsometr|thickness|CD\b|critical dimension|optical|interferometr|machine learning|"
                   r"deep learning|\bAI\b|virtual metrology|sampling|yield|reliab", re.I)
PKG = re.compile(r"HBM|high bandwidth memory|hybrid bond|Cu-?Cu|direct bond|SoIC|Foveros|3D|stack|TSV|"
                 r"through.silicon|micro-?bump|bump|chiplet|die-to-wafer|D2W|wafer-to-wafer|W2W|"
                 r"interposer|CoWoS|packag|bond|DRAM|memory|underfill|NCF|MUF|warpage", re.I)


def affs(a):
    return "; ".join(x.get("name", "") for x in a.get("affiliation", []))


rows, cov = [], []
for f in sorted(glob.glob(os.path.join(SRC, "*_crossref_*-volume-list.json"))):
    vol = os.path.basename(f).split("_crossref_")[1].replace("-volume-list.json", "")
    items = json.load(open(f))["message"]["items"]
    if vol.startswith("SPIE"):
        want = "Metrology, Inspection, and Process Control " + ("XXXIX" if "XXXIX" in vol else "XL")
        items = [i for i in items if (i.get("container-title") or [""])[0] == want]
    with_aff = sum(1 for i in items if any(a.get("affiliation") for a in i.get("author", [])))
    hits = 0
    for i in items:
        auths = i.get("author", [])
        alltext = " | ".join(affs(a) for a in auths)
        cos = [c for c, rx in CO.items() if rx.search(alltext)]
        semco = bool(SEMCO.search(alltext))
        if not cos and not semco:
            continue
        hits += 1
        title = re.sub(r"\s+", " ", (i.get("title") or [""])[0])
        dp = (i.get("published") or i.get("issued") or {}).get("date-parts", [[None]])[0]
        rows.append(dict(volume=vol, doi=i["DOI"], title=title,
                         companies=";".join(cos) + (";SEMCO(out of scope)" if semco else ""),
                         topic_flag="Y" if TOPIC.search(title) else "N",
                         pkg_mem_flag="Y" if PKG.search(title) else "N",
                         date="-".join(str(x) for x in dp if x),
                         n_auth=len(auths),
                         first_author=(auths[0].get("given", "") + " " + auths[0].get("family", "")).strip() if auths else "",
                         affiliations=re.sub(r"\s+", " ", alltext)[:600],
                         crossref_abstract="Y" if i.get("abstract") else "N",
                         source_file=os.path.relpath(f, ROOT)))
    cov.append((vol, len(items), with_aff, hits))
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("volume, items, items_with_any_affiliation, chipmaker_papers")
for c in cov:
    print(*c, sep=", ")
print("total chipmaker papers", len(rows), "| topic&pkg flagged", sum(1 for r in rows if r["topic_flag"] == "Y" and r["pkg_mem_flag"] == "Y"))
from collections import Counter
print(Counter(c for r in rows for c in r["companies"].split(";") if c))
