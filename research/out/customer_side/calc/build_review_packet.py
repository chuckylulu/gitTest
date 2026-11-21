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
    ("PAPM-222", "SK hynix authors say the optimised TSV SiO2 film process (IR inspection + FIB checks) was 'successfully applied in mass production' in the HBM WLP line (company claim)"),
    ("PAPM-201", "SK hynix: in-line optical chip-warpage measurement for HBM is a 'commercialized solution currently in use' (company claim)"),
    ("PAPM-206", "SK hynix in-line chip warpage: about 7-10 minutes for all 600 chips of a wafer"),
    ("PAPM-216", "SK hynix: IR post-bond die shift/tilt metrology validated on actual HBM wafers in a 'production-grade MI setup'"),
    ("PAPM-136", "SK hynix HBM4 (VLSI 2026): daisy chain + C-SAM show 'void-free' micro-bumps on Mechanical Test Vehicle 4"),
    ("SMP-031", "Intel (ECTC 2026, with EV Group): C2W bond-overlay metrology aims at '100% chiplet inspection' (today: reduced sampling plans)"),
    ("PAPL-046", "Intel (ECTC 2026): near-infrared post-bond chiplet-level overlay mapping on a fiducial-grid test vehicle"),
    ("PAPM-016", "Micron (ECTC 2025): wafer-to-wafer bonding for HBM density; CSAM 'clean of voids'; flow 'demonstrated'"),
    ("TALK-020", "Samsung (VLSI 2025 workshop): optical, X-ray microscopy, AFM and acoustic microscopy 'are examined' for hybrid bonding"),
    ("TALK-024", "Press only: Samsung reportedly validating Onto picosecond laser-ultrasound tools on mass-production lines"),
    ("XR-003", "Intel: on-package DRAM survived three times the DRAM maker's X-ray limit without infant mortality; long-term reliability may be reduced"),
    ("XR-015", "Press only: TSMC's SEMICON Taiwan 2026 forum keynote abstract reportedly lists 'DRAM/HBM damage concern by X-ray'"),
    ("PAPM-225", "Samsung: 191 Hitachi High-Tech IS4100 inspectors matched to +/-2% in a DRAM HVM line (memory front end)"),
    ("TALK-014", "Guest tech note by an Inha University professor on SK hynix's newsroom (Aug 2026): D2W hybrid bonding for HBM is 'progressing toward commercialization' (not SK hynix's own words)"),
]
INFER = [  # (ids, statement, inputs)
    ("SYN-001, SYN-002, SYN-008, SYN-019", "Production wording for HBM-line inspection comes only from SK hynix's own untestable claims (TSV-film IR/FIB checks; in-line chip warpage); Samsung's HBM micro-bump pre-screen is a proposal for mass production (pilot). Every other bonded-interface method is lab, test vehicle or press.",
     "PAPM-219, PAPM-221, PAPM-222 [C], PAPM-201 [C] (SK hynix JSTS), PAPM-049 (Samsung IRPS, 'We propose'); all other cells in calc/method_matrix.py"),
    ("XR-038", "In period, chipmaker X-ray-damage statements come from Intel (dose numbers, on-package DRAM), Micron (co-author, 3D NAND), Samsung (patent application) and TSMC (press only); none gives an HBM dose limit.",
     "XR-001..XR-013; searches listed in the XR module notes"),
    ("SMP-041", "HBM test intensity is rising (more insertions and items, higher test cost) but no chipmaker publishes a count or test time.",
     "SMP-009..SMP-015, SMP-038..SMP-040, PAPM-049"),
    ("SMP-042", "Memory makers present virtual metrology as extra coverage on every wafer, not as cutting physical measurements.",
     "SMP-001, SMP-002, SMP-005..SMP-008, SMP-022, SMP-025"),
    ("AW-058", "Inspection, metrology and test vendors are about one winner in ten on the award lists read in full; no category names an HBM or hybrid-bonding product.",
     "17 of 177 winner entries on 8 full lists (calc/AW_counts.py)"),
]
QUESTIONS = [
    "What does TSMC's own abstract (https://www.semicontaiwan.org/en/node/18506) say about X-ray damage, methods and design-for-metrology? Only press paraphrase was available.",
    "Is any non-electrical void or overlay inspection of HBM stacks in production at SK hynix or Samsung? Onto's reported SK hynix 2026 Best Partner Award for HBM hidden-defect prevention (Dragonfly G5) and TheElec's Samsung laser-acoustic report point that way, but neither is the chipmaker's own text.",
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
