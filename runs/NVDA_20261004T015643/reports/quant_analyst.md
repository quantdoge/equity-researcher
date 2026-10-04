# Quant Analyst

- Symbol: NVDA
- Elapsed: 97.2s

---
All data gathered. Compiling the quantitative report.

---

# NVDA — Quantitative Factor & Risk Analysis
*Data as of latest available (price $233.95, mkt cap ≈ $5.74T)*

## 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| Value | P/E 47.7, EV/EBITDA 39.3, P/FCF 59.3, P/B 36.4 | Bottom quartile of mega-cap universe (12/15; only AVGO/LLY pricier) | **Very Expensive** |
| Momentum | +14.8% (12-1 mo) | #2 of 15 mega-caps (behind MSFT +39.9%) | **Positive, moderate** |
| Quality | ROE 76.3%, GP/Assets 0.74, ROIC 77.3% | #3 of 15 (behind AAPL, LLY) | **High profitability, weak accruals** |
| Low Vol | Vol 37.8%, Beta 1.88 | Worst decile | **Negative** |
| Earnings Revision | −13.0% (EPS est. 20.0 vs 23.0 prior) | Downgrade | **Sell signal** |

## 2. Price Statistics (252d, vs SPY unless noted)

| Statistic | Value |
|-----------|-------|
| Alpha (annualized) | **+3.85%** |
| Beta | **1.886** (R² = 0.43 — high idiosyncratic component) |
| Sharpe | **0.97** (0% rf assumption) |
| Sortino | **1.64** |
| Annualized return / vol | +36.9% / 38.2% |
| Max drawdown | **−19.3%** |
| Peer return corr. | TSM 0.63, AVGO 0.51, AMD 0.48, MU 0.41; AAPL 0.07, MSFT 0.21 |

## 3. Composite Quant Signal: **NEUTRAL**

The cross-sectional picture is genuinely split. Positive contributors: strong relative momentum vs mega-cap peers and elite capital productivity (ROIC 77%, ROE 76%). Negative contributors: top-quartile-expensive valuation, near-2.0 beta / ~38% volatility, an EPS-estimate downgrade, and an accruals warning (0.084, above the 0.05 threshold) plus a Piotroski F-score of just 5 — profitability flags all pass, but efficiency/accrual flags (F3, F4, F8, F9) fail, signalling decelerating operating momentum from extraordinarily high levels.

## 4. Key Quant Risk Flags

- **Earnings-momentum reversal:** Revisions −13% and long-dated consensus shows decay (FY2030 EPS est. $23 → FY2031 $20), consistent with a post-drawdown reset of AI-capex expectations. Recent PT prints are split: Truist $346 / Piper $300 / D.A. Davidson $300 bullish, but Morgan Stanley ($230) and Wells Fargo ($210) sit *below* spot — a rare sign of target dispersion at the top.
- **Factor crowding (AI/semis):** Return correlation to TSM (0.63), AVGO (0.51), AMD (0.48), MU (0.41) shows NVDA is the epicentre of a crowded semicap trade; a de-rating would hit the complex simultaneously. Low correlation to AAPL/MSFT means little diversification hedge inside the mega-cap set.
- **High-beta, high-drawdown:** 38% vol, β≈1.9, −19.3% max DD in a year with only +15% momentum — the stock carries most of the market's AI risk with limited compensative alpha (+3.9%).
- **Liquidity:** Not a risk — ~$5.7T mega-cap, deepest tape in the market.

## Methodology Caveats
- Cross-sectional ranks use the bounded mega-cap universe (25 names incl. index funds), not the full ~40k FMP screen — treat rank as "within large-cap tech leaders," not the whole market.
- Revision signal is measured on a FY2031 forward period (est. supported by only ~10 analysts) — low statistical confidence; treat direction, not magnitude.
- Sharpe/Sortino assume 0% risk-free; alpha/beta from 252-day OLS with R² 0.43 (weak fit, alpha estimate noisy).

**Bottom line:** Momentum + elite profitability are real, but at 47× trailing earnings with a beta near 2, an accruals warning, and negative revision momentum, the quant stack does not justify chasing at spot. NVDA screens as a high-quality **hold** — the rare profile where story and numbers agree on "great company, demanding price, crowded trade."
