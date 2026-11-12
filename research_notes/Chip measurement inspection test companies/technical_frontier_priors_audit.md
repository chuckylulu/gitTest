# Technical frontier and priors audit: measuring and inspecting buried features in 3D and bonded chips

Research date: **12 November 2026**. Status: **first write (interim)**. Parts A and B are mostly complete; Part C (logic-node ramps, TSMC/Intel/Samsung bond-pitch roadmaps, Micron, JEDEC, vertical-channel DRAM) is **incomplete** and is being filled in. Labels: **[CC]** = company claim with no outside confirmation found; **[SEC]** = secondary report (press, analyst, aggregator); **[TER]** = tertiary (Wikipedia, market-research summaries). Coverage caveats: SPIE papers were read only as abstracts on the volume page, except the IBM/Nova paper, which was read in full. The SemiAnalysis ECTC roundup is partly paywalled. Equipment-maker earnings material is limited to KLA's October 2026 call, read through an auto-generated transcript.

## Summary verdict table

| # | Item | Verdict | Key source | Date |
|---|---|---|---|---|
| A1 | SE: buried post-bond defects are one of the hardest problems as pitch shrinks below the 4-9 µm production range | **Confirmed** (exact wording: "one of the most significant challenges"; "today's production levels of 4 to 9 µm") | Semiconductor Engineering, L. Peters | 10 Nov 2026 |
| A2 | EE Times: no roadmap for probing bond arrays below ~25 µm | **Confirmed; date corrected** (Jan 2026; the wording is the article's paraphrase of imec's view, "absence of any realistic roadmap") | EE Times, P. Brans | 26 Jan 2026 |
| A3a | TrendForce: hybrid bonding in HBM slipped to 16-high HBM4E at the earliest | **Confirmed for July 2026; now partly outdated, so corrected**: SK hynix said in Aug 2026 that hybrid bonding will not reach HBM4E (HBM5 at the earliest) | TrendForce [SEC]; Bits&Chips [SEC]; Tom's Hardware [SEC] | 7 Jul 2026; 24-26 Aug 2026 |
| A3b | SemiAnalysis ECTC 2026: Samsung reported hybrid bonding cuts thermal resistance by only 12-13%, so 20-24-high needs new approaches | **Corrected**: 12.2%/12.9% is the *internal HBM* thermal resistance in a 2-GPU + 8-HBM package model. The stack-level cut is ~19% (22.3%/29.1% at 2x/4x pad density) and the total-HBM cut only 3.5%/7.7%. "16-hi acceptable; 20-hi/24-hi need new approaches" is confirmed | SemiAnalysis (Ahmad, Wong, Patel et al.) [SEC] | 2 Jul 2026 |
| A4a | SPIE 2026: X-ray scattering and optical data fused with physics-informed ML | **Confirmed** (CD-SAXS + spectroscopic ellipsometry, physics-informed ML, 3D NAND, R² > 0.95 against SEM) | Proc. SPIE 13981 | Feb 2026 |
| A4b | Same volume names scarce training data as the brake | **Confirmed with nuance**: several abstracts name scarce reference or labelled data, but the keynote (per Chris Mack) called *trust* the biggest roadblock | Proc. SPIE 13981; lithoguru diary | Feb 2026 |
| A4c | IBM Research maps optical spectra straight to reference values with no optical model | **Corrected**: a joint IBM Research + Nova paper; "modeless" ML with physics-based spectral filtering (VTS); the reference is **AFM** (non-destructive), not EM cross-sections; trained on 15 wafers x 5 dies; blind-test R² ~0.8 at best and 0.35 at worst | Timoney et al., SPIE 13981-16 | Feb 2026 (PDF Apr 2026) |
| A5 | LAM 2026: table-top computational EUV microscope resolved 43.5 nm half-pitch on a real chip | **Confirmed with nuance**: 17.9 nm HHG grazing-reflection ptychography; 43.5 nm = diffraction limit = one reconstructed pixel; chip grating linewidth 42.7 nm by SEM; surface features only; not yet usable online | Chen et al., Light: Adv. Manuf. 7:112 | Online 9 Sep 2026 |
| B1 | Measurement steps per leading-edge wafer keep rising through 2028 (75%) | **Supported only by vendor statements; no node-level counts found** | KLA call [CC]; IRDS 2024 | 28 Oct 2026 |
| B2 | Buried bond-interface defects still a leading yield limiter in 2030 (60%) | **Mixed**: the detection gap is confirmed, but the named root causes are pre-bond (CMP, Cu recess, particles), research-scale W2W yields are 97-98%, and hybrid bonding in HBM slips to ~2028-30 | SE; IRDS 2024; IEEE EPS; ECTC 2026 | 2024-2026 |
| B3 | Computed methods take share from direct imaging 2029-33 (45%) | **Counter-evidence stronger today**: e-beam is broadening; inline CD-SAXS is limited to memory high-aspect-ratio work; logic needs >=100x brighter X-ray sources | IRDS 2024; SPIE 13981; KLA | 2024-2026 |
| B4 | Tools per wafer may fall after 2030 (35%) | **No supporting roadmap or vendor statement found**; virtual metrology and sampling optimisation exist, but vendors project growth | SPIE 13981; IRDS 2024; KLA | 2024-2026 |
| B5 | AI changes software and economics before physics | **Partly contradicted**: in dose- or photon-limited cases, learned or computational reconstruction changes what can be measured at all | SPIE 13981; LAM 2026 | 2026 |
| B6 | Learned denoising is safe for the expected and risky for the unexpected | **Supported qualitatively; no quantitative test found**; deep-learning enhancement is already applied to defect detection | SPIE 13981; lithoguru | 2026 |
| C | Roadmap facts | **Partly complete** (HBM done; logic and pitch roadmaps in progress) | see Part C | — |
| D | Contradictions with the background | 10 points listed | see Part D | — |

## A. Verification of background evidence items

### Takeaway
All five items trace to real 2026 sources. Two need correcting: the SemiAnalysis "12-13%" picks one of several thermal metrics, and the IBM "no optical model" case uses AFM, not EM cross-sections, and keeps physics-based filtering. One is now outdated: TrendForce's HBM4E timing has been overtaken by SK hynix's August 2026 statement.

### Cited Findings
**A1, Semiconductor Engineering, November 2026.**
- "Shrinking Hybrid Bonding Pitches Push Inspection Limits" (Laura Peters, 10 Nov 2026). Exact text: inspection struggles "as hybrid bonding pitches continue to scale down below today's production levels of 4 to 9 µm"; "Detecting buried defects after bonding remains one of the most significant challenges"; "no single technique provides the resolution, sensitivity, wafer coverage, and throughput required to identify every yield-critical defect." Key takeaways frame pitches as approaching "5 µm and below". — [SE, 10 Nov 2026](https://semiengineering.com/shrinking-hybrid-bonding-pitches-push-inspection-limits/)
- Method limits in the same article:
  - Acoustic micro-imaging (~200 MHz) gives the highest acoustic resolution, but "Ultrasound does not travel through air gaps that have a thickness down to about 0.1 µm". A 165 MHz transducer "gets you down to a resolution of 12 microns", and a 5 µm defect can be detected but not measured accurately (B. Schackmuth, Nordson). Acoustic imaging is currently done after full assembly.
  - X-ray: "A resolution of 150 nm has been demonstrated". Bruker XRDI does full-wafer inspection "at ~20wph" with zero edge exclusion [CC].
  - IR checks post-bond pad alignment through silicon.
  - Defect-size requirements reach "as low as 50 nm"; Cu pads are recessed 2-5 nm, controlled "within 2 nm across the wafer"; roughness must be ~0.5 nm RMS. "Even a single particle can delaminate the top wafer."
  - Micro-inspection samples "maybe two to five wafers per lot" (E. Akomer, Microtronic).
  - The article describes no AI/ML use in hybrid-bond inspection. — [SE, 10 Nov 2026](https://semiengineering.com/shrinking-hybrid-bonding-pitches-push-inspection-limits/)
- Earlier SE piece (G. Haley, 12 Aug 2025): "Optical methods are inherently limited by their resolution and can struggle with buried interfaces or subsurface voids"; acoustic, IR and X-ray "typically lack the resolution or contrast needed to detect nanoscale voids"; electrical test structures give "only partial wafer coverage". Onto: customers push "down to 6µm, 5µm, and even smaller pitches". — [SE, 12 Aug 2025](https://semiengineering.com/metrology-under-pressure-detecting-defects-in-fine-pitch-hybrid-bonding/)

**A2, EE Times.**
- "Hybrid Bonding Comes of Age Slowly and Collectively" (Pat Brans, **26 Jan 2026**). "The absence of any realistic roadmap for probing dense hybrid-bond arrays below ~25 µm pitch" forces a rethink of pre-bond test. Erik Jan Marinissen (imec): "From a test perspective, this technology is under development and not mature at all." "Dedicated sacrificial probe pads may offer a workaround, but at the cost of additional area and process complexity." Also: "A single particle can create a stand-off height that leads to many open defects, sometimes across die boundaries" (Marinissen). CMP is "the single largest source of yield variability in high-volume manufacturing" (V. Dubey, Fraunhofer ENAS). W2W bonding is "well established in high-volume production for image sensors and some memory devices", while die-to-wafer is "the central battleground". — [EE Times, 26 Jan 2026](https://www.eetimes.com/hybrid-bonding-comes-of-age-slowly-and-collectively/)
- IRDS 2024 lists "Fine pitch probing methods" and "Best testing and binning methods - known good dies" among the hybrid-bonding metrology requirements (section 5.12.2). — [IRDS 2024 Metrology](https://irds.ieee.org/images/files/pdf/2024/2024IRDS_MET.pdf)

**A3a, TrendForce on HBM4E timing.**
- TrendForce, 7 Jul 2026, citing ZDNet Korea [SEC]: industry forecasts point to "16-high HBM4E as the 'earliest likely adoption point'"; "12-high HBM4E products are still expected to remain the mainstream offering"; both makers kept thermo-compression bonding for HBM4; Samsung's Heat Path Block and SK hynix's iHBM are being tested for HBM5; the delay is driven by relaxed thickness limits and "delayed demand from key customers, including NVIDIA, for higher-stack-count HBM". — [TrendForce, 7 Jul 2026](https://www.trendforce.com/news/2026/07/07/news-samsung-sk-hynix-reportedly-reconsider-hybrid-bonding-timeline-16-high-hbm4e-may-be-earliest-adoption/)
- TrendForce, 6 Mar 2026, citing ZDNet [SEC]: Samsung "is expected to introduce the technology only partially at the earliest in 16-layer HBM4E products"; hybrid bonding "has not yet been deployed in mass production for HBM manufacturing"; "yields can decline when bonding up to 20 stacked chips." — [TrendForce, 6 Mar 2026](https://trendforce.com/news/2026/03/06/news-industry-weigh-825-900-%CE%BCm-hbm-thickness-for-20-high-stacks-potentially-slowing-hybrid-bonding)
- **Superseding update**: at Hot Chips (23 Aug 2026), SK hynix "pushed the introduction of hybrid bonding in high-bandwidth memory (HBM) back by another generation", extending "the life of microbump technology through HBM4E". VP Jaesik Lee said "producing reliable copper-to-copper bonds across 16 or 20 stacked memory dies remains a major manufacturing challenge". — [Bits&Chips, 26 Aug 2026](https://bits-chips.com/article/besi-faces-longer-wait-as-sk-hynix-pushes-hybrid-bonding-to-hbm5/) [SEC]; [Tom's Hardware, 24 Aug 2026](https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-says-hybrid-bonding-wont-be-ready-for-hbm4e-as-ai-memory-runs-into-a-775-micron-ceiling) [SEC]; summary: "Hybrid bonding remains in research for 20-layer-and-higher stacks and is not expected to reach HBM4E" — [MLQ, 25 Aug 2026](https://mlq.ai/news/sk-hynix-pushes-hybrid-bonding-to-hbm5-as-stacked-ai-memory-reaches-its-height-limit/) [SEC, AI-written summary]

**A3b, SemiAnalysis ECTC 2026 roundup (2 Jul 2026; partly paywalled) [SEC].**
- Samsung compared hybrid copper bonding with thermo-compression bonding in a 2.5D package with 2 GPU dies and 8 HBM stacks. Reported figures:
  - Internal HBM thermal resistance: "drops by 12.2% with air cooling and 12.9% with liquid cooling."
  - Total HBM thermal resistance: "drops by 3.5% with air cooling and 7.7% with liquid cooling."
  - Stack level: "Baseline HCB reduces stack thermal resistance by ~19% versus TCB", rising "to 22.3% at 2× pad density and 29.1% at 4× pad density."
  - Package effect: hybrid bonding "allows inlet temperatures to rise by 1-2 °C at constant package power or package power to increase by ~4%", with cooling power down ~7%.
  - Conclusion: "With 16-hi HBM, the thermal resistance is still acceptable" but for "20-hi and 24-hi HBM, new approaches are needed." — [SemiAnalysis, 2 Jul 2026](https://newsletter.semianalysis.com/p/ectc2026)
- Samsung's own public claim is "over 20% improvement in thermal resistance versus TC bonding" and support for "stacks exceeding 16 layers" (NVIDIA GTC, March 2026) [CC]. — [TrendForce, 1 Apr 2026](https://www.trendforce.com/news/2026/04/01/news-jedec-reportedly-plans-to-relax-hbm-height-specs-to-900%C2%B5m-potentially-slowing-hybrid-bonding-adoption/)

**A4, SPIE Advanced Lithography + Patterning 2026 (22-26 Feb 2026, San Jose); Proc. SPIE 13981 "Metrology, Inspection, and Process Control XL".**
- X-ray plus optical fusion: "High-resolution 3D NAND profile measurement using optical metrology and machine learning" (D. Choi, Y. Jang, S. Seo et al.; DOI 10.1117/12.3090491) combines "CDSAXS profile data with spectroscopic ellipsometer (SE) spectra using physics-informed machine learning". All sites reach R² > 0.95 against SEM references (average slope 0.899). — [SPIE vol. 13981](https://spie.org/Publications/Proceedings/Volume/13981)
- "Leveraging AI and ML in multimodal combined and hybrid metrology" (M.-A. Henn, A. Chew, P. Bajcsy et al.) fuses OCD with a second modality using ensemble and physics-informed neural networks: "ensemble learning methods consistently outperform traditional methods with only one model." — [SPIE vol. 13981](https://spie.org/Publications/Proceedings/Volume/13981)
- Data scarcity, in the same volume:
  - X-ray CD ML (A. Baranovskiy, Y. Amasay, P. Gin et al.): "A key challenge is the limited availability of high-quality reference data."
  - SEM synthesis: "hindered by the scarcity of high-quality training data."
  - Layout-guided SEM contours: "suffer from scarcity of annotated (labeled) images."
  - Few-shot SEMformer: "labeled 3D heights are extremely scarce", MAE ≈ 24 nm.
  - Virtual-metrology tool matching: "physical metrology is sparse and requires a considerable amount of time to reach statistical significance."
  - Overlay ML trained "using only 3–5 wafers". — [SPIE vol. 13981](https://spie.org/Publications/Proceedings/Volume/13981)
- Keynote framing: Steve McCandless (Micron), as reported by Chris Mack, named "the biggest roadblock to the widespread use of AI in metrology: trust". Mack on extrapolation: "I have my doubts." Many talks used ML. — [lithoguru SPIE 2026 diary](https://www.lithoguru.com/scientist/conferences/spie_diary_2026.html) [SEC, expert commentary]
- IBM paper: Timoney, Schoeche, Polomoff, Mittelstaedt, Malley, Sherwood, Omrani, Schmidt (IBM Research Albany), Cepler and Isbester (Nova), Turovets (Nova), "Inline monitoring of hybrid bonding Cu recess with Vertical Traveling Scatterometry machine learning" (SPIE 13981-16).
  - Keywords include "modeless" and "reference metrology". "Unlike conventional OCD ML that requires detailed underlayer modeling or pre and post delta measurements, this VTS-ML approach applies a single model applicable to both top and bottom wafer categories."
  - Reference was **AFM**: "Reference data from 5 measurement dies across 15 wafers", ~4 nm training range, tested on 22 blind wafers. Blind-test R² = 0.35 at cutoff A ("insufficiently trained") and ~0.8 at cutoffs B and C.
  - Requirement: ~0.1 nm sensitivity, with surface smoothness <1 nm.
  - Conclusion: "leveraging limited reference metrology in an R&D environment". — [IBM/Nova paper PDF](https://www.novami.com/wp-content/uploads/2026/04/13981-16-timoney-spie-alp-2026-vts-ml-cu-recess-final.pdf); talk listed 24 Feb 2026 — [IBM Research blog, 23 Feb 2026](https://research.ibm.com/blog/spie-2026-below-2-nm)

**A5, Light: Advanced Manufacturing 2026.**
- Chen Y., Xu H., Wang Q., Li Y. … Shi Y. (corresponding), Fan Z., "Table-top extreme ultraviolet grazing-reflection ptychography with full-pose self-calibration", Light: Adv. Manuf. 7:112, DOI 10.37188/lam.2026.112. Received 2 Jun, accepted 30 Jun, published online 9 Sep 2026. Institutions: UCAS, CAS institutes (AIR, IoP, SIOM), Jihua Lab and others. — [LAM article page](https://www.light-am.com/article/doi/10.37188/lam.2026.112)
- Setup: 17.9 nm high-harmonic source, 70° grazing incidence, NA 0.19 x 0.095, reconstructed pixel 43.5 x 70.0 nm.
- On the real chip: grating contrast 0.49 with full-pose calibration versus 0.13 without, and "Fig. S10b shows an actual grating linewidth of 42.7 nm … This confirms that the system resolution (half-pitch) reaches a diffraction limit of 43.5 nm." Grating spacing came out 2.22 µm against 2.26 µm by SEM (1.9% error).
- On the custom wafer: "features are not fully resolved even in full-pose reconstruction", with the minimum grating at 82.6 nm FWHM.
- Limits: single illumination angle; "practical deployment in online settings is limited by the computational speed of phase retrieval algorithms"; ~10⁷ photons needed for self-calibration.
- The paper's Table 3 lists an earlier table-top reflection system at 40 nm half-pitch (without real-chip inspection) — so the paper's "best resolution reported to date" claim needs that qualifier. — [LAM PDF](https://www.light-am.com/article/pdf/preview/LAM2026050195.pdf)

### Inferences
- A1 and A2 are sound, but A2 is ten months old and its "no roadmap" is a journalist's framing of a single imec interview, not a roadmap-body statement.
- A3b's "only 12-13%" undersells the stack-level effect (~19-29%) and oversells the package-level effect (3.5-7.7% total). The robust point is SemiAnalysis's: thermal benefit alone does not carry 20-24-high stacks.
- A4c undercuts part of the background: the showcase "no optical model" case used non-destructive AFM as ground truth, on a near-surface parameter. It is not evidence about buried 3D features calibrated against TEM.
- A5 shows computation recovering resolution from imperfect hardware, but at 43.5 nm on surface features. That is far from the 10-20 nm leading-edge CDs, and nothing here is buried.

### Gaps
- Full SPIE papers other than IBM/Nova are paywalled; author affiliations were not visible.
- The rest of the SemiAnalysis article is paywalled.
- No 2026 update on probing below 25 µm was found (SWTest 2026 not checked).

## B. Priors tested against current evidence

### Takeaway
- B1 (rising steps): vendor-supported but unquantified.
- B2 (bond defects in 2030): plausible, but the cause sits mostly before bonding, and HBM adoption is delayed.
- B3 (computed methods take share): weaker than e-beam's momentum.
- B4 (fewer tools after 2030): unsupported by any roadmap.
- B5 (AI before physics): partly wrong in dose-limited regimes.
- B6 (denoising risk): plausible but untested in public.

### Cited Findings
**B1, measurement steps rising through 2028 (75%).**
- For: KLA, Q1 FY2027 call, 28 Oct 2026 [CC; auto-generated transcript]:
  - R. Wallace: "Intensity is definitely going up."
  - B. Higgins: "In some products we see intensity levels in DRAM that are similar to leading edge logic"; "an uplift in process control intensity and conventional memory"; HBM dynamics ("less redundancy, IO counts, logic. And base die") lift intensity; legacy intensity is lower than leading edge.
  - Advanced packaging needs "more sampling steps because of the value of the die" and moves "from micron level sensitivity down to the 100 nanometer type sensitivity".
  - Advanced-packaging process-control revenue is "on track to hit $1.1 billion or more", up "more than 70%" year on year.
  - WFE in the "mid-$150 billion range" for 2026 and ">$200 billion" for 2027; 2030 framework "$220 billion plus or minus $20 billion". — [Motley Fool transcript, 29 Oct 2026](https://www.fool.com/earnings/call-transcripts/2026/10/29/kla-klac-q1-2027-earnings-call-transcript/)
- KLA did not give 2 nm, GAA or backside-power intensity figures on the call (search summary and transcript extract). — same source
- IRDS 2024 near-term challenges (2024-2029): nanosheet and CFET "require an increased need for in-line metrology for dimensional, compositional, and doping measurements at the atomistic scale"; the backside power network "requires new concepts of metrology over FEOL, BEOL, and A&P". — [IRDS 2024 MET, Table MET-1](https://irds.ieee.org/images/files/pdf/2024/2024IRDS_MET.pdf)
- New GAA-specific steps at SPIE 2026: "High landing energy e-beam inspection as an in-line blocked nanowire release metric for GAA yield ramp" (Patterson et al.); "Gate leakage evaluation of GAA transistors using SEMs" (Shirasaki et al.). DRAM: e-beam inspection for word-line defects, because bright-field and voltage contrast "lack the sensitivity". — [SPIE vol. 13981](https://spie.org/Publications/Proceedings/Volume/13981)
- Counter-evidence:
  - Learned speedups cut time per measurement, not the number of steps: an X-ray CD system cut "data-acquisition time by more than 6X" and AOIs "from 13 to just 2"; GAN denoising cut X-ray CD time "by up to 40%".
  - Virtual metrology already runs in 3D NAND mass production: "MMT is a key virtual metrology (VM) enabler for mass production" (Cho et al.). — [SPIE vol. 13981](https://spie.org/Publications/Proceedings/Volume/13981)
  - Memory de-spec slows the stack-height push: Nvidia is reportedly weighing 8/12-high HBM4 and 8-high HBM4E for Rubin Ultra. — [Herald Business, 20 Sep 2026](https://biz.heraldcorp.com/article/10878775) [SEC]

**B2, buried bond-interface defects a leading yield limiter in 2030 (60%).**
- For:
  - IRDS 2024: anneal "nano-voids" are "currently only detectable by off-line TEM". Acoustic resolution for bonded-wafer voids "approaches 60 microns (using a 110 MHz transducer)", and thinning the wafer to improve it is "not a manufacturable solution". IR review cannot cover 100% of a wafer. — [IRDS 2024 MET §5.6.2](https://irds.ieee.org/images/files/pdf/2024/2024IRDS_MET.pdf)
  - IEEE EPS summary of the ECTC 2025 special session (Mar 2026): confocal acoustic microscopy has "a resolution limit of approximately 10 µm, often insufficient for detecting voids in contemporary hybrid-bonded devices". It names the need to "detect sub-micron size voiding at the Cu-Cu interface" and in-situ feedback. — [IEEE EPS, Mar 2026](https://eps.ieee.org/wp-content/uploads/2026/03/Emerging-Technologies_-TC-Article_Hybrid-Bonding_031126_for_EPS_newsletter_FINAL.pdf)
  - SE (10 Nov 2026): no single technique suffices. — [SE](https://semiengineering.com/shrinking-hybrid-bonding-pitches-push-inspection-limits/)
  - Intel's ECTC 2026 low-temperature fine-grain Cu W2W gave electrical yield "around 60% in two of three samples" (a lower bound), with opens traced to benzotriazole residue at the interface. — [SemiAnalysis, 2 Jul 2026](https://newsletter.semianalysis.com/p/ectc2026)
  - SK hynix requires "a yield of 90 to 98 percent" and "a lifespan of three to five years" before adopting hybrid bonding (Kim Ji-hoon, SEMI panel, 9 Sep 2026). — [Herald Business, 20 Sep 2026](https://biz.heraldcorp.com/article/10878775) [SEC]
- Against:
  - Applied Materials (ECTC 2026, paper 18.4): "450nm pitch copper hybrid bonding achieving 98% yield across 20 million via links" [CC]. "Parts-per-million level open defects" were found by electron-beam absorbed current, with TEM-EELS showing a carbon-rich interface layer. — [ECTC 2026 tipsheet, 20 May 2026](https://ectc.net/wp-content/uploads/2023/03/2026-ECTC-REVISED-Technical-Tipsheet-with-images.pdf)
  - CEA-Leti reported >97% yield after a 100 °C anneal without plasma activation. — [SemiAnalysis](https://newsletter.semianalysis.com/p/ectc2026)
  - Panel consensus: "Pre-bond surface topography, Cu recess, oxide planarization, and surface defectivity remain primary contributors to bonding failure and yield loss" — the root causes are visible before bonding. — [IEEE EPS](https://eps.ieee.org/wp-content/uploads/2026/03/Emerging-Technologies_-TC-Article_Hybrid-Bonding_031126_for_EPS_newsletter_FINAL.pdf)
  - IRDS also says "a number of SAM tools" already support in-line *macro*-void metrology for bonded pairs in HVM. — [IRDS 2024](https://irds.ieee.org/images/files/pdf/2024/2024IRDS_MET.pdf)
- Emerging methods: picosecond laser acoustics for buried voids in HBM (Mehendale et al., SPIE 2026); e-beam process control for HBM hybrid bonding (Gal et al.); four-direction BSE SEM for Cu-pad recess, calibrated "with TEM-measured recess on 200-nm pads" (Kasai et al.). — [SPIE vol. 13981](https://spie.org/Publications/Proceedings/Volume/13981)

**B3, computed methods take share from direct imaging 2029-2033 (45%).**
- X-ray status (IRDS 2024):
  - CD-SAXS "has the required throughput for characterization of HAR contact holes and commercially available in-line tools have recently been introduced to the fab" (3D NAND and DRAM).
  - For logic, in-line use "will require significant improvements in compact X-ray sources to get the required throughput (<1 min) with a small spot size (<100 µm)"; "Current X-ray sources do not have a high enough X-ray brilliance"; future sources need "at least 100[x]" brightness over lab sources (symbol lost in extraction). — [IRDS 2024 MET](https://irds.ieee.org/images/files/pdf/2024/2024IRDS_MET.pdf)
- SPIE 2026 X-ray, soft X-ray and EUV work:
  - X-ray CD measured 3D NAND hole-to-hole distance across "2 full wafers with over 600 measurement sites".
  - Resonant soft X-ray scattering with FEM Maxwell solvers and ML, for CFET-like structures, with TEM as the baseline.
  - Hard-X-ray reflection CD with "sub-nanometer out-of-plane sensitivity".
  - A discharge-plasma soft-X-ray source and new tender/soft X-ray sources.
  - EUV scatterometry posed as Bayesian adaptive experiment design; a UHV EUV Mueller-matrix ellipsometer.
  - EUV mask ptychography at "11.5 nm" and "14 nm (at the wafer)".
  - A CD-SAXS damage caveat: linewidth changed 5% under the beam on EUV resist (Brookhaven/IBM, per Mack). — [SPIE vol. 13981](https://spie.org/Publications/Proceedings/Volume/13981); [lithoguru](https://www.lithoguru.com/scientist/conferences/spie_diary_2026.html)
- E-beam counter-trend at SPIE 2026:
  - Brightness and contrast correction for multibeam-SEM defect inspection.
  - Multicolumn e-beam inspection for EUV reticles.
  - High-kV cold-field-emission overlay in DRAM; high-voltage SEM see-through backscatter metrology.
  - An e-beam tool "capable of massive data collection".
  - ASML's e-beam inspection over areas large enough "to achieve one part per million defect capture rates" (per Mack). — [SPIE vol. 13981](https://spie.org/Publications/Proceedings/Volume/13981); [lithoguru](https://www.lithoguru.com/scientist/conferences/spie_diary_2026.html)
- KLA: "our relevancy with e beam inspection capability and the linkage we have to our optical becomes more pronounced" [CC]. — [KLA transcript](https://www.fool.com/earnings/call-transcripts/2026/10/29/kla-klac-q1-2027-earnings-call-transcript/)
- Market-research summaries call e-beam the fastest-growing inspection segment (~9.7-9.9% CAGR; multibeam 12.5% CAGR 2024-30) [TER, low reliability; segment definitions differ]. — [GMI](https://www.gminsights.com/industry-analysis/semiconductor-process-control-equipment-market); [SNS Insider](https://www.snsinsider.com/reports/semiconductor-defect-inspection-equipment-market-11288); [Strategic Market Research](https://www.strategicmarketresearch.com/market-report/e-beam-wafer-inspection-system-market)
- IRDS 2024: "Existing SEMs and SPMs are considered too slow" for sub-optical defects, and "existing optical techniques lose some sensitivity to defects smaller than 20 nm"; arrayed micro-column SEMs are proposed. — [IRDS 2024](https://irds.ieee.org/images/files/pdf/2024/2024IRDS_MET.pdf)

**B4, tools per wafer may fall after 2030 (35%).**
- For: IRDS 2024 says ML-assisted simulation should ensure "the proper type and number of measurements" and avoid "too many measurements (loss of time and money)", and that "sampling plan optimization is key". — [IRDS 2024](https://irds.ieee.org/images/files/pdf/2024/2024IRDS_MET.pdf)
- Also for: virtual metrology in 3D NAND mass production; ASML's "computational guided dynamic sampling e-beam inspection" improved defective-die capture "by up to 4.3x". — [SPIE vol. 13981](https://spie.org/Publications/Proceedings/Volume/13981)
- Against: KLA projects rising intensity and WFE to 2030 [CC]. Virtual metrology still needs sparse physical metrology to reach statistical significance (Kim et al., SPIE 2026). "ML is very good at interpolation, but not so good at extrapolation" (Kizu, per Mack). SE (11 Aug 2026) argues measurements must be re-verified after each physical change (title and summary only). — [KLA](https://www.fool.com/earnings/call-transcripts/2026/10/29/kla-klac-q1-2027-earnings-call-transcript/); [lithoguru](https://www.lithoguru.com/scientist/conferences/spie_diary_2026.html); [SE tag page](https://semiengineering.com/tag/metrology/)
- No roadmap, chipmaker or vendor statement forecasting fewer tools per wafer was found.

**B5, AI changes software and economics before physics.**
- Counter-cases where computation changed what can be measured within a dose or photon budget:
  - Generative-AI denoising for actinic EUV mask inspection reconstructs images "using 30X fewer exposures" (Kim, Long, Dogru et al.).
  - Deep-learning CD-SEM denoising allows fewer frames, mitigating "e-beam-induced damage", with repeatability improving from 0.095 to 0.073 nm (Liu et al.).
  - A CNN restores out-of-focus images for W2W overlay (Lin, Ku).
  - Physics-inspired deep learning extracts LER from noisy SEM images "without any training data with ground-truth edge profiles" (Kizu). — [SPIE vol. 13981](https://spie.org/Publications/Proceedings/Volume/13981)
- In the LAM paper, gradient-based full-pose self-calibration (not ML) raised contrast from 0.13 to 0.49, and "only the full-pose strategy successfully resolved the defects". — [LAM PDF](https://www.light-am.com/article/pdf/preview/LAM2026050195.pdf)

**B6, learned denoising safe for the expected, risky for the unexpected.**
- For:
  - SPIE 2026 "Detection of inference errors in deep learning denoising models and reliability analysis system for SEM metrology" proposes a "Transform Monitoring method that evaluates an indicator for inference error".
  - Fast-adaptation denoising "pre-trains the model on general pattern images and applies fine-tuning for new SEM image pattern types", implying domain-shift risk. — [SPIE vol. 13981](https://spie.org/Publications/Proceedings/Volume/13981)
  - Mack: "Talks on image denoising in particular do not excite me". NIST's Sathe judged synthetic training SEMs "exceptionally simplified and thus not representative". — [lithoguru](https://www.lithoguru.com/scientist/conferences/spie_diary_2026.html)
- Against or mitigating:
  - Learned enhancement is already applied to *finding* unexpected defects: "AI-based detection algorithm for optical inspection of critical defects on 2nm and 1.4nm technology nodes" (deep-learning image enhancement); generative denoising in EUV mask defect inspection.
  - Diffusion models detect SEM defects "without the need for labeled defect data".
  - Intel reported reduced false defects in optical inspection (per Mack). — [SPIE vol. 13981](https://spie.org/Publications/Proceedings/Volume/13981); [lithoguru](https://www.lithoguru.com/scientist/conferences/spie_diary_2026.html)

### Inferences
- B1 at 75% looks reasonable for memory and packaging, but it rests on KLA's statements alone; nothing independent quantifies steps for 2 nm, GAA or backside power.
- B2 should be reframed. The 2030 yield limiter is more likely pre-bond surface state and particles, with interface voids as the symptom. Inspection value may move upstream (pre-bond surface), not only to buried-interface imaging.
- B3: the evidence favours "both grow". X-ray and soft-X-ray share gains look confined to memory high-aspect-ratio work until much brighter compact sources exist. E-beam (multibeam, high-voltage, electron-beam absorbed current) is gaining in logic, DRAM and hybrid bonding. I would lower the prior.
- B4: no evidence for it; the 35% looks high relative to the evidence, though it is a post-2030 claim.
- B5: needs rewording: "AI changes the information extracted per dose/photon before it changes probe physics." In dose-limited regimes this does change what can be measured.

### Gaps
- No statements were retrieved from Applied Materials, Lam Research or ASML on process-control intensity by node, and no third-party process-control share of WFE by node.
- ASML, PSI, imec, Samsung and KLA 2026 programme status for EUV/soft-X-ray scatterometry and coherent diffraction imaging was not retrieved.
- No quantitative study of missed novel defects caused by denoising was found.
- No IEDM 2025 or IITC 2025/2026 hybrid-bonding yield data was retrieved.

## C. Roadmap facts (dated) — INCOMPLETE

### Takeaway
Hybrid bonding in HBM has moved from "HBM4" to "HBM4E at the earliest (Samsung, partial)" and then "HBM5 at the earliest (SK hynix)", because JEDEC height relief and MR-MUF/TC-NCF extensions removed the urgency. W2W hybrid bonding is already in volume in 3D NAND. Logic backside power is in volume at Intel.

### Cited Findings
- **SK hynix** (Hot Chips, 23 Aug 2026):
  - 12-high HBM4 is in mass production; 16-high HBM4 is in customer qualification (48 GB). The 16-high design hits the 775 µm cap with ~50 µm core dies.
  - 12-high HBM4E samples use Advanced MR-MUF; hybrid bonding is "in research" for 20-high and above; HBM5 is the earliest hybrid-bonding generation [CC]. — [MLQ, 25 Aug 2026](https://mlq.ai/news/sk-hynix-pushes-hybrid-bonding-to-hbm5-as-stacked-ai-memory-reaches-its-height-limit/) [SEC]; [Bits&Chips](https://bits-chips.com/article/besi-faces-longer-wait-as-sk-hynix-pushes-hybrid-bonding-to-hbm5/) [SEC]
  - Counterpoint expects SK hynix HBM5 "around 2029 to 2030". — [Seoul Economic Daily, 6 Apr 2026](https://en.sedaily.com/finance/2026/04/06/sk-hynix-eyes-hbm5-launch-by-2029-with-hybrid-bonding) [SEC]
  - Lee Kang-wook (SK hynix): hybrid bonding "will be essential for HBM stacks of 20 layers or more" (Mar 2026). — [TrendForce, 1 Apr 2026](https://www.trendforce.com/news/2026/04/01/news-jedec-reportedly-plans-to-relax-hbm-height-specs-to-900%C2%B5m-potentially-slowing-hybrid-bonding-adoption/) [SEC]
- **Samsung**:
  - HBM4 mass production from Feb 2026 (1c DRAM, 4 nm base die); HBM4E samples shipped May 2026; >400-layer V10 NAND uses wafer bonding; zHBM is a concept only [CC]. — [technologies.org, 5 Aug 2026](https://technologies.org/samsung-unveils-zhbm-and-400-layer-v10-bv-nand-at-fms-2026-and-wafer-bonding-is-the-common-thread/) [SEC]
  - Partial hybrid bonding at 16-high HBM4E at the earliest. — [TrendForce, 6 Mar 2026](https://trendforce.com/news/2026/03/06/news-industry-weigh-825-900-%CE%BCm-hbm-thickness-for-20-high-stacks-potentially-slowing-hybrid-bonding) [SEC]
  - Began introducing hybrid-bond inspection equipment, with an Onto Innovation joint development programme (The Elec via TrendForce). — [TrendForce, 1 Apr 2026](https://www.trendforce.com/news/2026/04/01/news-jedec-reportedly-plans-to-relax-hbm-height-specs-to-900%C2%B5m-potentially-slowing-hybrid-bonding-adoption/) [SEC]
- **Micron**: no hybrid-bonding HBM date found in primary sources — **could not verify**.
- **JEDEC heights**: 720 µm through HBM3E; 775 µm for HBM4.
  - Under discussion: ~900 µm "starting with seventh-generation HBM4E" (Newsis); 825-900 µm (ZDNet, Mar 2026); "around 900 micrometers to as much as 1,000 micrometers" including 20-high HBM5 (ZDNet, Jul 2026).
  - No JEDEC publication confirming a decision was found. — [TrendForce, 1 Apr 2026](https://www.trendforce.com/news/2026/04/01/news-jedec-reportedly-plans-to-relax-hbm-height-specs-to-900%C2%B5m-potentially-slowing-hybrid-bonding-adoption/); [TrendForce, 7 Jul 2026](https://www.trendforce.com/news/2026/07/07/news-samsung-sk-hynix-reportedly-reconsider-hybrid-bonding-timeline-16-high-hbm4e-may-be-earliest-adoption/) [SEC]
- **HBM interconnect today**: "HBM is in mass production with 20µm pitch and 5µm stack spacing"; the next generation is expected at ~10 µm I/O pitch. — [ECTC 2026 tipsheet](https://ectc.net/wp-content/uploads/2023/03/2026-ECTC-REVISED-Technical-Tipsheet-with-images.pdf)
- **Hybrid bonding in NAND**:
  - YMTC Xtacking (W2W, 3D NAND) since 2018. — [IEEE EPS](https://eps.ieee.org/wp-content/uploads/2026/03/Emerging-Technologies_-TC-Article_Hybrid-Bonding_031126_for_EPS_newsletter_FINAL.pdf)
  - Kioxia BiCS 10 (332 layers) bonds CMOS to the array [CC]. — [technologies.org](https://technologies.org/samsung-unveils-zhbm-and-400-layer-v10-bv-nand-at-fms-2026-and-wafer-bonding-is-the-common-thread/) [SEC]
  - Kioxia ECTC 2026: multi-stacked W2W Cu bonding for CBA with sub-800 nm pads. — [ECTC tipsheet](https://ectc.net/wp-content/uploads/2023/03/2026-ECTC-REVISED-Technical-Tipsheet-with-images.pdf)
- **Research pitch records**: 450 nm W2W at 98% yield (Applied Materials, ECTC 2026) [CC]; 400 nm W2W daisy chains (imec, IEDM 2023); IBM D2W/W2W below 2.5 µm (IEDM 2024). — [ECTC tipsheet](https://ectc.net/wp-content/uploads/2023/03/2026-ECTC-REVISED-Technical-Tipsheet-with-images.pdf); [IEEE EPS](https://eps.ieee.org/wp-content/uploads/2026/03/Emerging-Technologies_-TC-Article_Hybrid-Bonding_031126_for_EPS_newsletter_FINAL.pdf); [IBM/Nova paper refs](https://www.novami.com/wp-content/uploads/2026/04/13981-16-timoney-spie-alp-2026-vts-ml-cu-recess-final.pdf)
- **Logic** [TER; Wikipedia, last edited 21 Oct 2026]:
  - TSMC N2 entered volume production in Q4 2025; N2P volume Q3 2026; A16 (backside power) planned for "2026 H2" — current status not verified.
  - Intel 18A (RibbonFET + PowerVia) in HVM since late 2025; Panther Lake shipping Q1 2026; 18A-PT (3D stacking) 2028.
  - Samsung SF2 in mass production 2025 (Exynos 2600), with yields reportedly 50-60% into early 2026; SF2P ramping in 2026.
  - Rapidus began 2 nm GAA prototype production at IIM-1 in July 2025. — [Wikipedia "2 nm process"](https://en.wikipedia.org/wiki/2_nm_process)
- **IRDS 2024 long-term (2030-2037) metrology challenges**: "Nondestructive, production-worthy wafer and mask-level metrology for CD measurement for 3D structures, overlay, defect detection, and analysis"; "Metrology for the characterization of subsurface structures (dimensional and compositional measurements) is needed". — [IRDS 2024 MET](https://irds.ieee.org/images/files/pdf/2024/2024IRDS_MET.pdf)

### Inferences
- The volume need for buried hybrid-bond-interface inspection in HBM likely starts around 2028-2030 (HBM5, 20-high). Until then, HBM inspection demand is driven by microbump, TSV and molded stacks, not Cu-Cu interfaces.

### Gaps (to fill)
TSMC SoIC, Intel Foveros Direct and Samsung pitch roadmaps; TSMC A16 status as of Nov 2026; Intel 14A; Rapidus's 2027 target; vertical-channel DRAM and hybrid bonding in DRAM; the IRDS 2025 edition.

## D. Points where current evidence contradicts the background

1. **Reference data is not only destructive EM cross-sections.** The IBM/Nova "modeless" case used AFM. CD-SAXS serves as a reference for optical ML in 3D NAND. In-fab PFIB-SEM "ground truth" and automated energy-filtered TEM are emerging. TEM remains the anchor for many cases. — [IBM/Nova](https://www.novami.com/wp-content/uploads/2026/04/13981-16-timoney-spie-alp-2026-vts-ml-cu-recess-final.pdf); [SPIE vol. 13981](https://spie.org/Publications/Proceedings/Volume/13981)
2. **"Inferred by matching a simulated signal" is incomplete.** The 2026 trend includes empirical, model-free regression to reference data (VTS-ML: "Unlike conventional OCD ML that requires detailed underlayer modeling…"), alongside physics-informed and FEM-based solvers. — [IBM/Nova](https://www.novami.com/wp-content/uploads/2026/04/13981-16-timoney-spie-alp-2026-vts-ml-cu-recess-final.pdf)
3. **16-layer stacks are not hybrid-bonded.** 16-high HBM4 uses MR-MUF or TC-NCF within 775 µm; hybrid bonding targets 20-high and above (HBM5, ~2028-30). — [MLQ/Tom's Hardware](https://mlq.ai/news/sk-hynix-pushes-hybrid-bonding-to-hbm5-as-stacked-ai-memory-reaches-its-height-limit/)
4. **The TrendForce "16-high HBM4E at the earliest" is outdated for SK hynix** (August 2026: not HBM4E). — [Bits&Chips](https://bits-chips.com/article/besi-faces-longer-wait-as-sk-hynix-pushes-hybrid-bonding-to-hbm5/)
5. **"Only 12-13%" picks one metric.** Stack-level is ~19-29%, total-HBM 3.5-7.7%, and Samsung's own claim is >20%. — [SemiAnalysis](https://newsletter.semianalysis.com/p/ectc2026)
6. **EE Times item date:** January 2026, and it is a journalist's paraphrase of imec. — [EE Times](https://www.eetimes.com/hybrid-bonding-comes-of-age-slowly-and-collectively/)
7. **The EUV microscope result is surface-only, at 43.5 nm, single-angle and offline.** It is not evidence of computed imaging on buried or leading-edge features. — [LAM](https://www.light-am.com/article/pdf/preview/LAM2026050195.pdf)
8. **"AI before physics" is partly wrong.** Learned reconstruction cuts exposures 30x (EUV mask inspection) and SEM dose, changing what can be measured in dose-limited regimes. — [SPIE vol. 13981](https://spie.org/Publications/Proceedings/Volume/13981)
9. **The main hybrid-bond yield detractors are pre-bond surface conditions**, per the ECTC panel consensus, not buried defects per se. — [IEEE EPS](https://eps.ieee.org/wp-content/uploads/2026/03/Emerging-Technologies_-TC-Article_Hybrid-Bonding_031126_for_EPS_newsletter_FINAL.pdf)
10. **Measurement as the per-wafer "judge" is only partly true in hybrid bonding.** Micro-inspection samples 2-5 wafers per lot, acoustic imaging runs after full assembly, and IR review cannot cover 100% of a wafer. — [SE](https://semiengineering.com/shrinking-hybrid-bonding-pitches-push-inspection-limits/); [IRDS 2024](https://irds.ieee.org/images/files/pdf/2024/2024IRDS_MET.pdf)

## Sources (with dates)
- Semiconductor Engineering, Peters, "Shrinking Hybrid Bonding Pitches Push Inspection Limits", 10 Nov 2026 — https://semiengineering.com/shrinking-hybrid-bonding-pitches-push-inspection-limits/
- Semiconductor Engineering, Haley, "Metrology Under Pressure…", 12 Aug 2025 — https://semiengineering.com/metrology-under-pressure-detecting-defects-in-fine-pitch-hybrid-bonding/
- EE Times, Brans, "Hybrid Bonding Comes of Age Slowly and Collectively", 26 Jan 2026 — https://www.eetimes.com/hybrid-bonding-comes-of-age-slowly-and-collectively/
- TrendForce [SEC], 6 Mar, 1 Apr, 7 Jul 2026 — URLs above
- SemiAnalysis ECTC 2026 roundup [SEC], 2 Jul 2026 — https://newsletter.semianalysis.com/p/ectc2026
- ECTC 2026 technical tipsheet, 20 May 2026 — https://ectc.net/wp-content/uploads/2023/03/2026-ECTC-REVISED-Technical-Tipsheet-with-images.pdf
- IEEE EPS, Summary of ECTC 2025 hybrid-bonding special session, Mar 2026 — https://eps.ieee.org/wp-content/uploads/2026/03/Emerging-Technologies_-TC-Article_Hybrid-Bonding_031126_for_EPS_newsletter_FINAL.pdf
- Proc. SPIE 13981 (Metrology, Inspection, and Process Control XL), Feb 2026 — https://spie.org/Publications/Proceedings/Volume/13981
- Timoney et al. (IBM Research/Nova), SPIE 13981-16, Feb 2026 — https://www.novami.com/wp-content/uploads/2026/04/13981-16-timoney-spie-alp-2026-vts-ml-cu-recess-final.pdf ; IBM blog, 23 Feb 2026 — https://research.ibm.com/blog/spie-2026-below-2-nm
- C. Mack, SPIE 2026 diary [SEC], Feb 2026 — https://www.lithoguru.com/scientist/conferences/spie_diary_2026.html
- Chen et al., Light: Adv. Manuf. 7:112, online 9 Sep 2026 — https://www.light-am.com/article/doi/10.37188/lam.2026.112
- KLA Q1 FY2027 call, 28 Oct 2026 (transcript 29 Oct) — https://www.fool.com/earnings/call-transcripts/2026/10/29/kla-klac-q1-2027-earnings-call-transcript/
- IRDS 2024 Metrology — https://irds.ieee.org/images/files/pdf/2024/2024IRDS_MET.pdf
- Bits&Chips [SEC], 26 Aug 2026; Tom's Hardware [SEC], 24 Aug 2026; MLQ [SEC], 25 Aug 2026; Herald Business [SEC], 20 Sep 2026; Seoul Economic Daily [SEC], 6 Apr 2026; technologies.org [SEC], 5 Aug 2026 — URLs above
- Wikipedia "2 nm process" [TER], edited 21 Oct 2026 — https://en.wikipedia.org/wiki/2_nm_process
