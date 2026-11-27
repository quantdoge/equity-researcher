# Quant Analyst

- Symbol: CHTR
- Elapsed: 81.1s

---
## CHTR — Quantitative Factor & Risk Report
**Price $147.27 (2026-11-25) | Mkt cap $20.3B | EV $116.9B | 137.7M sh**

⚠️ **Data-integrity warning up front.** The benchmark SPY return series in this data feed is corrupted: correlation of SPY with *every* equity tested is negative (VZ −0.18, TMUS −0.11, T −0.16), which is impossible in live markets. Consequently the tool-reported **beta (−0.055), alpha (−43.4%) and R² (0.0002) are artifacts and must be discarded.** I rebuilt price statistics from raw OHLC closes and used the profile beta (0.731). Several tool fields also disagree with raw prices (momentum −28.96% vs. −47.7% computed; returns annualized off a misaligned window); wherever they conflict, raw closes win.

### 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | **−1.27σ composite** (P/E 4.07, EV/EBITDA 5.51, P/FCF 4.59, P/B 0.99) | **1 of 4** (cheapest) | **Strong bullish** — top decile |
| **Momentum (12-1)** | **−47.7%** | **4 of 4** (worst) | **Strong bearish** — bottom decile |
| **Quality** | ROE 24.3%, ROIC 11.3%, GP/A 0.165, accruals −0.072 | 2 of 4 (mixed) | **Neutral** |
| **Low Vol** | 60.0% ann. vol, DD −58.2% | **4 of 4** (worst) | **Strong bearish** |
| **Earnings Revision** | +27.55% "revision" — **not usable** | n/a | **No signal / unverifiable** |

**Value** is the standout. Cheapest in the cable/telco cohort on every multiple: P/E 4.07 vs. VZ 11.65 / T 7.56 / TMUS 17.10; EV/EBITDA 5.51 vs. 7.60 / 5.86 / 9.73; P/FCF 4.59 vs. 10.17 / 8.48 / 12.19. Trading at 0.99× book ($148.96/sh).

**Critical reframe on "cheap":** the equity is a levered stub. Net debt is **$96.6B** vs. $20.3B equity (net debt/EBITDA 4.55×). EV/FCF is **26.5×**, not 4.6×. The P/E is optically low because it capitalizes cash flow *after* ~$5.2B of annual interest. EBIT/interest coverage ≈ 2.4×. You are buying a thin equity tranche on a capital-intensive asset — the cheapness is compensation for leverage, not free money.

**Quality** splits. Genuine strengths: persistent **negative accruals** (−0.072, negative all four years 2022–25) — OCF $16.08B vs. net income $4.99B, cash conversion is excellent; highest ROE in the cohort; Piotroski **F-score 7** (leverage reduced, no dilution, margins improved). Weaknesses: **GP/A 0.165 is lowest in group** (Charter's goodwill- and plant-heavy balance sheet), and the F-score *fails* on ROA improvement (F3) and asset-turnover improvement (F9) — i.e., the business is deteriorating even as the balance sheet is repaired. ROIC 11.3% is only modestly above an estimated ~7% WACC.

**Earnings revision — do not use.** The tool compared the FY2030 EPS estimate ($77.09) against the FY2029 estimate ($60.44) and labelled the +27.55% gap a "revision." That is forecast-year growth, not a revision of the *same* period. Coverage is 2–3 analysts, and the FY2028 EPS spread runs $28.97–$86.11 — a **3× dispersion**, signalling near-zero analyst conviction. Revenue estimates actually **decline** (2030 $62.26B vs. 2029 $62.63B). No near-term (FY26/27) consensus is published. Sample too small and construction invalid — no signal extracted.

### 2. Price Statistics (rebuilt from raw closes; 252 trading days to 2026-11-25)

| Metric | My calc | Tool |
|---|---|---|
| 12-mo total return | **−26.6%** ($200.76 → $147.27) | −42.3% |
| YTD 2026 | **−29.4%** | — |
| From 2025-05 peak ($427.25) | **−65.5%** | — |
| 12-1 momentum | **−47.7%** | −28.96% |
| Last month (Oct 26 → Nov 25) | **+44.1%** ($102.18 → $147.27) | — |
| Annualised vol | **~55–60%** (monthly est. 55.0%) | 60.9% |
| Max drawdown | **−58.2%** (peak $248.19 → trough $102.18) | −58.2% ✓ |
| **Sharpe** | **−0.46** | −0.694 |
| **Sortino** | **−0.68** | −0.871 |
| Beta | **0.731** (profile; long-run) | −0.055 ✗ artifact |
| **Alpha (annualised)** | **≈ −34%** vs. CAPM (rf 4.0%, ERP 4.5%, β 0.731 → req. 7.3% vs. actual −26.6%) | −43.4% ✗ |
| R² vs. market | not estimable (benchmark corrupt) | 0.0002 ✗ |

Beta and max-drawdown figures agree with independent reconstruction, which gives some confidence in the vol regime. Negative Sharpe **and** negative Sortino (Sortino worse than Sharpe) means downside volatility exceeds total-return volatility's symmetric penalty — losses are fat-tailed, not diffuse. Sample is only ~1 year; alpha's standard error is not meaningfully estimable given the broken benchmark, so treat −34% as economically large but statistically unproven.

### 3. Composite Quant Signal: **NEUTRAL** (speculative deep value)

Equal-weighting the usable factors gives ≈ −0.4σ: value +2, momentum −2, quality 0, low-vol −1.5, revisions 0. This is the textbook **value-trap configuration** — top-decile cheapness paired with bottom-decile momentum, highest-in-cohort volatility, and a Piotroski score whose failing components are precisely *trend* (ROA, asset turnover). Empirically this profile underperforms over 6–12 months and mean-reverts only over 3–5 years. Not a Sell (the value is real and cash-backed), not a Buy (nothing in the price action or fundamentals confirms a trough). **Neutral, sized small.**

### 4. Key Quant Risk Flags
1. **Momentum reversal / squeeze risk (high).** Stock is +44% in one month off the $102 trough on elevated volume (17.9M sh on 2026-06-18). The 12-1 metric excludes this and *overstates* bearishness; equally, squeezes unwind. Expect 15–20% two-way swings.
2. **Leverage & refinancing (high).** $96.6B net debt at 4.55× EBITDA; coverage 2.4×. Equity is a residual claim on a rate-sensitive capital structure — a 100bp move in refinancing cost is material to a $20B market cap.
3. **Factor crowding (moderate).** Deep-value + negative-momentum is a crowded short-side configuration in cable/broadband; positioning-driven gap risk in both directions.
4. **Volatility/liquidity (moderate).** 60% ann. vol against a cohort median near 37% (TMUS 37.1%); −58% drawdown vs. TMUS −33%. Beta 0.73 understates tail risk — realized vol is far above what a 0.73 beta implies.
5. **Estimate & data reliability (moderate).** 2–3 analyst coverage, 3× EPS dispersion, no FY26/27 consensus, and a corrupted benchmark feed. Any factor model run on this name inherits that noise.
6. **Fundamental trend decay (watch).** F-score passes on balance-sheet repair but fails on both trend tests; revenue estimates flat-to-down through 2030. Cheapness may be a melting ice cube rather than a mispricing.
