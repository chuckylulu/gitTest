#!/usr/bin/env python3
"""Section 5 of the dossier: method x company matrix of production / pilot / lab / none, as [I] rows.

Usage: python3 -I research/out/customer_side/calc/method_matrix.py
Inputs : the assessments below (one per company x method), each citing evidence ids in
         research/out/customer_side/evidence.csv; the script checks that every cited id exists
         and reads each cited row's tag.
Outputs: calc/method_matrix.md (matrix + per-cell basis) and parts/SYN.csv ([I] rows SYN-001...).

Classification rule (applied by hand when writing the assessments, stated here so it can be audited):
  production = the company's own words say the method is used in mass production / HVM / production lines /
               "currently in use", or in-line monitoring in a fab;
  pilot      = validated on production wafers or lines, under qualification, or "demonstrated in"/"validated on"
               products, without a statement that it is deployed;
  lab        = test vehicle, feasibility, development, research, failure-analysis lab, or "examined";
  none found = no statement by the company in the documents read.
Scope: inspection or measurement of HBM stacks, hybrid- or wafer-bonded interfaces, TSVs / micro-bumps,
wafer/chip shape in stacking, and film / CD / defect metrology in memory fabs. Failure analysis of packages
that carry HBM counts as lab. A cell rests on the strongest status found in the company's own words;
press-only ([S]) or vendor-only items are named in the cell but never set the status.
"""
import csv, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
OUT = os.path.join(ROOT, "research", "out", "customer_side")
CO = ["SK hynix", "Samsung", "Micron", "TSMC", "Intel", "ASE", "Amkor"]
METHODS = ["optical", "infrared", "acoustic", "laser-acoustic", "X-ray CT / laminography",
           "X-ray scatterometry / XRF / XRD", "AFM", "e-beam", "electrical test",
           "extra: virtual metrology / ML sampling"]

# (company, method): (status, what/where in the company's words, evidence ids, confidence, reason)
A = {
 # ---------------- SK hynix
 ("SK hynix", "optical"): ("production", "HBM in-line chip-warpage optical module, \"commercialized solution currently in use\" ([C]); fab-wide optical inspection at each process step in development and mass production (newsroom)", "PAPM-201 PAPM-203 PAPM-206 TALK-006 TALK-007", "Medium", "HBM warpage production status is the company's own untestable claim; fab-wide statement is generic"),
 ("SK hynix", "infrared"): ("pilot", "post-bond die shift/tilt of micro-bump-stacked HBM measured by IR and validated \"using actual HBM device wafers in a production-grade MI setup\"; CVD-film IR inspection used to qualify a TSV-liner recipe that the authors say was applied in mass production ([C]) - the IR step itself is not described as a routine production inspection", "PAPM-213 PAPM-216 PAPM-219 PAPM-222", "Medium", "validation on production-grade setup and real HBM wafers, no deployment statement for the measurement"),
 ("SK hynix", "acoustic"): ("lab", "C-SAM on 12-layer HBM4 stacks of Mechanical Test Vehicle 4: \"void-free\"; SAM image of as-bonded SiCN wafers in a university-led study with SK hynix co-authors", "PAPM-134 PAPM-135 PAPM-136 PAPM-137 ADDM-043", "High", "test vehicle / lab"),
 ("SK hynix", "laser-acoustic"): ("none found", "", "", "Medium", "no SK hynix document read names it"),
 ("SK hynix", "X-ray CT / laminography"): ("none found", "", "", "Medium", "no SK hynix 2025-26 document read names X-ray for HBM/TSV/bonding (PAPM gap list)"),
 ("SK hynix", "X-ray scatterometry / XRF / XRD"): ("none found", "", "", "Medium", "none in abstracts or newsroom read"),
 ("SK hynix", "AFM"): ("none found", "Vendor material only: Infinitesima's homepage quotes SK hynix's head of DMI saying its Metron3D (high-speed AFM) showed sub-nm 3D metrology at HVM cost of ownership ([S], not counted)", "ADDM-063 ADDM-064", "Medium", "no SK hynix document names AFM"),
 ("SK hynix", "e-beam"): ("production", "fab-wide electron-microscope inspection at each process step in development and mass production (newsroom); for HBM, FIB cross-sections only qualified a TSV-liner recipe change (lab)", "TALK-006 TALK-007 PAPM-221 PAPM-222", "Medium", "production status rests on the generic front-end statement; the HBM use is a recipe-qualification check"),
 ("SK hynix", "electrical test"): ("lab", "HBM4 MTV4 daisy-chain resistance; HBM3E TSV keep-out-zone EM/TDDB and chip-level tests; back-side RDL daisy-chain test vehicle. Press only: an HBM4 system-level tester passed internal qualification ([S], not counted)", "PAPM-135 PAPM-136 PAPM-139 PAPM-140 PAPM-141 PAPM-142 PAPM-155 SMP-009 TALK-017", "Medium", "own words give test vehicles only; qualification report is press"),
 ("SK hynix", "extra: virtual metrology / ML sampling"): ("production", "Panoptes VM \"in its production lines since 2022\" and GRACE overlay VM in production since 2025, both by SK hynix's own claim ([C]); front-end, not HBM-specific", "TALK-004 SMP-005 SMP-007", "Medium", "company newsroom, explicit but untestable"),
 # ---------------- Samsung
 ("Samsung", "optical"): ("production", "191 Hitachi High-Tech IS4100 patterned-wafer inspectors matched in \"a Samsung Electronics high-volume manufacturing (HVM) line\" (memory front end, not HBM; an SKKU degree-programme paper whose first author is a Samsung engineer). For hybrid bonding: an interferometry surface map \"in under a minute\" developed as a SAM alternative and Nova broadband spectral interferometry for edge roll-off (Samsung-led SPIE 2025, lab); optical inspection \"examined\" (workshop)", "PAPM-223 PAPM-224 PAPM-225 ADDM-007 ADDM-008 ADDM-015 TALK-020", "Medium", "HVM line named, but not an official Samsung paper; HB optical work is development"),
 ("Samsung", "infrared"): ("lab", "IR photoemission / lock-in OBIRCH in V-NAND failure analysis, said to be \"reaching their limits\"", "PAPM-081 PAPM-086", "Medium", "FA lab use only; nothing on bonded interfaces"),
 ("Samsung", "acoustic"): ("lab", "SAM void maps of 3D NAND wafer-to-wafer hybrid Cu bonds, used to compare interfaces before and after CMP optimisation (Samsung-led SPIE 2025 paper, full text); stated limits: a full-wafer scan takes 10-20 min and penetration depth is limited, so the authors developed an interferometry alternative; acoustic microscopy \"examined\" for HB (workshop). Press only: talks with ultrasound vendors", "ADDM-007 ADDM-009 ADDM-010 TALK-020 TALK-027", "Medium", "process-development use; no production statement"),
 ("Samsung", "laser-acoustic"): ("none found", "Press only: Onto picosecond laser-ultrasound tools reportedly \"undergoing validation on mass production lines\" ([S], not counted)", "TALK-024 TALK-025", "Medium", "no Samsung document names it; the pilot claim is TheElec citing industry sources"),
 ("Samsung", "X-ray CT / laminography"): ("lab", "X-ray microscopy \"examined\" for hybrid bonding (VLSI 2025 workshop); patent application on in-line X-ray laminography/CT for HBM micro-bumps (a patent, not a use statement). Press only: talks with X-ray vendors", "TALK-020 XR-011 XR-012 TALK-027", "Medium", "no use statement beyond 'examined'"),
 ("Samsung", "X-ray scatterometry / XRF / XRD"): ("pilot", "X-ray diffraction CD (XCD / CD-SAXS) for deep VNAND structures, \"XCD Demonstrates Production-Level Measurement Capability\" ([C]); measurement time cut from 30 to about 5.7 min (Samsung-led 2026 deck with Onto and Rigaku co-authors). Pre-bond SiCN characterised by XPS, ToF-SIMS and MEIS (other methods)", "ADDM-017 ADDM-019 ADDM-020 ADDM-021 PAPM-058", "Low", "capability claim, no deployment statement; memory front end (VNAND), not HBM"),
 ("Samsung", "AFM"): ("pilot", "high-throughput in-line AFM \"performed on production wafers in the fab\" for hybrid bonding in VNAND (six wafers: three top, three bottom; Nearfield-led, 13 of 23 authors, 10 Samsung). The Samsung-led SPIE 2025 paper says AFM gives sub-nm Cu-recess resolution but its \"low throughput remains a challenge\" for HVM and high-speed AFM is at an early stage", "SMP-016 ADDM-011 ADDM-012 ADDM-013 TALK-020", "Medium", "production wafers, but a six-wafer study led by the tool vendor; VNAND, not HBM"),
 ("Samsung", "e-beam"): ("lab", "PFIB-SEM deprocessing applied to an HBM2 sample in a Thermo Fisher-led paper (5 of 6 authors Thermo Fisher, 1 Samsung); TEM of pre-bond SiCN; AI super-resolution SEM imaging (no status). SEM review/CD measurement in the fab named as a contamination source (implies routine use, not stated as such)", "PAPM-094 PAPM-095 PAPM-096 PAPM-058 SMP-017 PAPM-112 PAPM-113", "Low", "routine fab SEM use is implied, not stated"),
 ("Samsung", "electrical test"): ("lab", "pre-screen proposed \"for pre-screening of these interface failures in mass production\" (adoption not stated); EDS repair/ECC method \"Validated on HBM\" (setting not stated); tREFi measured in a chip-on-wafer test of 12-high HBM stacks, in a paper whose [C] that the cell transistor \"is demonstrated in High Band Width Memory (HBM) products\" concerns the transistor, not the test; leakage-current metrology for hybrid Cu bonding (SNU-led, 3 of 7 authors Samsung). None states validation on production wafers or lines", "PAPM-049 PAPM-107 PAPM-109 PAPM-110 PAPM-051 PAPM-052 PAPM-054", "Low", "a proposal and validations without a production setting"),
 ("Samsung", "extra: virtual metrology / ML sampling"): ("lab", "ML imputation where \"measurements are conducted on only about 4% of the products\" in DRAM development; SPIE VNAND mass-metrology VM paper attributed to Samsung by inference only", "PAPM-098 PAPM-099 PAPM-100 PAPM-193", "Medium", "development phase; SPIE attribution is [I]"),
 # ---------------- Micron
 ("Micron", "optical"): ("production", "AI-enhanced imaging and defect classification across \"front end, assembly and test\", by Micron's own claim ([C]); not HBM-specific", "TALK-038 TALK-039 SMP-022", "Medium", "company blog, generic and untestable"),
 ("Micron", "infrared"): ("none found", "", "", "Medium", "no Micron document read names it"),
 ("Micron", "acoustic"): ("lab", "CSAM \"clean of voids\" on wafer-to-wafer bonding aimed at HBM density; integration \"is demonstrated\"", "PAPM-015 PAPM-016 PAPM-017 PAPM-018", "High", "abstract: demonstration"),
 ("Micron", "laser-acoustic"): ("none found", "", "", "Medium", "no Micron document read names it"),
 ("Micron", "X-ray CT / laminography"): ("none found", "A co-authored lab X-ray irradiation study of 3D NAND exists but is not inspection use", "XR-007 XR-008", "Medium", "irradiation study, not inspection use"),
 ("Micron", "X-ray scatterometry / XRF / XRD"): ("lab", "X-ray reflectometry of 3D NAND ONON stacks validated against TEM \"as a process line monitoring tool\"; the paper supports \"future implementation\" (all six authors Micron)", "ADDM-026 ADDM-028 ADDM-029", "High", "validation study; future implementation"),
 ("Micron", "AFM"): ("none found", "", "", "Medium", "no Micron document read names it"),
 ("Micron", "e-beam"): ("production", "CD-SEM images \"are captured at metrology step to monitor structural measurements and detect anomaly\" (ML for them called \"crucial\" during in-line monitoring, deployment not stated); new in-line CD-SEM secondary-electron metric for DRAM container slant; e-beam inspection with fractal points \"in DRAM manufacturing\" (nuisance -98.1%, defects of interest +255.7%; ASML co-authors); off-line SEM overlay where capacitor tilt limits in-line metrology", "PAPM-007 PAPM-008 PAPM-002 ADDM-033 ADDM-034 PAPM-010", "Medium", "memory front end; HBM not named"),
 ("Micron", "electrical test"): ("pilot", "HBM4 12-high samples shipped to key customers with a \"highly capable memory built-in self-test (MBIST) feature\" ([C]); daisy chains in HBM development find voids before visual inspection (CTO at ITF World, quoted by press [S]; talk date not stated); added electrical coverage \"to prevent test escapes during production\" in graphics DRAM (proposed)", "ADDM-058 TALK-035 TALK-036 PAPM-026 PAPM-027", "Low", "MBIST is a product feature in customer samples (pre-ramp), by Micron's own claim"),
 ("Micron", "extra: virtual metrology / ML sampling"): ("pilot", "cloud VM validated on one year of production data in an HVM memory fab, \"meeting production release criteria\" (dry etch)", "SMP-025", "Medium", "release criteria met; deployment scale not stated"),
 # ---------------- TSMC
 ("TSMC", "optical"): ("lab", "Advanced Optical Metrology (AOM) of transparent carrier wafers (transmittance, roughness, bulk voids or cracks), \"successfully validated on 12-inch transparent carrier wafer\", under one minute (IMPACT 2025; last author Zhi-Hua Zou)", "ADDL-031 ADDL-033 ADDL-035", "Medium", "validation, no production statement"),
 ("TSMC", "infrared"): ("lab", "\"IR imaging\" of bonding quality in a university-led wafer-level transfer paper with two TSMC co-authors", "PAPL-001 PAPL-002", "Medium", "university-led research"),
 ("TSMC", "acoustic"): ("none found", "", "", "Medium", "no TSMC document read names it"),
 ("TSMC", "laser-acoustic"): ("none found", "", "", "Medium", "no TSMC document read names it"),
 ("TSMC", "X-ray CT / laminography"): ("none found", "Press only: SEMICON Taiwan 2026 forum keynote reportedly lists \"DRAM/HBM damage concern by X-ray\" and calls for X-ray-compatible HBM ([S]; abstract NOT RETRIEVED (tried: https://www.semicontaiwan.org/en/node/18506 with fetch.py, HTTP 403))", "XR-013 XR-015", "Medium", "no TSMC-authored text read"),
 ("TSMC", "X-ray scatterometry / XRF / XRD"): ("none found", "", "", "Medium", "no TSMC document read names it"),
 ("TSMC", "AFM"): ("none found", "", "", "Medium", "no TSMC document read names it"),
 ("TSMC", "e-beam"): ("none found", "", "", "Medium", "no in-scope TSMC document names it (die-level e-beam probing is adjacent)"),
 ("TSMC", "electrical test"): ("lab", "SoIC-CS daisy chains (\"proven feasible for the first time\" is a [C]); CoWoS-R via-chain/leakage tests (platform \"currently in production\" is a [C] about the platform, not the test); UCIe multi-die test on test vehicles; SWTest 2026 deck describes a distributed test flow with CP for known-good die, CPS for known-good SoIC stacks and RDL-CP on CoWoS interposers, status not stated", "PAPL-010 PAPL-011 PAPL-012 PAPL-006 PAPL-008 PAPL-022 ADDL-025 ADDL-026", "Medium", "test methods shown on test vehicles; the test-flow deck gives no status"),
 ("TSMC", "extra: virtual metrology / ML sampling"): ("lab", "ML 'Die of Interest' ranking of inline data; adaptive/targeted testing \"is envisioned\"", "SMP-035", "High", "explicitly envisioned"),
 # ---------------- Intel
 ("Intel", "optical"): ("lab", "image capture \"on the move\" for 100% chip-to-wafer bond-overlay metrology (wavelength not stated; development with roadmap; EV Group co-author)", "PAPL-055 PAPL-056 PAPL-059 PAPL-061", "Medium", "development paper; imaging band not stated so the cell is provisional"),
 ("Intel", "infrared"): ("lab", "NIR post-bond chiplet overlay mapping on a fiducial-grid test vehicle; patent application on IR bond-overlay metrology with fiducials (metal under a fiducial \"can block\" IR); SIL thermal imaging of warped 3D (Foveros) package samples in FA, and RF lock-in thermography whose use on 2.5/3D packages is only discussed (HBM named as context)", "PAPL-046 ADDL-055 ADDL-057 PAPL-078 PAPL-079 PAPL-089 PAPL-090", "High", "test vehicle / patent / FA"),
 ("Intel", "acoustic"): ("lab", "cSAM: \"no significant void formation\" in C2W hybrid bonding (with Applied Materials)", "PAPL-035", "High", "development paper"),
 ("Intel", "laser-acoustic"): ("none found", "", "", "Medium", "no Intel document read names it"),
 ("Intel", "X-ray CT / laminography"): ("lab", "3D X-ray CT of micro-bump joints (CPO TCB research); synchrotron XADA on a mock stacked die; X-ray dose study on on-package DRAM for board inspection", "PAPL-067 PAPL-082 XR-001 XR-002", "High", "research / FA / dose study"),
 ("Intel", "X-ray scatterometry / XRF / XRD"): ("none found", "", "", "Medium", "no Intel document read names it"),
 ("Intel", "AFM"): ("lab", "AFM and nanoindentation of hybrid-bonding Cu pads (NIST-led, Intel co-author)", "PAPL-073", "High", "research"),
 ("Intel", "e-beam"): ("lab", "FIB-SEM on Kelvin structures found interconnect gaps; low-kV SEM-EDX of Cu surface oxygen", "PAPL-036 PAPL-069", "High", "development / research"),
 ("Intel", "electrical test"): ("production", "micro-bump probing (wafer and die sort) \"in high volume production\" on Foveros since 2019: 25+ products, 300K+ wafers ([C], SWTest 2026, with FormFactor); EMIB micro-bump probing planned for 2026; 45 um native-pitch probing \"on track\" for HVM sort (with Technoprobe). Bonded-stack tests are lab: 10k-via daisy chains >90% yield, bond-via resistance, fluidic self-alignment readouts, EMIB-T HBM4E measurements, 9-wafer TSV DRAM cube", "ADDL-002 ADDL-004 ADDL-005 ADDL-016 ADDL-017 ADDL-018 ADDL-022 PAPL-033 PAPL-026 PAPL-029 PAPL-064 PAPL-094 PAPL-095", "Medium", "production status is Intel's own claim, for micro-bump sort (TSV / micro-bump step), not for hybrid bonds"),
 ("Intel", "extra: virtual metrology / ML sampling"): ("none found", "An Intel JMM 2025 abstract proposes scanner-topography virtual defect metrology giving gross-defect monitoring of every wafer and die at each litho step; it states no deployment and no product segment, and does not concern HBM or bonding, so it is not counted", "SMP-033", "Medium", "out of scope and no deployment statement"),
 # ---------------- ASE
 ("ASE", "optical"): ("none found", "Adjacent only (not HBM or hybrid bonding): a proprietary wire-bonding AI-AOI/AVI inspection system ([C], sustainability report) and AI substrate-defect detection (IMPACT 2025, deployment not stated); press: image anomaly-detection AI as an AGM focus ([S])", "ADDL-044 ADDL-045 TALK-048", "Medium", "in-scope use not stated"),
 ("ASE", "infrared"): ("none found", "", "", "Medium", "no ASE document read names it"),
 ("ASE", "acoustic"): ("none found", "Adjacent only: AI-enhanced SAM in flip-chip FA, not HBM or hybrid bonding (PVA TePla co-author)", "SMP-037", "Medium", "adjacent scope only"),
 ("ASE", "laser-acoustic"): ("none found", "", "", "Medium", "no ASE document read names it"),
 ("ASE", "X-ray CT / laminography"): ("lab", "3D X-ray microscopy in FA of FOCoS-B micro-bumps and FOCoS ASIC-HBM RDL; stated limit: field of view", "PAPL-107 PAPL-100 PAPL-101", "High", "failure-analysis flow"),
 ("ASE", "X-ray scatterometry / XRF / XRD"): ("none found", "", "", "Medium", "no ASE document read names it"),
 ("ASE", "AFM"): ("lab", "AFM of pre-bond Ag roughness and Cu protrusion / PI recess on hybrid-bonding test vehicles (NTU-led, ASE co-authors)", "PAPL-113 PAPL-119", "High", "test vehicles"),
 ("ASE", "e-beam"): ("lab", "SEM/EDS in micro-bump FA; SEM/TEM of a bonded interface on a 30 um-pitch test vehicle (NTU-led, 4 of 10 authors ASE)", "PAPL-108 PAPL-112 PAPL-115", "High", "FA / test vehicles"),
 ("ASE", "electrical test"): ("lab", "open/short and I-V curve tracing in FA of HBM-bearing fan-out packages; hybrid-bond electrical yield on a test vehicle (NTU-led, 4 of 10 authors ASE)", "PAPL-106 PAPL-112 PAPL-116", "High", "FA / test vehicles"),
 ("ASE", "extra: virtual metrology / ML sampling"): ("none found", "", "", "Medium", "none found"),
 # ---------------- Amkor
 ("Amkor", "optical"): ("none found", "Adjacent only: AI-vision automated defect classification on AOI cut AOI operators by 30% ([C], smart-manufacturing page, not HBM-specific); shadow moire warpage on a lidded FCBGA", "ADDL-051 PAPL-181", "Medium", "in-scope use not stated"),
 ("Amkor", "infrared"): ("none found", "", "", "Medium", "none found"),
 ("Amkor", "acoustic"): ("lab", "SAT at thermal-cycling read-points on a 2.5D CoW test vehicle with mimic HBMs; cracks confirmed by cross-section", "TALK-051 TALK-052", "High", "test vehicle"),
 ("Amkor", "laser-acoustic"): ("none found", "", "", "Medium", "none found"),
 ("Amkor", "X-ray CT / laminography"): ("none found", "", "", "Medium", "none found"),
 ("Amkor", "X-ray scatterometry / XRF / XRD"): ("none found", "", "", "Medium", "none found"),
 ("Amkor", "AFM"): ("none found", "", "", "Medium", "none found"),
 ("Amkor", "e-beam"): ("none found", "", "", "Medium", "none found"),
 ("Amkor", "electrical test"): ("production", "test-services page offers distributed test incl. \"in-situ test between key assembly steps and final test (SLT and ATE) for 2.5D & 3D\" ([C] service offer; HBM named only as market context; text undated); its ITC 2026 talk description names \"increasing production test times\"", "SMP-038 ADDL-049 TALK-049 TALK-050", "Low", "service offer, untestable; date of the offer text not stated"),
 ("Amkor", "extra: virtual metrology / ML sampling"): ("none found", "", "", "Medium", "none found"),
}


# What the production / pilot status rests on (shown in the matrix cell):
# HBM = HBM stack, TSV or micro-bump line; HB = hybrid / wafer bonding (not HBM); FE = memory front end; fab-wide = front end, assembly and test;
# 3D micro-bump = micro-bump sort of 3D-stacked logic; offer = service offering. [C] = the status is the company's own untestable claim.
SCOPE = {
    ("SK hynix", "optical"): "HBM [C]; FE [C]", ("SK hynix", "infrared"): "HBM", ("SK hynix", "e-beam"): "FE [C]",
    ("SK hynix", "extra: virtual metrology / ML sampling"): "FE [C]",
    ("Samsung", "optical"): "FE [C]", ("Samsung", "AFM"): "HB (VNAND)", ("Samsung", "X-ray scatterometry / XRF / XRD"): "FE [C]", ("Micron", "electrical test"): "HBM [C]", ("Intel", "electrical test"): "3D micro-bump [C]",
    ("Micron", "optical"): "fab-wide [C]", ("Micron", "e-beam"): "FE", ("Micron", "extra: virtual metrology / ML sampling"): "FE",
    ("Amkor", "electrical test"): "offer [C]",
}


def main():
    ev = {r["id"]: r for r in csv.DictReader(open(os.path.join(OUT, "evidence.csv"), encoding="utf-8"))}
    missing = sorted({i for v in A.values() for i in v[2].split() if i not in ev})
    if missing:
        raise SystemExit(f"cited ids not in evidence.csv: {missing}")
    assert len(A) == len(CO) * len(METHODS), f"{len(A)} cells, expected {len(CO)*len(METHODS)}"
    abbrev = {"production": "PROD", "pilot": "PILOT", "lab": "lab", "none found": "-"}
    md = ["| Method | " + " | ".join(CO) + " |", "|---|" + "---|" * len(CO)]
    for m in METHODS:
        md.append(f"| {m} | " + " | ".join(abbrev[A[(c, m)][0]] + (f" ({SCOPE[(c, m)]})" if (c, m) in SCOPE else "") for c in CO) + " |")
    rows, n = [], 0
    basis = ["", "### Basis for each cell (one [I] row each in evidence.csv, SYN-001 ...)", ""]
    for c in CO:
        for m in METHODS:
            n += 1
            st, what, ids, conf, reason = A[(c, m)]
            sid = f"SYN-{n:03d}"
            tags = sorted({ev[i]["tag"] for i in ids.split()})
            inputs = (ids.replace(" ", ", ") + f" (tags of inputs: {'/'.join(tags)})") if ids else "no company statement found in the documents read (section1_table.csv and module notes)"
            sc = SCOPE.get((c, m), "")
            rows.append(dict(id=sid, tag="[I]", claim=f"{c} - {m}: {st}" + (f" [rests on: {sc}]" if sc else "") + (f" ({what})" if what else ""), value=st + (f" ({sc})" if sc else ""),
                             unit="status class", period_fiscal="n/a", period_calendar="Jan 2025 - Nov 2026",
                             document="calc/method_matrix.py (assessment over evidence rows)", date="2026-11-21",
                             page_or_section="dossier section 5", url="", local_file="", quote="", confidence=conf,
                             note=f"Inputs: {inputs}. Confidence {conf}: {reason}. Script: research/out/customer_side/calc/method_matrix.py"))
            if st != "none found" or what:
                basis.append(f"- {sid} {c} / {m}: **{st}**" + (f" (rests on: {sc})" if sc else "") + f". {what}. Inputs: {ids or 'none'}. [I] {conf}.")
    with open(os.path.join(OUT, "parts", "SYN.csv"), "w", newline="", encoding="utf-8") as fh:
        cols = ["id", "tag", "claim", "value", "unit", "period_fiscal", "period_calendar", "document", "date",
                "page_or_section", "url", "local_file", "quote", "confidence", "note"]
        w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(rows)
    open(os.path.join(OUT, "calc", "method_matrix.md"), "w", encoding="utf-8").write("\n".join(md + basis) + "\n")
    from collections import Counter
    print("cells", len(rows), Counter(r["value"] for r in rows))
    for c in CO:
        print(c, Counter(A[(c, m)][0] for m in METHODS))


if __name__ == "__main__":
    main()
