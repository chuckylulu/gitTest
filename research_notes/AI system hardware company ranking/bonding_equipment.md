# Bonding equipment for chip stacking — thermo-compression (TC) bonders, hybrid (direct Cu-Cu) bonders D2W/W2W, thinning/dicing, inspection/metrology — notes as of 12 November 2026

Research date: 12 Nov 2026. Scope: equipment makers and what memory/logic customers have qualified and ordered (HBM economics excluded; covered elsewhere). No share prices, valuation multiples, market caps, price targets or share-price moves are collected here.

Labels used: [P] primary (company release/filing); [S] secondary (trade press, aggregator, call summary); [A] analyst / market-research estimate; [CC] company claim, unconfirmed by any outside party; [D] derived by me from cited figures (arithmetic shown or stated).

Method caveat (important for the report writer): the session's shared web-search budget (200 searches per turn, shared across all agents) ran out part-way through this workstream. After that point I only fetched pages already found, and did not use other search engines to get around the limit. As a result, coverage of mainland China, Taiwan, India, EV Group, Shibaura, Toray Engineering, Yamaha Robotics, Semes/Hanwha financials, Applied Materials' latest quarter, Kulicke & Soffa's latest quarter, and the inspection names other than Camtek is THIN and mostly flagged as unverified. Primary documents were obtained for BESI (Q3-2026 release, full PDF), Disco (Tanshin for Apr–Sep 2026) and Camtek (Form 6-K for Q3-2026).

---

## (1) Segment map — companies worldwide

### Takeaway
The HBM stacking-tool market in 2025–26 is still a thermo-compression (TC) market. Hanmi had ~71% of HBM TC-bonder revenue through Q3-2025 (TechInsights), but SK hynix now dual-/triple-sources from ASMPT and Hanwha. Hybrid bonding (HB) is in volume today mainly in logic: BESI is the D2W leader and is now allied with Applied Materials, which is raising its BESI stake to ~20%. W2W bonding (EV Group, Tokyo Electron, SUSS) is a separate, older market. Disco is the thinning/dicing constraint in both eras. Inspection "judges" (Camtek, Onto, KLA) gate bump and stack quality, but HB inspection is still small. Coverage is thin for China, Taiwan and India, mainly because the search budget ran out; India appears to have no relevant equipment maker, but I could not re-verify this.

### Cited Findings

**Map table** (Evidence column: a link means sourced in this session; "UNVERIFIED" means background knowledge not re-confirmed in H2-2026 sources, see §7)

| Company | Home | Listing / ticker | Role in segment | Why it matters / why left out | Evidence |
|---|---|---|---|---|---|
| BE Semiconductor Industries (Besi) | Netherlands | Euronext Amsterdam: BESI (OTC: BESIY) | D2W hybrid bonders; "TC Next" TC bonders; flip-chip and multi-module die attach; photonics die attach | D2W HB leader; 23 HB customers and >215 systems cumulative demand [CC]; Applied raising its stake to ~20% | [Besi Q3-2026 release, 22 Oct 2026](https://www.besi.com/fileadmin/user_upload/PR_Q3-2026.pdf) [P] |
| Hanmi Semiconductor | South Korea | KRX: 042700 | HBM TC bonders (TC Bonder 4 / 4.5 "Griffin"); wide TC bonder (planned late 2026); HB plant (target end-2026); 2.5D/FC bonders | HBM TC-bonder share leader (TechInsights 71.2% of revenue, cumulative to Q3-2025) | [Asia Economy, 22 Dec 2025](https://view.asiae.co.kr/en/article/2025122209224722092) [S/A]; ticker from [Akrostec](https://www.akrostec.com/indices/AKMNF50/events/2026-06-08t00-00-00z-hanmi-semiconductor-co-ltd-042700-other-17a77ad0) |
| ASMPT | Singapore HQ; Hong Kong-listed | HKEX: 0522 | TC bonders (C2S, C2W, HBM); 2nd-gen HB (sampling); photonics/CPO tools; SMT (under strategic review) | ~half of SK hynix's ~50 HBM4 TC bonder sets (Dec 2025); record bookings in Q3-2026 | [TrendForce citing The Elec, 12 Dec 2025](https://www.trendforce.com/news/2025/12/12/news-sk-hynix-reportedly-places-hbm4-tc-bonder-order-with-asmpt-as-hanmi-hanwha-patent-clash-heats-up/) [S]; [Dr. Web, 28 Oct 2026](https://www.drweb.de/asmpt-quartalszahlen-chipsparte-hbm/) [S] |
| Semes | South Korea | Private (Samsung Electronics subsidiary) | Captive TC bonders for Samsung HBM; going "straight to hybrid bonders" | No. 2 HBM TC share (TechInsights 13.1%, cumulative to Q3-2025); captive access to Samsung | [Asia Economy, 22 Dec 2025](https://view.asiae.co.kr/en/article/2025122209224722092); [MTN, 13 Feb 2026](https://news.mtn.co.kr/news-detail/2026021317395078451) [S] |
| Hanwha Semitech | South Korea | Not separately listed (Hanwha group; parent listing UNVERIFIED) | TC bonders for SK hynix (2025 contracts); 2nd-gen HB "SHB2 Nano"; D2W HB cluster reportedly at SK hynix for evaluation | SK hynix second/third source; in a patent fight with Hanmi | [TrendForce, 12 Dec 2025](https://www.trendforce.com/news/2025/12/12/news-sk-hynix-reportedly-places-hbm4-tc-bonder-order-with-asmpt-as-hanmi-hanwha-patent-clash-heats-up/); [TrendForce, 7 Oct 2025](https://www.trendforce.com/news/2025/10/07/news-hybrid-bonder-equipment-market-reportedly-near-2b-by-2028-as-korean-makers-race-to-next-gen-hbm-tools/) [S] |
| Yamaha Robotics (Shinkawa) | Japan | Subsidiary of Yamaha Motor (parent ticker UNVERIFIED: TSE 7272) | TC bonders (Micron, Samsung) | TechInsights 5.6% HBM TC share (cumulative to Q3-2025) | [Asia Economy, 22 Dec 2025](https://view.asiae.co.kr/en/article/2025122209224722092); [Asia Economy, 2024](https://view.asiae.co.kr/en/article/2024071607095917092) [S] |
| Toray Engineering | Japan | Subsidiary of Toray Industries (UNVERIFIED: TSE 3402) | TC bonders; historical Samsung supplier | Minor in HBM by 2025 (absent from TechInsights top 4) | [Asia Economy, 2024](https://view.asiae.co.kr/en/article/2024071607095917092) [S, dated] |
| Kulicke & Soffa | US (operations HQ Singapore — UNVERIFIED) | Nasdaq: KLIC | Fluxless TC bonders (formic-acid and plasma) | ~120 TCB systems in the field, half fluxless (fiscal Q1-2026); memory volume production expected FY2027 [CC] | Search-result excerpts of [MarketBeat FQ1-2026 call](https://www.marketbeat.com/instant-alerts/kulicke-and-soffa-industries-q1-earnings-call-highlights-2026-02-05/?.tsrc=rss) and [FQ2-2026 call](https://www.marketbeat.com/instant-alerts/kulicke-and-soffa-industries-q2-earnings-call-highlights-2026-05-08/) [S; pages not fetched] |
| Applied Materials | US | Nasdaq: AMAT (ticker UNVERIFIED but standard) | Co-develops integrated D2W HB systems with Besi ("Kinex" platform); EPIC Center; ~9% → ~20% Besi stake | Front-end giant entering HB through a specialist alliance | [Besi, 27 Oct 2026](https://www.besi.com/investor-relations/press-releases/details/applied-materials-to-increase-its-strategic-investment-in-be-semiconductor-industries/) [P]; [Bits&Chips, 26 Aug 2026](https://bits-chips.com/article/besi-faces-longer-wait-as-sk-hynix-pushes-hybrid-bonding-to-hbm5/) [S] |
| Tokyo Electron (TEL) | Japan | TSE: 8035 | W2W bonders and laser debond (product names UNVERIFIED); dominant front-end etch/deposition/coat | Group strength; China 36.4% of Jul–Sep 2026 revenue; bonding-specific data not disclosed | [TheOutpost / Investing.com, 30 Oct 2026](https://theoutpost.ai/news-story/tokyo-electron-q2-profit-jumps-27-as-ai-demand-for-semiconductor-equipment-accelerates-32910/) [S] |
| EV Group (EVG) | Austria | Private | W2W fusion/hybrid bonders (CIS, 3D NAND, backside power), D2W collective bonding, temporary bonding | Believed W2W leader; no 2026 data gathered | UNVERIFIED |
| SUSS MicroTec | Germany | Xetra: SMHN | Temporary bonding/debonding (HBM TSV wafers); W2W HB (UNVERIFIED); coaters; UV scanners incl. panel | Record H1-2026 orders, HBM-linked bonding orders | [SUSS H1-2026 release via Placera, 6 Aug 2026](https://www.placera.se/pressmeddelanden/suss-microtec-order-book-reaches-record-of-473-7-million-providing-strong-visibility-for-2027-20260806) [P via wire] |
| Shibaura Mechatronics | Japan | TSE: 6590 (UNVERIFIED) | Flip-chip / D2W bonders incl. HB (UNVERIFIED) | Listed by the coordinator; no 2026 evidence gathered | UNVERIFIED |
| LG Electronics (production-technology unit) | South Korea | KRX: 066570 (UNVERIFIED) | Developing HBM hybrid bonders; mass production targeted by 2028 | Possible captive/third-party entrant | [TrendForce citing SeDaily, 7 Oct 2025](https://www.trendforce.com/news/2025/10/07/news-hybrid-bonder-equipment-market-reportedly-near-2b-by-2028-as-korean-makers-race-to-next-gen-hbm-tools/) [S] |
| ASML | Netherlands | Euronext: ASML | Not a D2W HB competitor according to Besi; works with Besi on die stress and placement accuracy | Left out as a bonder; possible long-term 3D-transistor-stacking interest | [Besi Q3-2026 release](https://www.besi.com/fileadmin/user_upload/PR_Q3-2026.pdf) [P, CC] |
| Disco | Japan | TSE: 6146 | Grinders (thinning), dicers (blade, laser, stealth), consumables (blades, wheels) | Thinning/dicing constraint in both TC and HB eras; record shipments | [Disco Tanshin, 22 Oct 2026](https://www.disco.co.jp/jp/ir/library/doc/fr/fr20261022.pdf) [P] |
| Tokyo Seimitsu (Accretech) | Japan | TSE: 7729 (UNVERIFIED) | Grinders/polishers, dicers, probers | Likely No. 2 to Disco; no 2026 data gathered | UNVERIFIED |
| EO Technics | South Korea | KOSDAQ: 039030 (UNVERIFIED) | Laser grooving/dicing | Possible HBM laser supplier; not verified | UNVERIFIED |
| Camtek | Israel | Nasdaq: CAMT (SEC filer) | 2D/3D inspection and metrology for advanced packaging, HBM, CoWoS | Closest listed "judge" for bump/stack quality; AP ~80% of sales | [Camtek 6-K, 4 Nov 2026](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326005000/zk2636329.htm) [P] |
| Onto Innovation | US | NYSE: ONTO (UNVERIFIED) | Packaging inspection/metrology; joint development with Samsung on inspection | HB/HBM inspection contender | [TrendForce, 1 Apr 2026](https://www.trendforce.com/news/2026/04/01/news-jedec-reportedly-plans-to-relax-hbm-height-specs-to-900%C2%B5m-potentially-slowing-hybrid-bonding-adoption/) [S] |
| KLA | US | Nasdaq: KLAC (UNVERIFIED) | Broad process control incl. packaging inspection | Likely the largest "judge" overall; no 2026 data gathered | UNVERIFIED |
| Nova | Israel | Nasdaq/TASE: NVMI (UNVERIFIED) | Dimensional/materials metrology incl. advanced packaging | Possible HB metrology role; not verified | UNVERIFIED |
| Park Systems | South Korea | KOSDAQ: 140860 (UNVERIFIED) | Atomic-force microscopes (Cu pad recess/roughness, critical for HB) | Natural HB surface "judge"; not verified | UNVERIFIED |
| Lasertec | Japan | TSE: 6920 (UNVERIFIED) | Mainly EUV mask inspection | Left out: little packaging relevance found | UNVERIFIED |
| Mainland China: Piotech (SSE STAR 688072), U-Precision (unlisted), iSABers (private), Maxwell (SZSE 300751), Kingsemi (688037), Hwatsing (688120, thinning/CMP), GL Tech (300480, dicing), Skyverse (688361, inspection) | China | as listed (all UNVERIFIED) | HB/W2W bonders, temporary bonding, thinning, dicing, inspection | Domestic substitution, potential CXMT/YMTC suppliers; NO 2026 evidence gathered | UNVERIFIED — region thin (search budget exhausted; Chinese-language sources not reached) |
| Taiwan: Gallant Micro/GPM (TPEx 6640), Scientech (3583), GPTC (3131), All Ring (6187), C Sun (2467) | Taiwan | as listed (all UNVERIFIED) | CoWoS-line die bonders/sorters, wet/debond, dispensing/AOI, curing | TSMC CoWoS supply chain; no 2026 evidence gathered | UNVERIFIED — region thin (MOPS not reached) |
| India | — | — | No bonding, thinning, dicing or packaging-inspection equipment maker identified | Indian ATMP/OSAT projects buy imported tools | UNVERIFIED (not re-checked on NSE/BSE) |

**Segment-level facts: TC-bonder shares, customers, qualification, fluxless, disputes**
- HBM TC-bonder revenue share, cumulative Jan–Sep 2025 (TechInsights "2025 TC Bonder Market Report", as cited by Hanmi, published 22 Dec 2025): Hanmi 71.2%, Semes 13.1%, ASMPT 5.6%, Yamaha Robotics 5.6%. TechInsights expects ~13% CAGR to 2030 and a rebound from 2026 after "a temporary normalization process for TC bonders in 2025" — [Asia Economy, 22 Dec 2025](https://view.asiae.co.kr/en/article/2025122209224722092) [A relayed by an interested party]
- Hanmi's HBM TC revenue, cumulative to Q3-2025, was US$247.7m (~KRW 366bn) per the same report — [Asia Economy, 22 Dec 2025](https://view.asiae.co.kr/en/article/2025122209224722092) [S/A]
- **SK hynix:** Hanmi was the exclusive HBM TC-bonder supplier until 2024. ASMPT joined near the end of 2024 (Oct-2024 order for dozens of tools for HBM3E 12-high), and Hanwha Semitech entered in early 2025. In Apr-2025 Hanmi recalled ~60 support engineers from SK hynix, "widely viewed as a protest". In Nov-2025 SK hynix ordered seven dual-head ASMPT TC bonders (~KRW 30bn, ~KRW 4bn each) for HBM4. About 50 TC bonder sets were in HBM4 use, roughly half from ASMPT; Hanwha's bonders were "not currently in use" (Dec 2025) — [TrendForce citing The Elec, 12 Dec 2025](https://www.trendforce.com/news/2025/12/12/news-sk-hynix-reportedly-places-hbm4-tc-bonder-order-with-asmpt-as-hanmi-hanwha-patent-clash-heats-up/) [S]
- SK hynix awarded Hanmi a KRW 44.2bn order for TC Bonder 4.5 "Griffin" for HBM4 (~15 tools at ~KRW 3bn each, delivery to Cheongju by 2 Sep 2026). A Jan-2026 order was ~KRW 9.6–9.7bn — [TrendForce, 9 Jun 2026](https://www.trendforce.com/news/2026/06/09/news-sk-hynix-reportedly-places-44-2bn-won-tc-bonder-order-with-hanmi-accelerating-hbm4-ramp-up/); [Korea Times, 8 Jun 2026](https://www.koreatimes.co.kr/business/tech-science/20260608/sk-hynix-orders-new-equipment-worth-287-mil-for-next-gen-hbm4) [S]
- Hanmi patent suit against Hanwha Semitech filed Dec-2024; Hanwha sought invalidation May-2025 and countersued ~Oct-2025 — [TrendForce, 12 Dec 2025](https://www.trendforce.com/news/2025/12/12/news-sk-hynix-reportedly-places-hbm4-tc-bonder-order-with-asmpt-as-hanmi-hanwha-patent-clash-heats-up/) [S]
- Hanwha Semitech reportedly supplied an integrated D2W HB cluster to SK hynix for quality evaluation and won an extra HBM4 TC order (single "exclusive" report; date not visible) — [Digg aggregation](https://digg.com/tech/vvqd1wro) [S, unconfirmed]
- **Samsung:** TC bonders come mainly from Semes and Shinkawa (Toray historically). Semes' share rose as it adapted to TC-NCF (2024 reporting) — [Asia Economy, 2024](https://view.asiae.co.kr/en/article/2024071607095917092); [Asia Economy, 3 Jun 2024](https://www.asiae.co.kr/en/article/2024060313461781042) [S, dated]. No 2026 source on Samsung's HBM4 vendor mix was found.
- **Micron:** Shinkawa plus Hanmi (Hanmi added as second source for HBM3E). Micron has tested ASMPT and Besi (Macquarie view) — [Tech Investments](https://www.techinvestments.io/p/hbmdie-bonding-semicap-outlook) [A/S]
- **CXMT:** no source found on its bonder suppliers (see §7).
- **Qualified for HBM4:** Hanmi TC Bonder 4 entered mass production for HBM4 in Jul-2025, and Griffin 4.5 was ordered for HBM4 in Jun-2026; ASMPT tools are in HBM4 use at SK hynix — [Asia Economy, 22 Dec 2025](https://view.asiae.co.kr/en/article/2025122209224722092); [TrendForce, 12 Dec 2025](https://www.trendforce.com/news/2025/12/12/news-sk-hynix-reportedly-places-hbm4-tc-bonder-order-with-asmpt-as-hanmi-hanwha-patent-clash-heats-up/) [S]
- **Planned for HBM4E:** SK hynix reportedly told investors it keeps its current process (MR-MUF with TC) through HBM4 and HBM4E 16-high. At CES 2026 it showed a 16-high HBM4 using MR-MUF with DRAM thinned to 30 µm to fit 775 µm — [TrendForce, 13 Jan 2026](https://www.trendforce.com/news/2026/01/13/news-sk-hynix-may-stick-with-mr-muf-for-hbm4-16-high-despite-asmpt-tc-bonder-orders/) [S]. Demand is rising for Hanmi's Wide TC Bonder as makers enlarge die area instead of adopting HB — [TrendForce, 7 Jul 2026](https://www.trendforce.com/news/2026/07/07/news-samsung-sk-hynix-reportedly-reconsider-hybrid-bonding-timeline-16-high-hbm4e-may-be-earliest-adoption/) [S]
- **Fluxless:** SK hynix began full-scale fluxless evaluations in Q4-2025 for HBM4 16-high; "the evaluation results failed to meet expectations" and it judged the technology "premature given performance and cost" — [TrendForce citing DealSite, 13 Jan 2026](https://www.trendforce.com/news/2026/01/13/news-sk-hynix-may-stick-with-mr-muf-for-hbm4-16-high-despite-asmpt-tc-bonder-orders/) [S]. At K&S, formic-acid fluxless is in high-volume production (logic), plasma fluxless is in qualification at a major foundry, and memory volume production is expected FY2027 [CC] — K&S FQ1-2026 call (search-result excerpt; [MarketBeat](https://www.marketbeat.com/instant-alerts/kulicke-and-soffa-industries-q1-earnings-call-highlights-2026-02-05/?.tsrc=rss)) [S, page not fetched]
- ASMPT's HBM business: repeat orders from HBM makers, but "the timing of customers' new tool purchase decisions remains dependent on HBM4 product rollout schedules"; it has an exclusive joint evaluation programme with a key memory player (H1-2026) — [ASMPT interim release, 1 Aug 2026](https://news.marketersmedia.com/asmpt-announces-2026-interim-results-multiple-advanced-packaging-solutions-drive-strong-performance/89199421) [P via wire]. In Q3-2026 "memory makers are delaying larger bonding-tool purchases while they reassess the HBM4 roadmap" — [Dr. Web, 28 Oct 2026](https://www.drweb.de/asmpt-quartalszahlen-chipsparte-hbm/) [S]

### Inferences
- 2026 TC-bonder share by supplier is not published in anything I found. The order flow points to Hanmi's SK hynix share falling from ~100% (2024) toward roughly half for HBM4, with ASMPT taking most of the rest, and Hanmi regaining some volume in mid-2026 [D from the cited orders].
- Customer-qualification gates (SK hynix's yield and lifetime bars, Samsung's captive Semes, NVIDIA stack-height choices) decide supplier share more than supplier technology does.

### Gaps
- No 2026 market-share data (TechInsights, Yole) by supplier or by customer; no CXMT bonder data; no Samsung or Micron 2026 vendor split.
- Many map rows are UNVERIFIED (see §7), especially China, Taiwan, India, EVG, Shibaura, Toray, Tokyo Seimitsu and the inspection names other than Camtek.

---

## (2) Evidence on tests (a)–(e) for the key companies
Key companies chosen: **Besi, Disco, Tokyo Electron, Camtek, ASMPT, Hanmi**, with a short entry on **SUSS**. EV Group, Applied Materials and Kulicke & Soffa matter, but the evidence gathered on them was too thin for full tests.

### Takeaway
On the evidence available, Disco and Besi have the strongest combination of position, margins and cash. Disco owns a thinning/dicing constraint and earns consumables revenue that tracks customer utilisation. Besi owns D2W HB know-how and runs a 45.8% operating margin. Tokyo Electron is a high-quality, diversified front-end giant whose bonding business is small and undisclosed. Camtek is the clearest "judge", but its HB role lies in 2028 and later. ASMPT is diversified but lower-margin, with its TCB line exposed to HBM timing. Hanmi has 50% operating margins on a bridge product with concentrated customers and an unproven successor.

### Cited Findings

#### Besi (Netherlands) — primary: Q3-2026 release, 22 Oct 2026 ([PDF](https://www.besi.com/fileadmin/user_upload/PR_Q3-2026.pdf); [release page](https://www.besi.com/investor-relations/press-releases/details/be-semiconductor-industries-nv-announces-q3-2026-results/))

**(a) Position**
- Product lines: D2W hybrid bonding (SUCCESSOR); TC Next (TC bonder, BRIDGE for HBM; for logic, a successor to mass reflow); flip-chip and multi-module die attach (mainstream); photonics/CPO assembly.
- 2026 HB orders came from logic, CPO and memory: "Year to date, hybrid bonding orders have more than doubled versus fiscal 2025 as orders for HBM applications increased, more logic chiplet programs entered production, co-packaged optics use cases expanded faster than anticipated and edge AI device production began." HB adoption reached 23 customers and cumulative unit demand passed 215 systems [P, CC]
- "Of note, we received orders for both hybrid bonding and TC Next systems from a leading memory customer as they focus on the development of current and next generation HBM device structures." [P, CC; customer unnamed]
- On HBM timing: "Severe memory shortages this year have extended the use of lower stack heights in current HBM production beyond prior expectations." Besi expects HB to be "adopted in a range of stack heights over the next two years" and in stacks with "direct bonding of DRAM onto accelerator chips by the end of the decade" [P, CC]
- Besi does "not view ASML as a hybrid bonding competitor"; the two work jointly on die-stress programmes for placement accuracy [P, CC]
- HB slip record for HBM: expected at HBM4 → kept TC → 16-high HBM4E reported as earliest (Jul 2026) → SK hynix says HBM5 at the earliest (Aug 2026) — see §5.
- Besi owns no "judge". Its moat is process know-how in high-accuracy D2W placement. The outside signal is Applied's decision to raise its stake (below).

**(b) Lead — outside evidence**
- Applied Materials announced on 26 Oct 2026 that it would raise its Besi stake from ~9% to ~20% via an accelerated share purchase agreement (Form 8-K), subject to US antitrust review. Applied does not intend to seek a board seat and has no current plans to go above ~20%. The firms have collaborated since 2020 on "integrated hybrid bonding production systems", and Besi became an EPIC Center Innovation Partner (1 Oct 2026) — [Besi, 27 Oct 2026](https://www.besi.com/investor-relations/press-releases/details/applied-materials-to-increase-its-strategic-investment-in-be-semiconductor-industries/) [P]; [RTTNews, 26 Oct 2026](https://www.rttnews.com/3703117/applied-materials-to-increase-stake-in-be-semiconductor-industries-to-about-20.aspx); [TechNews TW, 28 Oct 2026](https://finance.technews.tw/2026/10/28/applied-materials-plans-to-raise-stake-in-besi-to-20/) [S]
- SK hynix "reportedly ordered" a pilot HB production line combining Applied and Besi equipment (the "Kinex" D2W platform) — [Bits&Chips, 26 Aug 2026](https://bits-chips.com/article/besi-faces-longer-wait-as-sk-hynix-pushes-hybrid-bonding-to-hbm5/) [S]
- Besi "currently leads the hybrid bonding market" — [TrendForce, 1 Apr 2026](https://www.trendforce.com/news/2026/04/01/news-jedec-reportedly-plans-to-relax-hbm-height-specs-to-900%C2%B5m-potentially-slowing-hybrid-bonding-adoption/) [S, no share figure]
- HB is "currently used mainly in logic" — [Bits&Chips, 22 Oct 2026](https://bits-chips.com/article/besi-sees-increasing-momentum-for-hybrid-bonding/) [S]
- Customer counts (15 at YE-2025 → 21 at end Q2-2026 → 23 in Q3-2026) are company figures — [Stock Titan copy of Q2-26 release](https://www.stocktitan.net/news/BESIY/be-semiconductor-industries-n-v-announces-q2-26-and-h1-26-v0syj60xvlwf.html) [P via wire, CC]

**(c) Revenue model**
- Mostly one-off equipment. The Q3 release discloses no service/spares share. Gross-margin gains came from "a more favorable product mix and price increases" (Q3-26 vs Q3-25) and "the pass through of price increases" (YTD) — evidence of pricing power [P]
- Labour flexibility: 402 temporary FTE (17%) of 2,403 total at 30 Sep 2026, versus 2,085 a year earlier. Revenue does not depend on labour hours or per-seat pricing [P]

**(d) Financial strength** (period: quarter to 30 Sep 2026; published 22 Oct 2026) [P unless marked]
- Q3-26: revenue €283.4m (+13.4% q/q, +113.6% y/y); orders €342.6m (+17.0% q/q, +96.1% y/y); gross margin 65.2%; operating income €129.7m (45.8% of revenue); EBITDA €139.9m (49.4%); net income €107.2m (37.8%); effective tax 13.3%; R&D (reported) €23.5m (8.3% of revenue).
- 9M-26: revenue €718.1m (+69.0%); orders €905.2m (+108.3%); GM 64.9%; operating income €302.4m; net income €247.8m. LTM orders "€1.2 billion" (CEO).
- FY2025 [D: sum of the release's quarterly table]: revenue €591.3m; orders €685.0m; operating income €173.1m; net income €131.7m. LTM to Q3-26 [D]: revenue €884.6m; operating income €358.6m; net income €290.6m.
- Cash: gross cash €591.9m; long-term debt (convertible notes) €345.3m, down from €508.1m at 31 Mar 2026 (equity rose €116m in Q2, consistent with a conversion [D, inference]); net cash €246.6m (−€7.8m at 30 Sep 2025).
- Free cash flow [D]: Q3-26 operating CF €107.1m − capex €2.8m − capitalised development €5.7m = ~€98.6m; 9M-26 €247.9m − €6.9m − €17.5m = ~€223.5m (~31% of revenue). Capex is very light (9M €6.9m, ~1% of revenue).
- Returns [D, rough]: LTM NOPAT ~€311m on net operating capital ~€425m implies ROIC around 70%+; LTM ROE ~54% on average equity. Both are sensitive to cash treatment.
- Shareholder returns: 9M-26 dividends €125.4m and buybacks €44.7m; a new €100m buyback runs from 27 Oct 2026.
- **Country concentration (revenue by customer location):** China €97.1m = 34% of Q3-26 (Q2-26 39%; Q1-26 46%; Q4-25 45%; Q3-25 41%); Asia-Pacific excluding China 56%; EU/USA/Other 10%. China was ~40% of LTM revenue [D]. Orders: China €137.5m = 40% of Q3-26 orders.
- **Customer type:** Q3-26 orders 41% IDMs / 59% foundries + subcontractors (Q1-26: 30%/70%).
- **Largest customer / top-5 share:** NOT DISCLOSED in the release (annual report not fetched — gap).
- Manufacturing footprint: "a substantial portion of our production facilities" in Asia-Pacific (release risk section; countries not named in the release).

**(e) Resilience and cycle**
- Cycle position: orders rose from €128.0m (Q2-25) to €342.6m (Q3-26), a 2.7x swing in five quarters [D] — high operating leverage both ways. Q4-26 guide: revenue flat ±5% "as certain customers request delivery dates for Q3-26 orders in alignment with H1-27 production capacity plans"; GM 63–65%; opex +5–10% "due primarily to higher strategic consulting costs" (unexplained) [P]. Inventories €122.7m vs €104.1m at Dec-25 [P].
- Export controls/tariffs: the release carries only generic tariff and export-regulation risk language. China at 34–46% of quarterly revenue through 2026 shows its tools were still shipping into China as of Q3-26 [P; inference on controls].

#### Disco (Japan) — primary: Tanshin for Apr–Sep 2026, 22 Oct 2026 ([PDF](https://www.disco.co.jp/jp/ir/library/doc/fr/fr20261022.pdf))

**(a) Position**
- Grinders (wafer thinning to the 30–50 µm range used in HBM), dicers (blade, laser) and consumables (blades, wheels). These are needed in both the TC era and the HB era, so they are neither BRIDGE nor SUCCESSOR but tool-agnostic (inference; product facts from the release narrative). The Tanshin says demand for advanced logic and HBM stayed high, shipments were led by high-value products, and consumables shipments stayed high, "linked to customers' equipment utilisation" (顧客の設備稼働率等に連動) [P]
- Owns a physical/process constraint (thinning and singulation know-how plus consumables), not a judge [inference].

**(b) Lead**
- Record shipments are outcome evidence [P]. No third-party market share was obtained in this session (gap).

**(c) Revenue model**
- Consumables revenue tracks customer utilisation (recurring). Its share of sales was not obtained (gap) [P qualitative].
- Contract liabilities (customer advances) rose to ¥79.6bn at 30 Sep 2026 from ¥50.0bn at 31 Mar 2026 — prepayment evidence [P].

**(d) Financial strength** (H1 = Apr–Sep 2026; published 22 Oct 2026) [P]
- Shipments ¥284.6bn (+37.2% y/y); net sales ¥257.1bn (+32.1%); gross profit ¥183.9bn (GM 71.5% vs 68.9% a year earlier [D]); operating income ¥116.6bn (+47.9%, margin 45.4%); net income ¥80.4bn (+43.7%, margin 31.3%).
- Balance sheet: cash and deposits ¥342.4bn; no interest-bearing debt on the balance sheet; equity ratio 76.1%; inventories ~¥160.8bn vs ~¥141.3bn at Mar-26 [D].
- Cash flow: operating CF ¥111.7bn (+181.5%); PP&E capex ¥12.9bn; company-defined FCF (OCF + ICF, after a ¥41.8bn increase in time deposits) ¥56.9bn; FCF excluding deposits ~¥98.8bn [D]; dividends paid ¥40.8bn.
- Returns [D]: annualised ROE ~26% (2 × ¥80.4bn on average equity ~¥607bn).
- Guidance (first disclosure for Apr–Dec 2026): sales ¥389.5bn (+28.2%), operating income ¥174.7bn (+38.4%), net income ¥121.9bn; shipments ¥434.2bn. This implies Oct–Dec 2026 sales ~¥132.4bn and operating income ~¥58.1bn (~44%), with shipments ~¥149.6bn, a new quarterly record [D]. FX assumption ¥151/USD.
- Preliminary Jul–Sep 2026 non-consolidated shipments were ¥123.9bn (+60.0% y/y, record) and non-consolidated sales ¥118.5bn (+38.9%) — [Gyokai Digest of TDnet, 6 Oct 2026](https://www.gyokaidigest.com/en/disclosures/6146-tdnet-20261006-140120261006546587) [S]. Secondary reports call this a miss against the ¥128.5bn forecast, but the comparison may mix non-consolidated and consolidated bases. Derived consolidated Q2 sales are ~¥142.7bn (H1 ¥257.1bn minus Q1 ¥114.3bn per a secondary Japanese summary) — unverified.
- Customer and country concentration: NOT OBTAINED (Disco's regional and product splits are in its supplementary materials, not fetched).

**(e) Resilience**
- Debt-free, cash-rich, utilisation-linked consumables, and rising customer advances. A capex pause would hit equipment shipments but leave the consumables base [inference]. Exposure to Japanese and US export controls on China was not verified (gap).

#### Tokyo Electron (Japan) — group-level, secondary: Investing.com via [TheOutpost, 30 Oct 2026](https://theoutpost.ai/news-story/tokyo-electron-q2-profit-jumps-27-as-ai-demand-for-semiconductor-equipment-accelerates-32910/); primary TEL release NOT fetched

**(a) Position**
- Front-end process know-how at scale (etch, deposition, coat/develop) plus W2W bonding and debond tools (bonding product details UNVERIFIED). Bonding-specific revenue is not disclosed [S].

**(b) Lead**
- Not tested for bonding (gap). The group guides that probe systems for advanced logic will rise ~60% this fiscal year [S, CC].

**(c) Revenue model**
- Q2 new-equipment sales were ¥734bn of ¥935bn revenue, implying ~¥201bn (~21%) from non-new-equipment (field solutions: service, parts, upgrades) [D; assumes revenue = new equipment + field solutions].

**(d) Financial strength** (quarter Jul–Sep 2026 = Q2 of FY to Mar 2027; published ~30 Oct 2026) [S]
- Revenue ¥935bn (+48.4% y/y); operating profit ¥295.4bn (+86.4%; ~31.6% margin [D]); net profit ¥212.6bn (+71.7%); FCF ¥310bn as reported. H1 revenue ~¥1.67tn (+41.3%) and H1 OP ¥506.8bn (+67.2%) per other summaries — consistent with Q1 ~¥732bn plus Q2 ¥935bn [D].
- FY guide: revenue ¥3.7tn, OP ¥1.169tn (+87.1%), NI ¥865bn, implying H2 revenue ~¥2.03tn [D]. Planned R&D ¥335bn and capex ¥190bn. TEL sees WFE at ~US$160bn in 2026 rising to >US$210bn in 2027 [CC].
- New-equipment mix: logic/foundry 56%, DRAM 34%, NAND 10%. China was 36.4% of quarterly revenue; FY China expected at 30–35%.
- Inconsistency flag: some aggregator headlines say "+27% profit", which conflicts with the body figures (+86.4% OP, +71.7% NI). I used the body figures.

**(e) Resilience**
- Diversified and service-backed, but China-heavy and exposed to US export controls on advanced equipment (article framing, not a TEL quote) [S].

#### Camtek (Israel) — primary: [Form 6-K, 4 Nov 2026](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326005000/zk2636329.htm); call summary [MarketBeat, 4 Nov 2026](https://www.marketbeat.com/instant-alerts/transcript-camtek-q3-earnings-call-highlights-2026-11-04/) [S]

**(a) Position**
- The closest listed "judge" in the segment: 2D/3D inspection and metrology that decides whether bumps, HBM stacks and CoWoS assemblies are good. Advanced packaging was ~80% of Q3-26 sales, mostly AI; Eagle G5 and Hawk were ~57% of systems revenue [S].
- Hybrid-bonding inspection activity is "low", not substantial in 2027, and becomes more meaningful in 2028+ — so the HB judge role is a future option, not a current position [S].
- Installed base ~4,000 systems [S, CC].

**(b) Lead**
- Orders above US$800m year-to-date (to the investor event), ~80% advanced packaging; OSATs slightly more than half; customers in all regions, including China, securing slots through 2027; first-ever one-year visibility [S, CC]. Management does not see smaller Chinese competitors as a significant threat [S, CC]. No third-party share was obtained (gap).

**(c) Revenue model**
- Service revenue ~US$40m in 2026 (~7% of ~US$595m FY revenue [D]), targeted to grow 35–40% a year toward ~US$100m within three years; AI software sales start in 2027 [S, CC].

**(d) Financial strength** (Q3-26 = quarter to 30 Sep 2026; published 4 Nov 2026) [P]
- Revenue US$161.3m (+28% y/y; +21% q/q); GM 50.0% GAAP / 51.1% non-GAAP; operating income US$39.8m GAAP (24.7%) / US$47.5m non-GAAP (29.5%); net income US$42.8m GAAP; operating CF US$71.1m.
- Cash, deposits and securities US$877.1m; convertible notes US$489.2m; net cash ~US$388m [D].
- 9M-26 revenue US$416.2m. Q4-26 guide ~US$180m (~+40% y/y); FY2026 ~US$595m; 2027 initial outlook >US$800m (~+35%). Long-term target US$1.2bn revenue in ~3 years at 34–36% operating margin [CC].
- Customer and country concentration: NOT in the 6-K; China described as "a meaningful part of the 2027 backlog" [S].

**(e) Resilience**
- Gross-margin headwinds from component shortages (memory, CPUs, handling parts) and a strong shekel; DSO ~90 days [S]. Exposure: OSAT capex, China, and Israeli operations (geopolitical risk; inference).

#### ASMPT (Singapore HQ, HKEX: 0522)

**(a) Position**
- TC bonders for logic chip-to-substrate (C2S; BRIDGE-to-successor for large AI packages), chip-to-wafer (C2W) and HBM (BRIDGE; successor HB due at HBM5); 2nd-gen HB (SUCCESSOR, at "sampling stage" with logic and memory customers [CC]); photonics/CPO; SMT (non-core, strategic review since Jan 2026) — [ASMPT interim release, 1 Aug 2026](https://news.marketersmedia.com/asmpt-announces-2026-interim-results-multiple-advanced-packaging-solutions-drive-strong-performance/89199421) [P via wire]; [Dr. Web, 28 Oct 2026](https://www.drweb.de/asmpt-quartalszahlen-chipsparte-hbm/) [S]

**(b) Lead**
- About half of SK hynix's ~50 HBM4 TC sets (Dec 2025) — [TrendForce/The Elec](https://www.trendforce.com/news/2025/12/12/news-sk-hynix-reportedly-places-hbm4-tc-bonder-order-with-asmpt-as-hanmi-hanwha-patent-clash-heats-up/) [S]
- Bulk orders for >50 C2S TCB tools from OSATs (Jul 2026); C2W bulk order from "a leading global IDM for advanced CPUs"; ultrafine-pitch TCB delivered to "the leading advanced logic customer" [CC] — [ASMPT release](https://www.asmpt.com/en/investor-relations/news-events/asmpt-secures-significant-wins/)
- Q3-26 record C2S orders came mainly from OSATs packaging for one unnamed large chipmaker [S].
- ASMPT puts the TCB addressable market above US$1.6bn by 2028 [CC].

**(c) Revenue model**
- Service and recurring share not obtained (gap).

**(d) Financial strength**
- Q3-26 (quarter to 30 Sep 2026; published 28 Oct 2026): revenue HK$5.247bn (+48.7% y/y); bookings HK$8.845bn (+137.9% y/y, record; book-to-bill ~1.69, highest since Q1-21); profit attributable HK$533m (loss a year earlier); net profit excluding one-offs ~€78.9m [S] — [10jqka, 28 Oct 2026](https://stock.10jqka.com.cn/20261028/c681160656.shtml); [Dr. Web, 28 Oct 2026](https://www.drweb.de/asmpt-quartalszahlen-chipsparte-hbm/)
- Segments Q3-26 [S]: Semiconductor Solutions revenue +1.5% q/q (Bloomberg: slightly below estimates), bookings +31.3% q/q; SMT revenue +13.2% q/q, segment profit +44.1% q/q, record bookings for a third straight quarter, including >US$100m of large or pulled-forward orders.
- Q4-26 guide: revenue US$670–730m; semiconductor revenue flat; bookings lower than Q3 [S].
- H1-26 (published 1 Aug 2026): revenue HK$8.90bn (+42.5%); bookings HK$12.75bn (+85.1%); adjusted GM 41.2% (Q2-26 42.5%); adjusted operating profit HK$1.24bn; net cash HK$3.63bn at 30 Jun 2026; Advanced Packaging revenue US$339.0m (30% of group); NEXX disposal closed 3 Jun 2026 [P via wire].
- China: SEMI mainstream revenue and bookings in China "especially strong" (no %) [P via wire]. Customer concentration not obtained.

**(e) Resilience**
- Diversification (SMT, mainstream, AP, photonics) cushions HBM timing. HBM tool purchases are being delayed as memory makers reassess HBM4 roadmaps [S]. SMT review outcome is pending.

#### Hanmi Semiconductor (Korea, KRX: 042700)

**(a) Position**
- HBM TC bonders (TC Bonder 4 / 4.5 Griffin) are a BRIDGE product: the successor (HB in HBM) is now due at HBM5 (~2029–30), which has slipped repeatedly (§5). Hanmi's own bridge extension is the Wide TC Bonder, launching late 2026 for HBM5/HBM6 [CC] — [MTN, 13 Feb 2026](https://news.mtn.co.kr/news-detail/2026021317395078451). Its HB successor plan: a KRW 100bn plant in Incheon (completion targeted end-2026) and HB for HBM6 by end-2027 [CC] — [Asia Economy, 22 Dec 2025](https://view.asiae.co.kr/en/article/2025122209224722092); [TrendForce, 7 Oct 2025](https://www.trendforce.com/news/2025/10/07/news-hybrid-bonder-equipment-market-reportedly-near-2b-by-2028-as-korean-makers-race-to-next-gen-hbm-tools/)
- Owns no judge and has no hard constraint. Its TC/MR-MUF process know-how was not enough to prevent SK hynix dual-sourcing [inference].
- KAIST Prof. Yu Hoe-jun: HB "will ultimately be adopted" and Hanmi "may fill the gap temporarily" — [MTN, 13 Feb 2026](https://news.mtn.co.kr/news-detail/2026021317395078451) [S]

**(b) Lead**
- TechInsights share 71.2% (cumulative to Q3-2025) [A]. Repeat HBM4 orders from SK hynix in 2026 [S]. Diversification: in Sep 2026 Hanmi began supplying 2.5D packaging equipment to a Taiwanese foundry (named as TSMC in the subheadline only), passing mass-production standards; it also won further FC bonder orders, and the FC Bonder 75 shipped to a global customer for the first time — [Money Today, 30 Oct 2026](https://www.mt.co.kr/en/industry/2026/10/30/2026103010252581828) [S]

**(c) Revenue model**
- One-off equipment. In 2025 Hanmi had ~60 support engineers on site at SK hynix (recalled Apr-2025), which shows field-support intensity [S]. No service share disclosed.

**(d) Financial strength** (Q3-26 = quarter to 30 Sep 2026; published 30 Oct 2026, per DART)
- Revenue KRW 181bn (+8.9% y/y); operating profit KRW 90.8bn (+33.9%); operating margin 50.2% (40.8% a year earlier). FX headwind and some revenue deferred into Q4; Hanmi expects record Q4 and a third straight record year — [Money Today, 30 Oct 2026](https://www.mt.co.kr/en/industry/2026/10/30/2026103010252581828); [Herald, 4 Nov 2026](https://mbiz.heraldcorp.com/article/10925615) [S]
- Overseas revenue averaged >72% over 15 years; Hanmi USA set up in San Jose in Oct 2026 [S].
- Net cash, FCF, capex, customer concentration (SK hynix's share of revenue) and 9M-26 totals: NOT OBTAINED (gap).

**(e) Resilience**
- Single product family and concentrated customers, a patent war with Hanwha, and SK hynix diversifying suppliers. On the other hand, every HB slip extends demand for its product (JEDEC relaxation, memory shortages keeping lower stacks) [inference from §5 evidence].

#### SUSS MicroTec (Germany, Xetra: SMHN) — short entry
- H1-26 (published 6 Aug 2026): orders Q1 €149.3m, Q2 €260.7m (record), H1 €410.0m; order book €473.7m (record), of which ~€220m is scheduled for 2027; one Q2 coating order of ~€115m from an OSAT supplying "a leading player in the AI chip module value chain". Sales H1 €202.8m vs €266.6m a year earlier (down ~24% [D]); GM H1 37.2%; EBIT margin H1 7.0%; FCF +€16.4m; cash €112.3m. 2026 guide: sales €425–485m, GM 35–37%, EBIT 8–10%. First panel-processing scanner shipped to Taiwan early Q3 — [Placera wire, 6 Aug 2026](https://www.placera.se/pressmeddelanden/suss-microtec-order-book-reaches-record-of-473-7-million-providing-strong-visibility-for-2027-20260806) [P via wire]
- Q1-26: bonding orders tied to HBM for AI modules were a key driver — [FinancialReports](https://financialreports.eu/filings/suss-microtec-se/quarterly-report/2026/43163299/) [P via aggregator]
- Q3-26 results were not found before the search budget ran out (gap).

### Inferences
- **Revenue recurrence across the group:** strongest at Disco (utilisation-linked consumables plus rising customer advances) and TEL (~21% field solutions, derived). Camtek's ~7% service is small but growing. Besi, Hanmi and ASMPT are predominantly one-off hardware sellers into a cyclical stream.
- **Resilience under the three AI-spending scenarios to 2030** (qualitative, my judgement):
  - *Steady growth (~55%):* Besi grows on logic/CPO HB with HBM HB later (HBM5). Disco grows with wafer and die counts per stack. TEL tracks WFE. Camtek grows on AP inspection. Hanmi keeps TC demand through HBM4E but faces share pressure. ASMPT grows on C2S TCB and photonics.
  - *Financing-led pause ~2028 (~25%):* Besi and Hanmi would see the sharpest order falls (Besi's orders swung 2.7x within five quarters). ASMPT is cushioned by SMT and mainstream. Disco is cushioned by consumables. TEL by field solutions. Camtek is exposed to OSAT capex.
  - *Acceleration (~20%):* HB pull-in benefits Besi/Applied, Semes and Hanwha. TC demand also rises in the near term (Hanmi, ASMPT). Disco and Camtek become capacity-bound.
- **Cycle position, Q3-2026:** records everywhere (Besi LTM orders ~€1.2bn; ASMPT book-to-bill 1.69; SUSS record backlog; Camtek >US$800m orders and slots booked through 2027; Disco record shipments and advances; TEL guiding WFE >US$210bn in 2027). Pricing is firm (Besi price increases, Camtek higher ASPs). Early digestion signals are appearing: Besi's flat Q4 with deliveries aligned to H1-27, ASMPT's lower Q4 bookings, and memory makers deferring bonder buys. This looks like a mid-to-late upcycle (inference).
- **China:** China was ~40% of Besi's LTM revenue and 36.4% of TEL's Q2 revenue. ASMPT and Camtek both cite strong China demand. Assembly, inspection and dicing tools evidently still ship to China as of Q3-2026 (inference: no binding control on these tool classes yet).

### Gaps
- Besi top-customer and top-5 shares and service share (annual report not fetched); Hanmi balance sheet, cash flow and customer concentration (DART not reached); Disco product/region split and consumables share; TEL primary release and bonding-specific revenue; ASMPT gross margin by segment in Q3-26, China %, service share; Camtek customer and country concentration; SUSS Q3-26.
- Applied Materials FQ4-2026 (due mid-Nov 2026) and K&S FQ4-2026 not available or not fetched.

---

## (3) Path forward — transitions, said vs done, funding, timing, verdicts

### Takeaway
The transition that matters for this segment is (3) solder-bump stacking to hybrid bonding. Some players are also exposed to (2) co-packaged optics and (4) panel packaging. Transitions (1), (5) and (6) barely touch these companies, apart from photonics assembly at Besi and ASMPT. Besi is "coherent": its successor is already shipping in logic and it is funded through an HBM slip. Disco is coherent because it is needed in either era. Camtek is coherent with an unproven HB option. TEL is coherent at group level, with bonding evidence thin. ASMPT and Hanmi are "partly coherent" because their HB successors are at sampling or plan stage, while their bridges last longer than expected.

### Cited Findings

**Besi** — transitions (3), (2), (4); beneficiary of (1) through photonics.
- SAID: HB adopted "in a range of stack heights over the next two years" and DRAM-on-accelerator by end of decade [P, CC].
- DONE: 23 HB customers; >215 systems cumulative demand; YTD-26 HB orders more than doubled vs FY2025; Q3-26 HB and TC Next orders from a leading memory customer [P, CC]; Applied alliance deepened (EPIC partner 1 Oct 2026; stake ~20% from 26 Oct 2026) [P]; reported SK hynix pilot line with Applied [S].
- FUNDED: net cash €246.6m; 9M FCF ~€223.5m [D]; R&D ~€23m per quarter [P]. Profitable through the HBM slip (Q3 net margin 37.8%) [P].
- TIMING: logic/CPO HB is now; HBM HB at HBM5 (~2029–30) per SK hynix and Counterpoint (§5).
- WHAT MUST GO RIGHT: memory makers adopt D2W HB from open-market suppliers rather than captive ones (Semes for Samsung); Besi keeps its accuracy/throughput lead over ASMPT gen-2, Hanwha, Hanmi and LG; China demand holds.
- Suggested verdict: **COHERENT** — the successor product ships in volume today (logic) and the company is funded through a 1–2 year slip in HBM.

**Disco** — transition (3) (neutral to positive: thinner dies and cleaner singulation); (4) panel/glass relevance not verified.
- DONE: record shipments on HBM and advanced logic; consumables tied to utilisation [P].
- FUNDED: debt-free, cash and deposits ¥342.4bn [P].
- Suggested verdict: **COHERENT** — not dependent on which bonding method wins. Caveat: its HB-specific process role (grinding/polishing for bond-ready surfaces, plasma or laser dicing) was not verified in this session.

**Tokyo Electron** — transition (3) (W2W/D2W bonding; details UNVERIFIED).
- SAID/DONE: no bonding-specific statements or figures found. Group R&D ¥335bn and capex ¥190bn planned [S].
- Suggested verdict: **COHERENT at group level; bonding path NOT ASSESSABLE** on the evidence gathered.

**Camtek** — transitions (3) (HB inspection) and possibly (4) (not verified).
- SAID: HB inspection meaningful from 2028+; AI software from 2027; US$1.2bn revenue target [S, CC].
- DONE: AP-heavy order book above US$800m; installed base ~4,000 [S, CC]; strong cash position [P].
- FUNDED: yes (net cash ~US$388m [D]).
- Suggested verdict: **COHERENT**, with the HB "judge" role unproven. What must go right: winning HB defect/void/Cu-recess inspection against KLA and Onto (Onto has a Samsung inspection JDP [S]).

**ASMPT** — transitions (3), (2) (CPO portfolio [CC]), (4) (chip-on-panel tool shipped for qualification [P via wire]), (1) (photonics tools for 800G/1.6T modules [S]).
- SAID: 2nd-gen HB "continued to gain traction", collaboration with logic and memory at "sampling stage" [CC].
- DONE: HBM4 TC tools in use at SK hynix [S]; >50 C2S TCB tools ordered by OSATs [CC]; NEXX sold; SMT review since Jan 2026 [S].
- FUNDED: net cash HK$3.63bn (Jun 2026) [P via wire].
- Suggested verdict: **PARTLY COHERENT** — the bridge is strong and diversified, but the HB successor is at sampling only, and memory TC orders are being deferred.

**Hanmi** — transition (3) (existential); (4) partly (FC Bonder 75 for large interposers, 2.5D equipment).
- SAID: Wide TC Bonder by end-2026; HB plant by end-2026; HB for HBM6 by end-2027 [CC].
- DONE: 2026 HBM4 orders (KRW 9.6bn Jan; KRW 44.2bn Jun) [S]; 2.5D/FC entry at a Taiwanese foundry (Sep 2026) [S]; Hanmi USA (Oct 2026) [S]. Plant completion status and any HB customer evaluation: NOT FOUND.
- FUNDED: 50% operating margins [S]; balance sheet not verified.
- TIMING: if HB in HBM arrives at HBM5 (~2029–30), an HB product by end-2027 is in time on paper. But rivals (Besi/Applied, Hanwha, Semes, ASMPT) are already in evaluation or pilot stages [S].
- Suggested verdict: **PARTLY COHERENT** — the bridge extension is credible and funded, and the company benefits from slips, but the successor is unproven.

**SUSS** — transitions (3) (temporary bonding for TSV wafers now; W2W HB UNVERIFIED) and (4) (panel scanner shipped to Taiwan).
- Suggested verdict: **PARTLY COHERENT** — record orders, but falling H1 revenue and single-digit EBIT margins limit funding headroom.

### Inferences
- Bridge-side companies (Hanmi, ASMPT's HBM TCB, K&S fluxless) gain from every slip, but face lumpy orders (memory makers deferring purchases). Successor-side companies (Besi, Applied) are funded through the slip by logic, CPO and edge-AI HB demand.

### Gaps
- No evidence found on Hanmi's HB customer evaluations or plant completion; TEL bonding roadmap; EVG D2W progress; Disco HB-specific tools; Camtek panel inspection.

---

## (4) Suggested ordering of key companies by quality alone (independent of price and size)

### Takeaway
1. **Disco** — owns a tool-agnostic physical/process constraint; utilisation-linked consumables; 45.4% operating margin; debt-free; rising customer advances.
2. **Besi** ≈ **Tokyo Electron (group)** — TIE I cannot separate. Besi has higher margins (45.8% operating), a successor-technology lead and Applied's endorsement, but is smaller, lumpier and ~40% China. TEL is broader, service-backed (~21%) and guides WFE growth, but runs ~31.6% operating margin, is 36% China, and its bonding position is unverified.
3. **Camtek** — judge-like position with one-year visibility and a net-cash balance sheet; HB judge role still ahead; ~29.5% non-GAAP operating margin.
4. **ASMPT** ≈ **Hanmi** — close; ordering is tentative. ASMPT is more diversified and has a successor at sampling, but adjusted GM is ~41–42% and the SMT review is unresolved. Hanmi earns 50% operating margins but on a BRIDGE product, with concentrated customers, disputes and an unproven successor. ASMPT is placed slightly ahead on resilience.
5. **SUSS** — record orders but weak current revenue and margins.
Not ranked (evidence too thin): EV Group, Applied Materials (bonding portion), K&S, Semes, Hanwha Semitech, Shibaura, Toray Engineering, Yamaha Robotics, all Chinese and Taiwanese names, and KLA/Onto/Nova/Park/Lasertec.

### Cited Findings
- Supporting figures are in §2: Besi Q3-26 ([PDF](https://www.besi.com/fileadmin/user_upload/PR_Q3-2026.pdf)), Disco H1 ([Tanshin](https://www.disco.co.jp/jp/ir/library/doc/fr/fr20261022.pdf)), Camtek ([6-K](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326005000/zk2636329.htm)), TEL ([TheOutpost](https://theoutpost.ai/news-story/tokyo-electron-q2-profit-jumps-27-as-ai-demand-for-semiconductor-equipment-accelerates-32910/)), ASMPT ([interim](https://news.marketersmedia.com/asmpt-announces-2026-interim-results-multiple-advanced-packaging-solutions-drive-strong-performance/89199421); [Dr. Web](https://www.drweb.de/asmpt-quartalszahlen-chipsparte-hbm/)), Hanmi ([Money Today](https://www.mt.co.kr/en/industry/2026/10/30/2026103010252581828)).

### Inferences
- Ordering weights (a) position and (c) recurrence as heavily as (d) margins, per the framework.

### Gaps
- Without customer-concentration data for Besi, Hanmi and Disco, the Besi/TEL and ASMPT/Hanmi ties cannot be broken.

---

## (5) Check of background priors (and leads)

### Takeaway
- Prior 1 (HB in HBM slipped to 16-high HBM4E at the earliest) is **UPDATED: it slipped further**. SK hynix said at Hot Chips (23 Aug 2026) that HB won't meet HBM4E needs, putting it at HBM5 at the earliest (~2029–30). Samsung's 16-high HBM4E remains possible but unconfirmed.
- Prior 2 (bridges last longer than roadmaps) is **CONFIRMED in direction**, with share loss now unlikely before ~2029.
- Prior 3 (packaging a binding constraint in 2028–30) is **NOT TESTABLE yet**, though consistent with 2026–27 tool lead times. Current evidence says the binding constraint in 2026 is memory supply itself.

### Cited Findings

**Prior 1 — "Direct Cu-Cu bonding for HBM slipped to 16-layer HBM4E at the earliest"** → UPDATED (slipped further for SK hynix; open for Samsung)
- Hot Chips 2026 (23 Aug 2026): SK hynix VP Jaesik Lee said HB "will not meet HBM4E requirements", so the transition comes "with HBM5 at the earliest". HB is being developed for 20+-high stacks; 12-high is in mass production and 16-high HBM4 is in customer qualification — [36Kr EN, 25 Aug 2026](https://eu.36kr.com/en/p/3954225477991553); [Bits&Chips, 26 Aug 2026](https://bits-chips.com/article/besi-faces-longer-wait-as-sk-hynix-pushes-hybrid-bonding-to-hbm5/) [S]
- SK hynix will not adopt HB below "at least 90 percent" yield. Its America senior director (SEMI, 9 Sep 2026) cited "a yield of 90 to 98 percent" and "a lifespan of three to five years" as non-negotiable. The industry now expects HB at HBM4E 16-high or HBM5 20-high — [Herald Business, 20 Sep 2026](https://biz.heraldcorp.com/article/10878775) [S]
- SK hynix keeps MR-MUF through HBM4 and HBM4E 16-high; fluxless evaluations failed (Jan 2026) — [TrendForce, 13 Jan 2026](https://www.trendforce.com/news/2026/01/13/news-sk-hynix-may-stick-with-mr-muf-for-hbm4-16-high-despite-asmpt-tc-bonder-orders/) [S]
- Samsung and SK hynix "reconsidering" the HB timeline; "16-high HBM4E … as the earliest likely adoption point"; 12-high HBM4E expected to be mainstream; 16-high customer discussions (incl. NVIDIA) "limited"; thermal alternatives (Samsung HPB, SK hynix iHBM) tested for HBM5 — [TrendForce, 7 Jul 2026](https://www.trendforce.com/news/2026/07/07/news-samsung-sk-hynix-reportedly-reconsider-hybrid-bonding-timeline-16-high-hbm4e-may-be-earliest-adoption/) [S]
- Samsung showed HB at NVIDIA GTC 2026, claiming >20% better thermal resistance than TC and support for stacks above 16-high — [TrendForce, 1 Apr 2026](https://www.trendforce.com/news/2026/04/01/news-jedec-reportedly-plans-to-relax-hbm-height-specs-to-900%C2%B5m-potentially-slowing-hybrid-bonding-adoption/) [S, CC]. Samsung had publicly committed to HB for HBM4 in May 2025 — [36Kr EN](https://eu.36kr.com/en/p/3954225477991553) [S]
- NVIDIA reportedly weighing HBM4 8/12-high and HBM4E 8-high for Rubin Ultra (H2-2027) because of HBM4E 12-high supply shortage — [Herald Business citing TrendForce, 20 Sep 2026](https://biz.heraldcorp.com/article/10878775) [S]
- SK hynix HBM5 expected ~2029–30, "the real turning point" for HB (Counterpoint) — [Asia Economy, 6 Apr 2026](https://view.asiae.co.kr/en/article/2026040613193475063) [A]. HBM5 expected to need HB, with availability at end of decade — [SemiEngineering, 13 Jan 2026](https://semiengineering.com/hbm4-sticks-with-microbumps-postponing-hybrid-bonding/) [S]
- Counterpoint from the equipment side: Besi says memory shortages "extended the use of lower stack heights … beyond prior expectations", yet expects HB "in a range of stack heights over the next two years" [P, CC] ([PDF](https://www.besi.com/fileadmin/user_upload/PR_Q3-2026.pdf)).
- Slip history: Oct-2025 forecasts had HB reaching ~50% of HBM production by 2028 in the HBM4E era (News1 via [TrendForce, 7 Oct 2025](https://www.trendforce.com/news/2025/10/07/news-hybrid-bonder-equipment-market-reportedly-near-2b-by-2028-as-korean-makers-race-to-next-gen-hbm-tools/)) — now contradicted.

**Prior 2 — "Bridging hardware (incl. solder-bump stacking tools) loses share 2028–2030; bridges last longer than roadmaps say"** → CONFIRMED in direction; timing likely back-loaded to ~2029–30+
- JEDEC raised the HBM4 limit from 720 µm to 775 µm, which removed the need for HB in HBM4 — [SemiEngineering, 13 Jan 2026](https://semiengineering.com/hbm4-sticks-with-microbumps-postponing-hybrid-bonding/) [S]. A further rise to ~900 µm is reported for HBM4E onward — [TrendForce citing Chosun Ilbo, 1 Apr 2026](https://www.trendforce.com/news/2026/04/01/news-jedec-reportedly-plans-to-relax-hbm-height-specs-to-900%C2%B5m-potentially-slowing-hybrid-bonding-adoption/); [3DNews citing Business Korea, 3 Apr 2026](https://3dnews.ru/1139386/jedec-razreshit-pamyati-hbm4e-podrasti-radi-uproshcheniya-proizvodstva-i-snigeniya-tseni). HBM5 could go from ~900 µm to ~1,000 µm — [TrendForce, 7 Jul 2026](https://www.trendforce.com/news/2026/07/07/news-samsung-sk-hynix-reportedly-reconsider-hybrid-bonding-timeline-16-high-hbm4e-may-be-earliest-adoption/) [S]. No official JEDEC publication found.
- Demand is rising for Hanmi's Wide TC Bonder (larger die area instead of HB) — [TrendForce, 7 Jul 2026](https://www.trendforce.com/news/2026/07/07/news-samsung-sk-hynix-reportedly-reconsider-hybrid-bonding-timeline-16-high-hbm4e-may-be-earliest-adoption/) [S]
- Caveat: a longer bridge life does not mean smooth bridge orders — memory makers are "delaying larger bonding-tool purchases" (ASMPT Q3-26, [Dr. Web](https://www.drweb.de/asmpt-quartalszahlen-chipsparte-hbm/)) [S].

**Prior 3 — "Packaging is one of the binding constraints on AI computing in 2028–2030"** → NOT TESTABLE for 2028–30; near-term evidence mixed
- Tightness now: Camtek customers securing slots through 2027 ([MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-camtek-q3-earnings-call-highlights-2026-11-04/)) [S]; Besi customers aligning deliveries with H1-27 capacity ([PDF](https://www.besi.com/fileadmin/user_upload/PR_Q3-2026.pdf)) [P]; SUSS ~€220m backlog for 2027 ([Placera](https://www.placera.se/pressmeddelanden/suss-microtec-order-book-reaches-record-of-473-7-million-providing-strong-visibility-for-2027-20260806)) [P]; Disco customer advances +59% in six months [D from P]; ASMPT longer lead times ([Dr. Web](https://www.drweb.de/asmpt-quartalszahlen-chipsparte-hbm/)) [S].
- Contrary or nuancing evidence for 2026: the visible binding constraint is memory supply — "severe memory shortages" (Besi [P]); NVIDIA reportedly lowering stack heights for supply reasons [S]; Camtek's own tool output constrained by memory/CPU component shortages [S].

**Leads to verify (from earlier reporting)**
- Applied ~9% Besi stake (Apr 2025) and integrated HB system (2025): the ~9% stake is CONFIRMED by Oct-2026 coverage ("from about 9%") — [RTTNews, 26 Oct 2026](https://www.rttnews.com/3703117/applied-materials-to-increase-stake-in-be-semiconductor-industries-to-about-20.aspx) [S]. The April-2025 date was NOT re-confirmed. The "Kinex" D2W HB platform co-developed with Besi is referenced in [Bits&Chips, 26 Aug 2026](https://bits-chips.com/article/besi-faces-longer-wait-as-sk-hynix-pushes-hybrid-bonding-to-hbm5/); its launch date was NOT re-confirmed. NEW: stake rising to ~20% (26 Oct 2026) [P].
- Hanmi–SK hynix dispute (2025) leading to dual-sourcing from Hanwha and ASMPT: CONFIRMED (trade press). Hanmi recalled ~60 engineers in Apr-2025; ASMPT supplied ~half of HBM4 TC sets; Hanwha contracted but its tools were not in HBM4 use (Dec 2025). Hanmi regained orders in Jan and Jun 2026 — [TrendForce/The Elec, 12 Dec 2025](https://www.trendforce.com/news/2025/12/12/news-sk-hynix-reportedly-places-hbm4-tc-bonder-order-with-asmpt-as-hanmi-hanwha-patent-clash-heats-up/); [TrendForce, 9 Jun 2026](https://www.trendforce.com/news/2026/06/09/news-sk-hynix-reportedly-places-44-2bn-won-tc-bonder-order-with-hanmi-accelerating-hbm4-ramp-up/) [S]
- Hanmi "wide" TC bonder and HB plan: CONFIRMED as company plans [CC] — [MTN, 13 Feb 2026](https://news.mtn.co.kr/news-detail/2026021317395078451); [Asia Economy, 22 Dec 2025](https://view.asiae.co.kr/en/article/2025122209224722092)
- JEDEC HBM4 relaxed to 775 µm: CONFIRMED [S]. Further relaxation to ~900 µm (HBM4E) and ~1,000 µm (HBM5) is REPORTED/UNDER DISCUSSION, not confirmed by JEDEC.
- ASMPT reviewing its SMT business: CONFIRMED — strategic review since Jan 2026 (sale, JV, spin-off/IPO, or retain); no outcome by the Q3-26 release — [Dr. Web, 28 Oct 2026](https://www.drweb.de/asmpt-quartalszahlen-chipsparte-hbm/) [S]

### Inferences
- For SK hynix, "16-high HBM4E at the earliest" should be replaced with "HBM5 (20-high, ~2029–30) at the earliest". For Samsung, 16-high HBM4E (~2027–28) remains a live but unconfirmed possibility. Besi's memory orders are development-stage (its own wording: "development of current and next generation HBM device structures").

### Gaps
- No official JEDEC document; no Micron HB timeline; no CXMT HB plans.

---

## (6) Open question — which successor ships in volume first; who captures the value

### Takeaway
D2W hybrid bonding is already in volume in logic chiplets, and Besi reports expansion into CPO and edge-AI devices. W2W HB has long been in volume in image sensors and NAND (background, unverified here). HBM is the last major application, at HBM5. Within HBM, the first "successors" to ship are bridge extensions (wide-die TC, fluxless TC at K&S if qualified), not HB. On value capture, the evidence points to a specialist-plus-giant alliance (Besi with Applied) in D2W logic, and captive suppliers having structural access in HBM (Semes at Samsung). Hanmi is late.

### Cited Findings
- **Volume today (logic):** "more logic chiplet programs entered production"; Q3-26 HB orders from logic, CPO and memory; "ongoing hybrid bonding capacity expansion planned by the leading industry players for logic, CPO and edge AI devices" — [Besi Q3-26](https://www.besi.com/fileadmin/user_upload/PR_Q3-2026.pdf) [P, CC]. HB "currently used mainly in logic" — [Bits&Chips, 22 Oct 2026](https://bits-chips.com/article/besi-sees-increasing-momentum-for-hybrid-bonding/) [S]. TSMC's HB pitch is at 6 µm (headline only; body not retrieved) — [Tom's Hardware](https://tomshardware.com/tech-industry/semiconductors/hybrid-bonding-roadmap-examined) [S].
- **Installed base:** Besi cumulative unit demand >215 systems (all applications) [P, CC]. No other supplier's installed base was found.
- **Order trends:** Besi YTD-26 HB orders >2x FY2025 [P]; ASMPT HB at sampling [CC]; Hanwha gen-2 HB to customers for testing H1-2026 [S]; Semes and Hanwha going straight to HB [S]; LG targeting 2028 [S]; Hanmi targeting end-2027 [CC].
- **Integrated giant:** Applied raising its stake to ~20% and co-developing integrated systems; SK hynix pilot line reportedly Applied+Besi; Applied VP: HB timing "is for the customer to answer" — [Besi, 27 Oct 2026](https://www.besi.com/investor-relations/press-releases/details/applied-materials-to-increase-its-strategic-investment-in-be-semiconductor-industries/) [P]; [Bits&Chips](https://bits-chips.com/article/besi-faces-longer-wait-as-sk-hynix-pushes-hybrid-bonding-to-hbm5/); [Herald](https://biz.heraldcorp.com/article/10878775) [S]
- **Captive:** Samsung relies heavily on Semes for TCB, making it "unlikely Samsung will adopt Hanmi's equipment, unless Hanmi's equipment strongly outperforms" (analyst) — [Tech Investments](https://www.techinvestments.io/p/hbmdie-bonding-semicap-outlook) [A]
- **Market-size reference points (all forecasts):** HB market ~KRW 2.8tn (~US$1.99bn) by 2028 if HB reaches ~50% of HBM (News1 Korea, Oct 2025 — now stale given the slips); ASMPT TCB addressable market >US$1.6bn by 2028 [CC]; hybrid bonder price ~KRW 4bn, more than twice a TC bonder [S] — [TrendForce, 7 Oct 2025](https://www.trendforce.com/news/2025/10/07/news-hybrid-bonder-equipment-market-reportedly-near-2b-by-2028-as-korean-makers-race-to-next-gen-hbm-tools/)
- **Inspection as judge of HB:** Camtek sees HB inspection as meaningful only from 2028 [S]; Onto has a Samsung inspection JDP; Samsung is working with multiple vendors on non-destructive defect detection (The Elec via TrendForce) [S].

### Inferences
- First volume successor beyond what already ships: CPO and edge-AI D2W HB (2026–27), then HBM HB at Samsung (possible 16-high HBM4E) or HBM5 (~2029–30).
- Value capture: in logic and CPO, the Besi–Applied alliance looks best placed. Applied's ~20% stake means the integrated giant captures part of the specialist's economics without owning it. In HBM, captive suppliers (Semes, possibly Hanwha at SK hynix) have qualification-access advantages, which caps the open-market share specialists can win at the last and largest application. Inspection and metrology vendors gain on either route, because HB raises the number of quality gates (Cu recess, particles, voids, overlay).

### Gaps
- No third-party HB share or installed-base data by supplier (D2W: Besi, ASMPT, TEL, Shibaura, Hanmi, Semes; W2W: EVG, TEL, SUSS). Intel Foveros Direct, AMD and image-sensor/NAND volume status not re-verified in this session.

---

## (7) What I could not verify

### Takeaway
The biggest gaps are China (domestic HB, thinning and dicing entrants, and CXMT bonder sourcing), the actual export-control texts touching packaging tools, customer concentration for Besi, Hanmi and Disco, and private or captive players' (EVG, Semes, Hanwha, LG) volumes. Much of this is because the shared search budget ran out mid-session.

### Cited Findings
- (none; this section lists gaps)

### Inferences
- Treat all map rows marked UNVERIFIED as leads, not facts.

### Gaps
- **China:** Piotech, U-Precision, iSABers, Maxwell, Kingsemi, Hwatsing, GL Tech, Skyverse — products, customers (YMTC, CXMT), revenues: not verified; cninfo/SSE/SZSE not reached. CXMT HBM bonder suppliers unknown. The 3DNews report notes looser JEDEC specs could ease Chinese entry ([3DNews, 3 Apr 2026](https://3dnews.ru/1139386/jedec-razreshit-pamyati-hbm4e-podrasti-radi-uproshcheniya-proizvodstva-i-snigeniya-tseni)) — unquantified.
- **Export controls and tariffs:** I could not retrieve current US (BIS), Dutch, Japanese (METI) or Korean rule texts covering bonding, dicing or packaging inspection tools for China. No 2026 source confirmed whether HB or TC bonders are controlled. The indirect evidence is that Besi (China 34–46% of quarterly revenue in 2026), TEL (China 36.4%), ASMPT and Camtek all report strong China demand. Besi's release carries generic tariff risk language. Applied's stake increase is subject to US antitrust review; whether China's SAMR must review it was not confirmed (the ctol.digital page returned 403).
- **Taiwan:** GPM, Scientech, GPTC, All Ring, C Sun — MOPS not reached.
- **India:** no player found; not re-checked on NSE/BSE.
- **EV Group, Shibaura, Toray Engineering, Yamaha Robotics, Tokyo Seimitsu, EO Technics, Park Systems, Nova, KLA, Onto (beyond the JDP mention), Lasertec, PVA TePla/Nordson (acoustic), Comet (X-ray):** no 2026 data gathered.
- **Kulicke & Soffa:** FQ3-26 statements (revenue +36% q/q; Advanced Solutions record; >US$100m FY2026 target) were seen only in search excerpts; FQ4-26 not yet published or not found.
- **Applied Materials:** FQ4-2026 (due ~mid-Nov 2026) not available; its own press release returned 403.
- **Besi:** top-customer / top-5 share, service share, manufacturing countries (annual report 2025 not fetched); reason for "strategic consulting costs" in Q4-26 opex.
- **Hanmi:** 9M-26 totals, net cash, FCF, customer concentration (DART not reached); HB plant completion; any HB customer evaluation; the meaning of the "US$247.7m cumulative revenue to Q3-2025" figure (TC-only or total).
- **Disco:** product split (equipment, consumables, service) and regional split; third-party share in grinders and dicers.
- **TEL:** primary release; bonding-specific revenue, products and customers.
- **Hanwha Semitech:** the HB-cluster-at-SK-hynix report (single source, undated); parent listing.
- **JEDEC:** no official HBM4E/HBM5 height publication found.
- **Micron:** HB timeline; current HBM4 bonder split.
- **2026 TC-bonder market shares** by supplier and by customer (TechInsights or Yole 2026 editions).

---

## (8) Sources (with publication dates; period covered in brackets)

### Takeaway
Primary sources: Besi (22 and 27 Oct 2026), Disco (22 Oct 2026), Camtek (4 Nov 2026). Most memory-timing evidence is Korean trade press relayed by TrendForce, Bits&Chips, 36Kr and Herald (Jan–Oct 2026).

### Cited Findings
**Primary**
- Besi, Q3-2026 results PDF, 22 Oct 2026 [Q3 and 9M to 30 Sep 2026] — https://www.besi.com/fileadmin/user_upload/PR_Q3-2026.pdf
- Besi, Q3-2026 results release page, 22 Oct 2026 — https://www.besi.com/investor-relations/press-releases/details/be-semiconductor-industries-nv-announces-q3-2026-results/
- Besi, "Applied Materials to Increase its Strategic Investment in Besi", 27 Oct 2026 — https://www.besi.com/investor-relations/press-releases/details/applied-materials-to-increase-its-strategic-investment-in-be-semiconductor-industries/
- Besi press-release index (accessed 12 Nov 2026) — https://www.besi.com/investor-relations/press-releases/
- Besi Q2-26 release (wire copy), Jul 2026 [Q2 to 30 Jun 2026] — https://www.stocktitan.net/news/BESIY/be-semiconductor-industries-n-v-announces-q2-26-and-h1-26-v0syj60xvlwf.html
- Disco, Tanshin for H1 of FY ending Mar 2027, 22 Oct 2026 [Apr–Sep 2026] — https://www.disco.co.jp/jp/ir/library/doc/fr/fr20261022.pdf
- Camtek, Form 6-K Q3-2026, 4 Nov 2026 [Q3 and 9M to 30 Sep 2026] — https://www.sec.gov/Archives/edgar/data/0001109138/000117891326005000/zk2636329.htm
- ASMPT, 2026 interim results release (wire copy), 1 Aug 2026 [H1 to 30 Jun 2026] — https://news.marketersmedia.com/asmpt-announces-2026-interim-results-multiple-advanced-packaging-solutions-drive-strong-performance/89199421
- ASMPT, "Secures Significant Wins" release (2026; date not captured) — https://www.asmpt.com/en/investor-relations/news-events/asmpt-secures-significant-wins/
- SUSS MicroTec, H1-2026 release (wire copy), 6 Aug 2026 [H1 to 30 Jun 2026] — https://www.placera.se/pressmeddelanden/suss-microtec-order-book-reaches-record-of-473-7-million-providing-strong-visibility-for-2027-20260806
- SUSS MicroTec, Q1-2026 statement (aggregator), May 2026 — https://financialreports.eu/filings/suss-microtec-se/quarterly-report/2026/43163299/
- SUSS MicroTec, Q3-2025 corporate news, 2025 — https://www.suss.com/news/corporate-news/2025/suss-erwartet-deutliche-belebung-beim-auftragseingang-im-vierten-quartal

**Secondary (trade press / aggregators / call summaries)**
- Bits&Chips, "Besi faces longer wait as SK Hynix pushes hybrid bonding to HBM5", 26 Aug 2026 — https://bits-chips.com/article/besi-faces-longer-wait-as-sk-hynix-pushes-hybrid-bonding-to-hbm5/
- Bits&Chips, "Besi sees increasing momentum for hybrid bonding", 22 Oct 2026 — https://bits-chips.com/article/besi-sees-increasing-momentum-for-hybrid-bonding/
- CXO Digital Pulse, Besi Q3 orders, 23 Oct 2026 — https://www.cxodigitalpulse.com/?p=63987
- RTTNews, Applied to increase Besi stake to ~20%, 26 Oct 2026 — https://www.rttnews.com/3703117/applied-materials-to-increase-stake-in-be-semiconductor-industries-to-about-20.aspx
- TechNews (Taiwan), Applied raises Besi stake to ~20%, 28 Oct 2026 — https://finance.technews.tw/2026/10/28/applied-materials-plans-to-raise-stake-in-besi-to-20/
- 36Kr EN (Semiconductor Industry Observer), SK hynix at Hot Chips 2026, 25 Aug 2026 — https://eu.36kr.com/en/p/3954225477991553
- Herald Business, SK hynix 90% yield threshold, 20 Sep 2026 — https://biz.heraldcorp.com/article/10878775
- TrendForce, Samsung/SK hynix reconsider HB timeline, 7 Jul 2026 — https://www.trendforce.com/news/2026/07/07/news-samsung-sk-hynix-reportedly-reconsider-hybrid-bonding-timeline-16-high-hbm4e-may-be-earliest-adoption/
- TrendForce, JEDEC reportedly plans ~900 µm, 1 Apr 2026 — https://www.trendforce.com/news/2026/04/01/news-jedec-reportedly-plans-to-relax-hbm-height-specs-to-900%C2%B5m-potentially-slowing-hybrid-bonding-adoption/
- TrendForce, industry weighs 825–900 µm, 6 Mar 2026 (title only) — https://trendforce.com/news/2026/03/06/news-industry-weigh-825-900-%CE%BCm-hbm-thickness-for-20-high-stacks-potentially-slowing-hybrid-bonding
- 3DNews, JEDEC to let HBM4E grow (citing Business Korea), 3 Apr 2026 — https://3dnews.ru/1139386/jedec-razreshit-pamyati-hbm4e-podrasti-radi-uproshcheniya-proizvodstva-i-snigeniya-tseni
- Semiconductor Engineering, "HBM4 Sticks With Microbumps, Postponing Hybrid Bonding", 13 Jan 2026 — https://semiengineering.com/hbm4-sticks-with-microbumps-postponing-hybrid-bonding/
- TrendForce, SK hynix may stick with MR-MUF for HBM4 16-high (citing DealSite), 13 Jan 2026 — https://www.trendforce.com/news/2026/01/13/news-sk-hynix-may-stick-with-mr-muf-for-hbm4-16-high-despite-asmpt-tc-bonder-orders/
- TrendForce, SK hynix HBM4 TC bonder order with ASMPT; Hanmi–Hanwha clash (citing The Elec), 12 Dec 2025 — https://www.trendforce.com/news/2025/12/12/news-sk-hynix-reportedly-places-hbm4-tc-bonder-order-with-asmpt-as-hanmi-hanwha-patent-clash-heats-up/
- TrendForce, SK hynix KRW 44.2bn Hanmi order, 9 Jun 2026 — https://www.trendforce.com/news/2026/06/09/news-sk-hynix-reportedly-places-44-2bn-won-tc-bonder-order-with-hanmi-accelerating-hbm4-ramp-up/
- Korea Times, SK hynix orders HBM4 equipment, 8 Jun 2026 — https://www.koreatimes.co.kr/business/tech-science/20260608/sk-hynix-orders-new-equipment-worth-287-mil-for-next-gen-hbm4
- TrendForce, hybrid bonder market near US$2bn by 2028 (citing News1, Data News, SeDaily), 7 Oct 2025 — https://www.trendforce.com/news/2025/10/07/news-hybrid-bonder-equipment-market-reportedly-near-2b-by-2028-as-korean-makers-race-to-next-gen-hbm-tools/
- Asia Economy, Hanmi TechInsights share / HB plant, 22 Dec 2025 — https://view.asiae.co.kr/en/article/2025122209224722092
- Asia Economy, Counterpoint on SK hynix HBM5 2029, 6 Apr 2026 — https://view.asiae.co.kr/en/article/2026040613193475063
- Asia Economy, TC bonder companies clash, Jul 2024 — https://view.asiae.co.kr/en/article/2024071607095917092
- Asia Economy, Semes next-gen TC bonder, 3 Jun 2024 — https://www.asiae.co.kr/en/article/2024060313461781042
- Asia Economy, Hanwha hybrid bonder early next year, 10 Sep 2025 — https://www.asiae.co.kr/en/article/2025091014483070591
- MTN (Money Today Broadcasting), Hanmi wide TC bonder vs Semes/Hanwha hybrid, 13 Feb 2026 — https://news.mtn.co.kr/news-detail/2026021317395078451
- Money Today, Hanmi Q3-2026 results, 30 Oct 2026 — https://www.mt.co.kr/en/industry/2026/10/30/2026103010252581828
- Herald, Hanmi Q3-2026 results, 4 Nov 2026 — https://mbiz.heraldcorp.com/article/10925615
- Dr. Web (Germany), ASMPT Q3-2026, 28 Oct 2026 — https://www.drweb.de/asmpt-quartalszahlen-chipsparte-hbm/
- 10jqka (Tonghuashun), ASMPT Q3-2026, 28 Oct 2026 — https://stock.10jqka.com.cn/20261028/c681160656.shtml
- FourWeekMBA, ASMPT record bookings, Oct 2026 — https://fourweekmba.com/ai-asmpt-bookings-hit-a-record-hk8-85b-on-ai-packaging-orders/
- TheOutpost (Investing.com), Tokyo Electron Q2 FY2027, 30 Oct 2026 — https://theoutpost.ai/news-story/tokyo-electron-q2-profit-jumps-27-as-ai-demand-for-semiconductor-equipment-accelerates-32910/
- Gyokai Digest (TDnet relay), Disco preliminary Jul–Sep 2026, 6 Oct 2026 — https://www.gyokaidigest.com/en/disclosures/6146-tdnet-20261006-140120261006546587
- TechNews (Taiwan), Disco shipments record, 24 Jul 2026 — https://finance.technews.tw/2026/07/24/disco-shipments-beat-forecasts-hit-record-high/
- MarketBeat, Camtek Q3-2026 call highlights, 4 Nov 2026 — https://www.marketbeat.com/instant-alerts/transcript-camtek-q3-earnings-call-highlights-2026-11-04/
- MarketBeat, K&S FQ1-2026 call highlights, 5 Feb 2026 (search excerpt only) — https://www.marketbeat.com/instant-alerts/kulicke-and-soffa-industries-q1-earnings-call-highlights-2026-02-05/?.tsrc=rss
- MarketBeat, K&S FQ2-2026 call highlights, 8 May 2026 (search excerpt only) — https://www.marketbeat.com/instant-alerts/kulicke-and-soffa-industries-q2-earnings-call-highlights-2026-05-08/
- Alpha Spread, Besi Q1-2026 call, Apr 2026 (search excerpt only) — https://www.alphaspread.com/security/aex/besi/investor-relations/earnings-call/q1-2026
- Tech Investments, HBM die-bonding semicap outlook (analyst; date not captured) — https://www.techinvestments.io/p/hbmdie-bonding-semicap-outlook
- Digg aggregation of "[Exclusive] Hanwha Semitech supplies hybrid bonding cluster to SK Hynix" (date not visible) — https://digg.com/tech/vvqd1wro
- Tom's Hardware, "The current state of Hybrid Bonding in 2026" (headline only retrieved) — https://tomshardware.com/tech-industry/semiconductors/hybrid-bonding-roadmap-examined

### Inferences
- Source quality: Korean memory-timing evidence comes from multiple independent outlets that agree (ZDNet Korea, The Elec, Newsis, Chosun Ilbo via TrendForce; Bits&Chips; 36Kr; Herald), which raises confidence in the HBM5 slip.

### Gaps
- Several pages returned 403 or paywalls (Applied's own release, ctol.digital, the Bits&Chips full text).
