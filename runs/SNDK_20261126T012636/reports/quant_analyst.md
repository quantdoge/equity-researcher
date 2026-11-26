# Quant Analyst

- Symbol: SNDK
- Elapsed: 36.5s

---
## SNDK — Sandisk Corporation | Quantitative Factor Report
**Sector:** Technology / Computer Hardware (NAND flash memory) · **Industry comps:** MU, WDC, SKHY (the tool's "sector" list returns mega-caps AAPL/MSFT/NVDA that are not comparables — ranks below are within the memory sub-industry)

---

### 1. Factor Scores Table

| Factor | Score (0–100) | Sub-Ind. Rank | Raw Inputs | Signal |
|---|---|---|---|---|
| **Value** | 78 | **1 / 4** | P/E 7.98 · EV/EBITDA 6.56 · P/FCF 7.94 · P/B 5.80 | **Attractive** |
| **Momentum (12-1)** | 25 | 3 / 4 | **−13.59%** (MU +4.53, SKHY +5.86, WDC −20.08) | **Negative** |
| **Quality** | 85 | **1 / 4** | ROE 72.7% · GP/Assets 0.643 · Accruals −0.011 · F-Score 7/9 | **Strong** |
| **Low Volatility** | 5 | **4 / 4** | Ann. vol 112.8% · Beta 3.85 · MaxDD −74.8% | **Very poor** |
| **Earnings Revision** | 55 | 2 / 3 | +1.11% (FY30 EPS 37.23 vs 36.82) — **n = 1 analyst** | **Insufficient evidence** |

**Value detail:** cheapest of usable peers on FCF (7.9x vs MU 11.7x, WDC 29.7x) and EV/EBITDA (6.6x vs MU 6.0x, WDC 20.8x). *SKHY multiples are corrupt (P/E 0.02, EV/EBITDA −0.15) and excluded from ranking.*

**Quality detail:** highest GP/Assets in the group by a wide margin (0.643 vs MU 0.549, WDC 0.455, SKHY 0.333). WDC's ROE of 106% is disqualified by an accruals ratio of **+0.396** (earnings backed by accruals, not cash). F-Score 7 is "moderate": fails on leverage (F5) and share dilution (F7).

---

### 2. Price Statistics (252-day window vs SPY)

| Metric | Value |
|---|---|
| Annualised return | **+55.0%** |
| Annualised volatility | **114.75%** (112.8% on vol-factor calc) |
| Beta vs SPY | **3.87** (R² = **0.2988**) |
| Alpha (annualised) | **+29.83%** — *t ≈ 0.31, **not statistically significant*** |
| Sharpe | **0.479** (0.555 alt. calc) |
| Sortino | **0.816** |
| Sortino/Sharpe ratio | 1.70 (downside vol better contained than total vol) |
| Max drawdown | **−74.78%** |
| Calmar (55.0 / 74.8) | 0.74 |

**Correlation / crowding:** SNDK–MU **0.847**, SNDK–SKHY **0.820**, SNDK–WDC **0.750**, SNDK–SPY 0.544. At 0.85 vs MU this is effectively a leveraged DRAM/NAND cycle bet — diversification benefit is close to zero.

**On the alpha:** the +29.8% point estimate is uninvestable as a signal. With R² of only 0.30, residual vol is ~96% annualised, so the standard error on alpha is roughly the same order as alpha itself. One year of data and a single boom-bust cycle cannot distinguish skill from a 3.9-beta memory tape.

---

### 3. Composite Quant Signal: **NEUTRAL**

Weighted (Value 25 / Momentum 25 / Quality 25 / Low-vol 15 / Revision 10) = **53.3**. Equal-weight = 49.6. Both land squarely in Neutral.

The two strongest factors point opposite directions and cancel: **best-in-class value + top-quartile quality** against **negative momentum, 4th-of-4 on volatility, and a −75% max drawdown**. A stock that scores well on value/quality but is in a confirmed momentum downtrend with 113% vol is a "wait for the tape to stabilise," not a "buy the dip" — and it fails the classic requirement of topping its group on value, momentum *and* quality simultaneously.

---

### 4. Key Quant Risk Flags

1. **Peak-cycle earnings distortion (highest severity).** FY2026 net income of $11.43B followed FY2025 −$1.64B, FY2024 −$0.67B, FY2023 −$2.14B. Four-year average net income = $1.74B → **normalised P/E ≈ 52x**, not 8x. The 7.98x P/E, 72.7% ROE and 0.643 GP/Assets are all artifacts of an NAND upcycle peak. This is the textbook value-trap signature, and the Value factor rank of 1/4 should be heavily discounted.
2. **Momentum reversal risk is already realised, not prospective.** Max drawdown of −74.8% from the June-2026 peak (~$292) leaves the stock in a high-beta downtrend. Negative 12-1 momentum plus 113% vol means position sizing dominates any alpha thesis.
3. **Factor crowding / no diversification.** 0.85 correlation with MU and 0.82 with SKHY. This is a pure memory-cycle expression; sector-neutral construction requires an offsetting short.
4. **Statistical insignificance across the board.** SNDK spun off in Feb-2025 — the 252-day window is roughly the entire listed history, all of it one cycle. Beta, alpha, Sharpe and Sortino all rest on ~1 year (n≈252). None are reliable to two significant figures.
5. **Earnings-revision signal is non-informative.** The model selected FY2030 consensus (EPS $37.23) with **num_analysts = 1**; the "prior" estimate ($36.82) is the FY2029 figure from a different 3-analyst cohort, not a time-series revision. The +1.11% is an apples-to-oranges diff, not revision momentum. FY2027 ($28.39, 12 analysts) → FY2028 ($36.21, 12 analysts) implies strong forecast growth, but direction-of-revision cannot be measured from this data.
6. **Liquidity is not a constraint.** Market cap $83.8–91.3B, average volume in the tens of millions of shares. No liquidity flag.

---

### 5. Data Integrity Caveats (read before using the numbers)

These are material and I could not fully reconcile them within budget:

- **Price basis conflict.** Valuation multiples are struck on a price of **$73.61** (P/E 7.98 = 73.61 / $9.22 diluted EPS, verified arithmetically). The OHLCV endpoint I retrieved closed at **$151.85** on 2026-07-31. On the $151.85 basis, P/E would be **~16.5x**, P/B ~11.6x, EV/EBITDA ~13.1x. The Value factor's *ordinal* rank (1/4 on P/FCF and EV/EBITDA) survives either basis; the *absolute* "8x earnings" claim does not. Note the −74.78% max drawdown reconciles exactly to $291.88 × (1 − 0.7478) ≈ $73.6, which suggests $73.61 is the true current price and the history endpoint simply truncates earlier.
- **Momentum cannot be reproduced.** From the raw OHLCV path I retrieved, a 12-1 return is strongly *positive* (Feb-2025 low ~$3.49 → June-2026 peak ~$292), not −13.59%. I could not reconstruct the −13.59% from available data, so flag Momentum as the **lowest-confidence** input in the table above. Treat the negative signal direction as plausible (a −75% drawdown from peak is real) but the magnitude as unverified.
- **Price-target feed is unusable.** Targets are published at 8× the "adjusted" value ($2,400 vs $300; $2,050 vs $256.25) with `price_when_posted` of $143.86 vs $207.56 for the same week — internally contradictory. Excluded from all analysis. Ratings are also null throughout, so no rating distribution is available.
- **SKHY valuation multiples corrupt** (P/E 0.02) — excluded from ranking. **MU revision score of −100%** is a data artifact (estimate went to 0.0), not a downgrade.
- **No dividend** (yield null), despite a headline referencing a "100% cash return" — unverified, excluded.

**Bottom line:** a genuinely high-quality, cheap-on-trailing-multiples NAND cyclical whose own factor profile argues it is a peak-cycle, high-beta, crowded, post-bust trade. Neutral — and the value score should not be taken at face value.
