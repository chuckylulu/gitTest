# Materials and atomic-scale simulation worldwide: software, companies, trust boundary, path forward (as of 12 November 2026)

Scope: quantum chemistry/DFT, molecular dynamics, machine-learned interatomic potentials (MLIPs), CALPHAD, AI materials-discovery platforms. Evidence gathered 12 Nov 2026. "Company claim, unconfirmed" = vendor statement no outside party has confirmed. Listed firms: business facts only (no share prices or multiples). Method note: the shared WebSearch budget, Exa and Firecrawl credits all ran out during the task; later facts come from direct fetches of known primary URLs (see "Could not verify").

**Summary for the report writer**
- Shape: a small, fragmented paid market built around a few de facto "judges": VASP for solid-state DFT (about 20% of NERSC computing cycles, the top code; 2018 data), Schrödinger's FEP+ for binding free energy in pharma, Thermo-Calc/CompuTherm CALPHAD databases for alloys, plus molecular quantum chemistry (Gaussian, Q-Chem). Around them sit free codes (LAMMPS, GROMACS, Quantum ESPRESSO, CP2K) and, since 2024, open-weight universal MLIPs that now top the independent leaderboard. Schrödinger is the only sizeable listed pure play (FY2025 revenue $255.9M; software $199.5M). Simulations Plus went private (Altaris, closed 6 Oct 2026) and is being combined with Chemical Computing Group.
- Capital has moved to AI-native private firms: CuspAI ($450M Series B at $2.6B, Jul 2026), Lila and Periodic Labs (reported, unannounced talks at $8.5B pre-money and $7.5B), Orbital Industries ($50M; now sells data-centre cooling hardware). China is strong in open models (DPA-4.1 from a DP Technology-linked consortium is #1 on Matbench Discovery, 31 Oct 2026). Korea has Samsung's model at #5. Japan's Matlantis is the main paid universal potential (>150 customers, company claim). Taiwan, India and Israel have no notable vendors (thin).
- Trust boundary: simulation decides what to make next, not what is true. FEP ranks compounds (accuracy close to assay reproducibility in a large Schrödinger-authored study), but assays decide. No regulator accepts atomistic simulation as filing evidence; the regulator-accepted modelling is pharmacometric (ICH M15 finalised by FDA June 2026). A computationally designed alloy (Ferrium S53) still needed AMS and MMPDS test data. "ML proposes, DFT certifies" is standard in materials screening, but experiments and novelty checks have overturned DFT-certified claims (A-Lab: 42 of 43 compounds with significant issues; MatterGen's TaCr2O6 was already known).
- arXiv 2605.08988 is real (Cardiff, v2 22 Oct 2026). Out-of-distribution force errors are 1-19x in-distribution depending on task; energy errors are up to ~900x. Scope: small H/C/N/O molecules. "Often an order of magnitude" is fair; a uniform "ten times" is not.
- Open vs paid: no revenue collapse yet (Schrödinger 2026 ACV guidance +12-17%; Certara software +11% in Q3 2026), but open FEP (OpenFE, 15 pharma partners) and open MLIPs erode the gap-filler case for paid tools. VASP now bans training AI on its code.
- Path forward favours owners of reference outputs that others train on (VASP, CALPHAD databases, FEP+), if they adopt GPUs (falling FP64 is a risk for DFT) and agents (Schrödinger Bunsen, Matlantis, VASP's AI hire). Paid universal potentials and seat-priced GUIs are most exposed.

## 1. Map: who sells what, ownership, size, funding (all regions)

### Takeaway
The paid core is a few hundred million dollars of software revenue, dominated by Schrödinger plus small private specialists (VASP, Thermo-Calc, Gaussian, Q-Chem, SCM, Materials Design, CompuTherm, QuesTek). The 2025-26 money and momentum sit with big-tech open models and heavily funded AI-native "discovery companies". These sell materials or IP more than software.

### Cited Findings
**Commercial and de facto standard codes (North America, Europe)**
- Schrödinger (US; NASDAQ: SDGR): FEP+, Glide, Desmond, Jaguar, LiveDesign, materials suite, MLFFs. 850 staff (363 PhDs) on 3 Feb 2026; ~40% of FY2025 revenue from outside the US; direct sales in the US, EU, UK, Japan, India and Korea, with distributors in markets including China — [10-K FY2025, 25 Feb 2026](https://www.sec.gov/Archives/edgar/data/1490978/000149097826000010/sdgr-20251231.htm). Detail in section 5.
- Dassault Systèmes BIOVIA (France): Materials Studio runs on the 3DEXPERIENCE cloud; its page names no ML potentials or GPU support — [3ds.com](https://www.3ds.com/products/biovia/materials-studio). BIOVIA is not reported separately. Life Sciences software revenue: Q3 2026 €265.7M (+1% at constant currency); 9M €776.7M (-2% cc) — [DS Q3, 28 Oct 2026](https://finance.yahoo.com/healthcare/articles/dassault-syst-mes-strong-q3-055900413.html). DS–NVIDIA deal (3 Feb 2026) pairs BioNeMo with BIOVIA models — [3ds.com](https://www.3ds.com/newsroom/press-releases/dassault-systemes-and-nvidia-partner-build-industrial-ai-platform-powering-virtual-twins).
- Synopsys QuantumATK: DFT, NEGF transport, MLFFs; accepts any ASE-compatible external MLFF — [docs](https://docs.quantumatk.com/manual/technicalnotes/external_mlff/external_mlff.html). GPU speed-ups (all company claims, unconfirmed): 15x on B200 ("measured" — [NVIDIA, 18 May 2025](https://blogs.nvidia.com/blog/semiconductor-industry-electronic-design-automation-blackwell-cuda-x)); up to 30x with cuEST at Applied Materials ([Synopsys, 16 Mar 2026](https://news.synopsys.com/2026-03-16-Synopsys-Showcases-NVIDIA-Partnership-Impact-and-Ecosystem-Innovation-at-GTC-2026)); up to 200x for MLFFs on Blackwell ([Synopsys, 26 Jul 2026](https://news.synopsys.com/2026-07-26-Synopsys-Showcases-Comprehensive-Autonomous-Engineering-Workflows-from-Silicon-to-Systems,-Developed-with-NVIDIA-Technology)).
- VASP Software GmbH (Vienna; private; licences signed by G. Kresse): a perpetual licence per research group covers the purchased release plus 3 years of minor upgrades; no annual fee. Commercial licences go only through Materials Design Inc., the "exclusive worldwide distributor" — [VASP FAQ](https://vasp.at/info/faq/); [purchase FAQ](https://vasp.at/info/faq/purchase_vasp/). Releases 6.6.0 (10 Mar 2026) and 6.6.1 (20 Jul 2026). A "VASP AI Expert" was hired for agent tools (7 Jul 2026). AI guidelines (16 Jun 2026) ban feeding VASP code or the PP-database to public models and ban using VASP material to train or clone models — [vasp.at news](https://vasp.at/info/post/). VASP uses ~20% of NERSC cycles and is the #1 code (allocation year 2018; older); >30x single-node speed-up on A100s vs CPU-era Cori — [Zhao et al. (LBNL, NVIDIA, VASP), CUG 2023](https://cug.org/proceedings/cug2023_proceedings/includes/files/pap130s2-file1.pdf).
- Gaussian Inc. (US, private): site blocked automated access; no 2025-26 facts verified. Q-Chem (US, private): v6.4 released 8 Dec 2025; GPU via BrianQC add-on — [Q-Chem](https://www.q-chem.com/news/2025-qc64-release). SCM (Amsterdam): AMS2026; ML potentials named: M3GNet, ANI-1ccx, user models — [SCM](https://www.scm.com/news/). Materials Design Inc. (US): MedeA, plus the VASP commercial channel.
- CALPHAD: Thermo-Calc Software AB (Stockholm; KTH spin-off 1997) is majority-owned by the non-profit foundation STT; >1,300 organisations in >60 countries (Jan 2020; older) — [Inderes](https://www.inderes.se/releases/thermo-calc-software-ab-thermo-calc-software-supporting-university-new-professorship-at-mit). Aggregator data — [largestcompanies.com](https://largestcompanies.com/company/Thermo-Calc-Software-AB-226607/closing-figures-and-key-ratios):

| Thermo-Calc (FY to Aug) | FY2025 | FY2024 |
|---|---|---|
| Turnover | EUR 12.38M | EUR 11.86M |
| Pre-tax profit | EUR 1.97M | EUR 2.67M |
| Average employees | 70 | 62 |
| Equity ratio | 72% | 71% |

  It bought out QuesTek Europe, now Thermo-Calc Solutions AB (5 Jun 2025) — [Metal AM](https://www.metal-am.com/thermo-calc-solutions-formed-following-the-acquisition-of-questek-europe/). CompuTherm LLC (US): Pandat 2026A; "PandatAi" LLM agents drive its PanLink engine (company claim, unconfirmed) — [computherm.com](https://computherm.com/).
- QuesTek Innovations (Evanston, private): ICMD SaaS plus Materials-by-Design services. Adopters include Aubert & Duval, The Exploration Company (Mar 2026) and Daido Steel — [QuesTek](https://questek.com/questeks-icmd-platform-expands-in-europe-with-new-and-continued-subscriptions-from-leading-innovators/). NASA SBIR (Apr 2026) — [QuesTek](https://questek.com/?p=6827). Citrine Informatics (US, private): materials-informatics SaaS; Series C ~$16M (2022/23). Revenue estimates conflict ($12.1M vs $6.5M; aggregators, unreliable) — [Latka](https://getlatka.com/companies/Citrine_Informatics).
- Adjacent, regulator-accepted modelling: Simulations Plus (GastroPlus) was taken private by Altaris (closed 6 Oct 2026). It is being combined with Altaris-owned Chemical Computing Group (MOE), which Schrödinger's 10-K names as a competitor — [8-K release](https://www.sec.gov/Archives/edgar/data/0001023459/000102345926000092/closingpr.htm). Reported deal value ~$375-377M — [Panabee](https://www.panabee.com/news/simulations-plus-acquisition-by-altaris-completes-for-377-million). Certara Q3 2026: revenue $94.9M (+4%); software $48.8M (+11%); services $46.1M (-2%); adjusted EBITDA $30.2M; cash $214.9M — [8-K, 5 Nov 2026](https://www.sec.gov/Archives/edgar/data/0001827090/000182709026000034/q32026earningsreleaseex99.htm).

**Asia and other regions**
- Japan, Matlantis Corp (ex-Preferred Computational Chemistry): founded 1 Jun 2021, owned 51% by PFN and 49% by ENEOS; Mitsubishi Corp a shareholder since Jun 2024; renamed Jul 2025; capital ¥310M; US arm in Cambridge MA — [profile](https://matlantis.com/en/company/profile/). Its PFP potential covers 96 elements. v8 (Jul 2025) is the "first" r2SCAN-trained universal MLIP (company claim, unconfirmed) — [release](https://matlantis.com/en/news/release-250716/). Customers: 100+ (Cabinet Office document, 30 Jun 2025) → ">150 companies and organizations" at the crystal-structure-prediction launch, 28 Jan 2026, with Honda as early adopter (company claim, unconfirmed) — [cas.go.jp](https://www.cas.go.jp/jp/seisaku/digital_global_kakuryokaigi/dai1/shiryo2.pdf); [release](https://matlantis.com/en/news/release-260128/). NVIDIA ALCHEMI integration (14 Apr 2026) — [StreetInsider](https://www.streetinsider.com/Press+Releases/Matlantis+Accelerates+Materials+Discovery+with+NVIDIA+ALCHEMI+Toolkit/26313307.html). Agent integration (27 May 2026): Claude Code/Codex run in the Matlantis terminal, guided by "Skills" on GitHub — [MONOist](https://monoist.itmedia.co.jp/mn/spv/2606/02/news020.html). No revenue disclosed.
- Korea: Samsung Electronics' EquFlashV2 is #5 on Matbench (11 Jun 2026) — [Matbench](https://matbench-discovery.materialsproject.org/). Virtual Lab Inc. (founded 2016; 13 staff) runs Materials Square, a pay-as-you-go cloud DFT/MD/CALPHAD service — [The VC](https://thevc.kr/virtuallab); [ACerS](https://ceramics.org/company/virtual-lab-inc).
- China, DP Technology (Beijing; founded 2018): Series C >RMB 800M (24 Dec 2025; Fortune Capital, Beijing AI and pharma funds, Lenovo Capital). Reported as a "unicorn" with cumulative funding of several billion yuan; valuation undisclosed. Bohrium has >3M users; clients include CATL, BYD and PetroChina (company claims, unconfirmed) — [PEdaily](https://news.pedaily.cn/202512/559044.shtml). DPA-4.1 (AI for Science Institute Beijing with PKU, DP Technology and IAPCM) is #1 and #3 on Matbench (31 Oct 2026) — [Matbench](https://matbench-discovery.materialsproject.org/). No Hong Kong IPO filing was found.
- China, other players. Hongzhiwei (Shanghai; founded 2014): Device Studio and DS-PAW plane-wave DFT; free for academia; runs on domestic Hygon CPUs — [36Kr](https://pitchhub.36kr.com/project/1818812402405507); [docs](https://hzw-devicestudio-doc.readthedocs.io/en/latest/). Other Chinese open models in the Matbench top 15: ShanghaiTech, CAS (MatRIS), Fudan.
- China, XtalPi (HKEX: 2228), H1 2026 — [XtalPi, 19 Aug 2026](https://www.thailand-business-news.com/pr-news/xtalpi-holdings-announces-2026-interim-results):

| XtalPi | H1 2026 | Note |
|---|---|---|
| Revenue | RMB393.6M | H1 2025: RMB517.1M; +73.8% excluding a 2025 US$51M upfront |
| Drug discovery solutions | RMB200.1M | |
| AI4S intelligent solutions | RMB193.5M | +136% |
| Net loss | RMB224.9M | adjusted net loss RMB105.5M |
| Cash | RMB8.67B | |

  In materials, it has a JinkoSolar tandem-solar-cell JV.
- Taiwan: no domestic vendor found. TSMC uses NVIDIA cuEST for chemistry simulation (~50x; NVIDIA claim, unconfirmed; Jun 2026) — [IT Brief](https://itbrief.com.au/story/tsmc-uses-nvidia-ai-to-boost-chip-factory-efficiency).
- India: Discovered Materials ($9M seed, Aug 2026, Lightspeed India; AI agents for semiconductor materials) — [Inc42](https://inc42.com/buzz/discovered-materials-raises-9-mn-for-ai-led-semiconductor-material-discovery/). Novyte Materials (INR 4.15 crore pre-seed) — [ISN](https://indianstartupnews.com/funding/ai-material-discovery-startup-novyte-materials-raises-rs-415-crore-led-by-theia-ventures-10920772).
- Israel: no atomistic-simulation vendor found.

**Big technology**
- Microsoft: MatterSim is open source. It predicted tetragonal TaP; UT Dallas synthesised it and UIUC measured 152 W/m/K — [MSR, 12 May 2026](https://www.microsoft.com/en-us/research/blog/advancing-ai-for-materials-with-mattersim-experimental-synthesis-faster-simulation-and-multi-task-models/). Skala 1.1, a learned exchange-correlation functional (Aug 2026; MIT licence): first in 32 of 55 GMTKN55 categories at meta-GGA cost (company claim, unconfirmed). It is in CP2K and on Azure AI Foundry — [MSR](https://microsoft.com/en-us/research/blog/broadening-access-to-skala-creates-a-faster-path-to-predictive-dft); [Quantum Insider](https://thequantuminsider.com/2026/08/24/microsofts-skala-ai-model-joins-cp2k-to-improve-quantum-mechanical-simulations/).
- Google DeepMind: GNoME (Nov 2023; older): 2.2M crystals, 380k "stable", 736 independently synthesised; DFT-verified — [DeepMind](https://deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning/). Planned an automated UK materials lab for 2026 (opening not confirmed) — [Fortune](https://fortune.com/2025/12/10/google-deepmind-uk-government-partnership-science-clean-energy/).
- Meta FAIR: OMol25 has >100M DFT calculations (ωB97M-V) across 83 elements, costing "billions of CPU core-hours" — [arXiv](https://arxiv.org/abs/2505.08762). UMA checkpoints (incl. an r2SCAN fine-tune) are gated; commercial use is allowed except in China, Russia, Belarus and sanctioned states — [HF](https://huggingface.co/facebook/UMA).
- NVIDIA ALCHEMI: Toolkit on GitHub/PyPI; batched relaxation and MD NIMs (Mar 2026); a VASP NIM in early access (3x geometry optimisation). Lila reports 50x faster screening (company claim, unconfirmed) — [NVIDIA, 22 Jun 2026](https://blogs.nvidia.com/blog/ai-for-science-software-cuda/).

**New entrants (private; funding as reported)**
- CuspAI (Cambridge UK): $450M Series B at $2.6B (20 Jul 2026), co-led by Kleiner Perkins and NEA, with Bezos Expeditions, AMD Ventures and the UK Sovereign AI Fund. Prior round: $100M at $520M (Sep 2025); >$670M raised in total. Customers named: ASML and Meta. Its "AI Materials Foundry" has >45 partners incl. NVIDIA, Samsung and Hyundai. Revenue undisclosed — [Tech.eu](https://tech.eu/2026/07/20/jeff-bezos-and-sovereign-ai-back-cuspai-in-450m-raise).
- Orbital Industries (formerly Orbital Materials, London): $50M Series B (28 May 2026; led by Plural, with NVentures). It now sells PFAS-free cooling fluid and modular data-centre units — [Tech.eu](https://tech.eu/2026/05/28/orbital-industries-secures-50m-to-scale-data-centre-infrastructure-systems/). Dealroom estimates a $200M valuation (unconfirmed) — [Dealroom](https://dealroom.co/companies/orbital-industries/). Orb models are Apache-2.0 (OrbMol-v2, May 2026) — [GitHub](https://github.com/orbital-materials/orb-models).
- Periodic Labs (Menlo Park; co-founded by the GNoME lead): $300M seed (Sep 2025; a16z, NVIDIA, DST) at ~$1.3B (reported). Talks for ≥$500M at $7.5B (Forbes, May 2026) were never announced. Bloomberg reports semiconductor customers (unconfirmed); 64 staff — [Contrary](https://research.contrary.com/company/periodic-labs/quick-facts).
- Lila Sciences (Cambridge MA; Flagship): $550M raised; >$1.3B valuation (Reuters, Oct 2025). Talks for ~$2B at ~$8.5B pre-money, anchored by CalPERS and NVentures (Bloomberg, 3 Jun 2026); not announced — [Reuters/Yahoo](https://finance.yahoo.com/news/exclusive-ai-lab-lila-sciences-101645837.html); [Bloomberg Law](https://news.bloomberglaw.com/private-equity/lila-sciences-said-in-talks-for-funds-at-8-5-billion-valuation).
- Other entrants:
  - Radical AI: $55M seed+ (Jul 2025; RTX Ventures, NVentures) — [Pulse 2.0](https://pulse2.com/radical-ai-55-million-series-seed-raised-for-advancing-materials-research).
  - SandboxAQ: >$300M at $5.3B pre-money (Dec 2024) — [BiopharmaTrend](https://biopharmatrend.com/post/1085-ai-startup-sandboxaq-raises-300m-at-5b-valuation-amid-biopharma-partnerships). A 2026 $500M Series F at ~$13.4-13.9B appears only on aggregators (unconfirmed).
  - Rowan: $2.1M pre-seed (Dec 2024) — [PitchBook](https://pitchbook.com/profiles/company/680304-43).
  - Kairos Materials: #2 on Matbench (13 Sep 2026); nothing else found.

### Inferences
- Measured paid incumbent software revenue (Schrödinger ~$200M, Thermo-Calc ~EUR 12M) is smaller than the capital raised by AI-native entrants in 2025-26 (CuspAI alone >$670M). Capital, not revenue, now sets the pace.
- Two business types are lumped together. Tool vendors sell software (Schrödinger, VASP, Thermo-Calc, Matlantis). Discovery companies sell materials, hardware or IP (CuspAI, Orbital, Periodic, Lila, Radical, XtalPi AI4S); they resemble drug-discovery partnerships.
- The ecosystem is splitting: China's open models lead the benchmark while Meta's UMA licence excludes China.

### Gaps
- Revenue for VASP, Gaussian, Q-Chem, SCM, Materials Design, CompuTherm, Matlantis and DP Technology. No Taiwanese or Israeli vendor; India only seed-stage.

## 2. Boundary of trust: what simulation is accepted for, and what still needs an experiment

### Takeaway
Simulation is decisive for internal, reversible choices (which compound to make, which alloy composition to try, which candidate to screen). It is not accepted as final evidence where a third party bears the risk (drug approval, flight-critical allowables, claims of new materials). There, assays, tests and synthesis remain the judge.

### Cited Findings
- FEP in lead optimisation: with careful preparation, FEP accuracy can be "comparable to experimental reproducibility", based on 13,732 FEP+ relative binding calculations (Ross et al., Schrödinger authors, Commun Chem, Oct 2023; older) — [DOAJ](https://doaj.org/article/79d1308e170847339a53931494a3e639). In OpenFE's industry benchmark, 15 pharma partners ran blinded calculations on their own data (public: 59 systems/876 ligands; private: 37/864). FEP+ showed "superior low error performance". OpenFE was "competitive" at ranking but had more outliers, and private sets showed "a noticeable step down in accuracy" (6 May 2025) — [OMSF](https://omsf.substack.com/p/the-free-energy-of-everything-benchmarking-openfe). Both are judged against assay data.
- AI affinity vs FEP: Boltz-2 claims to "approach" FEP at ≥1000x lower cost (18 Jun 2025) — [bioRxiv](https://www.biorxiv.org/content/10.1101/2025.06.14.659707v1). An independent UCL test against the ESMACS physics method found r = 0.24 and 0.45 (16,780 and 21,702 compounds), with only 1-2 of the top-100 compounds overlapping (Mar 2026) — [arXiv 2603.05532](https://arxiv.org/abs/2603.05532).
- Regulators: ICH M15 (model-informed drug development) became final FDA guidance in June 2026. It harmonises how MIDD evidence is assessed (pharmacometrics/PBPK, not atomistic) — [FDA](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m15-general-principles-model-informed-drug-development). FDA's AI draft guidance (Jan 2025) uses a risk-based credibility framework tied to "context of use" — [FDA](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and-biological). FDA–EMA good AI practice principles followed in Jan 2026 — [FDA CDER](https://www.fda.gov/about-fda/center-drug-evaluation-and-research-cder/artificial-intelligence-drug-development). FDA's 10 Apr 2025 roadmap encourages computational toxicity models in INDs to "reduce, refine, or potentially replace" animal tests, but never says models alone suffice — [FDA](https://www.fda.gov/news-events/press-announcements/fda-announces-plan-phase-out-animal-testing-requirement-monoclonal-antibodies-and-other-drugs).
- CALPHAD/ICME in alloy qualification: QuesTek's computationally designed Ferrium S53 still qualified through AMS 5922 and MMPDS-05 (2008). Its design allowables were estimated with DARPA "Accelerated Insertion of Materials" methods from limited test data — [AeroMat 2006](https://asm.confex.com/asm/aero06/techprogram/paper_13923.htm). First flight came in Dec 2010 on a T-38 landing-gear piston — [CHiMaD 2014](https://chimad.northwestern.edu/docs/SRG2014/SRG2014_Grabowski.pdf). ASM calls it the first ICME-designed material qualified to AMS and MMPDS (Oct 2021) — [ASM](https://static.asminternational.org/amp/202110/23/). These sources are older, but this is still the reference case.
- Materials screening: GNoME verified candidates with DFT; 736 were made independently — [DeepMind](https://deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning/). The A-Lab critique (Leeman et al., PRX Energy, 2024) found significant issues in 42 of 43 claimed materials; about two-thirds were likely known disordered phases — [Chemistry World](https://chemistryworld.com/news/new-analysis-raises-doubts-over-autonomous-labs-materials-discoveries/4018791.article). MatterGen's "new" TaCr2O6 matches a compound known since ~1971-72 that was in its training data (Materials Horizons, 2026) — [RSC](https://pubs.rsc.org/en/content/articlelanding/2026/mh/d6mh00268d).
- Learned potentials checked against experiment: a Columbia–Schrödinger Nature paper (14 Oct 2026) paired MLFF dynamics with solid-state NMR. It found up to 40% of Li+ in multi-ion clusters in LiPF6/EC electrolytes (secondary coverage) — [Interesting Engineering](https://interestingengineering.com/energy/research-reveals-unexpected-lithium-ion-clusters).

### Inferences
- No regulator or standards body was found to accept atomistic or MLIP results as primary evidence. The regulator-accepted modelling (PBPK) sits next door, at Simulations Plus and Certara.
- The trust ladder in practice runs: ML or generative proposal → DFT check → synthesis and characterisation → novelty check → standards testing. AI shortens the first two steps; the rest remain the judge.

### Gaps
- No primary MMPDS text or recent (2025-26) CALPHAD-based qualification case; regulator positions in Japan, China and Korea not checked.

## 3. Accuracy evidence: arXiv 2605.08988, benchmarks, critiques, "propose and certify"

### Takeaway
arXiv 2605.08988 broadly supports the prior: out-of-distribution errors are "often an order of magnitude" higher than in-distribution. But the effect is task-dependent and confined to small organic molecules. Leaderboards measure agreement with DFT, not with experiment.

### Cited Findings
- arXiv 2605.08988, "Benchmarking Compositional Generalisation for Machine Learning Interatomic Potentials" (Nourollah, Khalid, Leoni, Schockaert; Cardiff; v1 9 May 2026, v2 22 Oct 2026). GMD benchmark: small H/C/N/O molecules in vacuum, with PBE/def2-TZVP+D3BJ labels. The abstract says OOD errors are "often an order of magnitude higher", even for foundation models — [abs](https://arxiv.org/abs/2605.08988). Appendix tables — [HTML v2](https://arxiv.org/html/2605.08988v2):
  - MACE force ratios (OOD/ID): chain extension 1.8x, fusion 18.9x, duplication 8.0x, combination 2.5x.
  - Energy ratios: up to 911x for MACE and ~23,000x for NequIP.
  - UMA-Small: force ratio ~1x on three tasks, but its ID error (0.015-0.099 eV/Å) is several times MACE's (0.003-0.005 eV/Å).
  - Fine-tuning lowers ID error but not the gap. More data fixes chain-length gaps; worked examples do not fix compositional gaps.
  - The text is inconsistent: the conclusions say "three orders of magnitude" for energy where the results show about two.
- Matbench Discovery (fetched 12 Nov 2026): #1 DPA-4.1-Max-OAM-PFT (CPS 0.913, F1 0.935; 31 Oct 2026); #2 Kairos; #4 ShanghaiTech; #5 Samsung; #8 EPFL; #11 Meta eSEN. All of the top 15 train on MPtrj+OMat24+sAlex and publish weights. The site calls rankings "not a complete assessment or an endorsement"; stability is scored against a DFT hull — [Matbench](https://matbench-discovery.materialsproject.org/). DPA-4's developers claim ~1-day training on one RTX 5090 (company claim, unconfirmed) — [DeepModeling](https://blogs.deepmodeling.com/DPA4_05_22_2026/).
- Systematic softening: M3GNet, CHGNet and MACE-MP-0 underpredict energy-surface curvature; fine-tuning with even one extra data point corrects it (May 2024; older) — [arXiv](https://arxiv.org/abs/2405.07105).
- Validation in practice:
  - MatterSim thermal conductivity sits within a ±50% band vs experiment. MatterSim-MT predicts BaTiO3 polarisation of 38 μC/cm² against 26 measured — [MSR](https://www.microsoft.com/en-us/research/blog/advancing-ai-for-materials-with-mattersim-experimental-synthesis-faster-simulation-and-multi-task-models/).
  - VASP's on-the-fly MLFF reports a "spilling factor" error estimate (ML_IERR) — [VASP changelog](https://vasp.at/wiki/index.php/Changelog).
  - Orb reports no benefit from float64 over float32 — [GitHub](https://github.com/orbital-materials/orb-models).

### Inferences
- "A learned model proposes and a conventional solver certifies" describes standard practice: GNoME, Matbench workflows, fine-tuning on DFT, VASP's on-the-fly MLFF, and Bunsen driving physics engines. But DFT is not the final certifier for real-world claims; DFT-"certified" novelty has failed experimental and database checks. Learned components now also sit inside solvers (Skala), blurring the line.
- With every top-15 model trained on the same data, leaderboard gains say little about OOD robustness. Tests like 2605.08988 matter more for buyers.

### Gaps
- OOD benchmarks for condensed-phase, charged or transition-metal chemistry; any independent benchmark of Matlantis PFP; the Matbench paper text (unreadable).

## 4. Open source and open models vs paid products; pricing pressure

### Takeaway
Free codes and open weights are near parity on benchmarks. Paid incumbents still grow because buyers pay for validated workflows, support, hosting and accountability. No direct price-cut evidence was found. The clearest pressure is on paid universal potentials, the "gap-filler" layer.

### Cited Findings
- Open codes:
  - GROMACS 2026.4 is current — [GROMACS](https://manual.gromacs.org/current/release-notes/index.html). CP2K ships Skala — [Quantum Insider](https://thequantuminsider.com/2026/08/24/microsofts-skala-ai-model-joins-cp2k-to-improve-quantum-mechanical-simulations/). OpenFE is MIT-licensed — [OpenFE](https://openfree.energy/).
  - Yet the most-used materials code at NERSC is licence-paid VASP — [CUG 2023](https://cug.org/proceedings/cug2023_proceedings/includes/files/pap130s2-file1.pdf).
  - Schrödinger's 10-K lists AMBER, CHARMM, GROMACS, OpenMM and OpenFF as competition, plus AI-first firms and pharma in-house tools — [10-K](https://www.sec.gov/Archives/edgar/data/1490978/000149097826000010/sdgr-20251231.htm).
- Open-weight potential licences:
  - MACE-MP-0/MPA-0 are MIT, but the newer MACE-OMAT/MATPES/OMOL weights use the academic ASL — [mace-foundations](https://github.com/ACEsuit/mace-foundations).
  - Orb is Apache-2.0 — [GitHub](https://github.com/orbital-materials/orb-models). UMA permits commercial use, with geographic exclusions — [HF](https://huggingface.co/facebook/UMA).
  - PET-MAD-1.6 is r2SCAN-trained over 102 elements (2026) — [arXiv](https://arxiv.org/abs/2603.02089).
- Paid potential: Matlantis's r2SCAN edge (PFP v8, Jul 2025) is now matched by open r2SCAN models (PET-MAD-1.6; a UMA r2SCAN fine-tune). Pricing is quote-only; no prices found — [Matlantis](https://matlantis.com/en/news/release-250716/).
- Incumbent demand: Schrödinger net dollar retention fell to 100% in 2025 (113% in 2024) and ACV grew 4%. Its 2026 ACV guidance is +12-17% (Q2 +27%) — [FY2025 8-K](https://www.sec.gov/Archives/edgar/data/1490978/000149097826000009/sdgr-20251231xexx991.htm); [Q3 8-K](https://www.sec.gov/Archives/edgar/data/0001490978/000149097826000075/sdgr-20260930x8kxexx991.htm). Certara software rose 11% in Q3 2026 — [Certara](https://www.sec.gov/Archives/edgar/data/0001827090/000182709026000034/q32026earningsreleaseex99.htm).
- Hardware: NVIDIA Rubin native FP64 is ~33 TFLOPS, about H100 level, against 35 PFLOPS FP4. Emulation helps only dense matrix work; AMD's Malaya says it "starts to break down" for materials codes (Jan 2026) — [The Register](https://www.theregister.com/2026/01/18/nvidia_fp64_emulation/).

### Inferences
- Open models displace paid products at the potential layer and in academia, not yet at the reference-data layer. MLIPs are trained on DFT labels, so DFT demand shifts toward generating training data (OMol25 used billions of core-hours).
- Falling FP64 per dollar tilts work from DFT toward low-precision MLIPs. That is a long-run threat to per-calculation DFT revenue, and it explains the VASP and QuantumATK GPU/MLFF push.

### Gaps
- Price lists or discounting data (Matlantis, VASP, Gaussian, Schrödinger); industry usage of open MLIPs.

## 5. Schrödinger in depth

### Takeaway
ACV is re-accelerating in 2026 while GAAP software revenue dips because of the hosted shift. Losses continue, funded by $373M of cash, no debt and lumpy milestones. Its lead in physics-based drug design is real but concentrated in a few customers. AI is sold through existing licences, not as a separately priced product.

### Cited Findings
- Q3 2026 (quarter to 30 Sep; reported 4 Nov 2026) — [8-K](https://www.sec.gov/Archives/edgar/data/0001490978/000149097826000075/sdgr-20260930x8kxexx991.htm); [10-Q](https://www.sec.gov/Archives/edgar/data/0001490978/000149097826000076/sdgr-20260930.htm):

| Schrödinger | Q3 2026 | Note |
|---|---|---|
| Revenue | $64.5M | +19% |
| Software revenue | $38.2M | +6%; on-premise $13.4M, hosted $17.2M (+49%; 45% of software), maintenance $4.6M, services $3.0M |
| Drug discovery revenue | $24.2M | incl. $12.0M Structure Therapeutics milestone |
| ACV | $44.7M | +17%; trailing four quarters $214M |
| Software gross margin | 75% | |
| Opex | $64.4M | -13% |
| Net loss | $37.7M | |
| Cash and securities | $373M | no debt |

  FY2026 guidance was raised: ACV $222-232M, drug discovery revenue $75-85M.
- 9M 2026: revenue $182.0M (+8%); software $106.3M (-9%); net loss $91.8M; operating cash flow -$96.5M. Concentration: two customers were 20% and 15% of Q3 revenue. Software RPO is $80.9M (Dec 2025: $105.1M); $241M of the at-the-market share programme is unused — [10-Q](https://www.sec.gov/Archives/edgar/data/0001490978/000149097826000076/sdgr-20260930.htm).
- FY2025: revenue $255.9M (+23%); software $199.5M; software gross margin 74%; net loss $103.3M. ACV $198.5M (+4%). Top-20 pharma ACV $80.8M = 41% of ACV, and all top-20 pharma are licensees. 27 customers above $1M ACV; NDR 100%; gross dollar retention 96%. 2028 targets: ACV +10-15% a year, software gross margin in the high 70s, positive adjusted EBITDA by end-2028 — [FY2025 8-K](https://www.sec.gov/Archives/edgar/data/1490978/000149097826000009/sdgr-20251231xexx991.htm). The 10-K says cash covers ≥24 months — [10-K](https://www.sec.gov/Archives/edgar/data/1490978/000149097826000010/sdgr-20251231.htm).
- Licensing: licences are typically one year and grant a set number of calculations, tiered by volume, customer class, size and region. Management calls this "throughput-based" — [10-K](https://www.sec.gov/Archives/edgar/data/1490978/000149097826000010/sdgr-20251231.htm); [Q1 call summary](https://reportify.cn/transcripts/1249350152028819456). Target: 75% hosted by end-2028. Each 1% hosted shift costs ~$2-3M of reported revenue; software gross margin went 69% (Q1) → 71% (Q2) → 75% (Q3) — [Q2 call highlights](https://www.gurufocus.com/news/9009674/schrodinger-inc-sdgr-q2-2026-earnings-call-highlights-acv-surges-27-on-bunsen-launch-and-strong-drug-discovery-milestones); [Earnings Whispers](https://www.earningswhispers.com/article/SDGR/r1557).
- AI and GPUs:
  - Bunsen, an agentic "co-scientist" that runs Schrödinger's physics, entered early access in Q2 2026 on NVIDIA and Google Cloud infrastructure — [Q2 8-K](https://www.sec.gov/Archives/edgar/data/1490978/000149097826000067/sdgr-20260630x8kxexx991.htm). BMS is deploying it across research (5 Aug 2026); full release is expected by end-2026 — [BioSpace](https://www.biospace.com/press-releases/schrodinger-announces-strategic-collaboration-and-software-agreement-with-bristol-myers-squibb-to-deploy-ai-co-scientist-bunsen-for-agentic-drug-discovery).
  - The CEO says its value shows up as more core demand "rather than a separate pricing model" — [GuruFocus](https://www.gurufocus.com/news/9009674/schrodinger-inc-sdgr-q2-2026-earnings-call-highlights-acv-surges-27-on-bunsen-launch-and-strong-drug-discovery-milestones).
  - Bunsen runs ~80% of internal high-throughput calculations, and an 80-target toxicology panel contributes to ACV (company claims, unconfirmed) — [Earnings Whispers](https://www.earningswhispers.com/article/SDGR/r1557).
- Strategy:
  - Since Nov 2025 it does not take programmes into the clinic alone (~$70M savings) — [Q3 2025 8-K](https://www.sec.gov/Archives/edgar/data/1490978/000149097825000116/sdgr-20250930xexx991.htm).
  - The Ajax sale to Lilly brought ~$57M (Jun 2026) — [8-K](https://www.sec.gov/Archives/edgar/data/1490978/000149097826000059/sdgr-20260629.htm).
  - The chief commercial officer left 18 May 2026 — [8-K](https://www.sec.gov/Archives/edgar/data/1490978/000149097826000041/sdgr-20260518.htm).
  - Novartis: $150M upfront, up to $2.272B in milestones — [10-K](https://www.sec.gov/Archives/edgar/data/1490978/000149097826000010/sdgr-20251231.htm).
- Published validations (2026): FEP+ on macrocycles (>230 compounds, 5 targets); absolute FEP for integrins; the Nature MLFF paper — [Q2 8-K](https://www.sec.gov/Archives/edgar/data/1490978/000149097826000067/sdgr-20260630x8kxexx991.htm); [Q3 8-K](https://www.sec.gov/Archives/edgar/data/0001490978/000149097826000075/sdgr-20260930x8kxexx991.htm).

### Inferences
- The lead is evidenced by universal top-20 pharma licensing and by OpenFE's concession on low-error performance. The risk is concentration: two customers made up 35% of Q3 revenue. Leaving Bunsen unpriced is a bet that agents raise calculation throughput, which the licences capture.

### Gaps
- Q3 2026 call transcript; hosted margin by product; materials-science revenue share; Bunsen customer count.

## 6. Revenue models across the segment, and moves to usage- or outcome-based pricing

### Takeaway
Usage or throughput pricing already exists (Schrödinger calculations, Rowan credits, Materials Square pay-as-you-go). Outcome pricing comes through milestones and royalties, or through selling products. Seat-and-capacity subscriptions (Matlantis) and one-off licences (VASP) persist at the reference layer.

### Cited Findings
- Throughput/usage:
  - Schrödinger licences grant a set number of calculations (section 5).
  - Rowan credits cost 4¢; CPU jobs use 1 credit/min, GPU jobs 3/min and H100/H200 jobs 7/min (≈$2.40, $7.20, $16.80 an hour). Team plans get 2,000 credits a week; FEP is Enterprise-only — [Rowan](https://rowansci.com/pricing).
  - Materials Square is pay-as-you-go — [ACerS](https://ceramics.org/company/virtual-lab-inc).
- Seat plus capacity: Matlantis is hosted, with contract-set user and compute caps; a stable PFP release about every 6 months, each supported 2 years; free trial — [service spec](https://matlantis.com/static/documents/en/service_specification_en_v1.0.pdf). QuesTek ICMD is SaaS (section 1).
- One-off: VASP charges a per-group licence fee with a 3-year upgrade window — [VASP FAQ](https://vasp.at/info/faq/).
- Outcome-based:
  - Schrödinger milestones and royalties (16 royalty-eligible programmes; up to ~$5B eligible milestones) — [FY2025 8-K](https://www.sec.gov/Archives/edgar/data/1490978/000149097826000009/sdgr-20251231xexx991.htm).
  - XtalPi out-licensing (a >$400M potential GPCR deal) and equipment sales — [XtalPi](https://www.thailand-business-news.com/pr-news/xtalpi-holdings-announces-2026-interim-results).
  - Orbital sells cooling fluid and units; Periodic Labs plans an "intelligence layer" — [Contrary](https://research.contrary.com/company/periodic-labs/quick-facts).
- Labour hours: Certara services are 49% of Q3 revenue — [Certara](https://www.sec.gov/Archives/edgar/data/0001827090/000182709026000034/q32026earningsreleaseex99.htm). Thermo-Calc and QuesTek both run services arms.

### Inferences
- The segment moved off pure seats earlier than CAE did. The live shift is toward outcome pricing by AI-native firms, which carries biotech-like risk (milestone timing, binary results).

### Gaps
- CuspAI and DP Technology pricing; ALCHEMI NIM licence cost.

## 7. Quality tests and transitions for the five that matter most; background views tested

### Takeaway
Strongest are Schrödinger (closest to a decision-grade method in pharma), VASP (the DFT reference that MLIPs train on) and Thermo-Calc (CALPHAD databases). Most exposed is Matlantis (a paid gap-filler facing open models). DP Technology is strong at home but opaque.

### Cited Findings (assessments built on sources in sections 1-6)
- **Schrödinger**
  - (a) Position: near-judge for binding affinity; assays still decide.
  - (b) Lead: all top-20 pharma license it; 27 customers >$1M ACV; OpenFE concedes its low-error edge.
  - (c) Revenue model: throughput licences shifting to hosted (45%), plus milestones.
  - (d) Finances: software gross margin 75%; 9M cash burn $96.5M; $373M cash; no debt; two customers = 35% of Q3 revenue.
  - (e) Resilience: ~40% non-US revenue; China via distributors.
  - Transitions: pricing by use already done; GPUs/cloud done (Bunsen on NVIDIA/Google); agents said (full release end-2026), BMS deployment done; learned models done (MLFF validated by NMR); regulators said (toxicology). Must go right: hosted margin back to the high 70s, and Bunsen lifting throughput.
- **VASP**
  - Owns the solid-state DFT reference; #1 NERSC code (2018 data); one-off licences; finances unknown.
  - Done: GPU port (OpenACC since 6.2); MLFF with error estimate. Said: AI agents (hire, Jul 2026). Defensive on AI cloning (Jun 2026).
  - Must go right: monetising MLFF/AI use beyond one-off licences.
- **Thermo-Calc**
  - CALPHAD databases are the de facto reference, though qualification still needs tests.
  - EUR 12.4M turnover; profitable; 72% equity ratio; foundation owner.
  - No agent or GPU move found; rival CompuTherm says it has LLM agents.
- **Matlantis**
  - A gap-filler with >150 customers (company claim, unconfirmed); not on Matbench; sold as seats plus capacity.
  - Agents done (May 2026) and ALCHEMI kernels done, but its r2SCAN edge has been copied by open models.
  - Must go right: workflow lock-in (crystal-structure prediction, reactions) and enterprise trust.
- **DP Technology**
  - Platform plus models; protected domestic market (UMA excludes China); #1 on Matbench via the DPA-4.1 consortium.
  - Revenue undisclosed; exposed to GPU export controls.

### Inferences
- AI-spending scenarios to 2030:
  - Steady growth (~55%): incumbents grow ACV ~10-15%; AI-natives keep raising.
  - Financing-led pause around 2028 (~25%): hits cash-burning AI-natives and Schrödinger's milestone and biotech demand hardest; foundation-owned or profitable Thermo-Calc and VASP are least affected.
  - Faster acceleration (~20%): lifts throughput-priced revenue (Schrödinger, Rowan) and DFT data generation (VASP), while commoditising paid potentials faster.
- Priors tested:
  - "MLIPs err ~10x on unseen molecules": partly supported (1-19x for forces, worse for energy), narrow scope.
  - "Learned model proposes, solver certifies": true for screening, false as final proof.
  - "Open source displaces paid": true at the MLIP layer, not yet visible in incumbent revenue.
  - "Owning a judge protects": supported, with FP64 hardware the main threat.

### Gaps
- Private-company financials; customer-level adoption of open MLIPs.

### Could not verify
- Schrödinger's Q3 2026 call transcript; Bunsen pricing beyond management remarks.
- Funding: Lila and Periodic Labs round closings; SandboxAQ 2026 Series F; Orbital's $200M valuation; Kairos Materials' identity.
- Status and revenue: DP Technology's Hong Kong IPO plans; DP Technology, Matlantis and VASP revenue; Gaussian's 2025-26 status.
- Primary Nature page for the Columbia–Schrödinger paper; OpenFE preprint RMSE values.
- NVIDIA: VASP NIM general availability; cuEST release; ALCHEMI pricing.
- Whether Thermo-Calc databases were used in designing Ferrium S53.

### Dated source list (key primary sources; all others inline)
- 2023 — CUG paper, VASP ~20% of NERSC: https://cug.org/proceedings/cug2023_proceedings/includes/files/pap130s2-file1.pdf
- 2024 — Leeman et al., PRX Energy (A-Lab critique): https://journals.aps.org/prxenergy/abstract/10.1103/PRXEnergy.3.011002
- 6 May 2025 — OpenFE industry benchmark: https://omsf.substack.com/p/the-free-energy-of-everything-benchmarking-openfe
- 25 Feb 2026 — Schrödinger FY2025 8-K and 10-K: https://www.sec.gov/Archives/edgar/data/1490978/000149097826000009/sdgr-20251231xexx991.htm ; https://www.sec.gov/Archives/edgar/data/1490978/000149097826000010/sdgr-20251231.htm
- Mar 2026 — UCL Boltz-2 evaluation: https://arxiv.org/abs/2603.05532
- 2026 — MatterGen critique, Materials Horizons: https://pubs.rsc.org/en/content/articlelanding/2026/mh/d6mh00268d
- 10 Mar–20 Jul 2026 — VASP releases and AI guidelines: https://vasp.at/info/post/
- Jun 2026 — FDA ICH M15 final: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m15-general-principles-model-informed-drug-development
- 22 Jun 2026 — NVIDIA ALCHEMI: https://blogs.nvidia.com/blog/ai-for-science-software-cuda/
- 20 Jul 2026 — CuspAI Series B: https://tech.eu/2026/07/20/jeff-bezos-and-sovereign-ai-back-cuspai-in-450m-raise
- 19 Aug 2026 — XtalPi interim: https://www.thailand-business-news.com/pr-news/xtalpi-holdings-announces-2026-interim-results
- 6 Oct 2026 — Simulations Plus closing: https://www.sec.gov/Archives/edgar/data/0001023459/000102345926000092/closingpr.htm
- 22 Oct 2026 — arXiv 2605.08988 v2: https://arxiv.org/html/2605.08988v2
- 4 Nov 2026 — Schrödinger Q3 8-K and 10-Q: https://www.sec.gov/Archives/edgar/data/0001490978/000149097826000075/sdgr-20260930x8kxexx991.htm ; https://www.sec.gov/Archives/edgar/data/0001490978/000149097826000076/sdgr-20260930.htm
- 5 Nov 2026 — Certara Q3 8-K: https://www.sec.gov/Archives/edgar/data/0001827090/000182709026000034/q32026earningsreleaseex99.htm
- Fetched 12 Nov 2026 — Matbench Discovery: https://matbench-discovery.materialsproject.org/ ; UMA licence: https://huggingface.co/facebook/UMA ; Matlantis profile: https://matlantis.com/en/company/profile/ ; Rowan pricing: https://rowansci.com/pricing
