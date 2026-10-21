# Quant Analyst

- Symbol: GM
- Elapsed: 98.1s

---
## GM — Quantitative Factor & Risk Report
*General Motors Co. | Consumer Cyclical / Auto Manufacturers | Price $84.00 (last close 2026-10-13), mkt cap ~$75B, EV ~$178B*

### ⚠️ Data integrity warning — read first
Three independent feed inconsistencies materially affect the return-based statistics below, so I present **both** the tool output and a recomputation from raw OHLCV:

| Item | Tool / profile value | Raw adjusted-close data |
|---|---|---|
| Latest price | $77.09 (profile) | **$84.00** (2026-10-13 close) |
| 12-month return | −0.07% (Sharpe tool) | **+52.3%** (55.15 → 84.00) |
| Momentum (12-1) | +9.0% | **≈+55%** (85.37 vs 55.15) |
| Trailing P/E | 23.57x | 2025E EPS $10.35 → **8.1x**; 2026E $13.47 → **6.2x** |

The +9.0% "momentum" figure is exactly the ratio of the latest close to the stale profile price (84.00/77.09 = 1.0896) — a snapshot-stitching artifact, not a return. **Volatility (34.7%), beta (1.20) and max drawdown (−16.0%) are corroborated** by the raw series (intraday 91.67 → 76.91, Jul–Sep 2026 = −16.1%) and are usable. Return-based stats are not. Also unusable as published: TM P/E of 0.06x and a TD Cowen target of $33.

---

### 1. Factor Scores Table
Sector rank = rank of 5 pure auto peers (GM, F, TM, TSLA, STLA). Peer set is deliberately narrow; the broad "Consumer Cyclical" tag pulls in AMZN/HD/MCD, which are not comparables.

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | EV/EBITDA 9.64x · P/FCF 6.77x (**14.8% FCF yield**) · P/B 1.19x · Fwd P/E 6.2x · Div 0.9% | **2 / 5** (~65th pctile) | **Attractive** — cheapest quality-adjacent multiple in cohort after TM (3.99x); 3rd on P/FCF behind TM 1.43x and F 3.88x |
| **Momentum** | 12-1 ≈ **+55%** vs SPY +3.5% → **+51pp excess** | **1 / 5** (~95th pctile) | **Strong positive** — best in cohort (TM +9.9%, F −4.4%, TSLA −4.0%, STLA −13.3%) |
| **Quality** | ROE 4.27% · ROIC 1.5% · GP/A 0.071 · **Accruals −8.59%** · F-Score **4/9** | **3 / 5** (~40th pctile) | **Weak as reported** — but see caveat below |
| **Low Vol** | σ 34.69% · β 1.20 (SPY) | **2 / 4** (~60th pctile) | **Neutral/mixed** — high absolute vol; mid-pack among autos (TM 27.3%/0.88 best, TSLA 45.2%/2.19 worst) |
| **Earnings Revision** | Tool: +5.94% "upgrade" | n/a | **Unreliable — do not use** |

**Quality caveat (important):** ROE 4.27% and ROIC 1.5% are trailing figures wrecked by one-off charges. Prior three years: ROE 9.2% / 14.8% / 13.7%, ROIC 6.5% / 4.9% / 5.5%. Operating cash flow of **$26.87B** against net income of **$2.70B** confirms the earnings collapse is non-cash — the −8.59% accruals ratio is the best in the cohort and improving four straight years (−2.3% → −5.1% → −4.0% → −8.6%). On **normalized** ROE (~12–13%) GM would rank #2 of 5, not #3. The F-Score of 4/9 is a charge-year artifact, not a deterioration in cash economics (components: leverage and gross margin down, but positive ROA, positive OCF, clean accruals, no dilution).

**Revision caveat:** the tool compared the **2030E** estimate ($20.38) to the **2029E** estimate ($19.24) — consecutive fiscal years, not the same period three months apart. That is a growth curve, not a revision. No same-period revision history is available from this feed. Directional substitute: **price-target momentum is positive** — RBC $100→$102, DB $100→$101, GS $103→$112, UBS $114 — median target ~$106, implying **+26% upside**. Estimate dispersion is wide, however (2028E range $13.24–$18.59, ±16%; only 7 analysts; 2030E only 4).

### 2. Price Statistics (252-day window)

| Metric | Value | Assessment |
|---|---|---|
| Alpha (annualized, vs SPY) | **−20.6%** as reported | **Not credible** — raw data shows +52% return vs SPY +3.5%; direction is almost certainly positive |
| Beta | **1.20** (tool 1.196–1.202; profile 1.40) | High; use 1.20 |
| R² | **0.206** | Only 21% of variance is market-explained — 79% idiosyncratic |
| Annualized vol | **34.7%** | ~2x market; 4th-highest risk in peer screens |
| Max drawdown | **−16.0%** (91.67 → 76.91, Jul–Sep 2026) | Contained; vs F −30.5%, TM −31.9%, TSLA −33.6% |
| Sharpe | −0.002 as reported | Recomputed: 52.3% / 34.7% ≈ **1.5** (0% RF), ≈ **1.4** at a 4% RF |
| Sortino | −0.003 as reported | Recomputed materially higher than Sharpe — downside path (−16% DD) was far shallower than upside |
| 2-yr return | +90.8% (44.03 → 84.00) | ~+37%/yr CAGR |

**Statistical significance:** with R² = 0.206, annualized idiosyncratic vol = 34.7% × √0.794 = **30.9%**. Over a single 252-day window the standard error on annualized alpha is ≈30 percentage points, so the reported −20.6% alpha has a **t-stat of ≈ −0.7 — statistically indistinguishable from zero**. Same for Sharpe: SE ≈ ±1.0, so −0.08 or +1.5 are both inside the noise band. **One year of daily data cannot establish GM's alpha in either direction.** Do not treat the −20.6% as evidence of underperformance.

### 3. Composite Quant Signal: **BUY** (not Strong Buy)

| Pillar | Verdict |
|---|---|
| Value | ✅ Strong — 14.8% FCF yield, 6.2x forward earnings, 1.19x book |
| Momentum | ✅ Very strong — +51pp excess vs SPY, best in cohort, shallow drawdown |
| Quality | ⚠️ Weak reported, acceptable normalized — charges mask strong cash conversion |
| Low vol | ❌ Negative — β 1.20, σ 34.7% |
| Revisions | ⚠️ Unmeasurable; PT momentum constructive |

Two of five pillars are strongly positive, one is unmeasurable, and the two negatives (weak reported quality, high beta) cap the signal below Strong Buy.

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — elevated.** The 12-1 +55% run has stalled: GM made a lower high at $87.16 (Sep 14) versus the $90.11 July peak and was still 7% below it on Oct 13. Trailing 1-month return is roughly flat-to-negative. Momentum factors exhibit their worst drawdowns right after such flattening, and auto momentum is notoriously mean-reverting into the model year/cycle.
2. **Factor crowding.** GM is a consensus deep-value/cyclical long with a 1.19x book and 0.9% yield — exactly the profile that gets crowded. Correlation with **F is 0.574**, the highest pairwise link in the cohort: GM is effectively a beta expression on the whole legacy-auto trade, and STLA's −41% ROE shows how fast that trade unwinds.
3. **High beta + cyclicality.** β 1.20 with 34.7% vol against a 0.206 R². Tariff, China JV, and EV-charge risk are largely unhedged idiosyncratic exposures — the 79% unexplained variance is where the P&L actually lives.
4. **Estimate fragility.** 2026E EPS dispersion is tight ($13.18–$13.85) but out-years are not (±16% at 2028E, 4–7 analysts). The value case rests entirely on forward EPS being delivered; a miss on the $13.47 2026E pushes the stock back to ~15x on a still-depressed trailing base.
5. **Feed reliability.** Given the price/ratio/revision inconsistencies documented above, treat the value and revision *magnitudes* as directional only. The raw price series (corroborated by the analyst target feed) is the most trustworthy input here.

### Bottom line
GM is a **high-momentum, deep-value, low-quality-as-reported, high-beta** stock. The interesting asymmetry is that the "low quality" reading is an accounting artifact — $26.9B of operating cash flow versus $2.7B of net income, four years of improving accruals, and 14.8% FCF yield against 6.2x forward earnings. The quantitative caveats are real: the alpha statistic is meaningless at n=1 year, momentum is decelerating, and the earnings-revision input is methodologically broken and should not be cited in the memo.
