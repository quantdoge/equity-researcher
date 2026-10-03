# quant_analyst

_2026-08-22T07:43:55+00:00_

# AMD (Advanced Micro Devices, Inc.) — Quantitative Factor Analysis

**As of: August 21, 2026**

---

## 1. Data Sources & Coverage

| Source | Tool / Endpoint | Data Retrieved |
|--------|----------------|--------------|
| **FMP** | `statements/key-metrics` | AMD historical key metrics (FY2023–FY2025 preview) |
| **FMP** | `statements/key-metrics-ttm` | AMD, NVDA, INTC, QCOM TTM key metrics |
| **FMP** | `statements/metrics-ratios-ttm` | AMD TTM valuation ratios |
| **FMP** | `statements/financial-scores` | AMD Altman Z-Score & Piotroski F-Score |
| **FMP** | `economics/treasury-rates` | Latest U.S. Treasury curve (preview) |
| **FMP** | `economics/market-risk-premium` | Global market risk premiums (preview, USA value not shown in preview rows) |
| **Supplementary** | Finviz (AMD, NVDA, INTC, QCOM, AVGO) | Cross-sectionally consistent valuation, profitability, technical, and performance data as of Aug 21, 2026. *Used because FMP `chart/historical-price`, `technicalIndicators`, and several peer `metrics-ratios-ttm` calls hit the session tool-call limit.* |

---

## 2. Raw Factor Metrics — AMD vs. Semiconductor Peers

| Metric | AMD | NVDA | INTC | QCOM | AVGO | Source |
|--------|-----|------|------|------|------|--------|
| **Price** | 473.25 | 214.72 | 90.07 | 160.75 | 368.45 | Finviz |
| **Market Cap** | 772.6B | 5,196B | 473.3B | 168.8B | 1,753B | Finviz |
| **P/E (TTM)** | 121.46 | 32.88 | N/A (neg.) | 18.60 | 61.34 | Finviz |
| **Forward P/E** | 30.07 | 16.75 | 43.54 | 15.75 | 18.84 | Finviz |
| **PEG** | 0.40 | 0.35 | 0.46 | 5.00 | 0.33 | Finviz |
| **P/S** | 18.70 | 20.50 | 8.30 | 3.83 | 23.23 | Finviz |
| **P/B** | 11.49 | 26.61 | 5.19 | 6.14 | 19.99 | Finviz |
| **P/FCF** | 91.94 | 43.64 | 1,375.80 | 16.21 | 53.50 | Finviz |
| **EV/EBITDA** | 80.26 | 30.99 | 30.05 | 14.74 | 42.75 | Finviz |
| **EV/Sales** | 18.49 | 20.23 | 8.93 | 3.99 | 23.83 | Finviz |
| **ROE** | 10.20% | 114.29% | -12.18% | 33.75% | 37.28% | Finviz |
| **ROIC** | 9.11% | 77.17% | -8.30% | 22.90% | 19.50% | Finviz |
| **ROA** | 8.12% | 82.97% | -5.72% | 16.50% | 17.06% | Finviz |
| **Gross Margin** | 50.37% | 74.15% | 39.05% | 54.23% | 65.66% | Finviz |
| **Operating Margin** | 15.71% | 64.02% | 8.03% | 23.50% | 44.14% | Finviz |
| **Net Margin** | 15.58% | 62.97% | -19.79% | 21.01% | 38.85% | Finviz |
| **FCF Yield (TTM)** | 1.09% | 2.29% | 0.62% | 6.17% | — | FMP `key-metrics-ttm` |
| **Earnings Yield** | 0.83% | 3.06% | -2.46% | 5.45% | — | FMP `key-metrics-ttm` |
| **Current Ratio** | 2.61 | 3.44 | 1.60 | 2.02 | 2.24 | Finviz |
| **Debt/Equity** | 0.06 | 0.07 | 0.58 | 0.55 | 0.74 | Finviz |
| **Altman Z-Score** | 27.78 | — | — | — | — | FMP `financial-scores` |
| **Piotroski F-Score** | 8 | — | — | — | — | FMP `financial-scores` |
| **Beta** | 2.48 | 2.22 | 2.24 | 1.67 | 1.46 | Finviz |
| **RSI(14)** | 45.80 | 51.01 | 39.60 | 43.56 | 38.71 | Finviz |
| **Perf YTD** | +120.98% | +15.13% | +144.09% | -6.02% | +6.46% | Finviz |
| **Perf 1-Year** | +189.08% | +22.71% | +283.28% | +4.30% | +27.23% | Finviz |
| **Perf Quarter** | +5.26% | -2.18% | -23.99% | -24.68% | -11.12% | Finviz |
| **Perf Month** | -12.31% | +2.85% | -10.14% | -6.05% | -6.12% | Finviz |
| **Perf Week** | -8.00% | -4.64% | -12.13% | -3.04% | -6.24% | Finviz |
| **SMA50 Distance** | -7.25% | +3.44% | -16.74% | -9.96% | -5.16% | Finviz |
| **SMA200 Distance** | +43.47% | +9.95% | +25.96% | -4.44% | -0.20% | Finviz |
| **Volatility (Week / Month)** | 3.60% / 5.41% | 1.89% / 2.86% | 4.49% / 6.23% | 3.28% / 3.89% | 2.61% / 3.54% | Finviz |
| **Analyst Recommendation** | 1.54 (Buy) | 1.22 (Strong Buy) | 2.43 (Hold) | 2.61 (Hold) | 1.30 (Strong Buy) | Finviz |
| **Target Price vs Current** | +31.8% | +47.6% | +34.6% | +25.0% | +45.0% | Finviz |

---

## 3. Preliminary Factor Assessment (Directional)

**Important:** The table below provides *directional* signals based on raw cross-sectional comparison. **Formal z-scored factor scores and quintile sector ranks require computation by `quant_engineer`** (see Section 6).

| Factor | AMD Raw Standing | Directional Signal | Rationale |
|--------|----------------|-------------------|-----------|
| **Value** | P/E 121x (highest trailing in peer set except loss-making INTC); P/S 18.7x; EV/EBITDA 80x. Forward P/E 30x and PEG 0.40x suggest valuation is more reasonable on forward growth. | **Sell / Expensive** | AMD trades at a massive premium to QCOM (P/E 18.6x, EV/EBITDA 14.7x) and NVDA (P/E 32.9x, EV/EBITDA 31x) on trailing metrics. Only the forward PEG looks competitive. |
| **Momentum** | YTD +121%, 1-Year +189% (extremely strong long-term); but Month -12.3%, Week -8.0%, SMA50 -7.3% (negative short-term). | **Mixed / Reversal Risk** | Long-term trend is strongly positive, but recent price action is breaking down below 50-day MA. This is a classic momentum-reversal flag. |
| **Quality** | Piotroski 8 (strong); Altman Z 27.8 (very safe); ROIC 9.1%, ROE 10.2%. However, margins are mid-tier vs. peers. | **Neutral / Moderate** | Piotroski and Altman are excellent. But ROIC is well below NVDA (77%), QCOM (22.9%), and AVGO (19.5%). Debt is very low (D/E 0.06). |
| **Low Volatility** | Beta 2.48 (highest in peer set except INTC 2.24); Monthly volatility 5.41% (highest). | **Sell / High Risk** | AMD exhibits the most price volatility and the highest systematic risk (beta) among the peer group. |
| **Earnings Revision** | Analyst consensus 1.54 (Buy); target +31.8% above price. Recent analyst actions include several upgrades in May/Jun 2026. | **Buy (tentative)** | Direction is positive, but I do not have formal EPS estimate revision time-series from FMP `analyst/estimates`. |

---

## 4. Price Statistics (Observable vs. Computed)

| Statistic | Value | Status | Source / Note |
|-----------|-------|--------|---------------|
| **Beta (β)** | 2.48 | **Direct** | Finviz |
| **Alpha (α)** | *Not available* | **Requires computation** | Needs regression of AMD excess returns vs. market benchmark (e.g., QQQ or SPY) using `chart/historical-price-eod-full` for AMD and benchmark. |
| **Sharpe Ratio** | *Not available* | **Requires computation** | Needs daily return series from `chart/historical-price-eod-full` and risk-free rate (10Y Treasury ≈ 4.69% from FMP `economics/treasury-rates`). |
| **Sortino Ratio** | *Not available* | **Requires computation** | Needs downward deviation calculation from daily returns (same source as Sharpe). |
| **Max Drawdown** | *Not available* | **Requires computation** | Needs historical price series to compute peak-to-trough decline. |
| **RSI(14)** | 45.80 | **Direct** | Finviz |
| **SMA50 Distance** | -7.25% | **Direct** | Finviz |
| **SMA200 Distance** | +43.47% | **Direct** | Finviz |
| **ATR(14)** | 28.40 | **Direct** | Finviz |
| **52W High Distance** | -19.07% | **Direct** | Finviz |
| **52W Low Distance** | +217.15% | **Direct** | Finviz |

---

## 5. Quantitative Signals

| Signal | Reading | Interpretation |
|--------|---------|--------------|
| **RSI(14)** | 45.80 | Neutral territory — neither overbought (>70) nor oversold (<30). |
| **Trend vs. Moving Averages** | Price below SMA50 (-7.3%) but well above SMA200 (+43.5%) | Short-term trend is deteriorating; long-term trend remains intact. A "golden cross" or "death cross" assessment requires `quant_engineer` to compute exact MA crossovers on daily closes. |
| **Volatility Regime** | Weekly 3.60%, Monthly 5.41% | Elevated. AMD is experiencing a volatility expansion relative to NVDA (1.89%/2.86%) and AVGO (2.61%/3.54%). |
| **Price Momentum (Raw)** | 1-Year +189%, 1-Month -12.3% | Extreme long-term momentum; near-term negative. The 12-minus-1 month momentum signal is positive but decelerating rapidly. |
| **Distance to 52W High** | -19.1% | Not in extreme euphoria territory, but not a deep pullback either. |
| **Short Interest** | 2.32% of float, Short Ratio 1.30 | Low short interest — no significant short-squeeze potential or bearish crowding. |

---

## 6. Computations Required — Route to `quant_engineer`

The following metrics **cannot be retrieved directly** from FMP or other sources and require custom computation. I have identified the exact inputs needed.

### A. Cross-Sectional Factor Scores & Ranks
**Inputs needed:**
- FMP `statements/key-metrics-ttm` for AMD, NVDA, INTC, QCOM, AVGO *(4 of 5 already fetched; AVGO missing)*
- FMP `statements/metrics-ratios-ttm` for AMD, NVDA, INTC, QCOM, AVGO *(only AMD fetched)*
- FMP `statements/financial-scores` for all peers *(only AMD fetched)*

**Computation:**
1. **Value z-score** composite using inverse-rank of: P/E, P/S, EV/EBITDA, EV/Sales, P/FCF, FCF Yield. Higher z-score = cheaper.
2. **Quality z-score** composite using: ROIC, ROE, Gross Margin, Operating Margin, Current Ratio, Piotroski F-Score, Altman Z-Score.
3. **Momentum z-score** using 12-1 month returns, 6-1 month returns, and SMA200 distance.
4. **Low-Volatility z-score** using inverse of Beta, monthly volatility, and ATR.
5. **Composite Quant Signal** = weighted average of the four z-scores (e.g., 25% each) with sector rank (1=best, 5=worst).

### B. Alpha & Beta Estimation
**Inputs needed:**
- FMP `chart/historical-price-eod-full` for AMD (daily, last 2 years)
- FMP `chart/historical-price-eod-full` for market benchmark (QQQ or SPY, same period)
- FMP `economics/treasury-rates` for daily risk-free rate proxy (3M or 10Y)

**Computation:**
- Rolling 252-day regression: AMD excess return = α + β × Market excess return.
- Report α (annualized), β, R², and standard error.

### C. Sharpe & Sortino Ratios
**Inputs needed:**
- Same daily return series as above for AMD and peers.

**Computation:**
- Annualized Sharpe = (Mean daily return − Risk-free daily rate) / StdDev(daily returns) × √252
- Annualized Sortino = (Mean daily return − Risk-free daily rate) / Downside Deviation × √252
- Compute for AMD and all peers for cross-sectional comparison.

### D. Correlation Matrix & Drawdown
**Inputs needed:**
- Daily returns for AMD, NVDA, INTC, QCOM, AVGO from `chart/historical-price-eod-full`.

**Computation:**
- Pairwise return correlations (to assess factor crowding).
- Max drawdown (peak-to-trough) for AMD over 1-year and 2-year windows.

### E. Earnings Estimate Revision Momentum
**Inputs needed:**
- FMP `analyst/estimates` or `analyst/earnings-surprises` for AMD (EPS estimate history for current and next fiscal year).
- FMP `analyst/analyst-ratings` for revision direction.

**Computation:**
- 3-month and 1-month % change in consensus EPS estimates.
- Count of upgrades vs. downgrades in the last 90 days.
- Revision momentum score (+1 for upward, −1 for downward).

### F. 12-Minus-1 Month Price Momentum
**Inputs needed:**
- FMP `chart/historical-price-eod-full` for AMD and peers (daily closes).

**Computation:**
- Return from month-end T-12 to month-end T-1 (exclude most recent month to avoid reversal).
- Cross-sectional rank within peer group.

---

## 7. Composite Quant Signal (Preliminary)

> **Neutral / Cautious**

**Bullish elements:** Strong Piotroski score (8), very high Altman Z (27.8), explosive growth trajectory (EPS next 5Y est. +75%), analyst consensus is Buy (1.54), massive long-term momentum (+189% 1-year), low debt, reasonable forward PEG (0.40).

**Bearish elements:** Trailing valuation is the richest in the peer group (P/E 121x, EV/EBITDA 80x), beta/volatility is the highest (β=2.48, vol 5.41%), short-term momentum has turned sharply negative (month -12.3%, below SMA50), quality metrics (ROIC 9.1%, ROE 10.2%) lag the dominant AI semiconductor names (NVDA, AVGO).

**Key Risk Flags:**
1. **Momentum Reversal Risk:** 1-month return (-12.3%) vs. 1-year (+189%) indicates a violent trend deceleration. If this breaks the 200-day moving average, technical damage would be significant.
2. **Factor Crowding:** AMD's YTD +121% and 1-year +189% performance likely embeds high expectations. Any EPS miss or AI demand slowdown could trigger a high-beta unwind.
3. **Low Liquidity Risk:** Not flagged. Short interest is low (2.32%) and average volume is healthy (~29M shares/day).

---

## 8. Data Gaps & Honest Limitations

| Gap | Impact | Resolution |
|-----|--------|------------|
| AVGO `key-metrics-ttm` not fetched from FMP | Cannot compute formal cross-sectional rank on FMP-derived data for full peer set | Fetch via FMP or use Finviz proxy. |
| `chart/historical-price-eod-full` not fetched for any ticker | Cannot compute alpha, beta, Sharpe, Sortino, correlations, drawdown, or 12-1 momentum | Fetch 2-year daily history for AMD, NVDA, INTC, QCOM, AVGO, and benchmark (QQQ/SPY). |
| `technicalIndicators` not fetched for AMD | RSI and SMA values from Finviz are used instead of FMP | FMP `technicalIndicators` endpoints (RSI, SMA, ADX, standard-deviation) should be fetched for formal signal. |
| `analyst/estimates` not fetched | Earnings Revision signal is tentative only | Fetch EPS estimate history for formal revision momentum score. |
| USA market risk premium not extracted from FMP preview | CAPM/Alpha calculation lacks country-specific premium | Pull explicit USA row from `economics/market-risk-premium`. |
| FMP `metrics-ratios-ttm` for peers not fetched | Peer P/E, margins, etc. from Finviz only | Fetch to ensure metric consistency with AMD. |

---

**Bottom Line:** AMD is a high-conviction, high-volatility growth stock with a valuation that prices in near-perfection. The quantitative evidence supports a **Neutral** stance until: (1) the stock reclaims the 50-day moving average (momentum repair), or (2) the forward earnings trajectory catches up to the trailing multiple (value compression). A formal `quant_engineer`-computed composite score is required to move this to a firm Buy/Sell rating.
