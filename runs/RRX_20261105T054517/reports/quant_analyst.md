# Quant Analyst

- Symbol: RRX
- Elapsed: 24.9s

---
# RRX — Regal Rexnord Corporation | Quantitative Factor Report

**Sector:** Industrials — Industrial Machinery | **Price:** $173.38 | **Mkt Cap:** ~$11.5B | **Reporting period:** FY2025

---

## 1. Factor Scores Table

| Factor | Score / Raw Metric | Sector Rank (est.) | Signal |
|--------|-------------------|-------------------|--------|
| **Value** | P/E 41.1x · EV/EBITDA 13.4x · P/B 1.68x · **P/FCF 12.9x (7.7% FCF yield)** | 2nd quintile | Neutral |
| **Momentum** | 12-1M **−18.9%** · 6M +4.8% | Bottom quintile | Negative |
| **Quality** | ROE **4.1%** · GP/Assets 15.9% · Accruals −5.1% · **F-Score 8/9** | Mid | Mixed / Neutral |
| **Low Vol** | Ann. vol **55.9%** · Beta 2.20 | Bottom quintile | Negative |
| **Earnings Revision** | +18.5% (2030 EPS) — **1 analyst only** | n/a (low confidence) | Upgrade (weak) |

**Factor detail**
- **Value:** The headline P/E of 41.1x looks expensive, but it's distorted by depressed earnings (ROE 4.1%). On cash flow it's genuinely cheap — P/FCF 12.9x and EV/EBITDA 13.4x are undemanding vs. industrial-machinery norms. Split verdict.
- **Quality:** Contradictory. Trailing profitability is poor (ROE 4.1%, ROIC 5.75%, ROA 2.0%) — below cost of capital in most years. But the balance sheet is clean: **negative accruals (−5.1%)** every year since 2022 = high earnings quality (cash exceeds accounting profit), and **Piotroski F-Score 8/9** (only asset-turnover fails). This is a "self-help / deleveraging" profile — low returns now, strong cash conversion, improving trajectory (ROE −0.9% → 3.1% → 4.1% over 3 yrs).
- **Momentum:** The classic 12-1 momentum is firmly negative (bottom quintile). But the 6-month figure is **+4.8%**, indicating a short-term reversal/inflection off the lows. This is a nascent turnaround, not a confirmed uptrend.
- **Low Vol:** Weakest factor. 55.9% annualized vol and beta 2.2 (vs SPY) put RRX in the highest-risk cohort of Industrials — consistent with a levered (EV $16.1B vs mkt cap $11.5B), cyclical, mid-cycle-recovery name.

---

## 2. Price Statistics (252-day window, vs SPY)

| Metric | Value |
|--------|-------|
| Annualized return | **−11.37%** |
| Annualized volatility | 54.2–55.9% |
| **Alpha (annualized)** | **−0.73%** |
| **Beta** | **2.21** (R² 0.27) |
| **Sharpe ratio** | **−0.21** |
| **Sortino ratio** | **−0.28** |
| Max drawdown | **−37.9%** |
| Return / risk profile | Negative edge, high sensitivity |

**Interpretation:** Strongly negative risk-adjusted performance. Negative Sharpe *and* Sortino mean RRX has destroyed risk-adjusted value over the trailing year, and Sortino < Sharpe confirms downside volatility is the dominant driver. **Beta 2.21 with R² of only 0.27** is a red flag — the stock carries double the market's systematic risk, yet three-quarters of its variance is idiosyncratic (stock-specific), meaning it is *not* a clean market proxy and adds large unique risk to a portfolio.

---

## 3. Composite Quant Signal

### **NEUTRAL** (leaning cautious)

The factors genuinely conflict, and no clean edge exists:
- **Positives:** Cheap on cash flow (P/FCF 12.9x), strong F-Score (8), pristine accruals, upward long-term EPS revisions, and 6-month momentum just turned positive.
- **Negatives:** Negative 12-1 momentum, very high volatility (56%), beta >2, negative Sharpe/Sortino, and weak current returns on capital (ROIC 5.75% < ~WACC).

This is a **show-me turnaround**, not a factor-clean long. It fails a quality screen on profitability and a momentum screen outright; it only passes a value screen when you use cash-based (not earnings-based) multiples. Quantitatively it does not stack up as a Strong Buy or Buy on any rigorous multi-factor basis.

---

## 4. Key Quant Risk Flags

1. **⚠️ Estimate-revision signal is low-confidence.** The +18.5% "upgrade" is for the **2030** consensus and rests on **a single analyst** (revenue: 3). The nearer-term 2027 estimate has 8 analysts but I could not pair it to a 3-months-prior value, so the revision direction is *unreliable* — do not overweight this signal.
2. **⚠️ Momentum reversal / whipsaw risk.** 12-1M is −18.9% while 6M is +4.8% — a violent reversal. High-beta turnaround names with weak R² (0.27) are prone to sharp two-way swings; position sizing must respect 56% vol.
3. **⚠️ Factor crowding:** N/A on momentum (it's a bottom-quintile name, so no crowding). But it *is* a crowded "industrial turnaround/deleveraging" narrative — watch for value-trap dynamics if ROIC fails to climb above cost of capital.
4. **⚠️ Data reconciliation:** The low-vol module reported a Sharpe of **0.559**, which conflicts with the −0.21 Sharpe from the dedicated Sharpe/Sortino engine and with the −11.4% trailing return. I treat the **−0.21 as authoritative** (it reconciles with return/vol arithmetic); the 0.559 appears to be a stale/different-window artifact. Similarly, profile beta (1.09, likely 5-yr monthly) differs sharply from the 252-day daily beta (2.20) — both are "true," just different windows; use the 2.2 for near-term risk management.
5. **Leverage / cyclicality:** EV ($16.1B) vs equity ($11.5B) → D/E ~0.4 on an EV basis; combined with Industrials cyclicality and beta 2.2, RRX is a high-beta recovery bet sensitive to rate and industrial-demand shocks.

---

### Bottom line for the memo
RRX is a **cash-cheap, quality-improving, high-risk turnaround**. Quantitatively: **Neutral**. The value case rests entirely on depressed-earnings normalization (P/FCF 12.9x) and self-help deleveraging (F-Score 8, negative accruals), but negative 12-1 momentum, 56% volatility, beta 2.2, and negative Sharpe/Sortino cap conviction. **Verify near-term EPS revision direction with ≥5 analysts before upgrading** — the current upgrade signal is a single-analyst 2030 datapoint and should not be traded on.

*(Note: Peer-by-peer factor z-scores were not computed — the sector-peer list returned only mega-caps (GE, CAT, RTX, BA, etc.) that are not clean comparables to a $11.5B mid-cap machinery name, so sector ranks above are directional estimates from absolute metrics, not true cross-sectional quintiles.)*
