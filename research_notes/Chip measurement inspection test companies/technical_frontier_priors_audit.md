# Technical frontier and priors audit: measuring and inspecting buried features in 3D and bonded chips

**Research date: 12 November 2026.** This is the final version, rewritten after gap-filling. Scope: technical facts and roadmaps only, with no company assessment.

**Citations and labels.** Citations are keyed links ([s1] … [s43]); the Sources section gives the title, date and URL for each key.
- **[CC]**: company claim, no outside confirmation found.
- **[SEC]**: secondary report (press, analyst, aggregator).
- **[TER]**: tertiary (Wikipedia, market research).
- **[SS]**: seen only in a search-result summary; the page itself was not read (lowest confidence).

**Coverage limits.**
- SPIE Proc. 13981 was read as abstracts on the volume page; only the IBM/Nova paper was read in full.
- The SemiAnalysis ECTC roundup and the Bits&Chips Invisix piece are partly paywalled.
- KLA's call was read through an auto-generated transcript.
- No IRDS 2025 edition was found, so the 2024 edition is used.
- No IEDM 2025, VLSI 2026 or IITC papers were read.
- Applied Materials was seen only through an analyst summary; no Lam Research or ASML process-control statements were obtained.

## Summary verdict table

| # | Item | Verdict | Source | Date |
|---|---|---|---|---|
| A1 | SE: buried post-bond defects are among the hardest problems as pitch shrinks below the 4-9 µm production range | **Confirmed**. The wording is "one of the most significant challenges". The **4 µm lower bound is not corroborated**: TSMC SoIC is at 6 µm now and 4.5 µm by 2029; Intel ships 9 µm; Amkor says "about six microns" | [s1] [s14] [s3] | 10 Nov 2026; 2 Sep; 16 Jul 2026 |
| A2 | EE Times: no roadmap for probing bond arrays below ~25 µm | **Confirmed; date corrected to 26 Jan 2026**. It is the article's paraphrase of imec ("absence of any realistic roadmap") | [s6] | 26 Jan 2026 |
| A3a | TrendForce: hybrid bonding in HBM slipped to 16-high HBM4E at the earliest | **Confirmed as of Jul 2026; corrected for SK hynix**: in Aug 2026 it said "not HBM4E", so HBM5 at the earliest, and its Vera Rubin HBM is all MR-MUF | [s9] [s13] [s12] | 7 Jul; 24-26 Aug 2026 |
| A3b | SemiAnalysis ECTC 2026: Samsung's hybrid bonding cuts thermal resistance by only 12-13%; 20-24-high needs new approaches | **Corrected**. 12.2%/12.9% is the *internal-HBM* resistance in a 2-GPU + 8-HBM package model. Stack level is ~19% (22.3%/29.1% at 2x/4x pad density); total HBM is 3.5%/7.7%; Samsung's own figure is >20% [CC]. "16-hi acceptable, 20/24-hi need new approaches" is confirmed | [s10] [s8] | 2 Jul 2026 |
| A4a | SPIE 2026: X-ray scattering and optical data fused with physics-informed ML | **Confirmed** (CD-SAXS + ellipsometry, 3D NAND, R² > 0.95 against SEM) | [s22] | Feb 2026 |
| A4b | The same volume names scarce training data as the brake | **Confirmed with nuance**: many abstracts cite scarce reference or labelled data, but the keynote named *trust* the biggest roadblock | [s22] [s26] | Feb 2026 |
| A4c | IBM maps optical spectra straight to reference values without an optical model | **Corrected**. The paper is IBM Research + Nova; the "modeless" ML keeps physics-based spectral filtering (VTS); the reference is **AFM** (non-destructive) on a near-surface Cu recess; 15 wafers x 5 dies; blind R² ~0.8 at best, 0.35 at worst | [s23] | Feb 2026 |
| A5 | Light: Adv. Manuf.: table-top computational EUV microscope resolved 43.5 nm half-pitch on a real chip | **Confirmed with nuance**. 17.9 nm HHG reflection ptychography; 43.5 nm is the diffraction limit and equals one reconstructed pixel; chip grating linewidth 42.7 nm by SEM; surface features only, single angle, not yet usable online | [s27] [s28] | Online 9 Sep 2026 |
| B1 | Steps per leading-edge wafer keep rising through 2028 (75%) | **Supported by vendor statements and spending; no node-level step counts found** | [s29] [s30] [s21] | Aug-Oct 2026 |
| B2 | Buried bond-interface defects still a leading yield limiter in 2030 (60%) | **Mixed**. The detection gap is confirmed, but the root causes are mostly pre-bond, research W2W yields are 97-98%, hybrid bonding in HBM is ~2028-30, and in DRAM dies ~2028 | [s1] [s20] [s21] [s19] | 2024-2026 |
| B3 | Computed methods take share from direct imaging 2029-33 (45%) | **Counter-evidence is stronger today**: e-beam spending and adoption are rising; inline CD-SAXS is limited to memory high-aspect-ratio work; logic needs >=100x brighter sources; soft-X-ray scatterometry is at start-up stage | [s21] [s22] [s30] [s31] | 2024-2026 |
| B4 | Tools per wafer may fall after 2030 (35%) | **No supporting roadmap or vendor statement found**; vendors project growth to 2030 | [s21] [s22] [s29] | 2024-2026 |
| B5 | AI changes the software and economics of measurement before its physics | **Partly contradicted** in dose- and photon-limited measurements | [s22] [s28] | 2026 |
| B6 | Learned denoising is safe for the expected, risky for the unexpected | **Supported qualitatively; untested quantitatively**; deep-learning enhancement is already used for defect detection | [s22] [s26] | 2026 |
| C | Roadmap facts | **Mostly complete** (gaps: Samsung foundry bond pitch, JEDEC primary document, IRDS 2025) | Part C | — |
| D | Contradictions with the background | **12 points** | Part D | — |

## A. Verification of background evidence items

### Takeaway
All five items trace to real 2026 sources, but only A1 and A2 survive essentially intact. Three need correcting or updating:
- The "12-13%" is one of several thermal metrics.
- The IBM case uses AFM, not EM cross-sections, and keeps physics-based filtering.
- The TrendForce HBM4E timing has been overtaken by SK hynix's August statement.

The SE "4 µm" production lower bound is also not corroborated.

### Cited Findings
**A1, Semiconductor Engineering, November 2026.**
- Laura Peters, 10 Nov 2026 [s1]. Inspection struggles "as hybrid bonding pitches continue to scale down below today's production levels of 4 to 9 µm"; "Detecting buried defects after bonding remains one of the most significant challenges"; "no single technique provides the resolution, sensitivity, wafer coverage, and throughput required to identify every yield-critical defect." Pitches are said to be approaching "5 µm and below."
- Method limits in the same article [s1]:
  - Acoustic micro-imaging (~200 MHz) is the best acoustic option, but "Ultrasound does not travel through air gaps that have a thickness down to about 0.1 µm". At 165 MHz it "gets you down to a resolution of 12 microns", and a 5 µm defect can be detected but not measured accurately (Nordson). It is currently run after full assembly.
  - X-ray: "A resolution of 150 nm has been demonstrated"; Bruker XRDI does full-wafer inspection at "~20wph" [CC].
  - IR checks pad alignment through silicon.
  - Defect-size requirements reach "as low as 50 nm"; Cu recess is 2-5 nm, controlled "within 2 nm"; roughness must be ~0.5 nm RMS.
  - Micro-inspection samples "maybe two to five wafers per lot" (Microtronic).
  - The article mentions no AI/ML.
- Pitch cross-checks:
  - Amkor's Mike Kelly: "The go-to minimum pitch now is about six microns"; "There are roadmaps out there going all the way to one-micron pitch." Macro optical inspection cannot resolve the bond interface; post-bond electrical test is "the most direct evidence that the interface works" (article paraphrase). [s3] (SE, 16 Jul 2026)
  - TSMC (2026 North American Technology Symposium, as reported): pitch "from 9 microns in 2023 to 6 microns in 2025 and 4.5 microns by 2029"; "TSMC offers 6-micron pitch while its newest disclosed customer ships at 9; Intel ships at 9 with 3 on the roadmap." [s14] [SEC]
- Earlier SE (12 Aug 2025): optical methods "can struggle with buried interfaces or subsurface voids"; acoustic, IR and X-ray "typically lack the resolution or contrast needed to detect nanoscale voids". [s2]

**A2, EE Times.**
- Pat Brans, **26 Jan 2026** [s6]: "The absence of any realistic roadmap for probing dense hybrid-bond arrays below ~25 µm pitch" forces a rethink of pre-bond test.
- Erik Jan Marinissen (imec): "From a test perspective, this technology is under development and not mature at all." Sacrificial probe pads may work "at the cost of additional area and process complexity". "A single particle can create a stand-off height that leads to many open defects, sometimes across die boundaries."
- CMP is "the single largest source of yield variability in high-volume manufacturing" (Fraunhofer ENAS).
- IRDS 2024 lists "Fine pitch probing methods" and "known good dies" among hybrid-bonding metrology needs. [s21]

**A3a, TrendForce on HBM4E timing.**
- 7 Jul 2026, citing ZDNet Korea [SEC] [s9]: "16-high HBM4E as the 'earliest likely adoption point'"; "12-high HBM4E products are still expected to remain the mainstream offering"; HBM4 stayed on thermo-compression bonding; Samsung's Heat Path Block and SK hynix's iHBM are being tested for HBM5.
- 6 Mar 2026 [s7]: Samsung "is expected to introduce the technology only partially at the earliest in 16-layer HBM4E"; hybrid bonding "has not yet been deployed in mass production for HBM".
- **Update, Hot Chips, 23 Aug 2026** (Jaesik Lee, SK hynix America) [s13] [SEC]:
  - "SK hynix doesn't expect hybrid bonding to be ready for HBM4E", which pushes the transition "out to HBM5 at the earliest".
  - Hybrid bonding "remains at the research stage for stacks of 20 layers and above"; SK hynix "is still deciding which product gets it first".
  - Lee: "We are talking about 16 layers and 20 layers that we need to make the hybrid bonding, so it's very different from the one-layer stacking."
  - SK hynix holds "around 70% of Nvidia's HBM orders for the Vera Rubin generation … and all of it will be stacked with MR-MUF."
  - Corroborated by [s12] (Bits&Chips) and [s15] (MLQ summary).
- SK hynix (Kim Ji-hoon, SEMI panel, 9 Sep 2026) requires "a yield of 90 to 98 percent" and "a lifespan of three to five years" before adopting hybrid bonding. [s16] [SEC]

**A3b, SemiAnalysis ECTC 2026 roundup (2 Jul 2026; partly paywalled) [SEC] [s10].** Samsung's model compares hybrid copper bonding with thermo-compression bonding in a package with 2 GPU dies and 8 HBM stacks.
- "The internal HBM thermal resistance drops by 12.2% with air cooling and 12.9% with liquid cooling."
- "Total HBM thermal resistance drops by 3.5% with air cooling and 7.7% with liquid cooling."
- "Baseline HCB reduces stack thermal resistance by ~19% versus TCB", rising to "22.3% at 2× pad density and 29.1% at 4× pad density."
- Inlet temperature can rise 1-2 °C, or package power ~4%; cooling power falls ~7%.
- "With 16-hi HBM, the thermal resistance is still acceptable … with future generations moving to 20-hi and 24-hi HBM, new approaches are needed."

Other vendor figures:
- Samsung at GTC, March 2026: "over 20% improvement in thermal resistance versus TC bonding" [CC]. [s8]
- SK hynix deck: hybrid bonding at 20-high cuts thermal resistance "roughly 35% versus MR-MUF", allows 24% thicker core dies, and brings bump pitch "below 18 microns … against the 30 microns where MR-MUF is today" [CC]. [s13]

**A4, SPIE Advanced Lithography + Patterning 2026 (22-26 Feb 2026, San Jose); Proc. SPIE 13981 [s22].**
- X-ray plus optical fusion:
  - "High-resolution 3D NAND profile measurement using optical metrology and machine learning" (Choi, Jang, Seo et al.) combines "CDSAXS profile data with spectroscopic ellipsometer (SE) spectra using physics-informed machine learning". All sites reach R² > 0.95 against SEM.
  - Henn, Chew, Bajcsy et al. fuse OCD with another modality using ensemble and physics-informed neural networks.
- Data scarcity, in the same volume:
  - X-ray CD ML: "A key challenge is the limited availability of high-quality reference data."
  - SEM synthesis: "scarcity of high-quality training data".
  - SEM contours: "scarcity of annotated (labeled) images".
  - Few-shot SEMformer: "labeled 3D heights are extremely scarce".
  - Virtual-metrology matching: "physical metrology is sparse and requires a considerable amount of time to reach statistical significance".
  - Overlay ML trained "using only 3–5 wafers".
- Keynote (S. McCandless, Micron), per C. Mack: "the biggest roadblock to the widespread use of AI in metrology: trust". [s26] [SEC]
- IBM paper (Timoney, Schoeche, Polomoff … Schmidt, IBM Research Albany; Cepler, Isbester, Turovets, Nova), SPIE 13981-16 [s23]:
  - Keywords include "modeless" and "reference metrology". "Unlike conventional OCD ML that requires detailed underlayer modeling … this VTS-ML approach applies a single model applicable to both top and bottom wafer categories."
  - Reference: **AFM**, "5 measurement dies across 15 wafers", ~4 nm training range, 22 blind wafers.
  - Results: blind-test R² = 0.35 at cutoff A ("insufficiently trained") and ~0.8 at cutoffs B and C.
  - Framed as "leveraging limited reference metrology in an R&D environment".
  - Talk given 24 Feb 2026 [s24].

**A5, Light: Advanced Manufacturing 2026.**
- Chen Y., Xu H., Wang Q., Li Y. … Shi Y., Fan Z., "Table-top extreme ultraviolet grazing-reflection ptychography with full-pose self-calibration", LAM 7:112, DOI 10.37188/lam.2026.112. Accepted 30 Jun, online 9 Sep 2026. Institutions: UCAS and CAS institutes (AIR, IoP, SIOM), Jihua Lab and others. [s27]
- Setup: 17.9 nm high-harmonic source, 70° grazing incidence, NA 0.19 x 0.095, pixel 43.5 x 70.0 nm.
- Chip result: contrast 0.49 with calibration versus 0.13 without; "an actual grating linewidth of 42.7 nm … confirms that the system resolution (half-pitch) reaches a diffraction limit of 43.5 nm". [s28]
- On the custom wafer, "features are not fully resolved even in full-pose reconstruction" (82.6 nm FWHM).
- Limits: "practical deployment in online settings is limited by the computational speed of phase retrieval algorithms"; single angle; ~10⁷ photons needed.
- The paper's own Table 3 lists an earlier table-top reflection system at 40 nm half-pitch (no real chip), so the "best resolution reported to date" claim needs that qualifier. [s28]

### Inferences
- A2 rests on one imec interview reported in January; it is not a roadmap-body statement. IRDS only lists fine-pitch probing as a need.
- A3b: thermal benefit alone does not carry 20-24-high stacks. "Only 12-13%" understates the stack-level effect and overstates the package-level effect.
- A4c: the showcase "no optical model" case is a near-surface parameter with a non-destructive reference. It is not buried 3D metrology calibrated by TEM.
- A5: computation recovered resolution from imperfect hardware, but at 43.5 nm on surface features, far from leading-edge 10-20 nm CDs.

### Gaps
- Full SPIE papers (other than IBM/Nova) are paywalled; author affiliations were not visible.
- The rest of the SemiAnalysis article is paywalled.
- No 2026 update on probing below 25 µm was found (SWTest 2026 not checked).

## B. Priors tested against current evidence

### Takeaway
- B1 (rising steps) is vendor-supported but unquantified.
- B2 (bond defects in 2030) is plausible, but the cause sits mostly before bonding, and hybrid bonding arrives later in HBM than assumed.
- B3 (computed methods take share) is weaker than e-beam's momentum.
- B4 (fewer tools after 2030) is unsupported.
- B5 (AI before physics) is partly wrong where dose or photons are the limit.
- B6 (denoising risk) is plausible but publicly untested.

### Cited Findings
**B1, measurement steps per leading-edge wafer rising through 2028 (75%).**
- For:
  - KLA, 28 Oct 2026 [CC] [s29]: "Intensity is definitely going up"; "In some products we see intensity levels in DRAM that are similar to leading edge logic"; "an uplift in process control intensity and conventional memory"; HBM (logic and base die) lifts intensity.
  - KLA on advanced packaging: it needs "more sampling steps because of the value of the die" and moves "from micron level sensitivity down to the 100 nanometer type sensitivity". Advanced-packaging process-control revenue is "on track to hit $1.1 billion or more", up ">70%".
  - KLA market view: WFE "mid-$150 billion" in 2026, ">$200 billion" in 2027, "$220 billion plus or minus $20 billion" in 2030.
  - Applied Materials, Q3 FY2026: process diagnostics and control "expected to grow more than 50% in calendar 2026 … supported by demand for eBeam and optical inspection in advanced logic, DRAM, and packaging" (analyst-reported company expectation) [CC] [s30].
  - IRDS 2024 near-term (2024-29): nanosheet and CFET "require an increased need for in-line metrology … at the atomistic scale"; backside power "requires new concepts of metrology over FEOL, BEOL, and A&P". [s21]
  - New GAA-specific inspection steps appear at SPIE 2026: high-landing-energy e-beam as an "in-line blocked nanowire release metric for GAA yield ramp"; SEM gate-leakage tests. [s22]
- Gap: KLA gave no 2 nm, GAA or backside-power intensity figures [s29].
- Against:
  - AI cuts time per measurement, not steps: X-ray CD acquisition ">6X" faster and AOIs "from 13 to just 2"; GAN denoising cuts X-ray CD time "up to 40%". [s22]
  - Virtual metrology already runs in 3D NAND mass production ("MMT is a key virtual metrology (VM) enabler for mass production"). [s22]
  - Nvidia reportedly weighs 8/12-high HBM4 for Rubin Ultra [s16] [SEC]. SemiAnalysis: "Hybrid bonding's case in HBM was always stack height" [s11] [SS].

**B2, buried bond-interface defects a leading yield limiter in 2030 (60%).**
- For:
  - IRDS 2024: anneal "nano-voids … are currently only detectable by off-line TEM"; acoustic void resolution "approaches 60 microns (using a 110 MHz transducer)"; thinning wafers to improve it "is not a manufacturable solution"; IR review cannot cover 100% of a wafer. [s21]
  - IEEE EPS (Mar 2026, ECTC 2025 special session): confocal acoustic microscopy's "resolution limit of approximately 10 µm, often insufficient for detecting voids in contemporary hybrid-bonded devices"; a need to "detect sub-micron size voiding at the Cu-Cu interface". [s20]
  - Tolerances: "A single particle smaller than a micron holds the surfaces apart and leaves a gap spanning many pads"; surfaces may vary "no more than around 0.2 nanometers" [s14] [SEC]. Amkor: "It only takes one nanosized particle" [s3].
  - Intel's ECTC 2026 low-temperature fine-grain Cu W2W gave electrical yield "around 60% in two of three samples" (a lower bound), with opens tied to benzotriazole residue at the interface [s10].
  - SK hynix's 90-98% yield bar is not yet met [s16].
- Against:
  - Applied Materials (ECTC 2026, paper 18.4): "450nm pitch copper hybrid bonding achieving 98% yield across 20 million via links" [CC]. Its "parts-per-million level open defects" were found by electron-beam absorbed current, and TEM-EELS showed a carbon-rich interface layer [s19].
  - CEA-Leti: >97% yield after a 100 °C anneal [s10]. imec/EV Group: 200 nm W2W pitch with <40 nm overlay [s14] [SEC].
  - Panel consensus: "Pre-bond surface topography, Cu recess, oxide planarization, and surface defectivity remain primary contributors to bonding failure and yield loss" [s20].
  - IRDS: "a number of SAM tools" already support in-line *macro*-void metrology in HVM [s21].
- Methods in development: picosecond laser acoustics for buried HBM voids; e-beam process control for HBM hybrid bonding; backscatter-SEM Cu recess calibrated "with TEM-measured recess on 200-nm pads" [s22]. Onto (vendor blog): IR sub-surface inspection "can reveal voids and embedded defects that otherwise remain hidden" [CC] [s4].

**B3, computed methods take share from direct imaging 2029-33 (45%).**
- X-ray (IRDS 2024) [s21]:
  - For 3D NAND and DRAM, CD-SAXS "has the required throughput for characterization of HAR contact holes and commercially available in-line tools have recently been introduced to the fab".
  - Logic in-line use needs "<1 min" with a "<100 µm" spot; "Current X-ray sources do not have a high enough X-ray brilliance"; at least "100[x]" brighter sources are needed (symbol lost in extraction); inverse-Compton sources are proposed.
- SPIE 2026 X-ray, soft X-ray and EUV work [s22]:
  - X-ray CD on 3D NAND across "2 full wafers with over 600 measurement sites".
  - Resonant soft X-ray scattering with FEM Maxwell solvers and ML for CFET-like structures (TEM as baseline).
  - Hard-X-ray reflection CD with "sub-nanometer out-of-plane sensitivity".
  - A discharge-plasma soft-X-ray source.
  - EUV scatterometry framed as Bayesian adaptive design; a UHV EUV Mueller-matrix ellipsometer.
  - EUV mask ptychography at "11.5 nm" and "14 nm (at the wafer)".
  - Caveat: CD-SAXS changed EUV-resist linewidth by 5% during measurement (per Mack) [s26].
- Programmes:
  - Invisix, "spun out of ASML R&D", is "betting that soft X-ray scatterometry can close a growing visibility gap"; ASML kept only scanner-feedback metrology (23 Apr 2026) [s31] [SEC]. A related headline says Invisix raised €20M (unverified).
  - PSI's REGINE beamline (6-16 nm reflectometry, scatterometry, coherent diffraction); imec AttoLab 92 eV HHG EUV scatterometry (2025); NIST overview at FCMN, 17 Mar 2026 [s42] [SS].
  - No 2026 lensless-imaging programme was found at ASML, Samsung or KLA.
- E-beam counter-trend:
  - SPIE 2026 [s22] [s26]: multibeam-SEM defect inspection; multicolumn e-beam for EUV reticles; high-kV cold-field-emission DRAM overlay; high-voltage SEM see-through metrology; "massive data collection" e-beam; ASML e-beam inspection reaching "one part per million defect capture rates".
  - Applied Materials: process diagnostics and control +50% in 2026 on e-beam and optical [s30] [CC]; cold-field-emission e-beam revenue said to double to >$1B in 2026 [SS].
  - KLA: e-beam relevance "becomes more pronounced" [s29] [CC].
  - Market research names e-beam the fastest-growing segment (~9.7-9.9% CAGR; multibeam 12.5%) [s39] [TER].
  - IRDS: "Existing SEMs and SPMs are considered too slow"; optical "lose[s] some sensitivity to defects smaller than 20 nm" [s21].

**B4, tools per wafer may fall after 2030 (35%).**
- For:
  - IRDS 2024: ML should ensure "the proper type and number of measurements … to avoid too many measurements (loss of time and money)"; "Sampling plan optimization is key". [s21]
  - Virtual metrology in 3D NAND production; ASML "computational guided dynamic sampling e-beam inspection" improved defective-die capture "by up to 4.3x". [s22]
- Against:
  - KLA and Applied Materials project growth [s29] [s30].
  - Virtual metrology still needs sparse physical metrology [s22].
  - "Machine learning is very good at interpolation, but not so good at extrapolation" (AIST, per Mack) [s26].
  - SE argues measurements must be re-verified after each physical change (summary only) [s5].
- No roadmap or vendor statement forecasting fewer tools per wafer was found.

**B5, AI changes software and economics before physics.**
- Counter-cases where computation changes what can be measured within a dose or photon budget [s22]:
  - Generative denoising for actinic EUV mask inspection, "using 30X fewer exposures".
  - Deep-learning CD-SEM denoising allows fewer frames, mitigating "e-beam-induced damage" (repeatability 0.095 to 0.073 nm).
  - A CNN restores out-of-focus W2W overlay images.
  - Physics-inspired deep learning extracts LER "without any training data with ground-truth edge profiles".
- In LAM 2026, gradient-based self-calibration (not ML) meant "only the full-pose strategy successfully resolved the defects" [s28].

**B6, learned denoising safe for the expected, risky for the unexpected.**
- For [s22] [s26]:
  - SPIE 2026 "Detection of inference errors in deep learning denoising models … for SEM metrology" proposes a "Transform Monitoring method".
  - Denoisers need fine-tuning "for new SEM image pattern types".
  - Mack: "Talks on image denoising in particular do not excite me". NIST judged some synthetic training SEMs "not representative of real SEMs".
- Against or mitigating [s22] [s26]:
  - "AI-based detection algorithm for optical inspection of critical defects on 2nm and 1.4nm technology nodes" (deep-learning image enhancement).
  - Generative denoising used in EUV mask defect inspection.
  - Diffusion-model defect detection "without the need for labeled defect data".
  - Intel reported fewer false defects with ML.

### Inferences
- B1: 75% looks fair for memory and packaging but rests on vendor statements; no independent node-level step counts exist publicly.
- B2: reframe it. The 2030 limiter is more likely pre-bond surface state and particles, with interface voids as the symptom. Electrical test (daisy chains, electron-beam absorbed current) acts as the de facto judge, so value may move upstream to pre-bond inspection and to electrical screening.
- B3: evidence favours "both grow". X-ray share gains look confined to memory high-aspect-ratio work until much brighter compact sources exist. Soft-X-ray scatterometry is at start-up stage in 2026 (Invisix), which fits a 2029-33 window only for niches. E-beam is gaining now, so the prior looks too high for logic.
- B4: no evidence for it yet.
- B5: reword as "AI changes information per dose/photon before it changes probe physics". In dose-limited regimes this does change what can be measured.

### Gaps
- No Lam Research or ASML statements on process-control intensity were found, and no third-party process-control share of WFE by node.
- No quantitative study of denoising missing novel defects was found.
- IEDM 2025 and IITC 2025/26 hybrid-bonding yield papers were not read.

## C. Roadmap facts (as of 12 Nov 2026)

### Takeaway
- Hybrid bonding in HBM moved from HBM4, to HBM4E at the earliest (Samsung, partial), to HBM5 at the earliest (SK hynix, ~2028-30). JEDEC height relief and MR-MUF/TC-NCF extensions removed the urgency.
- Logic hybrid bonding is in volume at 6-9 µm.
- W2W hybrid bonding is in volume in 3D NAND and may enter DRAM dies (VCT) around 2028.
- Backside power is in volume at Intel 18A; TSMC A16 is reported for Q4 2026.

### Cited Findings
- **SK hynix** (Hot Chips, 23 Aug 2026) [s13] [s15] [SEC]:
  - 12-high HBM4 is in mass production; 16-high HBM4 is in customer qualification at 48 GB per cube, with ~50 µm core dies.
  - The 775 µm cap matches logic-wafer thickness: "the logic wafer thickness is also 775 microns."
  - 12-high HBM4E samples use Advanced MR-MUF; hybrid bonding is at the research stage for 20-high and above.
  - Industry sources say SK hynix ordered its first hybrid-bonding line in March (Applied Materials + Besi, ~₩20B) [SEC].
  - Counterpoint expects HBM5 "around 2029 to 2030" [s17] [SEC].
- **Samsung** [s18] [s7] [s8] [s14] [SEC/CC]:
  - HBM4 mass production from Feb 2026 (1c DRAM, 4 nm base die); HBM4E samples shipped May 2026.
  - Hybrid bonding partially at 16-high HBM4E at the earliest.
  - Hybrid-bond inspection tools being introduced, with an Onto joint development programme (The Elec).
  - Custom HBM logic dies reportedly on Samsung 2 nm for 2027 samples.
  - zHBM is a concept only.
- **Micron** [s37] [SS]: HBM4E has a customisable base die on a TSMC process (2027); roadmap HBM4 to HBM5/5E/6 over ~2028-30; wafer bonding at the 1-epsilon DRAM node. **No hybrid-bonded HBM date — could not verify.**
- **Nvidia**: Vera Rubin HBM from SK hynix is all MR-MUF [s13]; Rubin Ultra (2H 2027) is reportedly weighing 8/12-high HBM4 [s16] [SEC].
- **JEDEC heights** [s8] [s9] [s13] [SEC]:
  - 720 µm through HBM3E; 775 µm for HBM4.
  - Under discussion: ~900 µm from HBM4E (Newsis); 825-900 µm (ZDNet, Mar 2026); 900 to 1,000 µm including 20-high HBM5 (Jul 2026).
  - The date of the 775 µm decision conflicts (Tom's Hardware says "January" [s14]).
  - No JEDEC primary document was found.
- **HBM bump pitch** (figures conflict): "20µm pitch and 5µm stack spacing" in mass production [s19]; "HBM4 pad pitch at 10 microns" [s14]; MR-MUF "30 microns … today" [s13].
- **Logic hybrid-bond pitch** [s14] [SEC]:
  - TSMC SoIC: 9 µm (2023), 6 µm (2025), 4.5 µm by 2029. Stacked nodes go from N3P-on-N4 now to N2P-on-N2P by 2028 and A14-on-A14 by 2029. Face-to-face hybrid bonding gives ~14,000 signals/mm² versus ~1,500 for face-to-back TSV.
  - Intel Foveros Direct: 9 µm in high volume on Clearwater Forest (Xeon 6+, 18A); second generation targets 3 µm.
  - Bonder throughput: Applied/Besi Kinex ~1,600 die placements/h; Besi Chameo ~2,000/h [CC].
  - **Samsung foundry pitch roadmap: not found.**
- **Research records**:
  - W2W: 200 nm pitch, <40 nm overlay (imec/EVG, ECTC 2026) [s14]; 450 nm at 98% yield over 20M links (Applied Materials) [s19] [CC].
  - D2W: 1 µm (CEA-Leti, ECTC 2026) [s14] [s3].
  - IBM D2W/W2W below 2.5 µm (IEDM 2024) [s23].
- **NAND** [s20] [s18] [s19]:
  - YMTC Xtacking (W2W) since 2018.
  - Kioxia BiCS 10 (332 layers) bonds CMOS to the array [CC]; Samsung V10 (>400 layers) uses wafer bonding [CC].
  - Kioxia (ECTC 2026): multi-stacked W2W CBA with sub-800 nm pads.
- **DRAM** [s35] [s36] [SS]:
  - Samsung presented a 16 Gb 4F² vertical-channel DRAM with W2W hybrid Cu bonding at ISSCC (Feb 2026). The Elec (via TrendForce, 24 Apr 2026): development 2026, qualification 2027, mass production 2028, IGZO channel. Samsung has not committed publicly.
  - SK hynix plans a vertical-gate variant at the 10b node.
  - Micron declines 4F² and puts 1-delta in Boise in 2H 2027.
  - CXMT plans 4F² DDR5 by end-2026.
- **Logic ramps**:
  - TSMC N2 in volume from Q4 2025; N2P volume Q3 2026 [s33] [TER].
  - TSMC A16 (Super Power Rail backside power): "completed development and validation", mass production "in the fourth quarter of this year"; A14 in 2028 [s32] [SEC]. TSMC's Q3 2025 guidance put N2P/A16 in 2H 2026 [s43] [SS].
  - Intel 18A (RibbonFET + PowerVia) in HVM since late 2025 [s33]. Yields improving "7%-8% per month" (Lip-Bu Tan); 14A risk production late 2027, production 2028; Tesla reported as a 14A customer [s34] [SS].
  - Samsung SF2 in mass production 2025, with yields reportedly "50–60%" into early 2026; SF2P ramping in 2026 [s33] [TER]. Samsung 1.4 nm reportedly moved to 2029 [s32].
  - Rapidus: production start 2H FY2027, full scale FY2028, 6,000 rising to ~25,000 wafers/month; no committed volume customer [s38] [SS].
- **IRDS 2024 long-term (2030-37) challenges**: "Nondestructive, production-worthy wafer and mask-level metrology for CD measurement for 3D structures, overlay, defect detection"; "characterization of subsurface structures (dimensional and compositional measurements) is needed"; "Sampling plan optimization is key". [s21]

### Inferences
- Volume buried Cu-Cu interfaces in memory come first from W2W bonding (NAND now; DRAM dies possibly 2028), ahead of D2W HBM stacks (HBM5, ~2028-30).
- In logic, volume hybrid bonding sits at 6-9 µm D2W. The inspection problem "below 4-9 µm" in volume is therefore mostly a 2027-29 issue, at 4.5 µm and then 3 µm.

### Gaps
- Samsung foundry hybrid-bond pitch roadmap.
- JEDEC primary documents.
- IRDS 2025 edition.
- TSMC's own Q3 2026 statement on A16.
- Whether Rapidus will use backside power.
- Production W2W pitch in NAND.

## D. Points where current evidence contradicts the background

1. **"Production range 4-9 µm"**: the 4 µm lower bound is not corroborated for volume D2W logic. TSMC is at 6 µm (4.5 µm by 2029), Intel at 9 µm, Amkor "about six microns". [s14] [s3]
2. **Reference data is not only destructive EM cross-sections.** IBM/Nova used AFM; CD-SAXS serves as a reference for optical ML; in-fab PFIB-SEM "ground truth" exists. TEM remains common. [s23] [s22]
3. **"Matching a simulated signal" is incomplete.** Model-free regression to reference data ("modeless" VTS-ML) is advancing alongside physics-based solvers. [s23]
4. **16-high stacks are not hybrid-bonded.** 16-high HBM4 uses MR-MUF or TC-NCF within 775 µm; hybrid bonding targets 20-high and above (HBM5, ~2028-30); SK hynix's Vera Rubin HBM is all MR-MUF. [s13]
5. **TrendForce "16-high HBM4E at the earliest" is outdated for SK hynix.** [s13] [s12]
6. **"Only 12-13%" picks one metric** (stack 19-29%; total 3.5-7.7%; Samsung >20%). [s10] [s8]
7. **The EE Times item is January 2026**, and it paraphrases imec. [s6]
8. **The EUV microscope result is surface-only, 43.5 nm, single-angle and offline.** It is not evidence for buried or leading-edge computed imaging. [s28]
9. **"AI before physics" is partly wrong**: 30x fewer exposures (EUV masks) and lower SEM dose change what is measurable in dose-limited regimes. [s22]
10. **The main hybrid-bond yield detractors are pre-bond** (surface, CMP, Cu recess, particles), not buried defects per se. [s20]
11. **Measurement as the per-wafer "judge" is only partly true in hybrid bonding.** Micro-inspection samples 2-5 wafers per lot; acoustic imaging runs after assembly; post-bond *electrical* test is "the most direct evidence"; ppm opens were found electrically (electron-beam absorbed current), then by TEM. [s1] [s3] [s19]
12. **Change of emphasis, not a strict contradiction**: the first volume buried Cu-Cu interfaces in memory are W2W (NAND now, VCT DRAM ~2028 [SS]), not HBM stacks. [s20] [s35]

## Sources (with dates)
Each key's URL is in the link definitions directly below this list; keys with several URLs list them inline.
- [s1] Semiconductor Engineering, L. Peters, "Shrinking Hybrid Bonding Pitches Push Inspection Limits", 10 Nov 2026
- [s2] SE, G. Haley, "Metrology Under Pressure…", 12 Aug 2025
- [s3] SE, G. Haley, "Can Fine-Pitch Hybrid Bonding Go High Volume?", 16 Jul 2026
- [s4] SE sponsor blog, Y. Gao (Onto Innovation), 8 Oct 2026
- [s5] SE tag pages (accessed 12 Nov 2026; includes "How Long Does A Measurement Remain Valid?", 11 Aug 2026)
- [s6] EE Times, P. Brans, "Hybrid Bonding Comes of Age Slowly and Collectively", 26 Jan 2026
- [s7] TrendForce (citing ZDNet), 6 Mar 2026
- [s8] TrendForce (citing Chosun Ilbo, Newsis, The Elec), 1 Apr 2026
- [s9] TrendForce (citing ZDNet), 7 Jul 2026
- [s10] SemiAnalysis, Ahmad, TC, Wong, Patel, ECTC 2026 roundup, 2 Jul 2026
- [s11] SemiAnalysis post on X (reported Oct 2026; date unverified)
- [s12] Bits&Chips, P. van Gerven, 26 Aug 2026
- [s13] Tom's Hardware, L. James, Hot Chips SK hynix, 24 Aug 2026
- [s14] Tom's Hardware, L. James, "The current state of Hybrid Bonding in 2026", 2 Sep 2026
- [s15] MLQ (AI-written summary), 25 Aug 2026
- [s16] Herald Business, 20 Sep 2026
- [s17] Seoul Economic Daily (Counterpoint), 6 Apr 2026
- [s18] technologies.org (FMS 2026), 5 Aug 2026
- [s19] IEEE ECTC 2026 technical tipsheet, 20 May 2026
- [s20] IEEE EPS, Gorchichko et al., summary of ECTC 2025 hybrid-bonding special session, Mar 2026
- [s21] IEEE IRDS 2024, Metrology chapter
- [s22] Proc. SPIE 13981, Metrology, Inspection, and Process Control XL (conference 22-26 Feb 2026)
- [s23] Timoney et al. (IBM Research/Nova), SPIE 13981-16 (PDF posted Apr 2026)
- [s24] IBM Research blog, L. Meli, 23 Feb 2026
- [s26] C. Mack, SPIE 2026 diary, Feb 2026
- [s27] Chen et al., Light: Advanced Manufacturing 7:112, online 9 Sep 2026
- [s28] Same paper, PDF
- [s29] KLA Q1 FY2027 call, 28 Oct 2026 (transcript 29 Oct)
- [s30] Futurum, B. Burke, Applied Materials Q3 FY2026, 17 Aug 2026
- [s31] Bits&Chips, P. van Gerven, Invisix, 23 Apr 2026
- [s32] Design & Reuse (via BigGo), TSMC A16, 24 Aug 2026
- [s33] Wikipedia, "2 nm process" (edited 21 Oct 2026)
- [s34] [SS] Tom's Hardware (Intel 14A in 2028) — https://www.tomshardware.com/pc-components/cpus/we-cant-completely-vacate-the-client-market-says-intel-amid-wafer-supply-shortages-nova-lake-still-on-track-for-late-2026-release-14a-in-2028 ; TrendForce, 21 Nov 2025 — https://www.trendforce.com/news/2025/11/21/news-intels-two-front-push-18a-yields-reportedly-rise-7-monthly-14a-enters-definition-stage/
- [s35] [SS] TrendForce (citing The Elec), 24 Apr 2026 — https://www.trendforce.com/news/2026/04/24/news-samsung-reportedly-produces-sub-10nm-10a-dram-working-die-using-4f-square-and-vct-targets-2028-production/ ; Bits&Chips — https://bits-chips.com/?p=234158
- [s36] [SS] SemiWiki forum, ISSCC 2026 Samsung 16Gb VCT DRAM
- [s37] [SS] TweakTown (Micron roadmap) — https://www.tweaktown.com/news/114236/micron-reveals-ddr6-lpddr6-hbm-and-nand-roadmap-as-ai-memory-demand-keeps-climbing/index.html ; 3dnews — https://3dnews.ru/1115818 ; Futurum — https://futurumgroup.com/?p=97109
- [s38] [SS] Tom's Hardware (Rapidus 2027) — https://www.tomshardware.com/tech-industry/semiconductors/rapidus-targets-2nm-mass-production-in-2027-with-a-four-times-capacity-ramp ; TrendForce — https://www.trendforce.com/news/?p=53791
- [s39] [TER] Market research: GMI — https://www.gminsights.com/industry-analysis/semiconductor-process-control-equipment-market ; SNS Insider — https://www.snsinsider.com/reports/semiconductor-defect-inspection-equipment-market-11288 ; Strategic Market Research — https://www.strategicmarketresearch.com/market-report/e-beam-wafer-inspection-system-market
- [s42] [SS] EUV scatterometry programmes: NIST FCMN, 17 Mar 2026 — https://cdn.fs.pathlms.com/nGbQa5KQcWbGA561QHFN?dl=true ; PSI REGINE (EUV2023 abstract) — https://www.euv2023.ptb.de/fileadmin/documents/euv2023/abstracts/O01_Ekinci.pdf ; imec AttoLab (EPJ Web Conf. 2025) — https://www.epj-conferences.org/10.1051/epjconf/202533501019
- [s43] [SS] TSMC Q3 2025 call transcript, 17 Oct 2025

[s1]: https://semiengineering.com/shrinking-hybrid-bonding-pitches-push-inspection-limits/
[s2]: https://semiengineering.com/metrology-under-pressure-detecting-defects-in-fine-pitch-hybrid-bonding/
[s3]: https://semiengineering.com/can-fine-pitch-hybrid-bonding-go-high-volume/
[s4]: https://semiengineering.com/finding-critical-defects-before-they-become-costly-failures-process-control-for-hybrid-bonding-and-advanced-packaging/
[s5]: https://semiengineering.com/tag/metrology/
[s6]: https://www.eetimes.com/hybrid-bonding-comes-of-age-slowly-and-collectively/
[s7]: https://trendforce.com/news/2026/03/06/news-industry-weigh-825-900-%CE%BCm-hbm-thickness-for-20-high-stacks-potentially-slowing-hybrid-bonding
[s8]: https://www.trendforce.com/news/2026/04/01/news-jedec-reportedly-plans-to-relax-hbm-height-specs-to-900%C2%B5m-potentially-slowing-hybrid-bonding-adoption/
[s9]: https://www.trendforce.com/news/2026/07/07/news-samsung-sk-hynix-reportedly-reconsider-hybrid-bonding-timeline-16-high-hbm4e-may-be-earliest-adoption/
[s10]: https://newsletter.semianalysis.com/p/ectc2026
[s11]: https://x.com/SemiAnalysis_/status/2108256589559865346
[s12]: https://bits-chips.com/article/besi-faces-longer-wait-as-sk-hynix-pushes-hybrid-bonding-to-hbm5/
[s13]: https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-says-hybrid-bonding-wont-be-ready-for-hbm4e-as-ai-memory-runs-into-a-775-micron-ceiling
[s14]: https://www.tomshardware.com/tech-industry/semiconductors/hybrid-bonding-roadmap-examined
[s15]: https://mlq.ai/news/sk-hynix-pushes-hybrid-bonding-to-hbm5-as-stacked-ai-memory-reaches-its-height-limit/
[s16]: https://biz.heraldcorp.com/article/10878775
[s17]: https://en.sedaily.com/finance/2026/04/06/sk-hynix-eyes-hbm5-launch-by-2029-with-hybrid-bonding
[s18]: https://technologies.org/samsung-unveils-zhbm-and-400-layer-v10-bv-nand-at-fms-2026-and-wafer-bonding-is-the-common-thread/
[s19]: https://ectc.net/wp-content/uploads/2023/03/2026-ECTC-REVISED-Technical-Tipsheet-with-images.pdf
[s20]: https://eps.ieee.org/wp-content/uploads/2026/03/Emerging-Technologies_-TC-Article_Hybrid-Bonding_031126_for_EPS_newsletter_FINAL.pdf
[s21]: https://irds.ieee.org/images/files/pdf/2024/2024IRDS_MET.pdf
[s22]: https://spie.org/Publications/Proceedings/Volume/13981
[s23]: https://www.novami.com/wp-content/uploads/2026/04/13981-16-timoney-spie-alp-2026-vts-ml-cu-recess-final.pdf
[s24]: https://research.ibm.com/blog/spie-2026-below-2-nm
[s26]: https://www.lithoguru.com/scientist/conferences/spie_diary_2026.html
[s27]: https://www.light-am.com/article/doi/10.37188/lam.2026.112
[s28]: https://www.light-am.com/article/pdf/preview/LAM2026050195.pdf
[s29]: https://www.fool.com/earnings/call-transcripts/2026/10/29/kla-klac-q1-2027-earnings-call-transcript/
[s30]: https://futurumgroup.com/insights/applied-materials-q3-fy-2026-advanced-packaging-and-dram-accelerate-growth/
[s31]: https://bits-chips.com/article/invisix-steps-out-from-under-asmls-wings-with-soft-x-ray-metrology-bet/
[s32]: https://www.design-reuse.com/news/202531015-tsmc-completes-development-of-1-6nm-a16-process-mass-production-set-for-q4/
[s33]: https://en.wikipedia.org/wiki/2_nm_process
[s34]: https://www.tomshardware.com/pc-components/cpus/we-cant-completely-vacate-the-client-market-says-intel-amid-wafer-supply-shortages-nova-lake-still-on-track-for-late-2026-release-14a-in-2028
[s35]: https://www.trendforce.com/news/2026/04/24/news-samsung-reportedly-produces-sub-10nm-10a-dram-working-die-using-4f-square-and-vct-targets-2028-production/
[s36]: https://semiwiki.com/forum/threads/isscc-2026-samsung-electronics-demonstrated-a-16gb-dram.24808/latest
[s37]: https://www.tweaktown.com/news/114236/micron-reveals-ddr6-lpddr6-hbm-and-nand-roadmap-as-ai-memory-demand-keeps-climbing/index.html
[s38]: https://www.tomshardware.com/tech-industry/semiconductors/rapidus-targets-2nm-mass-production-in-2027-with-a-four-times-capacity-ramp
[s39]: https://www.gminsights.com/industry-analysis/semiconductor-process-control-equipment-market
[s42]: https://cdn.fs.pathlms.com/nGbQa5KQcWbGA561QHFN?dl=true
[s43]: https://www.fool.com/earnings/call-transcripts/2025/10/17/tsmc-tsm-q3-2025-earnings-call-transcript
