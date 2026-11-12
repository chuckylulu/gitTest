# Protecting connected and industrial devices that cannot be patched (OT/IoT/CPS security) and device-maker liability and regulation by jurisdiction — research notes as of 2026-11-12

Scope note: these notes cover OT/IoT/cyber-physical visibility, network shielding, segmentation, virtual patching and firmware/product security vendors, plus device-maker regulation. Research date is 2026-11-12. Partway through the research, the session's shared web-search budget ran out. After that I only fetched pages that had already come up in results, plus a few official primary pages, directly. So several Asian jurisdictions, UN R155/R156, IEC 62443, UK PSTI enforcement and Mitsubishi Electric's segment reporting are only partly verified (see each Gaps section). "[company claim, unconfirmed]" marks figures that only the company or its paid agents have published. My own arithmetic is labelled "my calculation".

Headline changes of ownership in 2025–2026, verified below:
- Armis to ServiceNow: closed 2026-04-20.
- Nozomi Networks to Mitsubishi Electric: closed 2026-01-28.
- Dragos (majority) to Accenture: closed 2026-09-16/17.
- Phosphorus to Dragos: 2026-06-01.
- runZero and NetRise to Dragos: closed 2026-07-31 and 2026-09-17.
- Elisity to IonQ: closed 2026-11-04.

That leaves Claroty as the largest independent CPS-protection pure play.

---

## 1. Per company: ownership, funding, revenue/ARR, customers, revenue model, analyst positioning, independent evidence

### Takeaway
In 2026 the OT/IoT category consolidated into strategic owners. Outside buyers paid about 20–23x ARR for the visibility/exposure leaders: ServiceNow–Armis about 22.8x ARR at announcement, and Accenture–Dragos+runZero+NetRise about 20.1x combined ARR. Mitsubishi Electric paid about 9.3x trailing revenue for Nozomi. The four Leaders in Gartner's 2026 Magic Quadrant for CPS Protection Platforms (dated 2026-03-03) are Nozomi, Claroty, Armis and Dragos. Three of them are now inside larger parents. Shielding specialists (TXOne, Waterfall, Zero Networks, Elisity) and firmware/product-security specialists (Finite State, ONEKEY, Cybellum) are much smaller and mostly disclose little.

### Cited Findings

**Analyst positioning (cross-company)**
- Gartner Magic Quadrant for CPS Protection Platforms, dated 2026-03-03, evaluated 13 vendors, with four Leaders. Claroty says it is a Leader for the second consecutive year — [Claroty blog, 2026-03-09](https://claroty.com/blog/claroty-named-a-leader-in-2026-gartner-magic-quadrant-for-cps-protection-platforms). The Leaders are Nozomi Networks, Claroty, Armis and Dragos — [Nozomi MQ page](https://www.nozominetworks.com/gartner-magic-quadrant-cps-protection-platforms); [Armis/Business Wire, 2026-03-04](https://www.businesswire.com/news/home/20260304220653/en/Armis-Named-a-Leader-for-Second-Consecutive-Year-in-2026-Gartner-Magic-Quadrant-for-CPS-Protection-Platforms); [Dragos press release](https://www.dragos.com/resources/press-release/dragos-named-leader-2026-gartner-magic-quadrant-cps-protection-platforms).
- Non-Leader placements come from a vendor (Nozomi) summary, not the Gartner document, and are not independently verified:
  - Challengers: Forescout, Tenable, Fortinet.
  - Niche Players: Microsoft, Cisco, Palo Alto Networks, Honeywell, TXOne Networks.
  - Visionary: Darktrace.
  - Source: [Nozomi MQ page](https://www.nozominetworks.com/gartner-magic-quadrant-cps-protection-platforms).
- Nozomi says it received the highest scores in all four use cases of the companion 2026 Gartner Critical Capabilities. This is vendor-reported Gartner content [company claim, unconfirmed] — [Nozomi blog](https://www.nozominetworks.com/blog/nozomi-networks-named-a-leader-in-2026-gartner-magic-quadrant-for-cps-protection-platforms-receives-highest-scores-across-all-critical-capabilities-use-cases).
- Forrester positions, as the vendors report them:
  - Claroty: Leader in The Forrester Wave: IoT Security Solutions, Q3 2025; Strong Performer in The Forrester Wave: OT Security Solutions, Q2 2024 — [Claroty blog, 2026-03-09](https://claroty.com/blog/claroty-named-a-leader-in-2026-gartner-magic-quadrant-for-cps-protection-platforms).
  - Nozomi: Leader in the Forrester Wave for IoT Security — [Nozomi press release, 2026-01-28](https://www.nozominetworks.com/press-release/nozomi-networks-enters-next-phase-of-growth-as-mitsubishi-electric-completes-acquisition).
- KLAS 2026 Healthcare IoT Security report: Asimily had the highest overall performance score, 96.6/100. This is reported via Asimily's release — [Yahoo Finance/Asimily release](https://finance.yahoo.com/news/asimily-leads-vendors-best-klas-133000280.html).

#### Armis (US/Israel) — now part of ServiceNow (NYSE: NOW)
- Announced 2025-12-22: ServiceNow to buy Armis for about $7.75B in cash. At announcement Armis reported more than $340M ARR, with year-over-year ARR growth above 50% [company figure]. Expected close was H2 2026 — [ServiceNow press release](https://newsroom.servicenow.com/press-releases/details/2025/ServiceNow-to-acquire-Armis-to-expand-cyber-exposure-and-security-across-the-full-attack-surface-in-IT-OT-and-medical-devices-for-companies-governments-and-critical-infrastructure-worldwide/).
- Closing and accounting, per [ServiceNow 10-Q for Q2 2026](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000076/now-20260630.htm):
  - Closed 2026-04-20, earlier than guided.
  - Preliminary consideration about $7.6B, settled in cash.
  - Goodwill $5,323M (not tax-deductible). Intangibles $2,530M: developed technology $1,950M, customer relationships $473M, backlog $54M, brand $53M.
  - Current deferred revenue acquired: $137M.
  - Effect on consolidated results was "not material", and no pro forma was presented.
- Financing, per the same [10-Q](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000076/now-20260630.htm):
  - A $4.0B term loan (April 2026), repaid in May 2026 with $4.0B of senior notes. The notes carry coupons of 4.25% to 6.30% and mature from 2028 to 2056.
  - A commercial paper program of up to $3.0B, with $2.1B outstanding at 2026-06-30.
  - Veza (identity security) closed separately on 2026-03-02 for about $1.2B.
- Armis Centrix sits inside the ServiceNow AI Platform and is still sold on its own — [Business Wire via Morningstar, 2026-04-20](https://www.morningstar.com/news/business-wire/20260419639334/servicenow-completes-armis-acquisition-closing-the-gap-between-asset-visibility-and-cyber-risk); [Calcalist](https://www.calcalistech.com/ctechnews/article/hyo11bqetwg).
- ServiceNow Q3 2026, reported 2026-10-28 — [8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371526000092/erq3fy26.htm):
  - Revenue $4,106M (+20.5% y/y); subscription revenue $3,988M (+21%).
  - Non-GAAP operating margin 32.5%; free cash flow $822M.
  - FY2026 subscription guidance $15,780–15,790M; FY2026 FCF margin guidance 36%.
  - At 2026-09-30, debt was about $7.52B and cash plus marketable securities about $6.96B (my calculation from the release).
  - The release mentions Armis only once: "capabilities from Armis and Veza feed directly into the Super Intelligence Control Tower" (Autonomous Security announcement). No Armis revenue or ARR is disclosed.
- Analyst position: Leader in the 2026 Gartner CPS MQ, for the second consecutive year — [Business Wire, 2026-03-04](https://www.businesswire.com/news/home/20260304220653/en/Armis-Named-a-Leader-for-Second-Consecutive-Year-in-2026-Gartner-Magic-Quadrant-for-CPS-Protection-Platforms).

#### Nozomi Networks (US/Switzerland) — now part of Mitsubishi Electric (TSE: 6503)
- 2025-09-09 agreement — [MELCO release No. 3821](https://www.mitsubishielectric.com/en/pr/2025/pdf/0909-1.pdf):
  - MELCO already held 7.0% (diluted) after a 2024 collaboration.
  - It agreed to buy the other 93.0% for US$883M by reverse triangular merger. Closing was planned "within 2025".
- Closed 2026-01-28, announced 2026-01-29 — [MELCO release No. 3862](https://www.mitsubishielectric.com/en/pr/2026/pdf/0129.pdf).
- Net revenue, US$ thousand, years to 31 December — [MELCO 0909-1](https://www.mitsubishielectric.com/en/pr/2025/pdf/0909-1.pdf); [MELCO 0129](https://www.mitsubishielectric.com/en/pr/2026/pdf/0129.pdf):
  - 2022: 42,377
  - 2023: 62,560
  - 2024: 74,695
  - 2025: 101,709
  - Growth rates (my calculation): +47.6% in 2023, +19.4% in 2024, +36.2% in 2025.
- Headcount was 315 at end-August 2025 and 336 in December 2025 — same releases.
- MELCO's acquisition deck — [MELCO deck, 2025-09-09](https://www.mitsubishielectric.com/en/pr/2025/pdf/0909-2.pdf):
  - Gross margin above 70%; 2022–2024 revenue CAGR 33%.
  - A "robust revenue foundation driven by subscriptions".
  - Customer base of more than 1,000 companies in 75 countries.
  - Products: Guardian and Guardian Air sensors; Arc and Arc Embedded software sensors, including one for PLCs launched in 2024; Vantage SaaS; Vantage IQ AI.
  - Roadmap: Serendie-related sales of ¥680B projected for FY2026 and ¥1.1T+ targeted for FY2031.
- Customer claims [company claim, unconfirmed]: 5 of the top 10 oil and gas companies, 7 of the top 10 pharma manufacturers, 7 of the top 10 utilities and 4 of the top 10 mining operations. Nozomi also says it is "the first privately held OT cybersecurity company to reach sustained cash flow and break-even performance". Partnerships in 2025: Schneider Electric, Hitachi Cyber, Nvidia, Dispel, Xona. Source: [Nozomi press release, 2026-01-28](https://www.nozominetworks.com/press-release/nozomi-networks-enters-next-phase-of-growth-as-mitsubishi-electric-completes-acquisition).
- Nozomi keeps its brand, leadership, vendor-neutral roadmap and partnerships — [Nozomi press release](https://www.nozominetworks.com/press-release/nozomi-networks-enters-next-phase-of-growth-as-mitsubishi-electric-completes-acquisition).
- Effect on MELCO's results: the closing release says MELCO "will promptly inform if there is a need to revise its consolidated performance forecasts". No revision was announced in the release — [MELCO 0129](https://www.mitsubishielectric.com/en/pr/2026/pdf/0129.pdf).
- MELCO's forecast for FY to March 2026: net sales ¥5,400B, operating profit ¥430B. Actual for FY to March 2025: ¥5,521.7B sales — [MELCO 0909-1](https://www.mitsubishielectric.com/en/pr/2025/pdf/0909-1.pdf).
- Customer enquiries are routed to the "OT Security Business Development Dept., Industry & Mobility Business Area" — [MELCO 0129](https://www.mitsubishielectric.com/en/pr/2026/pdf/0129.pdf).

#### Claroty (US/Israel) — independent, private
- Series F, 2026-01-22 — [SecurityWeek](https://www.securityweek.com/claroty-raises-150-million-in-series-f-funding/):
  - $150M led by Golub Growth.
  - Existing investors added up to $50M more, used for employee share purchases (secondary). Globes headlined the total as "$200m at over $3b valuation" — [Globes](https://en.globes.co.il/en/article-1001532712).
  - Total raised about $900M.
- Valuation:
  - Calcalist reported about $3B; the company has not confirmed a figure.
  - Earlier marks: above $1B after the $140M Series D (2021), and about $2.5B after the $100M round of March 2024.
  - SecurityWeek points out that an "80% increase" from $2.5B would not equal $3B — [SecurityWeek](https://www.securityweek.com/claroty-raises-150-million-in-series-f-funding/).
- ARR: "over $200M annualized recurring revenue" is a press estimate attributed to Golub, not a company disclosure — [JPost](https://www.jpost.com/business-and-innovation/article-884432); [BankInfoSecurity](https://www.bankinfosecurity.com/claroty-gets-150m-to-lead-in-ai-for-infrastructure-security-a-30598).
- IPO: CEO Yaniv Vardi told Calcalist the company "may be ready as early as 2027 if market conditions align" — [SecurityWeek](https://www.securityweek.com/claroty-raises-150-million-in-series-f-funding/). On 2026-05-07, Axios Pro ran "Claroty eyes IPO amid OT security shakeout"; it is paywalled and I saw only the headline and snippet — [Axios](https://www.axios.com/pro/enterprise-software-deals/2026/05/07/claroty-ipo-ot-security-shakeout-enterprise). I found no S-1 or public filing.
- Products: xDome (SaaS), Continuous Threat Detection (on-premises) and xDome Secure Access. Additions since 2025: Claroty Edge discovery, exposure scenarios, "device purpose for segmented network zones", AI-powered CPS Library — [Claroty blog](https://claroty.com/blog/claroty-named-a-leader-in-2026-gartner-magic-quadrant-for-cps-protection-platforms).
- Named customer case studies: Ohio State University Wexner Medical Center; Provincial Health Services Authority and Fraser Health (BC, Canada); Phlow — [Claroty blog](https://claroty.com/blog/claroty-named-a-leader-in-2026-gartner-magic-quadrant-for-cps-protection-platforms).

#### Dragos (US) — majority-owned by Accenture (NYSE: ACN) since September 2026
- Announced 2026-06-18 — [Accenture newsroom](https://newsroom.accenture.com/news/2026/accenture-to-strengthen-critical-infrastructure-defense-with-end-to-end-cybersecurity-platform-in-age-of-ai-driven-cyber-threats-and-geopolitical-risk):
  - Accenture takes a majority stake in Dragos (percentage not disclosed) and 100% of runZero and NetRise.
  - Combined enterprise value about $4.175B.
  - Combined ARR about $208M "as of June 2026", +53% y/y.
  - Headcount: Dragos 580; runZero 66; NetRise 57.
  - Accenture's own cybersecurity revenue was $10B in FY2025.
- Dragos alone is valued at $3.25B, per co-founder Robert M. Lee's LinkedIn post as reported by [SecurityWeek, 2026-06-18](https://www.securityweek.com/accenture-to-acquire-majority-stake-in-dragos-all-of-runzero-netrise-in-4-1-billion-ot-cybersecurity-push/).
- Closings, per the note on the [Accenture newsroom page](https://newsroom.accenture.com/news/2026/accenture-to-strengthen-critical-infrastructure-defense-with-end-to-end-cybersecurity-platform-in-age-of-ai-driven-cyber-threats-and-geopolitical-risk):
  - NetRise: 2026-07-31.
  - Dragos majority stake: 2026-09-16. Serra Ventures gives 2026-09-17 — [Serra Ventures](https://www.serraventures.com/news/dragos-deal-closes-in-september).
  - runZero: 2026-09-17. NetRise and runZero were acquired by Dragos itself.
- Governance after closing: Lee is CEO and now chairman; Dmitri Alperovitch rejoins the board; Accenture appoints directors. Dragos "will remain an independent and vendor-neutral company" — [SecurityWeek, 2026-09-21](https://www.securityweek.com/dragos-completes-netrise-and-runzero-acquisitions-following-accenture-deal/).
- Earlier steps:
  - Network Perception acquired October 2024 (network mapping and segmentation validation).
  - Phosphorus acquired 2026-06-01, terms undisclosed. Dragos claims a TAM above $50B [company claim, unconfirmed]. Source: [Dragos press release](https://www.dragos.com/resource/press-release/dragos-acquires-phosphorus).
  - In February 2026, Axios Pro reported Dragos looking at M&A and fundraising before a possible IPO; headline only — [Axios](https://www.axios.com/pro/enterprise-software-deals/2026/02/06/dragos-deals-fundraising-ipo).
- Analyst position: Leader in the 2026 Gartner CPS MQ, second year — [Dragos press release](https://www.dragos.com/resources/press-release/dragos-named-leader-2026-gartner-magic-quadrant-cps-protection-platforms).
- Sectors served (named in its own material): energy, manufacturing, water, transportation, data centres — [Dragos press release](https://www.dragos.com/resource/press-release/dragos-acquires-phosphorus).

#### Phosphorus Cybersecurity (US) — part of Dragos since 2026-06-01
- Funding before the acquisition:
  - $38M Series A (2022), led by SYN Ventures and MassMutual Ventures — [VentureBeat](https://venturebeat.com/security/phosphorus-cybersecurity-raises-38-million-to-secure-iot-devices).
  - $27M Series A2 (2023-12-20), led by Evolution Equity Partners — [GlobeNewswire](https://www.globenewswire.com/news-release/2023/12/20/2799227/0/en/Phosphorus-Raises-27-Million-Series-A2-Financing-Round-Led-by-Evolution-Equity-Partners.html).
  - Total about $65M (my sum).
- Capabilities, as described by Dragos: automated remediation including password rotation, firmware updates, certificate management and configuration hardening. Sonu Shankar runs it as GM inside Dragos — [Dragos press release](https://www.dragos.com/resource/press-release/dragos-acquires-phosphorus).

#### TXOne Networks (Taiwan) — private; Trend Micro majority-owned joint venture with Moxa
- Formed as a Trend Micro–Moxa joint venture. The letter of intent was signed in November 2018, and Trend Micro holds the majority — [Trend Micro TW press release, 2018-11-15](https://www.trendmicro.com/zh_tw/about/newsroom/press-releases/2018/2018-11-15.html).
- Funding:
  - $70M Series B agreement (2022), with TGVest leading at $20M — [CNEWS](https://cnews.com.tw/%E7%9E%84%E6%BA%96%E5%85%A8%E7%90%83%E8%B3%87%E5%AE%89%E5%B8%82%E5%A0%B4txone-networks%E7%8D%B27000%E8%90%AC%E7%BE%8E%E5%85%83b%E8%BC%AA%E5%8B%9F%E8%B3%87/).
  - US$51M (NT$1.65B) "B+" round announced 2024-05-08, led by TGVest — [Business Next](https://www.bnext.com.tw/article/79045/startup-txone-b-plus-round-funding).
  - Pegatron and China Development participated — [Yahoo TW](https://tw.stock.yahoo.com/news/txone-networks-b%E8%BC%AA%E5%A2%9E%E8%B3%87%E5%85%B1%E5%8B%9F%E5%BE%9716-5%E5%84%84%E5%85%83-%E5%92%8C%E7%A2%A9%E9%9B%86%E5%9C%98-073519634.html).
  - TXOne's newsroom shows no later round through 2026-11 — [TXOne news](https://www.txone.com/news/).
- IPO and revenue target: CEO 劉榮太 (Terence Liu) set a goal of US$100M in business, a Series C round, and a US listing "within two to three years", with timing subject to markets. Article date not confirmed (c. 2024–early 2025) — [Liberty Times](https://ec.ltn.com.tw/article/paper/1694296). I found no official revenue disclosure.
- Customers (company-sourced, via media, 2024): "3,600 enterprises". Named critical-infrastructure deployments include Taiwanese reservoirs and Sydney Metro — [Meet/Business Next](https://meet.bnext.com.tw/articles/view/51319); [Business Next](https://www.bnext.com.tw/article/79045/startup-txone-b-plus-round-funding).
- 2025–2026 product and partner record — [TXOne news](https://www.txone.com/news/):
  - Siemens certified TXOne Stellar for WinCC OA (2026-03-25).
  - Foxguard partnership for North American energy (2025-05-29).
  - Sennin OT risk/governance family (2026-04-30).
  - Virtual Portable Inspector (2026-06-30).
  - AI-driven Edge release and vEdgeIPS Pro virtual appliances (2026-09-02), with a claimed ">90%" cut in policy-deployment effort [company claim, unconfirmed].
- Analyst position: Niche Player in the 2026 Gartner CPS MQ, per the vendor summary — [Nozomi MQ page](https://www.nozominetworks.com/gartner-magic-quadrant-cps-protection-platforms).

#### Forescout (US) — private, owned by Advent International and Crosspoint Capital
- Taken private for about $1.9B in 2020, with the merger closing 2020-08-17 — [Forescout IR](https://investors.forescout.com/news-releases/news-release-details/forescout-be-acquired-advent-international-19-billion).
- Barry Mainz became CEO in January 2023, the fourth CEO since 2020 — [BankInfoSecurity](https://www.bankinfosecurity.com/forescout-gets-4th-ceo-since-2020-bringing-in-barry-mainz-a-21007).
- Analyst position: Challenger in the 2026 Gartner CPS MQ, per the vendor summary — [Nozomi MQ page](https://www.nozominetworks.com/gartner-magic-quadrant-cps-protection-platforms).
- I found no 2026 revenue, sale process or funding news.

#### Finite State (US) — private
- 2026-11-10: $27M Series C — [GlobeNewswire](https://www.globenewswire.com/news-release/2026/11/10/3399273/0/en/finite-state-raises-27-million-to-help-device-makers-fight-vulnpocalypse-with-ai-powered-product-security.html):
  - Led by funds managed by The O.H.I.O. Fund, with CIBC Innovation Banking, Energy Impact Partners, Energize Capital and National Grid Partners.
  - Purpose: international expansion and "more autonomous features" — [SecurityWeek](https://www.securityweek.com/finite-state-raises-27-million-to-secure-software-and-firmware-in-connected-devices/).
  - The platform analyses compiled firmware and binaries without needing source code — [SecurityWeek](https://www.securityweek.com/finite-state-raises-27-million-to-secure-software-and-firmware-in-connected-devices/).
  - The company ties the raise to AI-discovered flaws (a "Vulnpocalypse") and to the CRA and FDA premarket rules — [The IT Nerd](https://itnerd.blog/2026/11/10/finite-state-raises-27-million-to-help-device-makers-fight-the-vulnpocalypse-with-ai-powered-product-security/).

#### ONEKEY (Germany) — private
- One recorded round: a seed round on 2023-12-18, amount undisclosed, with eCAPITAL and PwC Germany among investors (aggregator) — [Tracxn](https://tracxn.com/d/companies/onekey/__YpQS3BQoHaF0CRmnNgnA3s0KCo0sudpB2pgcp3N22xk).
- Member of the EU-funded CRACoWi consortium (13 partners), which builds an AI assistant for CRA compliance — [DRJ](https://drj.com/industry_news/onekey-presents-cra-fast-start/).
- Products and recognition:
  - "CRA Fast Start" and continuous firmware monitoring (2026-04-30) — [Security Today](https://securitytoday.com/articles/2026/04/30/new-firmware-monitoring-tool-targets-cyber-resilience-act.aspx).
  - Embedded World 2026 "Best in Show" — [DRJ](https://drj.com/industry_news/onekey-presents-cra-fast-start/).
  - AI agent over firmware scan results (2026-09-01) — [remio](https://www.remio.ai/post/onekey-launches-evidence-first-ai-agent-for-firmware-security).

#### Cybellum (Israel) — owned by LG Electronics (KRX: 066570)
- 2021-09-23/24: LG bought an initial 64% for $140M plus a planned $20M SAFE, implying about $240M. It said it would buy the remaining shares "in the near future". Cybellum stays an independent brand — [SecurityWeek](https://www.securityweek.com/lg-acquire-vehicle-cybersecurity-firm-cybellum/).
- Cybellum says its CSMS tooling helped LG obtain TÜV Rheinland CSMS Level 3 certification (ISO/SAE 21434 / UN R155) in December 2024 [company claim, unconfirmed] — [Cybellum blog](https://cybellum.com/blog/lg-secures-level-3-csms-certification-following-usage-of-cybellums-csms-solutions/).

#### Zero Networks (Israel/US) — private
- 2025-06-03: $55M Series C led by Highland Europe, with F2, PICO, Venrock and USVP. Total raised above $100M. More than 120 staff, about 70 of them in Tel Aviv. Valuation and revenue undisclosed. Since the Series B: revenue +300% and customers tripled [company claim, unconfirmed] — [Calcalist](https://www.calcalistech.com/ctechnews/article/bkbtqi2geg); [SecurityWeek](https://www.securityweek.com/zero-networks-raises-55-million-for-microsegmentation-solution/).
- Product: agentless, automated microsegmentation, plus ZTNA and identity least-privilege — [SecurityWeek](https://www.securityweek.com/zero-networks-raises-55-million-for-microsegmentation-solution/).

#### Illumio (US) — private
- Last confirmed round: $225M Series F on 2021-06-23, at a widely cited $2.75B valuation — [Tracxn](https://tracxn.com/d/companies/illumio/__hhzx9XVNa_svwTE4hXez5CKCdMMj0aqvXugm5o2adYc).
- No IPO; Nasdaq Private Market lists it as private — [Nasdaq Private Market](https://www.nasdaqprivatemarket.com/company/illumio/).
- An IPO is "not on" the CEO's day-to-day plans. The same article reports bookings up nearly 100% and 27 customers above $1M ARR, for an undated fiscal year ending January — [SDxCentral](https://www.sdxcentral.com/news/illumio-rides-microsegmentation-new-wave-no-ipo-rush/).
- One site claims an S-1 was filed 2026-02-15. It conflicts with every other source and I treat it as unreliable — [TechStackIPO](https://www.techstackipo.com/company/illumio).

#### Waterfall Security Solutions (Israel) — private
- Sells hardware-enforced unidirectional gateways and HERA (hardware-enforced remote access, built from paired one-way gateways) — [DCD](https://www.datacenterdynamics.com/en/product-news/waterfall-security-launches-hera-hardware-enforced-remote-access/).
- 2026 activity:
  - Joint OT MDR with Siemens Energy (October 2026), in which data leaves OT one way and Siemens analysts monitor it — [Waterfall](https://waterfall-security.com/ot-insights-center/ot-cybersecurity-insights-center/ot-visibility-waterfall-siemens-energy/).
  - An "entry-level" unidirectional product (May 2026) — [Waterfall OT Insights](https://waterfall-security.com/ot-insights-center/).
  - Data-centre OT partnership with AXYS — [Industrial Cyber](https://industrialcyber.co/news/waterfall-security-and-axys-partner-to-deliver-ot-protection-for-data-centers/).
- I found no funding or revenue disclosures.

#### Radiflow (Israel) — majority-owned by Sabancı Group (Türkiye)
- 2022: Sabancı bought 51% for $45M, with a plan to own the whole company by 2025 — [SecurityWeek](https://www.securityweek.com/sabanci-group-acquires-majority-stake-ot-security-firm-radiflow-45-million/); [Industrial Cyber](https://industrialcyber.co/news/sabanci-group-to-acquire-radiflow-in-a-two-phase-process-focused-on-accelerating-growth/).
- Whether the second phase closed is not confirmed.

#### Cylus (Israel) — private, rail-focused
- $30M Series B (December 2021); total about $57M — [Cylus](https://www.cylus.com/post/cylus-the-global-leader-in-rail-cybersecurity-raises-30m-to-help-protect-trains-and-metros-worldwide).
- Launched Cylus.ai, with AI agent workflows, at InnoTrans in September 2026 — [PR Newswire listing](https://www.prnewswire.com/news/cylus/).

#### Asimily (US) — private, IoMT/healthcare
- KLAS 2026: top score of 96.6 — [Asimily release](https://finance.yahoo.com/news/asimily-leads-vendors-best-klas-133000280.html).
- "In Flight" partner tier (February 2026) — [SecurityBrief](https://securitybrief.news/story/asimily-adds-in-flight-tier-to-scale-iot-security).
- The last funding I found was $10M (November 2021, led by Ridge Ventures), per search results only.

#### Ordr (US) — private
- About $94M raised over 5 rounds (aggregator) — [Tracxn](https://tracxn.com/d/companies/ordr/__YFf67T6_LnRqhCH7RJ7mUTqWZKdXFnkCPE9arVMXANM).
- Joined the Cisco SolutionsPlus programme on 2026-04-06 — [Ordr](https://ordr.net/blog/cisco-solutionsplus).
- A competitor (Asimily) says Ordr "remains independent" with more than 500 enterprise customers — [Asimily](https://asimily.com/blog/ordr-alternatives/).

#### Xage Security (US) — private
- $15M equity round in December 2025, per a 2026-03-18 release titled "Xage Security Hits Record Growth…" — [GlobeNewswire](https://www.globenewswire.com/news-release/2026/03/18/3258084/0/en/xage-security-hits-record-growth-by-architecting-the-future-of-zero-trust-for-ai-and-critical-infrastructure.html). PitchBook labels it a $14.9M Series B3 — [PitchBook](https://pitchbook.com/profiles/company/166357-27).
- Total funding estimates range from $66M to $90M.

#### Elisity (US) — acquired by IonQ (NYSE: IONQ), closed 2026-11-04
- Announced 2026-10-12 — [IonQ 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526419609/ionq-ex99_1.htm):
  - All-stock deal worth up to $1.3B, including an earn-out of up to $150M.
  - Share price collar of $33.07–$49.61.
  - Claims: more than 100 enterprise deployments, revenue and customers doubled y/y, "zero churn among deployed customers" [company claim, unconfirmed].
- Completion — [IonQ](https://ionq.com/news/ionq-completes-acquisition-of-elisity-extending-quantum-security-for-enterprises-and-government):
  - $1.15B of IonQ stock at closing.
  - Earn-out of up to $150M tied to revenue milestones through January 2028.
- Earlier funding: $37M Series B (2024-04-30), led by Insight Partners — [Elisity](https://www.elisity.com/news/elisity-raises-37m-series-b-to-fuel-ai-innovation-in-identity-based-microsegmentation).

#### Incumbents' OT units (brief)
- 2026 Gartner CPS MQ placements, per the vendor summary — [Nozomi MQ page](https://www.nozominetworks.com/gartner-magic-quadrant-cps-protection-platforms):
  - Cisco, Palo Alto Networks, Honeywell and Microsoft: Niche Players.
  - Fortinet and Tenable: Challengers.
- Automation OEMs mostly partner rather than build:
  - Schneider Electric with Nozomi (2025) — [Nozomi](https://www.nozominetworks.com/press-release/nozomi-networks-enters-next-phase-of-growth-as-mitsubishi-electric-completes-acquisition).
  - Siemens certifies TXOne Stellar for WinCC OA — [TXOne](https://www.txone.com/news/).
  - Siemens Energy runs MDR on Waterfall gateways — [Waterfall](https://waterfall-security.com/ot-insights-center/ot-cybersecurity-insights-center/ot-visibility-waterfall-siemens-energy/).
  - Mitsubishi Electric bought Nozomi outright (above).

### Inferences
- Acquirers in 2026 paid strategic prices for visibility/exposure leaders. My calculations:
  - Armis: about 22.8x its >$340M ARR at announcement.
  - Dragos+runZero+NetRise: about 20.1x combined ARR of $208M.
  - Nozomi: about 9.3x 2025 revenue and 12.7x 2024 revenue, on an implied 100% equity value of about $949M (= $883M / 0.93).
  - Nozomi's lower multiple fits its slower 2024 growth (+19%) and its industrial buyer.
- Claroty is now the reference independent. If the ~$3B valuation and >$200M ARR estimates are both right, its Series F implies roughly 15x ARR (my calculation). Neither input is company-confirmed.
- On outside evidence, the "lead" tier is Nozomi, Claroty, Armis and Dragos: four Gartner Leaders (2026-03-03), plus outside buyers paying premium multiples for two of them. Below that tier, the evidence is thinner: TXOne's Niche placement, Forescout's Challenger placement, KLAS for Asimily, and company claims elsewhere.
- Revenue models differ in ways that matter for test (c):
  - Armis is agentless SaaS with ARR.
  - Nozomi is "subscription-driven" but still sells hardware sensors (Guardian, Guardian Air).
  - Claroty mixes SaaS (xDome) with on-premises CTD.
  - TXOne and Waterfall are appliance-heavy, inferred from their product lines; no revenue split is disclosed.
  - Dragos mixes a platform with services (incident response and assessments). Its new majority owner, Accenture, is mainly a labour-hours business.

### Gaps
- No Dragos-only ARR, no Claroty-confirmed ARR, valuation or customer count, and no TXOne revenue (Similarweb's $25–50M estimate is unreliable). There is also no revenue or ARR for Forescout, Illumio, Zero Networks, Waterfall, Radiflow, Cylus, Asimily, Ordr, Xage, ONEKEY, Finite State or Cybellum.
- Armis ARR at closing (April 2026) and since is not disclosed; ServiceNow calls the effect "not material".
- Mitsubishi Electric's FY2026 (to March 2027) quarterly materials were not retrieved. I could not confirm in which reporting segment Nozomi sits; the Industry & Mobility routing is only an organisational hint, or whether purchase-price allocation and goodwill were disclosed.
- Current ownership details not verified:
  - Whether LG now owns 100% of Cybellum.
  - Whether Sabancı completed phase 2 of Radiflow.
  - Moxa's current ownership and TXOne's exact share split. Trend Micro's securities report was not retrieved.
- No IDC MarketScape or Westlands Advisory positions were found. Forrester positions come only from vendor citations.
- Named government contracts and CISA partnerships for these vendors were not retrieved, because the search budget ran out.

---

## 2. Shielding: who actually enforces protection for devices that cannot be patched, versus visibility only — and who remediates IoT firmware

### Takeaway
Four groups of vendors actually enforce protection in front of devices that cannot be patched:
- **TXOne:** inline IPS appliances and virtual appliances, plus endpoint lockdown for legacy hosts.
- **Waterfall:** hardware-enforced one-way gateways, which physically remove the inbound path.
- **Segmentation vendors:** Zero Networks, Elisity, Illumio, and Asimily's NAC-driven segmentation.
- **Claroty:** partially, through "network protection" and secure access.

Armis, Nozomi and most of Dragos's core business are mainly visibility, detection and exposure management, which act through other enforcement points. Phosphorus, now in Dragos, is the clearest example of a vendor that actually remediates device firmware and credentials at scale. Finite State, ONEKEY, Cybellum and NetRise (now Dragos) work on the device-maker side, analysing firmware before shipment.

### Cited Findings
- **Waterfall:** gateways enforce one-way data flow in hardware, so "there is physically no inbound attack path". HERA pairs two one-way gateways for remote access — [Waterfall](https://waterfall-security.com/ot-insights-center/ot-cybersecurity-insights-center/ot-visibility-waterfall-siemens-energy/); [DCD](https://www.datacenterdynamics.com/en/product-news/waterfall-security-launches-hera-hardware-enforced-remote-access/).
- **TXOne:** sells Edge network-security appliances, adding vEdgeIPS Pro virtual appliances and an AI-driven policy release in September 2026. It also sells Stellar endpoint protection certified by Siemens for WinCC OA (2026-03-25), and Element/Portable Inspector agentless inspection (virtual version 2026-06-30). The June 2025 SageOne release added "intelligent vulnerability mitigation" — [TXOne news](https://www.txone.com/news/).
- **Zero Networks:** automated, agentless microsegmentation, plus ZTNA and identity least-privilege. Funding and growth figures are in section 1 — [SecurityWeek](https://www.securityweek.com/zero-networks-raises-55-million-for-microsegmentation-solution/).
- **Elisity:** identity-based microsegmentation, with more than 100 enterprise deployments [company claim] — [IonQ 8-K](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526419609/ionq-ex99_1.htm).
- **Asimily:** supports Security Group ACLs in Cisco ISE, applying segmentation policy by device classification and risk. Enforcement happens through the customer's NAC — [Asimily](https://asimily.com/).
- **Claroty:** product scope includes "network protection" and "secure access" alongside visibility and detection — [SecurityWeek](https://www.securityweek.com/claroty-raises-150-million-in-series-f-funding/). It added "device purpose for segmented network zones" — [Claroty blog](https://claroty.com/blog/claroty-named-a-leader-in-2026-gartner-magic-quadrant-for-cps-protection-platforms).
- **Nozomi:** MELCO describes the core technology as "intrusion detection and visualization" from data collection — [MELCO deck](https://www.mitsubishielectric.com/en/pr/2025/pdf/0909-2.pdf). Nozomi claims its latest Arc is the "industry's first cybersecurity solution to safely automate threat response in operational environments" [company claim, unconfirmed] — [Nozomi](https://www.nozominetworks.com/press-release/nozomi-networks-enters-next-phase-of-growth-as-mitsubishi-electric-completes-acquisition).
- **Dragos / Phosphorus (remediation):** "automates remediation workflows, including password rotations, firmware updates, certificate management, and configuration hardening". Dragos said asset visibility and integrated device intelligence would reach customers first, with automated remediation and a unified platform "to follow" — [Dragos press release](https://www.dragos.com/resource/press-release/dragos-acquires-phosphorus). Phosphorus's July 2026 data sheet describes CVE/KEV/EPSS-enriched firmware discovery, policy-driven upgrades and downgrades, and a firmware content-delivery network [company claim, unconfirmed] — [Phosphorus/Dragos data sheet](https://dragos.brightspotcdn.com/56/6f/a0428d13421aaaa598e7d4fbfe4d/dragos-phosphorus-company-firmware-management-data-sheet0902.pdf).
- **Dragos / Network Perception:** network visibility, segmentation validation and compliance — validation, not enforcement — [Dragos press release](https://www.dragos.com/resource/press-release/dragos-acquires-phosphorus).
- **Device-maker side (before shipment):**
  - Finite State analyses compiled firmware and binaries without source code — [SecurityWeek](https://www.securityweek.com/finite-state-raises-27-million-to-secure-software-and-firmware-in-connected-devices/).
  - ONEKEY does continuous firmware monitoring for CRA — [Security Today](https://securitytoday.com/articles/2026/04/30/new-firmware-monitoring-tool-targets-cyber-resilience-act.aspx).
  - NetRise adds "firmware-level visibility" and a software supply-chain dataset to Dragos — [Accenture newsroom](https://newsroom.accenture.com/news/2026/accenture-to-strengthen-critical-infrastructure-defense-with-end-to-end-cybersecurity-platform-in-age-of-ai-driven-cyber-threats-and-geopolitical-risk).
  - Cybellum runs product-security and CSMS tooling for vehicle and device makers — [Industrial Cyber](https://industrialcyber.co/news/cybellum-adds-features-to-its-product-security-platform-in-support-of-its-cybersecurity-management-system/).
- **Armis:** positioned as cyber exposure management and asset intelligence across IT, OT, IoT and medical devices. ServiceNow is combining it with Security Operations workflows — [ServiceNow 10-Q](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000076/now-20260630.htm); [ServiceNow press release](https://newsroom.servicenow.com/press-releases/details/2025/ServiceNow-to-acquire-Armis-to-expand-cyber-exposure-and-security-across-the-full-attack-surface-in-IT-OT-and-medical-devices-for-companies-governments-and-critical-infrastructure-worldwide/).

### Inferences
- Enforcement taxonomy, judged on the sources above:
  - **Physics-enforced:** Waterfall.
  - **Inline / host-enforced:** TXOne, plus Forescout's NAC heritage (background, not verified this session).
  - **Segmentation-enforced:** Zero Networks, Elisity, Illumio; also Asimily and Claroty through NAC or firewall policy.
  - **Detect-and-orchestrate:** Armis, Nozomi, Dragos core, Ordr. These rely on third-party enforcement points or ServiceNow workflows.
  - **Remediate:** Phosphorus/Dragos.
  - **Prevent at source:** Finite State, ONEKEY, Cybellum, NetRise.
- If AI raises the rate of vulnerability discovery in long-lived devices, the value of a control that does not depend on patching rises. That favours physical one-way controls and enforced segmentation over alert-only visibility. This is reasoning, not an observed market-share shift.
- Phosphorus-style remediation only works where the device maker has published fixed firmware. For end-of-life devices, the evidence on TP-Link end-of-life routers in section 5 shows the fallback is shielding or replacement.

### Gaps
- No independent test (lab benchmarks, MITRE-style evaluations) of how reliable the TXOne IPS or "virtual patching" is, or of how reliably Nozomi's automated response or Phosphorus's remediation work in production. All capability descriptions above are vendor descriptions.
- Xage's enforcement model and Forescout's current enforcement (NAC/eyeSegment) were not verified this session.

---

## 3. Path forward: transitions (3) patching → shielding, (5) device-maker liability and regulation, (2) machine-speed finding and fixing, (4) gated-model access and model-maker competition — said versus done

### Takeaway
- **Done:**
  - Capital committed to shielding and remediation: Dragos buying Phosphorus, NetRise and runZero; IonQ buying Elisity; Zero Networks' Series C; TXOne shipping AI-assisted IPS.
  - Capital committed to regulation-driven firmware security: Finite State's Series C on 2026-11-10, citing CRA and FDA; ONEKEY's CRA products.
- **Mostly still said:** machine-speed fixing claims, such as ServiceNow's "Autonomous Security / Super Intelligence Control Tower", Nozomi's "automated threat response" and Finite State's "more autonomous features".
- **No evidence found:** no vendor in scope disclosed privileged access to gated frontier models, and no model maker's OT/IoT security product was found.

### Cited Findings
- **Transition (3), patching → shielding, done:**
  - Dragos bought Phosphorus (2026-06-01) for remediation, and NetRise and runZero (closed 2026-07-31 and 2026-09-17) for firmware and exposure — [Dragos](https://www.dragos.com/resource/press-release/dragos-acquires-phosphorus); [Accenture](https://newsroom.accenture.com/news/2026/accenture-to-strengthen-critical-infrastructure-defense-with-end-to-end-cybersecurity-platform-in-age-of-ai-driven-cyber-threats-and-geopolitical-risk).
  - IonQ closed Elisity for $1.15B upfront in stock (2026-11-04) — [IonQ](https://ionq.com/news/ionq-completes-acquisition-of-elisity-extending-quantum-security-for-enterprises-and-government).
  - Zero Networks raised $55M (2025-06-03) — [Calcalist](https://www.calcalistech.com/ctechnews/article/bkbtqi2geg).
  - Waterfall launched an entry-level gateway (May 2026) and Siemens Energy MDR (October 2026) — [Waterfall](https://waterfall-security.com/ot-insights-center/).
  - TXOne released AI-driven Edge and vEdgeIPS Pro (2026-09-02) — [TXOne](https://www.txone.com/news/).
- **Transition (3), said:** Dragos says automated remediation "will follow" the visibility integration — [Dragos](https://www.dragos.com/resource/press-release/dragos-acquires-phosphorus).
- **Transition (5), regulation, done:**
  - Finite State raised $27M (2026-11-10), explicitly citing the CRA and FDA premarket rules — [The IT Nerd](https://itnerd.blog/2026/11/10/finite-state-raises-27-million-to-help-device-makers-fight-the-vulnpocalypse-with-ai-powered-product-security/).
  - ONEKEY shipped "CRA Fast Start" and continuous monitoring (April 2026) and joined the EU-funded CRACoWi consortium — [Security Today](https://securitytoday.com/articles/2026/04/30/new-firmware-monitoring-tool-targets-cyber-resilience-act.aspx); [DRJ](https://drj.com/industry_news/onekey-presents-cra-fast-start/).
  - Cybellum's tooling was used in LG's UN R155-aligned CSMS certification in December 2024 [company claim] — [Cybellum](https://cybellum.com/blog/lg-secures-level-3-csms-certification-following-usage-of-cybellums-csms-solutions/).
  - MELCO's rationale cites IEC 62443 and NIST SP 800-82 as making OT measures "mandatory" (company framing) — [MELCO deck](https://www.mitsubishielectric.com/en/pr/2025/pdf/0909-2.pdf).
- **Transition (2), machine-speed finding and fixing, said:**
  - ServiceNow (2026-10-28): "capabilities from Armis and Veza feed directly into the Super Intelligence Control Tower" — [ServiceNow 8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371526000092/erq3fy26.htm).
  - Finite State: "more autonomous features" — [SecurityWeek](https://www.securityweek.com/finite-state-raises-27-million-to-secure-software-and-firmware-in-connected-devices/).
  - Nozomi: Vantage IQ AI assistant and "game changing new innovations" promised for 2026 — [Nozomi](https://www.nozominetworks.com/press-release/nozomi-networks-enters-next-phase-of-growth-as-mitsubishi-electric-completes-acquisition).
  - ONEKEY: AI agent (2026-09-01) — [remio](https://www.remio.ai/post/onekey-launches-evidence-first-ai-agent-for-firmware-security).
  - Cylus.ai (September 2026) — [PR Newswire](https://www.prnewswire.com/news/cylus/).
  - Claroty: AI-powered CPS Library — [Claroty](https://claroty.com/blog/claroty-named-a-leader-in-2026-gartner-magic-quadrant-for-cps-protection-platforms).
- **Funding behind the plans:**
  - ServiceNow: FY2026 FCF margin guidance of 36% — [8-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371526000092/erq3fy26.htm).
  - Accenture: $10B cybersecurity revenue in FY2025 — [Accenture](https://newsroom.accenture.com/news/2026/accenture-to-strengthen-critical-infrastructure-defense-with-end-to-end-cybersecurity-platform-in-age-of-ai-driven-cyber-threats-and-geopolitical-risk).
  - Mitsubishi Electric: forecast operating profit of ¥430B for FY to March 2026 — [MELCO](https://www.mitsubishielectric.com/en/pr/2025/pdf/0909-1.pdf).
  - Claroty: $150M Series F — [SecurityWeek](https://www.securityweek.com/claroty-raises-150-million-in-series-f-funding/).
  - TXOne: last round May 2024 — [TXOne](https://www.txone.com/news/).
- **Transition (4), gated models:** Anthropic reported on 2025-11-13 that a Chinese state-sponsored group used Claude Code to run 80–90% of an espionage campaign against about 30 targets, including chemical manufacturers. The AI wrote its own exploit code. No IoT/OT targeting was reported — [Anthropic](https://www.anthropic.com/news/disrupting-AI-espionage).

### Inferences
Suggested path-forward verdicts (judgement):

| Company | Verdict | Reason |
|---|---|---|
| Armis / ServiceNow | Partly coherent | Funded and integrated into ServiceNow workflows. Enforcement for devices that cannot be patched is still indirect, and Armis's contribution is "not material" to the parent. What must go right: workflow-driven remediation must actually reach OT and medical devices without disrupting them. |
| Nozomi / MELCO | Partly coherent | Funded by an OEM parent. Must keep vendor neutrality while serving Serendie; MELCO's FY2031 target is ¥1.1T. Automated response is still a claim. |
| Claroty | Partly coherent to coherent | Funded; Gartner Leader. The IPO aspiration (2027) needs scale. Shielding exists (network protection, secure access) but depends on integrations. |
| Dragos / Accenture | Partly coherent | Shielding and remediation, firmware and exposure capabilities were actually acquired and closed. Integration is "to follow". Under a labour-hours parent, the platform could be pulled toward services. |
| TXOne | Coherent on transition (3) | Core enforcement products ship. Funding (no round since May 2024) and the IPO plan look slow. |
| Waterfall | Coherent | A physical constraint, with a product extension into remote access and MDR. Financing cannot be assessed. |
| Zero Networks | Coherent | Funded June 2025; enforcement product. |
| Elisity / IonQ | Partly coherent | Deal closed. The quantum-security rationale is a different thesis from OT shielding. |
| Finite State, ONEKEY, Cybellum | Coherent for transition (5) | Regulation-led demand. Exposed to transition (4) if frontier models commoditise binary analysis. |
| Forescout | Cannot assess / partly coherent | PE-owned, with CEO churn, a Challenger placement and no 2026 data. |

- Model-maker competition matters most for the device-maker analysis tools: binary/firmware analysis and SBOM triage are tasks frontier models are getting better at. It matters least for physical one-way controls and installed sensors with years of OT protocol data. This is reasoning, not observed evidence.

### Gaps
- No vendor in scope disclosed a gated frontier-model partnership, model-maker licensing, or country-specific access limits. I found no model-maker OT/IoT security product, given the search limits.
- No independent proof of AI-driven remediation results in OT, such as mean time to remediate or lists of customers who adopted it.

---

## 4. Regulation and liability by jurisdiction (status as of 2026-11-12)

### Takeaway
The EU has moved from law to live obligations. Since 2026-09-11, CRA reporting of actively exploited vulnerabilities and severe incidents has applied through ENISA's Single Reporting Platform. The CRA applies in full from 2027-12-11, but as of October 2026 no harmonised standard had been cited in the Official Journal. The revised Product Liability Directive treats software as a product from products placed on the market after 2026-12-08, but only 3 member states had transposed it by 2026-09-08.

The US is acting through supply-chain bans and state consumer-protection suits rather than a liability statute:
- The FCC's Covered List added foreign drones (2025-12-22), foreign consumer routers (2026-03-23), and robotics and inverters (July 2026).
- Five states have sued TP-Link.
- The Cyber Trust Mark has changed lead administrator twice.

Japan's JC-STAR is maturing (★3 requirements in 2026; mutual recognition with Singapore since 2026-06-01). China amended its Cybersecurity Law with effect from 2026-01-01.

### Cited Findings
**European Union**
- **CRA reporting** — [European Commission](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting):
  - From 2026-09-11, manufacturers must report actively exploited vulnerabilities and severe incidents.
  - Deadlines: early warning within 24h; notification within 72h; final report 14 days after a corrective measure is available (vulnerabilities) or one month after notification (incidents).
  - ENISA's Single Reporting Platform became operational on 2026-09-11. One submission reaches the coordinating CSIRT and ENISA.
  - A delegated act on grounds for CSIRT delay was adopted 2025-12-11.
  - Open-source stewards' reporting starts 2027-12-11.
  - Law firms confirm the platform went live on the day — [Crowell](https://www.crowell.com/en/insights/client-alerts/its-live-the-cyber-resilience-act-reporting-is-mandatory-as-of-today-11-september-2026).
- **CRA full application:** essential requirements apply from 2027-12-11 — [securehabits.nl](https://www.securehabits.nl/knowledge/cra-harmonised-standards-overview/).
- **CRA harmonised standards:**
  - CEN, CENELEC and ETSI accepted the standardisation request on 2025-04-03 — [CEN-CENELEC](https://www.cencenelec.eu/news-events/news/2025/newsletter/ots-62-cra/).
  - Status as of October 2026 — [securehabits.nl](https://www.securehabits.nl/knowledge/cra-harmonised-standards-overview/):
    - EN 40000-1-1 (vocabulary) and EN 40000-1-2 (principles, risk management) adopted.
    - EN 40000-1-3 (vulnerability handling) awaiting its formal vote.
    - EN 40000-1-4 (generic requirements) still a prEN draft.
    - Of 17 ETSI EN 304 6xx vertical standards, 10 were at EN-draft vote (including routers, smart home and firewall/IDS) and 7 at prEN vote.
    - No standard cited in the Official Journal, so there is no presumption of conformity yet.
  - Another tracker says the same about Official Journal citations as of 2026-10-17 — [CRA Evidence](https://craevidence.com/cra-compliance/harmonised-standards-status).
- **NIS2** — [Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/european-commission-refers-four-member-states-to-cjeu-over-nis2-transposition-delays):
  - Transposition deadline 2024-10-17; letters of formal notice 2024-11-28; reasoned opinions to 19 member states 2025-05-07.
  - On 2026-07-08 the Commission referred Ireland, Spain, France and the Netherlands to the CJEU, seeking lump sums and daily penalties.
  - In January 2026 the Commission proposed targeted NIS2 amendments.
- **Product Liability Directive (EU) 2024/2853** — [Reed Smith, 2026-09-08](https://www.reedsmith.com/articles/eu-product-liability-directive-where-things-stand-with-member-state-transposition/):
  - Transposition deadline 2026-12-09.
  - Applies to products placed on the market or put into service after 2026-12-08 (date changed by corrigendum).
  - Software and AI are "products".
  - Courts can order disclosure (Art. 9) and presume defectiveness or causation where proof is excessively difficult (Art. 10(4)). Data loss is recoverable damage.
  - Transposition status at that date:
    - Completed: Hungary, Croatia, Lithuania.
    - Drafts: Belgium, Cyprus, Czechia, Denmark, Finland, Germany, Italy, Netherlands, Poland, Slovakia, Slovenia, Sweden.
    - Initial steps: Austria, Bulgaria, Estonia, France, Ireland, Latvia, Romania.
    - No known progress: Greece, Luxembourg, Malta, Portugal, Spain.

**United States**
- **FCC U.S. Cyber Trust Mark (voluntary label):**
  - UL Solutions withdrew as Lead Administrator effective 2025-12-19, after an FCC national-security investigation into its China ties — [Cybersecurity Dive](https://www.cybersecuritydive.com/news/fcc-cyber-trust-mark-iot-labeling-ul-withdraw/808732/).
  - The replacement application window ran 2026-01-07 to 2026-02-09, extended to 2026-02-24 — [FCC DA 26-75](https://docs.fcc.gov/public/attachments/DA-26-75A1.pdf); [Lexology](https://www.lexology.com/library/detail.aspx?g=39d6f8c1-2ded-48d8-b2d1-fca494dae54e).
  - The FCC programme page lists ioXt Alliance as Lead Administrator effective 2026-04-13. It also lists a 2026-10-28 news item, "Carr Announces Trusty Will Lead U.S. Cyber Trust Mark Program". I saw this only in a search snippet of the page and could not open the release — [FCC](https://www.fcc.gov/CyberTrustMark).
  - A law-firm summary said that, as of the FCC's August 2026 notice, labelling standards and test procedures had not taken effect — [Lexology](https://www.lexology.com/library/detail.aspx?g=39d6f8c1-2ded-48d8-b2d1-fca494dae54e).
- **FCC Covered List:**
  - 2025-12-22: all foreign-produced drones and critical drone components. New models are barred from equipment authorisation; already-authorised models are not prohibited — [Holland & Knight](https://www.hklaw.com/en/insights/publications/2025/12/fcc-adds-all-foreign-made-drones).
  - 2026-03-23: consumer-grade routers produced in any foreign country, unless they hold Conditional Approval from DoW/DHS. This followed a 2026-03-20 National Security Determination — [Baker McKenzie](https://www.bakermckenzie.com/en/insight/publications/2026/04/united-states-fcc-adds-foreign-made-routers-to-covered-list).
  - Conditional approvals public notice, 2026-04-14 — [FCC DA 26-351](https://docs.fcc.gov/public/attachments/DA-26-351A1.pdf).
  - July 2026: advanced robotic devices and power inverters added. New rules bar authorisation of devices containing logic-bearing components (ICs, modules) made by Covered List entities — [Morgan Lewis](https://www.morganlewis.com/pubs/2026/09/fcc-covered-list-expands-as-national-security-controls-reach-deeper-into-technology-supply-chains).
  - Previously authorised routers may keep receiving security updates until at least 2027-03-01 under an FCC waiver — [The Hacker News](https://thehackernews.com/2026/10/tp-link-sued-by-four-more-us-states.html).
  - Chairman Carr's statement on further steps — [FCC-26-50A2](https://docs.fcc.gov/public/attachments/FCC-26-50A2.pdf).
- **State liability actions against TP-Link** — [The Hacker News, 2026-10-09](https://thehackernews.com/2026/10/tp-link-sued-by-four-more-us-states.html):
  - Texas sued in February 2026. Florida, Iowa, Montana and Nebraska sued on 2026-10-06 under consumer-protection laws. The suits allege misleading security, China-separation and privacy claims, citing exploited firmware flaws and end-of-life routers.
  - Remedies sought include injunctions, disgorgement and up to $10,000 per violation (Florida, Montana).
  - 21 attorneys general wrote to the FCC on 2026-10-07.
  - DoD listed TP-Link Technologies (China), not TP-Link Systems (US), as a Chinese military company in June 2026.
  - TP-Link denies the claims.
- **FDA §524B:**
  - The statute requires cyber-device makers to provide a post-market vulnerability plan, processes giving reasonable assurance of cybersecurity, and an SBOM.
  - Premarket cybersecurity guidance was re-finalised on 2026-02-03 to align with the QMSR, which took effect 2026-02-02, replacing the June 2025 version. This comes from vendor summaries, not FDA.gov — [Blue Goat Cyber](https://bluegoatcyber.com/news/regulatory-tracker/fda-2026-premarket-cybersecurity-guidance-finalized).
- **CISA Secure by Design pledge:**
  - Voluntary, with 68 initial signers in May 2024 — [CISA](https://www.cisa.gov/news-events/news/cisa-announces-secure-design-commitments-leading-technology-providers).
  - About 393 signers per a 2026-10-10 capture of CISA's page, reported by a vendor blog. CISA does not verify adherence — [Safeguard](https://safeguard.sh/resources/blog/cisa-secure-by-design-pledge-update-2026).

**United Kingdom**
- PSTI product security regime, in force since 2024-04-29 — [GOV.UK](https://www.gov.uk/government/publications/the-uk-product-security-and-telecommunications-infrastructure-product-security-regime):
  - Three requirements: no universal default passwords; a way to report security issues; a published minimum security-update period.
  - Duties fall on manufacturers, importers and distributors. OPSS (Department for Business and Trade) enforces.
  - The page was last updated 2024-05-02.

**Japan**
- JC-STAR — [IPA](https://www.ipa.go.jp/en/security/jc-star/index.html):
  - Established under METI policy (August 2024); scheme released 2024-09-30.
  - ★1 (self-declared) applications from 2025-03-25.
  - ★3 security requirements for network devices and network cameras released 2026-07-13, with conformance requirements on 2026-09-02. ★3/★4 use third-party evaluation and are meant for government and critical infrastructure.
  - Mutual recognition with Singapore's CLS from 2026-06-01.
  - Application documents for UK PSTI-compliant products from 2026-04-01.

**China**
- Cybersecurity Law amendment adopted 2025-10-28, effective 2026-01-01, including AI-related provisions — [Wikipedia](https://en.wikipedia.org/wiki/Cybersecurity_Law_of_the_People%27s_Republic_of_China).
- The July 2021 Regulations on the Management of Security Vulnerabilities in Network Products require reporting to MIIT and restrict disclosure, including to overseas organisations — [Wikipedia](https://en.wikipedia.org/wiki/Cybersecurity_Law_of_the_People%27s_Republic_of_China).
- The national Cybersecurity Incident Reporting Measures took effect 2025-11-01 — [Wikipedia](https://en.wikipedia.org/wiki/Cybersecurity_Law_of_the_People%27s_Republic_of_China).

**India**
- CERT-In Directions of 2022-04-28 — [CERT-In](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf):
  - Service providers, intermediaries, data centres, body corporates and government bodies must report listed incidents within 6 hours. "Attacks on Internet of Things (IoT) devices and associated systems" are a listed incident type.
  - Logs must be kept for 180 days, and clocks synchronised to NIC/NPL NTP servers.
  - Effective 60 days after issue.

### Inferences
- Liability is moving, in different ways:
  - **EU:** onto manufacturers through regulation (CRA) and strict liability (PLD). From December 2026, the PLD's presumptions and disclosure rules make software defects, including security defects, easier to litigate.
  - **US:** onto foreign-origin devices through supply-chain exclusion, and onto specific brands through state consumer-protection suits. There is still no federal device-security liability statute.
  - This divergence helps firmware/SBOM vendors in the EU (Finite State, ONEKEY, Cybellum). In the US it creates replacement cycles rather than retrofit demand.
- With no harmonised standards cited, more CRA class I/II products may need notified-body assessment before 2027-12-11. That is a near-term tailwind for testing and evidence tools, but it is time-bound.

### Gaps
The search budget ran out before I could verify the following. Background knowledge is given as unverified leads only.
- **UK PSTI:** penalties (background: up to £10m or 4% of worldwide revenue) and any OPSS enforcement actions in 2025–2026.
- **Japan Active Cyber Defense law:** background says it was enacted in May 2025, with phased implementation to about 2027. Unverified.
- **South Korea:** KISA's IoT security certification (background: voluntary, tiered) and penalties after the 2025 telecom breaches. Unverified.
- **Taiwan:** no verified 2025–2026 device-security rules.
- **China:** the 2021 rule's two-day MIIT reporting deadline (background: Art. 7) and the amended CSL's higher fines. Unverified.
- **India:** CCTV "Essential Requirements" under the Compulsory Registration Order (background: effective April 2025), MTCTE telecom testing and the Telecom Cyber Security Rules 2024. Unverified.
- **Singapore CLS:** only the JC-STAR mutual recognition was verified. Levels and the Finland/Germany/Korea recognitions were not.
- **UN R155/R156:** background says these became mandatory for all new EU vehicle registrations from July 2024. The UNECE page returned 403. IEC 62443 certification trends were not researched.
- **FCC Cyber Trust Mark:** whether any product carries the mark yet, and what the 2026-10-28 Trusty announcement actually says.
- **FDA:** the 2026 guidance details need checking on FDA.gov; the sources used are vendor blogs.
- **Fines:** no EU or UK fine against a device maker for a security failure in 2025–2026 was found. That may reflect search limits rather than absence.

---

## 5. Large device compromises 2025–2026 and AI-built exploit attribution (brief)

### Takeaway
Large IoT compromises in 2025–2026 were driven by supply-chain-tainted consumer devices (BADBOX 2.0) and by state actors exploiting end-of-life routers. In the sources I reviewed, no credible party attributed a 2025–2026 IoT botnet or OT incident to AI-built exploits. The nearest documented AI case, Anthropic's November 2025 report, involved IT targets, not devices.

### Cited Findings
- **BADBOX 2.0:** FBI PSA I-060525-PSA (2025-06-05) describes "millions of infected devices": TV streaming boxes, projectors, aftermarket vehicle infotainment, picture frames and other IoT. Most were made in China, and malware was pre-installed or installed during setup — [FBI IC3](https://www.ic3.gov/PSA/2025/PSA250605).
- **State actors on routers:** the FBI said in April 2026 that Russian military intelligence exploited CVE-2023-50224 in TP-Link routers. TP-Link said most affected products were end-of-life. State complaints also cite Microsoft's 2024 report of a China-based botnet made up mostly of TP-Link routers — [The Hacker News](https://thehackernews.com/2026/10/tp-link-sued-by-four-more-us-states.html).
- **AI attribution:** Anthropic (2025-11-13) attributed with high confidence to a Chinese state-sponsored group a campaign in which AI did 80–90% of the work, including writing exploit code, against about 30 targets in tech, finance, chemical manufacturing and government. No IoT/OT devices were mentioned — [Anthropic](https://www.anthropic.com/news/disrupting-AI-espionage).
- **Vendor framing:** Finite State markets its raise around a "Vulnpocalypse" of AI-discovered flaws. This is vendor framing, not attribution — [The IT Nerd](https://itnerd.blog/2026/11/10/finite-state-raises-27-million-to-help-device-makers-fight-the-vulnpocalypse-with-ai-powered-product-security/).

### Inferences
- The compromises that drove policy in 2026 (routers and drones on the Covered List, the TP-Link suits) are about where devices come from and about end-of-life support, not AI. That supports shielding and replacement demand regardless of how the AI-attribution debate turns out.

### Gaps
- Record IoT DDoS botnets of 2025–2026 (for example Aisuru and Kimwolf, from background knowledge), 2025–2026 OT incidents (European water and dam incidents, US water utilities), and Volt or Salt Typhoon device activity were not verified this session. Another researcher covers attribution in depth.

---

## 6. Entry-point data: valuations, implied multiples, exposure routes, size of security units versus listed parents, IPO timing

### Takeaway
None of the 2026 acquisitions gives a listed pure play.
- **Armis:** about 7% of ServiceNow's market value at deal price, about 2% of its revenue.
- **Nozomi:** about 1.5% of Mitsubishi Electric's market cap, about 0.3% of its revenue.
- **Dragos:** about 2% of Accenture's market cap.
- **Cybellum:** about 1% of LG Electronics at its 2021 price.
- **Elisity:** about 7–9% of IonQ.
- **TXOne:** sits inside Trend Micro, a $5.5B company, at an unknown share of value.

Claroty is the only scaled private candidate for a pure-play listing (aspiration: 2027). Dragos's IPO path was overtaken by Accenture's majority stake.

### Cited Findings
- **Market caps around 2026-11-11** (CompaniesMarketCap; sources differ where noted):
  - ServiceNow: $106.65B, share price $102.76; Nasdaq shows $106.64B — [CMC](https://companiesmarketcap.com/servicenow/marketcap/).
  - Mitsubishi Electric: $64.32B — [CMC](https://companiesmarketcap.com/mitsubishi-electric/marketcap/).
  - LG Electronics: $18.57B — [CMC](https://companiesmarketcap.com/lg-electronics/marketcap/).
  - Trend Micro: $5.46B, still listed — [CMC](https://companiesmarketcap.com/trend-micro/marketcap/).
  - Accenture: $149.84B per CMC versus $169.61B per Nasdaq, a conflict — [CMC](https://companiesmarketcap.com/accenture/marketcap/).
  - IonQ: $15.82B per CMC versus $14.72B per Nasdaq — [CMC](https://companiesmarketcap.com/ionq/marketcap/).
- **Deal and round prices:**
  - Armis: $7.75B announced; $7.6B preliminary consideration — [10-Q](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000076/now-20260630.htm).
  - Dragos: $3.25B; with runZero and NetRise, $4.175B combined EV — [SecurityWeek](https://www.securityweek.com/accenture-to-acquire-majority-stake-in-dragos-all-of-runzero-netrise-in-4-1-billion-ot-cybersecurity-push/).
  - Nozomi: $883M for 93% — [MELCO](https://www.mitsubishielectric.com/en/pr/2025/pdf/0909-1.pdf).
  - Elisity: $1.15B upfront plus up to $150M earn-out — [IonQ](https://ionq.com/news/ionq-completes-acquisition-of-elisity-extending-quantum-security-for-enterprises-and-government).
  - Cybellum: about $240M implied (2021) — [SecurityWeek](https://www.securityweek.com/lg-acquire-vehicle-cybersecurity-firm-cybellum/).
  - Radiflow: 51% for $45M (2022) — [SecurityWeek](https://www.securityweek.com/sabanci-group-acquires-majority-stake-ot-security-firm-radiflow-45-million/).
  - Claroty: about $3B reported (January 2026) — [SecurityWeek](https://www.securityweek.com/claroty-raises-150-million-in-series-f-funding/).
  - Illumio: $2.75B (2021) — [Tracxn](https://tracxn.com/d/companies/illumio/__hhzx9XVNa_svwTE4hXez5CKCdMMj0aqvXugm5o2adYc).
- **Trend Micro sale interest:** reported interest from Bain, Advent, EQT and KKR in February 2025; no deal found through November 2026 — [Reuters via Investing.com](https://www.investing.com/news/stock-market-news/exclusivebuyout-firms-vie-for-cybersecurity-firm-trend-micro-sources-say-3866262); [CMC](https://companiesmarketcap.com/trend-micro/marketcap/).
- **Secondary-market venues** list Claroty, Dragos and Illumio for accredited investors (presence only; no prices verified) — [Forge Claroty](https://forgeglobal.com/claroty_ipo/); [UpMarket Claroty](https://www.upmarket.co/private-markets/pre-ipo/claroty/); [Nasdaq Private Market Dragos](https://www.nasdaqprivatemarket.com/company/dragos/).

### Inferences
My calculations from the sources above.

**Implied multiples**

| Company | Price | Multiple |
|---|---|---|
| Armis | $7.75B | ≈22.8x ARR (>$340M, December 2025) |
| Dragos group | $4.175B | ≈20.1x ARR ($208M, June 2026) |
| Nozomi | ≈$949M (100%) | ≈9.3x 2025 revenue; ≈12.7x 2024 revenue |
| Claroty | ≈$3B | ≈15x ARR (>$200M press estimate); low confidence |

**Unit size relative to listed parent**

| Unit / parent | Share of parent market cap | Other measure |
|---|---|---|
| Armis / ServiceNow | $7.6B ≈ 7.1% | ARR ≈ 2.2% of FY2026 subscription guidance ($15.785B) |
| Nozomi / MELCO | ≈$0.95B ≈ 1.5% | 2025 revenue ≈ 0.28% of MELCO FY to March 2025 revenue (¥5,521.7B ≈ $36.8B at ¥150) |
| Dragos / Accenture | $3.25B ≈ 2.2% (CMC) or 1.9% (Nasdaq) | Combined ARR ≈ 2% of Accenture's $10B cyber revenue |
| Cybellum / LG | ≈$0.24B ≈ 1.3% | At 2021 value |
| Elisity / IonQ | ≈$1.15–1.3B ≈ 7–9% | — |

**ServiceNow as a whole**
- EV ≈ $106.65B + $7.52B debt − $6.96B cash and marketable securities ≈ $107.2B, excluding $2.05B of strategic investments.
- FY2026 revenue ≈ $16.2–16.3B: subscription guidance plus about 3% professional services, inferred from the Q3 mix.
- So EV/revenue ≈ 6.6x and EV/FCF ≈ 18x at 36% FCF margin guidance. Approximate.

**Exposure routes**
- Armis, Nozomi, Dragos, Cybellum: only via NOW, 6503, ACN and 066570, each heavily diluted.
- TXOne: via Trend Micro (4704) and Moxa if listed (unknown).
- Elisity: via IONQ, which mostly carries quantum exposure.
- Claroty: private secondaries for accredited investors only, or a potential IPO from 2027.
- Zero Networks, Illumio, Forescout, Waterfall, Asimily, Ordr, Xage, Cylus, Finite State, ONEKEY: no public route found.

Suggested entry labels, kept separate from quality:

| Company | Label | Reason |
|---|---|---|
| Armis via NOW | Fair for NOW as a whole; cannot assess as Armis exposure | Armis is too small a share of NOW. |
| Nozomi via MELCO | Cannot assess | Nozomi is immaterial to MELCO. |
| Claroty | Fair, low confidence | About 15x estimated ARR, below the 20–23x strategic deal marks; inputs unconfirmed. |
| Dragos via ACN | Cannot assess | — |
| TXOne via Trend Micro | Cannot assess | No TXOne financials. |
| Cybellum via LG | Cannot assess | — |
| Elisity via IonQ | Cannot assess | No ARR disclosed. |
| Other private companies | Cannot assess | — |

### Gaps
- No P/E or multiples for MELCO, LG, Trend Micro or Accenture were retrieved, and no Mitsubishi Electric segment data.
- Claroty's secondary prices and any 2026 tender offer pricing were not retrieved.
- Accenture's exact stake in Dragos and the minority holders are undisclosed.
- No Elisity ARR, so no implied multiple.
- Moxa's listing status and ownership are unknown.

---

## 7. Synthesis: per-company scorecard, regulation table, exclusions, dated source list

### Takeaway
On business position, the strongest assets are:
- A physical constraint (Waterfall).
- Enforcement points sitting in front of devices that cannot be patched (TXOne; Zero Networks and Elisity segmentation).
- Large installed sensor and data bases with Gartner-Leader validation (Nozomi, Claroty, Armis, Dragos).

Phosphorus inside Dragos is the main actual "fixer". The device-maker analysis firms are the most regulation-dependent group and the most exposed to frontier-model commoditisation. The scorecards below are judgements built on the cited findings in sections 1–6.

### Cited Findings

#### Regulation table (status as of 2026-11-12; sources in section 4)

| Jurisdiction / instrument | Status | Key dates | Who bears the obligation or liability |
|---|---|---|---|
| EU CRA (Reg. 2024/2847) | Reporting live; ENISA SRP operational | Reporting from 2026-09-11; full application 2027-12-11; OSS stewards 2027-12-11; no harmonised standard cited in the Official Journal as of October 2026 | Manufacturers report. Importer and distributor duties are background knowledge, not verified this session |
| EU NIS2 (Dir. 2022/2555) | IE, ES, FR, NL referred to the CJEU on 2026-07-08 for not notifying full transposition; trackers disagree on the exact count of transposed states | Deadline 2024-10-17; reasoned opinions to 19 member states 2025-05-07; amendment proposal January 2026 | Essential and important entities in critical sectors (operators, not device makers) |
| EU PLD (Dir. 2024/2853) | 3 of 27 transposed as of 2026-09-08 (HU, HR, LT) | Transposition by 2026-12-09; products placed on the market after 2026-12-08 | Economic operators: strict liability for defective products, software included |
| US FCC Covered List | Active, expanding | Drones 2025-12-22; routers 2026-03-23; robotics, inverters and logic-bearing components July 2026; router update waiver to at least 2027-03-01 | Foreign producers and importers (new models cannot be authorised) |
| US FCC Cyber Trust Mark | Voluntary; administrator turnover | UL out 2025-12-19; ioXt from 2026-04-13; Trusty named 2026-10-28 (unopened) | Volunteering manufacturers |
| US FDA §524B | Binding statute; guidance re-finalised 2026-02-03 (vendor-sourced) | QMSR effective 2026-02-02 | Cyber-device makers (premarket submissions) |
| US CISA Secure by Design | Voluntary pledge, about 393 signers (2026-10-10 capture) | Since May 2024 | Self-attesting software makers |
| US state attorneys general | 5 suits against TP-Link | Texas February 2026; FL, IA, MT, NE 2026-10-06 | Device brand owner (consumer-protection law) |
| UK PSTI | In force | Since 2024-04-29 | Manufacturers, importers, distributors; OPSS enforces |
| Japan JC-STAR | Voluntary label maturing | ★1 from 2025-03-25; ★3 requirements 2026-07-13 and 2026-09-02; Singapore mutual recognition from 2026-06-01 | Vendors (★1/★2 self-declared; ★3/★4 third-party evaluated) |
| China CSL amendment and vulnerability rules | In force | CSL amendment 2026-01-01; incident measures 2025-11-01; vulnerability rules 2021 | Network operators and product providers (report to MIIT) |
| India CERT-In Directions | In force | 2022-04-28 (+60 days); 6-hour reporting, IoT attacks included | Service providers, intermediaries, data centres, body corporates |
| Korea, Taiwan, Singapore detail, UN R155/R156, IEC 62443 | Not verified this session | See section 4 Gaps | — |

#### Dated source list (all accessed 2026-11-12)
**Companies**
- ServiceNow, Armis announcement (2025-12-22): https://newsroom.servicenow.com/press-releases/details/2025/ServiceNow-to-acquire-Armis-to-expand-cyber-exposure-and-security-across-the-full-attack-surface-in-IT-OT-and-medical-devices-for-companies-governments-and-critical-infrastructure-worldwide/
- ServiceNow 10-Q, Q2 2026 (period to 2026-06-30): https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000076/now-20260630.htm
- ServiceNow Q3 2026 8-K (2026-10-28): https://www.sec.gov/Archives/edgar/data/1373715/000137371526000092/erq3fy26.htm
- Armis Gartner MQ release (2026-03-04): https://www.businesswire.com/news/home/20260304220653/en/Armis-Named-a-Leader-for-Second-Consecutive-Year-in-2026-Gartner-Magic-Quadrant-for-CPS-Protection-Platforms
- Mitsubishi Electric releases: 0909-1 (2025-09-09) https://www.mitsubishielectric.com/en/pr/2025/pdf/0909-1.pdf; deck 0909-2 (2025-09-09) https://www.mitsubishielectric.com/en/pr/2025/pdf/0909-2.pdf; 0129 (2026-01-29) https://www.mitsubishielectric.com/en/pr/2026/pdf/0129.pdf
- Nozomi completion release (2026-01-28): https://www.nozominetworks.com/press-release/nozomi-networks-enters-next-phase-of-growth-as-mitsubishi-electric-completes-acquisition; MQ page: https://www.nozominetworks.com/gartner-magic-quadrant-cps-protection-platforms
- Claroty MQ blog (2026-03-09): https://claroty.com/blog/claroty-named-a-leader-in-2026-gartner-magic-quadrant-for-cps-protection-platforms
- SecurityWeek, Claroty Series F (2026-01-22): https://www.securityweek.com/claroty-raises-150-million-in-series-f-funding/
- Accenture, Dragos release (2026-06-18, closing note added later): https://newsroom.accenture.com/news/2026/accenture-to-strengthen-critical-infrastructure-defense-with-end-to-end-cybersecurity-platform-in-age-of-ai-driven-cyber-threats-and-geopolitical-risk
- SecurityWeek, Dragos (2026-06-18): https://www.securityweek.com/accenture-to-acquire-majority-stake-in-dragos-all-of-runzero-netrise-in-4-1-billion-ot-cybersecurity-push/
- SecurityWeek, Dragos closings (2026-09-21): https://www.securityweek.com/dragos-completes-netrise-and-runzero-acquisitions-following-accenture-deal/
- Dragos, Phosphorus acquisition (2026-06-01): https://www.dragos.com/resource/press-release/dragos-acquires-phosphorus
- TXOne newsroom (through 2026-09): https://www.txone.com/news/
- Business Next, TXOne B+ round (2024-05): https://www.bnext.com.tw/article/79045/startup-txone-b-plus-round-funding
- Liberty Times, TXOne IPO plan (c. 2024–25): https://ec.ltn.com.tw/article/paper/1694296
- Finite State Series C (2026-11-10): https://www.globenewswire.com/news-release/2026/11/10/3399273/0/en/finite-state-raises-27-million-to-help-device-makers-fight-vulnpocalypse-with-ai-powered-product-security.html; https://www.securityweek.com/finite-state-raises-27-million-to-secure-software-and-firmware-in-connected-devices/
- IonQ, Elisity announcement 8-K (2026-10-12): https://www.sec.gov/Archives/edgar/data/0001824920/000119312526419609/ionq-ex99_1.htm; completion (2026-11-04): https://ionq.com/news/ionq-completes-acquisition-of-elisity-extending-quantum-security-for-enterprises-and-government
- Calcalist, Zero Networks (2025-06-03): https://www.calcalistech.com/ctechnews/article/bkbtqi2geg
- SecurityWeek, LG–Cybellum (2021-09-24): https://www.securityweek.com/lg-acquire-vehicle-cybersecurity-firm-cybellum/
- SecurityWeek, Sabancı–Radiflow (2022): https://www.securityweek.com/sabanci-group-acquires-majority-stake-ot-security-firm-radiflow-45-million/
- CompaniesMarketCap pages (around 2026-11-11): ServiceNow, Mitsubishi Electric, LG Electronics, Trend Micro, Accenture, IonQ (URLs in section 6)

**Regulation**
- European Commission, CRA reporting (2026): https://digital-strategy.ec.europa.eu/en/policies/cra-reporting
- securehabits.nl, CRA standards (October 2026): https://www.securehabits.nl/knowledge/cra-harmonised-standards-overview/
- Hunton, NIS2 (2026-07-09): https://www.hunton.com/privacy-and-cybersecurity-law-blog/european-commission-refers-four-member-states-to-cjeu-over-nis2-transposition-delays
- Reed Smith, PLD (2026-09-08): https://www.reedsmith.com/articles/eu-product-liability-directive-where-things-stand-with-member-state-transposition/
- FCC Cyber Trust Mark page (2026): https://www.fcc.gov/CyberTrustMark
- Cybersecurity Dive, UL exit (December 2025): https://www.cybersecuritydive.com/news/fcc-cyber-trust-mark-iot-labeling-ul-withdraw/808732/
- Holland & Knight, drones (December 2025): https://www.hklaw.com/en/insights/publications/2025/12/fcc-adds-all-foreign-made-drones
- Baker McKenzie, routers (April 2026): https://www.bakermckenzie.com/en/insight/publications/2026/04/united-states-fcc-adds-foreign-made-routers-to-covered-list
- Morgan Lewis, Covered List (September 2026): https://www.morganlewis.com/pubs/2026/09/fcc-covered-list-expands-as-national-security-controls-reach-deeper-into-technology-supply-chains
- The Hacker News, TP-Link suits (2026-10-09): https://thehackernews.com/2026/10/tp-link-sued-by-four-more-us-states.html
- GOV.UK PSTI (page updated 2024-05-02): https://www.gov.uk/government/publications/the-uk-product-security-and-telecommunications-infrastructure-product-security-regime
- IPA JC-STAR (2026 updates): https://www.ipa.go.jp/en/security/jc-star/index.html
- Wikipedia, China CSL (accessed 2026-11-12): https://en.wikipedia.org/wiki/Cybersecurity_Law_of_the_People%27s_Republic_of_China
- CERT-In Directions (2022-04-28): https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf

**Incidents and AI**
- FBI IC3 BADBOX 2.0 PSA (2025-06-05): https://www.ic3.gov/PSA/2025/PSA250605
- Anthropic, AI-orchestrated espionage (2025-11-13): https://www.anthropic.com/news/disrupting-AI-espionage

### Inferences

#### Per-company scorecards (judgements; tests a–e on business position only, entry kept separate)

**Armis (ServiceNow)**
- (a) Position: owns a large cross-domain asset and exposure dataset (IT, OT, IoMT), now feeding ServiceNow workflows. No physical constraint; detection and prioritisation rather than a final "judge". Medium.
- (b) Lead: 2026 Gartner Leader (second year); ServiceNow paid about 22.8x ARR. Strong.
- (c) Revenue model: agentless SaaS ARR (>$340M, December 2025). Recurring. Strong.
- (d) Financial strength: standalone margins undisclosed. The parent has a 36% FCF margin guide and roughly neutral net debt after deal financing. Strong via the parent.
- (e) Resilience: mostly driven by regulation and asset owners, so steady in all three AI scenarios. A 2028 financing pause would hit ServiceNow's multiple more than Armis demand. Israeli R&D adds geopolitical risk. Medium-high.
- Path: partly coherent.
- Entry: only via NOW, where Armis is about 7% of value. NOW at about 6.6x EV/revenue (my estimate). Label: fair for NOW; cannot assess as Armis exposure.

**Nozomi Networks (Mitsubishi Electric)**
- (a) Position: passive OT/IoT sensors (including inside PLCs via Arc Embedded) plus an OEM installed base. Detection, not enforcement. Medium.
- (b) Lead: 2026 Gartner Leader; Forrester IoT Leader (vendor-cited); top-10 customer claims unconfirmed. Strong.
- (c) Revenue model: "subscription-driven", with some hardware sensors; gross margin above 70%. Medium-strong.
- (d) Financial strength: revenue $101.7M in 2025 (+36%); break-even claim unconfirmed; parent very strong. Medium-strong.
- (e) Resilience: industrial and infrastructure demand drivers; under a Japanese parent it is somewhat insulated from US–China device bans. Risk that its neutrality is questioned by MELCO's competitors. Medium-high.
- Path: partly coherent.
- Entry: about 1.5% of MELCO's cap. Label: cannot assess.

**Claroty**
- (a) Position: CPS visibility and exposure plus network protection and secure access; strong in healthcare (named hospital customers). Medium.
- (b) Lead: 2026 Gartner Leader (second year); Forrester IoT Leader Q3 2025 (vendor-cited). Strong.
- (c) Revenue model: SaaS (xDome) plus on-premises CTD; recurring. Strong.
- (d) Financial strength: "path to profitability", no figures; about $900M raised; $150M fresh in January 2026. Medium (cannot verify).
- (e) Resilience: regulation-driven demand. As an independent it depends on IPO markets (2027 aspiration), so a 2028 financing pause is its main risk. Israeli base. Medium.
- Path: partly coherent to coherent.
- Entry: about $3B (reported), about 15x estimated ARR; accredited secondaries only. Label: fair, low confidence.

**Dragos (Accenture majority)**
- (a) Position: OT threat intelligence and detection, plus remediation (Phosphorus), firmware (NetRise) and exposure (runZero). Detection plus a growing ability to fix. Medium-high.
- (b) Lead: 2026 Gartner Leader (second year); Accenture paid about 20x combined ARR. Strong.
- (c) Revenue model: platform subscription plus services (IR, assessments), with no split disclosed. The parent is labour-hours heavy. Medium.
- (d) Financial strength: standalone undisclosed; combined ARR $208M (+53%); parent strong. Medium-strong.
- (e) Resilience: critical-infrastructure and data-centre exposure. Accenture's consulting cycle could pull the platform toward bespoke services. Low export-control exposure. Medium.
- Path: partly coherent.
- Entry: about 2% of ACN. Label: cannot assess.

**TXOne Networks**
- (a) Position: owns enforcement points for legacy and unpatchable OT (inline IPS, endpoint lockdown, Siemens-certified). Medium-high.
- (b) Lead: Gartner Niche Player 2026; Siemens certification; claims of 3,600 enterprises and named infrastructure deployments (company-sourced). Medium.
- (c) Revenue model: appliance-heavy, inferred; mix undisclosed. Medium-weak.
- (d) Financial strength: no disclosures; last round May 2024; a Trend Micro majority owner. Cannot assess.
- (e) Resilience: semiconductor and manufacturing customer base ties it to the AI hardware cycle. That is positive in the steady and acceleration scenarios and negative in a 2028 pause. Taiwan cross-strait risk. Medium.
- Path: coherent on transition (3).
- Entry: via Trend Micro ($5.46B), share unknown. Label: cannot assess.

**Forescout**
- (a) Position: NAC/enforcement heritage (background, not verified). Medium.
- (b) Lead: Gartner Challenger 2026 (vendor summary). Medium.
- (c) Revenue model: unknown.
- (d) Financial strength: PE-owned since 2020; four CEOs since 2020. Weak or unknown.
- (e) Resilience: cannot assess.
- Path: partly coherent / cannot assess.
- Entry: no route. Label: cannot assess.

**Finite State**
- (a) Position: binary/firmware analysis producing CRA and FDA evidence. A gap that frontier models may close. Medium-weak.
- (b) Lead: no outside ranking found; investors include strategic utility VCs (National Grid Partners, Energy Impact). Weak-medium.
- (c) Revenue model: presumably SaaS (not disclosed).
- (d) Financial strength: $27M Series C on 2026-11-10. Cannot assess.
- (e) Resilience: regulation-led, so insulated from AI capex; highly exposed to transition (4). Medium.
- Path: coherent for transition (5).
- Entry: no route. Label: cannot assess.

**ONEKEY**
- (a) Position: automated firmware analysis; EU CRA focus; EU-funded consortium member. Medium-weak (same model-commoditisation risk).
- (b) Lead: Embedded World 2026 award only. Weak.
- (c) Revenue model: unknown.
- (d) Financial strength: seed round December 2023 only (aggregator). Weak or unknown.
- (e) Resilience: tied to the CRA calendar; demand peaks before 2027-12-11. Medium.
- Path: coherent for transition (5).
- Entry: no route. Label: cannot assess.

**Cybellum (LG)**
- (a) Position: product security and CSMS for vehicle and device makers, tied to UN R155 type approval. Medium.
- (b) Lead: LG CSMS Level 3 (company-cited). Weak-medium.
- (c), (d): unknown.
- (e) Resilience: automotive cycle exposure. Medium.
- Path: coherent for transition (5), not evidenced.
- Entry: about 1% of LG. Label: cannot assess.

**Zero Networks**
- (a) Position: automated, agentless segmentation, which enforces even when patching is impossible. Medium-high.
- (b) Lead: no outside ranking verified this session. Weak-medium.
- (c) Revenue model: subscription (inferred).
- (d) Financial strength: $55M (June 2025); growth claims unconfirmed. Medium.
- (e) Resilience: broad IT/OT applicability; Israeli base. Medium.
- Path: coherent.
- Entry: no route. Label: cannot assess.

**Illumio**
- (a) Position: host-based segmentation enforcement (background). Medium.
- (b) Lead: no 2026 evidence. Weak-medium.
- (c), (d): unknown; last round 2021.
- (e) Resilience: valuation reset risk. Medium-weak.
- Path: cannot assess.
- Entry: no route. Label: cannot assess.

**Waterfall Security Solutions**
- (a) Position: a physical one-way constraint that AI cannot remove. Strongest.
- (b) Lead: OEM validation (Siemens Energy MDR). Medium.
- (c) Revenue model: hardware-heavy (inferred). Medium-weak.
- (d) Financial strength: unknown.
- (e) Resilience: strong in all three scenarios; data-centre OT link. High.
- Path: coherent.
- Entry: no route. Label: cannot assess.

**Radiflow, Cylus, Asimily, Ordr, Xage**
- Small, niche positions:
  - Radiflow: under Sabancı.
  - Cylus: rail; Alstom ties (aggregator).
  - Asimily: KLAS 2026 top score; segmentation via Cisco ISE.
  - Ordr: Cisco SolutionsPlus.
  - Xage: $15M round December 2025.
- Tests c and d cannot be assessed for any of them. Path: partly coherent. Entry: cannot assess.

**Elisity (IonQ)**
- (a) Position: identity-based segmentation enforcement. Medium-high.
- (b) Lead: >100 deployments (company claim). Medium-weak.
- (c) Revenue model: "significant recurring revenue" (claim).
- (d) Financial strength: parent cash and stock; no ARR.
- (e) Resilience: now tied to IonQ's quantum strategy. Medium-weak.
- Path: partly coherent.
- Entry: about 7–9% of IONQ. Label: cannot assess.

#### Companies considered and excluded or covered only briefly (with reasons)
- **Covered inside their acquirers:** runZero and NetRise (in Dragos since 2026-07/09); Network Perception (in Dragos since October 2024); Veza (ServiceNow identity security, not device security).
- **Incumbents covered briefly per the brief:** Cisco Cyber Vision, Microsoft Defender for IoT, Palo Alto Networks, Fortinet, Honeywell and Tenable (2026 MQ Niche Players or Challengers, per vendor summary); Siemens, Rockwell and Schneider Electric (mainly partner models).
- **Darktrace:** 2026 MQ Visionary per vendor summary. Excluded as IT-led and outside the named list.
- **Earlier acquisitions not verified this session (background only):** SCADAfence (Honeywell), Verve Industrial (Rockwell), Medigate (Claroty), OTORIO (Armis).
- **Not researched because the search budget ran out:** Shift5, Sepio, Cylera, OPSWAT, Akamai Guardicore, ColorTokens, Fortress Information Security.

### Gaps
- The scorecards depend heavily on company or vendor-cited claims for tests (c) and (d), because most companies disclose no revenue mix, margins or concentration.
- Customer or country concentration is not disclosed for any company in scope.
- The web-search budget ran out mid-session, which limited verification of Asian regulation, incident data and several smaller vendors.
