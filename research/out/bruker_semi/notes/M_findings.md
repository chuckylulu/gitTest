# M findings: market share and competitive position, semiconductor X-ray metrology and automated AFM (second attempt)

Evidence rows: `research/out/bruker_semi/parts/M.csv` (M001-M027). quote_check: 24 FOUND, 0 NOT FOUND. The 3 [I] rows have no quotes.
Calculations: `research/out/bruker_semi/calc/M_calc.py`. CSV builder: `calc/M_build_csv.py`.
Fiscal years: Bruker, Rigaku and Park Systems all end Dec 31. Nova's FY ends Dec 31, Onto's ends on the Saturday nearest Dec 31 (FY2025 = to 2026-01-03), and KLA's ends in June.
Technical note: pdftotext could not extract the Japanese EDINET PDF (missing Adobe-Japan1 language pack). `_text/2024-09-20_rigaku-edinet_S100UEKD.txt` and `_text/2024-09-19_jpx_rigaku-new-listing-outline.txt` were therefore re-extracted with pdfminer, which keeps form-feed page breaks. The manifest rows were left unchanged.

## 1. X-ray metrology: third-party figures (all relayed by Rigaku; the vendor is never named)

| Year | Rigaku share | Market size | Yole edition | Where | Tag |
|---|---|---|---|---|---|
| 2022 | 26.9% | n/a | WFE Market Monitor Q2 2024 | IPO filing 有価証券届出書, 2024-09-20, p34 (M001) | [C] |
| 2023 | 29.5% | $481m (front-end X-ray metrology); $663m 2026F, 11.3% CAGR | Q2 2024 | IPO filing p34 (M001, M002) | [C] |
| 2023 | 30%; "Company A" 24%; others 46% | n/a | Q4 2024 | MTP Feb 2025 Fig.13 (R011) | [C] |
| 2024 | 38% | ~$498m | Q4 2025 | yuho FY2025 (R012, R013) | [C] |

- **New in this round:** the Rigaku IPO filing (EDINET S100UEKD, saved). It adds the 2022 share and the Q2-2024 market size. Note 6 (p35) shows that Yole computes the shares from **revenue by vendor**, so Yole does rank vendors, but the filing names none (M003).
- **Implied Rigaku revenue [I, Low] (M006):** ~$142m (2023) and ~$189m (2024).
- **"Company A" [I, Low] (M006, M007):** 24% × $481m ≈ $115m in 2023. This mixes editions.
- **Who "Company A" is: unresolved (M007).** Nova sells X-ray metrology (VeraFlex XPS + XRF, M009), so Bruker is not the only candidate. Do not assume Company A = Bruker.
- **Lock-in risk (M005) [C]:** Rigaku's IPO risk factor says customers who already run competitors' tools are hard to win. This cuts both ways for incumbents.
- **Competitor 10-Ks and annual reports name neither Bruker nor Rigaku, in full text (M008, M010, M011):**
  - Nova 20-F FY2025: names Onto and KLA.
  - Onto 10-K FY2025: names KLA, Nova and Camtek.
  - KLA FY25 ARS: names Applied, ASML, Hitachi High-Tech, Onto and Lasertec.

## 2. AFM: third-party figures (total AFM market; none splits automated or semiconductor AFM)

| Year | Park | Bruker | Others | Research firm | Relayed by | Tag |
|---|---|---|---|---|---|---|
| 2023 | 20.61% (#1) | not named | competitors' CAGR ~8% / ~10% (unnamed) | QY Research 2024 | Park release (M022) | [C] |
| 2024 | 21.7% | 15.8% | Oxford 14.3%, others 48.2% | MarketsandMarkets | KIRS report 2026-04-13, p8 chart (M013, M014); Dealsite, citing Park material (M015) | [S] |
| 2024 | "highest global revenue share"; market $513.6m | — | — | MarketsandMarkets | Park PR 2025-08-30 (M019) | [C] |
| 2025 | 23.8%, 340 units (#1) | not named | industrial grade = 14.54% of units, 43.41% of revenue (~$221m of $508.69m) | QY Research | Park release reprinted on I-Connect007 2026-10-08 (M020, M021) | [C] |

Qualitative claims:
- **Park, on overtaking Bruker:** Park's CEO says Park's revenue passed Bruker's in 2022, with Bruker now #2 and Oxford #3. Source: company-hosted interview [C] (M023), repeated at the May 2026 IR [S] (M024).
- **KIRS on industrial AFM:** Bruker is #2 in industrial AFM and Park's most direct competitor [S] (M016), no source given. Park and Bruker are the core industrial-AFM suppliers [S] (M017).
- **Park's own filing:** the Q3 2025 DART report calls No.1 in industrial automated AFM a **goal** [C] (M025). Industrial AFM is ~74% of Park's 9M 2025 revenue [F] (M026).
- **Conflict [I] (M027):** Bruker's brochure says "#1 Inline AFM" (P003, no source). KIRS ranks Bruker #2 in industrial AFM (no source). No third-party source gives vendor shares for automated or semiconductor AFM.

## 3. Gaps

**Yole public X-ray metrology vendor shares (named vendors)**
- NOT RETRIEVED (tried: yolegroup.com press release "15% in 2025 metrology & inspection" and the M&I 2026 report page, both HTTP 403 to the script. Not worked around. Web searches for Yole + Rigaku/Bruker/X-ray returned no secondary article with named shares.)
- Firecrawl: "Insufficient credits" on the first call; stopped using it.
- SECOND ATTEMPT RESULT: added nothing for named vendors. It did add the Q2-2024-edition figures via the Rigaku IPO filing (M001-M003).

**Identity of "Company A" (24%, 2023)**
- NOT DISCLOSED (read: Rigaku 有価証券届出書 2024-09-20, 第二部 事業の内容 / 経営方針 / 事業等のリスク, text search for 競合/他社/A社/Bruker/KLA/Nova; yuho FY2025; MTP Feb 2025 p10-11).
- SECOND ATTEMPT RESULT: added nothing. Nova was added as a plausible candidate besides Bruker [I] (M007).

**Rigaku Integrated Report 2025**
- NOT RETRIEVED (tried: web search for a PDF link. Only the businesswire announcement and the JS-rendered rigaku-holdings.com/english/ir/reports/ index were found).
- SECOND ATTEMPT RESULT: added nothing.

**TechInsights / VLSI process-control or metrology vendor ranking**
- NOT DISCLOSED in the public summary (read: TechInsights blog "Top IC Manufacturing Equipment Suppliers in 2025", 2026-07-17; it names only the top 5, M012).
- The detailed database is paid: NOT RETRIEVED. Supplier-award searches found no Bruker, Rigaku or Park winner.
- SECOND ATTEMPT RESULT: added nothing on Bruker or Rigaku.

**Gartner figures naming Bruker or Rigaku**
- NOT DISCLOSED (read: Nova 20-F FY2025 pp53 and 63, which cite Gartner only for WFE and process-control growth; Onto 10-K FY2025; KLA FY25 ARS).
- SECOND ATTEMPT RESULT: added nothing.

**SEMI reports with vendor shares**
- NOT RETRIEVED (not located in searches).
- SECOND ATTEMPT RESULT: added nothing.

**Competitor filings naming Bruker or Rigaku in X-ray or AFM**
- NOT DISCLOSED (read: Nova 20-F FY2025 Item 3 risk factors p20 and Item 4 Competition p58; Onto 10-K FY2025 Item 1 Competition p15; KLA FY25 ARS Item 1 Competition p20; full-text searches).
- SECOND ATTEMPT RESULT: added something. These are documented negative results with exact competitor lists (M008, M010, M011).

**Park Systems IR deck (May 2026) and 2025 annual business report**
- NOT RETRIEVED (tried these parksystems.com/content/dam/parksystems/investor/pdf/ guesses, all HTTP 404: "2025 Annual Report", "2025.4Q Annual Report", "2025 Business Report", "2026.1H Semi-Annual Report", "2026.1Q Quarterly Report". KIND/DART search forms not used. Quartr pages are AI summaries and were not used.)
- I used the hosted Q3 2025 and H1 2025 DART reports instead (Q3 cited).
- SECOND ATTEMPT RESULT: added something (M015 relays Park's own 2024 share material; M025, M026).

**Automated/industrial AFM vendor shares**
- NOT DISCLOSED (read: KIRS report pp3, 8, 17; Park PRs 2024 and 2025; I-Connect007 reprint; Park Q3 2025 report).
- SECOND ATTEMPT RESULT: added something. Industrial-grade share of the AFM market is 43.41% of revenue (M021), and there are qualitative rankings (M016, M017). There is still no vendor split.

**MarketsandMarkets and QY Research originals**
- NOT RETRIEVED (marketsandmarkets.com HTTP 403; QY report is paid).
- SECOND ATTEMPT RESULT: added nothing beyond the relays.

Saved but not cited:
- Rigaku IPO amendments (S100UID5 2024-10-09, S100UJPM 2024-10-17): pricing only.
- S100UL46 (2024-11-01).
- JPX new-listing outline (2024-09-19): no competitor data.
- Park H1 2025 report: same text as Q3.
- Park FX40 IR PR (prnewswire 2026-05-29): no share data.

## 4. Premise checks
- **"Rigaku IPO statement Sept–Oct 2024":** confirmed. The original was filed 2024-09-20, amendments 2024-10-09 and 2024-10-17, and listing was 2024-10-25.
- **"Company A at 24% in 2023":** confirmed only as an unnamed chart label (R011). The IPO filing gives Rigaku 29.5% for 2023 from an earlier Yole edition.
- **"Park Systems ... share vs Bruker":** the only Bruker figure (15.8%, 2024) covers the whole AFM market (research + industrial), not automated AFM.
- **Quartr summary:** its "48.2% Park share" is wrong. 48.2% is "others" in the chart (M014).
