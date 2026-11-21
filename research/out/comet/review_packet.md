# Review packet - Comet Holding AG (SIX: COTN)

For an independent reviewer with web search and a URL reader. Fiscal year = calendar year. Page numbers are physical PDF pages.
URLs: AR2025 = https://comet.tech/getContentAsset/cc64c1a0-0700-47e4-8e8e-be7d5b0ff657/8453dbad-8de3-45d3-9ff0-774682f4f15b/Comet_Annual-Report-2025-en.pdf ;
HY2026 = https://comet.tech/getContentAsset/20e73493-df93-42ea-9455-c2883ba7a3c2/8453dbad-8de3-45d3-9ff0-774682f4f15b/Comet-half-year-report-2026.pdf ;
Q3TU = https://comet.tech/news/comet-net-sales-growth-accelerates-further-in-q3-26-en-2026-10-7076a047 ;
CMD25 = https://comet.tech/getContentAsset/0f794b1a-cac3-4c6c-b08a-f7d6e05340cf/8453dbad-8de3-45d3-9ff0-774682f4f15b/Comet-CMD-2025_presentation_final.pdf (142 MB) ;
CMD23 = https://comet.tech/getContentAsset/403bbd24-d13e-461b-a082-acc60f427b5b/8453dbad-8de3-45d3-9ff0-774682f4f15b/Comet-CMD-2023_presentation_final.pdf

## 15 most important claims

| # | Tag | Claim | Value | Period | URL | Page |
|---|---|---|---|---|---|---|
| 1 | [F] | Net sales | CHF 457.0m (FY2024 restated 445.4m) | FY2025 (Jan-Dec 2025) | AR2025 | p76 |
| 2 | [F] | EBITDA and margin | CHF 46.3m, 10.1% (FY2024 restated 13.0%) | FY2025 | AR2025 | p76 |
| 3 | [F] | Net sales; EBITDA | CHF 239.8m; CHF 31.4m (13.1%), incl. CHF 4.5m one-time costs | H1 2026 (Jan-Jun 2026) | HY2026 | p10 |
| 4 | [F] | Q3 net sales; orders; book-to-bill | CHF 155.6m (+51.9%); CHF 275.6m; 1.77 | Q3 2026 (Jul-Sep 2026) | Q3TU | web text |
| 5 | [F] | FY2026 guidance raised | CHF 570-590m, reported EBITDA margin 17-19% incl. up to 3pp one-offs | FY2026 | Q3TU | web text |
| 6 | [F] | Largest customer (PCT, unnamed) | CHF 104.4m = 22.8% of group sales | FY2025 | AR2025 | p101 |
| 7 | [F] | Restatement: inventory items CHF 2.1m wrongly excluded from YE2024 write-downs; H1 2025 EBITDA 20.7m -> 23.0m | 2.1m | Dec 2024 / H1 2025 | HY2026 | p16 |
| 8 | [F] | Segment EBITDA by division | PCT 28.9m; IXS -4.0m; IXM 8.6m | H1 2026 | HY2026 | p22 |
| 9 | [C] | CA20 funnel: >60 evaluations, >25 qualifications, 5 orders (2023: 5 / 2 / 0) | 5 orders | as of 13 Nov 2025 | CMD25 | p63 |
| 10 | [C] | IXS "more than doubling the number of purchase orders for the CA20" | >2x | H1 2026 | HY2026 | p7 |
| 11 | [C] | CA20 Dose Manager switches off X-ray at a dose limit to protect "flash and DRAM"; no dose figure | - | page read 21 Nov 2026 | https://comet.tech/yxlon/products/ca20 | Efficiency / Dose Manager |
| 12 | [C] | 2028e divisional EBITDA margin targets: PCT 27-33%, IXS 5-9%, IXM 23-27% (group 22-27%) | 5-9% IXS | 2028e | CMD25 | p86 (read the rendered slide) |
| 13 | [C] | IXS: "focused actions, rather than large structural exits" | - | Mar 2026 | AR2025 | p25 |
| 14 | [F] | CHF 60m 2.00% bond issued Apr 2026, due 18 Apr 2031; CHF 100m RCF undrawn | 60m / 100m | 30 Jun 2026 | HY2026 | p26 |
| 15 | [C] | Comet's x-ray source ranks: #4 open micro focus, #3 open nano focus | #4 / #3 | 2023 | CMD23 | p49 |

Third-party counterweights worth checking: SEC Co. NF120 on Micron's HBM line since 2023 [S]
(https://www.asiae.co.kr/en/article/2026020408004004656); SFA in-fab HBM/TGV X-ray tool on an Excillum source [F]
(https://www.excillum.com/?p=10042); ZEISS NLX-100 shown as a demo tool in Yongin, 10 Jul 2026 [F]
(https://www.zeiss.com/semiconductor-manufacturing-technology/news-and-events/smt-press-releases/2026/innovation-center-korea.html).

## 5 inferences the conclusions lean on

1. **IXS lost money at EBITDA level in 5 of 9 half-years since 2022** [I] High. Inputs: segment EBITDA in half-year reports
   H1 2022-H1 2026 and annual reports FY2022-FY2025; H2 = FY minus H1 (calc/DV_halfyears.py). H1 2026 -4.0m, H1 2025 -7.5m.
2. **Guidance record FY2022-FY2025: 0 beats / 2 in-line / 6 misses vs initial guidance** [I] Medium (2022-2024 updates are
   newswire copies). Inputs: initial ranges (FY2022 570-610 / 21-23%; FY2023 440-480 / 13-15%; FY2024 440-480 / 15-17%; FY2025
   480-520 / 17-20%) vs results 586.4 / 20.3%, 397.5 / 11.3%, 445.4 / 13.6%, 457.0 / 10.1% (calc/A_guidance.py).
3. **H2 2025 EBITDA margin was 10.2%, not the 11.1% in the FY2025 deck** [I] High. Inputs: FY2025 EBITDA 46.3m on 457.0m; H1 2025
   restated EBITDA 23.0m on 227.2m (HY2026 p10); the deck used the un-restated 20.7m.
4. **At least ~11 cumulative CA20 purchase orders at 30 Jun 2026** [I] Low. Inputs: 5 orders at CMD 13 Nov 2025 (CMD25 p63);
   "more than doubled ... compared to YE25" (H1 2026 results deck, evidence row XS-060); assumes YE2025 count >= 5 and a cumulative base.
5. **CMD 2025 targets need 13.6-19.0% annual sales growth 2025-2028 and +10-15pp of margin** [I] High arithmetic. Inputs:
   FY2025 457.0m / 10.1%, LTM Jun 2026 margin 11.7%, target 670-770m / 22-27% (calc/DV_targets.py).

## 3 questions not settled

1. Is any CA20 running in high-volume production at a memory maker, foundry or OSAT, and how do Comet's orders split between lab
   (failure analysis) and fab units? No customer-side source was found; Comet gives no split.
2. What X-ray dose does a CA20 (or any rival) deliver per HBM/DRAM site, and what limit does the Dose Manager apply by default?
   No maker publishes a figure.
3. Which etch/deposition OEM is PCT's 22.8% customer, and has Synertia reached its ~10% RF-generator share target against
   Advanced Energy and MKS? Neither is disclosed; no third-party share data was retrieved.
