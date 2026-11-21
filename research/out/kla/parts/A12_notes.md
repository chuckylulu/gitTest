# KLA (KLAC) - A1 results and A2 leading signals

Fiscal year ends June 30. Quarters: Q2 FY26 = Oct-Dec 2025, Q3 FY26 = Jan-Mar 2026, Q4 FY26 = Apr-Jun 2026, Q1 FY27 = Jul-Sep 2026 (latest). $ in millions unless stated. Per-share figures: Q4 FY26 and later documents are post-split (10-for-1, effective June 11, 2026); the Q2 and Q3 FY26 releases and letters are pre-split [F] A1-037. No per-share figure is used below.
Scripts: `research/out/kla/calc/a12_results.py` (A1), `research/out/kla/calc/a12_leading.py` (A2). Every built-in check passed: segment and product sums, FY26 = sum of quarters, adjustment totals, recomputed non-GAAP margins within 0.05pp of KLA's stated figures.

## A1 Results

### Quarterly and annual P&L, GAAP vs non-GAAP

KLA's non-GAAP figures leave out the one-off items it names itself. For the four latest quarters that means only **acquisition-related charges**, which are mainly intangible amortisation [F] A1-009. In Q4 FY26 they also include an $11.6M discrete interest release, which sits below operating income [F] A1-010. FY25 also left out **restructuring/severance** of $7.1M [F] A1-016 and a **$239.1M goodwill and intangible impairment** of the PCB business [F] A1-015. Tax-only items affect net income, not margins: Pillar Two UTPR taxes ($20.2M in Q1 FY27) and discrete tax items [F] A1-011. KLA does not print an operating income line, so GAAP operating income here = revenue - COGS - R&D - SG&A (- impairment).

| Period | Revenue | YoY | GM GAAP | GM ex one-offs (non-GAAP) | OM GAAP | OM ex one-offs (non-GAAP) | One-offs above op. line | FCF | SBC | SBC/FCF |
|---|---|---|---|---|---|---|---|---|---|---|
| Q2 FY26 (Oct-Dec 25) | 3,297.1 | +7.2% | 61.4% | 62.6% | 41.3% | 42.8% | acq. 49.0 | 1,262.0 | 73.9 | 5.9% |
| Q3 FY26 (Jan-Mar 26) | 3,415.1 | +11.5% | 61.1% | 62.2% | 41.2% | 42.6% | acq. 47.0 | 622.3 | 83.9 | 13.5% |
| Q4 FY26 (Apr-Jun 26) | 3,657.6 | +15.2% | 61.4% | 62.4% | 42.5% | 43.7% | acq. 44.7 (+(11.6) below op.) | 817.1 | 82.1 | 10.0% |
| Q1 FY27 (Jul-Sep 26) | 4,136.0 | +28.9% | 61.9% | 62.7% | 45.0% | 46.1% | acq. 43.0 | 1,336.2 | 84.1 | 6.3% |
| FY26 (Jul 25-Jun 26) | 13,579.5 | +11.7% | 61.3% | 62.4% | 41.7% | 43.1% | acq. 189.7 (+(11.6) below) | 3,767.1 | 310.2 | 8.2% |
| FY25 (Jul 24-Jun 25) | 12,156.2 | +23.9% | 60.9% | 62.3% | 39.3% | 43.1% | acq. 219.7, restr. 7.1, impairment 239.1 | 3,746.6 | 265.0 | 7.1% |
| LTM to Sep 30, 2026 | 14,505.8 | +15.8% | 61.5% | 62.5% | 42.6% | 43.9% | acq. 183.6 | 4,037.6 | 324.1 | 8.0% |

Sources: revenue [F] A1-001..004; YoY [I] A1-005. GAAP GM as printed by KLA (61.9/61.4/61.1/61.4) [F] A1-006. Non-GAAP GM/OM as stated by KLA [F] A1-017..022. Margin table [I] A1-023, A1-024 (High). LTM [I] A1-025, A1-026 (High). FCF [F] A1-027..031: Q1 FY27 OCF 1,530.9 - capex 194.8 = 1,336.2 [F] A1-028. SBC [F] A1-032..035; SBC/FCF [I] A1-036.
- Q3 FY26 items KLA named but neither excluded nor quantified: opex higher on "prototype materials timing and other reserve adjustments", and other income helped by a mark-to-market gain on a strategic supply investment [F] A1-021. The amounts are NOT DISCLOSED (read: Q3 FY26 letter p5, Q3 FY26 release reconciliation), so the margin cannot be shown without them.
- FCF swings with working capital. Q3 FY26 FCF of $622M was low because deferred system revenue fell $237M and receivables rose $234M; this comes from the cash-flow statement in the Q3 FY26 release, not from a separate evidence row.

### Revenue by reported segment (USD M; YoY; share of revenue)

| Segment | Q2 FY26 | Q3 FY26 | Q4 FY26 | Q1 FY27 | FY26 |
|---|---|---|---|---|---|
| Semiconductor Process Control (incl. its services) | 3,004.6 (+9.0%; 91%) | 3,083.9 (+12.6%; 90%) | 3,256.8 (+13.2%; 89%) | 3,754.3 (+29.5%; 91%) | 12,244.7 (+11.9%; 90%) |
| Specialty Semiconductor Process | 140.6 (-12.4%) | 164.0 (+4.8%) | 159.7 (+12.6%) | 139.5 (+16.5%) | 584.1 (-0.5%) |
| PCB and Component Inspection | 152.2 (-5.5%) | 167.6 (-0.5%) | 241.1 (+56.5%) | 242.2 (+27.8%) | 750.4 (+20.7%) |

[F] A1-038..041; [I] A1-042.

### Revenue by major product group (10-Q/10-K disaggregation; USD M, YoY)

| Product | Q2 FY26 | Q3 FY26 | Q4 FY26 | Q1 FY27 | FY26 |
|---|---|---|---|---|---|
| Wafer Inspection | 1,572.8 (+0.7%) | 1,739.7 (+16.3%) | 1,781.1 (+0.5%) | 2,111.2 (+37.3%) | 6,630.8 (+7.0%) |
| Patterning (metrology + reticle inspection) | 696.2 (+31.2%) | 615.1 (-3.4%) | 728.1 (+60.8%) | 862.5 (+29.2%) | 2,706.8 (+23.2%) |
| Specialty Semi Process (systems) | 121.6 (-15.0%) | 144.2 (+4.2%) | 136.5 (+11.0%) | 113.6 (+13.3%) | 502.5 (-2.8%) |
| PCB & Component Inspection (systems) | 80.3 (-13.9%) | 95.1 (-8.7%) | 167.5 (+96.2%) | 167.5 (+42.8%) | 460.3 (+29.3%) |
| Services | 786.1 (+17.8%) | 774.8 (+15.8%) | 820.4 (+16.8%) | 850.5 (+14.2%) | 3,125.9 (+16.5%) |
| Other (refurb/legacy/upgrades) | 40.2 | 46.2 | 23.9 | 30.7 | 153.1 |

[F] A1-043..047; [I] A1-048. The Q4 FY25 base is derived as FY25 minus 9M FY25 and reconciles to reported Q4 FY25 revenue. No finer split (metrology vs reticle inspection, e-beam, optical) is given each quarter: NOT DISCLOSED (read: 10-Q Q1 FY27 segment note; Q1 FY27 letter p4-5; slides p6) [F] A1-049.

### End market (Semi Process Control systems only, semiconductor customers only, approximate)

KLA definition: "approximate Semi Process Control system-only sales to Foundry/Logic customers or Memory customers only" [F] A1-050.

| | Q2 FY26 | Q3 FY26 | Q4 FY26 | Q1 FY27 | Q2 FY27 guide |
|---|---|---|---|---|---|
| Foundry/logic | ~60% | ~62% | ~79% | ~72% | ~60% |
| Memory | ~40% | ~38% | ~21% | ~28% | ~40% |
| DRAM / NAND within memory | 75 / 25 | 86 / 14 | ~83 / 17 | NOT DISCLOSED (read: Q1 FY27 letter p4, slides p5) | ~84 / ~16 |

[F] A1-051..054; guide [C] A1-055. Implied DRAM share of the base: 30.0% / 32.7% / 17.4% [I] A1-056 (Medium; built from rounded approximations).

### Services

- Quarterly: $786M (+18%), $775M (+16%), $820M (+17%), $850M (+14%) [F] A1-057..060. FY26 $3,125.9M, +16.5%, 23.0% of revenue. LTM $3,231.8M (22.3%) [I] A1-061. CY25 $2.9B, +15% [F] A1-068.
- Contracted share: ">80% of revenue (up from >75% in CY22) coming from multi-year, subscription service contracts" [C] A1-062. Same Investor Day deck: "~3-year average contract length", "95% contract renewal rate", and "95% of revenue is recurring: inclusive of both contract and time-and-materials" [C] A1-063. Spoken at Investor Day, the contracts are "more than three years" [C] A1-064. This differs from the slide's "~3-year average", so treat contract length as about 3 years. The Nov 2025 update (CY24 actuals) gave >75% contracts, >95% renewal and >3 yr length [C] A1-065.
- KLA does not give a share of contracts on long-term agreements beyond the >80% figure, and no RPO for service contracts beyond deferred service revenue: NOT DISCLOSED (read: Investor Day slides p104-113; 10-Q Q1 FY27 Note 2).
- Long-term target: 13-15% CAGR, raised at the Mar 2026 Investor Day (12-14% in 2022, 9-11% in 2019) [C] A1-066. CY26 is expected at the top end of that range [C] A1-067.

### Advanced packaging / HBM / AI (light touch; the AP agent owns the deep dive)

KLA uses two AP revenue definitions, and they are not interchangeable:
- "calendar 2025 **total systems revenue** of approximately $950 million", >70% YoY (Q2 FY26 letter) [C] A1-069. The Investor Day slide labels it "~$950M KLA Advanced Packaging Revenue in 2025".
- AP "**Semiconductor Process Control product portfolio** revenue": ~$635M in 2025, rising to ~$1B in CY26 (Apr 2026 view) [C] A1-070. Since Jul 2026, "Advanced Packaging **process control systems** revenue" is expected at ~$1.1B in CY26, >70% YoY [C] A1-071. So the >70% growth is measured on the ~$635M process-control base.
- Intensity definition: "KLA Semi PC systems revenue in Advanced Packaging / Advanced Packaging Market" = 5.6% in 2025 [C] A1-072.
- Implied share of CY25 revenue ($12,745M): ~7.5% on the $950M total-systems basis and ~5.0% on the $635M process-control basis. The ~$315M gap is probably non-process-control AP systems (e.g. SPTS); KLA does not say so [I] A1-073 (Medium).
- KLA gives no HBM or AI percentage of revenue, only qualitative statements: NOT DISCLOSED (read: Q1 FY27 letter/slides/10-Q, Q4 FY26 letter) [F] A1-074.

## A2 Leading signals

| Item | Jun 30, 2025 | Dec 31, 2025 | Mar 31, 2026 | Jun 30, 2026 | Sep 30, 2026 | Evidence |
|---|---|---|---|---|---|---|
| Backlog ($B) | 7.86 | NOT DISCLOSED | NOT DISCLOSED | 12.57 | NOT DISCLOSED ("continues to grow") | [F] A2-001, A2-003; [C] A2-004 |
| Orders / book-to-bill | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | FY26 implied ~1.35 | NOT DISCLOSED | [I] A2-006 (Low) |
| Inventory total ($M) | 3,212.1 | 3,282.6 | 3,437.0 | 3,648.5 | 4,090.4 | [F] A2-007..010 |
| - raw materials | 1,491.8 | 1,568.7 | 1,648.4 | 1,849.7 | 2,126.9 | |
| - WIP | 833.9 | 836.2 | 929.6 | 937.7 | 1,076.9 | |
| - finished goods | 285.7 | 252.2 | 256.5 | 238.4 | 247.5 | |
| - customer service parts | 600.8 | 625.5 | 602.5 | 622.7 | 639.0 | |
| Contract liabilities ($M) | 1,713.7 | 1,727.9 | 1,448.9 | 1,775.1 | 1,707.8 | [F] A2-012..016 |
| - of which due <12 months | n/a | 84.3% | 82.6% | 86.6% | 86.5% | [I] A2-018 |
| - deferred system revenue | 816.8 | 858.1 | 620.8 | 932.9 | 843.0 | [F] A2-017 |
| Customer deposits (cur.+non-cur.) | 643.2 | 370.6 | 420.9 | 433.9 | 507.8 | [F] A2-019..021 |
| AR net ($M) | 2,263.9 | 2,073.6 | 2,304.5 | 2,889.2 | 3,072.1 | [F] A2-022, 024, 025 |
| Long-term AR ($M) | 0 | 0 | 0 | 180.7 | 266.8 | [F] A2-023 |
| DSO (days, trade AR) | | 57.9 | 60.7 | 71.9 | 68.3 | [I] A2-027 |
| Purchase commitments ($B) | n/a | 2.75 | 4.83 | 5.97 | 8.87 | [F] A2-029..032 |

- Backlog is "primarily consisting of sales orders where written customer requests have been received" [F] A2-002. It is disclosed only annually, in the 10-K. The FY26 10-K attributes the rise to AI-infrastructure demand. Unlike the FY25 10-K (71-76% within 12 months [F] A2-003), it gives **no share due within 12 months**: NOT DISCLOSED (read: 10-K FY26 Item 1 Backlog).
- KLA's 10-Q "transaction price not yet recognized" table equals contract liabilities only ("which equals our contract liabilities") [F] A2-013. It is not a full RPO or backlog figure, so the 10-Qs give no quarterly backlog: NOT DISCLOSED (read: 10-Q Q2 FY26, Q3 FY26, Q1 FY27 Note 2).
- Orders, bookings and book-to-bill: NOT DISCLOSED (read: Q2 FY26-Q1 FY27 letters, slides, releases, 10-Qs). The FY26 implied orders of ~$18.3B and book-to-bill of ~1.35 = (revenue + Δbacklog) / revenue [I] A2-006 (Low: cancellations, FX and backlog scope are unknown).
- Inventory signal: since Jun 2025 total inventory is up 27%, raw materials up 43% and WIP up 29%, while finished goods are down 13%. The raw-material share rose from 47.8% to 52.0% [I] A2-011. This pattern means building ahead of shipments, not unsold product (Medium). KLA says it raised purchase commitments "in part to secure the supply of key components" [F] A2-033. In Q2 FY26 it said lead times were rising on supply constraints [C] A2-005.
- Purchase commitments rose 3.2x in three quarters to $8.87B, equal to 1.59x LTM COGS [I] A2-034.
- Receivables: DSO rose from ~58 to ~68-72 days, and a long-term AR line appeared in Jun 2026 ($267M at Sep 2026) [F] A2-023. Factoring was $515M in FY26 vs $231M in FY25, but only $32M in Q1 FY27 [F] A2-028. Payment terms are 70-90% within 30-60 days of shipment [F] A2-026. Lower factoring in Q1 FY27 partly explains the DSO level; when factoring is high, reported DSO understates the true figure (Medium).

## Prior-claim check (research/prior/text/kla_metrology_audit.md, lines 21-68 and the KLA handoff row)

| Prior claim | Verdict | Correct value / comment | Evidence |
|---|---|---|---|
| Backlog $7.86B (Jun 30, 2025) to $12.57B (Jun 30, 2026) | CONFIRMED (amounts); CORRECTED (cause) | Amounts are right. The 10-K attributes the rise to "strong demand driven by the AI infrastructure buildout"; it does not cite optical supply bottlenecks as the prior file implies | [F] A2-001 |
| Services $3.1B FY26; $850M Q1 FY27 +14% YoY | CONFIRMED | FY26 $3,125.9M; Q1 FY27 $850.5M, +14.2% | [F] A1-046, A1-057; [I] A1-061 |
| >80% of services on >3-yr (fixed) subscription contracts; <20% T&M | CORRECTED | >80% of revenue from multi-year subscription contracts [C]; the written slide says "~3-year average contract length" (spoken: "more than three years"). "Fixed" is not KLA's word. The slide says 95% of services revenue is recurring including T&M, and gives no "<20% T&M" figure | [C] A1-062..064 |
| 95% contract renewal | CONFIRMED | 95% contract renewal rate (Investor Day); >95% in Nov 2025 update | [C] A1-063, A1-065 |
| Services CAGR target raised to 13-15% (Mar 2026) | CONFIRMED | | [C] A1-066 |
| Q1 FY27 revenue $4.14B, non-GAAP OM 46.1%, GM 61.9% / 62.7% | CONFIRMED | 4,136.0; 46.1% (recomputed 46.05%); GAAP GM 61.9%, NG 62.7% | [F] A1-001, A1-006, A1-017, A1-018 |
| Q1 FY27 +28.9% YoY | CONFIRMED | +28.9% | [I] A1-005 |
| LTM $14.51B | CONFIRMED | $14,505.8M (+15.8% YoY) | [I] A1-025 |
| LTM GM 61.5% / 62.5% | CONFIRMED | 61.47% / 62.47% | [I] A1-026 |
| Q1 FY27 FCF $1.34B (OCF $1.53B - capex $195M) | CONFIRMED | 1,530.9 - 194.8 = 1,336.2 | [F] A1-027, A1-028 |
| FY26 revenue $13.58B | CONFIRMED | 13,579.5 | [F] A1-002 |
| Q2 FY27 guidance $4.70B ± $200M | CONFIRMED | $4.7B ± $200M; NG GM 62.5% ± 1% | [C] A1-075 |
| Services 20.6% of Q1 FY27 revenue; FY26 23.0% | CONFIRMED | 20.6%; 23.0% | [I] A1-061 |
| Recurring ~16.5%-18.4% of total revenue | NOT VERIFIABLE as stated | >80% x FY26 services = ≥18.4% of FY26 revenue (illustrative lower bound only); KLA gives no recurring-revenue % of total | a12_results.py output |
| CY25: $9.0B Semi PC + $3.0B services / $12.74B; "94.2% Semi PC + Services; ~5.8% PCB/Comp" | CORRECTED | CY25 total $12,745M is right. Semi PC systems (WI+Patterning+Other) $8,971M + services $2,903M = 93.2%. PCB & Component segment = 5.2% (systems only 3.0%). Specialty Semi Process (4.4%) is missing from the prior split | Q2 FY26 slides p6-7; a12_results.py |
| Total AP revenue ~$950M CY25; AP process-control systems $1.1B+ in CY26 (+70%+) | CORRECTED (wording) | $950M is "total systems revenue" [C]. The CY26 figure is "approximately $1.1 billion" (not "$1.1B+") on a ~$635M process-control base, >70% YoY | [C] A1-069..071 |
| Gen4/Gen5 lead times >12 months; optical bottlenecks constrained H1 CY26 | NOT VERIFIABLE (in A1/A2 docs) | Q2 FY26 letter: lead times "increasing due to supply constraints", with no months stated | [C] A2-005 |

## Premise issues
- The prior file implies the 10-K ties the backlog rise to optical supply bottlenecks. The 10-K cites AI-driven demand (above).
- The prior file treats "$1.1B+" AP process control and "$950M total AP" as one series. They are different definitions; the CY25 base for the $1.1B is ~$635M.
- The prior handoff row's "94.2% / ~5.8%" CY25 mix does not reconcile with KLA's CY25 table (see above).
- "Order backlog" in the 10-Q intangibles note (Note 6) is an acquired-intangible category, not a backlog disclosure. Do not read it as one.
- Pre-split vs post-split: Q2 and Q3 FY26 per-share figures in their own releases (e.g. NG EPS $8.85, $9.40) are pre-split. The Q4 FY26 release restates them post-split ($0.94 for Q3 FY26).

## Gaps (for gaps.md)
- Quarterly backlog: NOT DISCLOSED (read: 10-Q Q2 FY26, Q3 FY26, Q1 FY27; letters and slides Q2 FY26-Q1 FY27).
- Backlog share due within 12 months at Jun 30, 2026: NOT DISCLOSED (read: 10-K FY26 Item 1 Backlog).
- Orders / bookings / book-to-bill: NOT DISCLOSED (read: letters, slides, releases, 10-Qs Q2 FY26-Q1 FY27).
- DRAM vs NAND split of Q1 FY27 actual memory revenue: NOT DISCLOSED (read: Q1 FY27 letter p4, slides p5).
- HBM or AI share of revenue: NOT DISCLOSED (read: Q1 FY27 letter, slides, 10-Q; Q4 FY26 letter).
- Finer product split (metrology vs reticle inspection, e-beam): NOT DISCLOSED (read: 10-Q Q1 FY27 segment note; letters).
- Amounts of the Q3 FY26 reserve/prototype opex items and the supply-investment mark-to-market gain: NOT DISCLOSED (read: Q3 FY26 letter p5; Q3 FY26 release).
- Services contract share by term beyond ">80%", and services RPO: NOT DISCLOSED (read: Investor Day slides p104-113; 10-Q Q1 FY27 Note 2).
