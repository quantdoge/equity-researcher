# Quant Analyst

- Symbol: SNDK
- Elapsed: 53.0s

---
# SNDK — Quantitative Factor Report

**Company:** SanDisk Corp. | Technology / Computer Hardware (NAND flash) | Price snapshot used by valuation tools: **$809.11**; latest OHLCV close (2026-07-31): **$1,214.83**

> ⚠️ **DATA INTEGRITY FLAG (read first):** The tool suite returns three inconsistent price snapshots. Valuation ratios/profile use **$809.11**; the price history ends at **$1,214.83** (2026-07-31); price targets reference **$1,150–$1,704** (Aug–Oct 2026). Multiples below are shown at *both* prices. Also: SNDK only began trading as a standalone entity in **Feb 2025 (~370 trading days)** — every 252-day statistic here is estimated on a **very short, single-regime sample** and should be treated as low-confidence.

## 1. Factor Scores Table

| Factor | Raw Value | Score (1–5) | Sector Rank | Signal |
|---|---|---|---|---|
| **Value** | P/E 10.97 · P/B 7.97 · EV/EBITDA 9.14 · P/FCF 10.91 (at $809) | **4** | 2 of 2 memory peers (MU cheaper on P/E); **top quintile vs broad semis** | Cheap |
| **Momentum** | 12-1 return **+13.11%** | **3** | 1 of 2 (vs MU +3.13%) | Positive but decelerating |
| **Quality** | ROE 72.7% · ROIC 76.8% · GP/Assets 0.643 · Accruals −0.011 · F-Score 7 | **5** | **1 of 2** (beats MU on ROE 61.4%, GP/A 0.549) | Strong (cycle-peak) |
| **Low Vol** | Ann. vol **111.4%** · Beta **3.94** · Max DD **65.5%** | **1** | 2 of 2 (MU vol 87.9%, beta 3.41) | Worst quintile |
| **Earnings Revision** | 2030 EPS −0.73% (297.84 vs 300.04) | **3** | Inconclusive (n=1) | Neutral / stale |

**Cross-sectional note:** The Technology sector list returned is dominated by mega-caps (AAPL, MSFT, NVDA, TSM, AVGO). The only clean NAND/DRAM comparables are **MU** and **SK hynix (SKHY)**; I computed MU directly as the anchor. SKHY metrics were not pulled (budget) — a gap.

## 2. Price Statistics

| Metric | Value | Comment |
|---|---|---|
| Alpha (ann., vs SPY) | **+62.65%** | ⚠️ **t-stat ≈ 0.65 — NOT statistically significant** |
| Beta (1y, OLS) | **3.96** | Range 3.94–5.65 across methods/windows |
| R² | **0.262** | 74% of variance is **idiosyncratic** |
| Sharpe (252d) | **0.91** | On 111.8% vol — wide CI |
| Sortino (252d) | **1.55** | Downside better-behaved than total vol |
| Ann. Return | **+101.8%** | Single-year, single-regime |
| Ann. Volatility | **111.8%** | Extreme |
| Max Drawdown | **−65.5%** | From ~$2,335 (Jun-26) to ~$1,016 (Jul-29) |

**Key statistical caveat:** With idiosyncratic vol ≈ 96%, the standard error on annualised alpha is roughly equal to the alpha itself. Neither the alpha (+62.6%, t≈0.65) nor the beta (t≈0.66) is distinguishable from noise at 95% confidence. The eye-catching alpha is an artefact of a short, explosive sample — **do not underwrite it.**

## 3. Valuation at Two Prices (reconciliation)

| Metric | At $809.11 (tool) | At $1,214.83 (latest close) |
|---|---|---|
| P/E | 10.97 | **~16.5** |
| P/B | 7.97 | ~12.0 |
| EV/EBITDA | 9.14 | ~13.9 |
| P/FCF | 10.91 | ~16.4 |

Still reasonable for a 70%-ROE franchise, but the "$809 cheapness" is partly a stale snapshot. On live price, SNDK is fairly-to-modestly valued, not deep value.

## 4. Composite Quant Signal: **BUY** (not Strong Buy)

Rare combination of **top-quintile Quality + Value** with **positive momentum** — the classic "cheap quality" screen. Held back from Strong Buy by: (1) momentum decelerating sharply (stock −48% off June peak), (2) worst-quintile Low-Vol score, (3) statistically insignificant alpha, and (4) earnings quality resting on a **memory-cycle peak** (ROE 73%, ROIC 77% are not sustainable levels).

## 5. Key Quant Risk Flags

1. **Momentum reversal risk — HIGH.** 12-1 momentum (+13%) masks a violent recent drawdown from ~$2,335 to ~$1,016 (−57% peak-to-trough intra-quarter). Classic late-cycle blow-off signature.
2. **Factor crowding / cyclicality.** Quality metrics are *peak-cycle* — ROE 73%, net margin in consensus (~$34B NI on ~$50B rev) is implausible and mean-reverting. Value trap risk if NAND pricing rolls over.
3. **Estimation instability (short sample).** ~18 months of history → alpha/beta/Sharpe all low-confidence. Beta estimates range 3.94–5.65.
4. **Extreme volatility & idiosyncratic risk.** 112% ann. vol, R² 0.26 — this is a high-beta (≈4x market) concentrated bet, not a diversified holding.
5. **Data-quality caveats.** (a) Three inconsistent price snapshots; (b) revision signal rests on **n=1 analyst** on the 2030 period — statistically meaningless; (c) consensus net-income estimates imply ~69% net margin, which I flag as a likely scaling/data error; (d) F-Score 7 (moderate) is dragged by lower leverage score and share dilution flags (F5, F7 = 0).
6. **Liquidity:** Adequate — mega-cap (~$115–190B depending on snapshot), heavy dollar volume; not a constraint.

**Bottom line:** Quantitatively a **cheap, high-quality, high-momentum** name — an attractive *factor* profile — but every one of those attributes is a **cyclical-peak reading on a 112%-vol, ~4-beta stock with a violently reversing tape.** The signal is Buy, but position sizing should reflect the drawdown and mean-reversion risk, and the headline alpha should be discounted as statistically insignificant.
