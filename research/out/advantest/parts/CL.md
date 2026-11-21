# CL - Candidate disputed claims (B1), facts for B2, dated catalysts (B3)

Advantest Corporation, TSE Prime 6857, Japan. The fiscal year ends 31 March, and Advantest names fiscal years by start year (FY2026 = Apr 2026-Mar 2027). IFRS, JPY.

- Evidence ids refer to `parts/CL.csv` (CL-001 to CL-132). The cross-references A5-003 and A5-004 point to module A5.
- Arithmetic is in `calc/CL_*.py`; each script's output is in the matching `.out.txt`.
- Teradyne reports by calendar quarter. Its Q3 2026 (Jul-Sep 2026) covers the same months as Advantest's FY2026 Q2.

## Premise notes

- **Run facts.** They hold. FY2026 Q2 (Jul-Sep 2026) results are dated 28 Oct 2026 [F] (CL-032). MTP3 runs FY2024-FY2026, so it ends 31 Mar 2027 [F] (CL-101).
- **AGM month.** The 84th AGM was held on 31 Jul 2026, not in June [F] (CL-096). The 2025 AGM amended the Articles to allow a July meeting [F] (CL-098).
- **Conflicting record dates.** Two company pages disagree on the next voting-rights record date:
  - The IR calendar says 31 Mar 2027 [F] (CL-095).
  - The Share Information page says 15 May, with the AGM within three months after it [F] (CL-097).
  - The 85th AGM date is therefore not committed [I] (CL-126, Medium).
- **Next results date.** The IR calendar gives only "January 2027" for the Q3 FY2026 results [F] (CL-094).
- **Next mid-term plan.** There is no fixed date for MTP4, only "around May 2027" [C] (CL-102).
- **Press date mismatches.**
  - The TrendForce file name carries a placeholder date (2026-01-01). The page metadata says 2026-10-05, and the CSV `date` column uses that (CL-056 to CL-058).
  - The Wing VC and Simply Wall St files are named by retrieval date (2026-11-21). They were published 2026-11-18 and modified 2026-10-29 (first published 2025-06-06).
- **Press error.** RCR Wireless (CL-021) describes the January 2026 guidance (sales JPY 1.07 tn, OI JPY 454.0 bn) as being for the year to 31 Mar 2027. The company document shows it was the FY2025 (Apr 2025-Mar 2026) forecast [C] (CL-130).
- **Simply Wall St source.** The page says it was produced by an LLM tool ("AnalystLowTarget"). It is used only for its qualitative bear arguments [S] (CL-023, CL-091). Its valuation content is excluded under the project rules.

## (a) Candidate disputed claims (8 candidates; the B1 ledger keeps 6)

| # | Claim | Who said it, when | Evidence for | Evidence against | Strongest tag on each side |
|---|---|---|---|---|---|
| C1 | AI-driven tester demand is durable: tester TAM keeps growing about 50% a year, with no slowdown into CY2027 | Advantest management, 28 Oct 2026 (CL-001, CL-002, CL-004); Teradyne CEO, 28 Oct 2026 (CL-018) | No slowing seen [C] (CL-002); supply constrained in CY2027 [C] (CL-005); 18-month customer forecasts [C] (CL-014); test share of capex 6.4% to 8.1% [C] (CL-018); forecast 2H FY2025 digestion did not occur [C] (CL-011) | Management credited demand pull-ins [C] (CL-009, CL-011); it expected a 2H FY2025 correction [C] (CL-131); capex is "highly fluid" [F] (CL-012); Teradyne 2H 2026 compute "program timing" [C] (CL-019); analysts saw trade-statistics divergence [S] (CL-016); digestion "worth tracking into 2027" [S] (CL-022) | For: [C]. Against: [C] for the specific pull-in statements; [F] only for the generic risk text |
| C2 | Advantest's SoC tester share keeps rising, from 66% (CY2025) to above 70%, including GPU/AI accelerators | Advantest management, 27 Apr and 28 Oct 2026 (CL-039 to CL-042) | Share 56% to 66% [C] (CL-039); majority of AI accelerator market [C] (CL-041); SoC sales +103.4% YoY vs Teradyne compute about +50% [I] (CL-115, Low); "replacement risk approaches zero" [S] (CL-050) | Teradyne expects share gains from dual-vendor adoption [C] (CL-044); ramps in mid-2027, 2027 and 2H 2027 [C] (CL-045 to CL-047); dual-vendor share range 30-70% [C] (CL-048); Advantest concedes customers may dual-source [C] (CL-043) | For: [C]. Against: [C] |
| C3 | Rising HBM/DRAM test intensity will lift Advantest's memory tester business | Advantest, 28 Oct 2026 (CL-053); TrendForce, 5 Oct 2026 (CL-057) | Memory TAM from 2.1 to 2.5-3.0 USD bn [C] (CL-007); DRAM back-end growth expected [C] (CL-053); test equipment may outgrow HBM output [S] (CL-057) | Memory share -2 pts in CY2025 and may fall in 2026 [C] (CL-051, CL-052); memory +21.6% YoY vs SoC +103.4%, and 2.2% below FY24 Q3 [I] (CL-114); Teradyne record memory revenue of USD 301m [F] (CL-055); Teradyne claims the HBM performance-test lead [C] (CL-054); HBM4 wafer-test orders to Digital Frontier and UniTest [S] (CL-056) | For: [C]. Against: [F] |
| C4 | China sales will normalise to about 20% of sales or less, and export controls have limited direct effect | Advantest management, 29 Jul 2026 (CL-060, CL-061) | About 19% [C] (CL-060); 18.9% in FY26 Q1 and Q2, LTM 19.5% [I] (CL-118); no major tariff impact expected [C] (CL-067) | China sales JPY 90.1 bn in FY26 Q2 vs 52.1 bn a year earlier [F] (CL-059), +72.9% [I] (CL-118); January 2026 guidance of 20-25% [C] (CL-132); EAR 3B992.b.4.b covers IC testers above 20 MHz [F] (CL-066); Chinese tester competitors named [F] (CL-065); Chinese memory ATE gaining [S] (CL-058) | For: [C]. Against: [F] |
| C5 | Concentration in a few AI customers (NVIDIA Group above 20%) is Advantest's main tail risk | Wing VC, 18 Nov 2026 (CL-022); Advantest risk factor (CL-070) | NVIDIA Group JPY 243,735m [F] (CL-068), 21.6% of sales [I] (CL-119); NVIDIA International 20.2% [F] (CL-069); top five about 50% [F] (CL-070) | CPU demand was the biggest factor in the FY2026 upgrade [C] (CL-071); V93000 capacity can be reconfigured across compute devices [C] (CL-072) | For: [F]. Against: [C] |
| C6 | An operating margin of 50% or more is sustainable | Advantest management, 28 Oct 2026 (CL-034, CL-075) | Q2 FY26 OPM 55.9% [F] (CL-025); GM above 70% [F] (CL-026); FY26 forecast 51.9% [C] (CL-034); 2H raised from 47.3% [C] (CL-035) | One-time inventory reversal in 1H, amount not disclosed [C] (CL-073); DRAM cost headwind [C] (CL-074); Q4 FY25 "optimal mix" may not recur [C] (CL-076); implied 2H 50.1% vs 1H 54.0% [I] (CL-117); Teradyne non-GAAP 31.6% [F] (CL-078), a 24.3-point gap [I] (CL-122) | For: [F]. Against: [C] |
| C7 | Supply capacity, not demand, is the binding constraint | Wing VC, 18 Nov 2026 (CL-092); Advantest, 28 Oct 2026 (CL-005, CL-086) | Capacity above 5,000 systems/yr, 10,000 pulled forward [C] (CL-081 to CL-083); memory parts tight [C] (CL-086); DDR4 being stockpiled [C] (CL-087); Teradyne says demand exceeds supply [C] (CL-020) | Inventories JPY 231.7 bn to 352.4 bn [F] (CL-088), +52.1% in six months [I] (CL-120); risk factor on excess inventory [F] (CL-089); 10,000 timing not yet fixed [C] (CL-083); overbuild risk [S] (CL-091) | For: [C]. Against: [F] |
| C8 | Tester TAM: Advantest's ~50%/yr growth and CY26e USD 13.0-14.5 bn vs Teradyne's 15-25% CAGR to USD 12-14 bn | Advantest, 28 Oct 2026 (CL-001, CL-007); Teradyne target model, updated 3 Feb 2026 and shown 27 Oct 2026 (CL-079) | CY24 to CY25 +50.0%, CY26e +44.4% to +61.1% [I] (CL-112) | Teradyne model [C] (CL-079); Advantest's CY26e already overlaps Teradyne's target band [I] (CL-113); a ~USD 8 bn 2026 figure was relayed in January 2026 [S] (CL-109), USD 5.0-6.5 bn below the current estimate [I] (CL-129) | For: [C]. Against: [C] |

Suggested cut to six for B1: drop C8 (it overlaps C1 and both sides are company models) and C5 (its facts are not in dispute, only their weight). If C5 is kept, merge it into C2.

### Notes per claim

**C1 Durability vs pull-in/digestion**
- Management's 2025 calls missed on the conservative side:
  - In Jul 2025 it expected a temporary 2H FY2025 digestion [C] (CL-008).
  - In Oct 2025 it expected a softer Q3 [C] (CL-010).
  - In Jan 2026 it said the digestion "did not occur" thanks to pull-in [C] (CL-011).
- In FY2025 Q3 (Oct-Dec 2025), SoC sales fell 4.9% QoQ but total sales rose 4.1%, helped by memory (+30.5%) [I] (CL-116, High).
- [I] Pull-ins cut both ways, so management's own near-term calls do not settle C1 either way (CL-128, Medium).
- TechNews reported Advantest saying it would watch for double ordering [S] (CL-110). No such wording appears in Advantest's saved English documents.
- Checkpoint: management will give a quantitative CY2027 outlook in January 2027 [C] (CL-003).

**C2 Share vs Teradyne dual sourcing**
- Advantest gives no share split by GPU, ASIC or CPU. It says V93000 configurations are similar across compute applications and customers can buy capacity and reconfigure it [C] (CL-072).
- Teradyne's dated milestones (mid-2027, 2027, 2H 2027) are the testable part of the dispute [C] (CL-045, CL-046, CL-047).

**C3 Memory/HBM**
- Advantest and Teradyne each claim leadership in different parts of memory test:
  - Advantest put its total memory tester share at around 60% [C] (CL-051).
  - Teradyne claims the higher share in HBM performance test [C] (CL-054).
- [I] Memory fell from 20.2% to 13.1% of Advantest's SoC+memory sales between FY25 Q2 and FY26 Q2 (CL-114, High).

**C4 China**
- Within six months, management's description moved from "around 20% to 25%" (Jan 2026) [C] (CL-132), also reported by RCR [S] (CL-062), to "approximately 19%" and "20% level or lower" (Jul 2026) [C] (CL-060, CL-061).
- Q2 FY26 China sales grew for both SoC and memory testers [F] (CL-063).
- Whether Advantest's testers fall under ECCN 3B992 is not disclosed by the company (see A4 gaps). The 2025-2026 BIS rules saved here set dates for the affiliates stay, remote access and data-centre licences [F] (CL-104, CL-105, CL-106). Module A4 judges that such rules reach Advantest through its customers [I] (A4-404).

**C6 Margins: one-offs named by management** (shown with and without, per the project rules)

| Period | Operating margin reported | Ex named one-offs | One-off named | Tag (ids) |
|---|---|---|---|---|
| FY2024 (Apr 2024-Mar 2025) | 29.3% | 32.0% | ~JPY 21.4 bn impairment in Q4 FY24 [F] (CL-038) | [I] (CL-121) |
| FY2025 (Apr 2025-Mar 2026) | 44.2% | 44.0% | ~JPY 2.5 bn divestiture gain in Q1 FY25 [F] (CL-038) | [I] (CL-121) |
| FY2026 Q2 (Jul-Sep 2026) | 55.9% [F] (CL-025) | cannot be computed | 1H inventory write-down reversal, amount not disclosed [C] (CL-073) | - |
| FY2026e (Apr 2026-Mar 2027) | 51.9% [C] (CL-034) | cannot be computed | same | - |

- Q2 FY26 financial income of JPY 14.7 bn (valuation gains on investment securities) sits below operating income. It affects pre-tax and net income, not the operating margin [F] (CL-031).
- [I] The MTP3 three-year aggregate operating margin is 44.9% (45.4% ex one-offs), against the revised target of 33-36% (CL-121, Medium). FY2026 in that figure is a forecast.

**C7 Capacity**
- The next-step target moved within three months: "15,000 systems or more" (Jul 2026) [C] (CL-085), then a doubling to 20,000 called a "Herculean effort" (Nov 2026) [C] (CL-084).
- Management says contract manufacturing keeps its cost base variable and limits risk [C] (CL-090).

## (b) B2 candidates

**Facts that most weaken the optimistic reading**
1. Management itself credited 2025 strength to demand pull-ins [C] (CL-009, CL-011). It had forecast a 2H FY2025 correction [C] (CL-131).
2. Concentration:
   - FY2025 sales to the NVIDIA Group were JPY 243,735m [F] (CL-068).
   - NVIDIA International alone was 20.2% of sales [F] (CL-069).
   - The top five customers were about 50% [F] (CL-070).
3. The 1H FY2026 margin included a one-time inventory write-down reversal of undisclosed size [C] (CL-073). Management names DRAM costs as a 2H headwind [C] (CL-074).
4. Memory test position:
   - Advantest's memory share fell about 2 points in CY2025 and may fall again in 2026 [C] (CL-051, CL-052).
   - Q2 FY26 memory sales were JPY 53.4 bn [F] (CL-028), against 54.6 bn in FY24 Q3 [F] (CL-029).
   - In the same months Teradyne posted record memory revenue of USD 301m [F] (CL-055).
5. Teradyne dates dual-vendor ramps in 2027: a hyperscaler mid-2027, a merchant GPU customer in 2027, and a second hyperscaler in 2H 2027 [C] (CL-045, CL-046, CL-047).
6. Inventories rose from JPY 231,718m to 352,426m in six months [F] (CL-088). The company's own risk factor names excess inventory and obsolescence [F] (CL-089).

**Facts that most weaken the pessimistic reading**
1. Record FY2026 Q2 (Jul-Sep 2026): sales JPY 477.7 bn [F] (CL-024), operating margin 55.9% [F] (CL-025), SoC test systems JPY 353.3 bn [F] (CL-027).
2. Growth broadened beyond GPUs: CPU testing for agentic AI was the biggest factor in the FY2026 upgrade [C] (CL-071). Teradyne also reports compute demand far above supply [C] (CL-020) and a rising test share of semiconductor capex [C] (CL-018).
3. The 2H FY2025 digestion management expected did not occur [C] (CL-011). Total quarterly sales rose from JPY 262.9 bn to 273.8 bn to 328.1 bn [F] (CL-030).
4. Balance sheet:
   - The only bond is the CB due 28 Mar 2031 [F] (CL-103).
   - Borrowings were nil at 31 Mar 2026 [F] (A5-003, A5-004).
   - A buyback of up to JPY 280 bn runs to 24 Mar 2027 [F] (CL-099).
5. China share has held near 19%: JPY 90.1 bn of 477.7 bn in FY26 Q2 [F] (CL-059, CL-024). Management guides to 20% or lower [C] (CL-061).
6. Customers now give 18-month forecasts, up from about six months [C] (CL-014).

## (c) Dated catalysts, Nov 2026 - Nov 2027

| Date | Event | Relevance | Tag (ids) |
|---|---|---|---|
| 2026-11-30 | Teradyne presents at the UBS Global Technology and AI Conference | read-across for C2 and C8 | [F] (CL-108) |
| 2026-12-01 | Interim dividend payment, JPY 49 per share | returns | [F] (CL-093) |
| 2027-01-10 | BIS stay of the Affiliates rule (90 FR 47201) ends unless extended again | C4 (customer-side controls) | [F] (CL-104) |
| 2027-01-19 | Comment deadline for the BIS remote-access IFR (effective 2026-11-19) | C4 | [F] (CL-105) |
| January 2027 (day not committed) | Q3 FY2026 results. First quantitative CY2027 tester-market outlook; capacity timing may follow | C1, C7, C8 | [F] (CL-094); outlook [C] (CL-003) |
| 2027-02-17 | Licence deadline for existing data-centre compute providers under the remote-access IFR (90 days after effective date) | C4 (customer-side) | [I] (CL-123) |
| Teradyne Q4 2026 call (date not committed) | Updated Teradyne target earnings model, including the ATE TAM | C2, C8 | [C] (CL-080) |
| 2027-03-24 | End of the buyback period. Cap is JPY 280 bn / 11m shares; JPY 265.4 bn of headroom remained after 31 Oct 2026 | returns | [F] (CL-099); [I] (CL-124) |
| 2027-03-31 | FY2026 ends, and with it MTP3 (targets are FY2024-FY2026 averages) | C6 | [F] (CL-101); targets [C] (CL-077) |
| 2027-03-31 or 2027-05-15 (company pages conflict) | Record date for AGM voting rights | governance | [F] (CL-095, CL-097) |
| Late April 2027 (date not committed) | FY2026 full-year results and FY2027 guidance | all | [I] (CL-127) |
| Around May 2027 (date not committed) | Fourth Mid-Term Management Plan, with outlook through CY2028-CY2029; a doubling to 20,000 SoC systems/yr is under internal discussion | C1, C7 | [C] (CL-102, CL-084) |
| May-Aug 2027 (date not committed; the 84th AGM was 31 Jul 2026) | 85th AGM | governance | [I] (CL-126) |
| Mid-2027 | Teradyne: next major ramp at its first hyperscaler | C2 | [C] (CL-045) |
| 2027 (no date) | Teradyne: additional revenue from its merchant GPU customer | C2 | [C] (CL-046) |
| 2H 2027 | Teradyne: capacity buys at its second hyperscaler | C2 | [C] (CL-047) |
| Date not committed | 10,000 SoC systems/yr: original target end FY2028 (Mar 2029), now aimed "roughly a year in advance"; the company says the timeline is not yet fixed. This likely falls outside the window | C7 | [C] (CL-082, CL-083) |
| Date not committed | Phase 2 of the Section 232 action: broader semiconductor tariffs after trade negotiations. The 25% tariff on a narrow chip category has applied since 2026-01-15; no tariff on semiconductor equipment is set | C4, C6 | [F] (CL-107) |
| Date not committed | New memory tester products with customer commitments, aimed at recovering memory share | C3 | [C] (CL-052) |
| None in window | Debt maturities: the CB is due 2031-03-28 and there are no borrowings | - | [I] (CL-125); [F] (CL-103) |
| - | Lock-ups: none identified. The CB offering's lock-up terms were not retrieved (see gaps) | - | - |

Missing items are listed in `parts/CL_gaps.md`.
