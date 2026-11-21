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
 ("SK hynix", "optical"): ("production", "HBM in-line chip-warpage optical module, \"commercialized solution currently in use\" ([C]); fab-wide optical inspection at each process step in development and mass production", "PAPM-201 PAPM-203 PAPM-206 TALK-006 TALK-007", "Medium", "HBM warpage production status is the company's own untestable claim; fab-wide statement is generic"),
 ("SK hynix", "infrared"): ("production", "TSV CVD-film IR inspection in the HBM WLP line \"successfully applied in mass production\"; post-bond die shift/tilt by IR validated in a \"production-grade MI setup\" on actual HBM wafers (pilot)", "PAPM-219 PAPM-222 PAPM-213 PAPM-216", "Medium", "journal full text read; 'applied in mass production' refers to the optimized TSV film process including its IR inspection step"),
 ("SK hynix", "acoustic"): ("lab", "C-SAM on 12-layer HBM4 stacks of Mechanical Test Vehicle 4: \"void-free\"", "PAPM-134 PAPM-135 PAPM-136 PAPM-137", "High", "abstract states a test vehicle"),
 ("SK hynix", "laser-acoustic"): ("none found", "", "", "Medium", "no SK hynix document read names it"),
 ("SK hynix", "X-ray CT / laminography"): ("none found", "", "", "Medium", "no SK hynix 2025-26 document read names X-ray for HBM/TSV/bonding (PAPM gap list)"),
 ("SK hynix", "X-ray scatterometry / XRF / XRD"): ("none found", "", "", "Medium", "none in abstracts or newsroom read"),
 ("SK hynix", "AFM"): ("none found", "", "", "Medium", "none in abstracts or newsroom read"),
 ("SK hynix", "e-beam"): ("production", "FIB cross-section of TSV SiO2 step coverage in a process \"successfully applied in mass production\"; fab-wide electron-microscope inspection at each process step", "PAPM-221 PAPM-222 TALK-006 TALK-007", "Medium", "FIB is used as the process monitor of a production process; fab-wide statement is generic"),
 ("SK hynix", "electrical test"): ("lab", "HBM4 MTV4 daisy-chain resistance; HBM3E TSV keep-out-zone EM/TDDB and chip-level tests; back-side RDL daisy-chain test vehicle. Press only: an HBM4 system-level tester passed internal qualification ([S], not counted)", "PAPM-135 PAPM-139 PAPM-140 PAPM-155 SMP-009 TALK-017", "Medium", "own words give test vehicles only; qualification report is press"),
 ("SK hynix", "extra: virtual metrology / ML sampling"): ("production", "Panoptes VM \"in its production lines since 2022\"; GRACE overlay VM in production since 2025 (front-end, not HBM-specific)", "TALK-004 SMP-005 SMP-007", "High", "company newsroom, explicit"),
 # ---------------- Samsung
 ("Samsung", "optical"): ("production", "191 Hitachi High-Tech IS4100 patterned-wafer inspectors matched in a DRAM HVM line (memory front end, not HBM); for hybrid bonding optical inspection is only \"examined\" (VLSI 2025 workshop)", "PAPM-224 PAPM-225 TALK-020", "High", "journal full text names the HVM line"),
 ("Samsung", "infrared"): ("lab", "IR photoemission / lock-in OBIRCH in V-NAND failure analysis, said to be \"reaching their limits\"", "PAPM-081 PAPM-086", "Medium", "FA lab use only; nothing on bonded interfaces"),
 ("Samsung", "acoustic"): ("lab", "acoustic microscopy \"examined\" for hybrid-bonding inspection (VLSI 2025 workshop abstract). Press only: talks/joint development with ultrasound vendors ([S], not counted)", "TALK-020 TALK-027", "Medium", "own words = 'examined'"),
 ("Samsung", "laser-acoustic"): ("none found", "Press only: Onto picosecond laser-ultrasound tools reportedly \"undergoing validation on mass production lines\" ([S], not counted)", "TALK-024 TALK-025", "Medium", "no Samsung document names it; the pilot claim is TheElec citing industry sources"),
 ("Samsung", "X-ray CT / laminography"): ("lab", "X-ray microscopy \"examined\" for hybrid bonding (VLSI 2025 workshop); patent application on in-line X-ray laminography/CT for HBM micro-bumps (a patent, not a use statement). Press only: talks with X-ray vendors", "TALK-020 XR-011 XR-012 TALK-027", "Medium", "no use statement beyond 'examined'"),
 ("Samsung", "X-ray scatterometry / XRF / XRD"): ("none found", "pre-bond SiCN characterised by XPS, ToF-SIMS and MEIS (other methods)", "PAPM-057 PAPM-058", "Medium", "no XRF/XRD/SAXS named"),
 ("Samsung", "AFM"): ("pilot", "high-throughput in-line AFM \"performed on production wafers in the fab\" for hybrid bonding in VNAND (three wafers; Nearfield co-authors); AFM \"examined\" for HB (workshop)", "SMP-016 TALK-020", "Medium", "production wafers, but a three-wafer study with the tool vendor; VNAND, not HBM"),
 ("Samsung", "e-beam"): ("lab", "PFIB-SEM deprocessing of HBM2 (with Thermo Fisher); TEM of pre-bond SiCN; AI super-resolution SEM imaging (no status). SEM review/CD measurement in the fab named as a contamination source (implies routine use, not stated as such)", "PAPM-094 PAPM-095 PAPM-057 SMP-017 PAPM-112 PAPM-113", "Low", "routine fab SEM use is implied, not stated"),
 ("Samsung", "electrical test"): ("production", "HBM buffer-die pad-to-micro-bump interface-resistance pre-screen \"in mass production\"; repair+ECC \"Validated on HBM\" and 12-High HBM chip-on-wafer refresh test \"demonstrated in HBM products\" (pilot); leakage-current metrology for hybrid Cu bonding (lab)", "PAPM-049 PAPM-105 PAPM-108 PAPM-109 PAPM-052 PAPM-054", "High", "explicit 'in mass production' in the IRPS 2025 abstract"),
 ("Samsung", "extra: virtual metrology / ML sampling"): ("lab", "ML imputation where \"measurements are conducted on only about 4% of the products\" in DRAM development; SPIE VNAND mass-metrology VM paper attributed to Samsung by inference only", "PAPM-098 PAPM-099 PAPM-193", "Medium", "development phase; SPIE attribution is [I]"),
 # ---------------- Micron
 ("Micron", "optical"): ("production", "AI-enhanced imaging and defect classification across \"front end, assembly and test\" (fab-wide, not HBM-specific)", "TALK-038 TALK-039 SMP-022", "Medium", "company blog, generic"),
 ("Micron", "infrared"): ("none found", "", "", "Medium", "no Micron document read names it"),
 ("Micron", "acoustic"): ("lab", "CSAM \"clean of voids\" on wafer-to-wafer bonding aimed at HBM density; integration \"is demonstrated\"", "PAPM-015 PAPM-016 PAPM-017", "High", "abstract: demonstration"),
 ("Micron", "laser-acoustic"): ("none found", "", "", "Medium", "no Micron document read names it"),
 ("Micron", "X-ray CT / laminography"): ("lab", "co-authored lab X-ray irradiation study of 3D NAND (not an inspection-use statement). Vendor claim only: SEC says it supplies HBM X-ray inspection tools to Micron (not counted)", "XR-007 XR-008", "Medium", "irradiation study, not inspection use"),
 ("Micron", "X-ray scatterometry / XRF / XRD"): ("none found", "", "", "Medium", "no Micron document read names it"),
 ("Micron", "AFM"): ("none found", "", "", "Medium", "no Micron document read names it"),
 ("Micron", "e-beam"): ("production", "CD-SEM image anomaly detection \"during in-line monitoring\"; new in-line CD-SEM secondary-electron metric for DRAM container slant; off-line SEM overlay where capacitor tilt limits in-line metrology", "PAPM-007 PAPM-008 PAPM-002 PAPM-010", "Medium", "in-line monitoring in a memory fab; HBM not named"),
 ("Micron", "electrical test"): ("lab", "daisy chains in HBM development find voids before visual inspection (CTO, quoted by press [S]); added electrical coverage \"to prevent test escapes during production\" in graphics DRAM (proposed)", "TALK-035 TALK-036 PAPM-026 PAPM-027", "Medium", "HBM item is press-quoted; DRAM item is a proposal"),
 ("Micron", "extra: virtual metrology / ML sampling"): ("pilot", "cloud VM validated on one year of production data in an HVM memory fab, \"meeting production release criteria\" (dry etch)", "SMP-025", "Medium", "release criteria met; deployment scale not stated"),
 # ---------------- TSMC
 ("TSMC", "optical"): ("none found", "", "", "Medium", "TSMC's own sites refuse scripts; no TSMC paper read names it"),
 ("TSMC", "infrared"): ("lab", "\"IR imaging\" of bonding quality in a university-led wafer-level transfer paper with two TSMC co-authors", "PAPL-001 PAPL-002", "Medium", "university-led research"),
 ("TSMC", "acoustic"): ("none found", "", "", "Medium", "no TSMC document read names it"),
 ("TSMC", "laser-acoustic"): ("none found", "", "", "Medium", "no TSMC document read names it"),
 ("TSMC", "X-ray CT / laminography"): ("none found", "Press only: SEMICON Taiwan 2026 forum keynote reportedly lists \"DRAM/HBM damage concern by X-ray\" and calls for X-ray-compatible HBM ([S]; abstract NOT RETRIEVED)", "XR-013 XR-015", "Medium", "no TSMC-authored text read"),
 ("TSMC", "X-ray scatterometry / XRF / XRD"): ("none found", "", "", "Medium", "no TSMC document read names it"),
 ("TSMC", "AFM"): ("none found", "", "", "Medium", "no TSMC document read names it"),
 ("TSMC", "e-beam"): ("none found", "", "", "Medium", "no in-scope TSMC document names it (die-level e-beam probing is adjacent)"),
 ("TSMC", "electrical test"): ("lab", "SoIC-CS daisy chains \"proven feasible for the first time\"; CoWoS-R via-chain/leakage tests (platform \"currently in production\" is a [C] about the platform, not the test); UCIe multi-die test on test vehicles", "PAPL-010 PAPL-011 PAPL-012 PAPL-006 PAPL-008 PAPL-022", "Medium", "test methods shown on test vehicles"),
 ("TSMC", "extra: virtual metrology / ML sampling"): ("lab", "ML 'Die of Interest' ranking of inline data; adaptive/targeted testing \"is envisioned\"", "SMP-035", "High", "explicitly envisioned"),
 # ---------------- Intel
 ("Intel", "optical"): ("lab", "image capture \"on the move\" for 100% chip-to-wafer bond-overlay metrology (wavelength not stated; development with roadmap; EV Group co-author)", "PAPL-055 PAPL-056 PAPL-059 PAPL-061", "Medium", "development paper; imaging band not stated so the cell is provisional"),
 ("Intel", "infrared"): ("lab", "NIR post-bond chiplet overlay mapping on a fiducial-grid test vehicle; SIL thermal imaging and RF lock-in thermography in FA of 3D/HBM packages", "PAPL-046 PAPL-078 PAPL-089", "High", "test vehicle / FA"),
 ("Intel", "acoustic"): ("lab", "cSAM: \"no significant void formation\" in C2W hybrid bonding (with Applied Materials)", "PAPL-035", "High", "development paper"),
 ("Intel", "laser-acoustic"): ("none found", "", "", "Medium", "no Intel document read names it"),
 ("Intel", "X-ray CT / laminography"): ("lab", "3D X-ray CT of micro-bump joints (CPO TCB research); synchrotron XADA on a mock stacked die; X-ray dose study on on-package DRAM for board inspection", "PAPL-067 PAPL-082 XR-001 XR-002", "High", "research / FA / dose study"),
 ("Intel", "X-ray scatterometry / XRF / XRD"): ("none found", "", "", "Medium", "no Intel document read names it"),
 ("Intel", "AFM"): ("lab", "AFM and nanoindentation of hybrid-bonding Cu pads (NIST-led, Intel co-author)", "PAPL-073", "High", "research"),
 ("Intel", "e-beam"): ("lab", "FIB-SEM on Kelvin structures found interconnect gaps; low-kV SEM-EDX of Cu surface oxygen", "PAPL-036 PAPL-069", "High", "development / research"),
 ("Intel", "electrical test"): ("lab", "10k-via daisy chains >90% yield; multi-level bond-via resistance; fluidic self-alignment \"preliminary readouts\"; EMIB-T HBM4E wideband measurements; 9-wafer TSV DRAM cube TSV resistance", "PAPL-033 PAPL-034 PAPL-026 PAPL-029 PAPL-064 PAPL-094", "High", "test vehicles / feasibility"),
 ("Intel", "extra: virtual metrology / ML sampling"): ("none found", "front-end litho virtual defect metrology on every wafer exists but is logic front end, out of scope", "SMP-033", "Medium", "out of scope for HBM / hybrid bonding"),
 # ---------------- ASE
 ("ASE", "optical"): ("none found", "Press only: \"high-efficiency image anomaly-detection AI\" named as a focus area ([S])", "TALK-048", "Medium", "no ASE technical document names it"),
 ("ASE", "infrared"): ("none found", "", "", "Medium", "no ASE document read names it"),
 ("ASE", "acoustic"): ("lab", "AI-enhanced SAM cuts scan time in flip-chip FA (adjacent: not HBM or hybrid bonding; PVA TePla co-author)", "SMP-037", "Medium", "adjacent scope only"),
 ("ASE", "laser-acoustic"): ("none found", "", "", "Medium", "no ASE document read names it"),
 ("ASE", "X-ray CT / laminography"): ("lab", "3D X-ray microscopy in FA of FOCoS-B micro-bumps and FOCoS ASIC-HBM RDL; stated limit: field of view", "PAPL-107 PAPL-100 PAPL-101", "High", "failure-analysis flow"),
 ("ASE", "X-ray scatterometry / XRF / XRD"): ("none found", "", "", "Medium", "no ASE document read names it"),
 ("ASE", "AFM"): ("lab", "AFM of pre-bond Ag roughness and Cu protrusion / PI recess on hybrid-bonding test vehicles (NTU-led, ASE co-authors)", "PAPL-113 PAPL-119", "High", "test vehicles"),
 ("ASE", "e-beam"): ("lab", "SEM/EDS in micro-bump FA; SEM/TEM of bonded interfaces on test vehicles", "PAPL-108 PAPL-115", "High", "FA / test vehicles"),
 ("ASE", "electrical test"): ("lab", "open/short and I-V curve tracing in FA of HBM-bearing fan-out packages; hybrid-bond electrical yield on test vehicles", "PAPL-106 PAPL-116", "High", "FA / test vehicles"),
 ("ASE", "extra: virtual metrology / ML sampling"): ("none found", "", "", "Medium", "none found"),
 # ---------------- Amkor
 ("Amkor", "optical"): ("none found", "shadow moire warpage on a lidded FCBGA (adjacent)", "PAPL-181", "Medium", "adjacent scope only"),
 ("Amkor", "infrared"): ("none found", "", "", "Medium", "none found"),
 ("Amkor", "acoustic"): ("lab", "SAT at thermal-cycling read-points on a 2.5D CoW test vehicle with mimic HBMs; cracks confirmed by cross-section", "TALK-051 TALK-052", "High", "test vehicle"),
 ("Amkor", "laser-acoustic"): ("none found", "", "", "Medium", "none found"),
 ("Amkor", "X-ray CT / laminography"): ("none found", "", "", "Medium", "none found"),
 ("Amkor", "X-ray scatterometry / XRF / XRD"): ("none found", "", "", "Medium", "none found"),
 ("Amkor", "AFM"): ("none found", "", "", "Medium", "none found"),
 ("Amkor", "e-beam"): ("none found", "", "", "Medium", "none found"),
 ("Amkor", "electrical test"): ("production", "test-services page offers \"in-situ test between key assembly steps and final test (SLT and ATE) for 2.5D & 3D\" (an offer, not a statement about a named product)", "SMP-038 TALK-049 TALK-050", "Low", "service offer; date of the text not stated"),
 ("Amkor", "extra: virtual metrology / ML sampling"): ("none found", "", "", "Medium", "none found"),
}


# What the production / pilot status rests on (shown in the matrix cell):
# HBM = HBM stack, TSV or micro-bump line; HB = hybrid / wafer bonding (not HBM); FE = memory front end, fab-wide;
# offer = service offering. [C] = the status is the company's own untestable claim.
SCOPE = {
    ("SK hynix", "optical"): "HBM [C]; FE", ("SK hynix", "infrared"): "HBM", ("SK hynix", "e-beam"): "HBM; FE",
    ("SK hynix", "extra: virtual metrology / ML sampling"): "FE",
    ("Samsung", "optical"): "FE", ("Samsung", "AFM"): "HB (VNAND)", ("Samsung", "electrical test"): "HBM",
    ("Micron", "optical"): "FE", ("Micron", "e-beam"): "FE", ("Micron", "extra: virtual metrology / ML sampling"): "FE",
    ("Amkor", "electrical test"): "offer",
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
