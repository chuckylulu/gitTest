# Weather and climate simulation worldwide (as of 12 November 2026)

## Summary for the report writer

- **In operation.** Every operational learned model starts from a physics analysis or is blended with physics:
  - ECMWF AIFS Single (25 Feb 2025) and AIFS ENS (1 Jul 2025; v2 on 12 May 2026)
  - NOAA AIGFS, AIGEFS and HGEFS (17 Dec 2025, GraphCast-based)
  - DWD AICON (official 2 Mar 2026) and Canada's GEML hybrid (May 2026)
  - NHC's real-time use of Google DeepMind guidance (since 2025); Israel's CorrDiff downscaling; Taiwan's hybrid typhoon tracks
  - China reports Fengqing deployed.

  No learned model is primary at the Met Office, Météo-France, JMA, KMA or IMD.
- **Skill.** Learned models beat physics on large-scale and track scores. In NHC's 2025 data, Google's 72-h Atlantic track error was 66.5 n mi against 81.4 for the official forecast; at 120 h in the eastern Pacific it was 87.3 against 111.9. They lose on intensity, peak winds and fine-scale rain. ECMWF also documents a −29 kt cyclone-intensity bias.
- **Prior test.** "Accuracy last" fails: speed and accuracy came together, and large ensembles followed. "Proposer certified by a solver" holds in altered form. Physics data assimilation, reanalysis and human consensus do the certifying; forecasting from observations alone is still experimental.
- **Builders.** Google leads on verified skill and gates its real-time data. NVIDIA's open models allow commercial use, while Pangu and FuXi are non-commercial. Open stacks commoditise models: Anemoi/AIFS, and ECMWF's 9 km data (free since 20 Oct 2026, delayed two hours).
- **GPU ports.** Only MeteoSwiss runs a physics model operationally on GPUs (ICON, since 2024). IFS on GPU is still in ECMWF's procurement benchmark. arXiv 2608.13122 is real but narrow: 162 of 387 regions, one node, single precision, one 30-minute case, 5.1×.
- **Commercial.** Durable positions rest on four things:
  - proprietary observations (Vaisala, Spire, WindBorne, Tomorrow.io, Weathernews)
  - accepted catastrophe models (Verisk, Moody's, KCC); all Florida-accepted models are conventional
  - licensed domestic forecasting (Japan's law of 29 May 2026)
  - embedded workflow.

  Firms repackaging open models on public inputs (Kweather) are the most exposed.
- **Weathernews.** FY5/2026 sales ¥24.5bn (+4.1%); operating margin 21.4%; 96% of sales recurring. It has ¥18.8bn cash and no debt. AI saves 15,300 staff-hours a month. Japan is 75% of sales.
- **2026 deals.** Tomorrow.io $210m Series F; WindBorne $37m at $250m post-money; Vaisala buying Atmo ($70m plus up to $60m).
- **Valuation (11–12 Nov 2026).** Weathernews ¥1,854, P/E ~22×, P/S ~3.3×. Vaisala €64.80, P/E 31×, P/S 3.8×. Spire $9.97, loss-making, P/S 5.8×. Verisk $205.98, P/E 31×, P/S 8.3×.

## 1. Operational status of learned models at public agencies

### Takeaway
Seven public centres run learned models in operations, and CMA reports deployment. Every one is initialised from a physics analysis, blended with physics, or filtered by forecasters. Verified gains are large-scale (tracks, synoptic patterns). The deficits are intensity, extremes and fine-scale rain.

### Cited Findings
- **ECMWF.** AIFS Single entered operations on 25 Feb 2025 at 28 km, against 9 km for IFS. ECMWF claims "up to 20%" gains (including cyclone tracks), ~1,000× less energy, and the same initial conditions as IFS — [ECMWF](https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ai-forecasts-become-operational). AIFS ENS followed on 1 Jul 2025: 51 members at 31 km, >10× faster, and it "relies on physics-based data assimilation". ECMWF says IFS "remains indispensable" for high-resolution and coupled processes — [ECMWF](https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ensemble-ai-forecasts-become-operational).
- **ECMWF v2.** AIFS v2 went live with IFS Cycle 50r1 on 12 May 2026. It is pre-trained on ERA5 (1979–2022) and fine-tuned on 2018–2024 analyses. It added the first data-driven wave forecast (wave height ~10% better than the physics wave model) and a snow-cover forecast. Known issues are Arctic 2 m temperature degradation and longer-lead losses — [Confluence AIFS Single v2](https://confluence.ecmwf.int/display/FCST/Implementation+of+AIFS+Single+v2); [AIFS ENS v2](https://confluence.ecmwf.int/display/FCST/Implementation+of+AIFS+ENS+v2).
- **ECMWF and outside models.** ECMWF stopped real-time runs of FourCastNet, Pangu, GraphCast and Aurora with the 50r1 upgrade. The new initial conditions degraded the fine-tuned models: "the fine-tuning strategy can be partially undermined" — [ECMWF, 11 May 2026](https://www.ecmwf.int/en/about/media-centre/aifs-blog/2026/farewell-external-ai-models).
- **NOAA.** Three models went operational on 17 Dec 2025. AIGFS uses 0.3% of GFS compute and runs 16 days in ~40 min. AIGEFS has 31 members, uses 9% of GEFS compute and adds 18–24 h of skill. HGEFS is a 62-member hybrid. All derive from GraphCast fine-tuned on GDAS analyses. AIGFS v1.0 degrades cyclone intensity — [NOAA](https://www.noaa.gov/news-release/noaa-deploys-new-generation-of-ai-driven-global-weather-models). On 27 Jul 2026 NOAA named Google DeepMind "the framework" for AIGFS — [NOAA](https://www.noaa.gov/news-release/noaas-use-of-cloud-infrastructure-grows-to-include-weather-prediction-models).
- **NHC, 2025 report (30 Mar 2026).** 2025 was "the first time that NHC incorporated AI-based models into real-time operations".

  | Measure | Lead times | Google ensemble mean (GDMI) | Official forecast (OFCL) |
  |---|---|---|---|
  | Atlantic track error (n mi) | 12 / 24 / 48 / 72 / 120 h | 19.6 / 26.4 / 41.4 / 66.5 / 173.1 | 20.4 / 31.1 / 49.2 / 81.4 / 168.5 |
  | Eastern Pacific track error (n mi) | 72 / 120 h | 45.3 / 87.3 | 52.6 / 111.9 |
  | Atlantic intensity error (kt) | 48 h | 12.3 | 13.1 |

  OFCL beat all models on Atlantic intensity at 12 h and 96 h, and beat GDMI on eastern Pacific intensity at every lead time. The ECMWF IFS (EMXI) had "no forecast skill" on Atlantic intensity — [NHC](https://www.nhc.noaa.gov/verification/pdfs/Verification_2025.pdf). NHC: "the official forecast is the most skillful and consistent" — [weather.gov](https://www.weather.gov/news/261102-AI-Hurricane-Forecasting).
- **NHC, 2026 season (preliminary).** Unofficial verification by J. Franklin to early September puts DeepMind ahead of all public track guidance and OFCL, by up to ~30% at day 5 — [Local10, 10 Sep 2026](https://www.local10.com/weather/hurricane/2026/09/10/the-ai-hurricane-model-that-continues-to-blow-away-the-competition/) (snippet only). For Hurricane Isaias (Cat 2, Florida Panhandle, Oct 2026) it was best on track but not on intensity. NHC Director Brennan: "we take that consensus approach" — [GPB/NPR, 26 Oct 2026](https://www.gpb.org/news/2026/10/26/how-ai-transforming-hurricane-forecasts).
- **DWD.** AICON is a 13 km graph neural network trained on the ICON-DREAM reanalysis and initialised from the ICON analysis. It entered 24/7 operation on 2 Sep 2025 and official use on 2 Mar 2026. It is open data and "part of the basis for DWD's weather warnings". It is better on most surface variables early in the forecast. It is worse on pressure after ~2 days and on geopotential, overestimates tropical ocean rain by up to 50%, and underestimates cyclone winds more than ICON does — [arXiv 2608.24651](https://arxiv.org/html/2608.24651).
- **ECCC (Canada).** The hybrid went operational on 27 May 2026: the physics model is nudged toward GEML (GraphCast-based) because AI models "forecast only a limited number of variables" and smooth details — [ECCC](https://www.canada.ca/en/environment-climate-change/news/2026/05/environment-and-climate-change-canada-launches-ai-weather-model-to-strengthen-forecasting-for-severe-weather.html).
- **Met Office.** FastNet is "in development"; AI "does not replace traditional science" — [Met Office, 4 Feb 2026](https://www.metoffice.gov.uk/blog/2026/how-does-the-met-office-use-ai). FastNet v1.1 is an experimental release under CC BY 4.0 — [Hugging Face](https://huggingface.co/MetOffice/FastNet-global).
- **JMA.** The plan of 26 Jun 2026 runs AI and physics as "両輪" (twin wheels). It targets a global AI model for typhoon tracks by ~2030, a high-resolution AI model by ~2035, and later 2-week AI ensembles and AI data assimilation. It puts GPU porting first and says "計算資源確保が重要" (securing compute is essential) — [JMA](https://www.jma.go.jp/jma/press/2606/26a/nwp_strategic_plan_2030_260626_1summary.pdf). Earlier, JMA tested FourCastNetv2, Pangu and GraphCast — [JMA NPD](https://www.jma.go.jp/jma/kishou/books/npdc/2024/npdc_report_2024_S.pdf). No operational JMA AI model was found.
- **KMA.** Since April 2026 KMA has run its own KIM model alone, after six years in parallel with the UM. It has 208 GPUs, an AI foundation model planned for 2026–2030, and an AI wind reanalysis since 10 Feb 2026 — [Daum/News1, 28 May 2026](https://v.daum.net/v/20260528142448171).
- **CMA.** CMA upgraded Fengqing, Fenglei and Fengshun and released the open "Fengyuan" base model (with Shanghai AI Lab) on 19 Dec 2025, without skill numbers — [Xinhua](https://www.news.cn/tech/20251219/99223b9d028a46faa3dda987a5f607b9/c.html). Fengqing is "业务化部署" (operationally deployed) — [People's Daily](https://paper.people.com.cn/rmrb/pc/content/202512/06/content_30118755.html) (search summary).
- **IMD.** BharatFS is a 6 km physics model, operational since May 2025. The first AI product, a 4-week monsoon-advance forecast, launched on 12 May 2026, with a 1 km Uttar Pradesh rain pilot — [Drishti IAS, 14 May 2026](https://www.drishtiias.com/daily-updates/daily-news-analysis/imds-new-ai-driven-weather-forecasting-systems/print_manually) (secondary).
- **CWA (Taiwan).** AI has been used in typhoon forecasting since 2024, inside a hybrid process where forecasters set the track. Google's model was best for Typhoon Bavi (Jul 2026). Rain is weak (25 km against 2–3 km needed). Downscaling is being built with NVIDIA, and GPUs were added to the 6th-generation supercomputer — [PTS, 22 Jul 2026](https://news.pts.org.tw/article/818850).
- **IMS (Israel).** IMS runs CorrDiff operationally to emulate its 2.5 km ICON; its director claims "90% reduction in compute time" (vendor-published) — [NVIDIA, 26 Jan 2026](https://blogs.nvidia.com/blog/nvidia-earth-2-open-models/).

### Inferences
- "Operational" means 24/7 production. It does not mean the learned model is the official forecast, which remains a human product built from blends.
- Centres with their own data assimilation and reanalysis (ECMWF, NOAA, DWD) moved first. Centres short of compute or reanalysis (JMA, KMA, IMD) lag.

### Gaps
- There is no independent multi-year verification for the CMA, CWA or IMD AI systems. Météo-France status was not read first-hand; only prototypes (AROME-IA) were found.

## 2. Does weather contradict the background view?

### Takeaway
Partly. Speed and headline accuracy arrived together, followed by scale (large ensembles), so a fixed speed→scale→accuracy order is contradicted. But trust still rests on physics. Learned models are initialised and trained by physics data assimilation and reanalysis, are checked by human consensus, and fail on extremes, small scales and unseen climates.

### Cited Findings
- **Against the prior.** GenCast beat ECMWF ENS on 97.4% of 1,320 targets — [arXiv 2312.15796](https://arxiv.org/abs/2312.15796). NHC's independent data show GDMI ahead of the official track forecast (see §1). ECMWF says ML is "routinely outperforming the IFS" on cyclone tracks and synoptic evolution — [ECMWF, 27 Mar 2026](https://www.ecmwf.int/en/about/media-centre/aifs-blog/2026/severe-storms-machine-learning). Scale came with cheapness: AIGEFS runs 31 members at 9% of GEFS compute, and NHC expects "thousands of possible forecast outcomes" — [NOAA](https://www.noaa.gov/news-release/noaa-deploys-new-generation-of-ai-driven-global-weather-models); [weather.gov](https://www.weather.gov/news/261102-AI-Hurricane-Forecasting).
- **Extremes.** ML forecasts underestimated peak winds in Storms Amy and Éowyn; "traditional numerical weather prediction, particularly the IFS, remains essential" — [ECMWF, 27 Mar 2026](https://www.ecmwf.int/en/about/media-centre/aifs-blog/2026/severe-storms-machine-learning). AIFS cyclone-intensity bias was −29 kt (~70 kt error in rapid intensification); a second ML corrector cut these to −2 kt and ~23 kt on 2025 data, "statistically indistinguishable" from Google's FNV3 — [ECMWF, 3 Aug 2026](https://www.ecmwf.int/en/about/media-centre/aifs-blog/2026/ai-tropical-cyclone-forecasts).
- **Outside the training data.** A FourCastNet trained without Category 3–5 storms "cannot accurately forecast Category 5" storms — [arXiv 2410.14932 (PNAS)](https://arxiv.org/abs/2410.14932). Hybrid-ML climate emulators "degrade significantly" under realistic shifts (Oxford preprint, May 2026) — [arXiv 2605.22248](https://arxiv.org/html/2605.22248). ClimaX precipitation errors rise by up to 8.44% under extreme forcing (preprint, Mar 2026) — [arXiv 2603.23043](https://arxiv.org/abs/2603.23043).
- **Dependence on physics.** ERA5 training data come from IFS Cycle 41r2. After 50r1, "biases are changing significantly, more than in typical IFS model upgrades", with ~30% worse Arctic 2 m temperature RMSE — [ECMWF, 12 May 2026](https://www.ecmwf.int/en/about/media-centre/aifs-blog/2026/adapting-aifs-50r1).
- **Possible break.** ECMWF's AI-DOP forecasts "without relying on a real-time atmospheric analysis" but is "still experimental". Losing microwave sounders causes "substantially larger errors" than in 4D-Var — [ECMWF, 3 Nov 2026](https://www.ecmwf.int/en/about/media-centre/aifs-blog/2026/observations-forecasts-bringing-ai-dop-real-time). Aardvark claims to beat an NWP baseline from raw observations (preprint) — [arXiv 2404.00411](https://arxiv.org/abs/2404.00411).

### Inferences
- A better description for weather: speed and large-scale accuracy came first, ensemble scale second, extremes and fine scales last.
- The "solver" that certifies is the data-assimilation chain plus forecasters. Hybrids put the learned model inside physics: ECCC nudges physics toward a learned model, and ECMWF corrects one learned model with another.
- No agency uses a learned model for official climate projections.

### Gaps
- No 2026 peer-reviewed multi-model test of physical consistency (energy or mass conservation) was found.

## 3. Model builders: licensing, openness, commercial use

### Takeaway
Google DeepMind leads on independently verified skill and sells access through Google Cloud. NVIDIA gives models away to sell hardware. Microsoft, Huawei and Fudan restrict commercial use. Public centres build on open code.

### Cited Findings
- **Google.** GraphCast code is Apache 2.0, with other materials under CC BY 4.0. The models are "not … endorsed by any government meteorological agency", and the WeatherNext 2 and Cyclones weights sit in a Google Cloud bucket — [GitHub](https://github.com/google-deepmind/graphcast). WeatherNext 2 (17 Nov 2025) is in BigQuery, Earth Engine, Vertex AI, Search and the Maps API. It beats its predecessor on 99.9% of variables (company claim, unconfirmed) — [Google](https://blog.google/technology/google-deepmind/weathernext-2/). WeatherNext 3 (3 Sep 2026) is hourly, ingests satellite data, has 64 members and claims "up to 50%" better rain (company claim). Data more than 1 h old is CC BY 4.0; real-time access needs an application; the model is not open — [XenoSpectrum (secondary)](https://xenospectrum.com/weathernext-3-hourly-satellite-forecast/). Cyclones code and weights were released in Aug 2026 — [RuntimeWire](https://runtimewire.com/article/google-deepmind-weathernext-cyclone-model-open-source).
- **NVIDIA.** Earth-2 (26 Jan 2026) comprises Medium Range (Atlas), Nowcasting (StormScope) and HealDA data assimilation, plus CorrDiff and FourCastNet3. Users: IMS (operational) and Brightband (daily runs); TWC and NWS are evaluating; also TotalEnergies, Eni, GCL, SPP/Hitachi, AXA and S&P Global Energy — [NVIDIA](https://blogs.nvidia.com/blog/nvidia-earth-2-open-models/). Commercial use is allowed — [SiliconANGLE](https://siliconangle.com/2026/01/26/nvidia-launches-earth-2-open-ai-weather-forecast-models-tools/). DTN integrates Earth-2 on AWS (22 Sep 2025) — [BusinessWire](https://www.businesswire.com/news/home/20250922015272/en/DTN-Advances-Real-Time-Weather-Intelligence-with-NVIDIA-Earth-2-on-AWS) (search summary; page blocked).
- **Others.** Microsoft's Aurora is "not designed or evaluated for direct operational decision-making"; commercial use is by request — [GitHub](https://github.com/microsoft/aurora). Huawei's Pangu weights are BY-NC-SA: "commercial use … is forbidden" — [GitHub](https://github.com/198808xc/Pangu-Weather). Fudan's FuXi weights are BY-NC-SA per a third-party README — [ai-models-fuxi](https://awesome.ecosyste.ms/projects/github.com%2Ftpys%2Fai-models-fuxi). FuXi-S2S is "research purposes only" — [Zenodo](https://zenodo.org/records/15718402).
- **Public stacks.** DWD moved to ECMWF's Anemoi in June 2024 — [DWD slides](https://events.ecmwf.int/event/464/contributions/5252/attachments/3223/5514/HPC-WS_Prill.pdf). AIFS v2 weights are on Hugging Face — [ECMWF](https://www.ecmwf.int/en/about/media-centre/aifs-blog/2026/adapting-aifs-50r1).

### Inferences
- Model weights are becoming free. The scarce inputs are analyses and observations (real-time, proprietary) and distribution channels (Google Search/Maps).

### Gaps
- FengWu licensing was not found. Official Fudan licence pages were not checked.

## 4. GPU ports of physical models

### Takeaway
Only MeteoSwiss runs a physics model operationally on GPUs. IFS has a GPU build awaiting procurement. E3SM/SCREAM is a research milestone. AI-assisted ports (CReSS, NICAM, FESOM2) are real but partial and not in production.

### Cited Findings
- **ICON.** "MeteoSwiss [is] the first national weather service to run ICON operationally on GPUs" (A100s on CSCS Alps; ICON replaced COSMO on 28 May 2024). It gains 5.5× socket-to-socket against CPU. Mixed precision in the dynamical core was "validated against a double-precision version"; data assimilation stays on CPU. DWD configurations are "supported and tested", but not run operationally on GPUs — [GMD 19:755, 23 Jan 2026](https://gmd.copernicus.org/articles/19/755/2026/). A 2026 preprint reports 1.9–5.8× on GH200 (snippet only) — [EGUsphere](https://egusphere.copernicus.org/preprints/2026/egusphere-2026-2531/egusphere-2026-2531.pdf).
- **IFS.** IFS was adapted with Loki source-to-source "recipes" and Field-API. "Initial, non-optimised GPU performance is already competitive with the highly optimised CPU performance." A GPU-enabled IFS is "in its current HPC procurement benchmark", and GPU modes are "planned to enter the mainline code in IFS Cycle 50r2" — [ECMWF Newsletter 186, Winter 2025/26](https://www.ecmwf.int/sites/default/files/elibrary/012026/81710-gpu-adaptation-of-the-ifs-for-eurohpc-machines.pdf). Tender ITT 2025/380 closed around 18 Feb 2026; no award was found — [tender listing](https://www.developmentaid.org/tenders/view/1557016/ecmwfitt2025380-procurement-of-a-high-performance-computing-facility).
- **E3SM/SCREAM.** SCREAM ran at 3.25 km globally at 1.26 simulated years per day on Frontier's AMD GPUs (2023) — [SC23](https://sc23.supercomputing.org/proceedings/tech_paper/tech_paper_pages/gbv102.html). No 2026 update was found.
- **WRF, MPAS and AceCAST.** WRF 4.8.0 (8 Jun 2026) notes do not mention GPUs — [GitHub](https://github.com/wrf-model/WRF/releases). MPAS 8.4.0 added OpenACC dynamical-core data residency and GPU halo exchange — [GitHub](https://github.com/MPAS-Dev/MPAS-Model/releases). TempoQuest's licensed GPU WRF, AceCAST, supports ARW only (based on WRF v4.4.2) and claims ~9× per node (vendor claim) — [AceCAST docs](https://acecast-docs.readthedocs.io/en/latest/FAQS.html); [NVIDIA blog](https://developer.nvidia.com/blog/microsoft-and-tempoquest-accelerate-wind-energy-forecasts-with-acecast).
- **arXiv 2608.13122 (Nagoya/Tokyo, 13 Aug 2026).** CReSS is ~260k lines of Fortran with 387 OpenMP regions. The 162 regions exercised by one typhoon case (2 km, 899×899×128 grid, 30 simulated minutes) were ported with OpenACC by Claude Code (Opus 4.5–4.6). Validation used element-wise 1e-5 relative tolerance in single precision, plus application checks at 1e-4. Time per step fell from 9.51 s on a 72-thread Grace CPU to 1.88 s on one GH200 GPU (5.1×), using Unified Memory. Five kernels differed numerically and were accepted. Effort was ~100 h of GPU-node time over ~3 months. The authors' words: "a scenario-specific validated GPU port, not a complete GPU port" — [arXiv](https://arxiv.org/html/2608.13122). The claim of "162 routines, 5.1× as a whole application" therefore holds only for that scenario on one node.
- **NICAM and FESOM2.** NICAM's port to Kokkos with Claude Code ran 1.71× (GH200) and 1.54× (MI300A) faster than Fortran/OpenACC, over 23 days at ~$5.6k in API tokens; it is not in production — [arXiv 2610.41313](https://arxiv.org/html/2610.41313). The FESOM2 ocean port (Claude Opus 4.7) gives a GPU node 1.6–3.7× a CPU node and is "not yet" a production replacement — [arXiv 2606.11356](https://arxiv.org/html/2606.11356).

### Inferences
- GPU ports move weather toward mixed and single precision (ICON, CReSS), which weakens the case for double-precision hardware. AI agents shorten porting but not validation.

### Gaps
- The ECMWF HPC award, DWD's GPU plans, SCREAM on El Capitan and AceCAST's 2026 status were not verified.

## 5. Commercial companies by region

### Takeaway
Leaders own observations (Vaisala, Spire, WindBorne, Tomorrow.io), regulated judges (Verisk, Moody's, KCC) or licensed national channels (Weathernews, Kweather). Coverage of private finances is thin everywhere, and thinnest for China, Korea, Taiwan and India.

### Cited Findings
- **North America: incumbents and data firms.**
  - The Weather Company is owned by Francisco Partners (deal announced in 2023) — [TechCrunch](https://techcrunch.com/2023/08/22/ibm-sells-the-weather-company-assets-to-francisco-partners). It uses AI super-resolution and an AI ensemble emulator due "later this calendar year", with forecasters "in parallel with AI". Its claim that AI plus humans beats either alone has no metrics given (company claim) — [TWC blog, 30 Jul 2026](https://www.weathercompany.com/blog/how-ai-weather-prediction-is-making-your-forecast-better/).
  - AccuWeather bought the TOA lightning network (13 Jan 2025) — [PR Newswire](https://prnewswire.com/news-releases/accuweather-acquires-toa-lightning-detection-network-and-technology-to-create-advanced-global-lightning-detection-network-302348450.html). It launched a ChatGPT app in March 2026 (search summary) — [AccuWeather press](https://www.accuweather.com/en/press/35738).
  - Spire is listed; see §6.
- **North America: venture-backed.**
  - Tomorrow.io raised $175m on 3 Feb 2026 (led by Stonecourt and HarbourVest; ~250 customers) — [Via Satellite](https://www.satellitetoday.com/finance/2026/02/03/tomorrow-io-raises-175m-to-build-out-deepsky-weather-constellation/). A $35m extension (Pitango, Harel) on 18 May 2026 brought the Series F to $210m. It has a Tel Aviv R&D centre and plans the DeepSky constellation — [Globes](https://en.globes.co.il/en/article-1001543247). A valuation above $1bn is reported only by secondary sources.
  - WindBorne raised a $37m Series B on 5 Aug 2026 at $250m post-money (Khosla, Galvanize). It flies ~600 balloons; NWS buys its data, and the Air Force and Navy fund research. Its claim that its data improve accuracy is unverified — [TechCrunch](https://techcrunch.com/2026/08/05/ai-makes-weather-prediction-better-can-windborne-make-it-lucrative/).
  - Atmo is being bought by Vaisala (§6). Brightband runs NVIDIA's Medium Range model daily ([NVIDIA](https://blogs.nvidia.com/blog/nvidia-earth-2-open-models/)); its $10m Series A (2024) is reported only by an aggregator.
  - Jupiter Intelligence's last round found was a $54m Series C in Oct 2021 (older) — [Coverager](https://www.coverager.com/?p=130668).
- **Europe.** Vaisala/Xweather (§6). Meteomatics raised a $22m Series C (29 Jan 2025, Armira) — [Meteomatics](https://www.meteomatics.com/en/news/meteomatics-series-c-funding-22-million-dollars/). Skyfora (Finland) raised €6.5m (Jun 2026) — [IO+](https://ioplus.nl/en/posts/ai-forecasting-startup-skyfora-raises-65-million-).
- **Japan.** Weathernews (§6).
- **South Korea.** Kweather (KOSDAQ 068100) calls itself the "국내 최대 민간 기상사업자" (Korea's largest private weather firm) — [Kharn](https://www.kharn.kr/news/article.html?no=31819). Q1 2026 revenue was KRW 3.9bn (+16.4%) with operating profit of ~KRW 0.2bn, driven by air-measurement products — [Dealsite, 14 May 2026](https://dealsite.co.kr/articles/161828). On 18 Sep 2026 it launched 10 AI products on NVIDIA FourCastNet3, Atlas, CorrDiff and StormScope, using GFS and KIM as inputs — [Dealsite](https://dealsite.co.kr/articles/169288).
- **China.** Moji (墨迹天气) has pivoted to business customers (energy, rail, aviation) and claims >150m monthly active users (company claim) — [CTDSB, Oct 2026](https://www.ctdsb.net/s522_202610/1638376.html). Some 16,000 firms list meteorology in their scope; ~3,000 operate and <400 have scale (2024 survey) — [Huxiu, Jul 2026](https://m.huxiu.com/article/4875932.html).
- **India.** Skymet's last disclosed rounds were a 2017 Series C ($8–10m, InsuResilience) and INR 12 crore of debt in 2021 (older) — [Business Standard](https://www.business-standard.com/article/companies/skymet-raises-8-10-mn-to-widen-weather-station-network-117121801352_1.html); [Entrepreneur](https://www.entrepreneur.com/en-in/finance/weather-startup-skymet-weather-raises-inr-12-cr-debt-funding/378618).
- **Israel and Taiwan.** Tomorrow.io's R&D centre is in Tel Aviv — [Globes](https://en.globes.co.il/en/article-1001543247). I found no Taiwanese private weather firm (gap).

### Inferences
- Kweather is the clearest "gap filler": its products are NVIDIA models run on public GFS and KIM inputs, which any firm with GPUs can replicate.
- Vaisala's price for Atmo is ~35× Atmo's 2025 sales and ~12× its contracted 2026 revenue (computed from the Vaisala figures), a sign that learned-model teams are scarce.

### Gaps
- No 2025–26 data were found on funding or valuation for Salient, Excarta, Zeus AI or Climavision, on StormGeo's or DTN's owners and finances, or on revenue for TWC or AccuWeather. The search budget ran out before targeted searches.

## 6. Quality tests for the strongest commercial companies (evidence only)

### Takeaway
Weathernews and Vaisala pass on position and finances. Verisk owns a regulatory judge. Spire owns hard observations but has weak finances. None has outside proof of a forecast-skill lead.

### Cited Findings
- **Weathernews (TSE 4825).** FY to 31 May 2026, from the earnings release (tanshin) of 9 Jul 2026 — [tanshin PDF](https://assets.finboard.net/tdnet-filings/20260708589783.pdf); [TDnet](https://www2.jpx.co.jp/disc/48250/081220260708589783_tse-acedjpsm-48250-20260709348250-ixbrl.htm):
  - **Results.** Sales ¥24,479m (+4.1%); operating profit ¥5,244m (+16.1%, 21.4% margin); net profit ¥3,806m; ROE 16.8%. Gross margin was 47.3%, and SG&A was flat at ¥6,342m.
  - **Sales mix.** Recurring ("stock") sales ¥23,554m (96%); one-off sales −8.9%. By domain: Sea ¥6,324m (+3.0%), Sky ¥1,523m (+15.5%), Land ¥7,111m (+5.4%), Internet ¥8,594m (+3.8%). By region: Japan ¥18,443m (75%), Asia ¥3,272m, Europe ¥2,512m (+11.0%), Americas ¥250m (−35.7%).
  - **Balance sheet.** Equity ratio 84.5%. Cash ¥18,825m. Operating cash flow ¥3,638m, against investing outflow of only ¥138m.
  - **AI and costs.** AI has cut "15,300時間/月" (staff-hours a month) and lowered personnel costs, while telecom and weather-data costs rose. A weather-radar asset was impaired after a "利用計画の見直し" (review of its usage plan).
  - **Targets.** Mid-term Vision 2026 (Jul 2026) aims to be an "AI Fusion Company" with gross margin ≥60% and ≥10% sales growth within 3 years. FY5/2027 guidance: sales ¥25.8bn (+5.4%), operating profit ¥5.4bn (+3.0%).
  - **Q1 FY5/2027 (Jun–Aug 2026)** per StockAnalysis (secondary): sales ¥6,338m (+5.5%), gross margin 54.8%, operating profit ¥893m (−2.2%) — [StockAnalysis](https://stockanalysis.com/quote/tyo/4825/financials/?p=quarterly).
- **Weathernews products and claims.**
  - AI-Nowcast (15 Oct 2026) is trained on its own radar, stations and user "Weather Reports". It claims +8 to +10.1 points capture of ≥10 mm/h rain and 1.3–1.6× threat score, self-verified (company claim, unconfirmed) — [WNI](https://jp.weathernews.com/news/57759/).
  - WxTech Data API has been sold abroad since 26 Aug 2026; pricing is undisclosed. The global API blends national models with its own AI. The "No.1 accuracy, 4 years" claim rests on a Tokyo Shoko Research survey (company-cited) — [WNI](https://jp.weathernews.com/news/57281/).
  - Its observation assets include >3,300 Sorakame cameras and the Soratena Pro sensor for Asia — [WNI news](https://jp.weathernews.com/news/).
- **Vaisala (Nasdaq Helsinki VAIAS).** Q3 2026 report of 27 Oct 2026 — [report](https://www.vaisala.com/sites/default/files/documents/Vaisala%20Interim%20Report%20January-September%202026.pdf):
  - **Group.** Orders €164.6m (+38%); sales €162.9m (+6%); EBITA 24.9%, a record helped by one-off US tariff refunds. Net cash €20m.
  - **Outlook.** FY2026 sales €610–630m and EBITA €110–120m (raised 12 Oct).
  - **Industrial Measurements** sales were +28%, driven by "data center, semiconductor" demand.
  - **Weather, Energy and Environment** sales fell 11%, while orders rose 53% (including a €25m Indonesian airports order).
  - **Xweather.** ARR €60.9m (+9%, including volume-based contracts). Q3 sales €15.7m, gross margin 79%, EBITA only 9.4% (6.2% for nine months), and R&D €14.8m over nine months (32% of sales). It offers APIs "including MCP for AI assisted workflows".
  - **Atmo.** Agreed in Jun 2026 for $70m plus up to $60m earn-out (2026–28). Atmo's 2025 sales were $2m with >$6m contracted for 2026; closing is expected in Q4.
- **Spire (NYSE SPIR).** Q3 2026 — [Spire](https://ir.spire.com/news-events/press-releases/detail/316/spire-global-announces-third-quarter-2026-results):
  - **Q3 results.** Revenue $18.0m (+42%; +77% excluding maritime), against a $20.6m consensus — [StockAnalysis](https://stockanalysis.com/stocks/spir/). Gross margin 46%; operating loss $20.2m; adjusted EBITDA −$8.6m.
  - **Balance sheet.** Cash $78.0m, no debt; remaining performance obligations $175.4m.
  - **Guidance.** FY2026 revenue $75–80m; FY2027 $96–106m.
  - **Contracts.** NOAA radio-occultation task order of $33.2m (to ~$66m with options) and a $28m hyperspectral microwave contract (target: operational by 2030).
  - **Risks.** A July 2025 SEC subpoena, reliance on government appropriations, trailing free cash flow of −$93m, and an Altman Z of −1.08 — [StockAnalysis](https://stockanalysis.com/stocks/spir/statistics/).
- **Verisk (Nasdaq VRSK).** Q3 revenue $809m, citing "the resilience of our subscription-based business model". It kept FY2026 revenue guidance of $3.19–3.24bn and cited "lighter weather" softness. Trailing gross margin 70%, operating margin 45%, FCF margin 34.6%, net debt $4.08bn — [StockAnalysis](https://stockanalysis.com/stocks/vrsk/); [stats](https://stockanalysis.com/stocks/vrsk/statistics/). Its hurricane model is Florida-accepted (§7).

### Inferences: five tests
- **(a) Position.**
  - Weathernews: workflow, its own observations and a licensed channel.
  - Vaisala: a physical constraint (sensors in official networks and airports).
  - Verisk: owns a judge.
  - Spire: hard observations sold to a few governments.
  - Kweather (§5): a gap filler.
- **(b) Lead.** No company has outside verification of forecast skill; WNI's and TWC's accuracy claims are surveys or company-made. NOAA's repeated awards are the only outside evidence of a data lead (Spire).
- **(c) Revenue model.** Recurring revenue at Weathernews (96%), Xweather (ARR, volume-based) and Verisk (subscriptions). Vaisala is mostly product and project sales. Spire runs government data contracts.
- **(d) Financial strength.** Weathernews and Vaisala are strong, with net cash. Verisk is cash-rich but leveraged. Spire is cash-burning.
- **(e) Resilience to 2030.**
  - Steady (55%): Weathernews compounds at a 20%+ margin; Vaisala rides data-centre build-outs.
  - 2028 pause (25%): it hits Vaisala's data-centre and semiconductor orders, and Spire most (it needs capital). Weathernews is least exposed, since its demand is weather-driven.
  - Acceleration (20%): repackagers erode (Weathernews' Internet domain and APIs, Kweather), while observations and regulated judges gain value.
  - Cross-border: Japan's 2026 law shields Weathernews; Spire depends on US and EU agencies.
- **Weathernews must** grow outside Japan (Americas fell 36%) and lift gross margin from 47–55% to 60% without losing its forecasters' edge.
- **Vaisala must** scale Xweather margins beyond single digits.
- **Spire must** reach positive EBITDA in 2027 as guided.

### Inferences: six transitions, said versus done
1. **Seats to usage or result pricing.** WNI says it is moving to SaaS; done so far is a 96% recurring base, but no usage pricing is disclosed. Xweather has done it: its ARR includes volume-based charges. Verisk sells subscriptions. Spire sells data contracts.
2. **CPUs to GPUs.** WNI said it would invest in "AI化" (AI conversion); its capex was tiny (¥207m for fixed and intangible assets in FY5/2026). Vaisala bought deep-learning capability (Atmo). Kweather built NVIDIA infrastructure.
3. **Agent-driven tools.** Xweather states an MCP offering. WNI's WxTech API makes no agent mention. Verisk announced AI-platform integrations including Claude (28 Oct 2026, StockAnalysis news).
4. **Open models.** Kweather and DTN have adopted NVIDIA's; WNI's global API blends national models. Must go right: owners must add data that open models lack.
5. **Learned models beside physics.** WNI's AI-Nowcast is in its app, and Xweather offers "AI-driven forecasts". No outside verification exists for either.
6. **Regulator and customer acceptance.** WNI holds a licence and backed the 2026 law. Spire's data enter NOAA operations. Verisk is accepted under Florida's new AI-disclosure standards.

### Gaps
- No market-share data for ship routing or aviation weather. No Verisk segment data on catastrophe models. Weathernews Q1 FY5/2027 figures were not taken from the primary filing.

## 7. Catastrophe and climate-risk models as regulated judges

### Takeaway
Regulators certify loss models through slow, documented review cycles. Every currently accepted Florida model is conventional, and the 2025 standards make AI use auditable rather than banning it.

### Cited Findings
- **Florida-accepted hurricane models.** As revised on 2 Oct 2026, the models accepted under the 2023 standards (all expiring 1 Nov 2027) are Cotality, FIU 8.3, Impact Forecasting 3.0, KCC 5.0, Moody's 25.0 (re-accepted with each platform release, most recently 2 Oct 2026) and Verisk 3.0.0. The flood models are from FIU, Impact Forecasting and KCC — [FCHLPM](https://fchlpm.sbafla.com/media/fdwlbsvn/20261002_2023hurricane_2021floodacceptedmodels.pdf).
- **2025 standards (1 Nov 2025).** New standard G-3, "Artificial Intelligence Use", requires documentation of AI policy, categories (in-house, proprietary, open source) and "training procedures, inference procedures, and measures of effectiveness", backed by audits and an on-site professional-team review. New standard CI-2 governs AI-based software engineering — [FCHLPM Report of Activities](https://fchlpm.sbafla.com/media/vjophvvg/2025-hurricane-roa.pdf).
- **How the modellers use AI.** KCC's Aug 2026 white paper describes "physical models enhanced by AI" and a move to annual releases; Karen Clark: "We are not blindly throwing AI at the data" — [Reinsurance News](https://www.reinsurancene.ws/ai-reshaping-cat-modelling-as-re-insurers-seek-more-current-risk-insight-reports-kcc/); [Global Reinsurance](https://www.globalreinsurance.com/home/kccs-clark-ai-can-sharpen-cat-models-without-making-them-a-black-box/1459603.article). Moody's uses AI exposure enrichment (white paper, Jul 2026) — [Moody's](https://www.moodys.com/web/en/us/site-assets/nahu-exposure-enrichment-2072026.pdf). Verisk put Hurricane Isaias insured losses at up to $2bn (13 Oct 2026) — [StockAnalysis news](https://stockanalysis.com/stocks/vrsk/).

### Inferences
- AI is entering catastrophe models through exposure data and component updates, not as learned hazard models. An entrant would need a full standards cycle (submissions under the 2025 standards) to become a judge.

### Gaps
- No evidence of any learned hazard model submitted or accepted by Florida or another certifier. Certifiers outside Florida (Lloyd's, Solvency II internal models, Japan's GIROJ) were not covered.

## 8. Who certifies and where the official voice sits

### Takeaway
Warnings are legally reserved to national services, and aviation to two designated centres. Licensing (Japan, Korea) protects domestic licensed firms. Open data lowers everyone's input costs.

### Cited Findings
- **WMO.** The Extraordinary Congress of 24 Oct 2025 resolved that "AI must complement, not replace" existing methods, and that local high-impact AI forecasts must be tested before operational use. It approved technical regulations on early-warning services supporting the national services' authoritative role, "enshrined in national legislation" — [WMO](https://public.wmo.int/node/32955). WMO has a Joint Advisory Group on AI and an AI nowcasting pilot — [WMO](https://wmo.int/secretariat/celeste-saulo/ai-disaster-resilience-bridging-science-standards-and-innovation).
- **ICAO.** Two designated World Area Forecast Centres, run by the Met Office (London) and NWS (Washington), have served since 1984 — [Met Office](https://www.metoffice.gov.uk/blog/2024/enhancing-aviation-safety-40-years-as-a-world-area-forecast-centre).
- **Japan.** The revised Meteorological Business Act was promulgated on 12 Dec 2025 and took effect on 29 May 2026. Foreign forecasters must appoint a domestic representative; permits can be revoked by simplified procedure; and unlicensed operators' names and apps can be published — [JMA white paper 2026](https://www.jma.go.jp/jma/kishou/books/hakusho/2026/index2.html). Weathernews backed the change (14 May 2026) — [WNI](https://jp.weathernews.com/wp-content/uploads/2026/05/20260514.pdf).
- **Korea.** The KMA commissioner: "only licensed forecasters may issue forecasts", with fines never yet imposed; sanctions are planned — [Daum](https://v.daum.net/v/20260528142448171).
- **US.** NHC's official forecast is a human-made consensus — [GPB/NPR](https://www.gpb.org/news/2026/10/26/how-ai-transforming-hurricane-forecasts).
- **Open data.** ECMWF's 9 km data became free on 20 Oct 2026 with a 2-hour delay; real-time 9 km data still requires a service agreement, and 25 km data has been free in real time since 2025 — [ECMWF](https://www.ecmwf.int/en/about/media-centre/news/2026/9-km-free-and-open-data-offers-step-change-localised-forecasts).

### Inferences
- The official voice protects licensed incumbents and observation suppliers, and limits big-tech entrants to "guidance". Open data both feeds and threatens repackagers.

### Gaps
- Chinese rules on foreign meteorological data and services, and India's private-forecast rules, were not verified (search budget exhausted).

## 9. Computing: AI supercomputers and double precision

### Takeaway
Weather centres are adding GPUs and moving to the cloud. Physics codes are already using lower precision, so the decline of native FP64 in AI chips hurts less than the prior assumes. Data assimilation stays on CPUs.

### Cited Findings
- **NOAA** will move its operational system, WCOSS, to Google Cloud (announced 27 Jul 2026). GFS and GEFS move through early 2027, with full completion by Dec 2027 — [NOAA](https://www.noaa.gov/news-release/noaas-use-of-cloud-infrastructure-grows-to-include-weather-prediction-models). Rhea, a $100m GPU research system, was funded in 2024 (older) — [Next Platform](https://www.nextplatform.com/hpc/2024/09/06/noaa-gets-100-million-windfall-for-rhea-research-supercomputer/1655580).
- **ECMWF** added a GPU partition in Bologna; JUPITER (EuroHPC's exascale system) is accelerator-only, with GH200 chips — [ECMWF Newsletter 186](https://www.ecmwf.int/sites/default/files/elibrary/012026/81710-gpu-adaptation-of-the-ifs-for-eurohpc-machines.pdf).
- **Elsewhere.** CWA's 6th-generation system added GPUs ([PTS](https://news.pts.org.tw/article/818850)); KMA obtained 208 GPUs ([Daum](https://v.daum.net/v/20260528142448171)); JMA stresses compute ([JMA](https://www.jma.go.jp/jma/press/2606/26a/nwp_strategic_plan_2030_260626_1summary.pdf)).
- **Precision.** MeteoSwiss runs a mixed-precision dynamical core and single-precision radiation in production ([GMD](https://gmd.copernicus.org/articles/19/755/2026/)). NVIDIA Rubin's native FP64 is ~33 TFLOPS, below H100; it emulates up to 200 TFLOPS for matrix operations only, and vector-heavy codes cannot use that — [The Register, 18 Jan 2026](https://www.theregister.com/2026/01/18/nvidia_fp64_emulation/).

### Inferences
- Learned models make inference cheap (AIGFS at 0.3% of GFS compute). Spending shifts to training and reanalysis, which still need large physics runs.

### Gaps
- No outcome of ECMWF's 2026 procurement; JMA's and KMA's next systems were not verified.

## 10. Valuation snapshot (listed; separate from quality evidence; no recommendation)

### Takeaway
Weathernews trades at a moderate multiple with net cash; Vaisala has re-rated; Verisk carries a premium; Spire is priced as an option.

### Cited Findings
- **Weathernews (4825.T).** ¥1,854 at the 12 Nov 2026 close. Market value ¥87.8bn on 47.376m shares issued including treasury stock (Yahoo/Kabutan), or ¥82.4bn on 44.42m shares excluding it (StockAnalysis). P/E 21.4× on the company forecast (22.1× trailing); P/S 3.2–3.3×; P/B 3.8×; EV ¥66.7bn; EV/EBITDA 11.7×; yield 2.70%. The year-to-date high was ¥2,200 (26 Feb 2026) and the low ¥1,802 (6 Nov 2026); 52-week change −8.1%. Shares split 2-for-1 on 1 Dec 2024 and again on 1 Mar 2026 — [Yahoo Japan](https://finance.yahoo.co.jp/quote/4825.T); [Kabutan](https://s.kabutan.jp/stocks/4825/); [StockAnalysis](https://stockanalysis.com/quote/tyo/4825/statistics/); [tanshin](https://assets.finboard.net/tdnet-filings/20260708589783.pdf).
- **Vaisala (VAIAS).** €64.80 at 12:44 EET on 12 Nov 2026. Market value €2.36bn; P/E 31.3× (25.0× forward); P/S 3.84×; EV/EBITDA 18.2×; 52-week range €40.90–67.00 (+54.1%); yield 1.33% — [StockAnalysis](https://stockanalysis.com/quote/hel/VAIAS/statistics/).
- **Spire (SPIR).** $9.97 at the 11 Nov 2026 close. Market value $391m; EV $323m; no P/E (loss-making); P/S 5.78× (4.07× forward). 52-week range $6.60–25.93 (+16.5%). It fell ~9% after Q3 results on 10 Nov, and price targets were cut (Craig-Hallum to $18, Stifel to $20). Short interest 9.4% — [StockAnalysis](https://stockanalysis.com/stocks/spir/); [stats](https://stockanalysis.com/stocks/spir/statistics/).
- **Verisk (VRSK).** $205.98 at the 11 Nov 2026 close. Market value $26.42bn; EV $30.50bn; P/E 31.3× (24.5× forward); P/S 8.32×; EV/EBITDA 19.85×; 52-week range $155.94–227.16 (−3.3%) — [StockAnalysis](https://stockanalysis.com/stocks/vrsk/statistics/).

### Gaps
- Kweather (068100) and Moody's were not priced. Price data are from aggregators and are delayed.

## Could not verify
- NHC's official 2026 verification (not yet published); the Local10 article body.
- WeatherNext 3 from Google's own pages (only a secondary source was read).
- Météo-France's AI status; CMA Fengqing's skill and start date; CWA's claims ("15 AI models", annual error cuts); IMD BharatFS's "64% better".
- Licences for FengWu and official FuXi; ECMWF's 2026 HPC award; DWD and JMA GPU operations; SCREAM on El Capitan; AceCAST's 2026 release.
- Tomorrow.io's valuation; finances of TWC, AccuWeather, DTN and StormGeo; funding for Salient, Excarta, Zeus AI and Climavision; Brightband's round (aggregator only).
- Chinese foreign-data rules; the size of the Korean and Chinese markets; any learned hazard model before a certifier.
- All company accuracy claims (WNI, TWC, WindBorne, Google, NVIDIA, Kweather) are company claims, unconfirmed.
- The WebSearch budget ran out mid-task.

## Sources (dated; URLs inline above; accessed 12 Nov 2026)
- **Agencies (primary).**
  - ECMWF news: 25 Feb 2025, 1 Jul 2025, 12 May 2026, 20 Oct 2026.
  - ECMWF AIFS blogs: 27 Mar, 11 May, 12 May, 3 Aug, 3 Nov 2026.
  - ECMWF Confluence pages for AIFS v2 (May 2026); ECMWF Newsletter 186 (Winter 2025/26).
  - NOAA releases: 17 Dec 2025 and 27 Jul 2026. NHC 2025 verification report (30 Mar 2026); weather.gov NHC Q&A (2026, undated).
  - ECCC (27 May 2026); Met Office blog (4 Feb 2026); JMA plan (26 Jun 2026) and white paper (2026).
  - WMO Congress release (24 Oct 2025); Florida Commission accepted-model list (rev. 2 Oct 2026) and 2025 Report of Activities (1 Nov 2025).
- **Agencies via media.** KMA (Daum/News1, 28 May 2026); CMA (Xinhua, 19 Dec 2025 and 28 Apr 2026); CWA (PTS, 22 Jul 2026); IMD (Drishti IAS, 14 May 2026); NHC 2026 season (Local10, 10 Sep 2026; GPB/NPR, 26 Oct 2026).
- **Papers.**
  - arXiv: 2608.24651 (25 Aug 2026), 2608.13122 (13 Aug 2026), 2610.41313 (2026), 2606.11356 (2026), 2605.22248 (May 2026), 2603.23043 (Mar 2026), 2312.15796, 2410.14932, 2404.00411.
  - Journals and conferences: GMD 19:755 (23 Jan 2026); SC23 SCREAM (2023).
- **Companies.**
  - Weathernews: tanshin (9 Jul 2026); releases of 26 Aug, 15 Oct and 14 May 2026.
  - Vaisala Q3 report (27 Oct 2026); Spire Q3 release (10 Nov 2026).
  - Google (17 Nov 2025; WeatherNext 3 via XenoSpectrum, Sep 2026); NVIDIA (26 Jan 2026); TWC blog (30 Jul 2026).
  - Deals and firms: TechCrunch (5 Aug 2026); Via Satellite (3 Feb 2026); Globes (18 May 2026); Dealsite (14 May and 18 Sep 2026); Kharn (Sep 2026); Huxiu (Jul 2026); Meteomatics (29 Jan 2025).
  - Catastrophe modelling: Reinsurance News and Global Reinsurance (KCC, Aug 2026); Moody's white paper (Jul 2026).
- **Market data (11–12 Nov 2026).** StockAnalysis, Yahoo Finance Japan, Kabutan.
