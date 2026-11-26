# Quant Analyst

- Symbol: BSP
- Elapsed: 41.2s

---
## BSP — Bending Spoons S.p.A. | Quantitative Factor Report
Price $46.29 · Mkt cap $29.4B · Technology / Software-Application (IT) · Data as of 2026-11-25

---

### ⚠️ Sample-Size Warning (read first)
BSP listed **2026-07-01**. Only **~102 trading days** of price history exist (~0.40 years). The tools returned "252-day" and "504-day" windows, but both silently truncated to the available series. **Every annualized price statistic below is a 5-month extrapolation, not a measured annual figure.** Treat Sharpe, Sortino, alpha, and beta as *indicative only* — confidence intervals are extremely wide.

---

### 1. Factor Scores

| Factor | Score | Sector Rank* | Signal |
|---|---|---|---|
| **Value** | **1 / 5** | Bottom (12/12) | **Strongly Negative** — EV/EBITDA 72.5x, P/FCF 95.6x, P/B 27.9x, P/E n/a (negative NI) |
| **Momentum** | **4 / 5** | Top tercile | **Positive** — +21.34% (but over ~4 months, *not* 12-1) |
| **Quality** | **2 / 5** | Bottom tercile | **Weak** — ROIC 7.58% & falling, F-score 4/9, ROE −0.01% |
| **Low Vol** | **1 / 5** | Bottom (12/12) | **Strongly Negative** — 110.2% annualized vol, 40.1% MDD |
| **Earnings Revision** | **3 / 5** | n/a | **Indeterminate** — tool reading is invalid (see below) |

\* Rank is vs. the 12-name sector screen (AAPL, MSFT, NVDA, TSM, AVGO, ANT, SKHY, MU, AMD, ASML, PLTR, CSCO). **This peer set is not comparable** — BSP is a $29B Italian acquirer of consumer apps being ranked against $0.4–5.2T semiconductor/hardware mega-caps. Ranks are directional at best; **true peer-relative quintiles are unavailable.**

**🚩 Earnings Revision Score is a data artifact — do not use it.** Reported "revision = +72.93%" comparing a $2.30 estimate to $1.33. But **2.30 / 1.33 − 1 = +72.93% exactly** — the tool compared FY2027E EPS to the *FY2026E* EPS and mislabeled the period. This is the FY26→FY27 growth rate, **not a 3-month analyst revision.** A genuine +73% 3-month revision is implausible. I score the factor from independent evidence instead (price targets, below).

**Value detail (trailing → forward compression):**

| Metric | Value | Signal |
|---|---|---|
| EV/EBITDA (2025A, $0.411B) | **72.5x** | Extreme |
| EV/EBITDA (2026E, $1.481B) | **20.1x** | Rich but defensible |
| EV/EBITDA (2027E, $2.399B) | **12.4x** | Reasonable |
| P/FCF | 95.6x | Extreme |
| P/B | 27.9x | Extreme — on *negative tangible* book |
| Forward P/E (2026E $1.33 / 2027E $2.30) | 34.8x / 20.1x | Rich / fair |

**Quality detail:**
- ROIC: 11.60% (2023) → 8.47% (2024) → **7.58% (2025)** — a three-year *decline*; now plausibly **below cost of capital**, while the stock prices 27.9x book.
- Piotroski F-Score **4/9** (Weak): fails positive-ROA, ROA improvement, lower leverage, no-dilution, asset-turnover improvement.
- Accruals ratio **−0.0611** (good) — cash earnings exceed net income, consistent with heavy D&A/amortization on acquired intangibles. Earnings are *cash-backed*, not accrual-inflated.
- **Goodwill + intangibles $3,501M = 73.6% of total assets.** Tangible book equity ≈ **−$2,507M**. Net debt $2,041M = **4.97x 2025A EBITDA** (1.38x on 2026E). Current ratio **0.82** (<1 → weak liquidity).
- Offsetting: revenue $387M → $671M → $1,306M (**+73%, +95%**), EBITDA margin 28.3% → 31.4%, operating CF **+$290.6M**.

**Earnings revision — independent read:** Consensus (6 analysts FY27 / 5 FY26) spreads are wide: FY27 EPS $1.95–$2.65 (±15%), FY26 $1.22–$1.43. Price-target direction is **mixed-to-modestly-positive**: BofA $36→$38 (Nov 16), Wells Fargo $48→$52 (Nov 23), Bernstein $47, BNP Paribas $40 — but UBS/CLSA **cut** to $36 (Sep 29), and two Mizuho $72 targets (Aug 11) are stale. **Recent median target ≈ $45–$47.5 vs. price $46.29 → ~0–3% implied upside.** Revisions no longer lead price.

---

### 2. Price Statistics

| Metric | Value | Reliability |
|---|---|---|
| Annualized return | **+87.78%** | ⚠️ 5-mo extrapolation (actual since day-1 close: **+14.3%**) |
| Annualized volatility | **110.24%** | High but directionally credible for a recent IPO |
| Beta vs SPY | **0.933** (R² = **0.0205**) | ❌ Not significant (t ≈ 1.45; 95% CI ≈ **[−0.35, 2.21]**) |
| Beta vs QQQ | **0.464** | ❌ Conflicts with SPY 0.93 and profile 1.48 |
| Beta (company profile) | **1.48** | Third, divergent estimate |
| **Alpha (annualized, vs SPY)** | **+94.97%** | ❌ **Statistically indistinguishable from zero** (SE ≈ 170%, t ≈ 0.55) |
| **Sharpe ratio** | **0.796** | ⚠️ Assumes 0% rf; at 4% rf → **0.76** |
| **Sortino ratio** | **1.603** | ⚠️ Short sample; downside dev. understated |
| **Max drawdown** | **−40.06%** | ✅ Verified: $53.44 (Aug 11) → $32.03 (Oct 2) |

**Beta is unidentifiable.** R² of 0.0205 means the market explains **2%** of BSP's variance — the stock is ~98% idiosyncratic. The three beta estimates (0.46 / 0.93 / 1.48) span a 3x range; none is usable. **Do not risk-adjust or hedge BSP with a market beta.**

**Alpha of +95% is an artifact of n≈102.** Wide-dispersion IPOs mechanically produce large point-estimate alphas with enormous standard errors. The honest reading: **no measurable risk-adjusted skill — zero evidence of alpha.**

---

### 3. Composite Quant Signal: **NEUTRAL**

Weights: Momentum 30% · Quality 25% · Value 20% · Revision 15% · Low-Vol 10% → composite **2.45 / 5.00** (Neutral band 2.0–3.0).

**Why not Sell:** revenue growth of +95% (2025) and +115% (2026E); positive operating cash flow $290.6M with negative accruals (clean earnings); forward multiples compress to 20.1x → 12.4x EV/EBITDA; recent PT direction upward; the 40% drawdown is already absorbed.

**Why not Buy:** 72.5x trailing EV/EBITDA and 95.6x P/FCF; **ROIC 7.58% and declining against 27.9x book**; negative tangible equity (−$2.5B); current ratio 0.82; F-score 4/9; alpha statistically zero; near-zero analyst-implied upside (~0–3%).

The qualitative growth story is real, but **the numbers do not yet certify it**: the market is already discounting the 2027 EBITDA inflection, so the quant signal is *fairly valued*, not *mispriced*.

---

### 4. Key Quant Risk Flags

1. **🚩 Return history is non-investable as a signal.** 102 trading days. No 12-1 momentum, no drawdown-through-cycle, no valid beta. **Any backtest on BSP is not statistically powered.** Do not use momentum or Sharpe/Sortino in position sizing.
2. **🚩 Factor-crowding / lock-up overhang.** IPO 2026-07-01 → the standard 180-day lock-up expires **~2026-12-28**. Volume already spiked to 19.7M (Oct 14) and 10.7M (Nov 24) vs. a ~2M average — distribution-like behavior. Supply shock risk is acute and near-dated.
3. **Momentum reversal risk: HIGH.** Peak-to-trough −40.1% completed inside 5 months; the stock has made two lower highs ($55.77, then $53.46). The +21.34% momentum reading is backward-looking and already decaying.
4. **Leverage/financing risk.** Net debt $2.04B = 4.97x 2025A EBITDA, current ratio 0.82, $415M short-term debt. Acquisition-driven model requires continuous debt access; a frozen credit market impairs the roll-up engine. Interest expense already $142.6M (2025) vs. $277.9M operating income.
5. **Negative tangible book (−$2.5B) → no valuation floor.** 73.6% of assets are goodwill/intangibles. Impairment risk is real; P/B is meaningless as a downside anchor.
6. **Merge/estimator risk.** Only **5–6 analysts**; FY27 EPS dispersion ±15%. Consensus is thin and low-confidence.
7. **Liquidity: adequate but thin.** ~$50–100M ADV; material for a $29B cap only for small positions. Universe factor ranks (value/quality) are unreliable due to the non-comparable peer set.

---
**Bottom line:** A genuine hyper-growth acquirer priced on 2027 perfection, with weak quality, negative tangible equity, and no statistically defensible risk-adjusted track record. **Neutral**, with the December lock-up expiry as the dominant near-term quant event. Re-underwrite only after ≥12 months of price history exists.
