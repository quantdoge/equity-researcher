# Quant Analyst

- Symbol: AXP
- Elapsed: 40.0s

---
I have everything I need across two parallel rounds. Writing the final report now.

---

# AXP — American Express Co. (NYSE: AXP)
**Quant Factor & Risk Analysis** | Sector: Financial Services / Credit Services | Mkt Cap: ~$204B | Price: $302.78

*Note: `get_sector_peers` returned index funds (market-cap ordered), so "Sector Rank" below is computed against the direct payments/consumer-credit comps cohort (V, MA, COF, DFS, JPM) where data was available. DFS valuation data was stale/unavailable — flagged.*

## 1. Factor Scores Table

| Factor | Score | Cohort Rank (1=best, of 5) | Signal |
|--------|-------|---------------------------|--------|
| **Value** | 0.6 / 1.0 | 2 | **Favorable** — P/E 19.7, P/FCF 13.2, EV/EBITDA 14.1 vs V (35.4/32.9/27.4) and MA (33.4/29.3/24.7). Clear discount to network peers; COF cheaper on P/B (0.93 vs 6.30) and P/FCF (4.0 vs 13.2). P/B 6.3× is the blemish. |
| **Momentum** | −0.45 / 1.0 | 5 | **Negative** — 12–1m momentum **−3.45%**; trailing 12m total return **−26.1%**. Worst of the cohort. |
| **Quality** | 0.8 / 1.0 | 1 | **Strong** — ROE 32.4%, ROIC 15.1%, GP/assets 22.3%, accruals **−2.5%** (favorable), Piotroski **7/9**. *Caveat: the automated quality tool labels the composite "low" despite all three components reading favorable — likely a threshold quirk; I score the raw inputs as strong.* |
| **Low Vol** | 0.3 / 1.0 | 4 | **Weak** — Ann. vol 26.8% (elevated for a mega-cap); beta 0.93 vs SPY; max drawdown −23.8%. |
| **Earnings Revision** | 0.9 / 1.0 | 1 | **Positive (Upgrade)** — Forward (FY30) consensus EPS revised **+7.9%** (27.18 → 29.32) over 3 months. EPS ladder FY27→FY30: 20.14 → 23.02 → 27.18 → 29.32. |

## 2. Price Statistics (252-day, vs SPY)

| Statistic | Value |
|-----------|-------|
| Alpha (ann.) | **−40.6%** ⚠️ (R² = 0.21 — low explanatory power; treat with caution) |
| Beta | 0.94 |
| Sharpe (0% Rf) | **−0.97** |
| Sortino | **−1.20** |
| Ann. return / vol | −26.1% / 26.9% |
| Max drawdown | **−23.8%** |
| Correlations | COF **0.76**, JPM 0.56, V 0.43, MA 0.44 |

AXP trades like a **consumer-credit lender** (0.76 corr with COF), not a pure network (0.43–0.44 with V/MA) — it carries full credit-cycle exposure.

## 3. Composite Quant Signal: **NEUTRAL**

**Positives:** Top-quartile profitability (32% ROE), negative accruals (high earnings quality), +7.9% EPS estimate momentum, and a meaningful valuation discount to V/MA — a rare value+quality+revision combination for this name.

**Negatives:** Directionally negative price momentum (−26% 1yr), negative alpha, Sharpe/Sortino well below zero, elevated volatility, and a 23.8% drawdown. History says fighting a −26% trailing tape is costly.

The estimates are being raised *while* price targets are being cut (Evercore −14% to $320; UBS/MS drift lower) — a classic **multiple-compression** setup. With price at $302.78 vs a $315 low-context target, risk/reward is balanced, not skewed. Net: **Neutral** (leaning cautious; a confirmed momentum turn + maintained EPS upgrades would flip this to Buy).

## 4. Key Quant Risk Flags
- **Multiple-compression risk:** EPS revisions up +7.9% but every recent PT cut — market is de-rating the franchise, not the earnings. Watch forward P/E vs 15–18× range.
- **Credit-cycle beta:** 0.76 correlation with COF; AXP carries cardholder loan risk. Any delinquency/watchlist deterioration hits the name hard.
- **Momentum reversal risk (two-sided):** Negative momentum + positive revisions + oversold Sharpe is a contrarian setup, but there is no trend confirmation yet — do not average down early.
- **Factor crowding:** P/B 6.3× and 1.2% dividend yield make this a premium-franchise positioning; unwind risk if the value-quality cohort gets hit.
- **Statistical caveats:** Alpha/inferred beta regression R² = 0.21 (252 obs) — alpha is noisy; FY30 revision based on only 6 analysts; modeled revenue data shows a discontinuity (FY29 $104B vs FY30 $76B — likely a data aggregation quirk, use with care). DFS comp valuation unavailable.

*Liquidity is not a concern — mega-cap, deeply traded.*
