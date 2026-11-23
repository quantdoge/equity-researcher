# Quant Analyst

- Symbol: GPN
- Elapsed: 49.7s

---
# GPN — Quantitative Factor Report
**Global Payments Inc.** | Financial Services / Credit Services | Price **$91.83** | Mkt cap ~$22.1B (240.2M sh) | EV ~$35.6B

⚠️ **Data note:** `get_sector_peers` returned only ETFs/Index funds (VTI, VTSAX, VFIAX…), not operating comparables. I built my own payment-processor peer set (V, MA, FIS; FI/FISV returned insufficient data). Sector ranks below are against **n=4**, so treat ranks as indicative, not statistically robust. `get_analyst_estimates` was unavailable on the data plan.

---

## 1. Factor Scores Table

| Factor | Score / Raw | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 15.75 · EV/EBITDA 10.33 · P/FCF 10.82 · **P/B 0.93** | **1 / 4** | **Strongly positive** — cheapest P/E in peer set by ~2x (V 32.9, MA 37.9, FIS 34.4); trades *below book* |
| **Momentum** | 12-1: **−12.42%** · 6-1: **−2.63%** | 3 / 4 | **Negative** — underperformer vs V (+11.6%) / MA (+10.1%); only FIS worse (−14.0%) |
| **Quality** | ROE 5.89% · ROIC 3.22% · GP/A 0.105 · Accruals −0.024 | **4 / 4** | **Negative** — tool signal "low"; ROIC collapsed 5.74%→3.22% y/y |
| **Low Vol** | Vol 48.4% ann. · Beta 0.453 | 2 / 4 | **Mixed** — very low market beta, but extreme idiosyncratic vol |
| **Earnings Revision** | +16.64% (2030E: $22.30 → $26.01) | **1 / 4** | **Positive** — corroborated by 4 upgrades/PT raises, no downgrades |

**Supporting quality detail (Piotroski F-Score = 6, "Moderate")**
| Component | Score |
|---|---|
| Positive ROA / positive OCF | ✅ / ✅ |
| ROA improvement | ❌ |
| Accruals quality | ✅ (negative accruals = conservative) |
| Lower leverage | ❌ |
| Positive equity change / no dilution | ✅ / ✅ |
| Gross margin improvement | ✅ |
| Asset turnover improvement | ❌ |

ROIC history: **3.22% (2025) → 5.74% (2024) → 5.38% (2023) → 5.37% (2022)**. The 2025 decline is the single most damaging quality datapoint — ROIC is now well below any reasonable cost of capital.

---

## 2. Price Statistics

| Metric | Value |
|---|---|
| Alpha (annualised, vs SPY) | **+47.07%** |
| Beta (vs SPY) | **0.455** |
| R² | **0.0203** |
| Sharpe (252d) | **0.726** |
| Sortino (252d) | **1.165** |
| Annualised return | 32.61% |
| Annualised volatility | 44.89% (alt. calc: 48.43%) |
| Max drawdown | **−24.0%** |
| Sortino / Sharpe ratio | 1.60 (fat right tail, acceptable) |

**Alpha is statistically insignificant.** With R² = 0.020 and σ = 44.9%, the standard error on annualised alpha is ≈44.9pp, giving **t ≈ 1.05 (p ≈ 0.30)**. Beta *is* significant (t ≈ 7.3). Interpretation: 98% of GPN's variance is unexplained by the market, and the headline "+47% alpha" is noise, not skill — it is the residue of a 2025 crash-and-rebound, not a persistent return stream.

**Correlation structure (252d):** GPN–SPY **0.142** (near-zero market linkage) · GPN–V 0.458 · GPN–MA 0.462 · GPN–FIS **0.471**. Note V–MA correlate 0.882 with each other but only ~0.46 with GPN — GPN is a *factor orphan*: it does not trade with the payments complex and does not trade with the market. Its price is driven by company-specific event risk.

---

## 3. Composite Quant Signal: **NEUTRAL** (positive-leaning)

| Factor | Weight | Contribution |
|---|---|---|
| Value (rank 1/4) | 30% | **+** strong |
| Earnings Revision (rank 1/4) | 20% | **+** moderate |
| Low Vol (rank 2/4) | 15% | 0 neutral |
| Momentum (rank 3/4) | 20% | **−** |
| Quality (rank 4/4) | 15% | **−−** strong negative |

The value + revision pair is genuinely attractive and is what keeps this off a Sell. But my framework penalises cheap-plus-deteriorating-returns heavily: **P/B < 1 combined with ROIC falling to 3.22% is the classic value-trap signature**, not a mispricing. Negative 12-1 and 6-1 momentum confirm the market has not yet re-rated the story. I would need two consecutive quarters of ROIC stabilisation plus confirmation that the +16.6% revision is in near-term (NTM) numbers, not a 2030 terminal estimate, to move to Buy.

**Upgrade trigger:** ROIC >5% and 12-1 momentum turning positive → Buy.
**Downgrade trigger:** another ROIC decline or an NTM estimate cut → Sell.

---

## 4. Key Quant Risk Flags

1. **Alpha is noise, not signal.** t ≈ 1.05 on 47% alpha with R² = 2%. Do not use trailing return as evidence of quality. *High severity for anyone anchoring on the "+47% alpha."*
2. **Value trap / capital destruction.** ROIC 3.22% is below cost of capital; ROE 5.89% on a book value of $99.01/sh against a $91.83 price. The 0.93 P/B is arguably *fair*, not cheap, if returns stay here. Leverage rose (F5 = 0) and asset turnover fell (F9 = 0).
3. **Extreme idiosyncratic volatility, no diversification value.** 48% vol with 0.45 beta and 0.14 SPY correlation → this is not a defensive low-beta holding; it is a single-name event-risk position. Max drawdown −24% understates tail risk given the April-2025 single-day gap (−20% intraday on 4/17/2025, 17.6M shares).
4. **Momentum reversal risk is already realised, not pending.** Both 12-1 (−12.4%) and 6-1 (−2.6%) are negative and consistent in sign — the direction is robust even though the vendor series shows magnitude inconsistency with the stated spot price.
5. **Revision signal is thin and long-dated.** The +16.64% revision is measured against the **2030-12-31** consensus ($22.30 → $26.01), not an NTM period. That is a low-reliability, sparse-coverage estimate. Directional corroboration from sell-side is strong (KeyBanc upgrade to OW, Oppenheimer upgrade to Outperform $115, Loop initiation Buy $137, PT raises from BofA $116, Mizuho $115, RBC $106, Wolfe $125, Truist $95→$86 Hold) — median PT ≈ **$110.5**, mean ≈ **$109.6**, implying ~+19% upside vs $91.83. But PT dispersion ($86–$137) is ~56% of spot, unusually wide — the Street itself has no consensus on this name.
6. **Data integrity caveats:** (a) price history series and the valuation/profile snapshot are not fully reconciled — I cut the history at 2026-06-30 while the live snapshot is $91.83; (b) two Sharpe figures were returned (0.726 at 44.89% vol vs 1.005 at 48.43% vol) implying different underlying windows — I report the dedicated Sharpe/Sortino tool as primary; (c) sector ranking rests on n=4. **None of these change the signal direction, but the precise magnitudes should not be treated as precise.**
7. **Liquidity: NOT a concern.** ADV ~2–5M shares (~$200–450M) with periodic 5–17M spikes. No crowding issue — GPN's 0.46 correlation to peers and low institutional momentum positioning argue *against* factor crowding; the risk here is neglect, not congestion.

**Bottom line:** A statistically cheap, deeply out-of-favour name with improving sell-side sentiment but deteriorating returns on capital and unproven alpha. The numbers do not yet support the recovery story — they support a **Neutral** with a hard requirement for ROIC confirmation.
