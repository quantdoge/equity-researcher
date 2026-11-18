# Quant Analyst

- Symbol: HUBS
- Elapsed: 44.1s

---
# HUBS (HubSpot, Inc.) — Quantitative Factor Report
**Price $216.30 (11/17/2026) · Mkt cap $11.51B (diluted 53.19M sh) · EV $10.06B (net cash ~$1.44B) · Technology / Application Software**

*Peer set = CRM, WDAY, NOW (the `get_sector_peers` tool returned mega-cap tech — AAPL/MSFT/NVDA — which is not a valid comparable set for an $11.5B application-software name; I substituted direct application-software comps validated by return correlation of 0.67–0.73). Rank 1 = most attractive of 4.*

## 1. Factor Scores Table

| Factor | Score (0–10) | Sector Rank | Signal |
|--------|--------------|-------------|--------|
| Value | **3** | 4 / 4 (on reported); 1 / 4 (on forward) | **Bearish on GAAP, Bullish on forward** — irreconcilable split |
| Momentum | **2** | 3–4 / 4 | **Bearish** — 12-1 ≈ **−46%** |
| Quality | **5** | 2 / 4 | **Neutral** — GP/A and accruals best-in-class; ROE/ROIC worst |
| Low Vol | **1** | 4 / 4 | **Strongly Bearish** — 66–79% vol, 72% max DD |
| Earnings Revision | **4** (low confidence) | 3 / 4 | **Mildly Bearish** — PT cuts, downgrade skew |

### Value — the single most important number in this report
| Metric | HUBS | CRM | WDAY | NOW | Peer median |
|---|---|---|---|---|---|
| P/E (GAAP trailing) | **251.5x** | 24.9x | 70.9x | 55.6x | 55.6x |
| P/B | 5.57x | 3.14x | 6.28x | 7.50x | 6.28x |
| EV/EBITDA (trailing) | **48.7x** | 14.7x | 41.1x | 31.1x | 31.1x |
| P/FCF (reported) | 16.3x | 12.9x | 17.7x | 21.3x | 17.7x |
| P/FCF (**SBC-adjusted**) | **64.1x** | — | — | — | — |
| **Forward P/E (2026E)** | **15.9x** | 24.9x | 70.9x | 55.6x | — |

The divergence is entirely a GAAP/non-GAAP artifact. 2025 GAAP diluted EPS was **$0.86**; consensus 2026E EPS is **$13.61** (18 analysts). On 2026E: EV/Sales **2.73x** ($10.06B / $3.688B), EV/EBITDA **9.3x** ($1.084B), P/E **15.9x** (2027E: 12.9x). Trailing EV/Sales is 3.21x. A ~19%-growth, 84%-gross-margin SaaS business at 2.7x forward EV/S is historically extreme cheapness — but it is cheap against *non-GAAP* earnings that exclude a $528M SBC charge.

## 2. Price Statistics (504-day window, vs SPY)

| Metric | Value |
|---|---|
| Annualised return | **−45.14%** |
| Annualised volatility | **66.24%** (252-day: 78.61%) |
| Alpha (annualised) | **−56.42%** |
| Beta | **0.589** (252-day: 0.108) |
| R² | **0.0132** — beta is statistically meaningless |
| Sharpe | **−0.675** |
| Sortino | **−0.938** |
| Max drawdown | **−72.06%** |
| Corr. w/ SPY (252d) | **0.0198** |
| Corr. w/ CRM / WDAY / NOW | 0.734 / 0.720 / 0.674 |

**Statistical integrity flags (material):**
- **The alpha and beta are not identifiable.** R² = 1.3% and SPY correlation = 0.02 mean 98.7% of HUBS' variance is idiosyncratic. The −56% "alpha" is not a measured risk-adjusted excess return; it is noise labelled as alpha. Do not use this beta for cost-of-equity or hedging.
- **Two of the momentum/vol tools disagree with the raw tape.** `calculate_momentum_score` returned **+16.14%** for a 252-day lookback, but the raw daily series shows $436.82 (10/17/2025) → $234.63 (10/19/2026) = **−46.3%**. The tool's implied entry price (~$186) corresponds to a ~110-trading-day window — the lookback is not being honoured. I report the computed −46.3% as authoritative; note that on the tool's own (shorter) basis HUBS still ranks 3rd of 4 vs CRM +23.0%, NOW +17.3%, WDAY +10.7%, so "momentum laggard" survives under both methods.
- The 252-day Sharpe of +0.285 and beta of 0.108 are inconsistent with a −46% one-year return and with the 504-day figures; window instability is severe. Treat the 504-day set as primary.
- Sample-size caveat: 504 trading days ≈ 2 years, one name, no cross-sectional context. All t-statistics are below conventional significance because volatility is 4x the market's.

**Price context:** −58.6% from the 9/22/2025 high of $522.97; 52-week range ≈ $169.63–$522.97; −46.1% YTD 2026; +3.7% over 6 months, +0.5% over 3 months, −7.8% over 1 month. The stock has flatlined at ~$216 since April — a volatility regime change, not a recovery.

## 3. Fundamentals / Earnings Quality (FY2025)
Revenue $3.131B (**+19.2% YoY**), gross margin **83.8%**, operating margin **0.36%** ($11.4M), GAAP net income $45.9M, EPS $0.86. **SBC $528.2M = 16.9% of revenue = 7.5x GAAP net income.** OCF $760.7M, capex $53.2M, FCF **$707.6M (22.6% margin)** — but SBC-adjusted FCF is only **$179.4M (5.7% margin)**.

ROE 2.22% / ROA 1.19% / **ROIC 0.49%** (2024: −2.55%, 2023: −9.47%). Accruals ratio **−0.186** and GP/Assets **0.681** both look top-tier — but the negative accruals are an artifact of SBC being added back, not evidence of cash discipline. Piotroski **F=7** (leverage, accrual, ROA-improvement points earned; dilution and gross-margin-trend points lost — shares outstanding still rose despite a $500M 2025 buyback).

## 4. Composite Quant Signal: **SELL**
Equal-weighted composite ≈ **3.0 / 10** (z ≈ −1.1σ vs peer set).
Value 3 · Momentum 2 · Quality 5 · Low-Vol 1 · Revisions 4.

This is a **trend-and-quality-of-earnings sell, not a valuation sell.** The quant evidence pointing down is overwhelming and statistically robust: −46% 12-1 momentum, 66–79% volatility, −0.68 Sharpe, −72% drawdown, ROIC of 0.49%, and 93% of reported FCF consumed by stock compensation. The only leg in HUBS' favour is forward multiple compression — 2.7x EV/S and 15.9x 2026E EPS — which is exactly the profile of a **value trap** until revenue growth proves it can hold ~18% while GAAP margins expand. I would require two consecutive quarters of upward *near-term* (FY2026/FY2027) EPS revisions before upgrading to Neutral.

## 5. Key Quant Risk Flags

1. **Quality-of-earnings / SBC dependence (highest severity).** $528M SBC vs $46M GAAP net income. Every "cheap" multiple in this report (P/FCF 16.3x, forward P/E 15.9x, EV/2026E EBITDA 9.3x) is SBC-adjusted. SBC-adjusted P/FCF is 64x. If SBC is treated as a real cost, HUBS is expensive, not cheap.
2. **Factor crowding / cohort de-rating.** 0.67–0.73 correlation with CRM/WDAY/NOW versus 0.02 with SPY. HUBS is not a low-beta defensive — it is a high-multiple SaaS proxy that trades with its cohort, and the cohort has de-rated together. Diversification benefit vs the index is illusory *only if* the low correlation is real; given R²=1.3% I treat it as a data artifact, not a hedge.
3. **Momentum reversal / trend risk.** Below all meaningful moving averages, −58.6% from the high, 72% max drawdown. Nothing in the tape supports catching this.
4. **Severe earnings-gap risk.** Volume has repeatedly spiked 4–8x on results: 1/29 (−11.2%), 2/3 (−10.5%), 5/8 (**−19.1%**), 8/6 (**−19.1%**), 11/5 (−5.4%). Realised gap risk dominates any position-sizing model based on average daily volume (~1.5–2.5M sh, ~$400M notional — absolute liquidity is fine; *event* liquidity is not).
5. **Estimate-revision signal is statistically void.** The +12.56% "upgrade" is on the **FY2030** EPS estimate with **n=4 analysts** — it fails any significance test and should be discarded. The higher-quality evidence is PT direction: raises to $265/$255 (10/30) followed by cuts to $215/$200 (11/5) and $190 (11/13); Cantor→Underweight ($170), UBS→Neutral, Barclays→Equalweight, BofA→Underperform. Mean recent PT ≈ **$230.5 (+6.6%)** — trivial upside for 66% volatility, i.e. a **negative reward/risk ratio**.
6. **Data-quality flags for the memo:** (a) the momentum and low-vol tools returned windows inconsistent with the raw tape — reproduce before citing; (b) `get_analyst_estimates` quarterly failed on subscription tier, so no near-term revision time series exists — **the revision factor is materially under-observed, not merely weak**; (c) trailing GAAP multiples and consensus forward EPS are on different accounting bases and must never be blended.

**Bottom line:** BUBS is a de-rated, high-idiosyncratic-risk SaaS name with genuinely strong unit economics (84% GM, 22.6% reported FCF margin) but GAAP profitability that is effectively elective. Quant composite = **Sell**; the lone offset is forward valuation, which requires fundamental confirmation the data does not yet provide.
