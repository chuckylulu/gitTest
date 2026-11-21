# Claims ledger, C1: "HBM4 and HBM4E add inspection steps per stack (versus HBM3E), increasing Camtek-addressable inspection/metrology demand per stack"

**Scope:** An adversarial review of claim C1 for Camtek Ltd. (Nasdaq/TASE: CAMT). Fiscal year = calendar year. Research date 2026-11-21. The latest reported quarter is **Q3 2026** (results and call on 2026-11-04). The latest company event is the Analyst & Investor Day on 2026-10-14.

**Method:**
- Started from `notes/05_hbm_inspection_steps.md`, with cross-checks against `02_`, `06_` and `08_`.
- Re-checked the key quotes at source. Live pages were re-fetched on 2026-11-21 for the Camtek Q1 2024, Q2 2025 and Q3 2026 calls, the Onto Q3 2026 call and the TrendForce 2024-09-30 release. Other Camtek quotes were re-read in the local transcript copies under `camtek_dl/hbm_steps/tx/`.
- Ran new searches for disconfirming evidence: Korean trade press, competing inspection vendors, X-ray/CT suppliers, GPU stack-height changes, HBM capacity and analyst questions.

**Tags:**
- [CO] = company-controlled.
- [IND] = independent.
- [CO-relayed] = a third party repeating Camtek.
- QUANTIFIED / QUALITATIVE marks each Camtek statement.
- DERIVED = arithmetic shown.

No recommendation or valuation is made.

---

## Ledger entry (summary)

| Field | Entry |
|---|---|
| **Claim** | HBM4 and HBM4E add inspection steps per stack (versus HBM3E), increasing Camtek-addressable inspection/metrology demand per stack. |
| **Who makes it, where** | **Camtek management.** No independent party was found making this claim in a per-stack or per-generation form. Main instances:<br>- Q1 2025 call, 2025-05-13 [4]: "transition for HBM3 to HBM4… brings additional opportunities with more inspection and metrology steps". QUALITATIVE.<br>- Q3 2025 call, 2025-11-10 [6]: "the move to HBM4 is going to be what we call inspection and metrology intensive because the bumps are getting tighter. There are going to be more bumps". QUALITATIVE.<br>- Q4 2025 call, 2026-02-18 [7]: "It is more metrology and inspection intensive". QUALITATIVE.<br>- Analyst Day, 2026-10-14 [10][11]: "increased complexity contributes more inspection and metrology steps"; HBM die-warp spec 1 mm → 100 µm. QUALITATIVE on steps; QUANTIFIED on spec.<br>- 20-F FY2024 and FY2025 [14]: "Chiplets and HBM, require more inspection and metrology steps". QUALITATIVE.<br>**Not repeated for HBM4/HBM4E in the latest call** (Q3 2026, 2026-11-04 [12]). There the step language is generic to "advanced packaging", and HBM4/HBM4E are not named. |
| **Verdict** | **Partly supported.** |
| **Confidence** | Medium (in the verdict). Low in any quantified version of the claim. |
| **Why** | (a) **Direction has independent support.** Independent sources show HBM4 is harder to make: finer bumps, thinner wafers, tighter warpage, lower yields than HBM3E, and HBM raising DRAM process-control intensity [21][23][24][26][31]. Onto says packaging process-control intensity and sampling rates are rising [20].<br>(b) **"Steps per stack" is never quantified.** No source quantifies it: not Camtek, not a memory maker, not a competitor, not an analyst. Camtek's own record argues against a per-stack frame. It said "we scan wafers", stack height "doesn't change our business", and there is "no" ASP uplift [1]. It said most HBM3 tools "will be used for HBM4 as well" [5], and bumps per wafer "stays in this range… not going to go to 300 million" [3].<br>(c) **The competitor names volume, not steps.** Onto's CEO said the HBM4 → HBM4E opportunity "is going to be driven a lot by volume… It's all about the wafers for us" [20].<br>(d) **Part of the new HBM inspection demand goes to methods or vendors outside Camtek's optical lines.** Examples: X-ray at Micron [34], CT at Samsung/SK hynix R&D [35], stacking-defect inspection by Nextin at SK hynix [32][33]. Onto displaced a "tool of record" for HBM4 2D inspection and 3D bump metrology at a leading HBM maker [19]. That weakens "Camtek-addressable".<br>(e) **"Per stack" is undercut by stack-height cuts.** GPU/ASIC makers are reportedly weighing 12-high → 8-high cuts [28]. Camtek also reports a "tendency… to reduce" memory density per module [10].<br>(f) **The biggest step-adder (hybrid bonding) is not in HBM4.** Its timing is disputed for HBM4E: earliest at 16-high HBM4E [27]. Camtek says HBM5 stays on bumps [10].<br>**Rule applied:** a claim backed on its key element only by company statements cannot be rated above "partly supported". |
| **Independent share of evidence** | **For the claim:** about 6 of 13 items are [IND]. They support *higher process-control difficulty/intensity in HBM4*, not *more Camtek steps per stack*. Every item that asserts more *steps* is [CO].<br>**Against the claim:** about 10 of 15 items are [IND]. The rest are Camtek's own earlier statements.<br>**Overall:** about 55% [IND] by item count (DERIVED: 16 [IND] of 28 items listed below). On the specific "more steps per stack" element, independent evidence is **0%**. |

---

## Sources used

Camtek, company-controlled
1. [CO] Camtek Q1 2024 earnings call, 2024-05-09, Motley Fool transcript (re-fetched 2026-11-21). https://www.fool.com/earnings/call-transcripts/2024/05/09/camtek-camt-q1-2024-earnings-call-transcript/
2. [CO] Camtek Q3 2024 earnings call, 2024-11-12, Motley Fool. https://www.fool.com/earnings/call-transcripts/2024/11/12/camtek-camt-q3-2024-earnings-call-transcript/ (local copy)
3. [CO] Camtek Q4 2024 earnings call, 2025-02-12, Motley Fool. https://www.fool.com/earnings/call-transcripts/2025/02/12/camtek-camt-q4-2024-earnings-call-transcript/ (local copy)
4. [CO] Camtek Q1 2025 earnings call, 2025-05-13, Quartr transcript on StockAnalysis. https://stockanalysis.com/stocks/camt/transcripts/315174-q1-2025/ ; Q1 2025 results release, 2025-05-13. https://www.camtek.com/news-and-events/camtek-announces-record-results-for-the-first-quarter-of-2025/
5. [CO] Camtek Q2 2025 earnings call, 2025-08-05, Motley Fool (re-fetched 2026-11-21). https://www.fool.com/earnings/call-transcripts/2025/08/05/camtek-camt-q2-2025-earnings-call-transcript/
6. [CO] Camtek Q3 2025 earnings call, 2025-11-10, Motley Fool transcript on Yahoo Finance. https://finance.yahoo.com/markets/stocks/articles/camtek-camt-q3-2025-earnings-165201423.html (local copy)
7. [CO] Camtek Q4 2025 earnings call, 2026-02-18, Quartr transcript on StockAnalysis. https://stockanalysis.com/stocks/camt/transcripts/407176-q4-2025/ (local copy)
8. [CO] Camtek Q1 2026 earnings call, 2026-05-12, StockAnalysis. https://stockanalysis.com/stocks/camt/transcripts/559247-q1-2026/ ; script slide https://cdn.camtek.com/wp-content/uploads/Script-presentation-Q1-2026.pdf
9. [CO] Camtek Q2 2026 earnings call, 2026-08-10, Motley Fool. https://www.fool.com/earnings/call-transcripts/2026/08/17/camtek-camt-q2-2026-earnings-call-transcript/
10. [CO] Camtek Analyst & Investor Day, 2026-10-14, Quartr transcript on StockAnalysis. https://stockanalysis.com/stocks/camt/transcripts/765438-analyst-day-2026/ (local copy, Q&A read in full)
11. [CO] Camtek Investor Presentation, 2026-10-14 (slides 17, 18, 20, 23, 25). https://cdn.camtek.com/wp-content/uploads/Camtek-Investor-Presentation-OCT26.pdf
12. [CO] Camtek Q3 2026 earnings call, 2026-11-04, Motley Fool (re-fetched 2026-11-21). https://www.fool.com/earnings/call-transcripts/2026/11/04/camtek-camt-q3-2026-earnings-call-transcript/
13. [CO] Camtek Q3 2026 script presentation, 2026-11-04. https://cdn.camtek.com/wp-content/uploads/Q3-2026-Script-Presentation.pdf
14. [CO] Camtek Form 20-F. FY2024 (filed 2025-03-19): https://www.sec.gov/Archives/edgar/data/1109138/000117891325000945/zk2532834.htm. FY2025 (filed 2026-03-19): https://cdn.camtek.com/wp-content/uploads/Camtek-2025-20F.pdf
15. [CO] Camtek Q4 2023 earnings call, 2024-02-20, Motley Fool. https://www.fool.com/earnings/call-transcripts/2024/02/20/camtek-camt-q4-2023-earnings-call-transcript/ (local copy)
16. [CO] Camtek press release, "Camtek Receives Over $105 Million Multi-System Orders from a Tier-1 OSAT and a Leading HBM Manufacturer", 2026-06-02. https://www.camtek.com/news-and-events/camtek-receives-over-105-million-multi-system-orders-from-a-tier-1-osat-and-a-leading-hbm-manufacturer/
17. [CO] Camtek Q1 2024 results release, 2024-05-09 (revenue $97.0M). https://cdn.camtek.com/wp-content/uploads/Q12024.pdf
18. [CO-relayed] Asia Economy, "Rafi Amit, Chairman of CAMT, Attends Semicon Korea 2025", 2025-02-20. https://www.asiae.co.kr/en/article/2025022001311158152

Independent
19. [IND] Onto Innovation (competitor) news release, "Onto Innovation Launches Dragonfly G5 Inspection System", 2026-03-16 (PDF text re-read). https://s24.q4cdn.com/480160064/files/doc_news/Onto-Innovation-Launches-Dragonfly-G5-Inspection-System-2026.pdf
20. [IND] Onto Innovation Q3 2026 earnings call, 2026-11-09, Motley Fool (CEO Michael Plisinski; re-fetched 2026-11-21). https://www.fool.com/earnings/call-transcripts/2026/11/10/onto-innovation-onto-q3-2026-earnings-call-transcript/
21. [IND] KLA September-2025-quarter call, 2025-10-29, Motley Fool. https://www.fool.com/earnings/call-transcripts/2025/10/30/kla-klac-q1-2026-earnings-call-transcript/ (local copy)
22. [IND, hearsay] Charles Shi (Needham analyst), question at the Camtek Analyst Day, 2026-10-14, as recorded in transcript [10]. This is an analyst's report of what he "did hear over the last couple of days". The underlying sources are not named.
23. [IND] SemiEngineering, "HBM Leads The Way To Defect-Free Bumps", 2025-11-11. It quotes Onto staff, so it is partly competitor marketing. https://semiengineering.com/hbm-leads-the-way-to-defect-free-bumps/
24. [IND] SemiEngineering, "HBM4 Sticks With Microbumps, Postponing Hybrid Bonding", 2026-01-13. https://semiengineering.com/hbm4-sticks-with-microbumps-postponing-hybrid-bonding/
25. [IND] SemiEngineering (Anne Meixner), "HBM Shifts Testing Left To Preserve AI Chip Yield", 2026-05-12. https://semiengineering.com/hbm-shifts-testing-left-to-preserve-ai-chip-yield/
26. [IND] TrendForce, "JEDEC Finalizes HBM4 Standard…", 2025-04-21. https://www.trendforce.com/news/2025/04/21/news-jedec-finalizes-hbm4-standard-potentially-easing-pressure-on-hybrid-bonding-adoption/
27. [IND] TrendForce, "Samsung, SK hynix Reportedly Reconsider Hybrid Bonding Timeline; 16-High HBM4E May Be Earliest Adoption", 2026-07-07. https://www.trendforce.com/news/2026/07/07/news-samsung-sk-hynix-reportedly-reconsider-hybrid-bonding-timeline-16-high-hbm4e-may-be-earliest-adoption/
28. [IND] EE Times Japan, 2026-09-30, reporting a TrendForce forecast dated 2026-09-29: HBM ASP +121% in 2027, GPU/ASIC makers weighing 12-high → 8-high, HBM4E ramp in late 2027. https://eetimes.itmedia.co.jp/ee/spv/2609/30/news066.html
29. [IND] TrendForce, "Micron Reportedly to Add 60K HBM Wafers/m…", 2026-09-04 (citing ETNews and Chosun Daily). https://www.trendforce.com/news/2026/09/04/news-micron-reportedly-to-add-60k-hbm-wafersm-reaching-100k-by-year-end-to-narrow-gap-with-samsung-sk-hynix/
30. [IND] TrendForce press release, 2024-09-30 (TSV capacity, end-2024 → end-2025). https://trendforce.com/presscenter/news/20240930-12319.html
31. [IND] NewDaily (Lee Na-ri), "GPU·HBM 다음 병목은 웨이퍼…", 2026-06-04. It quotes Hanwha Investment & Securities analyst Park Jun-young. https://biz.newdaily.co.kr/site/data/html/2026/06/04/2026060400152.html
32. [IND] Hankyung (Hwang Jung-hwan), "Nextin enters HBM supply chain in earnest…", 2025-05-24. https://www.hankyung.com/article/202505242860i
33. [IND, secondary] Wccftech (Muhammad Zuhair), "SK Hynix To Integrate 3D Inspection Units To Upscale 12-Layer HBM3E Yield Rates", 2024-10-31, citing BusinessKorea. https://wccftech.com/sk-hynix-integrate-3d-inspection-units-upscale-12-layer-hbm3e-yield-production/
34. [IND] TheElec, "SEC Wins 5.8 Billion Won HBM Inspection Order From Micron", 2026-11-10. https://www.thelec.net/news/articleView.html?idxno=15467
35. [IND] TheElec, "Techvalley Supplies HBM Inspection Equipment to Samsung Electronics and SK Hynix", 2026-04-13. https://www.thelec.net/news/articleView.html?idxno=6518 ; also TheElec, 2026-07-30, https://www.thelec.net/news/articleView.html?idxno=12670
36. [IND] TheElec, "Youngwoo DSP Tests WLP Inspection Tool at Korean Foundry", 2026-09-13. https://www.thelec.net/news/articleView.html?idxno=13870
37. [IND] DigiTimes (Flora Wang), "Samsung and SK Hynix expand microscope procurement to boost HBM yield", 2026-03-26/27. **Headline and teaser only** (paywall). https://www.digitimes.com/news/a20260326PD215.html
38. [IND] Onto Innovation's SK hynix "Best Partner Award" (event 2026-09-28), as summarized by BriefGlance on 2026-10-12. **Taken from notes/05; not re-verified** (Business Wire returned 403). https://briefglance.com/companies/onto-innovation-inc/pulses/88449
39. [IND] Tom's Hardware, "The current state of Hybrid Bonding in 2026", 2026-09-02. **Taken from notes/05; not re-fetched.** https://www.tomshardware.com/tech-industry/semiconductors/hybrid-bonding-roadmap-examined
40. [IND, low quality] Meticulous Research, HBM Inspection Equipment Market report page, August 2026. Its pages give conflicting market sizes ($0.9B vs $5.86B for 2025). Used only for its method-mix statement. https://www.meticulousresearch.com/product/hbm-inspection-equipment-market-6830
41. [IND] Korea Times / Yonhap, "SK hynix orders new equipment worth $28.7 mil. for next-gen HBM4", 2026-06-08 (Hanmi TC bonders). Context only. https://www.koreatimes.co.kr/business/tech-science/20260608/sk-hynix-orders-new-equipment-worth-287-mil-for-next-gen-hbm4

---

## 1. What exactly is claimed, and by whom

The claim has three separable parts. Each must hold for C1 to hold as written.

1. **HBM4/HBM4E add inspection or metrology *steps*** (process points where a wafer is inspected or measured), compared with HBM3E.
2. **The unit is per stack.** The added content scales with each HBM stack.
3. **The added steps are Camtek-addressable,** meaning optical 2D inspection and 3D bump metrology, or the FRT line, are tools Camtek sells or will sell.

Camtek statements bearing on the claim, in chronological order (verified against transcripts as noted):

| # | Date | Venue | Statement (verbatim where quoted) | Type | Supports or undercuts C1 | Src |
|---|---|---|---|---|---|---|
| CO-1 | 2024-02-20 | Q4 2023 call | "at one of our major customers, we have developed tens of new inspection and metrology steps over the last year". Asked which, Ramy Langer said: "those steps are in the advanced packaging world." | QUANTIFIED ("tens", one customer); **not tied to HBM** | Weak support (not HBM-specific) | [15] |
| CO-2 | 2024-05-09 | Q1 2024 call | "moving from eight to 12 doesn't change our business or our machines don't -- don't care because we -- we scan wafers… is there here any upside for ASP improvement? No there isn't" and "whether they will do it a stack of eight, 12, or 16, this really does not make any -- does not require any changes" (re-fetched 2026-11-21) | QUALITATIVE | **Undercuts** the per-stack frame (Camtek's own words) | [1] |
| CO-3 | 2024-11-12 | Q3 2024 call | "the HBMs are having more stacks, and this really means that we are going to scan more wafers… We're working very closely with our customers, trying to add more steps" | QUALITATIVE | Mechanism given is wafer count, not steps per wafer; adding steps is an aim | [2] |
| CO-4 | 2025-02-12 | Q4 2024 call | "the intensity will probably grow as you're putting more and more dies in the same module". On bumps: "you take a wafer, it's over [100] million. And it kind of stays in this range at least for the foreseeable future. It's not going to go to [300] million." Also: "in most cases 100% inspection" | QUALITATIVE / QUANTIFIED (>100M bumps per wafer; 100%) | Mixed: intensity "probably" grows; bump count per wafer is roughly flat | [3] |
| CO-5 | 2025-05-13 | Q1 2025 call | "the transition for HBM3 to HBM4… brings additional opportunities with more inspection and metrology steps in the manufacturing process." Release: HBM4 "expected to create increased demand for new tools with enhanced technical capabilities." | QUALITATIVE | **Supports** (the clearest statement of the claim; no count) | [4] |
| CO-6 | 2025-08-05 | Q2 2025 call | Asked about "content uplift from HBM3/3E to HBM4": "this means that we will scan more wafers. There is some change in the number of bumps, some pitch differences". Also: "the equipment that we sold or most of the equipment that we sold to HBM3 will be used for HBM4 as well" (re-fetched 2026-11-21) | QUALITATIVE | **Undercuts**: the uplift named is wafer volume, and the installed base is reused | [5] |
| CO-7 | 2025-11-10 | Q3 2025 call | "the move to HBM4 is going to be what we call inspection and metrology intensive because the bumps are getting tighter. There are going to be more bumps, the density grow, they will need to do more inspection and metrology." | QUALITATIVE | Supports intensity (not a step count) | [6] |
| CO-8 | 2026-02-18 | Q4 2025 call | "there is a lot more dense structures. The requirements are much higher. It is more metrology and inspection intensive." Also: capabilities "will enable us to increase our market share by penetrating into more inspection and metrology steps" | QUALITATIVE | Supports intensity; "more steps" framed as **share gain**, not as step count growth | [7] |
| CO-9 | 2026-10-14 | Analyst Day | "increased complexity contributes more inspection and metrology steps, but also contributes to demand of new tools beyond the capability of the installed tool base." HBM example: "today, we measure wafer warp for a spec of 1 mm… moving to die… warp metrology, as required with specking the HBM specs… a tighter spec of 100 µm and even lower. This cannot be met with a current sensor." Bump height "as small as 6 μm today… 5 μm and possibly even down to 3 μm"; 10th-gen sensor in 2027. | QUANTIFIED (warp spec, bump height); QUALITATIVE (steps) | Supports a *new tool demand* channel (die-warp, sub-5 µm bumps). The roadmap tools ship 2027–28 | [10][11] |
| CO-10 | 2026-10-14 | Analyst Day Q&A | Ramy Langer, replying to Needham: "We do not see this hesitancy… there is a tendency not to go with higher memory density in each of the module, actually to reduce it. But… they are adding a lot of capacity." | QUALITATIVE | Admits per-module memory content is falling; growth framed as capacity | [10] |
| CO-11 | 2026-11-04 | Q3 2026 call (latest) | "As advanced packaging becomes more complex, it requires more inspection and metrology steps". On HBM versus GPU: "the main opportunity for us is to gain market share in 2D for additional steps. This is not really specific that I can tell you whether it's a GPU or HBM." HBM4/HBM4E **not mentioned** in the call (re-fetched 2026-11-04 transcript, 2026-11-21) | QUALITATIVE | The latest wording generalizes away from HBM4 | [12][13] |
| CO-12 | FY2024, FY2025 | 20-F | "new packaging technologies, such as Chiplets and HBM, require more inspection and metrology steps"; "Camtek provides 100% inspection and metrology of all the components in the stack" | QUALITATIVE | Generic; not generation-specific | [14] |

**Bottom line on who claims it:** the claim is Camtek's. Its strongest form is CO-5 (May 2025) and CO-7 (Nov 2025). No Camtek statement gives a count of steps per HBM3E, HBM4 or HBM4E stack or wafer. No Camtek statement gives dollars per HBM wafer or tools per unit of HBM capacity. (Confirmed: notes/05 reviewed 15 calls, the investor day, three 20-Fs and the order releases. This review re-checked the calls cited above.)

---

## 2. Evidence for the claim

| # | Evidence | Tag | Date | Type | What it does and does not show | Src |
|---|---|---|---|---|---|---|
| F1 | Camtek statements CO-5, CO-7, CO-8 and CO-9 (above) | [CO] | 2025-05-13 to 2026-10-14 | QUALITATIVE (steps); QUANTIFIED (warp 1 mm → 100 µm; bump height 6 → 5 → 3 µm) | Company assertion only | [4][6][7][10][11] |
| F2 | KLA: "if you look at the requirements for HBM, I think it's increased [process control intensity] another point or so… the device is only as good as the weakest DRAM… you can't bin these devices." | [IND] (another equipment maker) | 2025-10-29 | QUANTIFIED (about +1 point of process-control intensity) | Shows HBM raises **DRAM front-end** process-control intensity (KLA's market), not packaging steps. It is not an HBM3E → HBM4 comparison. | [21] |
| F3 | Onto CEO: "process control intensity for packaging continues to increase and increased fairly dramatically"; "customers are deploying a lot more process control"; "that drives a higher sampling rate and thus a higher capital intensity." (re-fetched 2026-11-21) | [IND] (competitor) | 2026-11-09 | QUALITATIVE | Supports rising **packaging** intensity in general. Not HBM4-specific, and not steps per stack. | [20] |
| F4 | Onto G5 release: a leading HBM maker's evaluation covered "several applications critical to HBM4 yield"; ML recipes are "a key advantage for customers with a large number of inspection steps." | [IND] (competitor) | 2026-03-16 | QUALITATIVE | HBM4 has many inspection applications. The same release says Onto displaced the incumbent (see A6). | [19] |
| F5 | Bump scaling: "HBM3E features 30- to 20-micron bumps, but HBM4 will likely scale down to the 10-micron level"; "Bump scaling is pushing defect inspection to the limit"; "It's critical to catch these marginal defects using early inspection steps." | [IND] (trade press; partly quotes Onto) | 2025-11-11 | QUANTIFIED (bump pitch/size) | Harder inspection per wafer. Does not show more *steps*. | [23] |
| F6 | JEDEC HBM4 standard (JESD270-4) doubles the interface to 2,048 bits and channels from 16 to 32 per stack | [IND] | 2025-04-21 | QUANTIFIED | More I/O, so more bumps per die. Camtek's own Feb 2025 answer says bumps per wafer stay ">100 million… not going to go to 300 million" [3]. | [26] |
| F7 | HBM4 yields "considerably lower than… HBM3E… at all three DRAM makers" (Hanwha analyst Park Jun-young); warpage is a new bottleneck | [IND] (sell-side via trade press) | 2026-06-04 | QUALITATIVE | Lower yield usually raises process-control demand. The article names **backside-deposition** equipment as the beneficiary, not inspection. | [31] |
| F8 | SK hynix added 3D inspection units to the 12-high HBM3E line to raise yield | [IND, secondary] | 2024-10-31 | QUALITATIVE | Evidence of **added inspection with taller stacks**. It is within HBM3E (8 → 12-high), not HBM4, and the vendor named is Nextin, not Camtek (see A5). | [33] |
| F9 | SK hynix gave Onto a Best Partner Award for "a defect prevention system… for HBM", noting "HBM stacks [are] becoming thinner and more complex" | [IND] (customer, via competitor release summary) | 2026-09-28 event | QUALITATIVE | Customer confirmation that HBM defect control matters. The credit goes to a competitor. Not re-verified at source. | [38] |
| F10 | Samsung and SK hynix "expand microscope procurement to boost HBM yield"; "rising need for HBM testing and failure analysis is reshaping semiconductor inspection equipment markets" | [IND] | 2026-03-26 | QUALITATIVE (headline and teaser only) | More inspection/FA spending, but of an unspecified type (microscopes/FA, likely lab, not inline optical AOI). | [37] |
| F11 | Camtek orders tied to HBM4: more than $260M "order and forecast" from two HBM makers for 2026–27 (2026-05-12); a Hawk-only order of more than $50M from "a leading HBM player" for 2027 delivery (2026-06-02); HBM players more than 20% of the more than $600M in H1-2026 orders (2026-08-10) | [CO] | 2026 | QUANTIFIED | Shows HBM4-period demand exists. Does **not** separate capacity additions from added steps per stack. Camtek itself attributes the orders to "the transition to HBM4 together with continued capacity expansion" [9]. | [8][16][9] |
| F12 | Camtek roadmap items aimed at HBM: die-warp metrology to ≤100 µm, 10th-gen sensor for bumps under 5 µm, TSV depth (2027–28) | [CO] | 2026-10-14 | QUANTIFIED (specs) | Potential future addressable steps. Not yet products or revenue. | [10][11] |
| F13 | Asia Economy: Hawk "capable of testing up to 16 layers of HBM3E"; "25 units have been ordered… an additional 50 units will be contracted within this year" | [CO-relayed] | 2025-02-20 | QUANTIFIED | Relays Camtek. Contradicts Camtek's "we scan wafers" (see Contradictions). | [18] |

**Assessment of the "for" side:**
- Independent evidence (F2–F10) consistently supports **higher process-control difficulty and intensity in HBM generally and in HBM4**: finer bumps, more I/O, thinner and warpier wafers, lower yields.
- None of it counts steps. None shows the increase is **per stack**. None shows it accrues to **Camtek's** tool classes.
- The only "more steps" statements are [CO].

---

## 3. Evidence against the claim

| # | Evidence | Tag | Date | Type | Why it undercuts C1 | Src |
|---|---|---|---|---|---|---|
| A1 | Camtek, May 2024: "we scan wafers… it really doesn't matter whether it will be an eight-stack or a 12-stack… is there here any upside for ASP improvement? No there isn't"; "whether they will do it a stack of eight, 12, or 16, this really does not make any -- does not require any changes" | [CO] | 2024-05-09 | QUALITATIVE | Camtek's own model is per **wafer**, not per stack. Stack height does not change its tool or ASP. This contradicts the "per stack" part of C1. | [1] |
| A2 | Camtek, Aug 2025, on "content uplift" HBM3E → HBM4: "we will scan more wafers. There is some change in the number of bumps, some pitch differences"; "most of the equipment that we sold to HBM3 will be used for HBM4 as well" | [CO] | 2025-08-05 | QUALITATIVE | When asked directly about content uplift, management named wafer volume and acknowledged installed-base reuse. It did not name added steps. | [5] |
| A3 | Camtek, Feb 2025: bumps per HBM wafer "over [100] million… stays in this range at least for the foreseeable future. It's not going to go to [300] million." | [CO] | 2025-02-12 | QUANTIFIED | Limits the "more bumps" mechanism later cited in Nov 2025 (CO-7). | [3] |
| A4 | Onto CEO, asked about "the shift from HBM4 to 4E and the opportunity it presents": "from a packaging perspective, it's going to be driven a lot by volume"; "It's all about the wafers for us, the number of wafers being used to support that GPU or that processor"; "as long as… the wafer content stays the same or more"; HBM versus 2.5D growth "about the same"; "we haven't seen that big of a process control shift between the high-end technologies being used." (re-fetched 2026-11-21) | [IND] (main competitor) | 2026-11-09 | QUALITATIVE | The closest independent answer to C1's HBM4 → HBM4E question attributes demand to **volume**, with wafer content flat or higher, not to added steps. | [20] |
| A5 | Nextin (Korea) Kroki HBM inspection tool, developed at SK hynix's request and on the HBM3E 12-high line. It "detects defects that arise when DRAM dies are stacked vertically, such as warpage and cracks". Contracts of about KRW 10.64bn (disclosed 2025-05-22) and about KRW 6.4bn (2025-04-29). Analyst expects 15 units delivered in 2025. Nextin plans to add wafer-level inspection and 3D metrology. | [IND] | 2025-05-24 | QUANTIFIED | Inspection steps added for **taller stacks** (the per-stack dimension) went to a Korean vendor, not Camtek. Nextin's 3D-metrology plan targets Camtek's core step. | [32][33] |
| A6 | Onto G5: a leading HBM maker ordered double-digit G5 units "to support the majority of their 2D inspection needs and a similar number of orders for 3Di technology, displacing the previously established tool of record", with shipments from Q2 2026 | [IND] (competitor; PDF re-read) | 2026-03-16 | QUANTIFIED (double-digit units) | Even where HBM4 steps exist, they are contested. The displaced vendor is not named, so this is **not proof** that Camtek lost. Camtek's "tool of reference for all the 3D metrology for HBM4 at all the HBM manufacturers" claim (Nov 2025) [6] is in tension with it. | [19][6] |
| A7 | X-ray inspection: SEC (Korea) signed a KRW 5.8bn contract with Micron Singapore for NF120 X-ray inspection systems for HBM mass production. "The Micron order demonstrates the growing importance of X-ray inspection in HBM manufacturing." SEC is "seeking to enter the market for inline HBM inspection equipment." | [IND] | 2026-11-10 | QUANTIFIED | Part of the incremental HBM inspection demand is X-ray. Camtek does not sell X-ray (product map in notes/01). | [34] |
| A8 | CT inspection: Techvalley delivered one Teraton 3D X-ray CT system each to Samsung and SK hynix for HBM R&D (standard model about KRW 1bn). Used for "internal voids, bonding defects and micro-bump issues in HBM". An inline version is in development. | [IND] | 2026-04-13 / 2026-07-30 | QUANTIFIED | Post-stack defect detection (voids, bonding) is moving toward X-ray/CT. That is a technology Camtek does not offer. Camtek's own post-bond void tool is roadmap-only [11]. | [35] |
| A9 | Market-research view: X-ray is expected to be the largest share of HBM inspection equipment, "owing to its critical role in non-destructively detecting internal TSV voids and bond-line defects" | [IND, low quality] | 2026-08 | QUALITATIVE | Directional only. The source's own market sizes conflict. | [40] |
| A10 | Localization pressure: Youngwoo DSP VEGA S-1000 2D/3D bump AOI. Claims 103 WPH vs 42 WPH for competitors, defects ≥1.7 µm, bumps ≤5 µm. In validation at a Korean foundry; discussions with "a Korean memory-chip maker… about 40% complete". TheElec: the market is "dominated by… Israel's Camtek and U.S.-based Onto Innovation and KLA". | [IND] (vendor claims via trade press) | 2026-09-13 | QUANTIFIED (vendor claims, unverified) | More vendors are competing for the same HBM steps, which narrows the Camtek-addressable share. Throughput claims are unverified. | [36] |
| A11 | Stack height may fall: GPU/ASIC makers reportedly weighing cutting HBM per device from 12-high to 8-high because of HBM price rises (HBM ASP +121% YoY forecast for 2027). 8-high per-Gb price expected 10–20% above 12-high. | [IND] | 2026-09-30 (TrendForce 2026-09-29) | QUANTIFIED | Directly undercuts "per stack": fewer DRAM dies per stack. Camtek itself acknowledged a "tendency… to reduce" memory density per module [10]. | [28][10] |
| A12 | 16-high adoption limited: "discussions… on 16-high HBM remain limited… 12-high HBM4E products are still expected to remain the mainstream"; hybrid bonding's "earliest adoption" is 16-high HBM4E | [IND] | 2026-07-07 | QUALITATIVE | The largest step-adders (16-high, hybrid bonding) are later or narrower than the claim implies for HBM4/HBM4E. | [27] |
| A13 | Hybrid bonding delayed. Camtek: "slower than we expected"; "in 2027, I do not expect to see any substantial business coming from hybrid bonding"; HBM5 "is going to continue to be based on bumps". Independent: hybrid bonding to "debut in HBM4E and HBM5 at the end of the decade". | [CO] + [IND] | 2026-09-02 to 2026-11-04 | QUALITATIVE | The new step categories Camtek names (sub-150 nm pre-bond particles, Cu dishing, post-bond voids) mostly belong to hybrid-bonded stacks. They are therefore not part of mainstream HBM4/HBM4E. | [10][12][39] |
| A14 | KLA CEO: "over time, people will learn more about it, and they won't inspect at the frequency. So… the growth will continue, but it won't continue at the rate we've had" | [IND] | 2025-10-29 | QUALITATIVE | Sampling may fall as HBM yields mature. That offsets per-generation step additions. Camtek's "100% inspection" frame conflicts with it. | [21][3] |
| A15 | Needham analyst at the Camtek Analyst Day: "there seems to be some hesitation… customers have some hesitation to buy the dedicated 3D bump metrology. 2D is still ongoing for HBM-related demand… Interpretation may be they are kind of stuck in the limbo of HBM de-spec." Camtek denied it: "We do not see this hesitancy". | [IND, hearsay] | 2026-10-14 | QUALITATIVE | An independent channel signal against rising HBM 3D-metrology demand, which is Camtek's strongest HBM step. Sources are not named and the evidence is weak. | [22][10] |
| A16 | Part of HBM4 yield control is shifting to electrical test and DFT: "The number of test insertions for a 12-stack die can range from 3 to 12"; "Intermediate testing during the assembly process is becoming increasingly critical." Korean press reports HBM4-dedicated wafer testers ordered from DI/Digital Frontier and UniTest. | [IND] | 2026-05-12 | QUANTIFIED (test insertions) | The growth in HBM quality-control steps that is documented is in **electrical test**, a different equipment class. This does not refute optical steps but competes for the same yield-control budget. | [25] |
| A17 | Camtek's HBM weight has not risen through the HBM4 transition (DERIVED, see §5). Q1 2024 HBM = 40% of revenue. Mid-2026 HBM players = "over 20%" of orders. | [CO] data, DERIVED | 2024-05-09; 2026-08-10; 2026-11-04 | QUANTIFIED | If HBM4 added much Camtek content per wafer on top of capacity growth, HBM's share would be expected to rise, not fall. The two shares use different bases (revenue vs orders), so this is indicative only. | [1][17][9][12] |

---

## 4. Re-checks at source (this review)

| Item | Result |
|---|---|
| Q1 2024 call "we scan wafers… no ASP upside" | **Confirmed** verbatim on the Motley Fool page (re-fetched 2026-11-21) [1]. |
| Q2 2025 call "will be used for HBM4 as well", "scan more wafers", "some change in the number of bumps" | **Confirmed** verbatim (re-fetched) [5]. |
| Q3 2026 call: step language and HBM4 mentions | **Confirmed.** The step language is generic to "advanced packaging". The fetched transcript contains no mention of "HBM4" or "HBM4E". "the main opportunity for us is to gain market share in 2D for additional steps. This is not really specific… whether it's a GPU or HBM" [12]. The Q3 2026 script slide says "More inspection and metrology steps, as well as new tools" without naming HBM [13]. |
| Q3 2025 / Q4 2025 "inspection and metrology intensive" | **Confirmed** in local transcript copies [6][7]. |
| Q4 2024 ">100 million bumps… not 300 million" and "intensity will probably grow" | **Confirmed** in local copy (transcript renders "million" as "€… million") [3]. |
| Analyst Day: steps × beyond-installed-base, die-warp 1 mm → 100 µm, Needham "hesitation" question, "tendency… to reduce" density | **Confirmed** in local Quartr copy [10]. |
| Onto Q3 2026 "driven a lot by volume… all about the wafers" | **Confirmed** (re-fetched) [20]. |
| Onto G5 "displacing the previously established tool of record" | **Confirmed** in release PDF text [19]. |
| KLA "another point or so" and "won't inspect at the frequency" | **Confirmed** in local transcript copy [21]. |
| TrendForce 2024-09-30 Samsung TSV 120K → 170K wafers/month (end-2024 → end-2025); SK hynix +25% | **Confirmed** (re-fetched) [30]. |

---

## 5. DERIVED arithmetic (indicative only)

1. **Q1 2024 HBM revenue (DERIVED).** 40% × $97.0M (Q1 2024 revenue) = **≈ $38.8M** for the quarter, mostly HBM3/HBM3E [1][17].
2. **H1-2026 HBM order rate (DERIVED, lower bound).** Over 20% × over $600M = **over $120M** of orders from HBM players, 2026-01-01 to about 2026-08-10 [9]. That period is about 7.3 months, or about 2.43 quarters (7.3 / 3). $120M / 2.43 ≈ **over $49M per quarter** in orders. Caveats: orders are not revenue, and the figure includes HBM4 capacity additions.
3. **Two-customer HBM figure (DERIVED).** Over $260M of "order and forecast" across 2026–27 [8]. $260M / 8 quarters = **over $32.5M per quarter** on average. This is two customers only, includes forecast, and is a floor ("exceeding").
4. **Reading.** On these figures, Camtek's HBM-related order rate in the HBM4 period (about $49M/quarter, lower bound) is about **1.3×** its Q1 2024 HBM revenue rate (DERIVED: 49 / 38.8 ≈ 1.26). Over a similar span, TrendForce had Samsung's TSV capacity rising 120K → 170K wafers/month (+42%, DERIVED: 170/120 = 1.42) from end-2024 to end-2025, with SK hynix +25% [30]. By 2026, trade-press estimates put Samsung and SK hynix at about 150K–200K HBM wafers/month **each** and Micron heading to about 100K by end-2026 [29]. **These numbers cannot isolate steps per stack.** Bases differ (orders vs revenue; TSV vs DRAM wafers), and there is no 2024 industry total. They show **no sign** of Camtek HBM content growing much faster than HBM wafer capacity. That is what C1 would predict if steps per stack were rising materially. (Not an estimate of intensity; no ESTIMATE produced.)
5. **Dies per stack (DERIVED).** 12-high → 8-high = −33% DRAM dies per stack (8/12 = 0.667) [28]. 12-high → 16-high = +33% (16/12 = 1.333). Per Camtek's own wafer-based model [1], the per-stack framing tracks dies per stack × wafers. It is not a per-wafer step count.

---

## 6. Ruling

- **Survives:** HBM4 is harder to make than HBM3E. Bumps are finer, I/O is higher, dies are thinner with tighter warpage, and yields are lower. Independent sources [21][23][26][31] and a competitor [20] agree that packaging process-control intensity is rising. Camtek has a plausible path to new HBM-related steps in 2027–28: die-warp metrology and sub-5 µm bump sensors [10][11].
- **Does not survive scrutiny as stated:**
  - **"per stack":** Camtek's own model is per wafer [1]. Stack heights may fall (12 → 8-high) [28], and 16-high is limited [27].
  - **"adds inspection steps":** no step count exists from any party. The competitor ties HBM4 → HBM4E demand to volume [20]. Camtek itself named wafer volume and installed-base reuse when asked about the HBM3E → HBM4 content uplift [5].
  - **"Camtek-addressable":** stacking and post-bond defect inspection is going partly to Nextin, X-ray and CT vendors [32][34][35]. HBM4 2D/3D steps are being contested by Onto [19] and new Korean entrants [36]. Hybrid bonding, the clearest step-adder, is pushed out [12][27].
- **Verdict: partly supported (medium confidence).** The narrow, quantified version, "HBM4/HBM4E add N Camtek-addressable steps per stack", is **unresolved**, because nothing measures it.

---

## 7. What would change the verdict

Toward **supported**:
- A memory maker, OSAT, or independent analyst (Yole, TechInsights, TrendForce) publishing a count of optical inspection or metrology steps per HBM3E vs HBM4/HBM4E wafer or stack.
- Camtek disclosing HBM revenue per HBM wafer, or tools per 10K wafers/month, by generation. Camtek promised a capacity-per-system figure in Aug 2023 and never gave one.
- Evidence that HBM-related Camtek revenue grows faster than HBM TSV wafer capacity over 2026–27, for example HBM share of revenue rising back above the Q1 2024 level of 40%.
- Orders for Camtek's die-warp metrology or 10th-generation sensor from HBM makers specifically for HBM4E steps that did not exist at HBM3E.
- Independent trade-press confirmation that Camtek won new (not replacement) HBM4 steps at SK hynix, Samsung or Micron.

Toward **not supported**:
- Confirmation that the "tool of record" Onto displaced at a leading HBM maker [19] was Camtek.
- Reports of HBM bump-inspection sampling falling below 100% as HBM4 yields mature.
- Confirmed GPU/ASIC moves to 8-high HBM4/HBM4E [28].
- HBM players' share of Camtek orders falling further while industry HBM capacity grows.
- Further X-ray, CT or Korean-vendor wins for inline HBM inspection [34][35][36].

---

## 8. Dated next checkpoints

| Date (status) | Event | What to look for |
|---|---|---|
| Late Jan 2027 (expected; KLA reported its Dec-2025 quarter on 2026-01-29) | KLA December-2026-quarter call | Any update on HBM process-control intensity (the "another point" estimate) or packaging sampling trends [21]. |
| Early–mid Feb 2027 (expected; Onto Q4 2025 call timing; date not yet announced) | Onto Q4 2026 results | Dragonfly G5 and 3Di shipments to HBM makers that began in Q2 2026 [19]. Onto said 2027 G5 POs "already represent a doubling of 2026 Dragonfly G5 revenue" [20]. |
| Feb 2027 (expected) | SEMICON Korea 2027 | Camtek, Onto and Korean-vendor HBM4E inspection announcements; Nextin or Youngwoo DSP memory-maker qualifications [32][36]. |
| About mid-Feb 2027 (expected; Q4 2025 results were 2026-02-18; date not yet announced) | Camtek Q4/FY2026 results and call | Whether Camtek gives HBM revenue or order share for FY2026; any HBM4E step statements; delivery status of the over $260M HBM orders-plus-forecast [8]. |
| About mid/late Mar 2027 (expected; FY2025 20-F filed 2026-03-19) | Camtek FY2026 20-F | Whether the "HBM… require more inspection and metrology steps" language changes; customer concentration (which HBM makers are above 10%). |
| 2027 (Camtek guidance) | Camtek 10th-generation bump-height sensor launch (<5 µm bumps) [11]; delivery of the over $50M Hawk HBM order [16] | First Camtek tool tied to a new HBM spec; whether HBM makers order it. |
| 2027 (operations start, per TheElec) | Micron Singapore HBM / advanced-packaging facility ($7bn) [34] | Tool mix for inspection (optical vs X-ray) at a new HBM fab. |
| Late 2027 (TrendForce, via EE Times Japan) | HBM4E mass-production ramp [28] | Whether HBM4E adds new optical inspection or metrology steps; stack-height mix (8 / 12 / 16-high). |
| 2027–2028 (pending) | JEDEC decision on HBM5 package height (900–1,000 µm discussed) and memory-maker hybrid-bonding choice for 16-high HBM4E [27] | If hybrid bonding enters HBM4E 16-high, new step categories (pre-bond particle, dishing, post-bond void) become relevant to C1. |
| About May 2027 (expected) | Camtek Q1 2027 call | HBM 2027 magnitude, which Camtek said in Nov 2026 would be "significant" but declined to size [12]. |

---

## Contradictions

1. **Camtek's per-stack vs per-wafer framing (Camtek earlier vs later).**
   - May 2024: stack height "doesn't change our business… we scan wafers… no ASP upside" [1].
   - Feb 2025: "intensity will probably grow as you're putting more and more dies in the same module" [3].
   - Nov 2025: HBM4 "inspection and metrology intensive" [6].
   - Aug 2025, when asked about content uplift, the answer was "scan more wafers" plus installed-base reuse [5].
2. **"More bumps" (Nov 2025 [6]) vs "stays in this range… not going to go to 300 million" (Feb 2025 [3]).** Both are Camtek.
3. **Camtek "tool of reference/record for all the 3D metrology for HBM4 at all the HBM manufacturers" (2025-11-10 [6]) vs Onto.** Onto's release says it won "a similar number of orders for 3Di technology" (3D bump metrology) at a leading HBM maker, "displacing the previously established tool of record" (2026-03-16 [19]). The displaced vendor is not named.
4. **Camtek denies HBM 3D-metrology hesitation (2026-10-14 [10]) vs Needham's channel report of "hesitation… to buy the dedicated 3D bump metrology" (same event [22]).**
5. **Memory density per module.** Camtek, May and Nov 2025: a "major change in the density of the memory" in 2027 [4][6]. Camtek, Oct 2026: "tendency… to reduce" density per module [10]. Independent TrendForce, Sep 2026: 12-high → 8-high under consideration [28].
6. **"Up to 16 layers" (Asia Economy, 2025-02-20 [18], CO-relayed) vs "we scan wafers… 8, 12, or 16… does not require any changes" (Camtek, 2024-05-09 [1]).**
7. **100% inspection (Camtek [3][14]) vs falling inspection frequency over time (KLA [21]) vs "higher sampling rate" (Onto [20]).** The two independent sources point in opposite directions on sampling.
8. **HBM5 interconnect.** Camtek: HBM5 "is going to continue to be based on bumps" [10]. Tom's Hardware: hybrid bonding to "debut in HBM4E and HBM5 at the end of the decade" [39]. TrendForce: earliest at 16-high HBM4E [27].

---

## Not found / not verified

- **Not found (any source):** a count of inspection or metrology steps per HBM3E, HBM4 or HBM4E wafer or stack, from Camtek, SK hynix, Samsung, Micron, TSMC, Onto, KLA, Yole, TechInsights, TrendForce or sell-side.
- **Not disclosed by Camtek:** HBM revenue share after Q1 2024 (only "over 20%" of H1-2026 orders); dollars per HBM wafer; tools per unit of HBM capacity; which HBM makers placed the 2026 orders.
- **Not found:** any independent report naming Camtek as winner or loser of a specific HBM4 inspection step at SK hynix, Samsung or Micron. TheElec's site search for "Camtek" returned one article (Youngwoo DSP, 2026-09-13), which names Camtek only as an incumbent.
- **Not verified:** the identity of the "tool of record" Onto displaced [19]; the Onto/SK hynix award text [38] (Business Wire 403); ETNews's 2026-11-15 report on SK hynix HBM4 back-end equipment talks (bonding, dicing, inspection), seen only as a search summary with no vendors named. The TechPowerUp page (https://www.techpowerup.com/354861/) returned 403.
- **Not reachable:** pulse.bot (host not in this session's allowed network domains), so the TheElec original was used instead.
- **Snippet or teaser only:** DigiTimes 2026-03-26 microscope-procurement article [37].
- **Not found:** an industry-wide 2024 HBM TSV capacity total to compare with 2026 estimates, so no intensity ESTIMATE was made.
- **Not found:** any Camtek statement on HBM4 logic base-die inspection (foundry-made), or on die-to-wafer stack inspection.
