# Japan, South Korea and Taiwan: automated-security companies — quality tests, path forward and entry points (research date 2026-11-12)

Scope note: covers listed and private security companies in Japan, Korea and Taiwan relevant to automated vulnerability discovery and repair, code security, exposure management, OT/IoT shielding, detection and response, penetration testing and bug bounty, and machine-checked verification. TXOne Networks is covered by another researcher and appears here only as context. Method limit: the shared web-search budget for this session (200 searches across all agents) ran out about a third of the way through this research. After that I only fetched pages already found in search results or known primary sources (company IR pages, DARPA, ZDI, IPA, Taiwan's law database, StockAnalysis quote pages). I did not route around the limit through other search engines. Several items below are therefore marked as gaps. Every market figure is dated. Quality tests (business position) are kept separate from entry points (price).

## 1. Which, if any, belong in a global top 8–15 for automated security?

### Takeaway
At most one company from these three countries, Trend Micro, has a defensible case for a global top 8–15, and only at the bottom of that range. The case rests on two things: global scale, and ownership of a "judge" (the Zero Day Initiative (ZDI) and its Pwn2Own contests). It does not rest on leadership in machine-speed find-and-fix. Outside rankings put Trend Micro 5th–6th in its core categories by 2024, and its constant-currency revenue growth was +3% in Q3 2026. Theori (Korea–US, private; product brand "Xint") has the region's strongest independent evidence of autonomous vulnerability discovery: AIxCC 3rd in August 2025 at the lowest cost per point of the top three, and 2nd at Pwn2Own Ireland in October 2026 as team "Xint". But it is small (about 92 staff) and has no disclosed revenue, so it belongs on a watch list, not in the top 15. Samsung Research's place in Team Atlanta (the AIxCC winner) is evidence of Korean capability, not an investable security business. Every other company covered is a domestic champion, a services firm or a sub-scale niche vendor.

### Cited Findings
- **Trend Micro scale and growth.** Q3 2026 (quarter to 30 Sep 2026): net sales ¥75,317m, +9% reported and +3% in constant currency. Operating income ¥13,231m (18% margin, −17% YoY). TrendAI ARR $1,292m, +8% YoY. FY2026 guidance unchanged at ¥301.5bn sales and ¥44.4bn operating income (15% margin, −23%). Source: [Trend Micro FY2026 Q3 results deck, 2026-11-12](https://www.trendmicro.com/content/dam/trendmicro/global/en/about/investor-relations/reports-presentation/2026/financial-2026-presentation-negi-q3.pdf)
- **Trend Micro's outside rankings (latest found, 2024).**
  - Gartner Endpoint Protection Platforms Magic Quadrant (Sept 2024): 5th, behind CrowdStrike, Microsoft, SentinelOne and Palo Alto Networks.
  - Forrester cloud workload security (2024): 6th.
  - IDC CNAPP: 13.1% share in 2023, growing 11.3% a year against 31.5% for the market.
  - IDC endpoint: growing more slowly than any of the seven share leaders. Microsoft and CrowdStrike held nearly 44% of a $12.6bn endpoint market (IDC, 2024).
  - Source: [BankInfoSecurity, 2025-02-14](https://www.bankinfosecurity.com/blogs/private-equity-now-kicking-tires-on-trend-micro-p-3814)
- **The ZDI "judge" asset.**
  - Pwn2Own Ireland 2026 (Cork, 6–8 Oct 2026) was organised by TrendAI's ZDI. It paid $1,262,000 for 98 unique zero-days across 61 attempts by 29 teams. Source: [CyberInsider, 2026-10-09](https://cyberinsider.com/google-pixel-10-hacked-as-pwn2own-ireland-wraps-with-1-26-million-in-rewards/)
  - The 2025 Ireland event yielded 73 zero-days and $1,024,750. Source: [BleepingComputer (search-result summary; page returned 403 when fetched)](https://bleepingcomputer.com/news/security/hackers-earn-1262000-for-98-zero-days-at-pwn2own-ireland)
  - ZDI's advisory numbering had reached ZDI-26-953 by 2026-11-11, including AI/ML software such as Meta FAIRChem. Source: [ZDI published advisories, accessed 2026-11-12](https://www.zerodayinitiative.com/advisories/published/)
- **ZDI controversy.** In October 2026 ZDI reportedly disclosed six Linux kernel vulnerabilities on the public kernel mailing list without patches, against kernel guidance and its own policy (the "Black October" disclosures). Source: [Wikipedia "Trend Micro", accessed 2026-11-12](https://en.wikipedia.org/wiki/Trend_Micro). Secondary source; not independently verified.
- **AIxCC final (8 Aug 2025).**
  - Placings: Team Atlanta 1st ($4m), Trail of Bits 2nd ($3m), Theori 3rd ($1.5m).
  - Finalists found 54 unique synthetic vulnerabilities across 63 challenges and patched 43. That is 86% identified and 68% of those patched, up from 37% and 25% at the semifinal.
  - They also found 18 real vulnerabilities. Average patch time was 45 minutes; average cost about $152 per task.
  - Source: [DARPA, 2025-08-08](https://www.darpa.mil/news/2025/aixcc-results)
- **Team make-up.** Team Atlanta combined Georgia Tech, Samsung Research, KAIST and POSTECH. DARPA described Theori as "AI researchers and security professionals in the U.S. and South Korea" whose team "has won eight DEF CON CTF finals". Source: [DARPA, 2025-07-08](https://www.darpa.mil/news/2025/ai-cyber-challenge-winners-def-con-33). Theori's system was named RoboDuck. Source: [Infosecurity Magazine (search-result summary)](https://www.infosecurity-magazine.com/news/defcon-ai-cyber-challenge-winners/)
- **AIxCC cost efficiency, as published by Trail of Bits (2025-08-09).**

  | Team | Total spend | LLM | Compute | Cost per point |
  |---|---|---|---|---|
  | Team Atlanta | $103.3k | $29.4k | $73.9k | $263 |
  | Trail of Bits | $39.6k | — | — | $181 |
  | Theori | $31.8k | $11.5k | $20.3k | $151 |

  Source: [Trail of Bits](https://blog.trailofbits.com/2025/08/09/trail-of-bits-buttercup-wins-2nd-place-in-aixcc-challenge/)
- **Pwn2Own Ireland 2026 final standings.** Ikotas Labs $361,000 and 42.5 points; Xint $240,000 and 27.5 points; Team ZyGoat $125,000 and 27.5 points. Source: [CyberInsider, 2026-10-09](https://cyberinsider.com/google-pixel-10-hacked-as-pwn2own-ireland-wraps-with-1-26-million-in-rewards/). SecurityLab, citing ZDI, gives Ikotas 30 points, so the sources conflict. Source: [SecurityLab (search-result summary)](https://www.securitylab.ru/news/578559.php)
- **Xint (Theori) recognised by IDC.** Named an IDC Innovator for "Agentic Autonomous Penetration Testing for DevSecOps". Source: [Business Wire, 2026-08-13 (title only; page returned 403)](https://www.businesswire.com/news/home/20260813325954/en/Xint.io-Recognized-as-an-IDC-Innovator-for-Agentic-Autonomous-Penetration-Testing-for-DevSecOps)
- **DEF CON CTF record.**
  - The Korea–US–Canada joint team MMM won four straight titles, 2022–2025.
  - At DEF CON 34 (August 2026): Korean team 0x4b52 (KAIST Hacking Lab with the team HYPEBOY) placed 2nd. SuperDiceCodeLovers (mainly Enki Whitehat and Raon Secure hackers) placed 3rd.
  - Theori staff were among the mentors or leaders of several top-12 teams.
  - Source: [MTN (Korean), 2026-08-10](https://news.mtn.co.kr/news-detail/2026081011560011163)
  - Carnegie Mellon headline: "Carnegie Mellon's hacking team wins fourth straight, record ninth overall DEF CON Capture the Flag title". Source: [CMU, 2025-08-14 (headline only; page returned 503)](https://www.ri.cmu.edu/carnegie-mellons-hacking-team-wins-fourth-straight-record-ninth-overall-def-con-capture-the-flag-title/)
- **Theori's size and strategy.**
  - About 92 employees as of Sept 2026; last disclosed round was a Series A in June 2022. Source: [THE VC (Korean)](https://thevc.kr/theori)
  - Raised $15.4m over two rounds. Source: [SiliconANGLE, 2026-03-17](https://siliconangle.com/2026/03/17/theori-launches-xint-code-ai-platform-uncover-hidden-vulnerabilities-massive-codebases/)
  - Phasing out consulting and paid training during 2026 to focus on Xint. Source: [Seoul Economic Daily, 2026-10-08](https://en.sedaily.com/technology/2026/10/08/theori-drops-consulting-training-to-bet-all-on-ai-hacking)

### Inferences
- **Trend Micro: marginal inclusion at most.**
  - It is the only company from these countries with global scale (about $1.9bn of FY2026 guided sales at the Q3 average rate of ¥159.30/USD).
  - Its ZDI/Pwn2Own franchise works as a recognised judge: vendors accept its adjudication of exploit claims, results are final at the event, and each finding comes with an advisory. That judge is human-run and bounty-funded, however. AI-found bug supply (the 98 zero-days in Ireland 2026, up from 73) could strengthen it as the venue of record or commoditise its bounties.
  - Its product lead is eroding on outside evidence. On a list of "AI-native automation leaders" it would not qualify; on a list that weights installed base plus a judge it is about #12–15.
- **Theori: technically top-tier, commercially unproven.** It is the only JP/KR/TW company with two independent, recent, competitive results in autonomous offence: AIxCC 3rd, and Pwn2Own 2026 2nd if team "Xint" is Theori's. The AIxCC cost data show capital efficiency. Watch list, not top 15, until revenue, funding and model access are evidenced.
- **No other company covered shows outside evidence of a global lead in automated security.** Korea's strength is talent (CTF results, AIxCC) more than companies; Japan's is incumbency (Trend Micro) and government demand; Taiwan's is a few small AI-SOC and threat-intelligence vendors.

### Gaps
- No Gartner, Forrester or IDC ranking for Trend Micro dated 2025–2026 was retrieved; the latest found is 2024.
- CyberInsider does not state the affiliation of the Pwn2Own team "Xint". The link to Theori rests only on the shared name, Theori's Xint.io brand.
- Theori's revenue, cash, valuation and AI-model suppliers were not found.
- DARPA's "eight DEF CON CTF finals" for Theori likely counts wins by members of combined teams (PPP, MMM). Not verified.

## 2. Company-by-company: business model, financials, independent evidence of lead, model access, cross-border exposure; quality tests and path forward

### Takeaway
- **Recurring revenue is common; independent evidence of an automation lead is rare.** Trend Micro, CyCraft, S2W and GMO's Takumi are largely subscription or usage-priced. SK Shieldus, LAC, CHT Security and DEVCORE are mostly labour, services or system integration.
- **Theori is the clearest move away from billable hours.** It is exiting consulting by end-2026 and is an AIxCC and Pwn2Own placer, but its funding is thin.
- **Trend Micro is investing heavily but under strain.** It is paying for AI and cloud (9-month cloud cost +57%) while margins fall. On 2026-11-12 it dropped its "Road to 2028" plan and moved to annual guidance only.
- **Gated frontier-model access is now a demonstrated country-level risk.** A US export directive of 2026-06-12 cut off all foreign access to Anthropic's Mythos-class models and disrupted Japanese government vulnerability scanning. A Korean telecom's inclusion on the access list was reportedly the trigger.

### Cited Findings

#### Trend Micro (TSE Prime: 4704; also trades OTC as TMICY/TMICF)
- **Q3 2026 results** (all from [Q3 2026 deck, 2026-11-12](https://www.trendmicro.com/content/dam/trendmicro/global/en/about/investor-relations/reports-presentation/2026/financial-2026-presentation-negi-q3.pdf)).
  - Quarter: net sales ¥75,317m (+9%; +3% constant currency); operating income ¥13,231m (−17%); ordinary income ¥12,698m (−30%); net income ¥8,609m (−32%).
  - Nine months: net sales ¥223,913m (+10%); operating income ¥35,023m (−21%; 16% margin); net income ¥23,839m (−12%).
- **ARR by region and brand.**
  - TrendAI ARR at Q3 2026, restated after the small-business product Worry-Free moved to TrendLife: Japan $215m (+2% YoY), Americas $275m (+4%), Europe $383m (+12%), AMEA $419m (+13%); total $1,292m (+8%). Source: [Q3 2026 deck](https://www.trendmicro.com/content/dam/trendmicro/global/en/about/investor-relations/reports-presentation/2026/financial-2026-presentation-negi-q3.pdf)
  - Q3 2026 brand sales: TrendAI ¥57,017m (+12%; +5% constant currency); TrendLife ¥18,237m (+1%); Incubation ¥61m. Source: [same](https://www.trendmicro.com/content/dam/trendmicro/global/en/about/investor-relations/reports-presentation/2026/financial-2026-presentation-negi-q3.pdf)
- **Costs, cash and headcount.**
  - Cloud cost: ¥10,327m in Q3 2026 against ¥6,935m in Q3 2025; ¥32,368m over nine months (+57%).
  - Operating cash flow: ¥6,164m in Q3 (−64%).
  - Balance sheet at Sep 2026: cash ¥204,301m; marketable securities ¥31,893m; deferred revenue ¥218,816m.
  - Headcount: 6,592 at Sep 2026, of which R&D 2,033 and APAC/MEA 3,443.
  - Source: [same](https://www.trendmicro.com/content/dam/trendmicro/global/en/about/investor-relations/reports-presentation/2026/financial-2026-presentation-negi-q3.pdf)
- **Strategy change, 2026-11-12.** Trend Micro "decided not to hold an IR Day in 2026 and to not extend the current Road to 2028 road map … reverting to annual guidance only." Source: [Q3 2026 deck](https://www.trendmicro.com/content/dam/trendmicro/global/en/about/investor-relations/reports-presentation/2026/financial-2026-presentation-negi-q3.pdf)
- **Q2 2026 (reported 2026-08-13).**
  - Operating income ¥6.2bn (−54%; 8% margin). Cloud cost rose from ¥6.8bn to ¥12.7bn.
  - FY2026 operating-income guidance cut by ¥12bn to ¥44.4bn (margin from 19% to 15%), blamed on cloud and AI-token costs. The original ¥56.4bn appears in the [Q1 2026 deck](https://www.trendmicro.com/content/dam/trendmicro/global/en/about/investor-relations/reports-presentation/2026/financial-2026-presentation-negi-q1.pdf).
  - Vision One ARR +49%, net retention 122%, 45% of TrendAI ARR [company claim, unconfirmed].
  - "Sovereign AI" in 12 countries [company claim, unconfirmed].
  - Holding cash after deferred revenue: ¥4.0bn.
  - Former 2028 target: operating margin of 25–27%.
  - VicOne (vehicle security) at 1.5m vehicles and 45 customers [company claim, unconfirmed].
  - Source: [Investing.com, 2026-08-13 (AI-assisted article)](https://www.investing.com/news/company-news/trend-micro-q2-2026-slides-ai-investment-drives-growth-pressures-margins-93CH-4857326)
- **Balance-sheet ratio.** Equity ratio 30.8% at 30 Sep 2026 (30.2% at end-2025); net assets ¥127,338m; total assets ¥397,986m. Source: [TipRanks, 2026-11-12](https://www.tipranks.com/news/company-announcements/trend-micro-reports-higher-nine-month-sales-and-lower-profit)
- **Buybacks.**
  - New programme approved 2026-11-12: up to 917,600 shares (0.70%) or ¥5bn, bought on the open market between 2026-11-13 and 2026-12-23. Source: [TipRanks, 2026-11-12](https://www.tipranks.com/news/company-announcements/trend-micro-announces-share-buyback-program)
  - Earlier purchases: 797,200 shares for ¥6,232m (Nov 2025); 525,300 shares for ¥3,767m (Dec 2025); 344,900 for ¥1,837m (Feb 2026); 595,500 for ¥3,162m (Mar 2026).
  - Share count: 140,901,604 issued; 11,109,268 held in treasury at 2026-06-30. Source: [Trend Micro stock information](https://www.trendmicro.com/en_us/about/investor-relations/stocks-bonds.html)
  - The February 2026 programme closed at 940,400 shares for ¥4,999.9m. Source: [MarketScreener](https://www.marketscreener.com/news/trend-micro-incorporated-s-equity-buyback-announced-on-february-18-2026-has-closed-with-940-400-sh-ce7e5edcde80f220)
- **Private-equity interest.**
  - Reuters reported on 2024-08-08 that Trend Micro was exploring a sale. On 2025-02-13 it reported that Advent, Bain, EQT and KKR had expressed interest. Source: [BankInfoSecurity, 2025-02-14](https://www.bankinfosecurity.com/blogs/private-equity-now-kicking-tires-on-trend-micro-p-3814); [The Star/Reuters, 2025-02-13](https://www.thestar.com.my/tech/tech-news/2025/02/13/exclusive-buyout-firms-vie-for-cybersecurity-firm-trend-micro-sources-say)
  - The shares hit the daily limit (+16%) on the report. Source: [Bloomberg Japan, 2025-02-13](https://www.bloomberg.com/jp/news/articles/2025-02-13/SRLM9QT0G1KW00)
  - No TOB or sale agreement was found in Japanese or English results. A personal blog says none had been disclosed as of July 2026. Source: [Hatena blog (low reliability)](https://worklife-carrer.hatenablog.com/entry/2025/06/07/094954)
  - Inference: the November 2026 buyback and the switch to annual guidance point to an independent company.
- **Corporate structure.**
  - Enterprise business rebranded TrendAI (March 2026); consumer business rebranded TrendLife (April 2026).
  - TXOne Networks was formed in November 2018 as a joint venture with Moxa. ZDI came with the TippingPoint purchase (2015, $300m).
  - Global R&D headquarters is in Taipei; Eva Chen is CEO.
  - Source: [Wikipedia, accessed 2026-11-12](https://en.wikipedia.org/wiki/Trend_Micro)
- **Capital allocation.** The CFO said investors favoured growth investment over dividends. Source: [Investing.com, 2026-08-13](https://www.investing.com/news/company-news/trend-micro-q2-2026-slides-ai-investment-drives-growth-pressures-margins-93CH-4857326)

#### Theori / Xint (private; Seoul and Austin)
- **Products.**
  - Xint Code became commercially available 2026-03-17. It is a large-language-model-native static analysis tool that orchestrates several AI models and checks each finding's exploitability. Theori says it analyses millions of lines in under 12 hours and found a PostgreSQL flaw that had gone undetected for more than 20 years [company claim, unconfirmed]. MongoDB is the only named customer. Source: [SiliconANGLE, 2026-03-17](https://siliconangle.com/2026/03/17/theori-launches-xint-code-ai-platform-uncover-hidden-vulnerabilities-massive-codebases/); [Help Net Security, 2026-03-18](https://www.helpnetsecurity.com/2026/03/18/theori-xint-code/)
  - A later Xint.io release lists DARPA, Samsung, LG Electronics and Hyundai as customers [company claim, unconfirmed]. Source: [Business Wire (search-result summary)](https://www.businesswire.com/news/home/20260317129537/en/Xint-Code-Demonstrates-Human-like-Discovery-and-Prioritization-of-Business-Logic-Vulnerabilities-Analyzing-Millions-of-Code-Lines-in-Just-Hours)
- **Strategy (CEO Park Se-joon, interview 2026-10-07).**
  - Xint, an autonomous penetration-testing platform, launched in October 2025; Xint Pulse (on-demand assessment) in July 2026.
  - Consulting stops as a stand-alone profit line at end-2026 and is sold only as an add-on. The paid training platform closes by year-end.
  - Automatic identification of exposed assets moves forward to end-2026; automated intrusion and lateral-movement checks follow in 2027.
  - Demand rose after the 2026 financial-sector hacks.
  - Park: "the era of humans doing the hacking is already nearing its end."
  - Source: [Seoul Economic Daily, 2026-10-08](https://en.sedaily.com/technology/2026/10/08/theori-drops-consulting-training-to-bet-all-on-ai-hacking)
- **Funding.** Aggregators disagree: $13m over five rounds ([CB Insights](https://www.cbinsights.com/company/theori/financials)); $15.4m ([PitchBook](https://pitchbook.com/profiles/company/500894-92); [SiliconANGLE](https://siliconangle.com/2026/03/17/theori-launches-xint-code-ai-platform-uncover-hidden-vulnerabilities-massive-codebases/)); $32.4m, latest a grant on 2025-08-11 ([Caplight](https://www.caplight.com/company/theori)). Valuation not public; no IPO plan announced ([Caplight, undated](https://www.caplight.com/company/theori)). Investors include Naver, Hana Bank and Dunamu & Partners ([SiliconANGLE](https://siliconangle.com/2026/03/17/theori-launches-xint-code-ai-platform-uncover-hidden-vulnerabilities-massive-codebases/)).

#### Samsung Research (Team Atlanta)
- Samsung Research was one of four members of Team Atlanta, the AIxCC winner ($4m). Source: [DARPA, 2025-07-08](https://www.darpa.mil/news/2025/ai-cyber-challenge-winners-def-con-33); [DARPA, 2025-08-08](https://www.darpa.mil/news/2025/aixcc-results)
- Samsung Electronics and SK hynix invested in Anthropic's Series H, and Samsung was reported as a likely Project Glasswing (Mythos-access) participant, not officially confirmed. Source: [Korea Times, 2026-06-03](https://www.koreatimes.co.kr/amp/business/tech-science/20260603/korea-joins-anthropics-project-glasswing-for-mytos-cybersecurity-ai-model)

#### GMO Flatt Security ("Takumi byGMO") and GMO Cybersecurity by Ierae (group of GMO Internet Group, TSE Prime: 9449)
- **What Takumi does.** AI-based static and dynamic scanning; automatic fixes as pull requests with unit tests; AI penetration testing; Takumi Guard (blocks malicious packages); Takumi Runner (CI/CD traces); an endpoint agent.
- **Pricing.** ¥70,000/month base plus usage credits (250 credits included; ¥280 per extra credit). Guard costs ¥500 per user above 15 users; the endpoint agent ¥1,000 per device per month.
- **Customers and data handling.** "More than 300 organizations" [company claim, unconfirmed], with Nikkei, freee, Sansan and WealthNavi logos. Data is processed mainly in Japan; LLM inference for diagnosis is excluded unless a paid option keeps it in Japan.
- Source for all three: [Takumi page, accessed 2026-11-12](https://flatt.tech/takumi)
- **Anthropic partnership.** GMO Internet Group signed a strategic partnership with Anthropic on 2026-07-10 (announced 2026-07-28). It covers applying Anthropic models to GMO's cyber-defence services, a group-wide Claude Enterprise rollout, and joint CTF events drawing on about 200 GMO white-hat hackers. Takumi "will be equipped with the latest AI". Mythos and Glasswing are not mentioned. Source: [GMO release, 2026-07-28](https://group.gmo/en/news/article/852/)
- **DEF CON 34.** Engineers from GMO Ierae and GMO Flatt Security were on undef1ned, part of Blue Water, which won the DEF CON 34 CTF (6–9 Aug 2026). GMO teams also placed 2nd (IoT Village), 3rd (Game Hacking), 4th (Blue Team and Hardware) and 9th (Cloud). Source: [innovatopia (Japanese), August 2026](https://innovatopia.jp/cyber-security/cyber-security-news/115623/)
  - Accounts of Blue Water's make-up differ. Tsinghua and Georgia Tech list perfect blue, Water Paddler, r00timentary, RedBud, BunkyoWesterns and undef1ned. Source: [Tsinghua (search-result summary)](https://www.tsinghua.edu.cn/info/1180/127762.htm); [Georgia Tech (search-result summary)](https://hg.gatech.edu/node/691834)
- **Own incident.** GMO disclosed unauthorised access to a service of a consolidated subsidiary (2026-10-23), then goodwill payments (2026-10-24) and compensation measures at GMO Internet, Inc. (2026-11-06). Source: [GMO notice, 2026-10-23](https://group.gmo/en/ir_news/article/690/); [GMO news list](https://group.gmo/en/news/)
- **Stake in FFRI.** GMO Internet Group bought 372,400 FFRI Security shares on the open market between 2026-08-17 and 2026-10-30, taking its holding to 752,400 shares (9.61% of voting rights). Stated purpose: "pure investment". Source: [GMO notice, 2026-11-02](https://ir.group.gmo/en/pdf/irlibrary/gmo_disclose_info20261102_02_e.pdf)
- **Parent metrics (2026-11-12).** GMO Internet Group: revenue (TTM) ¥301.48bn; operating margin 21.83%; net debt ¥50.27bn. Source: [StockAnalysis](https://stockanalysis.com/quote/tyo/9449/statistics/)

#### FFRI Security (TSE Growth: 3692)
- Revenue (TTM) ¥4.36bn; operating margin 29.46%; net margin 23.49%; net cash ¥3.33bn; free cash flow (TTM) ¥1.31bn (2026-11-12). Source: [StockAnalysis](https://stockanalysis.com/quote/tyo/3692/statistics/)
- GMO holds 9.61%, acquired by 2026-10-30, as a pure investment. Source: [GMO notice](https://ir.group.gmo/en/pdf/irlibrary/gmo_disclose_info20261102_02_e.pdf)

#### Other Japanese listed candidates (financials as of 2026-11-12, all from StockAnalysis)

| Company | Revenue (TTM) | Operating margin | Net cash | FCF (TTM) | Note |
|---|---|---|---|---|---|
| Cyber Security Cloud (TSE: 4493) | ¥5.44bn | 22.94% | ¥3.42bn | ¥913m | Shares fell 17.55% on 2026-11-12 ([source](https://stockanalysis.com/quote/tyo/4493/statistics/)) |
| Digital Arts (TSE: 2326) | ¥11.87bn | 46.84% | ¥27.49bn | ¥11.07bn | ([source](https://stockanalysis.com/quote/tyo/2326/statistics/)) |
| HENNGE (TSE: 4475) | ¥12.78bn | 17.52% | ¥7.72bn | ¥2.88bn | Shares fell 7.50% on 2026-11-12 ([source](https://stockanalysis.com/quote/tyo/4475/statistics/)) |
| Ubiquitous AI (TSE: 3858) | ¥3.82bn | −6.10% | ¥1.24bn | −¥146m | ([source](https://stockanalysis.com/quote/tyo/3858/statistics/)) |

- **Procurement concentration.**
  - Between FY2023 and FY2025, tracked Japanese agencies awarded 788 cybersecurity contracts worth ¥199.7bn. The Ministry of Defense accounted for 88.0% of the value.
  - The Fujitsu group was the largest winner at ¥47.2bn (23.7%).
  - Large contracts usually go to Japanese primes and integrators holding the Unified Qualification; foreign products enter through their proposals.
  - Source: [Japan Public Sector Brief (third-party guide; figures compiled by the publisher from public award records), c. Sept–Oct 2026](https://publicsector.edamamejapan.com/japan-active-cyber-defense-law/)

#### AhnLab (KOSDAQ: 053800)
- **Q3 2026** (preliminary, disclosed 2026-10-28; consolidated):
  - Revenue KRW 79.5bn (+23.1%); operating profit KRW 10.9bn (+38.7%); net profit KRW 7.6bn (−40.4%).
  - Nine months: revenue KRW 209.8bn (+14.0%); operating profit KRW 18.2bn (+47.3%).
  - Company says network security grew by triple digits, EDR and MDR demand rose, and global business grew by double digits [company claim, unconfirmed].
  - Source: [MTN (Korean), 2026-10-28](https://news.mtn.co.kr/article/2026102810354690595); [Asiae, 2026-10-28](https://view.asiae.co.kr/article/2026102809512349625); [Digital Economy News](https://www.denews.co.kr/news/articleView.html?idxno=42909)
- **Trailing metrics (2026-11-12).** Revenue (TTM) KRW 278.55bn; operating margin 12.95%; net cash KRW 298.01bn; FCF (TTM) KRW 56.71bn; 52-week share-price change +89.79%. Source: [StockAnalysis](https://stockanalysis.com/quote/kosdaq/053800/statistics/)

#### SK Shieldus (private; EQT about 68%, SK Square about 32% since 2023)
- **Ownership.** EQT Infrastructure paid about KRW 2tn for 68% in 2023; SK Square kept 32%. Source: [IPE Real Assets](https://realassets.ipe.com/news/eqt-to-buy-south-korean-security-operator-sk-shieldus/10065421.article); [Korea Herald, 2023-07-20](https://www.koreaherald.com/view.php?ud=20230720000611)
- **Sale exploration.**
  - On 2026-01-29 EQT was weighing a sale of control and shortlisting buyers; no adviser had been appointed. Cyber customers include the Ministry of National Defense and the National Intelligence Service. Leaks at Coupang and SK Telecom were cited as lifting demand. Source: [thebell (Korean), 2026-01-29](https://www.thebell.co.kr/front/newsview.asp?key=202601291517028320105956)
  - A "KRW 6tn" valuation was headlined. Source: [thebell, 2026-01-28](http://m.thebell.co.kr/m/newsview.asp?svccode=00&newskey=202601281420516080107858)
- **Possible separate sale of the cyber unit** (thebell, 2026-02-25; [source](https://m.thebell.co.kr/m/newsview.asp?newskey=202602251335152120102494)).
  - Information security is about 30% of revenue, implying a value of at least about KRW 1tn.
  - CyberCX's 2025 sale at 2.6x revenue is the cited reference point.
  - Total borrowings were KRW 2.4389tn at end-Q3 2025, against KRW 65.9bn at end-2024. Interest paid over the first nine months of 2025 was KRW 34.9bn.
  - Capex is about KRW 300bn a year.
  - EBITDA: KRW 341.8bn (2023); KRW 457.4bn (2024); over KRW 500bn (2025, industry estimate).
  - Revenue: KRW 1.8735tn (2023); KRW 2.0047tn (2024); KRW 1.5944tn for the first nine months of 2025 (+9%).
  - A search-result summary instead gave KRW 1.0452tn for 2023 and KRW 2.2013tn for 2025, with operating profit of KRW 136.5bn (2024) and KRW 111.5bn (2025). The 2023 figures conflict. Source: [Top Daily (search-result summary; not opened)](https://www.topdaily.kr/articles/109944)

#### S2W (KOSDAQ: 488280)
- **IPO (August 2025).** Retail subscription from 2025-08-07; price range KRW 11,400–13,200; 1.58m new shares; lead underwriter Daishin Securities.
- **Plan at IPO.** 2024 revenue KRW 9.6bn with an operating loss of KRW 4.5bn. Targets were KRW 23.9bn revenue and KRW 3.9bn operating profit for 2026 (break-even year), and KRW 39.5bn revenue for 2027.
- **Model and ownership.** SaaS about 96% of revenue; customer retention about 96%. It is an INTERPOL partner and "the only Korean company supplying data to Microsoft's Copilot for Security" [company claim, unconfirmed]. About ten domestic financial investors held more than 70% before listing.
- Source: [Bloter (Korean), 2025-08-05](https://www.bloter.net/news/articleView.html?idxno=641512)
- **H1 2026.** Revenue KRW 4.3bn; operating loss KRW 5.4bn; equity KRW 18.6bn. Source: [Chickstock (search-result summary)](https://www.chickstockfi.com/stocks/488280/reports/2026-half)
- **Trailing metrics (2026-11-12).** Revenue (TTM) KRW 10.24bn; operating margin −78.99%; net cash KRW 15.51bn; FCF (TTM) −KRW 6.75bn. Source: [StockAnalysis](https://stockanalysis.com/quote/kosdaq/488280/statistics/)

#### Other Korean listed candidates (financials as of 2026-11-12, all from StockAnalysis)

| Company | Revenue (TTM) | Operating margin | Net cash | FCF (TTM) | Note |
|---|---|---|---|---|---|
| Genians (263860) | KRW 52.52bn | 19.47% | KRW 36.27bn | KRW 2.27bn | Shares rose 21.04% on 2026-11-12 ([source](https://stockanalysis.com/quote/kosdaq/263860/statistics/)) |
| IGLOO Corporation (067920) | KRW 178.86bn | 7.33% | KRW 48.61bn | KRW 9.47bn | Net margin −0.20% ([source](https://stockanalysis.com/quote/kosdaq/067920/statistics/)) |
| WINS Technet (136540) | KRW 96.80bn | 19.49% | KRW 96.17bn | KRW 16.16bn | ([source](https://stockanalysis.com/quote/kosdaq/136540/statistics/)) |
| Raonsecure (042510) | KRW 60.56bn | 5.93% | KRW 19.31bn | KRW 4.87bn | ([source](https://stockanalysis.com/quote/kosdaq/042510/statistics/)) |
| FASOO AI, formerly Fasoo (150900) | KRW 49.68bn | 10.42% | KRW 8.06bn | KRW 7.23bn | ([source](https://stockanalysis.com/quote/kosdaq/150900/statistics/)) |

- Raon Secure white-hat hackers were core members of the 3rd- (SuperDiceCodeLovers) and 4th-placed (Cold Fusion) DEF CON 34 CTF teams, and appeared in the 7th (Jinddabi's). Source: [MTN, 2026-08-10](https://news.mtn.co.kr/news-detail/2026081011560011163)
- **Autocrypt (private).**
  - Its red team won the DEF CON 34 Car Hacking Village CTF (7–9 Aug 2026), 1st of 83 teams. It had placed 3rd in 2025.
  - It describes itself as "the only designated automotive cybersecurity Technical Service provider in Asia-Pacific" [company claim, unconfirmed].
  - Source: [TechNode Global/PR Newswire Asia, August 2026](https://technode.global/prnasia/autocrypt-wins-def-con-34-automotive-hacking-competition-ranking-first-among-83-teams/)

#### CyCraft Technology (Taiwan Innovation Board: 7823, "CyCraft-KY")
- **Listing.** Pre-listing auction 21–23 Jan 2026: 1,580 (thousand) shares; floor NT$70.31; provisional underwriting price NT$90. Source: [CyCraft, January 2026](https://www.cycraft.com/en/news/auction-20260120)
  - Listed 2026-02-05. Source: [CyCraft listing release (search-result summary; page now 404)](https://www.cycraft.com/en/news/taiwans-first-ai-cybersecurity-stock-en-20260205); [Dealroom](https://app.dealroom.co/news/feed/taiwanese-ai-cybersecurity-firm-cycraft-lists-on-taiwan-innovation-board-after-22-76-revenue-growth)
- **Company-reported figures** [company claims, unconfirmed] ([CyCraft, January 2026](https://www.cycraft.com/en/news/auction-20260120)):
  - 2025 revenue +23%; subscriptions 90% of revenue; retention above 90%; deferred revenue +42% YoY at Q3 2025; cash NT$519m; no debt.
  - More than 600,000 AI sensors deployed; more than 1,000 semiconductor-supply-chain vendors (SEMI E187 driven).
  - More than 10 IT-service alliances in Japan; domestic partners CHT Security and HONLYNN.
  - "Recognized seven times" by Gartner; "the only Taiwanese vendor to pass" MITRE ATT&CK evaluations three times.
  - New products: XecGuard (an LLM firewall, slated for H1 2026) and XecART (AI red-teaming).
  - Gross margin 95% per [Dealroom](https://app.dealroom.co/news/feed/taiwanese-ai-cybersecurity-firm-cycraft-lists-on-taiwan-innovation-board-after-22-76-revenue-growth) (company-sourced).
- **Trailing metrics (2026-11-12).** Revenue (TTM) TWD 383.25m; operating margin −11.31%; net cash TWD 649.68m; FCF (TTM) TWD 2.06m. Source: [StockAnalysis](https://stockanalysis.com/quote/tpe/7823/statistics/)

#### CHT Security (TPE: 7765; Chunghwa Telecom group)
- Revenue (TTM) TWD 2.32bn; operating margin 23.96%; ROE 23.85%; net cash TWD 792.11m; FCF (TTM) TWD 532.99m (2026-11-12). Source: [StockAnalysis](https://stockanalysis.com/quote/tpe/7765/statistics/)
- Named by CyCraft as a domestic partner "(Chunghwa Telecom)". Source: [CyCraft](https://www.cycraft.com/en/news/auction-20260120)

#### TeamT5, DEVCORE (both private, Taiwan)
- **TeamT5.** A threat-intelligence firm focused on Asia-Pacific espionage groups. Products: ThreatVision, ThreatSonar, ThreatSonar Plus and ThreatSonar Anti-Ransomware. Serves "500+ organizations" [company claim, unconfirmed]. Japanese channel partners include Macnica and CTC. Awards: Taiwan Excellence Award 2026 and Computex Best Choice 2024. Funding and listing status are not on its site. Source: [TeamT5, accessed 2026-11-12](https://teamt5.org/en/)
- **DEVCORE.** Services: red team, product security research, penetration testing, consulting and training. Reports "400+ vulnerability disclosures" and "50+ bug bounty program reports" [company claim, unconfirmed]. Researcher Angelboy ranked #33 on Microsoft's MSRC 2024 Most Valuable Security Researchers list (as reported by DEVCORE). No product, funding or listing information. Source: [DEVCORE, accessed 2026-11-12](https://devco.re/en/)

#### Gorilla Technology (Nasdaq: GRRR; Taiwan-origin)
- Revenue (TTM) $140.40m; gross margin 17.29%; operating margin −27.58%; net cash $105.38m; FCF (TTM) −$34.91m; short interest 21.70% of shares outstanding (2026-11-12). Source: [StockAnalysis](https://stockanalysis.com/stocks/grrr/statistics/)
- Gorilla's IR site could not be reached (DNS blocked in this session).

#### Frontier-model access and cross-border exposure (all three countries)
- **Glasswing expansion.** On 2026-06-02 Anthropic expanded Project Glasswing (Mythos access) by about 150 institutions in more than 15 countries. Korean participants were reported to include Samsung Electronics, SK hynix and SK Telecom, and KISA was eligible. Korea had already decided to join OpenAI's cybersecurity consortium (GTAC). Anthropic said several AI companies would have Mythos-level models "within 6∼12 months". Source: [Kyunghyang Shinmun (English), 2026-06-03](https://www.khan.co.kr/en/article/202606031446037/)
- **Korean confirmation.** An MSIT official said KISA "has joined Project Glasswing and secured access to the Mythos model". Corporate participation was not officially confirmed. Source: [Korea Times, 2026-06-03](https://www.koreatimes.co.kr/amp/business/tech-science/20260603/korea-joins-anthropics-project-glasswing-for-mytos-cybersecurity-ai-model)
- **The cut-off and its trigger.**
  - Anthropic suspended all foreign access to "Fable 5" and "Mythos 5" after US export controls (about 2026-06-12).
  - The Washington Post (2026-06-15) said the White House moved after finding a Korean telecom "suspected of having ties to China" on an expanded access list. An initial list of 111 organisations had already been approved.
  - Source: [Korea JoongAng Daily, 2026-06-16](https://www.koreajoongangdaily.com/business/white-house-officials-pin-anthropic-ai-export-block-on-korean-telecom-report/12726842)
- **SK Telecom.** WIRED (2026-06-17) named SK Telecom. Its Mythos access was revoked; SK Telecom denies China ties. Anthropic opened a Seoul office on 2026-06-17; its first Asian office is in Tokyo. Source: [Joho no Todai, 2026-06-18](https://joho-todai.com/en/mythos-export-restrictions-sk-telecom/)
- **Directive detail and Japan impact.**
  - The BIS directive (2026-06-12) applied to all foreign nationals worldwide. Fable 5 was restored globally on 2026-06-30; Mythos 5 was "partially reinstated for certain approved U.S. organizations".
  - Japan's National Cyber Director, Yoichi Iida, said the directive "affected security vulnerability scanning operations for key government systems" and that "Japan should not rely on any one particular AI model". This came from a Kyodo interview published 2026-08-10.
  - Source: [TechTimes, 2026-08-10](https://www.techtimes.com/articles/323705/20260810/japans-cyber-chief-confirms-us-ai-export-ban-hit-government-security-scanning.htm)

### Inferences
Quality tests (a–e) and path forward per company. Tests concern business position only; entry points are in Section 4.

**Trend Micro**
- **(a) Position: medium.**
  - Owns the strongest judge in the region (ZDI/Pwn2Own): vendor-recognised and final at the event, though human-run.
  - Owns no verification tool, and its products sit where platform vendors and AI-native rivals are taking share.
  - No evidence of access to gated frontier models; it relies on "sovereign AI" deployments [company claim].
- **(b) Lead: eroding.** Gartner EPP 5th and Forrester cloud workload security 6th (2024); IDC CNAPP share growing at about a third of the market rate.
- **(c) Revenue model: strong.** Mostly subscription. TrendAI ARR $1.29bn; deferred revenue ¥218.8bn against about ¥301.5bn of FY2026 sales.
- **(d) Financial strength: solid but weakening.**
  - No debt and cash of about ¥204bn, but that cash is roughly matched by deferred revenue (Q2 holding cash after deferred revenue was only ¥4.0bn).
  - Operating margin is falling from 23% (Q3 2025) to 18% (Q3 2026); FY2026 is guided at 15%.
  - Q3 operating cash flow fell 64%.
  - Revenue is spread geographically: Japan 29%, APAC/MEA 29%, Europe 23%, Americas 19% of Q3 2026 sales (calculated from the deck's regional figures).
- **(e) Resilience: medium.**
  - Steady scenario (55%): AI token and cloud costs, 13.7% of Q3 sales, keep pressing on margins.
  - 2028 financing pause (25%): cheaper compute would help margins, and demand is regulation-led (Japan's Active Cyber Defense law), so relatively defensive.
  - Acceleration (20%): share loss to model makers' security products and US-gated tools.
  - Cycle position: mature.
  - Cross-border exposure: R&D is centred in Taipei and 52% of headcount is in APAC/MEA. China exposure is unverified.
- **Path forward.**
  - (1) Human-bounty ZDI could automate. No evidence of an AI-driven ZDI; the advisory count runs into the hundreds (ZDI-26-953).
  - (2) Vision One agentic detection and response. Done: AI and cloud spend +57% over nine months; Vision One ARR +49% [company].
  - (3) TXOne and VicOne shield devices that cannot be patched. Incubation revenue is tiny at ¥61m in Q3.
  - (4) Frontier-model dependence. Hedged by "sovereign AI"; no Mythos-class access evidenced.
  - (5) Regulation (JC-STAR, the Active Cyber Defense law's Article 42 supplier duties, vehicle rules via VicOne).
  - (6) Verified-when-written software: none.
  - Said versus done: the 2028 margin target of 25–27% was effectively abandoned on 2026-11-12, when the company stopped extending its roadmap.
  - Funded: yes. Timing: margin recovery is not plausible on the original 2028 schedule.
  - Must go right: cost-to-serve falls; Vision One cross-sell outruns the decline of legacy products; ZDI stays the venue of record.
  - **Verdict: partly coherent.** Spending matches the strategy, but the financial targets were withdrawn.

**Theori**
- **(a) Position: strong but dependent.** It builds automation that finds and validates flaws at machine speed, the strongest class in the brief. It owns neither a judge nor a model; Xint Code orchestrates third-party LLMs.
- **(b) Lead: high on independent technical evidence.** AIxCC 3rd with the best cost per point among the top three; Pwn2Own 2026 2nd if team "Xint" is Theori's; MMM members won DEF CON CTF 2022–2025; IDC Innovator 2026. Commercial evidence is unconfirmed.
- **(c) Revenue model: in transition** from labour (consulting, training) to platform; pricing undisclosed.
- **(d) Financial strength: unknown and likely thin.** About $15.4m raised; the last disclosed priced round was June 2022; plus the $1.5m AIxCC prize; 92 staff.
- **(e) Resilience: fragile.**
  - Steady scenario: demand rises after the Korean bank hacks.
  - Pause: funding risk, worsened by giving up consulting cash flow.
  - Acceleration: model makers' own security agents (Claude Security, OpenAI GTAC) compete head-on, and Mythos-class access for non-US entities was curtailed from June 2026. Whether Theori's US arm qualifies is unknown.
- **Path forward.**
  - Transitions (1), (2) and (4) apply.
  - Done: exiting consulting by end-2026; Xint launched (October 2025); Xint Code (March 2026); Xint Pulse (July 2026); competitive results.
  - Said: exposed-asset discovery by end-2026; lateral-movement checks in 2027.
  - Funded: not evidenced.
  - Must go right: a new funding round or revenue scale, durable access to frontier models, and differentiation from model makers' tools.
  - **Verdict: partly coherent, leaning coherent.** Strategy and execution line up; funding and model access are unproven.

**GMO Flatt Security / GMO Ierae (Takumi)**
- **(a) Position: medium.** AI-based scanning plus automatic-fix pull requests, sold with usage pricing on top of Anthropic models through the parent's partnership. No judge; no Mythos access disclosed.
- **(b) Lead.** Outside evidence covers talent only: DEF CON 34 CTF winning team and village CTF placings. "300+ organizations" is a company claim. No analyst rankings found.
- **(c) Revenue model: recurring and usage-scaled** (base fee plus credits).
- **(d) Financial strength: segment not disclosed.** The parent is diversified with modest net debt. A breach at a GMO subsidiary in October 2026 hurts the brand.
- **(e) Resilience.** Steady scenario: Japanese demand from the Active Cyber Defense law. Acceleration: Takumi could be reduced to a reseller layer over model-maker capability.
- **Path forward.**
  - Transitions (1), (2) and (4) apply.
  - Done: product shipped with pricing; Anthropic agreement; 9.61% stake in FFRI (financial, not strategic).
  - **Verdict: coherent at small scale.** Materiality to GMO cannot be assessed.

**AhnLab**
- **(a) Position: weak to medium.** Incumbent domestic endpoint and network vendor; no judge; no frontier-model evidence.
- **(b) Lead.** No outside rankings retrieved.
- **(c) Revenue model.** Product, maintenance and services mix not verified.
- **(d) Financial strength: good.** Net cash KRW 298bn; operating margin about 13%; Q3 operating profit +38.7%. Revenue is mostly Korean, with heavy exposure to domestic government and finance (inference).
- **(e) Resilience.** Breach-driven Korean budgets support the steady scenario. Acceleration risks commoditising antivirus and endpoint products.
- **Path forward.** Transition (2) partly applies (EDR/MDR growth) [company]. **Verdict: partly coherent.**

**SK Shieldus**
- **(a) Position: weak.** Labour, physical security and system integration; about 30% cyber.
- **(b) Lead.** Domestic Tier-1 public-sector customers.
- **(c) Revenue model.** Mostly labour and recurring service contracts.
- **(d) Financial strength: stretched.** KRW 2.44tn of debt; about KRW 300bn a year of capex.
- **(e) Resilience.** Korea-only, but helped by post-breach demand.
- **Path forward.** No automation evidence found. **Verdict: not coherent / cannot assess.** The 2026 sale or separation process dominates.

**CyCraft**
- **(a) Position: medium-small.** AI-driven managed detection and response, an LLM firewall and AI red-teaming; no judge.
- **(b) Lead.** Gartner and MITRE claims [unconfirmed].
- **(c) Revenue model: 90% subscription** [company].
- **(d) Financial strength.** Loss-making on a trailing basis, but with net cash of about TWD 650m.
- **(e) Resilience.** Concentrated in Taiwan and Japan, and exposed to geopolitics.
- **Path forward.** Transitions (2) and (4) apply. **Verdict: partly coherent.**

**S2W**
- **(a)/(c)** Threat-intelligence SaaS (96% of revenue) [company].
- **(d)** Losses widened in H1 2026, far below IPO targets. Net cash of KRW 15.5bn against about −KRW 6.8bn a year of FCF implies roughly two years of runway (inference).
- **Verdict: partly coherent, under-delivering.**

**FFRI and the other Japanese small caps**
- High margins (FFRI 29%, Cyber Security Cloud 23%, Digital Arts 47%).
- No outside evidence of an automation lead was retrieved. Business details were not re-verified in this pass (search budget).
- **Verdict: cannot assess.**

**CHT Security, DEVCORE, TeamT5, Autocrypt**
- CHT Security and DEVCORE are mostly labour and services (transition (1) not evidenced).
- TeamT5 is threat-intelligence software.
- Autocrypt is the main regional case for transition (5): device-maker liability, through its claimed automotive Technical Service designation.
- **Verdicts: cannot assess.**

### Gaps
- **Trend Micro.** Major shareholders and its percentage stake in TXOne; China operations, any China job cuts, and US-government concerns; 2025–2026 analyst rankings; whether it has any Mythos-class access.
- **Theori.** Revenue, cash, valuation, AI-model suppliers, and confirmation that team "Xint" at Pwn2Own is Theori staff.
- **Japanese companies.**
  - LAC (TSE: 3857): no data (StockAnalysis 404; Kabutan, Minkabu and Yahoo blocked or empty); KDDI shareholding not verified.
  - NRI Secure, NEC, Fujitsu, NTT Data and Hitachi security units: not researched beyond Fujitsu's procurement share.
  - FFRI's government/defense dependence; Cyber Security Cloud's and HENNGE's latest results (the cause of their 2026-11-12 share drops is unknown).
- **Korean companies.** Penta Security, Monitorapp, FESCARO, Findthegap and Sparrow (Fasoo's application-security affiliate) not researched. SK Shieldus's sale status after 2026-02-25 not verified.
- **Taiwanese companies.** Onward Security's ownership and status; TeamT5's and DEVCORE's funding and IPO plans.
- **Domestic models.** No evidence found that any covered company uses LG Exaone, Naver HyperCLOVA X, Samsung Gauss or a Japanese national model.

## 3. Regulation and demand drivers

### Takeaway
- **Japan.** Its Active Cyber Defense law took main effect on 2026-10-01 with incident and asset reporting for 258 critical-infrastructure operators. Communications-data and "neutralisation" powers follow in 2027. Procurement flows mostly through Japanese primes (Fujitsu won 23.7% of tracked cyber contracts by value, FY2023–25), so demand favours domestic integrators.
- **Korea.** A string of breaches (SK Telecom in 2025, Coupang, and AI-assisted bank hacks from late September 2026) is lifting telecom and bank security budgets.
- **Taiwan.** Its Cyber Security Management Act was amended on 2025-09-24, restricting "products harmful to national cyber security" and fining unreported incidents up to NT$10m.
- **Frontier-model gating.** The US export directive of June 2026 is now a regulatory demand driver of its own. Japan's cyber director explicitly calls for not relying on one model.

### Cited Findings
- **Japan: the Active Cyber Defense law and the national office.**
  - Formal name: Act on the Prevention of Damage from Unauthorized Acts against Important Computers (Act No. 42 of 2025). Promulgated 2025-05-23.
  - The National Cybersecurity Office replaced NISC on 2025-07-01. The Cabinet adopted the basic policy on 2025-12-23.
  - Source: [Japan Public Sector Brief](https://publicsector.edamamejapan.com/japan-active-cyber-defense-law/)
- **Japan: phased effective dates** (Source: [Japan Public Sector Brief](https://publicsector.edamamejapan.com/japan-active-cyber-defense-law/)).

  | Provision | Effective |
  |---|---|
  | Chapters 2, 8 and 9: asset notices, incident reports, threat-sharing council | 2026-10-01 |
  | Chapters 3–7: communications-information analysis | Within 2.5 years of promulgation (about November 2027) |
  | Companion act: access to and neutralisation of attack servers | Autumn 2027, per a September 2026 government briefing |

- **Japan: duties now in force.**
  - Coverage: 258 designated operators in 15 sectors.
  - Incident reports: a first report promptly and a full report within 30 days.
  - Asset notices for computers already in use on 2026-10-01: within six months (by March 2027).
  - Article 42 lets ministers request preventive measures from suppliers, including foreign suppliers.
  - About 100 organisations joined the threat-sharing council on 2026-10-01.
  - Source: [Japan Public Sector Brief](https://publicsector.edamamejapan.com/japan-active-cyber-defense-law/)
- **Japan: other accounts of the law.**
  - Baker McKenzie gives the enactment date as 2025-05-16 and says the law "will take full effect by 2027". It lists IT vendors and manufacturers of embedded programs used in critical systems among those covered. Source: [Baker McKenzie](https://connectontech.bakermckenzie.com/japans-new-active-cyber-defense-law-impact-on-businesses/)
  - The Diet passed the law on 2025-05-16, and Takaichi's cabinet adopted an implementation framework in March 2026. That is a different date from the 2025-12-23 basic policy and may be a different document. Source: [TechTimes, 2026-08-10](https://www.techtimes.com/articles/323705/20260810/japans-cyber-chief-confirms-us-ai-export-ban-hit-government-security-scanning.htm)
  - "Goes live October 1 … Report Promptly, Detail in 30 Days". Source: [Simplico, 2026-09-24](https://www.simplico.net/2026/09/24/active-cyber-defense-law-soc-incident-reporting/)
- **Japan: JC-STAR IoT labelling** (Source: [IPA, accessed 2026-11-12](https://www.ipa.go.jp/en/security/jc-star/index.html)).
  - Scheme released 2024-09-30; STAR-1 self-declarations accepted from 2025-03-25.
  - STAR-3 and STAR-4 (for government and critical infrastructure) require third-party evaluation and IPA certification. STAR-3 requirements for network devices and cameras were published in July and September 2026.
  - Mutual recognition with the UK's PSTI regime (from 2026-04-01) and Singapore's labelling scheme (from 2026-06-01).
- **Japan: AI budget and frontier-model gating.**
  - The National Cybersecurity Office has requested FY2027 funding for an AI-supported cyber response project (amount not given). Source: [Japan Public Sector Brief](https://publicsector.edamamejapan.com/japan-active-cyber-defense-law/)
  - The June 2026 US directive disrupted government vulnerability scanning; Japan's cyber director says Japan "should not rely on any one particular AI model". Source: [TechTimes, 2026-08-10](https://www.techtimes.com/articles/323705/20260810/japans-cyber-chief-confirms-us-ai-export-ban-hit-government-security-scanning.htm)
- **Korea: telecom security spending.**
  - The three carriers spent KRW 367.5bn on security in 2025 (+22% from KRW 301.2bn), about 7% of IT investment against 5.8% the year before.
  - SK Telecom alone rose from KRW 65.2bn to KRW 111.1bn and pledged about KRW 700bn over five years.
  - KT spent KRW 127.6bn; LG Uplus KRW 96.6bn.
  - The data come from KISA. Source: [Korea Times, 2026-07-13](https://www.koreatimes.co.kr/business/tech-science/20260713/telecoms-step-up-cybersecurity-spending-after-breaches)
- **Korea: AI-assisted bank hacks (October 2026).**
  - Shinhan said on 2026-10-01 that data on about 25,000 customers leaked. Shinhan, Hana and KB reported leaks in October 2026.
  - The Financial Supervisory Service found suspect IP addresses in 12 countries.
  - KB plans a 2027 security budget above KRW 100bn (KRW 86.1bn in 2026); Shinhan a record budget; Hana "tens of billions of won".
  - Korea launched a task force against AI-powered attacks, with a national strategy due by early 2027 (from a related-article teaser).
  - Source: [Korea JoongAng Daily, 2026-10-11](https://www.koreajoongangdaily.com/business/banks-boost-defenses-after-ailinked-hacks/12913975)
  - President Lee said AI appears to have been used. Source: [Japan Times, 2026-10-06 (headline; paywalled)](https://www.japantimes.co.jp/business/2026/10/06/south-korea-bank-hacks/)
  - The Financial Services Commission ordered firms to inspect every internet-facing system. Source: [American Banker (search-result summary)](https://www.americanbanker.com/news/ai-linked-hacks-hit-korean-banks-through-loan-agent-sites)
  - CrowdStrike reportedly tied the attacks to a China-based actor using an open-source AI penetration-testing agent alongside Claude Code. Source: [Shattered.io (secondary blog, low reliability)](https://shattered.io/crowdstrike-artex-ai-agent-korea-bank-hack-2026/)
- **Korea: other measures and signals.**
  - After Anthropic's Mythos preview, the Financial Supervisory Service urgently convened bank security staff in April 2026. Source: [FN News, 2026-04-13 (search-result summary)](https://en.fnnews.com/news/202604131822093743)
  - The Foreign Ministry's cyber budget rises from KRW 3.8bn to KRW 15.5bn after a hack at the Korea National Diplomatic Academy. Source: [FN News, 2026-09-01 (search-result summary)](https://en.fnnews.com/news/202609011319080930)
  - Coupang and SK Telecom leaks were cited as lifting cybersecurity demand. Source: [thebell, 2026-01-29](https://www.thebell.co.kr/front/newsview.asp?key=202601291517028320105956)
  - KISA's head called the DEF CON 34 CTF result a sign of how far Korea's capability has grown. Source: [MTN, 2026-08-10](https://news.mtn.co.kr/news-detail/2026081011560011163)
- **Taiwan: Cyber Security Management Act** (latest amendment 2025-09-24; Source: [Laws & Regulations Database of the ROC](https://law.moj.gov.tw/ENG/LawClass/LawAll.aspx?pcode=A0030297)).
  - The Ministry of Digital Affairs is the competent authority.
  - Government agencies may not use "products harmful to national cyber security" (Art. 11). Use by specific non-government agencies can be restricted (Art. 27).
  - Fines: failing to report an incident, NT$300,000–10,000,000 (Art. 29); breaching maintenance-plan or reporting duties after a correction order, NT$100,000–5,000,000 (Art. 30).
  - Critical-infrastructure providers must keep dedicated security staff and plans, and submit to audits (Art. 20 onward).
  - The database does not say which of these provisions the 2025 amendment added.
- **Taiwan: demand signals** [company claim]. CyCraft cites SEMI E187 adoption across more than 1,000 semiconductor-supply-chain vendors. Source: [CyCraft](https://www.cycraft.com/en/news/auction-20260120)

### Inferences
- **Japan.** The Active Cyber Defense law is mainly reporting and coordination now (2026), with operational powers from 2027. It boosts demand for monitoring, asset inventory and incident-response services, which favours domestic integrators (Fujitsu, NEC, NTT Data, LAC) and vendors that partner with them. Article 42 reaches foreign suppliers directly, which adds compliance cost for foreign software in critical systems.
- **Korea.** Breach-driven budget growth is large and recent: carriers +22% in 2025; KB's 2027 budget up more than 16%. It most directly helps domestic incumbents (AhnLab's Q3 revenue +23%, SK Shieldus) and AI-penetration-testing demand (Theori says financial-sector demand rose).
- **Taiwan.** The "products harmful to national cyber security" provisions favour domestic and allied vendors in government and critical-infrastructure procurement (CHT Security, CyCraft, TeamT5).
- **All three.** Frontier-model gating (June 2026) means the strongest automated tools may be available to US organisations first. That is a structural handicap for Japanese, Korean and Taiwanese vendors that depend on those models, and a policy push toward multi-model or domestic-model strategies.

### Gaps
- **Korea.**
  - ISMS-P and IoT-certification rule changes after the 2025–2026 breaches: not retrieved.
  - PIPC fines on SK Telecom (amount and date): not verified.
  - The KT femtocell and Lotte Card breaches: not verified. Korea Times mentions only "last year's security incidents" at KT.
- **Taiwan.** AI-security policy (an AI Basic Act and its status) not verified; which provisions the 2025 Cyber Security Management Act amendment added not confirmed.
- **Japan.** The exact Cabinet Order dates for Chapters 3–7 and the companion act's effective date need checking against official Cabinet Secretariat or National Cybersecurity Office notices; current figures come from third-party guides. JC-STAR's count of labelled products not retrieved.
- **Japan and GTAC.** That Japan also joined OpenAI's GTAC, and that the Japanese government or banks gained Mythos access, appeared only in search-result summaries. Unverified.

## 4. Valuation and entry points (kept separate from quality)

### Takeaway
- **Trend Micro.** On EV-based multiples it trades at or below the bottom of its five-year range: EV/Sales 2.18x, EV/EBITDA 8.2x, EV/FCF 9.9x. That is about half the EV/Sales of mature peers such as Check Point and Gen Digital. On earnings it is not cheap: forward P/E is about 26x against Check Point's 13.6x and Gen's 9.8x, and its "net cash" is largely customer prepayments. Suggested label: **fair**.
- **AhnLab.** Re-rated +90% in a year to EV/EBITDA 16.6x (upper half of its own range): **fair**.
- **Others.** FFRI (EV/Sales 12x), HENNGE and S2W look stretched. WINS, Fasoo AI and Digital Arts look cheap on multiples but are not core automated-security positions. Private names (Theori, SK Shieldus, Autocrypt, TeamT5, DEVCORE) cannot be assessed.

### Cited Findings

**Listed companies, 2026-11-12 close unless stated (all from StockAnalysis statistics pages)**

| Company | Price | Market cap | EV | EV/Sales | EV/EBITDA | EV/FCF | P/E trailing / forward | 52-week change |
|---|---|---|---|---|---|---|---|---|
| Trend Micro (4704) ([source](https://stockanalysis.com/quote/tyo/4704/statistics/)) | ¥6,660 | ¥864.42bn | ¥633.21bn | 2.18x | 8.16x | 9.94x | 24.67 / 26.45 | −15.42% |
| FFRI Security (3692) ([source](https://stockanalysis.com/quote/tyo/3692/statistics/)) | ¥7,190 | ¥56.87bn | ¥53.54bn | 12.23x | 37.45x | 40.66x | 55.54 / n/a | −29.51% |
| Cyber Security Cloud (4493) ([source](https://stockanalysis.com/quote/tyo/4493/statistics/)) | ¥2,185 | ¥22.07bn | ¥18.65bn | 4.17x | 16.39x | 24.85x | 23.48 / n/a | +15.30% |
| Digital Arts (2326) ([source](https://stockanalysis.com/quote/tyo/2326/statistics/)) | ¥5,300 | ¥71.15bn | ¥43.66bn | 3.68x | 6.59x | 3.94x | 18.37 / 16.33 | −27.99% |
| HENNGE (4475) ([source](https://stockanalysis.com/quote/tyo/4475/statistics/)) | ¥2,391 | ¥77.17bn | ¥69.22bn | 5.53x | 29.53x | 24.57x | 41.95 / n/a | +74.65% |
| Ubiquitous AI (3858) ([source](https://stockanalysis.com/quote/tyo/3858/statistics/)) | ¥412 | ¥4.31bn | ¥3.07bn | 0.80x | n/a | n/a | n/a (loss) | −2.60% |
| GMO Internet Group (9449) ([source](https://stockanalysis.com/quote/tyo/9449/statistics/)) | ¥3,153 | ¥295.72bn | ¥497.31bn | 1.65x | 5.65x | n/a | 17.93 / 13.16 | −8.71% |
| AhnLab (053800) ([source](https://stockanalysis.com/quote/kosdaq/053800/statistics/)) | KRW 115,200 | KRW 1.04tn | KRW 738.46bn | 2.71x | 16.59x | 13.32x | 21.35 / n/a | +89.79% |
| Genians (263860) ([source](https://stockanalysis.com/quote/kosdaq/263860/statistics/)) | KRW 31,350 | KRW 272.08bn | KRW 235.81bn | 3.59x | 18.15x | 82.90x | 26.51 / 17.19 | +51.08% |
| S2W (488280) ([source](https://stockanalysis.com/quote/kosdaq/488280/statistics/)) | KRW 9,470 | KRW 102.52bn | KRW 87.01bn | 8.50x | n/a | n/a | n/a (loss) | −58.56% |
| IGLOO (067920) ([source](https://stockanalysis.com/quote/kosdaq/067920/statistics/)) | KRW 6,410 | KRW 60.57bn | KRW 78.09bn | 0.42x | n/a | 7.91x | n/a | +18.27% |
| WINS Technet (136540) ([source](https://stockanalysis.com/quote/kosdaq/136540/statistics/)) | KRW 11,880 | KRW 124.94bn | KRW 29.13bn | 0.30x | 1.33x | 1.80x | 6.95 / n/a | −0.25% |
| Raonsecure (042510) ([source](https://stockanalysis.com/quote/kosdaq/042510/statistics/)) | KRW 14,570 | KRW 157.44bn | KRW 138.41bn | 2.29x | 19.42x | 28.41x | 35.33 / 26.66 | +49.44% |
| FASOO AI (150900) ([source](https://stockanalysis.com/quote/kosdaq/150900/statistics/)) | KRW 4,910 | KRW 55.50bn | KRW 49.48bn | 0.97x | 5.12x | 6.69x | 10.17 / n/a | +6.74% |
| CHT Security (7765) ([source](https://stockanalysis.com/quote/tpe/7765/statistics/)) | TWD 245 | TWD 9.97bn | TWD 9.17bn | 3.95x | 14.53x | 17.21x | 21.02 / 17.29 | −11.39% |
| CyCraft (7823), close 2026-11-11 ([source](https://stockanalysis.com/quote/tpe/7823/statistics/)) | TWD 77 | TWD 2.53bn | TWD 1.88bn | 4.90x | n/a | 912.61x | n/a (loss) | n/a |
| Gorilla Technology (GRRR), close 2026-11-11 ([source](https://stockanalysis.com/stocks/grrr/statistics/)) | $8.37 | $230.25m | $124.88m | 0.89x | n/a | n/a | n/a (loss) | −41.83% |

**Other quoted figures**
- **Trend Micro.** Net cash ¥231.36bn; FCF (TTM) ¥63.85bn; EBITDA ¥78.24bn; dividend yield 2.78%; ROE 29.98%. Consensus price target ¥6,537.50 ("Hold"). Source: [StockAnalysis](https://stockanalysis.com/quote/tyo/4704/statistics/). TipRanks shows a ¥6,000 target ("Hold"). Source: [TipRanks](https://www.tipranks.com/news/company-announcements/trend-micro-announces-share-buyback-program)
- **WINS** dividend yield 6.73%; **CHT Security** 3.95%; **IGLOO** 3.28%. Source: StockAnalysis pages linked in the table above.
- **Gorilla.** Average analyst target $32.83 from five analysts ("Strong Buy"); short interest 21.70%. Source: [StockAnalysis](https://stockanalysis.com/stocks/grrr/statistics/)

**Own five-year history (fiscal year-end values, StockAnalysis)**

| Year-end | Trend Micro EV/Sales | Trend Micro EV/EBITDA | Trend Micro EV/FCF | Trend Micro P/E | AhnLab EV/Sales | AhnLab EV/EBITDA | AhnLab P/E |
|---|---|---|---|---|---|---|---|
| FY2021 | 3.43 | 10.11 | 12.28 | 23.25 | 3.50 | 23.19 | 20.37 |
| FY2022 | 2.71 | 10.74 | 10.93 | 28.62 | 1.73 | 11.40 | 40.89 |
| FY2023 | 3.00 | 12.23 | 13.53 | 95.29 | 1.96 | 13.51 | 16.70 |
| FY2024 | 3.40 | 12.03 | 20.35 | 32.71 | 1.77 | 12.02 | 19.26 |
| FY2025 | 2.26 | 7.34 | 9.81 | 24.59 | 1.12 | 6.97 | 10.57 |

Sources: [Trend Micro ratios](https://stockanalysis.com/quote/tyo/4704/financials/ratios/); [AhnLab ratios](https://stockanalysis.com/quote/kosdaq/053800/financials/ratios/)

**Global peers (StockAnalysis, close 2026-11-11)**

| Peer | EV/Sales | EV/EBITDA | EV/FCF | P/E trailing / forward | Other |
|---|---|---|---|---|---|
| Check Point ([source](https://stockanalysis.com/stocks/chkp/statistics/)) | 4.65x | 15.71x | 11.38x | 17.55 / 13.64 | Operating margin 28.3% |
| Gen Digital ([source](https://stockanalysis.com/stocks/gen/statistics/)) | 4.92x | 10.30x | 14.57x | 15.48 / 9.81 | |
| Tenable ([source](https://stockanalysis.com/stocks/tenb/statistics/)) | 4.53x | 86.11x | 17.23x | n/a / 18.15 | |
| SentinelOne ([source](https://stockanalysis.com/stocks/s/statistics/)) | 6.94x | n/a | 134.81x | n/a / 60.01 | Operating margin −26% |

**Private companies and IPO reference points**
- **Theori.** No disclosed valuation; about $15.4m raised; no IPO plan announced. Source: [SiliconANGLE](https://siliconangle.com/2026/03/17/theori-launches-xint-code-ai-platform-uncover-hidden-vulnerabilities-massive-codebases/); [Caplight](https://www.caplight.com/company/theori)
- **SK Shieldus.** EQT reportedly seeks up to KRW 6tn for the whole company; the cyber unit is estimated at ≥KRW 1tn on CyberCX's 2.6x-revenue multiple. Source: [thebell, 2026-01-28](http://m.thebell.co.kr/m/newsview.asp?svccode=00&newskey=202601281420516080107858); [thebell, 2026-02-25](https://m.thebell.co.kr/m/newsview.asp?newskey=202602251335152120102494)
- **CyCraft.** Provisional underwriting price NT$90 in January 2026. Source: [CyCraft](https://www.cycraft.com/en/news/auction-20260120). Market cap about $86m on 2026-04-13. Source: [Multiples.vc](https://multiples.vc/public-comps/cycraft-technology-valuation-multiples)
- **S2W.** IPO price range KRW 11,400–13,200 in August 2025. Source: [Bloter](https://www.bloter.net/news/articleView.html?idxno=641512)

### Inferences
**Trend Micro: fair**
- **Market cap in dollars.** ¥864.42bn is about $5.43bn at ¥159.30/USD.
- **Below or at the bottom of its range.** EV/Sales of 2.18x is below every fiscal-year-end value since 2021 (2.26–3.43). EV/EBITDA of 8.16x and EV/FCF of 9.94x are near the bottom of their ranges (7.34–12.23 and 9.81–20.35).
- **On guidance.** P/E on FY2026 guided net income is about 28x (¥864.42bn ÷ ¥30.7bn); EV/EBIT is about 14.3x (¥633.21bn ÷ ¥44.4bn).
- **Adjusting for deferred revenue.** Treating deferred revenue (¥218.8bn) as debt-like puts EV at about ¥852bn, EV/Sales about 2.9x and EV/EBITDA about 10.9x. On that basis it is in line with history, not cheap.
- **What the price implies.** Roughly no growth in free cash flow and continued margin pressure (Q3 operating cash flow −64%).
- **Near-term events.**
  - Buyback window 2026-11-13 to 2026-12-23 (up to ¥5bn, about 0.6% of market cap).
  - FY2026 results and the first annual-only FY2027 guidance, probably February 2027 (date not verified).
  - Unresolved private-equity interest is a two-sided event risk.
- **Conditions that would improve the entry.** AI cost-to-serve falling; constant-currency growth back above 5%; operating margin recovering toward 20%; or a firm bid.

**AhnLab: fair (upper half of own range)**
- EV/EBITDA 16.6x against a fiscal-year-end range of 6.97–23.19; EV/Sales 2.71x against 1.12–3.50; P/E 21x.
- The +90% move prices in continued breach-driven domestic growth. Net cash is 29% of market cap.
- Near-term events: Q4 results (early 2027); the scale of 2027 bank budgets.

**Other listed companies: suggested labels**

| Company | Label | Reason |
|---|---|---|
| FFRI | stretched | EV/Sales 12x and P/E 56x on a small revenue base; GMO's 9.61% stake is a stated pure investment, not a bid signal |
| Cyber Security Cloud | fair | EV/EBITDA 16x after a 17.6% one-day drop on 2026-11-12, cause unknown |
| Digital Arts | attractive on multiples, but verify | EV/EBITDA 6.6x and net cash 39% of market cap; trailing FCF (¥11.07bn) almost equals revenue (¥11.87bn), which looks anomalous |
| HENNGE | stretched | EV/EBITDA 30x |
| Ubiquitous AI | cannot assess | Loss-making micro-cap |
| GMO Internet Group | cannot assess as security exposure | Security segment not disclosed |
| Genians | fair | Forward P/E 17x; EV/FCF 83x shows weak cash conversion |
| S2W | stretched | EV/Sales 8.5x while missing its own IPO targets; trades below the IPO range |
| IGLOO | fair | Low margin; EV above market cap despite net cash suggests non-equity claims (unverified) |
| WINS | attractive on multiples | Net cash 77% of market cap; P/E 7x; 6.7% yield; but a weak automation position |
| Raonsecure | stretched | P/E 35x on a 6% operating margin |
| FASOO AI | attractive on multiples | EV/EBITDA 5.1x; not core automated security |
| CHT Security | fair | EV/EBITDA 14.5x; forward P/E 17x; 4% yield |
| CyCraft | fair / cannot assess | EV/Sales 4.9x, loss-making, about 14% below the provisional IPO price; Innovation Board access rules unverified |
| Gorilla | cannot assess | 17% gross margin, losses, 22% short interest; not an automated-security business |

**Foreign-investor access**
- Trend Micro trades directly in Tokyo and over the counter in the US as TMICY (ADR) and TMICF (ordinary shares). Source: [GuruFocus, 2026-11-12](https://www.gurufocus.com/news/9193984/trend-micro-inc-tmicy-reports-strong-9month-earnings-highlights-dividend-sustainability); [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/trend-micro-inc-tmicf-q2-173114380.html)
- Korean and Taiwanese names trade on KOSDAQ, TWSE and TPEx (generally open to foreigners, per the brief).
- Private names: no direct route. Look-through exposure exists via listed holders such as SK Square for SK Shieldus, and Naver and Hana Financial for Theori, but it is immaterial.

### Gaps
- Five-year multiple ranges were retrieved only for Trend Micro and AhnLab.
- Forward consensus is missing for most small caps.
- Foreign-investor rules were not verified: the Korean registration regime as of 2026; Taiwan's FINI registration; whether foreigners can trade Innovation Board stocks (historically limited to qualified investors).
- No current valuation for TeamT5, DEVCORE, Autocrypt or Theori.
- No LAC quote.

## 5. Where Japanese-, Korean- or Chinese-language sources were needed; summary scorecard; exclusions; coverage limits; sources

### Takeaway
- **Korean-language sources were needed and used successfully.** They covered AhnLab's Q3 results, S2W's IPO and H1 results, the SK Shieldus sale, Theori's funding and headcount, and DEF CON team composition.
- **Japanese-language sources were needed and partly used.** I used Bloomberg Japan, a Kabutan headline, Newsweek Japan (Reuters), innovatopia and a Japanese blog. Kabutan and Minkabu returned 403 errors, and TDnet/EDINET were not reached; English-language IR documents filled part of the gap.
- **Chinese-language (Taiwan) sources were needed but not used.** MOPS, iThome, CommonWealth and DigiTimes were out of reach because the shared search budget ran out before the Taiwan-specific searches. Taiwan coverage relies on English company pages, the official English law database and quote pages.

### Cited Findings
- **Korean sources used:** [MTN](https://news.mtn.co.kr/article/2026102810354690595), [Asiae](https://view.asiae.co.kr/article/2026102809512349625), [thebell](https://www.thebell.co.kr/front/newsview.asp?key=202601291517028320105956), [Bloter](https://www.bloter.net/news/articleView.html?idxno=641512), [THE VC](https://thevc.kr/theori), [Seoul Economic Daily (English edition)](https://en.sedaily.com/technology/2026/10/08/theori-drops-consulting-training-to-bet-all-on-ai-hacking), [MTN DEF CON](https://news.mtn.co.kr/news-detail/2026081011560011163).
- **Japanese sources used:** [Bloomberg Japan](https://www.bloomberg.com/jp/news/articles/2025-02-13/SRLM9QT0G1KW00), [Kabutan headline](https://kabutan.jp/news/marketnews/?b=n202502130465), [Newsweek Japan/Reuters](https://www.newsweekjapan.jp/headlines/business/2025/02/537058.php), [innovatopia](https://innovatopia.jp/cyber-security/cyber-security-news/115623/), [ScanNetSecurity (headline)](https://scan.netsecurity.ne.jp/article/2026/09/28/56318.html). GMO's English IR notice was used in place of the Japanese TDnet filing. Source: [GMO](https://ir.group.gmo/en/pdf/irlibrary/gmo_disclose_info20261102_02_e.pdf)
- **Taiwan sources used (English only):** [Taiwan law database](https://law.moj.gov.tw/ENG/LawClass/LawAll.aspx?pcode=A0030297), [CyCraft](https://www.cycraft.com/en/news/auction-20260120), [TeamT5](https://teamt5.org/en/), [DEVCORE](https://devco.re/en/). An iThome article on Pwn2Own appeared in results but was not opened. Source: [iThome](https://www.ithome.com.tw/news/179590)

### Inferences

#### Compact per-company scorecard
Quality tests (a) position, (b) lead, (c) revenue model, (d) financial strength, (e) resilience; then path-forward verdict; then entry snapshot with suggested label. Entry is kept separate from quality.

**Trend Micro (TSE: 4704)**
- (a) Medium: owns the ZDI/Pwn2Own judge; no verification tool; no gated-model access evidenced.
- (b) Eroding: Gartner EPP 5th and Forrester cloud workload security 6th (2024); IDC CNAPP growth below market.
- (c) Strong: subscription-dominated; ARR $1.29bn (TrendAI).
- (d) Solid but weakening: no debt; cash roughly equals deferred revenue; operating margin 23%→18% (Q3 YoY); Q3 operating cash flow −64%.
- (e) Medium: helped by a pause; hurt by acceleration through gating and model-maker competition; Taipei R&D centre.
- Path: **partly coherent.** AI spend is real; 2028 targets withdrawn on 2026-11-12.
- Entry: ¥6,660, market cap ¥864bn, EV/Sales 2.18x, EV/EBITDA 8.2x, forward P/E 26x (2026-11-12). **Fair.**

**Theori / Xint (private, KR–US)**
- (a) Strong but dependent: machine-speed find and validate on third-party LLMs.
- (b) High technical evidence: AIxCC 3rd (2025), Pwn2Own Ireland 2nd (2026, team "Xint"), IDC Innovator (2026).
- (c) Moving from labour to platform; consulting ends by end-2026.
- (d) Unknown or thin: about $15.4m raised; 92 staff.
- (e) Fragile: funding risk in a pause; competition from model makers and gating in acceleration.
- Path: **partly coherent, leaning coherent.**
- Entry: private; no valuation. **Cannot assess.**

**GMO Flatt Security / Ierae (parent TSE: 9449)**
- (a) Medium: AI scanning plus auto-fix on Anthropic models.
- (b) Talent evidence only (DEF CON 34 CTF win via undef1ned); 300+ customers [company claim].
- (c) Usage-scaled subscription.
- (d) Segment not disclosed; parent has net debt of ¥50bn; own subsidiary breach (October 2026).
- (e) Domestic demand from the Active Cyber Defense law; risk of becoming a reseller of model-maker capability.
- Path: **coherent at small scale.**
- Entry: via GMO Internet Group (¥3,153; EV/EBITDA 5.7x; 2026-11-12). **Cannot assess** for security exposure.

**AhnLab (KOSDAQ: 053800)**
- (a) Weak to medium: domestic incumbent; no judge.
- (b) No outside evidence retrieved.
- (c) Mixed; not verified.
- (d) Good: net cash KRW 298bn; operating margin 13%.
- (e) Supported by Korean breach budgets; antivirus commoditisation risk.
- Path: **partly coherent.**
- Entry: KRW 115,200; EV/EBITDA 16.6x (upper half of five-year range); P/E 21x (2026-11-12). **Fair.**

**SK Shieldus (private, EQT 68%)**
- (a) Weak: labour, physical security and system integration; about 30% cyber.
- (b) Domestic Tier-1 public customers.
- (c) Labour and recurring service contracts.
- (d) Stretched: KRW 2.44tn of borrowings (Q3 2025); about KRW 300bn a year of capex.
- (e) Korea-only; breach tailwind.
- Path: **not coherent / cannot assess** (no automation evidence).
- Entry: private; EQT ask reportedly up to KRW 6tn; cyber unit ≥KRW 1tn estimated. **Cannot assess.**

**CyCraft (TIB: 7823)**
- (a) Medium-small: AI-driven MDR, LLM firewall, AI red-teaming.
- (b) Gartner and MITRE claims unconfirmed.
- (c) 90% subscription [company].
- (d) TTM revenue TWD 383m; operating margin −11%; net cash TWD 650m.
- (e) Taiwan and Japan concentration; geopolitical exposure.
- Path: **partly coherent.**
- Entry: TWD 77, EV/Sales 4.9x (2026-11-11), below the provisional IPO price of NT$90. **Fair / cannot assess.**

**CHT Security (TPE: 7765)**
- (a) Weak to medium: telecom-affiliated services.
- (b) None retrieved.
- (c) Services, likely labour-heavy (unverified).
- (d) Good: operating margin 24%; ROE 24%; net cash.
- (e) Supported by Taiwanese public-sector demand.
- Path: **cannot assess.**
- Entry: TWD 245; EV/EBITDA 14.5x; forward P/E 17x (2026-11-12). **Fair.**

**S2W (KOSDAQ: 488280)**
- (a) Small: threat-intelligence SaaS.
- (b) INTERPOL and Microsoft data-partner claims unconfirmed.
- (c) 96% SaaS [company].
- (d) Weak: H1 2026 operating loss KRW 5.4bn; about two years of runway.
- (e) Fragile.
- Path: **partly coherent, under-delivering.**
- Entry: KRW 9,470; EV/Sales 8.5x (2026-11-12). **Stretched.**

**FFRI Security (TSE: 3692)**
- (a) Not assessed; (b) none retrieved; (c) not verified.
- (d) Operating margin 29%, net cash.
- (e) Not assessed.
- Path: **cannot assess.**
- Entry: ¥7,190; EV/Sales 12.2x; P/E 56x (2026-11-12); GMO owns 9.61%. **Stretched.**

**Japanese small caps: Cyber Security Cloud (4493), Digital Arts (2326), HENNGE (4475)**
- (a)/(b) No outside lead evidence retrieved.
- (d) Profitable, with net cash.
- Path: **cannot assess.**
- Entry (2026-11-12):
  - Cyber Security Cloud: EV/EBITDA 16.4x. **Fair.**
  - Digital Arts: EV/EBITDA 6.6x. **Attractive on multiples** (verify the FCF figure).
  - HENNGE: EV/EBITDA 29.5x. **Stretched.**

**Korean small caps: Genians, IGLOO, WINS, Raonsecure, FASOO AI**
- (a)/(b) No automation evidence. Raon Secure's white-hat teams placed 3rd and 4th at DEF CON 34, a talent signal.
- (d) All have net cash.
- Path: **cannot assess.**
- Entry (2026-11-12):
  - Genians: **fair.**
  - IGLOO: **fair.**
  - WINS: **attractive on multiples.**
  - Raonsecure: **stretched.**
  - FASOO AI: **attractive on multiples.**

**Autocrypt (private)**
- (a) Device-maker-liability play (transition 5).
- (b) DEF CON 34 Car Hacking Village CTF 1st of 83 (independent); Technical Service designation [company claim].
- (c)–(e) Unknown.
- Path: **cannot assess.**
- Entry: **cannot assess.**

**TeamT5 / DEVCORE (private)**
- TeamT5: threat-intelligence software with Japanese channels.
- DEVCORE: offensive services (labour); MSRC MVR recognition; transition (1) not evidenced.
- Path: **cannot assess.**
- Entry: **cannot assess.**

**Gorilla Technology (Nasdaq: GRRR)**
- (a) Weak for this theme; gross margin 17%.
- (d) Loss-making, with net cash of $105m.
- Path: **not assessed.**
- Entry: $8.37; EV/Sales 0.89x (2026-11-11). **Cannot assess.**

#### Companies considered and excluded (or kept to context)

| Company | Reason |
|---|---|
| TXOne Networks | Covered by another researcher; context only (Trend Micro–Moxa joint venture since November 2018) |
| Samsung Research | Part of the AIxCC-winning team, but a corporate R&D unit, not a security vendor |
| NEC, Fujitsu, NTT Data, Hitachi, NRI Secure | Security is a small, undisclosed part of large IT-services groups with labour/SI models (inference). Fujitsu is the largest winner of Japanese government cyber contracts (¥47.2bn, FY2023–25). Not researched further |
| LAC (TSE: 3857) | Data not retrievable in this pass (quote sites blocked); services-led |
| Ubiquitous AI | Embedded-software micro-cap, loss-making; no automated-security evidence |
| HENNGE, Digital Arts | Identity and filtering, adjacent to automated security rather than core |
| Gorilla Technology | Smart-city and video integration with a low gross margin; not automated security |
| Penta Security, Monitorapp, FESCARO, Findthegap, Sparrow, Onward Security | Not researched (search budget exhausted) |

### Gaps

#### Coverage limits by country
- **Japan.**
  - TDnet/EDINET not accessed; Kabutan, Minkabu and Yahoo quote pages blocked or empty.
  - No data for LAC.
  - No 2025–26 Gartner, IDC or Forrester data for Trend Micro.
  - Trend Micro's China history and export-control exposure not verified.
  - Trend Micro's TXOne stake and major shareholders not verified.
  - Large IT groups' security units not researched.
- **Korea.**
  - DART/KIND not accessed.
  - ISMS-P and IoT rule changes, PIPC fines, and the KT femtocell and Lotte Card breaches not verified.
  - Several private firms not researched (Penta Security, Monitorapp, FESCARO, Findthegap, Sparrow).
  - No use of domestic models (Exaone, HyperCLOVA X, Gauss) documented for any covered firm.
  - Korean participation in Glasswing after June 2026 not verified.
- **Taiwan.**
  - No Chinese-language sources used (MOPS, iThome, CommonWealth, DigiTimes).
  - TeamT5's and DEVCORE's funding and IPO status, Onward Security's status, and the AI Basic Act not verified.
  - Innovation Board investor-eligibility rules not verified.
  - Gorilla's IR site (ir.gorilla-technology.com) could not be resolved in this session's network settings.
- **All countries.**
  - The shared web-search budget was exhausted mid-task; no further searches were run.
  - Some pages were blocked: BleepingComputer (403), Business Wire (403), Japan Times (402 paywall), CMU (503).
  - The status of foreign access to Mythos-class models after August 2026 was not verified.

#### Dated source list
Dates are publication dates where known, otherwise "accessed 2026-11-12".

**Trend Micro and its ZDI/Pwn2Own franchise**
- Trend Micro FY2026 Q3 results deck, 2026-11-12: https://www.trendmicro.com/content/dam/trendmicro/global/en/about/investor-relations/reports-presentation/2026/financial-2026-presentation-negi-q3.pdf
- Trend Micro FY2026 Q1 results deck, 2026 (cited via search summary): https://www.trendmicro.com/content/dam/trendmicro/global/en/about/investor-relations/reports-presentation/2026/financial-2026-presentation-negi-q1.pdf
- Investing.com, Trend Micro Q2 2026 slides, 2026-08-13: https://www.investing.com/news/company-news/trend-micro-q2-2026-slides-ai-investment-drives-growth-pressures-margins-93CH-4857326
- TipRanks, nine-month results, 2026-11-12: https://www.tipranks.com/news/company-announcements/trend-micro-reports-higher-nine-month-sales-and-lower-profit
- TipRanks, buyback, 2026-11-12: https://www.tipranks.com/news/company-announcements/trend-micro-announces-share-buyback-program
- Trend Micro stock and bond information (accessed 2026-11-12): https://www.trendmicro.com/en_us/about/investor-relations/stocks-bonds.html
- MarketScreener, February 2026 buyback closed (2026-03): https://www.marketscreener.com/news/trend-micro-incorporated-s-equity-buyback-announced-on-february-18-2026-has-closed-with-940-400-sh-ce7e5edcde80f220
- BankInfoSecurity, 2025-02-14: https://www.bankinfosecurity.com/blogs/private-equity-now-kicking-tires-on-trend-micro-p-3814
- The Star/Reuters, 2025-02-13: https://www.thestar.com.my/tech/tech-news/2025/02/13/exclusive-buyout-firms-vie-for-cybersecurity-firm-trend-micro-sources-say
- SiliconANGLE, 2025-02-13: https://siliconangle.com/2025/02/13/private-equity-firms-reportedly-competing-buy-cybersecurity-provider-trend-micro/
- Bloomberg Japan, 2025-02-13: https://www.bloomberg.com/jp/news/articles/2025-02-13/SRLM9QT0G1KW00
- Kabutan, 2025-02-13: https://kabutan.jp/news/marketnews/?b=n202502130465
- Newsweek Japan/Reuters, 2025-02: https://www.newsweekjapan.jp/headlines/business/2025/02/537058.php
- Hatena blog (low reliability), updated 2026-07: https://worklife-carrer.hatenablog.com/entry/2025/06/07/094954
- Wikipedia "Trend Micro" (accessed 2026-11-12): https://en.wikipedia.org/wiki/Trend_Micro
- GuruFocus, 2026-11-12: https://www.gurufocus.com/news/9193984/trend-micro-inc-tmicy-reports-strong-9month-earnings-highlights-dividend-sustainability
- Yahoo Finance, Q2 2026 call highlights, 2026-08: https://finance.yahoo.com/technology/ai/articles/trend-micro-inc-tmicf-q2-173114380.html
- ZDI published advisories (accessed 2026-11-12): https://www.zerodayinitiative.com/advisories/published/
- ZDI blog (accessed 2026-11-12): https://www.zerodayinitiative.com/blog
- CyberInsider, 2026-10-09: https://cyberinsider.com/google-pixel-10-hacked-as-pwn2own-ireland-wraps-with-1-26-million-in-rewards/
- BleepingComputer, 2026-10 (search summary): https://bleepingcomputer.com/news/security/hackers-earn-1262000-for-98-zero-days-at-pwn2own-ireland
- SecurityLab, 2026-10 (search summary): https://www.securitylab.ru/news/578559.php

**AIxCC and DEF CON**
- DARPA AIxCC results, 2025-08-08: https://www.darpa.mil/news/2025/aixcc-results
- DARPA finalists, 2025-07-08: https://www.darpa.mil/news/2025/ai-cyber-challenge-winners-def-con-33
- Trail of Bits, 2025-08-09: https://blog.trailofbits.com/2025/08/09/trail-of-bits-buttercup-wins-2nd-place-in-aixcc-challenge/
- Infosecurity Magazine, 2025-08 (search summary): https://www.infosecurity-magazine.com/news/defcon-ai-cyber-challenge-winners/
- MTN (DEF CON 34), 2026-08-10: https://news.mtn.co.kr/news-detail/2026081011560011163
- CMU, 2025-08-14 (headline): https://www.ri.cmu.edu/carnegie-mellons-hacking-team-wins-fourth-straight-record-ninth-overall-def-con-capture-the-flag-title/
- Tsinghua, 2026-08 (search summary): https://www.tsinghua.edu.cn/info/1180/127762.htm
- Georgia Tech, 2026-08 (search summary): https://hg.gatech.edu/node/691834
- innovatopia, 2026-08: https://innovatopia.jp/cyber-security/cyber-security-news/115623/
- ScanNetSecurity, 2026-09-28 (headline): https://scan.netsecurity.ne.jp/article/2026/09/28/56318.html

**Theori**
- SiliconANGLE, 2026-03-17: https://siliconangle.com/2026/03/17/theori-launches-xint-code-ai-platform-uncover-hidden-vulnerabilities-massive-codebases/
- Help Net Security, 2026-03-18: https://www.helpnetsecurity.com/2026/03/18/theori-xint-code/
- Business Wire, Xint Code, 2026-03-17 (search summary): https://www.businesswire.com/news/home/20260317129537/en/Xint-Code-Demonstrates-Human-like-Discovery-and-Prioritization-of-Business-Logic-Vulnerabilities-Analyzing-Millions-of-Code-Lines-in-Just-Hours
- Business Wire, IDC Innovator, 2026-08-13 (title only): https://www.businesswire.com/news/home/20260813325954/en/Xint.io-Recognized-as-an-IDC-Innovator-for-Agentic-Autonomous-Penetration-Testing-for-DevSecOps
- Seoul Economic Daily, 2026-10-08: https://en.sedaily.com/technology/2026/10/08/theori-drops-consulting-training-to-bet-all-on-ai-hacking
- THE VC (accessed 2026-11-12): https://thevc.kr/theori
- CB Insights: https://www.cbinsights.com/company/theori/financials
- PitchBook: https://pitchbook.com/profiles/company/500894-92
- Caplight: https://www.caplight.com/company/theori

**GMO**
- Takumi page (accessed 2026-11-12): https://flatt.tech/takumi
- GMO–Anthropic partnership, 2026-07-28: https://group.gmo/en/news/article/852/
- GMO FFRI share-acquisition notice, 2026-11-02: https://ir.group.gmo/en/pdf/irlibrary/gmo_disclose_info20261102_02_e.pdf
- GMO unauthorised-access notice, 2026-10-23: https://group.gmo/en/ir_news/article/690/
- GMO news list (accessed 2026-11-12): https://group.gmo/en/news/

**AhnLab**
- MTN, 2026-10-28: https://news.mtn.co.kr/article/2026102810354690595
- Asiae, 2026-10-28: https://view.asiae.co.kr/article/2026102809512349625
- Digital Economy News, 2026-10: https://www.denews.co.kr/news/articleView.html?idxno=42909

**SK Shieldus**
- thebell, 2026-01-28: http://m.thebell.co.kr/m/newsview.asp?svccode=00&newskey=202601281420516080107858
- thebell, 2026-01-29: https://www.thebell.co.kr/front/newsview.asp?key=202601291517028320105956
- thebell, 2026-02-25: https://m.thebell.co.kr/m/newsview.asp?newskey=202602251335152120102494
- Top Daily (search summary): https://www.topdaily.kr/articles/109944
- IPE Real Assets, 2023: https://realassets.ipe.com/news/eqt-to-buy-south-korean-security-operator-sk-shieldus/10065421.article
- Korea Herald, 2023-07-20: https://www.koreaherald.com/view.php?ud=20230720000611

**S2W**
- Bloter, 2025-08-05: https://www.bloter.net/news/articleView.html?idxno=641512
- Chickstock, H1 2026 (search summary): https://www.chickstockfi.com/stocks/488280/reports/2026-half

**Autocrypt, CyCraft, TeamT5, DEVCORE**
- TechNode Global, Autocrypt, 2026-08: https://technode.global/prnasia/autocrypt-wins-def-con-34-automotive-hacking-competition-ranking-first-among-83-teams/
- CyCraft auction notice, 2026-01-20: https://www.cycraft.com/en/news/auction-20260120
- CyCraft listing release, 2026-02-05 (search summary): https://www.cycraft.com/en/news/taiwans-first-ai-cybersecurity-stock-en-20260205
- Dealroom, 2026: https://app.dealroom.co/news/feed/taiwanese-ai-cybersecurity-firm-cycraft-lists-on-taiwan-innovation-board-after-22-76-revenue-growth
- Multiples.vc, 2026-04-13: https://multiples.vc/public-comps/cycraft-technology-valuation-multiples
- TeamT5 (accessed 2026-11-12): https://teamt5.org/en/
- DEVCORE (accessed 2026-11-12): https://devco.re/en/

**Frontier-model access**
- TechTimes, 2026-08-10: https://www.techtimes.com/articles/323705/20260810/japans-cyber-chief-confirms-us-ai-export-ban-hit-government-security-scanning.htm
- Korea JoongAng Daily, 2026-06-16: https://www.koreajoongangdaily.com/business/white-house-officials-pin-anthropic-ai-export-block-on-korean-telecom-report/12726842
- Korea Times, 2026-06-03: https://www.koreatimes.co.kr/amp/business/tech-science/20260603/korea-joins-anthropics-project-glasswing-for-mytos-cybersecurity-ai-model
- Kyunghyang Shinmun, 2026-06-03: https://www.khan.co.kr/en/article/202606031446037/
- Joho no Todai, 2026-06-18: https://joho-todai.com/en/mythos-export-restrictions-sk-telecom/

**Korean demand drivers**
- FN News, 2026-04-13 (search summary): https://en.fnnews.com/news/202604131822093743
- FN News, 2026-09-01 (search summary): https://en.fnnews.com/news/202609011319080930
- Korea Times, 2026-07-13: https://www.koreatimes.co.kr/business/tech-science/20260713/telecoms-step-up-cybersecurity-spending-after-breaches
- Korea JoongAng Daily, 2026-10-11: https://www.koreajoongangdaily.com/business/banks-boost-defenses-after-ailinked-hacks/12913975
- Japan Times, 2026-10-06 (headline): https://www.japantimes.co.jp/business/2026/10/06/south-korea-bank-hacks/
- American Banker, 2026-10 (search summary): https://www.americanbanker.com/news/ai-linked-hacks-hit-korean-banks-through-loan-agent-sites
- Shattered.io, 2026-10 (low reliability): https://shattered.io/crowdstrike-artex-ai-agent-korea-bank-hack-2026/

**Japanese and Taiwanese regulation**
- Japan Public Sector Brief, c. 2026-09/10: https://publicsector.edamamejapan.com/japan-active-cyber-defense-law/
- Baker McKenzie, 2025: https://connectontech.bakermckenzie.com/japans-new-active-cyber-defense-law-impact-on-businesses/
- Simplico, 2026-09-24: https://www.simplico.net/2026/09/24/active-cyber-defense-law-soc-incident-reporting/
- IPA JC-STAR (accessed 2026-11-12): https://www.ipa.go.jp/en/security/jc-star/index.html
- Taiwan Cyber Security Management Act (amended 2025-09-24; accessed 2026-11-12): https://law.moj.gov.tw/ENG/LawClass/LawAll.aspx?pcode=A0030297

**StockAnalysis quote and ratio pages (all accessed 2026-11-12; prices are the 2026-11-12 close unless marked 2026-11-11)**
- Japan: [4704](https://stockanalysis.com/quote/tyo/4704/statistics/) and [4704 ratios](https://stockanalysis.com/quote/tyo/4704/financials/ratios/); [3692](https://stockanalysis.com/quote/tyo/3692/statistics/); [4493](https://stockanalysis.com/quote/tyo/4493/statistics/); [2326](https://stockanalysis.com/quote/tyo/2326/statistics/); [4475](https://stockanalysis.com/quote/tyo/4475/statistics/); [3858](https://stockanalysis.com/quote/tyo/3858/statistics/); [9449](https://stockanalysis.com/quote/tyo/9449/statistics/)
- Korea: [053800](https://stockanalysis.com/quote/kosdaq/053800/statistics/) and [053800 ratios](https://stockanalysis.com/quote/kosdaq/053800/financials/ratios/); [263860](https://stockanalysis.com/quote/kosdaq/263860/statistics/); [488280](https://stockanalysis.com/quote/kosdaq/488280/statistics/); [067920](https://stockanalysis.com/quote/kosdaq/067920/statistics/); [136540](https://stockanalysis.com/quote/kosdaq/136540/statistics/); [042510](https://stockanalysis.com/quote/kosdaq/042510/statistics/); [150900](https://stockanalysis.com/quote/kosdaq/150900/statistics/)
- Taiwan: [7765](https://stockanalysis.com/quote/tpe/7765/statistics/); [7823](https://stockanalysis.com/quote/tpe/7823/statistics/) (2026-11-11)
- US-listed, 2026-11-11 close: [GRRR](https://stockanalysis.com/stocks/grrr/statistics/); peers [CHKP](https://stockanalysis.com/stocks/chkp/statistics/), [GEN](https://stockanalysis.com/stocks/gen/statistics/), [TENB](https://stockanalysis.com/stocks/tenb/statistics/), [S](https://stockanalysis.com/stocks/s/statistics/)
