# TH: limits of optical CD in HAR memory and GAA logic, and the role of X-ray CD (Q2)

**Evidence base**
- `TH.csv` has 45 rows: 39 [F], 2 [C], 4 [I]. `quote_check.py` found all 41 quotes in the saved files.
- **Full texts read:** Samsung+Nova (2024); IBM+Nova (2019, 2021 ×2, 2022, 2023, 2026); imec+Nova (2021, 2025); Nova (2026); IRDS Metrology chapters 2022–2024.
- **Abstract-only rows:** 15 rows cite a "SPIE volume page". Those pages give the abstract but no author affiliations.

**Premise check (leads)**
- **Choi/Jang/Seo, SPIE 13981:** the paper exists, and its abstract matches the lead (CD-SAXS + spectroscopic ellipsometry (SE) + ML, R2 > 0.95 vs SEM) [F] TH-008, TH-009. Its affiliation is unknown, so it should not be called a Samsung paper.
- **IRDS sentence:** confirmed, and the wording has not changed since 2022 [F] TH-012.
- **Timoney 13981-16:** real (Cu hybrid-bonding recess with an AFM reference) but off-topic, so not used.
- **Samsung–Nova release:** dated 27 Feb 2024; the file was saved as 2024-02-26.

## (a) Answer to Q2

**3D NAND channel holes and HAR contacts**
- **OCD limits**
  - Optical metrology has limited resolution toward the bottom of HAR structures [F] TH-001.
  - Samsung's flash team, writing with Nova, says the main HAR challenge is how lateral CDs vary with depth [F] TH-002. They reach bottom-CD R2 = 0.89 (RMSE < 5 Å) only with spectral interferometry plus ML trained on reference CDs [F] TH-003.
  - The dedicated OCD target polishes 1.5–2x slower than the array, so measurement in the cell is "a must" [F] TH-004.
  - Nova itself claims that depth profiling of deep 3D NAND was "previously inaccessible with OCD alone" [C] TH-005.
  - Abstracts add three more limits: carbon hardmasks are opaque at OCD wavelengths [F] TH-006; memory-hole OCD needs destructive SEM/TEM reference [F] TH-007; and CD-SAXS and OCD each have spot-size and model-dependence limits [F] TH-008.
- **Where X-ray enters**
  - IRDS says CD-SAXS has the throughput for HAR contact holes and that in-line tools are already in fabs [F] TH-012. A vendor tool takes a few minutes per site [F] TH-014.
  - IBM+Nova confirm that X-ray scattering has been demonstrated in-line on channel holes [F] TH-015.
  - CD-SAXS is now also the non-destructive label source for ML-based OCD [F] TH-007. Training SE spectra on CD-SAXS CDs gives R2 > 0.95 vs SEM [F] TH-009.
  - CD-SAXS throughput is still being optimised: angles of incidence were cut from 13 to 2 [F] TH-013.
- **Role left to OCD:** small-spot, local and edge measurement, against a CD-SAXS spot of about 300 µm [F] TH-010, TH-011. Overall assessment [I] TH-043 (Medium).

**DRAM capacitors and storage nodes (abstracts only)**
- **OCD limits:**
  - stacked-cylinder OCD models are inaccurate for the storage node [F] TH-016;
  - physical-modelling compute grows exponentially and reference labels are scarce [F] TH-017;
  - ML-OCD is an ill-posed inverse problem [F] TH-018.
- **X-ray:** XCD measures DRAM capacitors [F] TH-014, and IRDS says tall DRAM structures scatter strongly [F] TH-012.
- No chipmaker full text was read [I] TH-044 (Low).

**GAA nanosheet and CFET logic**
- **IRDS view:** parameter cross-correlation and quantum-confinement shifts are the main scatterometry problems [F] TH-019. IRDS still rates scatterometry among the best in-line options for GAA [F] TH-020.
- **imec+Nova:** cavity depth could only be measured by cross-section EM, and OCD correlations can give non-unique solutions [F] TH-024, TH-025.
- **IBM+Nova:**
  - Scatterometry is the only non-destructive in-line method for sheet-specific indents [F] TH-026.
  - Tiny, correlated volumes are the limit; spectral interferometry raised R2 vs STEM from 0.8 to 0.9 [F] TH-027.
- **CFET (imec+Nova):** OCD sensitivity falls for small SiGe residues, so ML is needed [F] TH-030, yet OCD tracks TEM at R2 0.85–0.99 [F] TH-031.
- **X-ray for logic**
  - IRDS treats lab CD-SAXS as reference-grade only. In-line use needs <1 min per site and a <100 µm spot [F] TH-021, plus sources at least 100x brighter [F] TH-022. IBM+Nova agree [F] TH-023.
  - CD-SAXS sensitivity has been shown only on test structures [F] TH-028.
  - GI-SAXS for CFET needs deeper probing and a smaller footprint [F] TH-032.
  - In practice X-ray enters as XRF, XRD or XRR inputs and references [F] TH-029, TH-033, TH-034, TH-038, TH-040.
- **Hybrid cost:** wide use was limited by cost of ownership [F] TH-036.
- **Overall assessment:** OCD with spectral interferometry and ML remains the in-line workhorse [I] TH-045 (Medium).

## (b) Nova papers involving X-ray
- **No CD-SAXS papers:** none of Nova's 45 publication pages is a CD-SAXS, T-SAXS or GI-SAXS paper [I] TH-042.
- **X-ray + optical hybrids (all co-authored with IBM):**
  - 2019: scatterometry + LE-XRF + ML for Cu voids [F] TH-037;
  - ASMC 2020 / TSM 2022: LE-XRF + scatterometry ML for SiGe indent [F] TH-038;
  - 2021: XRF reference and HRXRD sheet factor for indent OCD [F] TH-027;
  - 2026: an XRF-enhanced OCD model within in-line XPS [F] TH-040.
- **XRD as reference:** IBM 2021 Raman paper (Bruker HRXRD) [F] TH-039.
- **CD-SAXS mentioned only indirectly:** a citation [F] TH-028, a statement of needs [F] TH-015, TH-023, and a 2013 "+CD SAXS" hybrid entry in a review table [F] TH-035.
- **2016 hybrid release:** Nova announced an X-ray (thin film) + OCD hybrid offering "being evaluated by several key customers" [C] TH-041.

## (c) Gaps
- NOT RETRIEVED (tried: spiedigitallibrary.org and spie.org paper pages for DOI 10.1117/12.3090491; 212-byte bot-challenge stubs saved as 2026-04-22_spie-dl_abs-…Choi.html and 2026-04-22_spie_paper-page-…Choi….html, not cited) - full text and affiliations of Choi et al., Proc. SPIE 13981, 1398126
- NOT RETRIEVED (tried: spie.org volume pages 12053 and 12496; "Pardon Our Interruption" bot page) - SPIE MIPC 2022 and 2023 abstracts
- NOT RETRIEVED (tried: SPIE volume pages only; SPIE Digital Library paywall and bot challenge) - full texts behind TH-001, TH-006 to TH-011, TH-013, TH-014, TH-016 to TH-018, TH-032 to TH-034
- NOT DISCLOSED (read: spie.org volume pages 11325, 11611, 12955, 13426, 13981; proceedings.com TOC 13981) - author affiliations of all abstract-only papers (chipmaker vs vendor authorship unverified)
- NOT RETRIEVED (tried: SPIE DL PDF of JM3 22(3) 031205; non-PDF bot response) - JM3 2023 SAXS hole-tilt paper (SAXS as training input for OCD, per search snippet)
- NOT RETRIEVED (tried: NIST record has no full text; PubMed ID converter found no PMC copy) - Kline et al., JM3 16(1) 014001 (2017), compact-source CD-SAXS throughput (IRDS ref [169])
- NOT RETRIEVED (tried: web search for open-access chipmaker papers; SPIE DL blocked) - a chipmaker full-text paper on OCD limits for DRAM storage nodes
- NOT DISCLOSED (read: Yoon et al., Proc. SPIE 12955 129551S, section "Through cell metal contact") - type of reference metrology used to train the bottom-CD model
- NOT RETRIEVED (tried: Turovets 2026 Table 2 cites only SPIE course SC1100) - the 2013 OCD + CD-SAXS hybrid paper listed there
- NOT DISCLOSED (read: Nova publications sitemap (45 pages); year listings 2019, 2020, 2021; 2026 listing) - any Nova-authored or co-authored CD-SAXS / T-SAXS / GI-SAXS paper
- NOT RETRIEVED (tried: novami.com/year-publication/2018; HTTP 404) - Nova publications before 2019
- NOT DISCLOSED (read: IRDS 2024 Metrology chapter, cover and front pages) - exact release date of the 2024 edition
