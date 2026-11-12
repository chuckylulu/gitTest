# Cadence Design Systems, Inc. (NASDAQ: CDNS): chip verification and sign-off

Research date: 12 November 2026. All web checks were made on this date. This is the final version, merging an earlier partial pass with a continuation pass.

Tag key: [PRIMARY] filing or official document; [INDEPENDENT] confirmed by an outside party (customer, foundry, regulator, third-party data); [COMPANY CLAIM] stated by Cadence and not confirmed outside; [SECONDARY] press, analyst or aggregator only; [UNVERIFIED] could not verify; [INFERENCE] my own reasoning or arithmetic from cited inputs.

Process note: the shared web-search budget for this session ran out part-way through the continuation pass, and Firecrawl credits were also exhausted. After that I only fetched known URLs (Cadence and SEC filings, transcripts, foundry pages, Yahoo Finance's chart endpoint for daily prices). Some items are cross-referenced from other researchers' notes in this folder and say so. Gaps that needed fresh searches are listed at the end.

Overview: Cadence owns foundry-certified sign-off engines at every leading-edge foundry. It holds the larger share of emulation hardware and the de facto standard in analog/custom design. But the two most important final sign-off verdicts (static timing and DRC/LVS) are still dominated by Synopsys PrimeTime and Siemens Calibre. Financially it is very strong: 2026 growth is about 21%, non-GAAP margins are about 45%, about 80% of revenue is recurring, and no customer reaches 10%. Its AI-agent strategy is shipping, but nearly all its outcome claims are still its own.

---

## A. Quality tests (judged without share-price or valuation data)

### a. Position: does Cadence own a "judge"?

#### Takeaway
Cadence owns certified "judges" in sign-off and analog, plus the leading emulation hardware (a physical capacity constraint that AI does not remove). The decisive final sign-off verdicts on timing and physical verification are mostly passed through competitors' tools, though, so Cadence is a certified challenger there. Its AI agents (ChipStack and the other "Super Agents") sit in the weakest position on this test, as labour substitutes. Their stated purpose is to call Cadence's certified engines more often.

#### Cited findings: product by product
- **Sign-off: Tempus (timing), Quantus (extraction), Voltus (power/EM-IR), Pegasus (DRC/LVS), Certus, Liberate.**
  - TSMC, release of 23 Sep 2026 (NA OIP Forum): "digital full flow, signoff flow, and custom/analog flows are now certified for TSMC A16 and A14 process technologies".
    - The digital full flow is named as Innovus, Cerebrus, Tempus, EMX Planar 3D Solver, Voltus, Quantus, Pegasus and Liberate. Genus is only "enabled", not certified.
    - On N2P, analog, digital and sign-off flows are certified, but the tools are not named.
    - Artisan foundation IP for A14 is expected in Q4 2026. Virtuoso claims "up to 2.5X" fewer iterations [COMPANY CLAIM].
    - TSMC quote from Aveek Sarkar (director, Ecosystem and Alliance Management) on the "longstanding partnership".
    - Jasper, Xcelium, Conformal and Spectre are not mentioned, nor are ChipStack or Super Agent. [PRIMARY; foundry quote = INDEPENDENT in part] — [TSMC/Cadence release copy, 23 Sep 2026](https://finviz.com/news/394879/cadence-collaborates-with-tsmc-to-deliver-certified-tool-solutions-and-industry-leading-silicon-proven-ualink-ip-on-tsmc-advanced-processes)
  - TSMC's EDA Alliance certification grids (A14, A16, N2P, N3C, 3DFabric, "as of 10/01/2026") have columns only for Cadence, Synopsys and Siemens EDA. Categories include APR, timing, power, EMIR, DRC, LVS/LPE, RC, custom design and simulators. The per-cell status could not be machine-read. [PRIMARY] — [TSMC EDA Alliance](https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance) (also recorded in this folder's china.md and japan_korea_taiwan.md notes)
  - At the same forum, Synopsys showed A14-certified flows from implementation to sign-off, and Siemens had Calibre nmDRC, nmLVS, xACT and PERC certified for A14. [SECONDARY] — [Futurum](https://futurumgroup.com/insights/tsmcs-oip-forum-turns-agentic-chip-design-demos-into-production-flows/)
  - Samsung Foundry, release of 28 May 2026 (SAFE Forum; design-reuse copy dated 1 Jun 2026): a "comprehensive, certified flow" for second-generation 2nm.
    - The flow includes Innovus, Virtuoso Studio and Integrity 3D-IC. Quantus and Tempus are named as the sign-off tools, and Pegasus plus Tempus appear in the 3D Cube-H hybrid-bonding flow.
    - There is a new multi-year agreement broadening memory and interface IP. Samsung quote from Jongshin Shin (EVP, head of Foundry Design Platform Development).
    - SF2/SF3 flow certification was first announced in 2023. A Cadence blog of 31 Jul 2026 reportedly extends the certified flow to SF2P (search summary only; page not opened). [PRIMARY + Samsung quote] — [design-reuse](https://www.design-reuse.com/news/202530589-cadence-and-samsung-foundry-deepen-2nm-and-3d-ic-collaboration-to-meet-surging-ai-infrastructure-and-physical-ai-demand/) ; [Business Wire](https://www.businesswire.com/news/home/20260528147066/en/)
  - Intel Foundry, release of 27/28 Jul 2026: Cadence's AI-driven digital and custom reference flows are "certified on Intel 18A-P and Intel 14A" on "the latest Intel Foundry process design kits".
    - The flows cover synthesis, place and route, timing and power sign-off, physical and reliability verification, and analog/custom design. There is also an EMIB/EMIB-T packaging reference flow and a multi-year DTCO agreement targeting 14A. IP test chips have been validated in silicon on 18A.
    - Intel quote from Shawn Han (SVP & GM, Foundry Services): "Through co-optimized, certified design flows and silicon-validated IP, we give our customers greater confidence".
    - Individual tools and PDK versions are not named in the HPCwire copy. A secondary headline says 18A-P PDK 1.0 and 14A PDK 0.5. Intel 18A certification dates from 2025 (search summary). [PRIMARY + Intel quote] — [HPCwire copy](https://www.hpcwire.com/off-the-wire/cadence-certifies-ai-driven-reference-flows-for-intel-18a-p-and-intel-14a/) ; [Electronics World](https://www.electronicsworld.co.uk/ai-driven-digital-and-custom-reference-flows-tools-and-solutions-by-cadence-are-now-certified-on-intel-18a-p-pdk-1-0-and-intel-14a-pdk-0-5-technologies/42129/)
  - Rapidus: I found only the December 2024 collaboration, under which reference flows were "in development" (Cerebrus, Genus, Innovus, Tempus, Quantus, Voltus, Pegasus). Synopsys signed a parallel deal. Cadence says Rapidus will integrate the InnoStack AI Super Agent into its AI-Agent Design Solution, "targeting up to a 2X faster design turnaround" (Q2 2026) [COMPANY CLAIM]. No Rapidus certification was found. [PRIMARY 2024 / UNVERIFIED 2026] — [Business Wire 2024](https://www.businesswire.com/news/home/20241210546692/en/Cadence-and-Rapidus-Collaborate-on-Leading-Edge-2nm-Semiconductor-Solutions-for-AI-and-HPC-Applications) ; [eeNews](https://www.eenewseurope.com/en/rapidus-signs-2nm-deals-with-synopsys-cadence/)
  - Market reality, from SemiAnalysis estimates (21 May 2026): PrimeTime has "90%+" of timing sign-off and Calibre "85%+" of physical verification. TSMC specifies "Calibre-clean" DRC/LVS, and Samsung and Intel reportedly do the same. [SECONDARY estimate] — [SemiAnalysis EDA primer](https://newsletter.semianalysis.com/p/eda-market-primer)
  - The 10-K says Cadence works with foundries on PDKs "to ensure our core EDA products and solutions meet manufacturing sign-off requirements". [PRIMARY] — [FY2025 10-K](https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf)
- **Jasper (formal) and Conformal (equivalence checking).** Both are proof-type "judges" of functional correctness, but neither is foundry-certified, since certification covers physical and electrical flows. The 10-K lists Jasper and Xcelium as Cadence's two functional-verification products. On the Q3 call Devgan cited "strength of palladium and strength of Jasper" with no figures. ChipStack integrates with Jasper and Xcelium. I found no third-party share data for Jasper or Conformal, and Conformal is absent from the 2026 releases I read. [PRIMARY / COMPANY CLAIM] — [10-K](https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf) ; [Q3 2026 call](https://www.webull.com/news/15818016766808064)
- **Xcelium (simulation).** Estimated at about 40–45% share against VCS at 45–50% (SemiAnalysis estimate). It is a workhorse, not a judge. [SECONDARY]
- **Palladium (emulation) and Protium (FPGA prototyping).** Palladium is estimated at 55–60% of a $1.5bn+ emulation market, with ZeBu at 35–40% (SemiAnalysis estimate) [SECONDARY]. Hardware had "another record quarter, driven by continued strength in Palladium Z3 and Protium X3" (Q2 2026) [PRIMARY]. Devgan on Q1 2026: "Palladium Z3 continues to be the gold standard for emulation and drove multiple competitive displacement"; "we'll have a Z4 system before 2030" [COMPANY CLAIM]. The DVCon US 2026 paper (2–5 Mar 2026) describes Dynamic Duo III, a Cadence custom Z3 emulation processor plus AMD VP1902 FPGAs, "scalable to 48 billion gates" [COMPANY CLAIM; from market_structure_emulation_vip.md] — [DVCon](https://dvcon-proceedings.org/wp-content/uploads/Broadening-the-Adoption-of-Hardware-Assisted-Verification-with-Next-Generation-Emulation-Appliance.pdf)
- **Verisium (gen-AI verification and debug).** Described in the 10-K. No outside evidence found. On this test it is a gap-filler. [PRIMARY description only]
- **Verification IP.** The 10-K says VIP "enables system-level validation and integrates seamlessly with" Xcelium and Palladium. No share data found. [PRIMARY description only]
- **Virtuoso / Spectre (custom/analog).** The 10-K says Virtuoso is "considered the industry standard for custom and analog IC design" [COMPANY CLAIM]. SemiAnalysis says Virtuoso has "no credible competitor", with 450+ customers (Q4 2024) [SECONDARY]. Cadence reports "a significant competitive win with Spectre at a leading semiconductor supplier" (Q2 2026) [COMPANY CLAIM].
- **Innovus (place and route).** It gained 10–15 percentage points against Synopsys ICC2 between 2015 and 2020, then stabilised after Fusion Compiler launched (SemiAnalysis). [SECONDARY]
- **ChipStack and the AI "Super Agents".** These are ChipStack (front-end design and verification), InnoStack (digital implementation), ViraStack (analog), AuraStack (PCB and packaging), AgentStack (orchestration) and Maestro. Management's framing: "deterministic, physics-based engines, proprietary silicon correlated data" in the middle layer and "AI agents and orchestration at the top layer"; "autonomous agents ... call our underlying physically accurate engines more often" (Q2 2026). [PRIMARY statement] — [Q2 2026 prepared remarks](https://s206.q4cdn.com/597110084/files/doc_financials/2026/q2/CDNS-Q2-2026-Earnings-Conference-Call-Prepared-Remarks.pdf)

#### Inferences
- [INFERENCE] By the brief's test, Cadence's strongest positions are (i) certified sign-off and implementation engines at all three leading-edge foundries, (ii) Palladium, where it leads in hardware capacity, and (iii) Virtuoso, the de facto analog/custom standard. It does not own the market-standard final verdict in timing or DRC/LVS. Its sign-off strength is "certified and gaining" (management claim), not "the gate everyone must pass".
- [INFERENCE] Jasper and Conformal are the products most aligned with the prior that machine-proved regression becomes standard for AI-edited designs. The evidence on their market standing is the thinnest in this file.

#### Gaps
- Third-party share data for Jasper, Conformal, Tempus, Voltus, Quantus, Pegasus and VIP. I could not search after the budget ran out, and the SemiAnalysis primer's competitive section is paywalled.
- Per-tool, per-node certification status on TSMC's grid (not machine-readable), and certification at Rapidus.

### b. Lead: outside evidence of a technical and commercial lead

#### Takeaway
Outside evidence supports a real lead in emulation, analog/custom and foundry enablement. It also supports faster growth than the industry and than Synopsys's EDA business in 2026, which fits share gains. Outside evidence does not support a lead in timing or physical sign-off. Almost all AI-agent results and named deployments are Cadence's own statements.

#### Cited findings: independent or third-party
- All three leading-edge foundries put their own executives' quotes on 2026 certification releases: TSMC (23 Sep), Samsung (28 May) and Intel (27/28 Jul). TSMC's grids list only Cadence, Synopsys and Siemens. [INDEPENDENT in part; see a.]
- Share estimates (SemiAnalysis, 21 May 2026): emulation is Palladium 55–60% vs ZeBu 35–40%; simulation is Xcelium 40–45% vs VCS 45–50%; PrimeTime 90%+; Calibre 85%+. SemiAnalysis adds that ZeBu/HAPS posted a record year but "remains well behind Cadence's Palladium". [SECONDARY estimate] — [SemiAnalysis](https://newsletter.semianalysis.com/p/eda-market-primer)
- Industry comparison: SEMI ESD Alliance data show Q2 2026 industry revenue of $5,710.8m, up 12.2% year on year. Cadence's Q2 2026 revenue grew 24%, though this includes the Hexagon D&E acquisition. Synopsys's EDA revenue grew 8.5% in its quarter to July 2026, against Cadence Core EDA at +18% in Q2 and +20% in Q3. Segment definitions differ. [INDEPENDENT industry data / PRIMARY company data; from market_structure_emulation_vip.md and synopsys.md] — [ESD Alliance Q2 2026](https://www.prnewswire.com/news-releases/electronic-system-design-industry-posts-5-7-billion-in-revenue-in-q2-2026--esd-alliance-reports-302912151.html) ; [Synopsys Q3 FY2026 call](https://www.webull.com/news/15497781661541376)
- Competitors also report records in hardware-assisted verification. Synopsys reported "another record quarter for hardware-assisted verification" with "12 new and 66 repeat HAV customer wins" (26 Aug 2026), and its March 2026 HAV launch carried an NVIDIA quote. Siemens with Nvidia announced Veloce proFPGA CS (9 Apr 2026). [PRIMARY competitor sources, via synopsys.md and market_structure notes] — [Synopsys HAV](https://news.synopsys.com/2026-03-11-Synopsys-Introduces-Software-Defined-Hardware-Assisted-Verification-to-Enable-AI-Proliferation) ; [Siemens–Nvidia](https://news.siemens.com/en-us/siemens-nvidia-veloce/)
- Market demand for verification: the Siemens-sponsored Wilson Research study (8 Sep 2026; 604 respondents) finds verification takes 49% of IC/ASIC project time and first-silicon success was 5% in 2026 vs 14.4% in 2024, with a methodology break in 2024. [SECONDARY, sponsored by a competitor] — [Siemens blog](https://blogs.sw.siemens.com/verificationhorizons/2026/09/08/the-2026-functional-verification-study/)
- The Kimi K3 demonstration still needed EDA tools (open-source, 45nm). Analysts at BNP Paribas and Mizuho made this point (see B). [SECONDARY]

#### Cited findings: Cadence's own claims (not confirmed by the customers in the sources I read)
- "we are gaining share in almost all segments of our business"; "16 new full flow wins during the quarter" (Q3 2026). [COMPANY CLAIM] — [Q3 call](https://www.webull.com/news/15818016766808064)
- "expanded adoption of Tempus and Certus signoff tools on leading edge designs, with wins across hyperscalers, top semiconductor companies and startups"; "expanded our implementation and signoff footprint at frontier AI companies as well as at a marquee ASIC silicon vendor" (Q2 2026). In Q1 2026, "a marquee AI infrastructure company expanded their usage of our signoff solutions". Customers are unnamed. [COMPANY CLAIM] — [Q2 remarks](https://s206.q4cdn.com/597110084/files/doc_financials/2026/q2/CDNS-Q2-2026-Earnings-Conference-Call-Prepared-Remarks.pdf) ; [Q1 call](https://www.fool.com/earnings/call-transcripts/2026/04/27/cadence-cdns-q1-2026-earnings-transcript/)
- Hardware: "We added 12 new logos" plus "a notable competitive win with a major AI infrastructure provider" (Q2 2026). No hardware customer was named on the Q3 call. [COMPANY CLAIM]
- Named agent deployments (Q3 2026 call):
  - "MediaTek deployed chip stack into its production digital verification flow"
  - "the Renesas MCU team successfully deployed InnoStack"
  - "Samsung Foundry successfully used InnoStack"
  - Nokia "5x acceleration"
  - Socionext "up to a 5x overall productivity gain" (expected)
  - Q1 2026 named partners: Google, NVIDIA, MediaTek. [COMPANY CLAIM]
- Agent results:
  - ChipStack: "more than 40X faster RTL validation, reducing a typical five-week verification cycle to less than a day" (customer unnamed, Q2 2026)
  - ViraStack: "2X to 10X productivity"
  - AuraStack: "up to 15X higher productivity"
  - Maestro: "up to 30% higher quality and up to 5x greater token efficiency versus general purpose foundation model" (Q3 2026)
  - [COMPANY CLAIM] A TIKR headline reports Cadence saying a new agent "cut chip area 24% vs. general AI models" [SECONDARY headline only; article not read] — [TIKR](https://www.tikr.com/blog/cadence-says-its-new-ai-agent-cut-chip-area-24-vs-general-ai-models-heres-where-the-stock-could-go)
- Other Cadence datapoints cited by SemiAnalysis: Cerebrus 1,000+ tape-outs (Q1 2025); "ALL top 20 semiconductor companies using Cadence digital software" (Q4 2022). [COMPANY CLAIM via SECONDARY]

#### Inferences
- [INFERENCE] Growth twice the industry rate, and above Synopsys's EDA growth, is the best outside-checkable sign of share gains in 2026. Part of the gap is acquisitions (Hexagon) and the hardware upcycle.
- [INFERENCE] Nvidia appears in the 2026 hardware-verification launches of all three vendors, which points to multi-sourcing at the largest AI customer. I found no 2026 primary source naming Nvidia as a Palladium customer.

#### Gaps
- No independent confirmation from MediaTek, Renesas, Samsung Foundry, Nokia or Socionext of the agent results Cadence attributes to them.
- No 2026 primary source on Nvidia's use of Palladium.

### c. Revenue model

#### Takeaway
About 78–80% of revenue is recurring, mostly time-based licences of two to three years. About 20–23% is up-front (hardware, much of IP, some software), and the up-front share has been rising. Services are about 9%. Cadence is adding "subscription plus consumption" pricing for agents, and already has fixed-dollar drawdown ("card"/"token") arrangements, but discloses no consumption revenue.

#### Cited findings
- Mix and licence terms:
  - Recurring revenue was 80% in 2025 vs 83% in 2024 (recognised over time 76%, other recurring 4%); up-front 20% vs 17%. TTM recurring was 80% at Q4 2025 and 82% at Q1 2025.
  - Recurring includes over-time software licences, services, royalties, maintenance on IP and hardware, and hardware operating leases. "Other recurring" includes short-term software renewed at least annually and "non-cancelable commitments, whereby the customer commits to a fixed dollar amount over a specified period of time that can be used to purchase from a list of products".
  - Time-based licences run "generally two to three years", some "include the right for the customer to remix". Hardware is "either sold or leased", and emulation is also accessible through a Cadence-managed cloud. [PRIMARY] — [10-K](https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf)
- 2026 trend:
  - Recurring is ~80% expected for FY2026. TTM recurring/up-front was 78/22 at Q3 2026 (Q3 2025: 80/20).
  - Quarterly up-front: Q3'25 18%, Q4'25 21%, Q1'26 23%, Q2'26 22%, Q3'26 21%. Quarterly recurring: 82/79/77/78/79%.
  - Recurring revenue grew 18% year on year in Q3 2026, vs 11% growth in 2025. [PRIMARY] — [Q3 2026 CFO commentary](https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cfocommentary10262026ex9902.htm) ; [Q3 call](https://www.webull.com/news/15818016766808064)
- Product categories:
  - 2025 (2024): Core EDA 70% (71%), IP 14% (13%), SD&A 16% (16%). Core EDA includes "software, hardware, and services". [PRIMARY]
  - Quarterly, Q3'25 to Q3'26: Core EDA 71/69/71/68/69%; IP 14/15/14/15/15%; SD&A 15/16/15/17/16%.
  - Product and maintenance ($m): 1,208 / 1,332 / 1,349 / 1,431 / 1,487. Services ($m): 131 / 108 / 125 / 154 / 146. [PRIMARY] — [CFO commentary](https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cfocommentary10262026ex9902.htm)
  - Services revenue was $475.2m (9%) in 2025. [PRIMARY] — [10-K](https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf)
- Growth by segment in 2026:
  - Q1: Core EDA +18%, SD&A +18%, IP +22%.
  - Q2: IP "over 40%", Core EDA +18%, SD&A +37%.
  - Q3: Core EDA +20%, IP +24%, SD&A +30%.
  - Hardware revenue is not disclosed separately. Hardware was the "best quarter ever" in Q1, a record in Q2 and Q3, and "another record year" is expected. [PRIMARY / transcripts]
- Pricing for agents and use: management statements, verbatim with dates.
  - 17 Feb 2026 (Q4 2025 call):
    - Devgan: "So we will price it as like a virtual engineer or agent. So that would be extra business." ... "this is a misnomer that we are like seat count limited. We are exploration limited." He said an agentic flow "could run 10 or 100 experiments in parallel".
    - Wall: "we don't see AI forcing a wholesale change from subscriptions to consumption. Our customers still want predictable access to trusted sign-off engines. and certified flows. So multiyear subscription remains at the core of our business." ... "So we'll attach more usage-based pricing for incremental capacity and AI-driven optimization. We have card models and token models that handle all those things."
    - [PRIMARY transcript via secondary host] — [Motley Fool Q4 2025](https://www.fool.com/earnings/call-transcripts/2026/02/17/cadence-cdns-q4-2025-earnings-transcript/)
  - 27 Apr 2026 (Q1 call):
    - Devgan: new agentic products "will be priced as a subscription plus consumption model, very similar to other kind of leading AI tools. So that's a completely new category for Cadence."
    - Wall: "Our subscription model remains the anchor arrangement with our customers. The add-on monetization then comes incrementally through agentic workflow products that are kind of usage-based or consumption-based for capacity and through our token and card models. What's different about agentic AI is that it doesn't replace the core EDA engines. It calls them more often and it calls them intelligently." ... "We're not assuming a sudden step function in AI monetization in the guide".
    - Devgan: "There is no pushback at all. If we can deliver productivity, the customer is more than willing to engage."
    - [PRIMARY transcript via secondary host] — [Motley Fool Q1 2026](https://www.fool.com/earnings/call-transcripts/2026/04/27/cadence-cdns-q1-2026-earnings-transcript/)
  - 26 Oct 2026 (Q3 call):
    - Wall: "Our model allows customers to use their own LLM infrastructure ... And can license the underlying design agents ... the point is that greater customer usage should create greater value for Cadence."
    - Wall: "agents could perform much more design exploration than an individual engineer calling our underlying engines repeatedly, and that creates a potential for significantly more consumption of our core [EDA] tools"; "the economics of particular deployment options can vary, of course".
    - [PRIMARY transcript via secondary host] — [Q3 call](https://www.webull.com/news/15818016766808064)
- Channel: on 15 Apr 2026 ChipStack was made available on Google Cloud Marketplace, optimised with Gemini on Google Cloud, with an "up to 10X productivity" claim [PRIMARY release per search summary; COMPANY CLAIM for the figure] — [Business Wire](https://www.businesswire.com/news/home/20260415910313/en/Cadence-and-Google-Collaborate-to-Scale-AI-Driven-Chip-Design-with-ChipStack-AI-Super-Agent-on-Google-Cloud)
- Outside view: AI tools command "15-25% premiums" and renewals show "~20% uplift" from AI tools. The CFO's three-tier agentic monetisation is "an FY27–28 story". [SECONDARY] — [SemiAnalysis](https://newsletter.semianalysis.com/p/eda-market-primer)

#### Inferences
- [INFERENCE] Labour-hour exposure is small: services were about 9% of revenue. Exposure to one-off hardware is material and rising, within the 21–23% up-front share. The bulk of revenue is multi-year licences, priced on licence counts (seats/tokens) with remix rights. That makes the base sticky but tied to engineer and job counts until consumption pricing scales.
- [INFERENCE] The fixed-dollar drawdown arrangements (part of the 4% "other recurring") show that Cadence already runs usage-like contracts. The agent pricing extends existing instruments rather than building something new.

#### Gaps
- No disclosure of agent or consumption revenue, hardware revenue, VIP revenue or seat counts.

### d. Financial strength

#### Takeaway
Financial strength is very high. Non-GAAP operating margins are about 44–45%, free cash flow about $1.76bn a year (about 29% of revenue), net debt modest (about $1.2bn), no customer reaches 10%, and US revenue is 44%. The weak points are GAAP margins falling in 2026 (Hexagon amortisation and integration), stock-based compensation at about 9% of revenue, and China rising to 16% of quarterly revenue.

#### Cited findings
- FY2025 (released 17 Feb 2026):
  - Revenue $5.297bn (+14% vs $4.641bn). GAAP operating margin 28.2%, non-GAAP 44.6%. GAAP EPS $4.06, non-GAAP $7.14.
  - Operating cash flow $1.729bn and capex $142m, so FCF is about $1.587bn (derived).
  - Backlog $7.8bn; next-12-month RPO $3.8bn. Cash $3.001bn; long-term debt $2.480bn. [PRIMARY] — [Q4/FY2025 release](https://investor.cadence.com/news/news-details/2026/Cadence-Reports-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results/default.aspx)
- 2026 quarters:
  - Q1 (27 Apr): revenue $1.474bn (+19%). GAAP operating margin 29.3%, non-GAAP 44.7%. GAAP EPS $1.23, non-GAAP $1.96. Backlog $8.0bn; OCF $356m. [PRIMARY transcript] — [Q1 call](https://www.fool.com/earnings/call-transcripts/2026/04/27/cadence-cdns-q1-2026-earnings-transcript/)
  - Q2 (27 Jul): revenue $1.584bn (+24%). GAAP operating margin 28.4%, non-GAAP 45.5%. GAAP EPS $1.33, non-GAAP $2.11. Backlog $8.1bn; OCF $635m; DSO 65 days; buyback $200m. [PRIMARY] — [Q2 remarks](https://s206.q4cdn.com/597110084/files/doc_financials/2026/q2/CDNS-Q2-2026-Earnings-Conference-Call-Prepared-Remarks.pdf)
  - Q3 (26 Oct): revenue $1.633bn vs $1.339bn (+22%). GAAP operating margin 26.2% (31.8% a year earlier); non-GAAP 44.1% (47.6%). GAAP diluted EPS $1.05 (flat); non-GAAP $2.11 ($1.93). Record backlog $8.2bn; next-12-month RPO $4.2bn. Repurchases $400m, plus an additional $2.5bn authorisation. [PRIMARY] — [Q3 release, 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cdns10262026ex9901.htm)
- FY2026 guidance path:
  - 17 Feb: $5.9–6.0bn excluding Hexagon; GAAP operating margin 31.75–32.75%; non-GAAP 44.75–45.75%; non-GAAP EPS $8.05–8.15.
  - 27 Apr: $6.125–6.225bn including about $160m from Hexagon and about $0.28 of EPS dilution; non-GAAP EPS $7.85–7.95.
  - 27 Jul: $6.260–6.340bn (19% growth); non-GAAP operating margin 43.75–44.75%; non-GAAP EPS $8.05–8.15.
  - 26 Oct: $6.387–6.417bn (~21%); GAAP operating margin 28.2–29.2%; non-GAAP 44.2–45.2%; GAAP EPS $4.84–4.90; non-GAAP EPS $8.37–8.43; OCF ~$2.0bn; capex ~$240m.
  - Q4 2026 guide: $1.695–1.725bn (+18–20%); non-GAAP EPS $2.19–2.25. [PRIMARY] — [CFO commentary](https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cfocommentary10262026ex9902.htm)
- Cash flow and capital:
  - Quarterly FCF: Q4'25 $512m, Q1'26 $307m, Q2'26 $582m, Q3'26 $362m (TTM about $1.76bn, my sum).
  - Revenue from beginning backlog is about 64% of FY2026 (down from about 65%). Rule of 40 FY2026E is "~66%". SBC 2026E is $569m (~9% of revenue). Tax rate is about 27% GAAP and 16.5% non-GAAP.
  - FY2026 buybacks are ">50% of free cash flow" (about $400m planned in Q4). Diluted shares are 274–276m. [PRIMARY] — [CFO commentary](https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cfocommentary10262026ex9902.htm)
- Debt and liquidity:
  - Debt principal by quarter: $2.500bn (Q3'25), 2.500, 2.925, 2.500, 2.650bn (Q3'26). Cash: $2.753bn, 3.001, 1.407, 1.440, 1.452bn. About 15% of cash was in the US at Q3'26.
  - Senior notes: $500m 4.200% due 10 Sep 2027; $1.0bn 4.300% due 10 Sep 2029; $1.0bn 4.700% due 2034.
  - Revolver: $1.25bn (expandable to $1.75bn), expiring 14 Aug 2029. [PRIMARY] — [CFO commentary](https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cfocommentary10262026ex9902.htm) ; [10-K](https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf)
- Hexagon design and engineering (D&E) acquisition:
  - Agreement on 4 Sep 2025; completed 23/24 Feb 2026. About €2.70bn including about €150m of transaction taxes, paid 70% in cash (€1.89bn) and 30% in Cadence stock. MSC Nastran and Adams.
  - Expected about $160m of 2026 revenue and about $0.28 of 2026 non-GAAP EPS dilution, turning accretive in 2027.
  - Wall (Q3): "not really contributing much in the way of operating profit at all this year"; normal incremental margin is "54%, 55%". [PRIMARY via reprints / transcript] — [evertiq](https://evertiq.com/news/2026-02-24-cadence-completes-acquisition-of-hexagons-de-business) ; [HPCwire](https://www.hpcwire.com/off-the-wire/cadence-completes-acquisition-of-hexagons-design-and-engineering-business/)
- Returns: ROIC 17.09% (GAAP basis, aggregator), against 2.23% for Synopsys. [SECONDARY] — [StockAnalysis CDNS](https://stockanalysis.com/stocks/cdns/statistics/) ; [StockAnalysis SNPS](https://stockanalysis.com/stocks/snps/statistics/)
- Cost base and people: R&D was $1,768.8m (33% of revenue) in 2025. Employees were about 13,800 at 31 Dec 2025, and headcount was 15,753 at Q3 2026 after Hexagon. Devgan (Q1 2026) cited about 15,000 employees, about 10,000 in R&D. [PRIMARY / transcript]
- Concentration and geography:
  - No customer reached 10% of revenue in 2025, 2024 or 2023.
  - 2025 geography: US $2,311.0m (44%), Other Americas $168.3m (3%), China $680.0m (13%), Other Asia $1,005.2m (19%), EMEA $790.6m (15%), Japan $341.7m (6%). [PRIMARY] — [10-K](https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf)
  - Quarterly geography, Q3'25 to Q3'26: China 18/12/13/15/16%; Americas 43/47/45/43/43%; Other Asia 18/20/20/20/19%; EMEA 14/14/16/15/15%; Japan 7/7/6/7/7%. [PRIMARY] — [CFO commentary](https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cfocommentary10262026ex9902.htm)
  - Wall (Q1): "we still expect China to be about 13% for the year". Devgan (Q3): "there were some specific things with China revenue moving around". System companies are "45% of our business".

#### Inferences
- [INFERENCE] The cash fell from $3.0bn to $1.4bn in Q1 2026 while debt principal rose $425m temporarily. This is consistent with the Hexagon cash being funded mostly from cash plus a short revolver draw. Filings I read do not say so.
- [INFERENCE] Net debt is about $1.2bn, roughly 0.5x TTM GAAP EBITDA (about $2.2bn, implied by the aggregator's EV/EBITDA). The 2027 notes ($500m, due September 2027) are easily covered.
- [INFERENCE] Excluding Hexagon's about $160m, organic 2026 growth at the guidance midpoint is about 18%. This still includes 2025 acquisitions (Secure-IC, Artisan, VLAB).

#### Gaps
- ROIC from company data; a debt breakdown for Q3 2026 (what makes up the $2.65bn); customer concentration beyond the 10% test.

### e. Resilience

#### Takeaway
Resilience in a steady AI build-out is high. The main vulnerabilities are a record-high hardware base and an up-front share that has risen from 17% to about 22%. They also include 45% of revenue from system companies, whose AI programmes would be cut first in a financing-led pause, and 13–16% of revenue from China. History shows revenue fell 22% (2001–03) and 47% (2007–09) in earlier downturns. It grew through 2022–23.

#### Cited findings
- Revenue history (aggregator):
  - 2000 $1.27bn; 2001 $1.43bn; 2002 $1.29bn (−9.6%); 2003 $1.12bn (−12.85%); 2004 $1.19bn.
  - 2007 $1.61bn; 2008 $1.03bn (−35.7%); 2009 $0.85bn (−17.9%); 2010 $0.93bn; 2011 $1.14bn.
  - 2019 $2.33bn; 2020 $2.68bn; 2021 $2.98bn; 2022 $3.56bn (+19.2%); 2023 $4.08bn (+14.8%); 2024 $4.64bn; 2025 $5.29bn; TTM to Q3 2026 $6.13bn. [SECONDARY] — [companiesmarketcap](https://companiesmarketcap.com/cadence-design-systems/revenue/)
- Hardware cycle: "another record year for hardware" is expected in 2026. "hardware could be lumpy from quarter to quarter"; "no capacity or supply chain constraints"; inventory is being built ($448.8m vs $303.5m at end-2025, per market_structure notes). The 10-K notes reliance on "a single supplier or a limited number of suppliers for certain hardware components". Competitors also report records. [PRIMARY / transcript] — [Q3 call](https://www.webull.com/news/15818016766808064)
- AI-spending exposure: system companies are 45% of business. Devgan: "Google and Meta and Microsoft and Amazon and Tesla, everybody is doing more and more designs". TrendForce (secondary, via market_structure notes) puts the ASIC-based share of AI servers at 27.8% for 2026. It expects capex at nine cloud providers to rise about 90% to more than $886.7bn in 2026, and to about $1.3tn in 2027. [SECONDARY] — [TrendForce 3 Aug 2026](https://www.trendforce.com/presscenter/news/20260803-13161.html) ; [TrendForce 20 Jan 2026](https://www.trendforce.com/presscenter/news/20260120-12887.html)
- Design-start mix: the IBS chart in Cadence's DVCon 2026 paper shows 10,644 design starts in 2026, with about three-quarters at 28nm or above by 2030. [Third-party estimate via COMPANY slides; from market_structure notes] — [DVCon](https://dvcon-proceedings.org/wp-content/uploads/Broadening-the-Adoption-of-Hardware-Assisted-Verification-with-Next-Generation-Emulation-Appliance.pdf)
- Export controls and China:
  - On 27 Jul 2025 Cadence settled with BIS and DOJ over violations between 2015 and 2021, which "primarily involv[ed] sales ... valued at $45.3 million ... to a customer in China" plus onward technology transfer. It pleaded guilty to one count of conspiracy to commit export-control violations, under a three-year probationary term with compliance, reporting and cooperation duties. It also has a BIS settlement requiring two annual export-compliance audits, which "is a condition to our continued ability to export products". Penalties and forfeitures of $140.6m were paid in Q3 2025, which matches the brief's "roughly $140 million". [PRIMARY]
  - A BIS licence requirement for EDA exports to China, imposed 23 May 2025, was rescinded on 2 Jul 2025.
  - The Affiliates (50%) Rule took effect 29 Sep 2025, was suspended on 11 Nov 2025, and the 10-K said the suspension was "currently set to expire on November 9, 2026". [PRIMARY] — [10-K](https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf)
  - Update: on 5 Nov 2026 BIS extended the suspension to 10 Jan 2027. The extension is tied to the US–China framework (Busan) agreement, which was itself extended in September 2026 to 10 Jan 2027. The rule is suspended, not repealed. [SECONDARY law-firm briefings; Federal Register not checked] — [Clifford Chance](https://www.cliffordchance.com/briefings/2026/11/bis-suspends-affiliates-rule-until-january-10-2027.html) ; [Thompson Hine](https://www.thompsonhinesmartrade.com/2026/11/bis-extends-affiliates-rule-until-january-2027/) ; [Global Sanctions](https://globalsanctions.com/2026/11/us-bis-extends-suspension-50-rule-coming-into-force-until-10-january-2027/)
  - Cadence's guidance assumes export-control rules "remain substantially similar". [PRIMARY]
- China localisation: the 10-K names "emerging players in China such as Huada Empyrean, Xpeedic". Empyrean's 2025 revenue was RMB 1,324.98m (+8.40%), 90% domestic (from china.md). [PRIMARY] — [Empyrean 2025 annual report](https://static.cninfo.com.cn/finalpage/2026-04-28/1225217315.PDF)

#### Inferences (provisional, mine)
- [INFERENCE] **Steady growth (~55%):** this scenario fits the 2026 evidence (record backlog, three guidance raises, record hardware). Consensus growth of about 14% for 2027 looks consistent with it.
- [INFERENCE] **Financing-led pause around 2028 (~25%):** the exposed revenue is up-front hardware and IP, about 21–23% of the total, plus system-company programmes.
  - As an illustration only, a one-third fall in up-front revenue would cut total revenue by about 7%. The 78–80% recurring base and $8.2bn backlog cushion the rest.
  - The 2008–09 fall (−47% cumulative) is far worse than this illustration. I could not verify how much of it came from a licensing-model change rather than the recession, so it should not be used directly as a base case.
  - 2022–23 is the closest recent analogue. Cadence grew 19% and 15% then.
- [INFERENCE] **Faster acceleration (~20%):** upside comes from hardware capacity and consumption pricing. The same speed would also shorten the time before AI plus open tools is good enough for mature-node design, where most design starts sit.
- [INFERENCE] **Cycle position:** late in a hardware upcycle (records in 2025–26 at Cadence and Synopsys), with IP very strong and the up-front mix elevated. On this basis 2027 comparisons are harder than 2026.

#### Gaps
- Primary data for the 2001–03 and 2008–09 periods, including the licence-model effect in 2008. Hardware revenue history. How much of 2026 China revenue is catch-up.

---

## B. Path forward (industry transitions)

### Transition by transition: what Cadence has said versus done
- **(1) Verification labour to tools.**
  - Said: agents priced "like a virtual engineer"; "industry's first fully autonomous virtual AI Design Engineer" (Computex, with NVIDIA).
  - Done:
    - ChipStack acquisition agreed about 10 Nov 2025. ChipStack is a Seattle start-up from the AI2 Incubator, founded 2023, which raised more than $7m. Terms were undisclosed. Cadence claimed "70%" verification acceleration [COMPANY CLAIM]. — [GeekWire](https://www.geekwire.com/2025/cadence-to-acquire-seattle-startup-chipstack-to-boost-chip-design-automation/) ; [design-reuse](https://www.design-reuse.com/news/202529654-cadence-welcomes-chipstack/)
    - ChipStack AI Super Agent: early access from February 2026, with unnamed customers reporting "4X to 10X" [COMPANY CLAIM]. A Level-5 version running on NVIDIA's OpenShell runtime, plus AgentStack orchestration, was announced at Computex (about 31 May/1 Jun 2026), for early-access customers in H2 2026. The releases carry an Nvidia quote but no customer quotes. — [Business Wire](https://www.businesswire.com/news/home/20260531072918/en/Cadence-Announces-ChipStack-AI-Super-Agent) ; [design-reuse](https://www.design-reuse.com/news/202530621-cadence-unveils-industry-s-first-fully-autonomous-virtual-engineer-for-chip-design-powered-by-nvidia/)
    - More than 20 ChipStack engagements in Q2, "deployed in production across multiple chip designs". More than 100 Super Agent engagements by Q3, and MediaTek production use [COMPANY CLAIM].
    - The 10-K says the acquired technology is "deployed at leading chip companies and hyperscalers ... reducing verification cycles from weeks to days" [COMPANY CLAIM]. Services are about 9% of revenue, so labour erosion would hurt little.
- **(2) Seat licences to pricing by use.** Said: see the quotations in c ("subscription plus consumption"; "we don't see AI forcing a wholesale change"). Done: Google Cloud Marketplace listing (15 Apr 2026), existing card/token models and fixed-dollar drawdown contracts. Not done: no consumption revenue disclosed, and "We're not assuming a sudden step function in AI monetization".
- **(3) Simulation toward formal proof.** Said: little specific. Done: owns Jasper and Conformal, and ChipStack integrates with Jasper and Xcelium. Risk: Cadence's largest growth engine is emulation (simulation-based), and a shift of cycles to formal would move value within its own portfolio. No formal-specific roadmap was found.
- **(4) Proprietary engines vs open-source tools driven by AI.**
  - Said: Devgan (Q2): "to really do real designs, people use Cadence" (see the Kimi section). Devgan (Q1), on AI rewriting base tools such as Virtuoso and Innovus: "I'm not worried that some other party will be able to write any better base tools" [PRIMARY transcript].
  - Done: certification at A14, A16, N2P, 18A-P, 14A and second-generation 2nm. Open tools lack advanced-node PDKs (Tech Fund, secondary, via synopsys.md) — [Tech Investments](https://www.techinvestments.io/p/the-eda-crash-and-the-massive-ai).
  - Risk: mature nodes, where about three-quarters of design starts sit by 2030 and certification matters less. Bernstein's view that open tooling could pressure lower-end pricing "sooner than incumbents expect" (paraphrase) — [stockti](https://stockti.com/synopsys-shares-plunge-8-as-moonshot-ai-s-chip-demo-raises-eda-moat-concerns)
- **(5) Foundry certification as a barrier to entry.** This is the strongest evidence in the file: 2026 certifications at all three leading foundries with their executives' quotes, and TSMC grids listing only the three incumbents. The Rapidus position is unconfirmed. Cadence is the beneficiary of this barrier, not a challenger to it.
- **(6) A paying market for verified software.** Largely not applicable. VLAB Works (virtual prototyping for embedded software), Secure-IC (security IP and evaluation tools) and BETA CAE/Hexagon (mechanical simulation) are not machine-checked software proof. In software, Anthropic's research (22 Oct 2026) shows model makers producing proofs, with no product offered (from model_makers_hyperscalers.md) — [Anthropic](https://www.anthropic.com/research/formal-verification). Cadence has no stated buyer or product here.
- **(7) AI model makers offering verification themselves.**
  - Said: Devgan (Q3): "we have worked with OpenAI from the very beginning of when they got started ... same thing with Anthropic and Gemini, the 3 leading frontier models"; he also noted "very, very good open-weight ... models" [PRIMARY transcript]. Model-agnostic design: customers "use their own LLM infrastructure".
  - Done:
    - Google Gemini collaboration (15 Apr 2026, primary).
    - NVIDIA OpenShell and Computex (primary). ChipStack reportedly uses NVIDIA Nemotron models (BNP, secondary).
  - Competitive contrast: Synopsys announced GPT-Synopsys with OpenAI on 30 Sep 2026. The two are "preferred partners", OpenAI licenses Synopsys tools, and revenue is shared. Nvidia also bought $2bn of Synopsys stock ("not exclusive"). [PRIMARY competitor sources, via synopsys.md] — [GPT-Synopsys](https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence-to-Revolutionize-Chip-Design) ; [Nvidia–Synopsys](https://news.synopsys.com/2025-12-01-NVIDIA-and-Synopsys-Announce-Strategic-Partnership-to-Revolutionize-Engineering-and-Design)
  - I found no equivalent preferred-partner or revenue-share deal between Cadence and a frontier lab.
- **Funding and commitment:** R&D $1.77bn (33% of revenue) in 2025; FCF about $1.76bn a year; more than 50% of FCF going to buybacks; acquisitions since 2024 are BETA CAE, VLAB Works, Arm Artisan, Secure-IC, ChipStack and Hexagon D&E (about €2.7bn). The Intel 14A multi-year engagement is "expected to be a meaningful driver of growth over the next few years" [COMPANY CLAIM]. A first Tensilica DSP win at STMicroelectronics (Q2 2026).

### The July 2026 episode (Kimi K3)
- What Moonshot claimed:
  - The blog states results are "current as of July 16, 2026". K3 "designed a chip to serve a nano model built on its own architecture" in a single 48-hour autonomous run, using open-source EDA tools on the Nangate 45nm library.
  - The design fits within 4 mm², closes timing at 100 MHz and has 1.46m standard cells. Throughput was measured in simulation. No tape-out or sign-off is mentioned. [PRIMARY; COMPANY CLAIM by Moonshot] — [Kimi blog](https://www.kimi.com/blog/kimi-k3)
- Share move:
  - Friday 17 Jul 2026: CDNS closed $330.11, −9.47% from $364.65, on 5.19m shares versus about 1.3–1.6m on prior days. The intraday low cited was $329.50 (−9.64%) at 13:07 EDT. SNPS closed $384.28 (−7.85%), $382.98 intraday (−8.17%).
  - Following days: 20 Jul $329.93; 21 Jul $344.64 (+4.46%); 22 Jul $337.01; 23 Jul $330.46; 24 Jul $326.24 (−10.5% versus 16 Jul).
  - After Q2 results (27 Jul, after the close): 28 Jul $344.72 (+1.80%); 29 Jul $332.76 (−3.47%); 31 Jul $340.02.
  - [SECONDARY market data] — [Yahoo Finance chart API](https://query1.finance.yahoo.com/v8/finance/chart/CDNS?interval=1d) ; [ts2.tech](https://ts2.tech/en/synopsys-nasdaqsnps-stock-sinks-as-kimi-chip-demo-tests-the-eda-moat/) ; [TIKR](https://www.tikr.com/blog/cadence-stock-fell-9-in-a-day-on-a-chinese-ai-chip-demo-heres-where-the-stock-could-go-in-2026)
  - The 17 Jul close was the lowest since 30 April for CDNS and since 30 March for SNPS (MoneyDJ). Later, on 15 Sep 2026, CDNS hit a close 34.2% below its June high, after a 1 Sep software sell-off that TIKR attributes to rising bond yields.
  - **The background claim of "falls of about 9%" is right for Cadence and slightly high for Synopsys (about 8%).**
- Analysts:
  - BNP Paribas (Andrew DeGasperi): the reaction was "excessive and unreasonable" (translated), "buy the dip". He compared it to cybersecurity stocks' reaction to the "Mythos preview", said K3 relied on decades-old open-source tools, and said 45nm is not comparable with nodes below 5nm. He cited ChipStack cutting a five-week RTL cycle to 24 hours. [SECONDARY] — [MoneyDJ/TechNews, 20 Jul 2026](https://finance.technews.tw/2026/07/20/kimi-driven-selloff-makes-cadence-synopsys-buying-opportunities/) ; [Seeking Alpha, 17 Jul 2026](https://seekingalpha.com/news/4615018-cadence-synopsys-sink-as-moonshot-brings-eda-disruption-risks-bnp-says-buy-the-dip)
  - Mizuho: K3 still depended on existing EDA tools (search summary only).
  - Bernstein (Robin Zhu): K3 shows Chinese labs can "keep pace with the US frontier". He reportedly called the reaction "generally sensible", with open tooling able to pressure lower-end pricing sooner than expected. [SECONDARY] — [stockti, 17 Jul 2026](https://stockti.com/synopsys-shares-plunge-8-as-moonshot-ai-s-chip-demo-raises-eda-moat-concerns)
- Management:
  - The Q2 prepared remarks (27 Jul) did not name Kimi. They stressed "deterministic, physics-based engines" and raised guidance to 19% growth.
  - Q&A, as quoted by a blog and not checked against an official transcript: Devgan said "they said a chip, but I think it's a small block, which is about technology which is like 20 years old"; "So even to design a small block at such an old node, they needed EDA tools to do that"; "to really do real designs, people use Cadence to do that." He reportedly added that it ran 20–30 times slower than current frequencies (paraphrase; unverified). Baird's Joe Vruwink asked about open-source AI agents. [SECONDARY transcript excerpts] — [Expanse Stocks](https://expansestocks.substack.com/p/cadence-q2-2026) ; [Barchart](https://www.barchart.com/story/news/3606848/5-revealing-analyst-questions-from-cadence-design-systemss-q2-earnings-call)

### Provisional verdict (my judgment)
**Coherent (provisional), with lower confidence on transitions (4) and (7).**
- Words and actions line up:
  - The acquisition (Nov 2025) became a product (Feb 2026), which reached named production use (Q3 2026, company claim).
  - Certification renewed at every leading-edge node in 2026.
  - The pricing design (subscription plus consumption on top of certified engines) matches the stated thesis that agents call engines more often.
  - The plan is funded internally.
  - The timing is plausible: Level-5 is in early access in H2 2026, and outside analysts see monetisation as a 2027–28 story.
- What must go right:
  - (i) Agents raise engine consumption rather than cannibalise licences, which needs evidence in the February 2027 guide or later.
  - (ii) Foundry certification remains the gate for AI-generated designs at advanced nodes.
  - (iii) The hardware cycle does not reverse sharply.
  - (iv) China access holds after 10 Jan 2027.
  - (v) Cadence keeps access to frontier models without ceding the agent layer to a lab-backed rival stack such as GPT-Synopsys.
  - (vi) Hexagon turns accretive in 2027.

---

## C. Entry point (share price and valuation; kept separate from the quality tests)

### Takeaway
At $329.26 (close on 11 Nov 2026), Cadence trades at about 39x 2026 and 33x 2027 consensus non-GAAP EPS, and about 14.9x trailing EV/sales, with a free-cash-flow yield of about 2%. That is below its own five-year P/S and GAAP P/E medians but above its ten-year medians. It is also a clear premium to Synopsys on forward earnings and sales. The price is about 21% below the June 2026 high and about 20–24% above the 2026 lows.

### Cited findings
- Snapshot (close 11 Nov 2026):
  - Price $329.26; market cap $90.34bn; EV $91.61bn.
  - Trailing P/E 65.47 (GAAP); forward P/E 34.94; EV/sales 14.94; EV/EBITDA 41.26 (GAAP EBITDA); EV/FCF 51.94; FCF yield 1.95%; ROIC 17.09%. [SECONDARY aggregator] — [StockAnalysis](https://stockanalysis.com/stocks/cdns/statistics/)
- Recent prices:
  - 2 Nov $329.51; 3 Nov $323.75; 4 Nov $329.52; 5 Nov $311.43 (−5.49%); 6 Nov $319.92; 9 Nov $336.53 (+5.19%); 10 Nov $331.64; 11 Nov $329.26.
  - 12-month closing high $416.39 (2 Jun 2026; intraday $416.69). Closing low $265.66 (10 Apr 2026). 15 Sep 2026 close $273.96. The 11 Nov close is up 5.3% from the 31 Dec 2025 close ($312.58).
  - Other ±5% days in 2026: 3 Feb −7.15%; 17/18 Feb −5.34%/+7.60% (FY2025 results); 10/13 Apr −5.46%/+8.48%; 1 Jun +10.46% (Computex announcement window); 5 Jun −8.62% (SNPS −5.99%; cause not checked); 1 Sep −7.60%; 1 Oct +6.22%; 27 Oct +6.49% (Q3 results). [SECONDARY market data] — [StockAnalysis history](https://stockanalysis.com/stocks/cdns/history/) ; [Yahoo Finance chart API](https://query1.finance.yahoo.com/v8/finance/chart/CDNS?interval=1d)
- My calculations (inputs as cited) [INFERENCE]:
  - Price / FY2026 consensus non-GAAP EPS ($8.42) = 39.1x. Price / FY2027 consensus ($9.85) = 33.4x. Price / FY2026 GAAP EPS guidance midpoint ($4.87) = 67.6x.
  - EV / 2026E revenue ($6.40bn) = 14.3x. EV / 2027E revenue ($7.33bn) = 12.5x. EV / 2026E non-GAAP operating income (about $2.86bn at the midpoint margin) ≈ 32x.
  - FCF yield after deducting SBC ($569m) is about 1.3%.
- History (year-end values, aggregator; medians computed by me):
  - GAAP P/E: 2016 35.5; 2017 55.8; 2018 34.5; 2019 19.2 (likely depressed by a one-off GAAP gain; not checked); 2020 63.5; 2021 73.1; 2022 51.3; 2023 70.6; 2024 77.2; 2025 76.4; current 65.1. The five-year median is 73.1 (range 51.3–77.2); the ten-year median is 59.7 (range 19.2–77.2). — [companiesmarketcap P/E](https://companiesmarketcap.com/cadence-design-systems/pe-ratio/)
  - P/S: 2016 3.98; 2017 6.08; 2018 5.69; 2019 8.31; 2020 14.2; 2021 17.3; 2022 12.4; 2023 18.1; 2024 18.0; 2025 16.0; current 14.7 (the page body also shows 13.1, undated). The five-year median is 17.3 (range 12.4–18.1); the ten-year median is 13.3 (range 3.98–18.1). [SECONDARY] — [companiesmarketcap P/S](https://companiesmarketcap.com/cadence-design-systems/ps-ratio/)
- Peers (Synopsys, close 11 Nov 2026, from synopsys.md):
  - Price $462.12; market cap $88.56bn; EV $95.79bn; trailing P/E 81.94; forward P/E 26.26; EV/sales 10.17; EV/EBITDA 46.15 (GAAP, depressed by Ansys amortisation and restructuring); EV/FCF 34.86; net debt $7.23bn. [SECONDARY] — [StockAnalysis SNPS](https://stockanalysis.com/stocks/snps/statistics/)
  - Synopsys's FY2027 guidance is non-GAAP EPS of $19.04–19.12 (about 24x at $462.12, my calculation). Its long-term model to FY2030 is about 15% revenue CAGR and about 50% non-GAAP operating margin. [PRIMARY] — [Synopsys Investor Day, 30 Sep 2026](https://news.synopsys.com/2026-09-30-Synopsys-Details-Growth-Strategy-and-Long-term-Financial-Model-at-2026-Investor-Day)
  - Siemens EDA has no separate listing.
- Consensus (updated 9 Nov 2026, S&P Global data):
  - FY2026 revenue $6.41bn (+21.0%); FY2027 $7.33bn (+14.4%).
  - Non-GAAP EPS FY2026 $8.42 (+18.0%); FY2027 $9.85 (+16.9%). FY2028 is behind a paywall.
  - 24 analysts rate it "Strong Buy". Price targets: mean $411.76, median $420, low $300, high $470. [SECONDARY] — [StockAnalysis forecast](https://stockanalysis.com/stocks/cdns/forecast/)
- Management on run-rate: Wall (Q3), excluding Hexagon: "kind of mid teens for revenue growth, high teens for EPS growth". Devgan: next-year guidance comes "in February". No long-term financial targets from Cadence were found in this pass. [PRIMARY transcript]
- Revenue on seat or time-based licences and services: recurring is 78–80%, mainly 2–3-year time-based licences, and services are about 9%. Up-front revenue (hardware, IP and some software) is 21–23%. [PRIMARY]
- Near-term events:
  - 8 Dec 2026: Synopsys Q4 FY2026 results (read-across). [PRIMARY via newswire] — [Finviz](https://finviz.com/news/417651/synopsys-announces-earnings-release-date-for-fourth-quarter-and-fiscal-year-2026)
  - 10 Jan 2027: the extended suspension of the Affiliates Rule and the US–China framework expire.
  - About mid-February 2027: Cadence Q4 2026 results and 2027 guidance. The FY2025 release was on 17 Feb 2026, and the exact date was not found.
  - 10 Sep 2027: the $500m notes mature.
  - The DOJ probation runs three years from the 2025 plea.
  - No acquisition is pending.

### Inferences
- [INFERENCE] The price assumes a long period of growth well above nominal GDP. At a 1.95% FCF yield and an 8–9% required return, a simple perpetuity model implies about 6–7% FCF growth for ever (before deducting SBC). In practice that means consensus-like mid-teens growth for several years, followed by a slow fade. This is an illustration, not a valuation.
- [INFERENCE] Cycle position adds to entry risk. The 2026 numbers include a record hardware year, strong IP and about 3 percentage points of Hexagon growth, so 2027 consensus growth of 14% assumes these hold or are replaced.
- [INFERENCE] Conditions under which entry would look more attractive:
  - A price near the 2026 lows ($266–274), which would be about 27–28x 2027 consensus EPS.
  - P/S at or below the ten-year median (13.3x) or the 2022 trough (12.4x).
  - A February 2027 guide that shows agent or consumption revenue as additive, with hardware normalising without a guidance cut.
  - Clarity on the Affiliates Rule after 10 Jan 2027.
  - Another AI-scare sell-off like July's (about −10% in a week) that is not followed by any fundamental deterioration. In July, guidance was raised ten days after the sell-off.
  - (Analysis only; not a recommendation.)

### Gaps
- Five- and ten-year history of forward (non-GAAP) P/E and EV/EBITDA; FY2028 consensus; the confirmed date of the Q4 2026 results.

---

## Closing lists

### 1. What I could not verify
- Third-party market share for Jasper (formal), Conformal (equivalence), Tempus, Voltus, Quantus, Pegasus and Cadence VIP. The SemiAnalysis competitive section is paywalled.
- Per-tool status in TSMC's certification grid (not machine-readable); any Rapidus certification of Cadence tools; the Samsung SF2P blog of 31 Jul 2026 (search summary only).
- Customer confirmation of the agent results Cadence attributes to MediaTek, Renesas, Samsung Foundry, Nokia, Socionext and Rapidus. All of Cadence's agent speed-up figures (4–10X, 40X, 2.5X, 15X, 30%/5x) are company claims.
- 2026 primary evidence of Nvidia's use of Palladium.
- The exact Kimi K3 Q&A wording from an official transcript; Mizuho's note (search summary only); the cause of the −8.6% move on 5 Jun 2026.
- How much of the 2008–09 revenue fall came from licensing-model change rather than the recession; 2001–03 detail from filings.
- How the Hexagon cash was financed (my inference is cash plus a short revolver draw), and what makes up the $2.65bn debt at Q3 2026.
- Hardware, consumption and agent revenue (not disclosed); forward P/E and EV/EBITDA history; FY2028 consensus; the Q4 2026 results date.
- Whether Cadence has any preferred-partner or revenue-share agreement with OpenAI or Anthropic (Devgan says it "worked with" them; no agreement was found).

### 2. Where current evidence contradicts or fails to support the background views
- "Seat-priced tools face pressure once AI agents can drive open-source alternatives": **not visible yet.**
  - Core EDA grew 18–20% in 2026, recurring revenue +18%, and backlog reached a record $8.2bn.
  - Management says agents increase engine use, and a secondary source reports about 20% renewal uplift from AI tools.
  - The July sell-off was a market fear, not a change in the business. The prior can still prove right at mature nodes and after 2028, but 2026 data do not support it.
- "Value moves to the judge": **broadly supported, with a qualification for Cadence.**
  - The leading final sign-off judges (PrimeTime for timing, Calibre for DRC/LVS; "Calibre-clean" is TSMC's requirement) belong to Synopsys and Siemens.
  - Cadence's judge-like assets are certified but in minority positions. Its clearest lead is emulation hardware and analog/custom, not the final sign-off gate.
- "The three large design-tool vendors keep growing through 2029 (70%)": **consistent.** Cadence grows about 21% in 2026 against 12% for the industry, with 2027 consensus at +14%. There is no contrary evidence.
- "Verification labour loses pricing power": **not tested here.** Cadence's services are only about 9% of revenue, and Cadence is positioning its agents to take labour budgets.
- "Machine-proved regression checks standard for AI-edited chip designs by 2028 (60%)": **no supporting evidence found.** Cadence does not disclose formal or equivalence adoption, and its fastest-growing verification business is simulation-based emulation hardware.
- "Final sign-off stays with people": **not contradicted.** Cadence markets "Level-5 autonomy" and a "fully autonomous virtual AI Design Engineer", but certification is still of engines and flows, and Kimi K3 did no sign-off.
- Brief's figure "falls of about 9%" in July: **correct for Cadence** (−9.47% close). Synopsys fell about 8% (−7.85% close).

### 3. Sources with dates
- Cadence primary:
  - FY2025 Form 10-K (filed Feb 2026; covers FY2025) — https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf
  - Q4/FY2025 release, 17 Feb 2026 — https://investor.cadence.com/news/news-details/2026/Cadence-Reports-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results/default.aspx
  - Q2 2026 prepared remarks, 27 Jul 2026 — https://s206.q4cdn.com/597110084/files/doc_financials/2026/q2/CDNS-Q2-2026-Earnings-Conference-Call-Prepared-Remarks.pdf
  - Q3 2026 release (8-K Ex. 99.1), 26 Oct 2026 — https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cdns10262026ex9901.htm
  - Q3 2026 CFO commentary (Ex. 99.2), 26 Oct 2026 — https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cfocommentary10262026ex9902.htm
- Transcripts (secondary hosts):
  - Q4 2025, 17 Feb 2026 — https://www.fool.com/earnings/call-transcripts/2026/02/17/cadence-cdns-q4-2025-earnings-transcript/
  - Q1 2026, 27 Apr 2026 — https://www.fool.com/earnings/call-transcripts/2026/04/27/cadence-cdns-q1-2026-earnings-transcript/
  - Q3 2026, 26 Oct 2026 — https://www.webull.com/news/15818016766808064
  - Q3 2026 summary — https://www.roic.ai/quote/CDNS/transcripts/2026-year/3-quarter
  - Q2 2026 Q&A excerpts — https://expansestocks.substack.com/p/cadence-q2-2026 ; https://www.barchart.com/story/news/3606848/5-revealing-analyst-questions-from-cadence-design-systemss-q2-earnings-call
- Foundry releases and pages:
  - TSMC/Cadence, 23 Sep 2026 — https://finviz.com/news/394879/cadence-collaborates-with-tsmc-to-deliver-certified-tool-solutions-and-industry-leading-silicon-proven-ualink-ip-on-tsmc-advanced-processes
  - TSMC EDA Alliance grids (as of 1 Oct 2026) — https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance
  - Futurum on OIP (Sep 2026) — https://futurumgroup.com/insights/tsmcs-oip-forum-turns-agentic-chip-design-demos-into-production-flows/
  - Intel, 27/28 Jul 2026 — https://www.hpcwire.com/off-the-wire/cadence-certifies-ai-driven-reference-flows-for-intel-18a-p-and-intel-14a/ ; https://www.electronicsworld.co.uk/ai-driven-digital-and-custom-reference-flows-tools-and-solutions-by-cadence-are-now-certified-on-intel-18a-p-pdk-1-0-and-intel-14a-pdk-0-5-technologies/42129/
  - Samsung, 28 May/1 Jun 2026 — https://www.design-reuse.com/news/202530589-cadence-and-samsung-foundry-deepen-2nm-and-3d-ic-collaboration-to-meet-surging-ai-infrastructure-and-physical-ai-demand/ ; https://www.businesswire.com/news/home/20260528147066/en/
  - Rapidus, 10–11 Dec 2024 — https://www.businesswire.com/news/home/20241210546692/en/Cadence-and-Rapidus-Collaborate-on-Leading-Edge-2nm-Semiconductor-Solutions-for-AI-and-HPC-Applications ; https://www.eenewseurope.com/en/rapidus-signs-2nm-deals-with-synopsys-cadence/
- Acquisitions and products:
  - ChipStack, Nov 2025 — https://www.geekwire.com/2025/cadence-to-acquire-seattle-startup-chipstack-to-boost-chip-design-automation/ ; https://www.design-reuse.com/news/202529654-cadence-welcomes-chipstack/
  - ChipStack Super Agent, ~31 May 2026 — https://www.businesswire.com/news/home/20260531072918/en/Cadence-Announces-ChipStack-AI-Super-Agent ; https://www.design-reuse.com/news/202530621-cadence-unveils-industry-s-first-fully-autonomous-virtual-engineer-for-chip-design-powered-by-nvidia/
  - Google, 15 Apr 2026 — https://www.businesswire.com/news/home/20260415910313/en/Cadence-and-Google-Collaborate-to-Scale-AI-Driven-Chip-Design-with-ChipStack-AI-Super-Agent-on-Google-Cloud
  - Hexagon closing, 23–24 Feb 2026 — https://evertiq.com/news/2026-02-24-cadence-completes-acquisition-of-hexagons-de-business ; https://www.hpcwire.com/off-the-wire/cadence-completes-acquisition-of-hexagons-design-and-engineering-business/
  - DVCon US 2026 paper, Mar 2026 — https://dvcon-proceedings.org/wp-content/uploads/Broadening-the-Adoption-of-Hardware-Assisted-Verification-with-Next-Generation-Emulation-Appliance.pdf
- Kimi K3 episode:
  - Moonshot blog (results as of 16 Jul 2026) — https://www.kimi.com/blog/kimi-k3
  - ts2.tech, 17 Jul 2026 — https://ts2.tech/en/synopsys-nasdaqsnps-stock-sinks-as-kimi-chip-demo-tests-the-eda-moat/
  - TIKR (Jul and Sep 2026) — https://www.tikr.com/blog/cadence-stock-fell-9-in-a-day-on-a-chinese-ai-chip-demo-heres-where-the-stock-could-go-in-2026
  - stockti, 17 Jul 2026 — https://stockti.com/synopsys-shares-plunge-8-as-moonshot-ai-s-chip-demo-raises-eda-moat-concerns
  - Seeking Alpha (BNP), 17 Jul 2026 — https://seekingalpha.com/news/4615018-cadence-synopsys-sink-as-moonshot-brings-eda-disruption-risks-bnp-says-buy-the-dip
  - MoneyDJ/TechNews, 20 Jul 2026 — https://finance.technews.tw/2026/07/20/kimi-driven-selloff-makes-cadence-synopsys-buying-opportunities/
  - Tech Investments, 27 Jul 2026 — https://www.techinvestments.io/p/the-eda-crash-and-the-massive-ai
  - TIKR headline (date not checked) — https://www.tikr.com/blog/cadence-says-its-new-ai-agent-cut-chip-area-24-vs-general-ai-models-heres-where-the-stock-could-go
- Export controls: Clifford Chance (Nov 2026) — https://www.cliffordchance.com/briefings/2026/11/bis-suspends-affiliates-rule-until-january-10-2027.html ; Thompson Hine (Nov 2026) — https://www.thompsonhinesmartrade.com/2026/11/bis-extends-affiliates-rule-until-january-2027/ ; Global Sanctions (Nov 2026) — https://globalsanctions.com/2026/11/us-bis-extends-suspension-50-rule-coming-into-force-until-10-january-2027/
- Market data (retrieved 12 Nov 2026):
  - StockAnalysis statistics (close 11 Nov 2026) — https://stockanalysis.com/stocks/cdns/statistics/
  - StockAnalysis forecast (updated 9 Nov 2026) — https://stockanalysis.com/stocks/cdns/forecast/
  - StockAnalysis history — https://stockanalysis.com/stocks/cdns/history/
  - Yahoo Finance chart API (daily, Nov 2025–Nov 2026) — https://query1.finance.yahoo.com/v8/finance/chart/CDNS?interval=1d
  - companiesmarketcap revenue, P/E and P/S — https://companiesmarketcap.com/cadence-design-systems/revenue/ ; https://companiesmarketcap.com/cadence-design-systems/pe-ratio/ ; https://companiesmarketcap.com/cadence-design-systems/ps-ratio/
  - StockAnalysis SNPS — https://stockanalysis.com/stocks/snps/statistics/
- Industry and third party:
  - SemiAnalysis EDA primer, 21 May 2026 — https://newsletter.semianalysis.com/p/eda-market-primer
  - ESD Alliance Q2 2026, 19 Oct 2026 — https://www.prnewswire.com/news-releases/electronic-system-design-industry-posts-5-7-billion-in-revenue-in-q2-2026--esd-alliance-reports-302912151.html
  - Wilson/Siemens study, 8 Sep 2026 — https://blogs.sw.siemens.com/verificationhorizons/2026/09/08/the-2026-functional-verification-study/
  - TrendForce, 20 Jan and 3 Aug 2026 — https://www.trendforce.com/presscenter/news/20260120-12887.html ; https://www.trendforce.com/presscenter/news/20260803-13161.html
  - Empyrean 2025 annual report, 28 Apr 2026 — https://static.cninfo.com.cn/finalpage/2026-04-28/1225217315.PDF
  - Anthropic formal verification, 22 Oct 2026 — https://www.anthropic.com/research/formal-verification
- Competitor primary (via synopsys.md):
  - Synopsys Investor Day, 30 Sep 2026 — https://news.synopsys.com/2026-09-30-Synopsys-Details-Growth-Strategy-and-Long-term-Financial-Model-at-2026-Investor-Day
  - GPT-Synopsys, 30 Sep 2026 — https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence-to-Revolutionize-Chip-Design
  - Nvidia–Synopsys, 1 Dec 2025 — https://news.synopsys.com/2025-12-01-NVIDIA-and-Synopsys-Announce-Strategic-Partnership-to-Revolutionize-Engineering-and-Design
  - Synopsys HAV, 11 Mar 2026 — https://news.synopsys.com/2026-03-11-Synopsys-Introduces-Software-Defined-Hardware-Assisted-Verification-to-Enable-AI-Proliferation
  - Siemens–Nvidia, 9 Apr 2026 — https://news.siemens.com/en-us/siemens-nvidia-veloce/
  - Synopsys Q3 FY2026 call, 26 Aug 2026 — https://www.webull.com/news/15497781661541376
  - Synopsys Q4 date notice, 5 Nov 2026 — https://finviz.com/news/417651/synopsys-announces-earnings-release-date-for-fourth-quarter-and-fiscal-year-2026
