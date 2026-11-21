# Q5 – Nordson (NDSN) financial fact base: Test & Inspection (ATS segment) and group

Compiled 2026-11-21. Raw dated facts only. No opinions, prices or multiples. "NORDSON" = company document or management on a call. Transcript host is named for every call quote. Arithmetic done by the compiler is labelled **(computed)**. No Test & Inspection revenue figure has been derived from segment data.

## 0. Access notes and status items (read first)

- **SEC access.** www.sec.gov/Archives refused scripted curl (HTTP 403). It was read through WebFetch, which returns summaries and caps verbatim quotes at about 125 characters. Long 10-Q/10-K pages were truncated at about 75k characters, so the MD&A of the Q2 and Q3 FY2026 10-Qs could not be read on sec.gov. data.sec.gov JSON (submissions, companyfacts) worked with curl.
- **Full-text copies used.**
  - Nasdaq.com copies of the BusinessWire releases (the same text as 8-K Ex. 99.1): Q1–Q3 FY2024, Q1–Q2 FY2025, Q4 FY2025, Q1–Q3 FY2026.
  - The Nordson IR CDN (s202.q4cdn.com) for the FY2025 10-K PDF and investor decks.
  - pubt.io for the Q2 FY2026 10-Q MD&A.
  - last10k.com for an excerpt of the Q3 FY2026 10-Q MD&A.
  - TickerTrends (tickertrends.io) as the record of every call. The six target calls were cross-checked against Equibles (equibles.com) for the key quotes.
- **Tools that failed.** Firecrawl and Exa were out of credits (one try each). investors.nordson.com, businesswire.com, stocktitan.net and investing.com returned 403 to curl.
- **Q4 FY2026 results are NOT yet published as of 2026-11-21.** NORDSON IR release dated **6 Nov 2026**: Nordson will "release fourth quarter and fiscal year 2026 earnings on December 15, 2026, after the close of the market". The webcast is "Wednesday, December 16, 2026" at "8:30 AM ET". URL: https://investors.nordson.com/news/news-details/2026/Nordson-Corporation-Announces-Earnings-Release-and-Webcast-for-Fourth-Quarter-and-Fiscal-Year-2026/default.aspx . The EDGAR submissions list on 2026-11-21 has no 8-K after 2026-10-23, only Forms 4 and 4/A up to 2026-11-04.
- **8-K of 2026-10-23 (Items 7.01, 8.01, 9.01; accession 0000072331-26-000063): completion of the Contrinex acquisition.**
  - Item 8.01: on 23 Oct 2026 Nordson London Limited, a wholly owned subsidiary, bought all equity interests of Contrinex Holding SA (Switzerland) under a Share Purchase Agreement dated the same day. The enterprise value was about **USD 168 million** (WebFetch summary of the 8-K text).
  - Ex. 99.1 (press release, 23 Oct 2026, 8:30 AM), verbatim: "Contrinex, headquartered in Corminboeuf, Switzerland, generates approximately $50 million in annual revenue." It continues: "Contrinex will be integrated into Nordson's Advanced Technology Solutions segment." The acquisition "complements Nordson's test and inspection portfolio".
  - Srini Subramanian, EVP Nordson ATS: "We are excited to welcome Contrinex's nearly 500 employees into the Nordson family. Their differentiated sensor technology complements our test and inspection portfolio, particularly our growth focus on factory automation and control solutions".
  - Price is not in the release. Financing and accretion are NOT DISCLOSED (checked: 8-K, Ex. 99.1).
  - URLs: https://www.sec.gov/Archives/edgar/data/72331/000007233126000063/ndsn-20261023.htm ; https://www.sec.gov/Archives/edgar/data/72331/000007233126000063/nordsonskylightpressreleas.htm ; full-text copy https://finviz.com/news/407247/nordson-corporation-completes-acquisition-of-contrinex-expanding-its-industrial-sensing-and-automation-portfolio

## 0b. Segment structure changes (dates)

| Effective / disclosed | Change | Source |
|---|---|---|
| Q4 FY2022 (8-K 2.02 dated 8 Sep 2022) | Nordson went from two segments to three: Industrial Precision Solutions (IPS), Medical and Fluid Solutions (MFS) and Advanced Technology Solutions (ATS). The 8-K Ex. 99.1 gives recast quarterly segment sales and operating profit for FY2021 and Q1–Q3 FY2022. On the old basis, the Q3 FY2022 call reported ATS at "$321 million", including EFD and biopharma fluid components. | https://www.sec.gov/Archives/edgar/data/72331/000007233122000091/ndsn-sep20228kxex991.htm ; Q3 FY2022 call (TickerTrends) https://tickertrends.io/transcripts/NDSN/Q3-earnings-transcript-2022 |
| 3 Nov 2022 | CyberOptics acquired and "reported in our Advanced Technology Solutions segment" (FY2025 10-K, Note 3). | FY2025 10-K |
| 1 Nov 2024 (Q1 FY2025) | FY2025 10-K, Note 15: "Effective November 1, 2024, the MCS division was transferred from the IPS segment to the ATS segment ... prior year financial information was revised to be comparable." Goodwill of $29,010k was moved from IPS to ATS. | FY2025 10-K PDF https://s202.q4cdn.com/528247721/files/doc_financials/2025/ar/10-K.pdf |
| FY2025 (10-K) | Segment measure changed "from segment operating profit (loss) to segment EBITDA". Reporting units were reassessed, and the "reporting units should be the same as its operating segments: ATS, IPS and MFS". Before this, "Advanced Technology Solutions Segment - Test & Inspection" was a separate goodwill reporting unit (see 1). | FY2025 10-K |
| 2 Sep 2025 | Medical contract manufacturing product lines sold (MFS) | FY2025 10-K Note 4 |
| 16 Mar 2026 | CapstanAG Systems acquired (precision agriculture, IPS) | Q2 FY2026 release |
| 23 Oct 2026 | Contrinex acquired, to be integrated into ATS | 8-K 2026-10-23 |

Note on "adjusted EBITDA": Nordson labels the measure "EBITDA (non-GAAP)". It is defined as "operating profit plus certain adjustments, such as non-recurring cost reduction actions, fees and non-cash inventory charges associated with acquisitions, plus depreciation and amortization". The tables below use this figure wherever "adjusted EBITDA" is asked for.

---

## 1. Q5a – Every Nordson-stated Test & Inspection (T&I) number or statement found (since CyberOptics)

T&I revenue in dollars is **NOT DISCLOSED** for any period. Checked: 10-K FY2023, FY2024 and FY2025; 10-Q Q1–Q3 FY2026 (partial, see 0); every 8-K earnings release from Q4 FY2022 to Q3 FY2026; 16 call transcripts from Q4 FY2022 to Q3 FY2026; investor decks of Aug 2024, May 2025 and Aug 2026.

T&I margin is **NOT DISCLOSED** (same sources checked).

| Date | Document | Exact wording (verbatim) | Number | URL |
|---|---|---|---|---|
| 8 Aug 2022 | Press release, agreement to acquire CyberOptics (8-K Ex. 99.1) | CyberOptics "generates approximately $100 million in annual revenue"; "valued at $54.00 a share"; about $380 million "net of cash acquired". The release names Nordson's "Test & Inspection division within the Advanced Technology Solutions segment". Expected to close in "Nordson's first quarter fiscal 2023". | ~$100M annual revenue (period not specified); $54.00/sh; ~$380M net of cash | https://www.sec.gov/Archives/edgar/data/72331/000007233122000071/ndsn-aug20228kxex991.htm |
| 3 Nov 2022 | 8-K (Item 8.01), closing | Closing Date 3 Nov 2022; each share "was automatically converted into the right to receive $54.00 in cash, without interest" | $54.00/sh | https://www.sec.gov/Archives/edgar/data/72331/000007233122000121/ndsn-20221103.htm |
| FY2023–FY2025 | 10-K (FY2025 PDF), Note 3 | "We acquired CyberOptics for an aggregate purchase price of $377,843, net of cash of approximately $40,890 ... goodwill of $285,330 and identifiable intangible assets of $58,600 ... The financial results of CyberOptics were not material to our Consolidated Financial Statements." | $377.8M net; goodwill $285.3M | https://s202.q4cdn.com/528247721/files/doc_financials/2025/ar/10-K.pdf |
| 15 Dec 2022 | Q4 FY2022 call (TickerTrends), Joe Kelley (CFO) | "Just a reminder, it's about a $100 million business, we're integrating it into our test and inspection division." | ~$100M | https://tickertrends.io/transcripts/NDSN/Q4-earnings-transcript-2022 |
| 15 Dec 2022 | Same call, Joe Kelley | Q4 FY2022 ATS: "This segment had double digit growth in both the test and inspection and electronics dispense product lines, serving predominantly the semiconductor and electronics end markets." | T&I growth "double digit" (Q4 FY2022) | same |
| 15 Dec 2022 | Same call, S. Nagarajan (CEO) | "our electronics applications are split between dispense applications and more secular test and inspection processes." | – | same |
| 14 Dec 2022 | Q4 FY2022 release | "we enter fiscal 2023 with approximately $1 billion in backlog, inclusive of the acquired CyberOptics backlog." | Group backlog ~$1B | https://www.sec.gov/Archives/edgar/data/72331/000007233122000183/ndsn-20221214xex991.htm |
| 20 Feb 2023 | Q1 FY2023 release | ATS variance: organic 4.6%, acquisitions 13.5%, currency (3.7)%, total 14.4%. "The organic sales increase was driven by test and inspection product lines." CEO: "Growth was driven by the benefits of our CyberOptics acquisition" | CyberOptics acquisition contribution to ATS growth +13.5% | https://www.sec.gov/Archives/edgar/data/72331/000007233123000038/ndsn-q120238kxex991.htm |
| 21 Feb 2023 | Q1 FY2023 call (TickerTrends), Kelley / Nagarajan | Kelley: "Organic sales growth in the quarter was 5% plus another 14% from the CyberOptics acquisition." He added the organic growth "was driven by the Test and Inspection acoustic product line". Nagarajan: "We're also seeing weakness in optical Test and Inspection product lines relating to the memory end market." | Acq. +14% (rounded) | https://tickertrends.io/transcripts/NDSN/Q1-earnings-transcript-2023 |
| 22 May 2023 | Q2 FY2023 release | ATS: organic (9.9)%, acquisitions 12.3%, currency (1.7)%, total 0.7%. "Sales benefited from the acquisition impact of 12% partially offset by a decrease in organic sales of 10%". "slightly offset by continued growth in test and inspection product lines." | Acq. +12.3% | https://www.sec.gov/Archives/edgar/data/72331/000007233123000096/ndsn-q220238kxex991.htm |
| 23 May 2023 | Q2 FY2023 call (TickerTrends), Nagarajan | "Growth in our X-Ray test and inspection product lines are successfully muting the historic volatility of this cycle." He also said: "Our CyberOptics acquisition has more exposure to the memory end market, so its product lines have experienced weakness." | – | https://tickertrends.io/transcripts/NDSN/Q2-earnings-transcript-2023 |
| 21 Aug 2023 | Q3 FY2023 release | ATS: organic (12.8)%, acquisitions 10.7%, currency (0.4)%, total (2.5)%. "slightly offset by continued growth in test and inspection product lines." | Acq. +10.7% | https://www.sec.gov/Archives/edgar/data/72331/000007233123000141/ndsn-q320238kxex991.htm |
| 22 Aug 2023 | Q3 FY2023 call (TickerTrends), Nagarajan | "we continue to experience double-digit organic growth in medical interventional solutions and polymer processing product lines, as well as high-single-digit growth in the test and inspection business." | T&I growth "high-single-digit" (Q3 FY2023) | https://tickertrends.io/transcripts/NDSN/Q3-earnings-transcript-2023 |
| 13 Dec 2023 | Q4 FY2023 release | ATS Q4: organic (16.4)%, acquisitions 15.0%, currency 0.5%, total (0.9)%. FY2023 ATS: organic (9.2)%, acquisitions 12.9%, currency (1.1)%, total 2.6%. | CyberOptics contribution: Q4 +15.0%, FY2023 +12.9% of ATS growth | https://www.sec.gov/Archives/edgar/data/72331/000007233123000232/ndsn-20231213xex991.htm |
| 14 Dec 2023 | Q4 FY2023 call (TickerTrends), Kelley | "offset by the CyberOptics acquisition, which contributed 15%, the highest quarterly sales to date under Nordson ownership." | Acq. +15% | https://tickertrends.io/transcripts/NDSN/Q4-earnings-transcript-2023 |
| 20 Dec 2023 | FY2023 10-K, MD&A | ATS FY2023 sales $577,270 vs $562,859, with "a 12.9 percent increase from acquisitions". Organic decrease 9.2%: "The organic sales decrease was driven by lower demand in electronics dispense product lines", partially offset by test and inspection (WebFetch paraphrase of the rest of the sentence). | – | https://www.sec.gov/Archives/edgar/data/72331/000007233123000242/ndsn-20231031.htm |
| 20 Dec 2023 | FY2023 10-K, Critical Accounting Policies (goodwill test, measurement date 1 Aug 2023) | Row "Advanced Technology Solutions Segment - Test & Inspection": WACC 9.5%, excess of FV over CV 168%, goodwill $371,425k. Row "ATS - Electronics Systems": 9.0%, 387%, $27,534k. | T&I goodwill $371.4M | same |
| 21 May 2024 | Q2 FY2024 call (TickerTrends), Nagarajan | "our X-ray business, which experienced double-digit growth in fiscal 2023 is dealing with challenging comparisons in the second half of the year." He also said: "The acoustic test and inspection part of the business is also growing, which is more on the front end and on some new memory applications." | X-ray growth FY2023 "double-digit" | https://tickertrends.io/transcripts/NDSN/Q2-earnings-transcript-2024 |
| 22 Aug 2024 | Q3 FY2024 call (TickerTrends), Nagarajan | "Our x-ray product lines, which experienced double-digit growth in fiscal 2023, continued to deal with challenging comparisons in the fourth quarter." | – | https://tickertrends.io/transcripts/NDSN/Q3-earnings-transcript-2024 |
| 18 Dec 2024 | FY2024 10-K, Critical Accounting Estimates (measurement date 1 Aug 2024) | Row "ATS - Test & Inspection": WACC 8.5%, excess of FV over CV 173%, goodwill $375,707k. Row "ATS - Electronics Systems": 8.5%, 252%, $27,442k. MD&A: "The ATS organic sales decrease of 11.4 percent was driven by lower demand in electronics dispense product lines", plus lower T&I demand (paraphrase). | T&I goodwill $375.7M | https://www.sec.gov/Archives/edgar/data/72331/000007233124000177/ndsn-20241031.htm |
| 11 Dec 2024 | Q4 FY2024 release / 12 Dec 2024 call (Hopgood) | "Growth in the quarter was driven by improvement in selected test and inspection product lines, as well as modest improvement within our electronics dispense product lines." | ATS organic +3.9% | https://tickertrends.io/transcripts/NDSN/Q4-earnings-transcript-2024 |
| 19 Feb 2025 | Q1 FY2025 release | "driven by lower systems deliveries in electronics processing and x-ray product lines, partially offset by growth in optical sensors and measurement and control product lines." | ATS organic (9.6)% | https://www.nasdaq.com/press-release/nordson-corporation-reports-first-quarter-fiscal-2025-results-and-second-quarter |
| 20 Feb 2025 | Q1 FY2025 call (TickerTrends), Hopgood | "The decrease in sales was driven by double-digit declines in electronics processing and x-ray product lines". He added: "Orders were up double digits in the quarter versus the prior year, and backlog grew double digits sequentially from the end of the year for this segment." | X-ray "double-digit declines" | https://tickertrends.io/transcripts/NDSN/Q1-earnings-transcript-2025 |
| 29 May 2025 | Q2 FY2025 call (TickerTrends), Hopgood | "The growth in sales was driven by broad-based demand, notably in electronics dispense, optical, and x-ray inspection systems, all growing double-digits over the prior year." | Optical and X-ray growth "double-digits" (Q2 FY2025) | https://tickertrends.io/transcripts/NDSN/Q2-earnings-transcript-2025 |
| 29 May 2025 | Same call, Nagarajan (answering a question on the HPC share of ATS) | "I would say I think 50% of our business would be semiconductor high-power computing, as you describe it. And a couple of years ago, I don't know, if you go back, I want to say four, five years ago, maybe that number was 30% or so. Look, I'm guessing here 20% to 30% at past." | Semi/HPC ~50% of ATS (from 20–30% four to five years ago) | same |
| 29 May 2025 | Investor deck "FY25 Nordson Investor Presentation 5-29-25" | ATS FY2024 revenue "$596M", EBITDA "22%". ATS end markets: Semiconductors "50% of ATS Sales"; Automotive Electronics "14%"; General Electronics "36%". Market growth rates 6-8% / 6-8% / 3-5%. | Semi 50% of ATS | https://s202.q4cdn.com/528247721/files/doc_presentations/2025/May/29/FY25-Nordson-Investor-Presentation-5-29-25UD.pdf |
| 21 Aug 2025 | Q3 FY2025 call (TickerTrends), Hopgood | "The 15% organic sales increase was driven by double-digit growth in electronics dispense product lines ... as well as growth in our optical sensors and our measurement and controls businesses. This was partially offset by weakness in X-ray Inspection system sales during the quarter." | – | https://tickertrends.io/transcripts/NDSN/Q3-earnings-transcript-2025 |
| 10 Dec 2025 | Q4 FY2025 release | "Ongoing sales strength in electronics dispense systems was more than offset by fewer deliveries of test and inspection systems, particularly x-ray systems." | ATS organic (4.9)% | https://www.nasdaq.com/press-release/nordson-corporation-reports-record-fourth-quarter-and-fiscal-year-2025-results-2025 |
| 11 Dec 2025 | Q4 FY2025 call (TickerTrends), Nagarajan | "We remind our investors of semiconductor applications account for approximately 50% of ATS revenue." He also said: "Just for color, 50% of the revenues come from the semiconductor space, about 15% or so in the automotive and the rest is in electronics". | Semi ~50%, auto ~15% of ATS | https://tickertrends.io/transcripts/NDSN/Q4-earnings-transcript-2025 |
| 17 Dec 2025 | FY2025 10-K, MD&A | "The ATS organic sales increase of 4.1 percent was driven by robust growth in electronics dispense product lines and electronic processing and optical sensors, partially offset by weakness in x-ray inspection systems." The FY2024 sentence on the recast basis: "The ATS organic sales decrease of 11.2 percent was driven by lower demand in electronics dispense product lines, measurements and controls, as well as test and inspection product lines." | – | https://s202.q4cdn.com/528247721/files/doc_financials/2025/ar/10-K.pdf |
| 17 Dec 2025 | FY2025 10-K, Item 1 | The T&I description now covers "precision measurement and control technologies that ensure quality and reliability through in-line measurement sensors, gauges, and analyzers that use near-infrared, laser, X-ray, optical, and nucleonic technologies". Key end markets "include semiconductor packaging, printed circuit boards, flexible circuits, consumer electronics, as well as consumer non-durable, film extrusion and converting, cable and tubing and energy storage." | – | same |
| 18–19 Feb 2026 | Q1 FY2026 release / 10-Q MD&A | Release: "driven by ongoing growth in electronics dispense systems and recovering demand for x-ray systems." 10-Q: the ATS organic sales increase of 20.7 percent was "driven by ongoing growth in electronics dispense and recovering demand for x-ray systems". | ATS organic +20.7% | https://www.nasdaq.com/press-release/nordson-corporation-reports-record-first-quarter-fiscal-2026-results-and-increases ; https://www.sec.gov/Archives/edgar/data/72331/000007233126000014/ndsn-20260131.htm |
| 19 Feb 2026 | Q1 FY2026 call (TickerTrends), Nagarajan | "Semiconductor applications account for approximately 50% of revenue in the ATS segment and drove the overall double-digit organic growth in the first quarter." On AMI: "There, we are coming off of 2 really strong years of growth." | Semi ~50% of ATS | https://tickertrends.io/transcripts/NDSN/Q1-earnings-transcript-2026 |
| 20–21 May 2026 | Q2 FY2026 release / 10-Q MD&A (pubt.io) | "The ATS organic sales increase of 8.5 percent was driven by ongoing growth in electronics dispense systems." Six months: "The ATS organic sales increase of 13.8 percent was driven by exceptional growth in electronic dispense systems." | – | https://www.nasdaq.com/press-release/nordson-corporation-reports-record-second-quarter-fiscal-2026-results-and-increases ; https://pubt.io/view/CB56C43F60C767140DCB8905BBF6413C280F4576 |
| 21 May 2026 | Q2 FY2026 call (TickerTrends), Nagarajan | "In terms of number of applications, if you think about this business, over 50% of this business is in semiconductor now." | Semi ">50%" of ATS | https://tickertrends.io/transcripts/NDSN/Q2-earnings-transcript-2026 |
| 19 Aug 2026 | Q3 FY2026 release | "The organic sales increase was driven by strong growth in electronics dispense and test and inspection product lines." | ATS organic +30.9% | https://www.nasdaq.com/press-release/nordson-corporation-reports-record-third-quarter-fiscal-2026-results-and-increases |
| 20 Aug 2026 | Q3 FY2026 10-Q MD&A (excerpt via last10k; truncated at 125 chars) | "The ATS organic sales increase of 30.9 percent was driven by strong growth in electronics dispense" … Nine months: "The ATS organic sales increase of 20.1 percent was driven by exceptional growth in electronics dispense" … | – | https://last10k.com/sec-filings/ndsn/0000072331-26-000054.htm |
| 20 Aug 2026 | Investor deck "FY26 Nordson Investor Presentation 8-20-26" | ATS FY2025 revenue "$625M", EBITDA "24%", historical 5-year sales CAGR "9%" ($413M in 2020 to $625M in 2025). ATS end markets: Semiconductors "50% of ATS Sales", General Electronics "25%", Automotive Electronics "10%", Industrial "15%". Market growth rates 6-8% / 3-5% / 2-4% / 1-3%. ATS geography: Asia 67%, Americas 20%, Europe 13%. | Semi 50% of ATS | https://s202.q4cdn.com/528247721/files/doc_financials/2026/q3/FY26-Nordson-Investor-Presentation-8-20-26.pdf |
| 23 Oct 2026 | Contrinex release | "generates approximately $50 million in annual revenue"; "complements Nordson's test and inspection portfolio"; ATS segment; EV ~USD 168M (8-K) | ~$50M revenue | see 0 |

**Semiconductor share of total Nordson: NOT DISCLOSED as a single number** (checked: 10-Ks, decks, calls). Related group-level figures from NORDSON decks:
- "Electronics" was "27% of revenue" in the FY2025 profile (Aug 2026 deck).
- In the May 2025 deck, "Electronics 25% of revenue".
- In the Aug 2024 deck, "Electronics 27% of revenue" (approximate FY2023 mix, "for directional use only").

---

## 2. Q5b – ATS segment, quarterly and annual (USD thousands unless noted)

Columns: sales; YoY total %; organic %; acquisitions %; FX %; segment operating profit (GAAP); EBITDA (non-GAAP) and margin. Sources are the 8-K Ex. 99.1 releases (sec.gov or Nasdaq copies) listed in section 7.

**Basis A: as originally reported** (three-segment structure from Q4 FY2022, before the MCS transfer)

| Period (FY end 31 Oct) | Sales | YoY % | Organic % | Acq % | FX % | Seg. op. profit | EBITDA (margin) | Source (release date) |
|---|---|---|---|---|---|---|---|---|
| Q1 FY2022 (Jan-22) | 126,449 | +29.2 (computed vs recast 97,890) | NOT DISCLOSED on 3-segment basis (checked: 8-K 8 Sep 2022) | NOT DISCLOSED | NOT DISCLOSED | 27,234 | 29,497 (23%) [as comparative in Q1 FY2023 release] | 8-K 8 Sep 2022; Q1 FY23 release 20 Feb 2023 |
| Q2 FY2022 (Apr-22) | 146,757 | +20.3 (computed vs 121,992) | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | 40,144 | 42,391 (29%) | 8-K 8 Sep 2022; Q2 FY23 release |
| Q3 FY2022 (Jul-22) | 143,073 | +8.2 (computed vs 132,290) | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | 28,155 | 30,350 (21%) | 8-K 8 Sep 2022; Q3 FY23 release |
| Q4 FY2022 (Oct-22) | 146,580 | +20.7 | +27.8 | – | (7.1) | 37,720 (26%) | 39,795 (27%) | Q4 FY22 release 14 Dec 2022 |
| **FY2022** | 562,859 | +18.8 | +22.4 | – | (3.6) | 133,253 (24%) | 142,033 (25%) | same |
| Q1 FY2023 | 144,644 | +14.4 | +4.6 | +13.5 | (3.7) | 16,963 (adj. 27,258, 19%) | 31,070 (21%) | 20 Feb 2023 |
| Q2 FY2023 | 147,832 | +0.7 | (9.9) | +12.3 | (1.7) | 26,090 (adj. 28,050, 19%) | 32,060 (22%) | 22 May 2023 |
| Q3 FY2023 | 139,549 | (2.5) | (12.8) | +10.7 | (0.4) | 27,083 (adj. 29,132, 21%) | 32,966 (24%) | 21 Aug 2023 |
| Q4 FY2023 | 145,245 | (0.9) | (16.4) | +15.0 | +0.5 | 31,526 (22%) | 35,055 (24%) | 13 Dec 2023 |
| **FY2023** | 577,270 | +2.6 | (9.2) | +12.9 | (1.1) | 101,662 (17.6%; adj. 115,966, 20%) | 131,151 (23%) | 13 Dec 2023; FY23 10-K |
| Q1 FY2024 | 119,120 | (17.6) | (17.6) | – | – | 19,038 | 22,479 (19%) | 21 Feb 2024 |
| Q2 FY2024 | 114,685 | (22.4) | (21.6) | – | (0.8) | 18,784 | 24,146 (21%) | 20 May 2024 |
| Q3 FY2024 | 124,306 | (10.9) | (10.2) | – | (0.7) | 22,945 | 26,313 (21%) | 21 Aug 2024 |
| Q4 FY2024 | 152,109 | +4.7 | +3.9 | – | +0.8 | 33,464 | 40,620 (27%) | 11 Dec 2024 |
| **FY2024** | 510,220 | (11.6) | (11.4) | – | (0.2) | 94,231 | 113,559 (22%) | 11 Dec 2024; FY24 10-K |

**Basis B: recast with MCS in ATS** (effective 1 Nov 2024; as reported from Q1 FY2025 onward)

| Period | Sales | YoY % | Organic % | Acq % | FX % | Seg. op. profit | EBITDA (margin) | Source |
|---|---|---|---|---|---|---|---|---|
| FY2023 (recast) | 671,246 | – | – | – | – | NOT DISCLOSED on recast basis (checked: FY2025 10-K) | 144,731 (21.6%) | FY2025 10-K Note 15 |
| Q1 FY2024 (recast) | 135,925 | – | – | – | – | 18,304 | 23,205 (17%) | Q1 FY25 release |
| Q2 FY2024 (recast) | 136,698 | – | – | – | – | 20,693 | 27,538 (20%) | Q2 FY25 release |
| Q3 FY2024 (recast) | 145,870 | – | – | – | – | 26,032 | 30,873 (21%) | Q3 FY25 release |
| Q4 FY2024 (recast) | 177,064 | – | – | – | – | NOT DISCLOSED (checked: Q4 FY25 release, FY25 10-K) | 47,564 (27%) | Q4 FY25 release |
| **FY2024 (recast)** | 595,557 | (11.3) vs 671,246 | (11.2) | – | (0.1) | NOT DISCLOSED | 129,181 (21.7%) | FY2025 10-K |
| Q1 FY2025 | 121,363 | (10.7) | (9.6) | – | (1.1) | 18,123 | 22,771 (19%) | 19 Feb 2025 |
| Q2 FY2025 | 161,282 | +18.0 | +18.1 | – | (0.1) | 31,558 | 39,516 (25%) | 28 May 2025 |
| Q3 FY2025 | 171,260 | +17.4 | +14.6 | – | +2.8 | 36,877 | 41,546 (24%) | 20 Aug 2025 |
| Q4 FY2025 | 170,605 | (3.6) | (4.9) | – | +1.3 | NOT DISCLOSED (EBITDA-only tables) | 42,756 (25%) | 10 Dec 2025 |
| **FY2025** | 624,510 | +4.9 | +4.1 | – | +0.8 | NOT DISCLOSED (10-K measure changed to segment EBITDA) | 146,589 (23.5%) | 10 Dec 2025; FY25 10-K |
| Q1 FY2026 | 149,417 | +23.1 | +20.7 | – | +2.4 | NOT DISCLOSED | 32,600 (22%) | 18 Feb 2026 |
| Q2 FY2026 | 177,531 (record) | +10.1 | +8.5 | – | +1.6 | NOT DISCLOSED | 48,327 (27%) | 20 May 2026 |
| Q3 FY2026 | 219,880 (record) | +28.4 | +30.9 | – | (2.5) | NOT DISCLOSED | 65,695 (30%) (segment record) | 19 Aug 2026 |
| **9M FY2026** | 546,828 | +20.5 | +20.1 | – | +0.4 | NOT DISCLOSED | 146,622 (27%) | 19 Aug 2026 |

Notes:
- 9M FY2025 ATS operating profit was 86,558, against 65,029 for 9M FY2024 recast (Q3 FY2025 release).
- ATS depreciation and amortization was 18,741 in FY2025 and 19,102 in FY2024 (Q4 FY2025 release).
- ATS identifiable assets were $738,762k at FY2025 and $864,073k at FY2024 (FY2025 10-K).
- Q4 FY2026: NOT PUBLISHED (release scheduled 15 Dec 2026).

---

## 3. Q5c – Last six earnings calls: HBM / advanced packaging / AI / X-ray / acoustic / T&I / electronics

Host: TickerTrends (full transcripts, 6,400–7,900 words each). Cross-checked on Equibles (equibles.com/stocks/ndsn/calls/<yyyy-qn>). "HBM" and "high bandwidth/high-bandwidth" were searched in both hosts' texts for all six calls: **0 hits in every call.**

| Call (date) | Speaker | Verbatim quote(s) | HBM by name? |
|---|---|---|---|
| **Q2 FY2025, Thu 29 May 2025** (release 28 May 2025) https://tickertrends.io/transcripts/NDSN/Q2-earnings-transcript-2025 | S. Nagarajan (CEO) | "What you really see is this incredible investment that is going on for computing power, be it for AI, be it for cloud computing or e-commerce, any of that. ... And at the heart of all of that investment is really complex new generation computer chips and semiconductors, right. And plays really well to Nordson." / "I think we are at very early stages of the GPUs that are getting built. ... And we have new categories of products through our CyberOptics acquisition. We have a new generation of in-process sensors called WaferSense. And that is a product category that is growing very nicely for us." / "I would say I think 50% of our business would be semiconductor high-power computing ... as we will have packaging lines come on Nordson is going to benefit." | No |
| | D. Hopgood (CFO) | "The growth in sales was driven by broad-based demand, notably in electronics dispense, optical, and x-ray inspection systems, all growing double-digits over the prior year." | |
| **Q3 FY2025, Thu 21 Aug 2025** (release 20 Aug 2025) https://tickertrends.io/transcripts/NDSN/Q3-earnings-transcript-2025 | Nagarajan | "In addition to being located close to the customer, our products deliver leading productivity and quality in complex advanced packaging applications of semiconductors used for AI, cloud computing and more. Our applications are largely at the back end of the semiconductor packaging process, and we are experiencing that demand now." / "So semiconductor on track, electronic PCBA, high reliability ones are doing well." / "particularly we have new software subscription services in our X-ray business." | No |
| | Hopgood | "The 15% organic sales increase was driven by double-digit growth in electronics dispense product lines ... This was partially offset by weakness in X-ray Inspection system sales during the quarter." / "We're seeing -- we've been seeing good solid demand from our Acoustic and Optical products throughout the year." | |
| **Q4 FY2025, Thu 11 Dec 2025** (release 10 Dec 2025) https://tickertrends.io/transcripts/NDSN/Q4-earnings-transcript-2025 | Hopgood | "The year-over-year organic sales decline was driven by weakness in x-ray systems demand. We continue to see strong growth in electronic dispense product lines and stable demand for optical, acoustic and other product lines, but these were overshadowed by near-term weakness in x-ray systems during the quarter." / "organic sales were really weighed down by three specific areas: polymer processing systems, our automotive-related systems and selected X-ray Inspection applications." | No (memory referenced: "acoustic for memory") |
| | Nagarajan | "We remind our investors of semiconductor applications account for approximately 50% of ATS revenue. ... our products deliver leading productivity and quality in complex advanced packaging applications of semiconductors used for AI, cloud computing and more." / "I would say the strength continues and remains in the semiconductor space for the AI applications, cloud computing and such." / On X-ray: "it has great exposure to our semiconductor, but it also has a pretty solid exposure to automotive." He continued: "if you think about these composite structures that people are building, where you have both logic as well as memory on that, there are parts of that structure cannot be inspected with x-ray ... And for Nordson's position, we have both those technologies. So you typically use acoustic for memory and you use more x-ray for -- you use x-ray for logic chips, right?" On new technologies: "there is a transition in technology that is happening in testing as we speak and we have some new technologies that we are testing right now which certainly will have an impact, but probably not in '26, probably in '27." / "the x-ray business is in a good spot, certainly did not contribute last year." | |
| **Q1 FY2026, Thu 19 Feb 2026** (release 18 Feb 2026) https://tickertrends.io/transcripts/NDSN/Q1-earnings-transcript-2026 | Nagarajan | "Within advanced technology, our dispense and surface treatment product lines for semiconductor application continue to drive growth, while our X-ray systems that ensure the quality of semiconductor packaging are starting to inflect." / "ATS core competency is in the advanced packaging process of semiconductor manufacturing." / "Quality control of these costly and complex chips is also creating more opportunities for our test and inspection portfolio." / "If you think about our T&I, you want to think about it in 2 pieces. One is our X-ray businesses and the other one is our what we call as AMI businesses. And so these are acoustic emission-based inspection techniques and optical techniques." He added: "These complex chips are now both combined logic and memory on the same stack. And so these are very expensive chips and yield rates are everything here." / "this increased demand for AI chip capacity is playing out, and it's playing out in the packaging area right now." / On memory: "We don't have a significant amount of exposure, but we do have exposure in the memory space, in the traditional memory. And when there are capacity adds there, we will benefit." | No (memory referenced) |
| | Hopgood | "The 21% organic sales increase was driven by double-digit growth in electronics dispense product lines related to semiconductor applications as well as recovering demand for our X-ray systems." / "If you think of memory and general electronics requirements, we're starting to see announcements and discussions around capacity investments." | |
| **Q2 FY2026, Thu 21 May 2026** (release 20 May 2026) https://tickertrends.io/transcripts/NDSN/Q2-earnings-transcript-2026 | Nagarajan | "Within electronics and semiconductor applications, our dispense and surface treatment product lines continue to drive growth, while our test and inspection systems that ensure the quality of semiconductor packaging are also inflected." / "as the new AI applications occur, as AI infrastructure happens and semiconductors become more complex, more difficult to manufacture." / "over 50% of this business is in semiconductor now." / "a couple of things that you would probably be reading about is panel-level packaging. It's very, very early stage, but we are participating in developing these technologies. If you think about optical fibers and increased content of optical fibers and AI infrastructure, that's another big area." / "predominantly, we are seeing the growth today in our electronic dispense business and our test and inspection businesses are beginning to inflect and there is more to come there." | No ("advanced packaging" not said; "packaging" said in the panel-level context) |
| | Hopgood | "The 8% organic sales increase in the quarter was most notable in our electronics dispense product lines and reflects ongoing strength in semiconductor end market demand, which we're also seeing in orders across all of our ATS product lines." | |
| **Q3 FY2026, Thu 20 Aug 2026** (release 19 Aug 2026) https://tickertrends.io/transcripts/NDSN/Q3-earnings-transcript-2026 | Hopgood | "Organically, sales increased 31% with growth coming across both the Electronics Dispense and Test and Inspection product lines, reflecting the continued strength in semiconductor and broadening electronics end market demand." | No (no AI, memory or "advanced packaging" mention; "AI" count 0) |
| | Nagarajan | "Broad-based growth in the quarter with both our dispense business and T&I business. Clearly, the dispense business is typically ahead of the curve in terms of growth cycle, and that's what we saw. In the quarter, certainly, our T&I businesses continue to grow nicely, a good inflection point both for our X-ray and optical businesses. If you remember, these technologies are critical in ensuring semiconductor packaging." / "if you think about in terms of our dispense business, our test and inspection business, our exposure in EFD to electronics, all of them indicating that we are -- we still have room in this cycle". On M&A: "We certainly look at test and inspection as well as the other area we are spending time on." | |

Keyword counts per call in the TickerTrends text (memory / "advanced packaging" / x-ray / acoustic / "test and inspection" or "T&I" / "AI" / "data center" / HBM):

| Call | memory | adv. packaging | x-ray | acoustic | T&I | AI | data center | HBM |
|---|---|---|---|---|---|---|---|---|
| Q2 FY25 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| Q3 FY25 | 0 | 1 | 3 | 2 | 1 | 9 | 0 | 0 |
| Q4 FY25 | 2 | 1 | 17 | 2 | 0 | 4 | 1 (analyst) | 0 |
| Q1 FY26 | 5 | 1 | 13 | 3 | 7 | 3 | 1 (analyst) | 0 |
| Q2 FY26 | 0 | 0 | 0 | 0 | 11 | 4 | 0 | 0 |
| Q3 FY26 | 0 | 0 | 1 | 0 | 7 | 0 | 1 (IPS context) | 0 |

---

## 4. Q5d – Group-level fact base

### 4a. Group P&L (USD thousands except EPS). Sources: XBRL companyfacts, 8-K releases.

| Period | Sales | Organic % | Op. profit (GAAP) | Op. margin (computed) | Adj. op. profit | EBITDA non-GAAP (margin) | GAAP dil. EPS | Adj. EPS |
|---|---|---|---|---|---|---|---|---|
| FY2022 | 2,590,278 | +10.8 | 702,360 | 27.1% | 707,318 | 807,241 (31%) | 8.81 | 9.43 (orig.); 10.13 (revised definition excl. acq. amortization) |
| FY2023 | 2,628,632 | (1.4) | 672,761 | 25.6% | 707,076 | 818,974 (31%) | 8.46 | 9.03 (orig.); 9.85 (revised) |
| FY2024 | 2,689,921 | (2.5) | 674,001 | 25.1% | 712,993 | 849,168 (32%) | 8.11 | 9.73 |
| FY2025 | 2,791,687 | (2.5) | 711,725 | 25.5% | 748,995 | 899,518 (32%) | 8.51 | 10.24 |
| Q1 FY2025 | 615,420 | (9.4) | 140,947 | 22.9% | 151,073 | 188,103 (31%) | 1.65 | 2.06 |
| Q2 FY2025 | 682,938 | (2.4) | 168,750 | 24.7% | 179,576 | 217,154 (32%) | 1.97 | 2.42 |
| Q3 FY2025 | 741,509 | +2.1 | 187,767 | 25.3% | 200,664 | 238,511 (32%) | 2.22 | 2.73 |
| Q4 FY2025 | 751,820 | (1.1) | 214,261 | 28.5% | 217,682 | 255,751 (34%) | 2.69 | 3.03 |
| Q1 FY2026 | 669,461 | +6.5 | 166,405 | 24.9% | 166,405 | 202,990 (30%) | 2.38 | 2.37 |
| Q2 FY2026 | 740,847 | +6.6 | 197,203 | 26.6% | 198,872 | 235,187 (32%) | 2.09 | 2.86 |
| Q3 FY2026 | 817,667 | +11.7 | 223,092 | 27.3% | 225,937 | 262,483 (32%) | 2.73 | 3.25 |
| 9M FY2026 | 2,227,975 | +8.4 | 586,700 | 26.3% | 591,214 | 700,660 (31%) | 7.20 | 8.48 |
| Q4 FY2026 / FY2026 | NOT PUBLISHED (due 15 Dec 2026) | | | | | | | |

Net income: FY2023 487,493; FY2024 467,284; FY2025 484,474; Q1 FY2026 133,382; Q2 117,316; Q3 152,846; 9M 403,544. GAAP items in FY2026:
- Q1 FY2026: a non-cash gain on a minority investment.
- Q2 FY2026: a "one-time, non-cash settlement charge to annuitize about 30% of the U.S. pension obligation" and a "non-cash loss on minority investments".
- Q3 FY2026: a "non-cash loss on a minority investment".

### 4b. Segment sales and profit (USD thousands)

| Period | IPS sales | IPS op. profit | IPS EBITDA (m) | MFS sales | MFS op. profit | MFS EBITDA (m) | ATS sales | ATS op. profit | ATS EBITDA (m) | Corporate (OP / EBITDA) |
|---|---|---|---|---|---|---|---|---|---|---|
| FY2023 (orig.) | 1,391,046 | 460,889 | 498,775 (36%) | 660,316 | 189,367 | 245,834 (37%) | 577,270 | 101,662 | 131,151 (23%) | (79,157) / (56,786) |
| FY2023 (recast, FY25 10-K) | 1,297,070 | n/d | 485,195 | 660,316 | n/d | 245,834 | 671,246 | n/d | 144,731 | – / (56,786) |
| FY2024 (orig.) | 1,484,249 | 470,559 | 536,391 (36%) | 695,452 | 187,731 | 256,553 (37%) | 510,220 | 94,231 | 113,559 (22%) | (78,520) / (57,335) |
| FY2024 (recast) | 1,398,912 | n/d | 520,769 (37.2%) | 695,452 | n/d | 256,553 (36.9%) | 595,557 | n/d | 129,181 (21.7%) | – / (57,335) |
| FY2025 | 1,331,792 | n/d | 493,873 (37.1%) | 835,385 | n/d | 311,684 (37.3%) | 624,510 | n/d | 146,589 (23.5%) | – / (52,628) |
| 9M FY2025 | 970,079 | 308,153 | 356,453 (37%) | 615,883 | 150,241 | 224,023 (36%) | 453,905 | 86,558 | 103,833 (23%) | (47,488) / (40,542) |
| Q1 FY2026 | 326,861 | n/d | 110,311 (34%) | 193,183 | n/d | 70,206 (36%) | 149,417 | n/d | 32,600 (22%) | – / (10,127) |
| Q2 FY2026 | 350,466 | n/d | 123,578 (35%) | 212,850 | n/d | 79,193 (37%) | 177,531 | n/d | 48,327 (27%) | – / (15,911) |
| Q3 FY2026 | 367,249 | n/d | 129,900 (35%) | 230,538 | n/d | 88,291 (38%) | 219,880 | n/d | 65,695 (30%) | – / (21,403) |
| 9M FY2026 | 1,044,576 | n/d | 363,789 (35%) | 636,571 | n/d | 237,690 (37%) | 546,828 | n/d | 146,622 (27%) | – / (47,441) |

n/d = NOT DISCLOSED. Checked: FY2025 10-K, Q4 FY2025 release and Q1–Q3 FY2026 releases. From FY2025 the segment measure is EBITDA, and the releases show EBITDA only.

Segment organic growth in FY2026:

| Period | IPS | MFS | ATS |
|---|---|---|---|
| Q1 | +3.2% | +2.7% (acq/div (4.3)%) | +20.7% |
| Q2 | +5.0% (acq +0.8%) | +7.8% (div (3.9)%) | +8.5% |
| Q3 | +3.3% (acq +0.9%) | +10.6% (div (5.6)%) | +30.9% |
| 9M | +3.8% | +7.1% | +20.1% |

In FY2025, organic growth was IPS (5.1)%, MFS (3.1)% (acq +23.0%) and ATS +4.1%.

### 4c. FY2026 guidance as issued and revised

| Date | Document | FY2026 sales | FY2026 adj. EPS | Next-quarter guide | Actual for that quarter |
|---|---|---|---|---|---|
| 10 Dec 2025 | Q4 FY25 release | "$2,830 to $2,950 million". The call put it at "1% to 6% above fiscal 2025 sales", midpoint 3.5%. | "$10.80 to $11.50" (call: "6% to 12% growth", midpoint 9%) | Q1: $630–670M; $2.25–2.45 | Q1: $669.5M; $2.37 |
| 18 Feb 2026 | Q1 FY26 release | "$2,860 to $2,980 million" | "$11.00 to $11.60" | Q2: $710–740M; $2.70–2.90 | Q2: $740.8M; $2.86 |
| 20 May 2026 | Q2 FY26 release | "$2,930 to $3,010 million" | "$11.30 to $11.80" | Q3: $760–790M; $2.95–3.15 | Q3: $817.7M; $3.25 |
| 19 Aug 2026 | Q3 FY26 release | "$3,035 to $3,075 million". Deck: "sales growth now expected in the range of 9% to 10%". | "$11.80 to $12.00" (deck: "15% to 17%") | No separate Q4 guide in the release. Implied Q4 is $807–847M (computed: FY guide less 9M sales). | Q4 NOT PUBLISHED |

CEO, 19 Aug 2026 release: "This puts us on track to achieve over $3 billion in annual revenue for the full year." Long-term targets for 2025–2029 (Oct 2024 Investor Day, restated on the 11 Dec 2025 call): "average annual growth of 6% to 8% in revenue ... and 10% to 12% in adjusted EPS growth".

### 4d. Backlog and orders commentary (NORDSON)

| Date | Statement |
|---|---|
| 14 Dec 2022 | Enter FY2023 with "approximately $1 billion in backlog, inclusive of the acquired CyberOptics backlog" |
| 13 Dec 2023 | Enter FY2024 with "approximately $800 million in backlog" |
| 21 Feb 2024 | Enter Q2 FY2024 with "approximately $750 million in backlog, which continues to normalize and remain concentrated in systems businesses" |
| 20 May 2024 | Enter Q3 FY2024 with ~$700M |
| 21 Aug 2024 | Enter Q4 FY2024 with ~$650M |
| 11 Dec 2024 | "we enter fiscal 2025 with approximately $580 million in backlog." |
| 19 Feb 2025 | Entered Q2 FY2025 with "approximately $670 million in backlog, up approximately $85 million or 15% from the start of the year". ATS (call, Hopgood): "Orders were up double digits in the quarter versus the prior year, and backlog grew double digits sequentially from the end of the year for this segment." |
| 28 May 2025 | Backlog "up approximately 5% from the prior quarter" |
| 20 Aug 2025 | "Backlog is down approximately 5% sequentially following a strong third quarter." |
| 10 Dec 2025 | Enter FY2026 with "approximately $600 million in backlog, up 5% from the prior year end, excluding backlog associated with the divested business." |
| 18 Feb 2026 | Backlog "up approximately 4% over the prior year. Order entry momentum was broad-based in the quarter with particular strength in our ATS segment." |
| 20–21 May 2026 | "backlog up 18% compared to prior year". Call (Nagarajan): "The ATS segment, if you look at our 18% backlog growth, is one of the strongest is because of robust backlog growth in ATS." |
| 19–20 Aug 2026 | "backlog up 35% compared to prior year". Call (Hopgood): "Backlog growth was broad-based with all segments contributing, but particular strength coming from our Advanced Technology and Medical segments." |

ATS order growth in percent or dollars: NOT DISCLOSED. Checked: the Q2 FY2026 call (an analyst asked "Is it up single digits, double digits?" and got no number), the Q3 FY2026 call and the releases.

### 4e. Free cash flow (FCF = operating cash flow minus capex; USD thousands)

| Period | Op. cash flow | Capex | FCF | Conversion (NORDSON) |
|---|---|---|---|---|
| FY2023 | 641,282 | 34,583 | 606,699 (computed; not stated in Q4 FY23 release) | – |
| FY2024 | 556,193 | 64,410 | 491,783 | 105% |
| FY2025 | 719,175 | 58,060 | 661,115 (record) | 136% |
| Q1 FY2026 | 140,428 | – | 122,915 | 105% |
| Q2 FY2026 | – | – | 170,493 | 119% |
| Q3 FY2026 | – | – | 236,752 | 144% |
| 9M FY2026 | 570,473 | 40,313 | 530,160 | 125% |

### 4f. Net debt and leverage (NORDSON call statements; balance sheet from XBRL)

| Date (period end) | Statement | Balance sheet (USD thousands) |
|---|---|---|
| 31 Oct 2023 | "net debt was $1.6 billion, resulting in a leverage ratio of 2 times" (14 Dec 2023 call) | Cash 115,679; current debt 115,662; LTD 1,621,394 |
| 31 Oct 2024 | "net debt at $2.1 billion resulting in a leverage ratio of 2.5 times" (12 Dec 2024 call). Sep 2024: "$600 million in five-year notes at 4.5%" for Atrion. | Cash 115,952; current 103,928; LTD 2,101,197 |
| 30 Apr 2025 | "net debt was approximately $2.1 billion resulting in a leverage ratio of 2.4 times" | – |
| 31 Jul 2025 | "net debt was about $2 billion"; "improving our leverage ratio from 2.5x at the start of the year to 2.2x" | – |
| 31 Oct 2025 | "net debt was approximately $1.9 billion, resulting in a leverage ratio of 2.1x" | Cash 108,442; current 315,000; LTD 1,681,254 |
| 31 Jan 2026 | "net debt was approximately $1.9 billion. Our leverage ratio of 2.1x" | Cash 120,392; current 54,312; LTD 1,943,182 |
| 30 Apr 2026 | "net debt was approximately $1.8 billion. Our leverage ratio of 1.9x ... is now actually below the low end of our long-term target range" | Cash 102,017; current 50,000; LTD 1,836,356 |
| 31 Jul 2026 | "net debt was approximately $1.6 billion ... leverage ratio decreasing further to 1.7x" | Cash 113,431; short-term debt and current maturities 202,000 (incl. commercial paper 192,000); LTD 1,529,005 |

Target range: "long-term targeted leverage ratio of 2 times to 2.5 times" (29 May 2025 call).

Financing events:
- Sep 2023: "$850 million in five and 10 year bonds" to refinance ARAG bridge (14 Dec 2023 call).
- 30 Jan 2026: Amended and Restated Credit Agreement, $1,200M revolver maturing 30 Jan 2031. Proceeds repaid $248.0M of term loans. https://www.sec.gov/Archives/edgar/data/72331/000007233126000005/ndsn-20260130.htm
- 2 Jun 2026: $1.2B commercial paper program, maturities up to 364 days. https://www.sec.gov/Archives/edgar/data/72331/000007233126000034/ndsn-20260602.htm

### 4g. Acquisitions and divestitures since FY2023

| Deal | Signed / closed | Price | Segment | Revenue stated | Source |
|---|---|---|---|---|---|
| CyberOptics (acq.) | Agreed 8 Aug 2022; closed 3 Nov 2022 | $54.00/sh; $377,843k net of cash $40,890k | ATS (T&I) | ~$100M annual (8 Aug 2022) | See 1 |
| ARAG Group (acq.) | SPA 25 Jun 2023; closed 24 Aug 2023 | "approximately €957,000 [thousand], net of the repayment of approximately €30,300 of debt". FY2023 cash paid for all acquisitions net of cash: $1,422,780k (XBRL). | IPS | NOT DISCLOSED in 10-K | FY2025 10-K Note 3 |
| Atrion (acq.) | Merger agreement 28 May 2024; closed 21 Aug 2024 | $789,996k net of cash acquired | MFS | NOT DISCLOSED in 10-K | FY2025 10-K Note 3 |
| Medical contract manufacturing (div.) | Agreement signed 28 May 2025 (May 2025 deck); completed 2 Sep 2025 | Loss on sale $5,857k; total divestiture and related charges $12,545k. FY2025 cash flow "Sale (acquisition) of businesses, net" +28,107k. Call: "roughly $30 million in net proceeds". | MFS | NOT DISCLOSED | FY2025 10-K Note 4; Q4 FY25 call |
| CapstanAG Systems (acq.) | 16 Mar 2026 | 6M FY2026 cash flow "Acquisition of business, net of cash acquired" $(11,643)k. The release does not name the deal on this line. | IPS | NOT DISCLOSED ("small, but strategic") | Q2 FY26 release |
| Contrinex Holding SA (acq.) | SPA and closing 23 Oct 2026 | EV ~USD 168M | ATS | ~$50M annual | 8-K 23 Oct 2026 |

### 4h. Share repurchases and dividends (USD thousands)

| Period | Buybacks (cash flow) | Program shares / amount / avg price | Dividends paid | DPS declared |
|---|---|---|---|---|
| FY2023 | 89,708 | 373k sh / 79,786 / $213.62 | 150,356 | $2.63 |
| FY2024 | 33,339 | 123k sh / 28,198 / $228.60 | 161,438 | $2.82 |
| FY2025 | 306,367 | 1,400k sh / 299,565 / $214.03 | 179,069 | $3.16 |
| 9M FY2026 | 158,792 (Q1 ~82M, Q2 ~43M per calls) | – | 137,384 | quarterly $0.82 |

- Authorization: "On August 20 2025 ... authorized the repurchase of up to an additional $500,000"; "approximately $724,233 remained available" at 31 Oct 2025 (FY2025 10-K).
- 27 Aug 2026: quarterly dividend raised 15% "to $0.94 per common share from $0.82", payable 2 Oct 2026, record date 10 Sep 2026; "63rd consecutive year". https://finviz.com/news/386153/nordson-corporation-board-of-directors-increases-dividend-15-percent-marking-63-consecutive-years-of-annual-dividend-increases

### 4i. End-market and geographic mix

- Geography (FY2025 10-K):

| Region | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Americas | 1,149,760 | 1,178,626 | 1,205,830 (43.2%) |
| Europe | 682,676 | 726,100 | 722,221 (25.9%) |
| Asia Pacific | 796,196 | 785,195 | 863,636 (30.9%) |

  US sales were 922,733 in FY2025. Sales outside the US were 66.9% of total in FY2025.
- Geography FY2026 (10-Qs): Q1 Americas 261,930 / Europe 182,461 / APAC 225,070; 6M 570,183 / 376,920 / 463,205; 9M 901,654 / 569,351 / 756,970, against 9M FY2025 874,868 / 526,878 / 638,121.
- End markets (Aug 2026 deck, FY2025 profile, "for directional use only"): Electronics 27%, Medical 25%, Consumer non-durable 23%, Industrial 13%, Remaining 12%.
- Product type (same deck): Systems 60%, Parts and consumables 40%.
- Segment shares of FY2025 revenue: IPS 48%, MFS 30%, ATS 22%.
- ATS mix: see 1. It was 50% semiconductor / 25% general electronics / 10% automotive / 15% industrial in the Aug 2026 deck, against 50 / 36 / 14 (no industrial line) in the May 2025 deck.

---

## 5. Claim evidence: "Test & Inspection grows faster than the rest of its segment because of HBM and advanced packaging"

Statements bearing on relative growth of T&I against electronics dispense, and the reasons given (all NORDSON):

| Date | Source | Statement (verbatim) | Direction |
|---|---|---|---|
| 21 May 2026 | Q2 FY2026 call, Nagarajan (TickerTrends; Equibles has the same content) | "There is not really a lag between these different businesses. Right now, the strength is in our dispense businesses. ... We are seeing similar levels of growth in both -- in terms of demand from both these dispense as well as test and inspection. ... there are cases last year, we were growing our test and inspection faster than we were growing our dispense business. And this year, the last 3 quarters, our dispense business is far more robust than our test and inspection business. But when we look at our demand, look at our customer projects, look at all the things that we're working on, there is no difference really." | Dispense faster than T&I (Q4 FY25–Q2 FY26) |
| 20 Aug 2026 | Q3 FY2026 call, Nagarajan | "Clearly, the dispense business is typically ahead of the curve in terms of growth cycle, and that's what we saw. In the quarter, certainly, our T&I businesses continue to grow nicely, a good inflection point both for our X-ray and optical businesses." Release: growth "driven by strong growth in electronics dispense and test and inspection product lines". The 10-Q 9M MD&A sentence starts "driven by exceptional growth in electronics dispense". | Both grew in Q3 FY26; no relative figure |
| 21 May 2026 | Q2 FY2026 call / 10-Q | "predominantly, we are seeing the growth today in our electronic dispense business and our test and inspection businesses are beginning to inflect". 10-Q: the Q2 ATS organic increase of 8.5% was "driven by ongoing growth in electronics dispense systems"; the 6M increase of 13.8% by "exceptional growth in electronic dispense systems". | Dispense-led |
| 19 Feb 2026 | Q1 FY2026 call, Nagarajan | "Clearly, our dispense businesses were the strongest, and that is to be expected". On X-ray: "this is one is a little slower to recover when compared to our dispense business and when compared to our Acoustic Emission. ... our X-ray has some automotive exposure as well. the semi side of X-ray is doing really well and the auto is flattish". On AMI: "we are coming off of 2 really strong years of growth." | Dispense-led; X-ray recovering; X-ray slowed by auto |
| 11 Dec 2025 | Q4 FY2025 call / release | Q4 ATS organic (4.9)%: "Ongoing sales strength in electronics dispense systems was more than offset by fewer deliveries of test and inspection systems, particularly x-ray systems." On reasons: X-ray "also has a pretty solid exposure to automotive"; "you typically use acoustic for memory and you use more x-ray for ... logic chips"; new test technologies have an impact "probably not in '26, probably in '27". | T&I (X-ray) below dispense |
| 17 Dec 2025 | FY2025 10-K | FY2025 ATS +4.1% organic "driven by robust growth in electronics dispense product lines and electronic processing and optical sensors, partially offset by weakness in x-ray inspection systems." | X-ray below dispense in FY25 |
| 21 Aug 2025 | Q3 FY2025 call | "double-digit growth in electronics dispense product lines ... partially offset by weakness in X-ray Inspection system sales". Acoustic and Optical: "good solid demand ... throughout the year". | X-ray below dispense |
| 29 May 2025 | Q2 FY2025 call | "electronics dispense, optical, and x-ray inspection systems, all growing double-digits over the prior year." | Both double-digit |
| 20 Feb 2025 | Q1 FY2025 call | "double-digit declines in electronics processing and x-ray product lines, partially offset by growth in our optical sensors and measurement and control businesses." | Optical/MCS up; X-ray and dispense down |
| FY2024 | FY2024 10-K / calls | ATS organic (11.4)% "driven by lower demand in electronics dispense product lines" and T&I (paraphrase). 21 May 2024 call: "we fundamentally still believe the test and inspection business will be lower declines when compared to our dispense business. What you've got mixed in there is some tough comps in our X-ray business." | Both down; T&I expected to decline less |
| 22 Feb 2024 | Q1 FY2024 call, Nagarajan | "the test and inspection business cyclicality is much more muted when compared to our dispense business. That is a distinct difference. But, yes, it does go through a cycle". | Cyclicality comparison |
| FY2023 | Releases, calls, 10-K | The organic decline was in electronics dispense, "slightly offset by continued growth in test and inspection product lines" (Q2 and Q3 FY2023). Q3 FY2023 call: "high-single-digit growth in the test and inspection business". X-ray had "double-digit growth in fiscal 2023" (21 May 2024 call). CyberOptics (optical) weakness was "relating to the memory end market" (Q1 FY2023) and "has more exposure to the memory end market" (Q2 FY2023). | T&I grew while dispense fell |
| 22 Aug 2023 | Q3 FY2023 call, Nagarajan | "All along, we've talked about T&I yielding the amplitude of the cycles. ... It's smaller in T&I when compared to EPS [Electronics Processing Solutions]". | Lower amplitude in T&I |

Reasons management gave for T&I demand:
- Chip complexity and yield: "These complex chips are now both combined logic and memory on the same stack. And so these are very expensive chips and yield rates are everything here" (19 Feb 2026).
- Quality control of "costly and complex chips" (19 Feb 2026).
- X-ray and optical are "critical in ensuring semiconductor packaging" (20 Aug 2026).
- Acoustic inspection is used for memory and X-ray for logic (11 Dec 2025).
- Reasons given for X-ray lagging: automotive exposure (11 Dec 2025, 19 Feb 2026) and tough comparisons after double-digit FY2023 growth (May and Aug 2024).

**HBM:** not named on any of the six calls from May 2025 to Aug 2026. Checked: TickerTrends and Equibles full texts, 0 hits for "HBM" and "high bandwidth/high-bandwidth". HBM also does not appear in:
- the full-text releases grepped for this note (Q1–Q3 FY2024, Q1–Q2 FY2025, Q4 FY2025, Q1–Q3 FY2026);
- the investor decks of Aug 2024 and May 2025;
- the Aug 2026 investor deck text, where the ATS slides name "Underfill dispense for advanced packaging", "Wafer level and chip level inspection and metrology" and "2D / 2.5D / 3D Architecture";
- the FY2025 10-K text (grep of PDF: 0 hits for "HBM").

"Advanced packaging" is named as the ATS core competency (19 Feb 2026) and in Q3 FY2025 and Q4 FY2025 prepared remarks, but it is not tied to T&I growing faster than dispense. No Nordson statement was found that T&I grows faster than the rest of ATS because of HBM or advanced packaging. Checked: 16 calls from Dec 2022 to Aug 2026, 10-Ks FY2023–FY2025, releases and decks.

---

## 6. Other dated items

- 6 Nov 2026: Q4/FY2026 earnings date announced (15 Dec 2026 after close; webcast 16 Dec 2026, 8:30 AM ET).
- 23 Oct 2026: Contrinex closing (8-K).
- 27 Aug 2026: dividend +15% to $0.94 quarterly.
- 30 Jul 2026: leadership transition in Investor Relations (search-index headline only; not read).
- Q3 FY2026 call (20 Aug 2026) speakers: Matthew Matejka (Senior Director, IR), Sundaram Nagarajan (President and CEO), Dan Hopgood (EVP and CFO).

---

## 7. Sources (one URL per document)

SEC / EDGAR
- Submissions JSON (filing list, checked 2026-11-21): https://data.sec.gov/submissions/CIK0000072331.json
- XBRL companyfacts: https://data.sec.gov/api/xbrl/companyfacts/CIK0000072331.json
- 8-K 23 Oct 2026 (Contrinex): https://www.sec.gov/Archives/edgar/data/72331/000007233126000063/ndsn-20261023.htm
- Ex. 99.1 23 Oct 2026: https://www.sec.gov/Archives/edgar/data/72331/000007233126000063/nordsonskylightpressreleas.htm
- Q3 FY2026 Ex. 99.1 (19 Aug 2026): https://www.sec.gov/Archives/edgar/data/72331/000007233126000052/ndsn-q320268kxex991.htm
- Q2 FY2026 Ex. 99.1 (20 May 2026): https://www.sec.gov/Archives/edgar/data/72331/000007233126000022/ndsn-q220268kxex991.htm
- Q1 FY2026 Ex. 99.1 (18 Feb 2026): https://www.sec.gov/Archives/edgar/data/72331/000007233126000011/ndsn-q120268kxex991.htm
- Q4 FY2025 Ex. 99.1 (10 Dec 2025): https://www.sec.gov/Archives/edgar/data/72331/000007233125000138/ndsn-20251213xex991.htm
- Q3 FY2025 Ex. 99.1 (20 Aug 2025): https://www.sec.gov/Archives/edgar/data/72331/000007233125000112/ndsn-q320258kxex991.htm
- Q2 FY2025 Ex. 99.1 (28 May 2025): https://www.sec.gov/Archives/edgar/data/72331/000007233125000053/ndsn-q220258kxex991.htm
- Q1 FY2025 Ex. 99.1 (19 Feb 2025): https://www.sec.gov/Archives/edgar/data/72331/000007233125000030/ndsn-q120258kxex991.htm
- Q4 FY2024 Ex. 99.1 (11 Dec 2024): https://www.sec.gov/Archives/edgar/data/72331/000007233124000169/ndsn-20241213xex991.htm
- Q3 FY2024 Ex. 99.1 (21 Aug 2024): https://www.sec.gov/Archives/edgar/data/72331/000007233124000108/ndsn-q320248kxex991.htm
- Q2 FY2024 Ex. 99.1 (20 May 2024): https://www.sec.gov/Archives/edgar/data/72331/000007233124000070/ndsn-q220248kxex991.htm
- Q1 FY2024 Ex. 99.1 (21 Feb 2024): https://www.sec.gov/Archives/edgar/data/72331/000007233124000036/ndsn-q120248kxex991.htm
- Q4 FY2023 Ex. 99.1 (13 Dec 2023): https://www.sec.gov/Archives/edgar/data/72331/000007233123000232/ndsn-20231213xex991.htm
- Q3 FY2023 Ex. 99.1 (21 Aug 2023): https://www.sec.gov/Archives/edgar/data/72331/000007233123000141/ndsn-q320238kxex991.htm
- Q2 FY2023 Ex. 99.1 (22 May 2023): https://www.sec.gov/Archives/edgar/data/72331/000007233123000096/ndsn-q220238kxex991.htm
- Q1 FY2023 Ex. 99.1 (20 Feb 2023): https://www.sec.gov/Archives/edgar/data/72331/000007233123000038/ndsn-q120238kxex991.htm
- Q4 FY2022 Ex. 99.1 (14 Dec 2022): https://www.sec.gov/Archives/edgar/data/72331/000007233122000183/ndsn-20221214xex991.htm
- 8-K 8 Sep 2022 recast segments Ex. 99.1: https://www.sec.gov/Archives/edgar/data/72331/000007233122000091/ndsn-sep20228kxex991.htm
- CyberOptics agreement PR 8 Aug 2022: https://www.sec.gov/Archives/edgar/data/72331/000007233122000071/ndsn-aug20228kxex991.htm
- CyberOptics closing 8-K 3 Nov 2022: https://www.sec.gov/Archives/edgar/data/72331/000007233122000121/ndsn-20221103.htm
- 10-K FY2025 (filed 17 Dec 2025): https://www.sec.gov/Archives/edgar/data/72331/000007233125000144/ndsn-20251031.htm
- 10-K FY2024 (filed 18 Dec 2024): https://www.sec.gov/Archives/edgar/data/72331/000007233124000177/ndsn-20241031.htm
- 10-K FY2023 (filed 20 Dec 2023): https://www.sec.gov/Archives/edgar/data/72331/000007233123000242/ndsn-20231031.htm
- 10-Q Q1 FY2026 (filed 19 Feb 2026): https://www.sec.gov/Archives/edgar/data/72331/000007233126000014/ndsn-20260131.htm
- 10-Q Q2 FY2026 (filed 21 May 2026): https://www.sec.gov/Archives/edgar/data/72331/000007233126000024/ndsn-20260430.htm
- 10-Q Q3 FY2026 (filed 20 Aug 2026): https://www.sec.gov/Archives/edgar/data/72331/000007233126000054/ndsn-20260731.htm
- 8-K 30 Jan 2026 (credit agreement): https://www.sec.gov/Archives/edgar/data/72331/000007233126000005/ndsn-20260130.htm
- 8-K 2 Jun 2026 (commercial paper): https://www.sec.gov/Archives/edgar/data/72331/000007233126000034/ndsn-20260602.htm

Full-text mirrors (same documents)
- FY2025 10-K PDF (Nordson IR CDN): https://s202.q4cdn.com/528247721/files/doc_financials/2025/ar/10-K.pdf
- Q2 FY2026 10-Q MD&A (pubt.io): https://pubt.io/view/CB56C43F60C767140DCB8905BBF6413C280F4576
- Q3 FY2026 10-Q MD&A excerpt (last10k): https://last10k.com/sec-filings/ndsn/0000072331-26-000054.htm
- Nasdaq release copies:
  - https://www.nasdaq.com/press-release/nordson-corporation-reports-record-third-quarter-fiscal-2026-results-and-increases
  - https://www.nasdaq.com/press-release/nordson-corporation-reports-record-second-quarter-fiscal-2026-results-and-increases
  - https://www.nasdaq.com/press-release/nordson-corporation-reports-record-first-quarter-fiscal-2026-results-and-increases
  - https://www.nasdaq.com/press-release/nordson-corporation-reports-record-fourth-quarter-and-fiscal-year-2025-results-2025
  - https://www.nasdaq.com/press-release/nordson-corporation-reports-second-quarter-fiscal-2025-results-and-third-quarter
  - https://www.nasdaq.com/press-release/nordson-corporation-reports-first-quarter-fiscal-2025-results-and-second-quarter
  - https://www.nasdaq.com/press-release/nordson-corporation-reports-third-quarter-fiscal-2024-results-and-updates-annual
  - https://www.nasdaq.com/press-release/nordson-corporation-reports-second-quarter-fiscal-2024-results-and-updates-annual
  - https://www.nasdaq.com/press-release/nordson-corporation-reports-first-quarter-fiscal-2024-results-and-narrows-annual
- Contrinex PR (BusinessWire via Finviz): https://finviz.com/news/407247/nordson-corporation-completes-acquisition-of-contrinex-expanding-its-industrial-sensing-and-automation-portfolio
- Dividend PR 27 Aug 2026 (BusinessWire via Finviz): https://finviz.com/news/386153/nordson-corporation-board-of-directors-increases-dividend-15-percent-marking-63-consecutive-years-of-annual-dividend-increases

Nordson IR
- Q4/FY2026 earnings date release (6 Nov 2026): https://investors.nordson.com/news/news-details/2026/Nordson-Corporation-Announces-Earnings-Release-and-Webcast-for-Fourth-Quarter-and-Fiscal-Year-2026/default.aspx
- Investor presentation 20 Aug 2026: https://s202.q4cdn.com/528247721/files/doc_financials/2026/q3/FY26-Nordson-Investor-Presentation-8-20-26.pdf
- Investor presentation 29 May 2025: https://s202.q4cdn.com/528247721/files/doc_presentations/2025/May/29/FY25-Nordson-Investor-Presentation-5-29-25UD.pdf
- Investor presentation 22 Aug 2024: https://s202.q4cdn.com/528247721/files/doc_financials/2024/q3/FY24-Nordson-Investor-Presentation-8-22-2024.pdf

Earnings call transcripts (host: TickerTrends; cross-check host: Equibles)
- Q3 FY2026, 20 Aug 2026: https://tickertrends.io/transcripts/NDSN/Q3-earnings-transcript-2026 (Equibles https://equibles.com/stocks/ndsn/calls/2026-q3)
- Q2 FY2026, 21 May 2026: https://tickertrends.io/transcripts/NDSN/Q2-earnings-transcript-2026 (Equibles .../2026-q2)
- Q1 FY2026, 19 Feb 2026: https://tickertrends.io/transcripts/NDSN/Q1-earnings-transcript-2026 (Equibles .../2026-q1)
- Q4 FY2025, 11 Dec 2025: https://tickertrends.io/transcripts/NDSN/Q4-earnings-transcript-2025 (Equibles .../2025-q4)
- Q3 FY2025, 21 Aug 2025: https://tickertrends.io/transcripts/NDSN/Q3-earnings-transcript-2025 (Equibles .../2025-q3)
- Q2 FY2025, 29 May 2025: https://tickertrends.io/transcripts/NDSN/Q2-earnings-transcript-2025 (Equibles .../2025-q2)
- Q1 FY2025, 20 Feb 2025: https://tickertrends.io/transcripts/NDSN/Q1-earnings-transcript-2025
- Q4 FY2024, 12 Dec 2024: https://tickertrends.io/transcripts/NDSN/Q4-earnings-transcript-2024
- Q3 FY2024, 22 Aug 2024: https://tickertrends.io/transcripts/NDSN/Q3-earnings-transcript-2024
- Q2 FY2024, 21 May 2024: https://tickertrends.io/transcripts/NDSN/Q2-earnings-transcript-2024
- Q1 FY2024, 22 Feb 2024: https://tickertrends.io/transcripts/NDSN/Q1-earnings-transcript-2024
- Q4 FY2023, 14 Dec 2023: https://tickertrends.io/transcripts/NDSN/Q4-earnings-transcript-2023
- Q3 FY2023, 22 Aug 2023: https://tickertrends.io/transcripts/NDSN/Q3-earnings-transcript-2023
- Q2 FY2023, 23 May 2023: https://tickertrends.io/transcripts/NDSN/Q2-earnings-transcript-2023
- Q1 FY2023, 21 Feb 2023: https://tickertrends.io/transcripts/NDSN/Q1-earnings-transcript-2023
- Q4 FY2022, 15 Dec 2022: https://tickertrends.io/transcripts/NDSN/Q4-earnings-transcript-2022
- Q3 FY2022, 23 Aug 2022: https://tickertrends.io/transcripts/NDSN/Q3-earnings-transcript-2022
