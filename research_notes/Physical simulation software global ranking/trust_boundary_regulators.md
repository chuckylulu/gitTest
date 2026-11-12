# Trust boundary in physical simulation: regulators, certifiers and learned models (as of 12 Nov 2026)

STATUS: first version saved from the salvage digest; being extended. Sections marked [TODO] still to be researched.

## Q0. Where does the boundary sit, and does the prior hold?

### Takeaway
(Draft) Physics-based simulation is accepted as primary evidence in several regulated domains when validated against tests (seat certification by analysis, nuclear evaluation models under RG 1.203, FDA device CM&S under the 2023 credibility guidance). Learned models are accepted as regulated products (FDA-cleared AI devices, including a deep-learning CT-FFR device classed as "simulation software") and as trial-evidence tools under human oversight (AIM-NASH, FDA Dec 2025), but no aviation or nuclear regulator was found to accept a learned model as primary safety evidence.

### Cited Findings
- NRC-commissioned gap assessment (Oct 2024): use of AI models within the scope of RG 1.157 and RG 1.203 (ECCS/transient analysis) "is practically not allowed by the underlying regulations, mainly Part 50 Appendix K" — [NRC ML24290A059](https://www.nrc.gov/docs/ML2429/ML24290A059.pdf)
- EASA AI Roadmap 2.0 (10 May 2023): "First approvals of Level 1 AI/ML" foreseen 2025; Level 2 "around 2035 ... not a formal target"; EASA AI/ML policy finalised "by 2028" — [EASA Roadmap 2.0 PDF](https://www.easa.europa.eu/en/downloads/137919/en)
- FDA cleared DEEPVESSEL FFR (K213657, 1 Apr 2022), "coronary physiological simulation software" computing CT-FFR "using deep learning neural networks", predicate HeartFlow FFRCT (CFD-based), on a 244-patient clinical study vs invasive FFR — [FDA K213657](https://www.accessdata.fda.gov/cdrh_docs/pdf21/K213657.pdf)
- FDA qualified AIM-NASH, "the first AI drug development tool", 8 Dec 2025; "pathologists are fully responsible for final interpretation" — [FDA](https://www.fda.gov/drugs/drug-safety-and-availability/fda-qualifies-first-ai-drug-development-tool-will-be-used-mash-clinical-trials)

### Inferences
- (Draft) Prior holds under a narrow reading (learned model as primary evidence substituting for a physical test or for a physics-based safety analysis); is contradicted under a broad reading in medicine (learned model as the cleared device; learned model output accepted in trials with human sign-off).

### Gaps
- [TODO] full research pending.

## Q1. Civil aviation [TODO]
### Cited Findings
- EASA NPA 2025-07 "Detailed specifications and associated AMC and GM for Artificial intelligence trustworthiness", published 10 Nov 2025, comments to 10 Mar 2026 (extended), RMT.0742 (ToR 11 Sep 2024), responds to EU AI Act Art. 108 — [EASA NPA 2025-07](https://www.easa.europa.eu/en/document-library/notices-of-proposed-amendment/npa-2025-07)
- EASA AI Concept Paper Proposed Issue 03, 3 Jun 2026, adds reinforcement learning, symbolic AI, Level 3 ("advanced automation"); comments to 12 Aug 2026; "final Concept Paper deliverable" under Roadmap 2.0 — [EASA news](https://www.easa.europa.eu/en/newsroom-and-events/news/easa-releases-latest-issue-its-concept-paper-artificial-intelligence)
- EASA AI page lists no approval of an ML application; MLEAP outputs are research deliverables — [EASA AI](https://www.easa.europa.eu/en/domains/research-innovation/ai)

## Q2. Nuclear [TODO]
### Cited Findings
- NRC AI Strategic Plan published 29 Sep 2025 (ML25269A196); NRC page (updated 4 Nov 2026) now uses "Super Intelligence (SI)" per "September 29, 2026, Executive Order on Inaugurating the Era of Super Intelligence" (EO 14434) — [NRC AI](https://www.nrc.gov/ai.html)
- Gap assessment (SwRI for NRC, Oct 2024): 517 RGs reviewed, potential gaps in 71; framework "generally sufficient"; "no practical standards were identified" for endorsement; RG 1.203 guidance on "calculational devices" "can be applied to examine AI systems"; "frozen" model concept applicable to AI — [ML24290A059](https://www.nrc.gov/docs/ML2429/ML24290A059.pdf)
- TerraPower Kemmerer Unit 1: application 28 Mar 2024, final SE Dec 2025, Commission CP decision 9 Mar 2026 — [NRC](https://www.nrc.gov/reactors/new-reactors/advanced/who-were-working-with/applicant-projects/terrapower)
- NRC's own codes (TRACE, RELAP5, PARCS, MELCOR, MACCS, FRAPCON/FRAPTRAN, SAPHIRE, xLPR, FAVPRO 2024) used for "review of licensees' codes and performance of audit calculations" (page updated 7 Oct 2026) — [NRC codes](https://www.nrc.gov/about-nrc/regulatory/research/safetycodes.html)

## Q3. Medical devices and medicines [TODO]
### Cited Findings
- FDA final guidance "Assessing the Credibility of Computational Modeling and Simulation in Medical Device Submissions" (Nov 2023, FDA-2021-D-0980) applies to "physics-based, mechanistic, or other first principles-based models" — [FDA](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/assessing-credibility-computational-modeling-and-simulation-medical-device-submissions)
- MDDT list (current 10 Feb 2026): computational NAMs include Virtual MRI Safety Evaluations (16 Nov 2021), Visible Human CAD + Ansys HFSS/Mechanical femoral-nail MRI heating tool (30 Mar 2023), ENDPOINT numaScrew Virtual Pullout Test (10 Apr 2025), IVIES (3 Feb 2026); no tool described as ML — [FDA MDDT](https://www.fda.gov/medical-devices/medical-device-development-tools-mddt)
- FDA draft guidance on AI to support regulatory decision-making for drugs (Jan 2025, FDA-2024-D-4689), risk-based credibility framework by context of use; CDER page (current 1 May 2026) does not show it finalised; FDA–EMA "Guiding Principles of Good AI Practice in Drug Development" Jan 2026 — [FDA draft](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and-biological); [CDER AI](https://www.fda.gov/about-fda/center-drug-evaluation-and-research-cder/artificial-intelligence-drug-development)
- ICH M15 final as FDA guidance June 2026 (FR 3 Jun 2026), finalising Dec 2024 draft — [FDA M15](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m15-general-principles-model-informed-drug-development)
- FDA plan (10 Apr 2025) to reduce/replace animal testing for mAbs using NAMs incl. "AI-based computational models of toxicity" — [FDA](https://www.fda.gov/news-events/press-announcements/fda-announces-plan-phase-out-animal-testing-requirement-monoclonal-antibodies-and-other-drugs)

## Q4. Automotive [TODO]
## Q5. Maritime, offshore, wind [TODO]
## Q6. Buildings, civil, pressure equipment [TODO]
- MLIT register of certifications 1 Apr 2000–31 Mar 2013: only NTT Data's "SEIN La CREA 認定版" (RC and S) appear as new-law certified structural programs (SPRG) — [MLIT register PDF](https://www.mlit.go.jp/common/001109045.pdf)
## Q7. Semiconductors [TODO]
- TSMC EDA Tool Certification Program lists Cadence, Synopsys, Siemens EDA for A14/A16/N2P/N3C (tables "As of 10/01/2026"); 3DFabric table includes "Auto Chiplet Floorplan w/ Agentic AI" — [TSMC EDA Alliance](https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance)
## Q8. Power grids [TODO]
## Q9. Insurance and weather [TODO]
- Florida Commission accepted hurricane models under 2023 standards (list rev. 2 Oct 2026): Cotality, FIU public model, Impact Forecasting, KCC, Moody's RMS, Verisk; expiry 1 Nov 2027 — [FCHLPM list](https://fchlpm.sbafla.com/media/fdwlbsvn/20261002_2023hurricane_2021floodacceptedmodels.pdf)
- 2025 Hurricane Standards add G-3 "Artificial Intelligence Use" and CI-2 "AI-Based Software Engineering" (document and audit, not prohibit) — [FCHLPM 2025 ROA](https://fchlpm.sbafla.com/media/vjophvvg/2025-hurricane-roa.pdf)
## Q10. Cross-cutting standards and certifiers [TODO]
## Q11. Ranking and events to 2031 [TODO]

## INTERIM FINDINGS (session 2, to be merged)
- FAA Roadmap for AI Safety Assurance Version I (PDF created 28 Jun 2024, 31 pp): learned (static) vs learning AI; incremental; project-specific issue papers; milestones: policy statement + policy memo 4Q2024 (draft), Certification Position Papers 1Q2026, ACs TBD, SAE G-34/EUROCAE standard TBD; no Version II found — https://www.faa.gov/media/82891
- FAA AC 20-146A (29 Jun 2018): seat certification by computer modelling "validated by dynamic tests"; "The FAA will not accept a model validated against another validated model"; modelling "instead of dynamic testing" only for modifications of a certificated baseline with margin-of-safety limits — https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-146A.pdf
- EASA Concept Paper Proposed Issue 03 (3 Jun 2026, 239 pp): scope incl. "AI-based development and verification tools used to develop approved products"; excludes systems "directly contributing to the potential for fatalities ... loss of an aircraft"; frozen models only; Sec 3.3.7 Surrogate modelling: "In other cases, the surrogate model completely replaces the high-fidelity model ... the output of the surrogate model defines the required results. Consequently, the level of accuracy of a surrogate model should be at the same level as the credibility of the high-fidelity physics-based model or be compensated for"; Objective SU-SM-01; test set may be exclusively high-fidelity-model data for surrogates; DAL D/AL5/TQL5 for AI in catastrophic failure conditions "will not be accepted" — https://www.easa.europa.eu/en/downloads/143701/en
- EMA CHMP Qualification Opinion AIM-NASH, first published 20 Mar 2025: "first Qualification Opinion (QO) on an innovative development methodology based on artificial intelligence"; "the committee can accept evidence generated by the tool as scientifically valid in future applications"; readings verified by one expert pathologist vs three-pathologist consensus; model "locked"; major changes may require re-qualification — https://www.ema.europa.eu/en/news/ema-qualifies-first-artificial-intelligence-tool-diagnose-inflammatory-liver-disease-mash-biopsy-samples
- EMA qualified Unlearn's PROCOVA (prognostic covariate adjustment using ML "digital twins") 20 Sep 2022 (company account); FDA said it "does not appear to deviate from our guidance" (company claim, unconfirmed) — https://www.unlearn.ai/resources/summary-of-the-ema-september-2022-qualification-opinion-for-procova-tm
- FDA AI-enabled devices: "over 1,600 ... as of September 2026" (page current 22 Sep 2026) — https://www.fda.gov/medical-devices/digital-health-center-excellence/artificial-intelligence-enabled-medical-devices
- FDA AI-enabled device lifecycle draft guidance (Jan 2025) still draft; CDRH FY2027 agenda (RAPS, 2 Oct 2026) lists finalising it as top priority; PCCP final guidance 4 Dec 2024 — https://www.raps.org/resource/fda-s-device-center-releases-guidance-agenda-for-fy-2027.html
- NRC Part 53 final rule approved 25 Mar 2026, effective ~29 Apr 2026 (ANS 26 Mar 2026) — https://www.ans.org/news/2026-03-26/article-7881/nrc-unveils-part-53-final-rule/
- EO 14300 (23 May 2025) Sec 2(d): "Employ emerging technologies to safely accelerate the modeling, simulation, testing, and approval of new reactor designs"; 18-month decision deadline; final rules within 18 months — https://www.govinfo.gov/content/pkg/FR-2025-05-29/html/2025-09798.htm
- EO 14434 (29 Sep 2026; 91 FR 63129, 2 Oct 2026) is a terminology directive (AI -> "Super Intelligence"); commentators say it creates no new regulatory powers (Wiley; Arnold & Porter) — https://www.wiley.law/alert-Executive-Order-Rebrands-AI-as-Super-Intelligence-and-Signals-Potential-Federal-Legislative-Changes
- Euro NCAP (ESV26-283, Klug et al., Mar 2026): far-side VT procedure published 2023, monitoring from 2024 ("results are not yet used for scoring"); frontal VTC with HIII models "applied from 2026"; randomised validation load cases for far-side by 2026, frontal "anticipated by 2029"; HBM results collected by 2026, HBM for assessment planned by 2029; validation per ISO/TS 18571:2024; CATARC (China) ran parallel pilots — https://cdn.euroncap.com/cars/assets/ESV_26_283_EURO_NCAP_VIRTUAL_TESTING_IN_FRONTAL_IMPACTS_60a1873dec.pdf
- UN ADS: GRVA adopted draft UNR and recommended GTR Jan 2026; WP.29 adoption reported 24 Jun 2026; safety case reviewed by type-approval authority; validation via "virtual simulation, track, and real-world testing"; NHTSA published draft GTR for comment 23 Jan 2026 (Covington, 6 May 2026) — https://www.globalpolicywatch.com/2026/05/un-regulation-and-gtr-on-automated-driving-systems-current-state-of-play/ ; entry into force "late July 2026" per ERTICO (secondary) — https://ertico.com/unece-adopts-first-ever-global-rules-allowing-fully-autonomous-vehicles
- ASME VVUQ: published V&V 10-2019, V&V 20-2009, VVUQ 20.1-2024, VVUQ 30.1-2024, V&V 40-2018, VVUQ 60.1-2024; subcommittee VVUQ 70 "Verification and Validation of Machine Learning" (no standard listed); VVUQ 80 pharma, VVUQ 90 airframe structures — https://www.asme.org/codes-standards/publications-information/verification-validation-uncertainty
- FDA NAMs: year-one report (Apr 2026) says ISTAND permanent, NAMs Acceptability Database, mAb guidance change; draft NAMs guidance Mar 2026 (secondary: Spencer Fane, FASEB) — https://www.spencerfane.com/insight/fda-reports-meeting-year-one-goals-for-reducing-animal-drug-testing/
