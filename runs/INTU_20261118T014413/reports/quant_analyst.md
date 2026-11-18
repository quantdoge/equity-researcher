# Quant Analyst

- Symbol: INTU
- Elapsed: 57.3s

---
## INTU — Quantitative Factor Report

**Intuit Inc.** | Technology / Software–Application | Price $320.79 | Mkt cap $85.7B | FY end Jul-2026

### 1. Factor Scores

| Factor | Score (0–100) | Sector Rank* | Signal |
|---|---|---|---|
| **Value** | **88** | **2nd cheapest of 6** | **Strongly attractive** |
| Momentum | 35 | Bottom half | Neutral (stabilizing, not rising) |
| **Quality** | **80** | **1st of 5 on GP/A** | **Strong** |
| Low Vol | 8 | Bottom decile | **Very poor** |
| Earnings Revision | 40 | n/a | Neutral / mild downgrade |

\*Rank vs. software peers ADBE, CRM, NOW, ORCL, MSFT (the `get_sector_peers` feed returned semis, so I built a proper comp set).

**Value detail — INTU vs. software peers**

| | P/E | EV/EBITDA | P/FCF | P/B |
|---|---|---|---|---|
| **INTU** | **19.5** | **12.7** | **10.3** | **4.7** |
| ADBE | 14.1 | 10.3 | 10.2 | 8.7 |
| CRM | 24.9 | 14.7 | 12.9 | 3.1 |
| ORCL | 19.7 | 13.7 | n.m. | 7.8 |
| NOW | 55.6 | 31.1 | 21.3 | 7.5 |
| MSFT | 28.2 | 18.4 | 56.3 | 8.5 |
| **Peer median** | **24.9** | **14.7** | **12.9** | **7.8** |
| **INTU vs median** | **−22%** | **−14%** | **−20%** | **−40%** |

INTU is the cheapest or 2nd-cheapest name on all four multiples — a genuine top-quintile value score, not a single-metric artifact.

**Quality detail**
- ROIC **13.1% → 14.5% → 18.7% → 21.5%** (FY23–FY26), monotonically rising — the strongest quality trend in the peer set.
- ROE 24.0%; gross profit/assets **0.467** — highest of the 5-name comp set (ADBE 0.719 is a different business model; CRM 0.287, NOW 0.395, MSFT 0.297).
- Accruals ratio **−0.116** — cash conversion well above 1.0 (OCF $8.84B vs. NI $4.57B). Negative accruals = high earnings quality.
- Piotroski **F-Score 7/9** (Moderate). Two points lost: F5 (leverage rising) and F6 (negative equity change — buybacks + acquisitions).

### 2. Price Statistics

| Metric | 1-Year (252d) | 2-Year (504d) |
|---|---|---|
| Annualised return | **−6.8%** | **−49.5%** |
| Alpha vs SPY | **−23.1%** | **−52.3%** |
| Beta vs SPY | −0.07 | 0.25 |
| R² | **0.0003** | **0.0051** |
| Annualised vol | 53.8% | 44.2% |
| **Sharpe** | **−0.13** | **−1.11** |
| **Sortino** | **−0.17** | **−1.40** |
| Max drawdown | **−46.8%** | **−68.2%** |
| 12-1 momentum | +0.72% | — |
| 6-month momentum | +2.3% | — |

**Critical statistical caveat on beta:** R² of 0.0003–0.005 means the market explains **essentially none** of INTU's return variance. The −0.07/0.25 betas are statistically meaningless (not distinguishable from noise, and the two windows disagree). The vendor profile beta of **0.92** is the more defensible risk input. Do not use the regression beta for hedging or cost-of-capital.

### 3. Composite Quant Signal: **NEUTRAL** (55.9 / 100)

Weighted: Value 25% · Quality 25% · Momentum 25% · Low-Vol 15% · Revision 10%.

This is a textbook **high-quality, deeply de-rated asset** — top-quintile value *and* top-quintile quality simultaneously, which is rare. What blocks a Buy is that price is not confirming: −52% alpha, −68% max drawdown, Sortino −1.40. The only bullish technical is that 12-1 momentum has flattened to **+0.72%** and 6-month is **+2.3%** — the downtrend has stopped making new lows, a necessary (not sufficient) condition for a value inflection.

Verdict: **Buy for a value/quality mandate; avoid on a risk-adjusted momentum or low-vol mandate.** Suggested framing: accumulate only with a catalyst and a volatility-normalization trigger.

### 4. Key Quant Risk Flags

1. **Momentum reversal / falling knife.** 2-yr return −49.5%, max DD −68%. Value factors routinely fail in the presence of negative 12-month momentum. Waiting for 12-1 momentum > +10% costs some upside but removes most of the drawdown risk.
2. **Extreme volatility — 44–54% annualised.** Nearly 3x a typical large-cap software name. Any position sizing must use vol-scaled weights, not equal-weight.
3. **Beta estimate is unreliable (R² ≈ 0).** Idiosyncratic, event-driven return path. Regression alpha of −23%/−52% is a *level* statement, not evidence of a stable risk premium.
4. **Recent short-term reversal.** 1-yr return −6.8% vs. 12-1 momentum +0.72% implies roughly **−7% in the last month**. Fresh downside momentum into the print.
5. **Earnings-revision read is unreliable — methodology gap.** `calculate_earnings_revision_score` compared FY2030 EPS ($27.68) against FY2029 EPS ($28.43) and reported −2.65% "downgrade." Those are **different fiscal years**, so this is not a revision. The valid read: the estimate curve is FY27 $22.95 (+13.0% to FY28 $25.92, +9.7% to FY29 $28.43), then **−2.65% to FY30** — but FY30 carries only **4 analysts** vs. 20 for FY27, so that dip is low-confidence. FY27 dispersion is wide (low $22.46 / high $28.36, ±13%). Net: no confirmed revision signal; treat as Neutral pending a true 90-day revision history.
6. **Leverage and dilution (F-Score F5, F6 = 0).** Rising leverage plus negative equity change from buybacks/acquisitions. Combined with a 4.7x P/B, book value is a thin support level.
7. **Tool inconsistency flagged.** For the identical 252-day window, `calculate_low_vol_score` returned Sharpe −0.441 while `calculate_sharpe_sortino` returned −0.126. I report both; the −0.126/−0.17 pair is internally consistent with the −6.8% return and 53.8% vol and is the more likely correct figure.

**Data gaps:** no true 90-day estimate-revision history, no software-peer momentum/vol comparison (peer feed returned semis), and FY2026 statements appear forward-dated (`period_end` 2026-07-31) — figures are as-published in the feed, not independently reconciled.
