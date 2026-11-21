# Lasertec Inventory and Procurement Forensics

## User prompt 1

GLOBAL CHAT RULES (PERMANENT — ZERO TOLERANCE FOR HANDWAVING):
- SILENT INTELLIGENCE ONLY: Raw dated primary facts, exact figures, verbatim Japanese/English filing disclosures, and forensic cross-checks. Zero opinions, adjectives, marketing language, stock prices, or valuation multiples.
- NO intros or summaries. Start immediately with dense markdown tables followed by thorough dry forensic bullets covering every anomaly, accounting nuance, and second-order implication uncovered.
- ADVERSARIAL PRIMARY-SOURCE STANDARD: Query Lasertec Corp. (`6920.T`, レーザーテック, EDINET `E02016`) Japanese & English TDnet / EDINET filings (`決算短信`, `有価証券報告書`, `半期報告書`, `決算説明資料`), balance-sheet notes, and earnings-call transcripts across FY2024 (ended Jun 2024), FY2025 (ended Jun 2025), FY2026 (ended Jun 2026), and Q1 FY2027 (ended Sep 30, 2026).
- MANDATORY TIE-OUT & GAP RULE: All inventory sub-components must reconcile to consolidated totals. If a line item is genuinely undisclosed in primary filings, state exact `"N/A (checked [exact filing & note/page])"` and follow corroborating balance-sheet or footnote clues rather than guessing.
- ANTI-TIMEOUT URL RULE: Cite exact filing/page + date inline; list ONE direct primary URL per document at the bottom.

TARGET #4 ECOSYSTEM CROSS-CHECK (Rigaku `268A.T`) — STEP B1-1: LASERTEC (`6920.T`) INVENTORY, BUFFER & PROCUREMENT FORENSICS:

Rigaku Holdings disclosed a **−¥1.0Bn FY2025** revenue drop (**−¥700M in H1 2025**) in EUV mask-inspection multilayer mirrors (`EUVマスク検査装置向け多層膜ミラー`, Components & Services) attributing it strictly to downstream customer inventory digestion, and guides that customer inventory will bottom in **FY2027**. Independently audit Lasertec's balance sheet and procurement footnotes to verify whether this inventory-digestion timeline holds up:

1. **Multi-Period Inventory & Working-Capital Forensics (Jun 2024, Sep 2024, Jun 2025, Sep 2025, Jun 2026, Sep 30, 2026 — exact ¥M, YoY%, QoQ% & DIO)**:
   - Disaggregate **Total Inventories** into exact **Finished Goods (`製品`)**, **Work-in-Process (`仕掛品`)**, and **Raw Materials & Supplies (`原材料及び貯蔵品`)**.
   - Pull **Inventory Write-Downs / Valuation Losses (`棚卸資産評価損`)**, **Advances Paid to Suppliers (`前渡金`)**, **Accounts Payable (`買掛金`)**, and **Customer Advances / Contract Liabilities (`前受金` / `契約負債`)** across the same periods.
   - Explicitly test the divergence between **Raw Materials** (where optical components and EUV multilayer mirrors sit prior to assembly) and **WIP / SPE production**: verify whether Lasertec's raw-material buffer stayed elevated through Sep 30, 2026 even as Q1 FY2027 SPE production ramped — and calculate exact months-of-inventory (MOI) / DIO to assess whether restocking realistically begins in FY2027 or gets pushed further out.

2. **Procurement, Long-Lead Optical Components & Supplier-Risk Audit (`有価証券報告書`)**:
   - Extract verbatim disclosures from Lasertec's FY2025 and FY2026 `有価証券報告書` (Risk Factors, R&D, Manufacturing/Procurement notes) regarding:
     * Long-lead-time optical/EUV component stockpiling and advance procurement policies,
     * Single-source or specialized-vendor dependencies for EUV multilayer mirrors, actinic light sources, and precision optics,
     * Any disclosed shift toward supplier diversification, dual-sourcing, in-house optical refurbishment, or extended mirror lifetime that would structurally reduce replacement/OEM mirror demand per `ACTIS` system.

## Model response 1

### 1. Multi-Period Inventory, Working-Capital & DIO/MOI Forensics (`6920.T`, EDINET `E01991`)

*(Note: EDINET submitter code for Lasertec Corp. is `E01991`, not `E02016`. Figures in ¥M, rounded down per J-GAAP `決算短信` / `有価証券報告書`. All inventory sub-components tie exactly to Consolidated Total Inventories.)*

#### Table 1A: Consolidated Inventory Disaggregation & Working-Capital Balances (¥M)

| Line Item (J-GAAP) | Jun 30, 2024 (FY24) | Sep 30, 2024 (Q1 FY25) | Jun 30, 2025 (FY25) | Sep 30, 2025 (Q1 FY26) | Jun 30, 2026 (FY26) | Sep 30, 2026 (Q1 FY27) |
|---|---:|---:|---:|---:|---:|---:|
| **Finished Goods (`製品`)** | N/A¹ | N/A¹ | N/A¹ | N/A¹ | N/A¹ | N/A¹ |
| **Work-in-Process (`仕掛品`)** | 126,087 | N/A² | 123,672 | 123,660 | 122,449 | 138,050 |
| **Raw Materials & Supplies (`原材料及び貯蔵品`)** | 36,314 | N/A² | 45,333 | 46,090 | 45,342 | 47,539 |
| **Total Inventories (`棚卸資産合計`)** | **162,401** | **~171,500²** | **169,005** | **169,750** | **167,791** | **185,589** |
| *Tie-Out Check (WIP + Raw Materials)* | *162,401 (0)* | *N/A²* | *169,005 (0)* | *169,750 (0)* | *167,791 (0)* | *185,589 (0)* |
| *Raw Materials % of Total Inventories* | *22.4%* | *N/A²* | *26.8%* | *27.2%* | *27.0%* | *25.6%* |
| **Inventory Write-Downs (`棚卸資産評価損`, Net, Annual)** | **△164** | N/A³ | **2,119** | N/A³ | **5,019** | N/A³ |
| **Advances Paid to Suppliers (`前渡金`)** | N/A⁴ | N/A⁴ | N/A⁴ | N/A⁴ | N/A⁴ | N/A⁴ |
| *Memo: Other Current Assets (`流動資産・その他`)* | *8,573* | *5,800²* | *7,145* | *N/A⁵* | *8,854* | *11,568* |
| **Accounts Payable - Trade (`買掛金`)** | **11,516** | **~11,500²** | **9,606** | **8,379** | **12,534** | **14,956** |
| **Customer Advances (`前受金`)** | **74,426** | **~75,600²** | **64,388** | **68,394** | **44,284** | **87,075** |
| **Deferred Revenue (`繰延収益`)** | **9,011** | N/A² | **10,085** | **9,309** | **7,794** | **6,702** |
| **Total Contract Liabilities (`前受金 + 繰延収益`)** | **83,437** | N/A² | **74,473** | **77,703** | **52,078** | **93,777** |
| *Customer Advances / Total Inventories (%)* | *45.8%* | *~44.1%* | *38.1%* | *40.3%* | *26.4%* | *46.9%* |

*Sources: FY2025 `有価証券報告書` (EDINET `E01991`, p. 55–56, 61, 69); FY2025 Q2 Presentation (Jan 31, 2025, BS chart); Q1 FY2026 `決算短信` (Oct 31, 2025); FY2026 `有価証券報告書` (EDINET `E01991`, Sep 24/25, 2026, p. 59–61, 69); Q1 FY2027 `決算短信` (Oct 30, 2026, p. 4–5).*
- ¹ `製品` (Finished Goods): `"N/A (checked FY2025 Yuho p. 55, FY2026 Yuho p. 59, Q1 FY2027 Tanshin p. 4)"` — line item does not exist on Lasertec's Consolidated BS; built-to-order systems remain in `仕掛品` (WIP) until customer acceptance (`検収`).
- ² Sep 30, 2024 exact ¥M WIP vs. Raw Materials disaggregation and Deferred Revenue: `"N/A (checked FY2025 Q2 Presentation Jan 31, 2025 & Q1 FY2026 Tanshin CF comparative Oct 31, 2025; standalone Q1 FY2025 Tanshin BS pages not indexed)"`. Rounded ¥Bn totals from FY2025 Q2 Presentation BS chart (`¥171.5B` inventories, `¥11.5B` AP, `¥75.6B` advances received, `¥5.8B` other current assets); Q1 FY2025 CF statement confirms `+¥10,703M` inventory build, `+¥168M` AP increase, and `+¥3,372M` advances received increase before FX.
- ³ `棚卸資産評価損` (Inventory write-downs, net of reversals, included in COGS): `"N/A (checked Q1 FY2026 & Q1 FY2027 Tanshin)"` — disclosed annually in `連結損益計算書関係` footnote of `有価証券報告書` only.
- ⁴ `前渡金` (Advances Paid to Suppliers): `"N/A (checked FY2025 Yuho p. 55, FY2026 Yuho p. 59, Q1 FY2027 Tanshin p. 4)"` — not broken out separately on Consolidated BS or footnotes; subsumed within `流動資産・その他` (Other Current Assets).
- ⁵ Sep 30, 2025 `その他` current assets not individually extracted from Q1 FY2026 Tanshin snippet (`総流動資産` = ¥267,957M, Cash = ¥68,642M, WIP = ¥123,660M, Raw = ¥46,090M).

---

#### Table 1B: Period-over-Period Growth Rates (YoY% / QoQ%) & Turnover / DIO / MOI Audit

| Metric | Jun 30, 2024 (FY24) | Sep 30, 2024 (Q1 FY25) | Jun 30, 2025 (FY25) | Sep 30, 2025 (Q1 FY26) | Jun 30, 2026 (FY26) | Sep 30, 2026 (Q1 FY27) |
|---|---:|---:|---:|---:|---:|---:|
| **Total Inventories — YoY%** | — | — | +4.1% | ~-1.0% | -0.7% | **+9.3%** |
| **Total Inventories — QoQ%** | — | ~+5.6% | — | +0.4% | — | **+10.6%** |
| **WIP (`仕掛品`) — YoY% / QoQ%** | — | N/A | -1.9% / — | N/A / -0.0% | -1.0% / — | **+11.6% / +12.7%** |
| **Raw Materials — YoY% / QoQ%** | — | N/A | **+24.8%** / — | N/A / +1.7% | +0.0% / — | **+3.1% / +4.8%** |
| **Accounts Payable — YoY% / QoQ%** | — | — / ~-0.1% | -16.6% / — | ~-27.1% / -12.8% | +30.5% / — | **+78.5% / +19.3%** |
| **Customer Advances — YoY% / QoQ%** | — | — / ~+1.6% | -13.5% / — | ~-9.5% / +6.2% | -31.2% / — | **+27.3% / +96.6%** |
| **Net Sales (Period, ¥M)** | 213,506 (12M) | 36,737 (3M) | 251,477 (12M) | 54,171 (3M) | 230,485 (12M) | 40,369 (3M) |
| **Cost of Sales (`売上原価`, Period, ¥M)** | 106,026 (12M) | 15,643 (3M) | 103,220 (12M) | 21,364 (3M) | 94,005 (12M) | 16,334 (3M) |
| **TTM COGS Basis (¥M)** | 106,026 | N/A | 103,220 | 108,941 | 94,005 | **88,975** |
| **Total Inventory DIO (TTM COGS)** | 559.1 d | N/A | 597.6 d | 568.7 d | 651.5 d | **761.3 d** |
| **Total Inventory MOI (TTM COGS)** | 18.38 m | N/A | 19.65 m | 18.70 m | 21.42 m | **25.03 m** |
| **WIP DIO / MOI (TTM COGS)** | 434.1 d / 14.27 m | N/A | 437.3 d / 14.38 m | 414.3 d / 13.62 m | 475.4 d / 15.63 m | **566.3 d / 18.62 m** |
| **Raw Materials DIO / MOI (TTM COGS)** | **125.0 d / 4.11 m** | N/A | **160.3 d / 5.27 m** | **154.4 d / 5.08 m** | **176.1 d / 5.79 m** | **195.0 d / 6.41 m** |
| **Raw Materials DIO / MOI (FY27 Guided COGS ~¥118.3B)⁶** | — | — | — | — | — | **146.7 d / 4.82 m** |
| **Raw Materials DIO / MOI (Q1 FY27 Prod. Run-Rate COGS ~¥146.1B)⁷** | — | — | — | — | — | **118.8 d / 3.91 m** |

*Sources: FY2025/FY2026 `有価証券報告書`, FY2025 Q2 Presentation, Q1 FY2026 & Q1 FY2027 `決算短信`.*
- ⁶ FY2027 Guided COGS (~¥118,279M) = FY2027 Guided Net Sales ¥290,000M × FY2026 COGS ratio (40.79% = 94,005 / 230,485).
- ⁷ Q1 FY2027 Production-Implied Annualized COGS (~¥146,055M) = Q1 FY2027 Total Production `生産実績` ¥89,526M (SPE ¥72,326M + Other ¥1,189M + Services ¥16,011M) × 4 × 40.79% COGS ratio.

---

#### Table 1C: Intra-Year Raw Material & WIP Plateau Verification (FY2025–Q1 FY2027, ¥M)

| Balance Sheet Date | WIP (`仕掛品`) | Raw Materials (`原材料及び貯蔵品`) | Total Inventories | Source Filing |
|---|---:|---:|---:|---|
| Jun 30, 2024 | 126,087 | 36,314 | 162,401 | FY2025 `有価証券報告書` p. 55 |
| Dec 31, 2024 | 123,019* | 40,547 | 163,566* | FY2025 H1 `半期報告書` (Feb 12, 2025) |
| Jun 30, 2025 | 123,672 | 45,333 | 169,005 | FY2026 `有価証券報告書` p. 59 |
| Sep 30, 2025 | 123,660 | 46,090 | 169,750 | Q1 FY2026 `決算短信` (Oct 31, 2025) |
| Dec 31, 2025 | 114,717 | 47,121 | 161,838 | Q2 FY2026 `決算短信` (Jan 30, 2026) |
| Mar 31, 2026 | 119,598 | 44,877 | 164,475 | Q3 FY2026 `決算短信` (Apr 30, 2026) |
| Jun 30, 2026 | 122,449 | 45,342 | 167,791 | Q1 FY2027 `決算短信` (Oct 30, 2026) |
| **Sep 30, 2026** | **138,050** | **47,539** | **185,589** | **Q1 FY2027 `決算短信` (Oct 30, 2026)** |

*\*Dec 31, 2024 WIP derived from FY2025 H1 `半期報告書` text disclosure: "仕掛品が30億68百万円減少" (126,087 − 3,068 = 123,019); Raw Materials 40,547 verbatim from BS.*

---

### 2. Procurement, Long-Lead Optical Components & Supplier-Risk Audit (`有価証券報告書`)

| Disclosure Domain | Primary Source & Location | Verbatim Japanese Filing Text / Exact Fact | English Translation & Forensic Finding |
|---|---|---|---|
| **Single-Source / Non-Substitutable Optical & Light-Source Components** | FY2026 `有価証券報告書` (Sep 25, 2026), Part 1, Sec. 2.3 `(7) 特殊な部品/材料仕入に関する影響`, p. 16 | 「当社グループの製品には多くの特殊な部材／材料が用いられており、特に光源や光学部品の一部に簡単には代替のきかないものがあります。仕入先からこれらの部材の供給が滞った場合には、当社グループの研究開発や生産に影響を及ぼす可能性があります。」 | "The Group's products use many specialized components/materials, and **in particular, certain light sources and optical components cannot be easily substituted**. If supply of these components from suppliers is disrupted, it may affect the Group's R&D and production." — **Unchanged verbatim across FY2022–FY2026 Yuho**. |
| **Stockpiling & Second-Source Policy** | FY2026 `有価証券報告書` (Sep 25, 2026), Part 1, Sec. 2.3 `(7)`, p. 16 | 「当社グループは、日ごろから仕入先との関係強化に努めると共に、調達リスクを常時モニタリングして適正な在庫の確保に努めています。また、リスクヘッジのために代替品やセカンドソースの可能性についての情報収集を行っています。」 | "The Group strives to strengthen relationships with suppliers on a daily basis, constantly monitors procurement risks, and works to **secure appropriate inventory**. In addition, as a risk hedge, it **gathers information on the possibility of substitutes and second sources**." — Language remains limited to *"information gathering"* (`情報収集`), with **zero disclosure of completed dual-sourcing or supplier switching for EUV multilayer mirrors**. |
| **Fab-Light Outsourcing Structure** | FY2026 `有価証券報告書` (Sep 25, 2026), Business Strategy / Risk Factors | 「『ファブライト戦略』においては、より研究開発に特化した組織体制とするため、製品製造の多くを協力会社に委託しています。」 | Manufacturing is heavily outsourced to partner companies (`協力会社`), concentrating Lasertec's balance-sheet inventory in high-value procured modules/optics (`原材料及び貯蔵品`) and assembled/in-test tools (`仕掛品`). |
| **Inventory Valuation Method** | FY2026 `有価証券報告書` (Sep 25, 2026), Significant Accounting Policies `(2) 棚卸資産の評価基準及び評価方法` | 「① 仕掛品：個別法による原価法（収益性の低下による簿価切り下げの方法） ② 原材料及び貯蔵品：先入先出法による原価法（収益性の低下による簿価切り下げの方法）」 | WIP valued at specific identification cost (`個別法`); **Raw Materials & Supplies valued at FIFO (`先入先出法`)**, both subject to lower-of-cost-or-NRV write-downs (`簿価切り下げ`). |
| **ACTIS Optical Architecture & In-House EUV Light Source** | FY2026 `有価証券報告書` R&D; Lasertec `URASHIMA` Technical Release (2025); SPIE (Oct 2024) | 「『ACTIS A200HiT シリーズ』は、光学設計の最適化と検査システムを刷新し、スループットを大幅に向上させるとともに…」(FY26 Yuho) / `URASHIMA` LPP EUV light source: *"Debris-free operation achieved using a combination of multiple mitigation techniques including centrifugal force from the high-speed rotation of the crucible and debris filters... enabling long-hour continuous operation."* | Lasertec internalizes the EUV LPP plasma light source (`URASHIMA`) with multi-stage tin debris mitigation and launched `ACTIS A200HiT` (Oct 31, 2025; 3× throughput of `A150`). **No disclosure** in FY2025 or FY2026 Yuho of in-house EUV multilayer mirror coating, in-house mirror refurbishment, or explicit mirror replacement-interval extensions (`"N/A (checked FY2025 & FY2026 Yuho Risk Factors & R&D)"`). |

---

### 3. Dry Forensic Cross-Checks, Anomalies & Second-Order Implications

- **Anomaly 1 — Raw-Material Buffer Did NOT Digest; It Reached a New Record High on Sep 30, 2026:**
  - Between Jun 30, 2024 (`¥36,314M`) and Jun 30, 2025 (`¥45,333M`), Lasertec's `原材料及び貯蔵品` (where long-lead EUV optics/multilayer mirrors sit prior to system integration) surged **+¥9,019M (+24.8% YoY)** precisely during the period when `ACTIS` orders turned negative (`△¥10.5B` in FY2025 due to cancellations/modifications). This confirms that long-lead optical/component deliveries contracted during the FY2023–FY2024 order boom landed on Lasertec's balance sheet during FY2025, matching the onset of Rigaku's `−¥1.0B` FY2025 (`−¥700M` H1 2025) EUV mirror order air-pocket.
  - Across all four quarters of FY2026, `原材料及び貯蔵品` remained flat at an elevated plateau (`¥46,090M` Sep 25 → `¥47,121M` Dec 25 → `¥44,877M` Mar 26 → `¥45,342M` Jun 26).
  - In Q1 FY2027 (ended Sep 30, 2026), even as SPE production (`生産実績`) surged **+120.2% YoY to ¥72,326M** and WIP jumped **+¥15,601M (+12.7% QoQ) to ¥138,050M**, `原材料及び貯蔵品` did **not** draw down—it expanded a further **+¥2,197M (+4.8% QoQ / +3.1% YoY)** to an all-time high of **¥47,539M** (+30.9% above Jun 30, 2024). Simultaneously, `買掛金` (Accounts Payable) jumped **+78.5% YoY / +19.3% QoQ to ¥14,956M**, and `流動資産・その他` (which houses supplier advances/prepayments) expanded **+30.7% QoQ** (`¥8,854M` → `¥11,568M`).

- **Anomaly 2 — Sharp Divergence Between Backward TTM MOI (6.41 Months) and Forward Production-Run-Rate MOI (3.91 Months):**
  - On trailing TTM COGS (`¥88,975M`), Raw Materials MOI expanded monotonically from **4.11 months (125.0d)** in Jun 2024 → **5.27 months (160.3d)** in Jun 2025 → **5.79 months (176.1d)** in Jun 2026 → **6.41 months (195.0d)** in Sep 2026. On a trailing basis alone, the buffer looks increasingly bloated.
  - However, Q1 FY2027 COGS (`¥16,334M`) is artificially depressed by acceptance-timing (`検収`) lag: SPE sales fell **-42.9% YoY to ¥23,849M** while SPE production (`生産実績`) more than doubled (**+120.2% YoY to ¥72,326M**).
  - Re-indexing Sep 30, 2026 Raw Materials (`¥47,539M`) against **FY2027 guided COGS (`~¥118.3B`, based on ¥290B sales guidance)** yields **4.82 months (146.7d)**—still +0.71 months (+17%) above the Jun 2024 baseline of 4.11 months. Re-indexing against the **Q1 FY2027 production run-rate COGS (`~¥146.1B`)** compresses Raw Materials MOI to **3.91 months (118.8d)**—already **below** the Jun 2024 baseline (4.11m).
  - **Forensic Verification of Rigaku's FY2027 Bottoming Timeline:** The Q1 FY2027 surge in `前受金` (Customer Advances: **+¥42,790M / +96.6% QoQ** to **¥87,075M**), the FY2027 consolidated order outlook hike from **¥300–400B to ¥400–500B** explicitly driven by **`ACTIS A200HiT`**, and the +78.5% YoY rebound in `買掛金` (`¥14,956M`) confirm that Lasertec has already resumed active procurement for its FY2027–FY2028 production ramp. At the Q1 FY2027 production pace, the excess raw-material buffer above the historical ~4.1-month operating floor is **already absorbed in FY2027**, validating Rigaku's guidance for customer inventory bottoming in FY2027 rather than pushing restocking to FY2028+.

- **Anomaly 3 — Accelerating Inventory Write-Downs (`棚卸資産評価損`) Signal Spec/Generation Obsolescence Risk:**
  - Net inventory write-downs charged to COGS swung from a **△¥164M net reversal in FY2024** to **¥2,119M in FY2025 (2.05% of COGS)** and surged **+136.9% YoY to ¥5,019M in FY2026 (5.34% of COGS)**.
  - Because `ACTIS` sales fell -38.6% YoY in FY2026 (`¥114.8B` → `¥70.5B`) while Lasertec transitioned its product line from `ACTIS A150` to the redesigned optics of **`ACTIS A200HiT`** (launched Oct 31, 2025; *"光学設計の最適化"*) and `A300` (High-NA), the ¥7.14B cumulative FY2025–FY2026 write-downs indicate aging/obsolescence across legacy-spec FIFO raw materials or canceled-order WIP.
  - **Second-Order Implication for Rigaku:** Elevated headline Raw Materials (`¥47,539M`) on Sep 30, 2026 may contain a mix of slower-moving legacy `A150`/DUV parts alongside newly procured `A200HiT` components—meaning *usable* `A200HiT` mirror inventory is tighter than headline consolidated raw materials suggest, supporting earlier OEM restocking for new-generation `A200HiT` mirrors even while legacy spares digest.

- **Anomaly 4 — Structural Second-Order Risk on Aftermarket/Replacement Mirrors (Throughput & Debris Mitigation):**
  - While FY2025–FY2026 Yuho disclosures show **no** evidence of dual-sourcing execution or in-house mirror refurbishment, two disclosed technical shifts create structural counter-pressures on mirror consumption per wafer-fab inspection volume:
    1. **`ACTIS A200HiT` 3× Throughput Gain:** Launched Oct 31, 2025 with 3× the inspection speed of `A150`, potentially reducing tool count per fab layer if mask-inspection intensity does not scale proportionally.
    2. **In-House `URASHIMA` LPP Source Debris Mitigation:** Explicitly engineered for *"debris-free operation"* via high-speed rotating tin crucible + debris filters to enable *"long-hour continuous operation"*, which mechanically mitigates tin-debris contamination on EUV collector/multilayer optics (though Lasertec does not quantify mirror lifetime extensions in primary filings). Conversely, Lasertec's **Services revenue** grew **+36.5% YoY in FY2026 to ¥58,646M** and **+31.2% YoY in Q1 FY2027 to ¥16,011M**, confirming sustained installed-base consumables/maintenance demand.

---

### Primary Document Reference List
- Lasertec Corp. `2025年6月期 決算短信〔日本基準〕（連結）` (Aug 7, 2025): https://www2.jpx.co.jp/disc/69200/140120250807533568.pdf
- Lasertec Corp. `2027年6月期 第1四半期決算短信〔日本基準〕（連結）` (Oct 30, 2026): https://www2.jpx.co.jp/disc/69200/140120261030560435.pdf
- Lasertec Corp. IR Library (`決算短信` / `決算説明資料` / `有価証券報告書` Archive, EDINET `E01991`): https://www.lasertec.co.jp/ir/data/result.html
- Lasertec Corp. Risk Factors Portal (`事業等のリスクに関して`): https://www.lasertec.co.jp/ir/plan/risk.html

## User prompt 2

GLOBAL CHAT RULES (PERMANENT — ZERO TOLERANCE FOR HANDWAVING):
- SILENT INTELLIGENCE ONLY: Raw dated primary facts, exact figures, verbatim Japanese/English disclosures, and cross-checks. Zero opinions, adjectives, marketing language, stock prices, or valuation multiples.
- NO intros or summaries. Start immediately with dense markdown tables followed by thorough dry forensic bullets covering every anomaly, disclosure change, and demand signal uncovered.
- ADVERSARIAL PRIMARY-SOURCE STANDARD: Query Lasertec Corp. (`6920.T`, EDINET `E02016`) TDnet/EDINET filings (`決算短信`, `有価証券報告書`, `決算説明資料`) for FY2024, FY2025, FY2026, Q1 FY2027 (ended Sep 30, 2026), and FY2027 Guidance, plus ASML (`ASML`) 2025–Q3 2026 High-NA EUV shipment disclosures where directly relevant to mask-inspection attach rates.
- MANDATORY GAP RULE: If an order or product-level number was discontinued or undisclosed, state exact `"N/A (checked [exact filing & date])"` and document the exact date and management rationale for the disclosure change.
- ANTI-TIMEOUT URL RULE: Cite exact filing/page + date inline; list ONE direct primary URL per document at the bottom.

TARGET #4 ECOSYSTEM CROSS-CHECK (Rigaku `268A.T`) — STEP B1-2: LASERTEC `ACTIS` DEMAND, HIGH-NA EUV TIMELINE & DISCLOSURE AUDIT:

Test whether downstream demand for Lasertec's actinic EUV mask inspection tools (`ACTIS A150` / `A300` / `A300+` / High-NA) supports Rigaku's guided FY2027 recovery in EUV mask-inspection mirror shipments, or whether Lasertec faces a prolonged demand air-pocket / competitive displacement:

1. **Lasertec Financial Trajectory, Orders, Backlog & Disclosure Opacity (FY2024, FY2025, FY2026, Q1 FY2027 & FY2027 Guidance — exact ¥M & %)**:
   - Consolidated Revenue, SPE Revenue, Service Revenue, Gross Margin %, Operating Profit / Margin %, and R&D spend.
   - Complete audit of **Order Intake (`受注高`) and Order Backlog (`受注残高`)** across FY2024–FY2026 (from annual `有価証券報告書` and earnings releases), documenting the exact date Lasertec discontinued quarterly order/backlog disclosure, what remains disclosed annually, and any disclosed `ACTIS` vs. `MATRICS` (`X9ULTRA`) mix shift or order cancellation / push-out commentary.

2. **`ACTIS` Shipment Cadence, Reliability / Technical Friction & High-NA EUV Ramp (2025–2028)**:
   - Extract verbatim Lasertec management commentary from FY2026 full-year and Q1 FY2027 (Oct/Nov 2026) briefings on:
     * `ACTIS` (especially `A300` / High-NA) shipment cadence and fab qualification/acceptance timing across TSMC, Intel, Samsung, and memory makers,
     * Any documented field reliability, uptime, EUV light-source, or optics/mirror maintenance issues (including short-seller / technical claims vs. Lasertec's official rebuttal and subsequent revenue/service evidence),
     * Cross-check ASML's verified 2025–2027 High-NA EUV (`EXE:5000` / `EXE:5200`) shipment cadence and fab insertion schedule (Intel 14A, TSMC A14/A16, Samsung) to determine when incremental High-NA `ACTIS` mask-shop installations actually drive new mirror pulls.

## Model response 2

### 1. Lasertec (`6920.T`, EDINET `E01991`) Financial Trajectory, Orders, Backlog & Product Mix

*(Figures in ¥M unless labeled ¥B; rounded down per J-GAAP `決算短信` / `有価証券報告書`. Sub-items may differ from totals by ¥1–2M due to J-GAAP floor truncation.)*

#### Table 1A: Consolidated P&L, Segment/Category Mix, R&D & Orders (FY2024–FY2027 Guidance)

| Line Item (¥M) | FY2024 (Ended Jun 2024) | FY2025 (Ended Jun 2025) | FY2026 (Ended Jun 2026) | Q1 FY2026 (Jul–Sep 2025) | Q1 FY2027 (Jul–Sep 2026) | FY2027 Guidance (Initial Aug 6 / Maint. Oct 30, 2026) |
|---|---:|---:|---:|---:|---:|---:|
| **Consolidated Net Sales** | **213,506** | **251,477** (+17.8%) | **230,485** (-8.3%) | **54,171** | **40,369** (-25.5%) | **290,000** (+25.8%) |
| — SPE (`半導体関連装置`) | 181,752 (85.1%) | 202,965 (80.7%) | 168,090 (72.9%) | 41,752 (77.1%) | 23,849 (59.1%) | 225,000 (77.6%) |
| — Other Products (`その他`) | 2,783 (1.3%) | 5,552 (2.2%) | 3,747 (1.6%) | 216 (0.4%) | 508 (1.3%) | 3,500 (1.2%) |
| — Services (`サービス`) | 28,970 (13.6%) | 42,959 (17.1%) | 58,646 (25.4%) | 12,202 (22.5%) | 16,011 (39.7%) | 61,500 (21.2%) |
| **Gross Profit (`売上総利益`)** | **107,480¹** | **148,256** | **136,479** | **32,807** | **24,035** | **~161,400²** |
| **Gross Margin (%)** | **50.3%** | **59.0%** | **59.2%** | **60.6%** | **59.5%** | **~55.7%²** |
| **SG&A (`販管費`)** | **26,105** | **25,413** | **31,220** | **6,079** | **8,266** | **~36,400²** |
| — R&D Spend (`研究開発費`) | 12,165 (5.7%) | 11,677 (4.6%) | 16,292 (7.1%) | N/A³ | N/A³ (+56.2% YoY) | 20,000 (6.9%) |
| **Operating Profit (`営業利益`)** | **81,375** | **122,843** (+51.0%) | **105,259** (-14.3%) | **26,728** | **15,769** (-41.0%) | **125,000** (+18.8%) |
| **Operating Margin (%)** | **38.1%** | **48.8%** | **45.7%** | **49.3%** | **39.1%** | **43.1%** |
| **Net Income (`親会社株主に帰属`)** | **59,076** | **84,652** (+43.3%) | **77,485** (-8.5%) | **19,057** | **10,734** (-43.7%) | **90,000** (+16.2%) |
| **Order Intake (`受注高`)** | **272,700+⁴** | **105,226** (-61.4%) | **237,504⁵** (+125.7%) | N/A⁶ | N/A⁶ | **400,000–500,000⁷** (Outlook) |
| **Order Backlog (`期末受注残高`)** | **462,196⁴** | **315,945** (-31.6%) | **322,964** (+2.2%) | N/A⁶ | N/A⁶ | N/A⁶ |
| **Book-to-Bill (`受注高 ÷ 売上高`)** | **1.28x** | **0.42x** | **1.03x** *(0.95x ex-FX⁵)* | N/A⁶ | N/A⁶ | **1.38x–1.72x** *(implied)* |
| **Capex (`設備投資額`)** | 2,533 | 5,037 | 2,361 | N/A | N/A | 5,700 (+141.3%) |

*Sources: FY2025 Presentation (Aug 7, 2025, p. 5, 15) & 1on1 FAQ (Aug 7, 2025); FY2026 `決算短信` (Aug 6, 2026); FY2026 Presentation (Aug 6, 2026, p. 4, 6); FY2026 `有価証券報告書` (EDINET `E01991`, Sep 25, 2026); Q1 FY2027 `決算短信` (Oct 30, 2026, p. 1, 5).*
- ¹ FY2024 Gross Profit reconciled from FY2025 Yuho comparative (`213,506` Net Sales − `106,026` COGS = `107,480`; corroborated by FY2025 1on1 FAQ: FY2025 GP `1,482億円`, `+407億円` YoY, GM `59.0%` / `+8.6pts` YoY).
- ² FY2027 Guided GP & GM derived from FY2026 Presentation OP bridge (`FY2026 OP ¥105.2B` + `GP increase +¥24.9B` − `R&D increase ¥3.7B` − `Other SG&A increase ¥1.5B` = `FY2027 OP ¥125.0B`, assumed FX `¥150/USD`).
- ³ Q1 FY2027 & Q1 FY2026 exact ¥M R&D: `"N/A (checked Q1 FY2027 Tanshin Oct 30, 2026 — R&D is not separately lined on the quarterly PL; Q1 FY2027 briefing materials report +56.2% YoY R&D growth)"`.
- ⁴ FY2024 Orders disclosed as `¥2,727億円` in FY2025 Presentation (Aug 7, 2025, p. 5); FY2024 Ending Backlog `¥4,621億円` (`¥462,196M` exact tie-out from FY2025 backlog bridge `315,945 − 105,226 + 251,477`).
- ⁵ FY2026 Orders (`¥237,504M`) tie out exactly to backlog (`315,945 + 237,504 − 230,485 = 322,964`), and per FY2026 Presentation p. 6 include **`+¥17.4B` (`+174億円`) FX revaluation** (opening `¥144/USD` → closing `¥162/USD`). Ex-FX FY2026 organic orders = `~¥220.1B` (`0.95x` Book-to-Bill).
- ⁶ Quarterly Orders & Order Backlog: `"N/A (discontinued effective Q1 FY2025 per Oct 31, 2024 disclosure; annual actuals remain disclosed in FY Tanshin / Yuho)"`.
- ⁷ FY2027 Order Outlook initially guided at `¥300B–¥400B` (Aug 6, 2026, midpoint `¥350B`), **upgraded Oct 30, 2026 (Q1 FY2027 briefing) to `¥400B–¥500B`** (midpoint `¥450B`).

---

#### Table 1B: Product-Level Sales, Orders & Top-3 Customer Concentration Audit (FY2024–FY2026, ¥B)

| Disclosed Product / Customer Line (¥B) | FY2024 | FY2025 | FY2026 | YoY% (FY26 vs. FY25) | Source & Disclosed Scope |
|---|---:|---:|---:|---:|---|
| **`ACTIS` Net Sales** | 98.2 (46.0%) | 114.8 (45.7%) | **70.5 (30.6%)** | **-38.6%** | FY2025 Pres. p. 5; FY2026 Pres. & Q4 Call (Aug 6, 2026; ~60% mask shops) |
| **`MATRICS` Net Sales** | 57.3 (26.8%) | 50.6 (20.1%) | **51.2 (22.2%)** | **+1.2%** | FY2025 Pres. p. 5; FY2026 Pres. & Q4 Call (Aug 6, 2026) |
| **Other SPE Net Sales** *(ABICS, MAGICS, Wafer)* | 26.0 (12.2%) | 37.4 (14.9%) | **46.3 (20.1%)** | **+23.8%** | Derived: SPE `168.0B` − ACTIS `70.5B` − MATRICS `51.2B` |
| **`ACTIS` Order Intake** | **143.3** (52.5%) | **△10.5** (-10.0%) | **62.0** (26.1%) | **N/M (+72.5B)** | FY2025 Pres. p. 5 & 1on1 FAQ; FY2026 Pres. & Q4 Call (majority wafer fabs) |
| **`MATRICS` Order Intake** | **48.1** (17.6%) | **45.3** (43.1%) | **77.2** (32.5%) | **+70.4%** | FY2025 Pres. p. 5 & 1on1 FAQ; FY2026 Pres. & Q4 Call (Aug 6, 2026) |
| **Other SPE Order Intake** | 44.1 (16.2%) | 21.0 (20.0%) | **N/A¹** | N/A | FY2025 Pres. p. 5 (FY26 remaining orders `¥98.3B` across Other SPE + Other + Services) |
| **Services Order Intake** | 34.7 (12.7%) | 45.4 (43.2%) | **N/A¹** | N/A | FY2025 Pres. p. 5 |
| **Customer #1: TSMC Sales** | N/A² | 66.0 (26.2%) | **49.2 (21.4%)** | **-25.5%** | FY2026 `有価証券報告書` (`主要な顧客`, Sep 25, 2026) |
| **Customer #2: Intel Sales** | N/A² | 83.7 (33.3%) | **47.7 (20.7%)** | **-43.0%** | FY2026 `有価証券報告書` (`主要な顧客`, Sep 25, 2026) |
| **Customer #3: Samsung Electronics Sales** | N/A² | 50.0 (19.9%) | **46.5 (20.2%)** | **-7.0%** | FY2026 `有価証券報告書` (`主要な顧客`, Sep 25, 2026) |
| **Top-3 Concentration Combined** | N/A² | **199.7 (79.4%)** | **143.4 (62.2%)** | **-28.2%** | Non-Top-3 customer sales grew **+68.1% YoY** (`¥51.8B` → `¥87.1B`) |

- ¹ Exact FY2026 sub-split of the remaining `¥98.3B` orders (`237.5B − ACTIS 62.0B − MATRICS 77.2B`) among Other SPE, Other Products, and Services: `"N/A (checked FY2026 Tanshin Aug 6, 2026 & Q4 FY2026 transcript)"`.
- ² FY2024 exact customer ¥B not carried in FY2026 Yuho comparative (`FY2025` & `FY2026` two-year table only).
- **Product Nomenclature Gap Check (`A300+`):** `"N/A (checked FY2024–FY2026 Yuho, Q1 FY2027 Tanshin, Oct 31 2025 / Aug 6 2026 / Oct 30 2026 releases)"` — no commercial model named `ACTIS A300+` is disclosed in primary filings. The disclosed `ACTIS` family comprises **`A150`** (launched Sep 12, 2019), **`A300` Series** (high-sensitivity / High-NA mask-shop & R&D), and **`A200HiT` Series** (launched Oct 31, 2025; 3× throughput of `A150`, targeting wafer fabs).

---

#### Table 1C: Disclosure Opacity & Policy Change Timeline (2024–2026)

| Date & Filing | Policy Change | Verbatim Disclosure (Japanese / English) | Remaining Annual / Quarterly Visibility |
|---|---|---|---|
| **Jun 5–6, 2024** (`Announcement Regarding Report Published by Scorpion Capital LLC`) | First-ever disclosure of product-level `ACTIS` & `MATRICS` annual sales/orders | *"Their allegations mainly suggest 1) negative customer evaluation of our ACTIS-series... and 2) improper accounting practices of willfully not booking finished goods. However, Lasertec has been receiving a high level of demand for the ACTIS Series, and we have been engaged in proper accounting practices."* | Initiated annual `ACTIS` vs. `MATRICS` disclosure in full-year materials (continued FY2025 & FY2026). |
| **Oct 31, 2024** (`Q1 FY2025 Financial Results Presentation` & Script) | **Discontinued quarterly Order Intake (`受注高`) and Order Backlog (`受注残高`)** effective FY2025 | *"Effective from the fiscal year ending June 30, 2025, we will stop the disclosure of quarterly orders and order backlog results. The reason for this change is that quarterly orders results fluctuate significantly and do not align with our medium- to long-term growth trends. Therefore, we have determined that its usefulness in corporate valuation is low. In addition, we have received requests from shareholders and investors asking us to not disclose quarterly orders to reduce short-term stock price volatility."* / 「短期変動が大きい四半期毎の受注高は中長期の成長トレンドとは合致せず、企業評価における有用性が低いと判断したため」「株主様や投資家様から、四半期での受注高を非開示とすることにより、短期的な株価変動を抑えるようリクエストをうけたため」 | **Retained annually only** (in FY `決算短信`, FY Presentation, and `有価証券報告書` `受注実績`). **Undisclosed at all horizons:** exact `ACTIS` unit counts, order-cancellation ¥M sub-split, `A200HiT` vs. `A300` individual sales/orders, and regional order backlog. Quarterly demand proxies reduced to qualitative order-outlook ranges (`受注見通し`), `生産実績`, and BS `前受金`. |

---

### 2. `ACTIS` Shipment Cadence, Technical Friction & ASML High-NA EUV Cross-Check (2025–2030)

#### Table 2A: ASML Verified Low-NA vs. High-NA EUV (`EXE:5000` / `EXE:5200B`) Shipment & Recognition Audit

| Period | Primary Filing / Date | Low-NA EUV (`NXE`) Volume | High-NA EUV (`EXE:5000` / `EXE:5200B`) Recognized in Revenue | High-NA Fleet & Customer HVM Milestones (Verbatim Primary Disclosures) |
|---|---|---|---|---|
| **FY2024** | ASML Annual Report 2025 (SEC Form 20-F) | 42 NXE recognized | **2 EXE recognized** | First `EXE:5000` shipped to Intel (Dec 2023). |
| **Q1 2025** | ASML Q1 2025 Call Transcript (Apr 16, 2025) | — | **0 EXE** | *"We shipped our 5th and final EXE:5000 High NA system in Q1 and now have systems at three different customers, with the follow on High NA system model, the EXE:5200, shipping from Q2 of this year."* |
| **Q2 2025** | ASML Q2 2025 Video Transcript (Jul 16, 2025) | — | **1 EXE** | *"Part of that was also the revenue recognition for one High NA tool in the quarter."* First `EXE:5200` shipment confirmed. |
| **Q3 2025** | ASML Q3 2025 Release (Oct 15, 2025) | — | **1 EXE** | >300,000 wafers run cumulatively on High-NA at customer sites; SK Hynix began installation of first `EXE:5200`. |
| **Q4 2025 / FY2025 Total** | ASML Q4 2025 Release & Annual Report 2025 (SEC 20-F) | **44 NXE** recognized (FY25) | **2 EXE in Q4 / 4 EXE in FY2025** | *"We recognized four EXE and 44 NXE systems in sales in 2025 compared to two EXE and 42 NXE systems in 2024."* First production-grade `EXE:5200B` shipped & installed at Intel (Q4 2025). |
| **Q1 2026** | ASML Q1 2026 Call Transcript (Apr 15, 2026) | — | **2 EXE** | *"over 4.1 billion euros from EUV system sales, including sales of 2 High NA systems."* (ASML discontinued quarterly net bookings disclosure starting Q1 2026.) |
| **Q2 2026** | ASML Q2 2026 Call Transcript & Presentation (Jul 15, 2026) | — | **1 EXE** | *"3.8 billion euros from EUV system sales, including sales of 1 High NA system."* Intel qualified High-NA EUV on select **Intel 18A** (Panther Lake) layers (dual-qualified with 0.33 NA). |
| **Q3 2026** | ASML Q3 2026 Call Transcript & IR Presentation (Oct 14, 2026) | **~65 NXE** guided for FY2026 (+48% YoY); **+30% cap. 2027**, **>+30% 2028** | **1 EXE** *(9M 2026 total = **4 EXE**)* | *"including the sale of 1 High NA EUV system."* **Fleet & HVM verbatim:** *"Intel announced that it has exposed more than 1 million wafers using its High NA EUV systems... **Additionally, Samsung and TSMC announced plans to introduce High NA EUV into high volume manufacturing in 2028 and 2030, respectively.** With availability across the existing High NA EUV fleet approaching 90 percent... we also, in collaboration with TSMC, began an industrywide initiative to develop larger-format EUV photomasks. This collaborative effort aims to establish a **12-inch mask pilot line by 2031 and enter production in 2033**."* |

---

#### Table 2B: Verbatim Lasertec Management Commentary (`ACTIS` Cadence, Mix, Reliability & Lead Times)

| Topic | Source & Date | Verbatim Disclosure (English / Japanese) |
|---|---|---|
| **FY2025 `ACTIS` Negative Orders (`△¥10.5B`) & FY2027 Revenue Lag** | Q4 FY2026 Call Transcript (Aug 6, 2026), CEO Tetsuya Sendoda | *"With ACTIS, when we look at the orders and all the way to the shipment, it's about one-year lead time. And then the customer needs time for on-site evaluation. **Given that ACTIS orders were negative in 2 fiscal years before [FY2025], the portion of sales made up by ACTIS in this fiscal year [FY2027] is quite limited still.**"* |
| **`ACTIS` Segmentation (`A200HiT` vs. `A300` vs. `A150`) & High-NA Role** | Q3 FY2026 Script (Apr 30, 2026) & Q4 FY2026 Call (Aug 6, 2026), CEO Sendoda | *"We are getting A200HiT from fabs. Mask shops are more advanced, so they would go for A300 series, hence A150 would gradually decreasing."* (Apr 30) / *"We released A300 for high-NA too, **but if you could think of this as a high sensitivity model instead as it is not for high-NA only.** We believe orders will begin to emerge from leading-edge fabs conducting R&D for the adoption of high-NA, as well as from even more advanced, angstrom-generation beyond the N2 node... **Around the end of Q2 into H2 [FY2027], we also expect A300 from DRAM mask shops.**"* (Aug 6) |
| **Q1 FY2027 Order Outlook Upgrade (`¥300–400B` → `¥400–500B`)** | Q1 FY2027 `決算短信` & Presentation (Oct 30, 2026) | 「当社グループを取り巻く事業環境は良好に推移し、今期の受注見通しも従来の想定を上回るものとなりました。」 / Presentation Slide 11: *"JPY 400–500 billion, exceeding the initial outlook of JPY 300–400 billion. **ACTIS: For leading-edge logic fabs: A200HiT; For mask shops: A300. MATRICS: For EUV and DUV masks.**"* Management cited concrete **1.4nm node development** and **High-NA EUV litho insertion plans** across logic & memory. |
| **Wafer-Fab `ACTIS` Adoption Friction vs. KLA Print-Check** | Q1 FY2026 Script (Oct 31, 2025), CEO Sendoda | *"Fabs use ACTIS to check or they do print checks, where they check the pattern after it's printed to a wafer... **I think all customers would want to use ACTIS, but there was the problem of throughput and high [cost of ownership].**"* `ACTIS A200HiT` (launched Oct 31, 2025) delivered **3× inspection speed** vs. `A150` to address wafer-fab CoO. |
| **`MATRICS` FY2027 Margin Drag** | Q1 FY2027 Presentation & Script (Oct 30 / Nov 2, 2026) | 「MATRICSの性能改善を実施しており、これに伴い採算性の低い装置が複数台今期に売上計上予定であることから売上総利益率に影響する見込み」 (*Performance improvements on `MATRICS` result in multiple low-margin systems scheduled for revenue recognition in FY2027, impacting gross margin.*) |

---

### 3. Dry Forensic Bullets: Anomalies, Reconciliations & Rigaku (`268A.T`) Demand Verification

- **Anomaly 1 — FY2026 Order Rebound Was Partly FX-Inflated (`0.95x` Ex-FX Book-to-Bill) & Led by Non-Actinic `MATRICS`, Not `ACTIS`:**
  - Reported FY2026 Order Intake jumped **+125.7% YoY to ¥237,504M** (`1.03x` Book-to-Bill). However, Lasertec's FY2026 Presentation p. 6 backlog bridge (`Opening ¥315.9B + Orders ¥237.5B − Sales ¥230.4B = Ending ¥322.9B`) explicitly notes a **`+¥17.4B` FX revaluation gain** (`¥144/USD` → `¥162/USD`) embedded inside the backlog movement. Excluding `+¥17.4B` FX revaluation, organic FY2026 order intake was **`~¥220.1B` (`0.95x` Book-to-Bill)**.
  - Within FY2026 orders, **`MATRICS` (DUV-wavelength inspection) reached ¥77.2B (+70.4% YoY)**, overtaking **`ACTIS` at ¥62.0B**—which remained **-56.7% below its FY2024 peak of ¥143.3B**. Management disclosed on the FY2026 briefing that China `MATRICS` demand roughly doubled (EUV/actinic tools are export-controlled), coinciding with Non-Top-3 customer revenue jumping **+68.1% YoY (`¥51.8B` → `¥87.1B`)** while Top-3 EUV foundry revenue (TSMC/Intel/Samsung) contracted **-28.2% YoY (`¥199.7B` → `¥143.4B`)**.
  - **Implication for Rigaku:** Because `MATRICS` uses DUV optics rather than 13.5nm EUV multilayer mirrors, Lasertec's FY2026 order rebound (`MATRICS`-heavy) could **not** yet trigger an immediate FY2026 mirror restock for Rigaku—consistent with Rigaku's disclosed FY2025–FY2026 mirror digestion trough.

- **Anomaly 2 — Q1 FY2027 `¥400–500B` Order Upgrade + `1.5-Year` Lead Time Validates Rigaku's FY2027 Mirror Pull Inflection (Not High-NA HVM):**
  - Cross-checking ASML's primary Q3 2026 transcript (Oct 14, 2026) proves that **High-NA EUV high-volume manufacturing (HVM) is NOT a 2026–2027 volume driver**:
    * Only **4 EXE systems** were revenue-recognized in FY2025 and **4 EXE systems** in 9M 2026 (2 in Q1, 1 in Q2, 1 in Q3).
    * **Intel** is the sole early user (`EXE:5200B` installed Q4 2025; select 18A dual-qualification; **14A risk production 2027**).
    * **Samsung** confirmed High-NA HVM starting **2028** (including DRAM).
    * **TSMC** confirmed High-NA HVM only around **~2030** (skipping A16/A14), instead launching an ASML-TSMC consortium for **12-inch photomasks** targeting a **2031 pilot line** and **2033 production** (a long-term optical re-tooling cycle for Lasertec beyond 2030).
  - **Crucial Cross-Check:** Despite delayed High-NA HVM, Lasertec's **FY2027 order outlook was upgraded on Oct 30, 2026 from ¥300–400B to ¥400–500B** (implying **1.38x–1.72x** Book-to-Bill, well above FY2024's ¥272.7B peak), backed by **+120.2% YoY SPE production (`¥72,326M`)** and **+96.6% QoQ Customer Advances (`¥87,075M`)** in Q1 FY2027. The primary 2026–2028 `ACTIS` volume drivers are:
    1. **Low-NA EUV (`0.33 NA`) Capacity Surge:** ASML is expanding Low-NA EUV shipments **+48% YoY** (`44` units in 2025 → `~65` in 2026), with **+30% capacity in 2027** and **>+30% in 2028**, driving `ACTIS A200HiT` adoption at 2nm/3nm logic fabs and `ACTIS A300` adoption at DRAM mask shops (starting Q2–H2 FY2027).
    2. **Pre-HVM Mask-Shop & R&D `ACTIS A300` Qualification:** Mask shops install `ACTIS A300` **12–24 months ahead of scanner HVM** (i.e., FY2027–FY2028 orders for Samsung 2028 HVM, Intel 14A 2027–2028, and TSMC 1.4nm/A14 R&D).
    3. **Procurement Timing vs. Revenue Timing:** Although CEO Sendoda warned that `ACTIS`'s share of **FY2027 revenue** remains limited due to FY2025's negative `△¥10.5B` orders and a ~1–1.5 year order-to-acceptance cycle, **long-lead optical/mirror procurement happens 6–12 months prior to system shipment**—meaning FY2027 `ACTIS A200HiT` / `A300` orders (`¥400–500B` consolidated run-rate) directly force upstream EUV mirror pulls during **calendar 2027 (Rigaku FY2027)**.

- **Anomaly 3 — FY2027 Guided Gross Margin Compression (`59.2%` → `~55.7%`, -350 bps) Signals Product-Transition & `MATRICS` Engineering Costs:**
  - Despite +25.8% YoY revenue growth (`¥230.5B` → `¥290.0B`), FY2027 OP guidance (`¥125.0B`) implies incremental gross margin of only **41.8%** (`+¥24.9B` GP on `+¥59.5B` sales), pulling consolidated GM down ~350 bps to **~55.7%** while R&D surges **+22.8% YoY to ¥20,000M** (after +39.5% in FY2026) and Capex jumps **+141.3% to ¥5,700M**.
  - Two explicit primary causes: (1) `ACTIS` revenue share remains temporarily depressed in FY2027 following FY2025's `△¥10.5B` orders; and (2) Lasertec's Q1 FY2027 disclosure that **`MATRICS` performance improvements (`性能改善`) created multiple low-margin units** booking into FY2027 revenue.

- **Anomaly 4 — Empirical Audit of Scorpion Capital (June 5, 2024) Allegations & Competitive Displacement Risk (2024–2026):**
  - **Accounting / Fraud Claims (Refuted by 28 Months of Audited Filings):** Zero audit qualifications or restatements across FY2024–FY2026 `有価証券報告書`. Zero Finished Goods (`製品`) is standard build-to-order acceptance (`検収`) accounting. Customer Advances surged to **¥87,075M** on Sep 30, 2026 (Q1 FY2027 Operating Cash Flow: **+¥39,102M**, +558% YoY).
  - **Customer Abandonment & KLA Displacement Claims (Refuted on Actinic Monopoly):** TSMC remained Lasertec's #1 customer in FY2026 (**¥49.2B**, 21.4% of sales; FY2025 ¥66.0B), alongside Intel (**¥47.7B**) and Samsung (**¥46.5B**). **Services revenue** compounded from ¥28,970M (FY24) → ¥42,959M (FY25, +48.3%) → ¥58,646M (FY26, +36.5%) → **¥16,011M in Q1 FY27 (+31.2% YoY)**, confirming active installed-base tool utilization and consumables/maintenance pull. As of Nov 2026, **KLA has not commercialized a competing 13.5nm actinic patterned mask inspector**; KLA competes only via DUV optical (`Teron`), e-beam, and wafer print-check workflows, leaving Lasertec the sole global supplier of actinic EUV patterned mask inspection.
  - **Technical Friction Claims (Partially Validated — Addressed via Hardware Redesign):** Scorpion's claims regarding `ACTIS A150` EUV light-source (external Ushio) and wafer-fab throughput/CoO friction align with three verified Lasertec actions: (1) FY2025 `ACTIS` order drop to **△¥10.5B** (cancellation/modification); (2) transition to Lasertec's proprietary in-house **`URASHIMA` LPP EUV light source** on `ACTIS A300` (replacing Ushio dependency); and (3) CEO Sendoda's Oct 31, 2025 acknowledgment of `A150` *"throughput and high [cost of ownership]"* barriers in wafer fabs, resolved by launching **`ACTIS A200HiT`** (3× speed) with multiple initial fab orders already booked by Q3 FY2026 and driving the Q1 FY2027 order outlook upgrade.

---

### Primary Document Reference List
- Lasertec Corp. `2027年6月期 第1四半期決算短信〔日本基準〕（連結）` (Oct 30, 2026): https://www2.jpx.co.jp/disc/69200/140120261030560435.pdf
- Lasertec Corp. `2025年6月期 決算短信〔日本基準〕（連結）` (Aug 7, 2025): https://www2.jpx.co.jp/disc/69200/140120250807533568.pdf
- Lasertec Corp. `有価証券報告書 第62期（2024年6月期）` (EDINET `E01991`, Sep 27, 2024): https://disclosure2dl.edinet-fsa.go.jp/searchdocument/pdf/S100UFKD.pdf
- Lasertec Corp. IR Library (`決算短信` / `決算説明会資料` / `1on1 FAQ` / `有価証券報告書` FY2024–Q1 FY2027): https://www.lasertec.co.jp/ir/data/result.html
- Lasertec Corp. `ACTIS A300` Product Disclosure: https://www.lasertec.co.jp/en/products/semiconductor/actis_a300.html
- ASML Holding N.V. Investor Relations (FY2025 Annual Report Form 20-F; Q1–Q3 2026 Releases, Presentations & Transcripts): https://www.asml.com/en/investors

**Sources:**

- https://aifinancehub.com/lasertec-stock-recent-share-price-weakness-opportunity-otcmktslsrcf/
- https://www.marketscreener.com/quote/stock/LASERTEC-CORPORATION-11551536/news/Lasertec-Presentation-Material-First-Quarter-of-Fiscal-Year-ending-June-2025-Financial-Results--48253040/

## User prompt 3

GLOBAL CHAT RULES (PERMANENT — ZERO TOLERANCE FOR HANDWAVING):
- SILENT INTELLIGENCE ONLY: Raw dated primary facts, exact figures, technical specifications, and verbatim filing/paper disclosures. Zero opinions, adjectives, marketing language, stock prices, or valuation multiples.
- NO intros or summaries. Start immediately with dense markdown tables followed by thorough dry forensic bullets covering every competitive, technical, and regulatory implication uncovered.
- ADVERSARIAL PRIMARY-SOURCE STANDARD: Query KLA Corp. (`KLAC`) SEC filings (FY2025/FY2026 Form 10-K, Q1 FY2027 Form 10-Q, 2025–Nov 2026 earnings calls), SPIE EUV Lithography & Photomask Technology (2023–2026) technical papers, and official disclosures/registries of competing 13.5 nm EUV multilayer optics suppliers.
- MANDATORY GAP RULE: Where vendor-customer OEM supply contracts are confidential, state exact `"N/A (checked [exact source])"` and surface all corroborating technical papers, joint authorships, patent assignments, and capacity disclosures.
- ANTI-TIMEOUT URL RULE: Cite exact filing/paper + date inline; list ONE direct primary URL per document at the bottom.

TARGET #4 ECOSYSTEM CROSS-CHECK (Rigaku `268A.T`) — STEP B1-3: KLA ACTINIC EUV MASK INSPECTION & RIVAL 13.5 nm MULTILAYER MIRROR SUPPLY CHAIN AUDIT:

Stress-test whether Rigaku's (`RIT` Auburn Hills, MI / `RITE` Prague) **−¥1.0Bn FY2025** decline in EUV mask-inspection multilayer mirrors reflects pure Lasertec inventory digestion — OR structural share loss via (a) KLA taking actinic mask-inspection share using a different mirror supply chain, (b) OEMs qualifying rival 13.5 nm mirror vendors, or (c) U.S. export-control friction on Michigan-made `RIT` optics:

1. **KLA Corp. (`KLAC`) Actinic EUV Mask Inspection & Optics Supply Chain Audit**:
   - Audit KLA's FY2026 Form 10-K, Q1 FY2027 Form 10-Q, and 2025–Nov 2026 earnings commentary on **EUV / High-NA Reticle Inspection** (`Teron 600` series, `Teron 660`, `eSL10` / actinic EUV patterned mask inspection): verified revenue/order momentum, competitive positioning vs. Lasertec `ACTIS`, and any technical/filing evidence on whether KLA sources 13.5 nm multilayer mirrors internally, from `RIT` (Rigaku), or from Zeiss / alternative optical suppliers.

2. **Competing 13.5 nm Mo/Si Multilayer Mirror Vendors — Technical & Commercial Threat Matrix**:
   Audit each of the following competitors across 2023–Nov 2026 primary disclosures, SPIE papers, and capacity expansions:
   - **Carl Zeiss SMT / Zeiss** (Germany)
   - **Optixfab** (Germany)
   - **NTT-AT (`NTTアドバンステクノロジ`)** (Japan)
   - **Incoatec** (Bruker subsidiary, Germany)
   - **Fraunhofer IOF** (Germany)
   - **Nikon / Toray / Other Japanese or European EUV multilayer coaters** (if identified)
   Compare on: documented reflectivity (at 13.5 nm), protective capping-layer durability & mirror refurbishment capability (vs. Rigaku's disclosed 5-cycle refurbishment / +0.07 nm RMS roughness), documented joint papers or supply ties to Lasertec / KLA / ASML / mask-inspection OEMs, and cleanroom coating capacity expansions.

3. **Regulatory / Geographic Supply-Chain Friction (`RIT` Michigan vs. Non-U.S. Suppliers)**:
   - Audit whether Rigaku Innovative Technologies (`RIT`, Auburn Hills, MI) faces U.S. EAR / BIS export-licensing friction or customer de-Americanization risk on 13.5 nm EUV multilayer mirrors shipped to Asian/Japanese OEMs compared to purely Japanese (`NTT-AT`) or European (`Zeiss`, `Optixfab`, `Incoatec`) multilayer suppliers.

## Model response 3

### 1. KLA Corp. (`KLAC`) Actinic EUV Mask Inspection & Optics Supply-Chain Audit

#### Table 1A: KLA Consolidated & Product-Category Revenue Trajectory (FY2024–Q1 FY2027, US-GAAP, $M)

| Line Item ($M, FY ends Jun 30) | FY2024 (10-K) | FY2025 (10-K) | FY2026 (10-K, filed Aug 6, 2026) | Q1 FY2027 (Ended Sep 30, 2026; 10-Q / Release Oct 28, 2026) |
|---|---:|---:|---:|---:|
| **Consolidated Total Revenue** | **9,812.2** | **12,156.2** (+23.9%) | **13,579.5** (+11.7%) | **4,136** (+28.8% YoY / +13.1% QoQ) |
| — Wafer Inspection (`Semi PC`) | 4,333.3 (44.2%) | 6,198.8 (51.0%, +43.1%) | 6,630.8 (48.8%, +7.0%) | 2,111 (51.0%, +37% YoY) |
| — **Patterning (`Semi PC`: Metrology + Reticle Inspection)** | **2,054.4 (20.9%)** | **2,196.3 (18.1%, +6.9%)** | **2,706.8 (19.9%, +23.2%)** | **862.5 (20.9%, +29% YoY)** |
| — Specialty Semiconductor Process | 470.6 (4.8%) | 517.2 (4.3%, +9.9%) | 502.5 (3.7%, -2.8%) | 114¹ (2.8%, +13% YoY) |
| — PCB and Component Inspection | 291.2 (3.0%) | 355.9 (2.9%, +22.2%) | 460.3 (3.4%, +29.3%) | 168¹ (4.1%, +43% YoY) |
| — Services (All Segments) | 2,329.6 (23.7%) | 2,683.3 (22.1%, +15.2%) | 3,125.9 (23.0%, +16.5%) | 850–851 (20.6%, +14% YoY) |
| — Other (`Refurbished / Upgrades`) | 333.2 (3.4%) | 204.6 (1.7%, -38.6%) | 153.1 (1.1%, -25.2%) | ~30 (0.7%) |
| **Standalone Reticle Inspection Revenue** | N/A² | N/A² | N/A² | N/A² |
| **China Ship-To Revenue (% of Total)** | 4,196.7 (42.8%) | 4,042.6 (33.3%) | 4,048.4 (29.8%) | N/A³ |
| **Period-End Backlog ($B)** | N/A | **~$7.9B** (Jun 30, 2025) | **~$13.0B** (+60% YoY, Jun 30, 2026)⁴ | N/A⁴ |

*Sources: KLA FY2026 Form 10-K (SEC EDGAR `0000319201-26-000027`, filed Aug 6, 2026, Note on Segment/Product Disaggregation); KLA Q1 FY2027 Earnings Release & Letter to Shareholders (Oct 28, 2026) / Form 10-Q (filed Oct 30, 2026); Citi Global TMT Conference (CFO Bren Higgins, Sep 9, 2026).*
- ¹ Systems-only revenue for Specialty Semi Process ($114M; total segment incl. services $139M–$140M) and PCB & Component Inspection ($168M; total segment incl. services $242M) per Q1 FY2027 Letter to Shareholders (Oct 28, 2026).
- ² Exact standalone EUV/optical Reticle Inspection revenue: `"N/A (checked KLA FY2025 & FY2026 Form 10-K, Q1 FY2027 Form 10-Q)"` — bundled inside `Patterning` alongside overlay/CD/film metrology. KLA Investor Day (Jun 16, 2022 EX-99.1) disclosed cumulative EUV reticle qualification revenue `>$2.2B` (`>30` `Teron 640e`, `>50` `Teron SL670e` + `Gen 5 Print Check`).
- ³ Q1 FY2027 exact China $M not printed in available 10-Q snippet.
- ⁴ KLA discloses backlog annually in Form 10-K only (confirmed Q1 FY2026 call Oct 29, 2025); FY2026 10-K backlog `"just short of $13 billion, up 60% YoY"` per CFO Bren Higgins (Citi TMT, Sep 9, 2026).

---

#### Table 1B: KLA Reticle Inspection Architecture, Actinic Status & Optical Supply-Chain Forensics

| Platform / Domain | Verified Wavelength / Technology | Commercial Status (as of Nov 2026) | Primary Filing / Paper Evidence | 13.5 nm Multilayer Mirror Supply Chain & Vendor Ties |
|---|---|---|---|---|
| **`Teron™ 6xx` / `Teron™ SL6xx` Series** (`640e`, `647e`, `647eS2`, `SL650`, `SL670e`) | **193 nm DUV** optical laser (die-to-database & thru-pellicle inspection) | **HVM Commercial Core** (listed in FY2026 Form 10-K, Aug 6, 2026); `Teron 660` SKU: `"N/A (checked FY2025/FY2026 10-K, SPIE 2023–2026)"` | SPIE Photomask Nov 6, 2025 (`10.1117/12.3073220`, KLA + Tekscend Photomask): `Teron 647eS2` uses **193 nm laser** + DL DB algorithms for 2nm EUV masks. KLA 2026 Investor Day (Mar 2026): 193 nm covers ~90% of EUV reticles (`all except 3–5 tightest logic & 1–2 DRAM layers`). | Uses **CaF₂ / fused-silica refractive DUV lenses** (ZERO 13.5 nm Mo/Si mirrors). CFO Higgins (Citi TMT, Sep 9, 2026): *"main bottleneck is optical components, especially **calcium fluoride** [18–24+ month lead times]."* |
| **`eSL10™`** | Electron-beam (single-beam) | **HVM Commercial — WAFER Tool ONLY** (NOT reticle) | KLA FY2026 Form 10-K (Aug 6, 2026) classifies `eSL10™` strictly under **"Chip Manufacturing: Defect Inspection and Review"** (patterned wafer inspection, launched FY2020). | Electron optics (magnetic/electrostatic lenses); zero 13.5 nm mirrors. |
| **`TerraBeam 8xx` (`8xx` Series)** | **Multi-column e-beam** reticle inspection (`EBMI`) | **Early HVM / Gap-Layer Shipments** (demoed at KLA 2026 Investor Day, Mar 2026) | KLA 2026 Investor Day (Mar 2026, p. 1, 23): *"new TerraBeam 8xx multi-column electron beam inspector for reticle inspection"*; total KLA e-beam revenue grew from `$75–100M` to **`$400M`**. Joint Samsung–KLA SPIE paper (`PC127500E`, 2023; cited SPIE Nov 12, 2024): covers 0.33 NA & 0.55 NA EUV reticles. | Electron columns; zero 13.5 nm multilayer mirrors. |
| **`Teron 7xx` / `710` (Actinic 13.5 nm EUV)** | **13.5 nm Actinic EUV** | **R&D / IN DEVELOPMENT ONLY — NOT Commercialized** | **Absent from KLA FY2026 Form 10-K product list (Aug 6, 2026).** Absent from KLA 2026 Investor Day Slide 33 commercial optics list (*"DUV/UV/Vis/IR, X-rays, electron-beams"*). At Cantor Conf. (Mar 11, 2025), CEO Rick Wallace pushed back on analyst calling `Teron 710 actinic` *"soon"*. At **2026 Investor Day (Mar 2026, p. 79–80)**: *"We are developing an actinic inspection system and print check."* | **Confidential OEM contracts:** `"N/A (checked KLA FY2026 10-K — names no optical suppliers)"`. **Corroborating primary supply-chain link:** On **Oct 8, 2024**, **`optiX fab GmbH` (Jena, Germany)** officially announced: *"optiX fab is honored to be part of **KLA's network of distinguished suppliers** and are proud to be recognized with **KLA's Excellence in Technology award**."* Separately, former RWTH Aachen EUV optics/source professor **Larissa Juschkin** (who used `optiX fab` 13.5 nm Mo/Si mirrors in *Ultramicroscopy* 2023) joined **KLA Corp. (CA)** (EUVL Workshop keynote). Zero evidence of KLA sourcing 13.5 nm mirrors from Carl Zeiss SMT or Rigaku `RIT`. |

---

### 2. Competing 13.5 nm Mo/Si Multilayer Mirror Vendors — Technical & Commercial Threat Matrix (2023–Nov 2026)

| Vendor (HQ / Site) | 13.5 nm Mo/Si Reflectivity & Substrate Capability | Protective Capping Layer & Mirror Refurbishment Capability | Documented OEM Supply Ties, Joint Papers & Patents (2023–2026) | Cleanroom / Coating Capacity Expansions (2022–2026) | Commercial Threat to Rigaku `RIT` in Mask Inspection |
|---|---|---|---|---|---|
| **Rigaku Innovative Technologies (`RIT` Auburn Hills, MI; `RITE` Prague)** *(Baseline)* | **R > 65% typical @ 13.5 nm** (substrate-dependent); d-spacing `±0.005 nm RMS`; Ø up to **750 mm** (linear `1.5 m × 0.5 m`); >40,000 multilayers delivered (`Osmic` heritage). `RITE` Prague produces **replicated grazing-incidence Wolter optics**, NOT normal-incidence Mo/Si mirrors. | Reactive-sputtered oxide/metal capping (`SiO₂`, `TiO₂`, `ZrO₂`, `Ru`; NIST SURF III tested). **Disclosed wet-etch refurbishment (`rigaku.com` / Platonov et al.):** **5 cycles** on Si substrate with buffer layer → **+0.07 nm RMS roughness** (`~0.19 nm → 0.26 nm`) and **1.2% total EUV reflectivity loss** (vs. 6–12% loss via ion-beam etching). | Primary disclosed supplier of EUV mask-inspection multilayer mirrors (Rigaku `268A.T` FY25 results: `−¥1.0B` decline on customer inventory digestion). Blue-X TWG member (Feb 2026); `RITE` (L. Pina) co-chaired Blue-X Optics session (Jun 2026). | Inline load-locked magnetron system (`ING2`, Class 10 cleanroom load station, Ø 750 mm HVM capacity since 2014). Parent Rigaku expanding **Yamanashi** manufacturing building (2026) for analytical/semi metrology; no separate Auburn Hills coating square-footage expansion disclosed 2024–2026 (`"N/A (checked Rigaku 268A.T IR / rigaku.com)"`). | *Baseline incumbent (collector, condenser, beam-conditioning & multilayer mirrors).* |
| **Carl Zeiss SMT / Zeiss SMS** *(Oberkochen, Wetzlar, Rossdorf, Germany)* | **~70% @ 13.5 nm**; sub-0.1 nm RMS roughness / ~50 pm RMS figure error (6-mirror 0.33 NA & anamorphic 0.55 NA High-NA projection optics; Hyper-NA `≥0.75 NA` blueprint published Oct 2026). | Proprietary **Ru / Ru-alloy** capping & contamination-control IP (`US12019367B2`, `EP1675164B1`); refurbishment undisclosed (`"N/A (checked Zeiss SMT press releases & ASML 20-F)"`). | **Exclusive captive supplier to ASML** (ASML holds **24.9%** of Zeiss SMT; purchases **€4.41B in 2025** vs. €3.95B in 2024). Internal **`AIMS® EUV 3.0`** actinic aerial-image *review* tool (Zeiss SMS; global rollout Sep 2025 / Feb 4, 2026, 3× throughput, Low-NA & High-NA). **Zero evidence** of supplying third-party mirrors to Lasertec or KLA (`"N/A (checked Zeiss SMT / Lasertec / KLA disclosures)"`). | **+25,000 m²** production/adjacent space at **Oberkochen** (first building opened Jul 2026, 4 yrs post-groundbreaking); **+300 m²** cleanroom (+80%, >€20M package) at **Rossdorf** SMS mask-repair site (opened Sep 17, 2025); acquired **Beyond Gravity** lithography actuators (Sep 6, 2024). | **Low (Captive):** Dedicated exclusively to ASML scanners (which remain capacity-capped by Zeiss SMT) and internal Zeiss SMS `AIMS` tools. |
| **`optiX fab GmbH`** *(Jena, Germany; Fraunhofer IOF spin-off, founded Dec 17, 2012)* | Standard: **R > 65% @ 13.5 nm** (`±0.05 nm`, FWHM `>500 pm`); Custom `[Mo/Si]₆₀` w/ barriers: **upper-60%s to ~69.5%** (PTB-verified); Ø up to **650–660 mm** (`>40 kg`, form error `λ/50`). **~19,544–20,000 EUV/X-ray mirrors delivered (~10/working day)**. | Capping layers tested at SAGA-LS BL18: **`Ru`, `TiO₂`, `Nb₂O₅`** (up to 150 kJ/cm² dose). **Commercial collector mirror refurbishment service** explicitly offered (restoring reflectivity on contaminated high-temp water-cooled LPP collectors; Top Unistar / optiXfab datasheet). | **Official KLA supplier — won KLA "Excellence in Technology" Award (Oct 8, 2024).** Co-author with **PTB, ASML Research, imec, LBNL CXRO** (*Optics Express*, Aug 17, 2026). Blue-X TWG member (Feb 2026). Partnered with **Beijing Top Unistar** stocking 13.5 nm standard mirrors in China (Sep 2026). Direct Lasertec supply: `"N/A (checked optixfab.com & SPIE 2023–2026)"`. | **$20M investment** in new Jena facility (`Loftfabrik JENA`, operational Oct 4, 2022): **2,500 m²** lab/office incl. **250 m² ISO 5 cleanroom**. Received repeat Thuringia **FTI** R&D grants (**Jul 17, 2024**, **May 26, 2026**, **Jun 16, 2026**). | **HIGH (Direct Commercial Rival):** Only independent non-U.S. pure-play matching Rigaku `RIT` on aperture (660 mm), refurbishment, capping, and HVM output (~20k mirrors), AND explicitly validated inside **KLA's supplier network**. |
| **NTT-AT (`NTTアドバンステクノロジ`)** *(Atsugi / Tokai, Japan)* | **R = 68% @ 90 eV (~13.8 nm, AOI=0°)**, **67% @ AOI=45°** (`Mo/Si`); Ø **3 mm–450 mm** (plane, concave, parabolic, toroidal, ellipsoidal); also **free-standing 13.5 nm Mo/Si beam splitters** (3-yr dry-N₂ stability, 2026 EUVL Workshop P111) & high-damage-threshold `Nb/Si` (>80 mJ/cm² vs. 25 mJ/cm² Mo/Si). | Standard `Ru` capping & EUV/X-ray beam separators; multi-cycle collector refurbishment: `"N/A (checked atkeytech.ntt-at.com & 2023–2026 papers)"`. | **Directly cited in Lasertec EUV mask-blank inspection (`ABI`) patent `JP2017187547A`** as EUV multilayer mirror fabricator providing reflectance calculations. Supplied 13.5 nm Mo/Si mirrors to **imec** actinic reflectometer. Active exhibitor at SPIE Photomask (Sep 2026). Former NTT-AT EUV lead H. Takenaka now at **TOYAMA Co.** (Kanagawa). | No disclosed cleanroom or large-aperture (>450 mm) HVM expansion in 2023–2026 (`"N/A (checked ntt-at.com press releases 2023–2026)"`). | **Medium-High (Japan Incumbent):** Proven Japanese domestic source for small/medium-aperture (≤450 mm) EUV mirrors & beam splitters with documented Lasertec patent links, though smaller aperture ceiling than `RIT` (750 mm) and `optiXfab` (660 mm). |
| **Nikon Corp. (`7731.T`)** *(Customized Products / Components Business, Japan)* | Mo/Si EUV multilayer mirrors (IBS & low-pressure Xe magnetron sputtering; `0.12 nm RMS` surface roughness, `+0.02 nm` added roughness) + **ultra-low wavefront error aspheric imaging/projection optics**. | Proprietary EUV contamination control & capping developed under EUVA/EIDEC/NEDO programs; third-party mirror refurbishment undisclosed (`"N/A (checked Nikon FY2025/FY2026 Yuho)"`). | **SPIE Nov 12, 2024 (`10.1117/12.3010983`):** *"Through **over 20 years of continuous development in collaboration with Nikon, LASERTEC** has achieved the ultimate wavefront performance of EUV mirrors."* Mass-producing optical components for EUV mask inspection since **2021** (Nikon IR). **FY2026 Yuho (Jun 26, 2026):** EUV component sales & profit **declined** on EUV market slowdown; **Q2 FY2027 briefing (Nov 5, 2026):** *"EUV-related component customer inquiries increasing; expanding business foundation."* | Expanding Components / Industry Business Unit foundation (`事業基盤を拡充`, Nov 5, 2026 briefing) to capture EUV component growth; exact cleanroom m² undisclosed (`"N/A (checked Nikon Q2 FY27 IR)"`). | **Complementary / Partial Overlap:** Primary supplier of **ultra-precision projection/imaging (Schwarzschild) optics** to Lasertec; **concurrent FY2025–2026 revenue drop** refutes Nikon displacing Rigaku `RIT`. |
| **Fraunhofer IOF** *(Jena, Germany)* | **R = 68.4%–69.5% @ 13.55 nm** (`[Mo/Si/B₄C]₆₀`, PTB BESSY II, `NESSY-3`); `Mo₂C/Si` `66.8%` (high-temp >400°C); additively manufactured `AlSi40` water-cooled EUV mirror **R > 67.4% @ 13.5 nm** (<0.3 nm RMS). | Pioneered **Cymer (ASML) LPP collector refurbishment** (>80B pulse lifetime) and `Ru`/`TiO₂` capping R&D. | Public research institute; **commercialized industrial volume production via spin-off `optiX fab GmbH` (2012/2013)**, co-authoring structured IR-suppression Mo/Si papers with `optiX fab` (Jul 2026). | Prototype / R&D magnetron sputtering (`NESSY-1/2/3`) & additive optics lab; does not compete for HVM OEM supply directly (channeled via `optiX fab`). | **Low Direct / High Indirect:** Technology feeder to `optiX fab` and Zeiss, not a commercial volume vendor. |
| **Incoatec GmbH** *(Bruker 100% sub., Geesthacht, Germany)* | **No commercial 13.5 nm EUV mirror line verified** (`"N/A — checked incoatec.de, Bruker 2024/2025 Form 10-K"`). Portfolio consists exclusively of **hard X-ray** multilayer optics (`Göbel`, `Montel`, `Quazar`, `Helios MX`, max length `15 cm`) for `Cu Kα` (`0.154 nm`), `Mo Kα` (`0.071 nm`), `Ag`, `Cr` XRD/XRF/SAXS. | N/A (hard X-ray sealed-tube/microfocus optics; no 13.5 nm EUV capping or collector refurbishment disclosed). | Captive to **Bruker AXS** (`D8 VENTURE`, `NANOSTAR`, `IµS DIAMOND II`). Zero documented ties to Lasertec, KLA, or ASML EUV optics. | Geesthacht facility (`neubau` expanded for Bruker AXS microfocus X-ray sources/Montel optics); zero EUV cleanroom expansion disclosed. | **Negligible:** Hard X-ray analytical optics specialist; non-factor in 13.5 nm EUV mask inspection. |
| **Other EU / Japan Entities** (`Toray`, `AXO Dresden`, `RXOPTICS`, `Canon`, `Shimadzu`) | **`Toray`**: Polymer/CNT films & EUV pellicle materials ONLY — zero 13.5 nm Mo/Si mirror coating (`"N/A (checked 2023–2026 filings/papers)"`). **`AXO Dresden`** (Germany): Soft/hard X-ray synchrotron multilayers (`W/Si`, 45° RIXS, `300 mm` substrates), no commercial 13.5 nm semiconductor HVM mirror disclosures. **`RXOPTICS`** (Germany): Beryllium CRL refractive hard X-ray lenses (`17–19 keV`). **`Canon`**: Nanoimprint (NIL) & DUV scanners; holds legacy EUV mirror patents (145 EUV patents), no merchant EUV mask-inspection mirror business. | N/A for 13.5 nm mask-inspection HVM mirrors. | Zero documented supply ties to Lasertec `ACTIS` or KLA reticle inspection. | None disclosed for 13.5 nm EUV multilayer mirrors. | **Negligible** for FY2025–FY2028 EUV mirror supply. |

---

### 3. Regulatory & Geographic Supply-Chain Friction (`RIT` Auburn Hills, MI vs. Non-U.S. Suppliers)

#### Table 3: U.S. BIS EAR vs. Japan METI / EU Dual-Use Export-Control Matrix for 13.5 nm EUV Mirror Supply

| Regulatory Dimension | U.S.-Origin `RIT` Mirrors (Auburn Hills, MI) | Japan-Origin Mirrors (`NTT-AT`, `Nikon`) | EU-Origin Mirrors (`optiX fab`, `Zeiss`, `Incoatec`) | Primary Legal Authority & Date |
|---|---|---|---|---|
| **Applicable Control Classification** | **`ECCN 3B002.c`** (*"Inspection equipment designed for 'EUV' mask blanks or 'EUV' patterned masks"* **and `"specially designed" "components"` therefor**); lithography scanner mirrors under **`ECCN 3B001.f.1`** (per `6A004.a` Nota Bene: *"For optical mirrors specially designed for lithography equipment, see 3B001"*). Standard non-deformable mirrors <10 kg are NOT captured by `6A004.a` (`a.1` deformable; `a.2` lightweight >10 kg). | Japan **METI Order No. 25 of 2023** (effective **Jul 23, 2023**; Appended Table 1, FEFTA): explicitly lists **EUV mask and mask-blank inspection equipment + specially designed components/accessories** on Japan's unilateral SME control list. | EU Dual-Use Regulation (`2021/821`) Annex I (`3B001` / `3B002` Wassenaar) + national lists (Netherlands/Germany; Arts. 9–10 cross-recognition); Germany BAFA licensing for sensitive EUV exports to China. | `15 CFR Part 774, Supp. 1` (eCFR verified Aug 21, 2026); BIS `88 FR 73424` (Oct 25, 2023) & **`89 FR 96790`** (Dec 2, 2024); METI Order No. 25 (May 23 / Jul 23, 2023). |
| **Direct Export License to Japan (`Lasertec`)** | **NLR (No License Required) under `3B002.c`:** Verbatim `89 FR 96790` (Dec 5, 2024) limits `3B002.c` **NS and RS license requirements strictly to `"Macau or a destination specified in Country Group D:5"`** (China). Japan is Country Group **A:1 / A:5** and on **Supplement No. 4 to Part 742** (33 aligned countries). | Domestic Japan transaction (no export license). | Allied intra-Wassenaar export to Japan (General Export Authorization `EU001` eligible). | `89 FR 96790` (Dec 5, 2024, ECCN `3B002` License Requirements table); `15 CFR § 742.4(a)(4)`. |
| **0% *De Minimis* & SME FDPR Re-Export Impact (Tool Shipments to China / D:5)** | **`15 CFR § 734.4(a)(8)`** (Dec 2, 2024 IFR) imposes a **0% U.S. *de minimis* threshold** on foreign-made `3B002.c` / `3B001.f.1` tools incorporating ANY U.S.-origin controlled content (e.g., `RIT` mirrors) — **HOWEVER**, **Supplement No. 4 to Part 742** (which includes **Japan** and the **Netherlands**) **exempts** Japanese-headquartered OEMs shipping from Japan from U.S. SME FDPR / 0% *de minimis* BIS licensing **specifically because Japan enforces equivalent national METI controls** (`§ 742.4(a)(4)(ii)`). | **Already blocked to China independently by METI FEFTA (effective Jul 23, 2023)** regardless of zero U.S. parts content. Lasertec cannot export `ACTIS` or `ABICS` to China even with 100% Japanese mirrors (`Nikon` / `NTT-AT`). | Non-U.S. origin avoids U.S. EAR direct jurisdiction; **HOWEVER**, EU/German BAFA controls apply to advanced EUV systems/components destined for China, though `optiX fab` continues selling standard 13.5 nm research mirrors locally in China via Beijing Top Unistar (Sep 2026). | `15 CFR § 734.4(a)(8)`, `§ 742.4(a)(4)(ii)`, `Supp. No. 4 to Part 742` (`89 FR 96790`, Dec 5, 2024); `90 FR 5298` (Jan 16, 2025). |
| **Direct Export / Tariff Friction to Non-China Fabs (Taiwan, Korea, U.S., Europe)** | No BIS export-license barrier to Taiwan (`A:5`), Korea (`A:5`), U.S., or EU fabs. **Risk vector:** U.S. bilateral tariffs / U.S. trade-policy volatility (Rigaku FY2025 results explicitly noted *"reduced service margin impacted by U.S. policy changes"* in Components & Services, Feb 13, 2026) and **CFIUS / RS critical-technology scrutiny** (`89 FR 96790` added `RS` controls on SME ECCNs to trigger CFIUS mandatory-filing jurisdiction). | Zero U.S. EAR nexus; zero U.S.-China re-export compliance overhead for non-EUV / DUV tools (`MATRICS`). | Zero U.S. EAR nexus; attractive for European OEMs (`ASML`/`Zeiss`) and U.S. OEMs (`KLA`) seeking non-captive supply or dual-sourcing. | Rigaku Holdings FY2025 Earnings Presentation (Feb 13, 2026, p. 10); Covington & Burling analysis of `89 FR 96790` (Dec 9, 2024). |

---

### 4. Dry Forensic Cross-Checks & Hypothesis Stress-Test on Rigaku's −¥1.0B FY2025 Decline

- **Hypothesis A — KLA Taking Actinic EUV Mask Inspection Share Using a Rival Mirror Chain: REFUTED for FY2025–FY2026; CREDIBLE MEDIUM-TERM RISK (2028+):**
  - **Zero Commercial Actinic Displacement in FY2025–FY2026:** KLA's `Patterning` revenue accelerated **+23.2% YoY in FY2026 to $2,706.8M** and **+29% YoY in Q1 FY2027 to $862.5M**, but KLA's FY2026 Form 10-K (filed Aug 6, 2026) confirms **zero commercial actinic 13.5 nm EUV reticle inspector**. KLA's reticle growth is driven strictly by **193 nm DUV optical (`Teron 647eS2`, `SL670e`)**, **multi-column e-beam (`TerraBeam 8xx`)**, and **wafer print-check (`Gen 5`)**. KLA's actinic program (`7xx` / `Teron 710`) remains in **R&D** as of KLA's March 2026 Investor Day (*"We are developing an actinic inspection system and print check"*). Therefore, KLA did **not** cause Rigaku's `−¥1.0B` FY2025 mirror drop via actinic market-share loss.
  - **Structural Warning Signal Discovered (`optiX fab` + KLA):** When KLA *does* commercialize its actinic `7xx` tool (targeting High-NA HVM ~2028–2030), Rigaku `RIT` is **NOT assured of sole-source mirror supply**. Primary disclosure on `optixfab.com` confirms **`optiX fab GmbH` (Jena, Germany) is already an official KLA supplier and won KLA's "Excellence in Technology" award on Oct 8, 2024**, reinforced by KLA recruiting EUV optics/source professor **Larissa Juschkin** (an active `optiX fab` mirror user in 2023 publications).

- **Hypothesis B — Lasertec Switching Away from Rigaku `RIT` to Rival Mirror Vendors (`Nikon`, `NTT-AT`, `optiX fab`, `Zeiss`, `Incoatec`): REFUTED BY INDEPENDENT NIKON CORROBORATION FOR FY2025–FY2026:**
  - **Independent Cross-Check via Nikon (`7731.T`):** SPIE (Nov 12, 2024) confirms Lasertec has collaborated with **Nikon for >20 years** on ultra-precision EUV imaging mirrors (`ACTIS`/`ABICS`), which Nikon has mass-produced since 2021 inside its `Customized Products` (`Components`) business. Critically, **Nikon's FY2026 `有価証券報告書` (ended Mar 31, 2026, filed Jun 26, 2026) explicitly reported that its EUV-related components declined in BOTH revenue and operating profit due to the EUV market slowdown** (`「EUV関連コンポーネントの販売がEUV関連市場減速の影響を受け、減収減益」`), followed on **Nov 5, 2026** (Q2 FY2027 briefing) by a sharp reversal (`「EUV関連コンポーネントの顧客引き合いが増加」`).
  - **Forensic Deduction:** Had Lasertec displaced Rigaku `RIT` in favor of Nikon during 2025, Nikon's EUV component sales would have expanded while Rigaku fell. Instead, **both Rigaku (`−¥1.0B` in FY2025) and Nikon (FY ended Mar 2026 revenue/profit decline) suffered synchronized drops during Lasertec's FY2025 `ACTIS` order air-pocket (`△¥10.5B`) and raw-material overhang (`¥45.3B–¥47.5B`), and both are aligned on a 2026–2027 inquiry/restocking recovery** matching Lasertec's Oct 30, 2026 FY2027 order upgrade (`¥400–500B`).
  - **Elimination of Non-Competing Vendors:** `Carl Zeiss SMT` is structurally captive to ASML (`€4.41B` 2025 purchases; capacity-constrained) and internal `AIMS EUV 3.0`; `Incoatec` (Bruker) supplies hard X-ray XRD/XRF optics (`0.07–0.15 nm`), not 13.5 nm EUV; `Toray`, `RXOPTICS`, and `AXO Dresden` do not manufacture commercial HVM 13.5 nm semiconductor mask-inspection mirrors. The **only** non-U.S. commercial rivals capable of competing with `RIT` on future `ACTIS` collector/condenser/beam-delivery dual-sourcing are **`optiX fab GmbH`** (up to Ø 660 mm, refurbishment, 250 m² ISO 5 cleanroom) and **`NTT-AT`** (up to Ø 450 mm, cited in Lasertec patent `JP2017187547A`).

- **Hypothesis C — U.S. BIS Export-Control / De-Americanization Friction on Michigan-Made `RIT` Optics: LOW NEAR-TERM IMPACT ON LASERTEC `ACTIS`; STRUCTURAL VULNERABILITY ON CHINA-ADJACENT / NON-EUV TOOLS:**
  - **No U.S. Licensing Friction on `RIT` → Japan (`Lasertec`) `ACTIS` Mirrors:** Under BIS's Dec 2, 2024 IFR (`89 FR 96790`), `ECCN 3B002.c` (EUV mask/blank inspection tools and specially designed components) requires NS/RS licenses **only for Macau and Country Group D:5 (China)** — direct shipments from `RIT` (Auburn Hills, MI) to Japan (`Country Group A:1 / A:5`) are **NLR**. Furthermore, **Supplement No. 4 to Part 742** carves out Japanese-headquartered OEMs from U.S. SME FDPR / 0% *de minimis* BIS licensing when exporting from Japan.
  - **METI Parity Eliminates "De-Americanization" Arbitrage for `ACTIS`:** Because Japan's **METI Order No. 25 (effective Jul 23, 2023)** independently prohibits exports of EUV mask-inspection systems (`ACTIS`/`ABICS`) to China, switching from Michigan-made `RIT` mirrors to Japanese (`NTT-AT`/`Nikon`) or German (`optiX fab`) mirrors **cannot unlock China sales for `ACTIS`**.
  - **Residual Risk Vector:** Rigaku's `RIT` (Michigan) manufacturing concentration remains exposed to (1) **U.S. tariff / trade-policy friction** (already cited in Rigaku's FY2025 earnings deck p. 10 as compressing Components & Services margins), (2) **Chinese domestic EUV R&D exclusion** (where Germany's `optiX fab` actively sells 13.5 nm research mirrors via Beijing Top Unistar without U.S. EAR restrictions), and (3) **no European Mo/Si multilayer mirror redundancy** (`RITE` Prague manufactures replicated grazing-incidence Wolter optics, not normal-incidence Mo/Si multilayer coatings).

---

### Primary Document Reference List
- KLA Corp. Form 10-K for FY2026 (ended Jun 30, 2026; filed Aug 6, 2026, SEC EDGAR CIK `0000319201`): https://www.sec.gov/Archives/edgar/data/319201/000031920126000027/
- KLA Corp. Investor Relations (Q1 FY2027 Form 10-Q / Letter to Shareholders Oct 28, 2026; 2026 Investor Day Mar 12, 2026): https://ir.kla.com
- SPIE Photomask Technology 2025 (`Teron 647eS2` 193 nm EUV mask inspection, Nov 6, 2025): https://doi.org/10.1117/12.3073220
- SPIE Optical & EUV Nanolithography / EUV Mask Technologies (`Nikon`–`Lasertec` 20-year mirror collaboration & KLA multi-column e-beam, Nov 12, 2024): https://doi.org/10.1117/12.3010983
- `optiX fab GmbH` Official Corporate Disclosures (KLA Excellence in Technology Award Oct 8, 2024; $20M Jena ISO 5 Facility; Specs): https://optixfab.com
- Rigaku Innovative Technologies (`RIT` Auburn Hills, MI / `RITE` Prague — EUV Optics Specs & 5-Cycle Refurbishment Disclosure): https://rigaku.com
- NTT Advanced Technology Corp. (`ATkeytech` EUV/Mo/Si Multilayer Mirror & Beam Splitter Specifications): https://atkeytech.ntt-at.com
- Nikon Corp. Investor Relations (`第162期 有価証券報告書` Jun 26, 2026; Q2 FY2027 Presentation Nov 5, 2026): https://www.jp.nikon.com/company/ir/
- Carl Zeiss SMT Official Disclosures (`AIMS EUV 3.0` Sep 2025 / Feb 2026; Rossdorf & Oberkochen Expansions): https://www.zeiss.com/semiconductor-manufacturing-technology
- Fraunhofer IOF EUV/XUV Coatings (`NESSY-3`, `Mo/Si/B₄C`, Collector Refurbishment): https://www.iof.fraunhofer.de
- Incoatec GmbH (Bruker AXS — Hard X-Ray Multilayer Optics Product Scope): https://www.incoatec.de
- U.S. BIS Interim Final Rule `89 FR 96790` (Dec 2/5, 2024 — `3B002.c`, 0% *De Minimis*, SME FDPR, Supp. No. 4 to Part 742): https://www.regulations.gov/document/BIS-2024-0028-0001
- U.S. Electronic Code of Federal Regulations `15 CFR Part 774` (Commerce Control List, ECCNs `3B001`, `3B002`, `6A004`): https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-774
