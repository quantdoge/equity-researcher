# Quant Analyst

- Symbol: MRVL
- Elapsed: 75.7s

---
All data gathered. Here is the completed quantitative profile for **MRVL (Marvell Technology, Inc.)** — semis/Technology, mkt cap ~$237B, price ~$272.

---

## 1. Factor Scores Table

| Factor | Score / Raw | Sector Rank (5-name semi peer set)* | Signal |
|--------|-------------|-------------------------------------|--------|
| Value | P/E 88.6, EV/EBITDA 52.6, P/FCF 169.4 | 4/5 (richer than NVDA 48/40/60, AVGO 76/52/65, MU 14/11/21; only AMD 238/141/153 is pricier) | **Poor** |
| Momentum | 12-1m total return **−20.5%** | 5/5 — **worst** in set (NVDA +17.7%, AMD −10.3%, AVGO −5.5%) | **Negative** |
| Quality | ROE 18.7%, GP/assets 0.188, accruals +0.041, Piotroski 6/9, ROIC 7.0% | ~4/5 (GP/assets lowest of set; ROE below NVDA 76% / AVGO 29%, above AMD 7%) | **Low** |
| Low Vol | Ann. vol **85.1%**, beta vs SPY **3.11** | 5/5 — highest beta/vol in set | **Poor** |
| Earnings Revision | +34.0% upgrade (EPS est 18.49 vs 13.80) | 1/5 — only name with consensus EPS upgrades | **Bullish (thin sample)** |

\* The `rank_universe_by_factor` tool rejected both list and string universe formats (schema error), so global/sector percentiles are **approximated vs a 5-name direct-comparable set** (NVDA, AMD, AVGO, MU plus MRVL). Cross-sectional z-scores vs the full universe are **unavailable** — treat ranks as directional, not precise.

**Earnings-revision caveat:** the +34% compares the FY2031 consensus (18.49, n=9 analysts) vs the FY2030 figure (13.80, n=7) — a **far-dated forward period with thin, shrinking coverage**. Signal direction is credible (steep ramp: FY28→FY31 EPS 6.76 → 10.47 → 13.80 → 18.49; revenue 18.2B → 47.0B) but the magnitude is statistically fragile.

---

## 2. Price Statistics (252-day window vs SPY)

| Stat | Value | Note |
|---|---|---|
| Alpha (annualised) | **+133.1%** | **Unreliable** — R² = 0.23; market model explains little, alpha is a residual artifact of the extreme re-rating |
| Beta | **3.13** | Very high; ~3× market sensitivity |
| R² | 0.23 | Low explanatory power |
| Sharpe | **2.19** | High, but driven by one recent burst, not stability |
| Sortino | **3.69** | Strong downside-risk-adjusted return |
| Ann. return window | +187.9% | +55% total return over the year |
| Max drawdown | **−48.4%** | Severe — the stock halved intra-year |
| Ann. volatility | 85.1% | ~3.5× the typical large-cap |

**Key tension:** 12-1 momentum is **−20.5%** while the 1-year total return is **+55%** — this means the entire year's gain plus more occurred in just the last ~21 trading days, after a deep drawdown. That is a violent, recent momentum reversal.

---

## 3. Composite Quant Signal

**SELL** (not Strong Sell: the +34% estimate-revision momentum and strong Sharpe/Sortino are genuine offsets, but every cross-sectional factor except revisions ranks bottom-decile within its peer set).

Rationale: top-quintile-on-all-three (value ∩ momentum ∩ quality) is the framework's buy condition; MRVL is top-quintile on **none** — worst momentum of its comps, richest FCF multiple of its comps, extreme beta, and only marginal earnings quality (GP/assets 0.19, accruals +0.041 near the 0.05 redline, Piotroski 6/9 with failures on leverage and dilution).

---

## 4. Key Quant Risk Flags

1. **Momentum reversal risk — acute.** The 12-1 signal is negative (−20.5%) and the entire +55% annual return is concentrated in the trailing month; 85% vol with a −48% max drawdown says this can mean-revert violently. Beta 3.11 × crowded AI-semis positioning = amplified downside in any sector derating.
2. **Factor crowding.** MRVL-NVDA correlation is only 0.37 but MRVL-ARM 0.57 / MRVL-AMD 0.55 / MRVL-MU 0.53 — it sits in the high-beta AI-infrastructure cluster at beta ~3, so it is the most levered expression of a crowded trade.
3. **Low liquidity / structural caveats:** negligible dividend (0.09%), ~7.5k employees, and valuation multiples (P/E 88.6, P/FCF 169) leave almost no margin of safety if FY25-27 consensus (EPS ~7 further out) disappoints.
4. **Statistical reliability flags:** alpha +133% at R²=0.23 should be ignored as a standalone bullish input; the +34% revision is on FY2031 with ≤9 analysts; peer ranks are from a 5-name set, not the full universe — all are directional, not precise.

*Analyst note: everything hinges on the AI custom-silicon ramp validating those far-future EPS estimates. The data support a disciplined posture: rich valuation + negative momentum + 3× beta = poor risk-adjusted entry at current levels despite the revision tailwind.*
