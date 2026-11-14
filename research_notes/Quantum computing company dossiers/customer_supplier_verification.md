# Customer, supplier and partner verification of claims by IBM Quantum, Google Quantum AI, Quantinuum, IonQ, QuEra, PsiQuantum and IQM (as of 14 Nov 2026)

Source labels: **[V]** vendor-controlled (the quantum company's releases, blogs, filings, even when they quote a customer); **[J]** joint vendor-customer release or co-authored paper; **[C]** customer, host or buyer-controlled (including government buyers' own pages and procurement records); **[S]** supplier or partner-controlled; **[I]** independent (press, academics, aggregators). "(older)" means dated before 1 Jan 2026. "(dossier)" means the source is cited from a sibling dossier in this folder and was not re-opened in this session. "(excerpt)" means the content is known only from a search-engine excerpt and the page itself was not opened. USAspending figures come from my own queries of api.usaspending.gov on 14 Nov 2026 (spending_by_award and awards endpoints, recipient-name text and keyword filters, FY2008 to date). Dollar conversions marked "calc" are my arithmetic on filed percentages and totals.

## 1. Customers' own statements on results: do customers claim advantage over classical methods, or call the work exploratory? How do they differ from vendor descriptions?

### Takeaway
No customer in scope claims a demonstrated quantum advantage over the best classical methods in its own channel or its co-authored paper. HSBC's release comes closest ("world-first", "empirical evidence of the potential value"), but its own paper calls the method a "complementary explorative tool" and attributes the gain partly to hardware noise. The strongest wording ("outperforming classical", "narrow commercial advantage", large speedup multiples) comes from vendor releases. For AstraZeneca, Ansys, Mercedes-Benz, Boehringer Ingelheim and Moderna I found no customer-hosted statement, only quotes inside vendor releases or co-authored papers.

### Cited Findings
**HSBC (IBM): customer release vs customer-co-authored paper**
- HSBC's release (dated 25 Sep 2025 on the page; the downloadable PDF's filename begins "250923"; older) reports "up to a 34 percent improvement in predicting how likely a trade would be filled at a quoted price". The subheading phrases it as "up to 34% improvement in predicting the probability of winning customer inquiries in the European corporate bond market". — [HSBC, "HSBC demonstrates world's first-known quantum-enabled algorithmic trading with IBM", 25 Sep 2025](https://www.hsbc.com/news-and-views/news/media-releases/2025/hsbc-demonstrates-worlds-first-known-quantum-enabled-algorithmic-trading-with-ibm) [C/J]
  - Framing: "This is a ground-breaking world-first in bond trading" and "the world's first-known empirical evidence of the potential value of current quantum computers". It also calls the work a "Promising trial" that "delivered positive results on current quantum computing hardware" and "validated real and production-scale trading data on multiple IBM quantum computers".
  - Hedges: quantum computers "could potentially offer superior solutions over standard methods which use classical computers alone".
  - Philip Intallura (HSBC Group Head of Quantum Technologies): "a tangible example of how today's quantum computers could solve a real-world business problem at scale"; "we have great confidence we are on the cusp of a new frontier of computing in financial services".
  - IBM's Jay Gambetta: "Such work is essential to unlock new algorithms and applications."
  - The release does not mention backtesting, the role of hardware noise or any paper, and states no plan for production or live trading (my reading of the full page).
- The paper (arXiv:2509.17715, submitted 22 Sep 2025, 16 authors; affiliations not shown on the abstract page, HSBC and IBM per coverage) reports "a relative gain of up to ~ 34% in out-of-sample test scores", evaluated with a trade-execution backtest. It says "the inherent noise in current quantum hardware contributes to this effect and motivates further studies" and calls quantum computing "a complementary explorative tool in quantitative finance". It does not claim advantage. — [arXiv:2509.17715, "Enhanced fill probability estimates in institutional algorithmic bond trading using statistical learning algorithms with quantum computers", 22 Sep 2025](https://arxiv.org/abs/2509.17715) [J] (older)
- Independent critics:
  - Scott Aaronson called it "yet another 'qombie'". — [Shtetl-Optimized, 25 Sep 2025](https://scottaaronson.blog/?p=9170) [I] (older; dossier)
  - The Quantum Insider reports the authors say the gain is tied to one dataset, the 34% "remains puzzling", and the gain disappeared in noiseless simulation. — [The Quantum Insider, 28 Sep 2025](https://thequantuminsider.com/2025/09/28/bond-trading-quantum-bond-trading-a-deeper-look-at-hsbc-and-ibms-bond-trading-study/) [I] (older; dossier)
  - Global Trading said the claim "has been disputed by experts". — [Global Trading, 30 Sep 2025](https://www.globaltrading.net/experts-pour-cold-water-on-hsbc-quantum-computing-breakthrough/) [I] (older; dossier)

**JPMorganChase (Quantinuum): certified randomness and later work**
- JPMorganChase's page (26 Mar 2025) calls the work "the first to leverage this task of sampling to implement a potential useful cryptographic primitive". It uses no "advantage" or "beyond-classical" wording and makes no commercialisation claim. — [JPMorganChase Technology blog, "Certified randomness", 26 Mar 2025](https://www.jpmorganchase.com/about/technology/blog/certified-randomness) [C] (older)
  - Figures: a 56-qubit Quantinuum H2; about 2 s per circuit on the quantum computer against about 100 s estimated for the largest supercomputer; at least 71,313 bits of entropy, secure against an adversary "at least four times" more powerful than the largest supercomputer; verification on four supercomputers including Frontier, described as "computationally demanding".
  - Partners named: Quantinuum, ORNL, Argonne, UT Austin. Published in *Nature*.
- Vendor-side framing differs: coverage reports that Quantinuum said it would commercialise the certified-randomness protocol later in 2025, and that the authors acknowledge limitations for immediate production use. — [R&D World, Mar 2025](https://www.rdworldonline.com/nature-paper-details-first-experimental-generation-of-certified-randomness-via-quantum-computer/) [I] (older; excerpt)
- JPMorgan is also a Quantinuum shareholder and is named in the S-1 as a financial-services customer. Its statements are therefore not those of an arm's-length customer. — [Quantinuum S-1, 8 May 2026](https://www.sec.gov/Archives/edgar/data/0002110105/000162828026032836/quantinuum-sx1.htm) [V] (dossier)
- SoftBank and JPMorgan Chase were Helios early-access users (Nov 2025). — [Quantum Computing Report, 5 Nov 2025](https://quantumcomputingreport.com/quantinuum-launches-helios-quantum-computer-with-industry-leading-fidelity-and-singapore-partnership/) [I, relaying V] (older)
- Quantinuum's Q3 2026 release mentions "the largest cloud agreement in company history" with "a leading global financial institution", unnamed. — [Quantinuum Q3 2026 results, 5 Nov 2026](https://www.quantinuum.com/press-releases/quantinuum-reports-third-quarter-2026-results-and-raises-full-year-revenue-outlook) [V] (dossier)

**AstraZeneca (IonQ, with AWS and NVIDIA)**
- The only customer words I found are a quote inside IonQ's release (9 Jun 2025). Anders Broo (AstraZeneca, Executive Director, Pharmaceutical Science, R&D) calls it "an important step towards accurately modeling activation barriers for catalyzed reactions relevant to route optimizing in drug development". — [IonQ, "IonQ Speeds Quantum-Accelerated Drug Development Application With AstraZeneca, AWS, and NVIDIA", 9 Jun 2025](https://ionq.com/news/ionq-speeds-quantum-accelerated-drug-development-application-with) [V] (older)
  - The vendor release claims ">20x" speedup in time-to-solution versus prior benchmarks, and expected runtime cut "from months to days".
  - AWS's Eric Kessler, a partner, said future quantum computers are "not going to replace traditional compute, but instead accelerate specific, computationally intensive processing steps".
- The co-authored paper makes no quantum-advantage claim. Its speedups (9x measurement, 656x post-processing) are against a prior QC-AFQMC implementation, not against classical chemistry methods. — [arXiv:2506.22408, 27 Jun 2025](https://arxiv.org/abs/2506.22408) [J] (older; dossier)
- IonQ's CEO claimed "narrow commercial advantage", and The Quantum Insider called the work a proof of concept. — [The Quantum Insider, 9 Jun 2025](https://thequantuminsider.com/2025/06/09/ionq-speeds-quantum-accelerated-drug-development-application-in-partnership-with-astrazeneca-aws-and-nvidia/) [I] (older; dossier)
- No AstraZeneca-hosted release was found.

**Ansys (IonQ)**
- The release was issued by IonQ through Business Wire and titled "IonQ and Ansys Achieve Major Quantum Computing Milestone – Demonstrating Quantum Outperforming Classical Computing" (20 Mar 2025). It claims "12% faster performance over the classical computing alternative" on an LS-DYNA blood-pump problem, with up to 2.6M vertices and 40M edges. — [Business Wire (IonQ), 20 Mar 2025](https://businesswire.com/news/home/20250320514377/en/IonQ-and-Ansys-Achieve-Major-Quantum-Computing-Milestone-Demonstrating-Quantum-Outperforming-Classical-Computing) [V/J] (older; excerpt)
- The Quantum Insider's headline: "Hybrid Quantum Solver Simulated with IonQ Framework Delivers 12% Speedup; Hardware Validated on Small Instances". The 12% came from a simulated hybrid algorithm, with Forte validating only smaller instances. — [The Quantum Insider, 20 Mar 2025](https://thequantuminsider.com/2025/03/20/ionqs-devices-boost-ansys-simulations-achieving-up-to-12-faster-processing-over-classical-computers/) [I] (older; excerpt)
- The paper says "up to 12% for some problems". — [arXiv:2503.13128, 17 Mar 2025](https://arxiv.org/abs/2503.13128) [J] (older; dossier)
- I found no copy of the release on an Ansys-hosted page. [gap]

**BMW Group and Airbus (Quantinuum)**
- The joint release (2 Aug 2023) is posted on BMW Group's PressClub as well as Quantinuum's site. It describes a hybrid quantum-classical workflow for the oxygen reduction reaction on a platinum catalyst, in the paper "Applicability of Quantum Computing to Oxygen Reduction Reaction Simulations". It makes no advantage claim. — [BMW Group PressClub France, 2 Aug 2023](https://www.press.bmwgroup.com/france/article/detail/T0430258FR/bmw-group-airbus-et-quantinuum-collaborent-pour-accélérer-la-recherche-sur-la-mobilité-durable-à-l-aide-d-ordinateurs-quantiques); [Quantinuum, same release](https://www.quantinuum.com/press-releases/bmw-group-airbus-and-quantinuum-collaborate-to-fast-track-sustainable-mobility-research-using-cutting-edge-quantum-computers) [J] (older; excerpt)
  - Airbus's Isabell Gradert: "We can clearly envision the benefits of the study in our quest for sustainable and hydrogen powered alternatives such as the ZEROe aircraft."
- BMW Group was a Helios early user or collaborator in Nov 2025. — [Quantum Computing Report, 5 Nov 2025](https://quantumcomputingreport.com/quantinuum-launches-helios-quantum-computer-with-industry-leading-fidelity-and-singapore-partnership/) [I, relaying V] (older)
- Airbus and BMW are named among customers or collaborators in coverage of Quantinuum's S-1. — [The Quantum Insider, 26 May 2026](https://thequantuminsider.com/2026/05/26/honeywell-backed-quantinuum-files-for-landmark-quantum-ipo/) [I] (dossier)
- No Airbus or BMW statement from 2025–2026 on results was found.

**Mercedes-Benz (PsiQuantum)**
- The 2022 co-authored paper in *Physical Review Research*, "Fault-tolerant resource estimate for quantum chemical simulations: Case study on Li-ion battery electrolyte molecules", is a resource estimate for a future fault-tolerant photonic machine. No hardware was run. — [The Quantum Insider, 13 Apr 2022](https://thequantuminsider.com/2022/04/13/psiquantum-mercedes-benz-study-how-quantum-computers-can-accelerate-ev-battery-design/) [I] (older; excerpt)
  - The companies said simulating fluoroethylene carbonate is impossible on conventional computers and impractical on current machines.
  - PsiQuantum's blog says a fusion-based machine could do it "in under a day". — [PsiQuantum, "Counting qubits for better batteries"](https://www.psiquantum.com/research-soup/psiquantum-and-mercedes-benz-counting-qubits-for-better-batteries) [V] (older; excerpt)
- Engineering.com noted the study's aim was cost and requirements, not identifying a useful additive. — [engineering.com](https://www.engineering.com/?p=45191) [I] (older; excerpt)
- No Mercedes-Benz-hosted statement was found.

**Boehringer Ingelheim (PsiQuantum; earlier Google)**
- A co-authored preprint by PsiQuantum and BI's Quantum Lab (arXiv:2501.06165, Jan 2025) combines BLISS, tensor hypercontraction and PsiQuantum's Active Volume architecture. Reported speedups are 234x (cytochrome P450) and 278x (FeMoco). These are estimated runtimes on PsiQuantum's planned architecture, compared with prior fault-tolerant estimates, for "a platform still under development". — [The Quantum Insider, 15 Jan 2025](https://thequantuminsider.com/2025/01/15/psiquantum-boehringer-ingelheim-researchers-report-speedup-for-complex-molecular-simulations/) [I] (older; excerpt)
- A SAPT fault-tolerant algorithm paper (QC Ware, PsiQuantum, BI and Innsbruck) appeared in *PRX Quantum* 5, 010336 (2024). — [Quantum Zeitgeist](https://quantumzeitgeist.com/researchers-develop-quantum-algorithm-for-advanced-chemistry-calculations-aiding-drug-design) [I] (older; excerpt)
- PsiQuantum's write-up of QSP-EVE claims up to 1000x lower gate counts and 25% fewer qubits than prior methods, and notes current hardware cannot run it at scale. — [PsiQuantum, "PsiQuantum and Boehringer Ingelheim: Fault-tolerant quantum computation of molecular observables"](https://www.psiquantum.com/research-soup/psiquantum-and-boehringer-ingelheim-fault-tolerant-quantum-computation-of-molecular-observables) [V] (excerpt)
- No BI-hosted statement was found.

**Cleveland Clinic (IBM, with RIKEN)**
- Mar 2026: the 303-atom Trp-cage miniprotein was modelled on a Heron r2. Quantum Computing Report says relative conformer energies were "competitive with" MP2/CCSD classical benchmarks. — [IBM Quantum blog](https://www.ibm.com/quantum/blog/cleveland-clinic-protein-qcsc) [V]; [Quantum Computing Report](https://quantumcomputingreport.com/cleveland-clinic-and-ibm-implement-quantum-workflow-for-protein-simulation/) [I] (excerpt)
- 5 May 2026 joint release: protein complexes of up to 12,635 atoms (T4-lysozyme and trypsin in water) using IBM quantum computers plus two supercomputers, with the EWF-TrimSQD fragmentation method. — [Joint release, "Cleveland Clinic, RIKEN, and IBM Model a 12,635-Atom Protein…", via Bolsamania, 5 May 2026](https://www.bolsamania.com/nota-de-prensa_amp/mercados/cleveland-clinic-riken-and-ibm-model-a-12635-atom-protein---the-largest-known-to-be-simulated-with-quantum-computers--22413166.html) [J] (excerpt)
  - Quantum Computing Report: "a 40-fold increase in system size and a 210-fold improvement in accuracy" versus benchmarks from six months earlier, i.e. compared with earlier quantum runs, not with classical methods. — [Quantum Computing Report](https://quantumcomputingreport.com/cleveland-clinic-riken-and-ibm-simulate-12635-atom-protein-complex/) [I] (excerpt)
- Barron's reports the team "stopped short of claiming quantum advantage". Kenneth Merz (Cleveland Clinic) said the trajectory "suggests quantum computing may soon surpass the best purely classical approaches in chemical accuracy". — [Barron's via iTiger repost, "Quantum Will Supercharge Medicine. IBM's Milestone Proves the Future Is Near."](https://www.itiger.com/hant/news/2633996871) [I] (excerpt)
- IBM, a vendor, adds a further number: "Cleveland Clinic and RIKEN processed ~608 million samples ~33x faster with workflow automation". — [IBM, 11 Nov 2026](https://newsroom.ibm.com/2026-11-11-ibm-quantum-nighthawk-demonstrates-new-levels-of-speed-and-quality,-with-plans-to-scale-beyond-1,000-qubits-in-2027) [V] (dossier)
- The Cleveland Clinic newsroom page itself was not retrieved.

**E.ON (IBM)**
- E.ON's own release (2 Sep 2021, older) announced it as the first European utility to partner with IBM Quantum, for decentralised energy systems. — [E.ON via presseportal, 2 Sep 2021](https://www.presseportal.de/en/download/document/613093a63d00006991bd79ee-20210902-pm-quantencomputing-ibm-en.pdf) [C] (older; excerpt)
- E.ON, Qoro Quantum and the NQCC reported a preprint pipeline that cut quantum execution time by about 3x on IBM hardware. It mapped the PEGASE-1354 grid (1,354 buses, 1,710 lines) onto 156-qubit Heron processors. — [Quantum Computing Report, date not shown](https://quantumcomputingreport.com/e-on-qoro-quantum-and-nqcc-scale-constrained-optimization-on-ibm-heron-qpus-via-distributed-qaoa-and-spatial-packing/) [I] (excerpt)
- IBM claims an E.ON "15x speedup in quantum machine learning for grid optimisation" on Nighthawk r2. The comparison is with Heron, not with classical methods. — [IBM, 11 Nov 2026](https://newsroom.ibm.com/2026-11-11-ibm-quantum-nighthawk-demonstrates-new-levels-of-speed-and-quality,-with-plans-to-scale-beyond-1,000-qubits-in-2027) [V] (dossier)
- I found no E.ON statement on Nighthawk or the 15x figure.

**Moderna (IBM)**
- The co-authored preprint (arXiv:2505.05782, May 2025) ran instances of up to 156 qubits and up to 950 nonlocal gates, for mRNA sequences of up to 60 nucleotides. A noiseless tensor-network simulation scaled to 354 qubits. — [arXiv:2505.05782](https://arxiv.org/pdf/2505.05782) [J] (older; excerpt)
- 2024: 80 qubits on Heron for a 60-nucleotide sequence. The researchers acknowledged that "scalability of their methods to problem sizes exceeding 100 qubits remains an open question", and The Quantum Insider said calling it quantum advantage "may be a bit premature". — [The Quantum Insider, 3 Jun 2024](https://thequantuminsider.com/2024/06/03/moderna-ibm-quantum-researchers-use-quantum-computers-for-critical-step-in-rna-based-therapeutic-design/) [I] (older; excerpt)
- The only case study found is IBM's. — [IBM Quantum blog, "Moderna case study"](https://www.ibm.com/quantum/blog/moderna-case-study) [V]
- No Moderna-hosted statement was found.

**Differences between vendor and customer wording (summary)**
- HSBC: the release says "world-first" and "empirical evidence"; the paper says "explorative tool" and noise-dependent.
- Ansys: the IonQ-issued headline says "Quantum Outperforming Classical"; the paper says "up to 12% for some problems", with the headline result simulated.
- AstraZeneca: the IonQ CEO says "narrow commercial advantage"; AstraZeneca's quote says "important step towards"; the paper claims no advantage.
- JPMorgan: Quantinuum says it will commercialise; JPMorgan says "potential useful cryptographic primitive".
- Cleveland Clinic: the release says "largest… simulated"; Barron's says no advantage claim; Merz says "may soon surpass".

### Inferences
- The speedup multiples vendors attach to customers (E.ON 15x vs Heron; AstraZeneca 20x vs prior workflow; Cleveland Clinic 33x with workflow automation; 40x/210x vs runs six months earlier) compare against earlier quantum or hybrid runs, not against the best classical methods. On their own wording, none is an advantage claim.
- Customer-co-authored papers are consistently more cautious than the releases issued around them (HSBC, AstraZeneca, Ansys, Moderna).
- Several "customers" are also shareholders or ecosystem partners (JPMorgan in Quantinuum; NVIDIA and AWS in IonQ workflows). Their statements are partner statements, not arm's-length evaluations.
- Pharma and auto results with PsiQuantum (Mercedes, BI) are resource estimates for machines that do not yet exist. They cannot confirm or contradict present hardware performance.

### Gaps
- No customer-hosted page was found for AstraZeneca, Ansys/Synopsys, Mercedes-Benz, Boehringer Ingelheim, Moderna, or E.ON's 2026 work. The Cleveland Clinic newsroom original was not retrieved.
- JPMorgan's 2026 statements on Quantinuum were not found in JPMorgan channels. A quote attributed to Rob Otter ("Rapid hardware progress is compressing our time horizons…") surfaced only via a LinkedIn post and is unverified.
- No Airbus statement on quantum results in 2025–2026 was found. Airbus's current engagement status with Quantinuum is unknown.
- I found no statement from HSBC on whether the bond-trading method went into production.
- Google Quantum AI has no commercial customers to test. The sibling dossier found only grant-style NQCC Willow access (call 12 Dec 2025; first award to King's College London, 28 May 2026). — [NQCC, 12 Dec 2025](https://www.nqcc.ac.uk/updates/nqcc-and-google-quantum-ai-launch-new-initiative-to-accelerate-quantum-science-in-the-uk/) [C/gov] (dossier)

## 2. Deliveries and acceptance confirmed by hosts: dates, prices paid, acceptance status, published performance data

### Takeaway
Hosts' own channels confirm installation or inauguration for:
- RIKEN (IBM System Two, Jun 2025; Quantinuum Reimei, Feb 2025, upgraded to H2 by Nov 2026)
- Basque Government (IBM, Oct 2025)
- AIST (QuEra, installed May 2025, external access from Mar 2026)
- ORNL (IQM, Jun–Jul 2026)
- EuroHPC/LRZ (IQM Euro-Q-Exa, Feb 2026) and EuroHPC/IT4I (IQM VLQ, Sep 2025)
- EPB (IonQ Forte Enterprise, Sep 2026)
- Chungbuk (IQM Spark, Feb 2025)

No host publishes acceptance-test results or its own fidelity or benchmark data. Prices appear only for EU public buys (€25M, about €5M) and a reported AIST figure (¥6.5bn). Still unconfirmed or slipping as of 14 Nov 2026: Andhra Pradesh (IBM), KISTI (IonQ Tempo), Singapore (Quantinuum Helios), VTT 150-qubit (IQM) and CSC LUMI-IQ (IQM, 2027).

### Cited Findings
**RIKEN: IBM Quantum System Two (Kobe)**
- Joint release 23 Jun 2025: a 156-qubit Heron; IBM states a two-qubit error of 3×10⁻³ (best 1×10⁻³). — [IBM/RIKEN, 23 Jun 2025](https://newsroom.ibm.com/2025-06-23-ibm-and-riken-unveil-first-ibm-quantum-system-two-outside-of-the-u-s) [J] (older; excerpt)
- RIKEN's own notice (1 Jul 2025): a ceremony on 24 Jun 2025 at R-CCS Kobe marked "the launch of collaborative operation" of Fugaku and IBM Quantum System Two. — [RIKEN, 1 Jul 2025](https://www.riken.jp/en/news_pubs/news/2025/20250701_2/index.html) [C] (older; excerpt)
- RIKEN R-CCS (18 Nov 2025) lists "ibm_kobe" and "Reimei" as "already deployed". A new companion supercomputer (540 NVIDIA Blackwell GPUs, more than 21 PFLOPS FP64) was due in FY2025. The page gives no quantum performance figures and no user-access details. — [RIKEN R-CCS, 18 Nov 2025](https://www.r-ccs.riken.jp/en/outreach/topics/20251118-1/index.html) [C] (older; opened)
- Price paid: not disclosed by RIKEN or IBM in any source found.

**RIKEN: Quantinuum "Reimei" (Wako)**
- RIKEN and Quantinuum announced full operation on 12 Feb 2025. — [Quantinuum, "Quantinuum's Reimei quantum computer now fully operational at RIKEN"](https://quantinuum.com/press-releases/quantinuums-reimei-quantum-computer-now-fully-operational-at-riken-ushering-in-a-new-era-of-hybrid-quantum-high-performance-computing) [V/J] (older; excerpt). RIKEN's same-day page was not opened.
- Apr 2026: RIKEN announced procurement of an H2 to replace the 20-qubit H1. — [Kyodo News PR Wire, "RIKEN Scales Quantum-Supercomputing in Japan with Quantinuum System Upgrade", 15–16 Apr 2026](https://kyodonewsprwire.jp/release/202604167519) [J] (excerpt)
- 10 Nov 2026: the upgrade to System Model H2 (56 qubits) is complete, with an expanded partnership and SoftBank. — [The Quantum Insider, 10 Nov 2026](https://thequantuminsider.com/2026/11/10/quantinuum-riken-quantum-computing-partnership-japan/) [I] (excerpt); [Quantum Computing Report](https://quantumcomputingreport.com/riken-upgrades-reimei-fugaku-hybrid-quantum-platform-with-56-qubit-quantinuum-h2-processor/) [I] (excerpt)
- Vendor filing terms: "exclusive on premises access to a quantum processing unit" booked as a sales-type lease. The term is 45 months with fixed quarterly payments, and $21.6M of net investment in the lease was recorded at commencement in 2025. "Specialized quantum computing hardware" revenue of $16.526M was booked in 9M 2025. The 10-Q says one system is "on the RIKEN campus in Japan". — [Quantinuum 10-Q for Q3 2026, filed Nov 2026](https://www.sec.gov/Archives/edgar/data/2110105/000162828026072454/qnt-20260930.htm) [V] (opened)
- A Japanese-language search for a RIKEN procurement or award notice with a price found none.

**Basque Government: IBM Quantum System Two (Donostia-San Sebastián)**
- Inaugurated 14 Oct 2025 as Europe's first System Two, with two 156-qubit Heron processors in the Ikerbasque building. — [IBM newsroom, joint with Basque Government, 14 Oct 2025](https://newsroom.ibm.com/2025-10-14-the-basque-government-and-ibm-inaugurate-europes-first-ibm-quantum-system-two-in-donostia-san-sebastian) [J] (older; excerpt)
- Local press, 31 Dec 2025 (Idoia Alonso, NTM):
  - "A día de hoy se encuentra a un cuarto de su capacidad" (at a quarter of capacity).
  - Ten Basque research groups were running "primeros cálculos" (first calculations), and 23 entities had signed access agreements.
  - BasQ's Javier Aizpurua expected 50% capacity in January 2026.
  - Investment is "120 millones de euros hasta 2028" (€120M through 2028), co-financed by the Basque Government and provincial councils. This is the programme budget, not the IBM price.
  - Open access is "not contemplated" for now.
  - — [Onda Vasca, "El ordenador cuántico BasQ podría alcanzar la mitad de su capacidad en enero", 31 Dec 2025](https://www.ondavasca.com/el-ordenador-cuantico-basq-podria-alcanzar-la-mitad-de-su-capacidad-en-enero/) [I] (older; opened)

**TCS / Andhra Pradesh: IBM System Two (Amaravati)**
- Announced 2 May 2025 with a 156-qubit Heron, "subject to issuance of appropriate export licenses and closing definitive agreements". — [IBM newsroom, 2 May 2025](https://newsroom.ibm.com/2025-05-02-ibm,-tata-consultancy-services-and-government-of-andhra-pradesh-unveil-plans-to-deploy-indias-largest-quantum-computer-in-the-countrys-first-quantum-valley-tech-park) [J] (older; excerpt)
- Target dates have slipped repeatedly:
  - 1 Jan 2026 dedication. — [The Week, 2 May 2025](https://www.theweek.in/wire-updates/national/2025/05/02/mes11-ap-cm-ld-quantum-valley.html) [I] (older; excerpt)
  - Then "by March 2026". — [Outlook Business, Aug 2025](https://www.outlookbusiness.com/corporate/ibm-aims-to-debut-andhra-quantum-computer-by-march-2026-wants-india-to-focus-on-app-research) [I] (older; excerpt)
  - Then July 2026, in a report that cites 133 qubits, not 156. — [The Hans India](https://assets.thehansindia.com/andhra-pradesh/lokesh-sets-july-launch-for-ibm-quantum-system-in-amaravati-1041566) [I] (excerpt)
  - Then "full operational commissioning by September 2026". — [Quantum Computing Report, 3 Jul 2026](https://quantumcomputingreport.com/ibm-to-commission-one-of-indias-first-physical-quantum-computers-in-amaravati-by-september-2026/) [I] (excerpt)
  - Then "services may start January 2027" (Minister P. Narayana). — [Wikipedia citing The Hindu, 25 Aug 2026](https://en.wikipedia.org/wiki/Amaravati_Quantum_Valley) [I, secondary] (dossier)
- No report of installation or commissioning was found as of 14 Nov 2026.

**AIST (Japan): QuEra**
- AIST selected QuEra; the contract was reported at ¥6.5bn. — [The Quantum Insider, 30 Apr 2024](https://thequantuminsider.com/2024/04/30/aist-selects-queras-neutral-atom-quantum-computer-to-be-installed-alongside-nvidia-powered-abci-q-superco) [I] (older; dossier). The sibling dossier records a conflicting ¥5.4bn figure.
- Installed at Tsukuba in May 2025. — [The Quantum Insider, 29 May 2025](https://thequantuminsider.com/2025/05/29/quera-installs-first-quantum-computer-outside-its-lab/) [I, relaying V] (older)
- AIST's own SC25 panel lists the QuEra "Gemini" at 260 physical qubits, "available early 2026". — [AIST G-QuAT SC25 panel PDF](https://unit.aist.go.jp/g-quat/en/events/img/SC25/panels/02_Quantum01.pdf) [C] (older; excerpt)
- AIST notice of 24 Mar 2026: "ABCI-Q Starts Providing Quantum Computers Externally". It covers superconducting and neutral-atom machines, for NEDO-project joint research and external users, with "available access methods vary by quantum computer". — [AIST G-QuAT, 24 Mar 2026](https://unit.aist.go.jp/g-quat/HowToUse/en/news/news_en_20260324.html) [C] (excerpt; direct fetch failed with a connection reset)
- No AIST-published benchmark, acceptance result or usage statistics were found.

**UK NQCC testbeds**
- The QCTI Phase 1 report (21 Oct 2026) reprints supplier-written performance sections. For example, QuEra's CAST platform is described as having more than 200 physical qubits and more than 2,000 register sites. These are not NQCC measurements. — [NQCC QCTI Phase 1 report, 21 Oct 2026](https://www.nqcc.ac.uk/wp-content/uploads/2026/10/NQCC_Quantum-Computing-Testbed-Initiative_Phase-1-report.pdf) [C/gov, with S text] (dossier)

**Oak Ridge National Laboratory: IQM (and IonQ, IBM)**
- ORNL's own release (8 Jul 2026) on "Pathfinder", a 20-qubit IQM Radiance:
  - ORNL's first commercially procured on-premises quantum computer, owned and operated by ORNL.
  - Cooled by a Bluefors cryosystem.
  - No price and no fidelity data.
  - — [ORNL/OLCF, 8 Jul 2026](https://www.olcf.ornl.gov/2026/07/08/ornl-deploys-new-iqm-quantum-computer/) [C] (dossier)
- IonQ and ORNL ran a unit-commitment study on a 36-qubit Forte Enterprise (24 periods, 26 generators). ORNL's Suman Debnath described it, in IonQ's release, as a case study showing feasibility. It was part of DOE's GRID-Q project. I found no ORNL-hosted statement. — [IonQ via Business Wire, 31 Jul 2025](https://www.businesswire.com/news/home/20250731600318/en/IonQ-Partners-with-Oak-Ridge-National-Laboratory-Demonstrating-Quantum-Power-Grid-Optimization-Advancements) [V] (older; excerpt)
- ORNL's own release (5 Nov 2026) on an IBM–ORNL–AMD error-correction co-design platform notes IBM has shown up to 70 logical qubits and 438 "hard operations". DOE's target is 100 logical qubits running 100,000 hard operations by late 2028. — [ORNL, 5 Nov 2026](https://www.ornl.gov/news/ornl-ibm-and-amd-launch-new-co-design-platform-for-quantum-error-correction/) [C] (dossier)
- IBM's claimed "ORNL 12x" on Nighthawk has no ORNL statement behind it. — [IBM, 11 Nov 2026](https://newsroom.ibm.com/2026-11-11-ibm-quantum-nighthawk-demonstrates-new-levels-of-speed-and-quality,-with-plans-to-scale-beyond-1,000-qubits-in-2027) [V] (dossier)

**LRZ and IT4I: IQM (EuroHPC)**
- Euro-Q-Exa (54 qubits) at LRZ, inaugurated 12 Feb 2026:
  - Owned by the EuroHPC JU.
  - "Acquisition cost €25M": €10M EuroHPC JU, €15M BMFTR and the Bavarian ministry.
  - EuroHPC says the 150-qubit upgrade comes "by the end of 2026"; Commissioner Virkkunen says "early 2027".
  - — [EuroHPC JU, 12 Feb 2026](https://eurohpc-ju.europa.eu/inauguration-euro-q-exa-expanding-european-quantum-computing-infrastructure-2026-02-12_en) [C/gov] (dossier)
- VLQ (24-qubit star) at IT4I Ostrava, inaugurated 23 Sep 2025:
  - About €5M, split 50/50 between the EuroHPC JU and the LUMI-Q consortium.
  - Uses a Bluefors cryosystem.
  - — [EuroHPC JU, 23 Sep 2025](https://eurohpc-ju.europa.eu/vlq-europes-next-leap-towards-quantum-powered-research-and-innovation-2025-09-23_en) [C/gov] (older; dossier)
- IQM's claim that "LRZ in Germany has bought twice" — [IQM blog, 9 Sep 2026](https://iqm.tech/?p=20292) [V] (dossier). LRZ's own page on its first system was not retrieved.

**VTT and CSC (Finland): IQM**
- VTT has had 5-, 20- and 50-qubit IQM systems since 2021. VTT ordered 150 qubits (2026) and 300 qubits (2027); the 300-qubit machine is two 150-qubit processors with classical links. — [IQM, 20 May 2025](https://iqm.tech/?p=12802) [V] (older; dossier)
- IQM says the 150-qubit stage is "arriving late 2026". — [IQM blog, 9 Sep 2026](https://iqm.tech/?p=20292) [V] (dossier)
- Funding:
  - About €20M of Finnish state funding went to VTT for the first purchase. — [Teknologiateollisuus, 2 Jun 2026](https://teknologiateollisuus.fi/en/iqm-exports-quantum-computers-around-the-world-quantum-computing-is-our-next-major-opportunity/) [I] (dossier)
  - A €70M special government grant (2024) went to VTT for the 300-qubit system. — [eeNews Europe](https://www.eenewseurope.com/en/iqm-looks-to-the-end-of-the-nisq-quantum-era-with-300qubit-machine) [I] (older; excerpt)
- CSC selected IQM for LUMI-IQ on 8 Jul 2026, with delivery in 2027 and deployment in autumn 2027 at Kajaani. CSC states no value; IQM says €33M. — [LUMI/CSC, 8 Jul 2026](https://lumi-supercomputer.eu/iqm-selected-to-deliver-the-lumi-iq-quantum-computer/) [C] (dossier)
- No VTT-hosted confirmation of 150-qubit delivery or acceptance was found.

**KISTI (Korea): IonQ Tempo**
- IonQ says the agreement to deliver "Tempo 100" was finalised on 23 Dec 2025. — [The Quantum Insider (IonQ release), 23 Dec 2025](https://thequantuminsider.com/2025/12/23/ionq-and-kisti-finalize-agreement-to-deliver-100-qubit-quantum-system-in-south-korea/) [V] (older; excerpt)
- IonQ's 8-K of 25 Feb 2026 still called it "forthcoming". — [IonQ 8-K, 25 Feb 2026](https://www.sec.gov/Archives/edgar/data/1824920/000119312526071520/ionq-ex99_1.htm) [V] (dossier)
- KISTI's own announcement (19 Mar 2026) of a KISTI–NVIDIA–IonQ three-party MOU signed 18 Mar 2026 in San Jose:
  - Tempo, which "will be installed at KISTI", is to be physically connected to national supercomputer No. 6 "Hangang". Hangang starts operating in H2 2026. NVIDIA provides CUDA-Q.
  - KISTI states no qubit count, price, delivery date or acceptance criteria.
  - KISTI Director Lee Sik: "국가 슈퍼컴퓨터 6호기 한강과 양자컴퓨터 템포의 시너지를 극대화해…" ("maximise the synergy between national supercomputer No. 6 Hangang and quantum computer Tempo…").
  - — [Newsis, 19 Mar 2026](https://mobile.newsis.com/view/NISX20260319_0003556034) [I, reporting C] (opened)
- IonQ's Q3 2026 10-Q does not name KISTI. — [IonQ 10-Q, 5 Nov 2026](https://www.sec.gov/Archives/edgar/data/1824920/000119312526449829/ionq-20260930.htm) [V] (opened; searched)

**EPB (Chattanooga): IonQ Forte Enterprise**
- IonQ announced a "$22M deal" with EPB on 24 Apr 2025. — [Business Wire (IonQ), 24 Apr 2025](https://www.businesswire.com/news/home/20250424954681/en/IonQ-Announces-%2422M-Deal-with-EPB-Establishing-Chattanooga-Tennessee-as-the-First-Quantum-Computing-Networking-Hub-in-the-U.S) [V] (older; excerpt)
- EPB's own release (18 Sep 2026):
  - EPB "today launched" the Forte Enterprise and is "open for business" from early October 2026.
  - First customer: University of Tennessee at Chattanooga; a first Vanderbilt project is being lined up.
  - EPB Quantum Computing Fellows will run algorithms to optimise local power-grid circuits.
  - It cites a $4M NIST grant and IonQ's $15M for the Tennessee Quantum Communications Research Center.
  - It does not mention $22M and reports no results.
  - CEO Janet Rehberg: "Access to a quantum computer is rare and valuable."
  - — [EPB release via Fiber Broadband Association, 18 Sep 2026](https://fiberbroadband.org/2026/09/18/epb-launches-ionq-forte-enterprise-quantum-computer-in-chattanooga/) [C] (opened)

**Singapore: Quantinuum Helios**
- The NQO–Quantinuum partnership was announced 5 Nov 2025: Singapore would be the first country outside the US to host Helios, with NQCH (CQT, A*STAR IHPC, NSCC) as partner. — [Quantinuum, 5 Nov 2025](https://quantinuum.com/press-releases/singapores-national-quantum-office-and-quantinuum-forge-strategic-partnership-to-accelerate-quantum-computing) [V/J] (older; excerpt)
- The schedule has moved in Quantinuum's own documents:
  - "currently expected to be deployed in Singapore in late 2026" (10-Q, Nov 2026). — [Quantinuum 10-Q](https://www.sec.gov/Archives/edgar/data/2110105/000162828026072454/qnt-20260930.htm) [V] (opened)
  - "spring 2027" commissioning (Q3 2026 release, the same week). — [Quantinuum Q3 2026 release](https://www.quantinuum.com/press-releases/quantinuum-reports-third-quarter-2026-results-and-raises-full-year-revenue-outlook) [V] (dossier)
- A*STAR IHPC's page on the partnership returned "404: This page could not be found" on 14 Nov 2026. — [A*STAR IHPC](https://www.a-star.edu.sg/ihpc/news/news/press-release/nqo-and-quantinuum-forge-strategic-partnership-on-quantum-computing) [C] (checked)

**Chungbuk National University (Korea): IQM Spark**
- Korean press reports an operation ceremony hosted by Chungbuk Province on 28 Feb 2025 at CBNU:
  - A 5-qubit IQM Spark, described as the first commercial quantum computer procured through the government procurement system.
  - Goal: train 1,000 quantum workers by 2031.
  - — [CIO Korea](https://www.cio.com/article/3985975/iqm-%EC%B6%A9%EB%B6%81%EB%8C%80%EC%97%90-%EC%96%91%EC%9E%90%EC%BB%B4%ED%93%A8%ED%84%B0-%EA%B5%AC%EC%B6%95%C2%B7%C2%B7%C2%B7-6%EC%9B%94-%EC%A4%91-%EC%84%9C%EC%9A%B8-%EC%A7%80%EC%82%AC-%EA%B0%9C.html); [News Seoul](https://newsseoul.co.kr/news/view/1065568835011228) [I] (older; excerpt)
- IQM's site carries a CBQRC quote: "delivered on a fast 4-month timeline". — [IQM Spark page](https://iqm.tech/products/iqm-spark/) [V] (dossier)

**TSRI (Taiwan): IQM Spark**
- Purchase announced Nov 2024, with installation planned for Q2 2025. — [Go Photonics, relaying IQM](https://www.gophotonics.com/news/details/7373-taiwan-semiconductor-research-institute-chooses-iqm-spark-quantum-computer-to-boost-research) [I, relaying V] (older; excerpt)
- Taiwanese press reports TSRI's superconducting-quantum lab in Hsinchu Science Park "showcased" (展示) the 5-qubit computer built with IQM, on a 6 March date that coincided with NSTC launching phase 2 of the national quantum strategy. The year is not visible in the excerpt. — [iThome](https://www.ithome.com.tw/news/174257) [I] (excerpt)
- I found no TSRI or NARLabs release confirming formal acceptance or "啟用" (commissioning).

**Contradictions and qualifications recorded (deliveries)**
- Basque: the inauguration (Oct 2025) and "Europe's first" framing sit beside one-quarter capacity and restricted access at end-2025.
- EPB: the vendor headline says $22M; EPB's launch release omits it and cites $4M (NIST) and $15M (IonQ, a different centre).
- AIST: ¥6.5bn vs ¥5.4bn (dossier).
- Andhra Pradesh: 156 vs 133 qubits, and five successive target dates.
- Singapore: "late 2026" (10-Q) vs "spring 2027" (release).
- Euro-Q-Exa upgrade: "end of 2026" vs "early 2027" on the same EuroHPC page.

### Inferences
- "Delivered" and "inaugurated" do not mean "accepted at specification". No host in scope published acceptance criteria or test results, so acceptance status is unverifiable everywhere except for revenue-recognition hints in vendor filings (e.g., Quantinuum booking the RIKEN machine as a sales-type lease in 2025).
- Prices are disclosed only where EU public co-funding rules apply (EuroHPC) or in Japanese press (AIST). Asian and US host prices for IBM, IonQ and Quantinuum systems remain undisclosed.
- Every on-premises host confirmed here is public-sector or a public utility. EPB is municipally owned, and Chungbuk and TSRI are government-funded.

### Gaps
- RIKEN, KISTI, Japanese (GEPS/RIKEN) and Korean (KONEPS) procurement notices with prices: not found. A ₩48.2bn national-budget figure for a MSIT quantum service programme surfaced only in a search summary and could not be tied to a source page or to the Tempo price.
- Acceptance status for KISTI Tempo, VTT 150-qubit, Euro-Q-Exa upgrade, Singapore Helios and Andhra Pradesh: no host statement found.
- EU TED tender and award notices for EuroHPC or IQM: not searched this session.
- The Department of Industry FOI disclosure log (2026-095) could not be retrieved (HTTP 503, then connection reset).

## 3. Government customers: AFRL (IonQ), DOE, DARPA and other contracts with dollar values (USAspending.gov); Australia's terms with PsiQuantum

### Takeaway
USAspending confirms only a fraction of vendor-announced US government deals:
- Two AFRL contracts for PsiQuantum ($22.46M, 2022–24; and $10.84M, 2025–27, which I did not see in PsiQuantum's announcements).
- One AFRL contract for IonQ ($13.41M obligated, 2022–25).
- One Army award for Quantinuum ($3.98M, 2025–27).
- Small DARPA and AFRL awards for QuEra and IBM.

None of the DARPA QBI company awards appear under company names: neither IonQ's "up to $300M" Stage C, nor PsiQuantum's $31.8M and $125M, nor Quantinuum's Stage B. Neither do IonQ's announced $54.5M and $25.5M AFRL contracts. What USAspending does show for QBI is the government's own evaluator ($8.70M to UMD ARLIS) and the Illinois test site ($1.0M). Australia's published terms with PsiQuantum are equity plus loans tied to milestones. I found no published "sovereign access" clause.

### Cited Findings
**USAspending results by vendor (queried 14 Nov 2026; [C-gov record])**
- **IonQ**
  - Prime awards:
    - FA875022C1022 (Dept of the Air Force), "Trapped ion quantum computer": $13,414,043 obligated; period of performance 29 Sep 2022 to 28 Sep 2025. — [USAspending award](https://www.usaspending.gov/award/CONT_AWD_FA875022C1022_9700_-NONE-_-NONE-)
    - Missile Defense Agency SHIELD IDIQ HQ085926DG413 with a $500 initial order HQ085926FG316 (21 Jan 2026). — [USAspending award](https://www.usaspending.gov/award/CONT_AWD_HQ085926FG316_9700_HQ085926DG413_9700)
  - No IonQ-named record for:
    - the $54.5M AFRL contract IonQ announced on 27 Sep 2024 — [IonQ IR, 27 Sep 2024](https://investors.ionq.com/news/news-details/2024/IonQ-Announces-Largest-2024-U.S.-Quantum-Contract-Award-of-54.5M-with-United-States-Air-Force-Research-Lab/default.aspx) [V] (older)
    - the earlier $25.5M AFRL contract for barium systems at Rome, NY — [The Quantum Insider, 27 Sep 2024](https://thequantuminsider.com/2024/09/27/ionq-announces-54-5-million-contract-with-united-states-air-force-research-lab/) [I] (older; excerpt)
    - the $7.5M AFRL follow-on in Q3 2026 — [IonQ Q3 2026 8-K](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526449779/ionq-ex99_1.htm) [V] (dossier)
    - DARPA QBI Stage C, which IonQ describes as having "a potential value of up to $300 million" through 2029, with funding beyond the initial obligation "subject to future appropriations". — [IonQ, 7 Oct 2026](https://investors.ionq.com/news/news-details/2026/IonQ-Advances-to-Final-Stage-of-DARPAs-Quantum-Benchmarking-Initiative/default.aspx) [V] (dossier)
- **PsiQuantum**
  - Two AFRL awards are listed:
    - FA875022C1024, "Establishing state of the art integrated photonics for quantum computing applications": $22,458,948; 29 Sep 2022 to 28 Mar 2024. This matches the announced $22.5M AFRL contract.
    - FA875025CB030, "Integrating state of the art optical phase shifter in a photonics platform…": $10,835,118; 13 Mar 2025 to 13 May 2027.
    - — [USAspending FA875022C1024](https://www.usaspending.gov/award/CONT_AWD_FA875022C1024_9700_-NONE-_-NONE-); [USAspending FA875025CB030](https://www.usaspending.gov/award/CONT_AWD_FA875025CB030_9700_-NONE-_-NONE-)
  - No PsiQuantum-named record for the DARPA US2QC/QBI agreements of $31.8M (Sep 2025) and $125M (22 Jul 2026), or for the $100M CHIPS award. — [HPCwire (PsiQuantum release), 22 Jul 2026](https://www.hpcwire.com/off-the-wire/psiquantum-signs-125m-agreement-with-darpa/) [V] (dossier)
- **Quantinuum**
  - W911NF253A002 (Dept of the Army), "Physical Error Emulation to Logical Level (PEELL)": $3,979,300 obligated; 1 Oct 2025 to 30 Sep 2027. — [USAspending](https://www.usaspending.gov/award/ASST_NON_W911NF253A002_097)
  - No Quantinuum-named contract or IDV and no DARPA QBI record.
  - Quantinuum's 10-Q discloses a Commerce Department CHIPS "Other Transaction Agreement" dated 4 Sep 2026 for up to $100.0M:
    - $56.0M available on the award date, plus milestone payments of $32.0M and $12.0M.
    - "No amounts had been drawn under the Award as of September 30, 2026".
    - Commerce also acquired 2,369,528 Class A shares.
    - — [Quantinuum 10-Q, Q3 2026](https://www.sec.gov/Archives/edgar/data/2110105/000162828026072454/qnt-20260930.htm) [V] (opened)
- **QuEra**
  - 140D0422C0035, funded by DARPA and awarded via Interior: $1,500,000, Jul 2022 to Jul 2024, "Hardware-guided quantum algorithms and gate designs for near term neutral atom quantum computers".
  - HR001124P0310 (DARPA AQuA): $200,000, Aug to Dec 2024.
  - AFRL SBIR awards FA875020P1706 and FA875020P1708: about $150k each (2020).
  - No QBI Stage A or B record. — [USAspending 140D0422C0035](https://www.usaspending.gov/award/CONT_AWD_140D0422C0035_1406_-NONE-_-NONE-)
- **IBM** (keyword "quantum")
  - DARPA "Quantum Benchmarking Program" HR001122C0102: $2,087,796 (2022–23).
  - Army grant W911NF1410124, "Quantum validation and verification methods for superconducting qubits": $7,455,568 (2014–19).
  - AFRL FA875018C0098: $1,250,000 (2018–20).
  - No QBI Stage A/B/C record. — [USAspending HR001122C0102](https://www.usaspending.gov/award/CONT_AWD_HR001122C0102_9700_-NONE-_-NONE-)
- **Google:** no award with the keyword "quantum" under a Google recipient.
- **IQM:** no award to an IQM quantum entity. The IQM-named recipients (IQM Research Institute, IQM Tech Inc) are unrelated companies.
- **DARPA QBI evaluator and test site, the only QBI-labelled records:**
  - UMD Applied Research Laboratory for Intelligence and Security (ARLIS) delivery order HR001126FE003: $8,696,382 obligated; 6 Oct 2025 to 5 Apr 2027, potential end 5 Apr 2030. — [USAspending](https://www.usaspending.gov/award/CONT_AWD_HR001126FE003_9700_HQ003424D0003_9700)
  - Illinois Quantum and Microelectronics Park LLC, "Illinois DARPA Quantum Proving Ground (QPG) infrastructure supporting QBI": $1,000,000; 21 Apr 2025 to 30 Oct 2026. — [USAspending](https://www.usaspending.gov/award/ASST_NON_HR00112530327_097)
  - DARPA's QBI page lists IBM, IonQ and PsiQuantum in Stage C, Quantinuum and QuEra in Stage B, and Google in Stage A, as of 8 Oct 2026. — [DARPA QBI](https://www.darpa.mil/research/programs/quantum-benchmarking-initiative) [C-gov] (dossier)

**DOE**
- ORNL bought IQM's 20-qubit Pathfinder. The price is not disclosed, and DOE-lab purchases are made by the M&O contractor, so they do not appear as federal prime awards. — [ORNL/OLCF, 8 Jul 2026](https://www.olcf.ornl.gov/2026/07/08/ornl-deploys-new-iqm-quantum-computer/) [C] (dossier)
- No DOE prime award to any of the seven was found by the recipient and keyword queries.

**Australia: PsiQuantum terms (government's own documents and estimates reporting)**
- Treasury FOI 3641 (Finance estimates brief, 2024):
  - Each government invests A$466.4M "via an equity investment and loans", through Export Finance Australia on the National Interest Account.
  - Funding is tied to "agreed technology and infrastructure milestones" (commercial-in-confidence) with "security arrangements".
  - A$27.7M over 11 years is allocated for oversight.
  - PsiQuantum commits to an Asia-Pacific HQ in Brisbane, to "build and operate successive generations of its FTQC in Brisbane", and to "up to 400" jobs.
  - — [Treasury FOI 3641, Jul 2024](https://treasury.gov.au/sites/default/files/2024-07/foi-3641.pdf) [C-gov] (older; dossier)
- Loans of A$200M and A$75M at BBSY + 4.8%, plus a convertible equity instrument (US$125M, per the dossier). Neither loan nor equity conditions had been met at the Oct/Nov 2024 estimates. — [InnovationAus via Paul Fletcher MP site, 15 Nov 2024](https://www.paulfletcher.com.au/paul-media/innovationaus-govt-loan-untouched-psiquantum-capital-raise-incomplete) [I] (older; dossier)
- A$189.5M Commonwealth equity, as reported, citing the AFR. — [TechRepublic](https://www.techrepublic.com/article/psiquantum-australia-news/) [I] (older; excerpt)
- Dec 2025 Senate estimates: deputy secretary Helen Wilson said no drawdown had occurred. The Coalition said A$275M of federal loans were undrawn. — [Startup Daily, Dec 2025](https://www.startupdaily.net/topic/global-tech/psiquantums-brisbane-build-is-already-running-very-late/) [I] (older; excerpt)
- The site moved from Brisbane Airport to Moreton Bay Central (20–21 May 2026), with ground broken in June 2026. — [Business Wire (PsiQuantum), 20 May 2026](https://www.businesswire.com/news/home/20260520542043/en/PsiQuantum-Unveils-New-Australian-Site-at-Moreton-Bay-Central) [V]; [Startup Daily, 21 May 2026](https://www.startupdaily.net/topic/quantum-computing/psiquantum-moves-940m-quantum-build-brisbane-airport-moreton-bay/) [I] (dossier)
  - An aggregator says the operational target shifted to 2029. — [Pulse](https://www.pulse.bot/quantum/news/psiquantum-moves-620-m-quantum-computer-project-to-moreton-bay-delaying-launch-to-2029-81dcbba5-a7fd-4939-8554-178073d5ac3d/) [I, aggregator; uncorroborated] (excerpt)
- "Sovereign access": none of the government documents or reporting found specifies reserved or priority compute access for Australian government or researchers. The published commitments are HQ, local build/operate, jobs and partnerships.

### Inferences
- The mismatch between announced and recorded values reflects instrument type (DARPA QBI and Commerce CHIPS deals are Other Transaction agreements, which these USAspending queries did not surface under company names), ceilings vs obligations (IonQ's "up to $300M"; AFRL "$54.5M" vs obligations), and possibly reporting lag. It is not evidence that the deals do not exist. But it means most headline government values are vendor-stated ceilings that cannot be confirmed in public spending data.
- PsiQuantum has a second AFRL contract ($10.8M, Mar 2025 to May 2027) on the public record that is absent from the sibling PsiQuantum dossier's list of announced US awards.
- Australian money is conditional capital (equity and loans), not a purchase of compute. As of Dec 2025 the loans were undrawn, so it is not customer revenue for PsiQuantum.

### Gaps
- IonQ's $54.5M and $25.5M AFRL contracts: contract numbers and obligations not found. Whether either equals or modifies FA875022C1022 is unknown.
- DARPA QBI award amounts per company (Stages A–C) and DARPA's own statement of Stage C funding: not public in USAspending.
- DOE (national-lab subcontracts), NSF, and FPDS "Other Transaction" records: not queried.
- Australian agreement text (milestones, access terms) and any ANAO audit report: not found. The FOI disclosure log 2026-095 was unreachable.

## 4. Suppliers and partners: what they say about volumes, timelines and the state of the technology (GlobalFoundries, Linde, Honeywell Aerospace, AMD, NVIDIA, Bluefors/Oxford Instruments, SkyWater)

### Takeaway
Suppliers publish capability and capacity statements, not unit volumes. No supplier in scope disclosed quantum order volumes or contract values. The most concrete supplier-side financial signal is Oxford Instruments' 2025 sale of its quantum cryogenics unit: about £59M revenue and about £1M adjusted operating profit in FY25, sold for £60M. NVIDIA is simultaneously an investor in Quantinuum, PsiQuantum and QuEra, and an NVQLink integration partner of four of the seven (IonQ, IQM, Quantinuum, QuEra; not IBM, Google or PsiQuantum).

### Cited Findings
**GlobalFoundries (PsiQuantum; Quantinuum)**
- GF launched a "Quantum Technology Solutions" business on 21 May 2026, backed by a Commerce letter of intent for a $375M CHIPS award (not finalised). It says it will make QPUs plus cryogenic read-out and control chips. The release includes a PsiQuantum statement and an unnamed ion-trap company. — [GlobalFoundries, "GlobalFoundries launches Quantum Technology Solutions", 21 May 2026](https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions/) [S] (excerpt)
- Volume claims come from PsiQuantum, not GF:
  - Reuters headline: "Startup PsiQuantum says it is making millions of quantum computing chips". — [iTiger repost of Reuters, Feb 2025](https://itiger.com/news/2514285211) [I, relaying V] (older; excerpt)
  - PsiQuantum's chief scientific officer claimed yields that match standard semiconductors (excerpt).
  - An independent newsletter estimates industry-wide quantum-chip wafer volumes at "tens to hundreds of wafers" a year. — [Photoncap, "Quantum foundries: the revenue is…"](https://photoncap.net/p/quantum-foundries-the-revenue-is) [I] (excerpt)
- Quantinuum names GF as an onshore partner for "300 mm ion traps and electronics" under its CHIPS award, and as "one of several" foundries. — [Quantinuum 8-K exhibit, 8 Sep 2026](https://www.sec.gov/Archives/edgar/data/2110105/000162828026060934/quantinuum-finalizesx100.htm) [V] (dossier)

**Linde Engineering (PsiQuantum)**
- Linde will build and install a large cryogenic plant to cool "tens of thousands" of Omega chips to about 4 K. It will be built and tested offshore before installation in Brisbane (now Moreton Bay) "later this decade". Linde has installed more than 500 cryogenic plants. No contract value is given. — [Linde Engineering press release, May 2025](https://www.linde-engineering.com/news-and-events/press-releases/2025/linde-engineering-to-deliver-large-cryogenic-plant-to-psiquantum-in-australia) [S] (older; excerpt)
- PsiQuantum-side timing in the sibling dossier: cryoplant delivery in H2 2027 [V] (dossier). This is more specific than Linde's "later this decade".

**Honeywell Aerospace (Quantinuum ion traps)**
- Quantinuum's filings describe the arrangement:
  - Honeywell Aerospace ("AERO", spun off 29 Jun 2026) fabricates Quantinuum's ion traps under a 2026 Strategic Services and Supply Agreement.
  - Pricing is labour and materials plus 15%, with no purchase minimum, a 10-year term and automatic 5-year renewals.
  - AERO ceased to be a related party at the spin-off.
  - — [Quantinuum 10-Q, Q3 2026](https://www.sec.gov/Archives/edgar/data/2110105/000162828026072454/qnt-20260930.htm) [V] (dossier)
- No Honeywell Aerospace statement on volumes or timelines was found.
- USAspending "Honeywell + quantum" shows only DARPA Rydberg quantum-sensing contracts ($2,991,358, 2021–23; $804,798, 2025–26), unrelated to Quantinuum. [C-gov record]

**AMD (IBM decoding; PsiQuantum)**
- IBM ran a Relay-BP decoder for the gross code on a single AMD VU19P FPGA. It reports a 24 ns belief-propagation iteration, and 4-bit precision "sufficient to match a floating point implementation". — [arXiv:2510.21600, "Real-time decoding of the gross code memory with FPGAs", Oct 2025](https://arxiv.org/pdf/2510.21600) [V] (older; excerpt)
  - Press: about "10 times faster than needed". — [Tom's Hardware](https://www.tomshardware.com/tech-industry/quantum-computing/ibms-boffins-run-a-nifty-quantum-error-correction-algorithm-on-conventional-amd-fpgas-research-propels-ibms-starling-quantum-computer-project-forward) [I] (older; excerpt)
- AMD CTO Mark Papermaster is quoted: "We are very excited to be part of IBM's breakthrough in error correction for Quantum computing." The quote is known only from a search excerpt; its original post was not opened. [S] (excerpt)
- AMD hardware (MI355X GPUs, EPYC) is part of the ORNL–IBM–AMD co-design platform. — [ORNL, 5 Nov 2026](https://www.ornl.gov/news/ornl-ibm-and-amd-launch-new-co-design-platform-for-quantum-error-correction/) [C] (dossier)
- AMD plans an undisclosed equity investment in PsiQuantum. — [The Quantum Insider, 12 Nov 2026](https://thequantuminsider.com/2026/11/12/psiquantum-amd-expand-quantum-computing-infrastructure-partnership/) [I] (dossier)

**NVIDIA (NVQLink, CUDA-Q, NVentures)**
- NVQLink release (28 Oct 2025, older):
  - Text says "17 QPU builders", but names 19: Alice & Bob, Anyon, Atom Computing, Diraq, Infleqtion, IonQ, IQM, ORCA, OQC, Pasqal, Quandela, Quantinuum, Quantum Circuits, Quantum Machines, Quantum Motion, QuEra, Rigetti, SEEQC, Silicon Quantum Computing.
  - Five controller builders.
  - "Nine U.S. national labs", of which eight are named.
  - IBM, Google and PsiQuantum are not named. No latency or throughput figures are given.
  - Jensen Huang: "every NVIDIA GPU scientific supercomputer will be hybrid, tightly coupled with quantum processors"; this "marks the onset of the quantum-GPU computing era".
  - — [NVIDIA newsroom, 28 Oct 2025](https://nvidianews.nvidia.com/news/nvidia-nvqlink-quantum-gpu-computing) [S] (opened)
- NVentures investments: QuEra ($230M round, 2025), Quantinuum ($600M raise at $10B pre-money, Sep 2025), PsiQuantum ($1B Series E at $7B, Sep 2025). — [The Quantum Insider, 13 Sep 2025](https://thequantuminsider.com/2025/09/13/how-is-nvidia-betting-on-quantum-a-look-at-nventures-quantum-investment-playbook-from-skepticism-to-strategic-stakes/) [I] (older; excerpt); [DCD on PsiQuantum round](https://www.datacenterdynamics.com/en/news/psiquantum-raises-1bn-in-funding-including-from-nvidias-venture-capital-arm/) [I] (older; excerpt)
- NVIDIA is also party to customer deals: CUDA-Q in the AstraZeneca/IonQ workflow (9 Jun 2025) and the KISTI–NVIDIA–IonQ MOU (18 Mar 2026). See Sections 1 and 2.

**Bluefors and Oxford Instruments (dilution refrigerators)**
- Bluefors (2024): its expanded Syracuse, NY facility adds more than 35,000 sq ft and doubles cryocooler output, and lets Bluefors build dilution refrigerators in the US for the first time. CEO Jonas Geust says this makes Bluefors the largest US maker of dilution refrigerators. No unit volumes are given. — [Bluefors press release, 2024](https://bluefors.com/press-releases/bluefors-opens-expanded-u-s-production-facilities-becomes-biggest-producer-of-dilution-refrigerators-in-north-america/) [S] (older; excerpt)
- Bluefors' modular cryogenic platform: first multi-module delivery planned for "late 2026". — [Quantum Computing Report](https://quantumcomputingreport.com/bluefors-launches-modular-cryogenic-platform-for-large-scale-qubit-integration/) [I] (excerpt)
- Hosts confirm Bluefors cryosystems in ORNL's IQM Pathfinder and EuroHPC's VLQ (Section 2) [C] (dossier). IQM "relies on third-party cryostats" (DEFM14A) [V] (dossier).
- Oxford Instruments sold its NanoScience (quantum) business to Quantum Design for £60M (10 Jun 2025), including up to £3M deferred consideration tied to future "quantum scaling system revenue". NanoScience had about £59M revenue and about £1M adjusted operating profit in FY25. Rationale: refocus on materials analysis, semiconductors and healthcare. — [Oxford Instruments, 10 Jun 2025](https://www.oxinst.com/news/sale-of-oxford-instruments'-quantum-business,-nanoscience/) [S] (older; excerpt); [RNS via ticker.app](https://www.ticker.app/lse/OXIG/rns/2025-06-10/sale-of-oxford-instruments-quantum-business/1656M) [S] (older; excerpt)

**SkyWater (IonQ subsidiary since 31 Jul 2026)**
- Before the acquisition:
  - SkyWater's CEO described it as a "quantum foundry" with quantum customers "roughly doubling to seven". — [Oxbow Industries relaying EE Times, Dec 2025](https://oxbowindustries.com/2025/12/09/skywater-ceo-calls-company-quantum-foundry/) [I, relaying S] (older; excerpt)
  - A TD Cowen note lists PsiQuantum, D-Wave, Silicon Quantum Computing and QuamCore among them. — [Mark LaPedus Substack](https://marklapedus.substack.com/p/skywater-forms-foundry-alliance-with) [I] (excerpt; undated)
  - SkyWater and PsiQuantum expanded a silicon-photonics development agreement in 2023. — [DIGITIMES, May 2023](https://www.digitimes.com/news/a20230504VL203.html) [I] (older; excerpt)
- After the acquisition: D-Wave and SkyWater signed a multi-year extension (14 Oct 2026). SkyWater "continues to operate as a merchant foundry" for outside quantum developers. — [Quantum Computing Report, 14 Oct 2026](https://quantumcomputingreport.com/skywater-and-d-wave-extend-quantum-manufacturing-partnership-through-multi-year-agreement/) [I] (excerpt)
- No SkyWater quantum revenue figure was found. IonQ's claims about SkyWater output (12x wafer-lot output, design cycle down from nine months to two) are vendor statements. — [IonQ 8-K, 8 Sep 2026](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526384388/ionq-ex99_1.htm) [V] (dossier)

### Inferences
- Supplier statements support capacity build-out (GF unit, Bluefors plants, Linde plant) but give no volume data that could corroborate vendors' scaling timelines. The only quantitative supplier economics found (Oxford Instruments NanoScience: about £1M operating profit on about £59M revenue) point to thin margins in quantum cryogenics as of FY25.
- Partner overlap creates dependencies:
  - IonQ now owns the foundry (SkyWater) that also serves competitors and suppliers, including PsiQuantum (2023) and D-Wave.
  - NVIDIA invests in three of the seven and integrates four.
  - AMD partners with IBM and is investing in PsiQuantum.
  - GlobalFoundries serves both PsiQuantum and Quantinuum.
- Linde's "later this decade" is less specific than PsiQuantum-side "H2 2027", so the supplier statement does not confirm the vendor date.

### Gaps
- No unit-volume, order-book or revenue data from GF, Linde, Bluefors, AMD, NVIDIA or Honeywell Aerospace for quantum customers.
- No Honeywell Aerospace statement on trap production.
- Whether the PsiQuantum–SkyWater relationship continued after IonQ's acquisition is unknown.
- Whether the Oxford Instruments–Quantum Design sale closed, and Bluefors' 2026 order volumes, are not confirmed.
- NVQLink adoption status per vendor (production vs announced) is not known.

## 5. Revenue cross-check: do customers' procurement records or statements corroborate disclosed customer concentration?

### Takeaway
The concentration figures are confirmed in the vendors' own filings:
- RIKEN: 63% of Quantinuum's FY2024 revenue and 60% of FY2025.
- U.S. Government: 30% of Quantinuum's 9M 2026 revenue.
- Public sector: 99.5% of IQM's 2025 revenue.
- IonQ: one unnamed customer at 30% of Q3 2026 revenue.

Customer-side records corroborate the amounts only partly. No RIKEN price was found. Visible US federal obligations to Quantinuum ($3.98M Army) cover at most part of the roughly $6.7M implied for 9M 2026. IQM's public-sector total is consistent in order of magnitude with EuroHPC and Finnish public figures, but no record ties those amounts to specific revenue periods.

### Cited Findings
**Quantinuum: filed figures (10-Q, Q3 2026; opened)**
- Text: RIKEN "accounted for 17% of our revenue for the nine months ended September 30, 2026, 76% … for the nine months ended September 30, 2025, 60% … for the fiscal year ended December 31, 2025, and 63% … for the fiscal year ended December 31, 2024". The U.S. Government accounted for 30% of 9M 2026 revenue.
- Customer table: Customer A 16% (Q3 2026) and 24% (9M 2026); RIKEN ("Customer B") 19% and 17%; U.S. Government 32% and 30% (Q3 2025: 44%); Customer D 19% in Q3 2025.
- Revenue: $9.050M (Q3 2026), $22.285M (9M 2026), $2.715M (Q3 2025), $23.908M (9M 2025, including $16.526M hardware from the sales-type lease).
- Remaining performance obligations: $149.4M, of which 46.9% is expected within 12 months.
- — [Quantinuum 10-Q, Q3 2026](https://www.sec.gov/Archives/edgar/data/2110105/000162828026072454/qnt-20260930.htm) [V]
- Annual revenue: $23.0M (FY2024) and $30.9M (FY2025). — [Quantinuum 424B4/S-1 via sibling dossier](https://www.sec.gov/Archives/edgar/data/0002110105/000162828026032836/quantinuum-sx1.htm) [V] (dossier)
- Implied amounts (calc):
  - RIKEN: about $14.5M (FY2024), about $18.5M (FY2025), about $18.2M (9M 2025), about $3.8M (9M 2026), about $1.7M (Q3 2026).
  - U.S. Government: about $4.9M (FY2025, 16%), about $6.7M (9M 2026), about $2.9M (Q3 2026), about $1.2M (Q3 2025).
  - Customer A: about $5.3M (9M 2026).
- Customer-side corroboration:
  - RIKEN: no procurement record or price found. RIKEN's own pages confirm deployment only (Section 2).
  - The $21.6M net lease investment over a 45-month term is consistent in size with the 2025 RIKEN revenue (vendor-side only).
  - U.S. Government: USAspending shows the $3,979,300 Army PEELL award (from 1 Oct 2025). No DARPA QBI Stage B record is visible; DARPA's Stage B ceiling is up to $15M per company per the sibling dossier. The CHIPS award ($100M OT) had nothing drawn at 30 Sep 2026 and is an R&D award, not revenue as filed.

**IonQ: filed figures (10-Q, Q3 2026; opened)**
- Concentration: "one significant customer that accounted for 30% of total revenue" (Q3 2026) and "one significant customer that accounted for 16%" (9M 2026). In 2025, "three significant customers… 61%" (Q3 2025) and "two significant customers… 54%" (9M 2025). None is named.
- Revenue: $173.831M (Q3 2026), $318.549M (9M 2026), $39.866M (Q3 2025), $68.126M (9M 2025).
- Remaining performance obligations: about $1,168.0M, "including both funded… and unfunded… orders", of which about 50% is expected within 12 months.
- — [IonQ 10-Q, Q3 2026, filed 5 Nov 2026](https://www.sec.gov/Archives/edgar/data/1824920/000119312526449829/ionq-20260930.htm) [V]
- Implied (calc): about $52.1M (30% of Q3 2026) and about $51.0M (16% of 9M 2026). The near-equality suggests one customer whose revenue fell almost entirely in Q3 2026 (inference).
- The 10-Q text I searched does not mention KISTI, EPB, AFRL or DARPA by name.

**IQM: filed figures**
- Public-sector sales were 99.5% of 2025 revenue and 91.2% of 2024 revenue. Contracts are with universities, national research institutions and EuroHPC JU programmes. — [IQM/RF Acquisition DEFM14A, Jun 2026](https://www.sec.gov/Archives/edgar/data/0002052161/000119312526259964/d900375ddefm14a.htm) [V] (dossier)
- Revenue was €31.3M (2025) and €16.4M (2024). Implied public-sector revenue (calc): about €31.1M (2025) and about €15.0M (2024).
- Customer-side amounts (Section 2):
  - Euro-Q-Exa: €25M acquisition cost (inaugurated Feb 2026).
  - VLQ: about €5M (inaugurated Sep 2025).
  - VTT: about €20M state funding for its first purchase, plus a €70M grant (2024) for the 300-qubit programme.
  - LUMI-IQ: no value from CSC; €33M per IQM; delivery 2027.
  - ORNL, Chungbuk, TSRI: not disclosed.

**Contradictions and qualifications**
- None of the filed percentages is contradicted by a customer source.
- "Reportedly ~60% of 2025 revenue" (RIKEN) is confirmed exactly: 60% for FY2025. RIKEN's share then fell to 17% in 9M 2026 as US Government (30%) and the unnamed Customer A (24%) grew.

### Inferences
- The concentration claims are accurate as filed. Independent corroboration of the dollar amounts is weak because the dominant customers' payments run through instruments that do not publish prices: RIKEN's lease, DARPA OTs and EuroHPC procurements that report acquisition cost, not vendor revenue.
- For Quantinuum, the visible US federal obligation (about $4.0M, Army PEELL) equals about 60% of the implied 9M 2026 US Government revenue (about $6.7M). This is a ceiling on its contribution: it is an obligation for Oct 2025 to Sep 2027, so the revenue recognised from it in 9M 2026 is likely lower. Most of the US Government revenue therefore comes from awards not visible under Quantinuum's name, plausibly DARPA QBI Stage B (inference, unconfirmed).
- For IQM, public procurement values announced by hosts (€25M + about €5M + VTT's €20M) are of the same order as two years of public-sector revenue (about €46M, 2024–25). This is consistent with but does not prove the 99.5% figure, since revenue timing and IQM's share of "acquisition cost" are not disclosed.

### Gaps
- RIKEN contract values for the Quantinuum lease and the H2 upgrade, and for IBM System Two: not found in English or Japanese searches.
- Identity of Quantinuum's "Customer A" (24% of 9M 2026) and of IonQ's 30% customer: not disclosed.
- IQM revenue by customer and the IQM share of Euro-Q-Exa's €25M: not disclosed.
- EU TED award notices, Finnish Hilma notices (VTT, CSC) and German procurement records: not searched this session.
