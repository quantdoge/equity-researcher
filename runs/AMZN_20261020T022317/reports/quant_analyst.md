# Quant Analyst

- Symbol: AMZN
- Elapsed: 56.8s

---
# AMZN — Quantitative Factor Report

**Price:** $262.45 | **Mkt Cap:** $2.83T | **Sector:** Consumer Cyclical / Specialty Retail | Data as of FY2025 (12/31/25)

---

## 1. Factor Scores Table

| Factor | Score (raw) | Sector/Universe Rank | Signal |
|---|---|---|---|
| **Value** | P/E 36.6 · EV/EBITDA 17.4 · P/FCF 369.3 · P/B 6.91 | 10th of 17 mega-caps (~59th pct); **most expensive P/E** in reliable peer set | **Negative** |
| **Momentum (12-1)** | **+5.34%** | 7th of 25 (~72nd pct) | **Mildly Positive** |
| **Quality** | ROE 18.89% · GP/Assets 0.441 · Accruals **−0.0756** | 12th of 25 (~52nd pct); top-quartile accruals | **Positive (decelerating)** |
| **Low Vol** | Vol **35.0%** · Beta **1.38** · Max DD 19.4% | Bottom quartile vs sector | **Negative** |
| **Earnings Revision** | **+23.5%** (20.57 vs 16.65, prior 3mo) | Upgrade breadth unavailable | **Positive — caveat below** |

**Peer value cross-section (sector comparables, reliable only):**
P/E: AMZN 36.6 > TJX 30.2 > BKNG 24.6 > HD 21.8 > MCD 20.3 > LOW 16.5 → **AMZN is the most expensive.**
EV/EBITDA: TJX 20.3 > **AMZN 17.4** > MCD 15.5 > HD 14.8 > BKNG 14.6 > LOW 12.3 → mid-pack but above median (~14.8).
AMZN trades at a ~38% P/E premium to the peer median with no dividend. The premium is defensible only on growth; FCF yield is effectively nil on the reported P/FCF of 369 (capex-crushed, not a clean cash-generation signal — AWS capex cycle).

**Quality detail:** Accruals ratio is negative and *deepening* negative in the right direction (−7.6% FY25 vs −9.1% FY24) — cash earnings exceed accounting earnings, a genuinely high-quality marker. But **ROIC is deteriorating: 16.45% (FY24) → 14.18% (FY25)**, and ROE 20.72% → 18.89%. Piotroski F-Score **7/9 (Moderate)**, failing on F7 (share count rising — 10.83B diluted, dilution flag) and F9 (asset turnover not improving). That ROIC roll-over is the single most important quality datapoint here and it does *not* support the "compounding quality" narrative at current multiples.

> ⚠️ **Revision caveat:** the tool compared the **2030-12-31** forward period (20.57 vs 16.65), i.e. a 5-year-out estimate, **not** next-twelve-month. A +23.5% long-dated drift is weak evidence for near-term revision momentum. Treat as a mild positive, not a strong buy trigger. Sample/period mismatch — low confidence.

---

## 2. Price Statistics (252 trading days, vs SPY)

| Metric | Value |
|---|---|
| Annualised return | **+23.0%** |
| Annualised volatility | 35.0–35.2% |
| Beta (vs SPY) | **1.387** (profile beta 1.456) |
| **Alpha (annualised)** | **−6.12%** |
| R² | **0.270** |
| **Sharpe** | **0.655** |
| **Sortino** | **1.309** |
| Sortino/Sharpe ratio | 2.00 (fatter right tail; positive skew) |
| Max drawdown | **−19.35%** |

**Read:** beta 1.387, so a 23% return against a ~21% benchmark implies **negative risk-adjusted excess return (−6.1% alpha)**. AMZN outperformed on absolute terms but *underperformed its own beta-implied return*. R² of 0.27 means only 27% of variance is market-explained — 73% is idiosyncratic, so this is a stock-specific bet rather than an index proxy. Sortino (1.31) at roughly 2× Sharpe is meaningfully better than Sharpe alone suggests: downside vol is lower than total vol, so realised drawdowns have been shallower than the headline 35% vol implies.

> ⚠️ **Internal inconsistency:** `calculate_low_vol_score` reports Sharpe 0.404 while `calculate_sharpe_sortino` reports 0.655 on the same 252-day window. Different vol/annualisation handling between the two tools. I use **0.655** as primary (consistent with the 23.0%/35.2% inputs) and flag the discrepancy rather than split the difference.

---

## 3. Composite Quant Signal: **BUY** (not Strong Buy)

Factor scorecard: **1 clear positive (revisions), 2 moderate positives (momentum, quality), 2 negatives (value, low-vol).**

The bull case is entirely *quality-plus-revisions*: negative accruals, 18.9% ROE, +23.5% estimate drift, and price momentum still positive. The bear case is entirely *price and payoff*: most expensive P/E in its peer set, EV/EBITDA above peer median, **−6.1% alpha**, and **falling ROIC**. Momentum (+5.3%) also badly lags mega-cap peers (MSFT +30.5%, META +10.9%, NVDA +7.9%) — AMZN is a laggard *within* the winning cohort, which is a weaker setup than the absolute number implies.

A stock needs top-quintile on value AND momentum AND quality to rate Strong Buy. AMZN fails value decisively. **Buy, sized below benchmark-weight conviction.**

---

## 4. Key Quant Risk Flags

1. **Momentum reversal / laggard-in-crowd.** +5.3% 12-1 vs MSFT's +30.5%. AMZN sits inside the crowded mega-cap tech factor bucket while contributing the *least* momentum — the worst combination: fully exposed to a de-rating of that cluster, limited participation if it continues.
2. **Factor crowding.** Top holdings (AAPL 151.9, NVDA 76.3, MU 61.4, MSFT 30.2 quality scores) cluster heavily — AMZN at 18.9 is a *quality laggard* in a crowded quality trade. If quality unwinds, AMZN is beta to the unwind without the quality premium.
3. **ROIC compression.** 16.45% → 14.18% YoY. If the trend continues, the 36.6x P/E has no quality offset. Watch FY26 capex/AWS margin.
4. **High beta + high vol (1.38 / 35%).** Sharpe 0.655 is mediocre in absolute terms; 19.4% max DD is a live, recent drawdown figure.
5. **Negative alpha (−6.1%).** No statistical excess return vs benchmark over the window despite the beta risk taken.
6. **Dilution.** F-Score F7 = 0; diluted shares 10.83B rising. Modest EPS-quality drag.
7. **Valuation data integrity.** `price_to_fcf` of 369 is capex-distorted — do not use as a standalone value input. Peer ratios for **BABA (P/E 2.47, P/B 0.23) and PDD (P/E 1.25, negative EV)** are demonstrably broken (currency/ADS mismatch) and were **excluded** from the cross-section.
8. **Statistical significance caveats.** (a) Sector peer set for true Specialty Retail comps is n≈6 reliable names — ranks are indicative, not significant. (b) The `rank_universe_by_factor` tool operates on a **25-symbol mega-cap universe including index funds** (VOO, VTI, VFIAX), not the full ~40k listing set — percentiles are *universe rank*, not market-wide deciles. (c) Single 252-day window = one observation; Sharpe/alpha standard errors are wide (indicated Sharpe 95% CI spans roughly 0.1–1.2). (d) Revision signal is on a 2030 period — horizon mismatch.

---

**Bottom line:** Genuinely high *accounting* quality (negative accruals, 18.9% ROE) paired with a deteriorating *economic* return (ROIC −2.3pp) and the richest multiple in its peer group, for −6.1% alpha. The numbers support **Buy on quality and revision direction, but not at a premium valuation into decelerating returns.**
