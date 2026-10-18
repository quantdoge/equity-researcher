# Quant Analyst

- Symbol: NFLX
- Elapsed: 52.7s

---
## NFLX — Quantitative Factor Workup

### 1. Factor Scores

| Factor | Raw Metrics | Score | Sector Rank (of 5 media/internet) | Signal |
|---|---|---|---|---|
| **Value** | P/E 27.9 · EV/EBITDA 10.2 · P/FCF 32.2 · P/B 11.4 | Mid | **2 / 5** | **Positive** |
| **Momentum (12-1)** | R(12-1) = **−4.88%**; R(6m) = **−8.24%** | Poor | **5 / 5** | **Negative** |
| **Quality** | ROE 41.3% · ROIC 32.4% · GP/A 0.394 · Accruals 0.015 · F-Score **8/9** | High | **2 / 5** | **Strong Positive** |
| **Low Vol** | σ 37.1% · β 0.30 (see caveat) · MaxDD −37.8% | Poor on vol | ~4 / 5 (est.) | **Negative** |
| **Earnings Revision** | +17.59% "upgrade" | **UNRELIABLE** | n/a | **Not Confirmed** |

Peer value comparison (lower = better): NFLX EV/EBITDA **10.2 is the cheapest of the group** — DIS 12.5, META 17.5, GOOG 22.4, SPOT 44.2. Its P/E (27.9) and P/FCF (32.2) rank 3rd of 5, so the value composite lands rank 2.

### 2. Price Statistics

| Metric | 252-day | 504-day |
|---|---|---|
| Annualised return | **−21.67%** | **−26.15%** |
| Annualised vol | 37.63% | 33.40% |
| **Alpha (ann.)** | **−28.44%** | **−35.86%** |
| **Beta vs SPY** | **0.296** | **0.328** |
| **R²** | **0.011** | **0.015** |
| **Sharpe** | **−0.576** | **−0.783** |
| **Sortino** | **−0.860** | **−1.057** |
| Max drawdown | −37.79% | −37.79% |

### 3. Composite Quant Signal: **NEUTRAL**

Strong quality and mid-pack value (the two factors most predictive on a 12-month horizon) are offset by bottom-quintile momentum and deeply negative risk-adjusted returns. This is a textbook **quality-at-a-discount / potential value-trap** configuration — the fundamentals are real, but you are being paid nothing for the price path.

### 4. Key Quant Risk Flags

1. **⚠ The alpha is statistically meaningless — do not cite it.** With R² = 0.011, the regression explains ~1% of NFLX return variance. Standard error on alpha ≈ 0.147%/day, giving t ≈ **−0.77**. The −28.4% "alpha" is inside the noise band; it is an artifact, not skill or anti-skill.
2. **⚠ Beta of 0.30 is almost certainly a data-integrity fault.** NFLX's historical beta is ~1.1–1.3 with R² ~0.3–0.4. A 0.30 beta at R² 0.011 implies near-zero correlation to the market, which no mega-cap media name exhibits. 95% CI on beta is roughly [−0.01, 0.60], so the estimate is statistically bounded well below 1.0 — internally consistent but economically implausible. Treat all beta-adjusted figures as suspect.
3. **⚠ Earnings revision score is contaminated — period mismatch.** The tool's "prior" estimate of 5.42435 is *verbatim identical* to the **2029** consensus EPS. The +17.59% "revision" is simply the 6.38/5.42 = 17.59% **2029→2030 growth rate**, not a genuine analyst revision. Additionally, the 2030 estimate rests on only **15 analysts** vs 34 for 2027 — thin and noisy. Revision momentum is **unconfirmed**; do not score it as bullish.
4. **Momentum deceleration, not reversal.** Six-month return (−8.24%) is worse than twelve-month (−4.88%) — the trend is deteriorating, not basing. Negative momentum of this shape tends to persist 1–3 months; there is no reversal signal yet.
5. **Drawdown/vol asymmetry:** 37.1% annualised vol with a −37.8% max drawdown and a Sortino (−0.86) materially worse than Sharpe (−0.58) means downside volatility dominates. Poor risk-adjusted compensation.
6. **No liquidity or crowding concern** — mega-cap, negligible liquidity risk.

### Fundamental Support (validates the quality score)

ROIC has compounded upward every year: 16.0% → 18.5% → 24.4% → **32.4%** (2022→2025). ROE 41.3%. Accruals ratio of 0.015 is clean (only one positive-accrual year in four; the 2022 warning at 0.051 has fully reversed). F-Score 8/9 — the single miss is **F4 accruals quality**, consistent with accruals being positive but small. Implied EPS path: 3.80 (2027) → 4.54 (2028) → 5.42 (2029) → 6.38 (2030), ~20% CAGR, putting NFLX at ~19x 2027 earnings.

**Bottom line:** Quality and value are genuinely top-quartile — if momentum stabilises, this re-rates to Buy. On the current tape, the negative Sortino and bottom-quintile momentum keep it at Neutral.

*Data gaps: peer low-vol scores not computed (rank estimated from sector vol profile); analyst ratings not retrieved. Alpha/beta estimates carry the integrity caveats in flags 1–2.*
