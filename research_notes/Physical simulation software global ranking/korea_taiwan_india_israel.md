# Physical-simulation software in South Korea, Taiwan, India and Israel (as of 12 Nov 2026)

STATUS: v1 (digest mined; gap research in progress). Quality evidence and entry-point data are in separate sections.

**Summary for the report writer (draft v1)**
- None of the four countries has a vendor that owns a globally accepted sign-off "judge" for flow, structures, EM or thermal at the scale of Ansys/Synopsys, Siemens, Dassault or Cadence. The judges that matter locally are foreign tools certified by local gatekeepers (TSMC OIP, Samsung SAFE QEDA) and national codes (Korean nuclear codes, national weather models).
- Strongest home-grown solver owners: MIDAS IT (Korea, civil/geotechnical FEA, private, ~KRW 69bn 2025 revenue, ~33% operating margin per aggregator data), CoreTech System/Moldex3D (Taiwan, injection-moulding and chip-package moulding/warpage, private), FunctionBay/RecurDyn (Korea, multibody dynamics, private, no financials found). All are niche leaders on seat licences.
- Israel's relevant listed names are not simulation vendors but fab metrology firms whose measurements depend on physical modelling: Nova (model-based optical/materials metrology; Q3 2026 revenue USD 287.8m, GAAP operating margin 32%) and Camtek (inspection/metrology, ~80% advanced packaging). They are strong businesses, tied to the semiconductor capex cycle.
- India's scale is in labour-hour engineering services (Tata Elxsi, KPIT, LTTS, Tata Technologies, Cyient). These fill a gap that AI agents and better tools can close; KPIT shares are down ~54% over 52 weeks. India's simulation product firms are small and private.
- The only listed pure simulation vendor found is E8 (KOSDAQ 418620): revenue KRW 1.7bn (2025), operating loss KRW 11.2bn, market value ~KRW 7.6bn (~USD 5m) on 12 Nov 2026. It is not a candidate for a global ranking beyond a footnote.
- Coverage is thin for private Korean and Taiwanese firms (no DART/MOPS filings reached; aggregator data only).

---

## 1. South Korea: vendors, ownership, size, quality and path forward

### Takeaway
Korea has two credible solver owners (MIDAS IT in civil/structural FEA; FunctionBay in multibody dynamics), a large in-house simulation base at Samsung/SK hynix that buys foreign tools, and one listed micro-cap (E8). Korea's local "judges" are Samsung Foundry's SAFE certification (of foreign EDA tools) and state codes (KMA's Korean model; nuclear safety codes).

### Cited Findings
**MIDAS IT (마이다스아이티, private)**
- Founded 1 Sep 2000; co-CEOs Jung Seon-tae and Jung Seung-sik; business: structural design software and structural engineering design. Financials (NICE data via JobKorea, standalone, KRW): 2022 revenue 53.79bn; 2023 revenue 59.69bn, operating profit 10.01bn; 2024 revenue 58.97bn, OP 13.12bn, net 20.14bn; 2025 revenue 68.93bn (+17%), OP 22.64bn (+73%; ~32.8% margin), net 24.91bn. Employees 260 (2025), 247 (30 Jun 2026). Aggregator data, not checked against DART. — [JobKorea/NICE](https://m.jobkorea.co.kr/company/1776019?tabType=I)
- Product lines: MIDAS Civil, GTS NX, GEN, eGEN, FEA, FX+, NFX, MeshFree, SOILWORKS, CIM (BIM), plus a separate HR-software business (inAIR, JOBDA, H.) in affiliates. Offices since 2002 in China (several), USA (Chicago), India (Mumbai 2008, Chennai 2023), Japan, UK, Russia, Singapore, Dubai, Philippines, Poland (2023), Mexico and Australia (2024). Claims "No. 1" in architectural engineering software in Korea (2004), China (2007) and overseas (2008); US$10m export award (2022) — company claims, unconfirmed. — [MIDAS group site, page dated 3 Sep 2026](https://group.midasit.com/)
- Older item (2022): Hankyung headline "MIDAS IT plans KRW 40bn+ treasury-share buyback in H1" (8 Mar 2022). — [Hankyung](https://www.hankyung.com/article/202203067072i)

**FunctionBay (펑션베이, private)**
- HQ Pangyo; products RecurDyn (multibody dynamics, flexible bodies, contact, particle interface, toolkits; "RecurDyn 2027" released) and Particleworks (particle CFD, distributed — Particleworks is a Prometech, Japan, product). No financials, headcount, AI or GPU features on site. — [FunctionBay site](https://functionbay.com/en)

**E8 (이에이트, formerly E8IGHT; KOSDAQ 418620)**
- Founded May 2012; NFLOW particle-based CFD launched Apr 2014; NDX PRO digital twin 2021; KOSDAQ tech-special listing Feb 2024; renamed E8 May 2025; NAXiS/NAX Ops launched Feb 2026 ("physical AI operating platform"); NFLOW Ai (physics simulation + AI) Apr 2026. — [Hanwha Investment & Securities note, 26 Jun 2026 (mandatory note as IPO lead manager; Not Rated)](https://stock.pstatic.net/stock-research/company/16/20260629_company_649249000.pdf)
- IFRS consolidated (KRW bn): revenue 0.2 (2021), 0.3, 3.7, 2.3, 1.7 (2025); operating loss −7.1, −7.7, −5.3, −10.6, −11.2; net loss −11.4 (2025); free cash flow −15.7 (2025); cash 7.4; equity 14.6 (negative 2021-23). Q1 2026 revenue 0.4 (−50% YoY), operating loss 2.7. Backlog KRW 6.3bn. — [Hanwha note](https://stock.pstatic.net/stock-research/company/16/20260629_company_649249000.pdf)
- Customers: Samsung Electronics digital-twin contract ~KRW 0.8bn; Hyundai Motor ontology contract ~KRW 0.9bn (PoC converted). Orders KRW 10.7bn total, KRW 7.1bn backlog at end-2025. — [TheBell, 25 Mar 2026](https://www.mt.co.kr/article/2026032515359627862)
- NFLOW Ai launched 17 Apr 2026 as web SaaS using a GNN + U-Net "AI surrogate" — [Dealsite, 17 Apr 2026](https://dealsite.co.kr/articles/160371); data-centre cooling prediction added 30 Jul 2026 — [Dealsite](https://dealsite.co.kr/articles/166260); 10 Aug 2026 plan for third-party share placement and acquisition of an unnamed manufacturer as a "proving plant" — [Dealsite](https://dealsite.co.kr/articles/166892).
- Smart-city revenue (Sejong, Busan Eco Delta) delayed by LH land disputes; Busan first-year digital-twin budget ~KRW 3bn. IPO raised KRW 22.6bn; two later rights issues KRW 18.4bn. — [TheBell, 21 Jul 2026](https://www.mt.co.kr/article/2026072108209654443)

**In-house and gatekeepers**
- Samsung Foundry SAFE: "QEDA" program for "EDA tool certification" that "ensures tools meet Samsung's stringent process requirements"; partner names not listed. — [Samsung SAFE page](https://semiconductor.samsung.com/foundry/safe/)
- Samsung–NVIDIA AI factory (31 Oct 2025): >50,000 GPUs; cuLitho integrated into Samsung's OPC platform with "20x" performance (company claim). — [NVIDIA](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-and-Samsung-Build-AI-Factory-to-Transform-Global-Intelligent-Manufacturing/)
- Korea is Synopsys's third-largest geography: USD 325.6m revenue in the quarter to 31 Jul 2026 (vs 202.1m a year earlier, which had ~2 weeks of Ansys) and 837.6m in nine months — Synopsys Form 10-Q for the quarter ended 31 Jul 2026 — [SEC EDGAR, Synopsys filings](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000883241&type=10-Q)
- TOP500 (Jun 2026): Samsung Electronics SSC-24 #25 (106.2 PF, H100); NHN Cloud #20 (137.4 PF, B200) and #40; Kakao #39; NAVER #72; Kakao Enterprise #74; no KISTI system in the top 100. — [TOP500](https://www.top500.org/lists/top500/list/2026/06/)
- KMA: Korean numerical model (developed Apr 2020) ran alongside the UK Unified Model for six years; KMA runs the Korean model alone from Apr 2026; designed a Korean AI weather/climate foundation model structure Dec 2025; secured 208 GPUs Apr 2026. — [Daum/News, 28 May 2026](https://v.daum.net/v/20260528142448171)

### Inferences
- MIDAS IT is the Korean firm most likely to place in a global ranking (owned solvers, export base, high margin), but as a civil-engineering niche vendor; its "judge" is the licensed engineer plus design codes, not regulator-accepted software.

### Gaps
- (pending) Tae Sung S&E, Alsemy, Virtual Lab, Narnia Labs, MetaRiver, nuclear codes (SPACE), KISTI-6, Hyundai.

---

## 2. Taiwan
### Takeaway
(pending) CoreTech System/Moldex3D is the only Taiwanese solver owner of note; TSMC is the region's most important certifier.

### Cited Findings
- CoreTech System (科盛科技股份有限公司): registered 20 Nov 1995; responsible person 許嘉翔 (David Hsu); paid-in capital NT$412.2m (authorised NT$1.0bn); Zhubei, Hsinchu; last registration change 1 Oct 2026. — [GCIS company registry API](https://data.gcis.nat.gov.tw/od/data/api/6BBA2268-1367-4B42-9CCA-BC17499EBE8C?$format=json&$filter=Company_Name%20like%20%E7%A7%91%E7%9B%9B%E7%A7%91%E6%8A%80%20and%20Company_Status%20eq%2001&$skip=0&$top=10)
- Founders Prof. Rong-Yeu Chang (張榮語) and four others; products include Plastic Molding, Composite Molding, IC Packaging, Electronics Potting; Moldiverse cloud; "thousands of companies" use it (company claim). — [Moldex3D About](https://www.moldex3d.com/about/)
- TSMC EDA Alliance: 11 members as of 23 Sep 2026 (Cadence, iROC, Jedat, Keysight, Lorentz, Primarius, Siemens EDA, Silvaco, SkillCAD, Synopsys, Zuken); certification program run with Cadence, Siemens EDA, Synopsys covering A14/A16/N2P/N3C/3DFabric incl. thermal. No Taiwanese vendor listed. — [TSMC OIP EDA Alliance](https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance)
- AnaGlobe: IC layout (Thunder, Thunder SiP router for fan-out RDL/interposer/substrate, GOLF OpenAccess editor "adopted since 2007"); no TSMC certification mentioned. — [AnaGlobe](https://www.anaglobe.com/)

---

## 3. India
(pending)

## 4. Israel
(pending)

## 5. Boundary of trust by country
(pending)

## 6. Entry-point data (valuation and access) — kept separate from quality evidence
(pending; data in hand for E8, Nova, Camtek, Tata Elxsi, KPIT, LTTS, Tata Technologies, Cyient)

## 7. Could not verify; dated source list
(pending)
