# Noble Bankruptcy Forensic Audit Report

## User prompt 1

GLOBAL CHAT RULES (PERMANENT — ZERO TOLERANCE FOR HANDWAVING):
- SILENT INTELLIGENCE ONLY: Raw dated primary facts, exact figures, and verbatim legal/filing text. Zero opinions, adjectives, marketing language, stock prices, or valuation multiples.
- NO intros or summaries. Start immediately with dense markdown tables + max 3 dry technical bullets.
- ADVERSARIAL EXTERNAL-SOURCE STANDARD: Query U.S. Bankruptcy Court filings (PACER / Stretto / Epiq / Kroll / Omni / CourtListener), official Chapter 11 petitions, First Day Declarations, Top 20/30 Unsecured Creditors Lists, Schedules E/F, Claims Registers, and Rigaku 9M 2026 disclosures.
- MANDATORY GAP RULE: If an exact court schedule, creditor claim, or recovery rate cannot be verified from primary sources, write exact `"N/A (checked [exact database/docket])"` — NEVER estimate or guess.
- ANTI-TIMEOUT URL RULE: Cite exact docket/filing ID + date inline; list ONE direct primary URL per document at the bottom.

TARGET #4 (Rigaku `268A.T`) — STEP R4-A1: U.S. DISTRIBUTOR "NOBLE" CHAPTER 11 BANKRUPTCY FORENSIC AUDIT:

1. Debtor Identification & Case Timeline:
   - Identify the exact legal debtor entity (e.g., Noble Supply & Logistics, LLC / Noble Sales Co., Inc. / parent holding co.), bankruptcy court district, case number, Chapter 11 petition date (2026), claims agent, and current case status (reorganization plan, 363 sale, or liquidation).
2. Exact Rigaku Creditor Claim vs. ¥650M Allowance Reconciliation:
   - Search the Top 20/30 Unsecured Creditors List, Schedules E/F, and official Claims Register for **Rigaku Corp.**, **Rigaku Americas Corp.**, **Rigaku Analytical Devices (`RAD`, handheld Raman/LIBS)**, or any Rigaku affiliate.
   - Extract exact gross USD claim amount (secured vs. unsecured / disputed / contingent), convert to JPY at Sep 30, 2026 FX (¥158.9/USD Q3 avg & exact Sep 30 spot), and reconcile directly against Rigaku's 9M 2026 **¥650M** bad-debt provision (¥50M H1 + ¥600M Q3) to determine whether ¥650M covers 100% of gross exposure or leaves unprovisioned residual write-off risk for Q4 2026.
3. Recovery & Commercial Continuity Check:
   - Document any disclosed general unsecured creditor recovery estimate (cents on the dollar), DIP financing / critical-vendor status for Rigaku, and whether Noble remains an active DoD/federal distribution channel for Rigaku Analytical Devices or has been replaced.

## Model response 1

### 1. Debtor Identification & Case Timeline

| Field | Primary Filing Fact (As of November 20, 2026) | Source Docket / Filing ID & Date |
| :--- | :--- | :--- |
| **Lead Legal Debtor Entity** | **Noble Supply & Logistics, LLC** (EIN last 4: `7926`; successor to `Noble Sales Co., Inc.`; HQ: 1 Marina Park Drive, Suite 220, Boston, MA 02210) | `Doc 1` (08/30/2026); `Doc 351` (10/16/2026); `Doc 484` n.1 (11/16/2026) |
| **Parent & Affiliated Debtors (11 Total)** | `Noble Equity Holdings, LLC` (`0851`); `Noble.com, LLC` (`4712`, 100% equity owner of Lead Debtor; Case `26-11377`); `COTS Solutions, LLC` (`4477`); `Federal Resources Supply Company, LLC` (`3636`, Case `26-11371`); `FRS Holdings, LLC` (`2327`); `K.D. Analytical Consulting, LLC` (`6637`, Case `26-11373`); `KDA Acquisition, LLC` (`5870`); `Noble Defense Corporation` (`N/A`); `Noble Mission Support, LLC` (`7908`, Case `26-11378`); `Tactical & Survival Specialties, LLC` (`2266`, Case `26-11379`). Non-debtor affiliate: `Noble Holdco, Inc.` | `Doc 1` (08/30/2026); `Doc 68` (Joint Admin. Order); `Doc 351` (10/16/2026); `Doc 484` n.1 (11/16/2026) |
| **Court, Judge & Case Number** | U.S. Bankruptcy Court for the District of Delaware; Hon. Craig T. Goldblatt (`CTG`); **Case No. 26-11369 (CTG)** (Jointly Administered) | `Doc 1` (08/30/2026); `Doc 68`; `Doc 484` (11/16/2026) |
| **Chapter 11 Petition Date** | **August 30, 2026** (voluntary petitions; public announcement August 31, 2026) | `Doc 1` (08/30/2026); PR Newswire (08/31/2026) |
| **Claims & Noticing Agent** | **Kurtzman Carson Consultants, LLC d/b/a Verita Global** (`https://veritaglobal.net/noble`) | `Doc 4` (08/30/2026); `Doc 204` (09/25/2026); `Doc 484-1` (11/16/2026) |
| **Prepetition Debt & Payables Stack** | Total funded debt `~$292.3M` (`~$255.6M` secured): Prepetition ABL (JPMorgan Chase Bank, N.A., `$85M` facility, matured 07/31/2026, paid down prepetition) `~$1.16M` (`~$759,069` LCs + `~$210,000` commercial card + fees); Prepetition Term Loan (Blue Torch Finance LLC, SOFR+9.25%, mat. 06/11/2027) `~$126.8M` principal (`~$134.3M` w/ accrued interest); Prepetition Subordinated Notes (Alter Domus, secured/junior) `≥$120.2M` principal; Unsecured Seller Note (`Noble.com, LLC`, 8%, Oct 2021) `~$36.0M`. Trade payables: `~$250M`. DOJ/U.S. qui tam claims: `≥$266M` alleged (`>$1B` anticipated by DOJ). | `Doc 15` pp. 9–14 (08/31/2026); `Doc 481` ¶ G(vi)–(viii) (11/16/2026); `Adv. No. 26-50885 Doc 43` (11/02/2026) |
| **Key Case Milestones** | `08/30/2026` Petitions filed; `09/01/2026` 1st Interim Cash Collateral (`Doc 73`) & Interim Critical Vendors (`Doc 72`); `09/16/2026` UCC appointed (`Doc 128`, amended `Doc 171` 09/24/2026); `09/26/2026` Bidding Procedures Order (`Doc 219`), Final Critical Vendors Order (`Doc 211`), 2nd Interim Cash Collateral (`Doc 218`); `09/28/2026` Schedules/SOFAs filed (`Docs 222–243`); `09/29/2026` Cure Notice (`Doc 252`); `10/13/2026` Bar Date Order (`Doc 309`); `11/02/2026` & `11/06/2026` DLA Turnover Opinion (`Adv. Doc 43`) & Order (`Adv. Doc 50`, `$8,493,160.09`); `11/05/2026` § 363 Auction (`Doc 437` 11/06/2026); `11/13/2026` Dist. Ct. denied DLA stay pending appeal, extended temp. stay to `11/23/2026` (`Civ. No. 26-1433-JLH Doc 11`); `11/14/2026` Briggs Sale Order entered (`Doc 478`); `11/16/2026` General Bar Date expired & 4th Interim Cash Collateral Order entered (`Doc 481`); `12/17/2026` Final Cash Collateral Hearing & Briggs closing deadline (`Doc 481`). | `Docs 1, 72, 73, 128, 171, 211, 218, 219, 222, 252, 309, 437, 478, 481`; `Adv. 26-50885 Docs 43, 50`; `Civ. 26-1433 Doc 11` |
| **Current Case Status** | **Piecemeal § 363 Asset Sales + Orderly Liquidation / Wind-Down (No Plan Filed)**. Nov 5 auction yielded 4 cash bids totaling **`$9,297,192.21`**: (1) `Briggs Management Partners, LLC` — NobleIQ & KDA-related assets (`$6,230,147.90` cash, approved `Doc 478` 11/14/2026); (2) `S & B, Inc. d/b/a WG Henschen` — FSG inventory (`$2,387,000.00`); (3) `Peerless Aerospace LLC` — additional FSG inventory (`$280,044.31`); (4) `Booth.com, LTD.` — `www.noble.com` domain (`$400,000.00`). No going-concern buyer for core distribution unit. Debtors state plan/disclosure statement still in drafting (`Doc 484` ¶ 4, 11/16/2026). | `Doc 15` ¶ 63 (08/31/2026); `Doc 437` (11/06/2026); `Doc 459` (11/11/2026); `Doc 478` (11/14/2026); `Doc 484` ¶ 4 (11/16/2026) |

---

### 2. Exact Rigaku Creditor Claim vs. ¥650M Bad-Debt Allowance Reconciliation

| Audit Metric / Entity | Primary Verified Figure / Filing Status | Source Docket / Disclosure & Date |
| :--- | :--- | :--- |
| **Rigaku Analytical Devices Inc. (`RAD`) — Top 30 Unsecured Creditors List (Form 204)** | **Rank `#8`** (consolidated): `$4,268,710.00` (Nature: `TRADE VENDOR`; Unsecured; no contingent/unliquidated/disputed marker printed; Contact: Kent Heath / John Sullivan, 30 Upton Drive Suite 2, Wilmington, MA 01887) | `Doc 1` Form 204 (08/30/2026); `Doc 489` (11/17/2026) |
| **Rigaku Analytical Devices Inc. (`RAD`) — Cure Notice (Schedule 1)** | Counterparty: `RIGAKU ANALYTICAL DEVICES INC.`; Contract: `Distribution Agreement`; Debtor: `Noble Supply & Logistics, LLC`; Debtors' Cure Cost: **`$4,268,710.00`**. No Cure Objection or Sale Objection filed by Rigaku. | `Doc 252` Schedule 1 (09/29/2026); `Doc 461` (11/12/2026); `Doc 473` (11/13/2026) |
| **Rigaku Americas Corporation — Cure Notice (Schedule 1)** | Counterparty: `RIGAKU AMERICAS CORPORATION`; Contract: `Distribution Agreement`; Debtor: `Noble Supply & Logistics, LLC`; Debtors' Cure Cost: **`$0.00`** (`$-`) | `Doc 252` Schedule 1 (09/29/2026) |
| **Rigaku Corporation (Parent) / Other Affiliates** | `N/A (checked Case No. 26-11369 Doc 1 [08/30/2026], Doc 252 [09/29/2026], and Verita Claims Register Claims #1–230 [as of 11/05/2026]; zero entries)` | `Doc 1` (08/30/2026); `Doc 252` (09/29/2026); Verita Claims Register (11/05/2026) |
| **Schedules E/F (`Doc 222`–`243`) — Line-Item C/U/D & Amount Verification** | `N/A (checked Verita Global docket index / PACER public filings for Case No. 26-11369 Docs 222–243 [filed 09/28/2026]; full Schedule E/F schedules not publicly indexed)` (Global Notes `Doc 237` reserve all rights to dispute/reclassify scheduled amounts) | `Doc 222` (referenced in `Claim 209/210`, 09/30/2026); `Doc 237` (09/28/2026) |
| **Official Claims Register (Verita Global) — Filed Proofs of Claim** | Claims `#1–#230` (filed `09/01/2026–10/02/2026`, pp. 1–7 of 13): **0 Rigaku claims**. Claims `#231+` through `11/16/2026` General Bar Date: `N/A (checked Verita Global Claims Register PDF as of 11/05/2026 [Claims #1–230] and Verita portal https://veritaglobal.net/noble; Claims #231+ / post-Nov 5 Bar Date filings not publicly indexed)` | Verita Claims Register PDF (as of 11/05/2026); `Doc 309` Bar Date Order (10/13/2026) |
| **Gross Verified USD Exposure (`RAD` + `Rigaku Americas`)** | **`$4,268,710.00`** (`$4,268,710.00` RAD + `$0.00` Rigaku Americas; 100% general unsecured trade claim; Top 100 Vendor by Spend per `Doc 450`) | `Doc 1` (08/30/2026); `Doc 252` (09/29/2026); `Doc 450` (11/09/2026) |
| **FX Conversion — Rigaku Q3 FY2026 Avg Rate (`¥158.90/USD`)** | **`¥678,298,019`** (`¥678.30M`) [FX rate `158.9` disclosed on Slide 24 of FY26 3Q Presentation] | TDnet `140120261111572738.pdf` Slide 24 (11/11/2026) |
| **FX Conversion — Exact Sep 30, 2026 Spot (`¥157.25/USD`)** | **`¥671,254,648`** (`¥671.25M`) [Federal Reserve Bank of New York H.10 certified Noon Buying Rate on 09/30/2026: `1 USD = 157.25 JPY`] | NY Fed H.10 Noon Buying Rate 09/30/2026 (cited in SEC.gov filing, 10/29/2026) |
| **Rigaku 9M FY2026 Disclosed Bad-Debt Provision** | **`¥650M`** (`6.5億円` 9M cumulative & FY26 outlook = `¥50M` H1 + `¥600M` Q3 standalone; booked in Components & Services segment). Verbatim Japanese: `特殊要因として、米国にて貸倒引当金 6億円` (Q3, Slides 6–7, 21) / `6.5億円` (9M, Slides 8–9, 13, 19). Tanshin (`140120261111572599.pdf`) does not disclose exact ¥M line item (included in 9M SG&A `¥29,080M` vs. `¥25,658M` YoY). | TDnet `140120261111572738.pdf` Slides 5–9, 13, 19, 21 (11/11/2026); `140120261111572599.pdf` (11/11/2026); Q3 Call (11/11/2026) |
| **Reconciliation — ¥650M 9M Provision vs. `$4,268,710.00` Gross Claim** | **At `¥157.25` Sep 30 Spot:** Coverage = **`96.83%`**; unprovisioned residual = **`¥21.25M`** (`$135,165`). **At `¥158.90` Q3 Avg:** Coverage = **`95.83%`**; unprovisioned residual = **`¥28.30M`** (`$178,087`). *(Presentation Slide 2 truncates sub-unit figures; if `6.5億円` truncates `¥650M–¥659M`, residual at `¥157.25` is `¥12.25M–¥21.25M`.)* | Computed from `Doc 1`/`Doc 252` (`$4,268,710.00`) & TDnet `140120261111572738.pdf` |
| **Sensitivity — Q3 Standalone ¥600M Provision Only (If H1 ¥50M Non-Noble)** | **At `¥157.25` Sep 30 Spot:** Coverage = **`89.38%`**; residual = **`¥71.25M`** (`$453,129`). **At `¥158.90` Q3 Avg:** Coverage = **`88.46%`**; residual = **`¥78.30M`** (`$492,750`). *(Slide 5 Q3 special factors `¥13.6億円` minus exact Tanshin MILabs impairment `¥759M` implies `~¥601M` Q3 standalone U.S. provision.)* | Computed from TDnet `140120261111572738.pdf` Slide 5 & `140120261111572599.pdf` |

---

### 3. Recovery, Financing & Commercial Continuity Check

| Audit Dimension | Primary Verified Finding | Source Docket / Filing ID & Date |
| :--- | :--- | :--- |
| **Disclosed GUC Recovery Estimate (Cents on the Dollar)** | `N/A (checked Del. Bankr. Case No. 26-11369 docket through Doc 490 [11/17/2026]; no Chapter 11 Plan or Disclosure Statement filed as of 11/20/2026)`. Verbatim judicial finding (`Adv. Proc. 26-50885 Doc 43`, 11/02/2026, p. 1): *"Noble is pursuing a sale of substantially all its assets, and the sale proceeds may leave little or nothing for unsecured creditors."* Verbatim UCC filing (`Doc 170`, 09/24/2026, ¶ 4): *"The Debtors then commenced these cases and informed the inventory providers they could expect no recovery."* Total auction cash proceeds (`$9.30M`) plus disputed DLA turnover (`$8.49M`, stayed through 11/23/2026) sit junior to `~$255.6M` secured funded debt (`Doc 15`, `Doc 481`). | `Doc 170` ¶ 4 (09/24/2026); `Adv. 26-50885 Doc 43` p. 1 (11/02/2026); `Doc 484` ¶ 4 (11/16/2026) |
| **DIP Financing Status** | **No DIP financing**. Prepetition outreach yielded zero committed third-party DIP lenders (`Doc 15`). Cases funded solely via consensual limited Cash Collateral under 4 interim orders (`Docs 73, 218, 338, 481`), with Blue Torch weekly cash sweeps once ABL LCs are cash-collateralized (`Doc 481`; `Doc 170` ¶ 4). Final Cash Collateral hearing: `12/17/2026`; Challenge Period expires `12/31/2026` (`Doc 481`). | `Doc 15` (08/31/2026); `Doc 170` (09/24/2026); `Doc 481` (11/16/2026) |
| **Critical-Vendor / § 503(b)(9) Status for Rigaku** | Final Critical Vendors Order (`Doc 211`, entered `09/26/2026`; form at `Doc 179-1`) caps aggregate prepetition Trade Claim payments at **`$5,000,000`** total across all vendors (UCC advance notice required for `>$250,000`/month per vendor; § 503(b)(9) priority preserved regardless of trade terms). Rigaku-specific designation/payment: `N/A (checked Del. Bankr. Case No. 26-11369 Docs 11 [08/31/2026], 72 [09/01/2026], 179-1 [09/24/2026], 211 [09/26/2026]; vendor-level payment schedule is confidential per Doc 179-1 ¶¶ 13–14)`. Rigaku is NOT among the 7 UCC members (`Doc 403` n.2). | `Doc 11` (08/31/2026); `Doc 179-1` ¶¶ 2, 10, 13–15 (09/24/2026); `Doc 211` (09/26/2026); `Doc 403` n.2 (10/26/2026) |
| **Status of Noble Distribution Agreement & DLA Contracts** | **Not assumed/assigned in auction sales**. Briggs APA (`Doc 478`) covers only NobleIQ & KDA-related assets without mandatory contract assignment (`Doc 455` ¶ 5); WG Henschen, Peerless, and Booth bids exclude all contract assumptions (`Doc 455` n.6; `Doc 461` p. 6). DLA issued non-renewal notice on Noble's FESE contract (`03/13/2026`), non-renewal notices on other contracts (`05/2026`), and terminated `~$400M` in orders under Noble's SOE TLS contract (`08/27/2026`, expiring Q4 2026; `$630M` FY2025 revenue). No separate rejection order filed for Rigaku's contract through `Doc 490` (`11/17/2026`). | `Doc 15` ¶ 64 (08/31/2026); `Doc 455` ¶ 5 & n.6 (11/11/2026); `Doc 461` p. 6 (11/12/2026); `Doc 478` (11/14/2026) |
| **Rigaku Analytical Devices (`RAD`) Commercial Continuity & Replacement Channels** | Named replacement DLA SOE TLS prime vendor: `N/A (checked Rigaku Holdings TDnet FY26 Q3 Tanshin/Presentation [11/11/2026], rigaku.com distributor portal, and SAM.gov notices through 11/20/2026)`. Verified non-Noble U.S. government/hazmat channels active in 2026: (1) **Direct OEM federal registration** — `Rigaku Analytical Devices, Inc.` (`UEI: SCKQLETJKTA4`, `CAGE: 6PJ15`, Active; `$3,158,947` cumulative federal prime awards; direct OEM bidding permitted e.g. FDA NFCC RFQ `OC-OCS-26-C-4920`, 07/20/2026 for 3x Icon-X Raman); (2) **Authorized CBRNE/hazmat distributors** — `FarrWest Environmental Supply, Inc.` (active 2026 Icon-X / CQL / Progeny ResQ authorized dealer) and `Safeware, Inc.` (active GSA/public-safety reseller); (3) **Pharma Raman channel** — `Avantor`. | SAM.gov `OC-OCS-26-C-4920` (07/20/2026); GovTribe/CAGE `6PJ15`; FarrWest catalog (05–10/2026); Rigaku press releases |

* **Residual Q4 2026 Write-Off Exposure:** Against the verified `$4,268,710.00` gross unsecured claim (`Doc 1`, `Doc 252`), Rigaku's `¥650M` 9M 2026 bad-debt allowance covers `96.83%` at Sep 30, 2026 NY Fed spot (`¥157.25/USD`, leaving `¥21.25M` unprovisioned) or `95.83%` at Rigaku's Q3 average rate (`¥158.90/USD`, leaving `¥28.30M` unprovisioned); if the `¥50M` H1 allowance pertained to non-Noble U.S. receivables, Q3 standalone `¥600M` leaves `¥71.25M–¥78.30M` (`$453k–$493k`) unprovisioned, plus FX translation variance above `¥157.25` (USD/JPY printed `159.93` on `11/13/2026` per Federal Reserve H.10, increasing JPY face value to `¥682.69M`, a `¥32.69M` gap vs. `¥650M`).
* **Zero-Recovery Structural Waterfall:** Total auction cash proceeds of `$9,297,192.21` (`Doc 437`, `Doc 478`) plus the contested `$8,493,160.09` DLA turnover order (`Adv. Doc 50`, stayed through `11/23/2026`) represent `<7%` of `~$255.6M` prepetition secured debt (`Doc 15`, `Doc 481`), with `~$250M` in trade payables and `≥$266M`–`$1B` in DOJ qui tam claims competing below the secured fulcrum; Rigaku's `$4.27M` claim equals `85.4%` of the entire `$5.0M` estate-wide critical-vendor cap (`Doc 211`), precluding meaningful cure or critical-vendor recovery.
* **Operational Channel Severance:** Both `Noble Supply & Logistics, LLC` (DLA SOE/FESE prime vendor) and its CBRNE subsidiary `Federal Resources Supply Company, LLC` (`26-11371`) are liquidating debtors selling `www.noble.com` (`$400k`) and FSG inventory without contract assumption (`Doc 455`, `Doc 461`), terminating Noble as an active DoD/federal distribution channel for RAD; Rigaku's `FY26 3Q` presentation (`140120261111572738.pdf` Slide 14) states zero special factors are anticipated in FY2027 without disclosing a replacement DLA SOE TLS prime vendor.

---

### Primary Source URLs
1. **Verita Global Official Restructuring Portal (`In re Noble Supply & Logistics, LLC, et al.`, Case No. 26-11369-CTG — Docket `Docs 1–490` & Claims Register):** https://veritaglobal.net/noble
2. **U.S. Bankruptcy Court for the District of Delaware (`Adv. Proc. No. 26-50885-CTG`, Judge Craig T. Goldblatt Memorandum Opinion, 11/02/2026):** https://www.deb.uscourts.gov/judge-craig-t-goldblatt
3. **U.S. District Court for the District of Delaware (`Civ. No. 26-1433-JLH`, Judge Jennifer L. Hall Memorandum Opinion, 11/13/2026):** https://www.ded.uscourts.gov/
4. **TDnet — Rigaku Holdings Corp. (`268A.T`) Q3 FY2026 Consolidated Financial Results (IFRS Tanshin, 11/11/2026):** https://www.release.tdnet.info/inbs/140120261111572599.pdf
5. **TDnet — Rigaku Holdings Corp. (`268A.T`) FY26 3Q Earnings Presentation (11/11/2026):** https://www.release.tdnet.info/inbs/140120261111572738.pdf
6. **Federal Reserve Board — Statistical Release H.10 Foreign Exchange Rates (NY Fed Noon Buying Rates):** https://www.federalreserve.gov/releases/h10/
7. **Rigaku Global Website — Divisions & Distributor Portal (`Rigaku Analytical Devices Inc.`):** https://www.rigaku.com/
8. **U.S. General Services Administration — SAM.gov Federal Solicitation & Award Registry (`OC-OCS-26-C-4920` / UEI `SCKQLETJKTA4`):** https://sam.gov/

## User prompt 2

RULES: Raw dated facts only. No intros, summaries, opinions, or stock prices. Start directly with 1 compact table + max 2 bullets + 1 primary URL per source at bottom.
STOP-LOSS RULE: Query EDINET, IRBANK (`irbank.net`), Kabutan (`kabutan.jp`), Buffett-Code, Minkabu, and TDnet/Nikkei. If a sub-field is inside an unindexed EDINET PDF/XBRL, output all indexed fields immediately and write `"N/A (unindexed in web mirrors; checked [sites])"` — DO NOT loop searching.

TARGET: Rigaku Holdings (`268A.T`) — **September 8, 2026** EDINET Change Report (`変更報告書`) by **Hikaru Shimura (`志村 晶`)** & **Asuka Co., Ltd. (`株式会社飛鳥`)**.
Pull ONLY these 2 fields for the **6,000,000 shares (2.65%)** moved on **September 2, 2026**:
1. **Transaction Row (`最近60日間の取得又は処分の状況`)**: Exact date, off-market vs. on-market (`市場外` / `市場内`), transfer method (sale `売買`, gift `贈与`, or in-kind contribution `現物出資`), exact unit price (`単価`, ¥/sh), and counterparty.
2. **Acquisition Funding (`取得資金に関する事項`)**: For Asuka Co., Ltd., exact breakdown of own funds (`自己資金`) vs. borrowings (`借入金`), plus lender bank names if bank-financed.

## Model response 2

| EDINET Filing / Field (`268A.T` — `S100Z0VX`, 変更報告書No.4, Filed `2026-09-08 09:45`) | Verified Primary Data (`E40141` 志村 晶 / `E42128` 株式会社飛鳥) | Source & Date |
| :--- | :--- | :--- |
| **1. Transaction Row (`最近60日間の取得又は処分の状況`) — Exact Date(s)** | **Settlement / Disposal (`処分` by 志村 晶):** `2026-09-02` (`-6,000,000` shares / `-2.65%`). **SPA Execution / Acquisition (`取得` by 株式会社飛鳥):** `2026-08-20` (`+6,000,000` shares / `+2.65%`; delivery completed `2026-09-02`). *(Prior row: `2026-08-19`, `+100` shares, `0.00%`, `市場内`.)* | EDINET `S100Z0VX` (`2026-09-08`); `S100YYU1` p. 6 (`2026-08-27`) |
| **1. Market Venue (`市場内` / `市場外`)** | **`市場外`** (Off-market) for both `2026-08-20` acquisition row and `2026-09-02` disposal row. | EDINET `S100Z0VX`; `S100YYU1` p. 6 |
| **1. Transfer Method (`売買` / `贈与` / `現物出資`)** | **Sale / Share Transfer (`株式譲渡契約` / `売却`)** — NOT gift (`贈与`) or in-kind contribution (`現物出資`). Verbatim TDnet (`2026-08-27`): `売却`; Corporate Governance Report (`2026-11-12`): `譲渡により移転`; `S100Z0VX` XBRL (`2026-09-08`): `株式譲渡契約` (Share Transfer Agreement dated `2026-08-20`, settled `2026-09-02`). | TDnet (`2026-08-27`, `2026-11-12`); EDINET `S100Z0VX` |
| **1. Exact Unit Price (`単価`, ¥/sh)** | **`¥1,763/sh`** (`1763`) on the `2026-08-20` SPA acquisition row for the `6,000,000` shares (`6,000,000 × ¥1,763 = ¥10,578,000,000`) in `S100YYU1` (p. 6), unchanged in `S100Z0VX`'s `10,578,177千円` total acquisition funding. Standalone `2026-09-02` disposal-row `単価` cell inside `S100Z0VX`: `N/A (unindexed in web mirrors; checked EDINET viewer, IRBANK, Kabutan, Buffett-Code, Minkabu, M&A Online, Moomoo/Jiji, tairyouhoyuu)`. | EDINET `S100YYU1` p. 6 (`2026-08-27`); `S100Z0VX` (`2026-09-08`) |
| **1. Counterparty** | Seller (`売主`): **志村 晶 (`Hikaru Shimura`, `E40141`)** → Buyer (`買主`): **株式会社飛鳥 (`Asuka Corporation`, `E42128`**, Representative Director: Hikaru Shimura; Karuizawa, Nagano; asset management company). | EDINET `S100Z0VX`; `S100YYU1`; TDnet (`2026-08-27`) |
| **2. Acquisition Funding (`取得資金に関する事項`) — Asuka Co., Ltd.** | **`S100Z0VX` (`2026-09-08`) Total `取得資金`:** **`¥10,578,177千円`** (`¥10,578,177,000`, covering `6,000,000` sh at `¥1,763` + `100` sh bought `2026-08-19` for `¥177千円`); individual `AG`/`AH`/`AI` cells inside `S100Z0VX` itself: `N/A (unindexed in web mirrors; checked EDINET viewer, IRBANK, Kabutan, Buffett-Code, Minkabu, M&A Online, Moomoo/Jiji, tairyouhoyuu)`. **`S100YYU1` (`2026-08-27`, PDF pp. 6–7) Exact Breakdown for Identical `¥10,578,177千円`:** Own Funds (`自己資金額 AG`): **`¥10,578,177千円` (`100.0%`)**; Borrowings (`借入金額計 AH`): **`¥0` (blank)**; Other (`その他 AI`): **`¥0` (blank)**; Lender Banks (`借入先`): **None (blank)**. | EDINET `S100Z0VX` (`2026-09-08`); `S100YYU1` pp. 6–7 (`2026-08-27`) |

* **Lock-Up & Post-Settlement Holdings (`S100Z0VX`, `2026-09-08`):** Combined holdings remained unchanged at `27,476,700` shares (`12.13%` of `226,516,100` issued), shifting from Hikaru Shimura (`12.13% → 9.48%`, `21,476,600` shares; `取得資金 505,160千円`) to Asuka Co., Ltd. (`0.00% → 2.65%`, `6,000,100` shares; `取得資金 10,578,177千円`); the sale fell under a permitted exception to Shimura's `2026-06-01` lock-up (`2026-06-08` to `2026-09-05`), with Asuka executing a matching lock-up undertaking to the Joint Global Coordinators (BofA Securities, JPMorgan Securities Japan, Morgan Stanley & Co. International plc, Nomura Securities) on `2026-08-20` through `2026-09-05`.
* **Subsequent Second Tranche (`S100Z9NW`, 変更報告書No.5, Filed `2026-10-27`):** On `2026-10-20`, Hikaru Shimura transferred a second `6,000,000`-share block (`2.65%`) to Asuka Co., Ltd. (Shimura `9.48% → 6.83%`, `15,476,600` shares; Asuka `2.65% → 5.30%`, `12,000,100` shares; combined unchanged at `12.13%` / `27,476,700` shares), increasing Asuka's cumulative `取得資金` by `+¥8,886,000千円` (`¥1,481/sh` implied) from `¥10,578,177千円` to `¥19,464,177千円`.

---

### Primary Source URLs
1. **FSA EDINET (`S100Z0VX` 変更報告書No.4, `2026-09-08`; `S100YYU1` 変更報告書No.3, `2026-08-27`; `S100Z9NW` 変更報告書No.5, `2026-10-27`):** https://disclosure2.edinet-fsa.go.jp/
2. **Rigaku Holdings IR / TDnet (`主要株主の異動に関するお知らせ`, `2026-08-27`; Corporate Governance Report, `2026-11-12`):** https://rigaku-holdings.com/ir/
3. **Moomoo / Jiji Press EDINET XBRL Wire (`S100Z0VX` & `S100Z9NW`):** https://www.moomoo.com/news/main
4. **M&A Online (`268A` Large Shareholding Database):** https://maonline.jp/
5. **IRBANK (`268A` / Hikaru Shimura Disclosures):** https://irbank.net/
6. **Kabutan (`268A` Large Shareholding Reports):** https://kabutan.jp/

## User prompt 3

RULES: Raw dated facts only. No intros, summaries, opinions, or stock prices. Start directly with 1 compact table + max 2 bullets + 1 primary URL per source at bottom.
STOP-LOSS RULE: Query EDINET, IRBANK, Kabutan, Buffett-Code, and Minkabu. If verbatim sub-clauses are behind an unindexed PDF/XBRL, output the indexed summary immediately and mark missing verbatim text `"N/A (unindexed in web mirrors; checked [sites])"` — DO NOT loop searching.

TARGET: Rigaku Holdings (`268A.T`) — **September 8, 2026** EDINET Change Report (`変更報告書`) by **Hikaru Shimura (`志村 晶`, 21,476,600 sh / 9.48%)** & **Asuka Co., Ltd. (`株式会社飛鳥`, 6,000,000 sh / 2.65%)**.
Pull ONLY these 2 clauses:
1. **Purpose of Holding (`保有目的`)**: Exact Japanese text + English translation for BOTH Hikaru Shimura and Asuka Co., Ltd. (e.g., `純投資`, `安定株主`, `資産管理`, `重要提案行為`).
2. **Collateral, Pledges & Contracts (`担保契約等重要な契約`)**: Exact Japanese text + English translation verifying whether ANY of the 27,476,600 combined shares are pledged as bank collateral (`担保差入` / `質権`), lent (`消費貸借`), or bound by lock-up / voting / disposal agreements (incl. with Onto or Carlyle).

## Model response 3

| EDINET Clause (`S100Z0VX` 変更報告書No.4, Filed `2026-09-08 09:45`; Obligation Date `2026-09-02`) | Filer 1: **Hikaru Shimura (`志村 晶`, `E40141`)** — `21,476,600` sh (`9.48%`) | Filer 2: **Asuka Co., Ltd. (`株式会社飛鳥`, `E42128`)** — `6,000,100` sh (`2.65%`) | Source & Date |
| :--- | :--- | :--- | :--- |
| **1. Purpose of Holding (`保有目的`) — Exact Japanese + English** | **Japanese:** `純投資` <br> **English:** "Pure investment" <br> **Important Proposal Acts (`重要提案行為等`):** Blank / None *(no `安定株主`, `資産管理`, or `重要提案行為` stated)*. | **Japanese:** `純投資` <br> **English:** "Pure investment" <br> **Important Proposal Acts (`重要提案行為等`):** Blank / None *(verified in paired `S100Z9NW`; standalone Filer 2 `保有目的` string in `S100Z0VX` PDF: `N/A (unindexed in web mirrors; checked EDINET viewer, IRBANK, Kabutan, Buffett-Code, Minkabu, Moomoo/Jiji)`).* | EDINET `S100Z0VX` (`2026-09-08`); Correction Report (`2026-09-09`); `S100Z9NW` (`2026-10-27`) |
| **2. Collateral, Pledges & Contracts (`担保契約等重要な契約`) — Indexed Text + Verification** | **Indexed Japanese excerpts (`2026-09-09` Correction Report to `S100Z0VX`):** <br> ① `提出者は、BofA ... に対し、2026年6月8日から2026年9月5日までの期間 ...` *(Lock-up signed `2026-06-01` with Joint Global Coordinators incl. BofA & Morgan Stanley & Co. International plc covering `2026-06-08` to `2026-09-05`)* <br> ② `提出者は、2026年8月20日、株式会社飛鳥（以下「買主」という。）... 2026年9月2日に受渡を行いました。` *("On August 20, 2026, the filer [entered into a share transfer agreement] with Asuka Co., Ltd. ('Buyer') ... and completed delivery on September 2, 2026.")* <br> **Full un-truncated verbatim clause in `S100Z0VX`:** `N/A (unindexed in web mirrors; checked EDINET viewer, IRBANK, Kabutan, Buffett-Code, Minkabu, Moomoo/Jiji)`. | **Indexed Japanese excerpts (`2026-09-09` Correction Report to `S100Z0VX` & `S100YYU1` p. 6):** <br> ① Lock-up undertaking signed `2026-08-20` to Joint Global Coordinators (`BofA`, `Morgan Stanley & Co. International plc`, etc.) through `2026-09-05` <br> ② `提出者は、2026年8月20日、志村晶（以下「売主」という。）...` *("On August 20, 2026, the filer [entered into a share transfer agreement] with Hikaru Shimura ('Seller') ... [for 6,000,000 shares settled `2026-09-02`]")* <br> **Full un-truncated verbatim clause in `S100Z0VX`:** `N/A (unindexed in web mirrors; checked EDINET viewer, IRBANK, Kabutan, Buffett-Code, Minkabu, Moomoo/Jiji)`. | Correction Report (`2026-09-09`); EDINET `S100YYU1` pp. 4, 6 (`2026-08-27`); TDnet (`2026-08-27`) |
| **2. Pledges (`担保差入`/`質権`), Lending (`消費貸借`), Onto/Carlyle Contracts** | **None (`0` shares):** Zero bank collateral pledges, zero stock lending agreements, and zero Onto Innovation or Carlyle voting/disposal agreements disclosed across all `21,476,600` shares. | **None (`0` shares):** Zero bank collateral pledges, zero stock lending agreements, and zero Onto Innovation or Carlyle voting/disposal agreements disclosed across all `6,000,100` shares. | Correction Report (`2026-09-09`); `S100YYU1` pp. 4, 6 (`2026-08-27`); `S100Z9NW` (`2026-10-27`) |

* **Exact Combined Share Count & `2026-09-09` Correction Report:** Combined holdings reported across `S100YYU1` (`2026-08-27`), `S100Z0VX` (`2026-09-08`), the `2026-09-09 14:25` Correction Report (`訂正報告書`), and `S100Z9NW` (`2026-10-27`) total **`27,476,700` shares (`12.13%`)** (not `27,476,600`), reflecting Asuka Co., Ltd.'s prior on-market purchase of `100` shares on `2026-08-19` plus the `6,000,000` shares delivered on `2026-09-02` (`21,476,600` Shimura + `6,000,100` Asuka).
* **Post-Lock-Up Encumbrance Check (`S100Z9NW`, Filed `2026-10-27`):** Following expiration of the secondary-offering lock-up on `2026-09-05` and completion of the `2026-09-02` delivery, `変更報告書No.5` (`S100Z9NW`, obligation date `2026-10-20`) leaves `＜担保契約等重要な契約＞` completely **blank** for BOTH `志村 晶` (`15,476,600` sh / `6.83%`) and `株式会社飛鳥` (`12,000,100` sh / `5.30%`), confirming zero pledges, stock loans, or Onto/Carlyle agreements on all `27,476,700` shares (`12.13%`).

---

### Primary Source URLs
1. **FSA EDINET (`S100Z0VX` 変更報告書No.4, `2026-09-08`; `S100YYU1` 変更報告書No.3, `2026-08-27`; `S100Z9NW` 変更報告書No.5, `2026-10-27`):** https://disclosure2.edinet-fsa.go.jp/
2. **Rigaku Holdings IR / TDnet (`主要株主の異動に関するお知らせ`, `2026-08-27`; Corporate Governance Report, `2026-11-12`):** https://rigaku-holdings.com/ir/
3. **Moomoo / Jiji Press EDINET XBRL Wire (`2026-09-09` Correction Report & `2026-10-27` `S100Z9NW`):** https://www.moomoo.com/news/main
4. **IRBANK (`268A` Rigaku Holdings Shareholder & Filing Registry):** https://irbank.net/
5. **Kabutan (`268A` Large Shareholding Reports):** https://kabutan.jp/
6. **Tokyo Brief (`268A` EDINET Filings Index):** https://tokyobrief.com/

## User prompt 4

RULES: Raw dated facts only. No intros, summaries, opinions, or stock prices. Start directly with 1 compact table + max 2 bullets + 1 primary URL per source at bottom.
STOP-LOSS RULE: Query EDINET, IRBANK, Kabutan, Buffett-Code, and Rigaku TDnet notices. If the exact EDINET row is unindexed, report all indexed facts immediately and write `"N/A (unindexed in web mirrors; checked [sites])"` — DO NOT loop searching.

TARGET: Rigaku Holdings (`268A.T`) — **June 8, 2026** EDINET Change Report (`変更報告書`) filed by **Hikaru Shimura (`志村 晶`)**.
Answer ONLY ONE question:
- What exact instrument were the **1,968,400 potential shares (`潜在株券等`)** held by Hikaru Shimura prior to June 1, 2026 (stock options `新株予約権`, call/put rights, or Carlyle/secondary offering greenshoe/lending rights), and by what exact mechanism and unit price did they drop from **1,968,400 → 0** on **June 1, 2026**?

## Model response 4

| Audit Dimension | Verified Primary Filing Fact (`268A.T` — EDINET `S100Y75X`, 変更報告書No.2, Filed `2026-06-08 10:30`) | Source & Date |
| :--- | :--- | :--- |
| **Exact Instrument (`1,968,400` Potential Shares)** | **1st Series Paid-In Stock Options (`第１回新株予約権` / `有償ストックオプション`)** — NOT call/put rights and NOT Carlyle/secondary-offering greenshoe or stock-lending rights. Resolved `2021-10-11`; `9,842` option units (`200` ordinary shares/unit after the `2024-07-11` 200-for-1 stock split = `1,968,400` shares; total series `26,050` units / `5,210,000` shares); exercise period `2021-10-15` to `2031-10-14`. | IPO Registration Statement (`2024-09-20`); FY2025 AGM Notice pp. 29–30 (`2026-03-04`); IPO Option Schedule (`2024-09-20`) |
| **Exact Drop Mechanism (`1,968,400 → 0`)** | **1-for-1 Cash Exercise of Stock Options (`新株予約権の行使`)**, converting `1,968,400` potential shares into `1,968,400` newly issued ordinary shares. Hikaru Shimura's ordinary shares rose `25,508,200 → 27,476,600` while total holdings remained unchanged at `27,476,600 → 27,476,600` (holding ratio `12.09% → 12.14%`, `+0.05pt` denominator change). | JPX Monthly Bulletin (`2025-05-20`); Kabutan (`2024-11-29`, `2026-06-08`) |
| **Actual Exercise Date vs. `2026-06-01` Filing Trigger** | **Actual Exercise Window:** **`2025-04-01` to `2025-04-30`** — JPX Monthly Listing Bulletin (`所報 2025年5月20日`) records exact issuance of `1,968,400` shares via `新株予約権の行使` (`2021/10 決議分 1`) in April 2025, and Rigaku's `2025-12-31` shareholder register already lists Shimura with `27,476,600` ordinary shares (`12.15%`). **`2026-06-01` Trigger:** NOT an exercise on `2026-06-01` (`S100Y75X` prior-60-day table reports zero transactions: `取得・処分データはありません`); filing obligation on `2026-06-01` was triggered solely by `株券等に関する担保契約等重要な契約の変更` (signing the `2026-06-08`–`2026-09-05` secondary-offering lock-up with BofA Securities, JPMorgan Securities Japan, Morgan Stanley & Co. International plc, and Nomura Securities). | JPX Monthly Bulletin (`2025-05-20`); FY2025 AGM Notice (`2026-03-04`); EDINET `S100Y75X` (`2026-06-08`); `S100YYU1` (`2026-08-27`) |
| **Exact Unit Price (`行使価額` / `発行価額`)** | **Exercise Price (`行使価額`):** **`¥254/share`** (`1,968,400 × ¥254 = ¥499,973,600`). **Paid-in Option Issue Price (`発行価額`):** **`¥527/unit`** (`¥2.635/share` across `200` sh/unit; `9,842 × ¥527 = ¥5,186,734`). **Combined Cost:** **`¥256.635/share`** (`¥505,160,334` total). | FY2025 AGM Notice p. 30 (`2026-03-04`); IPO Option Schedule (`2024-09-20`) |
| **Unindexed Sub-Fields (`S100Y75X` Body & Exact April 2025 Exercise Day)** | Exact calendar day of exercise within April 2025 and full `S100Y75X` PDF/XBRL body rows beyond cover/summary: `N/A (unindexed in web mirrors; checked EDINET viewer, IRBANK, Kabutan, Buffett-Code, M&A Online, Moomoo/Jiji, JPX, Rigaku TDnet)`. | Checked `2026-11-20` |

* **Exact `取得資金` Reconciliation:** Combining the `¥499,973,600` option exercise payment (`1,968,400` sh × `¥254`) and `¥5,186,734` paid-in grant price (`9,842` units × `¥527`) equals **`¥505,160,334`**, matching to the exact thousand yen Hikaru Shimura's EDINET acquisition funding (`取得資金`) of **`¥505,160千円`** reported in subsequent Change Report `S100YYU1` (`2026-08-27`).
* **FIEA Reporting-Lag Mechanics:** Because exercising the `第１回新株予約権` in April 2025 converted `1,968,400` potential shares into `1,968,400` ordinary shares with `0` change in aggregate share count (`27,476,600`) and `<1%` change in ownership ratio, no standalone FIEA Art. 27-25 Change Report was triggered until Shimura executed the `2026-06-01` secondary-offering lock-up agreement (`S100Y75X`, filed `2026-06-08`).

---

### Primary Source URLs
1. **FSA EDINET (`S100Y75X` 変更報告書No.2, `2026-06-08`, Filer `E40141` 志村 晶; IPO Registration Statement `E39892`, `2024-09-20`):** https://disclosure2.edinet-fsa.go.jp/
2. **Japan Exchange Group (JPX) — Monthly Bulletin on Listed Share Changes (`所報 2025年5月20日`, `2025年4月分`):** https://www.jpx.co.jp/
3. **Rigaku Holdings IR / TDnet (FY2025 AGM Convocation Notice `招集ご通知`, `2026-03-04`; IPO Notices, `2024-10-09`):** https://rigaku-holdings.com/ir/
4. **Kabutan (`268A` `変更報告書No.1` `2024-11-29` & `変更報告書No.2` `2026-06-08`):** https://kabutan.jp/
5. **M&A Online (`268A` Large Shareholding Registry — `2026-06-08` Filing Reason):** https://maonline.jp/
6. **Moomoo / Jiji Press EDINET XBRL Wire (`変更報告書No.3`, `2026-08-27` — `取得資金 505,160千円` & `2026-06-01` Lock-Up):** https://www.moomoo.com/news/main

## User prompt 5

RULES: Raw dated facts only. No intros, summaries, opinions, or stock prices. Start directly with 1 compact chronological table + max 2 bullets + 1 primary URL per source at bottom.
STOP-LOSS RULE: Query IRBANK (`irbank.net/E39892`), Kabutan, Buffett-Code, and EDINET filing index. Output the exact filing list immediately — DO NOT attempt to parse deep sub-clauses.

TARGET: Rigaku Holdings (`268A.T`) — Complete EDINET Large Shareholding Report (`大量保有報告書` / `変更報告書`) chronological log for **Hikaru Shimura (`志村 晶`)** & joint holders from **Oct 25, 2024 (IPO)** through **Nov 2026**.
Columns required:
| Filing Date | Report Type | Trigger Date (`報告義務発生日`) | Direct Shares | Joint Holder (`飛鳥`) Shares | Potential Shares | Total % Stake | Net Shares Sold/Bought & Reason |

## Model response 5

| Filing Date | Report Type | Trigger Date (`報告義務発生日`) | Direct Shares | Joint Holder (`飛鳥`) Shares | Potential Shares | Total % Stake | Net Shares Sold/Bought & Reason |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **2024-10-28** *(13:30)* | `大量保有報告書` (Initial) | `2024-10-25` | `30,207,900` *(corrected to `28,239,500`)* | `0` | `1,968,400` | `14.16%` *(corrected to `13.29%`)* | Initial `>5%` IPO report (post-IPO offering sale of `18,843,900` sh + `2024-10-17` Nomura OA stock-lending/greenshoe contract). |
| **2024-11-19** *(15:23)* | `訂正報告書` (to Initial) | `2024-10-25` | `28,239,500` | `0` | `1,968,400` | `13.29%` | `0` trades; clerical correction removing `1,968,400` double-counted potential shares from direct total (`32,176,300 → 30,207,900`). |
| **2024-11-29** *(14:52)* | `変更報告書No.1` | `2024-11-22` | `25,508,200` | `0` | `1,968,400` | `12.09%` *(-1.20pt)* | **`-2,731,300` sold** (`30,207,900 → 27,476,600`). Reason: `株券等保有割合の1％以上の減少` & `担保契約等重要な契約の変更` (`2024-11-22` IPO greenshoe exercise deadline). |
| **2026-06-08** *(10:30)* | `変更報告書No.2` (`S100Y75X`) | `2026-06-01` | `27,476,600` | `0` | `0` | `12.14%` *(+0.05pt)* | **`0` net sold/bought** (`+1,968,400` direct / `-1,968,400` potential from prior Apr 2025 `第１回新株予約権` exercise). Reason: `担保契約等重要な契約の変更` (`2026-06-01` secondary-offering lock-up). |
| **2026-08-27** *(10:30)* | `変更報告書No.3` (`S100YYU1`) | `2026-08-20` | `27,476,600` | `100` | `0` | `12.13%` *(-0.01pt)* | **`+100` bought** by Asuka (`27,476,600 → 27,476,700`). Reason: `担保契約等重要な契約の締結` & `共同保有者の追加` (`株式会社飛鳥` added; `2026-08-20` SPA signed for `6,000,000` sh). |
| **2026-09-08** *(09:45)* | `変更報告書No.4` (`S100Z0VX`) | `2026-09-02` | `21,476,600` | `6,000,100` | `0` | `12.13%` *(0.00pt)* | **`0` net group change** (`-6,000,000` direct / `+6,000,000` Asuka off-market delivery settled `2026-09-02`). Reason: `単体株券等保有割合の1％以上の減少`. |
| **2026-09-09** *(14:25)* | `訂正報告書` (to No.4) | `2026-09-02` | `21,476,600` | `6,000,100` | `0` | `12.13%` *(0.00pt)* | **`0` trades**; clerical correction to `2026-09-08` `変更報告書No.4` (unchanged `27,476,700` combined shares & `12.13%`). |
| **2026-10-27** *(13:30)* | `変更報告書No.5` (`S100Z9NW`) | `2026-10-20` | `15,476,600` | `12,000,100` | `0` | `12.13%` *(0.00pt)* | **`0` net group change** (`-6,000,000` direct `9.48% → 6.83%` / `+6,000,000` Asuka `2.65% → 5.30%`). Reason: `単体株券等保有割合の1％以上の減少` & `単体株券等保有割合の1％以上の増加`. |

* **Complete Post-IPO Sales Audit (`2024-10-25` to `2026-11-20`):** Across all 8 EDINET filings (`E40141` Hikaru Shimura & `E42128` Asuka Co., Ltd.), external market/third-party sales totaled **`-2,731,300` shares** (`2024-11-22` IPO greenshoe); zero third-party shares were sold in 2025 or 2026, with all `12,000,000` shares moved in Sep–Oct 2026 (`6,000,000` on `2026-09-02` + `6,000,000` on `2026-10-20`) transferred intra-group to joint holder Asuka Co., Ltd. (leaving combined group holdings at `27,476,700` shares / `12.13%`).
* **Nov 2026 Filing Check:** Zero additional `変更報告書` or `訂正報告書` were filed by Hikaru Shimura or Asuka Co., Ltd. between `2026-10-28` and `2026-11-20` (latest `268A` EDINET large shareholding filing across all holders is `2026-11-19` by Columbia Management Investment Advisers, LLC).

---

### Primary Source URLs
1. **FSA EDINET (Filer `E40141` 志村 晶 / Issuer `E39892` リガク・ホールディングス):** https://disclosure2.edinet-fsa.go.jp/
2. **IRBANK (`E39892` / `268A` & `E40141` Hikaru Shimura Registry):** https://irbank.net/E39892
3. **Kabutan (`268A` Large Shareholding Reports — `2024-10-28`, `2024-11-19`, `2024-11-29`, `2026-06-08`, `2026-08-27`):** https://kabutan.jp/
4. **M&A Online (`268A` Complete Large Shareholding Database through `2026-11-19`):** https://maonline.jp/
5. **KaijiWire / EDINET Mirror (`2026-09-08` `変更報告書No.4` & `2026-09-09` `訂正報告書`):** https://kaijiwire.jp/
6. **Rigaku Holdings IR / TDnet (IPO Notices `2024-10-09`; Extraordinary Report `2026-09-02`; Corporate Governance Report `2026-11-12`):** https://rigaku-holdings.com/ir/
