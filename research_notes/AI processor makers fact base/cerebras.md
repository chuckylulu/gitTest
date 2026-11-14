# Cerebras Systems: fact base as of 14 November 2026 (products, roadmap, financials, customers, capacity, ownership, legal, science, cross-examination)

How to read the tags. **[CO-SEC]** means Cerebras said it in an SEC filing. Audited annual statements and unaudited quarterly statements are still company-reported. **[CO]** means a Cerebras press release, blog post, web page or executive statement. **[IND: X]** means it was independently measured or stated by X. **[CUST: X]** means a customer or partner said it in its own publication. That is outside Cerebras, but the source has an interest. **[PRESS]** means a press report with named or observable sourcing, such as a stock price. **[PRESS-UNNAMED]** means a press report citing unnamed people. **[EST]** means an analyst or industry estimate. **[SECONDARY]** means an aggregator or low-confidence site, used only where nothing better was found. Inferences are my own and appear only under "Inferences". Each figure has a date or period.

Method note. The primary documents were downloaded from SEC EDGAR and read in full text. They are the 2024 S-1, the 2026 S-1, the 424B4 final prospectus, the Q1–Q3 2026 earnings 8-Ks, the Q2 and Q3 2026 10-Qs, and the EDGAR filing index. Web search was cut off partway through: the shared WebSearch budget for the turn was exhausted and the Firecrawl credits ran out. Some independent checks are therefore listed under Gaps.

---

## Q0. Status of the four unverified leads

### Takeaway
Three of the four leads are confirmed, with corrections. The fourth (the CFIUS "clearance") is misleading as worded. CFIUS let Cerebras and G42 withdraw their filing after the deal was restructured, and G42's $335M investment never closed.

### Cited Findings
- **Lead 1: "Withdrew IPO in Oct 2025 after a $1.1B Series G at $8.1B." CONFIRMED.**
  - **Withdrawal.** Cerebras filed Form RW (registration withdrawal) on **2025-10-03**. [CO-SEC] — [SEC EDGAR submissions index, Cerebras Systems CIK 0002021728, retrieved 2026-11-14](https://data.sec.gov/submissions/CIK0002021728.json)
  - **Series G.** The $1.1B Series G was announced **2025-09-30** at an **$8.1B post-money valuation**, led by Fidelity and Atreides Management. [PRESS] — [Crunchbase News, "Cerebras Systems Halts IPO…", Mary Ann Azevedo, 2025-10-06](https://news.crunchbase.com/public/ipo/cerebras-systems-halts-ipo-ai-semiconductors/)
  - **Series G terms in the prospectus.** 30,359,557 Series G shares were sold at **$36.2324/share**, about $1.1B, in multiple closings through October 2025. [CO-SEC] — [Cerebras 424B4 prospectus, filed 2026-05-14](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- **Lead 2: "OpenAI agreed in Jan 2026 to buy up to 750 MW through 2028, reported above $10B." CONFIRMED, WITH CORRECTIONS.**
  - **Announcement and press valuation.** The deal was announced **2026-01-14**. CNBC reported "over $10 billion", citing "people close to the company". [PRESS-UNNAMED] — [CNBC, "Cerebras scores OpenAI deal worth over $10 billion…", Jordan Novet & Kate Rooney, 2026-01-14](https://www.cnbc.com/2026/01/14/cerebras-scores-openai-deal-worth-over-10-billion.html)
  - **Correction 1: committed, not "up to".** The Master Relationship Agreement (MRA) was signed in **December 2025**. The 750 MW is **contractually committed** ("Committed Capacity"). OpenAI also holds an **option on 1.25 GW more** by end-2030, for up to **2.0 GW** in total. [CO-SEC] — [Cerebras 10-Q Q3 2026, filed 2026-11-12](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
  - **Correction 2: Cerebras values it at more than $20B.** Cerebras's own figure is "**more than $20 billion**". [CO-SEC] — [424B4, 2026-05-14](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm); [CO] — [Q1 2026 results release (8-K Ex. 99.1), 2026-06-23](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026044941/cbrsannouncesfinancialresu.htm)
  - **Correction 3: loan and warrant.** The deal includes a **$1.0B secured working-capital loan** from OpenAI at 6%. It also includes a **warrant for 33,445,026 non-voting Class N shares** at $0.00001 per share (details under Q4). [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
- **Lead 3: "Raised early 2026 at ~$22–23B and planned to refile for an IPO in 2026." CONFIRMED, AND OVERTAKEN BY EVENTS.**
  - **Talks at $22B.** Bloomberg reported talks at a $22B valuation on **2026-01-13**. [PRESS-UNNAMED] — [Bloomberg, "Cerebras in Discussions to Raise Funds at $22 Billion Valuation", 2026-01-13](https://www.bloomberg.com/news/articles/2026-01-13/cerebras-in-discussions-to-raise-funds-at-22-billion-valuation) (search-result listing; not opened)
  - **Series H terms.** Cerebras sold 11,394,059 Series H shares at **$89.0156/share**, about **$1.0B**, in closings through **February 2026**. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
  - **Series H valuation.** One secondary source reports a ~$23B valuation; Forge reports $22.91B post-money. [SECONDARY] — [FNEX, "Cerebras Raises $1 Billion Series H at $23B Valuation"](https://fnex.com/cerebras-raises-1-billion-series-h-at-23b-valuation/); [Forge Global, "Cerebras IPO"](https://forgeglobal.com/cerebras_ipo/)
  - **Refiling and IPO.** Cerebras refiled confidentially (DRS) on **2025-12-22** and publicly (S-1) on **2026-04-17**. The IPO priced **2026-05-13**. [CO-SEC] — [EDGAR index](https://data.sec.gov/submissions/CIK0002021728.json)
- **Lead 4: "CFIUS cleared G42's investment in about Mar 2025." MISLEADING.**
  - **What Cerebras announced.** On **2025-03-31** Cerebras said it had obtained clearance from CFIUS to sell shares to G42. CNBC reported the same day that the parties had switched G42 to non-voting shares and withdrawn their notice. [CO, via PRESS] — [CNBC (syndicated, NBC Los Angeles), "AI chipmaker Cerebras announces CFIUS clearance…", Jordan Novet, 2025-03-31](https://www.nbclosangeles.com/news/business/money-report/ai-chipmaker-cerebras-announces-cfius-clearance-a-key-step-toward-ipo/3666820/)
  - **What the 2026 prospectus says.**
    - In Q1 2025, Cerebras and G42 agreed in principle to remove G42 as a party to the voting share purchase. They also agreed to remove G42's product pricing and volume commitments.
    - On that basis, **CFIUS granted the request to withdraw the Joint Voluntary Notice on 2025-03-27**.
    - G42's $335M purchase was **not consummated by the 2025-04-15 deadline**.
    - In Q3 2025 the agreement was restated to remove G42 entirely, and the G42 commercial agreement of May 2024 "was also terminated in its entirety".

    [CO-SEC] — [424B4, notes to financial statements](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)

### Inferences
- "CFIUS cleared G42" is not an accurate summary. CFIUS never cleared a completed G42 investment. It allowed the notice to be withdrawn after the deal was restructured, and the investment then lapsed.
- The "$10B" figure (unnamed sources, January 2026) and the "$20B" figure (Cerebras, from May 2026) may describe different bases. The $20B could include pass-through data-center costs, or the full term including extensions. The disclosures do not reconcile the two.

### Gaps
- OpenAI's own January 2026 blog post could not be retrieved (HTTP 403), so I could not check whether it states a dollar value.
- The Series H lead investor is not confirmed by a primary source.

---

## Q1. Products and their stage

### Takeaway
- **Hardware in production.** Cerebras ships the CS-3, built on the WSE-3 (TSMC 5 nm, 4T transistors, 44 GB on-wafer SRAM).
- **CS-4.** Launched August 2026, it is a three-wafer rack built on the "WSE-3 Turbo". It is not a new WSE-4 die.
- **Next die.** The "WSE-5", for a CS-5 targeted at early summer 2027, is in system test. As of the sources reviewed, no product called "WSE-4" exists.
- **Business mix.** Inference cloud services are now the larger revenue line.
- **Condor Galaxy.** The G42 Condor Galaxy program has disappeared from Cerebras's 2026 disclosures, and its delivery status is unverified.

### Cited Findings
**Hardware: WSE-3 and CS-3**
- **WSE-3 specifications.** [CO] — [Cerebras press release, "Cerebras announces third-generation wafer-scale engine", 2024-03-13](https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine); [CO-SEC] — [424B4 graphic, 2026-05-14](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
  - 4 trillion transistors
  - 900,000 cores
  - 44 GB on-chip SRAM
  - 46,225 mm² of silicon
  - 21 PB/s memory bandwidth
  - 214 Pb/s fabric bandwidth
  - 125 PFLOPS peak AI compute
  - TSMC 5 nm
- **Process history.** WSE-2 was made on TSMC 7 nm and WSE-3 on TSMC 5 nm. [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
- **CS-3 system claims.** [CO] — [WSE-3 press release, 2024-03-13](https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine)
  - Twice WSE-2 performance "in the same power envelope", at the same price.
  - Clusters of up to 2,048 CS-3 systems.
  - External MemoryX of 1.5 TB, 12 TB or 1.2 PB.
  - Models of "up to 24 trillion parameters".
  - The release gives no absolute power figure in kW.
- **On-premises sales.** On-prem systems are still sold. Hardware revenue in 2025 came mainly from on-prem demand from MBZUAI. [CO-SEC] — [424B4 MD&A](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- **Export licenses.** Cerebras holds export licenses for **CS-2, CS-3 and CS-4** systems to G42 and MBZUAI in the UAE. [CO-SEC] — [10-Q Q3 2026, risk factors](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)

**CS-4: next-generation system, launched August 2026**
- **Design.** [CO] — [Cerebras blog, "Introducing Cerebras CS-4", 2026-08-18](https://www.cerebras.ai/blog/introducing-cerebras-cs-4)
  - Three "Wafer Scale Engine 3 Turbo" processors per system, on the new "Nexus" rack platform.
  - Direct liquid cooling and 2 µs wafer-to-wafer latency.
  - "First CS-4 shipments begin this quarter" (Q3 2026).
  - "Up to 30x faster than GPU systems". The stated basis is "Artificial analysis and internal benchmarking (August 2026)".
  - Up to 2x CS-3 performance and up to 10x throughput per watt versus CS-3.
  - ">1,000 tokens/s" on models above 10 trillion parameters, described as an "extrapolation from internal benchmarking".
- **Reported rack figures.** [PRESS, relaying company specs] — [DatacenterDynamics, "Cerebras unveils CS-4 rack scale solution powered by four-trillion transistor WSE-3T chip", Aug 2026](https://www.datacenterdynamics.com/en/news/cerebras-unveils-cs-4-rack-scale-solution-powered-by-four-trillion-transistor-wse-3t-chip/) (search-result summary)
  - Per wafer: 250 PFLOPS and 43.2 PB/s.
  - Per rack: 750 PFLOPS, 129.6 PB/s memory bandwidth, 7.2 Tb/s I/O.
  - Each wafer is still 4T transistors, 900k cores and 44 GB SRAM.
- **Production status.** "CS-4 will soon be in full production", as of **2026-11-12**. [CO] — [Q3 2026 results release, 2026-11-12](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm)
- **Hot Chips 2026 details.** [PRESS, largely relaying vendor claims] — [ServeTheHome, "Cerebras Talks Going Rack-Scale with Their WSEs at Hot Chips 2026", Ryan Smith, 2026-08-25](https://www.servethehome.com/cerebras-talks-going-rack-scale-with-their-wses-at-hot-chips-2026/)
  - Each CS-4 "backpack" holds up to 30 power-supply units on 30 A breakers, with input up to 277 V AC.
  - Cooling capacity is double the CS-3 backpack's.
  - The WSE-3T clock is "roughly doubled".
  - On-wafer fabric is 53 PB/s.
  - The article states no kW figure.

**Next generation (announced, not shipped)**
- **CS-5 and WSE-5.** CS-5 was previewed at Hot Chips 2026 and is "targeted for early Summer 2027", aimed at "up to 10,000 tokens per second per user". The "**Wafer Scale Engine 5** to be deployed in CS-5 is back from the fab, completed bring up and is in system test". [CO] — [Q3 2026 results release, 2026-11-12](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm)
- **CS-5 targets.** 5,000 tokens/s per user on the largest frontier models and 3 million tokens/s per MW. [CO] — [Cerebras blog, "Ultrafast Frontier Inference: Cerebras deep dive at Hot Chips 2026", Aug 2026](https://www.cerebras.ai/blog/ultrafast-frontier-inference-cerebras-deep-dive-at-hot-chips-2026) (search-result summary)
- **CS-6.** It will stack DRAM on the wafer. No date or specifications were given. [PRESS] — [Tom's Hardware, "Hot Chips 2026: Cerebras lays out the future of wafer-scale AI…", Aug 2026](https://www.tomshardware.com/tech-industry/artificial-intelligence/hot-chips-2026-cerebras-lays-out-the-future-of-wafer-scale-ai-nexus-system-architecture-triples-rack-scale-performance-cs-6-wafer-to-incorporate-stacked-dram) (headline only retrieved); [ServeTheHome, 2026-08-25](https://www.servethehome.com/cerebras-talks-going-rack-scale-with-their-wses-at-hot-chips-2026/)

**Cerebras Inference cloud**
- **Launch.** The inference service launched in 2024. [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
- **Artificial Analysis quote.** In August 2024 Artificial Analysis wrote: "Cerebras Inference is achieving the fastest speeds we have ever benchmarked." [IND: Artificial Analysis, as quoted by Cerebras] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- **Models served, with company-stated speeds:**
  - Llama‑3.3 70B: **2,457 tokens/s**, against the fastest GPU cloud provider listed at 164 tokens/s. This is the basis of the "up to 15x" claim.
  - gpt‑oss‑120B: **1,735 tokens/s**. Other providers in the same chart: 458, 241, 260 and 295 tokens/s. The vendor labels are hard to match up in the extracted chart text.
  - Qwen‑3 235B, GLM 4.7 and MiniMax M2.5 are also shown.
  - Chart source line: "Cerebras data from internal measurements on April 14, 2026. Artificial Analysis benchmark published on April 14, 2026"; 10,000 input tokens. This is mixed provenance: company plus Artificial Analysis.

  [CO-SEC] — [424B4 charts, 2026-05-14](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- **Kimi K2.6 and Gemma 4.** Kimi K2.6 (1T-parameter MoE) and Gemma 4 31B are in **enterprise trials**. Kimi K2.6 reached "approaching 1,000 tokens per second as independently measured by Artificial Analysis". [CO] — [Q1 2026 release, 2026-06-23](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026044941/cbrsannouncesfinancialresu.htm)
- **Kimi K2.6 measurement and setup.** [IND: Artificial Analysis, per VentureBeat]; set-up details [CO] — [VentureBeat, "Cerebras says its chips run a trillion-parameter AI model nearly 7 times faster than GPU clouds", Michael Nuñez, 2026-05-20](https://venturebeat.com/technology/cerebras-says-its-chips-run-a-trillion-parameter-ai-model-nearly-7-times-faster-than-gpu-clouds)
  - 981 output tokens/s, measured by Artificial Analysis. That is 6.7x the next-fastest GPU cloud.
  - The model ran on about **20 CS-3 systems**, with weights stored at 4-bit.
  - It is enterprise-only and not generally available. Pricing is in the "middle-upper range of GPU pricing", per a Cerebras spokesperson.
- **OpenAI models.** "Enabled support for OpenAI GPT‑5.6 Sol at 750 tokens per second" (Q2 2026). Codex‑Spark was co-launched at ">1,000 tokens per second" (Q1 2026). [CO] — [Q2 2026 release, 2026-08-12](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm); [Q1 2026 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026044941/cbrsannouncesfinancialresu.htm)
- **Kimi K3.1.** Cerebras was a "day-zero launch partner" for Moonshot's 2.8T-parameter Kimi K3.1, at "up to 2,000 tokens per second". [CO] — [Q3 2026 release, 2026-11-12](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm)
- **Artificial Analysis provider page (fetched 2026-11-14).** [IND: Artificial Analysis] — [Artificial Analysis, Cerebras provider page](https://artificialanalysis.ai/providers/cerebras)
  - Only gpt‑oss‑120b (high and low reasoning) is listed.
  - Blended price **$0.39 per 1M tokens** (7:2:1 cache-hit : input : output).
  - Time to first answer token 1.77 s (high) and 0.73 s (low).
  - Error rate 0.0% (high) and 1.4% (low).
  - Output speed did not render in the fetch.
- **Pricing page (fetched 2026-11-14).** It shows no per-model price table and links to the docs. It mentions a one-time $5 promotional credit and a development tier "not intended for production use". It also lists access through AWS Marketplace, OpenRouter, Hugging Face and Vercel. [CO] — [cerebras.ai/pricing](https://www.cerebras.ai/pricing)

**Condor Galaxy (with G42)**
- **2024 description.** The 2024 S-1 sold capacity "via the Condor Galaxy Cloud owned by … G42, our partner CSP". [CO-SEC] — [S-1, filed 2024-09-30](https://www.sec.gov/Archives/edgar/data/2021728/000162828024041596/cerebras-sx1.htm)
- **2026 prospectus.** A full-text search of the 2026 424B4 finds **no mention of "Condor Galaxy"**. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- **CG‑3 announcement.** CG-3 was announced on 2024-03-13: 64 CS-3 systems, 8 exaFLOPs, in Dallas, "available Q2 2024". [CO] — [Cerebras press release, "Cerebras, G42 announce Condor Galaxy 3", 2024-03-13](https://www.cerebras.ai/press-release/cerebras-g42-announce-condor-galaxy-3) (search-result summary)
- **CG‑3 on Cerebras's current site.** It is listed as "delivering 8 exaFLOPs of compute with 64 CS-3 systems". Network capacity is "16 exaFLOPs" including CG‑3. No operational status or date is given. [CO] — [cerebras.ai/ai-supercomputer, fetched 2026-11-14](https://www.cerebras.ai/ai-supercomputer)
- **Sites listed as "online" in March 2025.** Santa Clara, Stockton and Dallas. [CO] — [Cerebras press release, six new datacenters, 2025-03-11](https://www.cerebras.ai/press-release/cerebras-announces-six-new-ai-datacenters-across-north-america-and-europe-to-deliver-industry-s)

**Data centers**
- **March 2025 plan (6 new sites):** [CO] — [Cerebras press release, 2025-03-11](https://www.cerebras.ai/press-release/cerebras-announces-six-new-ai-datacenters-across-north-america-and-europe-to-deliver-industry-s)
  - Minneapolis, Q2 2025.
  - Oklahoma City, Q3 2025 ("June 2025" in the body text): run with Scale Datacenter, "over 300 CS-3", Cerebras-owned hardware.
  - Montreal, Q3 2025 ("July" in the body text): Enovum / Bit Digital, Cerebras-owned hardware.
  - Midwest/Eastern US, Q4 2025.
  - Europe, Q4 2025.
  - The "remaining" sites are jointly operated with G42.
  - Target: more than 40M Llama‑70B tokens/s, with 85% of capacity in the US. No MW figures were given.
- **May 2026.** "Currently, these data center facilities are in California, Oklahoma, and Canada." Cerebras says it has more than 100 exaflops of deployed compute. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- **August 2026.** More than **600 MW** "live and under contract for delivery by the end of 2027". [CO] — [Q2 2026 release, 2026-08-12](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm)
- **November 2026.** **700 gross MW** secured for delivery by end‑2027, plus new contracts in **Norway and Finland** (Mikkeli). Forward-looking statements mention expansion across Europe and Canada and a "first presence in South America". [CO] — [Q3 2026 release, 2026-11-12](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm)
- **Lease commitments.** As of 2026-09-30, non-cancelable data-center leases not yet commenced total about **$8.5B** in undiscounted payments, starting in 2026–2027. Another **$217.8M** was signed in Q4 2026. [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)

**Partnerships and channels (with who confirms each)**
- **Meta Llama API.** Meta: "We're excited to announce a collaboration with Cerebras and Groq"; "early experimental access … by request". Meta gave no speed figures, and the Llama API was in limited preview. [CUST: Meta] — [Meta AI blog, LlamaCon recap, 2025-04-29](https://ai.meta.com/blog/llamacon-llama-news/)
- **Perplexity Sonar.** "Powered by Cerebras inference infrastructure, Sonar runs at … 1200 tokens per second". Perplexity's own footnote adds that the API Sonar "does not yet run on Cerebras inference infrastructure". [CUST: Perplexity] — [Perplexity blog, "Meet new Sonar", 2025-02-11](https://www.perplexity.ai/hub/blog/meet-new-sonar)
- **Cognition SWE‑1.5.** Served "at up to 950 tok/s – 6x faster than Haiku 4.5 and 13x faster than Sonnet 4.5". [CUST: Cognition] — [Cognition blog, "SWE-1.5", 2025-10-29](https://cognition.com/blog/swe-1-5)
  - Cerebras signed new cloud capacity agreements with **Cognition and Lovable** in Q2 2026. [CO] — [Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm)
- **Mistral.** Mistral's own Le Chat "Flash Answers" post ("~1000 words / sec") does **not name Cerebras**. [CUST: Mistral] — [Mistral, "The all new le Chat", 2025-02-06](https://mistral.ai/news/all-new-le-chat)
- **Distribution channels.** AWS Marketplace, Microsoft Marketplace, IBM watsonx Model Gateway, Vercel AI Gateway, OpenRouter and Hugging Face. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- **AWS.** [CO] — [Q1 2026 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026044941/cbrsannouncesfinancialresu.htm); [Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm)
  - A multi-year partnership began in March 2026.
  - Disaggregated inference splits the work: AWS **Trainium 3 does prefill** and **CS-3 does decode**.
  - It is expected on Amazon Bedrock in **Q1 2027**.
- **AMD.** Disaggregated inference "in production in Q4 2026". [CO] — [Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) ServeTheHome reports the pairing is with AMD Instinct MI455X GPUs. [PRESS] — [ServeTheHome, 2026-08-25](https://www.servethehome.com/cerebras-talks-going-rack-scale-with-their-wses-at-hot-chips-2026/)
- **Oracle.** Cerebras will be available in OCI "in 2027". There is also a "cloud deal with a top three hyperscaler". [CO] — [Q3 2026 release, 2026-11-12](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm) CNBC identifies the hyperscaler as **Microsoft**, signed in October 2026, with revenue starting Q1 2027 (per Feldman). [PRESS] — [CNBC, "Cerebras pops after beating on quarterly revenue and announcing Microsoft deal", Jordan Novet, 2026-11-12](https://www.cnbc.com/2026/11/12/cerebras-systems-cbrs-q3-earnings-report-2026.html)

### Inferences
- **No WSE-4.** The naming went WSE‑3 → WSE‑3 Turbo (in CS‑4) → WSE‑5 (in CS‑5). Third-party pages that describe a "WSE‑4" do not match any Cerebras product name found in these sources.
- **Per-wafer resources are unchanged in CS-4.** Each CS‑4 wafer has the same transistor count, core count and 44 GB SRAM as the WSE‑3. The claimed gains come from clock speed, power, I/O and system design, not from more memory per wafer.
- **Condor Galaxy.** The 2026 prospectus drops "Condor Galaxy", and in March 2025 Cerebras listed the CG-1/2/3 sites as "online". Together these suggest the program ended as a separate offering. Whether all three systems reached full planned scale is not independently confirmed.

### Gaps
- Independent confirmation of CG‑1, CG‑2 and CG‑3 delivery dates, and of what happened to the 2024 plan for more Condor Galaxy systems.
- MW per site and actual go-live dates for Oklahoma City, Montreal, Minneapolis and the European sites.
- Per-model list prices for Cerebras Inference.
- CS-3 and CS-4 power in kW.
- Notion, IBM and Hugging Face specifics beyond channel listings. Mistral's confirmation that it uses Cerebras.

---

## Q2. Roadmap and milestones, with dates (met, slipped or pending)

### Takeaway
- **IPO.** Planned for late 2024, it slipped about 19 months (the CFIUS/G42 overhang, then a withdrawal) and was completed on 2026-05-14.
- **Data centers.** The 2025 expansion plan was partly met. The scope of the March 2025 site list cannot be fully confirmed.
- **OpenAI capacity.** Delivery is behind contract, with service credits accruing since 2026-10-01.
- **CS-4.** Shipping started in Q3 2026, as promised.
- **CS-5.** Pending, with a summer 2027 target.

### Cited Findings
**IPO timeline** [CO-SEC] — [EDGAR index](https://data.sec.gov/submissions/CIK0002021728.json)
- Confidential DRS filed **2024-06-17**.
- Public S‑1 filed **2024-09-30**, planning a Nasdaq listing under the ticker "CBRS". [CO-SEC] — [S-1 2024](https://www.sec.gov/Archives/edgar/data/2021728/000162828024041596/cerebras-sx1.htm)
- CFIUS notice filed July 2024. The notice-withdrawal request was granted **2025-03-27**. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- RW (withdrawal) filed **2025-10-03**. [CO-SEC] — [EDGAR index](https://data.sec.gov/submissions/CIK0002021728.json)
  - Renaissance Capital estimated the withdrawn deal at ~$800M. [EST] — [Renaissance Capital, IPO withdrawal note, Oct 2025](https://www.renaissancecapital.com/IPO-Center/News/113984/ai-focused-chip-developer-cerebras-systems-withdraws-estimated-800-million) (search-result listing)
- Feldman's explanation: withdrawal was "to re-file with updated financials"; "the business has improved in meaningful ways"; not explaining it at the time "was a mistake". [CO, via PRESS] — [The Register, Tobias Mann, 2025-10-07](https://theregister.com/2025/10/06/cerebras_ipo_rest)
- New confidential DRS **2025-12-22**, DRS/A **2026-03-31**, public S‑1 **2026-04-17**, S‑1/As **2026-05-04** and **2026-05-11**, effectiveness **2026-05-13**. [CO-SEC] — [EDGAR index](https://data.sec.gov/submissions/CIK0002021728.json)
- **Pricing.** Priced **2026-05-13** at **$185**. 30,000,000 Class A shares, Nasdaq Global Select, ticker **CBRS**. Trading began 2026-05-14 and the deal closed 2026-05-15. A 4.5M-share over-allotment option was granted. [CO] — [Cerebras press release, "Cerebras Systems announces pricing of initial public offering", 2026-05-13](https://www.cerebras.ai/press-release/cerebras-systems-announces-pricing-of-initial-public-offering)
  - **Underwriters.** Morgan Stanley, Citigroup, Barclays and UBS led. Mizuho and TD Cowen were bookrunners.
  - **Price versus range.** Priced $25 above the top of a raised range. [PRESS] — [IPOScoop, "Cerebras (CBRS) prices IPO at $185"](https://www.iposcoop.com/the-ipo-buzz-cerebras-cbrs-prices-ipo-at-185-25-above-range-2/) (search-result summary)
- **Proceeds.** "$6.4 billion in gross proceeds", described as the "largest semiconductor IPO of all time". [CO] — [Q1 2026 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026044941/cbrsannouncesfinancialresu.htm) Net IPO proceeds after underwriting discounts were **$6,232.5M**. [CO-SEC] — [10-Q Q3 2026, cash-flow statement](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
- **First day.** Opened at $350, peaked at $386 intraday and closed at $311.07 (+68%). Market cap was about $95B at the close. CNBC called it the largest US tech IPO since Uber in 2019. [PRESS] — [CNBC, "Cerebras pops 68% in Nasdaq debut…", Jordan Novet, 2026-05-14](https://www.cnbc.com/2026/05/14/cerebras-cbrs-stock-trade-nasdaq-ipo.html)

**After the IPO**
- **Insider sales.** Feldman and Lie sold more than $240M of shares between 2026-08-20 and 2026-09-25.
- **Lockup releases.** Staged releases began 2026-08-19, with up to 14.6M shares every two weeks. Up to 19.4M shares were released on 2026-09-30.
- **Price on 2026-10-02.** The stock closed at **$166.43**, a post-IPO low at the time, with market cap just over $39B.

[PRESS] — [CNBC, "Cerebras stock hits post-IPO low…", Isabel O'Brien, 2026-10-02](https://www.cnbc.com/2026/10/02/cerebras-stock-hits-post-ipo-low-on-nvidia-pressure-lockup-expiration.html)
- **Lockup expiry and November price.** The main lockup expired around **2026-11-09 or 11-10**; sources differ on the exact date. The stock was about **$97.75** (−47% from the IPO price) by 2026-11-12. [SECONDARY] — [FinanceFeeds, "Cerebras lock-up expires with CBRS 49% below $185 IPO price", Nov 2026](https://financefeeds.com/cbrs-stock-cerebras-lock-up-expires-ahead-of-nov-12-q3-results/) (search-result summary)
- **2026-11-13.** Shares rose about 7% (CNBC). GuruFocus reported +11.7% to $109.19 at 9:53 a.m. ET. [PRESS] — [CNBC, 2026-11-12, updated 2026-11-13](https://www.cnbc.com/2026/11/12/cerebras-systems-cbrs-q3-earnings-report-2026.html); [GuruFocus, 2026-11-13](https://www.gurufocus.com/news/9198095/cerebras-stocks-jump-1170-after-raising-outlook-and-confirming-microsoft-cloud-deal) (search-result summary)

**Promises in the 2024 S-1 and what happened to them**
- **G42 commitments.** G42 committed to: [CO-SEC] — [S-1 2024](https://www.sec.gov/Archives/edgar/data/2021728/000162828024041596/cerebras-sx1.htm)
  - buy **$1.43B** of systems and services, prepaid before **2025-02-28**;
  - buy **$335M** of Series F‑2 shares by **2025-04-15**;
  - if it made large purchases ($500M–$5B), receive an option on more stock at a 17.5% discount.
- **Outcome: not met, terminated.** The share purchase was not completed. The May 2024 agreement was "terminated in its entirety" and the option was terminated, with G42 removed in Q3 2025. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)

**2025 data-center expansion (the March 2025 plan)**
- **Partly met.** By May 2026, Cerebras facilities were in California, Oklahoma and Canada. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- **Europe.** European capacity is under contract (Norway and Finland) as of November 2026. [CO] — [Q3 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm)
- **40M tokens/s target.** "Serve over 40 million tokens per second by the end of 2025" (Cerebras web page). [CO] — [cerebras.ai/ai-supercomputer](https://www.cerebras.ai/ai-supercomputer) I found no audited or independent confirmation that this was reached.

**Condor Galaxy schedule**
- CG‑3 was "available Q2 2024" per the March 2024 release. Its delivery date is unverified.

**OpenAI capacity: behind schedule**
- **Status at 2026-09-30.** "Without adjustment for any excused delays … we delivered less capacity to OpenAI than the quantity contemplated by the MRA". Delays "may continue through a portion of 2027".
- **Service credits.** "Service credits commenced accruing as of October 1, 2026".
- **Termination exposure.** Capacity terminable in 2026 is expected to be **less than 5%** of committed capacity.

[CO-SEC] — [10-Q Q3 2026, risk factors](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)

**Products**
- CS‑4 shipments began in Q3 2026, as promised in August 2026. "Full production" is still pending as of 2026-11-12. [CO] — [CS-4 blog](https://www.cerebras.ai/blog/introducing-cerebras-cs-4); [Q3 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm)

**Scheduled, not yet happened (as of 2026-11-14)** [CO] — [Q2 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm); [Q3 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm); [CNBC 2026-11-12](https://www.cnbc.com/2026/11/12/cerebras-systems-cbrs-q3-earnings-report-2026.html)
- Investor events: TomorrowX Summit on 2026-11-17 and the Barclays conference on 2026-12-09.
- AMD disaggregated inference in production: Q4 2026.
- Q4 2026 core revenue guidance: $310–330M.
- AWS Bedrock availability: Q1 2027.
- Microsoft revenue starts: Q1 2027.
- OCI availability: 2027.
- CS‑5: early summer 2027.
- 700 MW delivered: by end‑2027.
- "Triple revenue in 2027".

### Inferences
- Measured from the first public S-1 (2024-09-30) to the listing (2026-05-14), the IPO took about 19.5 months.
- The OpenAI delays and service credits contrast with the press release's "exceeded our guidance across the board". Both can be true: guidance covers revenue and margins, while the MRA covers capacity delivery. The release does not mention the shortfall, which is disclosed only in the 10-Q.

### Gaps
- The precise 2024 S-1 "use of proceeds" promises were not extracted.
- Which of the six March 2025 sites went live, and when, is not independently verified.

---

## Q3. Financials: S-1 figures, later filings, funding and debt

### Takeaway
- **Revenue growth.** $24.6M (2022) → $78.7M (2023) → $290.3M (2024) → $510.0M (2025) → $584.3M in 9M 2026.
- **GAAP results swing.** They are driven by large non-cash items: a G42 forward-contract liability, IPO stock compensation and customer-warrant amortization.
- **Losses in 2026.** Large GAAP losses after the IPO (9M 2026 net loss $625.8M). Company "core" (non-GAAP) results are near breakeven.
- **Liquidity and obligations.** About $7.8B of liquidity at 2026-09-30, against ~$8.5B of data-center leases not yet commenced and an $829M OpenAI loan balance.

### Cited Findings
**2024 S-1 figures** (period-end values; amounts in USD) [CO-SEC] — [S-1, filed 2024-09-30](https://www.sec.gov/Archives/edgar/data/2021728/000162828024041596/cerebras-sx1.htm)

| Period | Revenue | Gross margin | Net loss | Cash and investments | G42 share of revenue |
|---|---|---|---|---|---|
| FY2022 | $24.6M | 11.7% | $177.7M | $26.1M cash + $199.3M investments (2022-12-31) | Not given; three customers were 17%, 15% and 13% |
| FY2023 | $78.7M | 33.5% | $127.2M | $34.8M cash + $117.6M investments (2023-12-31) | **83%** |
| H1 2024 | $136.4M (H1 2023: $8.7M) | 41.1% | $66.6M (H1 2023: $77.8M) | $90.9M cash + $263.0M restricted cash + $118.6M investments (2024-06-30) | **87%** |

- G42 also made a **$300M prepayment** under an April 2024 agreement. A **$178.7M** G42 purchase order followed in July 2024.

**Annual figures from the 2026 prospectus** [CO-SEC] — [424B4, filed 2026-05-14](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- **FY2024**
  - Revenue **$290.3M**; gross margin **42.3%**.
  - GAAP net loss **$481.6M**, including a $401.3M fair-value charge on the G42 forward-contract liability.
  - Non-GAAP net loss $21.8M.
  - G42 was **85%** of revenue.
- **FY2025**
  - Revenue **$510.0M** (+76%): hardware $358.4M and cloud/services $151.6M.
  - Gross margin **39.0%**.
  - GAAP net income **$237.8M**, including a **$363.3M gain** when the G42 forward contract was extinguished.
  - Net income attributable to common shareholders **$87.9M**; non-GAAP net loss **$75.7M**.
  - **MBZUAI 62%** and **G42 24%** of revenue.
  - By region: EMEA $322.2M; US $187.6M.
  - Remaining performance obligations (RPO) were **$24.6B** at 2025-12-31, "a significant amount" from OpenAI.
  - 708 employees at 2025-12-31.
- **Material weaknesses** in internal control over financial reporting were identified for 2024 and 2025. They relate to accounting expertise (revenue, inventory, data-center assets, equity) and IT general controls.

**2026 quarterly results**
- **Q1 2026** (reported 2026-06-23): [CO] — [Q1 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026044941/cbrsannouncesfinancialresu.htm)
  - Revenue **$193.4M** (+94% YoY); GAAP gross margin 45%.
  - GAAP net loss **$14.0M**.
  - Core revenue $191.3M.
  - Cash and investments $3.3B.
- **Q2 2026** (reported 2026-08-12): [CO-SEC] — [10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056357/cbrs-20260630.htm); [CO] — [Q2 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm)
  - Revenue **$180.1M** (+74%); GAAP gross margin 14%.
  - Operating loss $477.2M; net loss **$450.5M**. Q2 2025 had net income of $309.5M because of the forward-contract gain.
  - Core revenue $209.9M (+103%); core gross margin 41%.
  - RPO **$25.4B**.
- **Q3 2026** (reported 2026-11-12): [CO] — [Q3 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm); [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
  - Revenue **$210.8M** (+55%): hardware $68.9M (Q3 2025: $96.8M) and cloud/services $141.9M (+265%).
  - GAAP gross margin **20.0%**: hardware 11.0%, cloud 24.3%.
  - Operating loss $224.1M; net loss **$161.2M** (−$0.67 per share).
  - Core revenue $230.9M (+70%); core gross margin 41%; core net income $29.8M.
  - RPO **$26.1B**. Recognition timing: ~33% within 24 months, 44% in months 25–48, the rest after.
- **Nine months 2026** [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
  - Revenue $584.3M; net loss $625.8M.
  - Stock-based compensation $541.7M.
  - Operating cash flow −$388.9M; capital expenditure $1,046.1M.
  - Accumulated deficit **$1.53B** at 2026-09-30.
- **Guidance (2026-11-12).** FY2026 core revenue raised to **$940–960M**, from $880–890M in August and $855–865M in June. 2027 revenue is expected to "triple". [CO] — [Q3 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm); [Q2 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm); [Q1 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026044941/cbrsannouncesfinancialresu.htm)
- **Analyst consensus (LSEG), from CNBC 2026-11-12.** [EST: LSEG consensus via CNBC] — [CNBC, 2026-11-12](https://www.cnbc.com/2026/11/12/cerebras-systems-cbrs-q3-earnings-report-2026.html)
  - Q3 core revenue expected $214.7M; actual $230.9M.
  - Q4 core revenue expected $271M, against guidance of $310–330M.
  - 2027 revenue expected $2.92B; "triple" implies about $2.85B.

**How "core" revenue differs from GAAP revenue**
- Core revenue excludes pass-through data-center revenue and adds back customer-warrant amortization.
- Customer-warrant assets were **$1.09B** at 2026-09-30 ($140.2M current and $951.8M non-current). They reduce GAAP revenue as they amortize: **$82.7M** in 9M 2026.

[CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)

**Balance sheet and debt at 2026-09-30** [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
- Cash **$3,074.8M**, restricted cash $444.0M and investments **$4,286.0M**. The company states liquidity of $7.8B.
- **OpenAI working-capital loan**
  - $1,004.6M was received in January 2026; $829.1M is outstanding after $175.5M of non-cash credits.
  - Interest is 6% and can be waived. It is secured by a lockbox account and matures no later than 2032-12-31.
  - Repayment is expected through service credits.
  - The loan can be accelerated if the MRA is terminated for reasons other than an OpenAI breach.
- **Revolving credit facility**
  - Morgan Stanley Senior Funding, signed 2026-04-14. It started at $250M, for letters of credit only, and rose to **$850M** on 2026-06-17 for general use.
  - It matures 2031-04-14 and requires minimum liquidity of $150M. It was **undrawn**.
- Operating lease liabilities $621.1M, plus the ~$8.5B of leases not yet commenced.

**Funding rounds**
- **Series F (Oct–Dec 2021).** 9,168,419 shares at **$27.7448**, **$254.4M** in total. G42 bought about 1.4M shares (~$40.0M, about 1% ownership) in November 2021. [CO-SEC] — [S-1 2024](https://www.sec.gov/Archives/edgar/data/2021728/000162828024041596/cerebras-sx1.htm)
- **Series F‑1 (Jul–Sep 2024).** **$85.0M** at $14.66 per share, including $45.0M from Alpha Wave. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- **Series G (Sep–Oct 2025).** About **$1.1B** at $36.2324 per share. Fidelity put in $700M, Alpha Wave $45M and Benchmark $25M. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm) The valuation was **$8.1B**. [PRESS] — [Crunchbase News, 2025-10-06](https://news.crunchbase.com/public/ipo/cerebras-systems-halts-ipo-ai-semiconductors/) Tiger Global, Valor and 1789 Capital also participated. [PRESS] — Verdict/Crunchbase search summaries, e.g. [Verdict](https://www.verdict.co.uk/ai-chipmaker-cerebras-withdraws-stock-market/) (not opened)
- **Series H (Jan–Feb 2026).** About **$1.0B** at $89.0156 per share. Benchmark put in $225M, Fidelity $100M and Alpha Wave $100M. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm) The valuation was about $23B. [SECONDARY] — [FNEX](https://fnex.com/cerebras-raises-1-billion-series-h-at-23b-valuation/)
- **Employee tender offer (December 2025).** 2,156,765 shares bought back at $36.2324, $78.1M in total. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- **Total raised before Series G.** About $1.8B since 2016, per Crunchbase data. [PRESS] — [Crunchbase News, 2025-10-06](https://news.crunchbase.com/public/ipo/cerebras-systems-halts-ipo-ai-semiconductors/)

### Inferences
- **Dollar revenue by customer, derived from the disclosed percentages:**
  - FY2025: MBZUAI about $316M; G42 about $122M.
  - FY2024: G42 about $247M.
  - 9M 2026: MBZUAI about $263M; OpenAI $146.8M (stated); G42 about $53M.
- **G42's $1.43B commitment.** It allowed purchases through third parties under commercial agreements with G42. MBZUAI's 2025 hardware purchases may have been, in effect, the channel for part of that demand. The filings do not say so explicitly.
- **GAAP gross margin fell in 2026** (45% in Q1 → 14% in Q2 → 20% in Q3), while core margin stayed around 41%. The gap comes from IPO-related stock compensation, customer-warrant amortization and data-center start-up costs.

### Gaps
- The Q1 2026 10-Q (filed 2026-06-24) was not reviewed in detail.
- The size and terms of any new debt financing that Feldman said was being evaluated on 2026-11-12. [PRESS] — [CNBC](https://www.cnbc.com/2026/11/12/cerebras-systems-cbrs-q3-earnings-report-2026.html)

---

## Q4. Customers and contracts: who is bound and who is only announced

### Takeaway
- **Concentration shifted, it did not shrink.** In 9M 2026, MBZUAI, OpenAI and G42 together were about 79% of revenue: MBZUAI 45% (a G42 related party), OpenAI 25% and G42 9%.
- **OpenAI is the main contract.** It is binding but performance-conditioned: 750 MW committed, a $1B loan and a warrant over 33.4M shares.
- **Hyperscalers.** AWS is a contract with a warrant. Microsoft is signed but its terms are undisclosed. Oracle is announced.

### Cited Findings
**Revenue concentration by period** [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm); [10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056357/cbrs-20260630.htm)

| Period | MBZUAI | G42 | OpenAI |
|---|---|---|---|
| Q3 2026 | **38%** (Q3 2025: 70%) | **7%** (Q3 2025: 14%) | **34%** |
| 9M 2026 | **45%** (9M 2025: 56%) | **9%** (9M 2025: 30%) | **25%** |
| Q2 2026 | 34% | 9% | Not stated |
| H1 2026 | 49% | 10% | Not stated |

- G42 and MBZUAI are treated as **related parties of each other** under ASC 850. Two customers made up 80% of accounts receivable at 2026-09-30.

**OpenAI Master Relationship Agreement (binding)** [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm); [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
- **Term.** Signed December 2025. 750 MW of Committed Capacity is deployed in tranches over **2026–2028**. Each tranche runs **3–4 years**, extendable by OpenAI to 5 years.
- **Option.** OpenAI can buy **1.25 GW more** by 2030, up to 2.0 GW in total.
- **Delivery conditions.** Capacity must be delivered across specified numbers of data centers on time-based milestones. Shortfalls trigger service credits, day-for-day shortening of the term, and termination rights after 90 days.
- **Revenue so far.** **$72.4M** in Q3 2026 and **$146.8M** in 9M 2026.
- **Warrant: 33,445,026 Class N shares at $0.00001, in three vesting blocks.**
  - 4,459,337 shares vested in January 2026, when the loan was funded.
  - 5,574,171 shares vested in **June 2026**, on market cap above $40B or certain fee payments.
  - 23,411,518 shares vest on capacity-delivery dates, including the optional extra capacity.
  - Exercised so far: 10,033,508 shares by 2026-09-30.
  - Expiry: 2035-12-24 at the latest.
  - Fair value at grant: $82.02 per share.
  - The warrant fully vests only if OpenAI buys the full 2 GW.
- **Other terms.** Plus the $1.0B loan (see Q3). OpenAI and Cerebras also agreed to co-design future models for future Cerebras hardware.
- **OpenAI statements.** [PRESS] — [CNBC, 2026-01-14](https://www.cnbc.com/2026/01/14/cerebras-scores-openai-deal-worth-over-10-billion.html); [CNBC, 2026-10-02](https://www.cnbc.com/2026/10/02/cerebras-stock-hits-post-ipo-low-on-nvidia-pressure-lockup-expiration.html)
  - Sachin Katti: "Cerebras adds a dedicated low-latency inference solution to our platform."
  - Sam Altman, October 2026: "Cerebras is a close partner, and we have a deep engagement pushing on the frontiers of speed."

**G42 and MBZUAI**
- **G42 equity since 2025.** Instead of the $335M purchase, G42 received warrants:
  - **1,857,516** Class N shares at $0.01 (December 2025; exercised January 2026; $82.02 per share fair value);
  - **1,655,975** Class N shares at $0.01 (April 2026; exercised April 2026; $90.23 per share fair value).

  [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
- **Exports.** CS-2, CS-3 and CS-4 exports to G42 and MBZUAI are licensed, with "rigorous security and compliance obligations". [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)

**AWS (binding commercial arrangement, with a warrant)**
- **Warrant.** Issued June 2026 to Amazon.com NV Investment Holdings for **2,696,678** Class N shares at **$100**. 269,668 shares vested immediately; the rest vest on AWS payment thresholds within 5 years. It expires 2033-06-19. [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
- **Partnership.** Multi-year, announced March 2026. [CO] — [Q1 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026044941/cbrsannouncesfinancialresu.htm)

**Microsoft, Oracle and other hyperscalers**
- **Microsoft.** "An important cloud deal with a top three hyperscaler. More will be shared next year." [CO] — [Q3 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm) CNBC: it is Microsoft, signed in October 2026, with no terms disclosed. [PRESS] — [CNBC, 2026-11-12](https://www.cnbc.com/2026/11/12/cerebras-systems-cbrs-q3-earnings-report-2026.html)
- **Oracle OCI.** Availability in 2027 (announced). [CO] — [Q3 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm)

**Other named customers**
- **Contracts or customers named by Cerebras.**
  - Cognition and Lovable have cloud capacity agreements (Q2 2026).
  - Block, Figma, AlphaSense, GSK and CrowdStrike are named as customers (Q2 2026).
  - Bilt was announced as a customer (Q3 2026).

  [CO] — [Q2 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm); [Q3 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm)
- **Training customers.** "Hardware and models we've trained for G42, MBZUAI, GlaxoSmithKline, Sandia National Laboratory, the U.S. Department of Defense". [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- **GSK.** A prospectus case study says GSK trained epigenomics models "10x faster than GPUs" with "120x more data". [CO-SEC, presented as a customer testimonial] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- **Customer-published.** Meta (Llama API experimental access, 2025-04-29), Perplexity (Sonar, 2025-02-11) and Cognition (SWE-1.5, 2025-10-29). Sources are listed under Q1.
- **National labs.** Sandia, LLNL and LANL ran molecular dynamics on the WSE‑2 (2024). [IND: LLNL] — [LLNL, 2024-11-20](https://www.llnl.gov/article/52081/nnsa-researchers-break-molecular-dynamics-timescale-barrier-worlds-largest-chip) NETL co-authored the SC20 stencil paper on the CS‑1. [IND: peer-reviewed SC20] — [arXiv 2010.03660, 2020-10-07](https://arxiv.org/abs/2010.03660)

### Inferences
**How binding each relationship is, as disclosed:**
- **Binding with financial terms:** OpenAI (MRA, loan and warrant) and AWS (warrant tied to payments).
- **Signed, terms undisclosed:** Microsoft.
- **Announced or planned:** Oracle OCI (2027), AMD disaggregated inference (Q4 2026) and AWS Bedrock (Q1 2027).
- **Cerebras-reported contract counterparties, no amounts:** Cognition and Lovable.
- **Customers or partners confirmed in their own publications:** Meta, Perplexity and Cognition.

**Ownership arithmetic.** With 243.0M total shares on 2026-11-05, OpenAI's exercised 10.03M Class N shares are about **4.1%** of shares outstanding. The full 33.4M warrant would be about **12.5%**, counting the unvested shares as issued. G42's 3.51M warrant shares are about **1.4%**.

### Gaps
- Microsoft deal value, MW and term. Oracle terms.
- Independent confirmation of the AstraZeneca, Mayo Clinic, Argonne and Notion relationships. They were not found in the filings, and search was not possible.
- MBZUAI contract terms (purchase orders or a framework agreement).

---

## Q5. Capacity: TSMC, manufacturing, data centers and tokens per second

### Takeaway
- **Wafers.** TSMC is the only wafer source, with no formal long-term allocation, per the November 2026 10-Q.
- **Assembly.** Contract manufacturing at Flex, Sanmina and Rocket EMS is scaling more than 10x in 2026.
- **Data centers.** 700 MW is contracted for delivery by end-2027.
- **Tokens per second.** The capacity figures are company projections, not audited or independently measured.

### Cited Findings
- **TSMC.** "We depend on one third-party foundry, … TSMC". "We have no formalized long-term supply or allocation commitments from TSMC". [CO-SEC] — [10-Q Q3 2026, filed 2026-11-12](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm); also in the [424B4, 2026-05-14](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- **Supply chain, as of August 2026.**
  - "Secured TSMC wafer supply needed for continued growth."
  - "We do not use HBM memory, CoWoS packaging or 3nm fabrication technology."
  - New factory lines at Flex, Sanmina and Rocket EMS, with manufacturing capacity up more than 10x in 2026.

  [CO] — [Q2 release, 2026-08-12](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm)
- **Exit rate.** Cerebras expects to exit 2026 with "more than 10x manufacturing capacity versus beginning of the year" and plans more factories in 2027. [CO] — [Q3 release, 2026-11-12](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm)
- **Supplier concentration.** Two suppliers were 12% and 11% of purchases in 9M 2026. [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
- **Data-center MW.**
  - More than 600 MW live plus contracted, as of August 2026. [CO] — [Q2 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm)
  - 700 gross MW for delivery by end-2027, as of November 2026. Cerebras says it is "among the largest non-hyperscaler AI clouds". [CO] — [Q3 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm)
- **Analyst view.** A Morgan Stanley note reportedly says most of the new capacity comes online from mid-2027. [EST: Morgan Stanley, via search summary] — [GuruFocus, 2026-11-13](https://www.gurufocus.com/news/9198095/cerebras-stocks-jump-1170-after-raising-outlook-and-confirming-microsoft-cloud-deal) (not opened)
- **Tokens-per-second claims (all company):**
  - Target of more than 40M Llama‑70B tokens/s across the new sites (March 2025). [CO] — [press release, 2025-03-11](https://www.cerebras.ai/press-release/cerebras-announces-six-new-ai-datacenters-across-north-america-and-europe-to-deliver-industry-s)
  - Disaggregated inference "increasing up to 5x the number of tokens that data centers can deliver". [CO] — [Q3 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm)
  - CS‑5 target of 3M tokens/s per MW. [CO] — [Hot Chips 2026 blog](https://www.cerebras.ai/blog/ultrafast-frontier-inference-cerebras-deep-dive-at-hot-chips-2026) (search-result summary)
  - CS‑4 "10x more token capacity" (internal benchmarks and projections). [CO] — [CS-4 blog](https://www.cerebras.ai/blog/introducing-cerebras-cs-4)
- **Capital spending.** Property and equipment purchases were $1,046.1M in 9M 2026, against $301.1M in 9M 2025. [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)

### Inferences
- The August 2026 "secured TSMC wafer supply" claim and the November 2026 10-Q's "no formalized long-term supply or allocation commitments" can both be true: there may be purchase orders without a long-term allocation agreement. They give different impressions of how firm supply is.
- The 700 MW is "gross" capacity "for delivery by end-2027". The OpenAI tranches are behind schedule (see Q2), so contracted MW is not the same as energized MW.

### Gaps
- Energized (live) MW today, as opposed to contracted MW.
- Wafer start volumes, yield and units shipped.
- Any independent audit of fleet-wide tokens per second.

---

## Q6. Ownership and key people

### Takeaway
- **Control.** The founders and pre-IPO holders control the company through high-vote Class B shares: 20 votes each, 99.2% of voting power at the IPO.
- **Large investors.** Fidelity, Benchmark, Foundation Capital, Eclipse and Alpha Wave held 5% or more before the IPO.
- **Strategic holders.** G42, OpenAI and AWS hold or can acquire only **non-voting Class N** shares.

### Cited Findings
**Share classes and voting** [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- Class A has 1 vote, Class B 20 votes and Class N none. Class B was to hold "approximately **99.2%** of the voting power" immediately after the IPO.
- The charter's "Founders" are **Andrew D. Feldman, Sean Lie, Jean-Philippe Fricker and Michael James**. Class B converts to Class A six months after no Founder remains an employee or director.

**Shares outstanding on 2026-11-05** [CO-SEC] — [10-Q Q3 2026, cover page](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
- Class A 160,084,168; Class B 69,203,688; Class N 13,715,508.
- At the IPO, 185,110,345 Class B shares were expected to be outstanding. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)

**Ownership as of 2026-03-31** [CO-SEC] — [424B4, Principal Stockholders](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)

| Holder | Before IPO, % of Class B (≈ voting power) | Before IPO, % of total outstanding | After IPO, % of total outstanding (excluding over-allotment) |
|---|---|---|---|
| Fidelity | 11.0% | 10.9% | 9.4% |
| Benchmark | 9.5% | 9.4% | 8.1% |
| Foundation Capital | 8.3% | 8.2% | 7.0% |
| Eclipse | 7.3% | 7.2% | 6.2% |
| Alpha Wave | 6.5% | 6.4% | 5.6% |
| Andrew Feldman | 5.4% | 5.3% | 4.6% (5.4% of voting power after the IPO) |
| Sean Lie | 2.9% | 2.8% | 2.4% |
| All executive officers and directors | 24.9% | 21.0% | 18.5% |

- G42 does not appear as a holder of 5% or more.

**Schedule 13D/13G filings after the IPO**
The percentages are reported as % of **Class A**, which under Rule 13d-3 counts the filer's convertible Class B. They are **not** % of total equity. Values were read from the filings' XML; the links go to EDGAR filing folders. [IND: SEC filings by holders]

| Filer | Form | Filed | Reported % of Class A |
|---|---|---|---|
| Eclipse | 13D | 2026-05-22 | Not stated |
| Tiger Global | 13G | 2026-05-22 | 8.69% |
| JPMorgan Chase | 13G | 2026-06-04 | 10.1% |
| FMR (Fidelity) | 13G | 2026-06-05 | 46.6% |
| Jane Street | 13G | 2026-08-13 | 5.1% |
| Benchmark | 13G | 2026-08-14 | 7.7% |
| Andrew Feldman | 13G | 2026-08-14 | 9.2% |
| Altimeter | 13G | 2026-08-14 | 6.2% |
| Foundation Capital | 13G | 2026-08-14 | 12.2% |
| Atreides | 13G | 2026-08-14 | 10.7% |

Filing folders: [Eclipse](https://www.sec.gov/Archives/edgar/data/2021728/000119312526237003/); [Tiger Global](https://www.sec.gov/Archives/edgar/data/2021728/000091957426003680/); [JPMorgan](https://www.sec.gov/Archives/edgar/data/2021728/000001961726000234/); [FMR](https://www.sec.gov/Archives/edgar/data/2021728/000031506626001423/); [Jane Street](https://www.sec.gov/Archives/edgar/data/2021728/000159588826000104/); [Benchmark](https://www.sec.gov/Archives/edgar/data/2021728/000110465926097224/); [Feldman](https://www.sec.gov/Archives/edgar/data/2021728/000149315226038435/); [Altimeter](https://www.sec.gov/Archives/edgar/data/2021728/000154161726000009/); [Foundation Capital](https://www.sec.gov/Archives/edgar/data/2021728/000164507626000004/); [Atreides](https://www.sec.gov/Archives/edgar/data/2021728/000177781326000008/)

**Earlier investors**
- Altimeter invested $10M in Series F (2021). Brad Gerstner was a director at the time. [CO-SEC] — [S-1 2024](https://www.sec.gov/Archives/edgar/data/2021728/000162828024041596/cerebras-sx1.htm)

**G42's stake**
- About 1% from Series F in November 2021: about 1.4M shares. [CO-SEC] — [S-1 2024](https://www.sec.gov/Archives/edgar/data/2021728/000162828024041596/cerebras-sx1.htm)
- 3,513,491 non-voting Class N shares from warrants exercised in January and April 2026. [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
- The planned $335M non-voting stake never closed. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)

**Executives** [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- Andrew D. Feldman: co-founder, CEO, President and director.
- Sean Lie: co-founder and CTO.
- **Robert (Bob) Komin**: CFO and Treasurer since March 2024.
- Dhiraj Mallick: COO since September 2023.

**Board: six members as of May 2026** [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)

| Director | Since | Affiliation |
|---|---|---|
| Andrew Feldman | — | CEO |
| Paul Auvil | July 2024 | — |
| Elena Donio | April 2026 | — |
| Lior Susan | April 2023 | Eclipse |
| Steve Vassallo | May 2016 | Foundation Capital |
| Eric Vishria | May 2016 | Benchmark |

**Insider trading plans and sales**
- **Plans.** Director plans under Rule 10b5‑1: Vassallo adopted one on 2026-08-24 (230,000 shares) and Susan on 2026-08-28 (376,714 shares). [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
- **Sales.** Feldman and Lie sold more than $240M from 2026-08-20 to 2026-09-25. [PRESS] — [CNBC, 2026-10-02](https://www.cnbc.com/2026/10/02/cerebras-stock-hits-post-ipo-low-on-nvidia-pressure-lockup-expiration.html)
- **Filing counts.** EDGAR shows 62 Form 4 and 15 Form 144 filings for the company to 2026-11-14. [CO-SEC] — [EDGAR index](https://data.sec.gov/submissions/CIK0002021728.json)

### Inferences
- **Voting power on 2026-11-05.** Class B fell from about 185M shares at the IPO to 69.2M, presumably through conversion and sales after lockup. At 20 votes per share against 160.1M Class A votes, Class B still holds about **89.6%** of the vote.
- **Market capitalization.** Using 243.0M total shares: about $23.8B at $97.75 (2026-11-12) and about $26.5B at $109.19 (2026-11-13 intraday).

### Gaps
- **Gary Lauterbach** is not mentioned in either S-1 or in the prospectus. His current role and holdings were not found.
- Whether Fricker and Michael James are still employed. (Michael James is a co-author of the 2024 SC24 MD paper.)
- G42's current total holding, including the 2021 Series F shares and any sales.

---

## Q7. Legal and regulatory matters

### Takeaway
- **CFIUS.** The process ended with G42 restructured out of the deal and the notice withdrawn on 2025-03-27, not with a completed investment.
- **Exports.** UAE export licenses are held, with security conditions.
- **CEO history.** Feldman's 2007 guilty plea and 2008 SEC settlement are disclosed.
- **Litigation.** A copyright class action filed in October 2025 is pending.
- **Controls.** Material weaknesses in internal control were reported for 2024 and 2025.

### Cited Findings
- **CFIUS.** Joint Voluntary Notice filed July 2024. The withdrawal was granted on **2025-03-27** "based on the foregoing representations": G42 removed as a party, non-voting stock only, and no pricing or volume commitments. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm) The public announcement framed this as "clearance" (2025-03-31). [PRESS] — [CNBC/NBC LA, 2025-03-31](https://www.nbclosangeles.com/news/business/money-report/ai-chipmaker-cerebras-announces-cfius-clearance-a-key-step-toward-ipo/3666820/)
- **Export controls.**
  - Licenses obtained for CS‑2, CS‑3 and CS‑4 exports to G42 and MBZUAI (UAE), with security and compliance conditions; the licenses can be revoked.
  - The filing references the October 2023 BIS rules (the UAE is in Country Group D:4) and the January 2025 AI Diffusion Framework.

  [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
- **CEO's past legal matter.**
  - Feldman was a defendant in *SEC v. Pereira* (N.D. Cal., No. 3:06-cv-06384-CRB) over Riverstone Networks' accounting for sales in 2001–2002.
  - He settled in 2008 without admitting or denying the allegations: a permanent injunction and **$289,507 plus interest**.
  - He **pleaded guilty in December 2007** to one count of circumventing accounting controls (15 U.S.C. §78m(b)(5), §78ff). The sentence was 3 years' probation and a $5,000 fine.

  [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- **Copyright lawsuit.** A **putative copyright class action** was filed in October 2025 in the N.D. Cal. The amended complaint concerns "certain large language models and datasets". Cerebras has answered, denying the claims, and cannot estimate the possible loss. [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
- **Material weaknesses** for FY2024 and FY2025, as listed under Q3. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- **Controlled-company governance.** The 20:1 dual-class structure lets Class B holders control votes even when Class B is as little as 5% of the A+B shares. [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)

### Inferences
- No SEC enforcement action against the company itself was found in the filings reviewed. The only SEC matter disclosed is the 2006–2008 case involving Feldman personally.

### Gaps
- The copyright case's caption, plaintiffs and docket number.
- Any CFIUS mitigation agreement or letter text.
- Any 2026 export-license changes (such as UAE license expansions or new conditions).

---

## Q8. The science: wafer-scale engineering, what is verified, what is unproven, and the physical limits

### Takeaway
- **Verified.** Wafer-scale integration works in production. Speed is independently verified for single-user output on supported models (Artificial Analysis) and for specific HPC kernels (national labs, peer-reviewed SC papers).
- **Not shown independently.** Cost per token at scale, efficient serving of very large models within 44 GB of SRAM per wafer, competitive training, multi-wafer utilization, and fleet reliability.
- **Signs of strain in the disclosures.** The company's own filings show delivery delays, service credits and low GAAP cloud margins.

### Cited Findings
**Engineering: how wafer-scale works, as Cerebras describes it** [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
- **Cross-reticle stitching.** Die are joined "at the wafer level, at the semiconductor fabrication plant" with a "proprietary cross-reticle connection". The result communicates "across the entire 46,225 mm² of silicon".
- **Yield through redundancy.** Flaws "are designed to be recognized, shut down, and routed around", using "redundant building blocks". Cerebras compares this to memory manufacturing.
- **Physical challenges the company cites.** Yielding a chip "58 times larger than the leading GPU"; delivering power "without melting the motherboard"; packaging "without cracking it"; cooling "without the coolant getting warm before it reached the other side". It was "among the first … to deliver water cooling to the processor".
- **CS‑4 power and cooling.** Up to 30 power supplies per wafer "backpack" on 30 A breakers at up to 277 V AC; liquid cooling with leak detection; double the CS‑3 backpack's cooling capacity. [PRESS] — [ServeTheHome, 2026-08-25](https://www.servethehome.com/cerebras-talks-going-rack-scale-with-their-wses-at-hot-chips-2026/)
- **CS-3 power.** WSE‑3 is said to double WSE‑2 performance "in the same power envelope". No kW figure is given. [CO] — [WSE-3 release, 2024-03-13](https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine)

**Demonstrated and independently verified**
- **Artificial Analysis**
  - August 2024: "fastest speeds we have ever benchmarked" (as quoted by Cerebras). [IND: AA via CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
  - May 2026: Kimi K2.6 at **981 output tokens/s**, 6.7x the next-fastest GPU cloud. [IND: Artificial Analysis, per VentureBeat] — [VentureBeat, 2026-05-20](https://venturebeat.com/technology/cerebras-says-its-chips-run-a-trillion-parameter-ai-model-nearly-7-times-faster-than-gpu-clouds)
  - Current AA page: gpt‑oss‑120b blended **$0.39/1M** tokens and time to first answer token of 0.73–1.77 s. [IND: Artificial Analysis] — [AA Cerebras provider page, fetched 2026-11-14](https://artificialanalysis.ai/providers/cerebras)
  - Secondary pages cite AA gpt‑oss‑120b readings of about 1,671–1,735 tokens/s (Oct–Nov 2026). These were not verified directly. [SECONDARY] — [Cerebras glossary page](https://www.cerebras.ai/glossary/what-is-the-fastest-ai-inference-platform) (search-result summary)
- **National labs, molecular dynamics (2024 Gordon Bell finalist)**
  - The LLNL, Sandia and LANL team with Cerebras ran on the WSE‑2. They reported **>699,000 timesteps/s** for 800,000 tantalum atoms, **457x** Frontier's rate in timesteps per second.
  - The team was a **2024 ACM Gordon Bell Prize finalist**.
  - LLNL's caveats: the results do "not mean the WSE-2 is faster overall than exascale systems". Frontier's and El Capitan's aggregate performance "remains much higher". The chip suits "smaller problems that need only one chip" and workloads with many timesteps. Tools need to mature.

  [IND: LLNL] — [LLNL, "NNSA researchers break molecular-dynamics timescale barrier with world's largest chip", 2024-11-20](https://www.llnl.gov/article/52081/nnsa-researchers-break-molecular-dynamics-timescale-barrier-worlds-largest-chip)
  - Sandia also reported 699 kilosteps/s against a decade-long ceiling of about 5 kilosteps/s. [IND: Sandia] — [Sandia Lab News, 2024-10-03](https://www.sandia.gov/labnews/2024/10/03/sandia-led-collaboration-achieves-one-of-worlds-fastest-molecular-dynamics-simulations/) (search-result summary)
- **Peer-reviewed SC24 paper.** "Breaking the Molecular Dynamics Timescale Barrier Using a Wafer-Scale System", Santos et al. Its arXiv v1 abstract (2024-05-13) reports >270,000 timesteps/s with the EAM potential, up to 800k atoms, and **179x** Frontier. [IND: peer-reviewed, SC '24 Article 8] — [arXiv 2405.07898](https://arxiv.org/abs/2405.07898)
- **Peer-reviewed SC20 paper (CS‑1 with NETL).** "Fast Stencil-Code Computation on a Wafer-Scale Processor", Rocki et al.: **0.86 PFLOPS**, about one-third of peak, running BiCGStab on a 600×595×1536 mesh. It discusses memory-capacity and precision issues. [IND: peer-reviewed SC20] — [arXiv 2010.03660, 2020-10-07](https://arxiv.org/abs/2010.03660)
- **Customer statements with numbers**
  - Perplexity: 1,200 tokens/s (Feb 2025, with the API caveat noted under Q1). [CUST] — [Perplexity, 2025-02-11](https://www.perplexity.ai/hub/blog/meet-new-sonar)
  - Cognition: up to 950 tokens/s (Oct 2025). [CUST] — [Cognition, 2025-10-29](https://cognition.com/blog/swe-1-5)
  - GSK: "10x faster" training. This appears only as a testimonial in Cerebras's own prospectus. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)

**Unproven or contested**
- **Cost per token at scale.** No audited per-token cost exists. GAAP **cloud** gross margin was 16.2% in Q3 2025, **24.3%** in Q3 2026 and 28.4% in 9M 2026. Core cloud margin was 46.9% in Q3 2026. Claims of "lower cost per token" from disaggregation, and CS‑4's "10x throughput/W", are company-only. [CO-SEC] — [Q3 release reconciliation](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm); [CS-4 blog](https://www.cerebras.ai/blog/introducing-cerebras-cs-4)
- **Very large models within 44 GB SRAM per wafer.** Kimi K2.6 (1T parameters) needed **about 20 CS‑3s** even with 4-bit weights. [CO via PRESS] — [VentureBeat, 2026-05-20](https://venturebeat.com/technology/cerebras-says-its-chips-run-a-trillion-parameter-ai-model-nearly-7-times-faster-than-gpu-clouds) The claim of "10T+ parameters at >1,000 tokens/s" is an extrapolation. [CO] — [CS-4 blog](https://www.cerebras.ai/blog/introducing-cerebras-cs-4) CS‑6 will add stacked DRAM. [PRESS] — [ServeTheHome](https://www.servethehome.com/cerebras-talks-going-rack-scale-with-their-wses-at-hot-chips-2026/)
- **Training competitiveness.**
  - The company's claims cover training up to 24T parameters, and training for G42, MBZUAI, GSK, Sandia and the DoD. [CO] — [WSE-3 release](https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine); [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
  - No independent training benchmark was found in this pass.
  - Revenue has shifted to inference: cloud and services were 60% of 9M 2026 revenue. [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
- **Utilization and economics of multi-wafer deployments.** Not disclosed.
- **Reliability at data-center scale.** [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
  - Cerebras says it and its data centers "have experienced … disruptions, outages, and other performance problems".
  - "As a result of degradation of service and interruptions to our platform, we have provided … service credits and/or refunds".
  - OpenAI capacity shortfalls are accruing service credits.

**Physical and engineering limits, as documented**
- **On-wafer memory is fixed.** 44 GB per wafer in both WSE‑3 and WSE‑3T. Larger models must be split across many wafers, as Kimi K2.6 on about 20 systems shows. [CO] — sources above.
- **Single foundry.** Sole-source TSMC with no long-term allocation. The node transition (7 nm → 5 nm) depends on TSMC. [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
- **Scope of the HPC advantage.** It is strongest for problems that fit on one wafer and need many iterations (LLNL caveat). The SC20 paper flags memory capacity and floating-point precision. [IND] — [LLNL](https://www.llnl.gov/article/52081/nnsa-researchers-break-molecular-dynamics-timescale-barrier-worlds-largest-chip); [arXiv 2010.03660](https://arxiv.org/abs/2010.03660)
- **Packaging.** Power delivery and cooling at wafer scale require custom packaging, the "backpacks". [CO] / [PRESS] — sources above.

### Inferences
- **Does it stand on solid ground? The narrow claim does; the economic claim is not yet shown.**
  - **On solid ground:** single-stream decode speed. It has repeated independent measurement (Artificial Analysis 2024–2026, customer posts from Perplexity and Cognition) and peer-reviewed HPC results.
  - **Not independently shown:** that the speed translates into competitive cost per token and reliable multi-hundred-MW delivery. In 2026 the company's own filings show low GAAP cloud margins, delivery delays and service credits.
- **Memory arithmetic.** At 4 bits, a 1T-parameter model needs about 500 GB for weights alone, roughly 11–12 wafers of 44 GB before KV cache and activations. That is consistent with the ~20 systems reported. Multi-wafer pipelining is therefore structural for frontier-size models, and per-wafer utilization becomes central to the economics.
- **Molecular dynamics figures.** The speedups grew between the May 2024 preprint (179x) and the November 2024 lab and vendor releases (457x lab, 748x vendor). The lab-published figure, 457x with explicit caveats, is the most conservative independent figure.

### Gaps
- The 2024 Gordon Bell Prize winner, to confirm that the Cerebras team was a finalist and did not win. The ACM page returned 403.
- Any SC25 (2025) Gordon Bell finalist involving Cerebras.
- Cerebras's role in the 2022 GenSLM Special Prize.
- Hot Chips and IEEE Micro architecture papers by Sean Lie, for spare-core redundancy figures. These were not retrieved.
- MLPerf participation.
- The Artificial Analysis live leaderboard comparing Cerebras with Groq, SambaNova and NVIDIA-based providers. It was not retrievable: the page did not render speeds, and search was exhausted.

---

## Q9. Cross-examination log: Cerebras's claims against other sources

### Takeaway
Cerebras's speed claims are broadly supported by independent measurement, but the headline multiples depend on the model chosen and on how the metric is framed. Its contract and financial framings (OpenAI value, CFIUS "clearance", "secured" supply, G42 dilution) diverge materially from what its own SEC filings and independent outlets show.

### Cited Findings
1. **OpenAI deal value**
   - **Press:** more than $10B, from unnamed sources. [PRESS-UNNAMED] — [CNBC, 2026-01-14](https://www.cnbc.com/2026/01/14/cerebras-scores-openai-deal-worth-over-10-billion.html) CNBC repeated "over $10 billion" on 2026-10-02. — [CNBC](https://www.cnbc.com/2026/10/02/cerebras-stock-hits-post-ipo-low-on-nvidia-pressure-lockup-expiration.html)
   - **Cerebras:** "more than $20 billion". [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
   - CNBC on 2026-05-14 also reported more than $20B. — [CNBC](https://www.cnbc.com/2026/05/14/cerebras-cbrs-stock-trade-nasdaq-ipo.html)
2. **OpenAI term**
   - **Press:** "through 2028". [PRESS] — [CNBC, 2026-01-14](https://www.cnbc.com/2026/01/14/cerebras-scores-openai-deal-worth-over-10-billion.html)
   - **Filings:** deployment runs through 2028, but each tranche runs 3–4 years, extendable to 5. About 33% of the $26.1B RPO is recognized by 2028-09-30, so about **67% comes after September 2028**: 44% in months 25–48 and the rest later. [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
3. **CFIUS**
   - **Announcement:** "clearance" (2025-03-31). [PRESS] — [CNBC/NBC LA](https://www.nbclosangeles.com/news/business/money-report/ai-chipmaker-cerebras-announces-cfius-clearance-a-key-step-toward-ipo/3666820/)
   - **Filings:** a withdrawal granted 2025-03-27 on representations; the G42 investment never closed. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
4. **Customer concentration framing**
   - **Press:** G42 "24% of 2025 revenue, down from 85%". [PRESS] — [CNBC, 2026-05-14](https://www.cnbc.com/2026/05/14/cerebras-cbrs-stock-trade-nasdaq-ipo.html)
   - **Filings:** MBZUAI, a G42 related party under ASC 850, was 62%. The UAE-related total was 86% in 2025. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm); [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
5. **2025 profit**
   - **Press:** "net income $88 million". [PRESS] — [CNBC, 2026-05-14](https://www.cnbc.com/2026/05/14/cerebras-cbrs-stock-trade-nasdaq-ipo.html)
   - **Filings:** GAAP net income $237.8M, including a $363.3M non-cash gain. Income attributable to common was $87.9M. The non-GAAP **net loss** was $75.7M. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
6. **TSMC supply**
   - **Press release:** "Secured TSMC wafer supply". [CO] — [Q2 release, 2026-08-12](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm)
   - **10-Q:** "no formalized long-term supply or allocation commitments from TSMC". [CO-SEC] — [10-Q Q3 2026, 2026-11-12](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
7. **OpenAI workload**
   - **Cerebras:** "OpenAI launch partner for frontier model GPT‑5.6 Sol" at 750 tokens/s. [CO] — [Q2 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm)
   - **SemiAnalysis, via CNBC:** OpenAI will run the "Ultrafast" mode for **GPT‑6.1 Sol on Nvidia GPUs instead of Cerebras hardware". Altman then called Cerebras "a close partner". [PRESS citing SemiAnalysis] — [CNBC, 2026-10-02](https://www.cnbc.com/2026/10/02/cerebras-stock-hits-post-ipo-low-on-nvidia-pressure-lockup-expiration.html)
8. **Delivery performance**
   - **Press release:** "We exceeded our guidance across the board". [CO] — [Q3 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm)
   - **10-Q, same day:** capacity delivered to OpenAI is below MRA levels, service credits accrue from 2026-10-01, and delays may run into 2027. [CO-SEC] — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)
9. **gpt‑oss‑120B speed**
   - **Cerebras claim, as reported:** more than 3,000 tokens/s. [CO via PRESS] — [The Register, 2025-10-07](https://theregister.com/2025/10/06/cerebras_ipo_rest)
   - **Prospectus chart:** 1,735 tokens/s (2026-04-14, 10k-token input, Cerebras internal measurements plus AA). [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
   - **Secondary pages citing AA:** about 1,671–1,735 tokens/s. [SECONDARY]
10. **"Up to 15x faster than NVIDIA GPUs"**
    - **Cerebras:** the headline multiple. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
    - **Same chart:** 15x holds for Llama‑3.3 70B (2,457 vs 164 tokens/s). For gpt‑oss‑120B the chart shows about 1,735 vs a best GPU cloud of about 458, roughly 3.8x. The vendor labels are ambiguous in the extracted chart text.
11. **Throughput versus per-user speed**
    - **NVIDIA:** gpt‑oss‑120b at **1.5 million tokens/s** on one GB200 NVL72 rack. This is a rack-level figure, so it is not a per-user speed. [IND: NVIDIA (competitor)] — [NVIDIA blog, 2025-08-05](https://blogs.nvidia.com/blog/openai-gpt-oss/)
    - **Cerebras:** its "fastest" claims refer to per-user output tokens/s. The two measure different things.
12. **Molecular dynamics speedup**
    - **Preprint:** 270k timesteps/s and 179x Frontier. [IND] — [arXiv v1, 2024-05-13](https://arxiv.org/abs/2405.07898)
    - **LLNL:** 699k timesteps/s and 457x, with caveats. [IND] — [LLNL, 2024-11-20](https://www.llnl.gov/article/52081/nnsa-researchers-break-molecular-dynamics-timescale-barrier-worlds-largest-chip)
    - **Cerebras:** more than 1.1M steps/s and 748x. [CO, via PRESS] — [HPCwire, 2024-11-19](https://www.hpcwire.com/2024/11/19/cerebras-sets-new-record-in-molecular-dynamics-at-1-1m-simulations-per-second/) (search-result summary)
13. **Data-center footprint**
    - **March 2025 plan:** 6 new sites, including Minneapolis, the Midwest/Eastern US and Europe by Q4 2025. [CO] — [press release, 2025-03-11](https://www.cerebras.ai/press-release/cerebras-announces-six-new-ai-datacenters-across-north-america-and-europe-to-deliver-industry-s)
    - **May 2026 prospectus:** facilities "currently" in California, Oklahoma and Canada only. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
    - The Cerebras web page says both "6 new" and "8 cutting-edge facilities". [CO] — [cerebras.ai/ai-supercomputer](https://www.cerebras.ai/ai-supercomputer)
14. **Condor Galaxy 3**
    - **March 2024:** "available Q2 2024". [CO] — [Cerebras CG-3 release, 2024-03-13](https://www.cerebras.ai/press-release/cerebras-g42-announce-condor-galaxy-3) (search-result summary)
    - **Since then:** no delivery confirmation found, and the 2026 prospectus does not mention Condor Galaxy. [CO-SEC] — [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)
15. **Perplexity "powered by Cerebras"**
    - Perplexity's own footnote says the API Sonar did "not yet run on Cerebras" (2025-02-11). [CUST] — [Perplexity](https://www.perplexity.ai/hub/blog/meet-new-sonar)
16. **Mistral**
    - Mistral's own launch post does not name Cerebras (2025-02-06). [CUST] — [Mistral](https://mistral.ai/news/all-new-le-chat)
    - Cerebras's claim to power Le Chat was not fetched, so this is unconfirmed rather than contradicted.
17. **Valuation at the IPO**
    - About $95B at the first-day close. [PRESS] — [CNBC, 2026-05-14](https://www.cnbc.com/2026/05/14/cerebras-cbrs-stock-trade-nasdaq-ipo.html)
    - About $67B. [SECONDARY] — [Wikipedia, Cerebras Systems](https://en.wikipedia.org/wiki/Cerebras_Systems) (search-result summary)
    - $56.4B fully diluted at $185. [SECONDARY] — [tech-insider.org](https://tech-insider.org/cerebras-ipo-filing-510m-revenue-openai-deal-23b-valuation-2026/) (search-result summary)
    - The differences come from different share counts and prices.
18. **Lockup dates**
    - Main expiry reported as 2026-11-09 versus 2026-11-10. Early staged releases began 2026-08-19. [PRESS] — [CNBC, 2026-10-02](https://www.cnbc.com/2026/10/02/cerebras-stock-hits-post-ipo-low-on-nvidia-pressure-lockup-expiration.html); [SECONDARY] — [FinanceFeeds](https://financefeeds.com/cbrs-stock-cerebras-lock-up-expires-ahead-of-nov-12-q3-results/)
19. **Share-price reaction on 2026-11-13**
    - About +7% (CNBC); +11.7% intraday (GuruFocus); +16–18% after hours (Quartz). These were measured at different times. [PRESS] — [CNBC](https://www.cnbc.com/2026/11/12/cerebras-systems-cbrs-q3-earnings-report-2026.html); [GuruFocus](https://www.gurufocus.com/news/9198095/cerebras-stocks-jump-1170-after-raising-outlook-and-confirming-microsoft-cloud-deal); [Quartz](https://qz.com/cerebras-stock-earnings-beat-microsoft-deal-111326) (search-result summaries)
20. **Why the IPO was withdrawn**
    - **Feldman (Oct 2025):** "the business has improved", so the financials needed updating. [PRESS] — [The Register](https://theregister.com/2025/10/06/cerebras_ipo_rest)
    - **CNBC (May 2026):** withdrawn "after scrutiny over its customer concentration". [PRESS] — [CNBC, 2026-05-14](https://www.cnbc.com/2026/05/14/cerebras-cbrs-stock-trade-nasdaq-ipo.html)
21. **"WSE‑4"**
    - Third-party pages describe a WSE‑4 with about 1.5M cores. [SECONDARY] — [mirrorfrog](https://mirrorfrog.com/en/docs/cards/cerebras/wse-4/) (search-result summary)
    - Cerebras's own materials name the WSE‑3 Turbo (CS‑4) and the WSE‑5 (CS‑5). [CO] — [CS-4 blog](https://www.cerebras.ai/blog/introducing-cerebras-cs-4); [Q3 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm)

### Inferences
- **Speed.** The direction of the claims ("fastest per-user tokens/s on the models we serve") is consistent with independent AA data. The size of the advantage varies about 4x–15x depending on model, input length and comparison set, and the 30x (CS-4) figure is partly internal.
- **Financial and contract framing.** The most consequential divergences are between press releases and 10-Q risk disclosures: TSMC supply, delivery against guidance, OpenAI deal value, and the CFIUS outcome.

### Gaps
- Groq's and SambaNova's own published speed claims for the same models. Not retrieved; search was exhausted.
- OpenAI's own blog text. Not retrieved (403).
- Whether the GPT‑6.1 Sol "Ultrafast" report was confirmed or denied by OpenAI beyond Altman's post.

---

## Q10. Final lists: (a) contradictions found; (b) what could not be found or verified

### Takeaway
There are 21 logged divergences, listed in (a). Missing items are listed in (b). The largest gaps are the Microsoft terms, Condor Galaxy delivery, live MW, CS-3 and CS-4 power, independent training benchmarks, and live competitor speed comparisons.

### Cited Findings
**(a) Contradictions or divergences found.** Sources for each item are in the Q9 log.
1. OpenAI deal value: more than $10B (unnamed sources) vs more than $20B (Cerebras).
2. OpenAI term: "through 2028" vs tranches of 3–5 years, with most revenue after September 2028.
3. CFIUS "clearance" vs a notice withdrawal, with the G42 investment never closed.
4. G42 concentration "fell to 24%" vs a UAE related-party share of 86% (2025) and 54% (9M 2026).
5. 2025 "net income $88M" vs GAAP $237.8M, including a $363M non-cash gain, and a non-GAAP loss of $75.7M.
6. "Secured TSMC wafer supply" vs "no formalized long-term supply or allocation commitments".
7. GPT‑5.6 Sol launch partner vs a report that GPT‑6.1 Sol "Ultrafast" runs on Nvidia.
8. "Exceeded guidance across the board" vs OpenAI capacity shortfalls and service credits.
9. gpt‑oss‑120B: more than 3,000 tokens/s (claim) vs about 1,735 tokens/s (prospectus chart, AA-linked).
10. "Up to 15x" holds for Llama‑3.3 70B but is about 3.8x for gpt‑oss‑120B in the same chart.
11. NVIDIA's 1.5M tokens/s per rack (aggregate) vs Cerebras's per-user "fastest": different metrics.
12. Molecular dynamics speedup: 179x (preprint) vs 457x (LLNL) vs 748x (Cerebras).
13. March 2025 plan of 6–8 sites vs May 2026 facilities in California, Oklahoma and Canada only.
14. CG‑3 "available Q2 2024" vs no delivery confirmation and absence from the 2026 prospectus.
15. Perplexity "powered by Cerebras" vs its own footnote that the API was not yet on Cerebras.
16. Mistral partnership: not confirmed in Mistral's own post.
17. IPO valuation: $95B vs $67B vs $56.4B, on different share and price bases.
18. Lockup expiry: 2026-11-09 vs 2026-11-10.
19. Size of the 2026-11-13 share-price move: 7% vs 11.7% vs 16–18%.
20. Reason for the IPO withdrawal: "business improved" vs "customer-concentration scrutiny".
21. "WSE‑4" on third-party sites vs Cerebras's WSE‑3T and WSE‑5 naming.

### Inferences
- The ten most decision-relevant items are 1–8, 10 and 13. Each pits a Cerebras marketing statement against Cerebras's own SEC risk disclosures or an independent source.

### Gaps
**(b) Could not find or verify (as of 2026-11-14)**
- Microsoft deal terms: value, MW and duration. Whether the "top three hyperscaler" deal is the same as the Microsoft deal is per CNBC only.
- Condor Galaxy 1, 2 and 3 delivery dates and status, and the fate of any further Condor Galaxy systems in the 2024 plan.
- Energized (live) MW, as opposed to contracted MW. Per-site MW and go-live dates for Oklahoma City, Montreal, Minneapolis, Norway and Finland.
- CS‑3 and CS‑4 power draw in kW; spare-core and redundancy percentages; wafer yield.
- Cerebras Inference per-model list prices beyond AA's blended $0.39/1M for gpt‑oss‑120b.
- The Artificial Analysis live leaderboard figures for Cerebras against Groq, SambaNova and GPU clouds (speeds did not render). Groq's and SambaNova's own current claims.
- OpenAI's own blog post on the deal (403). Whether OpenAI confirmed the GPT‑6.1 Sol hardware choice.
- The 2024 Gordon Bell winner (to confirm that the Cerebras team was a finalist only), any SC25 finalist, and Cerebras's role in the 2022 GenSLM prize.
- Independent training benchmarks, such as MLPerf.
- AstraZeneca, Mayo Clinic, Argonne, Notion and IBM relationship specifics. Mistral's confirmation.
- Gary Lauterbach's role. Whether J.P. Fricker and Michael James are currently employed.
- G42's current total shareholding, including its 2021 Series F shares and any sales.
- The caption and docket number of the October 2025 copyright class action.
- The Series H lead investor from a primary source. The Series G co-investors (Tiger Global, Valor, 1789 Capital) from a primary source.
- Today's share price (2026-11-14). The latest available is about $109 intraday on 2026-11-13.
- Process notes:
  - The shared WebSearch budget for the turn was exhausted midway.
  - Firecrawl returned "insufficient credits".
  - A direct page fetch with a browser user agent was denied by the session's permission policy.
  - These items remain open for a follow-up pass.
