# Quant Analyst

- Symbol: UNH
- Elapsed: 77.0s

---
## UNH — Quantitative Factor Report

**Data basis:** Price $349.91; LTM financials period-end 2025-12-31. Peer set for cross-sectional ranks = managed-care/health-insurer comparables (ELV, CI, HUM, CNC, CVS), constructed manually — note `get_sector_peers` returned *pharma* names (LLY, JNJ, ABBV…), which are not valid comps for a health insurer.

### 1. Factor Scores

| Factor | Score (raw) | Sector Rank (1=best of 6) | Signal |
|---|---|---|---|
| **Value** | P/E 26.45 · EV/EBITDA 15.99 · P/B 3.13 · P/FCF 19.81 · FCF yield ~5.0% · Div yield 2.62% | 3 / 6 | **Neutral** |
| **Momentum** | 12-1 return **+4.32%** (positive); 6-1 **+11.12%** | **5 / 6** | **Weak (relative)** |
| **Quality** | ROE 11.85% · ROIC 10.53% · GP/assets 0.268 · accruals **−0.0247** · F-Score 5/9 | 3 / 6 | **Neutral / deteriorating** |
| **Low Vol** | Vol 31.16% · Beta 0.342 · Max DD 19.32% · Sharpe 1.26 | 2 / 6 (vol); 4/6 (beta) | **Mild positive** |
| **Earnings Revision*** | +11.55% (see note) | 3 / 6 | **Neutral-positive** |

Peer comparison detail (raw):

| | UNH | ELV | CI | HUM | CNC | CVS |
|---|---|---|---|---|---|---|
| P/E | 26.45 | 15.96 | 12.87 | 39.21 | n/m (loss) | 58.53 |
| EV/EBITDA | 15.99 | 11.66 | 8.48 | 19.03 | n/m | 17.52 |
| P/FCF | 19.81 | 28.01 | 9.05 | 124.30 | 7.67 | 13.24 |
| ROE % | 11.85 | 12.86 | 14.23 | 6.70 | −33.27 | 2.35 |
| GP/Assets | 0.268 | 0.419 | 0.165 | 0.387 | 0.311 | 0.218 |
| Accruals | −0.025 | +0.011 | −0.023 | +0.006 | −0.153 | −0.035 |
| Vol % | 31.2 | 33.7 | 27.5 | 44.1 | 48.2 | 33.4 |
| Beta | 0.342 | 0.164 | 0.060 | 0.545 | 0.399 | −0.046 |
| 12-1 Mom % | +4.3 | +11.7 | +11.8 | +14.1 | +8.3 | −0.0 |
| Sharpe (1y) | 1.26 | 1.02 | 0.18 | 2.46 | 1.67 | 0.53 |

**Own-history context (the strongest part of the bull case):** ROIC has collapsed 19.75% (2022) → 19.45% (2023) → 17.99% (2024) → **10.53% (2025)**; ROE 23.3% → 11.85%. Trailing P/E of 26.5x sits on *depressed* GAAP EPS (~$13.23), while consensus FY2026 EPS of $20.60 implies a **forward P/E of ~17.0x** — near the low end of UNH's own decade range. P/B 3.13 and a 2.62% yield are also historically cheap for this name.

### 2. Price Statistics

| Metric | 1-Year (252d) | 2-Year (504d) |
|---|---|---|
| Annualised return | +32.7% | +17.6% |
| Alpha vs SPY | **+36.27%** | **+12.04%** |
| Beta vs SPY | 0.344 | 0.501 |
| R² | **0.025** | **0.030** |
| Sharpe | 1.04 (vol-tool: 1.26) | 0.47 (vol-tool: 0.54) |
| Sortino | 1.61 | 0.58 |
| Annualised vol | 31.2% | 37.0% |
| Max drawdown | −19.3% | −29.0% |
| F-Score | 5/9 (Moderate) | — |

**Statistical significance of the alpha:** residual vol ≈ σ√(1−R²) = 30.9% (1y) / 36.7% (2y); SE(α) ≈ resid vol / √years → t ≈ **1.2** (1y) and **0.5** (2y). **The reported alpha is not statistically distinguishable from zero.** With R² of 2.5–3.0%, ~97% of UNH's variance is idiosyncratic — this is a stock-specific event bet, not a market-exposure bet.

### 3. Composite Quant Signal: **NEUTRAL**

Scorecard: Value 3/6, Momentum 5/6, Quality 3/6, Low-Vol 2/6, Revision 3/6 — a stock in the *middle* of its peer group on almost every axis, with no factor in the top quintile (or even top third). Cheap versus **its own** history and low-vol/high-Sharpe versus **peers** are offset by (a) bottom-quartile relative momentum, (b) a genuine quality deterioration, not a temporary air-pocket, and (c) an F-Score of 5. Not a factor-model buy; the long thesis must rest on idiosyncratic mean-reversion in margins, which is not a quant signal.

### 4. Key Quant Risk Flags

1. **Data-integrity flags (material — do not use naively in the memo):**
 - The "Earnings Revision" tool compares **different fiscal years** (FY2030 $34.92 vs FY2029 $31.31 = exactly +11.55%), i.e. it is a *forward EPS growth rate*, **not** a same-period revision. Applied identically to all peers, so ranks hold, but the label is wrong.
 - The 252d return (+32.7%) and momentum (+4.32%) are **inconsistent with the observed price path** (Dec-2024 close $484 → Dec-2025 close $324, i.e. −33% calendar 2025; trough close $230.15 on 2025-08-01). The 504d max drawdown of −29.0% likewise understates the actual **−60.5%** peak-to-trough (peak close $582 → $230). Treat headline return/alpha/drawdown figures as unreliable; vol (~31%) is the one stat that reconciles with the raw series.
 - The quality module tags **all six** insurers "low" — the absolute threshold is not discriminating within this industry; rely on the raw components.
2. **Momentum reversal / near-term extension risk.** As reported, 12-1 momentum of +4.3% alongside a 32.7% annualised return mechanically implies **~+27% in the last 21 trading days**. If real, that is a marked near-term extension — the classic setup for short-horizon reversal. Momentum is the weakest-ranked factor here (5/6).
3. **Quality decay is the dominant fundamental risk.** ROIC down ~930bp in two years, gross-profit/assets below ELV and HUM, F-Score component failures on ROA improvement, leverage, equity change and gross margin. Negative accruals (−0.025) and positive operating CF are the only quality offsets.
4. **Extreme idiosyncratic concentration.** R² 0.025 means beta-based risk budgeting will *understate* true risk by a wide margin. A 0.34 beta to SPY does not make this a defensive position — the 2025 evidence is a −60% company-specific drawdown.
5. **Factor crowding / peer-group distress.** The peer set is uniformly impaired (CNC negative equity returns, HUM FCF yield <1%, CVS ROE 2.4%). Cross-sectional "mid-pack" rankings are therefore weak evidence of quality — it is mid-pack in a bad cohort.
6. **Liquidity is not a constraint** (>$300bn market cap, 4–10m ADV typical; 120m-share spike days are event-driven), so no liquidity penalty — but the event days themselves (2025-05-13/15, 2025-08-15, 2025-04-17) show **single-day gaps of −15% to −20%**, an unmodelable tail risk.

**Bottom line:** quantitatively Neutral — no factor support strong enough to justify an overweight, and no distress signal strong enough to justify a short. The only genuine quant positives are low realised vol/beta versus peers, the best Sharpe in the comp group behind HUM, a cheap forward multiple versus its own history, and a clean accruals profile.
