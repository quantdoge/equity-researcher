# Quant Analyst

- Symbol: MOH
- Elapsed: 54.0s

---
## MOH (Molina Healthcare) — Quantitative Factor Report
*Data as of the price tape through 2026-02-20. **See data-integrity warning below — it materially affects this name.***

---

### ⚠️ Data Integrity Flag (read first)

Two price series in the feed disagree by **35%**:

| Source | Price | Implied |
|---|---|---|
| Profile / valuation ratios | **$233.09** | P/E 26.1x, P/B 2.91x, mkt cap $11.8B |
| Daily OHLCV tape, 2026-02-20 close | **$151.00** | P/E 16.9x, P/B 1.89x, mkt cap $7.67B |

The tape is corroborated by FY2025 results **filed 2026-02-10** (revenue $45.4B, EPS $8.92) and by a −25.5% gap-down on 2026-02-06 on 10.3M shares. The $233.09 figure is stale (~July 2025 vintage). **I recompute all price-dependent statistics from the OHLCV tape and treat the tool's momentum/Sharpe/Sortino/max-drawdown outputs as unreliable.** Beta and correlation are internally consistent across two independent tools, so those I retain.

---

### 1. Factor Scores Table

| Factor | Score | Sector Rank (5 managed-care peers) | Signal |
|---|---|---|---|
| Value | **45 / 100** | 2 of 5 | Neutral (illusory — see note) |
| Momentum | **8 / 100** | 5 of 5 | Strong Negative |
| Quality | **22 / 100** | 5 of 5 | Strong Negative |
| Low Vol | **35 / 100** | 2 of 5 | Negative |
| Earnings Revision | **18 / 100** | 5 of 5 | Strong Negative |

**Composite: SELL** (composite z ≈ −0.9σ vs peer group)

**Value (45):** At the true $151 price, MOH screens cheap on trailing numbers — P/E **16.9x** vs ELV 17.8x, UNH 31.1x, HUM 46.9x; EV/EBITDA **7.7x** vs 12.7x / 18.4x / 22.2x. **But the cheapness is an artifact of a stale denominator:** FY2026E consensus EPS is **$5.26** (11 analysts), putting MOH on a **forward P/E of 28.7x** — mid-pack, not cheap. P/FCF is **−18.6x** (negative) vs ELV 31.2x, UNH 23.3x, CNC 8.5x — the worst in the group. Zero dividend.

**Momentum (8):** 12-month total return **−47.5%** ($291.46 → $151.00). Standard 12-1 momentum (excluding last 21 sessions) **−30.0%** ($283.81 → $198.75). *The tool reported +7.0% — inconsistent with the tape by ~37 points and rejected.* Peer set: ELV +9.6%, HUM +7.8%, CNC +4.4%, UNH +0.6%. MOH is the clear laggard.

**Quality (22):** Deterioration is the story, and it is severe.

| Metric | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| ROIC | 25.79% | 23.83% | 22.42% | **9.74%** |
| ROE | 26.72% | 25.88% | 26.22% | **11.60%** |
| Net income ($M) | 792 | 1,091 | 1,179 | **472** |
| Diluted EPS | 13.54 | 18.78 | 20.42 | **8.92** |
| Operating cash flow ($M) | — | 1,662 | 644 | **−535** |

ROIC has collapsed **−1,605 bps** in three years. Piotroski **F-Score = 3 (Weak)** — fails on operating cash flow, ROA trend, accruals, leverage, equity change, and gross margin. Gross profit/assets **0.2618** is the lowest of the five peers (ELV 0.419, HUM 0.387, CNC 0.311, UNH 0.268). Accruals ratio **0.0647** — above the 0.05 red line and the worst in the group (UNH −0.025, HUM 0.006, ELV 0.011).

**Low Vol (35):** Beta **0.116** vs SPY and correlation **0.0355** — mechanically the lowest-risk name in the group on a market-sensitivity basis. But absolute risk is high: annualized vol **46.8%** (tool figure, directionally corroborated by four single-day moves of −25.5%, −21.5%, −17.5%, −14.5% in the tape) and **max drawdown −65.3%** (close basis, $353.24 on 2025-04-03 → $122.65 on 2026-02-11). The low beta is a mirage: MOH's risk is entirely idiosyncratic and sector-driven (corr. with CNC **0.629**, ELV **0.582**), not market-driven, so beta understates drawdown risk badly.

**Earnings Revision (18):** *Tool output rejected.* It compared FY2030E ($23.50) to FY2029E ($21.04) = +11.67% "upgrade" — a five-year-forward comparison with **n=2 analysts**, which is not a revision signal. The real forward curve is a downward staircase:

| FY2025A | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---|---|---|---|---|
| $8.92 | **$5.26** | $9.65 | $13.78 | $21.04 | $23.50 |
| — | **−41%** | +83% | +43% | +53% | +12% |

FY2026E EPS of $5.26 versus FY2025 actual of $8.92 is a **−41% cut** and is the only well-populated estimate (11 analysts). Near-term revisions are sharply negative. The back-end recovery is thinly covered (6, 3, 2 analysts) and carries no statistical weight.

---

### 2. Price Statistics

| Statistic | Tool Output | Recomputed from Tape | Verdict |
|---|---|---|---|
| Alpha (ann., vs SPY) | +87.97% | Strongly negative | **Rejected** |
| R² vs SPY | 0.0013 | — | Alpha not significant (|t| < 1) |
| Beta vs SPY | 0.116 | 0.116 | ✅ Reliable |
| Correlation vs SPY | — | 0.0355 | ✅ Consistent with beta |
| Sharpe | +1.648 | **≈ −1.0** | **Rejected** (sign error) |
| Sortino | +3.228 | **≈ −0.8** (est.) | **Rejected** (sign error) |
| Annualized vol | 46.84% | ~47% | ✅ Plausible |
| Max drawdown | −25.54% | **−65.3%** | **Rejected** (understated 2.6x) |
| 12-mo total return | +76.45% | **−47.5%** | **Rejected** |
| 12-1 momentum | +7.0% | **−30.0%** | **Rejected** |

The alpha of +87.97% with **R² = 0.0013** is the tell: essentially none of MOH's variance is explained by the market, so the alpha estimate has a standard error far larger than the coefficient itself. It is noise, and it is also computed on the stale series. **Do not use any risk-adjusted return metric from this feed for MOH without re-derivation.**

---

### 3. Composite Quant Signal

## SELL

**Rationale:** MOH scores in the bottom quintile on four of five factors — momentum, quality, earnings revision, and (on absolute vol) low-vol. The one apparent support, valuation, dissolves on inspection: trailing P/E of 16.9x becomes 28.7x forward once the −41% FY2026 EPS cut is applied, and free cash flow is **negative** (−$636M, with a −$1.29B working-capital drain). This is a classic **value trap profile** — optically cheap trailing multiples, collapsing returns on capital (ROIC 25.8% → 9.7%), and consensus still cutting.

Not a Strong Sell only because: the balance sheet is not obviously levered, beta is genuinely low, and the 2027–2028 estimate path implies margin recovery if utilization normalizes — a real option, just an ununderwritable one with current data.

---

### 4. Key Quant Risk Flags

1. **🔴 DATA INTEGRITY — HIGHEST PRIORITY.** Price feed divergence of 35% ($233.09 vs $151.00) invalidates every price-dependent metric. All momentum, Sharpe, Sortino, max-drawdown, and alpha outputs for MOH should be discarded and re-run on a clean series. Two of five factor scores (momentum, revision) and three of eight price statistics were unusable.
2. **🔴 Earnings quality / cash conversion breakdown.** Net income +$472M against operating cash flow −$535M → cash-flow accruals ≈ +6.7% of average assets. FY2024→FY2025 swung OCF by **−$1.18B**. Working capital absorbed $1.29B. A healthcare payer drawing down cash this hard is signaling reserve/claims deterioration.
3. **🔴 Negative FCF with capital returns.** FCF −$636M while repurchasing $1.0B of stock — buyback funded from the balance sheet during a cash burn. P/FCF of −18.6x is not a valuation datum; it's a warning.
4. **🟠 Idiosyncratic drawdown risk, not market risk.** Beta 0.116 provides no protection: MOH has delivered a −65% peak-to-trough decline in twelve months while SPY correlation is 0.036. Risk models using beta will systematically understate MOH's VaR. Sector co-movement (CNC 0.629, ELV 0.582) means managed-care factor crowding transmits directly.
5. **🟠 Momentum reversal / gap risk — realized.** Three earnings-driven gaps of −17% to −25% in ten months. Trailing vol 46.8% with fat left tails; a short position carries substantial squeeze risk given the 2027–2030 estimate recovery and analyst targets clustering at $163–$255.
6. **🟡 Estimate coverage thinness at the long end.** FY2029E rests on 3 analysts, FY2030E on 2. Any factor model weighting long-dated growth here is fitting noise. FY2026E (11 analysts) is the only statistically usable point.
7. **🟡 Price targets dated inconsistently** (2026-10-23 to 2026-10-27, with `price_when_posted` of $199–$217 versus a tape price of $151) — cannot be reconciled to the current quote; excluded from the composite.
8. **🟢 Liquidity is not a constraint.** ~1.5–2.0M shares/day, ≈$250M notional. Position sizing is unconstrained.

---

**Bottom line:** Four of five factors are bearish and the fifth is a statistical artifact of a stale price. On the verified tape, MOH is a −47% trailing-return, sub-10%-ROIC, cash-burning payer trading at 28.7x forward earnings. **Sell**, with the explicit caveat that this conclusion rests on a recomputation that contradicts three of the eight supplied statistics — recommend re-running the full factor stack on a clean price series before sizing.
