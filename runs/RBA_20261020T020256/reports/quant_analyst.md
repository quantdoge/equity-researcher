# Quant Analyst

- Symbol: RBA
- Elapsed: 102.1s

---
## RBA — RB Global, Inc. | Quantitative Factor & Risk Report

**Data caveats up front (material):** two internal inconsistencies in the feed must be flagged before any score is read.
1. **Stale price basis.** The valuation/profile feed uses a price of **$79.81** (market cap $14.8B). RBA did not trade at $79.81 anywhere in the 17-month OHLCV window retrieved (range roughly $86–$119). That price corresponds to ~autumn 2024, so all trailing multiples below are **restated to the observed $102.66 close (2026-02-20)** by proportional scaling (labelled *rst*).
2. **Conflicting price-series maths.** The momentum/return/Sharpe tools report a **−22.3% 12‑1 momentum** and **−13.9% annualised return**. The actual daily bars show the opposite: $82.21 (2024-09-03) → $102.66 (2026-02-20) = **+24.9% (~+16% ann.)**, and 12‑1 momentum of **+12.5%** ($101.66 on 2025-02-20 → $114.41 on 2026-01-21, the close 21 sessions before the end). I report the tool values as requested **and** the series-verified values, and I weight the latter. Factor signals derived from the tool's momentum/return series are marked low-confidence.

---

### 1. Factor Scores

Peer set = CAT, CTAS, DE, UNP (Industrials, "Specialty Business Services" peer is only CTAS). **Ranks are within a 5-name sample — not a true sector quintile; treat as indicative.**

| Factor | Score (raw) | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 38.4 → **49.4 rst** | 5 / 5 | **Neutral (mixed)** |
| | EV/EBITDA 14.1 → **17.2 rst** | 2 / 5 | ← cheap leg |
| | P/FCF 20.4 → **26.2 rst** | 1 / 5 | ← expensive leg |
| | P/B 2.46 → **3.17 rst**; div 1.58% → **1.23 rst** | 2 / 5 | |
| | **Fwd P/E 23.6x (FY26E $4.34), 21.5x (FY27E $4.77)** | — | Reasonable |
| **Momentum (12‑1)** | **−22.29%** (tool) vs **+12.5%** (verified from bars) | 4 / 5 / n.m. | **Conflicting → low confidence** |
| **Quality** | ROE **7.2%**, ROIC **7.14%**, ROA 3.6% | 5 / 5 | **Negative** |
| | Gross profit/assets **0.138** (CAT .222, CTAS .541, UNP .209, DE .154) | 5 / 5 | Negative |
| | Accruals **−4.62%** (best in peer set) | 1 / 5 | Positive |
| | Piotroski **F = 7/9** (fails dilution F7, gross-margin F8) | 2–3 / 5 | Moderate |
| **Low Vol** | Vol **35.5%** (252d) | 4 / 5 | **Negative** |
| | Beta **0.809** (252d) / **0.639** (504d) | 2 / 5 | Positive |
| | Max DD **32.6%** | 4 / 5 | Negative |
| **Earnings Revision** | **+2.35%** (FY2028: $4.765→$4.877) — **n = 1 analyst** | n.m. | **Weak positive, not significant** |

Revision detail: FY26E EPS $4.343 → FY27E $4.765 (**+9.7%**), revenue $4.99B → $5.26B (**+5.4%**), EBITDA $1.870B → $1.940B. Earnings trajectory positive, but the formal revision score rests on a single analyst for FY28 and is **not statistically meaningful**.

---

### 2. Price Statistics

| Metric | Value | Note |
|---|---|---|
| Alpha (ann., vs SPY, 504d) | **−25.65%** | **t ≈ −1.3 → NOT significant** |
| Beta (504d / 252d) | **0.639** / **0.809** | Profile beta 0.527 |
| R² vs SPY | **0.0726** | **93% idiosyncratic** — alpha estimate unusable |
| Sharpe (504d) | **−0.473** | Tool; conflicts with +25% bar-derived return |
| Sortino (504d) | **−0.524** | Downside/upside asymmetry negative |
| Annualised return (tool) | −13.89% | vs **+16%** computed from OHLCV |
| Ann. vol (504d / 252d) | 29.4% / **35.5%** | Vol *rose* in the last year |
| Max drawdown | **−32.55%** (tool); **−19.5%** verified (117.40 → 94.49) | |
| 52-wk range (close basis) | $88.03 – $118.33 | Current $102.66 = **−13.2% from high, +16.6% off low** |
| Liquidity | median ~0.9M sh/day ≈ **$92M** | No liquidity constraint |

Dispersion of alpha: residual vol = 29.25%×√(1−0.0726) = **28.2%**; SE(alpha) ≈ 19.9% over 2 years. Any alpha between roughly −45% and +14% is consistent with the data. **The −25.7% alpha is noise, not evidence.**

---

### 3. Composite Quant Signal

**NEUTRAL (score ≈ 40/100 — negative tilt)**

- **Fails Quality outright:** ROE 7.2%, ROIC 7.1% versus a 24.8%/22.1% ROIC/ROE in 2022. ROIC is at or below plausible WACC (~8–9%) → no economic profit. Peers earn 4–6x the ROE. This is the single most defensible negative in the dataset.
- **Fails Low Vol:** 35.5% realised vol with R² of 7% means the risk is idiosyncratic and unhedgeable — the low-beta characteristic (0.64) provides no protection because it explains almost none of the variance.
- **Partly offset by valuation and revisions:** 17.2x EV/EBITDA is second-cheapest in the peer set (CAT 25.2x, CTAS 28.4x), forward P/E ~22x on FY27E, positive accruals quality, F-score 7, and sell-side targets of **$124–$145** versus $102.66 (all three ≥ $124 pts are post-dated 2025-11 to 2026-06, with two upgrades).

Not a Strong Sell — the cash-flow-backed earnings (accruals −4.6%) and EBITDA-based cheapness rule that out. Not a Buy — quality is bottom-of-peer and momentum evidence is genuinely unresolved.

---

### 4. Key Quant Risk Flags

1. **Data-integrity risk / stale multiples (high).** All trailing multiples in the feed are anchored ~17 months behind price. Anyone screening RBA on "P/E 38x, P/B 2.46" is understating valuation by ~29% (correct: ~49x, ~3.2x). Re-run valuation before sizing.
2. **Momentum factor unresolvable.** Tool says −22.3%, bars say +12.5%. Until reconciled, momentum should carry zero weight in the composite. Do not act on the "negative" tag.
3. **Event / post-earnings-drift risk (high, live).** 2026-02-12: −12.5% on **6.09M shares (≈3.5x normal)**; the 2026-02-18 gap to $112.37 **failed** and closed $106.73, then $102.98, $102.66 — a failed-recovery pattern with negative drift. Residual volatility is elevated and the position is 13% below the pre-event print.
4. **Quality trap / capital-allocation.** ROE collapse from 24.8% (2022) → 7.2% (2025) with P/B still ~3.2x is the classic IAA-integration signature: goodwill-rich equity, sub-cost-of-capital returns. F-score component F7 (no dilution) fails — share count is rising.
5. **Factor crowding: low.** R² of 7% vs SPY and sub-1.0 beta imply minimal overlap with crowded momentum/quality books; diversification benefit, but no factor tailwind.
6. **Sample-size flags.** Revision score n = 1 (FY28); peer ranks computed on 5 names. Neither supports statistical inference — don't quote the rank as a sector quintile.
7. **Liquidity: NOT a flag.** ~$92M/day; institutional sizing is not constrained.
