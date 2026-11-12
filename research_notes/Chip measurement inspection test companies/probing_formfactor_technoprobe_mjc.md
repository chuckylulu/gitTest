# Wafer probing and test interfaces for stacked/bonded chips: FormFactor, Technoprobe, Micronics Japan, the wider field, and the limits of probing dense bond arrays

**Research date: 12 November 2026.** Status: v2 (final for this pass). Web-search budget ran out mid-task, so the field scan relies on filings, market-data pages and FormFactor's competitor list. Coverage is thin on Chinese entrants, wafer-prober shares and Korean companies (see section 8).
Method: primary filings fetched directly (SEC EDGAR; Technoprobe IR / eMarket Storage; Micronics Japan (MJC) TDnet PDFs via eir-parts); IEEE Heterogeneous Integration Roadmap and SWTest papers downloaded; market data from stockanalysis.com checked 12 Nov 2026. "my calc" = arithmetic on cited figures. "company claim, unconfirmed" = no outside party confirms it. [S#] tags are links; dated list in section 9.
Latest periods: FormFactor Q3 FY2026 (to 26 Sep 2026; release 28 Oct; 10-Q 3 Nov 2026). Technoprobe 9M 2026 (to 30 Sep; release 11 Nov 2026, unaudited). MJC Q3 FY2026 (Jan-Sep; release 12 Nov 2026 at 15:30 JST, after the Tokyo close).
Change versus the brief's background: Teradyne still held 10% of Technoprobe on 11 Aug 2026, but on 6 Oct 2026 it agreed to invest $300M in FormFactor, and its CEO's namesake left Technoprobe's board on 28-29 Sep 2026. A company slide also shows Advantest holding 5% of Technoprobe.

---

## A. Evidence tables (quality tests a-e and transitions; entry-point data kept separate in A4 and section 7)

### A1. FormFactor (FORM, Nasdaq, Livermore, USA)

| Test | Evidence (dated) |
|---|---|
| (a) Position | Physical contact interface for wafer sort: probe cards (FY2025 $637.9M, 81% of revenue) plus engineering systems (probe stations, thermal, cryogenic, photonic; $147.1M, 19%) [S9]. Cards are "customized to our customers' unique wafer and chip designs" [S9]. Owns a physical constraint (fine-pitch, high-frequency MEMS contact made at volume). Does not own the test program or pass/fail data (inference). |
| (b) Lead | Audited customer data: one customer (SK hynix, per the quarterly table) 22.9% of FY2025 revenue [S9]; SK hynix 20.7% of Q3'26 and 24.5% of 9M'26; TSMC 12.8% of Q3'26 and 11.2% of 9M'26; Intel 11.2% of 9M'25, under 10% in 2026 [S5]. DRAM revenue +8.8% in FY2025, "driven by demand for HBM designs used in generative AI" [S9]. Third-party share: FormFactor's FY2025 probe-card revenue ($637.9M) equals 20.0% of TechInsights' $3,192M 2025 market, matching the unlabelled 20% slice in an MJC chart; FY2024 ($626.0M) equals 24.5%, matching a 24% slice (my calc; inference, labels not shown) [S32]. 10-K gives no numerical share; "compete favorably" is a company claim, unconfirmed [S9]. |
| (c) Revenue model | Design-specific cards bought with each new chip design, node or capacity add; no service, software, subscription or usage revenue line found. Systems is one-off capital equipment. Says it "generally do[es] not have a sufficient backlog" [S9]. Deferred revenue $36.6M (26 Sep 2026) vs $20.1M (27 Dec 2025) [S5]. No labour-hour revenue identified. |
| (d) Financial strength | FY2025: revenue $785.0M (+2.8%); GAAP GM 39.3%; op. margin 7.2%; R&D $115.7M (14.7%); tariffs cost 1.4 pts of GM [S9]. Q3'26: revenue $280.5M (+38.4% y/y); GAAP GM 54.7% (non-GAAP 56.5%, incl. ~380 bps one-off tariff refunds and Quantum cost benefit [S4]); GAAP op. margin 29.1% (my calc); FCF $64.8M; 9M'26 FCF $148.1M [S3]. Cash + securities $395.4M; debt $11.4M; $150M revolver undrawn [S3][S5]. ROIC 23.6% TTM [S11]. Concentration: SK hynix + TSMC 33.5% of Q3'26 [S5]. Country FY2025: South Korea 30.3%, Taiwan 25.8%, US 19.4%, China 7.4% ($58.0M, down from $103.0M / 13.5% in FY2024), Japan 5.5% [S9]. |
| (e) Resilience | HBM exposure concentrated at SK hynix (19-25% of revenue in every quarter of 2025 and 20.7% in Q3'26) [S5][S9]. Capacity-limited: productivity gains "moderating as we approach its capacity limits" (CEO, 28 Oct 2026) [S3]; Farmers Branch, Texas plant shipped first production unit, ~$400M/yr probe-card capability by end-2027, "capacity, not guaranteed revenue" (call summary) [S4]. Export controls: 10-K says trade restrictions have "caused decreasing demand from Chinese customers"; China revenue -44% in FY2025 (my calc) [S9]. Cycle: four record quarters in a row; Q4 guide $285M ±$10M, +1.6% q/q at midpoint [S3]. |
| T1 measurement→inference | Nothing found. |
| T2 AI-built designs/recipes | Nothing found. |
| T3 bonded stacks / packaging | DONE: HBM probe cards for 8-, 12- and 16-high stacks [S9]; Keystone Photonics bought 15 Dec 2025 ($20.6M net) for optical probing of silicon photonics, CPO and near-packaged optics [S5]; Systems record $59.5M in Q3'26 on CPO / TRITON [S3][S4]; 20% of the holding company that bought substrate/PCB maker FICT with MBK Partners ($67.2M; FICT is also a supplier) [S5]; FormFactor-Intel MEMS card for 40 µm-pitch parametric test, 20 µm in development (SWTest, Jun 2025) [S42]. SAID: Teradyne collaboration on HPC, advanced packaging, HBM, silicon photonics (12 Oct 2026) [S8]. Hybrid bonding not mentioned in the 10-K [S9]. |
| T4 hardware→software/data | Nothing beyond the collaboration's "from wafer to data center" wording (company claim, unconfirmed) [S8]. |
| T5 on-premises AI | Nothing found. |
| T6 fewer insertions after 2030 | No statement found. |

### A2. Technoprobe (TPRO, Euronext Milan, Cernusco Lombardone, Italy)

| Test | Evidence (dated) |
|---|---|
| (a) Position | Probe cards (logic-centric MEMS) plus final-test interface and burn-in boards since buying Teradyne's Device Interface Solutions (DIS Tech) on 27 May 2024 [S15][S20]. Cards "custom-made for each specific chip" [S12]. Physical constraint plus capacity; no data or test-program ownership (inference). |
| (b) Lead | Yole data (Sep 2024 monitor) cited by the company: 34% of the 2024 logic probe-card market ($1.6bn) and 60% of MEMS logic cards ($937M) [S16]. TechInsights via MJC chart: with FormFactor matching the 20% slice and MJC labelled at 14%, the remaining 22% slice ($702M) is most likely Technoprobe (2025 revenue EUR 628.4M incl. DIS boards), i.e. #1 in 2025 (inference; unlabelled) [S32][S15]. No customers named in documents read. |
| (c) Revenue model | Design-specific cards and boards; no service/software split. WinWay may use the TPEG technology for 5 years with ~US$60M minimum purchases (9 Dec 2025) [S24]. |
| (d) Financial strength | FY2025: revenue EUR 628.4M (+15.7%), GP 44.4%, EBITDA 32.1%, net profit EUR 98.8M [S15]. 9M'26: revenue EUR 787.4M (+68.8%), GP 56.8%, EBITDA EUR 376.3M (47.8%); Q3'26 EUR 323.3M (+130% y/y), GP 61.1%, EBITDA 52.6% [S12][S13]. Net cash (NFP) EUR 799.8M on 30 Sep 2026 [S12]. 9M OCF ~EUR 241M vs capacity capex ~EUR 150M (~EUR 91M FCF, my calc) [S12]. 2025 profit retained, no dividend; EUR 60M buyback done 19 Dec 2025 [S15]. Customer and China concentration not disclosed (could not verify). |
| (e) Resilience | FY2025 end-markets: consumer 48%, AI/data centre 38%, auto/industrial 14% (company) [S16]. Q4'26 guide EUR 270M ±3% (-16% q/q), GM 54.2%, EBITDA 45.1%, blamed on the ERP/MES go-live of 1 Oct 2026; FY26 narrowed to EUR 1,050-1,065M (top cut from EUR 1,100M) [S12]. Capacity: ~EUR 1.6bn run-rate by Q1'27, ~EUR 2.0bn by end-2027 (1.9x the FY26 guide midpoint, my calc), "fully self-funded" [S13]. China: Nexprobe (Shanghai/Suzhou, ~12,000 sqm), local partner paid US$35M for 30% (closed 14 Aug 2026), ramp in Q1 2027 [S13][S17]. |
| T3 stacks / packaging | DONE/SAID: HBM entry with vertical MEMS cards "up to full-wafer coverage"; electro-optical probing for CPO with fibre-array positioning [S13]; HBM test-flow slides (wafer level → reconstituted wafer → cube) [S16]; final-test boards via DIS [S16]. "Advanced Packaging segment is expected to accelerate over the 2026-2027 period" (company) [S15]. |
| T6 insertions | Says AI brings "increasing test intensity and more test insertions" (company claim, unconfirmed) [S13]. |
| T1, T2, T4, T5 | Nothing found. |

### A3. Micronics Japan (6871.T, Tokyo Prime; plants in Aomori, Oita)

| Test | Evidence (dated) |
|---|---|
| (a) Position | Memory probe cards (DRAM incl. HBM): 94% of probe-card revenue in Q3'26 (JPY 30,371M of 32,304M, my calc) [S29]. Physical constraint plus capacity. Small Test Equipment (TE) arm: Testalio tester, Excelyze engineering prober, sockets, FPD probes [S29]. |
| (b) Lead | TechInsights data (June 2026) charted by MJC: MJC 41% of the 2025 memory probe-card market ($1,019M), 40% in 2024; 14% of the total ($3,192M) in 2025, 13% in 2024; 2% of non-memory [S32]. Third-party data, chart prepared by the company. No customers named (annual report could not be text-extracted). |
| (c) Revenue model | Probe cards 98.6% of 9M'26 sales; TE 1.4% and loss-making (9M loss JPY 1,142M) [S28]. Stopped disclosing orders and backlog after FY2025 [S33]. |
| (d) Financial strength | FY2025: revenue JPY 70,173M (+26.1%), GM 48.2%, OP JPY 16,542M (23.6%), NI JPY 12,063M [S33]. 9M'26: revenue JPY 81,964M (+62.6%), OP JPY 26,993M (32.9%), NI JPY 19,506M; Q3'26 revenue JPY 32,757M (+89.4% y/y), GM 51.8%, OPM 34.9% [S29]. 30 Sep 2026: cash JPY 28.0bn, borrowings JPY 6.4bn (net cash ~JPY 21.6bn, my calc); net assets JPY 99.0bn of JPY 147.6bn [S28]. ROE 26.2%, ROIC 24.2% TTM [S36]. Region Q3'26: Asia ex-Japan 95.1%, Japan 4.4% [S29]; 2025 quarters: Korea 46-60%, Taiwan 27-37% [S33]. China not split out. |
| (e) Resilience | One end-market (DRAM/HBM). Q3 beat partly from sales pulled forward from Q4 [S31]; guidance implies Q4 revenue JPY 28.0bn vs JPY 32.8bn in Q3 (my calc) [S30]. Capacity: extra JPY 24.1bn capex for 2027-2028 at Aomori, for HBM-driven demand (26 Mar 2026) [S34]; land beside the Oita lab (31 Jul 2026) [S35]. |
| T3 stacks / packaging | SAID: developing "new technology for next-generation HBM" [S32][S33]. DONE: Testalio and Excelyze still under customer evaluation, no orders reported (Q3'26) [S29]. |
| T1, T2, T4, T5, T6 | Nothing found (glossary mentions DFT and BIST only) [S29]. |

### A4. Entry-point snapshot (separate from quality; detail in section 7)

| | FORM | TPRO.MI | 6871.T |
|---|---|---|---|
| Price / date | $95.78, close 11 Nov 2026 [S11] | EUR 22.76, 12 Nov 2026 12:49 CET [S26] | JPY 10,100, close 12 Nov 2026, before Q3 release [S36] |
| Recent path | High $149.31 (30 Sep); low $71.76 (5 Nov, -52%) [S45] | High EUR 36.84 (6 Oct); low EUR 20.52 (5 Nov, -44%) [S46] | High JPY 17,330 (9 Oct); low JPY 8,672 (6 Nov, -50%) [S47] |
| Market cap / EV | $7.51bn / $7.14bn | EUR 14.57bn / EUR 13.90bn | JPY 391.6bn / JPY 378.0bn |
| P/E trailing / fwd | 44.1 / 23.7 | 70.8 (stale TTM to H1'26) / 34.2 | 20.9 (stale TTM to Q2'26) / 16.2; 14.6 on new FY26 EPS forecast (my calc) |
| EV/sales; EV/EBITDA | 7.3; 28.4 | 18.9; 48.2 (stale); ~13.1 and ~28 on FY26 guide midpoint (my calc) | 4.6; 12.7 (stale); 3.4x FY26 sales forecast (my calc) |
| Consensus | Buy (11), mean target $144.70 | Buy (12) | 2 analysts, target JPY 10,900 |
| Reference deals | Teradyne: 2,234,887 new shares for ~$300M = ~$134.2/share, agreed 6 Oct 2026 (my calc) [S7] | T-Plus sold 2% to Vector Line at EUR 29.88 (17 Sep 2026) [S18] | n/a |
| 5-10y multiple range | could not verify | could not verify | could not verify |

---

## 1. Technical frontier: what can and cannot be probed

### Takeaway
The "no roadmap below ~25 µm" line is from EE Times (26 Jan 2026), reporting imec's Erik Jan Marinissen at the 2nd IEEE Hybrid Bonding Symposium. The IEEE Heterogeneous Integration Roadmap (HIR) test chapter (posted Oct 2026) independently says state-of-the-art micro-bumps are at 40 µm (some 30 µm) and 40 µm probing has been shown "only single-site". Production hybrid bonding is at 6-9 µm. So bonded faces are not probed: pre-bond known-good-die (KGD) uses sacrificial pads, and post-bond test goes through design-for-test (DFT), IEEE 1838 and built-in self-test (BIST).

### Cited findings
- EE Times, "Hybrid Bonding Comes of Age Slowly and Collectively", Pat Brans, 26 Jan 2026, on the 2nd IEEE Hybrid Bonding Symposium (hosted by SEMI, Silicon Valley, 22-23 Jan 2026) [S1]. Speaker: Erik Jan Marinissen, scientific director, imec. "From a test perspective, this technology is under development and not mature at all"; "The absence of any realistic roadmap for probing dense hybrid-bond arrays below ~25 µm pitch" means manufacturers "must rethink pre-bond testing strategies entirely"; below 10 µm "traditional assumptions about test access begin to break down"; "Dedicated sacrificial probe pads may offer a workaround, but at the cost of additional area and process complexity"; "A single particle can create a stand-off height that leads to many open defects, sometimes across die boundaries"; die-to-chiplet-to-stack test is "one of the most underestimated challenges ahead" [S1].
- Talk abstract (IEEE.tv; event dated 21-22 Jan 2026 there, conflicting with EE Times' 22-23 Jan): micro-bump probing feasible to 40 µm pitch; imec's unpublished 25 µm results "mixed"; sacrificial pads may be needed below 25 µm; pre-bond test advisable because skipping it can make product cost "uncontrollable"; every die-to-die interconnect must be tested at least once; imec's "E2 I-TEST" targets more coverage with fewer patterns; opens matter more than shorts; imec has bonded at 250 nm pitch [S2].
- HIR 2025 edition, Ch. 17 Test Technology (IEEE EPS, posted Oct 2026; co-chairs Ken Butler, Jeorge Hurtarte) [S41]:
  - "State-of-the-art micro-bump pitches are 40 µm; some advanced products already push this down to 30 µm... Feasibility of 40 µm probing has been demonstrated but only single-site. Future research should push this to multi-site testing and to even smaller pitches (10 µm)."
  - Copper hybrid bonding: "Reduced pin-count testing will be required for wafer probe, and DFT solutions are needed to enable complete wafer probe testing."
  - IEEE 1838-2019 (released 2020) is supported by "the three major EDA suppliers"; covers INTEST (die internals) and EXTEST (inter-die interconnects). Current products already include redundant interconnects and repair.
  - HBM: the old low-speed wafer sort plus at-speed package test model is "completely broken by HBM". Options: (1) known-good stacked die (KGSD) high-speed wafer sort through a probe card, limited by tight pitch, power and missed post-singulation defects; (2) singulated-die test on temporary carriers (128+ parallel, "still being proven for high-volume production"), reconstructed wafers, or direct handling (not mature). "Near-term solution likely to favor KGSD". JEDEC defines an IEEE bus and DA bus so HBM stacks can be tested through DFT "without probing delicate TSVs".
  - Requirement table (2026 column, one device class): array bump pitch 30 µm; sacrificial pads in a field of bumps at 100 µm pitch, 42x42 µm; 50,000 probe points per touchdown; 2-10 GHz wafer test.
  - Finest mechanical probing anywhere: display-driver pads 8 µm wide in production, 7 µm in engineering (2025); roadmap 3-5 µm by ~2035 and sub-1 µm "non-contact/hybrid" by ~2045.
  - Silicon photonics wafer test: probe pitch 50 µm now → <40 µm; 1,500 → 6,000 probes per photonic IC; vertical → vertical/MEMS.
  - Contactless: research on optical (laser Doppler vibrometry) and RF near-field readout for wafer-level test is "essential" (MEMS section).
- SWTest 2025 (Carlsbad, 2-4 Jun 2025):
  - Selvaraj, Dube et al., FormFactor with Intel: parametric MEMS card at 40 µm pitch, 25x25 µm pads, scrub <15 µm, stable contact resistance over 500 production touchdowns without cleaning; "20 µm capability in progress" [S42]. Vendor and customer authors; not independently replicated.
  - Kumar et al., Xallent with IBM: "there is lack of fine-pitch probe cards for testing chiplets and interposers with fine pitch micro-bumps, copper pillars, and hybrid bond pads"; Xallent's Kelvin probe (8 µm-thick probes, 5 µm spacing) measured micro-bump test structures on 300 mm wafers [S43].
  - Varga et al., EV Group: "AI and HPC Probing Devices Require New Integration Schemes" (probe-card build methods; detail not extracted) [S44].
- Technoprobe HBM test flow (May 2026): core and base dies tested at wafer level for raw defects (memory via sacrificial pads), partial stacks on a reconstituted wafer for interconnect (via sacrificial pads, marked "Intermediate ?"), finished cube at singulated level for performance; micro-cantilever needles "cannot be arranged to contact bump in a full grid", vertical MEMS can [S16].
- Production hybrid-bond pitch (search snippets only, not opened): TSMC SoIC 6 µm with a path to 4.5 µm by 2029; Intel Foveros Direct 9 µm; SK hynix (Hot Chips 2026) said hybrid bonding will not be ready for HBM4E [S39].

### Inferences
- Probing stops about 4-7x short of production hybrid-bond pitch, and two independent sources (imec; HIR) agree there is no multi-site path below 30-40 µm. The bond layer itself is tested electrically only after bonding, through DFT and IEEE 1838 access, and by inference from stack-level results.
- Probe-card value in stacks moves to sacrificial-pad KGD cards, full-wafer high-parallel DRAM core-die sort, and KGSD wafer sort. Each new HBM generation adds insertions today; a move to singulated-die carriers would shift some value to handlers and carriers.

### Gaps
- Finest pitch in volume production for HBM micro-bump or logic micro-bump probe cards: no product-level source; HIR's "40 µm, single-site" is the best public marker.
- E-beam or capacitive/inductive contactless probing developers: no source found. Names of the "three major EDA suppliers": not given in the excerpt.

---

## 2. Market: size, shares, HBM, consumable or capital good

### Takeaway
TechInsights (via MJC) put probe cards at $3.19bn in 2025, +25%; memory +29% on HBM. Matching unlabelled slices to company revenue suggests FormFactor led in 2024 (~24%) and Technoprobe in 2025 (~22% vs ~20%), with MJC third (14%) and dominant in memory (41%). Cards are design-specific and Yole calls them "test consumables", but orders follow new designs and capacity, so revenue recurs but is cyclical.

### Cited findings
- TechInsights (June 2026 data) charted by MJC, 13 Aug 2026 [S32]: total $2,552M (2024) → $3,192M (2025); memory $792M → $1,019M; non-memory $1,740M → $2,149M. 2025 total: 22%, 20%, MJC 14%, 9%, 6%, other 28% (2024: 24%, 22%, MJC 13%, 7%, 5%, other 29%). Memory 2025: MJC 41%, 23%, 14%, 9%, 3%, other 10%. Non-memory 2025: 33%, 19%, 14%, 4%, 2%, MJC 2%, other 26%. Only MJC is labelled.
- Yole via Technoprobe (May 2026): 2024 logic probe-card market $1.6bn (MEMS $937M, vertical $286M, cantilever $222M, other $194M); 2024 final-test interface board market $744M [S16]. Yole's tracker is the "Semiconductor Test Consumables market monitor"; product page: "recorded 2.9% growth in Q1-26", demand "rising sharply" from high-end memory, "mainly HBM" (search snippet) [S37].
- TechInsights sells probe-card reports with a top-10 supplier ranking (paywalled; page descriptions only) [S38].
- MJC forecasts (company): ~US$3.3bn market in 2026, +14% (Feb 2026) [S33]; ~US$3.5bn and an 18% CAGR over its plan period (Aug 2026) [S32].
- Consumable character: FormFactor cards are custom per design and contacts endure "hundreds of thousands, and even millions" of cycles [S9]; Technoprobe cards "custom-made for each specific chip" [S12].
- Demand drivers, company claims: Technoprobe cites more test intensity per wafer, denser interconnect, finer pitch, advanced packaging [S14] and "more test insertions" [S13]; FormFactor's DRAM growth came from "HBM designs used in generative AI" while foundry/logic fell on PC and server CPU weakness in 2025 [S9].

### Inferences
- FormFactor's probe-card revenue equals the 20% (2025) and ~24% (2024) slices; MJC's equals its labelled 14%; the 22% 2025 slice ($702M) is then most likely Technoprobe. The 33% non-memory slice (~$709M) is also Technoprobe-sized, and the 14% non-memory slice (~$301M) fits MPI's scale. None of this is labelled by TechInsights.
- HBM concentrates buying in three DRAM makers; SK hynix alone is 20-25% of FormFactor revenue.

### Gaps
- A labelled 2024-2025 ranking; HBM probe-card share by supplier and by customer; wafer-prober shares (Tokyo Seimitsu vs Tokyo Electron vs SEMICS) — no public source reached.

---

## 3. FormFactor detail (quality evidence)

- Q3 FY2026 (28 Oct 2026) [S3]: revenue $280,547K (+8.6% q/q); GAAP GM 54.7% (Q2 50.7% [S4]); GAAP op income $81,597K; non-GAAP op income $94,069K (33.5%); GAAP NI $73,820K ($0.93); non-GAAP EPS $1.04; FCF $64,778K. Foundry & Logic +10% q/q; Systems >20% q/q on CPO. 9M: revenue $764,933K; GAAP op income $156,044K; OCF $211,034K; capex $64,439K. Equity $1,181.3M.
- Q4 guide [S3]: $285M ±$10M; non-GAAP GM 54.0% ±1.5 pts; non-GAAP EPS $0.95 ±$0.09.
- Call (third-party summary) [S4]: Systems $59.5M; non-GAAP opex 23% of revenue; Q3 OCF $104.3M; tariff refunds ~$0.09 of EPS.
- FY2025 by market [S9]: Foundry & Logic $369.9M (47.1%, -3.0%); DRAM $247.4M (31.6%, +8.8%); Flash $20.6M (2.6%); Systems $147.1M (18.7%). Segment GM: probe cards 40.5%, systems 41.8%. FY2023 revenue $663.1M, op margin 12.4%.
- SK hynix by quarter [S9][S5]: 15.5% (Q1'24), 19.5%, 18.1%, 22.0%, 23.3% (Q1'25), 25.0%, 24.5%, 19.2% (Q4'25); 20.7% (Q3'26). Intel 15.7-17.1% in 2024 quarters; Samsung 12.4% (Q1'24); TSMC 10.4% (Q2'25), 12.8% (Q3'26).
- Restructuring (5 Jan 2026): closing Carlsbad and Baldwin Park, California; $32-40M charges, $30.7M taken by Q3 [S5]. 9M capex $64.4M vs $92.3M; construction in progress $117.8M; no buybacks in 9M'26 ($70.9M left) [S5].
- Teradyne [S6][S7][S8]: purchase agreement 6 Oct 2026, 2,234,887 new shares for ~$300.0M, closing expected in Q4 FY2026; ~2.8% stake post-issue (my calc); collaboration on HPC, advanced packaging, HBM, silicon photonics.
- 10-K [S9]: named probe-card rivals JEM, Korea Instrument, MJC, MPI, STAr Technologies, Max One, Technoprobe, TSE; probe-station rivals MPI, Semishare, STAr, Tokyo Electron, Wentworth. 2,153 staff (422 R&D). Farmers Branch bought June 2025.

## 4. Technoprobe detail (quality evidence)

- FY2025 (18 Mar 2026) [S15]: OCF EUR 212M; Santa Clara building sale EUR 26M; investments EUR 99M; minority stakes in Yee Wei Inc. (~EUR 20M) and Innostar Service Inc. (~EUR 7M). CEO: ~38% of revenue from AI; plan to double capacity by end-2027 (Italy and Taiwan). Called 2026 a year of "selection" for AI spending. 2027 targets (EUR 850-900M, EBITDA 38-40%) already exceeded by the 2026 guide.
- Quarters: Q1'26 EUR 187.0M, EBITDA 37.0% [S16]; Q2'26 EUR 277.1M (my calc); H1'26 EBITDA 44.4%, NI EUR 143.1M [S14]; Q3'26 EUR 323.3M, beating the EUR 314M guide [S12][S14]. FX cost EUR 30M of 9M revenue [S13].
- Capex [S13]: EUR 167M spent Jan-Sep (incl. EUR 17M leases); EUR 158M committed by week 44; ~EUR 270M Italy, ~EUR 80M elsewhere; Cernusco fab done Dec 2026, ramp Feb 2027 (+4,000 sqm probe-head assembly); added space in Agrate Brianza; ~4,600 staff; 650+ patents.
- Ownership [S16][S18][S19][S20][S21]: company slide (May 2026): Crippa family 60.5%, Teradyne 10.0%, Alba Europe 6.0%, Advantest 5.0%, treasury 2.0%, other float 16.5%. Teradyne holds 65,326,087 shares, gained double votes on 7 Aug 2026 (~11.6% of votes), may name one director while at or above 8%. After selling 2% to Vector Line Capital Fund II at EUR 29.88 (17 Sep 2026), T-Plus (family holding) has 50.448% of shares and ~59.2% of votes. Vector Line (backed by an unnamed "industrial and strategic partner") holds 5.382%, votes with T-Plus, may name a director, and may join any secondary sale "in caso di dual listing".
- Governance [S22][S12][S23][S25]: director Gregory Smith (appointed Dec 2024; same name as Teradyne's CEO quoted in [S8]; inference: Teradyne's nominee) resigned 28-29 Sep 2026, replaced 11 Nov 2026 by Andrea Guaccero, verified independent. CTO Joseph Parks left 6 Nov 2026; CEO Stefano Felici is interim CTO. IP lawsuit against a former employee (C.D. Cal., 19 Feb 2026).

## 5. Micronics Japan detail (quality evidence)

- Q3'26 [S29]: memory card sales by quarter (JPY M): 14,971 (Q3'25), 18,078, 19,245, 26,465, 30,371 (Q3'26); non-memory 1,945 → 1,933. Management: record memory sales from added capacity and pulled-forward sales; orders up sharply, "HBM-centred DRAM demand continues". Q3 capex JPY 3,569M, R&D JPY 2,159M, depreciation JPY 2,307M.
- 9M vs plan [S31]: revenue +10.5% and OP +20.5% above the 12 Aug forecast, from higher memory output and next-quarter sales brought forward.
- FY2026 forecast raised 12 Nov 2026 [S30]: revenue JPY 110.0bn (from 103.8bn), OP 36.1bn (from 31.4bn), NI 26.8bn, EPS JPY 691.30; dividend JPY 208 (from 178; FY2025 JPY 95). FX JPY 158/$ [S29].
- Balance sheet [S28]: investment securities +JPY 23.7bn in 9M, with unrealised gains +JPY 16.3bn (holdings not identified).
- Plan FV26 (ends 2026) [S32]: original targets revenue JPY 80bn, OP JPY 20bn, ROE 23%; 2023-2026 capex JPY 60.8bn and R&D JPY 25.4bn vs JPY 48bn / 22bn planned; revenue CAGR 39% vs market 18% (company claim, own market estimate).

## 6. Field scan (company category = background, not re-verified unless sourced; figures from [S48]-[S54], 12 Nov 2026)

- **Tokyo Seimitsu / Accretech (7729.T)**: wafer probers plus dicing, grinding and metrology. TTM revenue JPY 182.2bn, OPM 21.6%, ROIC 27.1%, net cash JPY 57.4bn [S48]. Prober share could not be verified.
- **Tokyo Electron**: wafer probers; named by FormFactor as a probe-station rival [S9]. Prober data not separable (could not verify).
- **SEMICS (Korea)**: wafer probers; no data gathered (could not verify).
- **MPI (6223.TWO, Taiwan)**: probe cards, probe stations, photonics/thermal test; named FormFactor rival [S9]. TTM revenue TWD 18.9bn, NI TWD 5.58bn, OPM 33.4%, GM 58.7%, ROIC 27.4%; market cap TWD 456.1bn; 52-week +159% [S49]. Size fits the unlabelled 14% non-memory TechInsights slice (inference).
- **Chunghwa Precision Test Tech (6510.TWO)**: probe cards and test boards (background). TTM revenue TWD 6.10bn, OPM 32.1%, ROIC 27.0%; market cap TWD 105.2bn; 52-week +113% [S54].
- **WinWay (Taiwan)**: test sockets and interfaces; licensed Technoprobe's TPEG with ~US$60M minimum purchases over 5 years (Dec 2025) [S24]. Financials not gathered.
- **Japan Electronic Materials (6855.T)**: probe cards, memory-weighted (background); named FormFactor rival [S9]. TTM revenue JPY 37.5bn, OPM 28.5%, ROIC 26.8%, net cash JPY 19.4bn; market cap JPY 86.2bn [S53].
- **Korea Instrument; TSE (Korea)**: probe cards (TSE also sockets/boards); named FormFactor rivals [S9]. No financials gathered.
- **ISC (095340.KQ)**: rubber test sockets (background). TTM revenue KRW 278.1bn, NI KRW 77.6bn, OPM 30.3%, ROIC 31.4%, net cash KRW 359bn; market cap KRW 3.03T; 52-week +81% [S51].
- **Leeno Industrial (058470.KQ)**: pogo pins and test sockets (background). Market cap KRW 3.97T, OPM 37.1%, ROIC 37.8%, no debt; the page's TTM revenue (KRW 80.7bn) and trailing P/E (150) look incomplete (could not verify) [S50].
- **Techwing (089030.KQ)**: memory test handlers; its HBM "Cube Prober" could not be verified this session. TTM revenue KRW 184.8bn, net loss KRW 11.7bn, OPM 17.4%, ROIC 6.6%, net debt KRW 275.6bn; 52-week -36% [S52].
- **Nidec SV Probe; Smiths Interconnect (Smiths Group); STAr Technologies; Max One; Semishare; Wentworth**: probe cards, sockets or stations (STAr, Max One, Semishare, Wentworth named in [S9]); no financials gathered.
- **Xallent (US start-up)**: fine-pitch Kelvin micro-bump probing with IBM (SWTest 2025) [S43].
- **Chinese entrants**: none sourced (search budget exhausted). Technoprobe's Nexprobe JV is itself a China-based TPEG producer from Q1 2027 [S13].

## 7. Entry-point data (separate from quality)

- **FORM** [S11][S45], checked 12 Nov 2026: close $95.78 on 11 Nov (+11.85% that day); pre-market $93.15 on 12 Nov; 52-week +78.9%. Market cap $7.51bn; EV $7.14bn; P/E 44.06 trailing, 23.66 forward (implied ~86% EPS growth, bases may differ, my calc); EV/sales 7.29; EV/EBITDA 28.35; EV/FCF 39.4; short interest 3.3%; Buy (11), mean target $144.70. Path: $149.31 (30 Sep) → $141.30 (6 Oct, Teradyne signing day; Teradyne's ~$134.2 was ~5% below) → $110.31 (28 Oct, results after close) → $97.46 (29 Oct, -11.6%) → $71.76 (5 Nov low) → $95.78 (11 Nov). Teradyne's price is ~40% above the 11 Nov close (my calc). Cause of the sector-wide October-November fall not verified. Guidance: Q4 $285M ±$10M; Q3 margin helped by non-recurring tariff refunds [S3][S4]. Events: Teradyne closing (Q4 FY26), Farmers Branch ramp, restructuring completion, Q4 results (date not verified).
- **TPRO** [S26][S46], checked 12 Nov 2026: EUR 22.76 (12:49 CET); market cap EUR 14.57bn; EV EUR 13.90bn; P/E forward 34.23 (trailing 70.8 on stale TTM); on FY26 guide midpoint EUR 1,057.5M at ~47% EBITDA, EV/sales ~13.1x and EV/EBITDA ~28x (my calc); 52-week +116%. Path: EUR 28.98 (17 Sep; Vector Line paid EUR 29.88) → EUR 36.84 (6 Oct high) → EUR 20.52 (5 Nov low) → EUR 23.70 (11 Nov, results after close) → EUR 22.68 (12 Nov intraday, -4.3%); a Reuters headline said the 2026 outlook was "trimmed" [S46]. Liquidity: float 82.8M shares (12.9%) per [S26] vs 16.5% per company slide [S16]; 20-day volume 2.1M shares (~EUR 48M/day, my calc). An Aug 2026 headline said the stock entered Milan's top 15 by value (headline only) [S55]. Events: ERP recovery by end-2026; Cernusco ramp Feb 2027; Nexprobe ramp Q1 2027; CTO vacancy; Teradyne relationship shift; dual-listing option in the Vector Line pact (no plan announced) [S19]; 2027 financial calendar published 11 Nov 2026 (not read).
- **MJC** [S36][S47], checked 12 Nov 2026: JPY 10,100 (-2.4%), before the 15:30 JST beat and forecast raise; market cap JPY 391.6bn; EV JPY 378.0bn (may not net out ~JPY 24bn of investment securities, could not verify); P/E 20.9 trailing / 16.2 forward; 14.6x new FY26 EPS forecast; 2.1% yield on JPY 208 (my calc); 52-week +23.6%; 2 analysts, target JPY 10,900. Path: JPY 17,330 (9 Oct high) → JPY 8,672 (6 Nov low) → JPY 10,100. Events: market reaction on 13 Nov; next mid-term plan after FV26 (timing not verified); guided Q4 step-down.
- **Brief data, 12 Nov 2026** (trailing / forward P/E; EV/sales; EV/EBITDA; 52-week):
  - Tokyo Seimitsu 7729.T: JPY 13,290; mkt cap JPY 539.4bn; 17.7 / 14.7; 2.7; 10.9; +23.4%; Buy (9), target JPY 20,063; yield 2.4% [S48].
  - MPI 6223.TWO: TWD 4,655; mkt cap TWD 456.1bn; 81.6 / 38.5; 24.3; 62.9; +159%; Strong Buy (14), target TWD 8,098 [S49].
  - Leeno 058470.KQ: KRW 52,500; mkt cap KRW 3.97T; 150 / 20.1 (trailing data suspect); EV n/a; -8.1%; Buy (13), target KRW 91,538 [S50].
  - ISC 095340.KQ: KRW 143,400; mkt cap KRW 3.03T; 38.9 / 25.3; 9.6; 28.2; +81.3%; Strong Buy (10), target KRW 244,050 [S51].
  - Techwing 089030.KQ: KRW 38,450; mkt cap KRW 1.37T; loss / 12.7; 8.9; 34.0; -35.9% [S52].
  - For context: JEM 6855.T JPY 5,880, 10.2 / 11.5, EV/EBITDA 5.5 [S53]; CHPT 6510.TWO TWD 3,195, 63.5 / 34.4, EV/EBITDA 43.0 [S54].
- 5-10 year multiple ranges and formal consensus growth: could not verify for any company.

## 8. Could not verify
- A labelled TechInsights or VLSI ranking for 2024/2025; HBM probe-card share by supplier and by customer; wafer-prober shares.
- Customer names and China share for Technoprobe and MJC (MJC's annual report is encrypted and could not be text-extracted); identity of MJC's investment securities.
- When and how Advantest got its 5% of Technoprobe; whether Teradyne has changed its 10% since 11 Aug 2026; whether Gregory Smith was Teradyne's nominee (name match only); the identity of Vector Line's backer.
- Finest pitch of HBM probe cards in volume production; developers of e-beam or capacitive/inductive contactless probing; Techwing Cube Prober status; Korea Instrument, TSE, SEMICS, Nidec SV Probe, Smiths Interconnect and Chinese entrants' financials and positions.
- FormFactor's Q3'26 revenue by market and the call transcript (IR site returned HTTP 403; only a third-party summary [S4] used).
- Cause of the 44-52% fall in all three stocks from early October to 5-6 November 2026; 5-10 year valuation ranges; consensus growth rates.
- Production hybrid-bond pitch figures and SK hynix's Hot Chips remarks (search snippets only) [S39].

## 9. Sources (document date; all accessed 12 Nov 2026)

[S1]: https://www.eetimes.com/hybrid-bonding-comes-of-age-slowly-and-collectively/ "EE Times, Pat Brans, 26 Jan 2026"
[S2]: https://ieeetv.ieee.org/hbs/the-impact-of-hybrid-bonding-on-testing-3d-stacked-dies "IEEE.tv Marinissen talk, posted 23 Jan 2026"
[S3]: https://www.sec.gov/Archives/edgar/data/0001039399/000103939926000040/ex9901-earningsreleasexq326.htm "FormFactor Q3 2026 release, 28 Oct 2026"
[S4]: https://www.mitrade.com/insights/news/live-news/article-0-2207359-20261029 "Mitrade call summary, 29 Oct 2026 (third-party)"
[S5]: https://www.sec.gov/Archives/edgar/data/1039399/000103939926000043/form-20260926.htm "FormFactor 10-Q Q3 2026, filed 3 Nov 2026"
[S6]: https://www.sec.gov/Archives/edgar/data/1039399/000103939926000043/ex41-teradyneformfactorreg.htm "Registration rights agreement, 6 Oct 2026"
[S7]: https://www.sec.gov/Archives/edgar/data/1039399/000103939926000037/form-20261006.htm "FormFactor 8-K, filed 13 Oct 2026"
[S8]: https://www.sec.gov/Archives/edgar/data/1039399/000103939926000037/ex-991.htm "FormFactor-Teradyne release, 12 Oct 2026"
[S9]: https://www.sec.gov/Archives/edgar/data/1039399/000103939926000009/form-20251227.htm "FormFactor 10-K FY2025, filed 20 Feb 2026"
[S11]: https://stockanalysis.com/stocks/form/statistics/ "stockanalysis FORM statistics, 12 Nov 2026"
[S12]: https://www.technoprobe.com/wp-content/uploads/2026/11/PR-9M-2026.pdf "Technoprobe 9M 2026 release, 11 Nov 2026"
[S13]: https://www.technoprobe.com/wp-content/uploads/2026/11/9M_2026_Results.pdf "Technoprobe 9M 2026 presentation, 11 Nov 2026"
[S14]: https://www.emarketstorage.it/sites/default/files/comunicati/2026-08/20260805_187949.pdf "Technoprobe H1 2026 release (Italian), 5 Aug 2026"
[S15]: https://www.technoprobe.com/wp-content/uploads/2026/03/PR-FY-2025_.pdf "Technoprobe FY2025 release, 18 Mar 2026"
[S16]: https://www.technoprobe.com/wp-content/uploads/2026/05/Technoprobe-Company-Presentation-May-2026.pdf "Technoprobe company presentation, 19 May 2026"
[S17]: https://www.technoprobe.com/wp-content/uploads/2026/08/Closing-PJ-Ibiza_Closing-PJ-Ibiza-VF.pdf "China partnership closing, 14 Aug 2026"
[S18]: https://www.technoprobe.com/wp-content/uploads/2026/09/Comunicato-in-nome-e-per-conto-di-T-PLUS-Press-Release-on-behalf-of-T-PLUS.pdf "T-Plus / Vector Line release, 22 Sep 2026"
[S19]: https://www.technoprobe.com/wp-content/uploads/2026/09/Informazioni-essenziali-ex-art.130-RE_Patto-Tplus-Vector-Line.pdf "T-Plus / Vector Line pact, 22 Sep 2026"
[S20]: https://www.technoprobe.com/wp-content/uploads/2026/08/Key-Information_Update-ENG.pdf "T-Plus / Teradyne / Technoprobe pact update, 11 Aug 2026"
[S21]: https://www.technoprobe.com/wp-content/uploads/2026/07/Estratto-Patto-Parasociale-Ex-art.129-RE-Estratto-Breve-VF.pdf "T-Plus / CK Yang pact extract, 20 Jul 2026"
[S22]: https://www.technoprobe.com/wp-content/uploads/2026/09/Director-resignation.pdf "Director resignation, 29 Sep 2026"
[S23]: https://www.technoprobe.com/wp-content/uploads/2026/11/PR-CTO.pdf "CTO resignation, 4 Nov 2026"
[S24]: https://www.technoprobe.com/wp-content/uploads/2025/12/PR-Strategic-Agreement.pdf "WinWay TPEG agreement, 9 Dec 2025"
[S25]: https://www.technoprobe.com/wp-content/uploads/2026/02/PR_US-Litigation.pdf "US litigation release, 19 Feb 2026"
[S26]: https://stockanalysis.com/quote/bit/TPRO/statistics/ "stockanalysis TPRO statistics, 12 Nov 2026"
[S28]: https://ssl4.eir-parts.net/doc/6871/tdnet/2913248/00.pdf "MJC Q3 FY2026 kessan tanshin, 12 Nov 2026"
[S29]: https://ssl4.eir-parts.net/doc/6871/tdnet/2913283/00.pdf "MJC Q3 FY2026 supplementary material, 12 Nov 2026"
[S30]: https://ssl4.eir-parts.net/doc/6871/tdnet/2913336/00.pdf "MJC forecast and dividend revision, 12 Nov 2026"
[S31]: https://ssl4.eir-parts.net/doc/6871/tdnet/2913300/00.pdf "MJC 9M forecast-vs-actual notice, 12 Nov 2026"
[S32]: https://ssl4.eir-parts.net/doc/6871/ir_material_for_fiscal_ym4/210517/00.pdf "MJC Q2 FY2026 results presentation (incl. TechInsights share chart), 13 Aug 2026"
[S33]: https://ssl4.eir-parts.net/doc/6871/ir_material_for_fiscal_ym4/198705/00.pdf "MJC FY2025 results presentation, 16 Feb 2026"
[S34]: https://ssl4.eir-parts.net/doc/6871/tdnet/2781196/00.pdf "MJC capacity capex notice, 26 Mar 2026"
[S35]: https://ssl4.eir-parts.net/doc/6871/tdnet/2859518/00.pdf "MJC land acquisition, 31 Jul 2026"
[S36]: https://stockanalysis.com/quote/tyo/6871/statistics/ "stockanalysis 6871 statistics, 12 Nov 2026"
[S37]: https://www.yolegroup.com/product/quarterly-monitor/semiconductor-test-consumables-market-monitor/ "Yole monitor product page (search snippet), 2026"
[S38]: https://techinsights.com/ja/node/59943 "TechInsights Annual Probe Card Report summary, May 2025 (description only)"
[S39]: https://www.tomshardware.com/tech-industry/semiconductors/hybrid-bonding-roadmap-examined "Tom's Hardware, 2026 (search snippets only)"
[S41]: https://eps.ieee.org/wp-content/uploads/2026/10/HIR_17_Test_Technology_final.pdf "IEEE HIR 2025 ed., Ch.17 Test Technology, posted Oct 2026"
[S42]: https://www.swtest.org/library/2025proc/pdf/M02_03_DUBE_SWTest-2025.pdf "SWTest 2025, FormFactor & Intel, Jun 2025"
[S43]: https://www.swtest.org/library/2025proc/pdf/M03_03_KUMAR_SWTest-2025.pdf "SWTest 2025, Xallent & IBM, Jun 2025"
[S44]: https://www.swtest.org/library/2025proc/pdf/T06_02_VARGA_SWTest-2025.pdf "SWTest 2025, EV Group, Jun 2025"
[S45]: https://stockanalysis.com/stocks/form/history/ "FORM price history, to 11 Nov 2026"
[S46]: https://stockanalysis.com/quote/bit/TPRO/history/ "TPRO price history, to 12 Nov 2026"
[S47]: https://stockanalysis.com/quote/tyo/6871/history/ "6871 price history, to 12 Nov 2026"
[S48]: https://stockanalysis.com/quote/tyo/7729/statistics/ "Tokyo Seimitsu statistics, 12 Nov 2026"
[S49]: https://stockanalysis.com/quote/tpex/6223/statistics/ "MPI statistics, 12 Nov 2026"
[S50]: https://stockanalysis.com/quote/kosdaq/058470/statistics/ "Leeno statistics, 12 Nov 2026"
[S51]: https://stockanalysis.com/quote/kosdaq/095340/statistics/ "ISC statistics, 12 Nov 2026"
[S52]: https://stockanalysis.com/quote/kosdaq/089030/statistics/ "Techwing statistics, 12 Nov 2026"
[S53]: https://stockanalysis.com/quote/tyo/6855/statistics/ "JEM statistics, 12 Nov 2026"
[S54]: https://stockanalysis.com/quote/tpex/6510/statistics/ "CHPT statistics, 12 Nov 2026"
[S55]: https://www.finanzaonline.com/notizie/rally-forsennato-di-technoprobe-35-dopo-rialzo-guidance-lai-stock-lombarda-entra-nella-top-15-di-piazza-affari "finanzaonline headline, Aug 2026 (headline only)"
