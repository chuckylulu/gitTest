# A4 / A5 notes: KLA Corporation (KLAC), concentration, geography, export rules, balance sheet and capital

Fiscal year ends June 30. Q1 FY27 = Jul-Sep 2026 (latest; 10-Q filed 2026-10-29). $ in thousands unless stated. Evidence ids refer to `parts/A4.csv` and `parts/A5.csv`. Arithmetic: `calc/a4_region_parse.py`, `calc/a4_segment_parse.py`, `calc/a4_china_share.py` (output `calc/a4_china_share_output.txt`), `calc/a5_capital.py` (output `calc/a5_capital_output.txt`).

No margin or profit figures are computed in A4/A5, so no one-off adjustment table is needed. The impairments listed under A5 are the one-off items management named for FY24 and FY25 (handled by A1 for margins).

## A4.1 Customers above 10%

| Period | >10% customers (revenue) | Named? | Evidence |
|---|---|---|---|
| FY26 (Jul 2025-Jun 2026) | one customer, ~19% | Yes: TSMC (Item 1 table) | [F] A4-046, A4-047 |
| FY25 (Jul 2024-Jun 2025) | one customer, ~19% | Yes: TSMC | [F] A4-046, A4-047 |
| FY24 (Jul 2023-Jun 2024) | one customer, ~13% | Yes: TSMC | [F] A4-048, A4-050 |
| FY23 / FY22 (context) | two customers 18% and 15% / 20% and 12% | Yes: TSMC and Samsung | [F] A4-049, A4-050 |
| Q1 FY26 (Jul-Sep 2025) | three customers 15%, 11%, 10% | No | [F] A4-052 |
| Q2 FY26 (Oct-Dec 2025) | two customers 17%, 11% | No | [F] A4-053 |
| Q3 FY26 (Jan-Mar 2026) | two customers 19%, 11% | No | [F] A4-054 |
| Q1 FY27 (Jul-Sep 2026) | two customers 21%, 13% | No | [F] A4-051 |

- Annual 10-Ks name the >10% customers; quarterly 10-Qs give percentages only, never names. [F] A4-046, A4-051
- Receivables: TSMC >10% of AR at Jun 30, 2024 (TSMC and Samsung at Jun 30, 2023) [F] A4-056; two customers at Jun 30, 2025 and Dec 31, 2025; three at Sep 30, 2025 and Mar 31, 2026 (unnamed) [F] A4-055.
- AR concentration at Jun 30, 2026 and Sep 30, 2026: NOT DISCLOSED (read: FY26 10-K Note 1 Concentration of Credit Risk and Note 17; Q1 FY27 10-Q Note 16).

## A4.2 Revenue by region, last 4 quarters (share of total, %)

| Region | Q2 FY26 (Oct-Dec 2025) | Q3 FY26 (Jan-Mar 2026) | Q4 FY26 (Apr-Jun 2026) | Q1 FY27 (Jul-Sep 2026) | LTM |
|---|---|---|---|---|---|
| China | 30.2 | 24.3 | 26.2 | 34.5 | 29.0 |
| Taiwan | 25.6 | 25.4 | 31.1 | 24.7 | 26.7 |
| North America | 12.0 | 12.0 | 17.9 | 14.9 | 14.3 |
| Korea | 14.5 | 19.9 | 10.2 | 12.0 | 14.0 |
| Japan | 6.9 | 5.3 | 5.8 | 3.9 | 5.4 |
| Rest of Asia | 5.9 | 5.8 | 4.3 | 5.3 | 5.3 |
| Europe and Israel | 4.9 | 7.2 | 4.6 | 4.7 | 5.3 |
| Total revenue ($k) | 3,297,146 | 3,415,078 | 3,657,556 | 4,136,015 | 14,505,795 |

[I] A4-036 to A4-040, High confidence; inputs are the 10-Q/10-K geography notes. Q4 FY26 printed directly in the Q1 FY27 10-Q QoQ table [F] A4-014.

## A4.3 China share by quarter, Q1 FY24 to Q1 FY27 (13 quarters)

| Quarter | Calendar | China ($k) | Total ($k) | China % | QoQ % | YoY % | Source |
|---|---|---|---|---|---|---|---|
| Q1 FY24 | Jul-Sep 2023 | 1,025,944 | 2,396,956 | 42.8 | - | - | [F] A4-001 |
| Q2 FY24 | Oct-Dec 2023 | 1,027,780 | 2,486,726 | 41.3 | +0.2 | - | [F] A4-002 |
| Q3 FY24 | Jan-Mar 2024 | 996,885 | 2,359,830 | 42.2 | -3.0 | - | [F] A4-003 |
| Q4 FY24 | Apr-Jun 2024 | 1,146,118 | 2,568,735 | 44.6 | +15.0 | - | [I] derived FY24 10-K minus 9M |
| Q1 FY25 | Jul-Sep 2024 | 1,198,305 | 2,841,541 | 42.2 | +4.6 | +16.8 | [F] A4-004 |
| Q2 FY25 | Oct-Dec 2024 | 1,092,525 | 3,076,851 | 35.5 | -8.8 | +6.3 | [F] A4-005 |
| Q3 FY25 | Jan-Mar 2025 | 792,884 | 3,063,029 | 25.9 | -27.4 | -20.5 | [F] A4-006 |
| Q4 FY25 | Apr-Jun 2025 | 958,854 | 3,174,741 | 30.2 | +20.9 | -16.3 | [I] derived FY25 10-K minus 9M |
| Q1 FY26 | Jul-Sep 2025 | 1,267,156 | 3,209,696 | 39.5 | +32.2 | +5.7 | [F] A4-007 |
| Q2 FY26 | Oct-Dec 2025 | 994,891 | 3,297,146 | 30.2 | -21.5 | -8.9 | [F] A4-008 |
| Q3 FY26 | Jan-Mar 2026 | 829,583 | 3,415,078 | 24.3 | -16.6 | +4.6 | [F] A4-009 |
| Q4 FY26 | Apr-Jun 2026 | 956,728 | 3,657,556 | 26.2 | +15.3 | -0.2 | [F] A4-014 |
| Q1 FY27 | Jul-Sep 2026 | 1,425,744 | 4,136,015 | 34.5 | +49.0 | +12.5 | [F] A4-010 |

Shares and growth rates: [I] A4-016 to A4-028, High (script `a4_china_share.py`). KLA itself prints +49% QoQ and +13% YoY for Q1 FY27 [F] A4-015.

Fiscal years: FY24 42.8%, FY25 33.3%, FY26 29.8% [F] A4-011 to A4-013. Calendar years: CY2024 40.9%, CY2025 31.5%, Jan-Sep 2026 28.7% [I] A4-029 to A4-031. Pre-surge baseline: FY21 26.5%, FY22 28.9%, FY23 27.3% [I] A4-034.

**China share of Semi Process Control systems.** NOT DISCLOSED (read: shareholder letters and earnings slides Q4 FY24-Q1 FY27; Investor Day 2026 slides and transcripts). KLA gives only a total-company China share. The CFO said the total includes non-semi-PC business in China (PCB, component inspection) that "skews the numbers a bit up", without quantifying it [S] A4-079. So the semi PC systems share is probably slightly below the total share, but the gap is unknown.

## A4.4 Prior-period figures changed between filings

- Regional revenue: no unexplained changes. All 7 regions plus the total for Q1-Q3 FY24, Q1-Q3 FY25 and Q1 FY26 are identical as first reported and as the prior-year column of the next 10-Q. FY23, FY24 and FY25 annual regional figures are identical across later 10-Ks. [I] A4-042, High.
- Segment revenue: no changes in amounts. The segment was renamed from "PCB, Display and Component Inspection" (through Q3 FY24) to "PCB and Component Inspection" (FY24 10-K onward). [I] A4-043.
- Presentation only: the Q4 FY24 letter shows China at 44%, but the figure derived from the 10-K is 44.6%. KLA rounded so the regions add to 100%. [I] A4-044, [F] A4-045. From Q1 FY26 the 10-Q prints region shares to one decimal place instead of whole percent. This is a format change only.

## A4.5 Export rules that bind KLA, and KLA's own estimate of each one's impact

| Rule (date) | What it restricts (as KLA or the FR text says) | KLA's own impact statement | Evidence |
|---|---|---|---|
| Oct 7, 2022 BIS IFR (87 FR 62186) | Licences needed for effectively all KLA products and services to China fabs making non-planar or <=16/14nm logic, >=128-layer NAND, or <=18nm half-pitch DRAM; limits on US-person support; limits on tools sold to China WFE makers | Preliminary **gross direct CY2023 impact of $500M-$900M** (based on backlog, before reallocation). By Aug 2023: "have not significantly impacted our operations to date" | [C] A4-057, A4-058, A4-059; FR text NOT RETRIEVED |
| Oct 17, 2023 update (SME IFR 88 FR 73424, published Oct 25, 2023; effective Nov 2023) | Revises the 2022 parameters, adds anti-circumvention measures, extends coverage to arms-embargoed countries | **No quantified impact**: "still evaluating these rules" | [F] A4-060, A4-061 |
| Dec 2, 2024 IFR (89 FR 96790) + Entity List additions; Jan 2025 follow-on rules | New SME controls, new foreign direct product (FDP) rules, HBM controls, more Entity List names, a revised advanced-DRAM definition | **~$500M ± $100M CY2025 revenue impact, ~70% systems** (first given early Dec 2024). **RPO cut by ~$430M** (about half due within 12 months). Services growth hit in Mar 2025 quarter | [F] A4-062, A4-064, A4-066; [C] A4-063; [S] A4-065 |
| Sep 29, 2025 Affiliates Rule IFR (90 FR 47201) | Entity List / MEU restrictions extended to entities ≥50% owned by listed parties | **~$300-350M across the Dec 2025 quarter and CY2026**, described as "extended export controls" (KLA did not name the rule). CFO: the Dec 2025 quarter impact was "fairly immaterial" | [F] A4-067; [C] A4-068; [S] A4-069 |
| Nov 10, 2025 suspension (FR 2025-19846), to Nov 9, 2026 | Affiliates Rule stayed | Jan 2026 CFO: China now expected **up** in CY2026, versus modestly down three months earlier; the affiliate business "feathered" back into the forecast; the recovered amount was "that ballpark" of $300-350M (no exact figure) | [F] A4-070, A4-071; [S] A4-072 |
| Nov 9, 2026 extension of the suspension to Jan 10, 2027 | Affiliates Rule still stayed | No KLA statement (falls after the Q1 FY27 10-Q). The Q1 FY27 10-Q has no new export risk factor | [S] A4-073; [F] A4-074 |
| 2026 SME-specific BIS rules | none found that KLA names | FY26 10-K and Q1 FY27 10-Q list no 2026 rule | [F] A4-074 |

- Calendar 2025 outcome against the Dec 2024 guidance: China revenue fell 9.5% in CY2025 [I] A4-032, against the "~20%" decline the CFO gave at UBS [S] A4-065. KLA did not publish a realised-impact figure for the $500M estimate: NOT DISCLOSED (read: Q2 FY25-Q4 FY26 letters and 10-Qs).
- The Affiliates Rule now returns on Jan 10, 2027 unless BIS extends the suspension again. This is a dated regulatory risk for the B3 catalysts list [S] A4-073.

## A4.6 "China revenue has normalised": evidence for and against

What KLA calls normal: a China share in the high-20s percent of revenue in CY2026 (letter [C] A4-041; CFO "27% to 29%" [S] A4-078), falling to the low-20s in 2027 [S] A4-078. The CFO attributed the decline partly to export controls and partly to "general normalization" [S] A4-075. China's growth is expected to be slower than WFE [S] A4-077.

For:
- CY2026 Jan-Sep China share is 28.7%, inside KLA's high-20s range [I] A4-031. If Q2 FY27 lands at a 25-29% China share, CY2026 comes out at 27.6-28.8% [I] A4-035.
- The pre-surge level (FY21-FY23) was 26.5-28.9%, so the current share matches history [I] A4-034.
- China revenue grew 6.4% in Jan-Sep 2026 against 18.6% total growth [I] A4-033. This is the slower growth that "normalisation" implies.

Against:
- Q1 FY27 China jumped +49% QoQ to 34.5% of revenue, driven by mature-node foundry/logic [F] A4-015. Quarterly swings of 24-40% persist [I] A4-016 to A4-028.
- In dollars, China revenue has not shrunk: FY26 was $4.05B, against $4.04B in FY25 and $4.20B in FY24 [F] A4-011 to A4-013. The share falls only because other regions grow.
- The FY26 share benefited from suspension of the Affiliates Rule. If the rule returns on Jan 10, 2027, KLA's own ~$300-350M estimate becomes relevant again [S] A4-072, A4-073.
- The stated 2027 level (low-20s) is below the CY2026 level, so KLA does not treat the current share as the floor [S] A4-078.

## A5.1 Balance sheet (Sep 30, 2026 unless stated)

| Item | Value | Evidence |
|---|---|---|
| Cash, equivalents and marketable securities | $4,741.2M (Jun 30, 2026: $4,902.4M; Mar 31: $4,957.9M; Dec 31, 2025: $5,207.5M; Sep 30, 2025: $4,683.6M) | [F] A5-001 to A5-005 |
| Senior notes principal | $5,950.0M; carrying value $5,723.3M | [F] A5-014 |
| Net debt (principal minus cash) | $1,208.8M (Q2 FY26 $742.5M, Q3 $992.1M, Q4 $1,047.6M) | [I] A5-028 |
| Revolver | $1.50B, Credit Agreement Jul 3, 2025, matures Jul 3, 2030 (+2 one-year extensions, +$500M accordion), undrawn | [F] A5-017 |
| Covenants | Max net leverage 3.25x (3.75x after a material acquisition); indenture limits on liens and sale-leaseback; 101% change-of-control put; in compliance | [F] A5-018, A5-019 |
| Commercial paper | NOT DISCLOSED (read: Q1 FY27 10-Q Note 7 and Liquidity; FY26 10-K Item 7 and Note 8). No programme mentioned | [I] A5-029 |
| Convertibles | None. All debt is fixed-rate senior unsecured notes | [I] A5-030 |
| Ratings | Moody's A2, S&P A-, Fitch A- | [F] A5-021 |
| Swaps | $2.00B of 2022 notes swapped fixed-to-floating (SOFR), FY26 | [F] A5-015 |
| Interest expense | Q2 FY26 $69.7M; Q3 FY26 $70.4M; Q4 FY26 $73.3M (derived); Q1 FY27 $67.9M; LTM $281.3M; FY26 $284.4M, FY25 $302.2M | [F] A5-022 to A5-025 range; [I] A5-026 |

Debt ladder (Q1 FY27 10-Q Note 7) [F] A5-006 to A5-013:

| Coupon | Maturity | Principal ($M) | Effective rate |
|---|---|---|---|
| 4.100% | Mar 15, 2029 | 800 | 4.159% |
| 4.650% | Jul 15, 2032 | 1,000 | 4.657% |
| 4.700% | Feb 1, 2034 | 500 | 4.777% |
| 5.650% | Nov 1, 2034 | 250 | 5.670% |
| 5.000% | Mar 15, 2049 | 400 | 5.047% |
| 3.300% | Mar 1, 2050 | 750 | 3.302% |
| 4.950% | Jul 15, 2052 | 1,450 | 5.023% |
| 5.250% | Jul 15, 2062 | 800 | 5.259% |
| **Total** | | **5,950** | weighted 4.668% effective / 4.629% coupon; 17.8 yrs [I] A5-027 |

There is no maturity before Mar 2029. The $750M note due Nov 1, 2024 was repaid [F] A5-020.

## A5.2 Buybacks, authorisation, dividend

| Quarter | Shares repurchased (post-split, k) | Cost ($M, trade date) | Evidence |
|---|---|---|---|
| Q1 FY26 (Jul-Sep 2025) | 6,230 (623 pre-split) | 564.4 | [F] A5-032 |
| Q2 FY26 (Oct-Dec 2025) | 4,600 (460 pre-split) | 537.6 | [F] A5-033 |
| Q3 FY26 (Jan-Mar 2026) | 4,400 (440 pre-split) | 631.9 | [F] A5-034 |
| Q4 FY26 (Apr-Jun 2026) | 3,011 (derived) | 570.1 (derived) | [I] A5-036 |
| Q1 FY27 (Jul-Sep 2026) | 4,914 | 942.9 (cash basis $935.8M) | [F] A5-031 |
| Last 4 quarters | 16,925 | 2,682.5 | [I] A5-037 |

- Authorisations: +$2B announced Sep 5, 2023 [F] (Q1 FY24 release, note in A5-039). +$5.00B in Q4 FY25, announced Apr 30, 2025 [F] A5-039, A5-041. +$7.00B in Q3 FY26 (Jan-Mar 2026), announced publicly with results on Apr 29, 2026 [F] A5-039, A5-040.
- Remaining authorisation: **$8.81B at Sep 30, 2026** [F] A5-038. Earlier: $9.74B (Jun 2026), $10.31B (Mar 2026), $3.94B (Dec 2025), $4.47B (Sep 2025), $5.03B (Jun 2025). The roll-forward reconciles within KLA's $10M rounding [I] A5-043.
- Dividend: $1.90/quarter pre-split from Apr 2025 [F] A5-041; $2.30/quarter pre-split from the May 2026 declaration [F] A5-040, which is $0.23 post-split; Q1 FY27 declared $0.230 [F] A5-042. Dividends paid in Q1 FY27: $305.1M.
- 10-for-1 split, effective Jun 11, 2026 (split-adjusted trading Jun 12). The Q1 FY27 10-Q and FY26 10-K show post-split, retroactively adjusted share counts. The Q1-Q3 FY26 10-Qs show pre-split counts, so multiply those by 10 to compare [F] A5-044. Shares outstanding: 1,302,962,435 (Oct 26, 2026), down 0.25% from the split-adjusted Apr 27, 2026 count [F] A5-045, [I] A5-046. All per-share figures above say whether they are pre- or post-split.

## A5.3 M&A (FY22 to FY27 YTD) and impairments since

| Date | Deal | Price | Evidence |
|---|---|---|---|
| Jul 1, 2021 (Q1 FY22) | Anchor Semiconductor | $81.7M (+ up to $35M contingent) | [F] A5-047 |
| Feb 28, 2022 (Q3 FY22) | ECI Technology | $431.5M cash ($266.4M goodwill) | [F] A5-048 |
| May 1, 2022 (Q4 FY22) | Unnamed private company | $8.6M | [F] A5-049 |
| Aug 9, 2022 (Q1 FY23) | Unnamed materials-supply company | $32.7M | [F] A5-050 |
| Aug 11, 2022 (Q1 FY23) | Sale of Orbograph | $110.0M consideration, $29.7M gain | [F] A5-050 |
| FY24-Q1 FY27 | No business acquisitions ($3.7M FY24 outflow = holdback payment) | - | [F] A5-050 note |

Impairments:
- Q2 FY24: $219.0M, PCB and Display ($192.6M goodwill + $26.4M intangibles) [F] A5-051.
- Q3 FY24: $70.5M Display goodwill after the March 2024 exit decision [F] A5-052.
- Q2 FY25: $239.1M, PCB ($230.4M goodwill + $8.7M intangibles) [F] A5-055.
- FY26 annual test (Dec 31, 2025): no impairment [F] A5-056.

Cumulative charges are $528.6M across three charges, all in the Orbotech-derived PCB and Display businesses (KLA does not tie them to the Orbotech deal by name in these filings). The Display exit followed a major Display customer's cancellation of a technology project, and a settlement was received in Q2 FY25 (amount NOT DISCLOSED) [F] A5-054.

## Prior-claim check (prior/text/kla_metrology_audit.md)

| Prior claim | Verdict | Evidence |
|---|---|---|
| "Q1 FY27 10-Q: China +49% QoQ / +13% YoY" | CONFIRMED. The exact share is 34.5% (the prior said "exact SEC % pending") | [F] A4-010, A4-015 |
| "Announced FPD manufacturing exit Mar 2024" | CONFIRMED (decision March 2024) | [F] A5-053 |
| "following customer project cancellation" | CONFIRMED (FY25 10-K) | [F] A5-054 |
| "ended manufacturing Dec 31, 2024" | CORRECTED: Dec 31, 2024 was the *announced target* for ending manufacturing of *most* Display products. No later filing confirms the actual completion date | [F] A5-053 |
| "$70.5M Q3 FY24 goodwill impairment" | CONFIRMED. The prior omits the related $219.0M (Q2 FY24) and $239.1M (Q2 FY25) PCB/Display impairments | [F] A5-051, A5-052, A5-055 |
| "Q1 FY27 10-Q accession 0000319201-26-000034 dated 2026-10-29" | CONFIRMED (ir.kla.com mirror URL; signature date October 29, 2026) | [F] A4-010 url |
| KLA handoff row "China %: Pending" | Now filled: Q1 FY27 34.5%; FY26 29.8%; LTM 29.0% | [I] A4-028, [F] A4-013 |
| KLA row "LTM $14.51B" (cross-check only, A1 scope) | Consistent: LTM regional total $14,505.8M | [I] A4-040 |

## Premise issues

- The prompt dates the 2023 update "Oct 17, 2023". That is the BIS announcement date. The SME rule was published in the Federal Register on Oct 25, 2023 (88 FR 73424) and took effect in November 2023 [F] A4-060.
- The prompt says KLA estimated "~$400-500M CY2025 impact" for the Dec 2024 rules. KLA's figure was ~$500M ± $100M, i.e. $400-600M, with ~70% in systems [C] A4-063.
- The prompt frames the "affiliates rule ~$300-350M" estimate as an FY26 figure. KLA framed it as the Dec 2025 quarter plus calendar 2026 (Oct 2025-Dec 2026), and attributed it to "extended export controls" without naming the Affiliates Rule [C] A4-068.
- The suspension of the Affiliates Rule did not simply end in Nov 2026. It was extended to Jan 10, 2027 [S] A4-073.
- The prompt expects a "China share of semi process control systems" figure. KLA does not publish one (NOT DISCLOSED above).
- Prior file: the FPD "ended manufacturing Dec 31, 2024" claim is corrected above.

## Gaps

- NOT RETRIEVED (tried: govinfo.gov PDF and HTML for FR 2022-21658, 502 errors): Oct 7, 2022 BIS IFR text. The date and scope are taken from 88 FR 73424 and KLA's filings.
- NOT RETRIEVED (tried: federalregister.gov, which returned a CAPTCHA page, now deleted; manifest row for `2025-11-12_bis-fr_affiliates-rule-suspension.html` points to a removed captcha page, use `2025-11-12_bis-fr_rule-affiliates-suspension-Nov2025.html`): the Nov 9, 2026 FR rule extending the suspension. Only a law-firm alert was saved [S].
- NOT RETRIEVED (tried: web search for a UBS Dec 4, 2024 transcript; Seeking Alpha is paywalled): KLA's own Dec 2024 statement. The ~$500M figure is [F] only via the Jan 2025 letter.
- NOT DISCLOSED (read: Q2 FY25-Q1 FY27 letters, 10-Qs, FY26 10-K): KLA's realised revenue loss against the $500M (CY2025) and $300-350M estimates.
- NOT DISCLOSED (read: letters/slides Q4 FY24-Q1 FY27, Investor Day 2026): China share of Semi Process Control systems revenue.
- NOT DISCLOSED (read: FY26 10-K Note 1 and Note 17, Q1 FY27 10-Q Note 16): customers above 10% of receivables at Jun 30 and Sep 30, 2026.
- NOT DISCLOSED (read: all 10-Qs Q1 FY26-Q1 FY27): names of the quarterly >10% customers.
- NOT DISCLOSED (read: FY25 10-K Item 7): amount of the Q2 FY25 Display customer settlement.
- NOT DISCLOSED (read: FY24-FY26 10-Ks): actual completion date of Display manufacturing wind-down.
- NOT DISCLOSED (read: Q1 FY27 10-Q Note 7, FY26 10-K): commercial paper programme. None mentioned.
