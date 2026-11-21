# Hybrid bonding in memory and logic: timing read from the equipment side

As of 21 November 2026. Scope: BE Semiconductor Industries (Besi), Applied Materials (with its Besi stake and the joint Kinex line), ASMPT, Kulicke & Soffa, EV Group, SUSS MicroTec, Tokyo Electron (TEL), Hanmi Semiconductor, Hanwha Semitech and SEMES. The other bonder makers found are Shinkawa (Yamaha Robotics), Toray Engineering, Piotech, NAURA's acquired unit, Maxwell, Bondtech, SET and LG Electronics' production-engineering institute; they appear where they have data.

Companion files:
- `evidence.csv`: one row per sourced figure or quote, with URL, date and source class.
- `gaps.md`: what was not found, and where it was looked for.
- `review_packet.md`: the claims this dossier leans on most, how to check them, and known conflicts.

## How to read this file

- **Source classes.** Every row in `evidence.csv` has one.
  - **P**: the company's own document on its own channel: results release, filing, slide deck, annual report, company newsroom, product page, or a transcript the company hosts.
  - **T**: a verbatim call transcript hosted by a third party (Motley Fool, StockAnalysis, TradingKey, Webull/Benzinga, Investing.com).
  - **S**: secondary: trade press, analysts, or a reporter's paraphrase of a company.
- **[I]** marks my inference. Text without [I] reports what a source says.
- **IDs.** Codes like (01-057) point to the row with that `id` in `evidence.csv`. The prefix names the research pass the row came from (listed in `review_packet.md`, section 6).
- **Quotes.** Quotes are verbatim as captured. Korean, Japanese and Chinese quotes are translated, with the original in `evidence.csv` where it was captured. Many pages were read through a summarising fetch tool, so `review_packet.md` lists quotes to spot-check before external use.
- **"Last 6 reported quarters".** These are the six most recent quarterly (or half-year) reports published by 21 Nov 2026:
  - calendar reporters: Q2-2025 to Q3-2026;
  - Applied: fiscal Q3 FY25 to Q4 FY26, the last ending 25 Oct 2026;
  - TEL: FY2026 Q1 (Apr–Jun 2025) to FY2027 Q2 (Jul–Sep 2026);
  - ASMPT and Kulicke & Soffa: see their sections.
- **Rules note.** `research/CLAUDE.md` still contains only a placeholder where its rules block should be, and `research/prior/` is empty. The conventions above were therefore set for this task and are stated so they can be re-mapped.

---

## Summary

1. **Every bonder maker that dated hybrid bonding (HB) in HBM has moved it later. Not one has moved it earlier.**
   - **Besi** (the HB leader): HBM4 in 2025-26 (Jun 2023) → "shifted out one year" (Jun 2024) → first HBM4e 16-high in 2026 (Jun 2025) → "1st production in HBM4e in 2027" (Jun 2026) → on 22 Oct 2026, adoption "over the next two years" with no year, after memory shortages "extended the use of lower stack heights".
   - **Hanmi** (the TCB leader): hybrid-bonder launch H2 2026 (Jul 2024) → end-2027 "for HBM6" (Jul 2025) → HB in HBM "around 2029" at 16-high and above (Jul 2026).
   - **ASMPT**: ready for 12H/16H with TCB (Feb 2024) → HB at "20-high … depending on JEDEC" (Mar 2026) → HB inflection "maybe 2029, 2030 … or even 2031" (Jul 2026) → "HBM layer count stagnation" and memory capex "pushed-out" (Oct 2026).
   - **Kulicke & Soffa**: HB for HBM "a little bit off for now" (Nov 2025) → "a few years away" (May 2026). Its own first hybrid tool slid from "first half of fiscal 2027" (Aug 2026) to "fiscal 2027" for "customer evaluation" (Nov 2026).
   - **SUSS**: "close to mass production" (Nov 2025) → "moving … away from die-to-wafer because runways are extended for TCB" (Mar 2026).
   - **Applied, TEL and EVG** never gave an HBM year.
2. **Memory makers have moved the same way.**
   - SK hynix: HB for 16-high HBM4 was an option in 2024. It then became "essential from 20 layers". Advanced MR-MUF was confirmed for HBM4 (Sep 2025) and for 12-high HBM4E samples (Jun 2026). In Sep 2026 SK hynix set a 90–98% yield bar.
   - Samsung: HB for HBM4 (May 2025) → 16-layer HBM4E (Jul 2025) → "some commercialization … at the HBM4E stage" while 16-stack products are "unnecessary" for now (Jan 2026).
   - Micron calls HB "clearly behind" (Sep 2026).
3. **The standard and the shortage are the main push factors.**
   - JEDEC let HBM4 grow from 720 to 775 µm (agreed Mar 2024, published Apr 2025). Proposals of about 900 µm (HBM4E) and up to 1,000 µm (20-high HBM5) were reported in Mar–Jul 2026; they are not adopted.
   - The 2026 memory shortage kept production on 12-high and lower stacks. NVIDIA was reported in Aug–Oct 2026 to be evaluating 8-high stacks for Rubin Ultra.
4. **The pull is real but sub-scale.**
   - Besi HB orders in 9M-26 more than doubled versus FY25, but they are mostly logic: 12 of 23 HB customers are logic and 3 are memory [I: chart decode].
   - SK hynix bought one Applied–Besi inline system (~KRW 20 bn, reported). Hanwha's second-generation hybrid bonder went to SK hynix for evaluation.
   - Samsung's reported 50-bonder Pyeongtaek line was not finalised as of July 2026.
   - Thermal claims favour HB: >20% lower thermal resistance (Samsung), 35% (SK hynix Hot Chips slide), "up to 30%" (Besi, citing a customer).
5. **TCB is where HBM money is today.**
   - Hanmi 9M-26 revenue was KRW 483 bn with no hybrid orders disclosed.
   - SK hynix split HBM4 TC bonder orders across Hanmi, Hanwha and ASMPT.
   - Applied guides ~90% packaging growth for 2026, "a large portion" HBM-related, which today means TSV, micro-bump and TC flows, not HB [I].
6. **HB is already in volume outside HBM.** Sony image sensors (2016), YMTC NAND (2019), AMD/TSMC SoIC (2022–23), Kioxia CBA NAND (2H24), Intel Foveros Direct (1H26), and Intel's 6 Kinex lines with 30 Besi bonders. DRAM wafer-to-wafer (W2W) is planned for about 2028 (Samsung 10a, reported). HBM is set to be the last large segment to adopt.
7. **Inspection on HB lines is mostly the bonder makers' own, and IR-based.**
   - Kinex integrates in-line overlay metrology. Besi does in-situ IR placement checks. EVG and SUSS have integrated IR overlay and void modules; SUSS's void resolution is only ">500 µm". TEL is developing X-ray overlay at <50 nm.
   - **No bonder maker names KLA, Onto, Camtek, Nova or another third-party inspection vendor as integrated in, or qualified with, its line.**
   - The vendors sell standalone: Onto (Dragonfly G5 at an HBM maker), Camtek, Auros (two IR overlay tools to Samsung for HB, ~KRW 6 bn).
8. **[I] First volume use of HB in HBM: 2H 2028 to end-2029, most likely 2029.** The range rests most on two statements: Besi's of 22 Oct 2026 and Hanmi's of 15 Jul 2026. See section 5.

---

## 1. Orders, revenue, installed base and customers (last 6 reported quarters)

### 1.0 What each company discloses

| Company | HB orders | HB revenue | TCB orders | TCB revenue | Cumulative HB installed / ordered | HB customers | Logic vs memory |
|---|---|---|---|---|---|---|---|
| Besi | Direction only ("more than doubled") | No | Direction, customer count; one order value (May 2025) | No | Cumulative unit **demand** >215 (Q3-26) | 23 (Q3-26) | Customer chart only (slide) |
| Applied | No (orders not reported) | No | n/a | n/a | Intel: 6 Kinex lines, 30 Besi bonders (via Besi) | "multiple" | No |
| ASMPT | First 2 HB tools for HBM ordered 2024; no later count | No | Direction only (e.g. "+50%" 1H25; "record" C2S Q3-26) | Growth only ("about 146%" FY25) | No (TCB: >500 tools) | No | CEO: TCB TAM mostly logic |
| Kulicke & Soffa | None (first HB tool to ship FY27) | None | Not by segment | Management figures per year (> $100 m FY26) | None (TCB: 120 in field, half fluxless) | n/a | "general semi" (logic) led; 1 HBM tool in qualification |
| Hanmi | None disclosed | None | DART per-contract filings (KRW) | Total only | n/a | 0 disclosed | No |
| Hanwha Semitech | None | None | DART filings 2025; press only 2026 | Segment line "semi equipment" | 1st gen (2022) + 2nd gen (2026) at SK hynix, evaluation | 1 (SK hynix) [I] | No |
| SEMES | None | None | None | None (inside "semi/display equipment") | n/a | Samsung only | No |
| SUSS | "single-digit" D2W activity (Nov 2026) | No | n/a (no TCB) | n/a | "two, three systems" sold in 2025 (with inkjet) | Not stated | "not out of the HBM space" |
| TEL | No (no orders reported) | Bonding ~¥30 bn/yr (FY25, FY26), not HB-only | n/a | n/a | No | No | Applications listed |
| EVG (private) | No | No | n/a | n/a | No | No | No |
| Piotech | Repeat orders (qualitative) | CNY 136 m FY2025 (+41.9%) | n/a | n/a | No | No | "advanced memory, advanced logic" |

### 1.1 Besi (calendar quarters, EUR m)

| Quarter (release) | Revenue | Orders | HB wording (P) | TCB / TC Next wording | HB customers; cumulative HB units |
|---|---|---|---|---|---|
| Q2-25 (24 Jul 2025) | 148.1 | 128.0 (−30.9% YoY) | Orders fell "due primarily to lower orders for hybrid bonding and mobile applications"; H1-25 HB revenue "more than doubled versus H1-24" | "significant new orders for TCB Next systems"; 5 May 2025 follow-on order for five TCB Next systems, ~$20 m (01-004) | not stated |
| Q3-25 (23 Oct 2025) | 132.7 | 174.7 | "A push out to Q4-25 of certain anticipated hybrid bonding bookings" (01-008); new foundry HB customer | order from "a fourth customer" (01-010) | not stated; "Intel now has 6 Kinex lines running with 30 HB" (01-009) |
| Q4-25 (19 Feb 2026) | 166.4 | 250.4 | "a significant increase in hybrid bonding orders", described in the Annual Report as "for logic applications" (01-014) | "adoption expanded to five customers for logic, memory and photonics" (01-017) | 18; "cumulative orders grew to 150+ systems" (01-015); logic installed base "over 130 systems" (01-019, T) |
| Q1-26 (23 Apr 2026) | 184.9 | 269.7 | "Unit orders for hybrid bonding systems more than doubled versus Q4-25" (01-022); "repeat orders from a memory customer for HBM"; "two evaluation tools" to "a second memory customer for HBM" (01-023) | "two new orders … adoption increasing to six customers" (01-024) | 20 |
| Q2-26 (23 Jul 2026) | 249.9 | 292.9 | HB orders "from two repeat customers and one new hyperscaler customer" (01-028) | "increased revenue and customer adoption" | 21 (01-027) |
| Q3-26 (22 Oct 2026) | 283.4 | 342.6 | "Year to date, hybrid bonding orders have more than doubled versus fiscal 2025" (01-032); orders "for logic, co-packaged optics and memory"; "orders for both hybrid bonding and TC Next systems from a leading memory customer" (01-034) | "seven customers" (01-035, T) | 23; "total cumulative unit demand exceeded 215 systems" (01-033) |

Revenue and orders: (01-001, 01-002, 01-006, 01-007, 01-012, 01-013, 01-020, 01-021, 01-025, 01-026, 01-030, 01-031).

- **HB customers by segment.** Read from the Nov 2026 deck chart (01-036; label decoding is [I]):

  | Segment | 2024 | 2025 | 2026 YTD |
  |---|---|---|---|
  | Logic | 8 | 9 | 12 |
  | Memory | 3 | 3 | 3 |
  | Photonics | 1 | 3 | 4 |
  | R&D | 3 | 3 | 4 |

  The same slide: "Customer mix skewed to logic currently via two leading customers".
- **Units.** Besi does not disclose HB units per quarter. Blickman, 23 Jul 2026: "No, we haven't disclosed units." (07-003) The cumulative figure went from 150+ (end-2025) to >215 (Q3-26). [I] That implies roughly 65 or more units booked in 9M-26; both figures are lower bounds.
- **Count conflicts.** Besi's own counts disagree:
  - HB customers at end-2025: 18 in the Q4-25 release, versus "15 at year end 2025" in the Q2-26 release.
  - TC Next customers: 6 (Apr 2026), 5 (Jun 2026 slide), 7 (Oct 2026 call).
- **AI share.** AI was about 50% of FY25 orders and about 60% of H1-26 system orders (01-018, 01-029).

### 1.2 Applied Materials (fiscal quarters, USD m)

Applied does not report orders or backlog (01-085 to 01-097).

| Fiscal quarter (release) | Revenue | Semi Systems mix: foundry-logic / DRAM / flash | Packaging, HBM and HB disclosure |
|---|---|---|---|
| Q3 FY25 (14 Aug 2025) | 7,302 | 69 / 22 / 9 | Packaging "on track to more than double to greater than $3,000,000,000 over the next few years" (01-086, T) |
| Q4 FY25 (13 Nov 2025) | 6,800 | 65 / 29 / 6 | Packaging "about $1.5 billion today" (01-088, T); HBM in FY25 "pretty close to flat" |
| Q1 FY26 (12 Feb 2026) | 7,012 | 62 / 34 / 4 | Advanced packaging "one of our highest growth businesses this year" |
| Q2 FY26 (14 May 2026) | 7,910 | 67 / 29 / 4 | Packaging to grow "more than 50% in calendar 2026" (01-093, T) |
| Q3 FY26 (13 Aug 2026) | 9,115 | 67 / 26 / 7 | ">70%" (01-095, T); new packaging tools incl. Opta Quad CMP "particularly critical for hybrid bonding" (01-096) |
| Q4 FY26 (12 Nov 2026) | 10,409 | 58 / 33 / 9 | "around 90% this calendar year"; CFO Hill: "a large portion of that in 2026 is HBM-related packaging" (01-098, T) |

**Hybrid bonding.**
- Feb 2025: "received volume orders from multiple leading-edge customers" for the integrated HB system (01-084, T).
- Kinex, launched 7 Oct 2025, is "being used by multiple leading-edge logic, memory and OSAT customers" (01-083).
- Nov 2026: "we're seeing adoption in high-volume manufacturing in logic … we serve about 80% of the steps for hybrid bonding" (01-099, T).
- No HB units or revenue are given.

**Besi stake.**
- Applied bought 9% on 14 Apr 2025 (01-078).
- On 26 Oct 2026 it agreed an accelerated share purchase to about 20%, "subject to" US HSR clearance; Applied has "no intention" to go beyond about 20% or to seek a board seat (01-079).
- Closing was not confirmed as of 12 Nov 2026.
- Takeover approaches to Besi, with Lam among the suitors, were reported in March 2026 (01-102, S). Besi said it "does not respond to market rumors" (01-074). No offer was made public.
- On 1 Oct 2026 Besi joined Applied's EPIC Center; the scope includes "Scaling of thermo-compression bonding (TCB)" (01-080).
- Applied does not disclose any income or valuation specific to Besi.

### 1.3 ASMPT

ASMPT reports quarterly in HK$, with US$ equivalents. Advanced packaging (AP), TCB and HB sit in the SEMI segment. From Q4-25 the figures are for continuing operations: NEXX was sold on 3 Jun 2026.

| Quarter (release) | Group revenue, US$ m | Group bookings, US$ m | SEMI bookings, US$ m | TCB / HB / memory wording (P unless marked) |
|---|---|---|---|---|
| Q2-25 (23 Jul 2025) | 436.1 | 481.6 | 212.5 | "TCB 1H 2025 orders were up 50% YoY" (02-007); "surpassing 500 TCB tools worldwide" (02-008); HBM3E 12H in HVM at "the leading HBM customer" (02-009); second-generation HB tool to ship "to an HBM customer in Q3" |
| Q3-25 (28 Oct 2025) | 468.0 | 462.5 | 207.8 | "TCB orders were up QoQ but remained at a lower level"; HBM4 12H TCB "first to secure orders from multiple HBM players" (02-015); fluxless AOR "superior scalability for HBM 16H and above" (02-016) |
| Q4-25 (4 Mar 2026) | 508.9 | 499.7 | 253.3 | FY25 AP revenue US$532.1 m, 30% of group (02-021); "Record TCB revenue growth about 146% YoY" (02-022); HBM4 16H: flux-based TCB adopted for sampling, AOR fluxless "under qualification" (02-024); HB: "customer buy-offs and shipped more tools in 2025" |
| Q1-26 (22 Apr 2026) | 507.9 | 727.0 | 309.6 | Four chip-to-wafer TCB tools booked from "a leading advanced logic customer" (02-031); a memory player is qualifying AOR "for HBM4 16H" (02-032) |
| Q2-26 (29 Jul 2026) | 630.0 | 903.6 | 428.1 | 1H26 AP US$339.0 m, 30% (02-036); bulk orders for ">50" chip-to-substrate TCB tools from OSATs (02-037); memory tool purchases "dependent on HBM4 product rollout schedules" (02-038); HB "moved to the sampling stage" |
| Q3-26 (28 Oct 2026) | 669.2 | 1,128.0 (record) | 563.3 | "Record TCB C2S orders" (02-048); memory: "larger capability-driven investments have been pushed-out" (02-049); HB "programmes at various stages of sampling, evaluation and qualification" (02-050) |

Revenue and bookings: (02-001, 02-002, 02-004, 02-012 to 02-014, 02-018 to 02-020, 02-029, 02-030, 02-033 to 02-035, 02-045 to 02-047).

- **TCB figures.** ASMPT gives no TCB revenue, bookings or units per quarter.
- **Installed base.** More than 500 TCB tools (mid-2025). The FIREBIRD page says "over 250 sets installed in mass production" (02-061). No HB installed base is given.
- **HB orders.** The first HB orders for HBM were "two of its next generation HB tools" (Jul 2024) (02-058).
- **Customers.** None are named.
- **Logic vs memory.** CEO, Oct 2026 call (T): "the majority of the TCB TAM in the next couple of years would come from logic versus memory, versus HBM" (02-052).
- **Korea proxy [I].** Revenue from Korea, all segments: HK$494.8 m (FY24) → HK$1,155.2 m (FY25) → HK$313.9 m in 1H26 against HK$877.3 m in 1H25 (02-026, 02-039). This fits a 1H25 peak in HBM TCB shipments to Korea and a 2026 pause.
- **SK hynix share (S).** About 50 TC bonder sets are used for SK hynix HBM4, roughly half from ASMPT. SK hynix placed a seven-tool ASMPT order in Nov 2025 (03-097, S).

### 1.4 Kulicke & Soffa

Fiscal years end in early October. K&S reports no bookings by segment. TCB sits in Advanced Solutions.

| Fiscal quarter (results) | Net revenue, US$ m | Advanced Solutions, US$ m | Memory end market, US$ m | TCB / HB wording (T unless marked) |
|---|---|---|---|---|
| FQ3-25 (6 Aug 2025) | 148.4 | 10.8 | 15.5 | "we have eight customers, and they are all in production" (02-064); TCB market ~US$1 bn in 2028, K&S target US$250–300 m (02-065) |
| FQ4-25 (20 Nov 2025) | 177.6 | 16.1 [derived] | 24.4 [derived] | First HBM system to ship in the Dec quarter, "probably 4E" (02-068); HB for HBM "a little bit off for now" (02-069) |
| FQ1-26 (5 Feb 2026) | 199.6 | 17.2 | 16.2 | "We have 120 TCBs in the field, and half of those are fluxless" (02-071); first HBM system shipped to "a large memory customer" (US), in qualification (02-073) |
| FQ2-26 (7 May 2026) | 242.6 | 24.5 | 31.3 | FY26 TCB ">$100 million", growth "at least 70%" (02-076); HB "still a few years away from gaining broad market adoption" (02-075) |
| FQ3-26 (6 Aug 2026) | 330.4 | 29.4 | 34.0 | FY27 TCB "$150 million-$200 million" (02-079); HB tool to a customer "in the first half of fiscal 2027" (02-078) |
| FQ4-26 (18–19 Nov 2026) | 410.3 (P) | 41.6 [derived] | 23.2 [derived] | FY27: more than twice as many TCB systems, install base +50% (02-084); first hybrid system "for a customer evaluation in fiscal 2027" (02-085) |

Revenue rows: (02-063, 02-066, 02-067, 02-070, 02-074, 02-077, 02-080 to 02-082).

- **Full-year figures (P, FY26 10-K).** Advanced Solutions US$112.7 m (FY25: 72.7). Memory end market US$104.7 m (FY25: 53.4). Backlog US$720.3 m (FY25: 245.3) (02-083).
- **TCB revenue (management).** About $64 m (2023), $55 m (2024), about $70 m (FY25), >$100 m (FY26 guide), $150–200 m (FY27 guide).
- **HB.** K&S has shipped no hybrid bonder.
- **Customers.** No HBM customer is named. The one HBM TCB system was "undergoing qualification" in May 2026, and no later status was found.
- **Logic vs memory.** TCB is described as logic-led: "it's general semi that's driving it" (May 2026).

### 1.5 Hanmi Semiconductor (KRW bn; DART filings)

| Quarter | Revenue | Operating profit | Export share [I] | HBM TC-bonder orders filed on DART in the quarter |
|---|---|---|---|---|
| Q2-25 | 180.0 | 86.3 | 77.8% | SK hynix 42.81 ('DUAL TC BONDER GRIFFIN', 16 May 2025) (03-023) |
| Q3-25 | 166.2 | 67.8 | 78.0% | none |
| Q4-25 | 83.0 | 27.6 | 79.1% | SK hynix 1.57 ("HBM equipment", 17 Nov 2025; press says it was packing equipment, unverified) (03-025) |
| Q1-26 | 50.9 | 8.5 | 89.9% | SK hynix 9.65 ('TC BONDER', 14 Jan 2026) (03-026) |
| Q2-26 | 251.2 | 130.3 | 72.8% | SK hynix 44.20 ("HBM4 … 'TC BONDER 4.5 GRIFFIN'", 8 Jun 2026) (03-027) |
| Q3-26 | 181.0 | 90.8 | 84.7% | none (non-HBM orders from UTAC and Samsung Electro-Mechanics) |

Revenue and operating profit: (03-001 to 03-012).

- **Hybrid orders and units.**
  - No hybrid-bonder order has been filed.
  - Hanmi says contracts beyond those filed are omitted because they could expose customer investment information. No Micron order has been filed since April 2024 (03-020). [I] Most export revenue therefore comes from unfiled orders, mainly Micron.
  - Unit installed base: not disclosed. Proxies: about KRW 600 bn cumulative sales to SK hynix over ten years (03-053, S); more than 30 units to Micron in 2024 (03-054, S).
- **Customers.**
  - HBM TC-bonder customers are SK hynix and Micron (S).
  - Samsung Electronics was listed as a customer in the H1-25 and Q3-25 reports. It is absent from FY25 onwards (03-015).
- **Memory vs logic:** not disclosed.
- **Capex.**
  - Plant 7, dedicated to hybrid bonders: KRW 28.5 bn; DART completion date 30 Nov 2026 (03-030), later restated as H1 2027.
  - Plant 8 site: KRW 56 bn (03-031).
- **Market share.** TechInsights puts Hanmi at 71.2% of the global TC-bonder market in Dec 2025, with SEMES at 13.1% and Hanwha at 3.2% (03-096, S). That is all TC bonders, not HBM only.

### 1.6 Hanwha Semitech (unlisted; reported inside Hanwha Vision; KRW bn)

| Quarter | Semitech segment revenue / OP | of which semiconductor equipment | TC-bonder orders |
|---|---|---|---|
| Q2-25 | 128.7 / −0.2 | 25.3 | SK hynix 38.5 (16 May 2025, DART) (03-060); earlier 21.0 + 21.0 in Mar 2025 (03-058, 03-059) |
| Q3-25 | 108.7 / −0.1 | 39.4 | none filed |
| Q4-25 | 135.7 / 0.9 | 41.2 | none filed |
| Q1-26 | 83.1 / −13.7 | 6.6 | SK hynix, "similar size" to Hanmi's 9.65 (press) (03-061, S) |
| Q2-26 | 147.7 / 14.0 | 35.5 | SK hynix HBM4, "similar size" to Hanmi's 44.2 (press) (03-062, S) |
| Q3-26 | 169.8 / 37.3 | 84.8 | none filed. [I] Q3 includes panel-level packaging tools (~KRW 60 bn of PLP orders this year, analyst) (03-072) |

Segment figures: (03-063 to 03-068).

- **Hybrid.**
  - The first-generation hybrid bonder went to SK hynix in 2022 (03-074, S).
  - The second-generation SHB2 Nano (0.1 µm) was delivered to SK hynix around April 2026 for evaluation (03-077, S).
  - No hybrid order is disclosed.
  - A Lam Research hybrid-bonder joint venture was dropped in early 2026 (03-078, S).
- **Customers.** SK hynix is the main customer of the segment (03-070).
- **Corporate.** Hanwha Vision denied a reported sale of Hanwha Semitech on 18 Nov 2026 (03-080).

### 1.7 SEMES (Samsung subsidiary; DART; KRW bn, whole company)

| Quarter | Q2-25 | Q3-25 | Q4-25 [I derived] | Q1-26 | Q2-26 | Q3-26 |
|---|---|---|---|---|---|---|
| Revenue | 567.6 | 571.0 | 794.9 | 596.3 | 740.3 | 807.7 |
| Operating profit | 35.6 | 66.5 | 67.1 | 96.1 | 91.4 | 118.5 |

Sources: (03-081 to 03-086).

- **Breakdown.** SEMES does not break out bonders. Its customers are Samsung entities (03-087).
- **TC bonders.** The DART product table lists the TC bonder SDB-30W but no hybrid bonder. SEMES reports more than KRW 500 bn of HBM TC-bonder sales since 2022 (03-088, S).
- **Hybrid.** A contracted die-to-wafer (D2W) hybrid bonder is under test at Samsung (03-090, S). A W2W hybrid test was reported as positive (03-091, S). SEMES is qualifying a HIWIN stage (03-093, S).

### 1.8 SUSS MicroTec (EUR m)

Hybrid bonders sit in the Advanced Backend Solutions (ABS) segment, alongside temporary bonders/debonders, coaters and imaging.

| Quarter | Group orders | Group sales | ABS orders | ABS sales | ABS order book | Bonder-specific |
|---|---|---|---|---|---|---|
| Q2-25 | 78.7 | 141.7 | 65.8 | 85.5 | 220.3 | Temporary-bonder follow-ups below prior year |
| Q3-25 | 70.0 | 119.0 | 62.4 | 93.8 | 187.1 | "Bonding solutions achieved their highest order volume so far this year" |
| Q4-25 | 117.6 | 117.6 | ≈92.0 [I] | ≈86.7 [I] | 185.4 | FY25 orders "distributed very evenly" across imaging, coating and bonding |
| Q1-26 | 149.3 | 86.5 | 99.7 | 55.7 | 229.8 | ~50% of segment orders were bonding, mainly temporary bonders for HBM (04-020) |
| Q2-26 | 260.7 | 116.2 | 226.5 | 93.2 | 361.7 | "less bonder orders and much more OSAT-related orders" (04-016) |
| Q3-26 | 223.5 | 97.0 | 176.9 | 74.9 | 464.3 | Bonding ~20% of 9M orders (04-007); D2W hybrid: "single-digit activities in terms of order activity" (04-009) |

Restated 2025 comparatives are used where SUSS gave them. Originally reported figures differ slightly; for example, Q2-25 ABS sales were 87.2 as first reported. Sources: (04-001 to 04-038).

- **Hybrid units.** "So we had last year two, three systems we sold" (2025, hybrid and inkjet combined) (04-028). Earlier orders: a 200 mm W2W tool (Q1 2024) and a BRIDG D2W/W2W tool (H1 2024).
- **Installed base:** not disclosed.
- **HBM customers.** Temporary bonders/debonders are at "all 3 major memory makers" (04-031). These are not hybrid bonders.

### 1.9 Tokyo Electron (JPY bn)

| Fiscal quarter | FY26 Q1 | FY26 Q2 | FY26 Q3 | FY26 Q4 | FY27 Q1 | FY27 Q2 |
|---|---|---|---|---|---|---|
| Net sales | 549.5 | 630.0 | 552.0 | 711.8 | 732.3 | 935.0 |

Sources: (04-049, 04-051, 04-056, 04-065, 04-067, 04-069).

- **Orders and bonder revenue.** TEL publishes no orders and no quarterly bonder revenue.
- **Bonding revenue.** About ¥30 bn in FY2025 (Apr 2024–Mar 2025) and again at "a 30-billion-yen scale" in FY2026 (04-070, 04-055).
- **Targets.** More than ¥500 bn cumulative bonder/3D-integration sales by 2030 (04-068). Annual sales above ¥100 bn "within the next one to two years" (May 2026).
- **Wafer-bonder market share (Gartner, via TEL).** 32% in CY2024, 27% in CY2025 (04-060, 04-059).
- **Advanced packaging.** About ¥200 bn revenue in FY2026 (04-057).
- **HB tools.** The W2W Synapse Si is "Moving toward High-Volume Manufacturing with major memory and logic customers" (04-062). D2W is "in development", with 16-high stacking demonstrated on blanket dielectric (04-063).
- **Not found:** installed hybrid units and customer names.

### 1.10 EV Group (private)

EVG publishes no revenue, orders, unit counts or customer counts (see gaps.md). What it does publish:
- production capacity "expanded … by more than 60 percent", driven by "strong demand for EVG's hybrid bonding" (Nov 2023) (04-082);
- "Multiple EVG40 D2W systems have already been installed at customer sites" (Sep 2025) (04-078);
- activation technology "proven in hundreds of installed modules" (04-083).

Reported, but not from EVG: SK hynix's V10 NAND W2W tools are "largely supplied by EVG … and Tokyo Electron" (TrendForce, Dec 2025, S) (07-011).

### 1.11 Piotech (China; CNY m)

| Quarter | Q2-25 | Q3-25 | Q4-25 | Q1-26 | Q2-26 [I] | Q3-26 |
|---|---|---|---|---|---|---|
| Revenue (all products) | 1,245.4 | 2,266.0 | 2,299.0 | 1,112.4 | ≈1,800.4 | 2,307.6 |

- **HB revenue.** CNY 136 m in FY2025 (+41.92%), mainly W2W hybrid, with "multiple units" passing customer verification (04-085).
- **Next-generation tools.** The W2W bonder Dione 300 eX passed customer verification in Q3-26 (04-095). The D2W hybrid bonder Pleione is in verification (04-092).
- **Not disclosed:** orders, units and customers.

### 1.12 Other makers found

TCB and D2W makers in Japan:

- **Shibaura Mechatronics.** Its bonders are for logic and 2.5D, not HBM stacking. It also makes the TFC-6800 D2W hybrid bonder.
  - Flip-chip bonder sales/orders: ¥26.6 bn / ¥27.8 bn in FY25 (Apr 2025–Mar 2026) (02-104); ¥13.9 bn / ¥39.1 bn in 1H FY26 (02-108). Group orders in Q1 FY26 were ¥52.0 bn, up 191% (02-107).
  - TFC-6800: units at "multiple customers" for evaluation. Revenue "planned for FY2027–28", i.e. Apr 2027–Mar 2029 (02-110).
- **Yamaha Robotics (Shinkawa).** Back-end ("SEMI") revenue was ¥34.4 bn (2024) and ¥36.7 bn (2025) (02-093).
  - HBM: "Client evaluations underway for a high-precision model targeting next-generation HBM" (10 Sep 2026) (02-094).
  - Samsung reportedly stopped using Shinkawa TC bonders by about May 2025 (03-094, S). Micron reportedly split TC-bonder supply between Shinkawa and Hanmi (02-099, S).
  - No TCB units or quarterly back-end figures are published.
- **Toray Engineering.** The UC5000 supports "TCB、DAF、Hybrid実装" (TCB, DAF and hybrid mounting) at 0.8 µm (TCB) and 0.2 µm (HB) (02-100). The company publishes no financials.

Other hybrid-bonder makers:
- **NAURA** is buying a Beijing hybrid-bonder start-up for CNY 405 m; the start-up is reported to have "repeat orders" (04-103, S).
- **AMEC** is investing in Qinghe Jingyuan (04-104, S).
- **Maxwell** reports a W2W hybrid bonder at 30 nm @3σ and a follow-on D2W order. This rests on a search summary only.
- **Bondtech** has the HB/CW3000 and HBWS3000 (04-105, S).
- **SET** makes the NEO HB, which is the die bonder inside SUSS's D2W tool.
- **Canon** reportedly plans a 2026 launch; not confirmed.
- **LG Electronics' production-engineering institute** reportedly targets mass production at end-2028; LG called a 2028 date "premature" (03-103, 03-104, S).
- **Lam Research and ASML** are named as entrants in press or by SUSS. No product has been announced.

---

## 2. Management statements on when HBM moves to hybrid bonding

⚑ marks a change in stated timing compared with an earlier statement by the same company. "Later" and "earlier" refer to the HBM generation, stack height or year at which HB enters volume.

### 2.0 Change log

| Company | Earlier statement | Later statement | Direction |
|---|---|---|---|
| Besi | 6 Jun 2023: HB "starting with HBM4", HBM4 "2025-26 … 12 - 16" | 6 Jun 2024: "Memory adoption confirmed but shifted out one year"; first HB "HBM4(E) 16high stacks in 2026" | Later (+1 yr) |
| Besi | 6 Jun 2024: HBM4(E) 16-high in 2026; "Some hybrid bonding adoption expected in HBM4" | 12 Jun 2025: "First hybrid bonded HBM4e 16 high stacks in 2026"; "TC and TC-fluxless will be primary technologies used through HBM4" | Later (HBM4 → HBM4e) |
| Besi | 12 Jun 2025: HBM4e 16-high in 2026 | 23 Apr 2026: "mainstream volume production in 2027. That roadmap stands"; 18 Jun 2026: "1st production in HBM4e in 2027" | Later (+1 yr) |
| Besi | 18 Jun 2026: "First mover is preparing for HVM in 2027" | 22 Oct 2026: adoption "over the next two years", "somewhat delayed", "precise dates … not known by us"; Nov 2026 deck drops the "first mover … HVM in 2027" bullet | Later, undated |
| Besi | Jun 2026 slide: drivers ">16 layers" | Oct–Nov 2026: "not a matter of stack height … 16 or 20 or 12"; ">=12Hi" | Stack-height trigger lowered (pull) while date slipped |
| ASMPT | 28 Feb 2024: TCB "ready for 12H/16H HBM" | 30 Oct 2025 and 4 Mar 2026 calls (S): HB at "20-high", "depending on JEDEC" | Later (16 → 20-high) |
| ASMPT | Mar 2026: HB "kicking in" at 20-high | 28 Jul 2026 (T): inflection "maybe 2029, 2030 … or even 2031"; TCB could extend "into HBM5" if JEDEC goes "beyond 900" | Later, first dated (2029–31) |
| ASMPT | Jul 2026: TCB demand for 16-high | 27–28 Oct 2026: "HBM layer count stagnation"; larger memory investments "pushed-out"; near-term HB demand cited is logic | Later |
| K&S | 5 Feb 2025: own HBM HVM "within 18-24 months" (TCB) | 20 Nov 2025: HB for HBM "a little bit off for now"; 7 May 2026: HB "a few years away" | Later (HB) |
| K&S | 6 Aug 2026: first HB tool to a customer "in the first half of fiscal 2027" | 19 Nov 2026: "first hybrid system for a customer evaluation in fiscal 2027" | Later [I] (window widened; "evaluation") |
| Hanmi | 5 Jul 2024: hybrid bonder launch "H2 2026" | 15 Jul 2025: launch "end-2027", "for HBM6"; HBM4 and HBM5 on TC | Later (+1 yr; to HBM6) |
| Hanmi | Jun–Jul 2025: hybrid plant 7 completion 30 Nov 2026 / H2 2026 | 9 Apr 2026 onward: "H1 2027" | Later |
| Hanmi | H1-25 and Q3-25 reports: HB "expected as the next-generation HBM stacking method" | FY25, Q1-26 and H1-26 reports: hybrid-bonder development "delayed by technical challenges"; wide TC bonder pitched for "20-high and above" | Later |
| Hanmi | Jul 2025: no adoption year | 15 Jul 2026: HB "around 2029" for "16-high and above" mass production | First dated year (2029) |
| Hanmi | H1-26 report: new bonding needed at "20단 이상" (20-high and above) | Q3-26 report (13 Nov 2026): "16단 이상" (16-high and above); "delayed" sentence removed | Threshold lowered (pull, ambiguous: answer offered is wide TC) |
| Hanwha Semitech | 10 Sep 2025: SHB2 Nano "customer evaluation in Q1 next year" | 25 Feb 2026: delivery "in H1" for performance testing; delivered to SK hynix ~Apr 2026 (S) | Slight slip [I] |
| SUSS | 7 Aug 2025: "earliest HBM4e if not HBM5" | 17 Nov 2025: "D2W HB close to mass production" | Earlier (tone) |
| SUSS | 17 Nov 2025: "D2W HB close to mass production" | 30 Mar 2026: "moving a bit sideways, a little bit away from die-to-wafer … because runways are extended for TCB"; 5 Nov 2026: "we don't see a mass adoption … yet" | Later |
| TEL | 31 Oct 2025: "drastic expansion" from ¥30 bn bonder sales | 7 May 2026: FY2026 at "a 30-billion-yen scale"; 4 Nov 2026: growth "from CY2027 onward" | Later (revenue cadence, not HBM timing) [I] |
| Shibaura | 13 May 2026: HB revenue "still some way off" | 5 Nov 2026: revenue "planned for FY2027–28" | Firmed, no slip |
| Applied, EVG, Piotech, SEMES, Yamaha, Toray | No HBM generation or year stated by management | — | No change can be marked |

### 2.1 Besi (CEO Richard Blickman unless stated)

| Date | Venue (class) | Statement | Generation / stack / year | ID |
|---|---|---|---|---|
| 6 Jun 2023 | Capital Markets Day slides (P) | "Hybrid Bonding can be used to stack 16 or more die, starting with HBM4"; HBM4 "2025-26 … 12 - 16 Memory Chips Hybrid Bonding"; "TCB for memory will probably be used to stack up to 12 dies" | HBM4, 2025-26, 12–16 | 01-037, 01-038 |
| 22 Feb 2024 | Q4-23 call (T) | "whether it's Generation 1 or 2, is not yet clear. But if you ask me, I would guess more Generation 2" ⚑ | HBM4 gen 2 | 01-039 |
| 25 Apr 2024 | Q1-24 call (T) | "the current view is HBM4, TCB, early versions using hybrid bonding, and as of HBM5, the world today expects that to be overwhelming hybrid bonding" | HBM4 early versions TCB; HBM5 HB | 01-040 |
| 6 Jun 2024 | Investor Day (P slides; T) | "Memory adoption confirmed but shifted out one year"; "First Hybrid packaged HBM4(E) 16high stacks in 2026"; Wiedner (SVP): "16 will be the tipping point" ⚑ | HBM4(E), 16-high, 2026 | 01-041, 01-043 |
| 24 Oct 2024 | Q3-24 call (T) | "Probably for HBM4, it will only be a very high-end range using hybrid." "Will it be at the high end of four, or will it be only at five?" | HBM4 high end / HBM5 | 01-044 |
| 23 Apr 2025 | Q1-25 release (P); call (T) | Release: "hybrid bonding orders from two leading memory producers for HBM 4 applications". Analyst: HB "will not be used in volume production until 2027"; Blickman: "pretty much how it is presented to us" | Volume 2027 | 01-045, 01-046 |
| 12 Jun 2025 | Investor Day (P slides; T) | "First hybrid bonded HBM4e 16 high stacks in 2026"; "HBM 5: Hybrid bonding only"; "TC and TC-fluxless will be primary technologies used through HBM4" ⚑ | HBM4e 16-high 2026; HBM5 (2028) HB only | 01-048, 01-049 |
| 24 Jul 2025 | Q2-25 call (T) | "We have understood 2026 qualification and mainstream production towards the end, and also certainly in 2027." | Qual 2026, mainstream late 2026–2027 | 01-050 |
| 23 Oct 2025 | Q3-25 call (T) | "a critical evaluation year 2026 … hybrid bonded devices should be available in their program by the end of next year … 2026-2027"; "for HBM4, most will be … in a reflow process TC" | 2026–2027 | 01-051 |
| 18–19 Feb 2026 | Annual Report (P); Q4-25 call (T) | AR: "HBM4 production is anticipated to begin in 2026 with HBM5 production estimated in 2028-2029"; HB "uniquely qualified … at or above 20 devices". Call: "will this move in 2026 or certainly in 2027?" | HBM5 2028–29 | 01-052, 01-053 |
| 23 Apr 2026 | Q1-26 call (T) | "setting up production capabilities towards the end of this year for mainstream volume production in 2027. That roadmap stands" | Mainstream 2027 | 01-054 |
| 18 Jun 2026 | Investor Day (P slides; T) | "Hybrid bonding on track for 1st production in HBM4e in 2027"; "Hybrid adoption in memory estimated to begin in 2027 • Starting with 16-high HBM4e stacks • HBM5 follows next"; "First mover is preparing for HVM in 2027" ⚑ | HBM4e 16-high, 2027 | 01-057, 01-058, 01-059 |
| 23 Jul 2026 | Q2-26 call (T) | "Some are voicing that it may delay. Others are voicing that it is imminent." | Uncertain | 07-002 |
| 22 Oct 2026 | Q3-26 release (P); call (T) | Release: "Severe memory shortages this year have extended the use of lower stack heights in current HBM production beyond prior expectations … We anticipate that hybrid bonding will be adopted in a range of stack heights over the next two years". Call: "The precise dates of when certain applications will hit mainstream volume is not known by us"; "adopting superior technologies has been somewhat delayed" ⚑ | "over the next two years"; no year | 01-063 to 01-066 |
| Nov 2026 | Investor presentation (P) | "First Insertion Point for Hybrid Bonding Anticipated in HBM 4e"; "All leading HBM players have installed Besi's hybrid bonding solutions"; drivers ">=12Hi"; "First mover … HVM in 2027" bullet absent; market slide still "Hybrid adoption in memory estimated to begin in 2027" | HBM4e anticipated | 01-068, 01-069 |

Logic, for comparison:
- Besi says AMD, Intel and Apple are "already in production" and Broadcom and NVIDIA Feynman are on the roadmap (Jun 2026, P).
- On the leading-GPU programme, the analyst summary "qualification … this year, possibly orders next year, and volume … in 2028" was "still more or less" right (22 Oct 2026, T) (01-067).

### 2.2 Applied Materials (CEO Gary Dickerson unless stated)

| Date | Class | Statement | ID |
|---|---|---|---|
| 15 Aug 2024 | T | "If you look even at new DRAM technologies like 4F2 or high-bandwidth memory, you're going to see adoption of hybrid bonding technologies" | 07-007 |
| 13 Feb 2025 | T | Integrated HB system "received volume orders from multiple leading-edge customers" | 01-084 |
| 14 Apr 2025 | P (8-K) | Terry Lee, CVP: the integrated system can take HB "to very high-volume manufacturing over the next several years" | 01-078 |
| 13 Nov 2025 | T | "in HBM, future generations will adopt hybrid bonding" | 01-089 |
| 12 Feb 2026 | T | "the number of dies in the HBM stacks is increasing from 12 today to 16 and then 20 or more in the future" | 01-091 |
| 12 Nov 2026 | T | "we're seeing adoption in high-volume manufacturing in logic … for sure, hybrid bonding will be adopted further in both logic and memory" | 01-099 |

[I] Applied has never named a generation or year for HB in HBM, so no change can be marked. Its rising 2026 packaging guidance (>50% → >70% → ~90%) is HBM-related packaging in general, not HB.

### 2.3 ASMPT (Group CEO Robin Ng to 11 Aug 2026; Bassel Haddad after)

| Date | Class | Statement | Generation / stack / year | ID |
|---|---|---|---|---|
| 28 Feb 2024 | P | TCB "ready for 12H/16H HBM" | 16H on TCB | 02-059 |
| 24 Jul 2024 | P | "won maiden orders for two of its next generation HB tools for HBM applications" | — | 02-058 |
| 26 Feb 2025 | P | AOR fluxless "16H bonded sample within the maximum stack-up height of 775 μm, paving the way for the tool's extension into HBM4" | 16H HBM4 on TCB | 02-055 |
| 23 Jul 2025 | P | "The Group expects HB to co-exist with other packaging technologies, and its adoption will be gradual." | — | 02-010 |
| 28 Oct 2025 | P | AOR gives "superior scalability for HBM 16H and above" | ≥16H on TCB | 02-016 |
| 30 Oct 2025 | S (snippet of call) | "if they have to switch to hybrid bonding, we will be there also to provide competitive solution for hybrid bonding for HBM 20-high" ⚑ | HB at 20-high | 02-017 |
| 4 Mar 2026 | S (inews24 paraphrase) | "TC bonding can handle up to 16-high, but at 20-high hybrid bonding may partially apply, depending on JEDEC standards" (tr.) | 20-high, JEDEC-dependent | 02-027, 02-028, 06-053 |
| 28 Jul 2026 | T | HB inflection "maybe 2029, 2030 kind of timeframe, or even 2031 … we can't really put a definitive timeframe on hybrid bonding yet"; height "could increase from the current 775 micron to beyond 900. If that happens, then TCB use could be extended for HBM packaging beyond HBM4 into HBM5" ⚑ | 2029–2031; HBM5 possibly TCB | 02-040, 02-041 |
| 27–28 Oct 2026 | T; P | Haddad: "HBM layer count stagnation"; "an adjustment to the timing rather than a change in the underlying demand"; HB demand growth "probably in the next 12 to 18 months" from foundry/IDM (logic). Release: "larger capability-driven investments have been pushed-out" ⚑ | Memory later; logic HB 2027–28 | 02-049, 02-051, 02-053 |

### 2.4 Kulicke & Soffa

| Date | Speaker (class) | Statement | ID |
|---|---|---|---|
| 2 May 2024 | Fusen Chen, CEO (T) | "current generation and next generation of HBM is going to be TCB"; Cu-Cu fluxless TCB "could potentially delay higher volume adoption of hybrid bonding" | 02-087, 02-088 |
| 5 Feb 2025 | Fusen Chen (T) | K&S HBM high-volume "probably within 18-24 months" | 02-091 |
| 20 Nov 2025 | Lester Wong, interim CEO (T) | First HBM TCB system, "probably 4E"; "for HBM hybrids, a little bit off for now" | 02-068, 02-069 |
| 5 Feb 2026 | Lester Wong (T) | "fluxless thermo-compression remain a strong alternative to hybrid bonding for the next generation HBM needs" | 02-072 |
| 7 May 2026 | Lester Wong (T) | "hybrid may be still a few years away from gaining broad market adoption" ⚑ | 02-075 |
| 6 Aug 2026 | Lester Wong (T) | "planning to deliver a hybrid bonding tool to a customer in the first half of fiscal 2027" | 02-078 |
| 19 Nov 2026 | Raj Talluri, CEO (T) | "We expect to ship our first hybrid system for a customer evaluation in fiscal 2027"; HB "an additional longer-term growth vector" ⚑ | 02-085 |

### 2.5 Hanmi Semiconductor (Chairman Kwak Dong-shin unless stated)

| Date | Class | Statement | Generation / stack / year | ID |
|---|---|---|---|---|
| 5 Jul 2024 | S (company release) | Hybrid bonder "2026년 하반기 … 출시" (launch in H2 2026) | Tool H2 2026 | 03-032 |
| 15 Jul 2025 | S | "JEDEC에서 … 775μm로 완화하면서 HBM4와 HBM5 모두 한미반도체 TC 본더로 제조가 가능해 고객들이 가격이 두배가 넘는 하이브리드 본더를 선택 하지 않을 것" (with JEDEC at 775 μm, HBM4 and HBM5 can both be made on Hanmi TC bonders, so customers will not choose hybrid bonders costing more than twice as much); "2027년 말 출시를 목표로 HBM6용 하이브리드 본더" (hybrid bonder for HBM6, launch targeted end-2027) ⚑ | HB at HBM6; tool end-2027 | 03-033, 03-034, 03-035 |
| 30 Jul 2025 | S (VP Kim Jeong-young, IR) | Hybrid bonder "2027년 출시" (launch in 2027); fluxless-bonder order already won | Tool 2027 | 03-038, 03-039 |
| 12 Mar 2026 | P (annual report; same text in Q1-26 and H1-26) | "하이브리드본더가 기술적 난제로 개발이 지연됨에 따라 20단 이상의 HBM 적층 시 보다 넓은 HBM칩을 적층할 수 있는 신장비의 필요성" (as hybrid-bonder development is delayed by technical challenges, new tools are needed to stack wider HBM dies at 20-high and above) ⚑ | 20-high on wide TC | 03-043 |
| 9 Apr 2026 | S (company release) | 2nd-gen hybrid prototype "연내" (within the year); hybrid plant "내년 상반기 가동" (operating H1 next year) ⚑ | Plant H1 2027 | 03-044 |
| 15 Jul 2026 | S (written interview, MK) | "하이브리드 본더는 2029년경 예상되는 16단 이상 HBM 양산 시점에 맞춰 적기에 공급" (supply hybrid bonders in time for the mass production of 16-high-and-above HBM expected around 2029) ⚑ | ≥16-high, ~2029 | 03-046 |
| 6 Oct 2026 | S | "2세대 하이브리드 본더 장비는 일정에 차질 없이 개발" (2nd-gen hybrid bonder on schedule); SK hynix and Micron reportedly asked for fast development | — | 03-049, 03-050 |
| 13 Nov 2026 | P (Q3-26 report) | New bonding needed "16단 이상" (16-high and above); "WIDE TC 본더" (wide TC bonder) launch in preparation; HB developed "in parallel"; "delayed" sentence dropped ⚑ | 16-high threshold | 03-051 |

### 2.6 Hanwha Semitech

- **Own tool dates.**
  - 1st-gen hybrid bonder to a customer in 2022 (03-074).
  - SHB2 Nano for "customer evaluation in Q1 next year" (10 Sep 2025) (03-073) → delivery "in H1" (25 Feb 2026) (03-076) → delivered to SK hynix about April 2026 (03-077).
  - All from Korean press (S).
- **Positioning.** HB described in Sep 2025 as essential for "20단 이상" (20-high and above) (S).
- **HBM timing.** No management statement on when HBM moves to HB was found. No change can be marked.

### 2.7 SEMES (and Samsung statements about SEMES tools)

- **SEMES.** TP team leader Choi Byung-gap, Aug 2025 (S): an HBM hybrid bonder with sub-500 nm positioning is in demo evaluation, prepared "HBM4 이후" (for after HBM4) (03-089).
  - An industry source (Feb 2026, S) says SEMES's roadmap assumes HB "HBM4E부터" (from HBM4E) at the customer. The same source says SEMES tools made Samsung's HB HBM4 samples, and that evaluation to volume supply "usually takes about 2 years" (03-090).
- **Samsung, Q4-25 call (29 Jan 2026), as reported (S).**
  - HB applied to HBM4 samples delivered to a key customer.
  - "some commercialization is planned at the HBM4E stage" (03-092, 05-030).
  - Same call: 16-stack HBM3E/HBM4 mass production is "unnecessary" given "very limited" demand.
- No SEMES executive gave a dated HBM timing, so no change can be marked for SEMES itself.

### 2.8 SUSS MicroTec (CEO Burkhardt Frick)

| Date | Class | Statement | ID |
|---|---|---|---|
| 27 Mar 2024 | P (SUSS-hosted transcript) | "for HBM4, it's not a must-have to have hybrid bonding mass production ready … hybrid bonding schedule is a bit relaxed now" | 04-043 |
| 7 Aug 2025 | P | "Our anticipation is earliest HBM4e if not HBM5 for broader introduction" | 04-037 |
| 17 Nov 2025 | P (CMD slides) | "W2W HB established and D2W HB close to mass production"; SUSS: "Enter Advanced Logic (short-term) & HBM (mid term)" | 04-032, 04-033 |
| 30 Mar 2026 | P | "Hybrid bonding … is moving a bit sideways, a little bit away from die-to-wafer application because runways are extended for TCB bonding equipment and also some customers, they are struggling with the process" ⚑ | 04-029 |
| 7 May 2026 | P | "We see more emphasis now on wafer-to-wafer hybrid bonding than on die-to-wafer" | 04-022 |
| 5 Nov 2026 | P | "the real takeoff for hybrid bonding for HBM is also not running smoothly because it's a big technology risk. TCB suppliers are extending the runway … So we don't see a mass adoption of that technology yet" | 04-008 |

### 2.9 Tokyo Electron (President & CEO Toshiki Kawai; company Q&A)

TEL gives no generation or year for HB in HBM.
- Its W2W tool is "Moving toward High-Volume Manufacturing with major memory and logic customers" (Mar 2026) (04-062).
- D2W for HBM is "in development", with 16-high demonstrated on blanket dielectric (04-063).
- "Hybrid bonding" is listed as moving "From POR to High Volume Manufacturing" (30 Jul 2026) (04-052).
- "For HBM, the number of stacked DRAMs will increase from 12 to 16 … within two years to come" (30 Jul 2026; not tied to HB) (04-053).
- 3D-integration growth "from CY2027 onward" (4 Nov 2026) (04-050).

### 2.10 EV Group, Piotech, Shibaura, Yamaha Robotics, Toray Engineering

- **EVG.** Since Feb 2026 it has repeated the same application wording: W2W HB "critical for … next-generation 3D NAND and DRAM", D2W "an important enabler of … HBM stacks" (04-074). No year or stack height.
- **Piotech (2025 annual report).** HB "expected to be introduced" in HBM "to support higher stack counts" (04-088). No year.
- **Shibaura.** HB revenue (logic, image sensors) is planned for FY2027–28 (02-110).
- **Yamaha Robotics.** An HBM model is under "client evaluations" (02-094).
- **Toray Engineering.** No statement found.

### 2.11 Memory makers (context; these set the bonder makers' timing)

**SK hynix**
- 25 Apr 2024 (S, call): "If the HBM package height standard is relaxed, the timing for applying hybrid bonding will be somewhat delayed" (05-007).
- Jul–Sep 2024 (S): HB and MR-MUF were both options for 16-high HBM4 (05-008, 05-009).
- 17 Apr 2025 (S): MR-MUF up to 16-layer HBM4; "Starting from 20-layer stacking, however, hybrid bonding is essential" (05-011) ⚑ (later: HB out of HBM4).
- 12 Sep 2025 (P): "adopted the Advanced MR-MUF process in HBM4" (05-012).
- Jan 2026 (S, investor briefings): current process kept "through the HBM4 and HBM4E 16-high products"; fluxless TCB "premature" (05-013, 05-014) ⚑.
- Mar 2026 (S): HB "essential for HBM stacks of 20 layers or more" (05-016).
- Apr 2026 (S): 12-high HB validation completed, working on yield (05-017).
- 18 Jun 2026 (P): "SK hynix utilizes Advanced MR-MUF technology for HBM4E products" (05-020).
- 23–26 Aug 2026 (S): Hot Chips framed HB as the route to 20+ layers. Bits&Chips reads this as HB delayed "by one generation" to HBM5 (05-021, 05-023) ⚑.
- 9 Sep 2026 (S): HB needs "a yield of 90 to 98 percent" and "a lifespan of three to five years" (05-025).

**Samsung**
- Oct 2023 (S quoting blog): HBM4 with "non-conductive film (NCF) assembly and hybrid copper bonding (HCB)" (05-026).
- Jun 2024 (S): HB "essential for HBM with 16 stacks and above" (05-027).
- May 2025 (S): HB for HBM4 (05-028).
- 23 Jul 2025 (S): "with its 16-layer HBM4E" ⚑ (05-029).
- 29 Jan 2026 (S, call): 16-stack "unnecessary"; "some commercialization is planned at the HBM4E stage" (05-030).
- 16 Mar 2026 (P, GTC): HCB "will enable next-generation HBM to achieve 16 or more layers", >20% lower thermal resistance (05-032).
- 22 Jul 2026 (S): ~50-bonder Pyeongtaek line, installs from end-2026, large-scale HB ~2029–2030 (05-034, 05-035).
- 29 Oct 2026 (S, call): HBM4E mass production 1H27, ramp 2H27; no HB mention (05-036).

**Micron**
- No dated HB commitment.
- 2 Sep 2026, CTO Scott DeBoer (S, tr.): "In terms of high-volume manufacturing capability, hybrid bonding is indeed clearly behind right now" (05-041).

---

## 3. Facts that push hybrid bonding in HBM later or pull it earlier (one dated table)

Push = later; Pull = earlier. "Std" = standard (JEDEC). The class column refers to the source of the row.

| Date | Fact | Push / Pull | Type | Class | ID |
|---|---|---|---|---|---|
| 2023-06-06 | Besi: "TCB for memory will probably be used to stack up to 12 dies"; "36% of HBM will use hybrid bonding by 2028 according to Yole" | Pull (baseline) | Forecast | P | 01-038, 07-001 |
| 2023-10-12 | Samsung: HBM4 to use "NCF assembly and hybrid copper bonding (HCB)" | Pull | Roadmap | S | 05-026 |
| 2024-03-13 | JEDEC participants reportedly agree 775 µm (from 720 µm) for 12/16-high HBM4; memory makers said 720 µm had "reached its limit" | Push | Std | S | 05-001 |
| 2024-03-27 | SUSS: with relaxed height, HB "not a must-have" for HBM4 | Push | Std | P | 04-043 |
| 2024-04-25 | SK hynix: if height is relaxed, HB timing "will be somewhat delayed" | Push | Std | S | 05-007 |
| 2024-05-02 | K&S: Cu-Cu fluxless TCB "could potentially delay higher volume adoption of hybrid bonding due to a more competitive cost of ownership" | Push | Fluxless TCB / cost | T | 02-087 |
| 2024-06-06 | Besi: "Change to max. 775µm allows 16-layer stacks with TCB but does not solve the heat issue"; memory adoption "shifted out one year" | Push | Std | P | 01-041, 01-042, 07-006 |
| 2024-06-12 | Samsung built a 16-stack HB HBM sample on SEMES tools; ECTC paper: HB "essential for HBM with 16 stacks and above" | Pull | Technical | S | 05-027 |
| 2024-09-03 | SK hynix: "feasibility of applying Advanced MR-MUF to 16-high products" confirmed | Push | MR-MUF | S | 05-009 |
| 2024-11-04 | SK hynix CEO: 16-high HBM3E on Advanced MR-MUF; HB "as a backup" | Push | MR-MUF | S | 05-010 |
| 2025-02-26 | ASMPT: fluxless 16H sample "within the maximum stack-up height of 775 μm" | Push | Fluxless TCB | P | 02-055 |
| 2025-04-17 | JEDEC publishes JESD270-4 (HBM4, up to 16-high). The 775 µm figure comes from press; the release gives no height | Push | Std | P / S | 05-002, 05-003 |
| 2025-04-18 | SK hynix: MR-MUF through 16-layer HBM4; HB "essential" from 20 layers | Push | MR-MUF | S | 05-011 |
| 2025-04-23 | Besi: HB orders "from two leading memory producers for HBM 4 applications" | Pull | Orders | P | 01-045 |
| 2025-04-23 | Besi CEO on cost: "Say 6 times higher using a hybrid process compared to a reflow process" | Push | Cost | T | 01-047 |
| 2025-06-12 | Besi: "TC and TC-fluxless will be primary technologies used through HBM4" | Push | Fluxless TCB | P | 01-049 |
| 2025-07-15 | Hanmi: with 775 µm, HBM4 and HBM5 both on TC; hybrid bonder > KRW 10 bn/unit, "more than twice" a TC bonder | Push | Std / cost | S | 03-034, 03-035 |
| 2025-07-23 | Samsung's HB entry reported as "16-layer HBM4E" (was HBM4) | Push | Roadmap | S | 05-029 |
| 2025-07-30 | Hanmi has won a fluxless-bonder order (delivery 2025) | Push | Fluxless TCB | S | 03-039 |
| 2025-08-12 | SemiAnalysis: HB "shifted back to 4E"; 775 µm a "blow to hybrid bonding adoption"; D2W HB yields "extremely difficult and expensive" | Push | Analyst / yield | S | 05-050 |
| 2025-09-12 | SK hynix HBM4 mass-production-ready on Advanced MR-MUF | Push | MR-MUF | P | 05-012 |
| 2025-10-07 | Korean analysts: HB ~50% of HBM output by 2028; HB-bonder market KRW 2.8 tn | Pull | Forecast | S | 05-054 |
| 2025-10-23 | Besi: "A push out to Q4-25 of certain anticipated hybrid bonding bookings" | Push | Orders | P | 01-008 |
| 2025-10-28 | ASMPT: fluxless AOR "superior scalability for HBM 16H and above with the lowest cost of transition" | Push | Fluxless TCB | P | 02-016 |
| 2025-11 (rep. 2025-12-12) | SK hynix orders 7 ASMPT TC bonders (~KRW 30 bn). ~50 TC sets used for HBM4, ~half ASMPT | Push | TCB capex | S | 03-097 |
| 2026-01-12 | SK hynix 16-layer HBM4 on MR-MUF, DRAM thinned to 30 µm to fit 775 µm | Push (and near a thinning limit) | MR-MUF | S | 05-015 |
| 2026-01-13 | SK hynix: fluxless TCB "premature"; current process "through the HBM4 and HBM4E 16-high products" | Push | MR-MUF | S | 05-013, 05-014 |
| 2026-01-29 | Samsung: 16-stack HBM3E/HBM4 "unnecessary" (demand "very limited"); HB HBM4 samples delivered; "some commercialization … at the HBM4E stage" | Push (stack demand) / Pull (samples) | Demand / roadmap | S | 05-030, 03-092 |
| 2026-02-05 | K&S: fluxless TCB "a strong alternative to hybrid bonding for the next generation HBM" | Push | Fluxless TCB | T | 02-072 |
| 2026-02-13 | Samsung CTO: HCB >20% lower thermal resistance (research); NVIDIA "request influenced" acceleration; tools moved in from March | Pull | Thermal / customer | S | 05-031, 05-045 |
| 2026-03-06 | JEDEC discussion of ~825–900 µm for HBM4E/HBM5 20-high (not adopted) | Push | Std (proposal) | S | 05-004 |
| 2026-03-12 | Hanmi annual report: hybrid-bonder development "delayed by technical challenges" | Push | Tool maturity | P | 03-043 |
| 2026-03-16 | Samsung GTC: HCB "reducing heat resistance by more than 20 percent, compared to … TCB", for "16 or more layers" | Pull | Thermal | P | 05-032 |
| 2026-03 (rep. 04-29) | SK hynix buys an Applied + Besi inline HB system (~KRW 20 bn), "first … intended for mass production" | Pull | Orders (pilot scale) | S | 05-018 |
| 2026-03-30 | SUSS: "runways are extended for TCB … some customers, they are struggling with the process" | Push | Fluxless TCB / yield | P | 04-029 |
| 2026-04-01 | JEDEC reportedly weighing ~900 µm from HBM4E (not adopted) | Push | Std (proposal) | S | 05-005 |
| 2026-04-06 | Counterpoint: SK hynix HBM5 "around 2029–2030" with HB at mass-production scale | Push | Analyst | S | 05-051 |
| 2026-04-10 | Hanwha SHB2 Nano 2nd-gen hybrid bonder delivered to SK hynix for evaluation | Pull | Tool | S | 03-077 |
| 2026-04-16 | Lam–Hanwha hybrid-bonder JV dropped, partly on the view that HB adoption in next-gen HBM may be delayed | Push | Corporate | S | 03-078 |
| 2026-04-23 | Besi: HB unit orders more than doubled QoQ; repeat HBM orders; two evaluation tools at a second memory maker | Pull | Orders | P | 01-022, 01-023 |
| 2026-04-23 | Besi CEO: "For HBM stacking, one still has to prove that [yield]" | Push | Yield | T | 01-056 |
| 2026-04-29 | SK hynix: 12-high HB validation completed; raising yields | Pull | Technical | S | 05-017 |
| 2026-05-26 | SK hynix iHBM (MR-MUF based) cuts thermal resistance 30%, targeted at HBM5 | Push (alternative to HB) | Thermal alternative | S | 05-019 |
| 2026-06-18 | SK hynix 12-high HBM4E samples on Advanced MR-MUF; heat resistance improved 17% vs HBM4 | Push | MR-MUF | P | 05-020 |
| 2026-06-18 | Besi: "1st production in HBM4e in 2027"; Samsung ECTC 2026 cited as "up to 30% better" thermal with HB | Pull | Roadmap / thermal | P | 01-057, 07-005 |
| 2026-07-06/07 | Samsung and SK hynix "reconsidering"; 12-high "most likely to remain the mainstream even in HBM4E"; JEDEC discussing 900 → up to 1,000 µm for 20-high HBM5 (not adopted) | Push | Std (proposal) / demand | S | 05-006, 05-037 |
| 2026-07-06/07 | HBM5E may double I/O to 4,096, which would require HB | Pull | Interface | S | 05-038 |
| 2026-07-15 | Hanmi: HB "around 2029" for ≥16-high mass production | Push | Roadmap | S | 03-046 |
| 2026-07-22 | Samsung reportedly building ~50 D2W HB line at Pyeongtaek, installs from end-2026; large-scale HB ~2029–2030; Besi order not finalised (price) | Pull (capex) / Push (date) | Capex / roadmap | S | 05-034, 05-035 |
| 2026-07-28 | ASMPT: HB inflection "2029, 2030 … or even 2031"; JEDEC "beyond 900" would extend TCB "into HBM5" | Push | Std / roadmap | T | 02-040, 02-041 |
| 2026-08-04 | NVIDIA evaluating 8-Hi HBM4e, 12-Hi HBM4 and 8-Hi HBM4 for Rubin Ultra | Push | Demand | S | 05-043 |
| 2026-08-23 | SK hynix Hot Chips: HB gives "35% lower thermal resistance", "24% thicker core die", pitch "below 18 um"; aimed at 20+ high | Pull (tech) / Push (20+ only) | Thermal | S | 05-021 |
| 2026-08-25 | SK hynix newsroom guest note: HB cost "two to three times higher" than flip chip; full-scale adoption "most likely … in HBM4E or HBM5, where stack heights are projected to exceed 20 layers" | Push | Cost | P (guest author) | 05-024, 07-008 |
| 2026-09-02 | Micron CTO: HB "clearly behind" in high-volume capability | Push | Readiness | S | 05-041 |
| 2026-09-09 (rep. 09-20) | SK hynix: HB requires 90–98% yield and 3–5-year life before use | Push | Yield bar | S | 05-025 |
| 2026-10-22 | Besi: "Severe memory shortages … extended the use of lower stack heights"; HB "over the next two years" | Push | Demand | P | 01-063, 01-064 |
| 2026-10-22 | Besi: HB and TC Next orders "from a leading memory customer" | Pull | Orders | P | 01-034 |
| 2026-10-27 | Rubin Ultra reportedly moving from 12-Hi HBM4E to 8-Hi HBM4; 8-Hi shipments 2Q27 | Push | Demand | S | 05-044 |
| 2026-10-28 | ASMPT: memory "larger capability-driven investments have been pushed-out"; "HBM layer count stagnation" | Push | Capex / demand | P / T | 02-049, 02-051 |
| 2026-10-29 | Samsung: HBM4E mass production 1H27, ramp 2H27 (no HB mention) | Neutral | Roadmap | S | 05-036 |
| 2026-11-04 | Camtek COO: HB business "will start to materialize more in the '28 and onwards … in '27, I don't expect to see any substantial business coming from hybrid bonding" | Push | Supplier view | T | 06-033 |
| 2026-11-05 | SUSS: "we don't see a mass adoption of that technology yet" | Push | Supplier view | P | 04-008 |
| 2026-11 | Besi: "Cost of ownership differential versus TCB reducing"; HB thermal resistance "up to 30% less than TCB as per recent customer benchmark" | Pull | Cost / thermal | P | 01-070, 07-004 |
| 2026-11-13 | Hanmi Q3 report: new bonding needed from 16-high (was 20-high); answer offered is a wide TC bonder | Ambiguous | Roadmap | P | 03-051 |
| 2026-11-18 | TrendForce: SK hynix's Aug 2026 roadmap places "bumpless TCB" as an interim step between fluxless TCB (~8 µm pitch) and HB | Push | TCB extension | S | 07-010 |

### 3.1 What the table does and does not contain

**Yield.** No maker has disclosed an HB yield for HBM.
- The only quantified bar is SK hynix's "90 to 98 percent" requirement (05-025).
- SK hynix says 12-high HB validation is done and yield work is under way (05-017). Besi says yield still has to be proven (01-056).

**Cost.**

| Source | Measure | Figure |
|---|---|---|
| Besi CEO, Apr 2025 | process cost vs reflow | about 6x (01-047) |
| SK hynix newsroom guest note | cost vs flip chip | 2–3x (07-008) |
| Hanmi | bonder price | HB >KRW 10 bn vs TC ~KRW 3 bn (03-035) |
| The Elec | Besi HB unit price | ~KRW 6 bn, about 2x rivals (07-009) |
| Besi, Nov 2026 | cost-of-ownership gap vs TCB | "reducing" (07-004) |

No cost-per-bit comparison was found.

**Thermal.**
- HB: >20% (Samsung, P), 35% (SK hynix slide, S) and up to 30% (Besi citing a customer, P) lower thermal resistance than TCB.
- Alternatives: SK hynix iHBM, built on MR-MUF, claims −30% (S).
- This repository's earlier prompt material (`prompts/Company research prompts.md`, on branch `ccr-75d5f61b-6qfsp9`) says "Samsung reported that it cuts thermal resistance by only 12-13%" (07-012). That figure was **not found** in any source. Samsung's own 2026 statements say ">20%", and Besi cites a Samsung ECTC 2026 result of "up to 30%" (see review_packet.md, conflicts).

**Standard.**
- 775 µm is effectively in force for HBM4. The JEDEC release states no height; the figure comes from press.
- About 900 µm (HBM4E) and up to 1,000 µm (20-high HBM5) are reported proposals only.
- [I] Adoption of either proposal would be the single largest push on the HBM5 timing. ASMPT's CEO says so directly (02-041).

---

## 4. Inspection and metrology attached to bonding lines

### 4.1 Bonder maker × named inspection or metrology partner, and integrated modules

| Bonder maker | Third-party inspection / metrology supplier named as integrated in, or qualified with, the line | Inspection / metrology integrated in, or sold with, the bonder | ID |
|---|---|---|---|
| Besi | **None named.** The only partner is Applied, which brings "metrology, inspection and particle defect control" to the joint Center of Excellence | Datacon 8800 CHAMEO ultra plus AC: "Inline IR Inspection … in-situ IR inspection capability, immediate feedback of placement accuracy without need of unloading material"; spec "100 nm @ 3 sigma". 9800 TC next: "High-Resolution Vision Systems … alignment and inspection" | 06-001, 06-002, 06-004, 06-007 |
| Applied (Kinex, with Besi) | **None external.** Metrology is Applied's own | Kinex: "Faster overlay measurement and drift detection achieved by integrated, in-line metrology" (7 Oct 2025). Besi SVP: Kinex includes "the measurement after the bonding, so the quality assurance" (Jun 2026, T). Futurum (S): "IR metrology", "closed-loop overlay (OVL) control", overlay iteration "from 1–2 hours down to ~10 minutes". Applied also sells standalone pre-bond tools: VeritySEM 7AP, SEMVision G7AP, Opta Quad CMP | 01-082, 01-072, 06-005, 06-006, 06-008 |
| ASMPT | **None.** Process partners only: KOKUSAI ELECTRIC (HB/TCB thin film), IBM | None stated on LITHOBOLT or FIREBIRD pages | 02-062, 06-020 |
| Kulicke & Soffa | **None** | None for TCB/HB. The "inline inspection" it mentions refers to its dispense product | 02-092 |
| EV Group | **None.** imec is a co-development partner; an ECTC 2026 paper on 100% bond-overlay measurement was co-authored with Intel | GEMINI FB: "Alignment verification module"; SmartView NT3 "sub 50 nm" alignment; integrated IR inspection station ("Void size detection down to 500 µm radius"); Inline Metrology Module. GEMINI FB D2W: "integrated metrology functions allowing feed-forward and feed-back loop". Standalone EVG40 NT2 and EVG40 D2W ("up to 2800 overlay measurement points … in just four minutes"; "Multiple … installed") | 06-009 to 06-012, 04-078, 04-084 |
| SUSS MicroTec | **None.** SET is the die-bonder partner | XBC300 Gen2 D2W/W2W: "full-field IR overlay measurement and IR void inspection, with a detection resolution >500 µm void sizes". XBC300 Gen2 SP: "in-line IR void detection". XBS300: up to six metrology modules per cluster | 06-014, 06-015, 04-047, 04-048 |
| Tokyo Electron | **None** | Developing "New X-ray imaging program for TEL's integrated metrology": overlay "< 50 nm", "Demo-ready in Q2 2026", "Moiré fiducials for multi-die HBM overlay" | 06-016, 04-064 |
| Hanmi | **None** | Own "HBM 6-SIDE INSPECTION", sold alongside TC bonders: inspects dies before stacking and the "6면의 외관과 접합 상태" (appearance and bond state of all six faces) after; in-house vision module "applied to … all our equipment" | 03-052, 06-018 |
| Hanwha Semitech | **None** | In-line flux-coating inspection on its TC bonders (subject of patent dispute with Hanmi); SHB2 Nano 0.1 µm alignment | 03-079, 06-019 |
| SEMES | **None** | TC bonder with "고정밀 Align" (high-precision alignment); separate HBM package probe station SEMPRO-H | 03-095 |
| Piotech | n/a (makes its own) | Separate in-house tools: Crux bond-overlay metrology (IR; "passed customer verification"; new-customer orders H1-26), Ascella bond strength, Volans void repair (in development) | 04-093 |
| Shibaura | **None** | TFC-6500: "IRインスペクション" (IR inspection) option; post-mount inspection. TFC-6800 HB: none stated | 02-113 |
| Yamaha Robotics, Toray Engineering | **None** | Nothing specific to TCB or HBM | 02-096 |

### 4.2 The inspection suppliers' side (standalone tools, not integrated in bonders)

| Supplier | HB / HBM item | Class | ID |
|---|---|---|---|
| Auros Technology | Samsung ordered 2 HE-900IR IR overlay tools (~KRW 3 bn each, ~KRW 6 bn total) for W2W alignment and Cu-Cu placement accuracy; reportedly rated above KLA IR Archer007. **The only HB-specific inspection order with a value found** | S | 06-042 |
| Onto Innovation | HBM maker made double-digit Dragonfly G5 and 3Di commitments for the HBM4 ramp, "displacing the previously established tool of record" (16 Mar 2026). Dragonfly G5 detects 150 nm defects for "CMP and hybrid bonding". EchoScan detects voids "as small as 1µm" vs incumbent "≥10µm". Over 10 Dragonfly G5 customers; 2027 POs double 2026 revenue (Nov 2026) | P / T | 06-024 to 06-029 |
| KLA | Advanced-packaging process-control revenue ~$635 m (2025) → ~$1.1 bn (2026). HB moves sensitivity "from micron level … down to the 100 nanometer type". No HB revenue disclosed | T | 06-021 to 06-023 |
| Camtek | >$50 m Hawk orders from "a leading HBM player" for 2027 delivery. HB business "in the '28 and onwards" | P / T | 06-030, 06-033 |
| Nova | WMC "adopted by one of the world's leading memory manufacturers for High Bandwidth Memory"; ">10 customers" | P / T | 06-035, 06-037 |
| PVA TePla | H1-26 metrology orders EUR 97.7 m, driven partly by ultrasonic inspection for HBM | P | 06-039 |
| Infinitesima | SK hynix ordered AFM metrology for HBM packaging (no value) | S | 06-043 |
| Bruker, Lasertec, Nearfield, Hitachi Power Solutions | Product claims for HB surface, recess and void metrology; no HB orders found | P / S | 06-044 to 06-048 |

### 4.3 What this shows [I]

- **The line is a closed loop run by the bonder maker.** Every in-line overlay, void or particle function sold as part of an HB line is the bonder maker's own: Applied/Besi, EVG, SUSS, TEL and Piotech.
- **Where the third-party vendors play.** Their HB and HBM business is standalone:
  - pre-bond surface and CMP: Onto, Bruker, Lasertec, Applied eBeam;
  - post-bond IR overlay: Auros, KLA IR Archer;
  - acoustic void inspection: Onto EchoScan, PVA TePla, Nordson, Hitachi.
- **Void resolution.** The integrated IR modules resolve only coarse voids: SUSS and EVG quote 500 µm-class figures. Standalone acoustic tools claim 1 µm (Onto) to 0.8 µm (PVA TePla). [I] That gap is why HBM HB lines will likely still need standalone void inspection.
- **Who is already buying.** Samsung has bought HB-specific overlay metrology (Auros), and SK hynix AFM (Infinitesima). This is consistent with pilot lines, not volume.

---

## 5. [I] Dated range for first volume use of hybrid bonding in HBM

**Definition.** "First volume use" means hybrid-bonded HBM stacks shipped in production quantities into a customer's qualified product. It excludes samples, qualification lots and evaluation tools.

**Range: 2H 2028 to end-2029. Most likely 2029. Samsung is most likely first, on a 16-high HBM4E or custom/stacked HBM part. SK hynix follows at 20-high HBM5 in 2029–2030.**

**The two statements it depends on most**

1. **Besi, Q3-2026 results release, 22 Oct 2026 (P; 01-063, 01-064).**
   > "Severe memory shortages this year have extended the use of lower stack heights in current HBM production beyond prior expectations. … We anticipate that hybrid bonding will be adopted in a range of stack heights over the next two years"

   On the call, Blickman added that "The precise dates … is not known by us" and that adoption "has been somewhat delayed" (T, 01-065, 01-066).

   *Why it bounds the early side:*
   - Besi is the HB vendor with the strongest incentive to be early. It sees all three memory makers' qualifications: "All leading HBM players have installed Besi's hybrid bonding solutions" (Nov 2026, P).
   - Four months earlier it had said "1st production in HBM4e in 2027" and "First mover is preparing for HVM in 2027" (01-057, 01-059). Dropping the year and moving to "over the next two years" from October 2026 puts adoption, at the latest, by about late 2028.
   - [I] "Adoption" in Besi's usage has meant production start, which precedes volume. So this statement supports 2H 2028 as the earliest likely volume window, not 2027.

2. **Hanmi Semiconductor, Chairman and CEO Kwak Dong-shin, written interview, 15 Jul 2026 (S; 03-046).**
   > "하이브리드 본더는 2029년경 예상되는 16단 이상 HBM 양산 시점에 맞춰 적기에 공급" ("[we will] supply hybrid bonders in time for the mass production of 16-high-and-above HBM expected around 2029")

   *Why it anchors the central and late side:*
   - Hanmi holds about 71% of the global TC-bonder market (TechInsights, via press) and supplies both SK hynix and Micron.
   - It is building a dedicated hybrid-bonder plant, due H1 2027, and a second-generation prototype that SK hynix and Micron reportedly asked it to accelerate.
   - Its year matches three independent signals:
     - ASMPT's CEO: "maybe 2029, 2030 … or even 2031" (02-040);
     - Samsung's reported Pyeongtaek line: large-scale HB in 2029–2030 (05-034);
     - Counterpoint: SK hynix HBM5 with HB in 2029–2030 (05-051).
   - Hanmi has an incentive to place HB late, because it sells TCB. That bias is offset by its own capex in HB. Its Q3-26 filing also lowered the stack height at which new bonding is needed from 20 to 16 (03-051).

**What would move the range**

- **Earlier, to 2H 2027 to 1H 2028.**
  - Samsung executes "some commercialization … at the HBM4E stage" (Jan 2026; 05-030) on its HBM4E schedule (mass production 1H27, ramp 2H27; 05-036).
  - This needs a customer for a 16-high HBM4E. Against it: NVIDIA's reported move to 8-high stacks for Rubin Ultra (05-043, 05-044); Samsung's own "16-stack … unnecessary" (05-030); 12-high "most likely to remain the mainstream even in HBM4E" (05-037). Camtek sees no substantial HB business in 2027 (06-033).
  - [I] Low-volume HB parts in 2027 are possible, but they would not meet the volume definition above.
- **Later, to 2030 or beyond.**
  - JEDEC adopts ~900 µm for HBM4E or up to 1,000 µm for 20-high HBM5 (05-005, 05-006). ASMPT says this would extend TCB "into HBM5" (02-041).
  - SK hynix holds to its 90–98% yield and 3–5-year lifetime bar (05-025).
  - SK hynix's thermal alternatives to HB (iHBM, −30%) succeed (05-019).
- **Not a timing signal.** Logic HB volume is already here: Intel, AMD, Apple and TSMC SoIC. ASMPT expects logic HB demand growth within 12–18 months. Logic HB volume does not by itself pull the HBM date.

---

## Method and limits (detail in gaps.md and review_packet.md)

- **How the work was done.** Six research passes ran in parallel, one per company group or theme. Each wrote dated notes with verbatim quotes and an evidence table. This dossier merges them. The source notes are not in the repository: they were working files in a temporary scratch directory. Every figure used is carried in `evidence.csv`.
- **Tool limits.** Partway through, the shared web-search budget and the Firecrawl credits ran out. Several company sites blocked automated access: Applied's IR site and newsroom, KLA, roic.ai and GuruFocus transcripts, and parts of Yole.
  - Some items therefore rest on third-party transcripts (class T) or press paraphrase (class S).
  - Several ASMPT 2025 and early-2026 call statements are search-snippet paraphrases.
- **Quote fidelity.** Many quotes were captured through a summarising fetch tool. They are verbatim as returned, but have not been checked character by character against the original page. `review_packet.md` lists the load-bearing ones to verify.
