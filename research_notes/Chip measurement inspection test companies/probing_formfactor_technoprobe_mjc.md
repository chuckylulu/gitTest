# Wafer probing and test interfaces for stacked/bonded chips: FormFactor, Technoprobe, Micronics Japan, the wider field, and the limits of probing dense bond arrays

**Research date: 12 November 2026.** Status: **v1, interim** (written after an interruption; the field scan, wafer-prober share and finest-production-pitch items are INCOMPLETE and are being worked on in a gap pass).
Method: primary filings fetched directly (SEC EDGAR; Technoprobe IR / eMarket Storage; Micronics Japan TDnet PDFs via eir-parts). Market data from stockanalysis.com checked 12 Nov 2026. "my calc" = arithmetic on cited figures. "company claim, unconfirmed" = statement by the company that no outside party confirms. Source tags like [S3] are links; the full list with dates is at the end.

Latest periods used: FormFactor Q3 FY2026 (quarter to 26 Sep 2026; released 28 Oct 2026; 10-Q filed 3 Nov 2026). Technoprobe 9M 2026 (to 30 Sep 2026; released 11 Nov 2026, unaudited). Micronics Japan (MJC) Q3 FY2026 (Jan-Sep 2026; released 12 Nov 2026 15:30 JST, after the Tokyo close).

---

## A. Evidence tables (quality tests a-e and transitions; entry-point data kept separate in table A4 and section 7)

### A1. FormFactor (FORM, Nasdaq, Livermore USA)

| Test | Evidence (dated) |
|---|---|
| (a) Position | Sells the physical contact interface for wafer sort (probe cards; ~79% of Q3'26 revenue, my calc from Systems $59.5M of $280.5M [S3][S4]) plus engineering probe stations / cryogenic / photonic systems (~21%). Cards are "customized to our customers' unique wafer and chip designs" [S9]. Owns a physical constraint (fine-pitch, high-frequency MEMS contact at volume); does not own the test program or the pass/fail data (inference). |
| (b) Lead | Audited customer disclosure: SK hynix 22.9% of FY2025 revenue (only >10% customer for the year) [S9]; SK hynix 20.7% of Q3'26 and 24.5% of 9M'26; TSMC 12.8% of Q3'26 and 11.2% of 9M'26; Intel 11.2% of 9M'25, <10% in 2026 [S5]. Third-party share: TechInsights data (charted by MJC, Aug 2026) show two suppliers at 22% and 20% of the $3.19bn 2025 market, consistent with Technoprobe and FormFactor, but labels are not shown, so could not verify which is which [S32]. 10-K gives no numerical share; "compete favorably" is a company claim, unconfirmed [S9]. |
| (c) Revenue model | Design-specific cards: new cards with each new chip design or node; no service, software, subscription or usage line found in filings read. Systems segment is one-off capital equipment. Deferred revenue $36.6M (26 Sep 2026) vs $20.1M (27 Dec 2025) [S5]. No revenue tied to labour hours identified. |
| (d) Financial strength | Q3'26 revenue $280.5M (+38.4% y/y, +8.6% q/q); GAAP GM 54.7%, non-GAAP 56.5%; GAAP op. income $81.6M (29.1% margin, my calc); non-GAAP EPS $1.04; FCF $64.8M; 9M'26 FCF $148.1M (OCF $211.0M, capex $64.4M) [S3]. ~380 bps of Q3 GM (~$10.5M, ~$0.09 EPS) came mainly from tariff refunds and favourable Quantum subcomponent costs, not expected to recur (third-party call summary) [S4]. Cash $138.2M + securities $257.2M; debt $11.4M; $150M revolver undrawn [S3][S5]. ROIC 23.6% TTM (stockanalysis) [S11]. Concentration: SK hynix + TSMC = 33.5% of Q3'26 [S5]. China ~7% of FY2025 revenue vs 14% FY2024 [S9]. |
| (e) Resilience | Heavily tied to HBM at SK hynix (20-25% of revenue each quarter of 2025-26) [S5][S9]. Capacity-limited: CEO says productivity gains from existing footprint "are moderating as we approach its capacity limits" [S3]; Farmers Branch, Texas plant shipped first production unit; ~$400M/yr probe-card capability by end-2027, "capacity, not guaranteed revenue" (call summary) [S4]. Export controls already cut China share by half (2024 to 2025) [S9]. Cycle: fourth straight record quarter; Q4 guide $285M ±$10M (+1.6% q/q at midpoint) [S3]. |
| T1 measurement→inference | Nothing found. |
| T2 AI-built designs/recipes | Nothing found. |
| T3 bonded stacks / packaging | DONE: HBM probe cards for 8-, 12- and 16-high stacks (10-K) [S9]; acquired Keystone Photonics 15 Dec 2025 ($20.6M net) for optical probing of silicon photonics, co-packaged optics (CPO) and near-packaged optics [S5]; Systems record $59.5M in Q3'26 on CPO / TRITON photonic systems [S3][S4]; 20% stake in HoldCo that bought substrate maker FICT with MBK Partners ($67.2M; FICT also a supplier) [S5]. SAID: Teradyne collaboration on HPC, advanced packaging, HBM and silicon photonics (12 Oct 2026) [S8]. Hybrid bonding not mentioned in 10-K [S9]. |
| T4 hardware→software/data | Nothing found beyond collaboration wording "from wafer to data center" (company claim, unconfirmed) [S8]. |
| T5 on-premises AI | Nothing found. |
| T6 fewer insertions after 2030 | No statement found. |

### A2. Technoprobe (TPRO, Euronext Milan, Cernusco Lombardone, Italy)

| Test | Evidence (dated) |
|---|---|
| (a) Position | Probe cards (logic-centric MEMS), plus final-test interface boards since buying Teradyne's Device Interface Solutions (DIS Tech) on 27 May 2024 [S15][S20]. "Custom-made for each specific chip" [S12]. Physical constraint + capacity; no data/test-program ownership (inference). |
| (b) Lead | Yole data cited by the company: 34% of the 2024 logic probe-card market ($1.6bn) and 60% of MEMS logic probe cards ($937M) (Yole Test Consumables monitor, Sep 2024, via company slide) [S16]. TechInsights (via MJC chart): 2025 non-memory leader at 33% of $2.149bn; the slice size (~$709M, my calc) matches Technoprobe's 2025 revenue (EUR 628.4M), but the chart does not label it [S32] (inference). No named customers or customer percentages in documents read. |
| (c) Revenue model | Design-specific cards and DIBs; no service/software split disclosed. Licence-style deal: WinWay may use Technoprobe's TPEG technology for 5 years with minimum purchases of ~US$60M (9 Dec 2025) [S24]. |
| (d) Financial strength | FY2025: revenue EUR 628.4M (+15.7%), GP 44.4%, EBITDA EUR 201.4M (32.1%), net profit EUR 98.8M [S15]. 9M'26: revenue EUR 787.4M (+68.8%), GP 56.8%, EBITDA EUR 376.3M (47.8%); Q3'26 revenue EUR 323.3M (+130% y/y, +16.7% q/q), GP 61.1%, EBITDA 52.6% [S12][S13]. Net financial position +EUR 799.8M (30 Sep 2026) [S12]. 9M OCF ~EUR 241M vs capacity capex ~EUR 150M (~EUR 91M FCF, my calc) [S12]. No dividend on 2025 profit (retained) [S15]; EUR 60M buyback completed 19 Dec 2025 [S15]. Customer and country concentration: not disclosed in documents read (could not verify). |
| (e) Resilience | End-markets FY2025: consumer 48%, AI/data centre 38%, auto/industrial 14% (company) [S16]. Q4'26 guide EUR 270M ±3% (-16% q/q), GM 54.2%, EBITDA 45.1%, blamed on ERP/MES go-live on 1 Oct 2026; FY26 guide narrowed to EUR 1,050-1,065M (top end cut from EUR 1,100M) [S12]. Capacity plan: ~EUR 1.6bn run-rate by Q1'27, ~EUR 2.0bn by end-2027 with further EUR 150-200M capex, "fully self-funded" [S13] (about 1.9x the 2026 revenue guide, my calc). China: Nexprobe (Shanghai/Suzhou, ~12,000 sqm) with a local partner holding 30% for US$35M (closed 14 Aug 2026), ramp in Q1 2027 [S13][S17]. |
| T3 stacks / packaging | SAID/DONE: HBM vertical MEMS probe cards "up to full-wafer coverage"; electro-optical probing for CPO with fibre-array positioning [S13]; "Enter the HBM segment" slides with HBM test flow (May 2026) [S16]; final-test boards via DIS Tech [S16]. "Advanced Packaging segment expected to accelerate over 2026-2027" (company) [S15]. |
| T6 insertions | Company says AI brings "increasing test intensity and more test insertions" (company claim, unconfirmed) [S13]. |
| T1, T2, T4, T5 | Nothing found. |

### A3. Micronics Japan (MJC, 6871.T, Tokyo; plants in Aomori and Oita)

| Test | Evidence (dated) |
|---|---|
| (a) Position | Memory probe cards (DRAM incl. HBM): memory = 94% of probe-card revenue in Q3'26 (JPY 30,371M of 32,304M, my calc) [S29]. Physical constraint + capacity. Small Test Equipment (TE) arm: testers (Testalio), engineering prober (Excelyze), sockets, FPD probes [S29]. |
| (b) Lead | TechInsights data (June 2026) charted by MJC: MJC 41% of the 2025 memory probe-card market ($1,019M), 40% in 2024 ($792M); 14% of the total market in 2025 ($3,192M), 13% in 2024 ($2,552M); 2% of non-memory [S32]. Third-party data, but the chart was prepared by the company. Customers not named. |
| (c) Revenue model | Probe cards 98.6% of 9M'26 sales; TE 1.4% and loss-making (9M segment loss JPY 1,142M) [S28]. Stopped disclosing orders/backlog after FY2025 ("not suitable" as an indicator) [S33]. |
| (d) Financial strength | FY2025: revenue JPY 70,173M (+26.1%), OP JPY 16,542M (23.6%), NI JPY 12,063M [S33]. 9M'26: revenue JPY 81,964M (+62.6%), OP JPY 26,993M (32.9%), NI JPY 19,506M; Q3'26 revenue JPY 32,757M (+89.4% y/y), GM 51.8%, OPM 34.9% [S29]. Cash JPY 28.0bn, borrowings JPY 6.4bn (net cash ~JPY 21.6bn, my calc), net assets JPY 99.0bn of JPY 147.6bn assets (30 Sep 2026) [S28]. ROE 26.2% TTM [S36]. Region: Asia ex-Japan 95.1% of Q3'26 sales [S29]; in 2025 quarters Korea 46-60% and Taiwan 27-37% [S33]. China not split out. |
| (e) Resilience | Single-segment exposure (DRAM/HBM). Q3'26 beat partly because some sales planned for Q4 were pulled into Q3 [S31]; FY guide implies Q4 revenue JPY 28.0bn, down from JPY 32.8bn in Q3 (my calc) [S30]. Capacity: Aomori new building (Dec 2024); extra JPY 24.1bn capex for 2027-2028 (approved 26 Mar 2026) [S34]; land bought next to Oita lab (31 Jul 2026) [S35]. |
| T3 stacks / packaging | SAID: developing "new technology for next-generation HBM" [S32][S33]. DONE: Testalio tester and Excelyze prober still "under customer evaluation" (no orders reported, Q3'26) [S29]. |
| T1, T2, T4, T5, T6 | Nothing found (glossary mentions DFT and BIST only). |

### A4. Entry-point snapshot (separate from quality; details in section 7)

| | FORM | TPRO.MI | 6871.T |
|---|---|---|---|
| Price / date | US$95.78, close 11 Nov 2026 (+11.85% that day) [S11] | EUR 22.76, 12 Nov 2026 12:49 CET [S26] | JPY 10,100, close 12 Nov 2026, before Q3 release [S36] |
| Market cap / EV | $7.51bn / $7.14bn | EUR 14.57bn / EUR 13.90bn | JPY 391.6bn / JPY 378.0bn |
| P/E trailing / forward | 44.1 / 23.7 | 70.8 (TTM to H1'26) / 34.2 | 20.9 (TTM to Q2'26) / 16.2; 14.6 on new FY26 forecast EPS JPY 691.30 (my calc) |
| EV/sales; EV/EBITDA | 7.3; 28.4 | 18.9; 48.2 (stale TTM); ~13.1 and ~28 on FY26 guide midpoint (my calc) | 4.6; 12.7 (stale TTM); 3.4x FY26 forecast sales (my calc) |
| Consensus | Buy, 11 analysts, avg target $144.70 | Buy, 12 analysts | 2 analysts, target JPY 10,900 |
| Reference deals | Teradyne buying 2,234,887 new shares for ~$300M = ~$134.2/share (agreement 6 Oct 2026, my calc) [S7] | T-Plus sold 2% to Vector Line at EUR 29.88 (17 Sep 2026) [S18] | n/a |
| 5-10y valuation range | could not verify | could not verify | could not verify |

---

## 1. Technical frontier: what can and cannot be probed in stacked and hybrid-bonded chips

### Takeaway
The "no roadmap below ~25 µm" line comes from EE Times (26 Jan 2026), reporting imec's Erik Jan Marinissen at the 2nd IEEE Hybrid Bonding Symposium: automated probing of fine-pitch micro-bump arrays has been shown down to 40 µm pitch, imec's 25 µm results were mixed, and below that the industry needs sacrificial probe pads or a rethink of pre-bond test. Production hybrid bonding is at 6-9 µm pitch, far below any probe roadmap, so bonded interfaces are tested electrically only through design-for-test after bonding.

### Cited findings
- EE Times, "Hybrid Bonding Comes of Age Slowly and Collectively", Pat Brans, 26 Jan 2026, covering the second IEEE Hybrid Bonding Symposium (hosted by SEMI, Silicon Valley, 22-23 Jan 2026) [S1]. Speaker: Erik Jan Marinissen, scientific director, imec. Quotes: "From a test perspective, this technology is under development and not mature at all"; "The absence of any realistic roadmap for probing dense hybrid-bond arrays below ~25 µm pitch" means "manufacturers must rethink pre-bond testing strategies entirely"; as pitches shrink "well below 10 µm", "traditional assumptions about test access begin to break down"; "Dedicated sacrificial probe pads may offer a workaround, but at the cost of additional area and process complexity"; "A single particle can create a stand-off height that leads to many open defects, sometimes across die boundaries"; expansion of test from die to chiplet to full stack is "one of the most underestimated challenges ahead" [S1]. Other speakers: Dongkai Shangguan (general chair), Joke De Messemaeker (imec), Vikas Dubey (Fraunhofer ENAS) [S1].
- Talk abstract, "The Impact of Hybrid Bonding on Testing 3D-Stacked Dies", Marinissen (imec), 2026 IEEE Hybrid Bonding Symposium (IEEE.tv page dates the event 21-22 Jan 2026 and was posted 23 Jan 2026; EE Times says 22-23 Jan, so the date conflicts): probing micro-bumps is feasible down to 40 µm pitch; imec's unpublished 25 µm results were mixed; with no clear probe roadmap below 25 µm, dedicated sacrificial pads may be needed; pre-bond test is generally advisable because skipping it can make total product cost uncontrollable; every die-to-die interconnect must be tested at least once (mid-, post-, final-bond); imec's "E2 I-TEST" aims for higher defect coverage with fewer patterns; open defects become more important than shorts; imec has shown bonding pitches down to 250 nm [S2]. (Abstract paraphrased by the fetch tool; one phrase quoted in search output: "automatically probing these large arrays of fine-pitch micro-bumps has shown to be feasible down to 40 um pitch".)
- Production hybrid-bond pitch (secondary, search snippets only, articles not opened): TSMC SoIC at 6 µm with a path to 4.5 µm by 2029; Intel Foveros Direct at 9 µm with 3 µm planned; SK hynix said at Hot Chips 2026 that hybrid bonding will not be ready for HBM4E (HBM5 at the earliest) and that MR-MUF extends through Nvidia Rubin [S39].
- HBM test flow, company view: FormFactor tests HBM "stacks of eight, twelve, or sixteen DRAM die" and says its high-frequency capability helps it compete (10-K, Feb 2026) [S9]; Technoprobe presented an "HBM test flow" comparing micro-cantilever and vertical MEMS probe cards (May 2026) [S16] and offers vertical cards "up to full-wafer coverage" [S13].
- A 2025 SWTest paper reportedly shows a MEMS probe approach at 40 µm pitch with 20 µm "in progress" (search-tool summary of SWTest 2025 proceedings; specific paper not identified) [S40].

### Inferences
- The probe-pitch frontier (~40 µm micro-bump arrays, uncertain at 25 µm) is roughly 4-7x coarser than production hybrid-bond pitch (6-9 µm). Hybrid-bonded faces therefore cannot be contacted directly; known-good-die relies on test before bonding through separate probe pads or design-for-test, and stack-level test relies on built-in self-test and boundary-scan-style access (consistent with the imec talk).
- For probe-card makers this shifts value toward (i) sacrificial-pad and pre-bond KGD cards, (ii) full-wafer, high-parallelism DRAM/HBM core-die test, and (iii) post-bond test through the stack's external bumps, rather than probing the bond layer itself.

### Gaps (INCOMPLETE; being worked in gap pass)
- Finest pitch in volume production for MEMS probe cards (HBM micro-bumps, logic C4/micro-bumps): no primary product or conference source captured yet.
- IEEE 1838 adoption, contactless/e-beam/optical probing developers: not yet sourced.

---

## 2. Market: size, shares, HBM, and whether probe cards are consumables

### Takeaway
TechInsights data (via MJC) put the probe-card market at $3.19bn in 2025, up 25% from $2.55bn in 2024; memory cards grew faster (+29%) on HBM. MJC leads memory (41%); the two largest overall slices (22%, 20%) fit Technoprobe and FormFactor but are not labelled. Cards are design-specific and analysts classify them as "test consumables", but orders follow new designs and capacity adds, so revenue is recurring yet cyclical.

### Cited findings
- TechInsights data (June 2026), charted by MJC, Aug 2026 [S32]: total market $2,552M (2024) → $3,192M (2025); memory $792M → $1,019M; non-memory $1,740M → $2,149M. 2025 total shares: 22%, 20%, MJC 14%, 9%, 6%, other 28% (2024: 24%, 22%, MJC 13%, 7%, 5%, other 29%). Memory 2025: MJC 41%, 23%, 14%, 9%, 3%, other 10% (2024: MJC 40%, 27%, 9%, 7%, 4%, other 12%). Non-memory 2025: 33%, 19%, 14%, 4%, 2%, MJC 2%, other 26%. Non-MJC slices are unlabelled. FX 149.57 JPY/$ (2025).
- Yole (via Technoprobe slide, May 2026): 2024 logic probe-card market $1.6bn = MEMS $937M, vertical $286M, cantilever $222M, other $194M; Technoprobe 34% of logic, 60% of MEMS logic [S16]. Yole's tracker is titled "Semiconductor Test Consumables market monitor" [S16][S37].
- Yole product page: probe-card market "recorded 2.9% growth in Q1-26"; demand "rising sharply driven by probe card used for high-end memory devices, mainly HBM" (search snippet) [S37].
- MJC forecasts (company): probe-card market ~US$3.3bn in 2026 (+14%) (Feb 2026) [S33]; ~US$3.5bn and an 18% CAGR over its FV26 plan period (Aug 2026) [S32]; drivers "HBM・NANDの三次元化" (3D HBM and NAND) [S32].
- Consumable character: FormFactor cards are custom to each wafer and chip design, and contacts must survive "hundreds of thousands, and even millions, of compression cycles" [S9]; Technoprobe cards are "custom-made for each specific chip" [S12].
- AI/HBM demand mechanism (company claims, unconfirmed): Technoprobe cites higher test intensity per wafer, denser interconnects, finer pitch and advanced packaging (H1'26) [S14] and "more test insertions" (Q3'26) [S13]; MJC cites HBM generation changes and output growth (Feb 2026) [S33].

### Inferences
- Applying the labelled slices to company revenues (my calc): the non-memory 33% slice (~$709M) matches Technoprobe's 2025 revenue (~$710M), and 19% non-memory + 23% memory (~$642M) matches FormFactor's probe-card business, implying Technoprobe ~22% and FormFactor ~20% of 2025 total. This is an inference, not a labelled third-party ranking.
- HBM concentrates buyers: three DRAM makers, with SK hynix alone 20-25% of FormFactor revenue.

### Gaps
- Labelled TechInsights/VLSI top-10 ranking for 2024 and 2025 (paywalled); HBM probe-card share by supplier and by customer (not found in public sources).
- Wafer-prober market share (Tokyo Seimitsu vs Tokyo Electron vs SEMICS): not yet sourced (INCOMPLETE).

---

## 3. FormFactor detail (quality evidence)

- Q3 FY2026 (to 26 Sep 2026), released 28 Oct 2026 [S3]: revenue $280,547K; GAAP GM 54.7% (Q2: 50.7% [S4]); non-GAAP GM 56.5%; GAAP op income $81,597K; non-GAAP op income $94,069K; GAAP NI $73,820K ($0.93); non-GAAP NI $82,278K ($1.04); FCF $64,778K. Foundry & Logic +10% q/q; Systems >20% q/q on co-packaged optics demand. Detailed mix by market was posted on the IR site (not accessible: HTTP 403).
- 9M 2026 [S3]: revenue $764,933K; GAAP GM 48.5%, non-GAAP 53.2%; GAAP op income $156,044K; GAAP NI $150,411K ($1.89); OCF $211,034K; capex $64,439K; FCF $148,060K. Equity $1,181.3M.
- Q4 FY2026 guidance [S3]: revenue $285M ±$10M; non-GAAP GM 54.0% ±1.5 pts; non-GAAP EPS $0.95 ±$0.09; GAAP EPS $0.84 ±$0.09.
- Call items (third-party summary, Mitrade, 29 Oct 2026) [S4]: Systems record $59.5M (+23% q/q); non-GAAP opex $64.4M (23% of revenue); OCF $104.3M in Q3; cash and investments $399M; Farmers Branch shipped first production unit; ~$400M annual probe-card capability by end-2027.
- Customers [S5][S9]: SK hynix share by quarter (10-K table as parsed): Q1'24 15.5%, Q2'24 19.5%, Q3'24 18.1%, Q4'24 22.0%, Q1'25 23.3%, Q2'25 25.0%, Q3'25 24.5%, Q4'25 19.2%; Q3'26 20.7%. Intel 15.7-17.1% in 2024 quarters, 12.0-12.4% Q1-Q2'25. Samsung 12.4% Q1'24. TSMC 10.4% Q2'25, 12.8% Q3'26. FY2024: two customers 33.5%. Receivables Sep 2026: three customers 22.0%, 15.0%, 13.7%.
- Restructuring (adopted 5 Jan 2026): consolidating Carlsbad and Baldwin Park, California; $32-40M charges, $30.7M taken by Q3'26 [S5]. Capex 9M'26 $64.4M vs $92.3M; construction in progress $117.8M [S5]. No buybacks in 9M'26; $70.9M authorisation left to 24 Apr 2027 [S5].
- Teradyne: Securities Purchase Agreement 6 Oct 2026 for 2,234,887 new shares for ~$300.0M, private placement, closing expected Q4 FY2026 [S7]; registration rights agreement effective 6 Oct 2026 [S6]; joint release 12 Oct 2026 announcing a "strategic collaboration" across HPC, advanced packaging, HBM and silicon photonics [S8]. Implied price ~$134.2/share; stake ~2.8% post-issue (my calc using 78.4M shares [S11]).
- 10-K FY2025 (filed 20 Feb 2026) [S9]: named probe-card competitors JEM, Korea Instrument, Micronics Japan, MPI, STAr Technologies, Max One, Technoprobe, TSE; probe-station competitors MPI, Semishare, STAr, Tokyo Electron, Wentworth. 2,153 employees (422 R&D). Farmers Branch bought June 2025; production from late FY2026. Says it "generally do[es] not have a sufficient backlog". FY2025 total revenue and revenue-by-market not yet captured (INCOMPLETE).

## 4. Technoprobe detail (quality evidence)

- FY2025 (18 Mar 2026) [S15]: revenue EUR 628,380K; GP EUR 279,087K (44.4%); EBITDA EUR 201,438K (32.1%); NI EUR 98,845K; equity EUR 1,242.0M; NFP EUR 684.2M. OCF EUR 212M; sale of Santa Clara building EUR 26M; investments EUR 99M; minority stakes in Yee Wei Inc. (~EUR 20M) and Innostar Service Inc. (~EUR 7M); buyback EUR 60M. CEO: ~38% of revenue from AI; plan to double capacity by end-2027 in Italy and other locations (Italy and Taiwan named). Called 2026 a year of "selection" for AI investment. 2027 targets brought forward: revenue EUR 850-900M, EBITDA 38-40% (since surpassed).
- Q1'26: revenue EUR 187.0M (+19.0%), EBITDA margin 37.0% [S16]. H1'26 (5 Aug 2026) [S14]: revenue EUR 464,051K (+42.4%); GP 53.8%; EBITDA EUR 206,151K (44.4%); NI EUR 143,108K; FY26 guide raised to EUR 1,050-1,100M and EBITDA 46-48%; capex to Q1'27 raised from EUR 250M to EUR 350M. Q2'26 revenue EUR 277.1M (my calc).
- 9M'26 (11 Nov 2026) [S12][S13]: see table A2. FX hit EUR 30M on revenue. Capex: EUR 167M finalised Jan-Sep (incl. EUR 17M leases); EUR 158M committed as of week 44; ~EUR 270M Italy, ~EUR 80M rest of world; Cernusco fab completion Dec 2026, ramp Feb 2027 (+4,000 sqm probe-head assembly); more space in Agrate Brianza. ~4,600 staff; 650+ patents.
- Governance and ownership: shareholding (company slide, May 2026): Crippa family 60.5%, Teradyne 10.0%, Alba Europe 6.0%, **Advantest 5.0%**, treasury 2.0%, other free float 16.5% [S16]. Teradyne holds 65,326,087 shares; it gained loyalty (double) voting rights on 7 Aug 2026, ~11.6% of votes; it can designate one director while holding at least 8% [S20]. T-Plus (family holding) 50.448% of shares and ~59.2% of votes after selling 2% to Vector Line Capital Fund II at EUR 29.88 on 17 Sep 2026; Vector Line (funded by an unnamed "industrial and strategic partner") now holds 5.382%, votes with T-Plus, may nominate one director, and may join any secondary offering "in case of dual listing" [S18][S19]. Director Gregory Smith (appointed Dec 2024; same name as Teradyne's CEO quoted in [S8]) resigned 28-29 Sep 2026; replaced on 11 Nov 2026 by Andrea Guaccero, verified as independent [S22][S12]. CTO Joseph Parks resigned effective 6 Nov 2026; CEO Stefano Felici is interim CTO [S23]. Lawsuit vs a former employee (C.D. Cal., 19 Feb 2026) over IP [S25].

## 5. Micronics Japan detail (quality evidence)

- Q3 FY2026 (12 Nov 2026) [S28][S29]: Jul-Sep revenue JPY 32,757M (+15.9% q/q); probe cards JPY 32,304M; TE JPY 453M; GP JPY 16,976M; OP JPY 11,436M; ordinary profit JPY 12,622M; NI JPY 8,045M. Memory card sales by quarter: 14,971 (Q3'25), 18,078, 19,245, 26,465, 30,371 (Q3'26); non-memory 1,945, 1,329, 1,383, 1,447, 1,933 (JPY M). Management: memory sales record on capacity increase and pulled-forward sales; orders up sharply q/q, "HBM-centred DRAM demand continues"; segment profit up on high-value DRAM products [S29]. Capex Q3 JPY 3,569M; R&D JPY 2,159M; depreciation JPY 2,307M [S29].
- 9M vs plan [S31]: revenue JPY 81,964M vs JPY 74,200M forecast (+10.5%); OP JPY 26,993M vs 22,400M. Reasons: memory card output above plan and some next-quarter sales brought forward.
- FY2026 forecast raised 12 Nov 2026 [S30]: revenue JPY 110,000M (from 103,800M), OP 36,100M (from 31,400M), ordinary 37,500M, NI 26,800M, EPS JPY 691.30; dividend JPY 208 (from 178; FY2025 JPY 95). FX assumption JPY 158/$, JPY 0.10/KRW [S29].
- Balance sheet 30 Sep 2026 [S28]: assets JPY 147,582M; liabilities JPY 48,566M; net assets JPY 99,015M; investment securities +JPY 23,744M in 9M, with unrealised gains on securities +JPY 16,299M (holdings not identified; could not verify).
- Mid-term plan FV26 (ends 2026) [S32]: original targets revenue JPY 80bn, OP JPY 20bn, OPM 25%, ROE 23%; now forecasting far above. 2023-2026 cumulative capex JPY 60.8bn and R&D JPY 25.4bn vs JPY 48bn / JPY 22bn planned. Company says its 2023-2026 revenue CAGR (39%) beat the probe-card market (18%) (company claim based on its own market estimate).
- Capacity [S34][S35]: JPY 24.1bn additional equipment/fit-out at Aomori and Aomori-Matsuzaki plants in 2027-2028, funded by cash and borrowing, explicitly for HBM-driven memory card demand; land (20,289 + 8,385 sqm) next to Oita Technology Laboratory (31 Jul 2026).

## 6. Field scan (INCOMPLETE in v1)

- Named by FormFactor as probe-card competitors (10-K, Feb 2026): JEM, Korea Instrument, MPI, STAr Technologies, Max One, TSE; probe-station competitors: MPI, Semishare, STAr, Tokyo Electron, Wentworth [S9].
- WinWay (Taiwan, test sockets/interfaces): licensed Technoprobe's TPEG technology for 5 years with a ~US$60M minimum purchase (9 Dec 2025) [S24].
- Remaining companies: to be filled in the gap pass.

## 7. Entry-point data (separate from quality)

- FORM [S11] (checked 12 Nov 2026): close US$95.78 on 11 Nov 2026 (+11.85% that day); pre-market US$93.15 on 12 Nov; 52-week change +78.9%; market cap $7.51bn; EV $7.14bn; P/E 44.06 trailing, 23.66 forward; EV/sales 7.29; EV/EBITDA 28.35; EV/FCF 39.4; net cash $368M; short interest 3.3% of shares; consensus Buy (11), mean target $144.70. Guidance: Q4'26 $285M ±$10M; Q3 GM boosted by non-recurring tariff refunds [S3][S4]. Events: Teradyne $300M placement closing (Q4 FY26) [S7]; Farmers Branch ramp; Q4 results ~early Feb 2027 (date not verified). Teradyne's implied entry ~$134/share is ~40% above the 11 Nov close (my calc); the price path between 6 Oct and 11 Nov 2026 was not verified.
- TPRO [S26] (checked 12 Nov 2026): EUR 22.76; market cap EUR 14.57bn; EV EUR 13.90bn; forward P/E 34.23; trailing figures use TTM to H1'26 (EUR 766.6M revenue) and are stale; on FY26 guidance midpoint EUR 1,057.5M and ~47% EBITDA margin, EV/sales ~13.1x and EV/EBITDA ~28x (my calc). 52-week +116%. Float 82.8M shares (12.9%); 20-day average volume 2.1M shares (~EUR 48M/day, my calc). Company quoted market cap ~EUR 18.5bn on 18 May 2026 [S16]. Guidance: Q4'26 EUR 270M; FY26 EUR 1,050-1,065M [S12]. Events: ERP recovery by end-2026; Nexprobe China ramp Q1'27; Cernusco fab ramp Feb 2027; CTO search; shift in Teradyne relationship (Teradyne investing in FormFactor; Teradyne-linked director left); dual-listing option referenced in the Vector Line pact (no plan announced) [S19]; FY2026 results date per 2027 calendar (published 11 Nov 2026, not read).
- MJC [S36] (checked 12 Nov 2026): JPY 10,100 close (-2.4%), before the 15:30 JST Q3 release and forecast raise; market cap JPY 391.6bn; EV JPY 378.0bn; P/E 20.9 trailing (TTM to Q2), 16.2 forward; 14.6x new FY26 EPS forecast and 2.1% yield on the JPY 208 dividend (my calc); 52-week +23.6%; 2 analysts, target JPY 10,900. Events: market reaction on 13 Nov to the raise; new mid-term plan after FV26 ends (timing not verified); Q4 step-down implied by guidance.
- Brief data for Tokyo Seimitsu (7729.T), MPI (6223.TWO), Leeno (058470.KQ), ISC (095340.KQ), Techwing (089030.KQ): INCOMPLETE in v1.

## 8. Could not verify (v1)
- Labelled third-party probe-card ranking/shares for 2024-2025; HBM probe-card share by supplier and by customer; wafer-prober shares.
- FormFactor FY2025 total revenue and 2025/2026 revenue by market (DRAM incl. HBM, flash, foundry & logic) and by country.
- Technoprobe customer concentration and China share; date and route of Advantest's 5% stake; whether Teradyne still holds 10% after 11 Aug 2026.
- MJC named customers and HBM exposure by customer; identity of MJC's investment securities.
- Finest production probe pitch; IEEE 1838 adoption; contactless/e-beam/optical probing developers.
- 5-10 year valuation ranges and consensus growth for all three.

## 9. Sources (date of document; all accessed 12 Nov 2026)

[S1]: https://www.eetimes.com/hybrid-bonding-comes-of-age-slowly-and-collectively/ "EE Times, Pat Brans, 26 Jan 2026"
[S2]: https://ieeetv.ieee.org/hbs/the-impact-of-hybrid-bonding-on-testing-3d-stacked-dies "IEEE.tv, Marinissen talk, posted 23 Jan 2026"
[S3]: https://www.sec.gov/Archives/edgar/data/0001039399/000103939926000040/ex9901-earningsreleasexq326.htm "FormFactor Q3 2026 release, 28 Oct 2026"
[S4]: https://www.mitrade.com/insights/news/live-news/article-0-2207359-20261029 "Mitrade call summary, 29 Oct 2026"
[S5]: https://www.sec.gov/Archives/edgar/data/1039399/000103939926000043/form-20260926.htm "FormFactor 10-Q, filed 3 Nov 2026"
[S6]: https://www.sec.gov/Archives/edgar/data/1039399/000103939926000043/ex41-teradyneformfactorreg.htm "Registration rights agreement, 6 Oct 2026"
[S7]: https://www.sec.gov/Archives/edgar/data/1039399/000103939926000037/form-20261006.htm "FormFactor 8-K, filed 13 Oct 2026"
[S8]: https://www.sec.gov/Archives/edgar/data/1039399/000103939926000037/ex-991.htm "FormFactor-Teradyne release, 12 Oct 2026"
[S9]: https://www.sec.gov/Archives/edgar/data/1039399/000103939926000009/form-20251227.htm "FormFactor 10-K FY2025, filed 20 Feb 2026"
[S11]: https://stockanalysis.com/stocks/form/statistics/ "stockanalysis FORM, checked 12 Nov 2026"
[S12]: https://www.technoprobe.com/wp-content/uploads/2026/11/PR-9M-2026.pdf "Technoprobe 9M 2026 release, 11 Nov 2026"
[S13]: https://www.technoprobe.com/wp-content/uploads/2026/11/9M_2026_Results.pdf "Technoprobe 9M 2026 presentation, 11 Nov 2026"
[S14]: https://www.emarketstorage.it/sites/default/files/comunicati/2026-08/20260805_187949.pdf "Technoprobe H1 2026 release (Italian), 5 Aug 2026"
[S15]: https://www.technoprobe.com/wp-content/uploads/2026/03/PR-FY-2025_.pdf "Technoprobe FY2025 release, 18 Mar 2026"
[S16]: https://www.technoprobe.com/wp-content/uploads/2026/05/Technoprobe-Company-Presentation-May-2026.pdf "Technoprobe company presentation, 19 May 2026"
[S17]: https://www.technoprobe.com/wp-content/uploads/2026/08/Closing-PJ-Ibiza_Closing-PJ-Ibiza-VF.pdf "China partnership closing, 14 Aug 2026"
[S18]: https://www.technoprobe.com/wp-content/uploads/2026/09/Comunicato-in-nome-e-per-conto-di-T-PLUS-Press-Release-on-behalf-of-T-PLUS.pdf "T-Plus/Vector Line release, 22 Sep 2026"
[S19]: https://www.technoprobe.com/wp-content/uploads/2026/09/Informazioni-essenziali-ex-art.130-RE_Patto-Tplus-Vector-Line.pdf "T-Plus/Vector Line pact key information, 22 Sep 2026"
[S20]: https://www.technoprobe.com/wp-content/uploads/2026/08/Key-Information_Update-ENG.pdf "T-Plus/Teradyne/Technoprobe pact update, 11 Aug 2026"
[S22]: https://www.technoprobe.com/wp-content/uploads/2026/09/Director-resignation.pdf "Director resignation, 29 Sep 2026"
[S23]: https://www.technoprobe.com/wp-content/uploads/2026/11/PR-CTO.pdf "CTO resignation, 4 Nov 2026"
[S24]: https://www.technoprobe.com/wp-content/uploads/2025/12/PR-Strategic-Agreement.pdf "WinWay TPEG agreement, 9 Dec 2025"
[S25]: https://www.technoprobe.com/wp-content/uploads/2026/02/PR_US-Litigation.pdf "US litigation release, 19 Feb 2026"
[S26]: https://stockanalysis.com/quote/bit/TPRO/statistics/ "stockanalysis TPRO, checked 12 Nov 2026"
[S28]: https://ssl4.eir-parts.net/doc/6871/tdnet/2913248/00.pdf "MJC Q3 FY2026 kessan tanshin, 12 Nov 2026"
[S29]: https://ssl4.eir-parts.net/doc/6871/tdnet/2913283/00.pdf "MJC Q3 FY2026 supplementary material, 12 Nov 2026"
[S30]: https://ssl4.eir-parts.net/doc/6871/tdnet/2913336/00.pdf "MJC forecast and dividend revision, 12 Nov 2026"
[S31]: https://ssl4.eir-parts.net/doc/6871/tdnet/2913300/00.pdf "MJC 9M forecast-vs-actual notice, 12 Nov 2026"
[S32]: https://ssl4.eir-parts.net/doc/6871/ir_material_for_fiscal_ym4/210517/00.pdf "MJC Q2 FY2026 results presentation, 13 Aug 2026"
[S33]: https://ssl4.eir-parts.net/doc/6871/ir_material_for_fiscal_ym4/198705/00.pdf "MJC FY2025 results presentation, 16 Feb 2026"
[S34]: https://ssl4.eir-parts.net/doc/6871/tdnet/2781196/00.pdf "MJC capacity capex notice, 26 Mar 2026"
[S35]: https://ssl4.eir-parts.net/doc/6871/tdnet/2859518/00.pdf "MJC land acquisition, 31 Jul 2026"
[S36]: https://stockanalysis.com/quote/tyo/6871/statistics/ "stockanalysis 6871, checked 12 Nov 2026"
[S37]: https://www.yolegroup.com/product/quarterly-monitor/semiconductor-test-consumables-market-monitor/ "Yole monitor product page (search snippet)"
[S39]: https://www.tomshardware.com/tech-industry/semiconductors/hybrid-bonding-roadmap-examined "Tom's Hardware, 2026 (search snippets only)"
[S40]: https://www.swtest.org/library/2025proc/pdf/M03_03_KUMAR_SWTest-2025.pdf "SWTest 2025 proceedings (paper not yet identified)"
