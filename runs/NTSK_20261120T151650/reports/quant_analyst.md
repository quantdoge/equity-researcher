# Quant Analyst

- Symbol: NTSK
- Elapsed: 73.1s

---
## NTSK (Netskope) — Quantitative Factor Report

### ⚠️ Data Integrity Note (read first)
NTSK IPO'd **2025-09-18**. The full price series available is **~295 trading days** (to 2026-11-20 close $24.00). Consequences:
- Any "504-day" statistic is **not** 504 days of history — it is the full post-IPO sample. Treat as ~1.2yr, not 2yr.
- The earnings-revision tool's **+407%** is a **period-mismatch artifact**: it compared FY2029E EPS ($0.186, 4 analysts) to the FY2028E EPS ($0.037) sitting in the "3-months-prior" slot. Different forecast horizons — not a like-for-like revision. **I discard it.**
- Share-count inconsistency: profile market cap **$9.8B** (≈408M shares, all classes) vs. ratios tool **$5.13B** (213.9M diluted). Likely dual-class. I use $5.13B for multiples and show both EV/Sales.

### 1. Factor Scores

| Factor | Score (0–100) | Sector Rank (est.) | Signal |
|---|---|---|---|
| Value | **2** | Bottom decile | Strongly negative — P/E n/a (loss), EV/EBITDA −7.8x, P/FCF **338.8x**, P/B **26.4x** |
| Momentum | **85** | Top quintile | Positive — 12-1m **+25.7%**; 1m **+21.1%**; +210% off Mar-26 low |
| Quality | **35** | 3rd quintile | Weak level, improving trend — ROIC −68.7%, ROE −349%, GP/assets 0.272, F-Score 6 |
| Low Vol | **5** | Bottom quintile | Strongly negative — vol **73–79%**, beta **1.59–1.76** |
| Earnings Revision | **55** (low confidence) | 2nd–3rd quintile | Neutral/positive but **not measurable** — rev. estimates intact; only 4–7 EPS analysts |

**Quality detail:** Gross margin improving 59.8% → 64.6% → **68.1%**; revenue +32.3% then +31.7% (FY25 $709M). Operating margin *deteriorated* to −92.0% (SGA +79% to $626M, IPO/stock-comp driven). Accruals ratio −0.405 is favourable but **mechanically so** — a loss-maker with positive OCF ($38.1M) always screens as "conservative accounting." Piotroski 6/9 flatters it: F1 (positive ROA) = 0 and F7 (no dilution) = 0.

### 2. Price Statistics

| Metric | 252d | ~2yr (full sample) | Reliability |
|---|---|---|---|
| Alpha (ann.) | +113.4% | +19.5% | **Not significant** |
| Beta vs SPY | 1.59 | 1.76 | Credible (corr. check ⇒ ~1.43) |
| R² | 0.085 | 0.101 | — |
| Ann. vol | 78.3% | 75.9% | High confidence |
| Sharpe (rf=0) | 2.02 | 0.46 | **Not significant** |
| Sortino | 2.75 | 0.66 | Not significant |
| Max drawdown | **−70.0%** (since IPO) | — | High confidence |
| Current DD from high | −9.5% (vs $26.52, 28-Oct-26) | — | — |

**Significance tests (the decisive point):** SE(alpha) ≈ σ·√(1−R²)/√years. For the 2yr window: SE ≈ 50.8% vs. alpha 19.5% ⇒ **t ≈ 0.38**. For 252d: SE ≈ 74.7% vs. 113% ⇒ **t ≈ 1.5**. SE(Sharpe) ≈ √((1+SR²/2)/years): 2yr t ≈ 0.62, 1yr t ≈ 1.16. **Every alpha/Sharpe figure is statistically indistinguishable from zero.** The R² of 0.09 means 91% of variance is idiosyncratic — this is a single-name event-driven bet, not a factor exposure.

**Tool discrepancies flagged:** vol/Sharpe/drawdown outputs are internally inconsistent with the raw series (e.g., 252d "annualised return 158%" vs. verified **+34.1%** actual; "max DD 37.1%" vs. verified **−70.0%** since IPO). I rely on the raw-series computations. Profile beta **2.989** is a 5-year monthly figure computed on 14 months of data — unusable.

**Exact verified returns:** since IPO (22.49 → 24.00) **+6.7%**; trailing 252d (17.90 → 24.00) **+34.1%**; 12-1 momentum (17.66 → 22.20) **+25.7%**; peak-to-trough **−70.0%** (25.79 → 7.73); trough-to-now **+210%**.

### 3. Composite Quant Signal

**NEUTRAL** (weighted composite **40/100**: Value 25% × 2 + Mom 25% × 85 + Qual 20% × 35 + LowVol 10% × 5 + Rev 20% × 55).

Extreme factor dispersion: **top-quintile momentum on bottom-decile value and volatility.** This is a high-beta, unprofitable, richly-priced recent IPO whose returns are almost entirely idiosyncratic. It ranks as a *tactical momentum long*, not a factor-quality holding. On a risk-adjusted, statistically defensible basis there is no evidence of alpha.

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — HIGH.** +25.7% 12-1m on 78% vol; the stock has already round-tripped −70% once post-IPO. Momentum this concentrated in a high-vol single name mean-reverts violently.
2. **No statistical support.** Alpha t ≈ 0.4–1.5; Sharpe t < 1.2. Sample of 295 days cannot validate any risk model.
3. **Factor crowding / data-quality risk.** Mega-cap-only peer list (AAPL, MSFT, NVDA, TSM, AVGO, ANT, SKHY, AMD — all >$700B) contains **no cloud-security comparables**, so true sector ranks are **estimated, not computed**. EV/Sales is 6.7x on 213.9M diluted shares or **13.3x** on the profile's 408M share count — the multiple may be twice what screens report.
4. **Valuation with no floor.** 338x P/FCF, 26x book, negative EBITDA. Net cash only ~$403M (~8% of $5.13B cap) — under one year of cash burn at the FY25 operating loss rate if SGA doesn't normalise.
5. **Event/supply risk.** Volume spikes (>10M shares) cluster on gap days: −21% (2026-03-12), −20% (2026-06-04), −13% (2026-10-16). Lockup-expiry and dual-class overhang unquantified.
6. **Liquidity: adequate, not a flag.** Median ≈ 3.4M shares (~$75M/day); position-sizeable for most funds, but thin relative to event-day flows.
7. **Earnings revision signal unusable** — 4–7 EPS analysts, no estimate history, and the reported revision is a horizon mismatch.

**Bottom line:** momentum is real and verifiable; everything else is either unmeasurable, statistically insignificant, or negative. Size for 78% vol, not for a factor score.
