# Quant Analyst

- Symbol: SNDK
- Elapsed: 60.2s

---
# SNDK (SanDisk) — Quantitative Factor & Risk Report

## ⚠️ Data Integrity Caveat (read first)
Two of my feeds disagree, and it materially affects interpretation:
- **`get_price_history`** returned a series from $4.50 (2025‑02‑13) to $151.85 (2026‑07‑31) — an internally coherent explosive ramp — but that series implies a ~2,700% trailing‑year return.
- **The risk/valuation engine** reports a 252‑day annualised return of **+58.73%** and uses a current price of **$73.61**, which is fully consistent with reported diluted EPS of $9.22, 1.24B diluted shares, $91.3B market cap, $15.7B book equity (ROE 72.66%) and $86.9B EV. The 8× target‑price adjustment factor in the analyst feed also points to a price‑space/split artifact.
- **Resolution used:** I treat `$73.61` / the engine outputs as the primary basis (internally consistent), and use the raw history only for *shape* (volatility regime, peak‑and‑reversal pattern), not for return math. Peer valuation for SKHY is also unusable (P/E 0.02, EV/EBITDA −0.15 → currency‑scale error). Peer set n=4 — **quintile ranks are not statistically meaningful.**

## 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 7.98 · EV/EBITDA 6.56 · P/FCF 7.94 · P/B 5.80 | **1 of 3** valid memory comps (MU #2, WDC #3) | **Strong positive** — top‑decile vs Technology |
| **Momentum** | 12‑1: **−13.59%** · 6m: **−22.67%** | 3 of 4 | **Negative** — but see divergence flag |
| **Quality** | ROE 72.66% · GP/Assets **0.643** · Accruals **−0.011** · F‑Score **7** | **1 of 4** (best GP/A, #2 ROE, clean accruals) | **Strong positive** (peak‑cycle inflated) |
| **Low Vol** | Vol **113.1%** · Beta 3.85 · MaxDD **74.8%** | **4 of 4 — worst** | **Strong negative** |
| **Earnings Revision** | +1.14% (upgrade) | n/a — **not rankable** | **Neutral / uninformative** |

**Peer context (memory/storage, 252d):**

| | Value (P/E, EV/EBITDA, P/FCF) | ROE | GP/Assets | Accruals | 12‑1 Mom | Vol | Beta | MaxDD |
|---|---|---|---|---|---|---|---|---|
| **SNDK** | 7.98 / 6.56 / 7.94 | 72.7% | 0.643 | −0.011 | −13.6% | 113.1% | 3.85 | 74.8% |
| MU | 8.09 / 5.96 / 11.66 | 61.4% | 0.549 | −0.024 | +4.5% | 91.9% | 3.52 | 51.0% |
| WDC | 11.22 / 20.76 / 29.72 | 106.3% | 0.455 | **+0.396** | −20.1% | 85.5% | 3.08 | 65.0% |
| SKHY | *invalid data* | 35.6% | 0.333 | −0.059 | +5.9% | 106.3% | 3.38 | 47.9% |

SNDK is the **highest‑quality, cheapest‑on-FCF, and most volatile** name in the group. MU is the cleaner expression of the same value+quality trade with half the drawdown.

**Revision detail — why "upgrade" is not usable:** the revision module compared **FY2030** consensus (+1.14%) where the estimate rests on **1 analyst**. The estimate ladder tells a more useful story — FY26 EPS $8.35 → FY27 $28.40 → FY28 $36.20 (n=12) → FY29 $36.81 → FY30 $37.23 — but FY27 dispersion is **low $3.76 / high $35.99, a 9.6× spread**. Consensus is not a consensus.

## 2. Price Statistics

| Metric | 252‑day | 126‑day |
|---|---|---|
| Annualised return | **+58.73%** | n/a (Sharpe −1.65 implies deeply negative) |
| Annualised volatility | 113.07% | **121.76%** |
| **Sharpe** | **0.511** | **−1.647** |
| **Sortino** | **0.869** | — |
| Beta vs SPY | 3.866 | 3.920 |
| **Alpha vs SPY (ann.)** | **+30.34%** (R² **0.299**) | — |
| Beta vs SOXX | **1.533** | — |
| **Alpha vs SOXX (ann.)** | **+20.85%** (R² **0.616**) | — |
| Max drawdown | **74.78%** | **74.78%** |

- **Alpha is not statistically significant.** Residual vol ≈ 71% (vs SOXX) gives an alpha t‑stat of roughly **0.3**; vs SPY, residual vol ≈ 96%, t ≈ **0.3**. The +30% "alpha" is a point estimate on ~1 year of data — indistinguishable from zero. Do not underwrite it.
- **Beta depends entirely on the benchmark** — 3.87 vs SPY (R² 0.30, poorly specified) vs 1.53 vs SOXX (R² 0.62, better specified) vs 5.65 in the company profile. Parameter instability of this magnitude is itself the signal: **risk decomposition is unreliable**.
- Sortino/Sharpe = 1.70 → returns are **positively skewed** (fat right tail, historically), which is exactly what a NAND cyclical looks like — and what reverses violently.
- **Momentum reversal already underway:** 12‑month Sharpe +0.51 → 3‑month Sharpe −1.65, with vol *rising* (113% → 122%). The raw series shows the same shape: a vertical ramp into a late‑June peak, then a ~50% drawdown. This is a **stage‑2 top, not a base**.

**Correlations:** MU **0.848**, SKHY **0.820**, WDC **0.751**, SPY 0.544. SNDK is essentially a levered MU position — no diversification value, and high **factor crowding** risk in the memory/AI‑storage trade.

## 3. Composite Quant Signal

Weighting: Value 25% · Quality 25% · Momentum 20% · Revisions 20% · Low Vol 10%
Score = 0.25(+2) + 0.25(+2) + 0.20(−1) + 0.20(0) + 0.10(−2) = **+0.6 of max +2.0**

# → NEUTRAL
*(Value/Quality leg: Strong Buy. Momentum/Low‑Vol leg: Sell. The two cancel.)*

**Why not Buy despite an 8× P/E:** FY2026 gross margin is **71.5%** ($14.47B on $20.25B revenue) against a revenue base that went $7.36B → $20.25B in one year. ROIC of 76.8% follows −12.2%, −3.9%, −16.3% in the three prior years. **Trailing multiples on peak-cycle NAND earnings are not a value signal — they are a cycle-position indicator.** Normalising gross margin toward the 30–45% historical band would roughly halve to two‑thirds of EPS, putting the stock at 15–25× — fair, not cheap. Piotroski 7/9 is decent but fails exactly where it matters for a cyclical: **F5 leverage up, F7 share dilution**.

## 4. Key Quant Risk Flags

1. **Peak-cycle earnings distortion (highest severity).** 71.5% gross margin and 76.8% ROIC are not sustainable in NAND. The 8× P/E and 6.6× EV/EBITDA are artifacts of a cyclical peak; a 30‑day puke could re-rate the multiple without price moving.
2. **Momentum reversal in progress.** 12‑1 −13.6%, 6m −22.7%, 126d Sharpe −1.65 with *rising* volatility. Classic post-parabolic breakdown; historical base rates favour further weakness over 1–3 months.
3. **Factor crowding / single-factor exposure.** 0.85 correlation to MU, 0.82 to SKHY. Your downside is one trade (AI memory) at 3.9× market beta — position sizing must be done at the *thematic* level, not the name level.
4. **Beta/alpha estimation is not credible.** R² 0.30 vs SPY, beta ranging 1.53–5.65 across specifications, alpha t‑stat ≈ 0.3, and only ~17 months of post-spin trading history (IPO Feb 2025). **Sample too small for statistical significance on any risk‑adjusted metric.**
5. **Drawdown asymmetry.** 74.8% realised max drawdown at 113% vol. A 1% portfolio weight behaves like 3.9%. Any Sharpe/Sortino figure here is a 1‑year statistic, not a characterisation.
6. **Estimate dispersion is extreme.** FY27 EPS range $3.76–$35.99 (n=12); FY30 revision rests on a single analyst. Treat the revision factor as **missing data**, not as neutral-to-positive.
7. **Data integrity.** Price feed, split adjustment, and analyst target scale are mutually inconsistent (see caveat). Re‑pull the desk‑marked price and post‑split share count before any trade sizing.

**Bottom line:** a genuinely high-quality, optically cheap cyclical at the *worst* point in its momentum and volatility profile. Neutral — constructive on the value/quality spread vs WDC and on a relative basis vs MU only once the 3‑month momentum reading stops deteriorating. Monitor: 12‑1 momentum turning positive, or vol compressing below ~90%.
