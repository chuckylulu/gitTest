# Thea Energy, Inc. (formerly Princeton Stellarators, Inc.): company fact file as of 14 November 2026

Source labels used throughout: **[C]** = company-controlled (Thea press releases, website, X account, and executive statements); **[I]** = independent (government records, peer-reviewed journals, journalism); **[I-agg]** = independent aggregator or tracker (Wikipedia, trackers, trade newsletters that mostly relay releases). Treat [I-agg] with caution. Peer-reviewed papers written by Thea staff are labelled **[I-peer, Thea-authored]**: the journal is independent, but the authors are not. Partner quotes that appear only inside Thea releases count as [C].

Method note: the shared web-search budget ran out partway through. After that, checks used direct fetches of known URLs and government or scholarly database APIs: SEC EDGAR full-text search, the USAspending.gov API, the Federal Register API, the Regulations.gov API and the Crossref API. Some searches were therefore never run (NJEDA records, patents, litigation, the 2022 seed round). These items are listed under Gaps.

---

## 1. Stage: what Thea makes (Eos, Helios, Canis, magnets), the DOE design review, Eos siting, and how the roadmap dates moved

### Takeaway
As of 14 Nov 2026 Thea is a design and magnet-hardware company. It has no plasma-confinement device yet. What it has done so far:
- Built and tested a 3×3 planar HTS coil array (Canis), announced March 2025 and peer-reviewed in IEEE TAS (October 2025).
- Operated one full-scale "Eos-spec" shaping coil above 6 T, announced May 2026. This result is unpublished.
- Published a 16-paper preconceptual design of its Helios power plant (Fusion Engineering and Design, Aug–Nov 2026).
- Had the Helios preconceptual design certified under DOE's Milestone program, announced 13 Jan 2026.

Eos is still targeted to be "online by 2030", but no site had been announced by 14 Nov 2026, although Thea repeatedly said it would pick a site in 2026. The Helios target has moved between "the 2030s", "2034" and "by 2035".

### Cited Findings

**Corporate basics**
- Thea was founded in 2022 as Princeton Stellarators, Inc. (PSI), a spin-off of PPPL and Princeton University. It is "based on technology licensed from PPPL", with all-planar coils developed by PPPL and licensed by Thea. Wikipedia cites PPPL news of 1 Feb 2023 for this; the PPPL page itself returned HTTP 403 in this session. — [Wikipedia, "Thea Energy" (accessed 14 Nov 2026)](https://en.wikipedia.org/wiki/Thea_Energy) [I-agg]
- The DOE Milestone selection release of 1 Jun 2023 was issued as "Princeton Stellarators" (Princeton, N.J.). — [Thea/GlobeNewswire, "Princeton Stellarators Selected for U.S. DOE Milestone-Based Fusion Development Program", 1 Jun 2023](https://thea.energy/press-release/princeton-stellarators-selected-for-u-s-department-of-energy-milestone-based-fusion-development-program/) [C]
- By 27 Jul 2023 the company described itself as "Thea Energy Inc., formerly Princeton Stellarators". — [Thea, "Thea Energy Selected for U.S. DOE Public-Private Partnership Award Through the INFUSE Program", 27 Jul 2023](https://thea.energy/press-release/thea-energy-selected-for-u-s-department-of-energy-public-private-partnership-award-through-the-innovation-network-for-fusion-energy-program/) [C]
- Thea's own history page says that in 2021 David Gates developed "stellarator magnet array technology at PPPL as part of the ARPA-E BETHE program", and that Thea then spun out that technology and a team from Princeton. The page says the project was "partially funded by the Stellar Energy Foundation". — [Thea, "History" page (accessed 14 Nov 2026)](https://thea.energy/history/) [C]

**Canis 3×3 planar HTS coil array (field-shaping demonstrator, not a plasma device)**
- Announced 20 Mar 2025. Specifications and results:
  - Nine HTS planar coils in a 3×3 array, operated at 20 K.
  - Up to ±140 A in all coils; estimated maximum stored energy 34.5 kJ.
  - Up to 47.2 mT measured on a plane 25 cm from the coils; calculated maximum field at the coils above 3 T.
  - Field "iso-surfaces recreated within 1% error of simulated predictions".
  - Thea says the array was built and operated "in a matter of months", but gives no test dates.
  - Thea says DOE "certified the completion of this test campaign, which included performance markers" from the Milestone program. — [Thea/GlobeNewswire, "Thea Energy Demonstrates Performance and Controllability of Small and Simple Magnets for Fusion Energy", 20 Mar 2025](https://thea.energy/press-release/thea-energy-demonstrates-performance-and-controllability-of-small-and-simple-magnets-for-fusion-energy/) [C]
- arXiv preprint: 33 authors (first author D. Nash), submitted 19 Mar 2025. The abstract reports closed-loop field control "within 1% of predicted field". — [arXiv:2503.18960, "Prototyping and Test of the 'Canis' HTS Planar Coil Array for Stellarator Field Shaping", 19 Mar 2025](https://arxiv.org/abs/2503.18960) [I-peer pending at the time, Thea-authored]
- Peer-reviewed version: IEEE Transactions on Applied Superconductivity vol. 35, issue 7 (October 2025 issue; Thea lists it as published 31 Jul 2025). Crossref metadata lists 15 authors, first author Daniel Nash. — [IEEE TAS, DOI 10.1109/TASC.2025.3594533](https://doi.org/10.1109/TASC.2025.3594533); [IEEE Xplore 11105783](https://ieeexplore.ieee.org/document/11105783) [I-peer, Thea-authored]
- PPPL director Steven Cowley, quoted inside Thea's release: "This magnet array milestone confirms a concept that was created at PPPL". — [Thea, 20 Mar 2025](https://thea.energy/press-release/thea-energy-demonstrates-performance-and-controllability-of-small-and-simple-magnets-for-fusion-energy/) [C]

**Full-scale planar shaping coil (May 2026)**
- What Thea reported on 13 May 2026:
  - Operation of its "first full-size, full-current, and full-field" Eos-spec planar shaping coil at 20 K, producing and controlling a field "over 6 T".
  - No current, coil dimensions or test duration given.
  - No independent verification and no publication; quench-survivability testing is still planned.
  - More than 50 generations of planar coils iterated in-house over about 18 months.
  - All shaping coils are a single standardized part.
  - A second manufacturing facility is planned for 2026. — [Thea/GlobeNewswire, "Thea Energy Announces Successful Operation of Full-Scale Planar Shaping Coils", 13 May 2026](https://thea.energy/press-release/thea-energy-announces-successful-operation-of-full-scale-planar-shaping-coils/) [C]
- In August 2026 Thea said it had "confirmed Eos-spec magnets meet field strength and precision requirements". No data was published. — [Thea, "Thea Energy Extends Series B Funding to Deploy Efficient and Economical Fusion Power", 18 Aug 2026](https://thea.energy/press-release/thea-energy-extends-series-b-funding-to-deploy-efficient-and-economical-fusion-power/) [C]
- The Eos encircling coil had not yet been validated as of 4 Nov 2026. Thea announced that MIT PSFC will test "a planar encircling coil" at full field and full force in PSFC's cryogenic facilities. No test dates or funding were given. — [Thea, "Thea Energy Collaborates with MIT's Plasma Science and Fusion Center on Planar Coil Magnet Program", 4 Nov 2026](https://thea.energy/press-release/thea-energy-collaborates-with-mits-plasma-science-and-fusion-center-on-planar-coil-magnet-program/) [C]; corroborated by [ANS Nuclear Newswire, "Thea Energy, MIT collaborate on testing stellarator magnet technology", 6 Nov 2026](https://www.ans.org/news/2026-11-06/article-8563/thea-energy-mit-collaborate-on-testing-stellarator-magnet-technology/) [I]

**Eos (first integrated stellarator; purpose and size as described over time)**
- February 2024: "large-scale integrated neutron source stellarator system". No target date was given. — [Thea/GlobeNewswire, "Thea Energy Announces $20 Million Series A Financing", 8 Feb 2024](https://thea.energy/press-release/thea-energy-announces-20-million-series-a-financing/) [C]
- January 2025 (Thea's summary of its Nuclear Fusion paper): a medium-sized design "requiring less than 40 MW of electric power". It would breed tritium of about 0.2 g/day (about 70 g/yr) via D-D fusion. Helios would be "roughly twice Eos's linear size". — [Thea, "Thea Energy Announces Peer-Reviewed Publications Outlining the Planar Coil Stellarator Approach…", 29 Jan 2025](https://thea.energy/press-release/thea-energy-announces-peer-reviewed-publications-outlining-the-planar-coil-stellarator-approach-for-commercial-fusion-energy/) [C]; underlying paper: [Swanson et al., Nucl. Fusion 65 026053 (28 Jan 2025), DOI 10.1088/1741-4326/ada56a](https://doi.org/10.1088/1741-4326/ada56a) [I-peer, Thea-authored]
- July 2025: Heatmap described the device being designed as using "about 450 magnets and roughly 15 megawatts of power". No operational timeline was given. — [Heatmap (Matthew Zeitlin), "Why Is Thea Energy, the Fusion Company, in New Jersey?", 17 Jul 2025](https://heatmap.news/climate-tech/thea-energy-fusion-new-jersey) [I]
- December 2025 onward: Eos is described as a "large-scale demonstration system… scheduled to be online by 2030". — [Thea/GlobeNewswire, "Thea Energy Completes Fusion Power Plant Preconceptual Design", 15 Dec 2025](https://thea.energy/press-release/thea-energy-completes-fusion-power-plant-preconceptual-design/) [C]
- February 2026: Berzin said Thea is "on track to operate Eos by 2030". He described a "Phase 2" in which Eos acts as a neutron source for blanket and fuel-cycle development and, through D-D fusion, breeds tritium and medical radioisotopes. — [POWER (Darrell Proctor), "The POWER Interview: Thea Energy's Fusion Architecture", 9 Feb 2026](https://www.powermag.com/the-power-interview-thea-energys-fusion-architecture/) [I outlet; content is CEO statements]
- July 2026: Eos will use "approximately 300 of these planar shaping coils". — [Thea, "Thea Energy Expands Magnet Manufacturing Lines with $20 Million ARPA-E SCALEUP Program Award", 27 Jul 2026](https://thea.energy/press-release/thea-energy-expands-magnet-manufacturing-lines-with-20-million-arpa-e-scaleup-program-award/) [C]
- November 2026: Eos uses "12 encircling coils and about 300 programmable shaping magnets" and is "targeted to come online by 2030". — [Thea, 4 Nov 2026 (MIT release)](https://thea.energy/press-release/thea-energy-collaborates-with-mits-plasma-science-and-fusion-center-on-planar-coil-magnet-program/) [C]; [Thea, "Thea Energy Appoints Pat Schweiger as Chief Engineer", 3 Nov 2026](https://thea.energy/press-release/thea-energy-appoints-pat-schweiger-as-chief-engineer/) [C]; [ANS, 6 Nov 2026](https://www.ans.org/news/2026-11-06/article-8563/thea-energy-mit-collaborate-on-testing-stellarator-magnet-technology/) [I]
- TechCrunch, May 2026: Thea plans to "begin construction of Eos, its 'power plant relevant' demonstration device, starting next year" (that is, 2027), and "hopes to complete its Eos demonstration reactor in 2030". — [TechCrunch (Tim De Chant), "With a new $100M raise, Princeton's Thea Energy is now a top-funded fusion startup", 27 May 2026](https://techcrunch.com/2026/05/27/with-a-new-100m-raise-princetons-thea-energy-is-now-a-top-funded-fusion-startup/) [I]

**Eos site status (no site announced as of 14 Nov 2026)**
- 19 May 2025 (date decoded from the post ID): Thea posted that it had "recently launched a process to evaluate & select the system's site". — [Thea Energy on X, status 1924465682386755859](https://x.com/TheaEnergy/status/1924465682386755859) [C]
- July 2025: executives pointed to a decommissioned coal plant in Jersey City as a possible brownfield site with an existing grid connection. Heatmap reported that no site had been chosen. — [Heatmap, 17 Jul 2025](https://heatmap.news/climate-tech/thea-energy-fusion-new-jersey) [I]
- December 2025 / January 2026: "in conversations with five states" and "expects to select and announce a location… in 2026". The states were not named. — [Thea, 15 Dec 2025](https://thea.energy/press-release/thea-energy-completes-fusion-power-plant-preconceptual-design/) [C]; [Thea/GlobeNewswire, "U.S. Department of Energy Certifies Thea Energy's Fusion Pilot Plant Preconceptual Design", 13 Jan 2026](https://thea.energy/press-release/u-s-department-of-energy-certifies-thea-energys-fusion-pilot-plant-preconceptual-design/) [C]
- 27 May 2026: the company "expects to choose a site later in 2026". — [Thea, "Thea Energy Raises $100 Million Series B Funding…", 27 May 2026](https://thea.energy/press-release/thea-energy-raises-100-million-series-b-funding-to-build-scalable-fusion-power-plants/) [C]
- 18 Aug 2026: "multiple potential sites have been evaluated"; no selection had been made. — [Thea, 18 Aug 2026](https://thea.energy/press-release/thea-energy-extends-series-b-funding-to-deploy-efficient-and-economical-fusion-power/) [C]
- A third-party tracker, verified 11 Oct 2026, lists "multiple sites under evaluation; selection expected in 2026". — [Nuclear News Network, "Eos (Thea Energy) — fusion project status and timeline"](https://www.nuclearnewsnetwork.com/industry-trackers/fusion-energy-companies/thea-eos) [I-agg]
- Thea's press-release index (newest item 4 Nov 2026) has no site announcement. — [Thea press-release index](https://thea.energy/press-release/) [C]

**Helios (power-plant concept)**
- Preconceptual design completed and announced 15 Dec 2025. Specifications as announced:
  - About 400 MWe net and 1.1 GW thermal; 8 m major radius; capacity factor above 85%.
  - 20 T maximum on-coil field; more than 1 m radial space for blanket and shielding.
  - "Tokamak-like X-point divertor", claimed to exhaust gas about 10× better than prior stellarator divertors.
  - First wall averages about 15 years; magnets over 40 years; plant 40+ years.
  - Operation planned "in the 2030s". No LCOE or capital-cost figures. — [Thea, 15 Dec 2025](https://thea.energy/press-release/thea-energy-completes-fusion-power-plant-preconceptual-design/) [C]
- arXiv overview, posted 8 Dec 2025 (v3 dated 5 Jan 2026; 42 named authors, first author C.P.S. Swanson):
  - Two-field-period quasi-axisymmetric (QA) configuration with aspect ratio 4.5.
  - 12 plasma-encircling HTS coils plus 324 field-shaping coils; 20 T maximum on-coil field.
  - 1.2 m minimum plasma-to-coil distance; 40-year minimum coil lifetime.
  - 1.1 GWth and **390 MWe** net; about 84-day biennial maintenance; **88%** capacity factor. — [arXiv:2512.08027](https://arxiv.org/abs/2512.08027) [Thea-authored preprint]
- 9 Sep 2026: 16 peer-reviewed papers appeared in a special issue of *Fusion Engineering and Design*, "The Helios Stellarator Power Plant Design by Thea Energy". The guest editors were Benedikt Geiger (UW–Madison) and Sophia Henneberg (MIT). The release lists:
  - D-T fuel and QA configuration.
  - First-wall lifetime "at least 11 years, averaging 18 years".
  - A claimed "zero risk" of plasma disruption.
  - Target operation "in the 2030s".
  - Still no cost figures. — [Thea, "Thea Energy Publishes the Most Practical Fusion Power Plant Design…", 9 Sep 2026](https://thea.energy/press-release/thea-energy-publishes-the-most-practical-fusion-power-plant-design-and-a-clear-path-toward-energy-on-the-grid/) [C]; [ScienceDirect special issue page](https://www.sciencedirect.com/special-issue/10L70JMWRNC) [I]
- The blanket concept in the special issue is a dual-coolant lead-lithium blanket. — [Pasmann et al., FED 231, 115951 (Oct 2026), DOI 10.1016/j.fusengdes.2026.115951](https://doi.org/10.1016/j.fusengdes.2026.115951) [I-peer, Thea-authored]
- Digital twin: on 8 Jun 2026 Thea announced a Helios digital twin and AI surrogate models with NVIDIA (Omniverse libraries), Synopsys (Ansys tools; breeding-blanket evaluation), Argonne (neutronics and blanket design) and PPPL (plasma codes and datasets). No contract value, funding mechanism or deliverable dates were stated. — [Thea, "Thea Energy Accelerates Fusion Energy with Helios Power Plant Digital Twin…", 8 Jun 2026](https://thea.energy/press-release/thea-energy-accelerates-fusion-energy-with-helios-power-plant-digital-twin-and-ai-surrogate-models-in-collaboration-with-nvidia-synopsys-argonne-national-laboratory-and-princeton-plasma-physics-lab/) [C]

**DOE Milestone program: Thea's milestones and the preconceptual design review (PDR)**
- DOE's own record (16 Jan 2025) lists two Thea science and technology milestones as met:
  - (1) "down-selection to a family of optimized stellarator equilibria";
  - (2) "engineering design, prototyping, and operation of a single high-temperature-superconducting magnet coil".
  - The same article says awardees aimed to present preconceptual designs "within the first 18 months (roughly late 2025)". — [U.S. DOE, "U.S. Department of Energy Announces Selectees for $107 Million Fusion Innovation Research Engine Collaboratives, and Progress in Milestone Program…", 16 Jan 2025](https://www.energy.gov/articles/us-department-energy-announces-selectees-107-million-fusion-innovation-research-engine) [I]
- PDR certification, announced 13 Jan 2026:
  - DOE certified the Helios preconceptual pilot-plant design after an independent expert panel review that included a site visit to Kearny and a 200-page report. Thea calls this the program's "final major milestone".
  - Thea says it is the "first" awardee to receive certification of its pilot-plant design.
  - Named reviewer: Felix Parra-Diaz, head of PPPL's theory department. Other panel members were not named.
  - DOE's Jean Paul Allain is quoted in the release: "The Milestone Program mandates a heightened level of accountability". — [Thea, 13 Jan 2026](https://thea.energy/press-release/u-s-department-of-energy-certifies-thea-energys-fusion-pilot-plant-preconceptual-design/) [C]
- A trade newsletter repeats the certification and the "first awardee" claim. It notes that it did not cite a DOE announcement. — [The Fusion Report (Frankie Berry), "Thea Energy Becomes First DOE Milestone Program Awardee to Complete Fusion Power Plant Design Review", 15 Jan 2026](https://thefusionreport.com/thea-energy-becomes-first-doe-milestone-program-awardee-to-complete-fusion-power-plant-design-review/) [I-agg]
- Independent federal records are consistent with DOE continuing the award after the PDR:
  - The DOE award DE-SC0024881 has a "Continuation" action on 16 Mar 2026, and new obligations on 9 Jun 2026 ($6.2M) and 28 Sep 2026 ($11.515M). — [USAspending.gov, award ASST_NON_DESC0024881_089 (API, last modified 10 Nov 2026)](https://www.usaspending.gov/award/ASST_NON_DESC0024881_089) [I]
  - Thea's project "Stellarator Fusion Pilot Plant Enabled by Array of Planar Shaping Coils" appears on DOE's 27 Mar 2026 awards list, alongside the ARC (CFS), Zap and Realta pilot-plant projects. — [DOE Office of Science, "Department of Energy Announces $320 Million for Research" awards list (27 Mar 2026)](https://science.osti.gov/Funding-Opportunities/Award/awards-announcement) [I]

**Manufacturing and capacity**
- Kearny headquarters, opened January 2025: about 15,000 sq ft at Hugo Neu's Kearny Point campus, with labs for high-field magnet manufacturing and operation. It supported "over 50 employees". — [Thea, "Thea Energy Announces New Headquarters…", 21 Jan 2025](https://thea.energy/press-release/thea-energy-announces-new-headquarters-to-support-core-technology-development-and-manufacturing/) [C]; [ROI-NJ (Tom Bergeron), 23 Jan 2025](https://www.roi-nj.com/2025/01/23/industry/energy-utilities/thea-energy-a-fusion-tech-company-opens-new-hq-in-kearny-with-aim-of-doubling-its-workforce/) [I]
- On-site equipment includes "Zeus", a winding machine for HTS tape, and a CNC mill. Each Canis magnet was linked to 50 sensors. — [Heatmap, 17 Jul 2025](https://heatmap.news/climate-tech/thea-energy-fusion-new-jersey) [I]
- The ARPA-E SCALEUP award will fund Thea's "first domestic production line for modular HTS magnets" and about 300 shaping coils for Eos. No throughput figures were given. — [Thea, 27 Jul 2026](https://thea.energy/press-release/thea-energy-expands-magnet-manufacturing-lines-with-20-million-arpa-e-scaleup-program-award/) [C]
- Berzin said Thea "validated its manufacturing infrastructure for the required rates". The interview gives no capacity numbers. — [POWER, 9 Feb 2026](https://www.powermag.com/the-power-interview-thea-energys-fusion-architecture/) [I outlet / CEO claim]
- A second facility is planned in Northern New Jersey. — [Thea, 27 May 2026](https://thea.energy/press-release/thea-energy-raises-100-million-series-b-funding-to-build-scalable-fusion-power-plants/) [C]; [Thea, 18 Aug 2026](https://thea.energy/press-release/thea-energy-extends-series-b-funding-to-deploy-efficient-and-economical-fusion-power/) [C]

**How the roadmap dates moved (all dated statements found)**
- 2023 to February 2024: neither Thea release (Jun 2023, Feb 2024) gives a target date for Eos or a pilot plant. — [Thea, 1 Jun 2023](https://thea.energy/press-release/princeton-stellarators-selected-for-u-s-department-of-energy-milestone-based-fusion-development-program/); [Thea, 8 Feb 2024](https://thea.energy/press-release/thea-energy-announces-20-million-series-a-financing/) [C]
- July 2025: Heatmap reported that "no commercialization or operational timeline is given". — [Heatmap, 17 Jul 2025](https://heatmap.news/climate-tech/thea-energy-fusion-new-jersey) [I]
- 15 Dec 2025: Eos "online by 2030"; Helios "in the 2030s". — [Thea, 15 Dec 2025](https://thea.energy/press-release/thea-energy-completes-fusion-power-plant-preconceptual-design/) [C]
- 9 Feb 2026: Eos by 2030; Helios deployment "by 2035". — [POWER, 9 Feb 2026](https://www.powermag.com/the-power-interview-thea-energys-fusion-architecture/) [I outlet / CEO claim]
- 27 May 2026:
  - TechCrunch: Eos construction from 2027 and completion in 2030; Helios "coming online in 2034". — [TechCrunch, 27 May 2026](https://techcrunch.com/2026/05/27/with-a-new-100m-raise-princetons-thea-energy-is-now-a-top-funded-fusion-startup/) [I]
  - Thea's own release: construction of the first Helios "expected to start before the end of the decade". — [Thea, 27 May 2026](https://thea.energy/press-release/thea-energy-raises-100-million-series-b-funding-to-build-scalable-fusion-power-plants/) [C]
- 8 Jun 2026: Gates said "on-demand, abundant fusion power by 2035". — [Thea, 8 Jun 2026](https://thea.energy/press-release/thea-energy-accelerates-fusion-energy-with-helios-power-plant-digital-twin-and-ai-surrogate-models-in-collaboration-with-nvidia-synopsys-argonne-national-laboratory-and-princeton-plasma-physics-lab/) [C]
- 3–6 Nov 2026: Eos "by 2030"; Helios "on the grid in the 2030s" and "commercial fusion by 2035". — [Thea, 3 Nov 2026](https://thea.energy/press-release/thea-energy-appoints-pat-schweiger-as-chief-engineer/) [C]; [Thea, 4 Nov 2026](https://thea.energy/press-release/thea-energy-collaborates-with-mits-plasma-science-and-fusion-center-on-planar-coil-magnet-program/) [C]; [ANS, 6 Nov 2026](https://www.ans.org/news/2026-11-06/article-8563/thea-energy-mit-collaborate-on-testing-stellarator-magnet-technology/) [I]

**Promised vs actual (dated)**
- Program schedule, met:
  - DOE expected preconceptual designs "roughly late 2025". — [DOE, 16 Jan 2025](https://www.energy.gov/articles/us-department-energy-announces-selectees-107-million-fusion-innovation-research-engine) [I]
  - Thea completed its design on 15 Dec 2025 and announced DOE certification on 13 Jan 2026. — [Thea, 15 Dec 2025](https://thea.energy/press-release/thea-energy-completes-fusion-power-plant-preconceptual-design/); [Thea, 13 Jan 2026](https://thea.energy/press-release/u-s-department-of-energy-certifies-thea-energys-fusion-pilot-plant-preconceptual-design/) [C]
- Canis paper "being submitted to a peer-reviewed journal" (March 2025), met:
  - Published in IEEE TAS, vol. 35(7), 2025. — [IEEE TAS DOI](https://doi.org/10.1109/TASC.2025.3594533) [I]
- Helios overview "submitted to a peer-reviewed journal" (December 2025 / January 2026), met:
  - Published as FED vol. 232, article 115999 (November 2026). — [FED DOI 10.1016/j.fusengdes.2026.115999](https://doi.org/10.1016/j.fusengdes.2026.115999) [I-peer, Thea-authored]
- Headcount "double… over the next year" from more than 50 (January 2025), slower than stated:
  - More than 75 by February 2026. — [POWER, 9 Feb 2026](https://www.powermag.com/the-power-interview-thea-energys-fusion-architecture/)
  - "Recently passed 100 employees" by 3 Nov 2026. — [Thea, 3 Nov 2026](https://thea.energy/press-release/thea-energy-appoints-pat-schweiger-as-chief-engineer/) [C]
- Eos site "announce in 2026": still pending as of 14 Nov 2026 (see the siting findings above).

### Inferences
- Thea has demonstrated magnet sub-systems only. No Thea device has confined plasma, so its physics claims for Eos and Helios rest on modelling, and the magnet claims rest on company-run tests. Only Canis has been peer-reviewed.
- Thea's own descriptions changed between 2024–25 and 2026:
  - Eos went from a "neutron source" needing under 40 MWe and breeding about 70 g/yr of tritium (2025) to a "power-plant-relevant, steady-state" demonstration with 12 encircling and about 300 shaping coils (2026).
  - The magnet count went from about 450 (Heatmap, 2025) to about 312 (2026).
  - These shifts may be design maturation rather than contradiction. No source reconciles them.
- The PDR schedule matches the program's 18-month first period counted from award signature on 3 Jun 2024 (USAspending), which ends around December 2025. Thea delivered at about the end of that window.
- With Eos construction said to start in 2027 and completion targeted for 2030, the site decision promised for 2026 is on the critical path. It had not been announced six weeks before year-end.

### Gaps
- The five candidate states for Eos are not named anywhere. No site agreement, lease or state announcement was found.
- No independent (DOE-issued) document confirms that DOE "certified" the Canis array test campaign. DOE's January 2025 list predates Canis and covers the single-coil milestone.
- No DOE-issued press release announcing the Helios PDR certification was found. Confirmation rests on Thea's release, which contains a DOE official's quote, plus the consistent USAspending continuation actions.
- The full-scale coil (>6 T) and "Eos-spec magnets meet requirements" claims have no published data or independent witnesses.
- No Eos or Helios cost estimates (capital cost or LCOE) have been disclosed.
- No status update was found on whether the second (Northern NJ) manufacturing facility, "planned for 2026", has opened.

---

## 2. Funding: equity rounds, investors, valuations, SEC filings, DOE, ARPA-E and INFUSE awards, state incentives, debt and revenue

### Takeaway
Disclosed private funding is about $130M as of May 2026: a $20M Series A (8 Feb 2024, led by Prelude Ventures) and a $100M Series B (27 May 2026, led by Thomas Tull's USIT). A Series B extension of undisclosed size followed on 18 Aug 2026. No valuation has been disclosed.

Federal support:
- USAspending shows $25.215M obligated to Thea under DOE Milestone award DE-SC0024881 through 28 Sep 2026, with only $3.0M of outlays reported.
- A $20M ARPA-E SCALEUP award was announced in July 2026 but was not yet visible in USAspending.
- Nine INFUSE awards. INFUSE money flows to the partner labs and universities, not to Thea.

No revenue, debt, cash or state incentives were found. Thea itself has no Form D on EDGAR; only three 2026 Form Ds filed by investor special-purpose vehicles (SPVs) appear.

### Cited Findings

**Equity rounds**
- **Pre-Series A / seed (2022–2023):** no disclosed round was found.
  - Heatmap reported Thea had raised "about $30 million total, including a $20 million Series A" as of July 2025. — [Heatmap, 17 Jul 2025](https://heatmap.news/climate-tech/thea-energy-fusion-new-jersey) [I]
  - The Fusion Report gave "over $30 million in private funding" as of January 2026. — [The Fusion Report, 15 Jan 2026](https://thefusionreport.com/thea-energy-becomes-first-doe-milestone-program-awardee-to-complete-fusion-power-plant-design-review/) [I-agg]
- **Series A, $20M, 8 Feb 2024.**
  - Lead: Prelude Ventures.
  - Participants: 11.2 Capital, Anglo American, Hitachi Ventures, Lowercarbon Capital, Mercator Partners, Orion Industrial Ventures, Starlight Ventures.
  - Use of funds: build and operate planar-coil magnet arrays, design and simulate Eos, grow the team.
  - Mark Cupta (Managing Director, Prelude Ventures) joined the board. — [Thea/GlobeNewswire, 8 Feb 2024](https://thea.energy/press-release/thea-energy-announces-20-million-series-a-financing/) [C]
  - Independently reported: [The Engineer, "Thea Energy raises $20m to advance fusion technology", 13 Feb 2024](https://www.theengineer.co.uk/content/news/thea-energy-raises-20m-to-advance-fusion-technology/) [I] (cited by Wikipedia; not opened directly).
- **Series B, $100M ("oversubscribed"), 27 May 2026.**
  - Lead: US Innovative Technology Fund (USIT, Thomas Tull).
  - New investors: General Innovation Capital Partners, Linse Capital, Calm Ventures, Climate Capital, Divergent Capital, Emerald Technology Ventures, Gaingels, Idemitsu Kosan, Overlay Capital, Timescale Ventures, Whatif (What If) Ventures.
  - Existing investors participating: Alumni Ventures, Hitachi Ventures, Lowercarbon Capital, Mercator Partners, Orion Industrial Ventures, Prelude Ventures, Starlight Ventures.
  - Use of funds: expand magnet manufacturing (including a second NJ facility), site and build Eos, double the team.
  - USIT's Gaetano Crupi is quoted. — [Thea, 27 May 2026](https://thea.energy/press-release/thea-energy-raises-100-million-series-b-funding-to-build-scalable-fusion-power-plants/) [C]
  - TechCrunch independently reported the same investor list. It quotes the startup as saying the round brings "total private investment to $130 million". No valuation was disclosed. — [TechCrunch, 27 May 2026](https://techcrunch.com/2026/05/27/with-a-new-100m-raise-princetons-thea-energy-is-now-a-top-funded-fusion-startup/) [I]
- **Series B extension, 18 Aug 2026** (amount, new total and valuation all undisclosed).
  - Named investors: Brevan Howard Macro Venture, Aloniq, ALJ Investments, Beyond Earth Ventures, plus unnamed "additional top-tier global strategic investors".
  - Thea says it is in "advanced talks with power offtakers, hyperscalers, and utility partners" and is "on track to double its headcount by year end". — [Thea, 18 Aug 2026](https://thea.energy/press-release/thea-energy-extends-series-b-funding-to-deploy-efficient-and-economical-fusion-power/) [C]

**SEC EDGAR (Form D)**
- EDGAR has no entity named "Thea Energy, Inc." or "Princeton Stellarators" (company-name index dated 14 Nov 2026). Full-text search for "Thea Energy" returns only three Form D filings, all by investor SPVs. — [SEC EDGAR full-text search, query "Thea Energy", forms D (run 14 Nov 2026)](https://efts.sec.gov/LATEST/search-index?q=%22Thea%20Energy%22&forms=D) [I]
  - **"Thea Energy B a Series of What If Ventures Master LLC"** (CIK 0002102886), administered by Sydecar LLC.
    - First sale 16 Mar 2026; $264,000 sold of a $264,000 offering; 7 investors.
    - Filed 17 Mar 2026. — [Form D primary_doc](https://www.sec.gov/Archives/edgar/data/2102886/000210288626000001/primary_doc.xml) [I]
  - **"OC Thea Energy Partners, LLC"** (CIK 0002129589). Related persons: Overlay Management, LLC and Chadd Evans.
    - First sale 17 Mar 2026; $1,015,000 sold of a $1,250,000 offering; 10 investors.
    - Signed 14 Apr 2026; filed 16 Apr 2026. — [Form D primary_doc](https://www.sec.gov/Archives/edgar/data/2129589/000091406226000035/primary_doc.xml) [I]
  - **"AVSF - Thea Energy 2026, LLC"** (CIK 0002127472). Signed by an officer of "Alumni Funds", the sole manager.
    - First sale 11 Apr 2026; $832,250 sold; 50 investors; minimum investment $10,000.
    - Filed 27 Apr 2026. — [Form D primary_doc](https://www.sec.gov/Archives/edgar/data/2127472/000212747226000001/primary_doc.xml) [I]

**DOE Milestone-Based Fusion Development Program**
- Program facts from DOE (16 Jan 2025):
  - $46M obligated initially across eight awardees for the first 18 months.
  - Authorized at $415M through FY2027 (CHIPS and Science Act).
  - Payments are made only after DOE verifies each milestone through independent review.
  - Companies fund more than 50% of milestone costs. — [DOE, 16 Jan 2025](https://www.energy.gov/articles/us-department-energy-announces-selectees-107-million-fusion-innovation-research-engine) [I]
- Thea was selected on 31 May / 1 Jun 2023 under DE-FOA-0002809. The amount was not disclosed at the time. — [Thea, 1 Jun 2023](https://thea.energy/press-release/princeton-stellarators-selected-for-u-s-department-of-energy-milestone-based-fusion-development-program/) [C]
- Wikipedia's program table lists Thea's initial amount as $7.5M, with a second period "announced". It says agreements were signed in June 2024, reportedly after IP-related delays. — [Wikipedia, "Milestone-Based Fusion Development Program" (accessed 14 Nov 2026)](https://en.wikipedia.org/wiki/Milestone-Based_Fusion_Development_Program) [I-agg]
- **Federal award record DE-SC0024881** ("Stellarator Fusion Pilot Plant Enabled by Array of Planar Shaping Coils"). — [USAspending.gov award page](https://www.usaspending.gov/award/ASST_NON_DESC0024881_089); [USAspending recipient profile, Thea Energy, Inc.](https://www.usaspending.gov/recipient/f49060d8-31ce-60b9-20d8-e22c775ea9de-R/latest) [I]
  - Recipient: Thea Energy, Inc. (UEI C6RDDSQK1KS8), small business, 1 Eastern Rd Ste 3-04 Bldg 197, Kearny NJ.
  - Program: CFDA 81.049 (Office of Science), award type "Other Financial Assistance".
  - Signed 3 Jun 2024; period of performance 5 Jun 2024 to 4 Jun 2027; place of performance Neshanic Station (Somerset County), NJ.
  - Obligations: $3,000,000 (3 Jun 2024, new award); $4,500,000 (10 Jan 2025); $0 actions on 21 Feb 2025, 10 Dec 2025 and 5 Mar 2026; "Continuation" on 16 Mar 2026 ($0); $6,200,000 (9 Jun 2026); $11,515,000 (28 Sep 2026).
  - **Total obligated: $25,215,000. Total outlays reported: $3,000,000** (record last modified 10 Nov 2026). No subawards.
- Thea has not disclosed milestone payment amounts. The January 2026 certification release gives none. — [Thea, 13 Jan 2026](https://thea.energy/press-release/u-s-department-of-energy-certifies-thea-energys-fusion-pilot-plant-preconceptual-design/) [C]

**ARPA-E**
- **SCALEUP: $20M**, announced by Thea on 27 Jul 2026.
  - Purpose: Thea's first domestic HTS magnet production line and about 300 Eos shaping coils.
  - Eligibility: SCALEUP funds prior ARPA-E awardees. Thea says its planar-coil technology "was developed under ARPA-E's BETHE program".
  - ARPA-E's Dave Nye is quoted in Thea's release. — [Thea, 27 Jul 2026](https://thea.energy/press-release/thea-energy-expands-magnet-manufacturing-lines-with-20-million-arpa-e-scaleup-program-award/) [C]
  - Secondary coverage says ARPA-E publicly named Thea and Xscape Photonics as "SCALEUP Ready" selectees on 9 Jul 2026, "up to $40 million" combined. ARPA-E's own page could not be retrieved, so this is not verified. — e.g., [Xenospectrum, "$20 Million for the US's First Fusion HTS Magnet Line…"](https://xenospectrum.com/en/thea-hts-magnet-scaleup/) [I-agg, unverified]
  - No ARPA-E (CFDA 81.135) transactions appear in Thea's USAspending recipient record. All $25.215M recorded is CFDA 81.049. — [USAspending recipient profile](https://www.usaspending.gov/recipient/f49060d8-31ce-60b9-20d8-e22c775ea9de-R/latest) [I]
- **BETHE:** per Thea, the BETHE work was done at PPPL in 2021, before the spin-out. It was not an award to Thea. — [Thea history page](https://thea.energy/history/) [C]

**DOE INFUSE (vouchers that fund lab and university partners' work)**
- **2022:** two awards; no details found. — [Wikipedia, "Thea Energy"](https://en.wikipedia.org/wiki/Thea_Energy) [I-agg]
- **2023:** one award with UC San Diego for a boron-based renewable first wall ("boron pebble rods"). The round funded 18 projects with $4.6M in total; Thea's share was not stated. — [Thea, 27 Jul 2023](https://thea.energy/press-release/thea-energy-selected-for-u-s-department-of-energy-public-private-partnership-award-through-the-innovation-network-for-fusion-energy-program/) [C]
- **2025:** three awards. — [Thea, "…Selected for Three U.S. DOE Public-Private Partnership Awards…", 11 Sep 2025](https://thea.energy/press-release/thea-energy-selected-for-three-u-s-department-of-energy-public-private-partnership-awards-through-the-innovation-network-for-fusion-energy-program/) [C]
  - PPPL: reel-to-reel HTS inspection for Eos magnets.
  - PPPL: AI/ML fast-particle confinement models.
  - Columbia: energetic-particle-driven oscillations in Eos.
  - The round funded 20 projects with $6.1M in total.
  - The Columbia project is independently visible as DOE award DE-SC0026019 to Columbia University, "Analysis of energetic-particle-driven Alfvén activity in the Eos stellarator…": $100,339.16, 1 Sep 2025 to 31 Aug 2026. — [USAspending, ASST_NON_DESC0026019_089](https://www.usaspending.gov/award/ASST_NON_DESC0026019_089) [I]
- **FY2026:** three selections, posted 2 Nov 2026, in a round of 28 projects totalling $8.5M. DOE notes that selection "is not a commitment… to issue an award". — [DOE Office of Science, INFUSE FY26 selection list, posted 2 Nov 2026](https://science.osti.gov/-/media/funding/pdf/Awards-Lists/2026/Awards-List-Spreadsheet-Template_INFUSE-FY26.pdf) [I]
  - Brian Chen (PI) with MIT: "Recovery Mode via Thermal Cycling of Neutron Irradiated HTS".
  - Angelica Ottaviano (PI) with PPPL: "Chemistry and radiance of boron ablation plumes relevant to deuterium edge fusion plasmas".
  - Todd Elder (PI) with MIT: "Adaptive Coil Current Optimization for Magnetic Island Suppression".
- Thea's stated count was "six DOE INFUSE awards" from January to August 2026 and "nine" on 4 Nov 2026. — [Thea, 13 Jan 2026](https://thea.energy/press-release/u-s-department-of-energy-certifies-thea-energys-fusion-pilot-plant-preconceptual-design/); [Thea, 4 Nov 2026](https://thea.energy/press-release/thea-energy-collaborates-with-mits-plasma-science-and-fusion-center-on-planar-coil-magnet-program/) [C]

**State incentives, debt, revenue**
- No New Jersey incentives (NJEDA, tax credits or grants) are mentioned in Thea's headquarters release, ROI-NJ or Heatmap. No NJ official is quoted. — [Thea, 21 Jan 2025](https://thea.energy/press-release/thea-energy-announces-new-headquarters-to-support-core-technology-development-and-manufacturing/) [C]; [ROI-NJ, 23 Jan 2025](https://www.roi-nj.com/2025/01/23/industry/energy-utilities/thea-energy-a-fusion-tech-company-opens-new-hq-in-kearny-with-aim-of-doubling-its-workforce/) [I]; [Heatmap, 17 Jul 2025](https://heatmap.news/climate-tech/thea-energy-fusion-new-jersey) [I]
- USAspending shows no loans: $0 loan face value on Thea's recipient profile. — [USAspending recipient profile](https://www.usaspending.gov/recipient/f49060d8-31ce-60b9-20d8-e22c775ea9de-R/latest) [I]

### Inferences
- **Federal support vs private equity.** Federal obligations of $25.2M under DE-SC0024881, plus the announced $20M SCALEUP award, total about $45M. That is about one-third of disclosed private equity ($130M, excluding the undisclosed extension).
  - Under DOE's rule that companies fund more than 50% of milestone costs, $25.2M of DOE obligations would imply more than $25M of matching private spending across those milestones.
  - "Obligated" is not "paid". Reported outlays are only $3.0M, though outlay reporting can lag.
- **Initial award and second period.**
  - The $7.5M initial Milestone amount on Wikipedia equals the first two USAspending obligations ($3.0M + $4.5M).
  - The FY2026 obligations ($17.715M) and the March 2026 "Continuation" action are consistent with a second period of performance. No source states its milestones or value.
- **Timing of the Series B.** The SPV Form Ds show capital being gathered for Thea from 16 Mar to 11 Apr 2026, about 6–10 weeks before the Series B was announced on 27 May 2026. That suggests the round had first closings in spring 2026.
- **Pre-Series A money.** Heatmap's "about $30M total" (July 2025) minus the $20M Series A implies about $10M of other pre-2025 private funding. Its form (seed, SAFE or other) is not documented.
- **Revenue.** Thea appears pre-revenue. The only commercial product mentioned is future tritium and medical-isotope output from Eos. DOE financial assistance is not revenue.

### Gaps
- No revenue, gross margin, cash balance, burn rate, debt or audited financials were found. Thea is private and discloses none.
- No valuation has been disclosed for either round. PitchBook and Crunchbase profiles exist but are paywalled.
- The Series B extension amount and the post-extension total are unknown.
- Seed or founding investors (2022–23) are not identified.
- Actual DOE milestone payments by date and amount are unknown. USAspending outlays may be incomplete.
- ARPA-E's own SCALEUP announcement, the award terms and the cost share were not retrieved.
- No search of NJEDA board minutes or NJ grant databases was possible (search budget exhausted). State incentives are therefore "not found", not "confirmed absent".
- Thea may have relied on exemptions that do not require a Form D, or filed under another legal name. Absence on EDGAR is a finding, not proof that no securities offering was made.

---

## 3. Customers, partners and contracts: offtake, MOUs, sites, supply, labs and universities, and what partners say

### Takeaway
Thea has announced no customer, offtake agreement, PPA, MOU with a utility, site agreement or named HTS-tape supplier as of 14 Nov 2026. It describes only "advanced talks" with offtakers, hyperscalers and utilities.

Its documented relationships are research collaborations:
- PPPL (licensor, INFUSE, digital twin)
- MIT PSFC (encircling-coil tests, INFUSE)
- Columbia University and UC San Diego (INFUSE)
- Argonne, NVIDIA and Synopsys (digital twin)
- An ORNL "strategic partnership project"

Almost all partner statements appear inside Thea's own releases. Independent confirmation comes mainly from DOE award records.

### Cited Findings
- **Offtake:** in August 2026 Thea said it was in "advanced talks with power offtakers, hyperscalers, and utility partners". No counterparties were named. — [Thea, 18 Aug 2026](https://thea.energy/press-release/thea-energy-extends-series-b-funding-to-deploy-efficient-and-economical-fusion-power/) [C]
- Berzin (February 2026) said Thea is working to formalize engagements with "hyperscalers, power offtakers, and commercialization partners" for the first Helios plant. No names were given. — [POWER, 9 Feb 2026](https://www.powermag.com/the-power-interview-thea-energys-fusion-architecture/) [I outlet / CEO claim]
- Berzin said the DOE certification lets Thea "definitively communicate confidence in this design" to offtakers and hyperscalers. — [The Fusion Report, 15 Jan 2026](https://thefusionreport.com/thea-energy-becomes-first-doe-milestone-program-awardee-to-complete-fusion-power-plant-design-review/) [I-agg]
- **Partnerships page:** the only described relationship is that "Thea Energy and ORNL are working together on a strategic partnership project". The page also shows unexplained logos linking to:
  - Kyoto Fusioneering, UC San Diego Center for Energy Research and PPPL;
  - UW–Madison Plasma Science and Innovation Center and Stony Brook CIEES;
  - magneticscorp.com and Max Planck IPP.
  - No HTS-tape supplier, utility, offtaker, MOU or site agreement is listed. — [Thea, "Partnerships" page (accessed 14 Nov 2026)](https://thea.energy/partnerships/) [C]
- **PPPL (licensor and collaborator):**
  - Thea's technology is "licensed from PPPL". — [Wikipedia, citing PPPL 1 Feb 2023](https://en.wikipedia.org/wiki/Thea_Energy) [I-agg]
  - PPPL is the partner on two 2025 INFUSE projects and one FY26 INFUSE project. — [Thea, 11 Sep 2025](https://thea.energy/press-release/thea-energy-selected-for-three-u-s-department-of-energy-public-private-partnership-awards-through-the-innovation-network-for-fusion-energy-program/) [C]; [DOE INFUSE FY26 list, 2 Nov 2026](https://science.osti.gov/-/media/funding/pdf/Awards-Lists/2026/Awards-List-Spreadsheet-Template_INFUSE-FY26.pdf) [I]
  - PPPL staff ran Helios plasma simulations on PPPL and NERSC supercomputers. PPPL's Jonathan Menard, quoted in Thea's release: "Thea Energy has modeled the Helios plasma using high-fidelity codes run on supercomputers here at PPPL." — [Thea, 15 Dec 2025](https://thea.energy/press-release/thea-energy-completes-fusion-power-plant-preconceptual-design/) [C]
  - PPPL is a digital-twin partner; Nate Ferraro (deputy head of PPPL theory) is quoted. — [Thea, 8 Jun 2026](https://thea.energy/press-release/thea-energy-accelerates-fusion-energy-with-helios-power-plant-digital-twin-and-ai-surrogate-models-in-collaboration-with-nvidia-synopsys-argonne-national-laboratory-and-princeton-plasma-physics-lab/) [C]
- **MIT PSFC:**
  - Collaboration announced 4 Nov 2026 to test a full-scale Eos encircling coil at full field and force. Zachary Hartwig (head of the PSFC Engineering Group), quoted: "PSFC's testing infrastructure is ideally suited to evaluate Thea Energy's encircling coils." — [Thea, 4 Nov 2026](https://thea.energy/press-release/thea-energy-collaborates-with-mits-plasma-science-and-fusion-center-on-planar-coil-magnet-program/) [C]; reported by [ANS, 6 Nov 2026](https://www.ans.org/news/2026-11-06/article-8563/thea-energy-mit-collaborate-on-testing-stellarator-magnet-technology/) [I]
  - MIT is also the partner on two FY26 INFUSE selections. — [DOE INFUSE FY26 list](https://science.osti.gov/-/media/funding/pdf/Awards-Lists/2026/Awards-List-Spreadsheet-Template_INFUSE-FY26.pdf) [I]
- **Columbia University:** 2025 INFUSE partner. Elizabeth Paul (assistant professor) is quoted. — [Thea, 11 Sep 2025](https://thea.energy/press-release/thea-energy-selected-for-three-u-s-department-of-energy-public-private-partnership-awards-through-the-innovation-network-for-fusion-energy-program/) [C]
  - DOE pays Columbia directly under DE-SC0026019 ($100,339.16). — [USAspending](https://www.usaspending.gov/award/ASST_NON_DESC0026019_089) [I]
  - Columbia's Carlos Paz-Soldan offered public commentary on Helios. — [Thea, 15 Dec 2025](https://thea.energy/press-release/thea-energy-completes-fusion-power-plant-preconceptual-design/) [C]
- **UC San Diego:** 2023 INFUSE partner (boron renewable first wall). — [Thea, 27 Jul 2023](https://thea.energy/press-release/thea-energy-selected-for-u-s-department-of-energy-public-private-partnership-award-through-the-innovation-network-for-fusion-energy-program/) [C]
- **Argonne, NVIDIA and Synopsys:** Helios digital-twin collaboration, 8 Jun 2026.
  - Quoted: John Tramm (Argonne), John Josephakis (NVIDIA), Steve Pytel (Synopsys).
  - No contract value or funding mechanism was stated. — [Thea, 8 Jun 2026](https://thea.energy/press-release/thea-energy-accelerates-fusion-energy-with-helios-power-plant-digital-twin-and-ai-surrogate-models-in-collaboration-with-nvidia-synopsys-argonne-national-laboratory-and-princeton-plasma-physics-lab/) [C]; independently reported by [ANS Nuclear Newswire, "Thea Energy collaborates with AI companies to develop stellarator digital twin", 17 Jun 2026](https://www.ans.org/news/2026-06-17/article-8128/thea-energy-collaborates-with-ai-companies-to-develop-stellarator-digital-twin/) [I] (not opened directly; seen in search results).
- **Government partners quoted in Thea releases:**
  - DOE's Jean Paul Allain (January 2026). — [Thea, 13 Jan 2026](https://thea.energy/press-release/u-s-department-of-energy-certifies-thea-energys-fusion-pilot-plant-preconceptual-design/) [C]
  - ARPA-E's Dave Nye: "Thea Energy has validated its magnets and outlined a clear strategy to scale". — [Thea, 27 Jul 2026](https://thea.energy/press-release/thea-energy-expands-magnet-manufacturing-lines-with-20-million-arpa-e-scaleup-program-award/) [C]
- **Strategic investors with industrial ties** (investors, not customers): Anglo American, Hitachi Ventures (Series A); Idemitsu Kosan (Series B). — [Thea, 8 Feb 2024](https://thea.energy/press-release/thea-energy-announces-20-million-series-a-financing/); [Thea, 27 May 2026](https://thea.energy/press-release/thea-energy-raises-100-million-series-b-funding-to-build-scalable-fusion-power-plants/) [C]
- **For context**, two peers do have offtake deals: CFS has a 200 MW Google PPA (June 2025) and a $1B Eni deal (September 2025); Helion has a 50 MWe Microsoft PPA (May 2023). — [Reuters, 30 Jun 2025](https://www.reuters.com/sustainability/climate-energy/google-strikes-deal-buy-fusion-power-mit-spinoff-commonwealth-2025-06-30/); [TechCrunch, 22 Sep 2025](https://techcrunch.com/2025/09/22/commonwealth-fusion-systems-books-a-1b-power-deal-for-its-future-fusion-reactor/); [The Verge, 10 May 2023](https://www.theverge.com/2023/5/10/23717332/microsoft-nuclear-fusion-power-plant-helion-purchase-agreement) [I] (all via Wikipedia citations; not opened directly)

### Inferences
- Every partner quotation found (PPPL, MIT, Columbia, Argonne, NVIDIA, Synopsys, DOE, ARPA-E) sits inside Thea-issued releases. Independent partner-issued evidence is limited to:
  - DOE's INFUSE FY26 list (MIT, PPPL);
  - DOE's January 2025 milestone article;
  - DOE's March 2026 awards list;
  - USAspending records (Thea's DOE award; Columbia's INFUSE award).
- PPPL plays several roles at once:
  - technology licensor (2023);
  - INFUSE partner;
  - modelling partner for Helios;
  - digital-twin partner;
  - home institution of the one named member of the DOE PDR review committee.
- Relative to CFS and Helion, Thea has no publicly announced customer.

### Gaps
- HTS-tape (REBCO) supplier or supply agreement: none disclosed.
- PPPL licence terms (exclusivity, royalties, field of use, patents covered): not found. PPPL pages returned HTTP 403.
- The scope and value of the ORNL "strategic partnership project": not disclosed.
- No partner (MIT, PPPL, Argonne, NVIDIA, Synopsys) press release issued on its own site was retrieved to confirm the collaborations independently.

---

## 4. People, governance, headcount and locations

### Takeaway
Thea is led by co-founder and CEO Brian Berzin and co-founder and CTO David Gates, who developed the planar-coil magnet-array concept at PPPL. Pat Schweiger was appointed Chief Engineer on 3 Nov 2026; his past roles include CTO at Oklo, chief engineer at CFS and SVP engineering at TerraPower.

Charles P. S. Swanson is lead author of the Eos and Helios design papers. His title is not confirmed in the sources. The only disclosed board member is Mark Cupta of Prelude (from February 2024).

Headcount grew from more than 50 (January 2025) to more than 75 (February 2026) to more than 100 (November 2026). The company moved from Princeton and Branchburg-area addresses to a Kearny, NJ headquarters (January 2025).

### Cited Findings
- **Brian Berzin, co-founder and CEO.**
  - Background in electrical engineering and in finance and investment; first joined the commercialization side of fusion in 2017. — [POWER, 9 Feb 2026](https://www.powermag.com/the-power-interview-thea-energys-fusion-architecture/) [I outlet]
  - Named CEO since the June 2023 release. — [Thea, 1 Jun 2023](https://thea.energy/press-release/princeton-stellarators-selected-for-u-s-department-of-energy-milestone-based-fusion-development-program/) [C]
- **David A. Gates, Ph.D., co-founder and CTO.**
  - Developed the "stellarator magnet array technology at PPPL as part of the ARPA-E BETHE program" in 2021. — [Thea history page](https://thea.energy/history/) [C]
  - Heatmap reports that he "won an Edison Patent Award for the stellarator work at Princeton". — [Heatmap, 17 Jul 2025](https://heatmap.news/climate-tech/thea-energy-fusion-new-jersey) [I]
  - Presented "Reinventing the Stellarator" at the MIT PSFC seminar (26 Sep 2023) and at Fusion Power Associates (19 Dec 2023). — [Wikipedia, "Thea Energy"](https://en.wikipedia.org/wiki/Thea_Energy) [I-agg]
- **Charles P. S. Swanson:**
  - first author of the Eos design paper — [Nucl. Fusion 65 026053, 28 Jan 2025](https://doi.org/10.1088/1741-4326/ada56a);
  - first author and arXiv submitter of the Helios overview — [arXiv:2512.08027](https://arxiv.org/abs/2512.08027); [FED 232, 115999](https://doi.org/10.1016/j.fusengdes.2026.115999) [I-peer, Thea-authored].
- **Pat Schweiger, Chief Engineer (appointed 3 Nov 2026).** He is the "design authority" for Thea's systems. Prior roles:
  - CTO at Oklo;
  - chief engineer at Commonwealth Fusion Systems, where he grew engineering to more than 400 people;
  - SVP of engineering at TerraPower;
  - began his career at DOE's Fast Flux Test Facility.
  - The release says Thea "recently passed 100 employees". — [Thea, 3 Nov 2026](https://thea.energy/press-release/thea-energy-appoints-pat-schweiger-as-chief-engineer/) [C]
- **Board:** Mark Cupta (Managing Director, Prelude Ventures) joined with the Series A. No other directors were disclosed in the releases reviewed. — [Thea, 8 Feb 2024](https://thea.energy/press-release/thea-energy-announces-20-million-series-a-financing/) [C]
- **Other named staff:**
  - Madeline Joanis (media contact) and Robin Brown (investor contact). — [Thea, 21 Jan 2025](https://thea.energy/press-release/thea-energy-announces-new-headquarters-to-support-core-technology-development-and-manufacturing/) [C]
  - FY26 INFUSE principal investigators: Brian Chen, Angelica Ottaviano, Todd Elder. — [DOE INFUSE FY26 list](https://science.osti.gov/-/media/funding/pdf/Awards-Lists/2026/Awards-List-Spreadsheet-Template_INFUSE-FY26.pdf) [I]
  - The Canis arXiv paper lists 33 Thea authors (first author D. Nash). The Helios overview lists 42 named authors. — [arXiv:2503.18960](https://arxiv.org/abs/2503.18960); [arXiv:2512.08027](https://arxiv.org/abs/2512.08027)
- **Headcount:**
  - "over 50" (21 Jan 2025). — [Thea](https://thea.energy/press-release/thea-energy-announces-new-headquarters-to-support-core-technology-development-and-manufacturing/) [C]; [ROI-NJ](https://www.roi-nj.com/2025/01/23/industry/energy-utilities/thea-energy-a-fusion-tech-company-opens-new-hq-in-kearny-with-aim-of-doubling-its-workforce/) [I]
  - "c. 70 (2025)", unsourced. — [Wikipedia](https://en.wikipedia.org/wiki/Thea_Energy) [I-agg]
  - "more than 75" (9 Feb 2026). — [POWER](https://www.powermag.com/the-power-interview-thea-energys-fusion-architecture/)
  - "double the team" (27 May 2026). — [Thea](https://thea.energy/press-release/thea-energy-raises-100-million-series-b-funding-to-build-scalable-fusion-power-plants/) [C]
  - "on track to double its headcount by year end" (18 Aug 2026). — [Thea](https://thea.energy/press-release/thea-energy-extends-series-b-funding-to-deploy-efficient-and-economical-fusion-power/) [C]
  - "recently passed 100 employees" (3 Nov 2026). — [Thea](https://thea.energy/press-release/thea-energy-appoints-pat-schweiger-as-chief-engineer/) [C]
- **Locations:**
  - Princeton, NJ datelines in 2023 and February 2024 releases. — [Thea, 1 Jun 2023](https://thea.energy/press-release/princeton-stellarators-selected-for-u-s-department-of-energy-milestone-based-fusion-development-program/); [Thea, 8 Feb 2024](https://thea.energy/press-release/thea-energy-announces-20-million-series-a-financing/) [C]
  - The DOE award's place of performance is Neshanic Station, Somerset County, NJ. — [USAspending](https://www.usaspending.gov/award/ASST_NON_DESC0024881_089) [I]
  - Wikipedia's Milestone table lists the company as being in Branchburg, NJ. — [Wikipedia](https://en.wikipedia.org/wiki/Milestone-Based_Fusion_Development_Program) [I-agg]
  - Headquarters in Kearny (Kearny Point) from January 2025; the recipient address is 1 Eastern Rd, Ste 3-04, Bldg 197, Kearny NJ 07032. — [USAspending recipient profile](https://www.usaspending.gov/recipient/f49060d8-31ce-60b9-20d8-e22c775ea9de-R/latest) [I]
  - TechCrunch refers to Thea's "lab in Jersey City". — [TechCrunch, 27 May 2026](https://techcrunch.com/2026/05/27/with-a-new-100m-raise-princetons-thea-energy-is-now-a-top-funded-fusion-startup/) [I]
  - A second facility is planned in Northern NJ. — [Thea, 27 May 2026](https://thea.energy/press-release/thea-energy-raises-100-million-series-b-funding-to-build-scalable-fusion-power-plants/) [C]
- Thea's "About" page names no leadership, founders or board members. — [Thea, "About" page](https://thea.energy/about/) [C]

### Inferences
- The founding team's PPPL lineage (Gates; the PPPL-licensed technology) explains PPPL's recurring roles (Section 3).
- Schweiger's appointment brings in-house experience of building a large high-field magnet device at CFS just as Thea moves from magnet hardware towards Eos construction. That last point is Thea's own framing.
- Neshanic Station is in Somerset County, which fits Wikipedia's Branchburg listing. The company most likely operated there before moving to Kearny in January 2025. This is unconfirmed.

### Gaps
- Gates' exact former PPPL title(s) and departure date were not verified (PPPL pages blocked; search budget exhausted).
- Swanson's title, and whether he is a co-founder, were not confirmed.
- No CFO, COO or general counsel was identified. Full board composition after the Series B is undisclosed. It is unknown whether USIT took a board seat.
- The TechCrunch "Jersey City lab" reference is unexplained. Every other source places the labs in Kearny.

---

## 5. Legal, licensing and regulatory: site permitting, state radiation licensing, the NRC fusion framework, patents and disputes

### Takeaway
No site permits or state radioactive-materials licences exist for Eos, because no site has been chosen. The applicable federal framework is still a proposal: the NRC published its proposed rule placing fusion machines under the byproduct-material (Part 30) framework on 26 Feb 2026, and comments closed on 27 May 2026. Thea filed a comment letter on 27 May 2026; its contents could not be retrieved. No final rule appears in the Federal Register as of 14 Nov 2026.

Thea's core technology is licensed from PPPL, but no Thea-owned patents could be verified. No litigation or disputes were found; the search for them was limited.

### Cited Findings
- **NRC proposed rule** "Regulatory Framework for Fusion Machines", published 26 Feb 2026.
  - It amends 10 CFR Parts 20, 30, 37, 50, 51, 72, 110, 150, 170 and 171 "to augment the existing byproduct material framework to be inclusive of fusion machines", with "technology-inclusive" requirements.
  - Draft guidance: NUREG-1556 Vol. 22. Docket NRC-2023-0071; RIN 3150-AL00. Comments were due 27 May 2026. — [Federal Register, FR Doc 2026-03865, 26 Feb 2026](https://www.federalregister.gov/documents/2026/02/26/2026-03865/regulatory-framework-for-fusion-machines) [I]
- **Final rule:** a Federal Register API query for NRC documents containing "fusion machines" returned only this proposed rule as of 14 Nov 2026. No final rule was found. — [Federal Register API query (run 14 Nov 2026)](https://www.federalregister.gov/api/v1/documents.json?conditions%5Bterm%5D=%22fusion+machines%22&conditions%5Bagencies%5D%5B%5D=nuclear-regulatory-commission) [I]
- **Thea's comment:** "Comment on FR Doc # 2026-03865… from Thea Energy" (NRC-2023-0071-0098), received 27 May 2026 and posted 28 May 2026. The attachment is titled "FINAL_Thea_Comment_Letter_Fusion_Regulation(20260527)". The docket held 53 comments in total. — [Regulations.gov, NRC-2023-0071-0098](https://www.regulations.gov/comment/NRC-2023-0071-0098) [I]
- **Licensing of core IP:** Thea's planar-coil technology was "developed by PPPL and licensed by Thea Energy". — [Wikipedia, citing PPPL news of 1 Feb 2023](https://en.wikipedia.org/wiki/Thea_Energy) [I-agg]
  - Thea says the magnet-array technology was developed at PPPL under ARPA-E BETHE in 2021. — [Thea history page](https://thea.energy/history/) [C]
- **Patents (indirect evidence only):** Gates "won an Edison Patent Award for the stellarator work at Princeton". — [Heatmap, 17 Jul 2025](https://heatmap.news/climate-tech/thea-energy-fusion-new-jersey) [I]
- **IP and the Milestone program:** program-wide award agreements were signed in June 2024, more than a year after selection, "reportedly over intellectual property concerns". This applied to the program generally, not to Thea specifically. — [Wikipedia, Milestone program](https://en.wikipedia.org/wiki/Milestone-Based_Fusion_Development_Program) [I-agg]
  - Thea's agreement was signed on 3 Jun 2024. — [USAspending](https://www.usaspending.gov/award/ASST_NON_DESC0024881_089) [I]
- **Eos regulatory profile as described by Thea:** D-D operation with tritium breeding of about 0.2 g/day (about 70 g/yr) and medical-isotope production. Both matter for a byproduct-material licence. — [Thea, 29 Jan 2025](https://thea.energy/press-release/thea-energy-announces-peer-reviewed-publications-outlining-the-planar-coil-stellarator-approach-for-commercial-fusion-energy/) [C]; [POWER, 9 Feb 2026](https://www.powermag.com/the-power-interview-thea-energys-fusion-architecture/)
- **Peer comparison:** Helion obtained Washington State radioactive-materials licences for its Orion plant in June 2026. — [Reuters, 16 Jun 2026](https://www.reuters.com/business/energy/helion-says-it-is-first-us-fusion-energy-firm-clear-regulatory-licenses-2026-06-16/) [I] (via Wikipedia; not opened directly)

### Inferences
- Once Eos is sited, its licensing would presumably sit under the NRC's byproduct-material approach. In an Agreement State, that means a state radioactive-materials licence.
  - The NRC's Agreement State page lists 39 Agreement States; the fetched text did not show New Jersey's status. — [NRC, Agreement States](https://www.nrc.gov/about-nrc/state-tribal/agreement-states.html) [I]
- With no final rule and no site, Thea's licensing pathway for Eos cannot yet be specified.

### Gaps
- The content of Thea's NRC comment letter is unknown (the attachment returned HTTP 403).
- No Thea-assigned US patents or published applications were verified. Justia and PPPL pages were blocked and web search was exhausted.
- No NJ Department of Environmental Protection (radiation) records, local zoning or permitting records, or environmental reviews for Thea were found. None are expected until a site is selected.
- No litigation, disputes, regulatory enforcement or IP challenges were found. This was not exhaustively searched.
- PPPL licence terms (exclusive or non-exclusive, royalties, patents covered) are unknown.

---

## 6. Publication record and verification status of announced results

### Takeaway
Thea has a substantial peer-reviewed record, almost all written by Thea staff:
- 4 Nuclear Fusion papers (January 2025) setting out the planar-coil and Eos physics basis;
- 1 PPCF paper (February 2025);
- the Canis magnet paper in IEEE TAS (2025);
- a JPP bootstrap-current paper co-authored with PPPL (October 2025);
- materials and neutronics papers (2025);
- a 16-paper Helios special issue in Fusion Engineering and Design (Aug–Nov 2026).

Journal peer reviewers are anonymous. The DOE design-review panel is unnamed except for PPPL's Felix Parra-Diaz. Several 2026 hardware claims are unpublished:
- the full-scale >6 T coil;
- Eos-spec magnet validation;
- manufacturing rate validation;
- the 200-page DOE report.

### Cited Findings
- **Nuclear Fusion vol. 65, no. 2, published 28 Jan 2025** (four papers):
  - D. Gates et al. (19 authors), "Stellarator fusion systems enabled by arrays of planar coils", 026052 — [DOI 10.1088/1741-4326/ada56c](https://doi.org/10.1088/1741-4326/ada56c)
  - T. Kruger, M. Martin, D. Gates et al., "Coil optimization methods for a planar coil stellarator", 026051 — [DOI 10.1088/1741-4326/ada56b](https://doi.org/10.1088/1741-4326/ada56b)
  - C. Swanson, D. Gates et al. (8 authors), "The scoping, design, and plasma physics optimization of the Eos neutron source stellarator", 026053 — [DOI 10.1088/1741-4326/ada56a](https://doi.org/10.1088/1741-4326/ada56a)
  - P. Bonofiglo, D. Dudt, C. Swanson, "Fast ion confinement in quasi-axisymmetric stellarator equilibria", 026050 — [DOI 10.1088/1741-4326/ada56d](https://doi.org/10.1088/1741-4326/ada56d)
  - All four are [I-peer, Thea-authored]; metadata from the Crossref API. Thea announced them on 29 Jan 2025. — [Thea, 29 Jan 2025](https://thea.energy/press-release/thea-energy-announces-peer-reviewed-publications-outlining-the-planar-coil-stellarator-approach-for-commercial-fusion-energy/) [C]
- **Plasma Physics and Controlled Fusion 67(3) 035019 (21 Feb 2025):** R. Wu, T. Kruger, C. Swanson, "Planar coil optimization for the Eos stellarator using sparse regression". — [DOI 10.1088/1361-6587/adb5b7](https://doi.org/10.1088/1361-6587/adb5b7) [I-peer, Thea-authored]
- **IEEE Transactions on Applied Superconductivity 35(7) (2025):** D. Nash et al., "Prototyping and Test of the 'Canis' HTS Planar Coil Array for Stellarator Field Shaping". — [DOI 10.1109/TASC.2025.3594533](https://doi.org/10.1109/TASC.2025.3594533) [I-peer, Thea-authored]
  - Two related talks at Magnet Technology 29 (4 and 6 Jul 2025). — [Thea, "Presentations & Publications" page](https://thea.energy/presentations-and-publications/) [C]
- **Journal of Plasma Physics 91(5) E141 (October 2025):** S. Saxena, N. Ferraro, M. Martin, A. Wright, "Bootstrap current modeling in M3D-C1". Affiliations: Thea, PPPL, UW–Madison. — [DOI 10.1017/S0022377825100834](https://doi.org/10.1017/S0022377825100834) [I-peer, co-authored with PPPL]
- **Other 2025 papers listed by Thea:**
  - Nuclear Materials and Energy vol. 44 (25 Jul 2025): boron nitride–boron pebble aggregate for renewable plasma-facing surfaces.
  - Fusion Engineering and Design vol. 220, art. 115364 (online 1 Aug 2025): material volume fractions for Monte Carlo transport. — [Thea publications page](https://thea.energy/presentations-and-publications/) [C]; [NME article](https://www.sciencedirect.com/science/article/pii/S2352179125001048); [FED article](https://www.sciencedirect.com/science/article/abs/pii/S0920379625005605) [I-peer]
- **Helios special issue, Fusion Engineering and Design vols. 229–232 (Aug–Nov 2026), 16 papers** (Crossref metadata; all first-authored by Thea staff). Examples:
  - Swanson et al. (41 authors), "Overview of the Helios design: A practical planar coil stellarator fusion power plant", FED 232, 115999 — [DOI](https://doi.org/10.1016/j.fusengdes.2026.115999)
  - Kruger et al., "Planar coil design for the Helios stellarator fusion power plant", FED 230, 115893 — [DOI](https://doi.org/10.1016/j.fusengdes.2026.115893)
  - Olatunji et al., "Design of the superconducting encircling coils for Helios…", FED 230, 115894 — [DOI](https://doi.org/10.1016/j.fusengdes.2026.115894)
  - Flom et al., "Design and conceptual modeling of a tokamak-like X-point divertor for the Helios quasi-axisymmetric stellarator", FED 230, 115846 — [DOI](https://doi.org/10.1016/j.fusengdes.2026.115846)
  - Martin et al., "MHD stability analysis of the Helios stellarator fusion power plant", FED 231, 115959 — [DOI](https://doi.org/10.1016/j.fusengdes.2026.115959)
  - von der Linden et al., "Alpha confinement in the quasi-axisymmetric Helios fusion power plant", FED 229, 115801 — [DOI](https://doi.org/10.1016/j.fusengdes.2026.115801)
  - Tang et al., "Facility power balance, thermodynamic cycle, and fuel cycle analysis for the Helios fusion power plant", FED 230, 115896 — [DOI](https://doi.org/10.1016/j.fusengdes.2026.115896)
  - Pasmann et al., dual-coolant lead-lithium blanket, FED 231, 115951 — [DOI](https://doi.org/10.1016/j.fusengdes.2026.115951)
  - Wasserman et al., cryostat and maintenance, FED 232, 116018 — [DOI](https://doi.org/10.1016/j.fusengdes.2026.116018) [I-peer, Thea-authored]
  - Special issue landing page. — [ScienceDirect special issue](https://www.sciencedirect.com/special-issue/10L70JMWRNC) [I]
- **Who reviewed:**
  - FED guest editors Benedikt Geiger (UW–Madison) and Sophia Henneberg (MIT), per Thea. — [Thea, 9 Sep 2026](https://thea.energy/press-release/thea-energy-publishes-the-most-practical-fusion-power-plant-design-and-a-clear-path-toward-energy-on-the-grid/) [C]
  - DOE PDR panel: "independent experts from national laboratories, research institutions, and universities"; only PPPL's Felix Parra-Diaz is named. — [Thea, 13 Jan 2026](https://thea.energy/press-release/u-s-department-of-energy-certifies-thea-energys-fusion-pilot-plant-preconceptual-design/) [C]
  - Public commentary on Helios came from Carlos Paz-Soldan (Columbia), Jonathan Menard (PPPL) and Scott Hsu (Lowercarbon Capital, a Thea investor). — [Thea, 15 Dec 2025](https://thea.energy/press-release/thea-energy-completes-fusion-power-plant-preconceptual-design/) [C]
- **Announced but unpublished:**
  - full-scale planar shaping coil >6 T at 20 K (13 May 2026) — [Thea](https://thea.energy/press-release/thea-energy-announces-successful-operation-of-full-scale-planar-shaping-coils/) [C];
  - "confirmed Eos-spec magnets meet field strength and precision requirements" (18 Aug 2026) — [Thea](https://thea.energy/press-release/thea-energy-extends-series-b-funding-to-deploy-efficient-and-economical-fusion-power/) [C];
  - manufacturing infrastructure "validated… for the required rates" (February 2026) — [POWER](https://www.powermag.com/the-power-interview-thea-energys-fusion-architecture/);
  - the 200-page DOE PDR report (not public) — [Thea, 13 Jan 2026](https://thea.energy/press-release/u-s-department-of-energy-certifies-thea-energys-fusion-pilot-plant-preconceptual-design/) [C];
  - digital-twin results (none published) — [Thea, 8 Jun 2026](https://thea.energy/press-release/thea-energy-accelerates-fusion-energy-with-helios-power-plant-digital-twin-and-ai-surrogate-models-in-collaboration-with-nvidia-synopsys-argonne-national-laboratory-and-princeton-plasma-physics-lab/) [C].

### Inferences
- **Verification status by result:**
  - DOE-confirmed: the equilibrium down-selection and the single-HTS-coil milestone (DOE, January 2025).
  - Peer-reviewed but company-run tests with no independent replication: Canis (3×3 array, 20 K, about 1% field accuracy).
  - Company-announced, with a DOE official quoted but no DOE-issued document found: Helios PDR certification. USAspending continuation actions are consistent with it.
  - Company-announced only: full-scale coil >6 T and Eos-spec magnet validation.
  - Peer-reviewed modelling, not experiment: Helios and Eos physics.
- The Helios special issue is entirely Thea-authored. Its scrutiny came from journal review under external guest editors, not from independent replication.
- The Canis author list shrank from 33 (arXiv) to 15 (IEEE TAS, per Crossref). This is common between preprint and journal versions and is noted only for completeness.

### Gaps
- APS-DPP abstracts and other conference contributions (2023–2026) were not compiled; the search budget was exhausted.
- No independent critiques or comment papers on the planar-coil approach were located in the time available. Stellarator physics critiques are covered by a separate researcher.
- The identities of journal referees are not public, by journal practice.

---

## 7. Contradictions and comparisons: Thea's statements vs independent sources, and vs other stellarator developers, CFS and Helion

### Takeaway
Thea's core claims are mostly consistent with independent records:
- DOE milestone records and federal award data;
- the peer-reviewed Canis and Helios papers;
- TechCrunch's report of the $100M Series B.

The documented discrepancies are about dates and descriptions, not fabrication:
- target years for Helios (2030s, 2034, by 2035);
- Helios specifications in the release vs the paper (about 400 vs 390 MWe; above 85% vs 88% capacity factor; first-wall life);
- Eos magnet count and power;
- TechCrunch's note that the encircling coils were dropped, which Thea's later releases contradict;
- the Series A date on Wikipedia;
- the "Jersey City lab".

Against peers, Thea is earlier-stage and less funded than CFS (SPARC under construction) and Helion (Polaris operating). Its Eos timing (2030) is similar to Proxima's planned prototype (2031). Its Helios timing (2034–2035) is similar to Type One's Infinity Two (mid-2030s).

### Cited Findings
**Thea vs independent sources**
- **Series A date.** The Thea release is dated 8 Feb 2024, and The Engineer reported the round on 13 Feb 2024. Wikipedia's text says "September 2024", citing a 19 Sep 2024 Yahoo Finance article. — [Thea, 8 Feb 2024](https://thea.energy/press-release/thea-energy-announces-20-million-series-a-financing/) [C]; [The Engineer, 13 Feb 2024](https://www.theengineer.co.uk/content/news/thea-energy-raises-20m-to-advance-fusion-technology/) [I]; contradicted by [Wikipedia](https://en.wikipedia.org/wiki/Thea_Energy) [I-agg]
- **Helios target date.**
  - "2030s" (Thea, 15 Dec 2025; 9 Sep 2026). — [Thea](https://thea.energy/press-release/thea-energy-completes-fusion-power-plant-preconceptual-design/) [C]
  - "by 2035" (POWER, 9 Feb 2026; ANS, 6 Nov 2026). — [POWER](https://www.powermag.com/the-power-interview-thea-energys-fusion-architecture/); [ANS](https://www.ans.org/news/2026-11-06/article-8563/thea-energy-mit-collaborate-on-testing-stellarator-magnet-technology/) [I]
  - "coming online in 2034" (TechCrunch, 27 May 2026). — [TechCrunch](https://techcrunch.com/2026/05/27/with-a-new-100m-raise-princetons-thea-energy-is-now-a-top-funded-fusion-startup/) [I]
  - Construction start "before the end of the decade" (Thea, 27 May 2026). — [Thea](https://thea.energy/press-release/thea-energy-raises-100-million-series-b-funding-to-build-scalable-fusion-power-plants/) [C]
- **Helios specifications, release vs paper.**
  - Net power about 400 MWe and capacity factor above 85% (releases) vs 390 MWe and 88% (arXiv abstract). — [Thea, 15 Dec 2025](https://thea.energy/press-release/thea-energy-completes-fusion-power-plant-preconceptual-design/) [C]; [arXiv:2512.08027](https://arxiv.org/abs/2512.08027)
  - First-wall life "average lifetime of about 15 years" (December 2025) vs "at least 11 years, averaging 18 years" (September 2026). — [Thea, 15 Dec 2025](https://thea.energy/press-release/thea-energy-completes-fusion-power-plant-preconceptual-design/); [Thea, 9 Sep 2026](https://thea.energy/press-release/thea-energy-publishes-the-most-practical-fusion-power-plant-design-and-a-clear-path-toward-energy-on-the-grid/) [C]
- **Encircling coils.**
  - TechCrunch's update note reads: "Thea's early designs called for the use of 12 encircling magnets. They were not added to later versions." — [TechCrunch, 27 May 2026](https://techcrunch.com/2026/05/27/with-a-new-100m-raise-princetons-thea-energy-is-now-a-top-funded-fusion-startup/) [I]
  - This is contradicted by Thea's 4 Nov 2026 release (Eos "uses 12 encircling coils and about 300 programmable shaping magnets") and the ANS report of 6 Nov 2026, and by the Helios papers (12 encircling + 324 shaping coils). — [Thea](https://thea.energy/press-release/thea-energy-collaborates-with-mits-plasma-science-and-fusion-center-on-planar-coil-magnet-program/) [C]; [ANS](https://www.ans.org/news/2026-11-06/article-8563/thea-energy-mit-collaborate-on-testing-stellarator-magnet-technology/) [I]; [arXiv:2512.08027](https://arxiv.org/abs/2512.08027); [FED 230, 115894](https://doi.org/10.1016/j.fusengdes.2026.115894)
- **Eos size and power.**
  - "Less than 40 MW of electric power" (Thea summary of the Nuclear Fusion paper, January 2025). — [Thea](https://thea.energy/press-release/thea-energy-announces-peer-reviewed-publications-outlining-the-planar-coil-stellarator-approach-for-commercial-fusion-energy/) [C]
  - "about 450 magnets and roughly 15 megawatts" (Heatmap, July 2025). — [Heatmap](https://heatmap.news/climate-tech/thea-energy-fusion-new-jersey) [I]
  - "12 encircling coils and about 300" shaping magnets (Thea, 2026). — [Thea](https://thea.energy/press-release/thea-energy-collaborates-with-mits-plasma-science-and-fusion-center-on-planar-coil-magnet-program/) [C]
- **Eos fuel.**
  - D-D (Thea, 2025; Berzin in POWER, February 2026). — [Thea](https://thea.energy/press-release/thea-energy-announces-peer-reviewed-publications-outlining-the-planar-coil-stellarator-approach-for-commercial-fusion-energy/) [C]; [POWER](https://www.powermag.com/the-power-interview-thea-energys-fusion-architecture/)
  - A tracker lists D-T. — [Nuclear News Network tracker](https://www.nuclearnewsnetwork.com/industry-trackers/fusion-energy-companies/thea-eos) [I-agg]
- **Lab location.** TechCrunch places Thea's lab in "Jersey City". Thea releases and federal records place the headquarters and labs in Kearny. — [TechCrunch](https://techcrunch.com/2026/05/27/with-a-new-100m-raise-princetons-thea-energy-is-now-a-top-funded-fusion-startup/) [I]; [Thea, 21 Jan 2025](https://thea.energy/press-release/thea-energy-announces-new-headquarters-to-support-core-technology-development-and-manufacturing/) [C]; [USAspending](https://www.usaspending.gov/recipient/f49060d8-31ce-60b9-20d8-e22c775ea9de-R/latest) [I]
- **Total private funding.** Consistent across sources: about $30M (Heatmap, July 2025), "over $30M" (Fusion Report, January 2026) and $130M after the Series B (TechCrunch, May 2026). — [Heatmap](https://heatmap.news/climate-tech/thea-energy-fusion-new-jersey); [Fusion Report](https://thefusionreport.com/thea-energy-becomes-first-doe-milestone-program-awardee-to-complete-fusion-power-plant-design-review/); [TechCrunch](https://techcrunch.com/2026/05/27/with-a-new-100m-raise-princetons-thea-energy-is-now-a-top-funded-fusion-startup/)
- **"First" claims, independent status.**
  - "first awardee to have its plant design milestone certified": repeated by the Fusion Report but not found in a DOE-issued document. — [Fusion Report](https://thefusionreport.com/thea-energy-becomes-first-doe-milestone-program-awardee-to-complete-fusion-power-plant-design-review/) [I-agg]
  - "world's first superconducting planar coil magnet array" and "world's first… X-point divertor in a stellarator": company claims with no independent assessment found. — [Thea, 13 Jan 2026](https://thea.energy/press-release/u-s-department-of-energy-certifies-thea-energys-fusion-pilot-plant-preconceptual-design/) [C]
- **INFUSE count.** "Six" through August 2026 and "nine" in November 2026. This is consistent with DOE's FY26 list of three Thea selections (2 Nov 2026), which are still subject to negotiation. — [DOE INFUSE FY26 list](https://science.osti.gov/-/media/funding/pdf/Awards-Lists/2026/Awards-List-Spreadsheet-Template_INFUSE-FY26.pdf) [I]

**Comparison with other developers (dated public positions)**
- **Type One Energy (stellarator).** Agreement with TVA for a 350 MW "Infinity Two" plant in Tennessee targeting the mid-2030s; an additional $87M convertible note; total funding above $160M (as of January 2026). — [The Fusion Report, 15 Jan 2026](https://thefusionreport.com/thea-energy-becomes-first-doe-milestone-program-awardee-to-complete-fusion-power-plant-design-review/) [I-agg]
  - Also a Milestone awardee, with $9.5M initial per Wikipedia. — [Wikipedia, Milestone program](https://en.wikipedia.org/wiki/Milestone-Based_Fusion_Development_Program) [I-agg]
  - Two FY26 INFUSE selections. — [DOE INFUSE FY26 list](https://science.osti.gov/-/media/funding/pdf/Awards-Lists/2026/Awards-List-Spreadsheet-Template_INFUSE-FY26.pdf) [I]
  - Not on the fusion pilot-plant entries of DOE's 27 Mar 2026 awards list as reported. — [DOE awards list, 27 Mar 2026](https://science.osti.gov/Funding-Opportunities/Award/awards-announcement) [I]
- **Proxima Fusion (stellarator, Germany).**
  - Funding: €130M Series A (CNBC, 11 Jun 2025; the Fusion Report says May 2025) and a €15M extension (September 2025). — [CNBC, 11 Jun 2025](https://www.cnbc.com/2025/06/11/nuclear-fusion-proxima-raises-148-million-in-record-funding-round.html) [I]
  - Stellaris design published in FED in February 2025; prototype "planned for 2031". — [Lion et al., FED 214, 114868](https://www.sciencedirect.com/science/article/pii/S0920379625000705) [I-peer]; [EE Times, 26 Feb 2025](https://www.eetimes.com/proxima-fusion-unveils-stellaris-a-breakthrough-in-fusion-power/) [I] (via [Wikipedia, "Proxima Fusion"](https://en.wikipedia.org/wiki/Proxima_Fusion); not opened directly)
  - A July 2026 round including Alphabet; the press-release slug indicates €411M, which is unverified. — [Proxima press release](https://www.proximafusion.com/press-news/proxima-fusion-raises-eu411-million-to-build-europes-commercial-fusion-champion) [Proxima-controlled]
- **Commonwealth Fusion Systems (tokamak).**
  - SPARC was described as 75% complete in April 2026, with turn-on expected in 2027. — [Reuters, 21 Apr 2026](https://www.reuters.com/business/energy/first-commercial-fusion-plant-nears-construction-us-commonwealth-ceo-says-2026-04-21/) [I]
  - The ARC plant (about 400 MWe) in Chesterfield County, VA, targets the early 2030s. — [Virginia Mercury, 18 Dec 2024](https://virginiamercury.com/2024/12/18/virginia-to-host-worlds-first-fusion-power-plant/) [I]
  - About $1B in capital was secured for the Chesterfield plant in July 2026. — [Richmond BizSense, 30 Jul 2026](https://richmondbizsense.com/2026/07/30/commonwealth-fusion-secures-1b-capital-raise-to-set-stage-for-chesterfield-power-plant/) [I]
  - Earlier rounds include an $1.8B Series B (2021) and an $863M Series B2 (August 2025). — [Latitude Media, 29 Aug 2025](https://www.latitudemedia.com/news/commonwealth-fusion-systems-tops-up-its-series-b-with-863-million/) [I] (all via [Wikipedia, CFS](https://en.wikipedia.org/wiki/Commonwealth_Fusion_Systems); not opened directly)
  - TechCrunch called Thea's timeline "in line with CFS". — [TechCrunch, 27 May 2026](https://techcrunch.com/2026/05/27/with-a-new-100m-raise-princetons-thea-energy-is-now-a-top-funded-fusion-startup/) [I]
- **Helion (FRC/pulsed).**
  - Polaris has operated since about January 2025 and reported 150 million °C D-T fusion on 13 Feb 2026. — [GeekWire, 13 Feb 2026](https://www.geekwire.com/2026/helion-reaches-record-150-million-degrees-celsius-as-it-strives-for-ambitious-commercial-fusion-launch/) [I]
  - Orion (50 MW, for Microsoft, target 2028) has been under construction near Malaga, WA, since July 2025. — [Reuters, 30 Jul 2025](https://www.reuters.com/business/energy/helion-energy-starts-construction-nuclear-fusion-plant-power-microsoft-data-2025-07-30/) [I]
  - Washington State licences were granted in June 2026. — [Reuters, 16 Jun 2026](https://www.reuters.com/business/energy/helion-says-it-is-first-us-fusion-energy-firm-clear-regulatory-licenses-2026-06-16/) [I]
  - $500M Series G (September 2026). — [GeekWire, 15 Sep 2026](https://www.geekwire.com/2026/helion-funding-round-grows-to-500m-amid-uncertainty-over-fusion-startups-microsoft-timeline/) [I] (all via [Wikipedia, Helion](https://en.wikipedia.org/wiki/Helion_Energy); not opened directly)

### Inferences
- **Federal milestones:** Thea's record matches independent federal data. DOE confirmed its first two milestones, and award obligations continued into FY2026.
- **Hardware:** Thea's lead consists of magnet sub-scale and coil tests, not integrated systems. CFS is building SPARC and Helion runs Polaris; Thea's first integrated device (Eos) is unsited and targeted for 2030.
- **Timelines:**
  - Thea's Eos date of 2030 is similar to Proxima's prototype target of 2031.
  - Thea's Helios target (2034–2035) is similar to Type One's Infinity Two (mid-2030s) and later than CFS's ARC (early 2030s) and Helion's Orion (2028).
  - Unlike Type One (TVA), CFS (Google, Eni) and Helion (Microsoft), Thea has no named utility or offtake partner.
- **Funding scale:** Thea's disclosed private funding ($130M plus an undisclosed extension) is a fraction of CFS's (multi-billion) or Helion's ($500M in one 2026 round). It is in the same range as Proxima's Series A plus extension and Type One's (above $160M as of January 2026).

### Gaps
- Directly opened sources for the competitor comparisons were limited. Most competitor facts here come via Wikipedia's citations of Reuters, CNBC, GeekWire and others and were not opened individually. Peer facts should be cross-checked against the dedicated competitor files.
- No DOE-issued statement ranks or compares the Milestone awardees' PDR status. The "first to complete" claim therefore rests on Thea and the Fusion Report.
- It could not be determined whether Thea's moving Helios dates reflect a formal schedule change or inconsistent messaging. No dated internal roadmap or investor deck was found.
