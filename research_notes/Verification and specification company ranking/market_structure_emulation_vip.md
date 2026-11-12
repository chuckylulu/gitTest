# Chip-verification market structure, emulation and prototyping hardware, verification IP and independent verification/sign-off vendors (position as of 12 November 2026)

Research date: 12 November 2026 (all searches and fetches run on this date, in two passes). FINAL structured version; it merges the first researcher's raw capture with the continuation pass. Nothing sourced in the first pass has been dropped; corrections are marked "CORRECTION".

Tag key: [PRIMARY] filing, official data or original document; [INDEPENDENT] confirmed by an outside party; [COMPANY CLAIM] stated by a company, not confirmed outside; [SECONDARY] press or analyst report only; [UNVERIFIED] could not verify. "My calculation" = arithmetic on cited figures, not a source figure.

Method notes:
- First pass: "the shared web-search budget for this session ran out after my first ~16 searches. Everything after that was gathered by fetching known URLs and listing pages directly (company newsrooms, PR Newswire listings, trade-press pages). I did not route searches through third-party search services."
- Continuation pass: built-in WebSearch worked for about 20 queries, then the shared 200-call budget ran out again. Firecrawl was out of credits. After the limit I ran no searches through other search engines. All later evidence comes from direct fetches of company sites, newsrooms, PDFs and the SEC XBRL API (data.sec.gov). Because of this, coverage of Breker, Ausdia, X-Epic and Corigine, and of 2001–2002 industry data, is thin.
- Cross-references to other researchers' files in the same folder (china.md, synopsys.md, cadence.md, siemens_eda.md, india_and_verification_services.md, specification_requirements_tools.md, ai_native_chip_verification_open_source.md) are labelled "cross-ref". The source URLs are those recorded in those files.

## 1. Market size and shares by segment, 2023–2026

### Takeaway
Third-party industry data (SEMI ESD Alliance EDMD) put electronic-design revenue at about $21.2bn in 2025 (my sum of the quarters, +10.2%) and $11.46bn in H1 2026 (+12.5%). The four-quarter moving average was +11.2% at Q2 2026, led by semiconductor IP (+16.6%) and APAC (+18.3%). No public third-party source sizes verification on its own. Functional verification sits inside "CAE" and physical verification inside "IC physical design & verification". Vendor shares for simulation, emulation and sign-off come only from analyst estimates. The most-cited set (SemiAnalysis) leaves out Siemens in emulation.

### Cited Findings
**ESD Alliance EDMD quarterly data**, $M (from the PR Newswire copies of the SEMI press releases) [PRIMARY]. YoY = year over year.

| Quarter | Release date | Total | YoY | CAE | IC phys. design & verif. | PCB & MCM | SIP | Services | Employment (tracked cos.) |
|---|---|---|---|---|---|---|---|---|---|
| Q1 2023 | (comparative in Q1 2024 release) | 3,951.1 | | | | | | | 57,696 |
| Q2 2023 | (comparative in Q2 2024 release) | 3,962.7 | | | | | | | 59,160 |
| Q3 2023 | (comparative in Q3 2024 release) | 4,702.4 | | | | | | | 59,737 |
| Q4 2023 | (comparative in Q4 2024 release) | 4,440.9 | | | | | | | 60,106 |
| Q1 2024 | 15 Jul 2024 | 4,521.6 | +14.4% | 1,621.1 | 769.6 | 378.9 | 1,578.1 | 173.9 | 61,653 |
| Q2 2024 | 7 Oct 2024 | 4,685.5 | +18.2% | 1,646.4 | 779.3 | 399.2 | 1,680.7 | 179.8 | 63,188 |
| Q3 2024 | 14 Jan 2025 | 5,114.5 | +8.8% | 1,922.2 | 854.4 | 450.8 | 1,686.2 | 200.8 | 62,417 |
| Q4 2024 | 14 Apr 2025 | 4,927.3 (restated to 4,955.2 in Q4 2025 release) | +11% | 1,696.9 | 797.9 | 476.2 | 1,760.7 | 195.6 | 61,827 (restated 62,833) |
| Q1 2025 | 15 Jul 2025 | 5,098.3 | +12.8% | 1,747.6 | 693.5 | 399.8 | 2,044.8 | 212.6 | 64,403 |
| Q2 2025 | 6 Oct 2025 | 5,089.4 | +8.6% | 1,929.0 | 701.9 | 430.5 | 1,826.7 | 201.2 | 72,529 |
| Q3 2025 | 12 Jan 2026 | 5,566.4 | +8.8% | 2,097.8 | 865.4 | 466.2 | 1,915.7 | 221.4 | 73,185 |
| Q4 2025 | 13 Apr 2026 | 5,466.3 | +10.3% | 1,887.4 | 777.2 | 484.6 | 2,083.2 | 233.9 | 71,517 |
| Q1 2026 | 13 Jul 2026 | 5,747.8 | +12.7% | 2,018.4 | 751.3 | 419.2 | 2,332.5 | 226.4 | 72,544 |
| Q2 2026 | 19 Oct 2026 | 5,710.8 | +12.2% | 2,077.6 | 818.3 | 364.2 | 2,199.0 | 251.7 | 71,396 |

Release URLs:
- Q2 2026: https://www.prnewswire.com/news-releases/electronic-system-design-industry-posts-5-7-billion-in-revenue-in-q2-2026--esd-alliance-reports-302912151.html (mirror: https://businessnewsthisweek.com/news/electronic-system-design-industry-posts-57-billion-in-revenue-in-q2-2026-esd-alliance-reports/)
- Q1 2026: https://www.prnewswire.com/news-releases/esd-alliance-reports-electronic-system-design-industry-posts-5-7-billion-in-revenue-in-q1-2026--302822272.html
- Q4 2025: https://www.prnewswire.com/news-releases/esd-alliance-reports-electronic-system-design-industry-posts-5-5-billion-in-revenue-in-q4-2025--302737536.html
- Q3 2025: https://www.prnewswire.com/news-releases/esd-alliance-reports-electronic-system-design-industry-posts-5-6-billion-in-revenue-in-q3-2025--302655485.html
- Q2 2025: https://www.prnewswire.com/news-releases/esd-alliance-reports-electronic-system-design-industry-posts-5-1-billion-in-revenue-in-q2-2025--302575024.html
- Q1 2025: https://www.prnewswire.com/news-releases/esd-alliance-reports-electronic-system-design-industry-posts-5-1-billion-in-revenue-in-q1-2025--302502842.html
- Q4 2024: https://www.prnewswire.com/news-releases/electronic-system-design-industry-posts-4-9-billion-in-revenue-in-q4-2024--esd-alliance-reports-302426889.html
- Q3 2024: https://www.prnewswire.com/news-releases/electronic-system-design-industry-posts-5-1-billion-in-revenue-in-q3-2024--esd-alliance-reports-302348514.html
- Q2 2024: https://www.prnewswire.com/news-releases/electronic-system-design-industry-posts-4-7-billion-in-revenue-in-q2-2024--esd-alliance-reports-302268652.html
- Q1 2024: https://www.prnewswire.com/news-releases/electronic-system-design-industry-posts-4-5-billion-in-revenue-in-q1-2024--esd-alliance-reports-302196526.html

Regions, $M (YoY where stated) [PRIMARY, same releases]:

| Quarter | Americas | EMEA | Japan | APAC |
|---|---|---|---|---|
| Q1 2024 | 1,937.2 | 579.0 | 280.7 | 1,724.7 |
| Q2 2024 | 2,034.9 | 584.6 | 305.4 | 1,760.6 |
| Q3 2024 | 2,325.4 | 645.6 | 298.5 | 1,845.0 |
| Q4 2024 | 2,171.8 | 622.3 | 318.4 | 1,814.8 |
| Q1 2025 | 2,208.3 | 651.5 | 314.2 | 1,924.2 |
| Q2 2025 | 2,282.4 | 650.9 | 277.4 | 1,878.7 |
| Q3 2025 | 2,402.2 (+3.4%) | 675.1 (+4.6%) | 264.0 (−11.5%) | 2,223.0 (+20.5%) |
| Q4 2025 | 2,473.5 (+13.9%) | 683.4 (+9.8%) | 258.5 (−18.8%) | 2,050.8 (+11.3%) |
| Q1 2026 | 2,433.8 (+10.2%) | 766.4 (+17.6%) | 283.1 (−9.9%) | 2,264.4 (+17.7%) |
| Q2 2026 | 2,443.5 (+7.1%) | 665.6 (+2.3%) | 303.1 (+9.3%) | 2,298.7 (+22.4%) |

- Q2 2026 region × category ($M): Americas CAE 921.5 / ICPD&V 339.1 / PCB 139.6 / SIP 881.7 / Services 161.5; EMEA 286.5 / 86.2 / 79.2 / 183.0 / 30.7; Japan 100.0 / 127.0 / 39.7 / 21.9 / 14.5; APAC 769.5 / 266.0 / 105.8 / 1,112.5 / 45.0. SIP split: reporting SIP companies 725.2; non-reporting (estimated: Arm excl. PIPD, CEVA, Rambus) 1,473.9. [PRIMARY] (Q2 2026 release)
- Q2 2026 four-quarter moving averages: total +11.2%; CAE +10.7%; IC physical design & verification +5.4%; PCB & MCM −1.3%; SIP +16.6%; services +15.2%; Americas +8.6%; EMEA +8.6%; Japan −8.2%; APAC +18.3%. Employment 71,396, −1.6% vs 72,529 in Q2 2025. Walden Rhines: "All product categories except Printed Circuit Board and Multi-Chip Module reported gains"; "All geographic regions reported growth in Q2". "Non-reporting SIP companies include ARM Holdings PLC (excl. ARM PIPD), CEVA Inc., and Rambus Inc."; "Beginning with Q4 2016, ARM PIPD exclusion is estimated." **The release does not break out China**, only APAC. [PRIMARY] (Q2 2026 release)
- My calculation from the as-reported quarters: 2023 total 17,057.1; 2024 19,276.8 using the restated Q4 2024 (+13.0%); 2025 21,220.4 (+10.1% vs restated 2024). 2025 by category: CAE 7,661.8 (+11.3%, 36.1% of total); ICPD&V 3,038.0 (−5.1%, 14.3%); PCB & MCM 1,781.1 (+4.5%, 8.4%); SIP 7,870.4 (+17.4%, 37.1%); services 869.1 (+15.9%, 4.1%). H1 2026 vs H1 2025: total +12.5%; CAE +11.4%; ICPD&V +12.5%; PCB −5.6%; SIP +17.0%; services +15.5%. 2025 by region: Americas 9,366.4 (+10.6%, 44.1%); APAC 8,076.7 (+13.0%, 38.1%); EMEA 2,660.9 (+9.4%, 12.5%); Japan 1,114.1 (−7.4%, 5.3%). Later releases restate some quarters, so these sums are approximate.
- China, from company disclosure (no third-party China series found): Cadence China revenue $680.0M in 2025 (13% of total, +19%), $573.1M in 2024 (12%) and $679.5M in 2023, a fall of about 15.7% in 2024 (my calculation). Cadence 2025 other regions: US $2,311.0M (+7%), Other Asia $1,005.2M (+17%), EMEA $790.6M (+13%), Japan $341.7M (+31%). [PRIMARY] Cadence FY2025 10-K https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf . Synopsys China −18% in FY2025 per its Q4 FY2025 call https://www.fool.com/earnings/call-transcripts/2025/12/10/synopsys-snps-q4-2025-earnings-call-transcript/ ; cross-ref synopsys.md: −22% excluding Ansys per the FY2025 10-K https://www.sec.gov/Archives/edgar/data/883241/000088324125000028/snps-20251031.htm .

**Third-party share estimates**
- SemiAnalysis "EDA Market Primer" (21 May 2026; paid; authors Kundojjala, Patel, Wong). Estimates: emulation "$1.5B+ market"; Palladium 55–60%, ZeBu 35–40%; VCS 45–50%, Xcelium 40–45%; PrimeTime 90%+; Calibre 85%+. Re-check on 12 Nov 2026: the emulation shares give no base and **do not mention Siemens Veloce**, so they read as a two-vendor split, not total-market shares. Questa is not mentioned for simulation. One chart is headed "Advanced Nodes, 7nm and Below". [SECONDARY; estimates] https://newsletter.semianalysis.com/p/eda-market-primer
- TrendForce 2024 global EDA shares: Synopsys 31%, Cadence 30%, Siemens EDA 13% (article of 2 Jun 2025), and 32% / 29% / 13% in a later TrendForce piece cited by EE Times China (5 Jan 2026), which also gives the view that the big three hold >80% in China. [SECONDARY; estimates] cross-ref siemens_eda.md https://www.trendforce.com/news/2025/06/02/news-china-revenue-at-risk-as-u-s-curbs-slam-eda-giants-impact-on-synopsys-cadence-and-more/ ; cross-ref china.md https://www.design-reuse.com/news/202529890-five-year-old-chinese-eda-firm-univista-sets-sights-on-ipo-led-by

**Company data relevant to segment sizing**
- Cadence product mix: Core EDA 70% (2025) / 71% (2024) / 76% (2023); IP 14% / 13% / 12%; SD&A 16% / 16% / 12%. Functional verification (Jasper, Xcelium, Verisium, Palladium, Protium) sits inside Core EDA and is not disclosed separately. [PRIMARY] Cadence FY2025 10-K (URL above)
- Synopsys Design IP was $1.75bn in FY2025 (−8%) and $474M in Q3 FY2026 (+11%). [PRIMARY transcripts] https://www.fool.com/earnings/call-transcripts/2025/12/10/synopsys-snps-q4-2025-earnings-call-transcript/ ; https://www.webull.com/news/15497781661541376

### Inferences
- About two-thirds of ESD Alliance SIP revenue in Q2 2026 (1,473.9 of 2,199.0) is the Alliance's own estimate for Arm, CEVA and Rambus. The SIP line is therefore lower-quality data than CAE or IC PD&V.
- In Q2 2026, APAC growth (+22.4%) was IP-heavy: SIP was 1,112.5 of APAC's 2,298.7, about 48%.
- Applying analyst shares to CAE (about $7.7bn in 2025) to back out a "verification market" would double-count. CAE also contains synthesis and other front-end tools, and the ESD Alliance does not publish sub-category definitions in the releases I read.

### Gaps
- No public third-party sizes for logic simulation, formal, FPGA prototyping, VIP or static sign-off; no Siemens Veloce share; no China figure in ESD Alliance releases. (Market-research-firm reports such as MarketsandMarkets appeared in search results but were not used: methods undisclosed, reliability low.)

## 2. Emulation and prototyping hardware

### Takeaway
All three vendors refreshed their hardware between 2024 and 2026. Cadence and Synopsys each report successive record hardware years, driven by AI and hyperscale buyers. FPGA-based systems from every vendor except the custom-chip emulators (Palladium, Veloce Strato) depend on one AMD device launched in 2023 (VP1902), and I found no announced successor. Hardware is the most cyclical revenue line: it is mostly recognised up-front and carries higher costs than software.

### Cited Findings
**Current generations and capacity** (all [COMPANY CLAIM] unless stated)
- Cadence Palladium Z3 / Protium X3, announced 17 Apr 2024: "16 million to 48 billion gates"; >2x capacity and 1.5x performance vs Z2/X2; Z3 uses a new custom Cadence emulation processor; built with NVIDIA BlueField DPU and Quantum InfiniBand; GA expected Q3 2024. https://www.businesswire.com/news/home/20240417697934/en ; https://design-reuse.com/news/56088/cadence-palladium-z3-protium-x3.html
- Cadence DVCon US 2026 slides (2–5 Mar 2026): "Dynamic Duo III" = Cadence custom Z3 emulation processor + AMD VP1902; scalable to 48 billion gates; new "System Studio" desktop-class configurations; an IBS design-starts chart (see §5). https://dvcon-proceedings.org/wp-content/uploads/Broadening-the-Adoption-of-Hardware-Assisted-Verification-with-Next-Generation-Emulation-Appliance.pdf
- Siemens Veloce CS, launched 20 Feb 2024 (date from a search summary of the launch release; [UNVERIFIED] exact date). Strato CS (emulation) and Primo CS (enterprise prototyping) scale from 40 million to 40+ billion gates; Strato CS blade ~170M gates; Primo CS blade 500M gates; proFPGA CS up to 4B gates per rack and 100 MHz. Strato CS uses Siemens' purpose-built Crystal accelerator chip; Primo CS and proFPGA CS use AMD Versal Premium VP1902. Up to 5x performance vs Veloce Strato; GA summer 2024. https://www.design-reuse.com/news/news55733.html ; https://www.allaboutcircuits.com/news/siemens-unveils-3-piece-emulation-and-prototyping-solution/ ; https://assets.new.siemens.com/siemens/assets/api/uuid:99a2b00e-4e5b-4bb2-97e5-3389195b0f5c/Siemens-Veloce-CS-EN-1.pdf
- Synopsys HAPS-200 and ZeBu-200, announced 13 Feb 2025, both on VP1902. HAPS-200: up to 2x performance and 4x debug bandwidth vs HAPS-100; up to 10.8 BG multi-rack. ZeBu-200: up to 2x runtime, 8x debug bandwidth and 6x capacity vs ZeBu EP1/EP2; up to 15.4 BG. ZeBu Server 5: "scalability beyond 60 billion gates". https://news.synopsys.com/2025-02-13-Synopsys-Expands-the-Industrys-Highest-Performance-Hardware-Assisted-Verification-Portfolio-to-Propel-Next-Generation-Semiconductor-and-Design-Innovation ; https://www.synopsys.com/blogs/chip-design/introducing-zebu-200-haps-200.html
- Synopsys 11 Mar 2026 launch ("software-defined hardware-assisted verification"): HAPS-200 12 FPGA (available), ZeBu-200 12 FPGA (Q3 2026), HAPS-200 1 FPGA desktop; software-defined ZeBu Server 5 with up to 2x performance; AMD VP1902; quotes from AMD (Salil Raje; Alex Starr) and NVIDIA (Narendra Konda). https://news.synopsys.com/2026-03-11-Synopsys-Introduces-Software-Defined-Hardware-Assisted-Verification-to-Enable-AI-Proliferation . Whether ZeBu-200 12 FPGA shipped in Q3 2026: [UNVERIFIED].
- Siemens + NVIDIA (9 Apr 2026): Veloce proFPGA CS captured "tens of trillions of cycles over a span of just a few days" on an NVIDIA chip architecture. Only proFPGA CS is named. [COMPANY CLAIM, with an NVIDIA executive quoted] https://news.siemens.com/en-us/siemens-nvidia-veloce/
- Siemens agreed in the week of 9 Nov 2026 to acquire Lauterbach (debug and trace), to be added to its hardware-assisted verification offering; not closed. [PRIMARY] cross-ref siemens_eda.md https://assets.new.siemens.com/siemens/assets/api/uuid:b0adfeab-2c49-4993-9319-7b7169cff52d/Presserede-Q4-2026-Presseformat-EN.pdf
- 2026 launches in Sep–Nov 2026: none found in the Synopsys newsroom (Oct–Nov releases cover GTC Berlin, Infineon virtual prototyping, a $1bn ASR). The Cadence newsroom returned 403. https://news.synopsys.com/

**Chips inside and AMD dependence**
- AMD Versal Premium VP1902: announced 27 Jun 2023; 18.5M logic cells; 2x the prior generation; chiplet-based "emulation-class"; sampling Q3 2023, production 1H 2024; AMD claims six generations of emulation devices over 17 years. [PRIMARY company release] https://d1io3yog0oux5.cloudfront.net/_5c6e5256418b233383c6aaff9fe5b7ad/amd/news/2023-06-27_AMD_Introduces_World_s_Largest_FPGA_Based_1141.pdf ; https://www.amd.com/en/solutions/emulation-prototyping/enterprise.html . No announced successor found on 12 Nov 2026 [UNVERIFIED that none exists].
- VP1902 users found: Synopsys ZeBu-200/HAPS-200; Cadence Protium X3; Siemens Primo CS and proFPGA CS; S2C Prodigy S8. S2C's S7 uses Virtex UltraScale+ VU19P. [COMPANY CLAIM] https://www.s2cinc.com/ . Custom silicon remains only in Palladium (Cadence processor) and Veloce Strato CS (Crystal).
- Cadence 10-K: "We depend on a single supplier or a limited number of suppliers for certain hardware components and contract manufacturers"; this "has resulted in, and could continue to result in, some product delivery delays". [PRIMARY] Cadence FY2025 10-K.

**Named customers**: NVIDIA (Synopsys HAPS-200 quote; Siemens proFPGA CS; Cadence Q4 2024: "advanced our long-standing partnership with NVIDIA through commitments across a range of our EDA, hardware, IP, and system software solutions"); AMD (Synopsys March 2026 quotes); Arm (Cadence Q4 2024: "We deepened our partnership with Arm through a broad expansion of our IP, hardware and AI driven design enablement solutions"); hyperscalers named only as a category ("particularly strong demand from AI and hyperscale customers"). [PRIMARY company documents] https://s206.q4cdn.com/597110084/files/doc_financials/2024/q4/CDNS-Q4-2024-Earnings-Conference-Call-Prepared-Remarks.pdf

**Order cycle: record years per earnings materials**
- Cadence 2024: "Our hardware family delivered yet another record year, adding over 30 new customers and almost 200 repeat customers in 2024". [PRIMARY] (Q4 2024 prepared remarks, Feb 2025, URL above). Secondary summaries add that Q4 2024 was the best hardware quarter ever and 2024 "a transition year for hardware". https://fintool.com/app/research/companies/CDNS/documents/transcripts/q4-2024
- Cadence 2025: "Hardware delivered another record year, adding more than 30 new customers, with seven of the top ten customers purchasing both Palladium Z3 and Protium X3 systems". [PRIMARY via reprints, Feb 2026] https://iconnect007.com/article/148885/cadence-reports-q4-fiscal-year-2025-financial-results/148882/ein ; https://www.businesswire.com/news/home/20260216202086/en . Futurum: hardware "a pipeline business", H2 FY2026 guide prudent [SECONDARY] https://futurumgroup.com/?p=86492
- Cadence 2026: Q3 2026 call (26 Oct 2026): "yet another record quarter"; "continue to expect another record year for hardware"; inventory $448.8M vs $303.5M at end-2025; backlog $8.2bn; revenue $1.633bn (+22%); core EDA +20%, IP +24%, SD&A +30%; FY2026 guide $6.387–6.417bn; 45% of business from system companies. [PRIMARY transcript via Webull] https://www.webull.com/news/15818016766808064
- Synopsys FY2025: "Our HAV business ended a record year with 12 competitive wins in the fourth quarter" (10 Dec 2025). https://www.fool.com/earnings/call-transcripts/2025/12/10/synopsys-snps-q4-2025-earnings-call-transcript/ . FY2026: "another record quarter for hardware-assisted verification"; "12 new and 66 repeat HAV customer wins in the quarter"; EDA revenue +8.5%; EDA growth "underpinned by ... record hardware revenue" (26 Aug 2026). [PRIMARY transcript] https://www.webull.com/news/15497781661541376 . Synopsys FY2024: no record-year statement found [UNVERIFIED].
- SemiAnalysis: "Cadence reports record hardware backlog entering 2026, with H2-weighted deliveries". [SECONDARY] (primer URL above)
- Siemens discloses no hardware revenue.

**Revenue recognition and margins**
- Cadence: "Our hardware products are either sold or leased to our customers. Our emulation hardware can also be accessed remotely via a Cadence-managed cloud arrangement." Leases run up to three years. Short leases (<2 years) are operating leases, recognised straight-line. Long leases (typically 3 years) are sales-type leases "with revenue and cost of sales recognized upon installation". Up-front (point-in-time) revenue is "primarily generated by our sales of hardware products, individual IP licenses and certain software licenses": 20% of revenue in 2025, 17% in 2024, 16% in 2023 (recurring 80% / 83% / 84%). [PRIMARY] Cadence FY2025 10-K
- Cadence: hardware costs are "higher, as a percentage of revenue, than our cost of software and IP products". Hardware product costs rose $57.6M in 2025, "primarily due to increased installations of hardware". Cost of product and maintenance was $518.7M (11% of related revenue) vs $436.6M (10%). Inventories: $303.5M (end-2025), $257.7M (end-2024), $448.8M (Q3 2026). [PRIMARY] same 10-K; Q3 call
- Synopsys: hardware ("primarily consist of prototyping and emulation systems") is "generally recognized as revenue at the time of shipment". [PRIMARY] cross-ref synopsys.md, FY2025 10-K https://www.sec.gov/Archives/edgar/data/883241/000088324125000028/snps-20251031.htm
- SemiAnalysis: emulation has capital-equipment economics with 5–7-year depreciation. The per-system annual software/maintenance fee is given inconsistently ($3–5M in one place, $2–3M in another). 70–83% of big-two revenue is time-based. [SECONDARY; estimates]

**Independents (brief) and China**
- S2C: Prodigy S8 (VP1902; S8-100 Logic System), S7 (VU19P), Logic Matrix, Player Pro, 90+ Prototype Ready daughter cards; lists emulation. Cross-ref china.md: "over 700 customers and more than 4,000 systems installed"; STAR-market IPO application filed 24 Aug 2021, no update since 28 Jul 2022. [COMPANY CLAIM] https://www.s2cinc.com/
- UniVista (合见工软, China): UVHS and next-generation UVHS-2 "all-scenario verification hardware", UVHP emulation acceleration, UV APS and PD-AS prototyping, UVS+ simulator, V-Builder/vSpace virtual prototyping. [COMPANY CLAIM] https://www.univista-isg.com/ . Cross-ref china.md: filed for IPO tutoring 26 Dec 2025.
- X-Epic (芯华章): site script-rendered; no content retrieved (same gap in china.md). Corigine: site returned HTTP 412. [UNVERIFIED]
- Aldec HES boards and HES-DVM Proto "Cloud Edition" (2 Jun 2021). https://www.aldec.com/en/company/news . Blue Pearl prototyping boards BPS-VU13 (21M ASIC gates), BPS-VU19 (43M), BPS-100 (100M). https://bluepearlsolutions.ai/ [COMPANY CLAIM]

**Substitutes**
- GPU acceleration: Synopsys at NVIDIA GTC Berlin (21 Oct 2026) showed "more than 20 GPU-enabled EDA and multiphysics solutions". **None of the named examples is a verification tool** (Sentaurus 12x, S-Litho up to 40x, Ansys Speos, Lumerical 13x). [PRIMARY] https://news.synopsys.com/2026-10-21-Synopsys-at-NVIDIA-GTC-Berlin-Delivering-Engineering-Precision-with-Speed
- Cloud: Cadence offers cloud-managed emulation access (10-K above). Revenue share not disclosed.
- Cadence 10-K on necessity: "For high-performance chips like microprocessors, graphics processing units ('GPUs'), and AI processors, hardware acceleration and software prototyping are essential to handle and reduce the time necessary for large-scale functional tests that could otherwise take weeks or months." [PRIMARY, vendor statement]

### Inferences
- **Constraint or bridge?** On the evidence to November 2026, hardware-assisted verification is a persisting constraint, not a fading bridge. Capacity rose from 48B gates (Z3, 2024) to beyond 60B gates (ZeBu Server 5, 2025 claim). Buyers are the largest AI chip makers. No GPU-accelerated RTL simulation product appeared in the vendor material reviewed. The pull is software bring-up: trillions of cycles in days, not RTL bug-finding alone. The weakness is the single-source AMD FPGA. The next fleet refresh probably waits for AMD's next emulation-class device, whose timing is unknown.
- Up-front recognition plus three consecutive record years means hardware revenue would fall fastest in a capex pause. The 48% inventory build at Cadence (end-2025 to Q3 2026, my calculation) suggests deliveries are concentrated in H2 2026.
- Implied ceiling for Cadence hardware: up-front revenue was about $1.06bn in 2025 (20% × $5,296.8M, my calculation), and that also includes IP and some software. This is consistent with an emulation market of $1.5bn+ (SemiAnalysis) only if hardware is a large share of that up-front revenue. Treat as a rough check.

### Gaps
- Vendor shares including Siemens; prototyping market size; hardware revenue for any vendor; cloud-emulation share; exact AMD roadmap; Veloce 2026 launches (Siemens newsroom script-rendered); Cadence 2026 newsroom (403).

## 3. Verification IP (VIP)

### Takeaway
VIP means pre-verified protocol models (bus-functional models, monitors, checkers, coverage, plus synthesizable transactors for emulation and assertion IP for formal) for standards such as PCIe, CXL, UCIe, DDR/HBM, USB and MIPI. The big three dominate (Siemens through its Avery acquisition). Independents are small Indian-rooted specialists (SmartDV, Truechip). No public share or size data exist. AI-generated testbenches are at research stage (2026 papers) and do not yet replace protocol-compliant VIP.

### Cited Findings
- What VIP covers (vendor description): SmartDV sells VIP "compatible with all verification languages, platforms and methodologies supporting all simulation, emulation and formal verification tools", plus memory models, SimXL emulation models (synthesizable transactors), assertion IP and post-silicon validation IP. [COMPANY CLAIM] https://www.smart-dv.com/
- Leaders: Siemens acquired Avery Design Systems (then "the leading simulation-independent verification IP supplier") and calls itself a VIP leader [COMPANY CLAIM] https://us.design-reuse.com/news/52934/siemens-avery-design-systems-acquisition.html . Synopsys earlier acquired nSys Design Systems ("a leading independent provider of verification IP"; date not verified) https://evertiq.com/design/25064 . Cadence blog "Cadence adds 10 new VIPs to strengthen verification IP portfolio for AI designs" (date not verified) https://community.cadence.com/cadence_blogs_8/b/cadence-japan/posts/cadence-adds-10-new-vips-to-strengthen-verification-ip-portfolio-for-ai-designs-jp . No VIP-specific third-party share found (search, 12 Nov 2026).
- SmartDV (Bangalore + San Jose; site smartdvtech.com): "500+ interface IP products and verification solutions (VIP)"; "300+ customers around the world—including seven of the top 10 semiconductor companies"; earlier site: "more than 250 experienced ASIC and SoC design and verification engineers". Design IP is customised via SmartCompiler. SmartDV acquired a MIPI/USB design-IP business on 9 Dec 2020. Other items: Codasip partnership, ISO 9001:2015, licensing deals (RANiX SDIO, MIPI SoundWire I3S). No acquisition of SmartDV found [UNVERIFIED either way]. [COMPANY CLAIM] https://smartdvtech.com/ ; https://www.smartdvtech.com/category/press-releases/ ; https://www.design-reuse.com/news/news49147.html
- Truechip (India): first customer shipments of CXL VIP (26 Sep 2019), PCIe Gen6 (11 Jun 2021), CXL 3 + CXL switch model (12 Aug 2022), UCIe VIP (29 Nov 2022), USB4v2 and MIPI A-PHY. It offers a 24x5 support model. Blog posts on PCIe Gen 7 (14 Oct 2026) and UCIe 3.0 (12 Dec 2025). Testimonials are anonymised (US HPC, Korean mobile SoC, Taiwanese tier-1). [COMPANY CLAIM] https://www.truechip.net/
- Pricing model: no public pricing found. Vendor pages describe per-product licensing ("licensing a single design IP core from us or dozens of VIP products", SmartDV) [COMPANY CLAIM]. Term versus perpetual structure: [UNVERIFIED].
- 2025–2026 deals near verification: Arteris closed its acquisition of Cycuity (hardware-security verification) in Jan 2026 [SECONDARY] https://pulse2.com/arteris-completes-cycuity-acquisition-to-add-silicon-hardware-security-assurance/amp/ ; GlobalFoundries completed its purchase of Synopsys' ARC processor-IP business on 2 Jun 2026 (processor IP, not VIP) [SECONDARY] https://evertiq.com/design/50027 ; CSRC approved Primarius' purchase of two IP firms on 26 Jun 2026 https://dealroom.co/news/137190-primarius-buys-two-ip-firms-for-2-17b-yuan-to-build-first-chinese-eda-ip/ ; Siemens bought Defacto (21 Jul 2026; cross-ref siemens_eda.md). No 2026 acquisition of a pure VIP vendor found.
- Standards bodies' compliance programmes: PCI-SIG workshops run interoperability tests (against other members' products) and compliance tests (against PCI-SIG test modules). Cadence says its PCIe 6.0 PHY + controller (TSMC N3) passed all official PCIe 6.0 tests at a late-July 2026 workshop and joined the Integrators List [COMPANY CLAIM] https://www.eejournal.com/industry_news/cadence-subsystem-for-pcie-6-0-architecture-achieves-first-pass-pci-express-specification-compliance/ . Synopsys IP was the first "Gold System" for PCIe 6.x compliance testing https://www.synopsys.com/blogs/chip-design/pcie-6x-compliance-testing-gold-system.html . No UCIe compliance-workshop schedule or integrators list found.
- AI generation (research, not commercial): HAVEN (arXiv 2604.27643, Apr 2026) uses LLM planning with fixed templates to generate UVM components. It reports 100% compile, 90.6% code coverage and 87.9% functional coverage on 19 open-source IPs (Direct, Wishbone, AXI4-Lite) and lists driver synthesis from protocol specifications as future work. https://arxiv.org/abs/2604.27643 . UVMarvel (arXiv 2605.04704, May 2026) builds subsystem-level UVM from specs via an intermediate representation and a bus-protocol library; 95.65% average code coverage; "several human working days" cut to 4.5 hours. https://arxiv.org/pdf/2605.04704 . Agnisys markets "AI-Generated UVM Testbenches from SoC Specifications" (register/spec-driven) [COMPANY CLAIM] https://www.agnisys.com/

### Inferences
- The threat to VIP from AI generation is real for simple buses and custom interfaces, but small for complex, fast-changing standards (PCIe 6/7, CXL 3, UCIe 3.0). There, the value lies in spec-compliance credibility, built partly through compliance-programme participation. The research papers above rely on a pre-built protocol library, which is effectively VIP.
- Independents compete on early availability of new protocol versions (Truechip "first customer shipment" pattern) and customisation (SmartDV). Neither is large enough to be a top-15 company.

### Gaps
- VIP market size, shares and pricing; dates of the nSys acquisition and the Cadence 10-VIP blog; UCIe compliance status.

## 4. Independent verification and sign-off tool vendors (non-big-three)

### Takeaway
Real Intent is the only independent whose checks (CDC/RDC static sign-off) are widely used as a formal sign-off step at major chip companies. Even so, it is private, with no revenue disclosure. The others are niche (Aldec, Blue Pearl), infrastructure (Verific), methodology (Breker) or specification tools (Agnisys). Consolidation continued in 2026 with Defacto bought by Siemens and Cycuity by Arteris. None clearly belongs in a global top 8–15 on economic weight. Real Intent is a borderline candidate if the ranking rewards owning an accepted sign-off check.

### Cited Findings
| Vendor | HQ / ownership (as of Nov 2026) | Products | Customers (claims) | Accepted sign-off step? | Source |
|---|---|---|---|---|---|
| Real Intent | Sunnyvale CA; founded 1998; "funded by Andy Bechtolsheim"; offices in Japan, Korea, India, Europe, Israel, China; no 2026 funding or M&A news on site | Ascent Lint, Meridian CDC/RDC/DFT, Conquest MAI (24 Feb 2026), Conquest Sentry (security), SafeConnect, Meridian CDC with Microarchitecture Analysis (30 Jun 2026), Riven sign-off AI agent "10X faster sign-off" (23 Jul 2026) | "more than 50 major semiconductor and systems company customers"; NVIDIA "a customer of Real Intent since 2000"; STMicroelectronics benchmark (Meridian RDC 25x noise reduction vs a competitor); Samsung Foundry adopted Meridian CDC (28 Oct 2020); lowRISC/OpenTitan (9 May 2024); Rivos RDC methodology case | Yes for CDC/RDC: positions itself as "static sign-off"; ISO 26262 compliance claims | [COMPANY CLAIM] https://www.realintent.com/company/ ; https://www.realintent.com/press-releases/ ; https://www.realintent.com/ |
| Breker Verification Systems | Site returned 403; ownership/funding 2026 [UNVERIFIED] | Portable Stimulus / test-suite synthesis (per brief) | Cross-ref ai_native notes: partnership with MooresLabAI | No (test generation, not sign-off) | ai_native_chip_verification_open_source.md |
| Verific Design Automation | Verific Design Automation, Inc. (US, 510 area code, Bay Area); no ownership change stated | SystemVerilog (IEEE 1800), VHDL (IEEE 1076), UPF (IEEE 1801) parsers sold as C++ source; INVIO; "EDA Store" opened 22 Jul 2026 | 49 logos incl. AMD, Cadence, IBM, Xilinx, Lattice, Microsemi, NVIDIA, Renesas, Siemens, Synopsys, YosysHQ | No; embedded front-end inside other vendors' tools | [COMPANY CLAIM] https://www.verific.com/ |
| Aldec | Henderson NV; private | Riviera-PRO, Active-HDL, ALINT-PRO (DO-254 plug-in; mixed-language rules, 14 Jan 2026), HES prototyping | FPGA and avionics; co-presented with Thales (2023) | DO-254 design-assurance linting (niche) | [COMPANY CLAIM] https://www.aldec.com/en/company/news |
| Blue Pearl (now "Blue Pearl AI Solutions") | Santa Clara CA; "privately held"; bluepearlsoftware.com 301-redirects to bluepearlsolutions.ai; rebrand undated | Visual Verification Suite+ ("signoff-grade validation to AI-generated RTL": Analyze RTL AI, CDC/RDC AI, AI Requirements Analysis, BPSim, HDLCreator); FPGA prototyping boards | No named customers; aerospace/defence, medical | FPGA lint/CDC (niche) | [COMPANY CLAIM] https://bluepearlsolutions.ai/ |
| Ausdia | Site returned 403 | Described in the brief as a sign-off tool vendor; product, ownership and 2026 status [UNVERIFIED] | — | [UNVERIFIED] | — |
| Agnisys | US-headquartered (cross-ref india notes) | IDesignSpec Suite, IDS-AI, IDS-NoC: executable specification → UVM RAL models, testbenches, assertions, C headers, documentation | Cross-ref specification notes: iCatch (Jun 2025), Etched (Dec 2024), Wacom (Nov 2023); 14 Oct 2026 partnership with Axiomise (IDS-NoC + nocProve formal) | No (spec/register automation feeding verification) | [COMPANY CLAIM] https://www.agnisys.com/ ; specification_requirements_tools.md |

- Others in other researchers' files: Axiomise and LUBIS EDA (formal sign-off services/tools, Europe); Defacto (acquired by Siemens 21 Jul 2026); Cycuity (acquired by Arteris, Jan 2026); S2C, UniVista, X-Epic (China); SmartDV, Truechip (VIP, §3).
- Standardisation of CDC/RDC: Agnisys co-presented a "CDC-RDC Verification Standard 1.0" tutorial at DVCon India 2026 (1–3 Sep 2026). [COMPANY CLAIM] cross-ref india notes https://www.agnisys.com/agnisys-at-dvcon-india-2026/

### Inferences
- **Top 8–15 test:** Real Intent has the best case among independents: an accepted sign-off check, flagship customers, and an AI agent launched in 2026. Its scale is unknown. The big three each sell competing CDC/RDC tools, which I did not quantify. S2C matters in prototyping (largest independent by its own installed-base claim) but is China-centred and not a sign-off verdict. Verific matters as an enabler: parsers inside the big three's and new entrants' tools. A study ranking "who checks chips" would place them as honourable mentions unless revenue data emerge. This is a judgment, not a measured ranking.
- The pattern from 2020 to 2026 is acquisition of independents (Avery→Siemens, Defacto→Siemens, Cycuity→Arteris). The remaining independents are more likely acquisition targets than future large standalone vendors (inference).

### Gaps
- Revenue, headcount and funding for every private vendor; Breker and Ausdia status; Real Intent share of CDC/RDC sign-off.

## 5. Demand and outcome statistics

### Takeaway
The brief's Wilson figure is right but needs qualifiers. It covers IC/ASIC respondents only, the 2024 figure was 14.4%, the study is vendor-sponsored, and recruitment changed in 2024. The brief's TrendForce "≈45% custom-chip unit growth in 2026" is a misreading. The 44.6% is an October 2025 forecast of AI-server shipment growth for servers based on cloud providers' in-house ASICs, not a measured chip-unit outcome. Demand drivers remain strong: R&D at leading chip designers grew double digits, cloud capex is forecast at +90% in 2026, and AI/hyperscale buyers dominate hardware purchases.

### Cited Findings
**Wilson Research Group / Siemens EDA 2026 Functional Verification Study** [vendor-sponsored survey; PRIMARY for what Siemens published]
- Published 8 Sep 2026 (blog by Harry Foster). "only 5% reported first-silicon success in 2026, compared with 14.4% in 2024" (IC/ASIC). Logic/functional errors "remain important and continue to be a major contributor to ASIC respins". Also "firmware, safety, security, power, clocking, timing" contributors, no percentages. The Methodology Reference Paper "explains the recruitment-methodology transition between the historical 2007–2022 studies and the current 2024–2026 study period". https://blogs.sw.siemens.com/verificationhorizons/2026/09/08/the-2026-functional-verification-study/
- "604 qualified participants: 320 working on IC/ASIC projects and 284 working on FPGA projects"; "uses the same qualified recruitment approach introduced in 2024" (sample-provider recruitment); "verification consumes roughly half of project time": 49% of IC/ASIC and 51% of FPGA project time. About 3 of 4 projects are behind schedule. 98% of FPGA respondents report non-trivial production escapes. 97% of IC/ASIC projects have embedded processors. AI: 82.8% beyond evaluation/pilot, 9.0% broadly integrated. "particularly strong participation from CPU, GPU, and AI accelerator-class projects". https://verificationacademy.com/topics/planning-measurement-and-analysis/2026-siemens-eda-and-wilson-research-group-functional-verification-study/ ; https://verificationacademy.com/topics/planning-measurement-and-analysis/wrg-industry-data-and-trends/2026-functional-verification-study-executive-findings-paper/
- Foster, 28 Oct 2026: "approximately three out of four IC/ASIC and FPGA projects are missing their original schedules". https://blogs.sw.siemens.com/verificationhorizons/2026/10/28/are-we-looking-beyond-the-numbers-in-the-2026-functional-verification-study/ . Leading AI uses: debug/root-cause, test generation, coverage analysis (cross-ref india notes).
- Trend: Foster (3 Sep 2025) called 2024's 14% "the lowest figure in more than twenty years of tracking this data" and wrote "60–70% of engineering effort in chip projects belongs in verification" (a different metric from time share). https://blogs.sw.siemens.com/verificationhorizons/2025/09/03/why-first-silicon-success-is-getting-harder-for-system-companies . SemiWiki [SECONDARY; 403 on fetch, search snippet only]: 5% against "a roughly 30% average held over at least a decade"; "significant growth in respins tied to accelerator-style designs". https://semiwiki.com/artificial-intelligence/373809-wilson-survey-signals-need-for-new-understanding-of-verification-success/
- Exact 2018/2020/2022 values, respin-cause percentages, verification-to-design engineer ratio and formal adoption sit in a login-gated "Data Atlas" [UNVERIFIED].

**TrendForce**
- 9 Oct 2025 Insights: "In 2026, cloud service providers' (CSPs) in-house ASICs are expected to grow by 44.6%, significantly surpassing GPUs at 16.1%", derived from "growth rates in total AI server shipments". [SECONDARY research-firm forecast] https://www.trendforce.com/insights/nvidia-scale-up-technology . **CORRECTION to the brief**: this is a forecast of AI-server shipment growth by accelerator type, made in Oct 2025, not realised 2026 custom-chip unit growth. No later TrendForce ASIC-only growth figure was found.
- 20 Jan 2026: AI server shipments >28% YoY in 2026; ASIC-based share 27.8%, GPU 69.7%; Google TPU ">40% annual growth in 2026"; AWS ASIC shipments to "more than double in 2025", then about +20% in 2026; Microsoft Maia v3 delayed (search summary). https://www.trendforce.com/presscenter/news/20260120-12887.html
- 18 Mar 2026: "ASIC-based AI servers are forecast to represent 27.8% of all AI server shipments in 2026"; "nearly 40% by 2030". https://www.trendforce.com/presscenter/news/20260318-12976.html
- 3 Aug 2026 (re-checked): 2026 AI server growth raised from 28% to nearly 31%. Nine CSPs (Google, Amazon, Meta, Microsoft, Oracle, ByteDance, Tencent, Alibaba, Baidu) to exceed US$886.7bn capex in 2026, about +90%, with the five North American hyperscalers nearly 90% of it. About $1.3tn in 2027 (nearly +50%). Google, AWS and Meta expand in-house ASICs in 2027. https://www.trendforce.com/presscenter/news/20260803-13161.html

**R&D, design starts and custom-chip programmes**
- R&D expense of six US-listed chip companies (SEC XBRL, retrieved 12 Nov 2026) [PRIMARY]: NVIDIA FY2025 (Jan 2025) $12.91bn → FY2026 $18.50bn (+43.3%); H1 FY2027 $13.38bn vs $8.28bn (+61.6%). AMD 2024 $6.46bn → 2025 $8.09bn (+25.2%); 9M 2026 $7.73bn vs $5.76bn (+34.2%). Broadcom FY2024 $9.31bn → FY2025 $10.98bn (+17.9%); 9M FY2026 $8.86bn vs $8.00bn (+10.8%). Qualcomm FY2025 $9.04bn → FY2026 $10.21bn (+12.9%). Intel 2024 $16.55bn → 2025 $13.77bn (−16.8%); 9M 2026 −3.0%. Marvell FY2025 $1.95bn → FY2026 $2.08bn (+6.7%); H1 FY2027 $1.39bn vs $1.03bn (+35%). Sum (my calculation, mixed fiscal years): $56.1bn → $62.5bn (+11.4%); excluding Intel +23.2%. https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json (NVIDIA; same pattern for CIK0000002488 AMD, CIK0001730168 Broadcom, CIK0000804328 Qualcomm, CIK0000050863 Intel, CIK0001835632 Marvell)
- Design starts: IBS chart in Cadence's DVCon 2026 slides shows 10,644 design starts in 2026, with about three-quarters at 28nm or above by 2030 [projection; COMPANY-presented third-party data]. (DVCon slides URL, §2.) Advanced-node design-start counts were not found separately.
- Buyer mix: Cadence says 45% of its business is from system companies (Q3 2026) and cites "particularly strong demand from AI and hyperscale customers" for hardware (above).

### Inferences
- Three things point to verification demand that exceeds what tools alone can solve: falling first-silicon success, roughly half of project time in verification, and heavy AI-accelerator participation. This supports hardware and sign-off spending. It also undercuts any claim that tools "own the verdict" (§8).
- R&D growth is concentrated in AI-exposed designers (NVIDIA, AMD, Marvell) while Intel cuts. Verification demand is therefore becoming more concentrated in a few large buyers, the same ones buying record hardware.

### Gaps
- Industry-wide semiconductor R&D (SIA, TechInsights) 2024–2026 not retrieved; Wilson historical series and detailed charts; realised 2026 ASIC volumes.

## 6. Cycle history and implications of a financing-led AI pause (~2028)

### Takeaway
Since the move to time-based licensing, EDA software has kept growing through semiconductor downturns. Synopsys grew 1.7% in FY2009, and both majors grew 8–19% in 2019 and 2022–23. The large historical revenue falls came at Cadence in 2008–09, when up-front product revenue and perpetual-licence habits dominated. That makes the up-front parts (hardware, some IP) the lines to watch in any 2028 pause.

### Cited Findings
- 2008–09 [PRIMARY, SEC XBRL]: Cadence revenue FY2008 $1,038.6M → FY2009 $852.6M (−17.9%) → FY2010 $936.0M. Product revenue (software licences plus hardware) 516.6 → 400.8 (−22.4%) → 471.6; services 133.5 → 106.6 (−20.1%) → 100.9; maintenance 388.5 → 345.3 (−11.1%) → 363.5. Synopsys FY2008 $1,337.0M → FY2009 $1,360.0M (+1.7%) → FY2010 $1,380.7M. https://data.sec.gov/api/xbrl/companyfacts/CIK0000813672.json ; https://data.sec.gov/api/xbrl/companyfacts/CIK0000883241.json
- SemiAnalysis [SECONDARY]: Cadence revenue fell 36% in one year under Mike Fister (consistent with FY2007→FY2008); operating margin −11% in 2009. "Under the old perpetual model, customers could skip maintenance during downturns. Time-based licensing removed that option." Synopsys and Cadence: "Thirteen years of unbroken growth through every cycle". (Primer URL, §1)
- 2019 [PRIMARY]: Cadence FY2019 $2,336.3M (+9.3% from $2,138.0M); Synopsys FY2019 $3,360.7M (+7.7% from $3,121.1M).
- 2022–23 [PRIMARY]: Cadence FY2020 $2,682.9M; FY2021 $2,988.2M; FY2022 $3,561.7M (+19.2%); FY2023 $4,090.0M (+14.8%); FY2024 $4,641.3M (+13.5%); FY2025 $5,296.8M (+14.1%). Synopsys FY2022 $5,081.5M (+20.9%, my calculation from FY2021 $4,204.2M); FY2023 $5,842.6M (+15.0%); FY2024 $6,127.4M (+4.9%, continuing operations after the software-integrity divestiture); FY2025 $7,054.2M (+15.1%, includes Ansys from July 2025). ESD Alliance 2023 quarterly totals 3,951.1 / 3,962.7 / 4,702.4 / 4,440.9 (§1).
- 2001–02: no primary data retrieved (sec.gov blocks undeclared automated clients; EDAC historical releases not found without search). [UNVERIFIED]
- Current buffers: Cadence backlog $8.2bn (Q3 2026); cross-ref cadence.md: $4.2bn of remaining performance obligations expected within 12 months. Siemens: "Fiscal 2027 is a strong renewal year for our EDA business" (12 Nov 2026; cross-ref siemens_eda.md). Cadence recurring share fell to 80% (2025) from 84% (2023) as hardware grew (§2).

### Inferences
- Implication for a financing-led AI pause around 2028 (scenario, not forecast):
  - (a) Subscription EDA software would likely slow rather than shrink, because multi-year contracts and backlog carry revenue through a year or two.
  - (b) Emulation and prototyping hardware is up-front, bought mostly by AI/hyperscale programmes and after three record years. It is the line most likely to fall, possibly sharply. Cadence's 2009 product line fell 22%.
  - (c) IP licensing follows design starts. Royalties follow unit volumes. The ESD Alliance SIP line is IP-heavy in APAC.
  - (d) Services are the most discretionary. Cadence services fell 20% in 2009.
- TrendForce's 2027 capex growth (~+50%, after ~+90% in 2026) implies deceleration before any pause. Hardware orders would be the first to show it.

### Gaps
- 2001–02 and 2008–09 industry-level (ESD Alliance/EDAC) data by category; hardware-only revenue history; Mentor/Siemens emulation history.

## 7. Labour versus tools

### Takeaway
No source splits verification spending between tools and people. The available proxies suggest people still dominate cost. Verification takes about half of project time, while EDA revenue is about a third of the R&D of just six large chip designers. Signs of labour price pressure exist but are thin, and EDA vendors' own headcount has started falling.

### Cited Findings
- Time and effort: verification is 49% of IC/ASIC project time (Wilson 2026); "60–70% of engineering effort" (Foster 2025). (URLs §5)
- EDA-vendor employment (ESD Alliance tracked companies) [PRIMARY]: 57,696 (Q1 2023) → 73,185 peak (Q3 2025) → 71,396 (Q2 2026). That is −2.4% from peak (my calculation) and −1.6% YoY, while revenue grew 12.2%. The step from 64,403 (Q1 2025) to 72,529 (Q2 2025, +12.6%) is unexplained in the releases [UNVERIFIED cause].
- Vendor headcount (cross-ref): Synopsys ~28,000 employees at FY2025 year-end; 2026 restructuring with "majority of the workforce reduction in fiscal 2026"; expected charges raised to $425–500M (26 Aug 2026) https://www.sec.gov/Archives/edgar/data/883241/000088324126000025/R70.htm (synopsys.md). Cadence ~13,800 employees at end-2025 and 15,753 at Q3 2026 after Hexagon (cadence.md).
- Labour pricing (cross-ref india_and_verification_services.md) [PRIMARY transcripts / SECONDARY data]: LTTS CEO, 14 Jul 2026: "the tools are being used as part of our bids to our customers, and we are having to pass on some productivity improvement". UK contract ads citing UVM: 27 → 18 → 10 (six-month windows to Nov 2024 / 2025 / 12 Nov 2026). Median hourly rate GBP 95 → 80 → 80, from samples too small to be reliable. https://www.ltts.com/system/files/2026-07/LTTS-Q1FY27-Earnings-Call-Transcript.pdf
- Proxy (my calculation): 2025 EDA revenue $21.2bn vs $62.5bn latest-FY R&D at six US-listed chip companies (§5).

### Inferences
- Verification is still mostly paid as engineer time. AI agents priced per "subscription of our agents ... consumption measure" (Synopsys, cross-ref synopsys.md) and an "agentic surcharge" (Siemens, cross-ref siemens_eda.md) are attempts to move part of that labour budget into tool revenue. No data yet show that the shift has happened.

### Gaps
- Tools/people split; verification-engineer headcount 2020–2026 (Wilson's engineer counts gated); verification-specific wage data outside the UK sample.

## 8. Segment table, cycle-position summary and closing lists

### Takeaway
Measured data are strong for total EDA, its five ESD Alliance categories and the regional split. They are weak or absent for every verification sub-segment, which rests on analyst estimates or vendor claims. In November 2026 hardware is at a cyclical high, IP is in a strong upswing, software is in steady mid-to-late expansion, and independent verification services face price pressure.

### Cited Findings: segment table

| Segment | Size (period) | Growth | Leaders and shares | Evidence quality |
|---|---|---|---|---|
| Total EDA/ESD (ESD Alliance) | $21.2bn 2025 (my sum); $11.46bn H1 2026 | +10.2% 2025; 4QMA +11.2% (Q2 2026) | Synopsys 31–32%, Cadence 29–30%, Siemens 13% (TrendForce 2024, estimates) | High for size [PRIMARY]; medium for shares [SECONDARY] |
| CAE (includes functional verification) | $7.66bn 2025 | +11.3% 2025; 4QMA +10.7% | Big three; not split | High for size |
| IC physical design & verification | $3.04bn 2025 | −5.1% 2025 (as reported); 4QMA +5.4%; H1 2026 +12.5% | Calibre 85%+ (physical verification); PrimeTime 90%+ (STA) (SemiAnalysis estimates, advanced nodes) | High for size; low for shares |
| Semiconductor IP | $7.87bn 2025 | +17.4% 2025; 4QMA +16.6% | Arm, Synopsys (Design IP $1.75bn FY2025), Cadence (IP 14% of revenue) | Medium: ~67% of Q2 2026 SIP is estimated by the ESD Alliance |
| EDA-vendor services | $0.87bn 2025 | +15.9% 2025; 4QMA +15.2% | Not split | High for size (excludes independent design-services firms) |
| Logic simulation | Not found | n/a | VCS 45–50%, Xcelium 40–45% (SemiAnalysis; Questa omitted) | Low |
| Emulation | "$1.5B+" (SemiAnalysis, May 2026) | Record years 2024–2026 (Cadence; Synopsys FY2025–26) | Palladium 55–60%, ZeBu 35–40% (two-vendor split; Veloce omitted) | Low to medium |
| FPGA prototyping | Not found | Record HAV years include prototyping | Synopsys HAPS, Cadence Protium, Siemens Primo/proFPGA; S2C claims 700+ customers | Low |
| Formal | Not found | n/a | Big three; independents Axiomise, LUBIS (see Europe notes) | None quantitative |
| Verification IP | Not found | n/a | Big three (Siemens incl. Avery); SmartDV, Truechip | Low (company claims) |
| Static functional sign-off (lint/CDC/RDC) | Not found | n/a | Big three; Real Intent (>50 major customers, claim) | Low |
| Independent verification services | See India notes | Mixed (LTTS Tech −8.5% YoY; MosChip revenue −19% Q2 FY27) | LTTS, Tessolve, MosChip and others | Medium (filings) |

### Inferences: cycle position as of 12 Nov 2026
- **(a) EDA software: mid-to-late expansion, steady.** 4QMA growth is +11%. APAC (+18%) leads and Japan is contracting (−8%). Backlogs are at records (Cadence $8.2bn). Vendor headcount is down 1.6% YoY, and AI-agent monetisation is starting. The main risks are China policy and a slowdown in AI programmes. Subscription models damp the downside (FY2009 Synopsys +1.7%).
- **(b) Emulation and prototyping hardware: cyclical peak / late upcycle.** This is the third straight record year. A full generation refresh ran from 2024 to 2026. Buyers are concentrated (seven of Cadence's top ten bought both Z3 and X3). Cadence's inventory build was +48% in nine months. Revenue is point-in-time and costs run higher than software. The product cycle depends on AMD's next emulation-class FPGA. This is the most exposed line in a pause.
- **(c) Semiconductor IP: strong upswing.** ESD Alliance SIP grew +17% in 2025 and H1 2026. Cadence IP was +24% (Q3 2026). Synopsys Design IP recovered to +11% after −8% in FY2025. Data quality is weaker because most of the ESD Alliance figure is estimated.
- **(d) Verification services: late-cycle, under price pressure.** EDA-vendor services grew (+15% 4QMA), but independent services firms show soft semiconductor segments and pass AI productivity on to clients. Capital is consolidating (Tessolve raised $75M in Oct 2026; cross-ref india notes https://cxotoday.com/media-coverage/tessolve-semiconductor-a-hero-electronix-company-secures-75-million-investment-from-vector-line-capital/).

### Gaps
#### Figures that are estimates (not measured)
- SemiAnalysis: emulation $1.5bn+; Palladium/ZeBu, VCS/Xcelium, PrimeTime, Calibre shares; emulation fees and depreciation.
- TrendForce: 2024 vendor shares; 44.6%/16.1% ASIC vs GPU AI-server growth (forecast); AI-server growth 28–31%; ASIC share 27.8%; CSP capex $886.7bn (2026) and ~$1.3tn (2027); Google/AWS ASIC growth.
- ESD Alliance: SIP for non-reporting companies (Arm excl. PIPD, CEVA, Rambus; 1,473.9 of 2,199.0 in Q2 2026); Arm PIPD exclusion.
- IBS design starts (10,644 in 2026; 2030 node mix), as presented by Cadence.
- My calculations: annual and half-year ESD Alliance sums, category shares, R&D aggregates, Cadence up-front revenue proxy, inventory growth, employment change.

#### What I could not verify
- Wilson 2018–2022 first-silicon values, respin-cause percentages, verification:design engineer ratio, formal adoption (gated Data Atlas).
- Size or shares for simulation, formal, prototyping, VIP and static sign-off; Siemens Veloce share; any vendor's hardware revenue.
- An AMD VP1902 successor; ZeBu-200 12-FPGA shipment; exact Veloce CS launch date; Synopsys FY2024 hardware record.
- Breker, Ausdia, X-Epic, Corigine 2026 status; SmartDV and Verific ownership beyond their sites; Real Intent revenue.
- 2001–02 EDA data; industry-wide semiconductor R&D; commercial GPU-accelerated RTL simulation; cloud-emulation revenue; tools-vs-labour split; VIP pricing; UCIe compliance programme; dates of the nSys acquisition and the Cadence 10-VIP blog.

#### Where current evidence contradicts the background views
- **"Verification tools own the verdict while verification labour loses its price"**: partly contradicted.
  - Tools are growing and sign-off tools hold dominant (estimated) shares, but first-silicon success fell to 5% despite them. Tools do not "own" a good verdict.
  - Verification still takes about half of project time, and EDA-vendor services grew 15%.
  - Labour price evidence is limited to LTTS pass-through and a tiny UK sample.
- **"The three large vendors keep growing through 2029"**: not contradicted, but at risk.
  - Supportive: 13 years of unbroken growth; double-digit 2025–26.
  - Against: Synopsys grew only +4.9% in FY2024, and its Design IP fell 8% in FY2025.
  - China fell 18–22% (Synopsys FY2025) and 15.7% (Cadence 2024).
  - Cadence's up-front share is rising (16% → 20%), which adds cyclicality.
  - EDA headcount is falling, and Cadence fell 17.9% in FY2009.
- **"First-silicon success improves by 2030"**: contradicted by the trend to date: 5% (2026) vs 14.4% (2024) vs ~30% decade average. Three in four projects are late. A methodology break in 2024 limits long-run comparisons.

#### Sources with dates (most-used)
- SEMI ESD Alliance EDMD releases, 15 Jul 2024 to 19 Oct 2026 (URLs §1).
- Cadence: FY2025 10-K (Feb 2026); Q4 2024 prepared remarks (Feb 2025); Q4 2025 release (Feb 2026); Q3 2026 call (26 Oct 2026); DVCon US 2026 slides (Mar 2026); Palladium Z3/Protium X3 release (17 Apr 2024).
- Synopsys: Q4 FY2025 call (10 Dec 2025); Q3 FY2026 call (26 Aug 2026); HAPS-200/ZeBu-200 release (13 Feb 2025); HAV release (11 Mar 2026); GTC Berlin release (21 Oct 2026); FY2025 10-K.
- Siemens: Veloce CS (Feb 2024); NVIDIA/Veloce proFPGA CS (9 Apr 2026); Q4 FY2026 speech (12 Nov 2026).
- AMD: VP1902 release (27 Jun 2023).
- Wilson/Siemens study pages (8 Sep 2026; 28 Oct 2026); Foster blog (3 Sep 2025); SemiWiki (Sep–Oct 2026, secondary).
- TrendForce (9 Oct 2025; 20 Jan 2026; 18 Mar 2026; 3 Aug 2026); SemiAnalysis primer (21 May 2026).
- SEC XBRL company facts (retrieved 12 Nov 2026).
- Company sites fetched 12 Nov 2026: Real Intent, Verific, Blue Pearl, Aldec, SmartDV, Truechip, S2C, UniVista, Agnisys.
- arXiv HAVEN (Apr 2026) and UVMarvel (May 2026).
- PCI-SIG workshop coverage (Jul–Aug 2026).
