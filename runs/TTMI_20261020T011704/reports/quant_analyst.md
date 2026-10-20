# Quant Analyst

- Symbol: TTMI
- Elapsed: 110.3s

---
# TTMI (TTM Technologies, Inc.) — Quantitative Factor Analysis

*Sector: Technology / Hardware, Equipment & Parts. Price: $99.10; Mkt Cap: ~$10.45B. Data window: trailing 252 days.*

---

## 1. Factor Scores Table

| Factor | Score / Raw | Sector Rank | Signal |
|--------|-------------|-------------|--------|
| **Value** | P/E 59.0, P/B 5.93, EV/EBITDA 27.5, P/FCF n.m. (≈0/neg.) | Bottom quintile (expensive) | **Bearish** |
| **Momentum (12-1)** | −15.31% | Below median | **Bearish** |
| **Quality** | Low composite (ROE 10.1%, GP/Assets 0.148, accruals −0.030) | Mid/low | **Neutral–Weak** |
| **Low Vol** | Ann. vol 85.4%, beta 3.28 | Bottom quintile | **Strongly Bearish** |
| **Earnings Revision** | +20.35% (FY28 EPS $8.71 vs $7.24 prior) | Positive | **Bullish** (thin coverage) |

**Notes on each factor:**
- **Value:** Unambiguously expensive on every multiple. P/FCF of −15,301 is not meaningful — it reflects near-zero/negative free cash flow (heavy capex against $292M OCF), not a valuation signal. Flag as a data-quality caveat rather than a metric.
- **Quality:** Mixed. Piotroski **F-Score = 8 (Strong)** and negative accruals (good earnings quality), but absolute returns on capital are only middling (ROE 10.1%, ROIC 9.1%). ROIC is on a clear improving trajectory (1.67% → 4.50% → 9.09%), which is the bullish thread.
- **Low Vol:** Worst-in-class. 85% annualized vol and beta ~3.3x place this in the highest-risk bucket.
- **Earnings Revision:** +20.35% upgrade is a genuine positive, **but only 2 analysts** cover the out-year — low statistical significance; treat with caution.

---

## 2. Price Statistics

| Metric | Value |
|--------|-------|
| Alpha (ann., vs SPY) | **+19.34%** |
| Beta (vs SPY, OLS) | **3.30** (profile lists 2.14 on longer window) |
| R² (vs SPY) | 0.257 — only 26% of variance market-explained; high idiosyncratic risk |
| Sharpe ratio | **0.40** (33.61% ann. return / 83.4% vol)* |
| Sortino ratio | **0.62** |
| Annualized return | +33.61% |
| Annualized volatility | 83.4–85.4% |
| Max drawdown | **−57.61%** |

\*A secondary vol-based Sharpe of 0.79 appears via a different annualization convention; the return/vol ratio of **0.40** is the internally consistent figure and the one I rely on.

---

## 3. Composite Quant Signal: **NEUTRAL (high-risk)**

The book is a tug-of-war. **Bulls** point to strong alpha (+19% vs SPY), positive estimate revisions (+20%), a strong F-Score (8), improving ROIC, and clean accruals. **Bears** point to a rich valuation (59x P/E, 27x EV/EBITDA), no free cash flow, the worst low-vol profile in the market (beta 3.3, 85% vol), a −58% maximum drawdown, and a *negative* 12-1 momentum print. The two dominant cross-sectional factors for a stock like this — **value and low-vol** — both score bottom-quintile, so it does not clear the bar for a Buy despite genuine quality improvement. Net: **Neutral**, appropriate only for high-risk-tolerance capital with a catalyst-driven view.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal risk (high):** 12-1 momentum is **−15.3%** while trailing-12M total return is **+33.6%** and the latest analyst price ($231 target, Oct-2026) sits far above the $99 spot. This divergence implies a violent recent move; 12-1 negative + short-term spike is the classic setup for mean-reversion.
2. **Factor crowding / extreme volatility:** Beta 3.3 and 85% vol put this in the most crowded, highest-beta risk bucket — acute drawdown exposure (realized −57.6% already) and likely to amplify any market selloff (R² only 0.26, so much of the risk is stock-specific, not hedgeable via index).
3. **Valuation + FCF gap:** 59x P/E and 27x EV/EBITDA with **near-zero/negative free cash flow**. The whole multiple rests on the *out-year* (FY28) earnings ramp — but that estimate carries **only 2 analysts**, so revision momentum is statistically fragile.
4. **Liquidity/data caveats:** Deep-cap equity, so liquidity itself is adequate; however, peer benchmarking against the returned "Technology" set (NVDA, AAPL, MSFT…) is **not a true comparable group** — a proper PCB/hardware peer set (e.g., Sanmina, Benchmark Electronics) would materially change sector-relative rankings. Sector ranks above are directional, not quintile-precise.

*Sample sizes: single 252-day price window; consensus forward estimates backed by 2 analysts only — treat revision signal and out-year multiple as low-confidence.*
