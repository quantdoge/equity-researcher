# Quant Analyst

- Symbol: GOOG
- Elapsed: 95.5s

---
## GOOG (Alphabet Inc.) — Quantitative Factor Report

**Sector:** Communication Services / Internet Content & Information · **Price:** $282.32 · **Mkt cap:** $3.453T · **Diluted shares:** 12.23B · **EV:** $3.385T (net cash ≈ $67B)

---

### 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 26.1 · EV/EBITDA 18.7 · P/B 8.3 · P/FCF 47.1 · FCF yield 2.1% | **6 / 6 (worst)** | **Negative** |
| **Momentum** (12-1) | **−1.98%** | **5 / 6** | **Negative** |
| **Quality** | ROE 31.8% · ROIC 27.2% · GP/Assets 0.404 · Accruals −5.5% | **2 / 6** | **Positive** |
| **Low Vol** | Vol 34.4% · Beta 1.387 · Max DD 29.2% | **3 / 6 (vol) · 5 / 6 (beta)** | **Neutral** |
| **Earnings Revision** | +19.1% "upgrade" | n/a | **Positive — but see flag #1** |

**Sector peer detail (6 largest Communication Services names):**

| | P/E | EV/EBITDA | P/FCF | ROE | GP/Assets | Accruals | 12-1 Mom | Vol | Beta |
|---|---|---|---|---|---|---|---|---|---|
| **GOOG** | 26.1 | **18.7** | **47.1** | 31.8 | 0.404 | −0.055 | −1.98% | 34.4% | 1.39 |
| META | 26.6 | 15.4 | 34.9 | 27.8 | 0.450 | −0.151 | +15.84% | 44.9% | 1.49 |
| NFLX | 24.5 | 9.0 | 28.3 | 41.3 | 0.394 | +0.015 | −0.99% | 37.8% | 0.23 |
| DIS | 16.2 | 12.6 | 19.9 | 10.8 | 0.181 | −0.029 | +5.70% | 27.1% | 0.55 |
| VZ | 10.8 | 7.7 | 9.4 | 16.2 | 0.156 | −0.049 | +3.83% | 29.2% | — |
| TMUS | 15.2 | 9.1 | 10.8 | 18.6 | 0.192 | −0.077 | −14.81% | 36.8% | — |

GOOG is **the most expensive name in its peer set** on both EV/EBITDA and P/FCF — a genuine factor headwind, not a rounding artifact. Quality rank is strong but second to META on the composite (META wins on GP/Assets and accruals).

**Quality supporting detail:** Piotroski F-Score **6/9** (Moderate). Points lost on ROA improvement, lower leverage, asset-turnover improvement. Cash conversion is exemplary: OCF/NI = 164.7/132.2 = **1.25x**, and accruals have been negative four straight years (−8.6% → −5.5%), i.e. persistently conservative accounting. ROIC 27.2% (down from 32.1% in FY24).

---

### 2. Price Statistics (252-day window, benchmark SPY)

| Metric | Value |
|---|---|
| Annualised return | **−20.57%** |
| Implied SPY return (derived from alpha/beta) | **≈ +11.4%** |
| Implied underperformance | **≈ −32 pp** |
| Alpha (annualised) | **−36.73%** |
| Beta | **1.395** (OLS) / 1.387 (vol model) / 1.198 (profile) |
| R² | **0.274** |
| Annualised volatility | 34.98% (vol model 34.42%) |
| **Sharpe** | **−0.588** |
| **Sortino** | **−0.804** |
| Max drawdown | **−29.16%** |
| Downside deviation (derived) | ≈ 25.6% |

**Consistency checks:** Sharpe is internally consistent (−20.57 / 34.98 = −0.588). Sortino being materially worse than Sharpe means downside volatility is running ~25.6% vs 35.0% total — return distribution is negatively skewed but downside-only vol is *lower* than total, so the Sortino penalty is driven by the negative numerator, not tail risk per se.

---

### 3. Composite Quant Signal: **NEUTRAL** (composite 40/100)

| Factor | Weight | Sub-score | Contribution |
|---|---|---|---|
| Value | 25% | 10 | 2.5 |
| Momentum | 25% | 20 | 5.0 |
| Quality | 25% | 80 | 20.0 |
| Low Vol | 15% | 40 | 6.0 |
| Earnings Revision | 10% | 60 | 6.0 |
| **Composite** | | | **39.5 ≈ Neutral** |

The profile is a **classic quality-vs-price barbell**: top-tier profitability and clean accruals, offset by the peer group's richest multiples and the weakest 12-month price action outside TMUS. This is *not* a Strong Buy setup — the two factors with the best historical payoff (value + momentum) both score in the bottom quintile.

---

### 4. Key Quant Risk Flags

1. **⚠ The revision "upgrade" is a period artifact, not a revision.** The tool's "prior" estimate (21.73759) is *identical* to the FY2029 consensus, while the "current" (25.89667) is FY2030. It is comparing **two different forward years**, so the +19.1% is a growth rate mislabelled as a revision. **I could not obtain a true same-period 3-month revision** — no near-term (FY2026) consensus is present in the estimate feed at all. Treat the revision signal as **unverified**.
2. **The forward estimate curve is genuinely strong, though.** FY2027 $15.32 → FY2028 $18.31 (+19.6%) → FY2029 $21.74 (+18.7%) → FY2030 $25.90 (+19.1%). A remarkably stable ~19% EPS CAGR. Implied forward P/E: **18.4x on FY27, 13.0x on FY29, 10.9x on FY30** — the valuation looks far less demanding on dated estimates, but coverage is thin (9–10 analysts for FY29/FY30) and the FY30 range is wide (23.46–28.62, ±10%).
3. **Momentum reversal / recent crash risk is severe.** 12-1 momentum is only −1.98%, but trailing 12-month total return is −20.6% — implying roughly **−19% in the last 21 trading days**. A one-month collapse of that magnitude after a flat prior 11 months is a high-risk continuation pattern and explains the 29.2% max drawdown. Do not read the modest −1.98% momentum figure as "mildly negative."
4. **Alpha is NOT statistically significant.** Residual vol = 34.98% × √(1−0.274) = **29.8%**; over a 1-year sample the standard error on annualised alpha is ≈29.8%, giving **t ≈ −1.2**. Likewise Sharpe t ≈ −0.59. **A 252-day window is far too short** — the −36.7% alpha should carry almost no weight in position sizing.
5. **Beta dispersion across sources is a data-integrity problem.** 1.198 (firm profile) vs 1.387 vs 1.395 — a 0.20 spread. Combined with peer betas that are economically implausible (VZ −0.516, TMUS −0.502, NFLX 0.23), the 252-day regression window appears **regime-distorted**. Sector low-vol ranks should be treated as indicative only.
6. **Factor crowding in Quality.** GOOG ranks 2nd on sector quality, but the rank is computed over only 6 names — a **very small cross-section**; one name's restatement flips the rank. On the wider 25-name universe screen GOOG ranks **6th** (score 31.83), 5th of the megacaps. Quality is real but not scarce.
7. **FCF compression is the core valuation risk.** P/FCF of 47.1 implies FCF ≈ $73.3B against $132.2B of net income — a **~45% earnings-to-FCF gap**, consistent with heavy capex. If AI capex intensity persists, the 2.1% FCF yield offers little downside support at 18.7x EV/EBITDA.
8. **Liquidity: no concern.** $3.45T cap, 12.23B shares. Not a flag — noted for completeness.
9. **Dividend yield 0.3%** — negligible income support; total-return case rests entirely on earnings compounding.

**Bottom line:** Quality and balance-sheet cleanliness are quantitatively confirmed (ROE 31.8%, ROIC 27.2%, negative accruals, F-Score 6). Value and momentum are quantitatively refuted — richest multiples in the peer set and bottom-quintile 12-month price action with a sharp recent breakdown. The strong alpha/Sharpe deficits are **statistically fragile** (t < 1.5, R² 0.27) and should not be over-interpreted. Composite: **Neutral**, with the distribution of outcomes skewed by whether the ~19% EPS growth trajectory survives the capex cycle.
