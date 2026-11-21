# PAPL notes: conference-paper evidence for TSMC, Intel, ASE (incl. SPIL), Amkor (Jan 2025 - 21 Nov 2026)

Files: `PAPL_table.csv` (41 rows, 26 papers), `PAPL.csv` (188 evidence rows, quote_check: FOUND 188 / NOT FOUND 0).
Every [F] row rests on the paper's abstract (Semantic Scholar record) or its Crossref record. **No full text was read.** IEEE papers: full text NOT RETRIEVED (ieeexplore.ieee.org bot challenge, per the access rules). ISTFA papers: full text NOT RETRIEVED (fetch.py gets HTTP 403 from dl.asminternational.org, tested 2026-11-21, manifest row for istfa2026p0194).

## How the set was built
- I read the titles of all 254 candidate rows for my companies (Intel 115, TSMC 97, ASE/SPIL 37, Amkor 4, Intel+SPIL 1). I read the abstracts of every packaging, FA or test paper among them (about 140). The 26 VLSI 2025 TSMC/Intel papers have no saved abstract. All their titles are device or circuit topics.
- I also re-scanned all Crossref volume listings with a looser affiliation pattern. That found 3 TSMC ECTC 2025 papers and 1 Intel IRPS 2025 paper that `paper_candidates.csv` misses (see Premise problems). I fetched S2 single records for the 3 TSMC papers and the Amkor IITC paper: `research/sources/customer_side/2026-11-21_semanticscholar_s2-*.json`. One of the 3 TSMC papers is in scope (PAPL-017).
- In table: TSMC 6 papers, Intel 14, ASE 6 (3 of them university-led with ASE co-authors), Amkor 0. A paper co-authored by Intel and SPIL (PAPL-155) is mine. It is out of scope because it inspects nothing.

## Findings by company

### TSMC: mostly electrical test, no inspection method named for SoIC or CoWoS HBM stacks
- SoIC-CS (logic base die with multilayered memory top dies): integration yield shown "on daisy chains" (PAPL-010, PAPL-011). Status: "proven feasible for the first time in this study" (PAPL-012). TSMC claims SoIC-CS can support 8/12/16-hi HBM on a logic base ([C] PAPL-013).
- CoWoS-R with 4 SoC + 12 HBM: RDL/via interconnects tested by via-chain continuity, comb/meander Rs and leakage current (PAPL-006, PAPL-007). The platform is "currently in production" ([C] PAPL-008). The warpage paper reports "good in-line yields" and "good process control in fine pitch ubump joining" but names no measurement method (PAPL-135, [C] PAPL-136).
- Micro-bumps: electromigration tests of Cu/Sn and Cu/Ni/Sn/Cu full-IMC micro-bumps (PAPL-018 to PAPL-020). The IRPS 2026 CoWoS EM paper covers RDL, TSV, micro-bump and C4 tiers but names no test method (PAPL-149, PAPL-150).
- Multi-die test: UCIe-based interconnect, logic and memory test and repair on N3P + CoWoS-S silicon test vehicles. The paper is co-authored with Synopsys (PAPL-022 to PAPL-024).
- Mechanical: double-cantilever and nano-indentation tests for CoWoS interface robustness (PAPL-015). This is borderline scope.
- Wafer-bonded interface: "IR imaging" for bonding quality (PAPL-002). The paper is university-led (NYCU/TSRI) with 2 TSMC Corporate Research co-authors (PAPL-001).
- No TSMC paper in the set names X-ray, acoustic, AFM, e-beam or overlay metrology for SoIC, CoWoS or HBM. Only 3 ECTC 2026 papers carry a TSMC Crossref affiliation, and none of them is about inspection.

### Intel: the most method-specific of the four
- **Bond overlay.** Near-infrared post-bond chiplet-level overlay mapping on a fiducial-grid test vehicle (PAPL-046). Chiplet distortion is "one of the biggest contributors" to post-bond overlay error (PAPL-047). Bonders are at "their accuracy limits" below 3 um pitch (PAPL-049).
- **100% C2W overlay metrology.** Images are taken "on the move" at alignment keys, "with 100% chiplet inspection" (PAPL-055, PAPL-056). The paper describes this as development "at Intel" with a roadmap (PAPL-059). It has an EV Group co-author (PAPL-061). The imaging wavelength is not stated in the abstract.
- **Post-bond voids.** C2W hybrid bonding, Intel with Applied Materials co-authors. cSAM showed "no significant void formation" (PAPL-035). 10k-via daisy chain <1 kOhm with >90% yield; device yield >99% (PAPL-033, PAPL-034). FIB-SEM on Kelvin structures found interconnect gaps (PAPL-036). EDX found etch residues (PAPL-037).
- **Electrical test of hybrid-bonded and TSV structures.**
  - Multi-level bond vias: tight resistance distribution (PAPL-026).
  - Fluidic self-alignment: interfacial resistance not increased, "preliminary readouts" (PAPL-029, PAPL-030).
  - EMIB-T for HBM4E: "wideband electrical measurements" (PAPL-064).
  - Fusion-bonded 9-wafer via-in-one TSV DRAM cube: TSV and contact-ring resistance tests (PAPL-094 to PAPL-097). This paper is SAIMEMORY-led with Intel, PSMC and AP Memory co-authors.
- **Bond-interface thermal metrology.** Thermoreflectance on a W2W fusion-bond layer, done on "a commercial fusion bonder" whose maker is not named (PAPL-041, PAPL-043). FDTR on hybrid-bond interfaces, with a Fouriers Scientific co-author (PAPL-051, PAPL-053).
- **Micro-bump joints and alignment.** 3D X-ray CT verifies joint quality and alignment (PAPL-067). Low-kV SEM-EDX measures Cu surface oxygen (PAPL-069). Both are from a CPO die-to-die TCB paper, still research ("a step towards that goal", PAPL-071).
- **Pre-bond Cu.** AFM and nanoindentation of HB-ready Cu pads (PAPL-073 to PAPL-075). The paper is NIST-led with an Intel co-author. The ULT-HB paper evaluates Cu pad recess but names no method (PAPL-138).
- **FA on 3D stacks.**
  - SIL thermal imaging after thermal flattening of warped Foveros samples (PAPL-078 to PAPL-080).
  - Synchrotron X-ray-assisted device alteration (XADA) on the base die of a mock stacked die (PAPL-082, PAPL-083).
  - RF-modulated lock-in thermography for 2.5/3D packages including HBM accelerators (PAPL-089 to PAPL-091).
- **Status words.** "test vehicle", "pathfinding test vehicles" (PAPL-144), "preliminary readouts", "feasibility", "development ... roadmap". The only manufacturing phrase is the [C] "high-volume manufacturing environment" for mid-BEOL hybrid bonding (PAPL-152).

### ASE (incl. SPIL): FA of HBM-bearing fan-out packages, plus university hybrid-bonding work
- **FOCoS-B (silicon bridges between ASIC and HBM), micro-bump FA.** The flow is O/S testing and I/V curve tracing (PAPL-106), then 3D X-ray microscopy with AI reconstruction (PAPL-107), then SEM/EDS (PAPL-108). Samples are lapped to about 10 um before XRM (PAPL-109). ASE claims shorter PFA cycle time ([C] PAPL-110) and a yield gain from the flux-clean fix ([C] PAPL-111).
- **FOCoS RDL between ASIC and HBM.** The conventional flow is O/S plus 3D X-ray microscopy (PAPL-100). ASE states two limits: limited X-ray field of view (PAPL-101) and slow FIB (PAPL-102). RDL defects are "a major contributor to yield loss in FOCoS packages" (PAPL-103).
- **Hybrid bonding (NTU-led, ASE Corporate R&D co-authors).**
  - AFM of pre-bond Ag roughness (PAPL-113) and of Cu-protrusion/PI-recess topography (PAPL-119).
  - EDS deposition selectivity (PAPL-114).
  - SEM/TEM bonded interface (PAPL-115).
  - FIB cross-sections (PAPL-120, PAPL-123).
  - Electrical yield (PAPL-116).
- **Mitsui Chemicals-led Cu/polymer hybrid bond.** 2,409-electrode daisy chain (PAPL-127).
- **ASE's own CoW hybrid-bonding void paper** reports yield rising "from 2.8% to 99%" but names no void-detection method (PAPL-131 to PAPL-133).
- **SPIL FOEB-T.** Wafer warpage affects die-to-wafer bonding accuracy and is "measured at each major step" (PAPL-146, PAPL-147). No method is named.

### Amkor: nothing in scope
- Four Amkor papers are in the set, and none inspects HBM, hybrid bonds, TSVs or micro-bumps.
  - Shadow moire on lidded FCBGA, adjacent (PAPL-181).
  - Lightmatter-led CoW 3D photonic engine, with a BER test only (PAPL-183, PAPL-184).
  - Glass-core FCBGA warpage, no method named.
  - IITC 2025 overview, which has no abstract.

## Full texts the user should save by hand (priority order)
1. Intel, ECTC 2026, 100% C2W bond overlay (EV Group co-author): https://doi.org/10.1109/ECTC51846.2026.00354
2. Intel, ECTC 2026, chiplet distortion / NIR overlay: https://doi.org/10.1109/ECTC51846.2026.00030
3. ASE, ECTC 2026, CoW hybrid-bonding voids (detection method missing from abstract): https://doi.org/10.1109/ECTC51846.2026.00059
4. Intel + Applied Materials, ECTC 2025, CMP for hybrid bonding (cSAM, daisy chain, FIB-SEM): https://doi.org/10.1109/ECTC51687.2025.00313
5. TSMC, ECTC 2025, SoIC Cool-Stacking (daisy chains; memory-on-logic): https://doi.org/10.1109/ECTC51687.2025.00055
6. TSMC, ECTC 2025, CoWoS-R warpage, 12 HBM ("in-line yields"; method missing): https://doi.org/10.1109/ECTC51687.2025.00026
7. ASE, ECTC 2026, FOCoS-B micro-bump 3D XRM workflow: https://doi.org/10.1109/ECTC51846.2026.00245
8. ASE, ECTC 2026, FOCoS ASIC-HBM RDL fault localization: https://doi.org/10.1109/ECTC51846.2026.00249
9. Intel, ISTFA 2026, stacked-die debug at a synchrotron (X-ray flux/dose): https://doi.org/10.31399/asm.cp.istfa2026p0194
10. Intel, ISTFA 2026, RF lock-in thermography for 2.5/3D and HBM packages: https://doi.org/10.31399/asm.cp.istfa2026p0419
11. Intel, ECTC 2026, ultra-low-temperature hybrid bonding (Cu pad recess; method missing): https://doi.org/10.1109/ECTC51846.2026.00224
12. TSMC, ECTC 2025, CoWoS-R 1.4/1.4 um RDL with 12 HBM: https://doi.org/10.1109/ECTC51687.2025.00047
13. Intel, ECTC 2026, CPO die-to-die TCB (3D X-ray CT, SEM-EDX): https://doi.org/10.1109/ECTC51846.2026.00325
14. Intel, IRPS 2026, EMIB-T (TSV) quality and reliability: https://doi.org/10.1109/IRPS61424.2026.11499343
15. Intel et al., VLSI 2026, fusion-bonded via-in-one TSV DRAM cube: https://doi.org/10.1109/VLSITechnologyandCir65830.2026.11577374

## Adjacent list (package inspection or FA, but not stacked/HBM; not in the table)
- ASE ISTFA 2025: AI enhancement of SAM images for flip-chip ELK cracks. Cuts SAM scan time; PVA TePla co-author (PAPL-158 to PAPL-162).
- ASE ECTC 2025: FOCoS fine-line RDL FA with LIT, 3D X-ray and FIB. HBM not stated (PAPL-177 to PAPL-179).
- ASE EPTC 2025: SAT on Al2O3 DBC substrates (power module), 10.1109/EPTC67330.2025.11392306.
- ASE EPTC 2025: shadow moire and X-ray on DSC power modules, 10.1109/EPTC67330.2025.11392279.
- ASE ECTC 2025: stud-pull vs DCB for Cu-polymer adhesion in fan-out, 10.1109/ECTC51687.2025.00240.
- ASE ICEP-IAAC 2025 "The Effect of Key Factors on 3D X-Ray Imaging for Fan-Out Package" (title only; Crossref record saved by another module, no abstract): 10.23919/ICEP-IAAC64884.2025.11003029.
- Amkor EPTC 2025: shadow moire on lidded FCBGA with indium TIM (PAPL-180, PAPL-181).
- Amkor ECTC 2026: Lightmatter Passage M CoW 3D photonic engine, BER test only (PAPL-182 to PAPL-184).
- Intel ISTFA 2026: X-ray CT de-warping on FCPGA packages with Dragonfly software; Comet Technologies co-authors; "adequate voxel resolution" (PAPL-163 to PAPL-167).
- Intel ISTFA 2026: quantum-diamond magnetic imaging vs LIT on 2.5D chiplet devices. MIT Lincoln Lab-led (PAPL-185, PAPL-186).
- Intel ISTFA 2025: LIT depth localization. Fraunhofer IMWS-led; 3D use only "potential" (PAPL-187, PAPL-188).
- Intel IPFA 2025: deep-learning defect detection of package physical components, "tailored for HVM" (PAPL-171 to PAPL-173).
- Intel ISTFA 2026: microwave plasma deprocessing for package FA (sample preparation), 10.31399/asm.cp.istfa2026p0669.
- TSMC IRPS 2025: EM of flip-chip Cu bumps (OSP/ENEPIG), 10.1109/IRPS48204.2025.10982917.
- TSMC ECTC 2025 / 2026: helium leak tests of direct-to-silicon cooling on CoWoS-R, 10.1109/ECTC51687.2025.00131 and 10.1109/ECTC51846.2026.00092. Not stack inspection.
- TSMC ECTC 2026: CoWoS-R board-level reliability (AXP DIC), 10.1109/ECTC51846.2026.00274.

## In topic, but the abstract names no method (not in table; evidence rows kept)
- ASE CoW hybrid-bond voids: PAPL-130 to PAPL-133.
- TSMC CoWoS-R warpage: PAPL-134 to PAPL-136.
- Intel ULT-HB Cu recess: PAPL-137, PAPL-138.
- Intel IR-debond carrier bow, 48% lower: PAPL-139, PAPL-140.
- Intel selective layer transfer bonding distortion: PAPL-141, PAPL-142.
- Intel EMIB-T Q&R: PAPL-143, PAPL-144.
- SPIL FOEB-T wafer warpage: PAPL-145 to PAPL-147.
- TSMC CoWoS EM: PAPL-148 to PAPL-150.
- Intel mid-BEOL hybrid bonding: PAPL-151, PAPL-152.
- Intel 4X-reticle fluxless TCB with HBM: PAPL-153, PAPL-154.
- Intel + SPIL SRAM chiplet on 25 um micro-bumps: PAPL-155 to PAPL-157.
- Also read; no method and no rows: TSMC SoW-X (10.1109/ECTC51687.2025.00005), Intel EMIB-T (10.1109/ECTC51687.2025.00051 and 10.1109/ECTC51846.2026.00051), Intel TCB with HBM (10.1109/ECTC51687.2025.00312), ASE FOCoS-B with TSV and HBM3 (10.1109/ECTC51687.2025.00158).

## Premise problems
1. `paper_candidates.csv` under-counts TSMC and Intel.
   - Its TSMC pattern needs "Taiwan Semiconductor Manufacturing", so it misses Crossref strings like "Taiwan Semiconductor, Manufacturing Company". That drops 10.1109/ECTC51687.2025.00131, .00036 and .00198. The last one is in scope (PAPL-017).
   - Its Intel pattern is case-sensitive, so it misses "INTEL Client Computing Group" (10.1109/IRPS48204.2025.10982850). That paper is out of scope.
2. The "companies" column marks any paper with one co-author from a chipmaker. Several of my in-table papers are led by universities, labs or suppliers: NYCU/TSRI (PAPL-001), NTU (PAPL-112, PAPL-118, PAPL-122), Mitsui Chemicals (PAPL-126), NIST (PAPL-072), SAIMEMORY (PAPL-093). They are chipmaker co-authored, not chipmaker-led.
3. `abstract_screen.csv` "methods" is noisier than "AI matches anywhere". Its AFM class also matches "recess", "topograph", "dishing" and "surface roughness". For example, ECTC 2026 00224 is flagged AFM but its abstract never says AFM (PAPL-138).
4. The Intel "100% Bond Overlay Measurement" paper exists as stated. Its full title is "Advanced Metrology for Heterogeneous Chiplet Integration with High-Speed 100% Bond Overlay Measurement". It is co-authored with EV Group (PAPL-061), so it is partly vendor material.
5. The ISTFA host test confirms the brief: DOIs redirect to dl.asminternational.org, which refuses fetch.py (HTTP 403).
6. The Crossref IPFA 2026 and IITC 2026 listings contain 0 items, so those 2026 volumes are not covered.

## Gaps
- ISTFA full texts. NOT RETRIEVED (tried: fetch.py https://doi.org/10.31399/asm.cp.istfa2026p0194 -> https://dl.asminternational.org/istfa/proceedings/ISTFA2026/85458/194/35954, HTTP 403, 2026-11-21). Same host for istfa2026p0419, p0587, p0424 and istfa2025p0011, p0482.
- IEEE full texts (all ECTC, IRPS, ITC, IPFA, VLSI, EPTC, ASMC papers above). NOT RETRIEVED (tried: none; ieeexplore.ieee.org bot challenge per access rules). URLs are in the save-by-hand list.
- Amkor IITC 2025 "Advanced Interconnection Technology Overview" abstract. NOT RETRIEVED (tried: api.semanticscholar.org DOI:10.1109/IITC66087.2025.11075360, abstract null; Crossref listing has no abstract).
- Abstracts of 26 TSMC/Intel VLSI 2025 papers. NOT RETRIEVED (tried: saved S2 batch, abstract null). All titles are device or circuit topics.
- IPFA 2026 and IITC 2026 papers. NOT RETRIEVED (tried: saved Crossref volume listings, 0 items).
- Void-detection method in ASE CoW hybrid-bonding void paper. NOT DISCLOSED (read: research/sources/customer_side/2026-11-21_semanticscholar_chipmaker-papers-2025-26-part1.json, abstract of 10.1109/ECTC51846.2026.00059).
- Imaging wavelength, tool, repeatability and throughput values of Intel 100% overlay metrology. NOT DISCLOSED (read: same part1 file, abstract of 10.1109/ECTC51846.2026.00354).
- NIR overlay tool maker and overlay accuracy numbers. NOT DISCLOSED (read: same part1 file, abstract of 10.1109/ECTC51846.2026.00030).
- Warpage and in-line inspection methods for large CoWoS-R. NOT DISCLOSED (read: same part1 file, abstract of 10.1109/ECTC51687.2025.00026).
- Cu pad recess measurement method. NOT DISCLOSED (read: same part1 file, abstract of 10.1109/ECTC51846.2026.00224).
- Wafer warpage measurement method, FOEB-T. NOT DISCLOSED (read: same part1 file, abstract of 10.1109/EPTC67330.2025.11392617).
- Makers of the cSAM, FIB-SEM and 3D XRM tools used by Intel and ASE. NOT DISCLOSED (read: same part1 file, abstracts of 10.1109/ECTC51687.2025.00313, 10.1109/ECTC51846.2026.00245, 10.1109/ECTC51846.2026.00249).
- Production or HVM status of any inspection method in the table. NOT DISCLOSED (read: abstracts of all 26 in-table papers, same part1/part2 files). The only production words concern the CoWoS-R platform ([C] PAPL-008, PAPL-136), not an inspection step.

## Leads for other modules (listed, not pursued)
- **X-ray dose / radiation and X-ray limits**
  - Intel synchrotron XADA: circuit "response scales with flux density and exposure time" (PAPL-086). Lab-source brightness limits throughput (PAPL-084).
  - ASE: 3D X-ray FOV limit (PAPL-101); lapping to about 10 um before XRM (PAPL-109).
  - Intel CT: voxel resolution (PAPL-166).
  - TSMC ISTFA 2025 e-beam probing of A16 notes "contamination buildup due to prolonged e-beam exposure" (die-level; abstract in the part1 file; 10.31399/asm.cp.istfa2025p0527).
- **Sampling, 100% inspection, virtual metrology and AI**
  - Intel 100% C2W overlay vs "reduced sampling plans" (PAPL-055 to PAPL-062).
  - ASE AI-enhanced SAM "decreases significantly SAM scanning time" (PAPL-160).
  - Intel DL package inspection for HVM (PAPL-172, PAPL-173).
  - Intel e-beam point scan, 1 billion hot spots/hour (PAPL-175).
  - Intel AI warpage model, <1% of physical time-to-data (PAPL-169).
  - Also: ASE GA-NN warpage prediction (10.1109/ECTC51687.2025.00274), Intel production-scale CP-stage ML binning (10.1109/ITC64303.2026.00008), Intel HVM cell-aware diagnostics (10.1109/ITC58126.2025.00046).
- **Tool vendors as co-authors or named**
  - EV Group (Intel overlay, PAPL-061)
  - Applied Materials (Intel CMP/HB, PAPL-038)
  - Fouriers Scientific (Intel FDTR, PAPL-053)
  - PVA TePla Analytical Systems (ASE SAM, PAPL-161)
  - Comet Technologies / Dragonfly (Intel CT, PAPL-164, PAPL-167)
  - Synopsys (TSMC UCIe test, PAPL-024)
  - Siemens EDA (Intel multi-die test, 10.1109/ITC64303.2026.00097)
  - "a commercial fusion bonder", maker not named (Intel W2W, PAPL-043)
