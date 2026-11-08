# Quant Analyst

- Symbol: AMD
- Elapsed: 42.7s

---
## AMD — Quantitative Factor & Risk Report

**Snapshot note (important):** The valuation/price-target feeds price AMD at **$449.04** with a Nov-2026 vintage, while the raw OHLCV feed terminates Feb-2026 at ~$200. All factor and risk statistics below come from the later snapshot; I flag where this creates inconsistency. Peer set is NVDA, AVGO, MU, TSM (n=5 incl. AMD) — **too small for robust quintile work; treat ranks as indicative, not statistically significant.**

---

### 1. Factor Scores Table

| Factor | Raw Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 169.5 · EV/EBITDA 100.1 · P/FCF 109.1 · P/B 11.7 | **4 of 4** (TSM data corrupt, excluded) | **Strongly Negative** — most expensive in peer set on all three multiples |
| **Momentum** | +25.28% (12-1) | **1 of 5** | **Positive** — best in peer group (NVDA +17.7, MU +17.7, TSM +12.7, AVGO −6.6) |
| **Quality** | ROE 6.88% · GP/Assets 0.223 · Accruals −0.0439 | **5 of 5** | **Strongly Negative** — lowest ROE *and* lowest GP/Assets; accruals are the only bright spot |
| **Low Vol** | Vol 76.9% · Beta 3.54 (252d) | **4 of 5** | **Negative** — highest beta, 2nd-highest vol (MU worse at 87.3%/3.30) |
| **Earnings Revision** | +28.83% (as reported) | **1 of 5** | **Positive, but see caveat** |

**Earnings Revision caveat — do not use the tool output.** `calculate_earnings_revision_score` returned "current EPS 44.395 (FY2030-12) vs prior 34.46 (FY2029-12)." That is a **fiscal-year comparison, not a 3-month revision** — it is simply the FY30/FY29 growth rate of 28.8% mislabelled as revision momentum. Substituting a valid proxy, the price-target record (10 notes, 2026-11-04/05) shows median PT **$649.50 vs $483.90 posted = +34.2%**, with 4 raised, 3 lowered, 3 reiterated. Net direction is genuinely positive, but all ten notes are from a **single date**, so cross-sectional information content is low.

**Composite factor rank:** (1+1+5+2+5)/5 = **2.8 / 5** — below midpoint. Classic **high-momentum / high-beta / expensive / low-quality** profile.

---

### 2. Price Statistics (vs SPY)

| Metric | 504d (2y) | 252d (1y) |
|---|---|---|
| Annualised return | **+118.87%** | — |
| Annualised volatility | 68.56% | 76.93% |
| **Beta** | **3.146** | **3.542** |
| **Alpha (annualised)** | **+62.16%** | — |
| R² | 0.340 | — |
| **Sharpe** (0% rf) | **1.726** | 1.466 |
| **Sortino** | **2.713** | — |
| Max drawdown | **−37.73%** | −37.73% |
| Sortino/Sharpe ratio | 1.57 | — |

**Statistical verdict on alpha:** With R² = 0.34, residual vol = 68.56% × √0.66 = **55.97%**. Annualised SE(alpha) ≈ 55.97/√2 = **39.6%**, giving **t ≈ 1.57**. That is **below the 1.96 threshold — the +62% alpha is NOT statistically significant.** 66% of AMD's variance is idiosyncratic noise, not stock-picking signal. Beta SE ≈ 0.20, so beta itself is precisely measured but **anomalously high** versus the company profile's 2.49 and AMD's long-run ~1.7–2.0.

---

### 3. Composite Quant Signal: **NEUTRAL**

Momentum and estimate direction are strong; valuation and quality are the worst in the peer group and there is no statistically significant alpha to justify paying 169× trailing earnings. This is a **sentiment/fundamental-story stock, not a factor stock.** Not a Buy on quant grounds; not a Sell given the positive price and revision trend.

**Valuation is entirely a forecast bet.** FY2025 (actual, filed 2026-02-04): revenue **$34.64B** (+34.3% y/y), net income **$4.34B**, diluted EPS **$2.65** → 169× at $449. Consensus requires **FY2026 rev $52.18B (+51%)** and **FY2027 rev $95.41B (+83%)** — FY2027 revenue 2.75× the FY2025 actual — at an implied **30.4% net margin vs. 12.5% delivered**. Forward multiples only look reasonable *if* that ramp lands: FY2026E 56.3×, FY2027E 25.7×, FY2028E 17.5×.

---

### 4. Key Quant Risk Flags

1. **Momentum reversal risk (HIGH).** The re-rating is event-concentrated: AMD gapped from $164.67 (Oct 3, 2025) to $226.45 open (Oct 6, 2025), **+37.5% in one session**. Momentum of this type has no earnings-anchored support and retraces violently; the −37.7% max drawdown (Q1–Apr 2025, $123.75 → $78.21) is the template.
2. **Alpha not significant (t≈1.57).** The headline +62% alpha cannot be distinguished from noise at 95% confidence. Do not cite it as evidence of skill or durable excess return.
3. **Beta estimate is unstable.** 3.15 (504d) vs 3.54 (252d) vs 2.49 profile. Risk models will mis-scale this position; a 10% market drawdown implies a 31–35% AMD drawdown under the fitted betas.
4. **Momentum magnitude inconsistency.** My reconstruction from the OHLCV feed implies roughly **+130%** 12-1 momentum through Jan-2026, not +25.28%. Direction agrees, magnitude does not — **the factor snapshot and price feed disagree materially.** Verify the reference date before relying on the +25.28% figure.
5. **Factor crowding / cluster co-movement.** AMD–SPY 0.65, **AMD–TSM 0.73 (highest in group)**, AMD–MU 0.67, AMD–NVDA 0.55. Diversification benefit within a semi/AI book is minimal; AMD adds ~zero independent exposure.
6. **Piotroski F-Score 8/9 "Strong"** — legitimate positive, but driven by margin/turnover improvement off a depressed base (FY2023 operating margin 1.8%). Note the one failed test: **F5 lower leverage = 0**, and ROIC is only **5.47%** — barely above cost of capital despite 34% revenue growth. Capital is not yet earning its keep.
7. **Data integrity failures.** (a) TSM value-factor output is corrupt (P/E 1.13, EV/EBITDA −0.04) — exclude from any valuation cross-section. (b) Earnings-revision tool is methodologically invalid, as detailed above.
8. **Liquidity: no flag.** Market cap ~$733B, $31K full-time employees, daily volume 20–250M shares. Deeply liquid; no capacity constraint.
9. **Small-sample warning.** All sector ranks rest on n=4–5 comparables. A true semiconductor cross-section needs 30+ names; these "ranks" carry wide error bars and should not be quoted as percentile scores.
