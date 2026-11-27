# Quant Analyst

- Symbol: MU
- Elapsed: 47.3s

---
## MU — Micron Technology | Quantitative Factor Report
*Reference price: $1,064.94 (last close 2026-09-30, price file). Fiscal year-end Sep-2026. Diluted shares 1.143bn.*

### ⚠️ Data-integrity flags (read first)
1. **Price discrepancy:** profile/valuation tools use **$601.25**, but the price file (and analyst notes: "price when posted" $1,045–$1,097 in late Sep/Oct 2026) put MU at **~$1,065**. All price-based multiples below are recomputed at $1,064.94; tool-native values are shown in brackets.
2. **Earnings-revision tool is defective:** it compared a forward period 5 years out (2031E EPS = $0.00, 6–8 analysts vs 22–25 for near years) against the 2030E ($207.52) → spurious **−100%**. Discarded; I use price-target and estimate trajectories as a proxy.
3. **TSM multiples corrupted** (P/E 1.03, EV/EBITDA −0.11) → excluded from peer ranking. SKHY has no factor data.

### 1. Factor Scores

| Factor | Score (0–100) | Metric | Sector Rank | Signal |
|---|---|---|---|---|
| **Value** | **95** | P/E 14.3x trailing / 6.1x FY27E (8.1x@tool price); EV/EBITDA 10.8x (6.0x); P/FCF 20.7x (11.7x); P/B 8.8x | **1 of 5** on all three multiples (NVDA 30.5x P/E, 25.0x EV/EBITDA; ASML 52.7/40.0; AVGO 63.1/43.5; AMD 153.2/90.5) | **Strong Buy** |
| **Momentum** | **70** (tool) / **98** (price file) | 12-1 momentum: **+4.53%** [tool, positive]; **+458.7%** [file: 167.03→933.29] | #3 of 6 (AMD +19.4%, TSM +6.5%, NVDA −1.9%, AVGO −7.3%, ASML −7.7%) — #1 on file basis | **Buy** |
| **Quality** | **88** | ROE 61.4%, ROIC **69.2%**, GP/assets 54.9%, accruals −2.4%, F-score **8/9** | ROE #2 of 6 (NVDA 76.3%); GP/assets #2 of 6 (NVDA 74.2%); accruals #5 of 6 | **Strong Buy** |
| **Low Vol** | **3** | Ann. vol **91.9%**, beta **3.52x** vs SPY, max DD **−51.0%** (tool) | **Last of 6** — highest beta in the group | **Strong Sell** |
| **Earnings Revision** | **75** (proxy) | Tool broken. PT median $1,400 = **+31%** upside; DA Davidson $2,000→$2,100→$3,000; Mizuho $1,375→$1,400; consensus FY27E EPS $175.22 vs FY26A $74.33 | Upward, but dispersion $1,250–$3,000 (2.4x range) | **Buy** |

### 2. Price Statistics (252-day window, vs SPY)

| Metric | Value |
|---|---|
| Annualised return | +94.0% |
| Annualised volatility | 91.9% – 93.6% |
| **Beta** | **3.52 – 3.54** (profile beta 2.37) |
| **Alpha (annualised)** | **+59.9%** |
| R² vs SPY | 0.378 *(62% idiosyncratic — this is a single-theme bet, not a diversified hold)* |
| **Sharpe** | **1.00** |
| **Sortino** | **1.67** (downside dev. 56% < total vol — fat left tail, right-skewed distribution) |
| Max drawdown | −51.0% (tool); **−39.1% close-to-close Jun 25 → Jul 29 2026** (−41.2% intraday, 1213.18→737.76) |
| 52-wk range (close) | ~$157 – $1,213; now **−12.2% below high**, still ~6.8x the low |
| Correlations | SPY 0.61, TSM 0.70, AMD 0.69, AVGO 0.56, **NVDA 0.54** (lowest) |

Fundamental backbone confirming the tape: revenue $15.5bn (FY23) → $25.1bn → $37.4bn → **$133.2bn (FY26, +256%)**; gross margin **80.7%**, operating margin 74.6%; OCF $89.7bn vs NI $85.0bn (clean conversion). Consensus FY27E revenue $277bn (+108%), FY28E $321bn (+16%) — i.e., the market is already paying for a *second* doubling.

### 3. Composite Quant Signal: **BUY** (not Strong Buy)
- Top-quintile on **value, quality and momentum simultaneously** — a rare triple, and the classic cyclical-peak configuration: cheap on trailing/forward multiples *only because* earnings are at record highs.
- **Score: 3.5 / 5.** Overweight vs semis peers justified on cross-sectional ranking; position size must be cut for the volatility/beta profile (92% vol, 3.5 beta). Sortino 1.67 and +59.9% alpha say the *risk-adjusted* return has been excellent — the raw risk is what's extreme.

### 4. Key Quant Risk Flags
1. **Normalisation risk (dominant):** 80.7% gross margin and 69% ROIC are unprecedented for memory. A 20% ASP compression halves EPS; at mid-cycle EPS of ~$30 the stock is 35x, not 6x. Trailing EV/EBITDA of 10.8x is *not* cheap for a DRAM cyclical at peak — the "value" score is cycle-dependent, not structural.
2. **Momentum reversal risk: high.** A −39% five-week drawdown already occurred in this cycle (Jun–Jul 2026); beta 3.5 means a 10% SPY drawdown ≈ −35% idiosyncratic-adjusted. Negative momentum in 3 of 5 peers (NVDA, AVGO, ASML) warns the semi momentum factor is decelerating.
3. **Factor crowding / consensus risk:** 10 of 10 PTs above $1,300, median +31% upside, one target at $3,000 — sell-side unanimity at an all-time high is a contrarian warning, and the 2.4x target dispersion implies wide model uncertainty on horizon estimates.
4. **Estimate reliability:** FY2031 consensus revenue range $121bn–$187bn (54% spread) and zero valid EPS prints beyond FY28 — long-dated estimates carry no statistical weight.
5. **Data-integrity risk:** stale $601.25 reference price understates every multiple by ~1.8x; earnings-revision factor unusable; TSM comps corrupted. Peer ranks are vs 5 valid names — small-sample, treat quintile labels as indicative (±1 rank).
6. **Liquidity: not a flag** (20–35m shares/day ≈ $25–35bn notional), but **index/ETF beta** amplifies flows in both directions.
7. **Sample note:** risk stats use 252 observations (adequate); ROIC/ROE trend has only 4 annual points, two of which are cycle-trough negative — the "quality improvement" is 2 observations wide, not statistically robust.
