#!/usr/bin/env python3
"""Count how many Section 1 documents name each method, among documents on the six named process steps
whose evidence is not press-only ([S]) or inference-only ([I]).
Usage: python3 -I research/out/customer_side/calc/method_counts.py  (prints one sentence; also used by build_dossier.py)
Method classes are matched on the table's method column (case-insensitive regexes below)."""
import csv, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
C = os.path.join(ROOT, "research", "out", "customer_side", "calc")
CLS = [
    ("electrical test", r"electrical test|daisy|resistance|leakage"),
    ("e-beam (SEM/TEM/FIB)", r"e-beam|\bSEM\b|\bTEM\b|\bFIB\b|electron|STEM"),
    ("AFM", r"\bAFM\b|atomic force"),
    ("acoustic microscopy", r"(?<!laser-)acoustic|\bC?-?SAM\b|\bSAT\b|cSAM"),
    ("optical", r"optical|interferom|moir|vision|reflectom|ellipsom"),
    ("infrared", r"infrared|\bIR\b|\bNIR\b|thermograph|OBIRCH"),
    ("X-ray CT / laminography", r"X-ray CT|laminograph|X-ray micro|\bXRM\b|X-ray"),
    ("X-ray scatterometry / XRF / XRD", r"XRF|XRD|SAXS|XRR|scatterometr|X-ray reflect"),
    ("laser-acoustic", r"laser-acoustic|picosecond|photoacoustic|laser ultras"),
]
rows = list(csv.DictReader(open(os.path.join(C, "section1_table.csv"), encoding="utf-8")))
sel = [r for r in rows if r["in_scope_step"] == "Y" and set(r["tag"].split("/")) - {"[S]", "[I]"}]
counts = []
for name, rx in CLS:
    n = sum(1 for r in sel if re.search(rx, r["method"], re.I))
    counts.append((n, name))
counts.sort(key=lambda x: -x[0])
txt = (f"Of the {len(sel)} Section 1 documents on the six named steps whose evidence is not press-only, "
       + ", ".join(f"{name} is named in {n}" for n, name in counts)
       + " (count by `calc/method_counts.py`; one document can name several methods).")
print(txt)
