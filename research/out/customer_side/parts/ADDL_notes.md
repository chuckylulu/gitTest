# ADDL notes: gap-fill for TSMC, Intel, ASE and Amkor (critic list, 11 candidates; run 2026-11-21)

Files: `ADDL.csv` (58 evidence rows: 37 [F], 20 [C], 0 [S], 1 [I]; all 58 quotes FOUND by `quote_check.py`), `ADDL_table.csv` (13 method rows, 10 documents).
Every document was fetched with `research/tools/fetch.py` and saved under `research/sources/customer_side/`. Period: 1 Jan 2025 to 21 Nov 2026. All added documents fall inside it. The Intel patent was filed in Jun 2023 but published on 2 Jan 2025, which is in period. The W07_01 deck describes Foveros production "since 2019" as history inside a June 2026 document.
Added 9 of 11 candidates. The other 2 are NOT RETRIEVED because their hosts refused fetch.py (see sections 2 and 4).
None of the added items describes an HBM-stack or hybrid-bond inspection in production. The closest items are:
- Intel's micro-bump sort (electrical test) on Foveros and EMIB;
- TSMC's test-insertion flow for CoWoS and SoIC, which names the HBM base die as a test target;
- Intel's patent on IR bond-overlay fiducials.

## 1. Findings

### 1.1 Intel
- **Micro-bump probing in HVM (SWTest 2026, deck W07_01, 8-10 Jun 2026).**
  - Authors: four Intel Foundry and two FormFactor; Intel-led (ADDL-001).
  - Production claim: Intel says it has probed micro-bumps in high-volume production on the Foveros product line since 2019 (ADDL-002). The summary table gives Foveros DOW36 (36 um min pitch) as "In Mass Production since 2019" for wafer sort and die sort (ADDL-004).
  - Volume: 25+ products at multiple sites, 300K+ wafers and 1500+ FormFactor probe heads (ADDL-005). Probe-card availability is about 90% (ADDL-006). Radial alignment is held to <=10 um "on many Foveros products in high volume" (ADDL-012).
  - EMIB:
    - Intel plans to start micro-bump probing on EMIB devices in 2026 (ADDL-003).
    - EMIB45 mixed-pitch probing is "Under development", with technology certification targeted by Q3 2026 (ADDL-007).
    - Bridge micro-bumps are 23-28 um CD at 45 um pitch (ADDL-008).
    - Intel and FormFactor are applying the Foveros experience to EMIB-T sort (ADDL-014).
    - EMIB45 test-vehicle contact resistance was within the passing limit at -10 C, 100 C and in a merged socket (ADDL-013).
  - Risks named: probe-induced defect modes and yield loss (ADDL-009). Controls against them include touchdown count, post-sort reflow to restore coplanarity, and assembly/reliability DOEs (ADDL-011).
  - Qualification plan: test-coupon materials are characterized by SEM, EDS and X-ray, and bump deformation is assessed (ADDL-010). The SEM/EDS/X-ray step characterizes probe and coupon materials, not product bumps.
  - This is the only production-status test statement found for Intel micro-bumps. It covers micro-bumps on Foveros and EMIB, not hybrid bonds and not HBM.
- **Native-pitch micro-bump probing (SWTest 2026, deck M02_01, with Technoprobe).**
  - Authors: one Intel Foundry presenter and one Technoprobe presenter (ADDL-015).
  - Intel's stated reason: yield on high-die-count packages drives a "shift-left" test strategy, so both core bumps and micro-bumps must be probed, even at native pitch below 50 um (ADDL-016).
  - Today: Foveros-S products such as Meteor Lake are probed at non-native pitch (>90 um) ([C], ADDL-017).
  - New solution: probing at 45 um native pitch with Technoprobe K Tech probes (ADDL-018).
  - Results on the test vehicle:
    - about 3000 micro-bump probes, no shorting, some partial contact (ADDL-019);
    - the bump-height difference between probed and unprobed bumps is within the assembly threshold; the instrument is not named (ADDL-020).
  - Technoprobe's own slide uses XRM (X-ray microscopy) 3D reconstruction to inspect the probe head, which is test hardware, not product (ADDL-021).
  - Status: "on track to pass criteria for high volume sort", so pre-HVM (ADDL-022, on a Technoprobe-presented slide).
  - Intel also says it is "rapidly adopting industry standard test platforms" (ADDL-023).
- **Patent US 2025/0006651 A1 (Intel; published 2 Jan 2025).**
  - Bibliographic data: ADDL-054.
  - Hybrid-bonding fiducials are used in a post-bond inspection step to measure bond overlay. The result is fed back to the bonder and fed forward to flag defective devices (ADDL-055).
  - Alignment metrology passes IR light through the silicon and ILD and works in reflective or transmissive mode (ADDL-056).
  - A metal-free zone under the fiducial is preferred because metal blocks the IR (ADDL-057).
  - HBM appears only in generic stacked-device boilerplate (ADDL-058).
  - It gives no production status. It supports the Intel IR-overlay rows PAPL-045 to PAPL-049 as a dated Intel description of how the overlay marks are built.

### 1.2 TSMC
- **TSMC test-insertion map (SWTest 2026, deck M03_02, Kenny Tang and Oscar Lee).**
  - The title slide prints no affiliation. The deck's disclaimer says all content is TSMC property (ADDL-024).
  - Distributed test flow (ADDL-025):
    - CP on SoC wafers and on SoIC top-die and bottom-die wafers gives the known-good die (KGD);
    - CPS on the SoIC stack gives the known-good stack (KGS);
    - RDL-CP runs on CoWoS-L/S/R interposers;
    - then come CoW, WLCP, an optional CoW-SDP step, oS, and AST for assembly quality.
  - The "CP Testing for Early Detection" slide shows >2, >2, ~2 and <1 weeks per stage, with cost markers rising from $ to $$$$ (ADDL-026). Its row labels are garbled Chinese in the text layer, so what the week figures measure is read only from the layout.
  - Fast stop-and-fix, read from chart labels ([C], ADDL-027): cycle time is 3.3X shorter for RDL-CP than for AST/FT, and 1.7X shorter for WLCP/SDP.
  - Test targets named: "HBM Base die" and "New media (Cu pad, uBump)" (ADDL-028).
  - Singulated-die probing capability: >800K pins and ~100 x 100 mm dies ([C], ADDL-029).
  - The deck's main subject is thermal management during probing (ADDL-030).
  - It gives no production status per insertion, no counts and no vendors. It moves TSMC's SoIC screening from nothing to a stated known-good-stack test (CPS).
- **Carrier-wafer optical metrology (IMPACT 2025, Oct 2025; all 8 authors TSMC, per Crossref; ADDL-031).**
  - Carrier wafers keep wafer warpage down in 2.5D/3D flows (ADDL-032). They must be free of bulk voids and cracks (ADDL-033).
  - The proposed Advanced Optical Metrology (AOM) measures transmittance, surface roughness and bulk defects (ADDL-034).
  - It was "successfully validated" on 12-inch transparent carriers (ADDL-035) and takes under one minute per measurement (ADDL-036).
  - Results were cross-checked against other inspection instruments, which are not named (ADDL-037).
  - Read from the abstract only. Status is validated or demonstrated, not production. It is an incoming-quality check on carrier wafers, not on bonded stacks.

### 1.3 ASE
- **AI defect detection (IMPACT 2025; all 4 authors ASE Corporate R&D, per Crossref; ADDL-038).**
  - The abstract's statement that "AI-based image inspection has been widely adopted" is general and is not said of ASE (ADDL-039).
  - Synthetic data with ~5K substrate defect images raised recall from 82.1% to 93.1% and precision from 82.2% to 93.4%, with half the real data (ADDL-040).
  - The CAD model reaches an escape rate <0.05% and false positives <1%, with ~10% uncertain cases (ADDL-041). The LAD model trains in about 5 minutes (ADDL-042).
  - Limits stated: annotation load, poor adaptability to new products, and having to maintain many models (ADDL-043).
  - Abstract only. Not HBM.
- **ASEH 2025 Sustainability Report (PDF dated 7 Sep 2026; the single test fetch of an aseglobal.com/en/pdf/ file returned 200).**
  - The 2025 development list has three items. Item (2) is "Wire-Bond Packaging: AOI integrated with high efficiency anomaly detection AI technology for complex wirebonding inspection" (ADDL-044).
  - ASE says it developed a proprietary wire-bonding AI-assisted inspection system with AI-AOI and AVI (ADDL-045). Its OOB platform cuts anomaly analysis "from days to hours" (ADDL-046).
  - The report has no HBM or hybrid-bond text.
  - Inference (ADDL-047, [I], Medium): the "high-efficiency image anomaly-detection AI" that ASE named at its June 2026 AGM (TALK-048 [S]) is most likely this wire-bond AOI item, not HBM inspection. The press article's three focus areas follow the report's three-item list, and its SiP sub-list matches item (3).

### 1.4 Amkor
- **ITC 2026 talk (Amkor's own event page).**
  - Omer Dossani, VP Global Test Services, presents "Advanced Packages, AI & Amkor: The OSAT Test Perspective" (ADDL-048).
  - Amkor's description of the talk ([C], ADDL-049): increasing production test times, multi-chiplet package challenges, and wafer- and package-level test-access constraints.
  - HBM is not named and no numbers are given. This is Amkor-hosted wording for the executive who is cited elsewhere only through trade press (SMP-039 [S]).
- **ITC 2025 talk.** Vineet Pancholi presented "Best Practices for Testing 2.5D Chiplet Package Designs" (ADDL-050). The Amkor page was already saved in this run but no row cited it.
- **Smart Manufacturing page (modified 7 Aug 2026), all [C].**
  - AI vision Automated Defect Classification cut AOI operators by 30% (ADDL-051).
  - Roadmap: expand ADC (ADDL-052).
  - FDC combined with SPC (ADDL-053).
  - Not HBM-specific.

## 2. Gaps
- NOT RETRIEVED (tried: https://pr.tsmc.com/system/files/newspdf/attachment/1e7873e182523d3351afd810dc413e0bce01ca5f/2026%20Supply%20Chain%20Management%20Forum%20Press%20Release%20%28E%29-final_wmn.pdf with fetch.py, HTTP 403; the 2025 PDF https://pr.tsmc.com/system/files/newspdf/attachment/ce3c12707f578ed01449842b2d7d4b3d1b6c1cbf/2025%20Supply%20Chain%20Management%20Forum%20Press%20Release%20%28E%29_final_wmn.pdf not tried after that refusal) - TSMC's own 2026 and 2025 supplier-award lists with English category names. AW-001 to AW-016 stay [S]. Please save both PDFs by hand.
- NOT RETRIEVED (tried: https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-11/foveros-direct-3d-tech-brief.pdf with fetch.py, HTTP 403; https://www.intel.com/content/www/us/en/foundry/packaging.htm not tried, host refuses scripted access) - Intel Foundry packaging page ("Advanced Chiplet Test", "Test Services") and the Foveros Direct 3D tech brief. gaps.md item 12 stays NOT RETRIEVED; it cannot be closed as NOT DISCLOSED from this run. Please save both by hand.
- NOT RETRIEVED (tried: none; ieeexplore.ieee.org bot challenge) - full texts of https://doi.org/10.1109/impact67645.2025.11281768 (TSMC) and https://doi.org/10.1109/impact67645.2025.11281550 (ASE).
- NOT RETRIEVED (tried: Amkor event page only) - slides or paper of the ITC 2026 talk "Advanced Packages, AI & Amkor: The OSAT Test Perspective" and of the ITC 2025 talk "Best Practices for Testing 2.5D Chiplet Package Designs".
- NOT DISCLOSED (read: 2026-06-08_swtest_tsmc-hpc-testing-ai-era-deck.pdf, pp1-28) - production status of each test insertion, production counts, tester/prober/probe-card vendors, and any HBM test or inspection method beyond the "HBM Base die" label.
- NOT DISCLOSED (read: 2026-06-08_swtest_intel-formfactor-microbump-probing-hvm-deck.pdf, pp1-16) - HBM; the X-ray technique used in materials characterization; the bump-deformation measurement method.
- NOT DISCLOSED (read: 2026-06-08_swtest_intel-technoprobe-native-pitch-microbump-probing-deck.pdf, p13) - bump-height instrument and values.
- NOT DISCLOSED (read: 2026-11-21_semanticscholar_record-10.1109-impact67645.2025.11281768.json, abstract) - optical principle, tool vendor, reference instruments, and whether AOM runs in production.
- NOT DISCLOSED (read: 2026-11-21_semanticscholar_record-10.1109-impact67645.2025.11281550.json, abstract) - whether the models run on ASE production lines, and the product or inspection station.
- NOT DISCLOSED (read: 2026-09-07_aseh_sustainability-report-2025-en.pdf, full-text search of 248 pages for "HBM", "high bandwidth memory", "hybrid bond") - any HBM or hybrid-bond inspection or metrology.
- NOT DISCLOSED (read: 2026-11-21_amkor_web-smart-manufacturing.html, full page) - which package lines or process steps use ADC; HBM.
- NOT DISCLOSED (read: 2026-11-21_amkor_event-itc-2026-osat-test-perspective.html, body) - test-time numbers, HBM, test methods.
- NOT DISCLOSED (read: 2025-01-02_googlepatents_intel-US20250006651A1-slit-fiducials.html, description) - production use and metrology tool vendor.

## 3. Premise problems in the critic's list
- M02_01 authors: the critic lists "Periasamy, Mahadevapuram, Ahmed, Ashok of Intel Foundry". The deck shows two presenters, Periasamy (Intel) and Parlato (Technoprobe). Ahmed and Ashok appear only in the acknowledgements. "Mahadevapuram" does not appear in the deck.
- M03_02: the deck does not print "TSMC" as the speakers' affiliation. TSMC ownership comes from the disclaimer (p28) and the "TSMC Secret" footer.
  - The critic's "cycle times (>2 weeks down to <1 week)" are per-stage spans whose labels are unreadable in the text layer.
  - "1.7X / 3.3X" are cycle-time chart labels. "Materials Saving!!" is a separate label.
- TSMC IMPACT paper: the critic calls Zhi-Hua Zou head of TSMC's Advanced Packaging Metrology Engineering division and a SEMICON Taiwan 2026 keynote speaker. Neither fact is in the saved Crossref or Semantic Scholar records, which give only the name and a TSMC affiliation (see leads).
- ASE IMPACT paper: "AI-based image inspection has been widely adopted" is a general statement in the abstract, not an ASE deployment claim.
- W07_01: the "SEM/EDS/X-ray characterization" is materials characterization of probe test coupons, not inspection of product bumps.
- Intel patent: "HBM-on-base-die stacking as context" appears only in generic boilerplate.
- Dates:
  - ASE report: 2026-09-07 is the PDF CreationDate; the ModDate is 2026-10-30.
  - Amkor Smart Manufacturing page: the HTML meta dateModified is 2026-08-07, not the critic's approximate 2026-08-01.
  - ITC 2026 page: published 2026-07-01, modified 2026-09-11.
- Host access:
  - The critic reported that www.intel.com and pr.tsmc.com answered WebFetch. fetch.py got HTTP 403 from both, so these hosts are not usable under the access rule.
  - aseglobal.com/en/pdf/ did serve the PDF to fetch.py.
  - patents.google.com returned 503 on the first try and 200 on a second try.

## 4. Candidates not added
- TSMC 2026 and 2025 Supply Chain Management Forum award PDFs (pr.tsmc.com): NOT RETRIEVED, fetch.py HTTP 403 on the one allowed test. The critic's category list came from WebFetch and stays a lead (section 5).
- Intel Foundry packaging page and Foveros Direct 3D tech brief (www.intel.com): NOT RETRIEVED, fetch.py HTTP 403 on the one allowed PDF test. The critic's quotes ("known good die before final assembly", "singulated die sort ... a best-in-class yield differentiator") stay leads.
- Partly added:
  - W07_01: FormFactor's outgoing radial-alignment data (243K springs across 15 cards) was left out. It is vendor outgoing-inspection data for its own probe cards.
  - M03_02: the thermal-solution slides (UCD >40% CCC, TDS roadmap) were left out. They concern probe-card hardware, not product inspection.

## 5. Unverified leads
- TSMC 2026 award list (via the critic's WebFetch, not read here). It reportedly gives these categories:
  - Advantest, Lasertec and V5 Technologies: "Excellent Production Support";
  - KLA: "Excellent Technology and Production Support and Excellence in Green Manufacturing";
  - All Ring Tech: "Excellent Production Support";
  - SPIL: "Excellent Turnkey Production Support".
  URL: the 2026 PDF above. Why it matters: it would upgrade AW-001 to AW-016 to [F] with English category names.
- Intel Foundry packaging page, https://www.intel.com/content/www/us/en/foundry/packaging.htm. Per the critic, it gives Intel's own wording on die-level test (singulated die sort, KGD before assembly, package-level burn-in, SLT). This would be an Intel [C] row on an added die-level test step.
- Zhi-Hua Zou's role at TSMC (head of Advanced Packaging Metrology Engineering) and his SEMICON Taiwan 2026 keynote: semicontaiwan.org refuses scripted access, so this is unconfirmed.
