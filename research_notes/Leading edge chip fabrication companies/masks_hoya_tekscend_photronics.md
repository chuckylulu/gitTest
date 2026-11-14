# Photomasks and mask blanks: Hoya, Tekscend Photomask, Photronics (shorter: DNP, AGC, mask-writer makers) — fact base as of 14 November 2026

Scope and method. Share prices are closes of 13 Nov 2026. Figures come from primary documents read in this session (kessan tanshin, securities reports, prospectus, Forms 10-K/10-Q/8-K, results decks, call transcripts) plus market-data pages. The session's shared web-search allowance ran out after four searches, so Nikkei/Reuters/Bloomberg could not be searched; everything else was fetched directly from company IR sites, SEC EDGAR, the eBeam Initiative and data pages (Kabutan, StockAnalysis, karauri.net). Gaps this caused are listed at the end.

Tags: [FILING] filed/audited or statutory-disclosure figure · [COMPANY CLAIM] company statement no outside party has confirmed · [CONFIRMED] company statement confirmed by a named outside party · [ESTIMATE] third-party estimate (incl. consensus and vendor-computed ratios) · [PRESS] secondary press summary. Share prices/volumes are exchange data quoted from Kabutan or StockAnalysis and carry only the source. "My calc" = arithmetic on cited figures. "Case against" bullets restate facts tagged earlier in the same section. Source IDs in square brackets resolve to URLs in the link list at the bottom of the file. Some SEC documents were read through a summarising fetch tool rather than line by line; figures from them match the press releases where both were read.

Fiscal years: Hoya "FY25" = April 2025–March 2026, "FY26" = year to March 2027. Tekscend calls the year to March 2027 "FY2026". Photronics FY2026 ended about 1 Nov 2026 (Q3 = quarter ended 2 Aug 2026). AGC's year is the calendar year. DNP "FY2026" = year to March 2027.

## Market structure: captive versus independent mask makers, EUV, writers, pellicles, blanks — who has pricing power?

### Takeaway
Captive mask shops hold roughly two-thirds of mask revenue (TSMC alone about 36% in 2024) and nearly all EUV mask production; independents hold about one-third, mostly below the leading edge, led by Tekscend (40.5% of merchant revenue, 2025). The margin evidence puts pricing power upstream of the merchant mask makers: Hoya's blank-and-substrate segment earns about 55% operating margin against 21–25% for Tekscend and Photronics, and Tekscend says it is absorbing blank price increases.

### Cited Findings
| Measure | Figure | Who measured / period | Tag, source |
|---|---|---|---|
| Captive : merchant split by value | 66.7% : 33.3% | SEMI "2025 Photomask Characterization Study", CY2025, as reproduced by Tekscend (10 Sep 2026) | [COMPANY CLAIM citing SEMI; SEMI report not seen] [T-IRF] |
| World mask revenue shares | TSMC captive 36%, other captive 30%, Tekscend 14%, other merchant 20% | Tekscend chart, CY2024, same SEMI basis | [COMPANY CLAIM citing SEMI] [T-IRF] |
| Captive : merchant, qualitative | captive 60–70% "mostly advanced nodes"; merchant 30–40% "mostly mature nodes, ~60% from Japanese companies" | N. Hayashi (DNP) keynote, eBeam Initiative, 9 Sep 2026 | [ESTIMATE] [M-HAY] |
| Total mask market | $5.0bn (2024), $5.28bn (2025), $6.5–7.8bn (2026E) | DNP estimate, same keynote | [ESTIMATE] [M-HAY] |
| Merchant market | $2,419m (2024), $2,701m (2025), $3,040m (2026F), $4,339m (2030F); CAGR 2024–30 10.2% | "DNP estimates based on SEMI data", 13 Jul 2026 | [ESTIMATE] [D-IRD] |
| Merchant market | $2.1bn (CY24) → $3.4bn (CY30E), CAGR 8.7%; later deck $2.0bn (CY25) → $2.6bn (CY28F), CAGR 9.1% | Tekscend, third-party vendor data + own estimate | [COMPANY CLAIM] [T-IRF], [T-H1B] |
| Merchant share, No.1 | Tekscend 40.5% in CY2025 (+2.7pt), tenth year at No.1; CY2024 37.8% | SEMI study, as cited by Tekscend | [COMPANY CLAIM citing SEMI] [T-H1B], [T-ASR] |

- Captive makers outsource the generation behind the edge. Tekscend: "captive manufacturers concentrat[e] on leading-edge technologies" and outsource nodes "one generation behind"; mask count per set rises from about 50 (28nm) to 70 (14nm) to 90 (7nm) [COMPANY CLAIM] — [T-FYQA]. DNP says the same and adds that "cutting-edge non-EUV optical masks will also be progressively outsourced" [COMPANY CLAIM] — [D-IRDQ].
- EUV work at independents is still pre-volume. Tekscend (13 May 2026): "the merchant [EUV] mask market itself has not yet been fully formed"; EUV was "around 5%" of its FY to March 2026 revenue, expected "around 8–9% by 2027–2028" [COMPANY CLAIM] — [T-FYQA]. Tekscend (Feb 2026): "Our primary EUV mask customers are currently Japanese manufacturers. We are developing prototypes and preparing for future mass production"; TSMC's Kumamoto fab's masks are "mainly produced in-house" [COMPANY CLAIM] — [T-3QQA]. DNP: EUV "test masks have already been sold"; volume production still ahead [COMPANY CLAIM] — [D-FYQ].
- Memory is the new outsourcing source. Tekscend: since the second half of its FY2025 "outsourcing has been on an increasing trend, driven by capacity constraints in in-house production at memory manufacturers"; the demand is "for DRAM photomasks" [COMPANY CLAIM] — [T-H1B], [T-Q1QA]. Samsung Electronics was 11.6% of Tekscend revenue in the year to March 2026 (¥15,063m), below 10% the year before [FILING] — [T-ASR].
- Chinese entrants: "There are already 20 or more photomask makers in China" (Tekscend, Nov 2025) [COMPANY CLAIM] — [T-1HQA25]. Photronics' 10-K names Shenzhen Newway and Shenzhen Qingyi among competitors [FILING] — [P-10K]. 96% of eBeam "luminaries" expect new mask shops in China by 2031 [ESTIMATE] — [M-EBLUM].
- Mask blanks. Hayashi lists blank suppliers as "HOYA, Shinetsu, AGC, S&S" [ESTIMATE] — [M-HAY]. Hoya (Apr 2026 FAQ): "Currently, only Japanese companies manufacture EUV blanks"; a Korean entrant is acknowledged [COMPANY CLAIM] — [H-3QF]. Hoya (30 Oct 2026): "qualified at all layers for N2 and A14 … currently see no competitor presence in A10. Some competing products are used for binary masks in mature EUV nodes such as 7nm and 5nm, but only to a limited extent" [COMPANY CLAIM] — [H-Q2T]. AGC (2 Jun 2026): "one of the market's leading two players"; EUV-blank sales reached ¥40bn in 2024, fell in 2025, recovering in 2026; its customers "are in mass production down to the 2-nm node for logic and the D1D generation for DRAM" and it is "also in mass production for phase shift masks" [COMPANY CLAIM] — [A-SEMI], [A-SEMIT].
- Blank pricing. Hoya: EUV-blank growth is "driven primarily by higher ASPs resulting from an improved product mix" (phase-shift and low-defect grades) [COMPANY CLAIM] — [H-Q1F]; but "discount demands for existing products (7nm, 5nm, binary, etc.) are extremely strong, and every customer makes annual requests for price reductions" [COMPANY CLAIM] — [H-3QT]. Tekscend: "we have also received price increase requests from blank suppliers and some of this impact remains our burden"; "EUV blanks are extremely expensive compared to conventional photomasks" [COMPANY CLAIM] — [T-3QQA], [T-FYQA].
- Mask pricing. Tekscend: "it is not always possible to fully pass through all costs"; negotiations "take place within a competitive environment" [COMPANY CLAIM] — [T-FYQA]. 45% of eBeam luminaries expect the fair-market value of a leading-edge logic mask set to rise at least 1.5x by 2031 (35% for DRAM); most others expect a smaller rise [ESTIMATE] — [M-EBLUM].
- Multi-beam writers. Hayashi lists e-beam writer makers as "NuFlare, IMS, JEOL, Vistec" and warns of "dependence on a few key players in each category and limited capacity" [ESTIMATE] — [M-HAY]. Intel consolidates IMS Nanofabrication; non-controlling holders owned 32% at 26 Sep 2026 (unchanged from a year earlier); income attributable to that 32% was $28m in the nine months of 2026 against a $25m loss a year earlier [FILING] — [M-INTC]. 93% of eBeam luminaries expect multi-beam writer purchases to rise over three years; 94% expect 2026 mask revenue above 2025 [ESTIMATE] — [M-EBPR]. Photronics cut FY2026 capex guidance from about $330m to $255–305m [FILING] — [P-10Q]; a call summary attributes the cut to the timing of vendor deliveries [PRESS] — [P-MB]. Tekscend: equipment and materials "are often specified by the customer", so switching supplier is hard [FILING] — [T-ASR].
- Pellicles. Suppliers listed: "Mitsui, Shin-Etsu, MLI, FST" [ESTIMATE] — [M-HAY]. 44% of luminaries say a pellicle extends EUV mask life more than 3x (32% a year earlier) [ESTIMATE] — [M-EBLUM].
- High-NA. 66% of luminaries expect 6x12-inch large-format masks within a decade [ESTIMATE] — [M-EBPR]. Hoya is "advancing customer engagement and internal validation for 12-inch High-NA large mask blanks" [COMPANY CLAIM] — [H-Q2P]. Tekscend's CEO expects Low-NA to carry 2nm to about 1.4nm, with High-NA "around 2029–2030" [COMPANY CLAIM] — [T-FYQA].
- Margins along the chain (latest quarter): Hoya Information Technology segment 55.1% [FILING] — [H-Q2R]; Tekscend 24.6% [FILING] — [T-H1B]; Photronics 21.1% [FILING] — [P-Q3].

### Inferences
- (Mine) The margin gap, plus Tekscend's admission that it absorbs blank price rises, says value accrues to the EUV-blank duopoly and to writer/inspection vendors rather than to merchant mask makers. Hoya's own remark about annual price-down requests on mature EUV grades shows that power is strongest at the newest node, where it has no qualified rival.
- (Mine) Merchant growth depends on captive shops running out of capacity, not on independents winning EUV work; a captive capacity catch-up would reverse it.
- (Mine) Market-size sources disagree by a wide margin (see conflicts list); shares are firmer than dollar sizes.

### Gaps
- No independent count of EUV masks per node or EUV mask prices was obtained; no SEMI document was read directly.
- IMS's named holders (Bain Capital, TSMC), writer capacity and backlog, NuFlare shipments and EUV pellicle capacity were not verifiable from the pages reached.
- No independent measurement of EUV-blank shares (Hoya versus AGC versus S&S Tech) was found.

## Hoya (TSE 7741)

### Takeaway
Hoya's Information Technology segment (mask blanks, HDD glass substrates, display masks, optics) is 41% of revenue and about 64% of segment profit at a 55% margin, growing over 20%, and is funding its own expansion and buybacks from ¥520bn of net cash. The questions are whether segment margins hold once new-plant depreciation arrives (peak FY28–29), whether a second blank supplier gains ground, and a share price at 28.5 times trailing earnings that fell after record results.

### Cited Findings
#### (a) Position
- Supplies mask blanks (EUV and DUV) to captive and merchant mask shops; also HDD glass substrates, display photomasks and optical glass [FILING] — [H-Q2R]. EUV-blank share: company says "our structure ensures high market share" (FY25 Q2 call, autumn 2025) [COMPANY CLAIM] — [H-2QT25]; no numeric share appears in any document read. Position at the leading edge: one of two volume suppliers; sole presence at A10 and all-layer qualification at N2/A14 are company statements only [COMPANY CLAIM] — [H-Q2T]. AGC's statement that 2nm-class volumes and phase-shift blanks are in mass production sits in tension with Hoya's description of rivals as confined to mature binary grades [COMPANY CLAIM] — [A-SEMIT].
- Customers: "very strong orders from major customers in both Taiwan and South Korea"; "some customers are evaluating a second supplier, a situation that has not changed" [COMPANY CLAIM] — [H-3QT]. Shipments to memory makers (HBM, DRAM) rising [COMPANY CLAIM] — [H-Q1F]. Customer concentration and China share are not disclosed; Asia/Oceania was 39.2% of FY25 revenue and 41.4% in Jul–Sep 2026 [FILING] — [H-FYR], [H-Q2R].
- HDD substrates: one main customer, a second starting in the fiscal fourth quarter, a third tied to HAMR ramp [COMPANY CLAIM] — [H-Q2T].
- Listing: TSE Prime, Nikkei 225 and TOPIX Core 30 member; 334.8m shares issued — [H-KB]; widely held (institutions about 63% per a data vendor [ESTIMATE] — [H-SA]); the largest-holder list was not checked.

#### (b) Economics
| ¥m | FY25 (Apr 2025–Mar 2026; published 30 Apr 2026) | Q2 FY26 (Jul–Sep 2026; published 30 Oct 2026) | H1 FY26 |
|---|---|---|---|
| Revenue | 947,749 (+9.4%) | 260,153 (+10.9%; constant currency +6%) | 515,895 (+13.4%) |
| Profit from ordinary operating activities | 285,241 (30.1%) | 89,354 (34.3%, +27.2%) | 171,721 (33.3%) |
| IFRS operating profit (IFRS 18 from FY26) | n/a | 90,805 (+33.2%) | 173,431 |
| Pre-tax profit | 327,668 (incl. about ¥35bn one-offs) | 91,591 | 177,586 |
| Profit to owners | 253,085 (+25.2%) | 70,709 (+27.6%) | 136,500 |
| Non-controlling share | –1,634 | –103 | –60 |
| EPS (¥) | 743.93 | 211.85 | 408.44 |
| Operating cash flow | 278,446 | 88,189 | 158,189 |
| Free cash flow (company definition: operating + investing) | 270,860 | 72,812 | 135,706 |
| Capital expenditure | 65,711 | 17,836 | — |
| R&D | 36,291 | 10,220 | — |
| Cash / interest-bearing debt | 574,092 / 42,241 | 561,941 / 42,211 | |
| Equity ratio | 78.4% | 77.8% | |
| Life Care revenue / segment profit | 590,680 / 107,003 (18.1%) | 153,366 / 32,585 (21.2%) | |
| Information Technology revenue / segment profit | 354,751 / 186,323 (52.5%) | 106,787 / 58,835 (55.1%) | |
| of which electronics (blanks, display masks, HDD substrates) | 295,757 | 89,440 | |

All [FILING] — [H-FYR], [H-Q2R]. Notes: FY25 free cash flow includes ¥41.1bn from sale of investments; operating cash flow less property purchases was ¥221.9bn (my calc) — [H-FYR]. The one-offs were about ¥24bn on buying out a China intraocular-lens venture partner, ¥7bn of divestments and ¥4bn of FX [COMPANY CLAIM] — [H-3QF]. Hoya reports no gross margin (expenses by nature); a vendor-derived trailing figure is 55.8% [ESTIMATE] — [H-SA].
- Returns: ROIC 21.1% for FY25 and 26.0% in Q2 FY26 [COMPANY CLAIM, own definition] — [H-FYT], [H-Q2P]; ROE 25.4% for FY25 (my calc on [H-FYR]); 27.7% trailing [ESTIMATE] — [H-SA].
- Product growth, Jul–Sep 2026: mask blanks +20% (EUV "+25% or more"), display masks +21%, HDD substrates +32% (3.5-inch "just under +30%"), optics +14%; in Life Care, eyeglass lenses +8% (constant currency +1%), endoscopes –10%, intraocular lenses +5% [COMPANY CLAIM] — [H-Q2P], [H-Q2T].
- Guidance: full-year FY26 revenue ¥1,043bn (+10.1%), issued 30 Oct 2026 only because the disclosure threshold was crossed; no profit forecast until the third-quarter release [FILING] — [H-Q2J]. Verbal: EUV blanks over 20%, DUV low single digit, blanks about 15%; HDD substrates raised from about 10% to over 15% [COMPANY CLAIM] — [H-Q2T].
- Returns to shareholders: FY25 treasury purchases ¥171,970m and dividends paid ¥81,903m [FILING] — [H-FYR]; ¥100bn buyback completed 17 Apr 2026 (3,576,300 shares, cancelled) [FILING] — [H-BB1]; ¥200bn authorised 31 Jul 2026 to 24 Mar 2027, ¥75.0bn spent by 31 Oct 2026 [FILING] — [H-BB2], [H-BB3]. FY25 dividend ¥295; FY26 interim ¥160 [FILING] — [H-Q2R].

#### (c) Execution record
- April 2026 outlook was blanks "10% plus, potentially up to around 15%" and HDD "high single-digit" [COMPANY CLAIM] — [H-FYT]; first-half delivery was blanks +20–21% and HDD +29–32%, and the outlook was raised twice — [H-Q1T], [H-Q2T].
- Segment margin benchmark moved from 50% to "around 52%" (Jul 2026) after 55.1% in two consecutive quarters; management said 55% "would not be easy to maintain" [COMPANY CLAIM] — [H-Q1T].
- Life Care: 20% margin benchmark reached (21.2%, including about 100bp temporary), but revenue was "below our internal plan", with US eyeglass lenses, China intraocular lenses and endoscopes named [COMPANY CLAIM] — [H-Q2T]. Impairments ¥4.9bn (FY25) and ¥6.1bn (FY24) [FILING] — [H-FYR]. Endoscope business put under strategic review including sale (31 Jul 2026) [FILING] — [H-ENDO].
- 2024 IT incident (an analyst on the May 2025 call called it "a cyber incident"): in April–June 2024 eyeglass lenses were "most affected", endoscope "production [was] suspended", inventory was written off and extra sales spending followed; the recovery phase was declared over in January–March 2025 [COMPANY CLAIM] — [H-24Q1T], [H-24Q4T].
- EUV blanks "dropped sharply due to inventory adjustments" in FY24 before recovering [COMPANY CLAIM] — [H-24Q4T].
- Outside confirmation: AGC and DNP's Hayashi confirm a small supplier set [M-HAY]; no outside party has confirmed Hoya's share, its A10 exclusivity or High-NA progress.

#### (d) Path forward
- Technology: A14/A10 need new phase-shift film materials and more EUV layers per set ("value added will be higher than in the N2 generation") [COMPANY CLAIM] — [H-Q1T]; High-NA 12-inch blanks under validation, pricing unsettled [COMPANY CLAIM] — [H-Q2T].
- Capacity: existing cleanrooms cover volume "through FY2027" [COMPANY CLAIM] — [H-3QT]; a new Singapore building, "total investment will exceed ¥40 billion" (call) or "50 billion yen" (FAQ), with production in FY28 [COMPANY CLAIM] — [H-FYT], [H-FYF]. HDD: Laos runs 4 of 12 possible lines, the rest installed through FY27; new Vietnam plant about ¥50bn, FY28, phase 1 under half of planned scale [COMPANY CLAIM] — [H-Q1T], [H-FYT]. CEO: "one new plant in each business may not be sufficient" [COMPANY CLAIM] — [H-Q2T].
- Cost: FY26 investment decisions of ¥120–130bn spread over FY26–28; depreciation up 5–6% in FY26, peaking "around fiscal 2028 to 2029" [COMPANY CLAIM] — [H-FYT].
- Funding: internal. Target net cash about ¥460bn; excess about ¥110bn at March 2026; more than 100% of free cash flow to be returned over about three years; ¥300bn kept for acquisitions and risk [COMPANY CLAIM] — [H-FYT], [H-FYF], [H-Q2T].

#### (e) Market facts (kept apart)
- Close 13 Nov 2026 ¥23,925; market value ¥8.01tn on issued shares — [H-KB]; ¥7.93tn excluding treasury stock [ESTIMATE] — [H-SA]. Net cash ¥519.7bn (my calc on [H-Q2R]).
- Trailing P/E 28.5x (trailing EPS ¥839.2, my calc; vendor 28.48x); price/book 7.83x; EV/EBITDA 18.0x [ESTIMATE] — [H-SA], [H-KB]. Consensus (17–18 analysts): FY to March 2027 revenue ¥1.05tn, EPS ¥834.83; FY to March 2028 revenue ¥1.15tn, EPS ¥957.48, i.e. 28.7x and 25.0x; 15 of 18 ratings are buy or strong buy, mean target ¥30,561, range ¥23,100–40,000 [ESTIMATE] — [H-SA]. Own history: the same vendor's fiscal-year P/E series runs 24.6–36.0 over FY2022–FY2026 [ESTIMATE; series definition unclear] — [H-SA].
- 2026 year to date +1.0% (from ¥23,685 on 30 Dec 2025); 12 months –1.6% (from ¥24,325 on 13 Nov 2025); 52-week high ¥30,400 (15 Apr 2026), low ¥21,575 (6 Nov 2026) — [H-KB], [H-SA].
- Reaction to results of 30 Oct 2026: closed ¥26,210 that day, ¥24,775 on 2 Nov (–5.5%), ¥22,395 on 6 Nov (–7.0% on a day when DNP, AGC and Tekscend also fell 5–9%), ¥23,925 on 13 Nov — [H-KB].
- Short data: no institutional short position of 0.5% or more reported since 2022 — [H-KU]; margin balances 6 Nov 2026: 11,900 shares short against 143,300 long — [H-KB].

#### (f) Case against
- Business: Life Care (59% of revenue) is not growing in constant currency and missed plan [H-Q2T]; segment margin sits above management's own sustainable level with depreciation rising from FY27 [H-Q1T]; HDD demand rests on hyperscaler spending, and Hoya called HDD makers' consideration of in-house glass substrates "within our expectations" [H-Q1T]; customers are evaluating a second blank supplier and a Korean entrant exists [H-3QT]; AGC is recovering share-relevant volume [A-SEMIT]; blank buyers are few (AGC: "not that many customers") [A-SEMIT].
- Governance: a shareholder derivative suit (notice 19 Feb 2026) seeks ¥23,624m from seven current and former directors, alleging the 2016 buyback exceeded the distributable amount; the company intervened for the defendants [FILING] — [H-LAW], [H-LAW2]. The 2024 IT incident; controls adopted since were not found in documents read.
- Shares: valuation leaves little margin (28.5x trailing, 7.8x book) and the stock fell on record numbers; against a short, ¥125bn of buyback authority remains to 24 Mar 2027 and no large holder is a known seller.
- Dated events: third-quarter results and first full-year profit forecast (late January or early February 2027) [H-Q2J]; outcome of the endoscope review; buyback end 24 Mar 2027; Vietnam Tet shutdown lowering fourth-quarter HDD margin [H-Q2T].

### Inferences
- (Mine) Business quality is high on the filed numbers: 30%+ operating margin, 25% ROE with 78% equity ratio, capex under 7% of revenue. The dependence is on one segment for two-thirds of profit.
- (Mine) The plan to 2030 is funded several times over from internal cash; the execution risk is timing of capacity against customer ramps, not money.
- (Mine) As a short, Hoya offers no obvious catalyst other than a margin reset when depreciation steps up or a visible second-source award; the buyback and absent short interest argue against crowding either way.

### Gaps
- Numeric EUV-blank share, size of the blanks business within the segment, customer concentration and China revenue are undisclosed.
- Why the shares fell 5.5% on 2 Nov 2026 was not established (no press access).

## Tekscend Photomask (TSE 429A; formerly Toppan Photomask)

### Takeaway
Tekscend is the largest independent mask maker (40.5% of merchant revenue) with improving mix and margins (operating margin 24.6% in Jul–Sep 2026), but it has entered a capex phase (¥63bn this year, above EBITDA) funded partly by ¥50bn of new bank debt, its EUV business is still prototypes, and China is 29% of revenue. The shares closed at ¥3,005, the ¥3,000 offer price of October 2025, with Toppan Holdings still holding 46.5% and free to sell since April 2026.

### Cited Findings
#### (a) Position
- Merchant photomasks from mature nodes to EUV development; revenue by node in Apr–Sep 2026: advanced (28nm and below) 38% (40% in Jul–Sep), middle 34%, mature 28%; logic 88%, memory 12% [FILING/briefing] — [T-H1B].
- Share and rivals: 40.5% of merchant revenue in CY2025 per SEMI as cited [COMPANY CLAIM citing SEMI] — [T-H1B]. The share figure for 2024 was corrected twice, from 38.9% to 37.8%, "due to errors in the underlying calculations" [FILING] — [T-CORR]. Competitors: Photronics, DNP, Chinese entrants; captive shops are both customers and potential competitors [FILING] — [T-ASR].
- Revenue by destination, Apr–Sep 2026 (US-dollar basis, read from chart): China 29%, United States 21%, Taiwan 13%, Europe 12%, Korea 11%, Japan 8%, other 6%; China was 28% in the year to March 2026 and 30% in each of the two quarters to June 2026 [FILING/briefing] — [T-H1B], [T-Q1B].
- Customers: Samsung Electronics 11.6% of revenue (year to March 2026) [FILING] — [T-ASR]; customers without mask shops named as UMC, Texas Instruments, STMicroelectronics, Infineon, GlobalFoundries [COMPANY CLAIM] — [T-IRF].
- Sites and ventures: plants in Japan (Asaka, on land leased from Toppan), Taiwan, Korea, the United States (Round Rock), China (Shanghai), a new Singapore plant, and Dresden via AMTC, a 50:50 venture with GlobalFoundries whose capacity is split 70% GlobalFoundries, 30% Tekscend [FILING] — [T-ASR]. The Shanghai Xuhui plant's leased buildings have four regulatory deficiencies; suspension or relocation is a stated risk [FILING] — [T-ASR].
- EUV partners: joint development agreement with IBM (25 Jan 2024, five years, 2nm-node EUV masks "including High-NA") [FILING] — [T-ASR]; "the only merchant mask vendor with development partnerships with both IBM and imec" [COMPANY CLAIM] — [T-IRF]. These are development agreements; no production order is disclosed. Rapidus is not named in any Tekscend document read.
- Ownership: at the IPO Toppan Holdings went from 50.10% to 46.57%; the Integral funds sold essentially everything (Ice Integral 2 LP from 20.91% to nil) [FILING] — [T-PAR]. At 30 Sep 2026: Toppan 46.52%, Master Trust 7.79%, Qatar Holding 4.76%, Integral 0.85%; Eastspring reported 6.43% [FILING] — [T-H1R]. One of seven directors is Toppan's CFO [FILING] — [T-CTRL].

#### (b) Economics
| ¥m | Year to Mar 2026 (published 13 May 2026) | Jul–Sep 2026 (published 11 Nov 2026) | Apr–Sep 2026 |
|---|---|---|---|
| Revenue | 129,576 (+9.8%) | 37,944 (+19.7%; US$ +11.4%) | 72,462 (+17.3%; US$ +7.1%) |
| Gross margin | 33.4% | 36.6% | 35.0% |
| Operating profit | 27,530 (21.2%; –2.4%) | 9,339 (24.6%) | 16,699 (23.0%; +29.5%) |
| Profit to owners (no minorities) | 24,947 | 6,752 | 12,053 (–2.4%) |
| EBITDA | 46,567 (35.9%) | 14,231 (37.5%) | 26,460 (36.5%) |
| Operating cash flow | 36,061 | — | 21,162 |
| Capital expenditure | 33,236 | 15,302 | 22,720 |
| Free cash flow | about +900 | — | –749 |
| R&D expense | 1,238 | — | — |
| Cash / borrowings | 51,552 / 1,460 | | 91,537 / 50,199 |
| Equity ratio | 75.6% | | 63.1% |
| ROE | 17.2% | | |

All [FILING] — [T-FYR], [T-ASR], [T-H1B]. Profit for the half fell because of "a decrease in the fair value of financial assets" (currency-swap valuation) [FILING] — [T-H1B].
- Guidance (unchanged 11 Nov 2026): revenue ¥140,100m (+8.1%), operating profit ¥29,800m (+8.2%), profit ¥23,700m (–5.0%), EBITDA margin 34.2%, dividend ¥70, assuming ¥145 per dollar against ¥160.04 actual in the half; half-year progress 51.7% of revenue and 56.0% of operating profit [COMPANY CLAIM] — [T-H1B]. Capex plan ¥63.0bn (growth ¥48.5bn, renewal ¥6.0bn, other ¥8.5bn) [FILING] — [T-ASR].
- Medium-term aims: revenue growth about 10% a year, operating margin about 20%, EBITDA margin about 40%; 78.8% of equipment fully depreciated [COMPANY CLAIM] — [T-IRF].

#### (c) Execution record
- Listing: 16 Oct 2025, offer price ¥3,000 (range ¥2,900–3,000); 7,000,000 new shares (about ¥19.5bn net to the company); 39,133,200 existing shares sold by five Integral-affiliated funds, upsized from 32,611,000, plus 6,070,300 over-allotment; 180-day lock-up to 13 Apr 2026 covering the sellers, Toppan, option holders and cornerstone Qatar Holding [FILING] — [T-IPO]. Total about 52.2m shares, about ¥157bn (my calc). No later sale by Toppan appears: 46,237,901 shares at IPO and 46,237 thousand at 30 Sep 2026 [FILING] — [T-PAR], [T-H1R].
- First-year forecast: ¥125,291m revenue, ¥25,500m operating profit, ¥18,878m profit (as standing 12 Feb 2026) was raised on 27 Mar 2026 and actuals came in at ¥129,576m, ¥27,530m and ¥24,947m; the profit beat owed much to "higher-than-expected derivative valuation gains" [FILING] — [T-REV], [T-FYR].
- Operating profit nonetheless fell 2.4% in that year and operating margin went 28.5%, 18.5%, 23.9%, 21.2% over the four years to March 2026; EBITDA margin has stayed between 35.7% and 37.3%, short of the 40% aim [FILING] — [T-IRF], [T-FYR].
- April–June 2026: Taiwan sales dropped on "a quality-related issue involving a certain customer", since "resolved through process modifications" [COMPANY CLAIM] — [T-Q1QA]; Taiwan recovered from 12% to 14% of revenue in the next quarter — [T-H1B].
- November 2025: management expected China's share to "go down on a gradual basis" [COMPANY CLAIM] — [T-1HQA25]; it rose to 29–30% [T-H1B]. Korea, flagged as the growth driver, fell to 9% of revenue in Jul–Sep 2026 after "temporary delays in qualification activities and tape-outs" [COMPANY CLAIM] — [T-Q1QA], [T-H1B].
- Confirmed by outsiders: SEMI share ranking (as cited); JCR long-term issuer rating A, stable, 30 Oct 2026 [CONFIRMED by JCR per company notice] — [T-JCR]. Resting on the company alone: EUV readiness, partnership exclusivity, "production capacity exceeds that of our competitors" [T-Q1QA].

#### (d) Path forward
- Schedule: Singapore plant production first half 2027; Round Rock advanced line second half 2027; third Korean (Icheon) plant second half 2028; EUV mass production 2027 [COMPANY CLAIM] — [T-H1B]. Investments "intended to meet demand in 2027–2028" [COMPANY CLAIM] — [T-FYQA].
- Funding: "Capital expenditures expected to exceed EBITDA … investment spending expected to significantly exceed operating cash flow this fiscal year", met by ¥50,000m of bank borrowing in the half [FILING] — [T-H1B]. Equity-ratio floor "around 60%, or at minimum above 55%" [COMPANY CLAIM] — [T-FYQA]. Payout about 30% [T-H1B].
- Hurdles named by the company: Chinese entrants and localisation ("no plans to use photomask manufacturing equipment from Chinese suppliers") [T-Q1QA]; customers taking work back in-house [T-ASR]; yen strength (over 90% of revenue is overseas) [T-FYQA]; EUV yields given blank cost [T-FYQA]; export controls [T-ASR].

#### (e) Market facts (kept apart)
- Close 13 Nov 2026 ¥3,005; market value ¥298.7bn on 99.39m shares; P/E 12.6x on company guidance, price/book 1.68x, yield 2.33% — [T-KB]. Trailing P/E 12.2x, EV/EBITDA 5.0x, float 46.1m shares [ESTIMATE] — [T-SA]. Net cash ¥41.3bn (my calc on [T-H1B]).
- Consensus (5 analysts; 2 buy, 3 hold): year to March 2027 revenue ¥148.6bn, EPS ¥276.93 (10.9x); year to March 2028 revenue ¥167.6bn, EPS ¥296.29 (10.1x); free cash flow –¥20.9bn this year; mean target ¥4,580, last updated 25 Sep 2026 [ESTIMATE] — [T-SA].
- Since listing: first day (16 Oct 2025) opened ¥3,570, closed ¥3,380; high ¥5,290 intraday on 11 May 2026; low ¥2,419 intraday on 6 Nov 2026. Against the ¥3,000 offer price +0.2%; 2026 year to date –0.8% (from ¥3,030); 12 months –14.0% (from ¥3,495) — [T-KB], [T-IPO].
- Reactions: –8.2% on 14 May 2026 (full-year results and guidance); –14.6% on 7 Aug 2026 (first quarter); after half-year results on 11 Nov 2026, –1.3% on 12 Nov and +1.0% on 13 Nov — [T-KB], [T-SA].
- Positioning: margin balances 6 Nov 2026 1,209,700 shares long against 6,300 short (192x) — [T-KB]; reported short positions JPMorgan 0.98% (6 Nov), Barclays 0.83% (10 Nov), Morgan Stanley MUFG 0.81% (11 Nov), about 2.6% of shares in total — [T-KU].

#### (f) Case against
- Business: free cash flow is negative through the build-out and debt went from ¥1.5bn to ¥50.2bn in six months [T-H1B]; returns depend on demand materialising in 2027–28 at four new lines at once; China 29% with 20-plus local rivals and a non-compliant leased plant [T-1HQA25], [T-ASR]; one customer above 10% [T-ASR]; EUV is prototypes for Japanese customers [T-3QQA]; blank costs are rising faster than they can be passed on [T-3QQA]; R&D expense is under 1% of revenue [T-ASR]; guidance implies a second half weaker than the first unless the yen stays weak.
- Governance and holders: Toppan's 46.5% is an overhang with no lock-up; Integral's near-total exit at the IPO was questioned by analysts and the company declined to comment [T-1HQA25]; share data in investor decks was corrected twice [T-CORR].
- Shares: at 10–12 times earnings and the offer price, much of this is arguably in the price; consensus EPS (¥277) sits 16% above company guidance (¥238.5), so a stronger yen cuts estimates; retail margin longs equal about 2.6% of float.
- Dated events: third-quarter results (February 2027, by last year's calendar); Singapore start-up in first half 2027; any Toppan placement.

### Inferences
- (Mine) Quality is middling-to-good: leading share and 17% ROE, but margins move with depreciation and mix, and bargaining power against blank suppliers and captive customers is limited.
- (Mine) The path is plausible but only partly self-funded for the next two years; the stated equity-ratio floor leaves room for more borrowing.
- (Mine) As a short the stock is cheap on earnings and already back at the offer price; the live risks are a Toppan sell-down, a yen rally and a delayed 2027 ramp.

### Gaps
- Rapidus relationship, EUV order status and blank-supply terms could not be confirmed. Reasons for the depressed profit in the year to March 2025 (¥9,945m) were not reviewed.

## Photronics (NASDAQ PLAB)

### Takeaway
Photronics is a net-cash merchant maker of chip and display masks whose revenue has been flat to down for three years (about $868m expected for FY2026) while gross margin slipped from 37.7% to 33.2%; high-end chip masks reached a record 44% of chip-mask revenue. About 30% of net income and three-quarters of cash belong to joint ventures half-owned by DNP, capex is doubling to replace end-of-life tools, and the shares halved after the May 2026 quarter.

### Cited Findings
#### (a) Position
- Products: chip masks 72% and display masks 28% of nine-month FY2026 revenue; "high-end" means 28nm and below for chips and G10.5+/AMOLED/LTPS for displays [FILING] — [P-10Q], [P-10K]. No EUV revenue is disclosed.
- Eleven plants: Taiwan 3, China 2 (Xiamen, Hefei), Korea 1, United States 3 (Allen, Boise, Brookfield), Europe 2 [FILING] — [P-10Q].
- Geography (origin): FY2025 Taiwan $283.8m (33%), China $221.0m (26%), Korea $158.5m (19%), United States $148.9m (18%), Europe $34.2m; nine months FY2026 Taiwan $207.9m (32%), China $176.3m (27%), Korea $124.4m, United States $111.7m [FILING] — [P-10K], [P-10Q].
- Customers: about 636; two above 10% (16% and 13%), top five about 50% of FY2025 revenue [FILING] — [P-10K]. Revenue "from a related party" was $102.9m in nine months of FY2026 (16%) [FILING] — [P-10Q].
- Competitors named: Tekscend, DNP (outside Taiwan and China), Hoya, Taiwan Mask, LG Innotek, SK-Electronics, Compugraphics, Shenzhen Qingyi, Shenzhen Newway, and captive shops [FILING] — [P-10K].
- Joint ventures: Photronics owns 50.01% of the Taiwan and Xiamen chip-mask ventures, DNP 49.99%; DNP has a put and Photronics a call on the China venture at net book value in certain circumstances; each had about $160.4m invested in it at 31 Oct 2025 [FILING] — [P-10K], [P-10Q].
- Holders: BlackRock 16.5%, Vanguard 10.3%, Dimensional 8.2%; directors and officers 3.3% [FILING] — [P-PROXY].

#### (b) Economics
| $m | FY2025 (to 31 Oct 2025; published 10 Dec 2025) | Q3 FY2026 (to 2 Aug 2026; published 26 Aug 2026) | Nine months FY2026 |
|---|---|---|---|
| Revenue | 849.3 (–2.0%) | 216.0 (+2.7%) | 651.1 (+2.8%) |
| Chip masks / display masks | 615.1 / 234.2 | 154.7 / 61.4 | 467.5 / 183.6 |
| High-end share of chip masks | 39% | 44% (record) | 42% |
| Gross margin | 35.3% | 33.2% | 33.2% |
| Operating margin | 24.5% | 21.1% | 21.9% |
| Net income, total | 190.2 | 43.9 | 147.3 |
| of which minority partners | 53.8 (28%) | 15.0 (34%) | 44.0 (30%) |
| Net income to shareholders / diluted EPS | 136.4 / $2.28 | 28.9 / $0.49 | 103.3 / $1.76 |
| Non-GAAP EPS | $2.01 | $0.50 | — |
| Operating cash flow | 247.8 | 76.3 | 220.6 |
| Capital expenditure | 188.1 | 37.0 | 130.4 |
| R&D | 15.8 | — | — |
| Share repurchases | 97.4 | 0 | 0 |
| Cash + short-term investments (in ventures) | 588.2 (422.3) | 672.8 (503.5) | |
| Debt | negligible | 3.9 | |

All [FILING] — [P-Q4], [P-10K], [P-Q3], [P-10Q]. Free cash flow $59.7m in FY2025 and $90.2m in nine months (my calc). ROE on shareholders' equity 11.9% for FY2025 (my calc). GAAP earnings were lifted by a $16.8m tax-allowance reversal and an $18.6m FX gain in Q4 FY2025 and $25.5m of FX gains in nine months of FY2026 [FILING] — [P-Q4], [P-10Q]. Cash attributable to shareholders is about $421m, or $7 a share, after giving DNP its half of venture cash (my calc).
- Guidance for the quarter to about 1 Nov 2026: revenue $207–227m, operating margin 19–24%, non-GAAP EPS $0.40–0.56 [COMPANY CLAIM] — [P-Q3]. Results not yet published; a data vendor estimates 9 Dec 2026 [ESTIMATE] — [P-SA].
- Capex: FY2026 payments now $255–305m, cut from about $330m, to "replace end-of-life mask-making equipment with higher-performing systems" [FILING] — [P-10Q], [P-10K]. Buyback authority remaining $27.6m [FILING] — [P-10Q].

#### (c) Execution record
- Revenue: $892.1m (FY2023), $866.9m (FY2024), $849.3m (FY2025) [FILING] — [P-10K]. Mainstream chip masks down 4.8% in nine months of FY2026 while high-end rose 13.5% [FILING] — [P-10Q].
- Q2 FY2026 (reported 28 May 2026): revenue $209.9m, gross margin 31.3%, and a third-quarter guide of $207–215m at 18–20% margin, blamed on design releases "delayed due to elevated fab utilization rates", memory supply constraints and geopolitics [COMPANY CLAIM] — [P-Q2]. The third quarter then came in above that guide ($216.0m, 21.1%) [FILING] — [P-Q3].
- A securities class action (Cooper v. Photronics, D. Conn., filed 6 Jul 2026) alleges misleading statements; the company disputes it [FILING] — [P-10Q].
- Management: George Macricostas (son of the founder) became Chairman and CEO on 28 May 2025, replacing Frank Lee, who now runs the Taiwan venture; the chief technology officer left on 29 Dec 2025 with severance; CFO Eric Rivera was also made President on 12 Jan 2026 [FILING] — [P-PROXY], [P-8K1], [P-8K3].
- Investment claims: US and Korea projects "remain on track" (Aug 2026); the Korean extension is to "diversify our geographic revenue mix" [COMPANY CLAIM] — [P-Q3], [P-Q4]. A call summary reports the CFO saying the peak of end-of-life upgrade spending could fall in 2027 rather than 2026 [PRESS] — [P-MB]. No outside confirmation of customer commitments was found.

#### (d) Path forward
- Hurdles: Chinese mask makers in a market that is 27% of revenue; mainstream-node decline; tool lead times; tariffs and export controls; dependence on DNP's continued partnership (put/call provisions) [FILING] — [P-10K], [P-10Q].
- Done so far: capex raised from $188m to $255–305m, no debt, buybacks paused in FY2026 [FILING] — [P-10Q].
- Funding: operating cash flow ($220.6m in nine months) covers capex at the current rate; most cash sits in the ventures, and $446.1m was held by foreign subsidiaries at 31 Oct 2025 [FILING] — [P-10K].

#### (e) Market facts (kept apart)
- Close 13 Nov 2026 $27.55; market value $1.63bn on 59.0m shares; trailing GAAP P/E 9.7x; price to shareholders' book about 1.27x (my calc) [ESTIMATE] — [P-SA].
- Consensus (3 analysts, all buy): FY2026 revenue $868.0m, non-GAAP EPS $2.01 (13.7x); FY2027 revenue $892.4m, EPS $2.08 (13.2x); targets $39–44, last changed 27 Aug 2026 (one cut from $55 to $44) [ESTIMATE] — [P-SA].
- 2026 year to date –13.9% (from $32.00); 12 months +28.0% (from $21.52 on 13 Nov 2025); 52-week high close $54.96 (11 May 2026), now 50% lower — [P-SA].
- Reactions: +45.4% on 10 Dec 2025 (Q4 FY2025); –36.4% on 28 May 2026 (Q2 FY2026); +3.2% on 26 Aug 2026 after opening 26% higher, then –8.4% on 28 Aug — [P-SA].
- Short interest 4.05m shares, 6.9% of shares outstanding, about 5 days to cover [ESTIMATE] — [P-SA].

#### (f) Case against
- Business: no growth for three years and falling gross margin while capex doubles, which reads as catch-up replacement rather than expansion; minorities take about 30% of profit; reported cash overstates what shareholders can reach; China exposure; two customers are 29% of revenue; family-led board (father and son) and senior turnover [P-PROXY]; pending class action [P-10Q].
- Shares: at 13–14 times non-GAAP earnings with flat estimates the price already reflects stagnation; short interest is moderate; the next results (about 9 Dec 2026) will carry FY2027 capex and margin signals, and past results days moved the stock 36–45%.

### Inferences
- (Mine) The business is sound but ordinary: adequate margins, net cash, little pricing power, growth confined to high-end mix.
- (Mine) Shareholder economics are weaker than headline figures because of the DNP half-share.
- (Mine) A short here is a bet on a margin miss during the capex peak; the balance sheet and already-halved price limit the payoff.

### Gaps
- Identity of the two large customers and the related party, site-level detail of US and Korean projects, and the call transcript itself were not read.

## Dai Nippon Printing and AGC (shorter: mask and mask-blank businesses only)

### Takeaway
For both groups the leading-edge mask business is a small part of a diversified company: DNP's front-end semiconductor (photomask) sales were ¥67bn, 4.4% of group sales, with EUV and nanoimprint volume still ahead in 2027; AGC's EUV blanks peaked at ¥40bn in 2024, about 2% of group sales, fell in 2025 and are recovering.

### Cited Findings
- DNP size: Semiconductors (front-end) sales ¥66bn (FY2022), ¥67bn (FY2025, year to March 2026), plan ¥110bn (FY2028) [COMPANY CLAIM] — [D-IRD]; Apr–Sep 2026 ¥39.9bn (+25.8%), 5.2% of group sales of ¥762.8bn [FILING/briefing] — [D-H1]. Electronics segment Apr–Sep 2026: sales ¥143.7bn, operating profit ¥31.9bn against group ¥55.2bn; group full-year forecast raised to sales ¥1,564bn and operating profit ¥113bn on 13 Nov 2026 [FILING] — [D-H1]. Group FY2025: sales ¥1,512.5bn, operating profit ¥101.0bn, ROE 8.9% [FILING] — [D-FY].
- DNP plan: photomask sales index 100 (FY2024), 104, 134, 162, 203, 227, 234 (FY2030), a 15.2% annual rate, raised from "mid-11%" a year earlier; photomask capex for FY2026–28 raised from ¥30bn to ¥70bn, "EUV accounts for a substantial proportion"; nanoimprint mass-production capex "not yet included" [COMPANY CLAIM] — [D-IRD], [D-IRDQ]. Cutting-edge sales to add ¥24bn in FY2028 over FY2024 [COMPANY CLAIM] — [D-IRDS].
- DNP and Rapidus: subcontract work under Rapidus's NEDO project "completed in March 2026 as planned"; "Investment in Rapidus in 2026"; commercialisation to start "with Rapidus's 2nm mass production"; 2nm-generation EUV mask pattern resolution achieved; High-NA "currently providing masks for evaluation" [COMPANY CLAIM] — [D-IRD]. EUV mask "full-scale mass production in 2027" (IR Day, 13 Jul 2026) against "around FY2028" (results Q&A, 13 May 2026) [COMPANY CLAIM] — [D-IRD], [D-FYQ].
- DNP nanoimprint: "sole supplier of masks for nanoimprint lithography"; template with 10nm line width "equivalent to the 1.4nm generation" under evaluation by several customers; partners named include Kioxia, Canon, imec, Rapidus; mass production targeted 2027 [COMPANY CLAIM] — [D-IRD], [D-IRDS].
- DNP is also Photronics' 49.99% partner in Taiwan and Xiamen [FILING] — [P-10K].
- DNP market facts: ¥2,743 on 13 Nov 2026; market value ¥1.18tn; P/E 14.6x; price/book 0.96x; 2026 year to date +1.8% — [D-SA].
- AGC size: EUV-blank sales "reached JPY40 billion in 2024", with 2025 "the bottom" after "demand from one particular customer declined"; 2026 to exceed 2024 on a comparable-period basis [COMPANY CLAIM] — [A-SEMIT]. Electronic Materials sales ¥183.6bn (2024), ¥168.5bn (2025, with "decrease in shipments of EUV mask blanks"), ¥134.5bn in Jan–Sep 2026 (+¥12.3bn, EUV-blank shipments up) [FILING] — [A-FY], [A-Q3]. Electronics segment 2025: sales ¥355.1bn, operating profit ¥47.5bn; group sales ¥2,058.8bn, operating profit ¥127.5bn [FILING] — [A-FY], [A-REV].
- AGC position and aims: "the sole blanks manufacturer in the world that covers the whole production process from glass materials to polishing and deposition"; High-NA blanks "under development"; plants at Motomiya and Koriyama; blanks are the largest product in its electronics semiconductor business; semiconductor-related sales to double by 2030 from 2025 [COMPANY CLAIM] — [A-SEMI], [A-SEMIT].
- AGC group context: 5 Nov 2026 cut of 2026 operating-profit forecast from ¥150bn to ¥120bn and net profit from ¥77bn to ¥40bn (automotive, chemicals, life science), Electronics forecast nudged up to ¥46bn; new CEO from 1 Jan 2027; shares –8.5% that day; ¥5,023 on 13 Nov 2026, market value ¥1.07tn, net debt ¥581bn [FILING; price data] — [A-REV], [A-Q3], [A-CEO], [A-SA].

### Inferences
- (Mine) Neither stock is a clean way to own or short leading-edge masks: the relevant business is 2–5% of sales. AGC's 2025 dip from a single customer shows how concentrated second-source blank demand is.

### Gaps
- AGC's current EUV-blank sales figure and capacity, the size of DNP's Rapidus investment and DNP's EUV customers other than Rapidus are not disclosed.

## What each has to get through in 2027–2030, what it has done, and how it is paid for

### Takeaway
Hoya and Photronics fund their plans from operating cash; Tekscend has started borrowing; DNP and AGC fund small programmes from group balance sheets. All five are adding capacity for the same 2027–2028 demand window.

### Cited Findings
| Company | Must get through | Done so far | Paid for by |
|---|---|---|---|
| Hoya | A14/A10 film change; High-NA 12-inch blanks; second-source evaluations and a Korean entrant; depreciation peak FY28–29; HDD customer ramps [H-Q1T], [H-3QT], [H-FYT] | N2 phase-shift volume; Singapore building and Vietnam plant decided; Laos lines being filled [H-FYT], [H-Q1T] | Own cash: free cash flow ¥270.9bn against ¥120–130bn of decisions; net cash ¥520bn [H-FYR], [H-Q2R] |
| Tekscend | Four start-ups in 2027–28; EUV mass production from 2027; China competition; Toppan overhang; yen [T-H1B], [T-1HQA25] | Singapore plant under construction; IBM and imec programmes; ¥22.7bn capex in six months [T-H1B], [T-ASR] | Operating cash plus ¥50bn bank debt; equity ratio 63.1%, floor about 60% [T-H1B], [T-FYQA] |
| Photronics | End-of-life tool replacement peaking 2026–27; China rivals; US and Korea high-end ramps; class action [P-10Q], [P-MB] | Capex raised to $255–305m; high-end 44% of chip masks [P-10Q], [P-Q3] | Operating cash; no debt; venture cash shared with DNP [P-10Q] |
| DNP | First EUV and nanoimprint volume in 2027; Rapidus's own ramp [D-IRD] | NEDO subcontract finished; capex plan ¥70bn [D-IRD] | Group cash flow (group capex plan ¥77bn for FY2026) [D-H1] |
| AGC | Regain volume at 2nm and High-NA against Hoya; weak group earnings [A-SEMIT], [A-REV] | In mass production for 2nm logic and phase-shift; capacity additions listed [A-SEMIT], [A-Q3] | Group balance sheet, net debt ¥581bn [A-SA] |

### Inferences
- (Mine) Simultaneous capacity additions by Tekscend, DNP and Photronics for 2027–28 raise the chance of merchant overcapacity if captive outsourcing slows; Hoya is the only one adding capacity against stated customer volume commitments [H-Q2T].

### Gaps
- No customer has publicly confirmed volume commitments to any of these plans.

## Could not verify; figures on which sources conflict

### Takeaway
The main unverified items are market shares in EUV blanks, EUV mask counts and prices, and anything that needed press searches; the main conflicts are market-size estimates and a few company dates and amounts.

### Cited Findings
Could not verify
- Hoya's numeric EUV-blank share, its A10 exclusivity and High-NA status (company word only) [H-Q2T]; AGC's "leading two" claim beyond its own word [A-SEMI]; S&S Tech's status.
- SEMI figures at source (seen only through Tekscend and DNP material) [T-IRF], [D-IRD].
- EUV masks per chip generation, EUV mask and blank prices, pellicle capacity (Mitsui Chemicals and others), IMS and NuFlare capacity, IMS's minority holders by name.
- Tekscend–Rapidus and Tekscend–IBM beyond the development agreement; any production EUV order at Tekscend or DNP.
- Photronics' fourth-quarter FY2026 results (not yet published), its two large customers, and details of US and Korean expansions.
- Controls adopted by Hoya after the 2024 IT incident; reason for Hoya's 2 Nov 2026 share fall; cause of the 5–6 Nov 2026 sector-wide fall.
- Nikkei, Reuters and Bloomberg reporting on any of the above (search allowance exhausted).

Conflicts
- Merchant market size for 2025: $2.70bn (DNP on SEMI data) [D-IRD] against about $2.0bn (Tekscend, Nov 2026) [T-H1B] and $2.1bn for 2024 (Tekscend, Sep 2026) [T-IRF]; DNP's total-market estimate of $5.28bn with a one-third merchant share would imply about $1.8bn (my calc) [M-HAY].
- Tekscend's 2024 share: 38.9% as first published, 37.8% after correction [T-CORR].
- Hoya's new EUV-blank building: "exceed ¥40 billion" [H-FYT] against "50 billion yen" [H-FYF].
- Hoya operating profit for Jul–Sep 2026: ¥89.4bn (management measure) against ¥90.8bn (IFRS) [H-Q2R]; market value ¥8.01tn [H-KB] against ¥7.93tn [H-SA].
- DNP EUV volume timing: 2027 [D-IRD] against "around FY2028" [D-FYQ]; DNP photomask growth: index implies near-doubling FY2025–28 [D-IRD] while the segment plan shows ¥67bn to ¥110bn [D-IRD].
- Photronics 12-month price change: +28.0% from the 13 Nov 2025 close (my calc) against +22.7% shown by the data vendor [P-SA].
- Tekscend P/E: 12.6x on company guidance [T-KB] against 10.9x on consensus [T-SA].

### Inferences
- (Mine) Where a company claim and a rival's claim collide (Hoya and AGC at 2nm), treat both as unconfirmed until a chipmaker or SEMI data settles it.

### Gaps
- A follow-up with press and SEMI access would close most items in the first list.

[H-Q2R]: https://ssl4.eir-parts.net/doc/7741/tdnet/2901246/00.pdf "Hoya Quarterly Report, Jul-Sep 2026 and H1, 30 Oct 2026"
[H-Q2P]: https://ssl4.eir-parts.net/doc/7741/tdnet/2901244/00.pdf "Hoya FY26 Q2 results presentation, 30 Oct 2026"
[H-Q2T]: https://www.hoya.com/wp-content/uploads/2026/11/FY26-Q2-Transcript_E-1.pdf "Hoya FY26 Q2 earnings call transcript, call 30 Oct 2026"
[H-Q2J]: https://ssl4.eir-parts.net/doc/7741/tdnet/2901247/00.pdf "Hoya kessan tanshin (Japanese), Q2 FY to Mar 2027, 30 Oct 2026"
[H-FYR]: https://ssl4.eir-parts.net/doc/7741/tdnet/2797234/00.pdf "Hoya Quarterly Report, Jan-Mar 2026 and FY25, 30 Apr 2026"
[H-FYT]: https://www.hoya.com/wp-content/uploads/2026/05/FY25-Q4-Transcript_E.pdf "Hoya FY25 Q4 earnings call transcript, 30 Apr 2026"
[H-FYF]: https://www.hoya.com/wp-content/uploads/2026/07/FY25-Q4-FAQ-en.pdf "Hoya FAQ on Q4 FY25 results, 1 Jul 2026"
[H-Q1T]: https://www.hoya.com/wp-content/uploads/2026/08/FY26_Q1_Transcript_E.pdf "Hoya FY26 Q1 earnings call transcript, 31 Jul 2026"
[H-Q1F]: https://www.hoya.com/wp-content/uploads/2026/09/FY26-Q1-FAQ_English.pdf "Hoya FAQ on Q1 FY26 results, 25 Sep 2026"
[H-3QT]: https://www.hoya.com/wp-content/uploads/2026/02/7921484a82cf3225cf5fd43a0b4a4a91.pdf "Hoya FY25 Q3 earnings call transcript, early 2026"
[H-3QF]: https://www.hoya.com/wp-content/uploads/2026/04/FY25-Q3-FAQ-en-1.pdf "Hoya FAQ on Q3 FY25 results, Apr 2026"
[H-2QT25]: https://www.hoya.com/wp-content/uploads/2025/11/FY25-Q2-Earnings-Call-Transcript_E.pdf "Hoya FY25 Q2 earnings call transcript, Nov 2025"
[H-24Q1T]: https://www.hoya.com/wp-content/uploads/2024/08/FY24-Q1-Earnings-Call-Transcript.pdf "Hoya FY24 Q1 earnings call transcript, Aug 2024"
[H-24Q4T]: https://www.hoya.com/wp-content/uploads/2025/05/c599456816588c342cdb67b08d1f1608.pdf "Hoya FY24 Q4 earnings call transcript, May 2025"
[H-BB1]: https://ssl4.eir-parts.net/doc/7741/tdnet/2797230/00.pdf "Hoya buyback completion and cancellation, 30 Apr 2026"
[H-BB2]: https://ssl4.eir-parts.net/doc/7741/tdnet/2859047/00.pdf "Hoya buyback decision, 31 Jul 2026"
[H-BB3]: https://ssl4.eir-parts.net/doc/7741/tdnet/2903111/00.pdf "Hoya buyback status, 2 Nov 2026"
[H-LAW]: https://ssl4.eir-parts.net/doc/7741/tdnet/2766532/00.pdf "Hoya notice of shareholder derivative lawsuit, 24 Feb 2026"
[H-LAW2]: https://ssl4.eir-parts.net/doc/7741/tdnet/2770220/00.pdf "Hoya notice of intervention in derivative lawsuit, 2 Mar 2026"
[H-ENDO]: https://ssl4.eir-parts.net/doc/7741/tdnet/2859053/00.pdf "Hoya strategic review of endoscope business, 31 Jul 2026"
[H-KB]: https://kabutan.jp/stock/kabuka?code=7741 "Kabutan price history and quote page for 7741, read 14 Nov 2026"
[H-SA]: https://stockanalysis.com/quote/tyo/7741/statistics/ "StockAnalysis statistics, forecast and history pages for TYO:7741 (S&P Global data), read 14 Nov 2026"
[H-KU]: https://karauri.net/7741/ "karauri.net compilation of reported short positions, 7741, read 14 Nov 2026"
[T-H1B]: https://contents.xj-storage.jp/xcontents/AS83405/6d05be1b/6fe1/4d9b/a123/eb86e87f98ca/140120261111572776.pdf "Tekscend Financial Results Briefing FY2026 Q2, 11 Nov 2026"
[T-H1R]: https://contents.xj-storage.jp/xcontents/AS83405/9f9fcf15/51cb/452b/8b4d/c84f10f1e0cb/20261111103458270s.pdf "Tekscend Semi-annual Securities Report to 30 Sep 2026, 11 Nov 2026"
[T-Q1B]: https://www2.jpx.co.jp/disc/429A0/140120260806511176.pdf "Tekscend first-quarter briefing (Japanese), 6 Aug 2026"
[T-Q1QA]: https://contents.xj-storage.jp/xcontents/AS83405/38e97259/d1d7/44a6/8c08/e7428a575be1/20260821194553631s.pdf "Tekscend FY2026 Q1 briefing Q&A, briefing 6 Aug 2026"
[T-FYR]: https://contents.xj-storage.jp/xcontents/AS83405/df046ba6/2f36/4734/a12e/4371a92d1ebe/140120260513528465.pdf "Tekscend Consolidated Financial Results, year to 31 Mar 2026, 13 May 2026"
[T-FYQA]: https://contents.xj-storage.jp/xcontents/AS83405/87de1f1c/4782/4d75/989b/1748d6d82266/20260604162330324s.pdf "Tekscend FY2025 full-year briefing Q&A, briefing 13 May 2026"
[T-ASR]: https://contents.xj-storage.jp/xcontents/AS83405/b224fd02/d92c/4d33/b6bd/97cb81e517ee/20260624114028023s.pdf "Tekscend Annual Securities Report, 5th fiscal year, 24 Jun 2026"
[T-REV]: https://contents.xj-storage.jp/xcontents/AS83405/50faa94b/175d/4e36/b01e/1fa91db4e1b8/140120260326589741.pdf "Tekscend forecast and dividend revision, 27 Mar 2026"
[T-CORR]: https://contents.xj-storage.jp/xcontents/AS83405/cbc0d993/48fd/4911/a228/16969dcaf526/20260619125457146s.pdf "Tekscend correction of market-share figures, 19 Jun 2026"
[T-IPO]: https://contents.xj-storage.jp/xcontents/AS83405/708c6ca8/ad78/43f4/8952/cbece0ee9717/S100WU2B.pdf "Tekscend amended securities registration statement (Japanese), 8 Oct 2025"
[T-PAR]: https://contents.xj-storage.jp/xcontents/AS83405/4a64bed8/2998/42a5/b1b2/5a24cd602c82/140120251015574401.pdf "Tekscend change in parent and major shareholder, 16 Oct 2025"
[T-CTRL]: https://contents.xj-storage.jp/xcontents/AS83405/540d437b/77fb/4fe0/ba78/f56bf82b3971/140120260630584704.pdf "Tekscend matters concerning controlling shareholder, 30 Jun 2026"
[T-JCR]: https://contents.xj-storage.jp/xcontents/AS83405/4766100a/b134/4fba/b604/524ca854ea93/140120261030560353.pdf "Tekscend notice of credit rating, 30 Oct 2026"
[T-IRF]: https://contents.xj-storage.jp/xcontents/AS83405/1457d6c0/c2f2/450d/ba8c/58532106c188/20260910160311945s.pdf "Tekscend company presentation, Nikkei-TSE IR Fair (Japanese), 10 Sep 2026"
[T-1HQA25]: https://contents.xj-storage.jp/xcontents/AS83405/18781ebb/abd2/4806/8ecc/2aba9f43d78f/20251121180033992s.pdf "Tekscend FY2025 first-half briefing Q&A, Nov 2025"
[T-3QQA]: https://contents.xj-storage.jp/xcontents/AS83405/d2a4790d/4761/4b8e/968c/38be9bd786df/20260224194704552s.pdf "Tekscend FY2025 Q3 briefing Q&A, Feb 2026"
[T-KB]: https://kabutan.jp/stock/kabuka?code=429A "Kabutan price history and quote page for 429A, read 14 Nov 2026"
[T-SA]: https://stockanalysis.com/quote/tyo/429A/statistics/ "StockAnalysis statistics, forecast and history pages for TYO:429A (S&P Global data), read 14 Nov 2026"
[T-KU]: https://karauri.net/429A/ "karauri.net compilation of reported short positions, 429A, read 14 Nov 2026"
[P-Q3]: https://www.sec.gov/Archives/edgar/data/0000810136/000081013626000006/plabQ32026EarningsEx99-1PR.htm "Photronics Q3 FY2026 press release, 26 Aug 2026"
[P-10Q]: https://www.sec.gov/Archives/edgar/data/810136/000114036126036138/plab-20260802.htm "Photronics Form 10-Q, quarter ended 2 Aug 2026, filed 10 Sep 2026"
[P-10K]: https://www.sec.gov/Archives/edgar/data/810136/000114036125045801/ef20057458_10k.htm "Photronics Form 10-K, FY2025, filed 17 Dec 2025"
[P-Q4]: https://www.sec.gov/Archives/edgar/data/810136/000114036125045083/ef20060918_ex99-1.htm "Photronics Q4 and FY2025 press release, 10 Dec 2025"
[P-Q2]: https://www.sec.gov/Archives/edgar/data/810136/000114036126023057/ef20074970_ex99-1.htm "Photronics Q2 FY2026 press release, 28 May 2026"
[P-8K1]: https://www.sec.gov/Archives/edgar/data/810136/000114036126000196/ef20062241_8k.htm "Photronics Form 8-K, CTO departure, 2 Jan 2026"
[P-8K3]: https://www.sec.gov/Archives/edgar/data/810136/000114036126001053/ef20062773_8k.htm "Photronics Form 8-K, officer appointments, 13 Jan 2026"
[P-PROXY]: https://www.sec.gov/Archives/edgar/data/810136/000153949726000750/n5545_x1-def14a.htm "Photronics proxy statement, 23 Feb 2026"
[P-MB]: https://www.marketbeat.com/instant-alerts/transcript-photronics-q3-earnings-call-highlights-2026-08-26/ "MarketBeat summary of Photronics Q3 FY2026 call, 26 Aug 2026"
[P-SA]: https://stockanalysis.com/stocks/plab/statistics/ "StockAnalysis statistics, forecast and history pages for PLAB (S&P Global data), read 14 Nov 2026"
[D-H1]: https://www.global.dnp/content/dam/dnp-global/pdf/en/ir/library/presentation/dnp_e_26Q2pre.pdf "DNP results presentation, Apr-Sep 2026, 13 Nov 2026"
[D-IRD]: https://www.global.dnp/content/dam/dnp-global/pdf/en/ir/library/presentation/dnp_e_26irday_pre.pdf "DNP IR Day presentation, 13 Jul 2026"
[D-IRDQ]: https://www.global.dnp/content/dam/dnp-global/pdf/en/ir/library/presentation/dnp_e_26irday_qa.pdf "DNP IR Day Q&A summary, 13 Jul 2026"
[D-IRDS]: https://www.global.dnp/content/dam/dnp-global/pdf/en/ir/library/presentation/dnp_e_26irday_pre_scr.pdf "DNP IR Day script, 13 Jul 2026"
[D-FY]: https://www.global.dnp/content/dam/dnp-global/pdf/en/ir/library/presentation/dnp_e_25Q4pre.pdf "DNP FY2025 results presentation, 13 May 2026"
[D-FYQ]: https://www.global.dnp/content/dam/dnp-global/pdf/en/ir/library/presentation/dnp_e_25Q4pre_qa.pdf "DNP FY2025 results Q&A, 13 May 2026"
[D-SA]: https://stockanalysis.com/quote/tyo/7912/statistics/ "StockAnalysis statistics and history for TYO:7912, read 14 Nov 2026"
[A-SEMI]: https://www.agc.com/en/ir/library/bizbriefing/pdf/2026_0602esemiconductor.pdf "AGC semiconductor business briefing, 2 Jun 2026"
[A-SEMIT]: https://www.agc.com/en/ir/library/bizbriefing/pdf/2026_0602esemiconductor_transcript.pdf "AGC semiconductor business briefing transcript, 2 Jun 2026"
[A-Q3]: https://ssl4.eir-parts.net/doc/5201/tdnet/2904806/00.pdf "AGC results presentation, Jan-Sep 2026, 5 Nov 2026"
[A-REV]: https://ssl4.eir-parts.net/doc/5201/tdnet/2904829/00.pdf "AGC revision of FY2026 forecast, 5 Nov 2026"
[A-FY]: https://ssl4.eir-parts.net/doc/5201/tdnet/2751534/00.pdf "AGC FY2025 results presentation, 6 Feb 2026"
[A-CEO]: https://ssl4.eir-parts.net/doc/5201/tdnet/2904841/00.pdf "AGC change in representative directors, 5 Nov 2026"
[A-SA]: https://stockanalysis.com/quote/tyo/5201/statistics/ "StockAnalysis statistics and history for TYO:5201, read 14 Nov 2026"
[M-EBPR]: https://www.ebeam.org/docs/ebeam-initiative-bacus-2026-roundup-release-final.pdf "eBeam Initiative press release on 15th Luminaries survey, 9 Sep 2026"
[M-EBLUM]: https://www.ebeam.org/docs/2026-ebeam-luminaries-survey-final-web.pdf "eBeam Initiative 2026 Luminaries survey results, Sep 2026"
[M-HAY]: https://www.ebeam.org/docs/ebeam-initiative-reception-keynote-n-hayashi-final-web.pdf "N. Hayashi (DNP), Photomask Ecosystem: Current Status and Issues, 9 Sep 2026"
[M-INTC]: https://www.sec.gov/Archives/edgar/data/50863/000005086326000191/intc-20260926.htm "Intel Form 10-Q, quarter ended 26 Sep 2026, filed 30 Oct 2026"
