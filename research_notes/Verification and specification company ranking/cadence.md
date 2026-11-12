# Cadence Design Systems, Inc. (NASDAQ: CDNS): chip verification and sign-off

Research date: 12 November 2026. All web checks were made on this date. This is the final version, merging an earlier partial pass with a continuation pass.

Tag key: [PRIMARY] filing or official document; [INDEPENDENT] confirmed by an outside party (customer, foundry, regulator, third-party data); [COMPANY CLAIM] stated by Cadence only; [SECONDARY] press, analyst or aggregator only; [UNVERIFIED] could not verify; [INFERENCE] my own reasoning or arithmetic from cited inputs.

Process note: the shared web-search budget ran out part-way through the continuation pass, and Firecrawl credits were exhausted. After that I only fetched known URLs (filings, transcripts, foundry pages, Yahoo Finance's daily-price endpoint). Items marked "via [file].md" are cross-referenced from other researchers' notes in this folder.

Overview: Cadence owns foundry-certified sign-off engines at every leading-edge foundry. It holds the larger share of emulation hardware and the de facto analog/custom standard. But the decisive final verdicts in timing and DRC/LVS sign-off are dominated by Synopsys PrimeTime and Siemens Calibre. Financially it is very strong: about 21% growth in 2026, about 45% non-GAAP margin, about 80% recurring revenue, and no customer at 10% or more. Its AI-agent strategy is shipping, but nearly all outcome claims are its own.

---

## A. Quality tests (judged without share-price or valuation data)

### a. Position: does Cadence own a "judge"?

#### Takeaway
Cadence owns certified judges in sign-off and analog/custom, plus the leading emulation hardware (a physical capacity constraint AI does not remove). The final timing and physical sign-off verdicts customers must pass, though, mostly run on competitors' tools, so Cadence is a certified challenger there. Its AI agents (ChipStack and other "Super Agents") are the weakest position on this test, as labour substitutes. Their stated purpose is to call Cadence's certified engines more often.

#### Cited findings: products
- **Sign-off: Tempus (timing), Quantus (extraction), Voltus (power/EM-IR), Pegasus (DRC/LVS), Certus, Liberate.** Foundry certification as of 2026:
  - **TSMC A16 and A14** (release 23 Sep 2026, NA OIP Forum): "digital full flow, signoff flow, and custom/analog flows are now certified".
    - The named digital flow is Innovus, Cerebrus, Tempus, EMX Planar 3D Solver, Voltus, Quantus, Pegasus and Liberate. Genus is only "enabled".
    - **N2P**: analog, digital and sign-off flows are certified, tools not named.
    - Artisan foundation IP for A14 is expected Q4 2026. Virtuoso claims "up to 2.5X" fewer iterations [COMPANY CLAIM].
    - TSMC quote from Aveek Sarkar (director, Ecosystem and Alliance Management).
    - Jasper, Xcelium, Conformal, Spectre, ChipStack and Super Agent are not mentioned. [PRIMARY; INDEPENDENT in part] — [release copy](https://finviz.com/news/394879/cadence-collaborates-with-tsmc-to-deliver-certified-tool-solutions-and-industry-leading-silicon-proven-ualink-ip-on-tsmc-advanced-processes)
  - TSMC's EDA Alliance grids (A14, A16, N2P, N3C, 3DFabric, "as of 10/01/2026") have columns only for Cadence, Synopsys and Siemens EDA. Categories include APR, timing, power, EMIR, DRC, LVS/LPE, RC, custom design and simulators. Per-cell status could not be machine-read. [PRIMARY] — [TSMC](https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance) (also in china.md / japan_korea_taiwan.md)
  - Same forum: Synopsys showed A14-certified flows from implementation to sign-off, and Siemens had Calibre nmDRC/nmLVS/xACT/PERC certified for A14. [SECONDARY] — [Futurum](https://futurumgroup.com/insights/tsmcs-oip-forum-turns-agentic-chip-design-demos-into-production-flows/)
  - **Samsung second-generation 2nm** (release 28 May 2026, SAFE Forum; copy dated 1 Jun 2026): a "comprehensive, certified flow" covering Innovus, Virtuoso Studio and Integrity 3D-IC.
    - Tempus and Quantus are named as the sign-off tools, and Pegasus plus Tempus appear in the 3D Cube-H hybrid-bonding flow.
    - A new multi-year agreement broadens memory and interface IP. Samsung quote from Jongshin Shin (EVP, head of Foundry Design Platform Development).
    - SF2/SF3 certification was first announced in 2023. A Cadence blog of 31 Jul 2026 reportedly extends the flow to SF2P (search summary only). [PRIMARY + Samsung quote] — [design-reuse](https://www.design-reuse.com/news/202530589-cadence-and-samsung-foundry-deepen-2nm-and-3d-ic-collaboration-to-meet-surging-ai-infrastructure-and-physical-ai-demand/) ; [Business Wire](https://www.businesswire.com/news/home/20260528147066/en/)
  - **Intel 18A-P and 14A** (release 27/28 Jul 2026): AI-driven digital and custom reference flows are "certified on Intel 18A-P and Intel 14A" on "the latest Intel Foundry process design kits".
    - Scope: synthesis, place and route, timing and power sign-off, physical and reliability verification, and analog/custom; also an EMIB/EMIB-T packaging flow and a multi-year DTCO agreement for 14A. IP test chips have been validated on 18A.
    - Intel quote from Shawn Han (SVP & GM, Foundry Services): "Through co-optimized, certified design flows and silicon-validated IP, we give our customers greater confidence".
    - Individual tools and PDK versions are not named in the copy I read. A secondary headline says 18A-P PDK 1.0 and 14A PDK 0.5. Intel 18A flows were certified in 2025 (search summary). [PRIMARY + Intel quote] — [HPCwire](https://www.hpcwire.com/off-the-wire/cadence-certifies-ai-driven-reference-flows-for-intel-18a-p-and-intel-14a/) ; [Electronics World](https://www.electronicsworld.co.uk/ai-driven-digital-and-custom-reference-flows-tools-and-solutions-by-cadence-are-now-certified-on-intel-18a-p-pdk-1-0-and-intel-14a-pdk-0-5-technologies/42129/) ; [Cadence blog, 2025](https://community.cadence.com/cadence_blogs_8/b/corporate-news/posts/cadence-digital-and-custom-analog-flows-certified-for-latest-intel-18a-process-technology)
  - **Rapidus 2nm**: only a December 2024 collaboration was found, with reference flows "in development" (Cerebrus, Genus, Innovus, Tempus, Quantus, Voltus, Pegasus). Synopsys signed a parallel deal. Cadence says Rapidus will integrate InnoStack into its AI-Agent Design Solution, "targeting up to a 2X faster design turnaround" (Q2 2026) [COMPANY CLAIM]. No certification was found. [PRIMARY 2024 / UNVERIFIED 2026] — [Business Wire 2024](https://www.businesswire.com/news/home/20241210546692/en/Cadence-and-Rapidus-Collaborate-on-Leading-Edge-2nm-Semiconductor-Solutions-for-AI-and-HPC-Applications) ; [eeNews](https://www.eenewseurope.com/en/rapidus-signs-2nm-deals-with-synopsys-cadence/)
  - Market reality (SemiAnalysis estimates, 21 May 2026): PrimeTime has "90%+" of timing sign-off and Calibre "85%+" of physical verification. TSMC specifies "Calibre-clean" DRC/LVS, and Samsung and Intel reportedly do the same. [SECONDARY] — [SemiAnalysis](https://newsletter.semianalysis.com/p/eda-market-primer)
  - The 10-K says Cadence develops PDKs with foundries "to ensure our core EDA products and solutions meet manufacturing sign-off requirements". [PRIMARY] — [FY2025 10-K](https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf)
- **Jasper (formal) and Conformal (equivalence).**
  - These are proof-type judges of functional correctness, outside foundry certification, which covers physical and electrical flows. The 10-K names Jasper and Xcelium as the two functional-verification products.
  - Devgan (Q3 2026) cited "strength of palladium and strength of Jasper", without figures. ChipStack integrates with Jasper and Xcelium.
  - No third-party share data was found, and Conformal does not appear in the 2026 releases I read. [PRIMARY / COMPANY CLAIM] — [Q3 call](https://www.webull.com/news/15818016766808064)
- **Xcelium (simulation)**: estimated at about 40–45% share against VCS at 45–50%. It is a workhorse, not a judge. [SECONDARY estimate]
- **Palladium / Protium (emulation and prototyping).**
  - Palladium is estimated at 55–60% of a $1.5bn+ emulation market, with ZeBu at 35–40% [SECONDARY estimate].
  - Hardware had "another record quarter, driven by continued strength in Palladium Z3 and Protium X3" (Q2 2026) [PRIMARY].
  - Devgan (Q1 2026): "Palladium Z3 continues to be the gold standard for emulation and drove multiple competitive displacement"; "we'll have a Z4 system before 2030" [COMPANY CLAIM].
  - The DVCon US 2026 paper (2–5 Mar) describes Dynamic Duo III (custom Z3 processor plus AMD VP1902 FPGAs), "scalable to 48 billion gates" [COMPANY CLAIM, via market_structure_emulation_vip.md] — [DVCon](https://dvcon-proceedings.org/wp-content/uploads/Broadening-the-Adoption-of-Hardware-Assisted-Verification-with-Next-Generation-Emulation-Appliance.pdf)
- **Verisium** (gen-AI verification and debug) and **verification IP**: described in the 10-K (VIP "integrates seamlessly with" Xcelium and Palladium). No outside evidence or share data was found. These are gap-fillers on this test. [PRIMARY description only]
- **Virtuoso / Spectre (custom/analog).**
  - Virtuoso is "considered the industry standard" (10-K) [COMPANY CLAIM]. SemiAnalysis says it has "no credible competitor", with 450+ customers (Q4 2024) [SECONDARY].
  - Cadence reports "a significant competitive win with Spectre at a leading semiconductor supplier" (Q2 2026) [COMPANY CLAIM].
- **Innovus (place and route)**: gained 10–15 percentage points against ICC2 in 2015–2020, then stabilised after Fusion Compiler launched. [SECONDARY]
- **Agents**: ChipStack (front-end design and verification), InnoStack (digital), ViraStack (analog), AuraStack (PCB/packaging), AgentStack (orchestration) and Maestro.
  - Framing (Q2 2026): "deterministic, physics-based engines, proprietary silicon correlated data" in the middle layer, and "autonomous agents ... call our underlying physically accurate engines more often". [PRIMARY] — [Q2 2026 prepared remarks](https://s206.q4cdn.com/597110084/files/doc_financials/2026/q2/CDNS-Q2-2026-Earnings-Conference-Call-Prepared-Remarks.pdf)

#### Inferences
- [INFERENCE] Cadence's strongest positions are certified sign-off and implementation engines at all three leading-edge foundries, Palladium's lead in hardware capacity, and Virtuoso. In sign-off it is "certified and gaining", not "the gate everyone must pass".
- [INFERENCE] Jasper and Conformal fit best with the prior that machine-proved regression checks become standard. They are also the products with the thinnest outside evidence.

#### Gaps
- Third-party share for Jasper, Conformal, Tempus, Voltus, Quantus, Pegasus and VIP. The SemiAnalysis competitive section is paywalled, and searches were unavailable.
- Per-tool TSMC grid status; certification at Rapidus.

### b. Lead: outside evidence of a technical and commercial lead

#### Takeaway
Outside evidence supports a lead in emulation, analog/custom and foundry enablement. Cadence also grew faster than the industry and than Synopsys's EDA business in 2026, which fits share gains. There is no outside evidence of a lead in timing or physical sign-off. Agent results and named deployments are Cadence's own statements.

#### Cited findings: outside evidence
- All three leading-edge foundries put executive quotes on 2026 certification releases, and TSMC's grids list only the three incumbents (see a). [INDEPENDENT in part]
- Share estimates (SemiAnalysis, 21 May 2026): Palladium 55–60% vs ZeBu 35–40%; Xcelium 40–45% vs VCS 45–50%; PrimeTime 90%+; Calibre 85%+. ZeBu/HAPS had a record year but "remains well behind Cadence's Palladium". [SECONDARY] — [SemiAnalysis](https://newsletter.semianalysis.com/p/eda-market-primer)
- Industry versus Cadence:
  - SEMI ESD Alliance industry revenue was $5,710.8m in Q2 2026, up 12.2%. Cadence's Q2 revenue rose 24%, including Hexagon.
  - Synopsys EDA grew 8.5% (quarter to July 2026), against Cadence Core EDA at +18% (Q2) and +20% (Q3). Segment definitions differ.
  - [INDEPENDENT industry data; via market_structure_emulation_vip.md and synopsys.md] — [ESD Alliance](https://www.prnewswire.com/news-releases/electronic-system-design-industry-posts-5-7-billion-in-revenue-in-q2-2026--esd-alliance-reports-302912151.html) ; [Synopsys Q3 FY2026 call](https://www.webull.com/news/15497781661541376)
- Competitors also report records in hardware-assisted verification:
  - Synopsys: "another record quarter", "12 new and 66 repeat HAV customer wins" (26 Aug 2026). Its March 2026 HAV launch carried an NVIDIA quote.
  - Siemens with Nvidia announced Veloce proFPGA CS (9 Apr 2026).
  - [PRIMARY competitor sources, via synopsys.md / market_structure notes] — [Synopsys HAV](https://news.synopsys.com/2026-03-11-Synopsys-Introduces-Software-Defined-Hardware-Assisted-Verification-to-Enable-AI-Proliferation) ; [Siemens–Nvidia](https://news.siemens.com/en-us/siemens-nvidia-veloce/)
- Demand context: the Siemens-sponsored Wilson Research study (8 Sep 2026; 604 respondents) finds verification takes 49% of IC/ASIC project time and first-silicon success was 5% in 2026 vs 14.4% in 2024, with a methodology break in 2024. [SECONDARY, competitor-sponsored] — [Siemens](https://blogs.sw.siemens.com/verificationhorizons/2026/09/08/the-2026-functional-verification-study/)
- Kimi K3 still needed EDA tools (open-source, 45nm), as BNP Paribas and Mizuho noted (see B). [SECONDARY]
- Competitors named in the 10-K: Synopsys (incl. Ansys), Siemens EDA, Keysight, Schrödinger, CEVA, Altium (Renesas), Zuken, and "emerging players in China such as Huada Empyrean, Xpeedic". [PRIMARY]

#### Cited findings: Cadence's claims (not confirmed by the customers in the sources I read)
- "we are gaining share in almost all segments of our business"; "16 new full flow wins during the quarter" (Q3 2026). [COMPANY CLAIM] — [Q3 call](https://www.webull.com/news/15818016766808064)
- Sign-off claims:
  - Q2 2026: "expanded adoption of Tempus and Certus signoff tools on leading edge designs, with wins across hyperscalers, top semiconductor companies and startups"; "expanded our implementation and signoff footprint at frontier AI companies as well as at a marquee ASIC silicon vendor".
  - Q1 2026: "a marquee AI infrastructure company expanded their usage of our signoff solutions".
  - No customer named. [COMPANY CLAIM] — [Q2 remarks](https://s206.q4cdn.com/597110084/files/doc_financials/2026/q2/CDNS-Q2-2026-Earnings-Conference-Call-Prepared-Remarks.pdf) ; [Q1 call](https://www.fool.com/earnings/call-transcripts/2026/04/27/cadence-cdns-q1-2026-earnings-transcript/)
- Hardware: "We added 12 new logos" and "a notable competitive win with a major AI infrastructure provider" (Q2). No hardware customer was named on the Q3 call. [COMPANY CLAIM]
- Named agent deployments (Q3):
  - "MediaTek deployed chip stack into its production digital verification flow"
  - "the Renesas MCU team successfully deployed InnoStack"
  - "Samsung Foundry successfully used InnoStack"
  - Nokia "5x acceleration"; Socionext "up to a 5x overall productivity gain" (expected)
  - Named partners in Q1: Google, NVIDIA, MediaTek. [COMPANY CLAIM]
- Agent results:
  - ChipStack: "more than 40X faster RTL validation, reducing a typical five-week verification cycle to less than a day" (customer unnamed, Q2)
  - ViraStack: "2X to 10X productivity" (>25 engagements); AuraStack: "up to 15X higher productivity"
  - Maestro: "up to 30% higher quality and up to 5x greater token efficiency versus general purpose foundation model" (Q3)
  - [COMPANY CLAIM] A TIKR headline reports an agent "cut chip area 24% vs. general AI models" [SECONDARY headline only] — [TIKR](https://www.tikr.com/blog/cadence-says-its-new-ai-agent-cut-chip-area-24-vs-general-ai-models-heres-where-the-stock-could-go)
- Other company datapoints cited by SemiAnalysis: Cerebrus 1,000+ tape-outs (Q1 2025); "ALL top 20 semiconductor companies using Cadence digital software" (Q4 2022). [COMPANY CLAIM via SECONDARY]

#### Inferences
- [INFERENCE] Growing at twice the industry rate, and above Synopsys's EDA rate, is the best outside-checkable sign of 2026 share gains. Part of the gap comes from Hexagon and the hardware upcycle.
- [INFERENCE] Nvidia appears in 2026 hardware-verification launches of all three vendors, which suggests it multi-sources. No 2026 primary source names Nvidia as a Palladium customer.

#### Gaps
- Customer confirmation of attributed agent results; 2026 primary evidence on Nvidia and Palladium.

### c. Revenue model

#### Takeaway
About 78–80% of revenue is recurring, mainly two-to-three-year time-based licences. About 20–23% is up-front (hardware, much of IP, some software), and that share is rising. Services are about 9%. Agents are to be sold as "subscription plus consumption" on top of existing card/token and fixed-dollar drawdown contracts. No consumption revenue is disclosed.

#### Cited findings
- 10-K definitions [PRIMARY] — [10-K](https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf):
  - Recurring revenue was 80% in 2025 vs 83% in 2024 (recognised over time 76%, other recurring 4%); up-front 20% vs 17%. TTM recurring was 80% at Q4 2025 and 82% at Q1 2025.
  - Recurring covers over-time software licences, services, royalties, IP and hardware maintenance, and hardware operating leases. "Other recurring" includes short-term annually renewed software and "non-cancelable commitments, whereby the customer commits to a fixed dollar amount over a specified period of time that can be used to purchase from a list of products".
  - Time-based licences run "generally two to three years", and some carry remix rights. Hardware is "either sold or leased", and emulation is also offered through a Cadence-managed cloud.
  - Services were $475.2m (9%) in 2025.
- 2026 trend [PRIMARY] — [Q3 2026 CFO commentary](https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cfocommentary10262026ex9902.htm) ; [Q3 call](https://www.webull.com/news/15818016766808064):
  - FY2026 recurring is expected at ~80%. TTM recurring/up-front was 78/22 at Q3 2026 (Q3 2025: 80/20).
  - Quarterly up-front: Q3'25 18%, Q4'25 21%, Q1'26 23%, Q2'26 22%, Q3'26 21%. Quarterly recurring: 82/79/77/78/79%.
  - Recurring revenue grew 18% year on year in Q3 2026, against 11% growth in 2025.
- Product categories:
  - 2025 (2024): Core EDA 70% (71%), including "software, hardware, and services"; IP 14% (13%); SD&A 16% (16%).
  - Quarterly, Q3'25 to Q3'26: Core EDA 71/69/71/68/69%; IP 14/15/14/15/15%; SD&A 15/16/15/17/16%.
  - Product and maintenance revenue ($m): 1,208/1,332/1,349/1,431/1,487. Services ($m): 131/108/125/154/146. [PRIMARY]
- 2026 growth: Q1 Core EDA +18%, SD&A +18%, IP +22%; Q2 IP "over 40%", Core EDA +18%, SD&A +37%; Q3 Core EDA +20%, IP +24%, SD&A +30%. Hardware is not disclosed separately: Q1 was the "best quarter ever", Q2 and Q3 were "another record quarter", and "we continue to expect another record year for hardware". [PRIMARY / transcripts]
- Agent and usage pricing, verbatim:
  - **17 Feb 2026** (Q4 2025 call) — [Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/02/17/cadence-cdns-q4-2025-earnings-transcript/)
    - Devgan: "So we will price it as like a virtual engineer or agent. So that would be extra business." ... "this is a misnomer that we are like seat count limited. We are exploration limited." He said an agentic flow "could run 10 or 100 experiments in parallel".
    - Wall: "we don't see AI forcing a wholesale change from subscriptions to consumption. Our customers still want predictable access to trusted sign-off engines. and certified flows. So multiyear subscription remains at the core of our business." ... "So we'll attach more usage-based pricing for incremental capacity and AI-driven optimization. We have card models and token models that handle all those things."
  - **27 Apr 2026** (Q1 call) — [Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/04/27/cadence-cdns-q1-2026-earnings-transcript/)
    - Devgan: new agentic products "will be priced as a subscription plus consumption model, very similar to other kind of leading AI tools. So that's a completely new category for Cadence."
    - Wall: "Our subscription model remains the anchor arrangement with our customers. The add-on monetization then comes incrementally through agentic workflow products that are kind of usage-based or consumption-based for capacity and through our token and card models. What's different about agentic AI is that it doesn't replace the core EDA engines. It calls them more often and it calls them intelligently." ... "We're not assuming a sudden step function in AI monetization in the guide".
    - Devgan: "There is no pushback at all. If we can deliver productivity, the customer is more than willing to engage."
  - **26 Oct 2026** (Q3 call) — [Webull](https://www.webull.com/news/15818016766808064)
    - Wall: "Our model allows customers to use their own LLM infrastructure ... And can license the underlying design agents ... the point is that greater customer usage should create greater value for Cadence."
    - Wall: "agents could perform much more design exploration than an individual engineer calling our underlying engines repeatedly, and that creates a potential for significantly more consumption of our core [EDA] tools"; "the economics of particular deployment options can vary, of course".
  - [PRIMARY transcripts via secondary hosts]
- Channel: from 15 Apr 2026, ChipStack is on Google Cloud Marketplace, optimised with Gemini, with an "up to 10X productivity" claim. [PRIMARY per search summary; figure is COMPANY CLAIM] — [Business Wire](https://www.businesswire.com/news/home/20260415910313/en/Cadence-and-Google-Collaborate-to-Scale-AI-Driven-Chip-Design-with-ChipStack-AI-Super-Agent-on-Google-Cloud)
- Outside view: AI tools command "15-25% premiums", and renewals show about 20% uplift from AI tools. The CFO's three-tier agent monetisation is "an FY27–28 story". [SECONDARY] — [SemiAnalysis](https://newsletter.semianalysis.com/p/eda-market-primer)

#### Inferences
- [INFERENCE] Labour-hour exposure is small (services about 9%). Exposure to one-off hardware is material and rising. Most revenue is multi-year licences priced on licence counts (seats or tokens): sticky, but tied to job counts until consumption pricing scales.
- [INFERENCE] The fixed-dollar drawdown contracts (part of the 4% "other recurring") show usage-like pricing already exists. Agent pricing extends existing instruments.

#### Gaps
- Agent, consumption, hardware and VIP revenue; seat counts.

### d. Financial strength

#### Takeaway
Very strong: about 44–45% non-GAAP operating margin, about $1.76bn a year of FCF (about 29% of revenue), net debt of about $1.2bn, no customer at 10% or more, and US revenue at 44%. Weaker points: GAAP margins fell in 2026 (Hexagon), stock-based compensation is about 9% of revenue, and China rose to 16% of quarterly revenue.

#### Cited findings
- **FY2025** (released 17 Feb 2026):
  - Revenue $5.297bn (+14% vs $4.641bn). GAAP operating margin 28.2%, non-GAAP 44.6%. GAAP EPS $4.06, non-GAAP $7.14.
  - OCF $1.729bn; capex $142m; so FCF is about $1.587bn (derived).
  - Backlog $7.8bn; next-12-month RPO $3.8bn. Cash $3.001bn; long-term debt $2.480bn. [PRIMARY] — [release](https://investor.cadence.com/news/news-details/2026/Cadence-Reports-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results/default.aspx)
- **Q1 2026** (27 Apr): revenue $1.474bn (+19%); GAAP/non-GAAP operating margin 29.3%/44.7%; EPS $1.23/$1.96; backlog $8.0bn; OCF $356m. [PRIMARY transcript] — [Q1 call](https://www.fool.com/earnings/call-transcripts/2026/04/27/cadence-cdns-q1-2026-earnings-transcript/)
- **Q2 2026** (27 Jul): revenue $1.584bn (+24%); operating margin 28.4%/45.5%; EPS $1.33/$2.11; backlog $8.1bn; OCF $635m; buyback $200m. [PRIMARY] — [Q2 remarks](https://s206.q4cdn.com/597110084/files/doc_financials/2026/q2/CDNS-Q2-2026-Earnings-Conference-Call-Prepared-Remarks.pdf)
- **Q3 2026** (26 Oct):
  - Revenue $1.633bn vs $1.339bn (+22%). GAAP operating margin 26.2% (31.8% a year earlier); non-GAAP 44.1% (47.6%).
  - GAAP diluted EPS $1.05 (flat); non-GAAP $2.11 ($1.93).
  - Record backlog $8.2bn; next-12-month RPO $4.2bn.
  - Repurchases $400m (1.305m shares), plus a new $2.5bn authorisation. [PRIMARY] — [8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cdns10262026ex9901.htm)
- **FY2026 guidance path**:
  - Feb: $5.9–6.0bn excluding Hexagon; GAAP operating margin 31.75–32.75%; non-GAAP 44.75–45.75%; non-GAAP EPS $8.05–8.15.
  - Apr: $6.125–6.225bn, including about $160m of Hexagon revenue and about $0.28 of EPS dilution; non-GAAP EPS $7.85–7.95.
  - Jul: $6.260–6.340bn (19% growth); non-GAAP operating margin 43.75–44.75%; non-GAAP EPS $8.05–8.15; OCF ~$2bn; about 50% of FCF to buybacks.
  - **Oct (current)**: $6.387–6.417bn (~21%); GAAP operating margin 28.2–29.2%; non-GAAP 44.2–45.2%; GAAP EPS $4.84–4.90; non-GAAP EPS $8.37–8.43; OCF ~$2.0bn; capex ~$240m.
  - Q4 2026 guide: $1.695–1.725bn (+18–20%); GAAP/non-GAAP operating margin 30–31%/44–45%; EPS $1.23–1.29/$2.19–2.25. [PRIMARY] — [CFO commentary](https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cfocommentary10262026ex9902.htm)
- **Cash and capital** (same source):
  - Quarterly FCF: Q4'25 $512m, Q1'26 $307m, Q2'26 $582m, Q3'26 $362m (TTM about $1.76bn, my sum).
  - About 64% of FY2026 revenue comes from beginning backlog (down from about 65%). Rule of 40 FY2026E is "~66%". SBC 2026E is $569m (~9% of revenue).
  - Tax rate ~27% GAAP, 16.5% non-GAAP. Non-GAAP other income/expense $(101)–(91)m. FY2026 buybacks ">50% of free cash flow" (~$400m planned in Q4). Diluted shares 274–276m.
  - DSO by quarter (Q3'25–Q3'26): 55/64/67/65/66 days.
- **Debt**:
  - Principal by quarter: $2.500/2.500/2.925/2.500/2.650bn. Cash: $2.753/3.001/1.407/1.440/1.452bn. About 15% of cash was in the US at Q3'26.
  - Senior notes: $500m 4.200% due 10 Sep 2027; $1.0bn 4.300% due 10 Sep 2029; $1.0bn 4.700% due 2034.
  - Revolver: $1.25bn (expandable to $1.75bn), expiring 14 Aug 2029. [PRIMARY] — [10-K](https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf)
- **Hexagon D&E**:
  - Agreement 4 Sep 2025 (HSR and FDI approvals required); completed 23/24 Feb 2026.
  - About €2.70bn including about €150m of taxes, paid 70% in cash (€1.89bn) and 30% in shares. MSC Nastran and Adams.
  - About $160m of 2026 revenue, about $0.28 dilution, accretive in 2027. Integration "progressing well, with key deals closed with top customers" (Q2).
  - Wall (Q3): "not really contributing much in the way of operating profit at all this year"; normal incremental margin "54%, 55%". [PRIMARY via reprints / transcript] — [evertiq](https://evertiq.com/news/2026-02-24-cadence-completes-acquisition-of-hexagons-de-business) ; [HPCwire](https://www.hpcwire.com/off-the-wire/cadence-completes-acquisition-of-hexagons-design-and-engineering-business/)
- **Returns and costs**:
  - ROIC 17.09% (GAAP, aggregator) against Synopsys at 2.23%. [SECONDARY] — [StockAnalysis](https://stockanalysis.com/stocks/cdns/statistics/) ; [SNPS](https://stockanalysis.com/stocks/snps/statistics/)
  - R&D $1,768.8m (33%) in 2025. About 13,800 employees at end-2025; headcount 15,753 at Q3 2026, after Hexagon. Devgan cited about 15,000 staff, about 10,000 in R&D. [PRIMARY]
- **Concentration and geography**:
  - No customer reached 10% of revenue in 2025, 2024 or 2023.
  - 2025: US $2,311.0m (44%), Other Americas $168.3m (3%), China $680.0m (13%), Other Asia $1,005.2m (19%), EMEA $790.6m (15%), Japan $341.7m (6%). [PRIMARY] — [10-K](https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf)
  - Quarterly, Q3'25–Q3'26: China 18/12/13/15/16%; Americas 43/47/45/43/43%; Other Asia 18/20/20/20/19%; EMEA 14/14/16/15/15%; Japan 7/7/6/7/7%. [PRIMARY]
  - Wall (Q1): "we still expect China to be about 13% for the year". Devgan (Q3): "there were some specific things with China revenue moving around". System companies are "45% of our business".

#### Inferences
- [INFERENCE] Cash fell $1.6bn in Q1 2026 while debt rose $425m temporarily. This fits Hexagon's cash being funded mainly from cash plus a short revolver draw; the filings I read do not say so.
- [INFERENCE] Net debt is about $1.2bn, about 0.5x TTM GAAP EBITDA (~$2.2bn, implied by the aggregator's EV/EBITDA). Organic 2026 growth, excluding Hexagon's ~$160m, is about 18% at the guidance midpoint, and that figure still includes the 2025 acquisitions.

#### Gaps
- What the $2.65bn of debt at Q3 2026 consists of; company-reported ROIC.

### e. Resilience

#### Takeaway
Cadence is resilient in a steady AI build-out. The vulnerabilities are a record hardware base and an up-front share that has risen from 17% to about 22%. They also include 45% of revenue from system companies (first to cut in a financing-led pause) and 13–16% from China. Revenue fell 22% in 2001–03 and 47% in 2007–09, but grew through 2022–23.

#### Cited findings
- Revenue history [SECONDARY aggregator] — [companiesmarketcap](https://companiesmarketcap.com/cadence-design-systems/revenue/):
  - 2000 $1.27bn; 2001 $1.43bn; 2002 $1.29bn (−9.6%); 2003 $1.12bn (−12.85%); 2004 $1.19bn.
  - 2007 $1.61bn; 2008 $1.03bn (−35.7%); 2009 $0.85bn (−17.9%); 2010 $0.93bn; 2011 $1.14bn.
  - 2019 $2.33bn; 2020 $2.68bn; 2021 $2.98bn; 2022 $3.56bn (+19.2%); 2023 $4.08bn (+14.8%); 2024 $4.64bn; 2025 $5.29bn; TTM to Q3 2026 $6.13bn.
- Hardware cycle:
  - 2026 is expected to be "another record year". Management says "hardware could be lumpy from quarter to quarter" and there are "no capacity or supply chain constraints".
  - Inventory was $448.8m vs $303.5m at end-2025 (via market_structure notes). The 10-K notes reliance on "a single supplier or a limited number of suppliers for certain hardware components". [PRIMARY / transcript] — [Q3 call](https://www.webull.com/news/15818016766808064)
- AI exposure:
  - System companies are 45% of the business. Devgan: "Google and Meta and Microsoft and Amazon and Tesla, everybody is doing more and more designs".
  - TrendForce puts ASIC-based AI servers at 27.8% of 2026 AI-server shipments, and expects nine cloud providers' capex to rise about 90% to more than $886.7bn in 2026 and about $1.3tn in 2027 (via market_structure notes). [SECONDARY] — [TrendForce, 3 Aug 2026](https://www.trendforce.com/presscenter/news/20260803-13161.html) ; [TrendForce, 20 Jan 2026](https://www.trendforce.com/presscenter/news/20260120-12887.html)
- Design-start mix: the IBS chart in Cadence's DVCon 2026 paper shows 10,644 design starts in 2026, about three-quarters at 28nm or above by 2030. [Third-party estimate via COMPANY slides] — [DVCon](https://dvcon-proceedings.org/wp-content/uploads/Broadening-the-Adoption-of-Hardware-Assisted-Verification-with-Next-Generation-Emulation-Appliance.pdf)
- Export controls [PRIMARY] — [10-K](https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf):
  - 27 Jul 2025 settlement with BIS and DOJ over violations between 2015 and 2021, "primarily involving sales ... valued at $45.3 million ... to a customer in China", plus onward technology transfer.
  - Cadence pleaded guilty to one count of conspiracy to commit export-control violations: three-year probation, with compliance, reporting and cooperation duties. Under the BIS settlement (two annual audits), compliance "is a condition to our continued ability to export products".
  - $140.6m paid in Q3 2025, which matches the brief's "roughly $140 million".
  - A BIS licence requirement for EDA exports to China (23 May 2025) was rescinded on 2 Jul 2025.
  - The Affiliates (50%) Rule took effect 29 Sep 2025 and was suspended 11 Nov 2025, "currently set to expire on November 9, 2026".
- Update: on 5 Nov 2026 BIS extended the suspension to 10 Jan 2027, tied to the US–China (Busan) framework, itself extended in September 2026 to 10 Jan 2027. The rule is suspended, not repealed. [SECONDARY law-firm briefings; Federal Register not checked] — [Clifford Chance](https://www.cliffordchance.com/briefings/2026/11/bis-suspends-affiliates-rule-until-january-10-2027.html) ; [Thompson Hine](https://www.thompsonhinesmartrade.com/2026/11/bis-extends-affiliates-rule-until-january-2027/) ; [Global Sanctions](https://globalsanctions.com/2026/11/us-bis-extends-suspension-50-rule-coming-into-force-until-10-january-2027/)
- Guidance assumes export rules "remain substantially similar" [PRIMARY].
- Chinese rival Empyrean had 2025 revenue of RMB 1,324.98m (+8.40%), 90% domestic (via china.md). [PRIMARY] — [Empyrean annual report](https://static.cninfo.com.cn/finalpage/2026-04-28/1225217315.PDF)

#### Inferences (provisional, mine)
- [INFERENCE] **Steady growth (~55%)**: this fits the 2026 evidence (record backlog, three guidance raises, record hardware) and 2027 consensus of +14%.
- [INFERENCE] **Financing-led pause around 2028 (~25%)**: the exposure is up-front hardware and IP (21–23% of revenue) plus system-company programmes.
  - Illustration only: a one-third fall in up-front revenue would cut total revenue by about 7%. The 78–80% recurring base and $8.2bn backlog cushion the rest.
  - The 2008–09 fall (−47%) should not be used directly. I could not verify how much of it came from a licensing-model change.
- [INFERENCE] **Faster acceleration (~20%)**: upside from hardware capacity and consumption pricing. The same speed shortens the time before AI plus open tools is good enough at mature nodes.
- [INFERENCE] **Cycle position**: late in a hardware upcycle (records at Cadence and Synopsys), with IP strong and the up-front mix high, so 2027 comparisons are harder.

#### Gaps
- Filing-level data for 2001–03 and 2008–09; hardware revenue history; how much of 2026 China revenue is catch-up.

---

## B. Path forward (industry transitions)

### Transition by transition: said versus done
- **(1) Verification labour to tools.**
  - Said: agents priced "like a virtual engineer"; an "industry's first fully autonomous virtual AI Design Engineer" (Computex 2026, with NVIDIA).
  - Done:
    - ChipStack acquisition agreed about 10 Nov 2025. It is a Seattle start-up from the AI2 Incubator, founded 2023, which raised more than $7m; terms undisclosed; Cadence claimed "70%" verification acceleration [COMPANY CLAIM]. — [GeekWire](https://www.geekwire.com/2025/cadence-to-acquire-seattle-startup-chipstack-to-boost-chip-design-automation/) ; [design-reuse](https://www.design-reuse.com/news/202529654-cadence-welcomes-chipstack/)
    - Super Agent in early access from February 2026 ("4X to 10X", unnamed customers) [COMPANY CLAIM]. A Level-5 version on NVIDIA OpenShell, plus AgentStack, was announced around 31 May/1 Jun 2026 for early-access customers in H2 2026. The releases carry an Nvidia quote and no customer quotes. — [Business Wire](https://www.businesswire.com/news/home/20260531072918/en/Cadence-Announces-ChipStack-AI-Super-Agent) ; [design-reuse](https://www.design-reuse.com/news/202530621-cadence-unveils-industry-s-first-fully-autonomous-virtual-engineer-for-chip-design-powered-by-nvidia/)
    - More than 20 ChipStack engagements and "deployed in production across multiple chip designs" (Q2); more than 100 Super Agent engagements and MediaTek production use (Q3) [COMPANY CLAIM; see b].
    - The 10-K says the technology is "deployed at leading chip companies and hyperscalers ... reducing verification cycles from weeks to days" [COMPANY CLAIM].
  - Services are only about 9% of revenue.
- **(2) Seat licences to pricing by use.** Said: see c. Done: Google Cloud Marketplace listing (15 Apr 2026); card/token models and fixed-dollar drawdown contracts. Not done: no consumption revenue disclosed; "not assuming a sudden step function".
- **(3) Simulation toward formal proof.** Said: little specific. Done: owns Jasper and Conformal, and ChipStack integrates with Jasper and Xcelium. Tension: the biggest verification growth engine is emulation, which is simulation-based, so a shift of cycles to formal moves value within Cadence's own portfolio. No formal-specific roadmap was found.
- **(4) Proprietary engines against open-source tools driven by AI.**
  - Said: Devgan (Q1, asked whether AI could rewrite Virtuoso or Innovus): "I'm not worried that some other party will be able to write any better base tools". Devgan (Q2): "to really do real designs, people use Cadence" [PRIMARY/SECONDARY transcripts].
  - Done: 2026 certifications at A14, A16, N2P, 18A-P, 14A and Samsung second-generation 2nm. Open tools lack advanced-node PDKs (Tech Fund, via synopsys.md) — [Tech Investments, 27 Jul 2026](https://www.techinvestments.io/p/the-eda-crash-and-the-massive-ai).
  - Exposed flank: mature nodes, about three-quarters of design starts by 2030. Bernstein, paraphrased, says open tooling could pressure lower-end pricing "sooner than incumbents expect" — [stockti](https://stockti.com/synopsys-shares-plunge-8-as-moonshot-ai-s-chip-demo-raises-eda-moat-concerns).
- **(5) Foundry certification as a barrier to entry.** This is the strongest evidence in the file: certifications at all three leading foundries with executive quotes, and TSMC grids listing only the three incumbents. Rapidus is unconfirmed. Cadence benefits from the barrier.
- **(6) A paying market for verified software.** Largely not applicable. VLAB Works (virtual prototyping), Secure-IC (security IP and evaluation tools) and BETA CAE/Hexagon (mechanical simulation) are not machine-checked software proof, and Cadence states no buyer or product. Model makers are the visible actors: Anthropic's 22 Oct 2026 research produced proofs for open-source software without offering a product (via model_makers_hyperscalers.md). — [Anthropic](https://www.anthropic.com/research/formal-verification)
- **(7) AI model makers offering verification themselves.**
  - Said: Devgan (Q3): "we have worked with OpenAI from the very beginning of when they got started ... same thing with Anthropic and Gemini, the 3 leading frontier models"; he also noted "very, very good open-weight ... models". The design is model-agnostic: customers "use their own LLM infrastructure".
  - Done: Google Gemini collaboration (15 Apr 2026); NVIDIA OpenShell and Computex. ChipStack reportedly uses NVIDIA Nemotron (BNP, secondary).
  - Contrast: Synopsys has GPT-Synopsys with OpenAI ("preferred partners", OpenAI licenses Synopsys tools, revenue sharing; 30 Sep 2026), and Nvidia bought $2bn of Synopsys stock ("not exclusive"; 1 Dec 2025) [PRIMARY, via synopsys.md] — [GPT-Synopsys](https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence-to-Revolutionize-Chip-Design) ; [Nvidia–Synopsys](https://news.synopsys.com/2025-12-01-NVIDIA-and-Synopsys-Announce-Strategic-Partnership-to-Revolutionize-Engineering-and-Design).
  - No comparable Cadence agreement with a frontier lab was found.
- **Funding and commitment:** R&D $1.77bn (33%); FCF about $1.76bn a year; more than 50% of FCF to buybacks.
  - Acquisitions since 2024: BETA CAE (Q2 2024), VLAB Works, Arm Artisan foundation IP and Secure-IC (all 2025), ChipStack and Hexagon D&E (about €2.7bn).
  - The Intel 14A multi-year engagement is "expected to be a meaningful driver of growth over the next few years" [COMPANY CLAIM]. First Tensilica DSP design win at STMicroelectronics (Q2 2026).

### The July 2026 episode (Kimi K3, 17 July 2026)
- **Moonshot's claim** (blog; results "current as of July 16, 2026"): K3 "designed a chip to serve a nano model built on its own architecture" in a single 48-hour autonomous run, using open-source EDA tools on the Nangate 45nm library. The design fits within 4 mm², closes timing at 100 MHz and has 1.46m standard cells. Throughput was measured in simulation; no tape-out or sign-off is mentioned. [PRIMARY; Moonshot claim] — [Kimi blog](https://www.kimi.com/blog/kimi-k3)
- **Share move:**
  - 17 Jul: CDNS closed $330.11, −9.47% from $364.65, on 5.19m shares versus about 1.3–1.6m on prior days. The intraday price was $329.50 (−9.64%) at 13:07 EDT. SNPS closed $384.28 (−7.85%), $382.98 intraday (−8.17%).
  - Following days: 20 Jul $329.93; 21 Jul $344.64 (+4.46%); 22 Jul $337.01; 23 Jul $330.46; 24 Jul $326.24 (−10.5% versus 16 Jul).
  - After Q2 results (27 Jul): 28 Jul $344.72 (+1.80%); 29 Jul $332.76 (−3.47%); 31 Jul $340.02.
  - It was the lowest CDNS close since 30 April (MoneyDJ). The later low of 15 Sep 2026 ($273.96, −34.2% from the June high) followed a 1 Sep software sell-off that TIKR attributes to rising bond yields.
  - [SECONDARY market data] — [Yahoo Finance chart API](https://query1.finance.yahoo.com/v8/finance/chart/CDNS?interval=1d) ; [ts2.tech](https://ts2.tech/en/synopsys-nasdaqsnps-stock-sinks-as-kimi-chip-demo-tests-the-eda-moat/) ; [TIKR](https://www.tikr.com/blog/cadence-stock-fell-9-in-a-day-on-a-chinese-ai-chip-demo-heres-where-the-stock-could-go-in-2026)
  - **The brief's "falls of about 9%" is right for Cadence and slightly high for Synopsys (about 8%).**
- **Analysts:**
  - BNP Paribas (Andrew DeGasperi) called the reaction "excessive and unreasonable" (translated), "buy the dip". He likened it to cybersecurity stocks after the "Mythos preview", said 45nm is not comparable with nodes below 5nm, and cited ChipStack cutting a five-week RTL cycle to 24 hours. — [MoneyDJ/TechNews, 20 Jul](https://finance.technews.tw/2026/07/20/kimi-driven-selloff-makes-cadence-synopsys-buying-opportunities/) ; [Seeking Alpha, 17 Jul](https://seekingalpha.com/news/4615018-cadence-synopsys-sink-as-moonshot-brings-eda-disruption-risks-bnp-says-buy-the-dip)
  - Mizuho said K3 still depended on existing EDA tools (search summary).
  - Bernstein (Robin Zhu) said K3 shows Chinese labs can "keep pace with the US frontier", and reportedly called the reaction "generally sensible". [SECONDARY] — [stockti, 17 Jul](https://stockti.com/synopsys-shares-plunge-8-as-moonshot-ai-s-chip-demo-raises-eda-moat-concerns)
- **Management:**
  - The Q2 prepared remarks did not name Kimi. They stressed "deterministic, physics-based engines" and raised guidance to 19% growth.
  - Q&A, as quoted by a blog: Devgan said "they said a chip, but I think it's a small block, which is about technology which is like 20 years old"; "So even to design a small block at such an old node, they needed EDA tools to do that"; "to really do real designs, people use Cadence to do that." He reportedly added that it ran 20–30 times slower than current frequencies (paraphrase, unverified).
  - Baird's Joe Vruwink asked about open-source AI agents.
  - [SECONDARY transcript excerpts] — [Expanse Stocks](https://expansestocks.substack.com/p/cadence-q2-2026) ; [Barchart](https://www.barchart.com/story/news/3606848/5-revealing-analyst-questions-from-cadence-design-systemss-q2-earnings-call) ; Q3 summary — [roic.ai](https://www.roic.ai/quote/CDNS/transcripts/2026-year/3-quarter)

### Provisional verdict (my judgment)
**Coherent (provisional), with lower confidence on transitions (4) and (7).**
- Words match actions:
  - The acquisition (Nov 2025) became a product (Feb 2026), which reached named production use (Q3 2026; company claim).
  - Certification was renewed at every leading-edge node in 2026.
  - Pricing (subscription plus consumption on certified engines) matches the thesis that agents call engines more often.
  - The plan is funded internally.
  - The timing is plausible: Level-5 in early access in H2 2026, and monetisation seen as 2027–28.
- What must go right:
  - Agents add engine consumption rather than cannibalising licences; check in the February 2027 guide.
  - Certification remains the gate for AI-generated advanced-node designs.
  - Hardware does not reverse sharply.
  - China access holds after 10 Jan 2027.
  - Cadence keeps frontier-model access without ceding the agent layer to a lab-backed rival stack such as GPT-Synopsys.
  - Hexagon becomes accretive in 2027.

---

## C. Entry point (share price and valuation; separate from the quality tests)

### Takeaway
At $329.26 (close 11 Nov 2026), Cadence trades at about 39x 2026 and 33x 2027 consensus non-GAAP EPS, about 14.9x trailing EV/sales, and a ~2% FCF yield. That is below its five-year P/S and GAAP P/E medians, above its ten-year medians, and a clear premium to Synopsys on forward earnings and sales. The price is about 21% below the June 2026 high and 20–24% above the 2026 lows.

### Cited findings
- **Snapshot** (close 11 Nov 2026): price $329.26; market cap $90.34bn; EV $91.61bn; trailing P/E 65.47 (GAAP); forward P/E 34.94; EV/sales 14.94; EV/EBITDA 41.26 (GAAP); EV/FCF 51.94; FCF yield 1.95%; ROIC 17.09%. [SECONDARY] — [StockAnalysis](https://stockanalysis.com/stocks/cdns/statistics/)
- **Prices:**
  - Recent closes: 2 Nov $329.51; 3 Nov $323.75; 4 Nov $329.52; 5 Nov $311.43 (−5.49%); 6 Nov $319.92; 9 Nov $336.53 (+5.19%); 10 Nov $331.64; 11 Nov $329.26.
  - 12-month closing high $416.39 (2 Jun 2026; intraday $416.69). Closing low $265.66 (10 Apr 2026). 15 Sep close $273.96. The latest close is +5.3% versus 31 Dec 2025 ($312.58).
  - Other ±5% days: 3 Feb −7.15%; 17/18 Feb −5.34%/+7.60% (FY2025 results); 10/13 Apr −5.46%/+8.48%; 1 Jun +10.46% (Computex window); 5 Jun −8.62% (SNPS −5.99%; cause not checked); 1 Sep −7.60%; 1 Oct +6.22%; 27 Oct +6.49% (Q3 results). [SECONDARY] — [StockAnalysis history](https://stockanalysis.com/stocks/cdns/history/) ; [Yahoo Finance chart API](https://query1.finance.yahoo.com/v8/finance/chart/CDNS?interval=1d)
- **My calculations** [INFERENCE]:
  - Price / FY2026 consensus EPS ($8.42) = 39.1x; / FY2027 ($9.85) = 33.4x; / FY2026 GAAP EPS guidance midpoint ($4.87) = 67.6x.
  - EV / 2026E revenue = 14.3x; / 2027E = 12.5x. EV / 2026E non-GAAP operating income (~$2.86bn) ≈ 32x.
  - FCF yield after SBC is about 1.3%.
- **History** (year-end; medians computed by me) [SECONDARY] — [P/E](https://companiesmarketcap.com/cadence-design-systems/pe-ratio/) ; [P/S](https://companiesmarketcap.com/cadence-design-systems/ps-ratio/):
  - GAAP P/E: 2016 35.5; 2017 55.8; 2018 34.5; 2019 19.2 (likely a one-off GAAP gain; not checked); 2020 63.5; 2021 73.1; 2022 51.3; 2023 70.6; 2024 77.2; 2025 76.4; now 65.1. The five-year median is 73.1 (range 51.3–77.2); the ten-year median is 59.7.
  - P/S: 2016 3.98; 2017 6.08; 2018 5.69; 2019 8.31; 2020 14.2; 2021 17.3; 2022 12.4; 2023 18.1; 2024 18.0; 2025 16.0; now 14.7 (the page body also shows 13.1, undated). The five-year median is 17.3 (range 12.4–18.1); the ten-year median is 13.3.
- **Peer** (Synopsys, close 11 Nov 2026, via synopsys.md):
  - $462.12; market cap $88.56bn; EV $95.79bn; trailing P/E 81.94; forward P/E 26.26; EV/sales 10.17; EV/EBITDA 46.15 (GAAP, depressed by Ansys amortisation and restructuring); EV/FCF 34.86; net debt $7.23bn [SECONDARY] — [StockAnalysis SNPS](https://stockanalysis.com/stocks/snps/statistics/).
  - FY2027 guidance non-GAAP EPS $19.04–19.12 (~24x, my calculation). Long-term model to FY2030: ~15% revenue CAGR and ~50% non-GAAP operating margin [PRIMARY] — [Investor Day, 30 Sep 2026](https://news.synopsys.com/2026-09-30-Synopsys-Details-Growth-Strategy-and-Long-term-Financial-Model-at-2026-Investor-Day).
  - Siemens EDA is not separately listed.
- **Consensus** (updated 9 Nov 2026; S&P Global data):
  - Revenue FY2026 $6.41bn (+21.0%); FY2027 $7.33bn (+14.4%). Non-GAAP EPS FY2026 $8.42 (+18.0%); FY2027 $9.85 (+16.9%). FY2028 is behind a paywall.
  - 24 analysts rate it "Strong Buy". Price targets: mean $411.76, median $420, range $300–470. [SECONDARY] — [StockAnalysis forecast](https://stockanalysis.com/stocks/cdns/forecast/)
- **Management run-rate**: Wall (Q3), excluding Hexagon: "kind of mid teens for revenue growth, high teens for EPS growth". Next-year guidance comes "in February". No Cadence long-term targets were found. [PRIMARY transcript]
- **Licence and services share**: recurring 78–80% (mainly 2–3-year time-based licences); services about 9%; up-front 21–23%. [PRIMARY]
- **Near-term events:**
  - 8 Dec 2026: Synopsys Q4 FY2026 results (read-across) — [Finviz](https://finviz.com/news/417651/synopsys-announces-earnings-release-date-for-fourth-quarter-and-fiscal-year-2026)
  - 10 Jan 2027: the Affiliates Rule suspension and the US–China framework expire.
  - About mid-February 2027: Cadence Q4 results and 2027 guidance. The FY2025 results came on 17 Feb 2026; the exact date was not found.
  - 10 Sep 2027: $500m of notes mature.
  - Three-year DOJ probation runs from the 2025 plea.
  - No pending acquisition.

### Inferences
- [INFERENCE] At a 1.95% FCF yield and an 8–9% required return, a simple perpetuity implies about 6–7% FCF growth for ever (before SBC). In practice that means mid-teens growth for several years, then a slow fade. This is an illustration, not a valuation.
- [INFERENCE] 2026 includes a record hardware year, strong IP and about 3 percentage points of Hexagon growth, so 2027 consensus (+14%) assumes these hold or are replaced.
- [INFERENCE] Entry would look more attractive with any of the following:
  - A price near the 2026 lows ($266–274), about 27–28x 2027 EPS.
  - P/S at or below the ten-year median (13.3x) or the 2022 trough (12.4x).
  - A February 2027 guide showing agent or consumption revenue as additive, with hardware normalising without a guidance cut.
  - Clarity after 10 Jan 2027.
  - Another AI-scare sell-off without fundamental damage; in July, guidance was raised ten days after the sell-off.
  - (Analysis only; not a recommendation.)

### Gaps
- Five- and ten-year forward P/E and EV/EBITDA history; FY2028 consensus; the confirmed Q4 results date.

---

## Closing lists

### 1. What I could not verify
- Third-party share for Jasper, Conformal, Tempus, Voltus, Quantus, Pegasus and Cadence VIP (the SemiAnalysis competitive section is paywalled).
- Per-tool TSMC grid status; any Rapidus certification; the Samsung SF2P blog of 31 Jul 2026 (search summary only).
- Customer confirmation of agent results attributed to MediaTek, Renesas, Samsung Foundry, Nokia, Socionext and Rapidus. All of Cadence's agent figures (4–10X, 40X, 2.5X, 15X, 30%/5x) are company claims.
- 2026 primary evidence of Nvidia using Palladium.
- An official-transcript check of the Kimi Q&A wording; Mizuho's note; the cause of the −8.6% move on 5 Jun 2026.
- The licensing-model share of the 2008–09 revenue fall; filing-level data for 2001–03.
- Hexagon cash financing (inferred: cash plus a short revolver draw) and what the Q3 2026 debt consists of.
- Hardware, consumption and agent revenue; forward P/E and EV/EBITDA history; FY2028 consensus; the Q4 2026 results date.
- Any preferred-partner or revenue-share deal between Cadence and OpenAI or Anthropic (Devgan says only that it has "worked with" them).

### 2. Where current evidence contradicts or fails to support the background views
- **"Seat-priced tools face pressure once AI agents can drive open-source alternatives": not visible yet.**
  - Core EDA grew 18–20% in 2026, recurring revenue +18%, and backlog reached a record $8.2bn.
  - A secondary source reports about 20% renewal uplift from AI tools.
  - The July sell-off was a market fear, not a change in the business. The prior may still hold at mature nodes or after 2028.
- **"Value moves to the judge": broadly supported, with a qualification for Cadence.**
  - The dominant final sign-off judges (PrimeTime; Calibre, with "Calibre-clean" the TSMC requirement) belong to Synopsys and Siemens.
  - Cadence's clearest leads are emulation and analog/custom; its sign-off engines are certified but in minority positions.
- **"Big three keep growing through 2029 (70%)": consistent.** Cadence grows about 21% in 2026 against the industry's 12%, with 2027 consensus at +14%.
- **"Verification labour loses pricing power": not tested here.** Cadence's services are only about 9% of revenue, and its agents target labour budgets.
- **"Machine-proved regression checks standard for AI-edited chip designs by 2028 (60%)": no supporting evidence found.** There is no formal or equivalence adoption disclosure, and Cadence's fastest-growing verification business is simulation-based emulation.
- **"Final sign-off stays with people": not contradicted.** Cadence markets "Level-5 autonomy", but certification is still of engines and flows, and Kimi K3 did no sign-off.
- **Brief's "falls of about 9%" in July: correct for Cadence** (−9.47% close). Synopsys fell about 8% (−7.85% close).

### 3. Sources with dates
- **Cadence primary:**
  - FY2025 10-K (filed Feb 2026) https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf
  - Q4/FY2025 release (17 Feb 2026) https://investor.cadence.com/news/news-details/2026/Cadence-Reports-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results/default.aspx
  - Q2 2026 prepared remarks (27 Jul 2026) https://s206.q4cdn.com/597110084/files/doc_financials/2026/q2/CDNS-Q2-2026-Earnings-Conference-Call-Prepared-Remarks.pdf
  - Q3 2026 release (26 Oct 2026) https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cdns10262026ex9901.htm
  - Q3 2026 CFO commentary (26 Oct 2026) https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cfocommentary10262026ex9902.htm
- **Transcripts:**
  - Q4 2025 (17 Feb 2026) https://www.fool.com/earnings/call-transcripts/2026/02/17/cadence-cdns-q4-2025-earnings-transcript/
  - Q1 2026 (27 Apr 2026) https://www.fool.com/earnings/call-transcripts/2026/04/27/cadence-cdns-q1-2026-earnings-transcript/
  - Q3 2026 (26 Oct 2026) https://www.webull.com/news/15818016766808064
  - Q3 summary https://www.roic.ai/quote/CDNS/transcripts/2026-year/3-quarter
  - Q2 excerpts (Jul 2026) https://expansestocks.substack.com/p/cadence-q2-2026 ; https://www.barchart.com/story/news/3606848/5-revealing-analyst-questions-from-cadence-design-systemss-q2-earnings-call
- **Foundry:**
  - TSMC/Cadence (23 Sep 2026) https://finviz.com/news/394879/cadence-collaborates-with-tsmc-to-deliver-certified-tool-solutions-and-industry-leading-silicon-proven-ualink-ip-on-tsmc-advanced-processes
  - TSMC grids (as of 1 Oct 2026) https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance
  - Futurum (Sep 2026) https://futurumgroup.com/insights/tsmcs-oip-forum-turns-agentic-chip-design-demos-into-production-flows/
  - Intel (27/28 Jul 2026) https://www.hpcwire.com/off-the-wire/cadence-certifies-ai-driven-reference-flows-for-intel-18a-p-and-intel-14a/ ; https://www.electronicsworld.co.uk/ai-driven-digital-and-custom-reference-flows-tools-and-solutions-by-cadence-are-now-certified-on-intel-18a-p-pdk-1-0-and-intel-14a-pdk-0-5-technologies/42129/
  - Intel 18A (2025) https://community.cadence.com/cadence_blogs_8/b/corporate-news/posts/cadence-digital-and-custom-analog-flows-certified-for-latest-intel-18a-process-technology
  - Samsung (28 May/1 Jun 2026) https://www.design-reuse.com/news/202530589-cadence-and-samsung-foundry-deepen-2nm-and-3d-ic-collaboration-to-meet-surging-ai-infrastructure-and-physical-ai-demand/ ; https://www.businesswire.com/news/home/20260528147066/en/
  - Rapidus (Dec 2024) https://www.businesswire.com/news/home/20241210546692/en/Cadence-and-Rapidus-Collaborate-on-Leading-Edge-2nm-Semiconductor-Solutions-for-AI-and-HPC-Applications ; https://www.eenewseurope.com/en/rapidus-signs-2nm-deals-with-synopsys-cadence/
- **Products and acquisitions:**
  - ChipStack (Nov 2025) https://www.geekwire.com/2025/cadence-to-acquire-seattle-startup-chipstack-to-boost-chip-design-automation/ ; https://www.design-reuse.com/news/202529654-cadence-welcomes-chipstack/
  - Super Agent / Computex (~31 May 2026) https://www.businesswire.com/news/home/20260531072918/en/Cadence-Announces-ChipStack-AI-Super-Agent ; https://www.design-reuse.com/news/202530621-cadence-unveils-industry-s-first-fully-autonomous-virtual-engineer-for-chip-design-powered-by-nvidia/
  - Google (15 Apr 2026) https://www.businesswire.com/news/home/20260415910313/en/Cadence-and-Google-Collaborate-to-Scale-AI-Driven-Chip-Design-with-ChipStack-AI-Super-Agent-on-Google-Cloud
  - Hexagon (23–24 Feb 2026) https://evertiq.com/news/2026-02-24-cadence-completes-acquisition-of-hexagons-de-business ; https://www.hpcwire.com/off-the-wire/cadence-completes-acquisition-of-hexagons-design-and-engineering-business/
  - DVCon (Mar 2026) https://dvcon-proceedings.org/wp-content/uploads/Broadening-the-Adoption-of-Hardware-Assisted-Verification-with-Next-Generation-Emulation-Appliance.pdf
- **Kimi K3:**
  - Moonshot (results as of 16 Jul 2026) https://www.kimi.com/blog/kimi-k3
  - ts2.tech (17 Jul 2026) https://ts2.tech/en/synopsys-nasdaqsnps-stock-sinks-as-kimi-chip-demo-tests-the-eda-moat/
  - TIKR (Jul–Sep 2026) https://www.tikr.com/blog/cadence-stock-fell-9-in-a-day-on-a-chinese-ai-chip-demo-heres-where-the-stock-could-go-in-2026
  - stockti (17 Jul 2026) https://stockti.com/synopsys-shares-plunge-8-as-moonshot-ai-s-chip-demo-raises-eda-moat-concerns
  - Seeking Alpha (17 Jul 2026) https://seekingalpha.com/news/4615018-cadence-synopsys-sink-as-moonshot-brings-eda-disruption-risks-bnp-says-buy-the-dip
  - MoneyDJ/TechNews (20 Jul 2026) https://finance.technews.tw/2026/07/20/kimi-driven-selloff-makes-cadence-synopsys-buying-opportunities/
  - Tech Investments (27 Jul 2026) https://www.techinvestments.io/p/the-eda-crash-and-the-massive-ai
  - TIKR headline (date not checked) https://www.tikr.com/blog/cadence-says-its-new-ai-agent-cut-chip-area-24-vs-general-ai-models-heres-where-the-stock-could-go
- **Export controls** (Nov 2026): https://www.cliffordchance.com/briefings/2026/11/bis-suspends-affiliates-rule-until-january-10-2027.html ; https://www.thompsonhinesmartrade.com/2026/11/bis-extends-affiliates-rule-until-january-2027/ ; https://globalsanctions.com/2026/11/us-bis-extends-suspension-50-rule-coming-into-force-until-10-january-2027/
- **Market data** (retrieved 12 Nov 2026):
  - https://stockanalysis.com/stocks/cdns/statistics/ (close 11 Nov 2026)
  - https://stockanalysis.com/stocks/cdns/forecast/ (updated 9 Nov 2026)
  - https://stockanalysis.com/stocks/cdns/history/
  - https://query1.finance.yahoo.com/v8/finance/chart/CDNS?interval=1d
  - https://companiesmarketcap.com/cadence-design-systems/revenue/ ; https://companiesmarketcap.com/cadence-design-systems/pe-ratio/ ; https://companiesmarketcap.com/cadence-design-systems/ps-ratio/
  - https://stockanalysis.com/stocks/snps/statistics/
- **Industry and third party:**
  - SemiAnalysis (21 May 2026) https://newsletter.semianalysis.com/p/eda-market-primer
  - ESD Alliance Q2 2026 (19 Oct 2026) https://www.prnewswire.com/news-releases/electronic-system-design-industry-posts-5-7-billion-in-revenue-in-q2-2026--esd-alliance-reports-302912151.html
  - Wilson/Siemens (8 Sep 2026) https://blogs.sw.siemens.com/verificationhorizons/2026/09/08/the-2026-functional-verification-study/
  - TrendForce (20 Jan and 3 Aug 2026) https://www.trendforce.com/presscenter/news/20260120-12887.html ; https://www.trendforce.com/presscenter/news/20260803-13161.html
  - Empyrean (28 Apr 2026) https://static.cninfo.com.cn/finalpage/2026-04-28/1225217315.PDF
  - Anthropic (22 Oct 2026) https://www.anthropic.com/research/formal-verification
- **Competitor primary** (via synopsys.md):
  - Investor Day (30 Sep 2026) https://news.synopsys.com/2026-09-30-Synopsys-Details-Growth-Strategy-and-Long-term-Financial-Model-at-2026-Investor-Day
  - GPT-Synopsys (30 Sep 2026) https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence-to-Revolutionize-Chip-Design
  - Nvidia–Synopsys (1 Dec 2025) https://news.synopsys.com/2025-12-01-NVIDIA-and-Synopsys-Announce-Strategic-Partnership-to-Revolutionize-Engineering-and-Design
  - HAV (11 Mar 2026) https://news.synopsys.com/2026-03-11-Synopsys-Introduces-Software-Defined-Hardware-Assisted-Verification-to-Enable-AI-Proliferation
  - Siemens–Nvidia (9 Apr 2026) https://news.siemens.com/en-us/siemens-nvidia-veloce/
  - Synopsys Q3 FY2026 call (26 Aug 2026) https://www.webull.com/news/15497781661541376
  - Synopsys Q4 date (5 Nov 2026) https://finviz.com/news/417651/synopsys-announces-earnings-release-date-for-fourth-quarter-and-fiscal-year-2026
