# Quant Analyst

- Symbol: NET
- Elapsed: 51.9s

---
# Cloudflare, Inc. (NET) — Quantitative Factor Analysis

**Price:** $328.44 | **Market Cap:** ~$117.6B | **Sector:** Technology / Software–Infrastructure | **Beta (profile):** 1.645

## 1. Factor Scores Table
Sector rank = cross-sectional position within same-industry peer set {NET, MSFT, PLTR, CSCO} (1 = best of 4).

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | P/E n/m (loss-making); EV/EBITDA 1,078×; P/FCF 353×; P/B 78× | **4 / 4** (most expensive) | **Strong Sell** — extreme premium |
| **Momentum** | 12-1 return **+27.5%** | 3 / 4 | **Buy** (positive, but behind PLTR 41.6% & MSFT 29.6%) |
| **Quality** | ROE −7.0%; ROIC −4.0%; GP/Assets 26.8%; Piotroski F **4** ("Weak"); accruals −12.7% (good) | **4 / 4** | **Sell** — unprofitable despite positive accruals quality |
| **Low Vol** | Ann. vol **69.9%**; beta 1.49; max DD 27.3% | 3 / 4 | **Sell** — high-vol name |
| **Earnings Revision** | Fwd EPS est. revised **+28.2%** over 3mo (2030 period: 3.36 → 4.31) | n/a (peer data unavailable) | **Strong Buy** — clear upward revision momentum |

**Factor conflict:** The model is split — valuation/quality are bottom-of-peer-group (bearish) while momentum and estimate revisions are firmly bullish. Classic expensive, high-growth momentum profile.

## 2. Price Statistics (252-day window, vs SPY)
| Metric | Value | Note |
|--------|-------|------|
| Alpha (annualised) | **+79.6%** | ⚠️ **Not statistically robust** — see R² |
| Beta | **1.49** | ~1.5× market sensitivity; regression and vol-calc agree |
| R-squared | **0.077** | Only ~8% of variance explained by SPY → ~92% idiosyncratic |
| Sharpe ratio | **1.269** | Solid, but return-driven (0% RF assumption) |
| Sortino ratio | **1.685** | Favourable; limited downside deviation vs total vol |
| Annualised return | +87.8% | |
| Annualised volatility | 69.2–69.9% | Very high |
| Max drawdown | −27.26% | |

## 3. Composite Quant Signal: **NEUTRAL (momentum-tilted)**
Momentum (+27.5%) and estimate-revision momentum (+28.2%) argue Buy; valuation (EV/EBITDA >1,000×, P/FCF 353×) and quality (negative ROE/ROIC, F-score 4) argue Sell. These offset to a **Neutral** composite — a high-conviction directional call is not supported by the factor spread. A momentum/trend-following mandate could justify a tactical Buy; a value/quality mandate would screen it out entirely.

## 4. Key Quant Risk Flags
- **⚠️ Alpha is statistically fragile.** R² = 0.077 means the +79.6% "alpha" carries a very wide standard error — returns are almost entirely idiosyncratic, so the alpha estimate is not reliable and should not be treated as skill. *One-year daily sample (n≈252) is a single regime; insufficient for robust factor inference.*
- **Valuation / factor-crowding risk.** EV/EBITDA 1,078× and P/FCF 353× vs peer MSFT 19×/59× and CSCO 22×/34×. Extreme premium embeds near-flawless multi-year execution; highly crowded growth trade.
- **Momentum-reversal risk.** High-flying name with 69.9% vol and a −27% drawdown within the window — sharp mean-reversion episodes are likely; momentum is positive but ranked only 3/4 and decelerating vs MSFT/PLTR.
- **Leverage/beta risk.** Beta 1.49 amplifies market drawdowns; high-vol screen places it bottom-tier on risk-adjusted defensiveness.
- **Profitability gap.** Still GAAP loss-making (net income −$102M) with negative ROIC; F-score 4/9 flags weak fundamentals — quality is structurally impaired.
- **Data gaps:** Peer earnings-revision scores and true forward-period consensus unavailable → revision rank not benchmarked; treated as an absolute signal only. Liquidity is *not* a concern (large-cap, ~$117B).
