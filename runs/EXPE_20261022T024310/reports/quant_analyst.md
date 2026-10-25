# Quant Analyst

- Symbol: EXPE
- Elapsed: 182.3s

---
# EXPE — Expedia Group, Inc. | Quantitative Factor Analysis
**Sector:** Consumer Cyclical / Travel Services · **Price:** $285.64 · **Mkt Cap:** ~$32.7–37.7B (see note) · **Industry peer:** BKNG

---

## 1. Factor Scores Table

| Factor | Score / Raw | Sector Rank (Travel Svcs) | Signal |
|--------|-------------|---------------------------|--------|
| **Value** | P/E 29.1 · EV/EBITDA 16.1 · P/FCF 12.1 · P/B 14.8 | Mid — expensive vs BKNG on earnings, cheaper on FCF | **Neutral** |
| **Momentum (12-1)** | −2.58% total return | Top of pair (BKNG −10.6%) but absolute negative | **Sell / Negative** |
| **Quality** | ROE 50.8% · GP/Assets 0.543 · Accruals −10.6% · F-score 5/9 | Top — "high" quality signal vs BKNG "low" | **Buy** |
| **Low Vol** | Ann. vol 50.8% · β 0.857 · Max DD 37.2% | Bottom — vol >> BKNG 40.4% | **Sell / Poor** |
| **Earnings Revision** | +9.17% (fwd EPS 33.99 vs prior 31.13) | Mid — upgrade, but BKNG stronger (+16.1%) | **Buy** |

**Value detail:** Earnings multiples are full (P/E 29.1 vs BKNG 23.9; EV/EBITDA 16.1 vs 14.2), but FCF yield is genuinely attractive — P/FCF 12.1 implies ~8.3% FCF yield, and EXPE is *cheaper* than BKNG on cash flow (BKNG P/FCF 14.2). A "cheap-on-cash, expensive-on-earnings" split → Neutral composite.

**Quality detail:** Best-in-pair. Accruals ratio of −10.6% (net income $1.29B vs operating CF $3.88B) signals very high cash conversion — no earnings-quality red flag. ROE 50.8% is partly leverage/negative-tangible-book driven (P/B 14.8), so treat ROE with caution; the more reliable signals are GP/Assets and accruals. Piotroski F-score 5/9 (Moderate) — deductions on ROA improvement, leverage, equity change, and asset turnover.

---

## 2. Price Statistics (252-day window, vs SPY)

| Metric | Value |
|--------|-------|
| **Alpha (annualized)** | **−6.37%** |
| **Beta** | 0.857 (calc) / 0.862 (regression); company-reported β 1.362 |
| **R² (vs SPY)** | 0.049 — *very low; ~95% of variance is idiosyncratic* |
| **Annualized volatility** | 50.8–51.0% |
| **Annualized return** | 20.85% |
| **Sharpe ratio** | 0.409 (dedicated calc) / 0.145 (low-vol module) |
| **Sortino ratio** | 0.551 |
| **Max drawdown** | −37.2% |

**Note on Sharpe discrepancy:** two modules return 0.409 vs 0.145 for the same window — I flag this as a data inconsistency. Using the dedicated Sharpe/Sortino tool (0.409/0.551) as primary; either way, risk-adjusted return is weak-to-mediocre.

---

## 3. Composite Quant Signal: **NEUTRAL** (slight negative tilt)

The factors split cleanly: **Quality (+)** and **Earnings Revision (+)** are offset by **Momentum (−)**, **Alpha (−6.4%)**, and **elevated volatility (50.8%, −37% max DD)**. Low R² (0.049) means the beta estimate is statistically fragile — EXPE trades on company-specific travel-cycle news, not market direction. No factor cluster justifies a directional call; momentum and risk metrics argue against a Buy despite strong fundamentals.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal / continuation risk** — 12-1 momentum is −2.58% and BKNG peer is −10.6%; the whole Travel Services group is in a downtrend. Negative alpha (−6.4%) confirms underperformance vs benchmark.
2. **Statistical fragility of beta/alpha** — R² = 0.049 means the 252-day regression explains almost none of EXPE's returns; alpha and beta estimates carry wide error bars. Do not over-trust these figures.
3. **High volatility / drawdown** — 50.8% annualized vol and −37.2% max drawdown are severe; position sizing should reflect this.
4. **ROE distortion** — 50.8% ROE rests on a thin/leveraged equity base (P/B 14.8). Quality should be judged on accruals and GP/Assets (both favorable), not headline ROE.
5. **Estimate horizon caveat** — the revision metric compares a 2030 forward estimate (33.99 vs 31.13); only 7 analysts cover the 2030 period vs 22 for 2027. The +9.17% upgrade is directionally positive but thinly covered — lower confidence.
6. **Market-cap inconsistency** — profile ($32.7B) vs valuation module ($37.7B) differ; likely share-count/timing mismatch. Use with caution.

**Data gaps:** True cross-sectional percentile ranks require a fuller Travel Services cohort; only BKNG is a clean comp (AMZN/TSLA/HD etc. in the broad "Consumer Cyclical" peer list are not travel comps). Ranks above are pair-relative, not full-universe quintiles.
