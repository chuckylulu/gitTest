# Bonding equipment for chip stacking — thermo-compression (TC) bonders, hybrid (direct Cu-Cu) bonders D2W/W2W, thinning/dicing, inspection/metrology — notes as of 12 November 2026

Research date: 12 Nov 2026. Scope: equipment makers, and what memory and logic customers have qualified and ordered. HBM economics are excluded (covered elsewhere). No share prices, valuation multiples, market caps, price targets or share-price moves are collected here.

**Labels:**
- [P] primary — company release, filing or annual report
- [S] secondary — trade press, aggregator, call summary
- [A] analyst or market-research estimate
- [CC] company claim, unconfirmed by any outside party
- [D] derived by me from cited figures (arithmetic stated)

**Method caveat.** The session's shared web-search budget (200 per turn across all agents) ran out mid-workstream, and later the Exa and Firecrawl credits ran out too. After that, I fetched only pages already found or primary URLs I could construct: company IR pages, SEC EDGAR, annual-report PDFs. No search engine was used to get around the limit.

Primary documents obtained:
- Besi: Q3-2026 release (full PDF) and 2025 Annual Report
- Disco: Tanshin for Apr–Sep 2026
- Tokyo Electron: Q2 FY2027 Tanshin, presentation and Q&A
- ASMPT: Q3-2026 release and 5 Nov 2026 SMT decision
- SUSS: Q3-2026 quarterly statement and 27 Oct 2026 ad hoc
- Camtek: 6-K, Q3-2026
- Onto Innovation: 8-K, Q3-2026
- Kulicke & Soffa: 8-K, fiscal Q3-2026
- Applied Materials: 8-K of 26 Oct 2026 on the Besi stake

Coverage is still THIN for mainland China, Taiwan, India, EV Group volumes, Shibaura, Toray Engineering, Yamaha Robotics, Semes, Hanwha Semitech, KLA, Nova, Park Systems and Lasertec. Unverified items are flagged.

---

## (1) Segment map — companies worldwide

### Takeaway
HBM stacking is still a TC-bonder market in 2025–26. Hanmi held ~71% of HBM TC-bonder revenue through Q3-2025 (TechInsights), but SK hynix now buys from ASMPT and Hanwha as well.

Hybrid bonding (HB) runs in volume today mainly in logic. Besi is the D2W leader: per its annual report, six integrated Applied+Besi HB lines with 30 Besi bonders are installed at a leading logic customer. Applied is raising its Besi stake from ~9% (bought April 2025) to ~20%.

W2W bonding (EV Group, Tokyo Electron, SUSS) is an older, separate market. Disco is the thinning/dicing constraint in both eras. Inspection "judges" (Camtek, Onto, KLA) gate bump and stack quality; HB inspection is still small. India appears to have no relevant equipment maker (not re-verified).

### Cited Findings

**Map table.** Evidence column: a link means sourced in this session; "UNVERIFIED" means background knowledge not re-confirmed in H2-2026 sources (see §7).

| Company | Home | Listing / ticker | Role in segment | Why it matters / why left out | Evidence |
|---|---|---|---|---|---|
| BE Semiconductor Industries (Besi) | Netherlands | Euronext Amsterdam: BESI (OTC: BESIY) | D2W hybrid bonders; TC Next TC bonders; flip-chip and multi-module die attach; photonics | D2W HB leader: 23 HB customers and >215 systems cumulative demand (Q3-26) [CC]. TechInsights shares in die attach and advanced die placement (below). Applied raising stake to ~20% | [Besi Q3-2026 PDF, 22 Oct 2026](https://www.besi.com/fileadmin/user_upload/PR_Q3-2026.pdf); [Besi Annual Report 2025](https://www.besi.com/fileadmin/data/Investor_Relations/_Semi__Annual_Reports/Annual_Report_2025.pdf) [P] |
| Hanmi Semiconductor | South Korea | KRX: 042700 | HBM TC bonders (TC Bonder 4 / 4.5 "Griffin"); Wide TC bonder (planned late 2026); HB plant (target end-2026); 2.5D/FC bonders | HBM TC share leader: 71.2% of revenue cumulative to Q3-2025 (TechInsights) | [Asia Economy, 22 Dec 2025](https://view.asiae.co.kr/en/article/2025122209224722092) [S/A]; ticker per [Akrostec](https://www.akrostec.com/indices/AKMNF50/events/2026-06-08t00-00-00z-hanmi-semiconductor-co-ltd-042700-other-17a77ad0) |
| ASMPT | Singapore HQ, Hong Kong-listed | HKEX: 0522 | TC bonders (C2S, C2W, HBM); 2nd-gen HB at sampling; photonics/CPO (AMICRA); SMT (retained 5 Nov 2026) | ~Half of SK hynix's ~50 HBM4 TC sets (Dec 2025). Record bookings Q3-26 | [ASMPT Q3-2026 release, 28 Oct 2026](https://www.asmpt.com/en/investor-relations/news-events/asmpt-announces-2026-third-quarter-results-record-group-bookings-and-strong-earnings-across-semi-smt/) [P]; [TrendForce/The Elec, 12 Dec 2025](https://www.trendforce.com/news/2025/12/12/news-sk-hynix-reportedly-places-hbm4-tc-bonder-order-with-asmpt-as-hanmi-hanwha-patent-clash-heats-up/) [S] |
| Semes | South Korea | Private (Samsung Electronics subsidiary) | Captive TC bonders for Samsung HBM; going "straight to hybrid bonders" | No. 2 HBM TC share: 13.1% (TechInsights, cumulative to Q3-2025) | [Asia Economy, 22 Dec 2025](https://view.asiae.co.kr/en/article/2025122209224722092); [MTN, 13 Feb 2026](https://news.mtn.co.kr/news-detail/2026021317395078451) [S] |
| Hanwha Semitech | South Korea | Not separately listed (Hanwha group; parent listing UNVERIFIED) | TC bonders for SK hynix (2025 contracts); 2nd-gen HB "SHB2 Nano"; D2W HB cluster reportedly under SK hynix evaluation | SK hynix second/third source; in a patent dispute with Hanmi | [TrendForce, 12 Dec 2025](https://www.trendforce.com/news/2025/12/12/news-sk-hynix-reportedly-places-hbm4-tc-bonder-order-with-asmpt-as-hanmi-hanwha-patent-clash-heats-up/); [TrendForce, 7 Oct 2025](https://www.trendforce.com/news/2025/10/07/news-hybrid-bonder-equipment-market-reportedly-near-2b-by-2028-as-korean-makers-race-to-next-gen-hbm-tools/) [S] |
| Yamaha Robotics (Shinkawa) | Japan | Subsidiary of Yamaha Motor (parent ticker UNVERIFIED) | TC bonders (Micron, Samsung) | 5.6% HBM TC share (TechInsights, cumulative to Q3-2025) | [Asia Economy, 22 Dec 2025](https://view.asiae.co.kr/en/article/2025122209224722092) [S] |
| Toray Engineering | Japan | Subsidiary of Toray Industries (UNVERIFIED) | TC bonders; historical Samsung supplier | Minor in HBM by 2025 (absent from TechInsights top 4) | [Asia Economy, 2024](https://view.asiae.co.kr/en/article/2024071607095917092) [S, dated] |
| Kulicke & Soffa | US-incorporated; operating HQ Singapore | Nasdaq: KLIC | Fluxless TC bonders (formic-acid, plasma) | FQ3-26 revenue US$330.4m; Advanced Solutions plant expansion due H2 FY2027 | [K&S 8-K Ex.99.1, 5 Aug 2026](https://www.sec.gov/Archives/edgar/data/56978/000005697826000030/ex991liveq32026.htm) [P] |
| Applied Materials | US | Nasdaq: AMAT | Co-develops integrated D2W HB systems with Besi ("Kinex"); EPIC Center; ~9% → ~20% Besi stake | Front-end giant entering HB through a specialist alliance | [Applied 8-K Ex.99.1, 26 Oct 2026](https://www.sec.gov/Archives/edgar/data/6951/000162828026067303/ex991prforprojectbasil.htm) [P] |
| Tokyo Electron (TEL) | Japan | TSE: 8035 | W2W bonders and laser debond (product details UNVERIFIED); dominant front-end coat/develop, etch, deposition; probers | Group quality; expects "3D integration of advanced packaging to grow significantly from CY2027" [CC] | [TEL Q2 FY2027 presentation, 30 Oct 2026](https://www.tel.com/ir/library/report/i61j9u00000000gf-att/fy27q2presentations-e2.pdf); [Q&A](https://www.tel.com/ir/library/report/i61j9u00000000gf-att/FY27Q2_EarningCall_QA_E.pdf) [P] |
| EV Group (EVG) | Austria | Private | W2W fusion/hybrid bonders; D2W collective bonding; temporary bonding | Believed W2W leader (UNVERIFIED). 2026: with imec, showed W2W HB at 200 nm interconnect pitch [CC]; topped TechInsights customer-satisfaction survey for 14th year | [EVG news list, accessed 12 Nov 2026](https://www.evgroup.com/company/news/) [P, titles only] |
| SUSS MicroTec | Germany | Xetra: SMHN | Temporary bonding/debonding (TSV wafers incl. HBM); permanent bonders (W2W HB UNVERIFIED); coaters; UV scanners incl. panel | Record order book (€600.6m), but 9M sales −22% and FY26 guidance cut | [SUSS Q3-2026 statement, 5 Nov 2026](https://www.suss.com/en/content/download/3521/file/2026_11_05_SUSS_Quarterly%20Statement%20as%20of%20September%2030,%202026.pdf) [P] |
| Shibaura Mechatronics | Japan | TSE (ticker UNVERIFIED) | Flip-chip / D2W bonders incl. HB (UNVERIFIED) | On the coordinator's list; no 2026 evidence gathered | UNVERIFIED |
| LG Electronics (production-technology unit) | South Korea | KRX (ticker UNVERIFIED) | Developing HBM hybrid bonders; mass production targeted by 2028 | Possible entrant | [TrendForce citing SeDaily, 7 Oct 2025](https://www.trendforce.com/news/2025/10/07/news-hybrid-bonder-equipment-market-reportedly-near-2b-by-2028-as-korean-makers-race-to-next-gen-hbm-tools/) [S] |
| ASML | Netherlands | Euronext: ASML | Not a D2W HB competitor according to Besi; joint die-stress / placement-accuracy work | Left out as a bonder | [Besi Q3-2026 PDF](https://www.besi.com/fileadmin/user_upload/PR_Q3-2026.pdf) [P, CC] |
| Disco | Japan | TSE: 6146 | Grinders (thinning), dicers (blade, laser), consumables (blades, wheels) | Thinning/dicing constraint in both eras; record shipments | [Disco Tanshin, 22 Oct 2026](https://www.disco.co.jp/jp/ir/library/doc/fr/fr20261022.pdf) [P] |
| Tokyo Seimitsu (Accretech) | Japan | TSE (ticker UNVERIFIED) | Grinders/polishers, dicers, probers | Likely No. 2 to Disco; no 2026 data gathered | UNVERIFIED |
| EO Technics | South Korea | KOSDAQ (ticker UNVERIFIED) | Laser grooving/dicing | Not verified | UNVERIFIED |
| Camtek | Israel | Nasdaq: CAMT | 2D/3D inspection and metrology for advanced packaging, HBM, CoWoS | Closest pure-play "judge"; advanced packaging ~80% of sales | [Camtek 6-K, 4 Nov 2026](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326005000/zk2636329.htm) [P] |
| Onto Innovation | US | NYSE: ONTO | Packaging inspection (Dragonfly G5, Firefly), OCD metrology (Atlas G6); 27% Rigaku stake (Aug 2026); inspection JDP with Samsung | Larger "judge"; record AP revenue Q3-26; backlog >US$1.3bn | [Onto 8-K Ex.99.1, 9 Nov 2026](https://www.sec.gov/Archives/edgar/data/704532/000119312526453582/onto-ex99_1.htm) [P]; [TrendForce, 1 Apr 2026](https://www.trendforce.com/news/2026/04/01/news-jedec-reportedly-plans-to-relax-hbm-height-specs-to-900%C2%B5m-potentially-slowing-hybrid-bonding-adoption/) [S] |
| KLA | US | Nasdaq (ticker UNVERIFIED) | Broad process control incl. packaging inspection | Likely the largest judge overall; no 2026 data gathered | UNVERIFIED |
| Nova | Israel | Nasdaq/TASE (UNVERIFIED) | Dimensional/materials metrology incl. advanced packaging | Not verified | UNVERIFIED |
| Park Systems | South Korea | KOSDAQ (UNVERIFIED) | Atomic-force microscopes (Cu pad recess and roughness, critical for HB) | Natural HB surface "judge"; not verified | UNVERIFIED |
| Lasertec | Japan | TSE (UNVERIFIED) | Mainly EUV mask inspection | Left out: little packaging relevance found | UNVERIFIED |
| Mainland China: Piotech (SSE STAR), U-Precision (unlisted), iSABers (private), Maxwell (SZSE), Kingsemi (SSE STAR), Hwatsing (thinning/CMP), GL Tech (dicing), Skyverse (inspection) | China | All tickers UNVERIFIED | HB/W2W bonders, temporary bonding, thinning, dicing, inspection | Domestic substitution; potential CXMT/YMTC suppliers; no 2026 evidence (Piotech site returned 503) | UNVERIFIED — region thin |
| Taiwan: Gallant Micro/GPM, Scientech, GPTC, All Ring, C Sun | Taiwan | All tickers UNVERIFIED | CoWoS-line die bonders/sorters, wet/debond, dispensing/AOI, curing | TSMC CoWoS supply chain; no 2026 evidence | UNVERIFIED — region thin (MOPS not reached) |
| India | — | — | No bonding, thinning, dicing or packaging-inspection equipment maker identified | Indian ATMP/OSAT projects import tools | UNVERIFIED (NSE/BSE not checked) |

**Segment-level facts: TC-bonder shares, customers, qualification, fluxless, disputes**

*Shares*
- HBM TC-bonder revenue share, cumulative Jan–Sep 2025 (TechInsights "2025 TC Bonder Market Report", as cited by Hanmi): Hanmi 71.2%, Semes 13.1%, ASMPT 5.6%, Yamaha Robotics 5.6%. TechInsights expects ~13% CAGR to 2030 and a rebound from 2026 after "a temporary normalization process for TC bonders in 2025" — [Asia Economy, 22 Dec 2025](https://view.asiae.co.kr/en/article/2025122209224722092) [A, relayed by an interested party]
- TechInsights (Dec 2025, as presented by Besi): Besi's share of die attach rose from 37% (2020) to 40%, 40%, 46% and 50% (2024). Its share of "advanced die placement" (<7 µm accuracy) was 81%, 79%, 78%, 81% and 82% over 2020–2024. Both exclude TCB, wire bonding and dicing — [Besi Annual Report 2025](https://www.besi.com/fileadmin/data/Investor_Relations/_Semi__Annual_Reports/Annual_Report_2025.pdf) [A via P]

*SK hynix sourcing*
- Hanmi was the exclusive HBM TC supplier until 2024. ASMPT joined near end-2024 (Oct-2024 order for HBM3E 12-high), and Hanwha Semitech entered in early 2025.
- In Apr-2025 Hanmi recalled ~60 support engineers, a move "widely viewed as a protest".
- In Nov-2025 SK hynix ordered seven dual-head ASMPT TC bonders (~KRW 30bn) for HBM4. About 50 TC sets were in HBM4 use, roughly half from ASMPT; Hanwha bonders were "not currently in use" (Dec 2025) — [TrendForce citing The Elec, 12 Dec 2025](https://www.trendforce.com/news/2025/12/12/news-sk-hynix-reportedly-places-hbm4-tc-bonder-order-with-asmpt-as-hanmi-hanwha-patent-clash-heats-up/) [S]
- Hanmi won a KRW 44.2bn TC Bonder 4.5 "Griffin" order for HBM4 (~15 tools, delivery by 2 Sep 2026) after a ~KRW 9.6–9.7bn Jan-2026 order — [TrendForce, 9 Jun 2026](https://www.trendforce.com/news/2026/06/09/news-sk-hynix-reportedly-places-44-2bn-won-tc-bonder-order-with-hanmi-accelerating-hbm4-ramp-up/); [Korea Times, 8 Jun 2026](https://www.koreatimes.co.kr/business/tech-science/20260608/sk-hynix-orders-new-equipment-worth-287-mil-for-next-gen-hbm4) [S]
- Patent dispute: Hanmi sued Hanwha in Dec-2024; Hanwha filed for invalidation in May-2025 and countersued around Oct-2025 [S, same TrendForce Dec-2025 source].
- Hanwha reportedly supplied an integrated D2W HB cluster to SK hynix for evaluation (single undated "exclusive" report) — [Digg aggregation](https://digg.com/tech/vvqd1wro) [S, unconfirmed]

*Other memory makers*
- Samsung: TC bonders mainly from Semes and Shinkawa (Toray historically) — [Asia Economy, 2024](https://view.asiae.co.kr/en/article/2024071607095917092) [S, dated]. No 2026 vendor split found.
- Micron: Shinkawa plus Hanmi; has tested ASMPT and Besi (Macquarie view) — [Tech Investments](https://www.techinvestments.io/p/hbmdie-bonding-semicap-outlook) [A/S]. No source found for CXMT.

*Qualification and fluxless*
- Qualified for HBM4: Hanmi TC Bonder 4 (mass production Jul-2025) and Griffin 4.5 (ordered Jun-2026); ASMPT tools in HBM4 use at SK hynix [S, sources above].
- Planned for HBM4E: SK hynix reportedly keeps MR-MUF/TC through HBM4 and HBM4E 16-high. Its 16-high HBM4 at CES 2026 used 30 µm DRAM to fit 775 µm — [TrendForce, 13 Jan 2026](https://www.trendforce.com/news/2026/01/13/news-sk-hynix-may-stick-with-mr-muf-for-hbm4-16-high-despite-asmpt-tc-bonder-orders/) [S]. Demand is rising for Hanmi's Wide TC Bonder — [TrendForce, 7 Jul 2026](https://www.trendforce.com/news/2026/07/07/news-samsung-sk-hynix-reportedly-reconsider-hybrid-bonding-timeline-16-high-hbm4e-may-be-earliest-adoption/) [S]
- Fluxless at SK hynix: evaluations for HBM4 16-high (from Q4-2025) "failed to meet expectations"; judged "premature given performance and cost" — [TrendForce citing DealSite, 13 Jan 2026](https://www.trendforce.com/news/2026/01/13/news-sk-hynix-may-stick-with-mr-muf-for-hbm4-16-high-despite-asmpt-tc-bonder-orders/) [S]
- Fluxless at K&S (FQ1-26 call, search-result excerpt only): ~120 TCB systems in the field, half fluxless; plasma fluxless in qualification at a major foundry; memory volume production expected FY2027 [CC] — [MarketBeat](https://www.marketbeat.com/instant-alerts/kulicke-and-soffa-industries-q1-earnings-call-highlights-2026-02-05/?.tsrc=rss) [S]

*Memory-maker purchase timing*
- ASMPT (H1-26): HBM tool purchase timing "remains dependent on HBM4 product rollout schedules"; exclusive joint evaluation programme with a key memory player — [ASMPT interim release, 1 Aug 2026](https://news.marketersmedia.com/asmpt-announces-2026-interim-results-multiple-advanced-packaging-solutions-drive-strong-performance/89199421) [P via wire]
- ASMPT (Q3-26): "memory makers are delaying larger bonding-tool purchases while they reassess the HBM4 roadmap" — [Dr. Web, 28 Oct 2026](https://www.drweb.de/asmpt-quartalszahlen-chipsparte-hbm/) [S]

### Inferences
- No 2026 TC-share data was found. Order flow suggests Hanmi's SK hynix share fell from ~100% (2024) toward roughly half for HBM4, with ASMPT taking most of the rest, and Hanmi regaining some volume in mid-2026 [D].
- Customer qualification gates decide supplier share more than supplier technology: SK hynix yield and lifetime bars, Samsung's captive Semes, and NVIDIA's stack-height choices.

### Gaps
- No 2026 TechInsights/Yole share by supplier or customer; no CXMT bonder data; no Samsung or Micron 2026 vendor split.
- Map rows marked UNVERIFIED (China, Taiwan, India, Shibaura, Toray, Tokyo Seimitsu, KLA, Nova, Park, Lasertec) need checking.

---

## (2) Evidence on tests (a)–(e) for key companies
Key companies: **Disco, Tokyo Electron, Besi, Camtek, ASMPT, Hanmi**. Short entries cover **Onto Innovation, SUSS and Kulicke & Soffa**. EV Group (private) and Applied (bonding portion) had too little evidence for full tests.

### Takeaway
- **Disco** and **Tokyo Electron** own physical/process constraints and earn recurring revenue: utilisation-linked consumables at Disco; 20.4% Field Solutions at TEL. Both have strong balance sheets.
- **Besi** has third-party share leadership in advanced die placement (82%, TechInsights) and the highest margins in the group (45.8% operating, Q3-26). It is also the most cyclical, with China at ~40% of revenue.
- **Camtek** and **Onto** are the clearest "judges", but their HB judge role lies in 2028 and later.
- **ASMPT** is diversified with lower margins (~17.6% adjusted operating, Q3-26); its HB is at sampling.
- **Hanmi** earns ~50% operating margins on a BRIDGE product, but its quarterly revenue swings wildly, its operating cash flow was negative in H1-26, and its successor is unproven.

### Cited Findings

#### Besi (Netherlands)
Primary sources: [Q3-2026 PDF, 22 Oct 2026](https://www.besi.com/fileadmin/user_upload/PR_Q3-2026.pdf); [Annual Report 2025](https://www.besi.com/fileadmin/data/Investor_Relations/_Semi__Annual_Reports/Annual_Report_2025.pdf).

**(a) Position**

*Products*
- D2W hybrid bonding: SUCCESSOR.
- TC Next: BRIDGE for HBM; for logic, the successor to mass reflow.
- Flip-chip and multi-module die attach; photonics.
- 2025 revenue mix: ~70% advanced packaging; ~60% for leading-edge devices needing <7 µm placement accuracy [P].

*Hybrid-bonding progress*
- YE-2025: 18 HB customers; cumulative HB orders 150+ systems [P, CC].
- 2025: six integrated HB production lines installed at "a leading logic customer", built "in collaboration with Applied Materials incorporating 30 hybrid bonders in six platforms" [P].
- Roadmap: 100 nm accuracy (<6 µm pad pitch, 2,000 UPH, installed base >150) → 50 nm (<3 µm, >3,000 UPH; first prototype 2025) → 25 nm (<1 µm, >5,000 UPH) [P, CC].
- Q3-2026: YTD HB orders "more than doubled versus fiscal 2025 as orders for HBM applications increased, more logic chiplet programs entered production, co-packaged optics use cases expanded faster than anticipated and edge AI device production began"; 23 customers; >215 systems [P, CC].
- Q3-2026 orders "for both hybrid bonding and TC Next systems from a leading memory customer as they focus on the development of current and next generation HBM device structures" [P, CC].
- Data conflict: a search summary of the Q2-26 release put YE-2025 HB customers at 15, but the Annual Report says 18. The primary figure (18) is used here.

*HBM view*
- "Severe memory shortages this year have extended the use of lower stack heights in current HBM production beyond prior expectations."
- Besi expects HB "adopted in a range of stack heights over the next two years", and DRAM-on-accelerator "by the end of the decade" [P, CC].
- The 2025 Annual Report assumed HBM5 production in 2028–2029 and said HB is "uniquely qualified to assemble memory stacks at or above 20 devices" [P, CC].

*Moat*
- No judge; the moat is high-accuracy placement know-how.
- Besi does "not view ASML as a hybrid bonding competitor" [P, CC].

**(b) Lead — outside evidence**
- TechInsights share: die attach 50% and advanced die placement 82% (2024 data, published Dec 2025) [A via P].
- Applied's 8-K (26 Oct 2026): Applied is raising its stake to ~20%, "add[ing] to Applied Materials' current investment in Besi, which Applied initially made in April 2025". It uses an accelerated share purchase agreement; delivery depends on the HSR Act waiting period. Applied has "no intention to increase its investment in Besi beyond approximately 20 percent" and "does not intend to seek board representation". Applied's Prabu Raja: hybrid bonding and next-generation interconnect are "increasingly critical enablers of energy-efficient AI compute performance" — [Applied 8-K Ex.99.1](https://www.sec.gov/Archives/edgar/data/6951/000162828026067303/ex991prforprojectbasil.htm) [P]
- SK hynix "reportedly ordered" a pilot HB line combining Applied and Besi equipment — [Bits&Chips, 26 Aug 2026](https://bits-chips.com/article/besi-faces-longer-wait-as-sk-hynix-pushes-hybrid-bonding-to-hbm5/) [S]
- HB "currently used mainly in logic" — [Bits&Chips, 22 Oct 2026](https://bits-chips.com/article/besi-sees-increasing-momentum-for-hybrid-bonding/) [S]

**(c) Revenue model**
- Spares and service were 15% of revenue in 2025 (16% in 2024), "typically less cyclical" [P].
- Equipment ASPs exceed €400,000, with 4–12-week lead times. Orders can be cancelled on payment of fees that are "generally not sufficient" to offset the loss, which caveats backlog quality [P].
- Pricing power: Q3-26 gross margin rose on "a more favorable product mix and price increases" [P].
- No per-seat or labour-hour pricing. Temporary staff were 402 of 2,403 FTE (17%) at 30 Sep 2026 [P].

**(d) Financial strength** (quarter to 30 Sep 2026, published 22 Oct 2026, unless noted) [P]

*Q3-26*
- Revenue €283.4m (+13.4% q/q, +113.6% y/y); orders €342.6m (+17.0% q/q, +96.1% y/y).
- Gross margin 65.2%; operating income €129.7m (45.8%); EBITDA €139.9m (49.4%); net income €107.2m (37.8%); tax rate 13.3%.

*Longer periods*
- 9M-26: revenue €718.1m (+69.0%), orders €905.2m (+108.3%), net income €247.8m.
- LTM: orders "€1.2 billion"; revenue €884.6m and operating income €358.6m [D].
- FY2025: revenue €591.3m [D]; orders €685m (+16.8%); operating income €173.1m (−11.5% vs 2024) [P].

*Balance sheet and cash*
- Gross cash €591.9m; convertible notes (long-term debt) €345.3m, down from €508.1m in Q1. Equity rose €116m in Q2, consistent with a conversion [inference]. Net cash €246.6m (−€7.8m a year earlier).
- FCF [D]: Q3 ~€98.6m (OCF €107.1m − capex €2.8m − capitalised development €5.7m); 9M ~€223.5m (~31% of revenue). Capex is ~1% of revenue.
- Returns [D, rough]: ROIC ~70%+ (LTM NOPAT ~€311m on ~€425m net operating capital); LTM ROE ~54%.

*Concentration*
- Customers (FY2025): "no customer represented more than 10% of our revenue and the largest ten customers accounted for approximately 44%" [P, AR]. Top-5 share not disclosed.
- Country: China was 34% of Q3-26 revenue (39% Q2-26, 46% Q1-26, 45% Q4-25) and ~40% of LTM [D]; Asia-Pacific ex-China 56%; EU/USA/Other 10%. China was 40% of Q3-26 orders. Asian customers were ~76% of 2025 revenue; USD was 72% of revenue [P].
- Customer type: Q3-26 orders 41% IDM / 59% foundries + subcontractors [P].

*Footprint and targets*
- Production in Malaysia (cleanroom doubled), China (Leshan), Vietnam and Singapore. "customers continue their migration to Southeast Asia from China" (2025). Asians are 68% of headcount [P].
- Long-term targets: revenue €1.5–1.9bn, gross margin 64–68%, operating margin 40–55% [CC].

**(e) Resilience and cycle**
- Orders swung 2.7x in five quarters (€128.0m Q2-25 → €342.6m Q3-26), and 2025 operating income fell even during the AI boom [D/P].
- Q4-26 guide: revenue flat ±5% "as certain customers request delivery dates for Q3-26 orders in alignment with H1-27 production capacity plans"; GM 63–65%; opex +5–10% "due primarily to higher strategic consulting costs" (reason not given) [P].
- Export controls: only generic tariff and export-regulation risk language. China at 34–46% of 2026 quarterly revenue suggests no binding restriction on its tools [P; inference].

#### Disco (Japan)
Primary source: [Tanshin, 22 Oct 2026](https://www.disco.co.jp/jp/ir/library/doc/fr/fr20261022.pdf), covering Apr–Sep 2026.

**(a) Position**
- Grinders (thinning), dicers and consumables are tool-agnostic: needed in both the TC and HB eras [inference].
- Demand for advanced logic and HBM stayed high, and shipments were led by high-value products.
- Consumables shipments stayed high, "linked to customers' equipment utilisation" (顧客の設備稼働率等に連動) [P].
- Disco owns a physical/process constraint, not a judge [inference].

**(b) Lead**
- Record shipments [P]. No third-party share was obtained (gap).

**(c) Revenue model**
- Consumables revenue follows customer utilisation; its share of sales was not obtained.
- Contract liabilities (customer advances) rose from ¥50.0bn (31 Mar 2026) to ¥79.6bn (30 Sep 2026) [P].

**(d) Financial strength** [P]
- H1 results: shipments ¥284.6bn (+37.2%); sales ¥257.1bn (+32.1%); GM 71.5% vs 68.9% a year earlier [D]; operating income ¥116.6bn (+47.9%, 45.4% margin); net income ¥80.4bn (+43.7%).
- Balance sheet: cash and deposits ¥342.4bn; no interest-bearing debt; equity ratio 76.1%.
- Cash flow: operating CF ¥111.7bn; PP&E capex ¥12.9bn; FCF excluding a ¥41.8bn increase in time deposits ~¥98.8bn [D]; dividends ¥40.8bn.
- Returns: annualised ROE ~26% [D].
- Guidance for Apr–Dec 2026: sales ¥389.5bn, operating income ¥174.7bn, shipments ¥434.2bn. This implies Oct–Dec sales ~¥132.4bn, operating income ~¥58.1bn (~44%) and record shipments ~¥149.6bn [D].
- Preliminary Jul–Sep non-consolidated shipments ¥123.9bn (+60.0%) — [Gyokai Digest/TDnet, 6 Oct 2026](https://www.gyokaidigest.com/en/disclosures/6146-tdnet-20261006-140120261006546587) [S]. "Miss" reports in secondary sources may mix non-consolidated and consolidated bases.
- Customer, country and product split: NOT OBTAINED. The supplementary deck was not found on the IR pages fetched.

**(e) Resilience**
- Debt-free and consumables-backed, with rising prepayments. Export-control exposure not verified.

#### Tokyo Electron (Japan, group level)
Primary sources: [Tanshin](https://www.tel.com/ir/library/report/i61j9u00000000gf-att/fy27q2tanshin-e.pdf), [presentation](https://www.tel.com/ir/library/report/i61j9u00000000gf-att/fy27q2presentations-e2.pdf) and [Q&A](https://www.tel.com/ir/library/report/i61j9u00000000gf-att/FY27Q2_EarningCall_QA_E.pdf), all 30 Oct 2026, for Q2 of FY to Mar 2027 (Jul–Sep 2026).

**(a) Position**
- Front-end process constraint: "our coaters/developers, with a market share of more than 90%" [P, CC].
- Bonding tools are not broken out.
- TEL expects "the 3D integration of advanced packaging to grow significantly from CY2027 onward" [CC].
- Batch ALD for deep-trench capacitors: "Growing demand for advanced packaging; over 200 units expected to ship in both FY2027 and FY2028" [CC].
- Probers: record shipments expected (~+60% y/y) [CC].

**(b) Lead**
- Bonding not tested (gap).

**(c) Revenue model**
- Field Solutions in Q2 were ¥191.0bn: parts and services ¥144.3bn, used equipment and modification ¥46.6bn. That is 20.4% of revenue [P/D].
- New equipment was ¥734.4bn (+38% q/q): logic/foundry 56%, DRAM 34%, NAND 10% [P].

**(d) Financial strength** [P]
- Q2: net sales ¥935.0bn (+27.7% q/q, +48.4% y/y); GM 47.8%; operating income ¥295.3bn (31.6%); R&D ¥85.2bn; capex ¥32.3bn; FCF ¥310.4bn; cash on hand ¥579.7bn.
- H1: net sales ¥1,667.5bn (+41.3%); operating income ¥506.8bn (+67.2%); net income ¥376.9bn (+56.0%). Equity ratio 68.2%; annualised ROE ~36% [D].
- FY to Mar 2027 forecast: net sales ¥3,700bn (+51.4%); GM 47.9%; operating income ¥1,169bn (31.6%); R&D ¥335bn. H2 forecast net sales ¥2,032.5bn; H2 new-equipment sales ¥1,560bn; FY new equipment +59%.
- Q2 revenue by region: China ¥339.9bn (36.4%), South Korea ¥190.7bn (20.4%), Taiwan ¥180.4bn (19.3%), North America ¥76.6bn (8.2%), Japan ¥72.2bn (7.7%), Europe ¥41.7bn (4.5%), SE Asia/Others ¥33.2bn (3.5%).
- Note: an aggregator headline citing "+27%" profit growth conflicts with the primary figures above.

**(e) Resilience and cycle**
- WFE outlook, "based on an aggregation of customers' capital investment plans": CY2026 ~US$160bn; CY2027 >US$210bn, with "factory automation, wafer-level packaging and other" at ~US$10bn rising to the low teens of billions [P, CC].
- "At present, our discussions with customers do not indicate a slowdown in CY2028" [P, CC].
- China exposure 36% [P]. Export-control specifics not verified.

#### Camtek (Israel)
Primary source: [6-K, 4 Nov 2026](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326005000/zk2636329.htm). Call summary: [MarketBeat, 4 Nov 2026](https://www.marketbeat.com/instant-alerts/transcript-camtek-q3-earnings-call-highlights-2026-11-04/) [S].

**(a) Position**
- A "judge" for bumps, HBM and CoWoS. Advanced packaging was ~80% of Q3 sales; Eagle G5 and Hawk were ~57% of systems revenue [S].
- HB inspection is "low" and becomes meaningful only in 2028+ [S].
- Installed base ~4,000 systems [S, CC].

**(b) Lead**
- Orders >US$800m year to date (to the investor event), ~80% advanced packaging; OSATs just over half.
- Customers, including in China, are booking slots through 2027 [S, CC]. No third-party share obtained.

**(c) Revenue model**
- Service ~US$40m in 2026, about 7% of the ~US$595m FY revenue [D]. Target: 35–40% growth a year. AI software starts in 2027 [S, CC].

**(d) Financial strength** [P]
- Q3 (to 30 Sep 2026): revenue US$161.3m (+28% y/y); GM 50.0% GAAP / 51.1% non-GAAP; operating income US$39.8m GAAP (24.7%) / US$47.5m non-GAAP (29.5%); operating CF US$71.1m.
- Cash, deposits and securities US$877.1m against converts of US$489.2m: net cash ~US$388m [D].
- Guidance: FY26 ~US$595m; 2027 >US$800m; target US$1.2bn at 34–36% operating margin [CC].
- Concentration: not disclosed. China is "meaningful" in the 2027 backlog [S].

**(e) Resilience**
- Component shortages and a strong shekel weigh on gross margin [S].
- Exposed to OSAT capex, China, and Israel geopolitics [inference].

#### Onto Innovation (US) — short entry
Primary source: [8-K Ex.99.1, 9 Nov 2026](https://www.sec.gov/Archives/edgar/data/704532/000119312526453582/onto-ex99_1.htm), Q3 to 30 Sep 2026.
- Revenue US$409.7m (+87.8% y/y); GM 54.8% GAAP / 57.6% non-GAAP; operating income US$95.4m (23.3%) GAAP / US$133.5m (32.6%) non-GAAP.
- Backlog ">$1.3 billion"; cash and securities US$1.25bn.
- Advanced Packaging and Specialty Devices hit record revenue "primarily driven by the Dragonfly G5 and Firefly inspection systems".
- Bought a 27% interest in Rigaku (closed Aug 2026).
- Guidance: FY26 growth >45%; Q4 revenue US$430–450m [P].

#### ASMPT (HKEX: 0522)
Primary sources: [Q3-2026 release, 28 Oct 2026](https://www.asmpt.com/en/investor-relations/news-events/asmpt-announces-2026-third-quarter-results-record-group-bookings-and-strong-earnings-across-semi-smt/); [SMT decision, 5 Nov 2026](https://www.asmpt.com/en/investor-relations/news-events/asmpt-concludes-strategic-options-assessment-and-retains-smt-solutions-segment/).

**(a) Position**
- TC bonders: C2S for logic (record orders "led by strong demand for larger compound-die TCB tools" from OSAT partners of a leading advanced logic customer); C2W (repeat orders from "a leading global IDM for advanced CPUs"); HBM (BRIDGE).
- 2nd-gen HB at "sampling stage" (H1-26) [CC].
- Photonics: record bookings and revenue; AMICRA won a bulk order for Near-Packaged Optics [P].
- SMT: retained after a strategic review (Jan–Nov 2026). AI-related demand is >50% of SMT bookings in 2026 YTD [CC].
- New Group CEO Bassel Haddad took over on 11 Aug 2026 [P, IR listing].

**(b) Lead**
- ~Half of SK hynix's HBM4 TC sets (Dec 2025) [S].
- Bulk orders for >50 C2S TCB tools (29 Jul 2026) [CC] — [release](https://www.asmpt.com/en/investor-relations/news-events/asmpt-secures-significant-wins/).
- SMT bookings share ~24% (2025) → ~31% (2026 YTD) [CC].

**(c) Revenue model**
- Service and recurring share not obtained.

**(d) Financial strength** [P]
- Q3-26: revenue HK$5,247.0m (US$669.2m; +6.3% q/q, +48.7% y/y); bookings HK$8,845.1m (US$1,128.0m; +137.9% y/y); book-to-bill 1.69.
- Margins: GM 42.1% (adjusted 42.9%); operating profit HK$798.6m (~15.2%) [D]; adjusted operating profit HK$922.4m (~17.6%) [D]; net profit HK$533.2m (adjusted HK$689.7m).
- Segments: SEMI bookings +156.3% y/y, "led by TCB, Photonics and Flip Chip"; SMT bookings a record for the third quarter running (+122.1% y/y), including >US$100m of bulk orders and pull-ins.
- Q4 guide: revenue US$670–730m; SEMI flat on "longer lead times of AP products".
- H1-26: net cash HK$3.63bn [P via wire]. Advanced Packaging bookings ~US$340m in 2026 YTD, "~25% of segment bookings" (SEMI segment; wording ambiguous) [CC].
- SMT 2027 targets: revenue ~US$1.6bn, GM ~40%, segment margin 20% [CC].
- China: SEMI mainstream "especially strong" in H1 (no %) [P via wire].

**(e) Resilience**
- Diversified. HBM tool purchases are deferred while memory makers reassess HBM4 [S]. With SMT retained, the conglomerate structure continues.

#### Hanmi Semiconductor (KRX: 042700)

**(a) Position**
- TC Bonder 4 / 4.5 is a BRIDGE product; HB in HBM is now due at HBM5, ~2029–30 (§5).
- Bridge extension: Wide TC Bonder, launching late 2026 [CC] — [MTN, 13 Feb 2026](https://news.mtn.co.kr/news-detail/2026021317395078451).
- Successor plan: KRW 100bn HB plant in Incheon (target end-2026); HB for HBM6 by end-2027 [CC] — [Asia Economy, 22 Dec 2025](https://view.asiae.co.kr/en/article/2025122209224722092); [TrendForce, 7 Oct 2025](https://www.trendforce.com/news/2025/10/07/news-hybrid-bonder-equipment-market-reportedly-near-2b-by-2028-as-korean-makers-race-to-next-gen-hbm-tools/).
- No judge or hard constraint: SK hynix dual-sourced anyway [inference].
- KAIST Prof. Yu Hoe-jun: Hanmi "may fill the gap temporarily" [S].

**(b) Lead**
- 71.2% TechInsights share (cumulative to Q3-2025) [A]; repeat HBM4 orders in 2026 [S].
- From Sep 2026, 2.5D equipment shipped to a Taiwanese foundry (named TSMC only in a subheadline); FC Bonder 75 first shipment — [Money Today, 30 Oct 2026](https://www.mt.co.kr/en/industry/2026/10/30/2026103010252581828) [S]

**(c) Revenue model**
- One-off hardware; heavy field support (60 engineers on site at SK hynix in 2025) [S].

**(d) Financial strength**
- Q3-26 (published 30 Oct 2026, per DART): revenue KRW 181bn (+8.9%); operating profit KRW 90.8bn (50.2%) [S].
- Quarterly history, filing-based aggregator [Stockanalysis](https://stockanalysis.com/quote/krx/042700/financials/?p=quarterly) [S]:

  | Quarter | Revenue (KRW bn) | Operating margin |
  |---|---|---|
  | Q1-25 | 147.4 | 47.2% |
  | Q2-25 | 180.0 | 47.8% |
  | Q3-25 | 166.2 | 40.8% |
  | Q4-25 | 83.0 | 33.3% |
  | Q1-26 | 50.9 | 16.6% |
  | Q2-26 | 251.2 | 51.9% |

- Derived totals [D]: FY2025 revenue ~KRW 576.7bn, operating profit ~KRW 251.2bn (43.6%). 9M-26 revenue ~KRW 483bn, operating profit ~KRW 230bn.
- Cash: operating CF −KRW 38.4bn (Q1-26) and −KRW 18.2bn (Q2-26). Net cash fell from KRW 274.7bn (Dec-25) to KRW 87.3bn (Jun-26). Q2-26 capex KRW 19.2bn [S].
- Overseas revenue averaged >72% over 15 years [S]. Customer concentration not obtained.

**(e) Resilience**
- One product family with concentrated customers; patent dispute; SK hynix diversifying. Revenue swung 5x between Q1-26 and Q2-26 [D].
- Every HB slip extends demand for its tools [inference].

#### SUSS MicroTec (Xetra: SMHN) — short entry
Primary sources: [Q3-2026 statement, 5 Nov 2026](https://www.suss.com/en/content/download/3521/file/2026_11_05_SUSS_Quarterly%20Statement%20as%20of%20September%2030,%202026.pdf); [ad hoc, 27 Oct 2026](https://www.suss.com/en/news/ad-hoc/suss-microtec-se-suss-resolves-production-relocation-and-adjusts-guidance-for-fiscal-year-2026).
- Q3-26 orders €223.5m (+219.3%); 9M orders €633.5m; order book €600.6m (+118.5%); 9M book-to-bill 2.1.
- Q3 sales €97.0m (−18.5%); 9M €299.8m (−22.3%). Q3 GM 36.5%; Q3 EBIT €4.1m (4.2%); 9M EBIT 6.1%.
- Q3 FCF €48.9m; net cash €112.1m.
- Advanced Backend: the Bonding product line "declined significantly to around one-third of segment sales". Coating was ~50% of tool orders; the Q2 OSAT mega-order was expanded by ~€50m.
- Sales "concentrated in Taiwan and China".
- FY26 guidance cut on 27 Oct 2026: sales €405–425m (from €425–485m); EBIT 5–7% (from 8–10%). Garching manufacturing closes; production concentrates in Zhubei (Taiwan) and Sternenfels; ~€6.2m one-offs [P].

#### Kulicke & Soffa (Nasdaq: KLIC) — short entry
Primary source: [8-K Ex.99.1, 5 Aug 2026](https://www.sec.gov/Archives/edgar/data/56978/000005697826000030/ex991liveq32026.htm), quarter to 4 Jul 2026.
- Revenue US$330.4m (vs US$148.4m a year earlier and US$242.6m in FQ2); GM 47.8%; net income US$57.4m; adjusted FCF US$41.0m.
- FQ4 guide ~US$375m ±US$20m. Expanded Advanced Solutions plant due in H2 FY2027. Interim CEO/CFO Lester Wong [P].
- FQ4-26 (to 3 Oct 2026) not yet found.

### Inferences
- **Revenue recurrence:** TEL 20.4% (Field Solutions) ≈ Besi 15% (spares/service) > Camtek ~7%. Disco's consumables are utilisation-linked (share unknown). Hanmi, ASMPT and K&S shares are unknown or predominantly one-off.
- **Three AI-spending scenarios to 2030** (my judgement):
  - *Steady growth (~55%):* all grow; Besi gains from logic/CPO HB, with HBM HB at HBM5.
  - *Financing-led pause ~2028 (~25%):* steepest falls at Hanmi (already showing 5x quarterly swings and negative operating cash flow) and Besi (2.7x order swings). Disco is cushioned by consumables and TEL by Field Solutions. ASMPT is cushioned by SMT. Camtek and Onto are exposed to OSAT capex. TEL's own customer talks show no CY2028 slowdown [CC].
  - *Acceleration (~20%):* HB pull-in favours Besi/Applied, Semes and Hanwha; Disco, Camtek and Onto become capacity-bound.
- **Cycle position:** Q3-26 shows record orders and backlogs everywhere (Besi, ASMPT, SUSS, Camtek, Onto, Disco advances, TEL). Pricing is firm. Early digestion is visible: Besi's flat Q4, ASMPT's flat SEMI and lower Q4 bookings, memory makers deferring bonder buys, SUSS's lower guidance on component constraints. This looks like a mid-to-late upcycle.
- **China:** ~40% of Besi's LTM revenue; 36.4% of TEL's Q2; SUSS sales concentrated in Taiwan and China; strong China demand at ASMPT and Camtek. Back-end tools evidently still ship to China [inference].

### Gaps
- Disco product, region and customer split; Hanmi customer concentration (DART not reached); ASMPT service share and China %; Camtek and Onto concentration; TEL bonding products.
- Applied FQ4-26 not yet released; K&S FQ4-26 not found.

---

## (3) Path forward — transitions, said vs done, funding, timing, verdicts

### Takeaway
The transition that matters here is (3) solder-bump stacking to hybrid bonding. Some players are also exposed to (2) CPO and (4) panel. Transitions (1), (5) and (6) barely touch these firms, apart from photonics assembly at Besi and ASMPT.

| Company | Suggested verdict |
|---|---|
| Besi | Coherent |
| Disco | Coherent |
| TEL | Coherent (group) |
| Camtek / Onto | Coherent, with the HB judge role unproven |
| ASMPT | Partly coherent |
| Hanmi | Partly coherent |
| SUSS | Partly coherent |

### Cited Findings

**Besi** — transitions (3), (2), (4); benefits from (1) via photonics.
- SAID: HB "in a range of stack heights over the next two years"; DRAM-on-accelerator by end of decade [P, CC].
- DONE:
  - Six integrated Applied+Besi HB lines (30 bonders) at a leading logic customer in 2025 [P].
  - 23 customers; >215 systems; HB orders more than doubled YTD-26 [P, CC].
  - HB and TC Next orders from a leading memory customer [P, CC].
  - Applied stake rising to ~20%; Besi became an EPIC Innovation Partner [P].
  - SK hynix pilot line reported [S].
- FUNDED: net cash €246.6m; 9M FCF ~€223.5m [D]; 37.8% net margin through the HBM slip [P].
- TIMING: logic and CPO HB now; HBM HB at HBM5, ~2029–30 (§5).
- MUST GO RIGHT: memory makers buy open-market rather than captive (Semes) tools; Besi keeps its accuracy and throughput lead (50/25 nm roadmap); China demand holds or shifts to Southeast Asia.
- **Verdict: COHERENT** — the successor already ships in volume in logic, and the company is funded through a 1–2-year HBM slip.

**Disco** — (3) neutral to positive (thinner dies, cleaner singulation); (4) not verified.
- DONE: record shipments; rising advances [P].
- FUNDED: debt-free; ¥342.4bn cash and deposits [P].
- **Verdict: COHERENT** — Disco does not depend on which bonding method wins. Its HB-specific tool roles were not verified.

**Tokyo Electron** — (3) W2W/D2W (details UNVERIFIED); TEL itself flags 3D integration growth from CY2027 [CC].
- DONE: deep-trench-capacitor ALD for advanced packaging, >200 units a year expected [CC].
- FUNDED: R&D ¥335bn; FCF ¥310bn in Q2 [P].
- **Verdict: COHERENT at group level; bonding path not assessable.**

**Camtek / Onto** — (3) HB inspection.
- Camtek sees it as meaningful only from 2028 [S]. Onto bought 27% of Rigaku, which adds X-ray metrology adjacency [P; relevance inferred].
- FUNDED: both net cash [P/D].
- **Verdict: COHERENT, HB judge role unproven.** Onto has a Samsung inspection JDP [S].

**ASMPT** — (3), (2) (CPO portfolio, NPO bulk order [P]), (4) (chip-on-panel tool in qualification [P via wire]), (1) (800G/1.6T module tools [P]).
- SAID: HB gen-2 at sampling [CC].
- DONE: HBM4 TC in use at SK hynix [S]; record C2S TCB orders [P]; SMT retained with 2027 targets [CC].
- FUNDED: net cash HK$3.63bn [P via wire].
- **Verdict: PARTLY COHERENT** — strong, diversified bridge; HB successor only at sampling; memory TC orders deferred.

**Hanmi** — (3) is existential; (4) partly (FC Bonder 75, 2.5D).
- SAID: Wide TC by end-2026; HB plant end-2026; HB for HBM6 by end-2027 [CC].
- DONE: 2026 HBM4 orders; 2.5D/FC entry at a Taiwanese foundry; Hanmi USA (Oct 2026) [S]. Q2-26 capex rose to KRW 19.2bn [S], consistent with plant spending [inference]. No HB customer evaluation found.
- FUNDED: high margins, but net cash fell to KRW 87.3bn (Jun-26) and operating cash flow was negative in H1-26 [S].
- **Verdict: PARTLY COHERENT** — a credible bridge extension, an unproven successor, and a thinner cash cushion than its margins suggest.

**SUSS** — (3) temporary and permanent bonding; (4) panel scanner shipped to Taiwan.
- **Verdict: PARTLY COHERENT** — record orders, but falling sales, 4–7% EBIT, a guidance cut, and a shrinking bonding line.

### Inferences
- Bridge-side companies gain from every slip but face lumpy orders. Successor-side companies (Besi with Applied) are funded through the slip by logic, CPO and edge-AI HB.

### Gaps
- Hanmi HB evaluations and plant status; TEL and EVG D2W progress; Disco HB tools; Camtek and Onto panel inspection.

---

## (4) Suggested ordering of key companies by quality alone (independent of price and size)

### Takeaway

| Rank | Company | Basis |
|---|---|---|
| 1 | **Disco** | Tool-agnostic constraint; utilisation-linked consumables; 45.4% operating margin; debt-free; rising advances |
| 2 (tie) | **Tokyo Electron (group)** | >90% coater/developer share [CC]; 20.4% Field Solutions; 31.6% operating margin; ROE ~36% [D]. But 36% China, and bonding is marginal |
| 2 (tie) | **Besi** | Highest margins and returns (45.8% operating, ROE ~54%); TechInsights 82% advanced-placement share; 15% service; no customer >10%. But most cyclical, ~40% China, HBM HB slipping |
| 4 (tie) | **Onto** | Larger and broader judge (only partly assessed) |
| 4 (tie) | **Camtek** | Judge position; 29.5% non-GAAP operating margin; net cash; HB judge role from 2028 |
| 6 | **ASMPT** | Diversified, with record bookings, but ~17.6% adjusted operating margin and HB at sampling |
| 7 | **Hanmi** | 50% margins on a BRIDGE product, with extreme lumpiness, negative H1-26 operating cash flow and an unproven successor |
| 8 | **SUSS** | Record orders, but weak sales, margins and a guidance cut |

- The TEL/Besi tie cannot be separated with confidence.
- Disco versus TEL/Besi is also close. Disco ranks first because it is indifferent to the bonding transition.
- Not ranked (thin evidence): EV Group, Applied (bonding portion), K&S, Semes, Hanwha, Shibaura, Toray, Yamaha, all China and Taiwan names, KLA, Nova, Park, Lasertec.

### Cited Findings
- Figures as in §2: [Besi PDF](https://www.besi.com/fileadmin/user_upload/PR_Q3-2026.pdf), [Besi AR 2025](https://www.besi.com/fileadmin/data/Investor_Relations/_Semi__Annual_Reports/Annual_Report_2025.pdf), [Disco Tanshin](https://www.disco.co.jp/jp/ir/library/doc/fr/fr20261022.pdf), [TEL presentation](https://www.tel.com/ir/library/report/i61j9u00000000gf-att/fy27q2presentations-e2.pdf), [Camtek 6-K](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326005000/zk2636329.htm), [Onto 8-K](https://www.sec.gov/Archives/edgar/data/704532/000119312526453582/onto-ex99_1.htm), [ASMPT Q3](https://www.asmpt.com/en/investor-relations/news-events/asmpt-announces-2026-third-quarter-results-record-group-bookings-and-strong-earnings-across-semi-smt/), [Hanmi via Stockanalysis](https://stockanalysis.com/quote/krx/042700/financials/?p=quarterly), [SUSS Q3](https://www.suss.com/en/content/download/3521/file/2026_11_05_SUSS_Quarterly%20Statement%20as%20of%20September%2030,%202026.pdf).

### Inferences
- The ordering weights (a) position and (c) recurrence as heavily as (d) margins, per the framework.

### Gaps
- Disco's third-party share and consumables share, and Hanmi's customer concentration, would sharpen the top and bottom of the order.

---

## (5) Check of background priors (and leads)

### Takeaway

| Prior | Verdict | Current evidence |
|---|---|---|
| 1. HB in HBM slipped to 16-high HBM4E at the earliest | **UPDATED — slipped further** | SK hynix (Hot Chips, 23 Aug 2026): HB won't meet HBM4E needs; HBM5 at the earliest (~2029–30). Samsung's 16-high HBM4E possible but unconfirmed |
| 2. Bridges last longer than roadmaps | **CONFIRMED** | Share loss unlikely before ~2029 |
| 3. Packaging a binding constraint in 2028–30 | **NOT TESTABLE** | Consistent with 2026–27 lead times; TEL's customers indicate no CY2028 slowdown [CC]. In 2026 the visible binding constraint is memory supply |

### Cited Findings

**Prior 1 → UPDATED**
- Hot Chips 2026: SK hynix VP Jaesik Lee said HB "will not meet HBM4E requirements" (HBM5 at the earliest). HB is for 20+-high stacks; 16-high HBM4 is in customer qualification — [36Kr EN, 25 Aug 2026](https://eu.36kr.com/en/p/3954225477991553); [Bits&Chips, 26 Aug 2026](https://bits-chips.com/article/besi-faces-longer-wait-as-sk-hynix-pushes-hybrid-bonding-to-hbm5/) [S]
- SK hynix requires "at least 90 percent" yield; a SEMI talk (9 Sep 2026) set "a yield of 90 to 98 percent" and "a lifespan of three to five years" as non-negotiable — [Herald Business, 20 Sep 2026](https://biz.heraldcorp.com/article/10878775) [S]
- SK hynix keeps MR-MUF through HBM4 and HBM4E 16-high; fluxless failed evaluation — [TrendForce, 13 Jan 2026](https://www.trendforce.com/news/2026/01/13/news-sk-hynix-may-stick-with-mr-muf-for-hbm4-16-high-despite-asmpt-tc-bonder-orders/) [S]
- Samsung and SK hynix are "reconsidering"; 16-high HBM4E is "the earliest likely adoption point"; 12-high HBM4E is the expected mainstream — [TrendForce, 7 Jul 2026](https://www.trendforce.com/news/2026/07/07/news-samsung-sk-hynix-reportedly-reconsider-hybrid-bonding-timeline-16-high-hbm4e-may-be-earliest-adoption/) [S]
- Samsung showed HB at GTC 2026 (>20% better thermal resistance; >16-high support) — [TrendForce, 1 Apr 2026](https://www.trendforce.com/news/2026/04/01/news-jedec-reportedly-plans-to-relax-hbm-height-specs-to-900%C2%B5m-potentially-slowing-hybrid-bonding-adoption/) [S, CC]
- NVIDIA is reportedly weighing lower stacks for Rubin Ultra because of supply — [Herald, 20 Sep 2026](https://biz.heraldcorp.com/article/10878775) [S]
- Counterpoint: HBM5 ~2029–30 is HB's "real turning point" — [Asia Economy, 6 Apr 2026](https://view.asiae.co.kr/en/article/2026040613193475063) [A]
- Besi assumed HBM5 production in 2028–29 (AR 2025, early 2026) — now later per SK hynix [P vs S].
- Oct-2025 forecasts had HB at ~50% of HBM by 2028 — [TrendForce, 7 Oct 2025](https://www.trendforce.com/news/2025/10/07/news-hybrid-bonder-equipment-market-reportedly-near-2b-by-2028-as-korean-makers-race-to-next-gen-hbm-tools/). This is now contradicted.

**Prior 2 → CONFIRMED (timing back-loaded to ~2029–30+)**
- JEDEC HBM4 limit raised from 720 µm to 775 µm — [SemiEngineering, 13 Jan 2026](https://semiengineering.com/hbm4-sticks-with-microbumps-postponing-hybrid-bonding/) [S]
- ~900 µm reported for HBM4E — [TrendForce citing Chosun Ilbo, 1 Apr 2026](https://www.trendforce.com/news/2026/04/01/news-jedec-reportedly-plans-to-relax-hbm-height-specs-to-900%C2%B5m-potentially-slowing-hybrid-bonding-adoption/); [3DNews citing Business Korea, 3 Apr 2026](https://3dnews.ru/1139386/jedec-razreshit-pamyati-hbm4e-podrasti-radi-uproshcheniya-proizvodstva-i-snigeniya-tseni)
- ~1,000 µm discussed for HBM5 — [TrendForce, 7 Jul 2026](https://www.trendforce.com/news/2026/07/07/news-samsung-sk-hynix-reportedly-reconsider-hybrid-bonding-timeline-16-high-hbm4e-may-be-earliest-adoption/) [S]. No official JEDEC publication found (jedec.org returned 403).
- Besi: memory shortages "extended the use of lower stack heights" [P].
- Caveat: memory makers are "delaying larger bonding-tool purchases" (ASMPT Q3) [S], and Hanmi's revenue swings show that longer bridge life does not mean smooth bridge orders.

**Prior 3 → NOT TESTABLE for 2028–30**
- Tightness now:
  - Camtek slots booked through 2027 [S].
  - Besi deliveries aligned to H1-27 capacity [P].
  - SUSS order book €600.6m [P].
  - Onto backlog >US$1.3bn [P].
  - Disco advances +59% in six months [D].
  - ASMPT "longer lead times of AP products" [P].
  - TEL: "discussions with customers do not indicate a slowdown in CY2028" [P, CC].
- The 2026 binding constraint is memory: "Severe memory shortages" (Besi) [P]; NVIDIA reportedly lowering stack heights [S]; component shortages at Camtek and SUSS [S/P].

**Leads**
- Applied ~9% Besi stake and integrated HB system — **CONFIRMED**:
  - The initial investment was made "in April 2025" [P, Applied 8-K, 26 Oct 2026].
  - The integrated Applied+Besi HB lines were in production use in 2025: six lines with 30 bonders at a leading logic customer [P, Besi AR 2025].
  - New: stake rising to ~20%, subject to the HSR waiting period [P].
- Hanmi–SK hynix dispute and dual-sourcing — **CONFIRMED** [S] (§1).
- Hanmi Wide TC and HB plan — **CONFIRMED** as company plans [CC].
- JEDEC HBM4 at 775 µm — **CONFIRMED** [S]. Further relaxation **REPORTED**, not confirmed.
- ASMPT SMT review — **CONFIRMED AND CONCLUDED**: the review ran Jan–Nov 2026, and on 5 Nov 2026 the Board decided to **retain** SMT [P].

### Inferences
- Replace "16-high HBM4E at the earliest" with "HBM5 (20-high, ~2029–30) at the earliest for SK hynix; 16-high HBM4E (~2027–28) still possible but unconfirmed for Samsung". Besi's 2026 memory HB orders are for development, per its own wording.

### Gaps
- No official JEDEC text; no Micron or CXMT HB timeline.

---

## (6) Open question — which successor ships in volume first; who captures the value

### Takeaway
D2W HB already ships in volume in logic (six Applied+Besi lines with 30 bonders at a leading logic customer in 2025) and is spreading to CPO and edge AI. W2W HB has long been in volume in image sensors and NAND (background, UNVERIFIED). HBM comes last, at HBM5. Within HBM, the first "successors" are bridge extensions (wide-die TC, possibly fluxless), not HB.

On value capture, the evidence favours a specialist-plus-giant alliance (Besi with Applied at ~20%) in logic. In HBM, captive suppliers (Semes) have structural access. Hanmi is late. Inspection and metrology (Camtek, Onto) gains either way.

### Cited Findings
- **Logic volume:**
  - Six integrated HB lines with 30 Besi bonders at a leading logic customer (2025) [P, AR].
  - "more logic chiplet programs entered production" and HB capacity expansion is planned "for logic, CPO and edge AI devices" [P, Q3-26, CC].
  - HB is "mainly in logic" [S, Bits&Chips].
  - TSMC is at 6 µm pitch — headline only, [Tom's Hardware](https://tomshardware.com/tech-industry/semiconductors/hybrid-bonding-roadmap-examined) [S].
- **Installed base and orders:**
  - Besi: >150 HB installed base at YE-2025; >215 systems cumulative demand by Q3-26 [P, CC].
  - ASMPT HB at sampling [CC]; Hanwha gen-2 HB in customer tests from H1-26 [S]; Semes and Hanwha going straight to HB [S]; LG targets 2028 [S]; Hanmi targets end-2027 [CC].
  - EVG/imec showed W2W HB at 200 nm pitch (May 2026) [CC].
- **Integrated giant:**
  - Applied's 8-K extends co-innovation "beyond hybrid bonding into new interconnect architectures", including "scaling of thermo-compression bonding and new die-on-wafer, die-on-die and die-on-panel integration platforms" [P].
  - TEL sees 3D integration of advanced packaging growing from CY2027 [P, CC].
- **Captive:** Samsung relies on Semes for TCB (analyst view) — [Tech Investments](https://www.techinvestments.io/p/hbmdie-bonding-semicap-outlook) [A].
- **Market-size reference points (forecasts):**
  - HB ~US$2bn by 2028 (News1, Oct 2025; now stale) [S].
  - ASMPT TCB addressable market >US$1.6bn by 2028 [CC].
  - Besi: market potential of 350–600 systems cumulative through 2030 for a "new product" (context suggests TC Next; ambiguous) [CC].
  - Hybrid bonder ~KRW 4bn, more than 2x a TC bonder [S].
- **Judges:** Camtek sees HB inspection from 2028 [S]; Onto has record AP inspection revenue (Dragonfly G5, Firefly), a Rigaku stake and a Samsung inspection JDP [P/S].

### Inferences
- First volume successor after logic: CPO and edge-AI D2W HB (2026–27), then HBM HB at Samsung (possibly 16-high HBM4E) or at HBM5 (~2029–30).
- Value capture:
  - Logic and CPO: Besi plus Applied. Through its ~20% stake, Applied captures part of the specialist's economics without control.
  - HBM: captive suppliers have qualification access, which caps open-market share at the largest application.
  - Judges gain on either route, because HB adds quality gates (Cu recess, particles, voids, overlay).

### Gaps
- No third-party HB share or installed base by supplier. Intel Foveros Direct, AMD, image-sensor and NAND volumes were not re-verified.

---

## (7) What could not be verified

### Takeaway
The biggest remaining gaps are:
- China: domestic HB, thinning and dicing entrants, and CXMT bonder sourcing.
- The actual export-control rule texts for packaging tools.
- Hanmi's customer concentration, and Disco's product, region and share data.
- Volumes at the private and captive players (EVG, Semes, Hanwha, LG).

### Cited Findings
- (none — list of gaps)

### Inferences
- Treat UNVERIFIED map rows as leads, not facts.

### Gaps
- **China:** Piotech, U-Precision, iSABers, Maxwell, Kingsemi, Hwatsing, GL Tech, Skyverse — products, customers and revenues not verified. Piotech's site returned 503; cninfo was not reached. CXMT's HBM bonder suppliers are unknown. Looser JEDEC specs may ease Chinese entry — [3DNews, 3 Apr 2026](https://3dnews.ru/1139386/jedec-razreshit-pamyati-hbm4e-podrasti-radi-uproshcheniya-proizvodstva-i-snigeniya-tseni) (unquantified).
- **Export controls and tariffs:** no current US BIS, Dutch, Japanese METI or Korean rule texts on bonding, dicing or packaging-inspection tools were retrieved.
  - Indirect evidence of continued China sales: Besi (China 34–46% of 2026 quarterly revenue), TEL (36.4%), SUSS (sales concentrated in Taiwan and China), ASMPT, Camtek.
  - Besi lists generic tariff risk.
  - Applied's stake needs only HSR clearance per its 8-K. Whether China's SAMR must review it was not confirmed.
- **Taiwan** (MOPS) and **India** (NSE/BSE): not checked.
- **No 2026 data:** EV Group volumes or financials, Shibaura, Toray Engineering, Yamaha Robotics, Tokyo Seimitsu, EO Technics, Park Systems, Nova, KLA, Lasertec, PVA TePla/Nordson (acoustic), Comet (X-ray).
- **Kulicke & Soffa:** HBM4 qualification status; FQ4-26.
- **Applied:** FQ4-2026 not yet released (EDGAR shows no Nov-2026 8-K as of 12 Nov 2026).
- **Besi:** top-5 customer share; reason for Q4 "strategic consulting costs"; whether the 350–600-system estimate refers to TC Next or HB.
- **Hanmi:** customer concentration; reasons for the net-cash decline (dividends or buybacks?); HB plant completion; HB customer evaluations; the meaning of "US$247.7m cumulative revenue to Q3-2025" (TC-only or total).
- **Disco:** product, region and customer split; third-party shares.
- **TEL:** bonding products, revenue and customers.
- **Hanwha:** the HB-cluster report (single undated source); parent listing.
- **JEDEC:** official HBM4E/HBM5 heights (jedec.org returned 403).
- **Micron:** HB timeline and HBM4 bonder split.
- **2026 TC-bonder shares:** TechInsights or Yole 2026 editions.

---

## (8) Sources (publication date; period covered in brackets)

### Takeaway
Primary sources dominate the company financials: Besi, Disco, TEL, ASMPT, SUSS, Camtek, Onto, K&S, Applied. HBM-timing evidence is mostly Korean trade press relayed by TrendForce, Bits&Chips, 36Kr and Herald (Jan–Oct 2026). These outlets are independent of each other and agree.

### Cited Findings
**Primary**
- Besi, Q3-2026 results PDF, 22 Oct 2026 [Q3/9M to 30 Sep 2026] — https://www.besi.com/fileadmin/user_upload/PR_Q3-2026.pdf
- Besi, Q3-2026 release page, 22 Oct 2026 — https://www.besi.com/investor-relations/press-releases/details/be-semiconductor-industries-nv-announces-q3-2026-results/
- Besi, Annual Report 2025, 2026 [FY2025] — https://www.besi.com/fileadmin/data/Investor_Relations/_Semi__Annual_Reports/Annual_Report_2025.pdf
- Besi, Applied stake acknowledgement, 27 Oct 2026 — https://www.besi.com/investor-relations/press-releases/details/applied-materials-to-increase-its-strategic-investment-in-be-semiconductor-industries/
- Applied Materials, 8-K Ex.99.1, 26 Oct 2026 — https://www.sec.gov/Archives/edgar/data/6951/000162828026067303/ex991prforprojectbasil.htm
- Disco, Tanshin H1 FY to Mar 2027, 22 Oct 2026 [Apr–Sep 2026] — https://www.disco.co.jp/jp/ir/library/doc/fr/fr20261022.pdf
- Tokyo Electron, Tanshin Q2 FY2027, 30 Oct 2026 [Apr–Sep 2026] — https://www.tel.com/ir/library/report/i61j9u00000000gf-att/fy27q2tanshin-e.pdf
- Tokyo Electron, presentation, 30 Oct 2026 — https://www.tel.com/ir/library/report/i61j9u00000000gf-att/fy27q2presentations-e2.pdf
- Tokyo Electron, earnings Q&A, 30 Oct 2026 — https://www.tel.com/ir/library/report/i61j9u00000000gf-att/FY27Q2_EarningCall_QA_E.pdf
- ASMPT, Q3-2026 results, 28 Oct 2026 — https://www.asmpt.com/en/investor-relations/news-events/asmpt-announces-2026-third-quarter-results-record-group-bookings-and-strong-earnings-across-semi-smt/
- ASMPT, SMT strategic review concluded (retain), 5 Nov 2026 — https://www.asmpt.com/en/investor-relations/news-events/asmpt-concludes-strategic-options-assessment-and-retains-smt-solutions-segment/
- ASMPT, news list (incl. CEO change 11 Aug 2026; SMT review start 21 Jan 2026; TCB AOR C2W milestone 5 Feb 2026), accessed 12 Nov 2026 — https://www.asmpt.com/en/investor-relations/news-events/
- ASMPT, 2026 interim results (wire), 1 Aug 2026 — https://news.marketersmedia.com/asmpt-announces-2026-interim-results-multiple-advanced-packaging-solutions-drive-strong-performance/89199421
- ASMPT, >50 C2S TCB tools, 29 Jul 2026 — https://www.asmpt.com/en/investor-relations/news-events/asmpt-secures-significant-wins/
- SUSS MicroTec, Q3-2026 quarterly statement, 5 Nov 2026 — https://www.suss.com/en/content/download/3521/file/2026_11_05_SUSS_Quarterly%20Statement%20as%20of%20September%2030,%202026.pdf
- SUSS MicroTec, ad hoc on relocation and guidance, 27 Oct 2026 — https://www.suss.com/en/news/ad-hoc/suss-microtec-se-suss-resolves-production-relocation-and-adjusts-guidance-for-fiscal-year-2026
- SUSS MicroTec, H1-2026 release (wire), 6 Aug 2026 — https://www.placera.se/pressmeddelanden/suss-microtec-order-book-reaches-record-of-473-7-million-providing-strong-visibility-for-2027-20260806
- Camtek, 6-K Q3-2026, 4 Nov 2026 — https://www.sec.gov/Archives/edgar/data/0001109138/000117891326005000/zk2636329.htm
- Onto Innovation, 8-K Ex.99.1 Q3-2026, 9 Nov 2026 — https://www.sec.gov/Archives/edgar/data/704532/000119312526453582/onto-ex99_1.htm
- Kulicke & Soffa, 8-K Ex.99.1 FQ3-2026, 5 Aug 2026 [quarter to 4 Jul 2026] — https://www.sec.gov/Archives/edgar/data/56978/000005697826000030/ex991liveq32026.htm
- EV Group, news list, accessed 12 Nov 2026 — https://www.evgroup.com/company/news/

**Secondary / analyst**
- Bits&Chips, 26 Aug 2026 — https://bits-chips.com/article/besi-faces-longer-wait-as-sk-hynix-pushes-hybrid-bonding-to-hbm5/
- Bits&Chips, 22 Oct 2026 — https://bits-chips.com/article/besi-sees-increasing-momentum-for-hybrid-bonding/
- 36Kr EN, 25 Aug 2026 — https://eu.36kr.com/en/p/3954225477991553
- Herald Business, 20 Sep 2026 — https://biz.heraldcorp.com/article/10878775
- TrendForce, 7 Jul 2026 — https://www.trendforce.com/news/2026/07/07/news-samsung-sk-hynix-reportedly-reconsider-hybrid-bonding-timeline-16-high-hbm4e-may-be-earliest-adoption/
- TrendForce, 1 Apr 2026 — https://www.trendforce.com/news/2026/04/01/news-jedec-reportedly-plans-to-relax-hbm-height-specs-to-900%C2%B5m-potentially-slowing-hybrid-bonding-adoption/
- 3DNews, 3 Apr 2026 — https://3dnews.ru/1139386/jedec-razreshit-pamyati-hbm4e-podrasti-radi-uproshcheniya-proizvodstva-i-snigeniya-tseni
- SemiEngineering, 13 Jan 2026 — https://semiengineering.com/hbm4-sticks-with-microbumps-postponing-hybrid-bonding/
- TrendForce, 13 Jan 2026 — https://www.trendforce.com/news/2026/01/13/news-sk-hynix-may-stick-with-mr-muf-for-hbm4-16-high-despite-asmpt-tc-bonder-orders/
- TrendForce, 12 Dec 2025 — https://www.trendforce.com/news/2025/12/12/news-sk-hynix-reportedly-places-hbm4-tc-bonder-order-with-asmpt-as-hanmi-hanwha-patent-clash-heats-up/
- TrendForce, 9 Jun 2026 — https://www.trendforce.com/news/2026/06/09/news-sk-hynix-reportedly-places-44-2bn-won-tc-bonder-order-with-hanmi-accelerating-hbm4-ramp-up/
- Korea Times, 8 Jun 2026 — https://www.koreatimes.co.kr/business/tech-science/20260608/sk-hynix-orders-new-equipment-worth-287-mil-for-next-gen-hbm4
- TrendForce, 7 Oct 2025 — https://www.trendforce.com/news/2025/10/07/news-hybrid-bonder-equipment-market-reportedly-near-2b-by-2028-as-korean-makers-race-to-next-gen-hbm-tools/
- Asia Economy, 22 Dec 2025 — https://view.asiae.co.kr/en/article/2025122209224722092
- Asia Economy, 6 Apr 2026 — https://view.asiae.co.kr/en/article/2026040613193475063
- Asia Economy, Jul 2024 — https://view.asiae.co.kr/en/article/2024071607095917092
- MTN, 13 Feb 2026 — https://news.mtn.co.kr/news-detail/2026021317395078451
- Money Today, 30 Oct 2026 — https://www.mt.co.kr/en/industry/2026/10/30/2026103010252581828
- Herald, 4 Nov 2026 — https://mbiz.heraldcorp.com/article/10925615
- Stockanalysis (filing-based aggregator), Hanmi quarterly financials, accessed 12 Nov 2026 [Q1-25 to Q2-26] — https://stockanalysis.com/quote/krx/042700/financials/?p=quarterly
- Dr. Web, 28 Oct 2026 — https://www.drweb.de/asmpt-quartalszahlen-chipsparte-hbm/
- TheOutpost/Investing.com, TEL, 30 Oct 2026 (superseded by primary) — https://theoutpost.ai/news-story/tokyo-electron-q2-profit-jumps-27-as-ai-demand-for-semiconductor-equipment-accelerates-32910/
- Gyokai Digest/TDnet, Disco preliminary, 6 Oct 2026 — https://www.gyokaidigest.com/en/disclosures/6146-tdnet-20261006-140120261006546587
- MarketBeat, Camtek Q3 call, 4 Nov 2026 — https://www.marketbeat.com/instant-alerts/transcript-camtek-q3-earnings-call-highlights-2026-11-04/
- MarketBeat, K&S FQ1-26 call, 5 Feb 2026 (search excerpt only) — https://www.marketbeat.com/instant-alerts/kulicke-and-soffa-industries-q1-earnings-call-highlights-2026-02-05/?.tsrc=rss
- RTTNews, 26 Oct 2026 — https://www.rttnews.com/3703117/applied-materials-to-increase-stake-in-be-semiconductor-industries-to-about-20.aspx
- Tech Investments (analyst; date not captured) — https://www.techinvestments.io/p/hbmdie-bonding-semicap-outlook
- Digg aggregation, Hanwha HB cluster (undated) — https://digg.com/tech/vvqd1wro
- Tom's Hardware (headline only) — https://tomshardware.com/tech-industry/semiconductors/hybrid-bonding-roadmap-examined

### Inferences
- Confidence in the HBM5 slip is high: several independent Korean and international outlets agree, and Besi's own wording (development-stage memory orders; lower stacks extended) is consistent with it.

### Gaps
- Blocked or paywalled: Applied's website release (403), ctol.digital (403), Bits&Chips full text, jedec.org (403), Piotech (503).
