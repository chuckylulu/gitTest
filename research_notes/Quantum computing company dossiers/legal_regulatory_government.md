# Legal, regulatory and government-funding matters: IBM Quantum, Google Quantum AI, Quantinuum, QuEra, PsiQuantum, IQM (plus US government equity/awards incl. IonQ, and IonQ legal gaps) — status as of 14 Nov 2026

Labels: **[CO]** company-controlled (company filings, releases, company-authored papers; trade-press reprints of releases are "[CO-relay]"). **[IND]** independent (journalists, law firms, analysts). **[IND-gov]** government/agency record. **[IND-court]** court docket record. "(older)" = dated before 2026. "(dossier)" = carried over from the earlier company dossiers in this folder and not re-fetched in this session. All EDGAR, CourtListener, Federal Register API, gov.uk, NIST and EC pages below were fetched directly on 14 Nov 2026 unless marked "(search summary)", which means the fact came from a search-engine summary of the page and the page itself was not opened.

Verification of the earlier research the coordinator asked me to check:
- Quantinuum on Nasdaq as QNT: confirmed. Form 8-A12B was filed 4 Jun 2026 and the 424B4 on 5 Jun 2026; EDGAR lists ticker QNT on Nasdaq — [EDGAR submissions, CIK 2110105 [IND-gov]](https://data.sec.gov/submissions/CIK0002110105.json).
- The 2021 CFIUS NSA: confirmed, and **it terminated on 3 Nov 2026** (see Q3).
- IQM on Nasdaq as IQMX via the RAAQ SPAC: confirmed. IQM filed Form 8-A12B on 1 Jul 2026 and RAAQ filed a 25-NSE delisting notice the same day. RAAQ filed a 15-12G on 13 Jul 2026. EDGAR tickers are IQMX and IQMXW — [EDGAR, CIK 2113060 [IND-gov]](https://data.sec.gov/submissions/CIK0002113060.json); [EDGAR, RAAQ CIK 2052161 [IND-gov]](https://data.sec.gov/submissions/CIK0002052161.json).
- IQM material weaknesses for FY2024–FY2025: confirmed (see Q2).
- Chakraborty v. PsiQuantum: confirmed. It **settled and was dismissed with prejudice in Oct 2025** (see Q1).
- CHIPS awards:
  - IBM: the form is now disclosed. It is $650M at closing plus $350M on milestones, and Anderon issued Commerce a minority equity interest (see Q4).
  - Quantinuum: confirmed at 2,369,528 shares at $42.20.
  - PsiQuantum: the equity condition is confirmed by Commerce's LOI announcement, but the final equity terms are undisclosed.

---

## 1. Litigation: court cases involving Quantinuum, IQM, QuEra, PsiQuantum, Google's quantum work or IBM's quantum business

### Takeaway
Federal docket searches found **no case in which Quantinuum, IQM, QuEra, Google (quantum) or IBM's quantum business is a party**. They found no securities class action, derivative suit or quantum patent case against any of them. The only party case found is PsiQuantum's Title VII employment suit (*Chakraborty v. PsiQuantum*, N.D. Cal. 5:25-cv-03374). It **settled in mediation (certified 8 Oct 2025) and was dismissed with prejudice (terminated 31 Oct 2025)**. The same plaintiff has a live pro se defamation suit against an individual in N.D. Ill. (1:26-cv-00106) in which PsiQuantum is not a party. State courts, including Delaware Chancery, and arbitration were not searchable.

### Cited Findings
**Search method (14 Nov 2026).**
- CourtListener RECAP (federal dockets) and opinion searches, sorted by filing date. Queries:
  - "Quantinuum"
  - "IQM Quantum", "IQMX", "Real Asset Acquisition"
  - "QuEra", "QuEra Computing"
  - "PsiQuantum"
  - "Google Quantum AI", "IBM Quantum", "Honeywell Quantum", "Cambridge Quantum"
  - "qubit" AND "Google LLC"; "qubit" AND "International Business Machines"
  - caseName:IonQ; "Rocket Lab" AND "IonQ"
- Hit counts:
  - Quantinuum: 6 RECAP hits, 0 opinions.
  - "IQM Quantum": 0. "Real Asset Acquisition": 0.
  - "PsiQuantum": 10 RECAP hits, 0 opinions.
  - "QuEra Computing": 1 hit.
  - "Google Quantum AI": 1 hit. "IBM Quantum": 3 hits.
  - — [CourtListener search, "Quantinuum" [IND-court]](https://www.courtlistener.com/?q=%22Quantinuum%22&type=r); [CourtListener search, "PsiQuantum" [IND-court]](https://www.courtlistener.com/?q=%22PsiQuantum%22&type=r)
- Limits:
  - Federal courts only.
  - RECAP full-text coverage is partial, though new federal case names are ingested broadly.
  - The CourtListener API needs authentication, so the HTML search was used.
  - State courts, Delaware Chancery, foreign courts (Finland, UK, Australia) and arbitration are not covered.

**PsiQuantum**
- *Chakraborty v. PsiQuantum Corp.*, No. 5:25-cv-03374 (N.D. Cal.):
  - Filed 16 Apr 2025, when PsiQuantum removed it from state court and answered.
  - Cause: 42 U.S.C. §2000e (Title VII) job discrimination, nature of suit 442. Plaintiff Romit Chakraborty demanded a jury.
  - Assigned to District Judge Noel Wise and referred to mediation (Jill Kopeikin).
  - Mediation sessions were held on 23 Sep and 7 Oct 2025. On 8 Oct 2025 the mediator certified "The case settled".
  - A stipulation of dismissal of the entire action with prejudice (FRCP 41(a)(1)(A)(ii)) was filed 30 Oct 2025. The case was terminated 31 Oct 2025.
  - The trial set for 21 Sep 2026 was therefore vacated. Settlement terms are not on the docket.
  - — [CourtListener docket 69900901 [IND-court]](https://www.courtlistener.com/docket/69900901/chakraborty-v-psiquantum-corp/)
- *Chakraborty v. Gagliardi*, No. 1:26-cv-00106 (N.D. Ill.):
  - Filed pro se on 5 Jan 2026 by Romit Chakraborty against Laura Gagliardi. Nature of suit 320 (assault, libel and slander); diversity jurisdiction.
  - Dismissed 28 Jan 2026 for an unpaid fee, then reinstated 24 Feb 2026.
  - The second amended complaint was filed 31 Jul 2026. The defendant moved for judgment on the pleadings on 11 Aug 2026 (response due 2 Sep, reply due 16 Sep).
  - Fact discovery deadline: 30 Nov 2026. New filings were made on 13 Nov 2026.
  - PsiQuantum is **not** a party. CourtListener indexes the docket under "PsiQuantum", but the defendant's relationship to PsiQuantum was not verified.
  - — [CourtListener docket 72110483 [IND-court]](https://www.courtlistener.com/docket/72110483/chakraborty-v-gagliardi/)
- *G Squared Equity Management LP v. Cassandra Capital GmbH*, No. 1:25-cv-12036 (N.D. Ill.):
  - Filed 1 Oct 2025 by a venture-capital manager seeking a declaratory judgment in a contract dispute (nature of suit 190). Assigned to Judge John Robert Blakey.
  - PsiQuantum is not a party. The docket is indexed under "PsiQuantum"; the subject (possibly PsiQuantum securities) was not verified.
  - — [CourtListener docket 71521108 [IND-court]](https://www.courtlistener.com/docket/71521108/g-squared-equity-management-lp-v-cassandra-capital-gmbh/)
- Other "PsiQuantum" hits are only mentions in bankruptcy dockets: Linqto Texas (Bankr. S.D. Tex. 2025), ATech/Akoustis (Bankr. D. Del. 2024), FTX (Bankr. D. Del. 2022), Suitable Technologies, LATAM, Puerto Rico. — [CourtListener search [IND-court]](https://www.courtlistener.com/?q=%22PsiQuantum%22&type=r)

**Quantinuum**
- None of the 6 RECAP hits names Quantinuum as a party. The hits are:
  - *Cohen v. Quantum Computing Inc.* (D.N.J. 2025). This is the QCi securities case, which concerns a different company.
  - *Honeywell Int'l v. OPTO Electronics* (4th Cir. 2023).
  - *Cohesity v. Cartesian Theatre* (N.D. Cal. 2024).
  - *Crady v. 3M* (E.D. Mo. 2025).
  - The Pacifica of the Valley and Yellow Logistics bankruptcies.
  - — [CourtListener [IND-court]](https://www.courtlistener.com/?q=%22Quantinuum%22&type=r)
- Company statement: "We are currently involved in… legal proceedings, claims, and investigations in the ordinary course of our business… we do not believe that the final outcome of any matters… [is] reasonably likely to have a material adverse effect". — [Quantinuum Q3 2026 10-Q, filed 10 Nov 2026 [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162828026072454/qnt-20260930.htm)

**IQM**
- No federal docket hits for "IQM Quantum", "IQMX" or "Real Asset Acquisition". — [CourtListener [IND-court]](https://www.courtlistener.com/?q=%22IQM+Quantum%22&type=r)
- Company statement: "We are not currently subject to any pending or threatened claims or actions that we believe, if determined adversely to us, would reasonably be expected… to have a material adverse effect". — [IQM F-1/A, 18 Aug 2026 [CO]](https://www.sec.gov/Archives/edgar/data/2113060/000119312526355643/d36013df1a.htm)

**QuEra**
- Most of the 75 "QuEra" hits are a personal name. "QuEra Computing" appears only in the ATech (Akoustis) bankruptcy docket (Bankr. D. Del. 2024), as a mention and not as a litigant. — [CourtListener [IND-court]](https://www.courtlistener.com/?q=%22QuEra+Computing%22&type=r)

**Google and IBM (quantum)**
- "Google Quantum AI": 1 hit (*Pizzuto v. Derrick*, D. Idaho), unrelated.
- "qubit" AND "Google LLC": only unrelated hits (e.g., *WSOU Investments v. Google*, W.D. Tex. 2020; bankruptcy dockets).
- No quantum patent suit was found for either company. — [CourtListener [IND-court]](https://www.courtlistener.com/?q=%22qubit%22+AND+%22Google+LLC%22&type=r)
- "IBM Quantum" hits:
  - *Luton v. IBM Corporation*, No. 7:26-cv-00075 (M.D. Ga.). Removed 25 Mar 2026; the plaintiff is "The New Faith Church and co-op Inc."; nature of suit is other statutory actions. No visible link to the quantum business.
  - *AAPT v. NSF* (D.D.C. 2025) and *NYT v. Microsoft* (S.D.N.Y. 2023), which are mentions only.
  - — [CourtListener docket 72750501 [IND-court]](https://www.courtlistener.com/docket/72750501/luton-v-ibm-corporation/)

### Inferences
- Quantinuum was about 32% below its IPO price by mid-Nov 2026 (dossier) and IQM traded below its $10 reference price (dossier). Even so, neither has a federal securities suit naming it as of 14 Nov 2026. A new federal class action would normally appear in CourtListener's case-name index within days, so this absence is reasonably informative for federal court. It says nothing about state court or demand letters.
- The only PsiQuantum party litigation found was resolved by settlement. The plaintiff's follow-on defamation case is against an individual.

### Gaps
- State-court dockets were not searched: California Superior Court (Santa Clara/Alameda), Delaware Chancery (for derivative or books-and-records actions), Colorado, Massachusetts and Illinois.
- Finnish, German, UK and Australian courts were not searched. No arbitration records are available.
- The settlement terms in *Chakraborty v. PsiQuantum* are not public. The complaint (PACER) was not purchased.
- I could not confirm what links *Chakraborty v. Gagliardi* and *G Squared v. Cassandra Capital* to PsiQuantum.
- USPTO PTAB records (IPRs) and ITC investigations were not searched for Google or IBM quantum patents.

---

## 2. SEC staff scrutiny: comment letters on Quantinuum's S-1 and IQM's F-4/F-1, changes to technical and market claims, and IQM's material-weakness remediation

### Takeaway
**No SEC staff comment letters or company responses (CORRESP, UPLOAD, DRSLTR) have been released on EDGAR for Quantinuum, IQM or RAAQ as of 14 Nov 2026.** This is so even though the SEC's stated practice is release "no sooner than 20 business days" after effectiveness. What the staff asked therefore cannot be documented.

Comparing successive drafts shows that Quantinuum's claim language changed mainly between the confidential DRS (17 Feb 2026) and DRS/A1 (31 Mar 2026):
- Sources were attached to the superlatives "highest fidelity", "most accurate" and "first", and in one case the source changed from an independent benchmark to Quantinuum's own Helios paper.
- The logical-qubit figure moved from "50… overhead of less than 2" to "48… 2:1".
- A "bookings" metric ($79.3M FY2025) was added with a definition.

IQM's claims barely changed across its drafts. IQM's three material weaknesses remained "ongoing" in remediation as of the 18 Aug 2026 F-1/A.

### Cited Findings
**EDGAR record**
- Quantinuum's (CIK 2110105) EDGAR filing list shows:
  - DRS 17 Feb 2026; DRS/A 31 Mar 2026; DRS/A 23 Apr 2026.
  - S-1 8 May 2026; S-1/A 26 May 2026; S-1/A 1 Jun 2026; S-1MEF and EFFECT 3 Jun 2026.
  - 424B4 5 Jun 2026; 10-Qs 13 Aug and 10 Nov 2026.
  - **No CORRESP, UPLOAD or DRSLTR entries.**
  - — [EDGAR submissions JSON [IND-gov]](https://data.sec.gov/submissions/CIK0002110105.json)
- IQM Quantum Computers Oyj (CIK 2113060; formerly "IQM Finland Oy", Feb–Jun 2026). Its filing list shows:
  - DRS 3 Apr 2026; F-4 14 May 2026; F-4/A 3 Jun 2026; EFFECT 5 Jun 2026; 424B3 5 Jun 2026.
  - F-1 3 Aug 2026; F-1/A 18 Aug 2026; EFFECT 26 Aug 2026.
  - 424B3 26 Aug and 9 Nov 2026; S-8 13 Nov 2026.
  - **No CORRESP or UPLOAD.**
  - RAAQ (CIK 2052161) also has none.
  - — [EDGAR submissions, IQM [IND-gov]](https://data.sec.gov/submissions/CIK0002113060.json); [EDGAR submissions, RAAQ [IND-gov]](https://data.sec.gov/submissions/CIK0002052161.json)
- EDGAR full-text search returned 0 CORRESP and 0 UPLOAD hits for "Quantinuum" and 0 CORRESP hits for "IQM". The 3 UPLOAD hits for "IQM" are an unrelated 2009–2010 issuer (Inicia Inc). — [EDGAR FTS [IND-gov]](https://efts.sec.gov/LATEST/search-index?q=%22Quantinuum%22&forms=CORRESP)
- SEC policy: the Division of Corporation Finance "makes its comment letters and company responses… public on… EDGAR no sooner than 20 business days after it has completed its review of a periodic or current report or declared a registration statement effective." — [SEC, "Filing Review Process" (page last updated 27 Sep 2019) [IND-gov]](https://www.sec.gov/divisions/corpfin/cffilingreview.htm)

**Quantinuum: changes between drafts.** These come from my sentence-level comparison of the seven versions; the SEC letters are not public.
- **Gate-fidelity superiority claim.**
  - DRS (17 Feb 2026): Helios' 99.921% two-qubit fidelity "is the highest two-qubit gate fidelity among commercially available gate-based quantum computing systems, based on the 2025 Montañez-Barrera et al." This is an independent benchmarking study of 24 QPUs (arXiv:2502.06471).
  - DRS/A1 (31 Mar 2026): the same claim is "based on the 2025 Ransford et al." This is "Helios: A 98-qubit trapped-ion quantum computer" (arXiv:2511.05465), Quantinuum's own system paper.
  - 424B4 (5 Jun 2026): "…based on the 2025 Ransford et al. Study **and our analysis of public filings of our peer companies**".
  - — [DRS [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162827926000199/filename1.htm); [DRS/A1 [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162827926000391/filename1.htm); [424B4 [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162828026041003/quantinuum-424b4.htm)
- **"Most accurate commercial quantum computer"**: "according to the 2025 Ransford et al." was added in DRS/A1. — [DRS/A1 [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162827926000391/filename1.htm)
- **Logical-qubit claim.**
  - DRS: "Helios achieved these 50 logical qubits from only 98 physical qubits, an overhead of less than 2".
  - DRS/A1: "48 logical qubits… an error-correcting overhead in a commercial setting of 2:1… according to the 2026 Dasu et al." (arXiv:2602.22211).
  - DRS/A2 (23 Apr 2026): "**the first to achieve** an error-correcting overhead in a commercial setting of 2:1".
  - The comparator "overhead of up to 100" became "up to 100:1 as best-in-class according to the 2025 Google Quantum Nature Study".
  - — [DRS/A2 [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162827926000511/filename1.htm)
- **"First" claims given sources in DRS/A1:**
  - "we were the first in the industry to implement logical qubits with a higher accuracy than physical qubits, according to the 2021 Ryan-Anderson et al." (arXiv:2107.07505).
  - "H1 was the first commercial quantum system to demonstrate 'Three Nines'… according to the 2025 Kretschmer et al." (arXiv:2509.07255).
  - — [DRS/A1 [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162827926000391/filename1.htm)
- **Bookings metric.**
  - Added in DRS/A1: "Bookings were $79.3 million for the year ended December 31, 2025. Bookings represent the aggregate dollar value of customer contracts executed during a given period. The ultimate value of our bookings is impacted by new contracts, modifications and terminations."
  - The S-1 (8 May 2026) added: "Bookings were $1.3 million for the three months ended March 31, 2026 compared to $1.9 million for the three months ended March 31, 2025."
  - Mentions of "bookings" by version: DRS 0; DRS/A1 12; S-1 through 424B4 15; **Q3 2026 10-Q 0**.
  - — [S-1 [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162828026032836/quantinuum-sx1.htm); [Q3 10-Q [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162828026072454/qnt-20260930.htm)
- **Positioning wording.** "Quantinuum is a leading quantum computing company" (DRS) became "a leading full-stack quantum computing company" (DRS/A1). The S-1 added:
  - "We believe we have achieved the highest logical qubit count with the lowest overhead as of December 31, 2025 based on publicly available information."
  - "…the highest recorded QV of any company in our industry in each of the last 5 years, with our latest QV results exceeding… our closest competitor… by a factor of 2^14 = 16,384."
  - — [S-1 [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162828026032836/quantinuum-sx1.htm)
- **Stable items.**
  - "Quantum advantage" appears 23 times in every version.
  - The peer-group sentence still cites Montañez-Barrera et al. for "the companies with the highest two-qubit gate fidelity".
  - From S-1 (8 May) to 424B4 (5 Jun) the only substantive claim-area change was new CHIPS IP-restriction language in S-1/A1, covering U.S.-company ownership of funded inventions for 10 years.
  - — [S-1/A1, 26 May 2026 [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162828026037917/quantinuum-sx1a.htm)
- **Material weakness.** Quantinuum discloses none. Its only reference is the forward-looking "If we identify one or more material weaknesses in the future…". — [Q3 2026 10-Q [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162828026072454/qnt-20260930.htm)

**IQM: changes between drafts and remediation status**
- Draft changes:
  - DRS (3 Apr) to F-4 (14 May 2026): the "Industry and Market Data" disclaimer text was added; revenue-recognition categories were added (customised on-prem systems "sold under a development, fabrication, delivery, installation and commissioning contract"; standardised systems); the order-backlog table was reformatted. The DRS table showed backlog of €67.3M at end-2025, against €30.1M at end-2024, and FY2025 order intake of €68.5M.
  - F-4/A (3 Jun 2026) added: "Our revenue for the year ended December 31, 2025 was €31.3 million, and we have a strong order backlog of over €67 million."
  - No hedging of "leading" or "first" language was observed. Counts are "leading" 27→29 and "quantum advantage" 24–25.
  - — [IQM DRS [CO]](https://www.sec.gov/Archives/edgar/data/2113060/000119312526141573/filename1.htm); [F-4 [CO]](https://www.sec.gov/Archives/edgar/data/2113060/000119312526222654/d900375df4.htm); [F-4/A [CO]](https://www.sec.gov/Archives/edgar/data/2113060/000119312526255796/d900375df4a.htm)
- **Material weaknesses** were identified while preparing the FY2024–FY2025 audited statements:
  - (i) the design and operating effectiveness of IT general controls (IT operations, user access, change management);
  - (ii) the financial-reporting process, including "lack of sufficient financial reporting and accounting personnel with knowledge of IFRS and SEC reporting requirements";
  - (iii) "lack of segregation of duties in both business and IT processes".
- **Remediation** is described as "ongoing". It consists of:
  - hiring experienced IT staff for ITGCs;
  - hiring finance and accounting staff with IFRS and SEC qualifications;
  - "establishing defined policies for approval of transactions, access control and the segregation of duties".
  - The filing states: "We cannot assure you that the measures… will be sufficient". The F-1/A names possible investigations by Nasdaq, Nasdaq Helsinki, the SEC or FIN-FSA as a risk.
  - No Section 404 management report is due until the year after IQM's first annual report.
  - — [IQM F-1/A, 18 Aug 2026 [CO]](https://www.sec.gov/Archives/edgar/data/2113060/000119312526355643/d36013df1a.htm)
- The 9 Nov 2026 prospectus supplement contains no material-weakness update (0 mentions). — [IQM 424B3, 9 Nov 2026 [CO]](https://www.sec.gov/Archives/edgar/data/2113060/000119312526452244/d186136d424b3.htm)

### Inferences
- The DRS→DRS/A1 changes match what Corporation Finance staff typically ask for: support for superlatives, and definition and context for key metrics. However, the letters are unpublished, so the changes cannot be attributed to SEC comments rather than company or underwriter decisions.
- Quantinuum's "highest fidelity" claim now rests on its own system paper plus its reading of peers' filings, rather than on the independent benchmark first cited.
- Quantinuum gave a bookings figure in the prospectus ($79.3M FY2025; Q1 2026 $1.3M, down from $1.9M) and dropped the metric in its 10-Qs.
- All three IQM weaknesses concern basic control infrastructure. Remediation depends on hiring. No completion date was given as of Aug 2026.

### Gaps
- All SEC comment letters and responses for Quantinuum's DRS/S-1 and IQM's DRS/F-4/F-1 are unreleased as of 14 Nov 2026, and no reason for the delay was found. A FOIA request would be the only alternative route.
- IQM's Q3 2026 interim report (6-K, 5 Nov 2026) was not reviewed in full. Its exhibit may contain an ICFR update; the cover document showed none.
- Whether Quantinuum's change of source for the fidelity claim came from an SEC comment is unknown.

---

## 3. Export controls and investment screening (US BIS, EU, UK, Finland, Japan, China; CFIUS/NSIA/Finnish screening)

### Takeaway
- **US.** The 6 Sep 2024 BIS interim final rule (ECCN 4A906; 89 FR 72926) is still the core US quantum control. A Federal Register search found **no BIS document mentioning "quantum" after 16 Sep 2025** through 14 Nov 2026. The 2025 quantum-related BIS actions were Entity List additions of Chinese suppliers and institutes (28 Mar 2025; 16 Sep 2025).
- **EU.** The EU added quantum computers and cryogenic items to Annex I. The Commission adopted the update on 8 Sep 2025, and it took effect on 15 Nov 2025 per secondary sources.
- **Other jurisdictions.**
  - Finland: national quantum controls (Act 500/2024) since 15 Sep 2024.
  - UK: national entries (PL9014) since 1 Apr 2024, reportedly replaced by "500-series" entries from 16 Dec 2025.
  - Japan: listed quantum computers effective 9 Sep 2024.
- **China.** No Chinese countermeasure naming a US quantum company was found.
- **Investment screening.**
  - Quantinuum's 2021 CFIUS NSA **terminated on 3 Nov 2026**.
  - IQM's SPAC merger had no CFIUS, NSIA or Finnish screening approval as a closing condition; only HSR applied.
  - No screening record was found for QuEra or PsiQuantum.

### Cited Findings
**US (BIS)**
- The IFR of 6 Sep 2024 (89 FR 72926; FR doc. 2024-19633) "is implementing export controls on several semiconductor, quantum, and additive manufacturing items". BIS issued corrections on 27 Dec 2024 (89 FR 105448, doc. 2024-30723). — [Federal Register API listing [IND-gov]](https://www.federalregister.gov/api/v1/documents.json?conditions%5Bterm%5D=quantum&conditions%5Bagencies%5D%5B%5D=industry-and-security-bureau&order=newest); [89 FR 72926 text (govinfo) [IND-gov]](https://govinfo.gov/content/pkg/FR-2024-09-06/html/2024-19633.htm)
- ECCN 4A906.a thresholds (C-NOT error by qubit band):
  - 34–99 qubits: ≤1×10⁻⁴
  - 100–199 qubits: ≤1×10⁻³
  - 200–349 qubits: ≤2×10⁻³
  - 350–499 qubits: ≤3×10⁻³
  - 500–699 qubits: ≤4×10⁻³
  - 700–1,099 qubits: ≤5×10⁻³
  - 1,100–1,999 qubits: ≤6×10⁻³
  - License Exception IEC is available for countries with equivalent controls.
  - — (dossier: ibm_quantum.md, citing 89 FR 72926) [IND-gov](https://govinfo.gov/content/pkg/FR-2024-09-06/html/2024-19633.htm)
- **Entity List, 28 Mar 2025 (90 FR 14032).** BIS added the following "for acquiring and attempting to acquire U.S.-origin items in support of advancing China's quantum technology capabilities":
  - Scikro (Hong Kong) Instruments Ltd and Scikro (Shanghai) Instrument Co., suppliers of dilution refrigerators "to Chinese parties on the Entity List as well as defense-related Chinese entities";
  - …Opto-electronics (Chongqing) Co.; Chongqing Southwest Integrated Circuit Design Co.; ORICAS Import and Export (Beijing) Corp.; Physike Technology Co.
  - — [govinfo, FR doc. 2025-05426 [IND-gov]](https://www.govinfo.gov/content/pkg/FR-2025-03-28/html/2025-05426.htm)
- **Entity List, 16 Sep 2025 (90 FR 44496).** BIS added the Chinese Academy of Sciences National Time Service Center for space-domain activities "as well as China's quantum technology capabilities". The license requirement covers all EAR items, with a presumption of denial. — [govinfo, FR doc. 2025-17893 [IND-gov]](https://www.govinfo.gov/content/pkg/FR-2025-09-16/html/2025-17893.htm)
- **No later BIS quantum rules.** BIS published 78 Federal Register documents from 1 Oct 2025 to 9 Nov 2026. The term search "quantum" returns none after 16 Sep 2025; the 2026 rules concern drones, polysilicon, UAE treatment, advanced-computing licence policy, Entity List revisions and similar topics. — [Federal Register API, BIS docs since 1 Oct 2025 [IND-gov]](https://www.federalregister.gov/api/v1/documents.json?conditions[agencies][]=industry-and-security-bureau&conditions[publication_date][gte]=2025-10-01&order=newest&per_page=100)

**Company export-control disclosures**
- Quantinuum lists the United States, United Kingdom, France, Spain, Germany, Denmark, Finland, Norway, Slovenia, Japan, Canada and the Netherlands as having "recently enacted export controls on quantum computing hardware and related software". It says it "may be required to obtain export licenses for transactions that we previously believed did not require such licenses". No specific licence is disclosed. — (dossier) [424B4 [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162828026041003/quantinuum-424b4.htm)
- On China, Quantinuum states: "we do not currently conduct business in certain jurisdictions that are subject to heightened geopolitical tensions, including China". It also says the CHIPS Award's "restrictions on transferring or licensing project intellectual property to foreign countries and entities of concern" and "the U.S. government's status as a stockholder, may cause certain foreign governments, state-owned enterprises and customers to view us as aligned with U.S. government policy objectives… we may be excluded from or disadvantaged in procurements". — [Q3 2026 10-Q [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162828026072454/qnt-20260930.htm)
- IQM says it is subject to "Regulation (EU) 2021/821… and Finnish Act on the Export Control of Dual-Use Items (500/2024)" and that "certain of our products and technology are subject to export licensing or approval requirements". No specific licence is disclosed. — [IQM F-1/A [CO]](https://www.sec.gov/Archives/edgar/data/2113060/000119312526355643/d36013df1a.htm)

**EU**
- The Commission adopted the Annex I update on 8 Sep 2025. It adds "Controls related to quantum technology (e.g. quantum computers, electronic components designed to work at cryogenic temperatures, parametric signal amplifiers, cryogenic cooling systems, cryogenic wafer probers)". It also "includes commitments that Member States have accepted". Entry into force follows the two-month scrutiny period. — [European Commission DG TRADE, 8 Sep 2025 [IND-gov]](https://policy.trade.ec.europa.eu/news/2025-update-eu-control-list-dual-use-items-2025-09-08_en)
- It was published as Delegated Regulation (EU) 2025/2003 in the Official Journal on 14 Nov 2025 and entered into force 15 Nov 2025. Under Finland's MFA guidance, the EU entry number is used where it applies and the national entry otherwise. — [Finnish Government release (search summary; 403 on fetch) [IND-gov]](https://valtioneuvosto.fi/en/-/update-to-eu-control-list-of-dual-use-items-enters-into-force); [Cooley, 5 Dec 2025 (search summary) [IND]](https://www.cooley.com/news/insight/2025/2025-12-05-eu--issues-2025-update-to-dual-use-control-list)

**Finland, UK, Japan (older except where noted)**
- **Finland.** The Act on the Export Control of Dual-Use Items (500/2024) took effect 15 Sep 2024. Its national control list covers "quantum computers, components thereof, and components used in the manufacture of quantum computers" and advanced semiconductor items. The Ministry for Foreign Affairs is the licensing authority. The US added Finland to License Exception IEC destinations effective 17 Sep 2024. — [Finnish MFA (search summary) [IND-gov]](https://um.fi/current-affairs/-/asset_publisher/gc654PySnjTX/content/kaksikayttotuotteiden-vientivalvontaa-koskeva-laki-ja-asetus-vientivalvontaneuvottelukunnasta-astuivat-voimaan); [Borenius, 8 Jul 2024 (search summary) [IND]](https://borenius.com/legal-alerts/2024/07/08/finnish-export-controls-adapt-to-technological-developments-amid-geopolitical-tensions)
- **UK.**
  - The Export Control (Amendment) Regulations 2024 (SI 2024/346) took effect 1 Apr 2024. They add PL9013–PL9015; PL9014 covers quantum computers, qubit devices and circuits, quantum control and measurement items, and related software and technology.
  - The sources conflict on EU treatment. Deloitte says a licence is required for all destinations; Akin Gump says a revised open general licence allows exports to all 27 EU states.
  - — [legislation.gov.uk SI 2024/346 [IND-gov]](https://www.legislation.gov.uk/uksi/2024/346/made/data.html); [Akin Gump (search summary) [IND]](https://akingump.com/en/insights/alerts/international-unilateral-export-controls-an-increased-focus-on-advanced-technologies)
  - The national PL9013–9015 entries were deleted and replaced with "500 series" entries by the Export Control (Amendment) (No. 2) Regulations 2025, in force 16 Dec 2025. — [Baker McKenzie (search summary) [IND]](https://sanctionsnews.bakermckenzie.com/?p=4927)
- **Japan.**
  - METI's list-control amendments adding quantum computers, cryo-CMOS circuits and related items were promulgated 8 Jul 2024 and took effect 9 Sep 2024. — [Baker McKenzie (search summary) [IND]](https://sanctionsnews.bakermckenzie.com/japan-updates-listed-controlled-items-to-include-sensitive-items-such-as-quantum-computers)
  - A further 2025 amendment (Cabinet Order No. 102 of 2025, promulgated 28 Mar 2025, effective 28 May 2025 per TIMEWELL) covered advanced chips and quantum-related items. Press reports gave other dates, including a 5 Feb 2025 announcement. — [TIMEWELL (search summary) [IND]](https://timewell.jp/en/columns/japan-supplementary-export-control-2025); [Bloomberg, 31 Jan 2025 (search summary) [IND]](https://www.bloomberg.com/news/articles/2025-01-31/japan-plans-to-curb-exports-of-chips-quantum-computing-tech)

**China (countermeasures)**
- 22 Jun 2026:
  - MOFCOM put 10 US entities on its export-control list, "primarily concentrated in the defense, aerospace, unmanned systems, and rare earth sectors". Named examples are Red Cat, Teal Drones and USA Rare Earth.
  - The Ministry of Finance barred procurement from 46 US entities, e.g., Lockheed Martin, Boeing Defense and Shield AI.
  - The advisory names none of IonQ, Quantinuum, IBM, Google, Rigetti, D-Wave, PsiQuantum, QuEra, Infleqtion or Atom Computing. Not all 56 entities are named.
  - — [Arnold & Porter, 2 Jul 2026 [IND]](https://arnoldporter.com/en/perspectives/advisories/2026/07/china-imposes-export-control-and-government-procurement-restrictions-on-designated-us-companies)
- On 5 Aug 2026 MOFCOM put 7 US entities, including Applied DNA Sciences, on the Anti-Foreign Sanctions Law countermeasure list. None was identified as quantum. — [CMS (search summary) [IND]](https://cms.law/en/chn/legal-updates/china-strengthens-counter-sanctions-and-export-control-regime)

**Investment screening: Quantinuum (CFIUS)**
- On 23 Jul 2021 the company and subsidiaries filed a joint voluntary notice for the Honeywell–Cambridge Quantum "NewCo" transaction. CFIUS found no unresolved national-security issues on 24 Nov 2021, after an NSA was signed with DoD, DOE and Treasury as monitoring agencies (CMAs). — [Q3 2026 10-Q [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162828026072454/qnt-20260930.htm)
- **NSA terms** as described in the prospectus:
  - "limitations on hiring foreign nationals or granting them access to certain facilities, technologies or information";
  - CMA approval or non-objection before certain new employees may access specified IP;
  - CMA approval or non-objection "for certain vendor relationships, facility changes, or property acquisitions";
  - "limitations on developing specified IP outside designated countries";
  - mandatory reporting;
  - no replacement Chairman, CEO, COO or Chief Legal Officer without CMA non-objection, with CMA non-action after a set period counting as non-objection;
  - described as "ongoing and indefinite".
  - — [424B4, 5 Jun 2026 [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162828026041003/quantinuum-424b4.htm)
- **Termination:** "On November 3, 2026, we received a letter from the CMAs notifying the Company that the NSA terminated." Quantinuum remains subject to export controls and the CHIPS Award's research-security, domestic-IP-control and domestic-production requirements. Future foreign investments may face CFIUS review, and those that are "Covered Transactions" under the charter and Stockholder Agreement need Transaction Committee approval first. — [Q3 2026 10-Q, filed 10 Nov 2026 [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162828026072454/qnt-20260930.htm)

**Investment screening: IQM**
- Regulatory matters: "The Business Combination Agreement and Transactions are not subject as a closing condition to any additional federal, state or foreign regulatory requirement or approval, except for (i) filings and registration with the Cayman Registrar… and (ii) the expiration or early termination of the waiting periods… under the HSR Act." — [IQM F-4/A, 3 Jun 2026 [CO]](https://www.sec.gov/Archives/edgar/data/2113060/000119312526255796/d900375df4a.htm)
- The filings describe the Finnish Act 172/2012 regime in general terms only:
  - A non-resident acquiring ≥10% of voting power must notify the Ministry of Economic Affairs and Employment, which "has to confirm the acquisition unless [it] would jeopardize important national interests".
  - Defence-sector targets need approval in advance.
  - No IQM-specific notification is disclosed. "CFIUS" and "National Security and Investment" appear 0 times in IQM's F-4/F-1 versions.
  - — [IQM F-1/A [CO]](https://www.sec.gov/Archives/edgar/data/2113060/000119312526355643/d36013df1a.htm)

**Investment screening: QuEra and PsiQuantum**
- No public CFIUS, NSIA or FIRB record was found. Investors named in the dossiers include Google, SoftBank Vision Fund 2 and NVentures (QuEra), and the Australian Commonwealth via Export Finance Australia, Temasek, BlackRock and others (PsiQuantum). — (dossiers quera.md, psiquantum.md)

### Inferences
- With the NSA ended, the binding national-security constraints on Quantinuum are now export controls, the CHIPS Award's research-security, IP and domestic-production terms, and the company's own Transaction Committee gate on foreign "Covered Transactions". The removal of the officer-appointment non-objection requirement for the Chair, CEO, COO and CLO is the most concrete operational change.
- The EU's 2025 listing harmonised quantum controls across member states. Finland, IQM's home, already had national controls from 2024, so IQM's exports outside the EU needed licences before and after the change, subject to EU and national general authorisations.
- No US rule since Sep 2024 has changed the 4A906 thresholds, as far as the Federal Register term search shows.

### Gaps
- Not checked: the text of Delegated Regulation (EU) 2025/2003 on EUR-Lex (exact entry numbers for quantum computers), the UK "500-series" entries and Japan's 2025 Cabinet Order text.
- No company disclosed a specific export licence, licence denial, ECCN or ECN self-classification, or BIS "is-informed" letter. This applies to QuEra's AIST and NQCC shipments, IQM's ORNL and Maryland activity, Quantinuum's RIKEN, Singapore and Qatar deployments, and IBM's RIKEN, Spain and India systems.
- MOFCOM's full 2025–2026 listing texts were not read. That no US quantum company has been listed is confirmed only from secondary legal summaries.
- No CFIUS, NSIA or Finnish screening records exist publicly for QuEra, PsiQuantum or IQM's listing. CFIUS filings are confidential.
- China's rare-earth export controls (e.g., on ytterbium) and their effect on trapped-ion suppliers were not researched.

---

## 4. Government funding and equity stakes, 2025–2026 (Commerce/CHIPS, DoD OSC, DOE, DARPA, states, Business Finland/EIB/EU for IQM, Japan)

### Takeaway
- **Commerce CHIPS programme.** On 21 May 2026 Commerce signed 9 CHIPS letters of intent worth **$2.013B**, each conditional on a **minority, non-controlling equity stake**. Recipients include IBM ($1B), Quantinuum, PsiQuantum, Atom, D-Wave, Infleqtion and Rigetti (~$100M each), Diraq (≤$38M) and GlobalFoundries ($375M). **IonQ, QuEra and IQM were not among them.**
- **Finalised awards:**
  - Quantinuum: Award Agreement 4 Sep 2026; 2,369,528 shares to Commerce on 9 Sep 2026 at $42.20; tranches of $56M, $32M and $12M.
  - IBM's subsidiary Anderon: 14 Sep 2026; $650M at closing plus $350M on milestones; Anderon, not IBM, issued Commerce a minority equity interest.
  - PsiQuantum: 8 Sep 2026; equity terms undisclosed.
- **DoD.** OSC made a **conditional** loan commitment of up to $150M to PsiQuantum (8 Oct 2026). DARPA QBI ceilings are $15M for Stage B and $300M for Stage C. Stage C (as of 8 Oct 2026) includes IBM, IonQ and PsiQuantum; Quantinuum and QuEra are in Stage B.
- **DOE** renewed its five NQISRCs at up to $625M on 4 Nov 2025.
- **States:**
  - Illinois: PsiQuantum about $200M; IBM a $25M grant via U. Illinois.
  - Maryland: $5M grant plus $20M of a $50M commitment for IonQ.
  - New Mexico: $1.5M LEDA for Quantinuum.
  - Colorado: a $74M quantum tax-credit programme, with no Quantinuum-specific award found.
  - Tennessee: $20M proposed.
  - New York: $360M programme, none specific to Anderon.
- **IQM.** The EIB €35M convertible loan (2022) was **fully repaid by Dec 2025**. Grant income was €3.4M in 2025.
- **Japan.** AIST's ¥6.5B purchase from QuEra (2024), and IBM's RIKEN System Two installed under a NEDO-commissioned project.

### Cited Findings
**Commerce CHIPS: programme**
- The release states that Commerce "announced the signing of 9 letters of intent to provide $2.013 billion in federal incentives under the CHIPS and Science Act". It continues:
  - "GlobalFoundries will receive $375 million in planned funding"; "IBM will receive $1 billion… to establish a new quantum foundry subsidiary".
  - Atom Computing $100M; Diraq "up to $38 million"; D-Wave $100M; Infleqtion $100M; PsiQuantum $100M (electro-optic materials, high-temperature single-photon detectors, ultra-low-loss packaging); Quantinuum $100M (low-loss integrated photonics, optical components at trapped-ion wavelengths); Rigetti "up to $100 million".
  - "The Department will receive a minority, non-controlling equity stake in each company as a condition for receiving the funds".
  - Solicitation 2025-NIST-CHIPS-CRDO-01.
  - — [Commerce/NIST release, 21 May 2026 [IND-gov]](https://www.nist.gov/document/quantum-chips-press-release)
- **IonQ** was not among the LOI signatories. — [same [IND-gov]](https://www.nist.gov/document/quantum-chips-press-release); [PostQuantum, M. Ivezic, 9 Sep 2026 [IND]](https://postquantum.com/industry-news/chips-act-quantum-equity-ota/)
- **IonQ background (older).** In Oct 2025 the WSJ reported preliminary Commerce talks with IonQ, Rigetti and D-Wave about funding in exchange for equity, possibly via warrants, IP licences, royalties or revenue sharing. IonQ declined to comment. A Commerce spokesperson said: "The Commerce Department is not currently negotiating equity stakes with quantum computing companies." — [TechSpot (search summary) [IND]](https://www.techspot.com/news/109986-us-commerce-department-considers-taking-equity-quantum-computing.html); [Barron's via Tiger (search summary) [IND]](https://www-web.itiger.com/news/2577308367)

**Commerce CHIPS: Quantinuum (final)**
- Award Agreement:
  - On 4 Sep 2026 Quantinuum LLC signed an **Other Transaction Agreement** ("Award Agreement") for up to **$100.0M**.
  - The Securities Issuance Agreement was signed 8 Sep 2026. **Commerce acquired 2,369,528 Class A shares on 9 Sep 2026** at a "contractual issuance price of $42.20 per share".
- Tranches:
  - Award Date Tranche: $56.0M (1,326,936 shares).
  - Milestone 1: $32.0M (758,249 shares).
  - Milestone 2: $12.0M (284,343 shares).
- Use of funds and period: funds go only to eligible project costs and must be applied within 30 days or returned. The period of performance runs to the earlier of milestone completion or 5 years.
- Clawback and repurchase: clawback is possible "without forfeiting the Shares". If Commerce terminates for convenience, the company may repurchase the proportionate unfunded shares "for an aggregate purchase price of $1.00".
- Share restrictions: limits on registration rights, transferability and voting.
- Accounting: the shares are excluded from EPS as not yet issued and outstanding for accounting purposes. No clawback liability was recognised at 30 Sep 2026.
- — [Quantinuum Q3 2026 10-Q [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162828026072454/qnt-20260930.htm)
- IP condition: ownership of patentable inventions from funded work, and of certain background IP, must stay with US companies for 10 years after the period of performance or the first commercial sale. — [S-1/A, 26 May 2026 [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162828026037917/quantinuum-sx1a.htm)
- Further terms reported from 8-Ks:
  - The price was the lower of $48.00 (IPO price $60 less 20%) and the award-date close less 15%.
  - Commerce will not vote its shares except on adverse changes.
  - Commerce may sell only the fraction of shares matching disbursed funds without company consent.
  - — [PostQuantum, 9 Sep 2026 [IND]](https://postquantum.com/industry-news/chips-act-quantum-equity-ota/)

**Commerce CHIPS: IBM/Anderon (final)**
- "On September 14, 2026, Anderon LLC… an IBM subsidiary, finalized an award agreement… providing an incentive of up to an aggregate $1.0 billion". Further terms:
  - "IBM has contributed $1.0 billion of cash into Anderon, along with intellectual property and other assets".
  - "$650 million of the award [was made available] at closing… and an additional $350 million will be granted upon the achievement of contractual milestones".
  - "**Anderon issued a minority equity interest to the Department**", which IBM presents as a noncontrolling interest.
  - Commerce has termination-for-convenience and clawback rights. Undeployed funds may be invested in US government securities. IBM keeps control and consolidates Anderon.
  - — [IBM Q3 2026 10-Q, filed 22 Oct 2026 [CO]](https://www.sec.gov/Archives/edgar/data/51143/000005114326000095/ibm-20260930.htm)
- Date discrepancy: IBM's newsroom release announcing the finalisation is dated 16 Sep 2026; the 10-Q gives 14 Sep. — [IBM newsroom, 16 Sep 2026 (dossier) [CO]](https://newsroom.ibm.com/2026-09-16-anderon,-an-ibm-company,-finalizes-agreement-with-the-u-s-department-of-commerce-for-a-1-billion-chips-award-to-accelerate-r-d-for-u-s-based-pure-play-quantum-foundry)

**Commerce CHIPS: PsiQuantum and others (final)**
- PsiQuantum signed definitive documentation (reported 8 Sep 2026). "No equity terms disclosed." — [PostQuantum [IND]](https://postquantum.com/industry-news/chips-act-quantum-equity-ota/); [TQI, 8 Sep 2026 (release-based; dossier) [CO-relay]](https://thequantuminsider.com/2026/09/08/psiquantum-finalizes-100m-us-government-award-quantum-computing-rd/)
- Comparators reported from 8-Ks:
  - Rigetti: 7,739,938 shares at an implied $12.92.
  - D-Wave: 7,095,721 shares at $14.093.
  - GlobalFoundries: 9,907,399 shares at $37.85 (about $375M).
  - Atom Computing, Infleqtion and Diraq had not finalised as of 17 Sep 2026.
  - — [PostQuantum, 9 Sep 2026 (updated 27 Sep) [IND]](https://postquantum.com/industry-news/chips-act-quantum-equity-ota/)

**DoD: Office of Strategic Capital and DARPA**
- PsiQuantum OSC loan:
  - Conditional commitment for a loan of "up to $150 million" from the Department of War's OSC for the 140,000 sq ft Milpitas "PsiFactory" (test, assembly and cryogenic systems), announced 8 Oct 2026.
  - It is "strictly conditional"; a final commitment requires satisfying "financial, legal, technical, and regulatory conditions". It is to be combined with PsiQuantum's own investment.
  - — [TQI, 8 Oct 2026 (release-based; search summary) [CO-relay]](https://thequantuminsider.com/2026/10/08/psiquantum-conditional-150m-loan-california-quantum-facility/); [Quantum Computing Report (search summary) [IND]](https://quantumcomputingreport.com/psiquantum-secures-conditional-150-million-loan-commitment-from-u-s-office-of-strategic-capital/)
  - QCR describes it as part of a ~$350M DoW quantum package. — [QCR (search summary) [IND]](https://quantumcomputingreport.com/u-s-department-of-war-announces-350-million-quantum-package-highlighted-by-150-million-osc-loan-commitment-for-psiquantum/)
- DARPA QBI:
  - Per-performer ceilings: Stage A up to $1M; Stage B up to $15M; Stage C up to $300M.
  - Stage C: Atom Computing, Diraq, IBM, IonQ, Microsoft, PsiQuantum.
  - Stage B: Nord Quantique, Photonic, Quantinuum, Quantum Motion, QuEra, Silicon Quantum Computing, Xanadu.
  - Google Quantum AI is listed under Stage A. IQM is not listed. The list is "current as of Oct. 8, 2026".
  - — [DARPA QBI page [IND-gov]](https://www.darpa.mil/research/programs/quantum-benchmarking-initiative)
- PsiQuantum's DARPA agreements: $125M "expanded", performance-based QBI agreement (22 Jul 2026); $31.8M Stage C agreement (Sep 2025, older). — (dossier) [HPCwire reprint of PsiQuantum release [CO-relay]](https://www.hpcwire.com/off-the-wire/psiquantum-signs-125m-agreement-with-darpa/)

**DOE**
- On 4 Nov 2025 DOE announced $625M to renew its five National QIS Research Centers (BNL C2QA, ANL, LBNL, ORNL QSC, Fermilab SQMS) for up to five years. Each gets $125M in FY2025 dollars, with later years subject to appropriations. Older. — [TQI, 4 Nov 2025 (search summary) [IND]](https://thequantuminsider.com/2025/11/04/doe-announces-625-million-to-advance-national-quantum-information-science-research-centers/); [DOE (search summary) [IND-gov]](https://www.energy.gov/node/4853605)
- Quantinuum reports participating in "four winning proposals under Phase 1" of the DOE Genesis Mission. — (dossier) [Quantinuum Q3 2026 release [CO]](https://www.sec.gov/Archives/edgar/data/2110105/000162828026071000/q32026earningspressrelease.htm)

**States**
- **Illinois (PsiQuantum; older except where noted).**
  - MICRO Tier 2 agreement effective 12 Jul 2024: 154 jobs by 31 Dec 2029 at ≥120% of the county average wage; up to 15 years of credits; recapture on default. — (dossier) [Illinois DCEO MICRO agreement [IND-gov]](https://dceo.illinois.gov/content/dam/soi/en/web/dceo/expandrelocate/incentives/micro-agreements/psiquantum-corp-micro-agreement-executed-redacted-v2-redacted.pdf)
  - About $200M of state incentives, including $92M through MICRO, against a $1.1B company investment. — (dossier) [Capitol News Illinois, 26 Jul 2024 [IND]](https://capitolnewsillinois.com/news/quantum-business-park-coming-to-chicago-backed-by-700m-from-state-of-illinois/)
- **Illinois (IBM).** A $25M state grant went to the University of Illinois Board of Trustees for the Chicago IBM System Two (purchase, site preparation, relocation). The system went live as announced on 6 Nov 2026. — (dossier) [XenoSpectrum, Nov 2026 [IND]](https://xenospectrum.com/en/ibm-quantum-system-two-chicago-nighthawk/)
- **Colorado.**
  - HB24-1325 (signed May 2024) created a 100% refundable credit for shared quantum-facility capital (≤$44M in reservations) and loan-loss credits (≤$30M, 2025–2036), about $74M in total. — [Colorado General Assembly, HB24-1325 (search summary) [IND-gov]](https://leg.colorado.gov/bills/HB24-1325); [QCR (search summary) [IND]](https://quantumcomputingreport.com/colorado-governor-signs-a-bill-providing-74-million-in-tax-credits-for-quantum-r-d-but-there-is-a-catch/)
  - In Feb 2025 the state offered more than $4.3M of incentives for "Project Q-Chips" in Broomfield. The company was not named, and Quantinuum was not confirmed. — [BizWest, 20 Feb 2025 (search summary) [IND]](https://bizwest.com/2025/02/20/state-offers-4m-in-incentives-for-broomfield-quantum-companys-expansion)
  - Quantinuum's prospectus discloses no state incentive (my search of the 424B4).
- **New Mexico (Quantinuum).**
  - The State and the City of Albuquerque each provide $750,000 in LEDA funds (announced 18 Aug 2026) for an integrated-photonics R&D hub at 5501 Wilshire.
  - Quantinuum is to invest $32.5M. Officials project $86.4M of economic impact over 10 years. The first phase is due by end-2026 and a second lab in 2027.
  - — [NM EDD LEDA document, Aug 2026 (search summary) [IND-gov]](https://edd.newmexico.gov/wp-content/uploads/2026/08/QuantinuumLEDA.pdf); [QCR (search summary) [IND]](https://quantumcomputingreport.com/quantinuum-secures-1-5m-in-city-and-state-leda-funding-to-expand-rd-center-in-albuquerque/); [TQI, 20 Aug 2026 (search summary) [IND]](https://thequantuminsider.com/2026/08/20/quantinuum-expands-research-operations-albuquerque/)
  - New Mexico also runs a federal-match programme for DARPA QBI Stage C performers that work in-state (minimum $1M per award). — [QCR (search summary) [IND]](https://quantumcomputingreport.com/new-mexico-adds-darpa-qbi-stage-c-and-quantumeagle-to-targeted-federal-match-grant-program/amp/)
- **Maryland (IonQ).**
  - The "Capital of Quantum" initiative launched in Jan 2025 with a $1B goal. — [Governor of Maryland release, Jan 2025 (search summary) [IND-gov]](https://governor.maryland.gov/news/press-releases/governor-moore-announces-1-billion-capital-quantum-initiative)
  - The FY2027 budget includes $20M toward a multi-year $50M commitment for IonQ's College Park HQ.
  - There is a separate $5M Board of Public Works grant for HQ design and construction, and a $7.5M UMD–IonQ agreement (Apr 2026).
  - It is unclear how the $5M and the $50M relate.
  - — [TQI, 29 Apr 2026 (search summary) [IND]](https://thequantuminsider.com/2026/04/29/maryland-doubles-down-on-quantum-with-ionq-hq-funding-and-startup-infrastructure/); [QCR (search summary) [IND]](https://quantumcomputingreport.com/ionq-secures-5m-maryland-grant-for-global-headquarters-construction/)
- **New York.** A $360M state quantum allocation ($300M for SUNY Stony Brook and $60M for regional hubs) was found. **No state award specific to Anderon was found.** — [QCR (search summary) [IND]](https://quantumcomputingreport.com/new-york-deploys-360-million-for-stony-brook-and-regional-hubs-supported-by-1-37b-in-federal-foundry-commitments/)
- **Tennessee (IonQ).**
  - The Governor proposed $20M for a Tennessee Quantum Initiative (Feb 2026); legislative approval is not confirmed. EPB has a $4M NIST grant.
  - The IonQ–EPB deal (Apr 2025) is worth $22M, and IonQ is investing $15M in a Chattanooga research centre. EPB launched an IonQ Forte Enterprise on 18 Sep 2026.
  - — [TQI, 4 Feb 2026 (search summary) [IND]](https://thequantuminsider.com/2026/02/04/tennessee-quantum-initiative-20m-state-4m-federal-grant/); [TQI, 18 Sep 2026 (search summary) [IND]](https://thequantuminsider.com/2026/09/18/epb-launches-ionq-forte-enterprise-quantum-computer-chattanooga/)

**IQM (EU and Finland)**
- EIB loan:
  - "On February 9, 2022, we entered into a convertible loan agreement with the European Investment Bank… two tranches of €25.0 million and €10.0 million." The loan carried a fixed 5.0% rate, a six-year maturity from disbursement and a conversion option.
  - "Since the loan was fully repaid the derivative financial liability was derecognized as of December 2025."
  - — [IQM F-1/A [CO]](https://www.sec.gov/Archives/edgar/data/2113060/000119312526355643/d36013df1a.htm)
- Government grant income was €3,359K in 2025 and €3,853K in 2024. In 2020 the Finnish subsidiary "received a loan granted by the Finnish Ministry of Finance" for quantum R&D; the amount is not given. — [IQM F-4/A [CO]](https://www.sec.gov/Archives/edgar/data/2113060/000119312526255796/d900375df4a.htm)
- Q2 2026: other operating income rose to €1.7M, from €0.6M, "driven by higher grant income resulting from newly funded research and development projects".
- Public-sector customers were 98.0% of H1 2026 revenue and 99.5% of H1 2025 revenue, including EuroHPC JU-funded programmes. — [IQM F-1/A [CO]](https://www.sec.gov/Archives/edgar/data/2113060/000119312526355643/d36013df1a.htm)
- Older support:
  - Business Finland grants of €3.3M, and an EIC Accelerator award of a €2.5M grant plus up to €15M of equity. Undated in the source. — [Help Net Security (search summary) [IND]](https://www.helpnetsecurity.com/?p=148964)
  - VTT received a €70M special government grant in 2024 for a 300-qubit computer supplied by IQM. — [VTT (search summary) [IND]](https://www.vttresearch.com/en/news-and-ideas/iqm-quantum-computers-supply-finland-world-leading-superconducting-300-qubit-quantum)
- No 2025–2026 Business Finland or new EIB award to IQM was found. IQM's 2026 pre-listing financing was €50M from BlackRock-managed funds (Mar 2026). — [TQI, 30 Mar 2026 (search summary) [CO-relay]](https://thequantuminsider.com/2026/03/30/iqm-secures-e50-million-financing-to-accelerate-global-growth/)

**Japan**
- QuEra:
  - AIST awarded QuEra a ¥6.5B contract (30 Apr 2024) for a gate-based neutral-atom system next to ABCI-Q. It was installed in Tsukuba in May 2025. — (dossier, older) [QuEra release [CO]](https://www.quera.com/press-releases/aist-selects-quera)
  - AIST's G-QuAT has offered external access to the QuEra system since 24 Mar 2026. — [AIST G-QuAT (dossier; page returned HTTP 503 to the earlier researcher) [IND-gov]](https://unit.aist.go.jp/g-quat/HowToUse/en/news/news_en_20260324.html)
- IBM: the RIKEN IBM Quantum System Two (156-qubit Heron, Kobe, unveiled 23 Jun 2025) was installed "as part of a project commissioned by NEDO" (under METI) to link Fugaku and quantum computers. No amount is disclosed. — [IBM newsroom, 23 Jun 2025 (search summary) [CO]](https://newsroom.ibm.com/2025-06-23-ibm-and-riken-unveil-first-ibm-quantum-system-two-outside-of-the-u-s); NEDO detail from the RIKEN Japanese announcement (search summary; not opened)

### Inferences
- The two structures differ:
  - Quantinuum and the other public quantum companies issued parent-level common stock to Commerce at a discount, priced against the full award. Commerce keeps the shares even if funds are clawed back, and only termination for convenience lets the company buy back unfunded shares for $1.
  - IBM took a subsidiary-level route. Commerce holds a minority interest in Anderon, not IBM, which limits the government's exposure to the foundry vehicle.
- Arithmetic: the share values reconcile to the award. 2,369,528 × $42.20 ≈ $99.99M ≈ the $100M award. At 30 Sep 2026, Quantinuum had the portion of each award available at signing without milestones was $56M (56%) for Quantinuum and $650M (65%) for Anderon (arithmetic from the 10-Qs).
- Among the six assigned companies, only IBM (CHIPS + QBI Stage C), Quantinuum (CHIPS + Stage B) and PsiQuantum (CHIPS + Stage C) have both CHIPS money and DARPA QBI status. QuEra has DARPA Stage B but no CHIPS letter of intent. IQM has neither.

### Gaps
- PsiQuantum's CHIPS terms: equity percentage and instrument, tranche split and award date.
- Anderon: Commerce's percentage interest, the price, and whether warrants were issued. The IBM 10-Q gives no percentage.
- Whether OSC has made PsiQuantum's conditional loan final.
- DARPA QBI contract values for IBM, IonQ, Quantinuum and QuEra individually; only the ceilings are public.
- Japan: the yen value of the NEDO-commissioned RIKEN–IBM project and the budget line funding AIST's QuEra purchase.
- Business Finland awards to IQM in 2025–2026 (the Business Finland site was not checked).
- Whether Tennessee's $20M was enacted.
- Whether Colorado's "Project Q-Chips" was Quantinuum.
- Any New York ESD incentive for Anderon.

---

## 5. IonQ legal gaps (coordinator scope addition): suits 2023–2026, 2026 "non-cash legal settlements", short-seller reports, UK NSIA / ID Quantique approvals, the investor in the equity offerings

### Takeaway
- **Lawsuits.** No IonQ derivative suit and no new securities, contract or IP case naming IonQ was found in federal dockets for 2023–2026. After Wolfpack's report there were only law-firm "investigations". The one new federal case is an FMLA employment suit, *Jones v. IonQ Quantum, Inc. & Vector Atomic*, N.D. Cal. 4:26-cv-03806. It was removed 30 Apr 2026 and has been stayed since 11 May 2026.
- **Settlements.** The 2026 "non-cash legal settlements" were $5.7M in Q2 and $5.525M for nine months. The 93,879 shares ($4.825M) recorded in Q3 match **exactly the 93,879 shares issued on 1 Jul 2026 to Rocket Lab USA, Inc. "pursuant to pre-existing contractual obligations"**. The underlying dispute is not described.
- **Short sellers.** Kerrisdale (Mar 2025) attacked valuation, roadmap and transparency. Wolfpack (4 Feb 2026) alleged earmark-dependent DoD revenue, unfunded bookings and insider sales. IonQ called the latter "false, misleading, and unsubstantiated claims".
- **UK NSIA.** A UK final order (in force 11 Sep 2025) cleared the Oxford Ionics deal on conditions: hardware hosted in the UK and functions kept in the UK.
- **ID Quantique.** No CFIUS or Swiss approval for ID Quantique is disclosed.
- **Investor.** All three offerings were sold through J.P. Morgan as sole underwriter. **The SEC filings do not name the end investor, but IonQ's press releases name Heights Capital Management for July 2025, October 2025 and October 2026.**

### Cited Findings
**(1) Cases 2023–2026**
- Case-name search "IonQ" returns only:
  - *Jones v. IonQ Quantum, Inc.* (N.D. Cal. 2026);
  - *Defeo v. IonQ* (4th Cir., two dockets);
  - *Fisher v. IonQ* (D. Md. 2022);
  - *Leacock v. IonQ* (D. Md. 2022).
  - — [CourtListener, caseName:IonQ [IND-court]](https://www.courtlistener.com/?q=caseName%3AIonQ&type=r)
- *Jones v. IonQ Quantum, Inc. and Vector Atomic, Inc.*, No. 4:26-cv-03806 (N.D. Cal.):
  - Removed 30 Apr 2026 from Alameda County Superior Court (No. 26CV176972). Cause 29 U.S.C. discrimination, nature of suit 751 (FMLA).
  - A joint stipulation "Staying Litigation" was granted 11 May 2026. The case was reassigned to Magistrate Judge Laurel D. Beeler.
  - A status report was filed 14 Oct 2026, and a status conference was set for 12 Nov 2026.
  - — [CourtListener docket 73273934 [IND-court]](https://www.courtlistener.com/docket/73273934/jones-v-ionq-quantum-inc/)
- *Fisher v. IonQ*, No. 8:22-cv-01536 (D. Md.): a securities case filed 22 Jun 2022 and consolidated into lead case 22-cv-1306. It was closed with the 28 Sep 2023 dismissal with prejudice, so it is part of the already-documented class action. — [CourtListener docket 67840234 [IND-court]](https://www.courtlistener.com/docket/67840234/fisher-v-ionq-inc/)
- Company statement: "there were no legal proceedings pending other than those for which we have determined that the possibility of a material outflow is remote". — [IonQ Q2 2026 10-Q, Note 12 [CO]](https://www.sec.gov/Archives/edgar/data/1824920/000119312526341001/ionq-20260630.htm); Q3 Note 12 uses the same framework — [IonQ Q3 2026 10-Q [CO]](https://www.sec.gov/Archives/edgar/data/1824920/000119312526449829/ionq-20260930.htm)
- Law-firm notices after Wolfpack were investigations, not complaints:
  - Scott+Scott (whether directors or officers breached fiduciary duties);
  - Ademi LLP (5 Feb 2026, focused on nearly $400M of executive stock sales);
  - Robbins LLP.
  - — [Scott+Scott (search summary) [IND]](https://scott-scott.com/sec-investigation/ionq-inc/); [Ademi via Barchart (search summary) [IND]](https://www.barchart.com/story/news/61874/ademi-llp-investigates-claims-of-securities-fraud-against-ionq-inc); [24/7 Wall St, 15 Feb 2026 (search summary) [IND]](https://247wallst.com/investing/2026/02/15/ionq-stock-falls-2-5-this-week-on-short-seller-report-and-legal-probe-converge/)
- Separate SOX matter: after the SkyWater acquisition (31 Jul 2026), IonQ took on SkyWater's previously identified **material weaknesses** in "revenue accounting process" and "account reconciliations at… Fab 25". These "cannot be considered remediated until our remediation plans are completed". — [IonQ Q3 2026 10-Q [CO]](https://www.sec.gov/Archives/edgar/data/1824920/000119312526449829/ionq-20260930.htm)

**(2) "Non-cash legal settlements"**
- Q2 2026 Adjusted EBITDA reconciliation: "Non-cash legal settlements and related costs" of **$5,700K** for both Q2 and the first half of 2026 (nil in 2025). — [IonQ Q2 2026 results, 8-K Ex. 99.1, 5 Aug 2026 [CO]](https://www.sec.gov/Archives/edgar/data/1824920/000119312526335040/ionq-ex99_1.htm)
- Q3 2026: **$(175)K** for Q3 and **$5,525K** for nine months. — [IonQ Q3 2026 results, 8-K Ex. 99.1, 5 Nov 2026 [CO]](https://www.sec.gov/Archives/edgar/data/1824920/000119312526449779/ionq-ex99_1.htm)
- Statement of equity, Q3 2026: "Issuance of common stock related to legal settlements: 93,879 [shares]… $4,825 [thousand]". — [IonQ Q3 2026 10-Q [CO]](https://www.sec.gov/Archives/edgar/data/1824920/000119312526449829/ionq-20260930.htm)
- Unregistered sales: "On July 1, 2026, pursuant to pre-existing contractual obligations, the Company issued to Rocket Labs USA, Inc. 93,879 shares of the Company's common stock", relying on §4(a)(2) and Reg D. — [IonQ Q2 2026 10-Q, Part II Item 2 [CO]](https://www.sec.gov/Archives/edgar/data/1824920/000119312526341001/ionq-20260630.htm)
- No 8-K on a settlement was found. The CourtListener search "Rocket Lab" AND "IonQ" returned no case between them. — [CourtListener [IND-court]](https://www.courtlistener.com/?q=%22Rocket+Lab%22+AND+%22IonQ%22&type=r)

**(3) Short-seller reports**
- **Kerrisdale Capital (March 2025, older).** The report date is not given on the pages read; the Stocktwits page metadata is inconsistent (it shows "updated March 5, 2026"). It was published as a blog post. Allegations:
  - IonQ trades at a "staggering" 40× consensus 2026 revenue, as a ~$5B company whose stock had tripled.
  - Scepticism about the roadmap from 80–100 physical qubits to more than 4,000 by 2026 and 32,000 by 2028.
  - Former employees flagged "monumental" scaling challenges.
  - Management lacks transparency, and the CEO had sold $37M of stock: "hallmarks of a disaster in the making".
  - The stock fell nearly 4% to $20.97 mid-session.
  - — [Stocktwits [IND]](https://stocktwits.com/news-articles/markets/equity/ionq-stock-slides-on-kerrisdale-short-report/ch7dju4RbRv)
  - Further claims from a search summary of Benzinga (page returned 403): no disclosed photonic-interconnect metrics, and a former executive saying a claimed 32-qubit system (2020) was 11 qubits. — [Benzinga, Mar 2025 (search summary) [IND]](https://benzinga.com/trading-ideas/movers/25/03/44307671/is-high-flying-ionq-stock-a-disaster-in-the-making-shares-slide-as-short-seller-raises-red-f)
- **Wolfpack Research (4 Feb 2026).** Allegations:
  - Up to 86% of IonQ's 2022–2024 revenue came from Pentagon research funding the Pentagon "never requested", added as "backdoor earmarks" and cancelled after 2025.
  - The AFRL $54.5M award (Sep 2024) had only $12M funded.
  - Of $75.6M of 2024 Pentagon bookings, about $21M was funded; the other $54.6M (58% of total bookings) was unfunded.
  - IonQ later stopped reporting bookings.
  - Managers, including CEO Niccolo de Masi and former CEO Peter Chapman, sold almost $400M of stock after the earmarks were removed, and new 10b5-1 plans were adopted.
  - IonQ "bought" revenue through Capella ($425M), Vector Atomic, the ID Quantique controlling stake ($116M) and SkyWater ($1.8B).
  - Wolfpack disclosed a short position.
  - — [Fortune, J. Kahn & J. Edwards, 4 Feb 2026 [IND]](https://fortune.com/2026/02/04/ionq-wolfpack-research-short-seller-says-quantum-computing-company-misled-investors-about-cancelled-government-backdoor-earmarks/)
- **IonQ's response** came in a statement after Fortune's deadline on 4 Feb 2026: "false, misleading, and unsubstantiated claims from a short-seller that is attempting to profit by driving down the price of IonQ shares". DCD adds that IonQ said the report contains "substantial misrepresentations as to IonQ's government relationships, business strategy, and financial sustainability". — [Fortune [IND]](https://fortune.com/2026/02/04/ionq-wolfpack-research-short-seller-says-quantum-computing-company-misled-investors-about-cancelled-government-backdoor-earmarks/); [DCD (search summary) [IND]](https://www.datacenterdynamics.com/en/news/ionq-disputes-claims-from-short-seller-that-lost-government-contracts-have-left-546m-black-hole-in-companys-revenue/)
- **Market move (sources conflict).** Fortune reported the stock about 8% lower at the 4 Feb close. MarketBeat reported a close of $30.37, down 14.1% (5 Feb 2026). Morgan Stanley's Schedule 13G/A filed 12 Feb 2026 coincides with reports that it cut its stake below 5%. — [MarketBeat (search summary) [IND]](https://www.marketbeat.com/instant-alerts/ionq-nyseionq-stock-price-down-141-heres-why-2026-02-05/); [EDGAR, IonQ subject filings [IND-gov]](https://data.sec.gov/submissions/CIK0001824920.json)
- No other 2025–2026 short-seller report on IonQ was found.

**(4) UK NSIA (Oxford Ionics) and ID Quantique**
- The Chancellor of the Duchy of Lancaster made a final order under s.26 of the National Security and Investment Act 2021, "which comes into force on 11 September 2025" (parties: IonQ Inc. and Oxford Ionics Limited). The deal may proceed on condition that the parties:
  - "(i) host current and future generations of Oxford Ionics' trapped-ion quantum computing hardware in the UK to allow for its independent assessment and validation on request as part of current or future government programmes or contracts";
  - "(ii) maintain Oxford Ionics' science, engineering and infrastructure functions in the UK, including suitably qualified and experienced personnel, tangible and intangible assets and manufacturing capacity related to the development of trapped-ion quantum computing hardware".
  - The risk cited is "Oxford Ionics' leading role in developing cutting edge quantum computing capabilities".
  - — [GOV.UK notice of final order, published 11 Sep 2025 [IND-gov]](https://www.gov.uk/government/publications/acquisition-of-oxford-ionics-limited-by-ionq-inc-notice-of-final-order/acquisition-of-oxford-ionics-limited-by-ionq-inc-notice-of-final-order)
- The share purchase agreement (signed 7 Jun 2025) set consideration at $1,065M in IonQ stock plus $10M cash. Its closing conditions included "the obtainment, expiration, or termination… of certain regulatory approvals imposed by governmental entities". — [IonQ 8-K, 9 Jun 2025 [CO]](https://www.sec.gov/Archives/edgar/data/1824920/000119312525137398/d17095d8k.htm)
- IonQ announced on 12 Sep 2025 that "all deal conditionality [was] satisfied". — [TQI, 12 Sep 2025 (search summary) [IND]](https://thequantuminsider.com/2025/09/12/uk-clears-ionq-acquisition-of-oxford-ionics-with-conditions/)
- IonQ's 2025 10-K and Q3 2026 10-Q do not mention the NSIA order (0 hits).
- **ID Quantique:** IonQ announced completion of its controlling-stake acquisition on 6 May 2025. No CFIUS or Swiss approval is mentioned in that release, in the 10-K or in the 10-Q text searched; "CFIUS" appears 0 times. — [IonQ release, 6 May 2025 (search summary) [CO]](https://ionq.com/news/ionq-completes-acquisition-of-id-quantique-cementing-leadership-in-quantum); [IonQ 2025 10-K [CO]](https://www.sec.gov/Archives/edgar/data/1824920/000119312526071562/ionq-20251231.htm)

**(5) Investor in the July 2025, October 2025 and October 2026 offerings**
- **SEC filings** name only "J.P. Morgan Securities LLC as sole underwriter". The underwriting tables list J.P. Morgan as the only purchaser, and no end investor is named in the 424B5s or 8-Ks:
  - July 2025: 14,165,708 shares at $55.49; 3,855,557 pre-funded warrants; 36,042,530 Series A warrants at $99.88, 7-year. — [424B5, 7 Jul 2025 [CO]](https://www.sec.gov/Archives/edgar/data/1824920/000119312525155901/d872422d424b5.htm); [8-K, 9 Jul 2025 [CO]](https://www.sec.gov/Archives/edgar/data/1824920/000119312525156889/d35359d8k.htm)
  - October 2025: 16,500,000 shares; 5,005,400 pre-funded warrants; 43,010,800 Series B warrants; combined price $93.00. — [424B5, 10 Oct 2025 [CO]](https://www.sec.gov/Archives/edgar/data/1824920/000119312525236452/d68634d424b5.htm); [8-K, 14 Oct 2025 [CO]](https://www.sec.gov/Archives/edgar/data/1824920/000119312525238353/d36977d8k.htm)
  - October 2026: 20,500,000 shares; 29,500,000 pre-funded warrants; 100,000,000 Series C warrants. — [424B5, 14 Oct 2026 [CO]](https://www.sec.gov/Archives/edgar/data/1824920/000119312526421074/d165327d424b5.htm); [8-K, 16 Oct 2026 [CO]](https://www.sec.gov/Archives/edgar/data/1824920/000119312526424230/ionq-20261014.htm)
- **IonQ press releases name the investor:**
  - Jul 2025: the securities "were purchased from the underwriter by Heights Capital Management, Inc." — [IonQ release, 7 Jul 2025 (search summary) [CO]](https://ionq.com/news/ionq-announces-pricing-of-usd1-0-billion-equity-offering)
  - Oct 2025: the securities were sold to "an entity managed by Heights Capital Management" at $93, with Series B warrants at $155. — [IonQ IR release, 10 Oct 2025 (search summary) [CO]](https://investors.ionq.com/news/news-details/2025/IonQ-Announces-Pricing-of-2-0-Billion-Equity-Offering/default.aspx); [TQI (search summary) [CO-relay]](https://thequantuminsider.com/2025/10/10/ionq-announces-pricing-of-2-0-billion-equity-offering/)
  - Oct 2026: the securities "will be purchased from the underwriter by an entity managed by Heights Capital Management, Inc.", with Skadden as investor counsel; price $40, Series C warrants at $69.46, closed 16 Oct 2026. — [TQI, 14 Oct 2026 (search summary) [CO-relay]](https://thequantuminsider.com/2026/10/14/ionq-announces-pricing-2-billion-equity-offering/); [QCR (search summary) [IND]](https://quantumcomputingreport.com/ionq-announces-pricing-of-2-0-billion-equity-offering-purchased-by-heights-capital-management/)
- **No Schedule 13G** from Heights Capital on IonQ appears on EDGAR from Jul 2025 to Nov 2026. The 13G/13G-A filers in that period are Vanguard, BlackRock and Morgan Stanley. — [EDGAR, IonQ subject filings [IND-gov]](https://data.sec.gov/submissions/CIK0001824920.json)

### Inferences
- The Q2 accrual of $5.7M and the Q3 share issuance of $4.825M (93,879 shares) plus a $(175)K Q3 true-up give the $5.525M nine-month total. Together with the matching share count, this indicates that the "legal settlement" was the Rocket Lab share issuance. "Pursuant to pre-existing contractual obligations" suggests a contract dispute, but IonQ has not said so.
- The NSIA conditions tie IonQ to keeping Oxford Ionics' hardware generations and engineering base in the UK and available for UK government validation. This constrains any consolidation of trapped-ion R&D in the US.
- Heights is consistently identified only in company releases, not in the registration documents, where J.P. Morgan is the nominal purchaser. The absence of a 13G is consistent with ownership blockers in the warrants, but this was not verified.

### Gaps
- The nature of the Rocket Lab claim and any settlement agreement, which is not exhibited in the filings found.
- State-court or Delaware Chancery derivative or §220 actions; only law-firm investigation notices were found.
- The Kerrisdale and Wolfpack reports themselves, and the exact date of the Kerrisdale report.
- IonQ's verbatim response to Kerrisdale. A search summary attributed "baseless… every few years" to de Masi, but this is not verified.
- Any IonQ 8-K or blog rebuttal to Wolfpack beyond the statements to the press.
- Any CFIUS filing for IonQ's foreign acquisitions, and Swiss treatment of the ID Quantique deal.
- Whether the October 2026 offering's purchaser entity is the same Heights fund as in 2025; the releases say "an entity managed by".
- The warrant blocker percentages.
