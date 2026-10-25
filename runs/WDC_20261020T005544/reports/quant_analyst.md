# Quant Analyst

- Symbol: WDC
- Elapsed: 161.3s

---
## WDC — Quantitative Factor Report
*Western Digital Corp. | Technology / Computer Hardware (HDD + NAND flash) | Mkt cap ~$131.8B | Price $352.21*

**Data caveats up front:** The sector-peer feed returns only mega-cap platform semis (NVDA, AAPL, MSFT, TSM, AVGO, MU) — **not true storage comps like Seagate (STX)**. "Sector Rank" below is therefore an *estimated* quintile, not a computed cross-sectional z-score. Sample size = 1 year of daily data (~252 obs), adequate for vol/alpha but the momentum and revision signals carry internal inconsistencies flagged below.

### 1. Factor Scores Table

| Factor | Score | Est. Sector Rank | Signal |
|--------|-------|------------------|--------|
| **Value** | P/E 14.5 · EV/EBITDA 13.1 · P/FCF 38.4 | 2nd quintile (cheap on earnings, rich on cash) | Neutral / Mild + |
| **Momentum** | −23.1% (12-1) | 5th quintile | **Negative** |
| **Quality** | ROE 106% · GP/Assets 0.455 · Accruals 0.396 · F-Score 7 | 4th quintile | **Low** |
| **Low Vol** | Ann. vol 81.5% · β 2.92 · MaxDD −55.5% | 5th quintile | **Very Negative** |
| **Earnings Revision** | +48.2% (fwd EPS 65.73 vs 44.36) | 1st quintile* | Upgrade (low confidence*) |

\* **Revision flag:** The revision tool compares a **2030-07-03** forward period (5 years out) — a mislabeled/far-dated consensus bucket, not the near-term FY. Meanwhile the *price-target* tape shows recent **PT cuts** (Wells Fargo $730→$450, UBS $525→$470 in Oct). Treat the +48% "upgrade" as high-magnitude but **low-reliability**; the live analyst action is decelerating.

### 2. Price Statistics (1Y, vs SPY)

| Metric | Value |
|--------|-------|
| Annualised return | +84.4% |
| Alpha (annualised) | **+56.4%** |
| Beta | **2.94** |
| R² | 0.224 (only ~22% market-explained → mostly idiosyncratic) |
| Annualised vol | 81.5% |
| Sharpe (0% rf) | 1.03 |
| Sortino (0% rf) | 1.65 |
| Max drawdown | **−55.5%** |

**Divergence flag:** Total 1Y return (+84%) and Sharpe (1.03) are strongly positive, yet 12-1 momentum is −23% and the 8-week price tape shows $578→$352. The stock peaked mid-2026 and is in a violent correction; the trailing-return stats are being flattered by an earlier run-up that the 12-1 window captures as a peak-to-trough. **The two measures disagree — treat the +84% return as stale.**

### 3. Composite Quant Signal: **NEUTRAL (High-Risk)**

Justification: Genuine positives are the large positive alpha, top-tier value on earnings multiples, a cheap P/E, and an elevated (if unreliable) revision print. These are offset by **bottom-quintile momentum, extreme 2.9 beta / 82% vol, a −55.5% drawdown, and a warning-level accruals ratio (0.396)** — 2026 net income of $9.42B vs operating cash flow of only $3.93B means earnings are running far ahead of cash. A high-beta AI-storage cyclical that has already doubled and is rolling over is not a factor-model "buy"; it's a momentum-reversal short candidate on the risk-adjusted stack despite the cheap headline multiple.

### 4. Key Quant Risk Flags
- **Earnings-quality deterioration:** Accruals ratio 0.396 (vs 0.012 prior year) = red flag; net income >> operating cash flow. F-Score loses the accruals point (F4=0) and the dilution point (F7=0).
- **Momentum reversal risk:** Bottom-quintile 12-1 momentum while sitting on a −55% peak-to-trough drawdown — classic late-cycle de-rating pattern.
- **Factor crowding / high beta:** β 2.94 vs SPY with low R² (0.22) means chiefly a levered AI-storage/thematic proxy; any rotation out of the trade hits it 3× the market.
- **ROE 106% is not quality** — it is a thin/near-zero book-equity artifact; do not read it as capital efficiency.
- **Revision signal unreliable** (5-yr-dated period) and contradicted by falling price targets.
- **Liquidity:** not a concern — mega-cap, ~$130B.

*Bottom line for the memo: WDC screens as a cheap-multiple, high-alpha, but low-quality, high-volatility, negative-momentum name. On a pure factor composite it is Neutral; the risk-adjusted profile (Sortino 1.65 vs vol 82%, β 2.9) argues for position-size discipline, not conviction long.*
