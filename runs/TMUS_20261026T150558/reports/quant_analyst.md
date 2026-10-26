# Quant Analyst

- Symbol: TMUS
- Elapsed: 130.7s

---
# TMUS — Quantitative Factor Analysis

**T-Mobile US, Inc.** | Communication Services / Telecom Services | Price $146.41 | Mkt cap ~$157B | 252-day window

## 1. Factor Scores Table

| Factor | Score (0–100) | Sector Rank* | Signal |
|--------|:---:|:---:|--------|
| **Value** | 45 | 3 of 3 | Neutral |
| **Momentum** | 20 | 3 of 3 | Bearish |
| **Quality** | 65 | 1 of 3 | Positive |
| **Low Vol** | 25 | 3 of 3 | Bearish |
| **Earnings Revision** | 75 | 1 of 3 | Positive |

*Rank among pure telecom comparables where I have matching data: TMUS / VZ / T. Broad Comm-Services peers (GOOG, META, NFLX, DIS) are internet/media, not valuation-comparable — excluded.

**Underlying raw metrics**

| Factor | TMUS | VZ | T | TMUS positioning |
|--------|:---:|:---:|:---:|--------|
| P/E | 15.05 | 10.72 | 6.93 | Most expensive |
| EV/EBITDA | 9.01 | 7.66 | 5.61 | Most expensive |
| P/FCF (FCF yield) | 10.73 (~9.3%) | 9.36 | 7.78 | Most expensive |
| P/B | 2.79 | — | — | — |
| ROE | 18.57% | 16.24% | 17.04% | **Best** |
| ROIC | 10.33% | — | — | — |
| GP/Assets | 19.2% | 15.6% | 17.8% | **Best** |
| Accruals ratio | −7.74% | −4.94% | −4.38% | **Best** (cash earnings > NI) |
| 12-1 Momentum | −13.0% | +7.1% | +14.1% | **Worst** |
| EPS revision (fwd) | +16.5% | +6.6% | +10.1% | **Best** |
| Piotroski F | 5 (Moderate) | — | — | — |

TMUS trades at a 25–70% premium to VZ/T on every multiple — but earns that premium on ROE, gross profitability, and accruals quality. The question is whether growth (revenue est. ~$80B→$109B by 2030) justifies it. The composite quality tool flags "low," driven by asset-heavy GP/Assets ~19% — a structural telecom trait, not a deterioration signal; raw ROE/accruals are genuinely strong.

## 2. Price Statistics (252 trading days, vs SPY)

| Metric | Value |
|--------|:---:|
| Annualised alpha | **−11.48%** |
| Beta vs SPY | −0.506 |
| R² | **0.0318** |
| Annualised volatility | 37.37% |
| Max drawdown | −33.23% |
| Annualised return | −21.81% |
| Sharpe ratio | **−0.584** |
| Sortino ratio | −0.666 |
| 12-1 momentum | −13.0% |

The stock has de-rated hard over the trailing year: −22% annualized return, 33% peak-to-trough drawdown, and negative alpha. Risk-adjusted performance is poor on both Sharpe and Sortino. **Critical caveat:** R² = 0.032 means SPY explains only ~3% of TMUS's variance — the reported beta of −0.51 is **not statistically meaningful** and should not be read as a reliable defensive hedge. All three telecoms show ~−0.5 beta vs SPY in this window, suggesting a regression artifact rather than true negative market sensitivity.

## 3. Composite Quant Signal: **NEUTRAL** (negative tilt)

Weighted composite (Value 20 / Momentum 25 / Quality 20 / LowVol 15 / Revision 20) ≈ **46/100**.

Genuine tension in the data: **quality and estimate revisions are top-of-group**, but **momentum, volatility, and relative valuation are bottom-of-group**. Quality + a ~9.3% FCF yield + 2.9% dividend provide valuation support and cap downside; but a −13% 12-1 momentum reading with −11.5% alpha is the strongest single-factor headwind in the model. Quality rarely rescues a collapsing trend near-term. Net: **Neutral** — not a Sell because the fundamental quality/revision profile and ~9% FCF yield are real, but nowhere near a Buy while momentum and alpha are this negative. A pure momentum screen would classify it **Sell**.

## 4. Key Quant Risk Flags

1. **Momentum reversal / falling-knife risk** — −13% 12-1 momentum, −22% annualized return, 33% drawdown with no trend stabilization visible. Bottom of peer group on momentum.
2. **Negative alpha & weak risk-adjusted returns** — alpha −11.5%/yr, Sharpe −0.58, Sortino −0.67; persistently underperforming SPY.
3. **Unreliable beta (R² = 3.2%)** — reported beta −0.51 is statistically hollow; do **not** size TMUS as a low-beta/defensive hedge on this estimate. Single 252-day window is also short for factor inference.
4. **Quality-at-a-premium / de-rating risk** — most expensive of the telecom trio on P/E, EV/EBITDA and P/FCF; premium requires continued growth delivery. Any growth disappointment invites further multiple compression.
5. **Earnings-revision data quality** — the +16.5% upgrade rests on the **2030** estimate covered by only **5 analysts** (vs 17 on 2027). Thin, long-dated, low-confidence; near-term 2027 revision trend not observed. Treat the "Positive" revision signal as directional, not high-conviction.
6. **Price targets are being cut** — Bernstein $220→$180, Scotiabank $243→$232→$217→$212 — even though absolute targets ($170–232) sit well above spot. Raymond James upgrade to Outperform ($170) is the lone positive catalyst; sentiment direction is cooling.
7. **High volatility for the sector** — 37% annualized vol is the highest of the three telecoms, with the deepest drawdown; poor fit for a low-volatility sleeve.

*Data note: peer ranking covers only VZ and T (matching factor data available); broad Communication Services comparables lack comparable multiples in this pull. Beta/alpha/sharpe figures derive from a single 252-day window and are subject to small-sample error.*
