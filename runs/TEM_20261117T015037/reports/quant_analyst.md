# Quant Analyst

- Symbol: TEM
- Elapsed: 69.0s

---
## TEM (Tempus AI, Inc.) — Quantitative Factor Report
**Sector:** Healthcare / Medical-Healthcare Information Services · **Price:** $64.76 (2026-11-16) · **Mkt cap:** $11.29B · **EV:** $11.86B · **IPO:** 2024-06-14

⚠️ **Data integrity flag up front:** the factor tools' return-based outputs do not reconcile with the raw daily price series I pulled. The tape shows TEM at **$64.76 on 2026-11-16**, i.e. **−26.4%** since 2025-10-01 and **−2.5%** over the trailing 12 months, yet the tools report **+52.6% annualised return** and **+23.6% 12-1 momentum**. I report both and treat my recomputed series figures as authoritative where they conflict. All return-based signals below should be read as vintage-sensitive.

---

### 1. Factor Scores Table

| Factor | Score | Sector/Peer Rank | Signal |
|---|---|---|---|
| **Value** | P/E −45.93 · EV/EBITDA −100.06 · P/FCF −46.00 · **P/B 22.96** | Bottom decile (unrankable; all earnings multiples negative) | **Strong Sell** |
| **Momentum** | +23.61% (12-1, tool) vs **−2.5%** (recomputed 12M); last 1M **+0.06%** (flat) | **2 of 6** in comp set (~83rd pct) | **Buy (decaying)** |
| **Quality** | ROE −49.87% · GP/Assets **0.351** · Accruals −0.0118 · F-Score **5/9** | 3 of 4 in comp set (~40th pct) | **Neutral / Sell** |
| **Low Vol** | Vol **82.49%** · Beta **2.389** · Max DD 32.55% (see caveat) | **4 of 4 (0th pct)** | **Strong Sell** |
| **Earnings Revision** | **+94.33%** on FY2030 EPS (2.945 vs 1.516), 4 analysts | Rank n/a | **Buy — low quality** |

**Value:** No composite z-score is computable. Negative P/E, EV/EBITDA and P/FCF are artifacts of GAAP losses (net income −$245M, EBITDA −$119M), not evidence of cheapness. The only usable metric, **P/B 22.96** against book value of $2.82/share, is extreme. On value, TEM is objectively expensive.

**Quality:** Genuinely bifurcated. **Gross profit/assets of 0.351** is strong — above TMO (0.165) and ABT (0.284), second only to DOCS (0.511) — confirming real pricing power in the diagnostics/Insights mix (gross margin 62.7% in FY25, up from 55.0%). But **ROE −49.87%, ROA −10.77%, ROIC −13.91%**, and both F1 (positive ROA) and F2 (positive OCF) fail. **Accruals of −0.0118 are clean**, so the loss is cash-real, not accounting-driven. F-Score 5/9 "Moderate." Note ROE/ROIC of +15.5%/+21.9% in 2022–23 are pre-IPO artifacts of a near-zero equity base and should be ignored — the 2024 ROE of −1,252.79% shows how unstable that denominator is.

**Low Vol:** Unambiguously the worst name in the comp set on risk. 82.49% annualised vol is **2.6x TMO** (31.83%), **1.9x VEEV** (43.81%), and beta 2.389 vs TMO 0.636 / VEEV 0.388 / DOCS 0.725. This is a high-beta, single-theme instrument, not a defensive healthcare holding.

**Earnings revision:** Read the +94.33% with heavy skepticism. It compares an **FY2030** estimate — five years out, **4 analysts**, EPS range 2.86–3.06 — against its value 3 months prior. This is not the standard 1-year-forward revision signal; it is a long-dated DCF output drifting with narrative. The *near-term* curve is more informative and is where the real information sits:

| FY | EPS est | Revenue est | Implied growth |
|---|---|---|---|
| 2026E | −0.05 | $1.601B | +25.9% (vs FY25 $1.272B) |
| 2027E | −0.02 | $1.988B | +24.1% |
| 2028E | +0.55 | $2.412B | +21.3% |
| 2029E | +1.52 | $2.706B | +12.2% |
| 2030E | +2.95 | $3.103B | +14.7% |

Breadth of the 2026/2027 EPS estimates is tight (−0.23 to +0.02) around breakeven — consensus expects **no GAAP profitability until FY2028**. Revenue trajectory is the strongest single quantitative fact in this dataset.

---

### 2. Price Statistics

| Metric | Value | Note |
|---|---|---|
| Alpha (annualised, vs SPY) | **+24.46%** | **t ≈ 0.32 — NOT significant** |
| Beta (vs SPY) | **2.401** | t ≈ 9.1 — highly significant |
| R² | **0.1754** | only 17.5% of variance is market — 82.5% idiosyncratic |
| Sharpe (252d) | **0.633** | tool; see caveat |
| Sortino (252d) | **1.199** | tool |
| Annualised vol | 82.49–82.96% | consistent across tools |
| Max drawdown (tool) | 32.55% | **understates reality** |
| Max drawdown (recomputed, closes) | **−59.8%** | $103.25 (2025-10-08) → $41.55 (2026-07-29) |
| Trailing 12M total return (recomputed) | **−2.5%** | vs tool's +52.6% annualised |
| Off 52-wk closing high ($85.08, 2026-09-28) | **−23.9%** | |
| Off Jul-2026 low ($41.55) | **+55.9%** | |

**The alpha is not statistically significant.** With R²=0.175, idiosyncratic annualised vol is ~75.3% (82.96 × √0.825), so the standard error on annualised alpha is roughly ±75pp over a one-year sample. A +24.5% alpha with a t-stat of ~0.3 is statistically indistinguishable from zero. Anyone citing "24% alpha" for TEM is quoting noise. The **beta of 2.40 is real and robust**.

The reported 32.55% max drawdown is inconsistent with the visible price path — the stock actually halved-and-then-some from the Oct-2025 peak to the Jul-2026 trough. The tool's figure appears to be a window artifact. Use **−59.8%** for risk sizing.

---

### 3. Composite Quant Signal: **NEUTRAL** (high-dispersion, speculative)

Two of five factors (value, low-vol) are bottom-of-universe, one is mid (quality, clean accruals but negative ROIC), one is positive but decaying (momentum), and one is positive but statistically hollow (revision). Mechanically this lands at Neutral. The dispersion is the point: TEM is a **growth/revision bet financed by volatility**, and a standard multi-factor composite has no clean way to score it because four of five factors are either negative or undefined.

**What the numbers support:** revenue compounding ~25%, clean accruals, gross profit/assets in the top tier of the comp set, beta-backed market sensitivity, and a consensus revenue curve that keeps compounding to 2030.
**What the numbers reject:** any claim of value, any claim of risk-adjusted quality, and — critically — any claim of statistically demonstrable alpha.

**Corroborating third-party signal:** 8 recent price targets, median **$80** (+23.5% vs spot); last four (Nov-2026) median **$87** (+34%). But dispersion is wide ($66 H.C. Wainwright → $100 BTIG), Jefferies moved only *to Hold* at $70, and Goldman *initiated Neutral* at $75. Sell-side is constructive on price, agnostic on rating — consistent with Neutral.

---

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — HIGH.** Tool momentum +23.6%, but the series shows the 12M return is −2.5%, the last month is +0.06%, and the stock is −23.9% off its Sept-Oct 2026 high. The +55.9% off the July low is a recovery leg inside a −59.8% drawdown, not a durable trend. This is late-stage momentum; 12-1 screens will hold the name long after the drift has flipped.
2. **Data-vintage inconsistency — MATERIAL.** Return-series outputs (momentum +23.6%, annualised return +52.6%) contradict the raw daily closes (−2.5% 12M). Do not build sizing off the tool's return figures without reconciling the vendor's window.
3. **Small-sample / short history — HIGH.** IPO 2024-06-14. Under 2.4 years of trading, so the 252-day beta/alpha/Sharpe windows span essentially one regime (post-IPO de-rate → AI re-rating). Beta 2.40 is directionally sound; Sharpe 0.633 and Sortino 1.199 are **not** reliable — do not treat as stable statistics.
4. **Factor crowding — LOW, but thematic instead.** Correlations are low: TMO 0.53, DOCS 0.28, VEEV 0.26, HQY 0.14, ABT 0.07. TEM is a standalone AI-healthcare theme, not a crowded healthcare factor. The crowding risk is **AI-narrative** crowding, not sector-factor crowding.
5. **Dilution — real.** Shares 162.1M → 174.3M (+7.5%); F7 no-dilution **fails**. Cash burn persists: OCF −$218M (FY25) after −$189M (FY24), with P/FCF −46.0. FY2028 GAAP breakeven implies ≥2 more years of external funding reliance.
6. **Liquidity — NOT a flag.** ADV ≈ 6–7M shares (~$420M/day), spikes to 22.5M. Fully liquid.
7. **Valuation floor absent.** With negative EBITDA and $0.57B net debt against a $11.86B EV, there is no earnings-based support. Multiple compression is the dominant downside driver, exactly as happened Oct-2025 → Jul-2026.
