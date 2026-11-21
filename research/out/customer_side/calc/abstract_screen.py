#!/usr/bin/env python3
"""Screen chipmaker-affiliated papers by abstract text for (a) in-scope objects and (b) inspection,
metrology or test methods. Writes calc/abstract_screen.csv; the shortlist is read by hand afterwards.
Usage: python3 -I research/out/customer_side/calc/abstract_screen.py
"""
import csv, glob, json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
S = os.path.join(ROOT, "research", "sources", "customer_side")
C = os.path.join(ROOT, "research", "out", "customer_side", "calc")
SCOPE = {
    "HBM": r"\bHBM\d?E?\b|high[- ]bandwidth memory",
    "hybrid bonding": r"hybrid[- ]bond|Cu[- /]*Cu|direct bond|SoIC|Foveros Direct|wafer[- ]to[- ]wafer|die[- ]to[- ]wafer|chip[- ]to[- ]wafer|\bW2W\b|\bD2W\b|\bC2W\b|bonding interface|bond interface",
    "TSV/micro-bump": r"\bTSVs?\b|through[- ]silicon|micro-?bump|\bµ-?bump|microbump|Cu pillar",
    "stack": r"stack(ed|ing)? (die|dies|DRAM|memory|chip)|\d+-?(high|Hi)\b|core die|base die",
    "wafer shape": r"warpage|wafer (shape|bow|flatness)|\bbow\b|distortion",
    "memory film/CD": r"\bDRAM\b|3D NAND|V-NAND|memory cell|capacitor|bit ?line|word ?line|buried channel|BCAT|VCT|4F2",
}
METHOD = {
    "optical": r"optical (inspection|microscop|metrolog|profil)|\bAOI\b|bright[- ]field|dark[- ]field|interferometr|white[- ]light|confocal|ellipsometr|scatterometr|\bOCD\b|moir[eé]|photolumin|reflectometr",
    "infrared": r"infrared|\bIR (imag|inspect|microscop|camera|transmission)|\bNIR\b|\bSWIR\b|thermograph|lock-in thermo",
    "acoustic": r"acoustic|\bSAM\b|\bC-?SAM\b|\bSAT\b|ultrason",
    "laser-acoustic": r"picosecond|laser[- ]acoustic|laser ultrason|photoacoustic",
    "X-ray CT/laminography": r"X-?ray|\bCT\b|computed tomograph|laminograph|tomograph",
    "XRF/XRD/SAXS": r"\bXRF\b|\bXRD\b|SAXS|x-?ray (diffraction|fluorescence|scatter|reflectiv)|\bXRR\b",
    "AFM": r"\bAFM\b|atomic force|profilom|surface roughness|topograph|dishing|recess",
    "e-beam": r"\bSEM\b|\bTEM\b|\bSTEM\b|electron microscop|e-?beam|electron beam|\bEBSD\b|\bFIB\b|voltage contrast|\bEDS\b|\bEDX\b|CD-SEM",
    "electrical test": r"electrical(ly)? (test|measure|character|probe|verif)|daisy[- ]chain|contact resistance|leakage current|\bKGD\b|known[- ]good|probe card|wafer test|burn-in|\bBIST\b|open/short|kelvin",
    "overlay/alignment metrology": r"overlay|misalign|alignment (accuracy|error|metrolog|measure)",
    "AI/VM": r"machine learning|deep learning|neural network|virtual metrology|\bAI\b|artificial intelligence|\bCNN\b",
}
INSPECT = r"inspect|metrolog|measur|characteriz|detect|non-?destructive|imaging|monitor|screen|test"
rows = []
recs = {}
for f in glob.glob(os.path.join(S, "*_semanticscholar_chipmaker-papers-2025-26-part*.json")):
    for r in json.load(open(f)):
        if r:
            recs[(r.get("externalIds") or {}).get("DOI", "").lower()] = (r, os.path.relpath(f, ROOT))
cand = list(csv.DictReader(open(os.path.join(C, "paper_candidates.csv"))))
for c in cand:
    r, src = recs.get(c["doi"].lower(), (None, ""))
    ab = (r or {}).get("abstract") or ""
    text = c["title"] + " " + ab
    sc = [k for k, rx in SCOPE.items() if re.search(rx, text, re.I)]
    me = [k for k, rx in METHOD.items() if re.search(rx, text, re.I if k not in ("acoustic",) else re.I)]
    insp = len(re.findall(INSPECT, text, re.I))
    rows.append(dict(volume=c["volume"], doi=c["doi"], companies=c["companies"], title=c["title"],
                     scope=";".join(sc), methods=";".join(me), inspect_words=insp,
                     has_abstract="Y" if ab else "N", s2_file=src,
                     shortlist="Y" if (sc and (me or insp >= 2)) else "N"))
with open(os.path.join(C, "abstract_screen.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("papers", len(rows), "with abstract", sum(r["has_abstract"] == "Y" for r in rows),
      "shortlist", sum(r["shortlist"] == "Y" for r in rows))
