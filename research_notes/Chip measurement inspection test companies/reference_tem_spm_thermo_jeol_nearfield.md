# Reference measurement by electron microscope and scanning probe: Thermo Fisher (semiconductor EM), JEOL, ZEISS, Tescan, Nearfield Instruments and the independent analysis labs

Research date: 12 November 2026. Prices and multiples were checked on 11-12 Nov 2026.
Status: INTERIM version, written after a usage-limit interruption. Sections marked [INCOMPLETE] are still being worked on.

Labels used below:
- "company claim, unconfirmed" means only the company says it.
- "derived" means my own arithmetic from the cited figures.
- "snippet only" means I saw it in a search-result excerpt but could not open the page.
- ¥1億 = ¥100 million. "FY3/2026" means the fiscal year ended 31 March 2026.

Status of the latest quarter for each company (as of 12 Nov 2026):
- **Thermo Fisher:** Q3 2026 published 21 Oct 2026; the 10-Q was filed 30 Oct 2026.
- **JEOL:** first half of FY3/2027 (Apr-Sep 2026) **not yet published**. It is due 13 Nov 2026, with the briefing on 19 Nov 2026 ([JEOL IR schedule](https://www.jeol.co.jp/ir/schedule.html)). The latest JEOL figures are Q1 (Apr-Jun 2026, published 14 Aug 2026).
- **Taiwanese labs:** iST reports Q3 on 13 Nov 2026; MA-tek and MSScorps on 16 Nov 2026 (next-earnings dates on stockanalysis.com). For Q3 2026 only monthly revenue is public.
- **ZEISS:** FY2025/26 (to 30 Sep 2026) is not yet published. The prior year came out 18 Dec 2025.

---

## 1. Compact evidence tables

### 1.1 Thermo Fisher Scientific (NYSE: TMO): semiconductor electron microscopy, inside the Analytical Instruments segment

| Test | Dated evidence |
|---|---|
| (a) Position | **Owns the instrument and automation layer of the destructive reference step, not the data.**<br>- Thermo Fisher says TEM "serves as the primary source for reference data in semiconductor design and fabrication".<br>- It also says "leading manufacturers generate tens of thousands of TEM datasets monthly" for process-variation analysis, fab-tool calibration, defect mechanisms and quality control (blog, 14 Aug 2025; company claim, unconfirmed) [S14].<br>- The datasets are produced on tools in the customers' own labs and fabs. I found no Thermo Fisher data product. |
| (b) Lead | **No third-party share** for semiconductor TEM or FIB-SEM was found (no Gartner, TechInsights, Yole or SEMI figure). Market-research aggregators conflict and are not usable (one gives TMO 55-60% of electron microscopy overall, mostly cryo-EM; another gives TMO 35%, ZEISS 22%, JEOL 18%, Hitachi 12%) [S39].<br>- R&D World (19 Mar 2025), an independent outlet, names rival automation efforts at JEOL and Hitachi, and in-house systems at Intel and imec [S11].<br>- Q3 2026: segment growth was "helped by demand for electron microscopes from semiconductor customers, the company said" (press report) [S6]. |
| (c) Revenue model | EM revenue, and its split between hardware and service, is **not disclosed**.<br>- At group level, Q3 2026 product revenue was $6,753M (+4.1%) and service revenue $5,384M (+16.2%) [S4]. The service line is dominated by biopharma services, so it says nothing about EM.<br>- No usage-based or data revenue found. |
| (d) Financial strength | **Group FY2025:**<br>- Revenue $44,556M (+4%; organic +2%); adjusted operating margin 22.7%; free cash flow $6,337M [S2].<br>- Analytical Instruments: $7,554M (17.0% of the group), segment margin 23.0% (26.2% in 2024; the fall is put down to tariffs and FX) [S2][S3].<br>**Q3 2026:**<br>- Group revenue $12,137M (+9%; organic +6%); adjusted operating margin 24.5%.<br>- Analytical Instruments: $2,002M (+5.8%, derived); margin 26.9% (22.6% a year earlier) [S1].<br>**Balance sheet and returns:**<br>- At 26 Sep 2026: debt $41.37B against cash $5.46B plus $0.60B short-term investments, so net debt ≈ $35.3B (derived) [S1].<br>- Leverage at the end of Q1 2026: 3.8x gross, 3.5x net [S5].<br>- ROIC 9.0% (Nov 2026) against 15.2% in FY2021 [S18].<br>**Customer and country concentration:** none disclosed for EM. China fell in 2025 [S3], declined at a low-single-digit rate in Q1 2026 [S5] and grew at a low-double-digit rate in Q3 2026 [S6]. |
| (e) Resilience | Semiconductor EM is a small part of a group with about $48B of revenue, driven mainly by pharma and biotech.<br>- Analytical Instruments organic growth was -2% in Q1 2026 [S5], followed by growth led by EM in Q2-Q3 2026 [S6][S40].<br>- Tariffs cut the segment margin by 3.2 points in 2025 [S3].<br>- Export controls: only generic risk-factor language [S3]. |
| Transitions | (1) No inference or stated-uncertainty product; everything images or measures directly [S10][S12].<br>(2) Vulcan "AI-enhanced imaging", pitched as relief for lab "labor constraints" (company claim) [S11].<br>(3) Helios MX1 (Oct 2025) for "logic, memory, and advanced packaging"; a 2026 blog series on 2.5D/3D packaging failure analysis [S10][S17].<br>(4) No software or data revenue line.<br>(5) Vulcan offers "real-time lab-to-fab data exchange" and a fab host connection, so it runs on the customer's premises [S11][S13].<br>(6) No statement found. |
| Entry point | $717.71 (close 11 Nov 2026); market cap $265.9B; EV $301.2B.<br>- P/E 37.8x trailing, 26.7x forward.<br>- EV/EBITDA 24.8x, against 20.4-22.4x at FY2021-25 year-ends.<br>- FY2026 guidance raised 21 Oct 2026: revenue $47.7-48.2B, adjusted EPS $25.13-25.43 [S7][S18]. |

### 1.2 JEOL (TSE: 6951)

| Test | Dated evidence |
|---|---|
| (a) Position | Two different businesses:<br>- **Scientific & Metrology Instruments:** TEM, FIB-SEM, SEM, NMR. This sits on the reference side.<br>- **Industrial Equipment:** e-beam mask writers (multi-beam MBMW line, single-beam) and spot-beam lithography. This is a physical-constraint business tied to the lithography roadmap, and it earns most of the profit.<br>JEOL says that, as structures shrink and stack, "part of the CD-SEM market" is moving to TEM/FIB-based inspection (29 May 2026; company claim, unconfirmed) [S21]. |
| (b) Lead | No third-party semiconductor TEM share was found.<br>- On 14 Aug 2026, TEM and FIB for semiconductor inspection were **still at the "customer evaluation stage"**; JEOL says the evaluations are "steadily progressing" toward full adoption (company claim) [S22]. So there is no announced tool-of-record win.<br>- Outside recognition is scientific, not commercial: top Japanese company on the 2025 Nature Index "Count", and highly-cited researchers [S21]. |
| (c) Revenue model | Mainly one-off hardware.<br>- The FY3/2030 plan aims to raise the maintenance-contract rate and "high value-added services", lifting the Scientific & Metrology margin from 12.0% to 19.1% [S21].<br>- Service share of revenue: not disclosed in the documents I read. |
| (d) Financial strength | **FY3/2026:**<br>- Sales ¥179.4B (-8.8%); operating profit ¥26.0B (14.5%); net profit ¥22.1B (record, +18.2%).<br>- ROE 15.7%; internal ROIC 12.3% (18.1% a year earlier); equity ratio 59.9%.<br>- Cash and deposits ¥38.9B against borrowings ¥25.2B, so net cash ≈ ¥13.8B (derived).<br>- Operating cash flow ¥16.0B; capex on property, plant and equipment ¥13.5B; free cash flow ≈ ¥2.2B (derived) [S19][S20].<br>**Segments:** Industrial ¥19.4B profit at 40.2% margin; Scientific ¥13.1B at 11.2% [S19].<br>**China:** ¥35.6B, or 19.9% of sales (22.8% the year before). 34% of Industrial (mask-writer) sales go to China [S19].<br>**Semiconductor customers (derived from plan targets, company management basis):** about ¥50.5B of sales (28%) and about ¥19.8B of operating profit (about 76% of group operating profit) [S21]. |
| (e) Resilience | **Q1 FY3/2027 (Apr-Jun 2026):** sales -39.1% to ¥24.5B; operating loss ¥2.0B. Industrial sales fell 65.6%: multi-beam revenue timing, and single-beam sales hit by "tighter export controls" and China demand settling [S22].<br>**May 2026:** multi-beam recovery at major customers "delayed" [S19].<br>The business is lumpy and cyclical, with direct exposure to China and to export controls. |
| Transitions | (1) **Said:** TEM/FIB inspection is replacing part of CD-SEM [S21]. **Done:** launched the "ACE eye" semiconductor TEM for process monitoring (2026) [S22]; adoption is still under evaluation.<br>(2) **Said:** AI and automation for its next-generation platform [S22]. **Done:** no named AI-recipe product.<br>(3) LazEdge femtosecond-laser SEM for large-area cross-sections [S22].<br>(4) Maintenance-contract push [S21].<br>(5) and (6): nothing found. |
| Entry point | ¥6,680 (12 Nov 2026); market cap ¥325.4B; EV ¥307.4B.<br>- P/E 21.5x trailing (depressed by the Q1 loss), 13.6x forward, 15.4x on JEOL's FY3/2027 EPS guidance (derived).<br>- EV/EBITDA 12.9x, against a range of 5.2-18.1x at FY3/2022-26 year-ends.<br>- First-half results due 13 Nov 2026 [S25]. |

### 1.3 Nearfield Instruments (private, Rotterdam)

| Test | Dated evidence |
|---|---|
| (a) Position | **Non-destructive in-line scanning-probe (AFM) metrology** on product wafers, for high-aspect-ratio trenches, gate-all-around recesses and multilayer stacks. AUDIRA (AFM combined with very-high-frequency ultrasound) is pitched for buried features and voids (company claim) [S31][S35].<br>This could act as an in-line reference that needs no cross-section (inference). |
| (b) Lead | **A customer has confirmed high-volume use:** Samsung memory's VP for Metrology & Inspection, Young Hoon Sohn, said on 17 Apr 2024 that QUADRA was in high-volume manufacturing, used alongside ASML YieldStar [S29].<br>- Repeat orders (Dec 2024) and purchase orders from a "major US customer" (Feb 2025): company claims; customers unnamed [S34].<br>- AUDIRA: no independent validation found. |
| (c) Revenue model | Systems plus service. Revenue not disclosed. |
| (d) Financial strength | Not disclosed. About 450 staff (Jun 2026) [S31]; ING bank financing (Dec 2025) [S34]. |
| (e) Resilience | Customer concentration is probably high: Samsung is the only named customer, and "most customers [are] in Asia and the US" [S30]. Export-control position: could not verify. |
| Transitions | (1) Sidewall Imaging mode (25 Feb 2026).<br>(3) Hybrid-bonding metrology note (16 Jan 2026); A*STAR IME packaging collaboration (19 May 2025); multi-year imec project (18 Nov 2025) [S34]. |
| Entry point | Private.<br>- Series D: €330M ($380M) at a valuation of about €1.4B ($1.6B), 22 Jun 2026. Led by Fidelity; also Temasek, QIA, M&G, Walden Catalyst, Innovation Industries, Invest-NL (€30M with the Deep Tech Fund), ING and TNO Ventures [S27][S31][S33].<br>- Earlier round: €135M, 18 Jul 2024 [S34]. |

### 1.4 ZEISS (Carl Zeiss AG): lighter treatment [PARTLY INCOMPLETE]

| Item | Dated evidence |
|---|---|
| Size | FY2024/25 (to 30 Sep 2025, published 18 Dec 2025): group revenue €11.896B (+9%); EBIT €1.552B (+7%, about 13% margin). Semiconductor Manufacturing Technology (SMT) revenue €5.055B (+23%, from €4.122B) [S36]. SMT EBIT not found. |
| Relevant units | Actinic mask qualification, multi-beam SEM, FIB-SEM and 3D X-ray microscopes. [INCOMPLETE: to verify] |
| Ownership and exposure | Foundation-owned (Carl-Zeiss-Stiftung). The only listed vehicle, Carl Zeiss Meditec, is medical. [INCOMPLETE: to verify] |

### 1.5 Tescan (Czech Republic, private): [INCOMPLETE, nothing gathered yet]

### 1.6 Independent analysis labs (they sell analysis by the case or sample)

| Lab | Latest operating data | Margins (trailing 12 months, stockanalysis, 12 Nov 2026) | Notes |
|---|---|---|---|
| MA-tek (TPEx 3587) | Q3 2026 revenue NT$1,697M (+16.1% y/y, +3.2% q/q); 9M NT$4,765M (+17.0%); September NT$569M, a record for the seventh month running [S37] | Gross 31.2%; operating 12.6%; net 9.8% [S38] | Demand drivers: AI-accelerator projects, advanced-node and packaging R&D and validation, HBM/NAND, Japan lab capacity, Cs-corrected TEM for CFET and 2D materials (company statements) [S37] |
| iST (TPEx 3289) | [INCOMPLETE] Trailing revenue NT$4.77B [S38] | Gross 23.5%; operating 2.9%; net 8.3% [S38] | Q3 results due 13 Nov 2026 |
| MSScorps (6830) | [INCOMPLETE] Trailing revenue NT$2.38B [S38] | Gross 25.1%; operating 2.8%; net 0.6% [S38] | Share price up 201% in 52 weeks [S38] |
| Wintech Nano (SSE STAR 688757) | Trailing revenue CNY 623M [S38] | Gross 36.6%; operating 9.1%; net 5.8% [S38] | Last results 24 Oct 2026 |
| Eurofins EAG | [INCOMPLETE] | n/a | Part of Eurofins Scientific (listed in Paris) |

---

## 2. Supporting detail: business quality and transitions (no share-price data here)

### 2.1 How reference data is produced today, and who buys the tools

#### Takeaway
Reference data comes from focused-ion-beam (FIB) lamella preparation followed by TEM/STEM imaging, plus FIB-SEM slice-and-view. The vendors' push is to automate the whole chain (robotic transfer, fab host connection, AI image analysis) and to move it from the lab into the fab.

#### Cited findings
- Thermo Fisher says leading manufacturers "generate tens of thousands of TEM datasets monthly" (14 Aug 2025; company claim, unconfirmed). It names four reasons TEM is the reference: increasing 3D complexity, shrinking critical dimensions, EUV requirements, and atomic interface analysis. Gate-all-around and 3D NAND channels need "atomic-scale imaging" [S14].
- **Metrios 6 (S)TEM** (27 Jun 2023): fully automated TEM metrology. Claims up to 20% higher average productivity than the previous generation and "at least two times faster" EDS data collection with Ultra-X (company claims) [S12].
- **Metrios 6S** adds SEMI-standard TEM-grid handling and host connection, for automatic grid transfer from the Helios 6 HXS FIB-SEM [S13].
- The Vulcan infographic describes Helios 6 HXS plus Metrios 6S, joined by automated mobile robots or overhead transport, tool automation and a factory host connection [S13].
- A 2026-dated Thermo Fisher document describes automated energy-filtered TEM metrology for memory devices [S13].
- **Vulcan Automated Lab** (18-19 Mar 2025): robotic sample handling, AI-enhanced imaging, high-throughput TEM metrology and "real-time lab-to-fab data exchange". Thermo Fisher calls it "among the first commercially available" systems combining these (company claim). R&D World says traditional TEM workflows need specialised operators and cause long delays, and names comparable efforts at JEOL, Hitachi, Intel and imec [S11].
- **Helios MX1 PFIB-SEM** (28 Oct 2025): "fully automated wafer analysis system", placed in the fab for "immediate in-line data". It does automated 3D reconstruction and metrology for logic, memory and advanced packaging [S10][S16].
  - Argon plasma FIB: "improved throughput by 20x compared to traditional gallium-based milling" (company claim, no test conditions given).
  - "Outsourcing metrology or defect analysis to the lab can add several days to the turnaround time" (6 Oct 2025, Mohan Iyer, VP/GM Semiconductor) [S16].
- JEOL (29 May 2026) says "FIB and TEM structural shape measurement (inspection) has become indispensable for yield improvement in advanced semiconductor manufacturing" and that "evaluation at major customers is progressing smoothly" (company claims). Its products: JIB-PS500i FIB-SEM, JEM-ACE200F high-throughput TEM, JSM-IT810 SEM, and a HAADF-STEM FinFET length-measurement example [S21].
- Market size and third-party shares for semiconductor TEM and FIB-SEM: only aggregator figures, which conflict. For example, the top three vendors are put at about 97% of TEM, but the reports give no methodology [S39].

#### Inferences
- The volume of TEM/FIB data appears to be rising with 3D structures. Every vendor is selling automation and in-fab placement.
- That shortens the slow lab loop. It also keeps both the data and any AI on the customer's premises.

#### Gaps
- Throughput and cost per TEM sample or lamella: no figure found yet. [INCOMPLETE]
- Tool-buyer split between chipmaker labs and independent labs: not found.
- Third-party market size and shares: not found.

### 2.2 Thermo Fisher semiconductor EM: size, products, customers, parent results

#### Takeaway
Thermo Fisher does not disclose EM or semiconductor revenue. EM is one of three businesses in Analytical Instruments, which is about 17% of the group. It was the named driver of the segment's 2025 growth and of the Q2-Q3 2026 recovery. The segment margin rebounded to 26.9% in Q3 2026.

#### Cited findings
**Segment description (10-K for FY2025, filed 26 Feb 2026) [S3]:**
- The segment contains chromatography & mass spectrometry, chemical analysis, and electron microscopy.
- EM "serves customers in the life sciences, materials sciences, and semiconductor markets". In semiconductors it "provides integrated workflows that power research and development and production solutions".

**FY2025 [S3][S2]:**
- Analytical Instruments revenue $7,554M (+1%, organic 0%).
- Within it, EM grew by $87M and chromatography & mass spectrometry by $83M; chemical analysis fell by $78M. "Organic revenues were flat in 2025 primarily due to growth in the electron microscopy…"
- Segment income $1,736M (-11%); margin 23.0% against 26.2%, "primarily from the impacts of tariffs and related foreign exchange".
- Q4 2025 segment margin 26.3% (-420 bp). Sales grew in North America, Europe and Asia-Pacific but fell in China. About 125,000 employees.

**Quarterly 2026:**
- Q1 2026 (call, 23 Apr 2026): segment revenue flat; organic -2%; adjusted margin 20.7% (-250 bp). Industrial & Applied flat; China down at a low-single-digit rate; Academic & Government down at a low-single-digit rate. Clario closed 24 Mar 2026 for about $9B plus earn-outs. Leverage 3.8x gross / 3.5x net debt to adjusted EBITDA [S5].
- Q2 2026: segment revenue about $1.85B (+7%), "led by the company's electron microscopy business" (GenomeWeb, snippet only) [S40]. This matches my derivation: first-half 2026 segment revenue $3,562M, minus Q1 roughly flat at about $1.72B, gives Q2 about $1.84B (derived from [S1]). Another summary gives $1.72B, which looks like the year-earlier figure.
- Q3 2026 (21 Oct 2026) [S1]:
  - Segment revenue $2,002M against $1,893M; segment income $538M (26.9%) against $429M (22.6%).
  - Nine months: $5,564M, margin 23.7% (21.6%).
  - Group: revenue $12,137M (organic +6%); adjusted operating income $2,968M (24.5%); adjusted EPS $6.68 (+15%); nine-month free cash flow $4,618M; buybacks $4.0B; acquisitions $8.877B net. The microbiology divestiture was completed in Q3.
  - Press report: segment helped "by demand for electron microscopes from semiconductor customers"; China grew at a low-double-digit rate; CEO Marc Casper targets a return to about 7% organic growth "in late 2027 or early 2028" [S6].
  - Quarterly release highlight: the EMPAD G2 electron detector, for "next-generation electronics, memory and energy technologies" [S1].
- **FY2026 guidance (raised 21 Oct 2026) [S6][S7]:** revenue $47.7-48.2B; organic growth 4%; adjusted EPS $25.13-25.43; free cash flow $7.0-7.5B.

**Products relevant to reference data:**
- Metrios 6/6S (S)TEM (2023) [S12][S13]
- Vulcan Automated Lab (Mar 2025) [S11]
- Helios 6 HXS (in the Vulcan workflow) and Helios MX1 PFIB-SEM (Oct 2025) [S10]
- Krios 5 and Glacios 3 cryo-TEM: life sciences, not semiconductors [S2][S5]

**Customers:** none named in the launches I read [S10][S11].

#### Inferences
- Semiconductor demand appears to be the swing factor in Analytical Instruments' 2026 recovery (company attribution reported by the press).
- The size of the semiconductor EM business remains unknown. It is a small share of group revenue: Analytical Instruments as a whole is about 17%.

#### Gaps
- EM revenue, semiconductor share, service/consumable mix, named customers, China share of EM: not disclosed, and no sourced estimate found.
- Leverage at Q3 2026: not found (net debt derived).

### 2.3 JEOL: results, segments, semiconductor exposure, plan, China

#### Takeaway
JEOL's profit pool is mask writers (Industrial Equipment, 40% margin), not microscopes (Scientific & Metrology, 11% margin). Semiconductor customers were about 28% of sales but about three-quarters of operating profit in FY3/2026 (derived). Inspection TEM/FIB is still being evaluated by customers. China and export controls hit Q1 FY3/2027 directly.

#### Cited findings
**FY3/2026 (決算短信, 15 May 2026) [S19]:**
- Group: sales ¥179,353M (-8.8%); operating profit ¥26,017M (-26.7%); ordinary profit ¥28,610M; net profit ¥22,097M (+18.2%); EPS ¥432.58; dividend ¥132 (payout 30.5%).
- Scientific & Metrology: sales ¥116,295M (-6.8%), segment profit ¥13,069M (prior year ¥15,017M).
- Industrial: sales ¥48,131M (-14.8%), profit ¥19,363M (prior year ¥26,316M).
- Medical: sales ¥14,926M, profit ¥64M. Sold to Sysmex on 1 Apr 2026.
- By region: Japan ¥58,788M; Americas ¥27,636M; **China ¥35,609M** (Scientific ¥18,496M; Industrial ¥16,470M); other ¥57,319M.
- Capex ¥20.2B (prior year ¥7.0B; construction in progress +¥11.6B). Buyback via tender offer: 2.30M shares for ¥11.84B (Feb-Mar 2026), linked to "Nikon's sale of shares" [S21].

**Commentary (May 2026) [S19][S20][S21]:**
- EM inquiries are "solid" despite cuts to US science budgets.
- China: the stimulus budget has wound down and export controls have tightened.
- Multi-beam mask writers: the recovery "is delayed at major customers".
- Spot-beam e-beam lithography demand comes from DFB lasers for AI-datacentre transceivers.
- Orders ¥180.1B; backlog ¥103.9B; overseas share of sales 67.2% [S20].

**FY3/2027 guidance (15 May 2026; unchanged on 14 Aug 2026) [S19][S21][S22]:**
- Sales ¥164.0B; operating profit ¥26.5B (+1.9%); net ¥21.3B; EPS ¥432.64; first half: sales ¥63.0B and operating profit ¥6.0B (-49.7%).
- Scientific ¥121.4B sales and ¥16.4B profit (13.5%); Industrial ¥42.6B and ¥16.7B (39.3%).
- FX assumptions ¥155/$ and ¥175/€; orders ¥170B; capex ¥23B.

**Q1 FY3/2027 (14 Aug 2026) [S22]:**
- Sales ¥24.5B; operating profit -¥2.0B.
- Scientific ¥19.5B (-8.8%); Industrial ¥5.0B (-65.6%, operating margin 4.4% against 49.7%).
- "Inspection TEM and FIB are still at the customer evaluation stage."
- In China, delays in renewing the import tax exemption for universities cut sales, but orders were firm.

**Medium-term plan (FY25-29, "Evolving Growth 2.0") [S21]:**
- FY3/2030 targets: sales ¥205B; operating profit ¥44B (21.5%); ROE and ROIC of 15% or more.
- Semiconductor domain: sales ¥70B (+¥19.5B on FY3/2026) and operating profit ¥28B (+¥8.2B). That implies about ¥50.5B and about ¥19.8B in FY3/2026 (derived).
- Main semiconductor markets are Korea and Taiwan. Support set-ups: the JEOL-Taiwan Semiconductor Solution Center, JEOL Korea Solution Suite-X, a new SI Semiconductor Business HQ, and the Kumamoto University "SEMIC" co-creation lab (2 Mar 2026).
- Cash allocation for FY25-29: capex ¥75B, R&D ¥56B, dividends ¥35.5B, and M&A in semiconductors and life sciences.
- MBMW-401 multi-beam mask writer for 10Å-class High-NA mass production; new "Shift Passes Stripe Scheduling" writing mode (company claim).

**Previous first half (H1 FY3/2026, 14 Nov 2025):** sales ¥82.0B; ordinary profit ¥12.9B, below the IFIS consensus [S26].

#### Inferences
- In a quality judgement, JEOL's semiconductor "judge" exposure (TEM/FIB) is small and unproven in fabs. Its economic engine is mask writers, which depend on lithography and are exposed to China and to export controls.
- The IMS Nanofabrication link matters for the profit pool, but its terms were not found.

#### Gaps
- Terms of the IMS Nanofabrication partnership.
- TEM market share.
- Service revenue share.
- Customer names and concentration.

### 2.4 Nearfield Instruments

#### Takeaway
Nearfield is the only company in this group with customer-confirmed high-volume production use of a new in-line reference-type measurement (QUADRA at Samsung memory). Its subsurface claims (AUDIRA) have not been independently validated. In June 2026 it raised Europe's largest deep-tech round.

#### Cited findings
- Founded 2016 as a TNO spin-off; CEO and co-founder Hamed Sadeghian [S27][S32].
- **Series D, 22 Jun 2026:** €330M ($380M); valuation about €1.4B ($1.6B), "oversubscribed several times" [S28].
  - Led by Fidelity [S27][S31].
  - Participants named: Temasek, Walden Catalyst, M&G, QIA, Innovation Industries, Invest-NL (€30M with the Deep Tech Fund), ING, TNO Ventures. Sources differ on which investors were new and which existing [S27][S32][S33].
  - Use of funds: Applications Centres of Excellence, production capacity, support, R&D [S31].
  - A new production line in Rotterdam opened that week, with Asian capacity "probably Singapore" (FD via DutchNews) [S30].
- About 450 staff; offices in Taiwan, Korea, Japan, Singapore, the US and Belgium [S31].
- Earlier funding: €135M round (18 Jul 2024); EIC Accelerator (15 Jul 2024); ING bank financing (16 Dec 2025) [S34]. Invest-NL has been involved since 2020 [S33].
- **Customer evidence:** Samsung's HVM confirmation (17 Apr 2024) [S29]. Purchase orders, mostly from unnamed customers: Asian fab (30 Jul 2024), "leading manufacturer in East Asia" (21 Oct 2024), repeat orders that "fill up" the 2025 order book (24 Dec 2024), "major US customer" plus a US subsidiary (10 Feb 2025) [S34].
- **Products (company claims):**
  - QUADRA, "fully validated for measuring dense structures with high aspect ratios on advanced DRAM and logic devices" [S35].
  - Lightning Mode: "160-fold" faster image acquisition than current automated AFM (Jul 2024) [S35].
  - Sidewall Imaging (25 Feb 2026) [S34].
  - AUDIRA subsurface measurement of buried features and voids [S35].
- Sadeghian says process control is becoming "the new checkpoint", as critical as lithography (FD interview via DutchNews) [S30].

#### Gaps
- Revenue, installed base, customers other than Samsung, and independent validation of AUDIRA. [INCOMPLETE]

### 2.5 ZEISS and Tescan: [INCOMPLETE]
- ZEISS SMT FY2024/25 revenue €5.055B (+23%); group EBIT €1.552B [S36]. Products, ownership and SMT EBIT are still to be verified.
- Tescan: nothing gathered yet.

### 2.6 Independent labs

#### Takeaway
The Taiwanese labs report record revenue on AI-accelerator, advanced-node, packaging and HBM work. Their margins are thin except at MA-tek. Their revenue is per case or sample, so it scales with analysis volume and with capacity in tools and engineers.

#### Cited findings
- **MA-tek:**
  - September 2026 revenue NT$569M (a record for the seventh month running).
  - Q3 2026 NT$1,697M (+16.14% y/y); 9M NT$4,765M (+16.99%).
  - Growth drivers, per the company: AI-accelerator projects, advanced-node and new-packaging R&D and validation (more materials-analysis and failure-analysis cases), HBM/NAND, the Japan lab, GaN/SiC reliability, silicon photonics/CPO, and Cs-TEM for CFET and 2D materials (7 Oct 2026) [S37].
  - Q3 2025 EPS NT$2.11 [S37].
  - Equipment includes sub-ångström TEM and SIMS [S37].
- Trailing margins and balance sheets for iST, MSScorps and Wintech Nano: see table 1.6 [S38].

#### Gaps
- iST and MSScorps monthly/Q3 revenue, capacity plans, Eurofins EAG, and lab data rights or confidentiality terms. [INCOMPLETE]

### 2.7 Who ends up owning the reference data: evidence so far [INCOMPLETE]

**Points toward chipmakers:**
- Thermo Fisher's own framing is that the "tens of thousands" of monthly datasets are generated by manufacturers [S14].
- Automation is sold for installation in the customer's fab with a fab host connection [S10][S11][S13].
- Intel and imec run in-house automated TEM [S11].
- Samsung's metrology VP decided the Nearfield HVM qualification [S29].

**Points toward labs:**
- Lab revenue is growing at mid-to-high teens on R&D and validation work for AI chips and packaging [S37]. This is mainly the pre-production phase, where data may belong to the fabless or chipmaker client.

**Points toward tool makers:** none found yet. No vendor reference dataset or data-licensing deal found.

---

## 3. Entry-point data (kept separate from quality)

### 3.1 Thermo Fisher (TMO)
Source: stockanalysis.com, checked 12 Nov 2026 [S18].
- **Price and size:** $717.71 (close 11 Nov 2026); 370.5M shares; market cap $265.9B; EV $301.2B.
- **Multiples now:** P/E 37.8x trailing, 26.7x forward; EV/Sales 6.36x; EV/EBITDA 24.8x; EV/EBIT 33.4x; EV/FCF 39.7x; FCF yield 2.86%; debt/EBITDA 3.28x.
- **Own history (year-end multiples):**

| Year-end | P/E | Forward P/E | EV/EBITDA | EV/Sales |
|---|---|---|---|---|
| FY2021 | 34.0 | 32.6 | 21.0 | 6.95 |
| FY2022 | 31.2 | 25.0 | 20.4 | 5.42 |
| FY2023 | 34.2 | 24.7 | 21.9 | 5.47 |
| FY2024 | 31.4 | 22.9 | 21.0 | 5.32 |
| FY2025 | 32.5 | 24.1 | 22.4 | 5.61 |

- **Consensus:**
  - 2026: revenue $48.0B (+7.7%); EPS $25.28 (+10.6%).
  - 2027: revenue $50.54B (+5.3%); EPS $27.78 (+9.9%).
  - 27 analysts: 20 Strong Buy, 3 Buy, 3 Hold, 1 Sell. Price target $590-830, average $756.52.
  - The price has risen 24.5% over 52 weeks.
- **Derived:** 28.4x the 2026 guidance-midpoint EPS; 25.8x the 2027 consensus EPS.
- **Guidance:** raised 21 Oct 2026 (see 2.2).
- **Near-term events:** Q4 and FY2026 results with 2027 guidance (expected late January 2027; date not verified); the pace of semiconductor EM orders; US academic funding; tariffs.

### 3.2 JEOL (6951.T)
Source: stockanalysis.com, checked 12 Nov 2026 [S25].
- **Price and size:** ¥6,680 (12 Nov 2026, -2.1% on the day); 48.7M shares; market cap ¥325.4B; EV ¥307.4B; cash ¥32.2B; debt ¥14.3B (stockanalysis basis).
- **Multiples now:** P/E 21.5x trailing, 13.6x forward; P/B 2.36x; EV/Sales 1.92x; EV/EBITDA 12.9x; EV/EBIT 16.8x; dividend yield 1.98%. The price has risen 29.9% over 52 weeks.
- **Own history (fiscal year-ends):**

| Year-end | P/E | EV/EBITDA | EV/Sales | P/B |
|---|---|---|---|---|
| FY3/2022 | 28.5 | 18.1 | 2.42 | 4.08 |
| FY3/2023 | 12.2 | 6.6 | 1.19 | 2.13 |
| FY3/2024 | 14.7 | 9.7 | 1.79 | 2.55 |
| FY3/2025 | 12.5 | 5.2 | 1.07 | 1.71 |
| FY3/2026 | 12.7 | 8.0 | 1.41 | 1.93 |

- **Consensus** (5-6 analysts; last updated 17 Aug 2026):
  - FY3/2027: sales ¥168.6B (-6.0%); EPS ¥428.35.
  - FY3/2028: sales ¥188.6B (+11.9%); EPS ¥525.79 (+22.8%).
  - Price target ¥7,000-11,000, average ¥8,720. Ratings: 3 Strong Buy, 1 Hold, 1 Strong Sell (Oct 2026).
- **Derived:** 15.4x the company's FY3/2027 EPS guidance; 12.7x the FY3/2028 consensus EPS.
- **Cycle position:** trough-like first half (guidance: first-half operating profit -49.7%), with the recovery weighted to the second half.
- **Events:** first-half results 13 Nov 2026 and briefing 19 Nov 2026 [S23]; multi-beam order timing; export-control changes affecting China mask writers.

### 3.3 Listed labs
Source: stockanalysis.com, 12 Nov 2026 [S38].

| Lab | Price | Market cap | Trailing P/E | Forward P/E | EV/EBITDA | P/B | 52-week change | Next results |
|---|---|---|---|---|---|---|---|---|
| MA-tek (3587) | NT$188 | NT$13.5B | 22.5x | 14.3x | 6.6x | 2.26x | -5.1% | 16 Nov 2026 |
| iST (3289) | NT$115 | NT$10.0B | 24.1x | 17.1x | 10.4x | 2.10x | +11.7% | 13 Nov 2026 |
| MSScorps (6830; listed as TPE, i.e. TWSE main board, on stockanalysis) | NT$456 | NT$24.8B | n/m (1,751x) | 47.9x | 30.4x | 7.31x | +201% | 16 Nov 2026 |
| Wintech Nano (688757.SS) | CNY 27.11 | CNY 10.9B | 295x | n/a | 50.9x | 12.2x | -4.7% | n/a |

Other figures from the same source:
- MA-tek: EV/Sales 2.31x; dividend yield 2.4%.
- iST: EV/Sales 2.40x; dividend yield 5.6%.
- MSScorps: EV/Sales 11.2x.
- Wintech Nano: EV/Sales 19.3x.

### 3.4 Private, or hard for a foreign investor to reach
- **Nearfield:** see 1.3. There is no public route (inference).
- **ZEISS:** foundation-owned [to verify].
- **Tescan:** [INCOMPLETE].
- **Eurofins EAG:** reachable only through Eurofins Scientific [to verify].

---

## 4. What I could not verify (so far)
- Thermo Fisher EM revenue, semiconductor share, service mix, customers, China share. No sourced estimate.
- Third-party (Gartner, TechInsights, Yole, SEMI) shares for semiconductor TEM and FIB-SEM. Only conflicting aggregator figures.
- Cost and throughput per TEM sample; split of tool purchases between chipmaker and independent labs.
- JEOL first-half FY3/2027 results (published 13 Nov 2026, after the research date); terms of the IMS partnership; JEOL service share.
- Nearfield revenue and installed base; AUDIRA independent validation.
- Leverage of Thermo Fisher at Q3 2026; whether Thermo Fisher's CFO changed in 2026. The Oct 2026 press piece quotes "CFO Jim Meyer", while the Q1 2026 call had Stephen Williamson.
- MSScorps listing venue: stockanalysis shows TWSE ("TPE:6830"), while the brief says .TWO.

## 5. Sources (access date 12 Nov 2026 unless stated)
- [S1] Thermo Fisher Q3 2026 earnings release, 8-K Ex.99.1, 21 Oct 2026. https://www.sec.gov/Archives/edgar/data/0000097745/000009774526000173/q32026earnings8kex99_1.htm
- [S2] Thermo Fisher Q4/FY2025 results release, 29 Jan 2026. https://www.biospace.com/press-releases/thermo-fisher-scientific-reports-fourth-quarter-and-full-year-2025-results
- [S3] Thermo Fisher 10-K FY2025, filed 26 Feb 2026. https://www.sec.gov/Archives/edgar/data/97745/000009774526000018/tmo-20251231.htm
- [S4] Thermo Fisher 10-Q Q3 2026, filed 30 Oct 2026. https://www.sec.gov/Archives/edgar/data/97745/000009774526000179/tmo-20260926.htm
- [S5] Thermo Fisher Q1 2026 call transcript, 23 Apr 2026. https://www.fool.com/earnings/call-transcripts/2026/04/23/thermo-fisher-tmo-q1-2026-earnings-transcript/
- [S6] ValueTheMarkets, "Thermo Fisher raises 2026 outlook after Q3", Oct 2026. https://www.valuethemarkets.com/news/thermo-fisher-nyse-tmo-raises-2026-outlook-after-q3
- [S7] BioSpectrum Asia, Q3 2026 results, Oct 2026. https://biospectrumasia.com/company-results/102/28563/thermo-fisher-scientific-hits-12-14-billion-in-q3-revenue-as-innovation-fuels-double-digit-earnings-growth.html
- [S10] Helios MX1 launch: BusinessWire, 28 Oct 2025, https://www.businesswire.com/news/home/20251028143011/en/ ; SelectScience, 7 Nov 2025, https://www.selectscience.net/article/thermo-fisher-scientific-introduces-the-helios-mx1-pfib-sem
- [S11] Vulcan Automated Lab: BusinessWire, 18 Mar 2025, https://www.businesswire.com/news/home/20250318064982/en ; R&D World, 19 Mar 2025, https://www.rdworldonline.com/thermo-fisher-launches-vulcan-automated-lab-to-accelerate-semiconductor-analysis-with-ai-and-tem-automation/
- [S12] Metrios 6 launch, BusinessWire, 27 Jun 2023. https://www.businesswire.com/news/home/20230627214530/en
- [S13] Metrios 6S page, https://www.thermofisher.cn/cn/en/home/electron-microscopy/products/transmission-electron-microscopes/metrios/instruments/metrios-6s-stem.html ; Vulcan infographic, https://documents.thermofisher.com/TFS-Assets/MSD/brochures/fully-integrated-vulcan-automated-lab-infographic.pdf ; EFTEM memory note, https://documents.thermofisher.com/TFS-Assets/MSD/Reference-Materials/automated-eftem-metrology-advanced-memory-devices.pdf
- [S14] Thermo Fisher blog, "TEM in Semiconductors: Generating Ground Truth Insights", 14 Aug 2025. https://www.thermofisher.com/blog/semiconductors/tem-analysis-semiconductor-development/
- [S15] Thermo Fisher blog, DRAM automated TEM metrology, 6 Nov 2025. https://www.thermofisher.com/blog/semiconductors/dram-device-dram-fabrication-tem-metrology/
- [S16] Thermo Fisher blog, multi-ion-species PFIB, 6 Oct 2025. https://www.thermofisher.com/blog/semiconductors/faster-time-to-data-in-the-fab-with-multi-ion-species-plasma-fib/
- [S17] Thermo Fisher semiconductor blog index (2026 packaging posts). https://www.thermofisher.com/blog/semiconductors/
- [S18] stockanalysis.com TMO statistics, ratios and forecast, 11-12 Nov 2026. https://stockanalysis.com/stocks/tmo/statistics/ ; https://stockanalysis.com/stocks/tmo/financials/ratios/ ; https://stockanalysis.com/stocks/tmo/forecast/
- [S19] JEOL 決算短信 FY3/2026, 15 May 2026. https://www2.jpx.co.jp/disc/69510/140120260514534200.pdf
- [S20] JEOL 決算説明資料 FY3/2026, 15 May 2026. https://www.jeol.co.jp/assets/pdf/ir/financial_report/financial_report_61_4_gim76efe.pdf
- [S21] JEOL 決算説明会 deck FY3/2026 and medium-term-plan update, 29 May 2026. https://www.jeol.co.jp/assets/pdf/ir/financial_report/financial_report_61_5_K1cGir.pdf
- [S22] JEOL Q1 FY3/2027 決算説明資料, 14 Aug 2026. https://www.jeol.co.jp/assets/pdf/ir/financial_report/financial_report_62_1_1ekfuZ.pdf
- [S23] JEOL IR schedule. https://www.jeol.co.jp/ir/schedule.html
- [S25] stockanalysis.com JEOL statistics, ratios and forecast, 12 Nov 2026. https://stockanalysis.com/quote/tyo/6951/statistics/ ; https://stockanalysis.com/quote/tyo/6951/financials/ratios/ ; https://stockanalysis.com/quote/tyo/6951/forecast/
- [S26] Monex Scouter, JEOL H1 FY3/2026 against consensus, 14 Nov 2025. https://scouter.monex.co.jp/news/detail/6951_20251114_act_20251114_153133_6
- [S27] TNO, "Nearfield Instruments unicorn status", 22 Jun 2026. https://www.tno.nl/en/newsroom/2026/06/nearfield-instruments-unicorn-status/
- [S28] Bits&Chips, Series D, 22 Jun 2026. https://bits-chips.com/article/nearfield-closes-record-330-million-euro-funding-round/
- [S29] Bits&Chips, "Nearfield penetrates HVM at Samsung", 1 May 2024. https://bits-chips.com/article/nearfield-instruments-penetrates-high-volume-chip-manufacturing-at-samsung/
- [S30] DutchNews, 22 Jun 2026. https://www.dutchnews.nl/2026/06/chip-firm-nearfield-raises-380m-in-boost-for-dutch-deep-tech/
- [S31] Evertiq, 24 Jun 2026. https://evertiq.com/design/2026-06-24-nearfield-instruments-raises-380-million-in-largest-ever-dutch-deep-tech-round
- [S32] IO+, 22 Jun 2026. https://ioplus.nl/en/posts/largest-deep-tech-round-330-million-nearfield-instruments
- [S33] Invest-NL, 22 Jun 2026. https://invest-nl.nl/en/news/invest-nl-participates-in-the-largest-dutch-deeptech-round-ever-330-million-for-nearfield-instruments
- [S34] Nearfield Instruments news page (items from Jun 2024 to Oct 2026). https://www.nearfieldinstruments.com/news
- [S35] Nearfield product claims: https://www.electronicspecifier.com/?p=33184 ; https://siliconsemiconductor.net/article/120837/Repeat_orders_for_QUADRA_high-throughput_metrology_system ; https://www.generation-nt.com/communiques-presse/nearfield-instruments-eur-quadra-in-line-semiconductor-metrology-2048804
- [S36] ZEISS FY2024/25 results, 18 Dec 2025. https://www.zeiss.com/corporate/en/about-us/present/newsroom/press-releases/press-conferences.html ; https://vietnamnews.vn/media-outreach/1732184/zeiss-concludes-fiscal-year-2024-25-with-solid-growth.html
- [S37] MA-tek monthly and Q3 revenue (Cnyes via UAnalyze), 7 Oct 2026. https://uanalyze.com.tw/articles/4397556683 ; China Times, 7 Oct 2026, https://wantrich.chinatimes.com/news/20261007900442-420101 ; UDN, 2026, https://udn.com/news/story/7254/9553400 ; Q3 2025 EPS, https://uanalyze.com.tw/articles/9305138083
- [S38] stockanalysis.com statistics for MA-tek, iST, MSScorps and Wintech Nano, 12 Nov 2026. https://stockanalysis.com/quote/tpex/3587/statistics/ ; https://stockanalysis.com/quote/tpex/3289/statistics/ ; https://stockanalysis.com/quote/tpe/6830/statistics/ ; https://stockanalysis.com/quote/sha/688757/statistics/
- [S39] TEM market aggregators (low reliability, conflicting). https://www.intelmarketresearch.com/transmission-electron-microscope-market-15729 ; https://www.marketresearch.com/Prof-Research-v4036/Transmission-Electron-Microscope-TEM-Global-40422628
- [S40] GenomeWeb, Q2 2026 (snippet only; page returned 403). https://www.genomeweb.com/business-news/thermo-fisher-stock-surges-firm-raises-full-year-guidance-strong-q2-results
