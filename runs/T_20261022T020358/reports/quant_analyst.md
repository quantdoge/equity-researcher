# Quant Analyst

- Symbol: T
- Elapsed: 273.9s

---
All data gathered. Here's the full quantitative read.

---

# AT&T Inc. (T) — Quantitative Factor Report

**Sector:** Communication Services / Telecommunications Services · **Price:** $21.91 · **Mkt Cap:** ~$150–157B · **EV:** ~$313B
**Data as of FY2025-12-31 financials; 252-day (12-month) price window**

## 1. Factor Scores Table

Sector rank is measured against the **telecom-services comparables (VZ, TMUS)** — the honest peer set. The wider Communication Services sector (GOOG, META, NFLX, DIS) is not a valid multiple comparable for a capital-intensive carrier. Ranking "of 3" is inherently coarse; treat ranks as directional, not statistically robust.

| Factor | Score / Raw Value | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E **7.21** · EV/EBITDA **5.72** · P/FCF **8.09** · P/B **1.22** · FCF yield **12.4%** · Div yield **5.07%** | **1 of 3** (cheapest on all 4 multiples) | **Strong Buy** |
| **Momentum (12-1)** | **+18.92%** | **1 of 3** | **Buy** (but see reversal flag) |
| **Quality** | ROE **17.04%** · GP/Assets **0.178** · Accruals **−0.044** · ROIC **8.27%** · F-Score **8/9** | **2 of 3** (behind TMUS) | **Neutral–Buy** |
| **Low Vol** | Ann. vol **29.92%** · β **−0.47** · Max DD **−28.9%** | **2 of 3** (VZ 28.6% lowest) | **Neutral** |
| **Earnings Revision** | Forward EPS **+11.21%** vs prior | **2 of 3** (TMUS +16.5%) | **Buy** (low confidence) |

**Peer comparison (raw factor inputs):**

| Metric | **T** | VZ | TMUS |
|---|---|---|---|
| P/E | **7.21** | 10.73 | 15.82 |
| EV/EBITDA | **5.72** | 7.67 | 9.28 |
| P/FCF | **8.09** | 9.37 | 11.27 |
| ROE % | 17.04 | 16.24 | **18.57** |
| Gross Profit/Assets | 0.178 | 0.156 | **0.192** |
| Accruals ratio | −0.044 | −0.049 | **−0.077** |
| Ann. volatility % | 29.92 | **28.64** | 35.79 |
| Momentum 12-1 % | **+18.92** | +9.54 | −10.96 |
| EPS revision % | +11.21 | +6.56 | **+16.47** |

T wins value and momentum outright; loses quality and low-vol to TMUS/VZ respectively. The **value + momentum + revision triple-positive** combination is the core of the bull case.

## 2. Price Statistics (252-day window, benchmark SPY)

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility | **29.92%** | High for a "defensive" telecom |
| Beta (regression vs SPY) | **−0.476** | **Not credible** — see flags |
| R-squared | **0.0434** | Only 4.3% of variance explained |
| Alpha (annualised) | **+8.63%** | **Not statistically significant** |
| Sharpe ratio | **−0.02** | Negative risk-adjusted return |
| Sortino ratio | **−0.025** | Negative downside-adjusted return |
| Annualised return (252d) | **−0.6%** | Flat-to-down year |
| Max drawdown | **−28.9%** | Severe; ~1.0x the vol |
| 12-1 momentum | **+18.92%** | Strong through ~Sept |

**Critical read on the alpha/beta:** the regression beta of −0.476 (profile-reported 5Y beta: **+0.431**) is economically implausible for a telecom and the R² of 4.3% means the estimate is indistinguishable from zero. Consequently the **+8.63% "alpha" carries essentially no statistical weight** — a t-statistic of roughly 1.1 on 252 observations. Do not cite this alpha as evidence of outperformance. The negative Sharpe/Sortino and the positive 12-1 momentum are also in tension, but that's coherent, not contradictory: momentum excludes the last 21 trading days, so it captures strength through September while the trailing-year total return is dragged down by the recent slide.

## 3. Composite Quant Signal

### **BUY** — moderate conviction (4 of 5 factors positive, one neutral)

Supporting: deepest valuation in the telecom peer group on every multiple; top-ranked 12-1 momentum; Piotroski **F-Score 8/9** with all profitability, leverage and efficiency tests passing except asset turnover; four consecutive years of **negative accruals** (−0.10, −0.059, −0.071, −0.044) confirming cash earnings exceed reported earnings; EPS estimates revised **+11.2%**.

Working against: trailing Sharpe and Sortino are **negative**, so the factor case is entirely forward-looking — there is no realised risk-adjusted return to lean on. Quality is mid-pack, and ROIC (8.27%) is trending down (9.29% → 9.03% → 8.27%), which is the most under-appreciated negative in the file. ROE of 17% is largely a leverage artefact, not operating excellence.

## 4. Key Quant Risk Flags

1. **MOMENTUM REVERSAL RISK — highest priority.** The +18.9% 12-1 reading is stale by construction. Analyst price targets posted between 21 Sept and 21 Oct show the stock at $25.42 falling to $21.91 — a **≈−13.8% move in about one month**, exactly the window 12-1 momentum deliberately excludes. The trend that generated the momentum score has broken. This is a classic momentum-crash setup, and it is why the Sharpe (−0.02) and Sortino (−0.025) are negative while momentum looks positive. **Treat the momentum factor as impaired, not bullish.**

2. **Estimate-revision signal is weak and low-quality.** The "prior" estimate is a **single analyst's FY2030 figure** (`num_analysts: 1`). A one-analyst, five-year-out consensus is not a revision trend — it is one person's model. Compare with FY2027, which carries 12 analysts (EPS $2.567). The +11.21% "upgrade" should carry almost no weight. Additionally, the FY2030 estimate ($3.55) versus FY2027 ($2.57) implies a ~38% EPS ramp in three years — an aggressive CAGR that itself needs scrutiny.

3. **Price-target direction contradicts the estimate direction.** Targets have been cut repeatedly and recently: Goldman $30→$27, Scotiabank $29.25→$27.50→$26.50, plus a Bernstein downgrade to Market Perform. Sell-side *ratings and targets* are deteriorating even as the model's EPS-revision factor reads positive. The consensus target band ($24–$36, mid ~$26.50) implies ~+21% upside, but the *direction* of travel is down. Divergence between estimate levels and target revisions is a warning.

4. **Leverage and dividend carry risk.** Net debt ≈ **$155.7B** (EV $313B − mkt cap $157B), or **~2.6–2.9x EBITDA**. The 5.07% yield is covered at ~37% of EPS and ~41% of FCF ($19.4B FCF vs ~$8.0B dividends), so coverage is adequate — but with ROIC at 8.27% and falling, incremental capital is at risk of earning below cost of capital. A 5% yield in a rising-rate tape is a duration liability.

5. **Quality signal is internally split.** The quality factor model outputs `quality_signal: "low"` because gross profit/assets is only 0.178 — a structural feature of capital-intensive carriers — while the Piotroski F-Score reads 8/9 "Strong." Both are true; the low gross-margin-to-assets ratio caps quality-factor ranking regardless of the F-Score. Asset turnover is the one failing F-Score test (F9 = 0), corroborating the ROIC decline.

6. **Low-vol factor is compromised.** All three telecoms returned regression betas near **−0.47**, which is a data artefact, not a real property of the stocks. Relative volatility ranking (VZ 28.6% < T 29.9% < TMUS 35.8%) is usable; the beta figures are not. T is *not* a low-volatility name at ~30% annualised vol and a 28.9% max drawdown.

7. **Sample-size caveats.** Peer ranking rests on **n=3** — no statistical significance is possible. Single-year regression with R² = 0.043. Revision signal n=1 analyst. The only high-confidence inputs here are the valuation multiples, the accruals history (4 years) and the F-Score.

## Bottom Line

T is the cheapest large-cap telecom in its peer group and screens well on momentum *as measured*, earnings quality and balance-sheet-improvement tests — an attractive value-plus-revision profile. But the momentum reading is backward-looking and has already reversed in the most recent month, trailing risk-adjusted returns are negative, ROIC is deteriorating, and the estimate-revision signal rests on a single analyst. **Buy on valuation with a hard stop on the momentum reversal; do not size this as a momentum trade.**
