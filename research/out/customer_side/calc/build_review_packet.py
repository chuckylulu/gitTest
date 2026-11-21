#!/usr/bin/env python3
"""Build review_packet.md (for an outside reviewer with web search and a URL reader, none of our files).
Claims are pulled from evidence.csv by id so tag / value / period / URL / page stay in sync with the evidence.
Usage: python3 -I research/out/customer_side/calc/build_review_packet.py
"""
import csv, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
OUT = os.path.join(ROOT, "research", "out", "customer_side")
ev = {r["id"]: r for r in csv.DictReader(open(os.path.join(OUT, "evidence.csv"), encoding="utf-8"))}
CLAIMS = [  # (id, one-line statement for the reviewer)
    ("PAPM-049", "Samsung PROPOSES an electrical pre-screen of HBM buffer-die pad-to-micro-bump interface resistance for use in mass production (adoption not stated)"),
    ("PAPM-222", "SK hynix authors say the optimised TEOS SiO2 TSV-liner deposition process was 'successfully applied in mass production' in the HBM WLP line; IR film inspection and FIB cross-sections only qualified the recipe and are not described as production inspection steps (company claim)"),
    ("PAPM-201", "SK hynix: in-line optical chip-warpage measurement for HBM is a 'commercialized solution currently in use' (company claim)"),
    ("ADDL-002", "Intel (SWTest 2026, with FormFactor): micro-bump probing (wafer/die sort) in high-volume production on Foveros since 2019 (company claim; micro-bump test, not hybrid bonds)"),
    ("PAPM-216", "SK hynix reports 'final validation using actual HBM device wafers in a production-grade MI setup' for IR post-bond die shift/tilt metrology"),
    ("PAPM-136", "SK hynix HBM4 (VLSI 2026): daisy chain + C-SAM show 'void-free' micro-bumps on Mechanical Test Vehicle 4"),
    ("SMP-031", "Intel (ECTC 2026, with EV Group): C2W bond-overlay metrology aims at '100% chiplet inspection' (today: reduced sampling plans)"),
    ("PAPL-046", "Intel (ECTC 2026): near-infrared post-bond chiplet-level overlay mapping on a fiducial-grid test vehicle"),
    ("PAPM-016", "Micron (ECTC 2025): wafer-to-wafer bonding for HBM density; CSAM 'clean of voids'; flow 'demonstrated'"),
    ("TALK-020", "Samsung (VLSI 2025 workshop): optical, X-ray microscopy, AFM and acoustic microscopy 'are examined' for hybrid bonding"),
    ("TALK-024", "Press only: Onto laser-ultrasound tools at Samsung are reportedly 'undergoing validation' on mass-production lines"),
    ("XR-003", "Intel: on-package DRAM survived three times the DRAM maker's X-ray limit without infant mortality; long-term reliability may be reduced"),
    ("XR-015", "Press only: TSMC's SEMICON Taiwan 2026 forum keynote abstract reportedly lists 'DRAM/HBM damage concern by X-ray'"),
    ("ADDM-007", "Samsung-led SPIE 2025 paper: post-bond void maps of 3D NAND wafer-to-wafer hybrid bonds come from SAM; a full-wafer SAM scan takes 10-20 minutes, so an interferometry alternative was developed"),
    ("TALK-014", "Guest tech note by an Inha University professor on SK hynix's newsroom (Aug 2026): D2W hybrid bonding for HBM is 'progressing toward commercialization' (not SK hynix's own words)"),
]
INFER = [  # (ids, statement, inputs)
    ("SYN-001, SYN-002, SYN-019, SYN-049", "Production wording for an inspection or test step on stacked dies exists only as company claims (Intel micro-bump sort on Foveros; SK hynix HBM chip warpage 'currently in use', location unstated). SK hynix IR die-shift metrology and Micron's HBM4 MBIST are pilot at most; Samsung's HBM electrical tests are lab (a proposal and a validation); every hybrid- or wafer-bonded-interface method is lab or pilot. Confidence Medium.",
     "ADDL-002 [C], PAPM-201 [C], PAPM-216, PAPM-049 ('We propose'), PAPM-107, PAPM-110 [C], ADDM-058 [C], SMP-016; all cells in calc/method_matrix.py"),
    ("XR-038", "In period, chipmaker X-ray-damage statements come from Intel (dose numbers, on-package DRAM), Micron (co-author, 3D NAND), Samsung (patent application) and TSMC (press only); none gives an HBM dose limit.",
     "XR-001..XR-018, XR-024; searches listed in the XR module notes. Confidence Medium"),
    ("SMP-041", "HBM test intensity is rising (more insertions and items, higher test cost) but no chipmaker publishes a count or test time.",
     "SMP-009..SMP-015, SMP-038..SMP-040, PAPM-049, ADDL-016, ADDL-025, ADDL-049. Confidence Medium: the strongest items are press or abstracts"),
    ("SMP-042", "VM and AI are presented mainly as extra coverage (every wafer) and faster analysis; no chipmaker gives a percentage cut in physical measurements. Micron's 'to improve sampling efficiency' may include fewer measurements, and in DRAM development Samsung measures 'only about 4% of the products' and fills the rest by ML imputation.",
     "SMP-001, SMP-002, SMP-005..SMP-008, SMP-025, SMP-033, PAPM-099, PAPM-100. Confidence Medium: Micron's wording is ambiguous and missing reduction figures may reflect non-disclosure"),
    ("AW-058", "Inspection, metrology and test vendors are about one winner in ten on the award lists read in full; no category names an HBM or hybrid-bonding product.",
     "17 of 177 winner entries on 8 full lists (calc/AW_counts.py). Confidence Medium: vendor class is assigned by company type"),
]
QUESTIONS = [
    "What does TSMC's own abstract (https://www.semicontaiwan.org/en/node/18506) say about X-ray damage, methods and design-for-metrology? Only press paraphrase was available.",
    "Is any non-electrical void or overlay inspection of HBM stacks in production at SK hynix or Samsung? Onto's reported SK hynix 2026 Best Partner Award for HBM hidden-defect prevention and TheElec's Samsung laser-acoustic report point that way, but neither is the chipmaker's own text.",
    "Do the full texts of the key papers (Intel ECTC 2026 100% overlay; ASE ECTC 2026 CoW voids; SK hynix VLSI 2026 HBM4; Samsung IRPS 2025) name tools, X-ray or AFM use, and production status that the abstracts omit?",
]


def row(i, text):
    r = ev[i]
    url = r["url"] or "(no public URL)"
    m = re.search(r"api\.semanticscholar\.org/graph/v1/paper/DOI:([^?]+)", url) or re.search(r"api\.crossref\.org/works/(10\.[^?\s]+)", url)
    if m:  # give the reviewer the publisher landing page, not an API call
        url = "https://doi.org/" + m.group(1)
    return f"| {i} | {r['tag']} | {text} | {r['value'] or '-'} | {r['period_calendar']} | {url} | {r['page_or_section'] or '-'} |"


L = ["# Review packet - customer_side (21 Nov 2026)", "",
     "Question: what SK hynix, Samsung, Micron, TSMC, Intel, ASE and Amkor themselves say (Jan 2025 - Nov 2026) they use to inspect and measure HBM stacks and hybrid-bonded interfaces.",
     "",
     "Caveats:",
     "- Conference items rest on **abstracts**: the publisher pages refuse scripts, so a reviewer with a subscription can go further than we did.",
     "- Tags: [F] primary document read; [C] company claim; [S] press; [I] our inference.",
     "",
     "## 15 most important claims", "",
     "| Id | Tag | Claim | Value | Period | Public URL | Page / section |", "|---|---|---|---|---|---|---|"]
L += [row(i, t) for i, t in CLAIMS]
L += ["", "## 5 inferences the conclusions lean on", ""]
for n, (i, t, inp) in enumerate(INFER, 1):
    L.append(f"{n}. [I] {t} (rows {i}). Inputs: {inp}.")
L += ["", "## 3 questions we could not settle", ""]
L += [f"{n}. {q}" for n, q in enumerate(QUESTIONS, 1)]
open(os.path.join(OUT, "review_packet.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
print("review_packet.md", sum(len(x) for x in L), "chars")
