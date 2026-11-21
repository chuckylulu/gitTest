# Review packet — Nova Ltd. (NVMI), research date 21 Nov 2026

For a reviewer with web search and a URL reader. Fiscal year = calendar year. "p." = physical PDF page; the printed page is in brackets where different.

## 15 most important claims

| # | Tag | Claim and value | Period | Public URL | Page |
|---|---|---|---|---|---|
| 1 | [F] | Revenue $287,841k (+28% YoY); non-GAAP operating income $102,186k | FQ3 FY2026 (Jul–Sep 2026) | https://www.novami.com/wp-content/uploads/2026/11/nova-q3-2026-financial-results-20261105.pdf | p.6 (income statement); p.8 (reconciliation) |
| 2 | [F] | Outlook: revenue $305–315M; non-GAAP EPS $3.03–3.18 | FQ4 FY2026 (Oct–Dec 2026) | same as #1 | p.2 |
| 3 | [F] | Revenue by customer location: China 33% (2025), 39% (2024), 36% (2023) | FY2023–FY2025 | https://www.novami.com/wp-content/uploads/2026/02/a2634307.pdf (20-F FY2025) | p.168 [F-40], Note 16B |
| 4 | [F] | Customer A 23%, Customer B 10% of 2025 revenue; top five 51% | FY2025 | same 20-F | p.169 [F-41]; p.57 [48] |
| 5 | [F] | Entity-List Chinese customers buy Nova tools; the U.S. subsidiary needs a BIS licence to ship tools, parts or service to them | as of Feb 2026 | same 20-F | p.12 [3] |
| 6 | [F] | XPS and SIMS lines are made in Fremont, CA; optical CD and Raman in Israel; Nova's products are "not currently subject to control under Israeli law" | as of Feb 2026 | same 20-F | p.25 [16]; p.14 [5] |
| 7 | [F] | BIS extended the Affiliates Rule suspension through 10 Jan 2027 (doc 2026-22793, 91 FR 70789) | Nov 2026 | https://www.federalregister.gov/documents/2026/11/09/2026-22793/extension-of-the-suspension-of-expansion-of-end-user-controls-for-affiliates-of-certain-listed | abstract |
| 8 | [F] | $750M 0% convertible notes due 15 Sep 2030; conversion ~$320.16/share (3.1234 shares per $1,000); the only debt | issued Sep 2025 | same 20-F | p.156 [F-28] |
| 9 | [F] | Capped calls cost $51.8M; cap $415.03/share (75% over $237.16) | Sep 2025 | same 20-F | p.158 [F-30] |
| 10 | [F] | 2024 product revenue: logic 62%, memory 23%, advanced packaging 15% (chart labels); "Advanced packaging includes hybrid bonding and HBM processes" | FY2024 | https://www.novami.com/wp-content/uploads/2025/03/nova-investor-day-2025-final-presentation.pdf | p.10; p.7 footnote |
| 11 | [S] | Advanced packaging "nearly one-quarter" of product revenue (CFO/CEO on call, third-party transcript) | FQ2 FY2026 | https://stockanalysis.com/stocks/nvmi/transcripts/669145-q2-2026/ | prepared remarks |
| 12 | [F] | Rigaku–Onto capital and business alliance: agreement of 21 Apr 2026 for Onto to buy 27.0% of Rigaku; joint CD-SAXS + OCD work since May 2025 | Apr 2026 | https://ssl4.eir-parts.net/doc/268A/tdnet/2792714/00.pdf | p.2 |
| 13 | [F] | GlobalFoundries (with Nova) reports VeraFlex XPS as process of record for SiGeB epi composition in a GF high-volume fab | 2026 paper | https://www.novami.com/wp-content/uploads/2026/10/published-paper-download-ai-metrology.pdf | p.3 |
| 14 | [F] | IRDS 2024: CD-SAXS has the throughput for HAR contact holes, with in-line tools recently introduced; for logic, sources need at least 100x more brightness | 2024 roadmap | https://irds.ieee.org/images/files/pdf/2024/2024IRDS_MET.pdf | p.20–21 |
| 15 | [F] | Samsung + Nova: 3D NAND bottom CD reached R² 0.89 only with spectral interferometry + ML; the OCD target polishes 1.5–2x slower than the array | 2024 (Proc. SPIE 12955) | https://www.novami.com/wp-content/uploads/2024/05/unique-spectral-interferometry-solutions-for-complex-high-aspect.pdf | p.6; p.5 |

## Five inferences the conclusions lean on most

1. **LTM revenue, FCF and SBC/FCF.** LTM revenue is $1,000.7M (+17.4%), LTM FCF $254.5M and SBC/FCF 11.0%.
   - Inputs: revenue, operating cash flow, PP&E purchases and SBC from the FQ4 FY2025, FQ1, FQ2 and FQ3 FY2026 releases (novami.com quarterly PDFs), plus the prior-year columns.
   - Method: sums in `calc/metrics.py`. Confidence High.
2. **Guidance record.** No miss in 8 quarters: revenue 3 beats / 5 in-line; non-GAAP EPS 6 / 2.
   - Inputs: the "Outlook" bullets of each release vs the next release's actuals (FQ3 FY2024–FQ3 FY2026 PDFs).
   - Confidence High.
3. **Net cash** ≈ $1.05B.
   - Inputs: 30 Sep 2026 balance sheet (#1 PDF): cash 188,156; short-term deposits 395,865; securities 493,297 + 711,846; long-term/restricted deposits 11,448; less the $750,000k note principal.
   - Confidence High. The total includes $11.4M of restricted deposits.
4. **China revenue in dollars** rose to $290.6M in FY2025 (+10.8%) while its share fell from 39% to 33%.
   - Inputs: claim #3 shares × 20-F revenue ($672.4M FY2024; $880.6M FY2025).
   - Confidence High; ±0.5 pt rounding.
5. **Ledger 1 (optical CD with ML vs X-ray).** "Optical CD with ML keeps pace and X-ray stays a reference tool" holds for GAA logic but not for HAR memory.
   - Inputs: #14 and #15; SPIE 13981 abstracts (CD-SAXS labels for ML-OCD, R² > 0.95; affiliations not shown); Onto's claim of two key customers for CD-SAXS (Onto release, 20 Apr 2026, s24.q4cdn.com); Rigaku's T-SAXS adoption in memory mass production (Rigaku 3Q FY2026 materials).
   - Confidence Medium: the memory-side evidence is partly abstracts and vendor claims.

## Three questions I could not settle

1. **XPS vs XRF socket.** Who holds the production socket for HKMG and dipole ultra-thin-film metrology: Nova's XPS + LE-XRF or Rigaku's XRF/XRD tools? Both claim leadership, and Yole (via Rigaku) hides competitor names. This decides how exposed VeraFlex is when XPS rivals arrive in 2H 2027.
2. **China revenue under licence.** How much of Nova's China revenue depends on U.S.-made XPS/SIMS shipped under licence to Entity-List customers, or to their 50%-owned affiliates? This decides the impact if the Affiliates Rule resumes on 10 Jan 2027. Nova discloses neither split.
3. **Onto–Rigaku in memory.** Will the Onto–Rigaku CD-SAXS + OCD hybrid displace Nova OCD in HAR memory? The two "key customers" are unnamed, the hybrid engine is a 1Q 2027 target, and Nova's memory revenue hit a record in FQ3 FY2026.
