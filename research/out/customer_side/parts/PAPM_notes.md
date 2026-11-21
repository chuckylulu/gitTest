# PAPM notes: conference-paper evidence for SK hynix, Samsung Electronics and Micron (Jan 2025 to 21 Nov 2026)

Files: `PAPM_table.csv` (50 rows, 42 papers), `PAPM.csv` (232 evidence rows: 212 [F], 15 [C], 5 [I]; every quote FOUND by `quote_check.py`), counts script `research/out/customer_side/calc/PAPM_counts.py`.
Conference papers here are evidenced by their abstract only. For the IEEE papers the full text is NOT RETRIEVED (ieeexplore.ieee.org bot challenge). For ISTFA (ASM) papers the publisher page was not tried. For SPIE the full text is NOT RETRIEVED (spiedigitallibrary.org bot challenge).
**Exception: four 2025 JSTS journal papers**, added at the coordinator's request, were read in full from the open-access article pages on jsts.org. They are three SK hynix papers and one SKKU paper whose first author is a Samsung Electronics engineer (PAPM-198 to PAPM-229).

How the set was built: I read the titles of all 304 rows in `calc/abstract_screen.csv` whose companies include SK hynix, Samsung or Micron. I then read the abstracts of about 110 of them, plus all 117 SPIE MIPC XXXIX/XL records that had a scope or company keyword, out of 309. A paper went into the table only if its abstract names (a) an in-scope object and (b) a method. In-scope papers whose abstract names no method have evidence rows only and are listed in section 1.4.

## 1. Findings by company

### 1.1 SK hynix (8 papers in the table, 11 rows)
- **HBM chip warpage, in-line (JSTS 2025, full text).** This is the clearest production statement in the module.
  - Problem: the authors state there is "currently no equipment or method for direct in-line measurement of chip warpage", as ultra-thin wafers are bonded to carrier wafers [C] (PAPM-199). Destructive sampling gave a sample "far too small" (PAPM-208).
  - Method: SK hynix added "an optical module for warpage measurement" and vacuum chucking to the automated 400 mm ring-frame handler (PAPM-203).
  - Validation: against an Akrometrix AXP destructive reference, the agreement is cosine 0.8805, Pearson 0.6610, R2 0.4369 (PAPM-204, PAPM-205).
  - Throughput: about 7-10 min for 600 chips with CTD-VC (PAPM-206). For the destructive flux-based UF-SL/CF-SL methods, a 3D laser scanner at ~10 um x-y resolution takes about 5 min per wafer (PAPM-207).
  - The destructive flux-based variants are limited by "time, cost, and operational complexity" (PAPM-209).
  - Claims, tagged [C]: "world's first" (PAPM-200); "implemented into measurement equipment and developed into a commercialized solution currently in use" (PAPM-201); method "transferred to measurement equipment suppliers", with the suppliers not named (PAPM-202).
- **HBM post-bond die shift and tilt by infrared (JSTS 2025, full text).** This is bond overlay in the stack.
  - SK hynix says tools "optimized for planar DRAM wafers" "fail to accurately assess" die shift and tilt, particularly post-bonding (PAPM-211); traditional overlay "cannot detect" them (PAPM-212).
  - Its method is IR imaging with a dual scan of base-wafer fiducials and top-die patterns (PAPM-213, PAPM-214).
  - Challenges the method addresses (not stated as remaining limits): "low contrast and IR resolution constraints" (PAPM-215).
  - Validated on "actual HBM device wafers in a production-grade MI setup" (PAPM-216).
- **TSV films in the HBM WLP line (JSTS 2025, full text).** "CVD film IR inspection" and FIB cross-section of SiO2 step coverage over TSVs (PAPM-218, PAPM-219, PAPM-221). The authors state the process was "successfully applied in mass production" [C] (PAPM-222); the yield drop from TSV edge damage occurred with an intermediate trial recipe (PAPM-220).
- **HBM4 stack, micro-bumps and voids.** The VLSI 2026 HBM4 paper (SK hynix Inc. / SK hynix America) checks micro-bump joint integrity "for entire 12-layer stacks" in two ways: daisy-chain resistance and Confocal Scanning Acoustic Microscopy (C-SAM). The result reported is "void-free and high micro-bump integrity". The work used "Mechanical Test Vehicle 4 (MTV4)", which places it at test-vehicle stage (PAPM-134, PAPM-135, PAPM-136, PAPM-137). The abstract names die warpage as a challenge but does not say how warpage was measured (PAPM-138).
- **TSV in HBM3E.** Electrical reliability tests (EM, IMD TDDB) plus "Chip level tests" were used for the TSV keep-out zone in HBM3E (PAPM-139, PAPM-140, PAPM-141, PAPM-142).
- **Pre-bond surface and bond overlay (hybrid bonding).** The SiCN pre-bond surface was characterized by VSFG spectroscopy and zeta potential (PAPM-146). The stated motivation is bonding alignment accuracy "towards below 200 nm pitch" (PAPM-145). This is a joint paper: first and last authors Yokohama National University, 4 of 10 authors SK hynix, 3 Tokyo Electron (bonder maker) (PAPM-143, PAPM-144).
- **W2W bonding interface strength.** An in-situ vision system films the Maszara blade test and measures crack velocity, which is an optical method (PAPM-152, PAPM-153). The authors state that the conventional test "has limitations in the amount of information" it yields (PAPM-151).
- **3D stacked memory, base-die back-side RDL.** A daisy-chain test vehicle with EM and TDDB tests and an 8-layer stack (PAPM-155, PAPM-156, PAPM-157, PAPM-158).
- **Other SK hynix papers.** Hybrid-bonding misalignment and dishing appear only in FEM simulation, with stability "even with up to 20% misalignment" (PAPM-160, PAPM-161). The 4F2 VG DRAM uses a "wafer-bonded structure" with die thinning, and no metrology is named (PAPM-163). The IITC 2025 paper on HBM wafer-level-packaging interconnect has no abstract (PAPM-164).
- **Lead (VM).** SK hynix's own newsroom says it has used Gauss Labs' Panoptes VM in production lines since 2022 [C] (PAPM-197). It also lists two joint SK hynix / Gauss Labs papers (PAPM-231); their match to SPIE MIPC XL DOIs is by title [I] (PAPM-232).

### 1.2 Samsung Electronics (18 papers + 3 SPIE by inference, 22 rows)
- **DRAM HVM optical defect inspection fleet (JSTS 2025, full text).**
  - An SKKU degree-programme paper: the first author is a Samsung Electronics engineer (1 of 3 authors); it is not an official Samsung Electronics paper (PAPM-223).
  - 191 Hitachi High-Tech IS4100 patterned-wafer inspectors at after-develop, after-etch and post-CMP checkpoints were sensitivity-matched to within ±2% in "a Samsung Electronics high-volume manufacturing (HVM) line" (PAPM-224, PAPM-225, PAPM-226).
  - Scope: 300 mm 10-nm-class D1y DRAM (PAPM-227).
  - Manual matching was "often requiring over three hours per tool"; PM time fell 45% (PAPM-228, PAPM-229).
  - This is memory front-end inspection, not HBM.
- **HBM electrical test is the most specific statement in this set.** The IRPS 2025 paper from DRAM Yield Enhancement pre-screens the pad to micro-bump interface resistance on the HBM buffer die "in mass production", by making small BEOL layout changes. The authors' reason: such failures are "hard to find in the HBM-DRAM fabrication site" (PAPM-046, PAPM-047, PAPM-048, PAPM-049, PAPM-050). Two more HBM electrical tests:
  - EDS repair integrated with on-die ECC, "Validated on HBM", which addresses "the rising test cost" (PAPM-105, PAPM-106, PAPM-107);
  - a refresh (tREFi) chip-on-wafer test at 120 C "for 12-High stacked HBM devices" (PAPM-108, PAPM-109); the cell transistor "is demonstrated in ... HBM products" is a company claim [C] (PAPM-110).
- **Hybrid Cu bonding.**
  - A "fast and non destructive" leakage-current method on a 20,000-pad array is called "a process sensitive electrical metrology signal"; the leakage origin "was verified through bonding misalignment analysis". The paper is Seoul National University-led, with 3 of 7 Samsung authors (PAPM-051, PAPM-052, PAPM-053, PAPM-054, PAPM-055).
  - Pre-bond SiCN plasma activation was characterized by TEM, ToF-SIMS, XPS and MEIS (PAPM-057, PAPM-058).
  - In-scope papers with no method named in the abstract:
    - Cu recess "within a nanometer range" by wet ALE (PAPM-116, PAPM-117, PAPM-118);
    - SiCN bond strength up to 2.11 J/m2 (PAPM-120);
    - edge dot-void vs edge roll-off in W2W bonding, from "experimental analysis" (PAPM-126, PAPM-127);
    - HCB and TCB HBM test vehicles, measured for thermal behaviour only (PAPM-129).
- **Wafer bonding in memory (V-NAND).** Two 450-layer cell wafers were bonded, and the "alignment deterioration" from large warpage was "solved by applying new overlay correction technology". The bond-overlay metrology is not named (PAPM-123, PAPM-124).
- **Failure analysis (FA) of packages and HBM.**
  - Samsung Semiconductor Inc. (San Jose) gave an invited review of the 2.5D/3D package FI-FA flow: fault isolation, cross-section, micro-probing and electron microscopy (PAPM-060, PAPM-061).
  - A vendor-led paper (5 of 6 authors ThermoFisher, 1 Samsung DRAM project engineer) deprocessed an HBM2 sample using a "Helios Hydra 5+ PFIB-SEM" (PAPM-094, PAPM-095, PAPM-096).
- **V-NAND fault localization (FA).**
  - Lock-in OBIRCH for depth isolation in Cell-over-Peripheral, with Hamamatsu co-authors (PAPM-081, PAPM-082, PAPM-083, PAPM-084).
  - IR-source photoemission and OBIRCH "are reaching their limits" as NAND height grows. Visible thermoreflectance (VTR) is proposed instead; 1 of 9 co-authors is from Hamamatsu (PAPM-085, PAPM-086, PAPM-087, PAPM-088).
  - Channel-hole navigation on Thermo Fisher's iFAST platform: 97.6% detection success at the "developmental stage". Joint paper: 3 of 9 co-authors are ThermoFisher (PAPM-089, PAPM-090, PAPM-091, PAPM-092).
- **DRAM films and lines (electrical).**
  - GIDL-asymmetry detection of lateral silicide diffusion, described as moving "from reactive microscopy to proactive electrical monitoring". The novelty, "zero-defect", "real-time" and turnaround wording are claims and are tagged [C] (PAPM-067, PAPM-068, PAPM-069, PAPM-070, PAPM-071, PAPM-230).
  - BCAT word-line disconnection screening. Test time falls from 10 h to 5 h. The conventional L4 test "often damages weak dies" (PAPM-076, PAPM-077, PAPM-078, PAPM-079).
  - A method to detect potential high-k defect sites by laser-induced leakage-current mapping "has been proposed and examined" (ZrO2 capacitor arrays). DRAM is not named in the abstract; 2 of 7 authors are Samsung (PAPM-073, PAPM-074).
  - Chip-level extraction of mismatch across "millions" of bit-line sense amplifiers in packaged DRAM (PAPM-102, PAPM-103, PAPM-104).
  - Chip-edge burnout in thinned, warped memory dies in multi-die packages, found by DC tests after assembly (PAPM-063, PAPM-064, PAPM-065).
- **Sampling (lead).** In DRAM development "measurements are conducted on only about 4% of the products". ML imputation fills in the rest (PAPM-098, PAPM-099, PAPM-100).
- **e-beam side effect (lead).** Micro-bubble coating defects were traced to "wafer review or critical dimension (CD) measurements using a scanning electron microscope (SEM)". The cause was carbon contamination in the SEM chamber (PAPM-112, PAPM-113, PAPM-114).
- **SPIE papers attributed by product term only, [I] Medium/Low.** Each of these papers names "VNAND" / "V-NAND", Samsung's product term. The ISTFA 2026 Samsung paper uses the same term next to "SAMSUNG" (PAPM-091).
  - OES plus deep-learning prediction of the memory-hole distortion profile on "8-th generation VNAND", best R2 0.69 / 0.58 (PAPM-183, PAPM-184, PAPM-185, PAPM-186);
  - macro-optical colour inspection of HAR etch defects in "3D V-NAND" (PAPM-188, PAPM-189, PAPM-190, PAPM-191);
  - wafer mass metrology (MMT) on "9th-generation VNAND", with stated limits of "near-zero site coverage and limited directional information" (PAPM-193, PAPM-194, PAPM-195, PAPM-196).

### 1.3 Micron (9 papers + 4 SPIE, 17 rows)
- **HBM / wafer bonding.** The only in-scope Micron packaging abstract is the ECTC 2025 W2W bonding paper, aimed at "HBM product density":
  - post-bond checks: "CSAM results are clean of voids" and an "X-section" of both bonding interfaces;
  - the top wafer is thinned to "less than 2um";
  - integration into "the new memory wafer-to-wafer (W2W) bonding flow is demonstrated" (PAPM-015, PAPM-016, PAPM-017, PAPM-018).
  The VLSI 2025 "High Bandwidth Memory for AI" paper has no abstract in either record (PAPM-038). The VLSI 2026 review says only that "advanced metrology solutions are essential" [C] (PAPM-040).
- **DRAM CD and overlay.**
  - An inline CD-SEM secondary-electron metric for container slant, validated against TEM and linked to yield (PAPM-002, PAPM-003, PAPM-004, PAPM-005).
  - CD-SEM image anomaly detection "during in-line monitoring" (PAPM-007, PAPM-008).
  - Off-line SEM overlay of capacitor to metal RDL, used because "severe capacitor tilt limits the reliability of inline fab metrology". It takes about 7 min per image pair (PAPM-010, PAPM-011, PAPM-012, PAPM-013).
- **Detection limits Micron states.**
  - An oxide void in Flash "not easily detectable by the inline inspection" and missed by initial electrical test (PAPM-020, PAPM-021).
  - A DRAM particle defect "undetectable through standard electrical testing" (PAPM-023, PAPM-024).
  - Increased electrical coverage and wafer-level analysis "to prevent test escapes during production" in graphics DRAM "have been proposed" (not stated as deployed) (PAPM-026, PAPM-027).
- **e-beam FA in memory.**
  - "low-dose TEM imaging" of photoresist. Other protection methods caused "distortion from preparation and beam interaction" (PAPM-029, PAPM-030, PAPM-031, PAPM-032).
  - AI-guided FIB thinning for DRAM/NAND, using Thermo Fisher AIPs; 8 of 16 authors are Thermo Fisher. "Successfully implemented" is a self-reported in-use claim [C] (PAPM-034, PAPM-035, PAPM-036, PAPM-037).
- **SPIE papers that name Micron.** The records carry no affiliations, so authorship is unverified.
  - Inline automated PFIB-SEM "ground truth" CD metrology on 3D NAND "in collaboration with Micron", with slit-width repeatability 3σ 0.64 nm (PAPM-166, PAPM-167, PAPM-168, PAPM-169).
  - ASML 25-beamlet multi-e-beam inspection evaluated "on Micron Technology's DRAM and 3D-NAND devices" (PAPM-171, PAPM-172, PAPM-173).
  - ASML ML-guided e-beam sampling with defective-die capture "up to 4.3x on Micron Technology's memory devices" (PAPM-175, PAPM-176, PAPM-177).
  - A "1β DRAM" EBI coverage paper recommending 1.99% in-die coverage. It is attributed to Micron [I] Low on node naming only (PAPM-180, PAPM-181).
- **Leads.**
  - VM validated on "one year of production data ... in an HVM memory fab" (PAPM-042, PAPM-043).
  - Terrestrial TID threshold "shown to be inconsequential" for DRAM. This is not inspection dose (PAPM-045).

### 1.4 Cross-company pattern
These counts come from `calc/PAPM_counts.py` run on `PAPM_table.csv`, and are [I] High.
- **HBM / stacking / bonding: 23 rows from 17 papers.**
  - electrical test: 8 rows (Samsung 5, SK hynix 3);
  - e-beam: 4 rows (Samsung 3, SK hynix 1);
  - acoustic: 2 rows (SK hynix C-SAM on HBM4 TV; Micron CSAM on W2W);
  - optical: 2 rows (SK hynix crack-velocity vision; SK hynix in-line chip warpage);
  - infrared: 2 rows (both SK hynix JSTS: post-bond die shift/tilt; TSV film inspection);
  - other: 5 rows.
- **No X-ray or AFM row.** None of the three companies' 2025-26 conference abstracts, nor the four JSTS full texts, names X-ray CT, laminography or AFM for HBM, TSV or hybrid bonding.
- **Memory film / CD / FA: 27 rows from 25 papers.** These are dominated by e-beam: Micron 5 rows, plus 4 in SPIE papers that name Micron or are attributed to it.
- **Status and limits.** 21 of 50 rows have no stated status and 31 of 50 have no stated limits. Statements of mass production or HVM:
  - Samsung bump-resistance paper (PAPM-049);
  - Samsung DRAM optical-inspection fleet (PAPM-224);
  - SK hynix TSV-film paper [C] (PAPM-222);
  - SK hynix warpage "commercialized solution currently in use" [C] (PAPM-201);
  - the Samsung-attributed MMT paper (PAPM-195).
  Test vehicles are explicit for SK hynix (PAPM-135, PAPM-158).
- **Reliability.** These counts measure what abstracts (and four journal full texts) mention, not what fabs use.

## 2. Papers whose full text the user should save by hand (priority order)
1. SK hynix, VLSI 2026, "High Bandwidth Memory 4 (HBM4) Package Development Challenges". 10.1109/vlsitechnologyandcir65830.2026.11577576, https://doi.org/10.1109/vlsitechnologyandcir65830.2026.11577576. The S2 record marks it open access (CC BY).
2. Samsung, IRPS 2025, "Study on the Measurement Method of Interface Resistance in HBM-DRAM...". 10.1109/irps48204.2025.10983202, https://doi.org/10.1109/irps48204.2025.10983202
3. Samsung, ECTC 2026, "Dependence of Leakage Current Characteristics on Bonding Dielectrics in Fine-Pitch Hybrid Cu Bonding". 10.1109/ectc51846.2026.00250, https://doi.org/10.1109/ectc51846.2026.00250
4. Micron, ECTC 2025, "Advanced Memory Wafer-to-Wafer Bonding with Support of Recyclable Carrier Systems". 10.1109/ectc51687.2025.00097, https://doi.org/10.1109/ectc51687.2025.00097
5. Samsung, ECTC 2025, wet ALE for Cu surface topography in hybrid bonding. The Cu-recess metrology is not named in the abstract. 10.1109/ectc51687.2025.00098, https://doi.org/10.1109/ectc51687.2025.00098
6. Samsung, VLSI 2026, "Demonstration of Cell Multi-Bonding (CMB) Technology..." (bond overlay under large warpage). 10.1109/vlsitechnologyandcir65830.2026.11577637, https://doi.org/10.1109/vlsitechnologyandcir65830.2026.11577637
7. SK hynix + TEL, ECTC 2025, "Bond Wave Analysis of SiCN for Fine Pitch Hybrid Bonding". 10.1109/ectc51687.2025.00350, https://doi.org/10.1109/ectc51687.2025.00350
8. SK hynix, IRPS 2025, "Effect of TSV - Keep Out Zone on BEOL Reliability of HBM3E". 10.1109/irps48204.2025.10982993, https://doi.org/10.1109/irps48204.2025.10982993
9. Samsung Semiconductor Inc., IRPS 2025 invited, "Fault Isolation and Failure Analysis Challenges in Advanced Packages". 10.1109/irps48204.2025.10982912, https://doi.org/10.1109/irps48204.2025.10982912
10. Micron, VLSI 2025, "High Bandwidth Memory for AI" (no abstract anywhere). 10.23919/vlsitechnologyandcir65189.2025.11074880, https://doi.org/10.23919/vlsitechnologyandcir65189.2025.11074880
11. SK hynix, IITC 2025, "Metal interconnection of high bandwidth memory in wafer level packaging" (no abstract). 10.1109/iitc66087.2025.11075373, https://doi.org/10.1109/iitc66087.2025.11075373
12. Samsung, ECTC 2025, "Simulation Analysis of Edge Dot-Void Formation and Edge Roll-Off Effects in Wafer-to-Wafer Bonding" (void detection method not named). 10.1109/ectc51687.2025.00213, https://doi.org/10.1109/ectc51687.2025.00213
13. Micron, ASMC 2026, "Inline Detection of DRAM Container Etch Slant using Secondary Electron Detector on CD-SEM". 10.1109/asmc69324.2026.11551247, https://doi.org/10.1109/asmc69324.2026.11551247
14. Micron, ISTFA 2026, "DRAM Capacitor-Metal Redistribution Layer Overlay Measurement...". 10.31399/asm.cp.istfa2026p0596, https://doi.org/10.31399/asm.cp.istfa2026p0596
15. SPIE MIPC XL, "PFIB-SEM wafer DualBeam applications for ground truth in-fab 3D NAND metrology" (names Micron). 10.1117/12.3092424, https://doi.org/10.1117/12.3092424

## 3. SPIE papers needing affiliation check
The SPIE MIPC XXXIX (Feb 2025) and XL (Feb 2026) records carry no affiliations, in either Crossref or Semantic Scholar. The user should save each page from https://doi.org/<DOI>.

**Attributed in the table by inference only; please confirm the authors:**
- 10.1117/12.3087830 (1β DRAM, Micron?) https://doi.org/10.1117/12.3087830
- 10.1117/12.3051179 (VNAND, Samsung?) https://doi.org/10.1117/12.3051179
- 10.1117/12.3090309 (V-NAND, Samsung?) https://doi.org/10.1117/12.3090309
- 10.1117/12.3085527 (VNAND MMT, Samsung?) https://doi.org/10.1117/12.3085527

**Named Micron but authorship unknown:** 10.1117/12.3092424, 10.1117/12.3056182, 10.1117/12.3093590 (URLs as https://doi.org/<DOI>).

**A. HBM, hybrid bonding, wafer-bond overlay and distortion, TSV, micro-bump (none names a chipmaker)**
- 10.1117/12.3095356 | MIPC XL | Buried void inspection in high bandwidth memory with picosecond laser acoustics | https://doi.org/10.1117/12.3095356
- 10.1117/12.3093061 | MIPC XL | eBeam process control for yield and reliability in advanced HBM hybrid bonding | https://doi.org/10.1117/12.3093061
- 10.1117/12.3090618 | MIPC XL | Inspection and metrology of micro-bumps and hybrid copper bonding using high-resolution 3D x-ray imaging (imaged an Nvidia GPU 8-layer HBM stack and an AMD 5800X3D, which are teardowns, not chipmaker statements) | https://doi.org/10.1117/12.3090618
- 10.1117/12.3050400 | MIPC XXXIX | Challenges and responses of metrology technologies for the new wave of 3d NAND devices (HCB in 3D NAND) | https://doi.org/10.1117/12.3050400
- 10.1117/12.3049615 | MIPC XXXIX | Shape-induced overlay for wafer-to-wafer hybrid bonding (uses "CBA", a Kioxia/WD term, so probably none of the seven) | https://doi.org/10.1117/12.3049615
- 10.1117/12.3088567 | MIPC XL | Characterization and mitigation of wafer bonding-induced distortions to enable the post-bonding lithography requirements of advanced nodes (DRAM 4F2/3D DRAM; TEL bonder named) | https://doi.org/10.1117/12.3088567
- 10.1117/12.3089964 | MIPC XL | Characterization and prediction of overlay signatures in WxW bonding processes for BS-PDN | https://doi.org/10.1117/12.3089964
- 10.1117/12.3089026 | MIPC XL | Bonding-induced overlay fingerprint modeling using Zernike polynomials | https://doi.org/10.1117/12.3089026
- 10.1117/12.3090515 | MIPC XL | Advanced overlay metrology for wafer-to-wafer hybrid bonding in 3D integration | https://doi.org/10.1117/12.3090515
- 10.1117/12.3090683 | MIPC XL | Novel scanner corrections ... lithography after wafer-to-wafer bonding | https://doi.org/10.1117/12.3090683
- 10.1117/12.3090568 | MIPC XL | Optical overlay metrology challenges in next-gen semiconductor nodes (IR metrology for W2W) | https://doi.org/10.1117/12.3090568
- 10.1117/12.3051014 | MIPC XXXIX | Cu pad height evaluation technique using four-directional BSE signal of SEM for hybrid bonding applications | https://doi.org/10.1117/12.3051014
- 10.1117/12.3090676 | MIPC XL | Cu pad metrology using four-directional BSE signal of SEM for hybrid bonding applications | https://doi.org/10.1117/12.3090676
- 10.1117/12.3091416 | MIPC XL | Inline monitoring of hybrid bonding Cu recess with vertical traveling scatterometry machine learning | https://doi.org/10.1117/12.3091416
- 10.1117/12.3051799 | MIPC XXXIX | Ultrafast AFM metrology for hybrid bonding applications | https://doi.org/10.1117/12.3051799
- 10.1117/12.3051135 | MIPC XXXIX | Toward extreme throughput nanotopography metrology with atomic force microscope arrays | https://doi.org/10.1117/12.3051135
- 10.1117/12.3089715 | MIPC XL | Twenty heads are better than one: scalable microAFM for high-throughput metrology and inspection | https://doi.org/10.1117/12.3089715
- 10.1117/12.3093880 | MIPC XL | Comprehensive post-CMP surface metrology using large-area atomic force microscopy with optical-level throughput | https://doi.org/10.1117/12.3093880
- 10.1117/12.3051414 | MIPC XXXIX | Atomic force microscopy: from research lab to high-volume manufacturing | https://doi.org/10.1117/12.3051414
- 10.1117/12.3050578 | MIPC XXXIX | Phase retrieval of periodic patterns (Cu pad dishing, simulation) | https://doi.org/10.1117/12.3050578
- 10.1117/12.3050820 | MIPC XXXIX | Suitability of half-wavelength contact acoustic microscopy to detect deeply buried voids | https://doi.org/10.1117/12.3050820
- 10.1117/12.3090939 | MIPC XL | Enabling metrology and inspection for CFET structures using hybrid qualification approaches (W2W voids by SAM; logic) | https://doi.org/10.1117/12.3090939
- 10.1117/12.3051519 | MIPC XXXIX | Revolutionizing 3D defect analysis with advanced DualBeam (FIB/SEM) (Thermo Fisher-authored) | https://doi.org/10.1117/12.3051519
- 10.1117/12.3050969 | MIPC XXXIX | Spectral reflectometry for process monitoring in high aspect ratio TSV fabrication | https://doi.org/10.1117/12.3050969
- 10.1117/12.3051271 | MIPC XXXIX | Machine learning-based 3D TSV metrology for advanced packaging | https://doi.org/10.1117/12.3051271
- 10.1117/12.3090822 | MIPC XL | In-line defect inspection and review of micromasking defects within high aspect ratio through-silicon vias | https://doi.org/10.1117/12.3090822
- 10.1117/12.3090552 | MIPC XL | Photocathode SEM with pixel current modulation ... (HAR TSV depth) | https://doi.org/10.1117/12.3090552
- 10.1117/12.3090559 | MIPC XL | Nondestructive depth metrology of high-aspect-ratio TSVs using yield controlled e-beaming (YCeB) (no abstract) | https://doi.org/10.1117/12.3090559
- 10.1117/12.3090787 | MIPC XL | Nano-TSV to BPR connection optimization (logic BSPDN) | https://doi.org/10.1117/12.3090787
- 10.1117/12.3060349 | MIPC XXXIX | X-ADAPT: AI-driven design-based strategy to address x-ray compatibility challenges in advanced packaging metrology | https://doi.org/10.1117/12.3060349
- 10.1117/12.3090548 | MIPC XL | GUIDE-X: VLM-LLM-based AI assistant for artifact detection and operator guidance in x-ray inspection | https://doi.org/10.1117/12.3090548
- 10.1117/12.3060363 | MIPC XXXIX | Towards zero defects: machine learning-driven solder bump reliability in semiconductor packaging | https://doi.org/10.1117/12.3060363
- 10.1117/12.3052399 | MIPC XXXIX | 3D metrology and inspection to enable the rise of stacked transistors, wafers, and chips | https://doi.org/10.1117/12.3052399

**B. DRAM / 3D NAND film, CD and overlay metrology (none names a chipmaker)**
- 10.1117/12.3051521 | DRAM capacitor-to-capacitor short ... large field of view SEM metrology | https://doi.org/10.1117/12.3051521
- 10.1117/12.3051156 | 3D reconstruction of 3D NAND memory etch profiles using FIB-SEM | https://doi.org/10.1117/12.3051156
- 10.1117/12.3048889 | CD-SAXS within-spot uniformity with mass CDSEM and 3D tomography (3D NAND) | https://doi.org/10.1117/12.3048889
- 10.1117/12.3090197 | Hole-to-hole distance variance in 3D NAND using Axion x-ray CD metrology | https://doi.org/10.1117/12.3090197
- 10.1117/12.3090205 | Axion physics-augmented AI ... tilt measurement in memory devices | https://doi.org/10.1117/12.3090205
- 10.1117/12.3090470 | GAN autoencoder denoising in x-ray CD metrology (3D NAND, DRAM) | https://doi.org/10.1117/12.3090470
- 10.1117/12.3090227 | Adaptive CD parameter evaluation in x-ray metrology with ML (3D NAND) | https://doi.org/10.1117/12.3090227
- 10.1117/12.3090491 | High-resolution 3D NAND profile measurement using optical metrology and ML | https://doi.org/10.1117/12.3090491
- 10.1117/12.3051616 | Dual beam-based ultra-fast process control on HAR memory devices | https://doi.org/10.1117/12.3051616
- 10.1117/12.3090492 | In-situ metrology for HAR channel holes via diagonal milling and one-shot SEM | https://doi.org/10.1117/12.3090492
- 10.1117/12.3090657 | Automated energy-filtered TEM metrology of 3D NAND and DRAM | https://doi.org/10.1117/12.3090657
- 10.1117/12.3056047 | Fast joint in-device metrology of overlay and tilt of multi-tier 3DNAND | https://doi.org/10.1117/12.3056047
- 10.1117/12.3051166 | Overlay and wafer stress control in semiconductor manufacturing (3D NAND, DRAM) | https://doi.org/10.1117/12.3051166
- 10.1117/12.3087454 | On-product overlay control in advanced 3D NAND nodes | https://doi.org/10.1117/12.3087454
- 10.1117/12.3051176 | Simultaneous in-die overlay and tilt in DRAM HVM | https://doi.org/10.1117/12.3051176
- 10.1117/12.3054121 | YieldStar AEI / IDM for DRAM, 3DNAND (ASML product) | https://doi.org/10.1117/12.3054121
- 10.1117/12.3051685 | ASR adoption as a holistic monitor solution in DRAM technology | https://doi.org/10.1117/12.3051685
- 10.1117/12.3090364 | On-device ADI overlay in advanced DRAM using high kV CFE | https://doi.org/10.1117/12.3090364
- 10.1117/12.3087581 | Large-area overlay measurement via DBM (DRAM) | https://doi.org/10.1117/12.3087581
- 10.1117/12.3090085 | MTD control for oblique intersecting layers in DRAM | https://doi.org/10.1117/12.3090085
- 10.1117/12.3107535 | Overlay accuracy in advanced DRAM: NZO stability | https://doi.org/10.1117/12.3107535
- 10.1117/12.3090253 | NZO improvement on DRAM by recipe optimization | https://doi.org/10.1117/12.3090253
- 10.1117/12.3089098 | Scan fingerprint characteristics ... DRAM structure properties | https://doi.org/10.1117/12.3089098
- 10.1117/12.3090488 | DRAM process overlay control via time-series ML (no abstract) | https://doi.org/10.1117/12.3090488
- 10.1117/12.3053227 | Dual-camera imaging overlay metrology (latest DRAM devices) | https://doi.org/10.1117/12.3053227
- 10.1117/12.3090223 | Robust AEI sampling strategy (Peri-Array boundary) | https://doi.org/10.1117/12.3090223
- 10.1117/12.3051267 | Full-wafer 3D metrology based on imaging ellipsometry (DRAM cell blocks) | https://doi.org/10.1117/12.3051267
- 10.1117/12.3050684 | Nondestructive in-cell conductivity metrology for memory using near-field THz ("integrated ... in a memory production line") | https://doi.org/10.1117/12.3050684
- 10.1117/12.3052524 | 3D-DRAM Si/SiGe superlattices: inspection strategies | https://doi.org/10.1117/12.3052524
- 10.1117/12.3051646 | Image quality measurement ... in-line CDSEM (DRAM layers) | https://doi.org/10.1117/12.3051646
- 10.1117/12.3090786 | Contour-based metrology ... advanced DRAM patterning | https://doi.org/10.1117/12.3090786
- 10.1117/12.3090162 | CD extreme values ... DRAM hexagonal contact hole (EUV) | https://doi.org/10.1117/12.3090162
- 10.1117/12.3090909 | Stochastics metrology and yield in DRAM HVM | https://doi.org/10.1117/12.3090909
- 10.1117/12.3091842 | High resolution EBI for advanced DRAM word line defectivity (no abstract) | https://doi.org/10.1117/12.3091842
- 10.1117/12.3090702 | e-tilt based pattern profile metrology (DRAM SADP) | https://doi.org/10.1117/12.3090702
- 10.1117/12.3051560 | EUV process window using large-FOV eBeam metrology (DRAM device) | https://doi.org/10.1117/12.3051560
- 10.1117/12.3089713 | BSE grey level CD-SEM scumming in high-NA EUV (D0a DRAM) | https://doi.org/10.1117/12.3089713
- 10.1117/12.3050176 | OES structure prediction during etching (DRAM datasets) | https://doi.org/10.1117/12.3050176
- 10.1117/12.3051932 | Zernike-based track module matching for wafer CDU (DRAM) | https://doi.org/10.1117/12.3051932
- 10.1117/12.3090707 | Smart Zernike ... CDU control (DRAM) | https://doi.org/10.1117/12.3090707
- 10.1117/12.3093878 | Nondestructive sidewall imaging for 3D profiling of logic and memory (no abstract) | https://doi.org/10.1117/12.3093878
- 10.1117/12.3090163 | OCD simulation domains for ML-based OCD (DRAM) | https://doi.org/10.1117/12.3090163

**C. Memory, device type not named (low priority):** 10.1117/12.3051274, 10.1117/12.3051452, 10.1117/12.3048535, 10.1117/12.3051763, 10.1117/12.3090778 (URLs as https://doi.org/<DOI>).

SK hynix's own newsroom lists two joint SK hynix / Gauss Labs papers (PAPM-231); by title and author match they are MIPC XL 10.1117/12.3087531 and 10.1117/12.3089595 [I] (PAPM-232). Both are on VM, outside this module's process steps.

## 4. Premise problems
- **HANA Micron counted as Micron.** `paper_candidates.csv` tags 5 papers as "Micron" whose only Micron-like affiliation is HANA Micron Inc., a Korean OSAT unrelated to Micron Technology: ECTC 2025 00286, 00348, 00336 and ECTC 2026 00289, 00104. Two would otherwise be in scope: 00348, a bridge-die package with HBM dies and metallographic micro-bump analysis, and 00336, a micro-bump vertical wire checked by electrical test. Both are excluded.
- **Other Samsung affiliations.**
  - Samsung Display (VLSI 2026 11577439) is a separate company.
  - Samsung Research America, Samsung Semiconductor India, Samsung Semiconductor Inc. and Samsung Austin Semiconductor are Samsung Electronics units and are kept. Samsung Austin's passivation-crack paper (IRPS 2026 11499186) is foundry/logic and out of scope.
  - Samsung Electro-Mechanics (ECTC 2026 00102) is already marked out of scope.
- **Keyword-screen noise.**
  - SPIE 10.1117/12.3052652 matched "memory" only through "in memory of Ben Bunday".
  - The method flags "X-ray CT" for VLSI 2026 papers matched the letters "CT". No abstract from the three companies actually names X-ray.
- **Conflicting access rules for SPIE.** The common brief lists spiedigitallibrary.org as accepting scripted access, but the module prompt says it refuses. I followed the module prompt and did not test either way.
- **SPIE dates.** Crossref gives publication dates of 24 Apr 2025 (XXXIX) and 8 Apr 2026 (XL). The conferences were held in Feb 2025 and Feb 2026. The table uses the Crossref date, and `period_calendar` uses the conference month.
- **VLSI 2025 has no abstracts.** VLSI 2025 DOIs carry the 10.23919 prefix. The publisher elided the abstracts in Semantic Scholar, and Crossref has none, so all 35 VLSI 2025 papers from the three companies lack abstracts.
- **Vendor-led co-authorship weakens the "chipmaker statement" reading.**
  - ISTFA 2026 p0474 (Samsung HBM2 PFIB) lists 5 ThermoFisher affiliations and 1 Samsung.
  - ECTC 2025 00350 (SK hynix bond wave) has Yokohama National University first and last authors, 4 of 10 SK hynix authors and 3 Tokyo Electron co-authors.
  - ISTFA 2025 p0244 (Micron AAT) and p0563 (Samsung OBIRCH) have Thermo Fisher and Hamamatsu co-authors respectively; p0495 (Samsung VTR) has 1 Hamamatsu co-author of 9; ISTFA 2026 p0749 (Samsung iFAST) has 3 ThermoFisher co-authors of 9.
  - ECTC 2026 00250 (Samsung leakage) is Seoul National University-led (3 of 7 Samsung); IRPS 2026 11499353 (ZrO2 mapping) has 2 of 7 Samsung authors; JSTS 25.6.623 is an SKKU degree-programme paper with a Samsung engineer as first author.
- **The JSTS warpage paper, as described by the coordinator / TALK module.**
  - Correction: the "transferred to measurement equipment suppliers" sentence is in the Introduction (PAPM-202). The abstract instead says the work was "implemented into measurement equipment and developed into a commercialized solution currently in use" (PAPM-201). Both are company claims [C].
  - The Crossref title truncates "UV-Induced" to "UV-In".
  - The Crossref and Semantic Scholar records carry no affiliation or abstract. The SK hynix affiliation comes from the jsts.org article page (PAPM-198).
- **JSTS is a journal, not a conference.** It was added at the coordinator's request.

## 5. Gaps
- Full texts of the 35 IEEE papers (34 with prefix 10.1109, 1 with 10.23919) in the table and evidence: NOT RETRIEVED (tried: none, per brief; ieeexplore.ieee.org returns a 202 bot challenge). URLs are in each row's `url` column.
- Full texts of the 10 ISTFA papers: NOT RETRIEVED (tried: Semantic Scholar and Crossref records only; dl.asminternational.org not tried).
- Full texts and affiliations of the SPIE MIPC XXXIX/XL papers: NOT RETRIEVED (tried: Crossref volume listings and Semantic Scholar batch; spie.org / spiedigitallibrary.org refuse scripted access).
- Abstracts of Micron "High Bandwidth Memory for AI" (VLSI 2025) and SK hynix "Metal interconnection of high bandwidth memory in wafer level packaging" (IITC 2025): NOT RETRIEVED (tried: Semantic Scholar batch record, where the abstract is elided or null; Crossref volume listing, which has no abstract).
- X-ray CT / laminography / 2D X-ray for HBM, TSV or bonding in SK hynix, Samsung or Micron abstracts: NOT DISCLOSED (read: 2026-11-21_semanticscholar_chipmaker-papers-2025-26-part1.json and -part2.json, abstracts of all 264 three-company papers that have one).
- AFM for pre-bond Cu recess or dishing in the three companies' abstracts: NOT DISCLOSED (read: same files, abstracts). The Samsung wet-ALE paper targets nm-level Cu recess, but its abstract names no measurement.
- Infrared inspection of bonded interfaces or bond overlay in the three companies' conference abstracts: NOT DISCLOSED (read: same files, abstracts). The conference mention of IR is Samsung's statement that IR OBIRCH/photoemission reach their limits in V-NAND FA (PAPM-086). IR for post-bond die shift/tilt does appear in SK hynix's JSTS 2025 paper (PAPM-213).
- Supplier of SK hynix's commercialized in-line chip-warpage solution: NOT DISCLOSED (read: 2026-11-21_jsts_paper-hbm-chip-warpage-thin-wafer.html, full text).
- Supplier or wavelength of the IR die-shift tool in SK hynix's JSTS paper: NOT DISCLOSED (read: 2025-10-31_jsts_paper-hbm-stacked-die-ir-metrology-cv.html, full text).
- Affiliations in Crossref for JSTS 2025-26 records: NOT DISCLOSED (read: 2026-11-21_crossref_cr-jsts-2025-25-5-585-skhynix-hbm-warpage.json and 2026-11-21_crossref_search-jsts-2025-26-affiliation.json, author records; the affiliation query returned 0 results).
- Die-warpage measurement method in SK hynix HBM4: NOT DISCLOSED (read: 2026-11-21_semanticscholar_chipmaker-papers-2025-26-part2.json, abstract of 10.1109/vlsitechnologyandcir65830.2026.11577576).
- Bond-overlay metrology in Samsung CMB V-NAND: NOT DISCLOSED (read: 2026-11-21_semanticscholar_chipmaker-papers-2025-26-part2.json, abstract of 10.1109/vlsitechnologyandcir65830.2026.11577637).
- Tool maker for any HBM / hybrid-bonding measurement by the three companies: NOT DISCLOSED (read: same files, abstracts, and the three SK hynix JSTS full texts). The vendor links are:
  - FA tools (Thermo Fisher, Hamamatsu);
  - TEL as a co-author of the bond-wave paper;
  - Akrometrix AXP, used only as the destructive reference in the warpage paper (PAPM-204).
- Status (pilot, HVM, in-line) for 21 of 45 table rows: NOT DISCLOSED (read: abstracts as cited in `PAPM_table.csv`).
- Affiliations of all SPIE MIPC XXXIX/XL records: NOT DISCLOSED (read: 2026-11-21_crossref_SPIE-MIPC-XXXIX-2025-volume-list.json and -XL-2026-volume-list.json, author records).

## 6. Leads for the other modules
**X-ray dose / radiation or beam damage.** No X-ray dose statement by the three companies was found. Related statements:
- Micron TID threshold for terrestrial radiation "inconsequential" (PAPM-045);
- Micron "low-dose TEM imaging" and beam-interaction distortion of photoresist (PAPM-029, PAPM-030);
- Samsung SEM-chamber contamination from CD/review SEM (PAPM-112, PAPM-113);
- Samsung conventional L4 electrical screen "often damages weak dies" (PAPM-077).
- Unattributed SPIE: 10.1117/12.3090552 (photocathode SEM "distributes electron dose") and 10.1117/12.3090618 (nano-CT vs laminography resolution/throughput for an HBM stack).

**Sampling, 100% inspection, virtual metrology.**
- Samsung DRAM development measures "only about 4% of the products" (PAPM-099).
- Micron VM in an HVM memory fab (PAPM-042, PAPM-043).
- Micron-named ASML CGI dynamic e-beam sampling (PAPM-175, PAPM-176, PAPM-177).
- "1β DRAM" EBI 1.99% in-die coverage (PAPM-180).
- Samsung-attributed MMT "near-zero site coverage" (PAPM-194) and OES-based hole-profile prediction (PAPM-183).
- Samsung DRAM in-fab metrology anomaly detection (PAPM-133).
- SK hynix Panoptes VM since 2022 [C] (PAPM-197).
- Samsung GIDL "real-time monitoring" [C] (PAPM-071).
- Unattributed SPIE: 10.1117/12.3051267 ("impossible to achieve full coverage measurement with existing measurement technologies"); 10.1117/12.3090223 (AEI sampling).
- SK hynix measures the warpage of "all chips" on a wafer in about 7-10 min, replacing destructive sampling (PAPM-206, PAPM-208).
- No other 100%-inspection statement by the three companies was found.

**Tool vendors.**
- Thermo Fisher: Micron AAT (PAPM-034, PAPM-036), Samsung HBM2 PFIB (PAPM-094, PAPM-095), Samsung iFAST (PAPM-090), Micron-named "Wafer DualBeam" (PAPM-166).
- Hamamatsu: Samsung OBIRCH (PAPM-081); Samsung VTR co-author (PAPM-085).
- Tokyo Electron: SK hynix bond wave (PAPM-144).
- ASML: Micron-named MBI and CGI (PAPM-172, PAPM-176).
- Gauss Labs: SK hynix VM [C] (PAPM-197, PAPM-231).
- Hitachi High-Tech: 191 IS4100 patterned-wafer inspectors in a Samsung DRAM HVM line (PAPM-225).
- Akrometrix: AXP used as the destructive warpage reference by SK hynix (PAPM-204).
- Unnamed "measurement equipment suppliers" commercialized SK hynix's chip-warpage method (PAPM-202). The paper also mentions an unnamed "certain equipment supplier" of vertical-hold wafer warpage systems.
- SPIE vendor products in unattributed papers: TEL bonder (10.1117/12.3088567), ASML YieldStar (10.1117/12.3054121, 10.1117/12.3051685), "Axion" X-ray CD (10.1117/12.3090197, 10.1117/12.3090205), Lam "ATR80" test device (10.1117/12.3051616), Thermo Fisher Helios (10.1117/12.3051519).

## 7. Unverified leads and adjacent papers (no row)
- **SK hynix, ECTC 2026, "FEA-Integrated 3PB And BOR Testing For Fracture Strength Characterization Of Ultra-thin Dies".** It uses SEM fractography of thin dies, but its abstract does not tie this to HBM, so it is out of scope. https://doi.org/10.1109/ectc51846.2026.00267
- **Samsung, ECTC 2026, "In-Situ Cure Monitoring of EMC by Fiber Bragg Grating and Dielectric Sensors ... for Accurate Warpage Prediction".** This is package warpage, not stacking. https://doi.org/10.1109/ectc51846.2026.00068
- **Samsung, ECTC 2025, "VCS (Vertical Copper Post Stack)" and ECTC 2026 multi-stacked FOWLP Cu post.** Memory stacking without TSV. Warpage is mentioned, but no method is named. https://doi.org/10.1109/ectc51687.2025.00354 and https://doi.org/10.1109/ectc51846.2026.00009
- **Samsung, ECTC 2026, "Novel Microbump Structure ... (SoSBF)".** HBM micro-bump with a 1.0 um joint gap; no inspection method is named. https://doi.org/10.1109/ectc51846.2026.00326
- **Samsung, VLSI 2026, "Vertically Stacked Dram Technology for Scaling Evolution".** The peri wafer is bonded to the cell wafer; no metrology is named. https://doi.org/10.1109/vlsitechnologyandcir65830.2026.11577221
- **Samsung, IEDM 2025, 2-layer CIS with hybrid Cu-Cu bonding.** An image sensor, not memory; no method is named. https://doi.org/10.1109/iedm50572.2025.11353616
- **Other 2025-26 JSTS hits from the Crossref topic query** (`2026-11-21_crossref_search-jsts-2025-26-topic.json`, 11 results). Affiliations below come from search snippets only and are not verified:
  - "Real-time TSV 3D Shape Defect Inspection System Using Deep Learning based Fast Object Detection": Kumoh National Institute of Technology per snippet, not a chipmaker. https://doi.org/10.5573/JSTS.2025.25.6.645
  - "High-precision Resistance Modeling for 3D Hybrid Bonding with Contact Resistance Integration": Seoul National University of Science & Technology per snippet. https://doi.org/10.5573/JSTS.2025.25.5.556
  - "Characteristics of PVD SiCN for Application in Hybrid Cu Bonding": SeoulTech per snippet. https://doi.org/10.5573/JSTS.2025.25.1.102
  - Affiliation not checked, and the topics are thermal or design: https://doi.org/10.5573/jsts.2026.26.2.97 (heat dissipation in high-stacked HBM) and https://doi.org/10.5573/jsts.2026.26.4.292 (voltage control in hybrid-bonding 3D NAND).
- **Samsung, J. Micro/Nanopatterning (JM3) 2025, "massive metrology ... HB VNAND".** A journal paper, not a conference paper. Its record is saved by another module (`2025-09-12_semanticscholar_s2-jmm-041405-samsung-massive-metrology-hb-vnand`), and it is worth cross-checking against the V-NAND bonding rows here.

## Corrections after verification (2026-11-21)
- Rows corrected after an independent two-stage quote check: PAPM-017, PAPM-027, PAPM-036, PAPM-051, PAPM-054, PAPM-071, PAPM-073, PAPM-076, PAPM-085, PAPM-089, PAPM-090, PAPM-094, PAPM-110, PAPM-143, PAPM-151, PAPM-185, PAPM-190, PAPM-197, PAPM-199, PAPM-205, PAPM-207, PAPM-210, PAPM-211, PAPM-215, PAPM-220, PAPM-222, PAPM-223, PAPM-228.
- Follow-on note edits: PAPM-095, PAPM-096 (vendor-led paper), PAPM-212 to PAPM-216 (no Semantic Scholar record saved).
- Retagged [F] to [C] (in-use or state-of-the-art claims): PAPM-036, PAPM-110, PAPM-197, PAPM-199, PAPM-222.
- New rows: PAPM-230 [C] (turnaround claim split from PAPM-071), PAPM-231 [F] (newsroom paper list), PAPM-232 [I] (newsroom papers matched to SPIE DOIs).
- `PAPM_table.csv`: co-authorship qualifiers added to the chipmaker column for vendor-, university- or jointly-led papers; [C] noted in the status column for PAPM-036, PAPM-110 and PAPM-222; wording aligned for PAPM-027, PAPM-054, PAPM-185, PAPM-190, PAPM-207, PAPM-215 and PAPM-228. Table counts in section 1.4 are unchanged.
