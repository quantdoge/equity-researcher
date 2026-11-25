# Quant Analyst

- Symbol: KYMR
- Elapsed: 100.5s

---
## KYMR — Quantitative Factor & Risk Report
*Data as of close 2026-11-24: $173.92 | Mkt cap $14.85B | EV $13.91B | Healthcare / Biotechnology (clinical-stage, pre-revenue)*

### ⚠️ Data-integrity finding (read first)
The momentum tool returned **-3.16%** for a 252-day lookback. I reverse-engineered this: **117.57 / 121.41 − 1 = −3.16% exactly** — i.e. the prices from **2026-10-27** and **2026-08-17**. The tool's price series is truncated to ~71 trading days, so a "252-day" request was silently clamped to a ~50-day window. **The reported momentum figure is invalid.** Recomputing from the raw daily series: P(2025-11-24)=$65.59 → P(2026-10-27)=$117.57 = **+79.2% 12-1 momentum**, not −3.2%. The two Sharpe readings (1.586 vs 1.79) and the max-drawdown figure (−24.98%, which I cannot reproduce in any 12-month window) point to inconsistent feed windows across tools. Treat all tool outputs as indicative and the recomputed figures as authoritative.

### 1. Factor Scores
| Factor | Score / Raw | Sector Rank (biotech peer set) | Signal |
|---|---|---|---|
| **Value** | P/E −47.1, EV/EBITDA −45.9, P/FCF −62.6, P/B 9.29 | **N/A** — no earnings/FCF denominator | **Not investable on value.** EV = 39.8× *2030E* revenue ($349M); 2027–29E revenue is only $40–72M |
| **Momentum** | **+79.2%** (12-1, recomputed) vs tool's −3.16% | **1 of 4** (NUVL +18.0%, RVMD −12.2%, ARVN −19.0%) | **Strong positive** — top of peer set |
| **Quality** | ROE −19.7%, ROIC −21.0%, GP/assets 0.023, accruals −0.045 | Bottom quintile on profitability | **Negative** (accruals clean, but no earnings) |
| **Low Vol** | 61.8% ann. vol, β 1.579 vs SPY (1.237 vs XBI), max DD 25.0% | **Highest beta of peer set** | **Negative** — anti-low-vol |
| **Earnings Revision** | +17.97% (FY2030 EPS −6.25 → −5.12), 13 analysts | Positive | **Positive but low-information** (
