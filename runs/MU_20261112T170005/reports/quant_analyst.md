# Quant Analyst

- Symbol: MU
- Elapsed: 55.2s

---
# MU (Micron Technology) — Quantitative Factor Report
Prices as of 2026-09-10 tape; fiscal year ends ~early September.

⚠️ **Two data-integrity issues found up front (materially affect the factor outputs):**
1. `earnings_revision` returned **−100%** by comparing a *2031* EPS estimate of **0.00** against a *2030* estimate of **267.29** — and that same 2031 row carries `revenue_estimate = $156B` but `eps_estimate = 0` and `net_income_estimate = 0`. This is a **missing-field/period-alignment bug, not a downgrade.** I do not use it.
2. The price used by the factor tools (`$787–788`) is **stale**. The OHLCV tape closes at **$977.26** on 2026-09-10, and analyst PT logs record `price_when_posted` of $910–1,097 through Aug–Oct 2026. I therefore report multiples **on both bases**. The stale price understates MU's multiples by ~24%.

## 1. Factor Scores

| Factor | Score (raw) | Sector Rank (semis, n=7) | Signal |
|---|---|---|---|
| **Value** | P/E 10.59 (13.1 adj), EV/EBITDA 7.92 (9.8 adj), P/FCF 15.26 (18.9 adj), FCF yield 6.6% (5.3% adj), P/B 6.50 (8.07 adj) | **1 / 6 valid** | **Strong positive** |
| **Quality** | ROE 61.4%, ROIC 69.2%, GP/Assets 0.549, accruals **−2.4%**, Piotroski **8/9** | **1 / 7** | **Strong positive** |
| **Momentum (12-1)** | +4.28% (tool series) · **+521% on raw tape** | **2 / 7** (1/7 on tape) | Positive |
| **Low Vol** | Vol 87.8%, β 3.31, max DD 45.9% | **7 / 7** (worst) | **Strong negative** |
| **Earnings Revision** | Feed broken (−100% artifact). PT-based proxy: **positive** | ~2 / 7 | Positive (low confidence) |

**Value cross-section (P/E · EV/EBITDA · P/FCF):** MU **10.6 · 7.9 · 15.3** | NVDA 33.7 · 27.7 · 41.9 | ASML 61.4 · 46.7 · 53.2 | AVGO 76.5 · 52.4 · 65.8 | AMD 221 · 131 · 142 | INTC N/M (neg. EPS). *TSM excluded — feed returned P/E 1.23 / EV/EBITDA 0.02, a broken ADR/share-unit mismatch.* MU is cheapest on all three multiples even after the ~24% price uplift.

**Quality cross-section:** MU (61.4 ROE / 0.549 GP/A / −2.4% accruals / "high") and ASML (49.0 / 0.341 / −6.0% / "high") are the only names flagged high. NVDA has higher ROE (76.3) and GP/A (0.742) but **+8.4% accruals** drags it to "low". AMD 6.9 ROE, INTC negative ROE. **MU's combination of top-decile ROIC with negative accruals (cash earnings > accounting earnings) is genuinely rare.**

**Revision detail (proxy):** 10 recent PTs, median **$1,400** vs ~$1,000 price (+40%); D.A. Davidson $2,100→$3,000, Baird→$1,520, Mizuho→$1,400; only one cut (Wells Fargo $1,400). Consensus EPS path: FY26 **73.85** → FY27 **175.61** (+138%) → FY28 211.13 (+20%) → FY29 217.90 (+3%) → FY30 267.29. Upward-revised but **sharply decelerating**, and FY28 analyst range is $138–$341 (±48% dispersion) — the growth assumption, not the multiple, is the real variable.

## 2. Price Statistics (252d, vs SPY)

| Metric | Value |
|---|---|
| Annualised return | +125.6% (tool model) — **tape close-to-close 2025-09-10→2026-09-10: +599.4%** ($139.75→$977.26) |
| Annualised volatility | **88.0%** |
| Beta (OLS vs SPY) | **3.33** (profile β 2.37; SE ≈ 0.29 → 95% CI ~2.75–3.91) |
| Alpha (annualised) | **+70.3%** |
| R² | **0.297** |
| Sharpe (rf=0) | **1.43** |
| Sortino (rf=0) | **2.36** |
| Max drawdown | 45.9% (tool) · **−39.1% close-to-close** peak $1,213.18 (25-Jun-26) → $738.88 (29-Jul-26); −41.2% intraday |
| Current vs peak | **−19.4%** |

**Alpha is not statistically significant.** With R² = 0.30 and residual vol ≈ 73.8% annualised, SE(α) ≈ 74% against a point estimate of 70% (**t ≈ 0.95**). The 70% alpha is statistically indistinguishable from zero — it is beta-3.3 exposure to a huge semis move, not demonstrable skill. Beta is, however, robustly elevated: only ~30% of MU's variance is market-explained, i.e. **70% is idiosyncratic/sector-specific risk.**

**Correlations (252d):** AMD 0.66, SPY 0.54, AVGO 0.53, NVDA 0.47. Highest-β peer is AMD (3.62), then MU (3.31), INTC (3.38).

## 3. Composite Quant Signal

**BUY** — not Strong Buy. Equal-weight rank composite = **2.6 of 7 (top ~37% of semis)**.

Three factors are top-quintile (Value 1/7, Quality 1/7, Momentum 2/7), which on a naive sum would screen **Strong Buy**. I downgrade one notch for two reasons: (a) the **Low-Vol factor is dead-last (7/7)** — an 88% vol, β 3.3, −41% drawdown profile fails every risk-adjusted screen and makes the Sharpe of 1.43 almost entirely a function of one extraordinary year; (b) the **revision component is unverifiable** and the value signal rests on **peak-cycle earnings**.

## 4. Key Quant Risk Flags

1. **Value-trap / cycle-peak earnings (highest severity).** P/E 10.6 looks cheap only on trailing EPS of **$74.34** (NI $84.97B / 1.143B sh). Three years ago (FY2023) MU earned **−$5.83B** with ROIC of **−9.9%**. The entire "value" score is a cyclical earnings artifact — EV/EBITDA 7.9 vs NVDA 27.7 is the market pricing mean-reversion, not mispricing. Cheapness on peak memory EPS has historically preceded drawdowns, not protected against them.
2. **Momentum-reversal risk is extreme, not moderate.** +599% in 12 months, then **−41% in five weeks** (Jun 25 → Jul 29). Realised vol 88%. Beta 3.33 ± 0.59 means a 10% SPY drawdown implies roughly **−33% on MU**. The 12-1 momentum signal is directionally bullish but flags as a *late-stage, high-acceleration* move — the classic profile preceding reversal.
3. **Data integrity (act on this).** Revision feed returned a spurious −100% sell signal from an empty 2031 EPS field; TSM's valuation feed is similarly corrupted (P/E 1.23). Any peer-relative or composite screen run on these feeds would misrank the whole semis sleeve. **Exclude TSM value and INTC (N/M) from rankings; treat MU revision as unquantified.**
4. **Factor crowding.** $0.9–1.0T cap, the purest US-listed HBM/DRAM AI-scarcity proxy, correlation 0.66 with AMD. Only 30% R² vs SPY means MU is a crowded *sector-factor* bet — a memory-pricing or AI-capex narrative break hits on idiosyncratic, not market, beta.
5. **Analyst dispersion / estimate fragility.** FY2028 EPS range $138–$341 with 30 analysts; the FY27 +138% growth step is doing all the work. A modest HBM pricing reset compresses both E and the multiple simultaneously — double-counted downside.
6. **Liquidity: NO FLAG.** ~25M shares/day, ~$25B notional. But note volume spikes of 60–85M clustered on down days (2026-03-30 73.8M; 2026-07-29 69.8M) indicating institutional distribution into weakness.
7. **Sample size.** n = 252 daily obs is adequate for beta/vol, **marginal for alpha** (t≈0.95, not significant) and **insufficient for the FY31–FY30 estimate rows** (6–9 analysts on those periods vs 22–30 on FY26–FY28 — do not rely on long-dated estimates).

**Bottom line:** MU ranks **#1 of 7 semis on both value and quality** with a positive momentum/revision tilt, which is the rare top-quintile value+quality+momentum combination. But it is **dead-last on low-volatility with β = 3.3 and a statistically insignificant alpha**, and its value score is manufactured by cycle-peak memory earnings. Size accordingly: this is a **high-conviction business, low-conviction risk-adjusted position.**
