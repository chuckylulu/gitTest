# CL - Candidate disputed claims (B1), facts for B2, dated catalysts (B3)

Advantest Corporation, TSE Prime 6857, Japan. The fiscal year ends 31 March, and Advantest names fiscal years by start year (FY2026 = Apr 2026-Mar 2027). IFRS, JPY.

- Evidence ids refer to `parts/CL.csv` (CL-001 to CL-143). The cross-references A5-003 and A5-004 point to module A5.
- Arithmetic is in `calc/CL_*.py`; each script's output is in the matching `.out.txt`.
- Teradyne reports by calendar quarter. Its Q3 2026 (quarter ended 27 Sep 2026) covers about the same months as Advantest's FY2026 Q2 (Jul-Sep 2026).
- The verification log for this module is `parts/CL_verify.md`.

## Premise notes

- **Run facts.** They hold. FY2026 Q2 (Jul-Sep 2026) results are dated 28 Oct 2026 [F] (CL-032). MTP3 runs FY2024-FY2026, so it ends 31 Mar 2027 [F] (CL-101).
- **AGM month.** The 84th AGM was held on 31 Jul 2026, not in June [F] (CL-096). The Integrated Annual Report 2026 gives the same date [F] (CL-134). The 27 Jun 2025 AGM amended the Articles so that the meeting can be held in July [F] (CL-098, CL-134).
- **Record dates: what each document prints.**
  - IR calendar: "Mar.31 Record date for the Voting rights at the ordinary general meeting of shareholders and for the distribution of year-end dividend" [F] (CL-095).
  - Share Information page: "Ordinary general meeting of shareholders: May 15"; "Year-end dividend: March 31" [F] (CL-097).
  - 84th annual securities report (statutory filing): May 15 of each year is the record date for voting rights; the meeting is held within three months of it; dividend record dates are 30 Sep and 31 Mar [F] (CL-133).
  - Integrated Annual Report 2026: the record date for voting rights moved from March 31 to May 15 [F] (CL-134).
  - [I] For voting rights, 15 May governs. The IR calendar line looks outdated: it printed the same 31 Mar line for the 84th AGM, whose record date the filing gives as 15 May 2026. 31 Mar remains the record date for the year-end dividend (CL-126, Medium).
- **Next results date.** The IR calendar gives only "January 2027" for the Q3 FY2026 results [F] (CL-094).
- **Next mid-term plan.** There is no fixed date for MTP4, only "around May 2027" [C] (CL-102).
- **Press dates.** The source files now carry their printed dates: TrendForce 2026-10-05, Wing VC 2026-11-18, Simply Wall St 2026-10-29 (last update; first published 2025-06-06).
- **Press error.** RCR Wireless (CL-021) describes the January 2026 guidance (sales JPY 1,070.0 bn, OI JPY 454.0 bn) as being for the year to 31 Mar 2027. The company document shows it was the FY2025 (Apr 2025-Mar 2026) forecast [C] (CL-130).
- **TechNews figures.** TechNews (15 Jan 2026) relayed a "USD 8 bn 2026 ATE peak" attributed to Advantest [S] (CL-109). Advantest's own estimate of 28 Jan 2026 was USD 10.7-12.2 bn for CY2026 [C] (CL-138). [I] The TechNews number is 2.7 bn below even that low end and is not traceable to a company document, so it is no longer used as evidence (CL-129, High).
- **Simply Wall St source.** The page source says the author "AnalystLowTarget is a tool utilizing a Large Language Model (LLM)". The narrative is an LLM synthesis of consensus data, not the view of an identifiable analyst. It is kept as [S] context only (CL-023, CL-091) and is not used as evidence on any ledger side. Its valuation content is excluded under the project rules.

## (a) Candidate disputed claims (8 candidates; the B1 ledger keeps 6)

| # | Claim | Who said it, when | Evidence for | Evidence against | Strongest tag on each side |
|---|---|---|---|---|---|
| C1 | AI-driven tester demand is durable: tester TAM keeps growing about 50% a year, with no slowdown into CY2027 | Advantest management, 28 Oct 2026 (CL-001, CL-002, CL-004); Teradyne CEO, 28 Oct 2026 (CL-018, CL-020) | No slowing seen [C] (CL-002); supply constrained in CY2027 [C] (CL-005); CY2026 TAM estimate raised from USD 10.7-12.2 bn (Jan 2026) to 13.0-14.5 bn (Oct 2026) [C] (CL-138, CL-007), +2.3 bn [I] (CL-129); 18-month customer forecasts [C] (CL-014); forecast 2H FY2025 digestion did not occur [C] (CL-011); FY2026 Q2 sales +81.7% YoY [F] (CL-024), same on the tanshin basis [I] (CL-141) | Management credited 2025 strength to demand pull-ins [C] (CL-009, CL-011) after expecting a correction [C] (CL-131); Teradyne revenue -1.7% QoQ in Q3 2026 [F] (CL-137) and Q4 guide midpoint -0.5% vs Q3 [C] (CL-136), [I] (CL-139), with 2H compute "program timing" [C] (CL-019); capex is "highly fluid" [F] (CL-012); analysts saw a trade-statistics divergence [S] (CL-016) that Advantest declined to explain [F] (CL-017); digestion "worth tracking into 2027" [S] (CL-022) | For: [F] for current demand only; [C] for durability. Against: [F] for Teradyne's own revenue and the generic risk text; [C] for anything specific to Advantest |
| C2 | Advantest's SoC tester share keeps rising, from 66% (CY2025) to above 70%, including GPU/AI accelerators | Advantest management, 27 Apr and 28 Oct 2026 (CL-039 to CL-041) | Share 56% to 66% [C] (CL-039); majority of the AI accelerator tester market [C] (CL-041); SoC test system sales +103.4% YoY [I] (CL-114, from [F] CL-029) vs Teradyne compute "nearly 50%" [F] (CL-049), a gap of at least 53 points [I] (CL-115, Low: scopes differ); "replacement risk approaches zero" [S] (CL-050) | Teradyne expects share gains from dual-vendor adoption [C] (CL-044); dated ramps mid-2027, 2027 and 2H 2027 [C] (CL-045 to CL-047); dual-vendor share range 30-70% [C] (CL-048); Advantest concedes customers may consider dual-vendor strategies [C] (CL-043) | For: [C] for share; [F] only for the growth inputs, whose scopes differ. Against: [C] |
| C3 | Rising HBM/DRAM test intensity will lift Advantest's memory tester business | Advantest, 28 Oct 2026 (CL-053); TrendForce, 5 Oct 2026 (CL-057) | Memory TAM from USD 2.1 bn (CY2025) to 2.5-3.0 bn (CY2026e) [C] (CL-007); DRAM back-end growth expected [C] (CL-053); memory sales +21.6% YoY in FY2026 Q2 [I] (CL-114); test equipment may outgrow HBM output [S] (CL-057) | Memory share fell about 2 points in CY2025 and may fall again in 2026 [C] (CL-051, CL-052); FY2026 Q2 memory sales JPY 53.4 bn [F] (CL-028), 6.8% below FY2025 Q3 and 2.2% below FY2024 Q3 [I] (CL-114) while SoC sales doubled; Teradyne record memory revenue of USD 301m [F] (CL-055); Teradyne claims the higher HBM performance-test share [C] (CL-054); HBM4 wafer-test orders to Digital Frontier and UniTest [S] (CL-056); TBSTest near 15% of China's memory ATE [S] (CL-058) | For: [C]. Against: [F] |
| C4 | China sales stay at about 20% of sales or less, and export controls have limited direct effect | Advantest management, 28 Jan 2026 (CL-067) and 29 Jul 2026 (CL-060, CL-061) | About 19% [C] (CL-060); China ship-to share 18.9% in FY2026 Q1 and Q2, LTM 19.5% [I] (CL-118, from [F] CL-059, CL-024, CL-030); no major tariff impact expected [C] (CL-067) | China sales JPY 90.1 bn in FY2026 Q2 vs 52.1 bn a year earlier [F] (CL-059), +72.9% [I] (CL-118); in Jan 2026 management gave 20-25% [C] (CL-132); EAR 3B992.b.4.b covers IC testers above a 20 MHz pattern rate [F] (CL-066), but whether Advantest's testers fall there is not disclosed; Chinese tester competitors named by Advantest [F] (CL-065); dated BIS rules on affiliates and remote access [F] (CL-104 to CL-106); no Advantest statement on the Nov 2026 rule (see gaps) | For: [F] for the share inputs; [C] for the outlook. Against: [F] for rule texts and sales levels; no document links a rule to Advantest's own sales |
| C5 | Concentration in a few AI customers (NVIDIA Group above 20%) is Advantest's main tail risk | Wing VC, 18 Nov 2026 [S] (CL-022); Advantest risk factor (CL-070) | NVIDIA Group JPY 243,735m [F] (CL-068), 21.6% of sales [I] (CL-119); NVIDIA International 20.2% [F] (CL-069); top five about 50% (FY2024 about 48%) [F] (CL-070) | CPU demand was the biggest factor in the FY2026 upgrade [C] (CL-071); V93000 capacity can be reconfigured across compute devices [C] (CL-072) | For: [F]. Against: [C] |
| C6 | An operating margin of 50% or more is sustainable | Advantest management, 28 Oct 2026 (CL-034, CL-075) | FY2026 Q2 OPM 55.9% [F] (CL-025) and GM 71.1% [F] (CL-026); the 1H margin includes a one-off of undisclosed size (CL-073); FY2026 forecast 51.9% [C] (CL-034); 2H forecast "low 50%" range [C] (CL-075), raised about 3 points from 47.3% [C] (CL-035) | One-time inventory write-down reversal in 1H, amount not disclosed [C] (CL-073); DRAM cost headwind [C] (CL-074); Q4 FY2025 "optimal mix" may not recur [C] (CL-076); implied 2H 50.1% vs 1H 54.0% [I] (CL-117) | For: [F] for the current quarter; [C] for sustainability. Against: [C] |
| C7 | Supply capacity, not demand, is the binding constraint | Wing VC, 18 Nov 2026 [S] (CL-092); Advantest, 28 Oct and 12 Nov 2026 (CL-005, CL-015, CL-086) | Capacity above 5,000 systems/yr, 10,000 brought forward, 20,000 under discussion [C] (CL-081 to CL-083, CL-143); demand exceeds supply [C] (CL-015); memory parts tight [C] (CL-086); DDR4 being stockpiled [C] (CL-087); Teradyne says compute demand far exceeds supply [C] (CL-020) | Inventories JPY 231.7 bn to 352.4 bn [F] (CL-088), +52.1% in six months [I] (CL-120); company risk factor on excess inventory and obsolescence [F] (CL-089); CEO puts meeting demand ahead of write-down risk [C] (CL-140); 10,000 timing not final [C] (CL-083); Teradyne's flat Q4 guide [I] (CL-139) | For: [C]. Against: [F] for the inventory level, but the build matches the company's stated strategic stocking (CL-087, CL-140), so it is not direct evidence of weak demand |
| C8 | Tester TAM: Advantest's ~50%/yr growth and CY2026e USD 13.0-14.5 bn vs Teradyne's 15-25% CAGR to USD 12-14 bn | Advantest, 28 Oct 2026 (CL-001, CL-007); Teradyne target model, updated 3 Feb 2026 and shown 28 Oct 2026 (CL-079) | CY2024 to CY2025 +50.0%, CY2026e +44.4% to +61.1% [I] (CL-112); CY2026e raised by USD 2.3 bn since Jan 2026 [I] (CL-129) | Teradyne model [C] (CL-079); Advantest's CY2026e already overlaps Teradyne's target band [I] (CL-113). The TechNews USD 8 bn figure is dropped as evidence (see premise notes) | For: [C]. Against: [C] |

**Recommended six for B1:** C1, C2, C3, C4, C6, C7.
- C1: the central dispute (durable demand vs pull-in and digestion), with dated checkpoints in January 2027.
- C2: the share dispute has dated Teradyne milestones in 2027 that will test it.
- C3: the only candidate where the "against" side rests on [F] figures from both companies.
- C4: regulatory dates fall inside the catalyst window (Jan-Feb 2027), and management's own range has moved.
- C6: the margin claim depends on an undisclosed one-off, a cost headwind the company named, and an implied 2H decline.
- C7: inventory and capacity statements point in different directions, and the January 2027 outlook and the May 2027 MTP4 will update them.
- Drop C5: its facts are not in dispute, only their weight. Use it in B2 and as the main vulnerability.
- Drop C8: both sides are company models, it overlaps C1, and Teradyne's target year is not stated.

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
- Teradyne's dated milestones (mid-2027, 2027, second half of 2027) are the testable part of the dispute [C] (CL-045, CL-046, CL-047).

**C3 Memory/HBM**
- Advantest and Teradyne each claim leadership in different parts of memory test:
  - Advantest put its total memory tester share at around 60% [C] (CL-051).
  - Teradyne claims the higher share in HBM performance test [C] (CL-054).
- [I] Memory fell from 20.2% to 13.1% of Advantest's SoC+memory sales between FY2025 Q2 and FY2026 Q2 (CL-114, High).

**C4 China**
- Within six months, management's description moved from "around 20% to 25%" (Jan 2026) [C] (CL-132), also reported by RCR [S] (CL-062), to "approximately 19%" and "20% level or lower" (Jul 2026) [C] (CL-060, CL-061).
- The computed shares fit the July statement: 18.9% in FY2026 Q1 (Apr-Jun 2026) [I] (CL-118).
- FY2026 Q2 China sales grew for both SoC and memory testers [F] (CL-063).
- Whether Advantest's testers fall under ECCN 3B992 is not disclosed by the company (see A4 gaps). The 2025-2026 BIS rules saved here set dates for the affiliates stay, remote access and data-centre licences [F] (CL-104, CL-105, CL-106). Module A4 judges that such rules reach Advantest through its customers [I] (A4-404).

**C6 Margins: one-offs named by management** (shown with and without, per the project rules)

| Period | Margin reported | Ex named one-offs | One-off named by management | Tag (ids) |
|---|---|---|---|---|
| FY2024 (Apr 2024-Mar 2025) | OPM 29.3% | 32.0% | ~JPY 21.4 bn impairment in Q4 FY2024 [F] (CL-038) | [I] (CL-121) |
| FY2025 (Apr 2025-Mar 2026) | OPM 44.2% | 44.0% | ~JPY 2.5 bn divestiture gain in Q1 FY2025 [F] (CL-038) | [I] (CL-121) |
| FY2026 1H (Apr-Sep 2026) | OPM 54.0% | NOT DISCLOSED (read: Q2 FY2026 Financial Briefing Q&A Summary, A5; FY2026 Q2 Consolidated Financial Results; 85th semi-annual securities report) - amount of the inventory write-down reversal | 1H inventory write-down reversal [C] (CL-073) | [I] (CL-117) |
| FY2026 Q2 (Jul-Sep 2026) | OPM 55.9% [F] (CL-025); GM 71.1% [F] (CL-026) | not computable (same NOT DISCLOSED item) | same reversal; its split between Q1 and Q2 is not given | - |
| FY2026 2H (Oct 2026-Mar 2027), implied | OPM 50.1% [I] (CL-117); company says "low 50%" [C] (CL-075) | no one-off named for 2H | DRAM cost increase is a named headwind, not a one-off [C] (CL-074) | [I] (CL-117) |
| FY2026e (Apr 2026-Mar 2027) | OPM 51.9% [C] (CL-034) | not computable (same NOT DISCLOSED item) | same reversal | - |
| MTP3 three-year aggregate (FY2024-FY2026e) | 44.9% | 45.4% (FY2026 not adjustable) | the items above | [I] (CL-121, Medium) |
| Teradyne Q3 2026 (quarter ended 27 Sep 2026) | GAAP OPM 30.8% [F] (CL-135) | non-GAAP 31.6% [F] (CL-078, CL-135) | acquired intangibles amortization USD 5.3m, restructuring and other 2.0m, ERP related 3.7m [F] (CL-135) | [I] (CL-122) |

- FY2026 Q2 financial income of JPY 14.7 bn (valuation gains on investment securities) sits below operating income. It affects pre-tax and net income, not the operating margin [F] (CL-031).
- [I] The MTP3 three-year aggregate operating margin is 44.9% (45.4% ex one-offs), against the revised target of 33-36% (CL-121, Medium). FY2026 in that figure is a forecast.
- [I] Advantest's FY2026 Q2 OPM was 25.1 points above Teradyne's GAAP margin and 24.3 points above its non-GAAP margin (CL-122, Medium). Accounting bases and portfolios differ, and Advantest's figure includes the undisclosed reversal, so this is context rather than evidence on either side of C6.

**C7 Capacity**
- The next-step target moved within three months:
  - "15,000 systems or more" (29 Jul 2026) [C] (CL-085).
  - A doubling to 20,000, "under active internal discussion based on customer demand" (28 Oct 2026) [C] (CL-143).
  - On 12 Nov 2026 management called 20,000 a "Herculean effort" needing more time, but "real numbers" the industry needs [C] (CL-084).
- Management says contract manufacturing keeps its cost base variable and limits risk [C] (CL-090).
- The Group CEO says management and the Board see strategic inventory as "gold" and worry more about meeting demand than about write-downs [C] (CL-140).

## (b) B2 candidates

**Facts that most weaken the optimistic reading** (recommended three marked *)
1. \* Concentration:
   - FY2025 sales to the NVIDIA Group were JPY 243,735m [F] (CL-068).
   - NVIDIA International alone was 20.2% of sales [F] (CL-069).
   - The top five customers were about 50% [F] (CL-070).
2. \* Inventories rose from JPY 231,718m to 352,426m in six months [F] (CL-088). The company's own risk factor names excess inventory and obsolescence [F] (CL-089).
3. \* Memory test position:
   - FY2026 Q2 memory sales were JPY 53.4 bn [F] (CL-028), below 57.3 bn in FY2025 Q3 and 54.6 bn in FY2024 Q3 [F] (CL-029).
   - In the same months Teradyne posted record memory revenue of USD 301m [F] (CL-055).
   - Advantest's memory share fell about 2 points in CY2025 and may fall again in 2026 [C] (CL-051, CL-052).
4. Management itself credited 2025 strength to demand pull-ins [C] (CL-009, CL-011). It had forecast a 2H FY2025 correction [C] (CL-131).
5. The 1H FY2026 margin included a one-time inventory write-down reversal of undisclosed size [C] (CL-073). Management names DRAM costs as a 2H headwind [C] (CL-074).
6. Teradyne dates dual-vendor ramps in 2027: a hyperscaler mid-2027, a merchant GPU customer in 2027, and a second hyperscaler in the second half of 2027 [C] (CL-045, CL-046, CL-047). Its total revenue fell QoQ in Q3 2026 [F] (CL-137), and it guides Q4 flat [C] (CL-136).

**Facts that most weaken the pessimistic reading** (recommended three marked *)
1. \* Record FY2026 Q2 (Jul-Sep 2026): sales JPY 477.7 bn [F] (CL-024), operating margin 55.9% [F] (CL-025), SoC test systems JPY 353.3 bn [F] (CL-027). The tanshin year-to-date figures give the same values [I] (CL-141).
2. \* Balance sheet:
   - The only bond is the CB due 28 Mar 2031 [F] (CL-103).
   - Borrowings were nil at 31 Mar 2026 [F] (A5-003, A5-004).
   - A buyback of up to JPY 280 bn runs to 24 Mar 2027 [F] (CL-099).
3. \* The 2H FY2025 digestion management expected did not occur [C] (CL-011). Single-quarter sales rose from JPY 262.9 bn (FY2025 Q2) to 273.8, 328.1 and 367.5 bn [F] (CL-030), then 477.7 bn [F] (CL-024).
4. Growth broadened beyond GPUs: CPU testing for agentic AI was the biggest factor in the FY2026 upgrade [C] (CL-071). Teradyne also reports compute demand far above supply [C] (CL-020) and a rising test share of semiconductor capex [C] (CL-018).
5. China share has held near 19%: JPY 90.1 bn of 477.7 bn in FY2026 Q2 [F] (CL-059, CL-024). Management guides to 20% or lower [C] (CL-061).
6. Customers now give 18-month forecasts, up from about six months [C] (CL-014).

## (c) Dated catalysts, Nov 2026 - Nov 2027

| Date | Event | Relevance | Tag (ids) |
|---|---|---|---|
| 2026-11-30 | Teradyne presents at the UBS Global Technology and AI Conference | low: possible read-across for C2 | [F] (CL-108) |
| 2026-12-01 | Interim dividend payment, JPY 49.00 per share (record date 30 Sep 2026) | returns | [F] (CL-093) |
| 2027-01-10 | BIS stay of the Affiliates rule (90 FR 47201) ends unless extended again | C4 (customer-side controls) | [F] (CL-104) |
| 2027-01-19 | Comment deadline for the BIS remote-access IFR (effective 2026-11-19) | C4 | [F] (CL-105) |
| January 2027 (day not given) | Q3 FY2026 results. First quantitative CY2027 tester-market outlook; possibly more detail on the 10,000-system date | C1, C7, C8 | [F] (CL-094); outlook [C] (CL-003, CL-143) |
| 2027-02-17 | Licence deadline for existing data-centre compute providers under the remote-access IFR (90 days after the effective date) | C4 (customer-side) | [I] (CL-123) |
| Teradyne Q4 2026 call (date not given) | Updated Teradyne target earnings model, including the ATE TAM; Q4 actual vs USD 1,250-1,350m guide | C1, C2, C8 | [C] (CL-080, CL-136) |
| 2027-03-24 | End of the buyback period. Cap is JPY 280 bn / 11 million shares; JPY 265.4 bn of headroom remained after 31 Oct 2026 | returns | [F] (CL-099); [I] (CL-124) |
| 2027-03-31 | FY2026 ends, and with it MTP3 (targets are FY2024-FY2026 averages). Record date for the year-end dividend | C6, returns | [F] (CL-101, CL-133); targets [C] (CL-077) |
| 2027-05-15 | Record date for voting rights at the 85th AGM (the IR calendar's 31 Mar line conflicts) | governance | [F] (CL-133, CL-097, CL-134); [I] (CL-126) |
| Late April 2027 (date not committed) | FY2026 full-year results and FY2027 guidance | all | [I] (CL-127) |
| Around May 2027 (date not committed) | Fourth Mid-Term Management Plan, with outlook through CY2028-CY2029; a doubling to 20,000 SoC systems/yr is under internal discussion | C1, C7 | [C] (CL-102, CL-143) |
| 15 May-15 Aug 2027 (date not committed; the 84th AGM was 31 Jul 2026) | 85th AGM | governance | [I] (CL-126) |
| Mid-2027 | Teradyne: next major ramp at its first hyperscaler | C2 | [C] (CL-045) |
| 2027 (no date) | Teradyne: additional revenue from its merchant GPU customer | C2 | [C] (CL-046) |
| Second half of 2027 | Teradyne: capacity buys at its second hyperscaler | C2 | [C] (CL-047) |
| Date not committed | 10,000 SoC systems/yr: original target end FY2028 (Mar 2029), now aimed "roughly a year in advance"; the company says the schedule is not final. This likely falls outside the window. A later doubling to 20,000 needs "some additional time" | C7 | [C] (CL-082, CL-083, CL-084) |
| Date not committed | Phase 2 of the Section 232 action: broader semiconductor tariffs after trade negotiations. The 25% tariff on a narrow chip category has applied since 2026-01-15; no tariff rate on semiconductor equipment is set | C4, C6 | [F] (CL-107) |
| Date not committed | New memory tester products with customer commitments, aimed at recovering memory share | C3 | [C] (CL-052) |
| None in window | Debt maturities: the CB is due 2031-03-28 and there are no borrowings | - | [I] (CL-125); [F] (CL-103) |
| - | Lock-ups: none identified. The CB offering's lock-up terms were not retrieved (see gaps) | - | - |

Missing items are listed in `parts/CL_gaps.md`.
