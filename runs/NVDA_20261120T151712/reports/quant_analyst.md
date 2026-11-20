# Quant Analyst

- Symbol: NVDA
- Elapsed: 43.9s

---
## NVDA — Quantitative Factor Report
**As of 2026-11-20 close · $140.92 · mkt cap $3.45T · Technology / Semiconductors**
Peer set (n=6 large-cap semis): TSM, AVGO, AMD, MU, ASML

### 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 28.8 · EV/EBITDA 23.5 · P/FCF 35.7 (FCF yield 2.8%) · P/B 22.0 | **2nd of 5** (MU 8.7 cheaper) | **Attractive** — cheap vs. own history |
| **Momentum** | 12-1: **−6.3%** (tool); 1M −34.9%; 3M −34.9%; 6M −36.8% | **3rd of 6** (AMD +7.0, TSM −2.5) | **Negative / broken** |
| **Quality** | ROE 76.3% · ROA 58.1% · GP/Assets 0.742 · accruals 0.084 | **2nd of 6** (ROE & GP/A both **#1**, accruals #6) | **Strong, ex-accruals** |
| **Low Vol** | σ 40.3% · β 1.74 · max DD 41.1% | **1st of 6** (AMD σ77/β3.5, MU σ87/β3.3) | **Best in group, but absolutely high** |
| **Earnings Revision** | +33.1% (FY2031 EPS $33.19 vs $24.94) | **2nd of 5** (AVGO +46.2, AMD +30.5) | **Upgrade — low information value** |

Note the quality composite tool prints "low" **only** because of accruals; on ROE (76.3%) and GP/Assets (0.742, 2.4× the nearest peer) NVDA is the best-in-class operator in the sector.

### 2. Price Statistics (252d vs SPY)

| Metric | Value |
|---|---|
| Alpha (annualised) | **−41.0%** |
| Beta | **1.75** (R² 0.400 → **60% idiosyncratic**) |
| Sharpe | **−0.79** |
| Sortino | **−1.23** (downside dev ≈26.3%) |
| Ann. vol | 40.3–40.8% |
| Max drawdown | **−41.1%** (peak close $239.24 on 2026-10-06 → $140.92) |
| 126d Sharpe / Sortino | −1.71 / −2.55 (ann. ret −71%) |
| 63d Sharpe / Sortino | **−4.70 / −6.12** (ann. ret −186%) |

**The entire drawdown is one month.** From 2026-10-22 ($212.21) to 2026-11-20 ($140.92) the stock fell **−33.6% in 21 sessions**, including 747.7M shares traded on 2026-11-12 (≈4× ADV) — a capitulation print. Every risk ratio decays monotonically as the window shortens: this is a momentum break, not a slow de-rating.

Correlations (252d): SPY 0.63 · TSM 0.67 · ASML 0.55 · AMD 0.49 · AVGO 0.47. NVDA is *not* a sector-complex hedge; its 0.63 SPY correlation with β 1.75 makes it a levered market bet at the worst moment.

Fundamental deceleration (real, not just price): ROE 91.9%→76.3%, ROIC 90.9%→77.3%, ROA 65.3%→58.1% YoY. Piotroski **F=5/9** — loses points on ROA trend, gross margin trend, asset turnover, and accruals. Net income $120.1B vs OCF $102.7B (85.6% cash conversion).

### 3. Composite Quant Signal

| Factor | Score /100 | Weight |
|---|---|---|
| Value | 70 | 20% |
| Quality | 78 | 25% |
| Low Vol | 62 | 10% |
| Momentum | 25 | 20% |
| Revisions | 72 | 25% |
| **Composite** | **63 / 100** | — |

## → NEUTRAL (upper end; "accumulate only after the momentum base forms")

**The tension is explicit:** cross-sectionally NVDA grades #1–#2 on four of five factors — a rare, genuinely attractive multi-factor profile, and P/E 28.8 on ROE 76% is the cheapest it has been in years. But the price-based factors are in free-fall (63d Sortino −6.1), and a −41% alpha with β 1.75 means the market is repricing the growth durability, not just the multiple. A quant model does not buy a −34% one-month gap with no consolidation: the sign of the price factors dominates timing even when the rank factors dominate selection. What flips this to **Buy**: 20+ sessions without a new low, 12-1 momentum back above 0, and accruals below 0.05.

### 4. Key Quant Risk Flags

1. **Momentum reversal / knife risk (highest severity).** −33.6% in 21 sessions, 63d Sharpe −4.70, volume capitulation on 11-12 with no retest of support. Short-term reversal is the single most hostile factor state.
2. **High-beta, low-R² exposure.** β 1.75 (2.22 on the profile's longer window), R² 0.40. Two-thirds of the variance is unhedged idiosyncratic AI-capex risk. Worst possible β profile to hold into a momentum break.
3. **Accruals deterioration.** 0.084 vs *negative* accruals at every peer (AVGO −0.026, AMD −0.044, TSM −0.073, ASML −0.060). Receivables/inventory are building faster than earnings. Not yet alarming (85.6% conversion) but trending the wrong way three years running (0.025 → 0.079 → 0.084) and it is why F-score and the quality composite are capped.
4. **Estimate-revision signal is low-grade.** The "3-month revision" is measured against **FY2029–FY2031** forward periods, not NTM — it captures 5-year-out consensus drift, which is far less predictive and far more model-driven than the 12-month revisions the factor is designed for. The native `analyst-estimates` endpoint is **unavailable on this subscription**, so I could not verify NTM revisions directly. Treat the +33% as weak evidence.
5. **Momentum score does not reconcile with the price tape.** The momentum tool returns −6.26% (12-1), but recomputing from raw closes over the same convention (2025-11-19 $186.07 → 2026-10-22 $212.21) gives **+14.0%**. Likewise the feed's 12-month return (−32.3%) does not reconcile with raw closes (−21.8%), though max drawdown (−41.1%) does. **Signs are reliable; magnitudes are not.** Sector ranks should be read as indicative, not statistically ranked.
6. **Broken peer data, thin sample.** TSM P/E prints 1.02 / EV-EBITDA −0.11 (ADR-currency error) and MU's revision prints 0.0 (−100%, artifact) — both excluded, leaving **n=5** for value and revisions. At n=5 a quintile rank carries no statistical significance; treat ranks as ordinal context only.

**Not flagged:** liquidity. ADV ≈150–200M shares ($25B+), $3.45T cap — no crowding or capacity constraint. Note that all 10 analyst targets ($170–$293, median $224.7, +59% vs spot) were published 2026-11-18 at ~$155 and **pre-date the final −3% leg and the 11-12 capitulation** — stale, not confirming.
