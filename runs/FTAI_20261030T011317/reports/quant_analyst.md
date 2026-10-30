# Quant Analyst

- Symbol: FTAI
- Elapsed: 55.0s

---
All data gathered. Writing the report now.

---

# FTAI Aviation Ltd. (FTAI) — Quantitative Factor Report

**Sector:** Industrials / Aerospace & Defense · **Price:** $196.01 · **Mkt Cap:** $20.1B · **As-of:** FY2025 statements (period end 2025-12-31)

---

## 1. Factor Scores Table

Sector rank = position among the four largest Aerospace & Defense comps I actually have data for (**GE, RTX, LMT, BA**) plus FTAI, so n=5. **1 = best, 5 = worst.**

| Factor | Score (0–100) | Sector Rank | Key Inputs | Signal |
|---|---|---|---|---|
| **Value** | 25 | **4 / 5** | P/E 42.6 (4th), EV/EBITDA 21.8 (4th), P/FCF −19.2 (negative) | **Negative** |
| **Momentum** | 5 | **5 / 5** | 12-1M return **−24.6%** vs peers −1.1% to −8.4% | **Strongly Negative** |
| **Quality** | 55 | **2 / 5** | ROIC 20.4% (rising 4 yrs), GP/Assets 0.178 (1st), **accruals 0.186 (5th)** | **Mixed** |
| **Low Volatility** | 5 | **5 / 5** | σ 67.7%, β 2.61, MaxDD −49.9% | **Strongly Negative** |
| **Earnings Revision** | 30 | **4 / 5** | Tool +48.5% **invalid** (see §5); 5 brokers cut PTs ~15–20% | **Negative** |
| **Composite** | **25.3** | — | Weights: Val 20 / Qual 25 / Mom 25 / LowVol 15 / Rev 15 | **SELL** |

**Peer comparison detail**

| Metric | **FTAI** | GE | RTX | LMT | BA |
|---|---|---|---|---|---|
| P/E | 42.6 | 38.4 | 40.2 | **29.9** | 69.6 |
| EV/EBITDA | 21.8 | 28.4 | 20.2 | **19.1** | 21.3 |
| P/FCF | **−19.2** | 46.0 | 36.3 | 21.6 | −70.1 |
| ROE | 149.9\* | 46.1 | 10.0 | 74.7 | 41.0 |
| GP/Assets | **0.178** | 0.130 | 0.104 | 0.127 | 0.026 |
| Accruals | **0.186** | 0.001 | −0.022 | −0.059 | 0.007 |
| 12-1M Mom | **−24.6%** | −8.4% | −4.8% | −1.1% | −7.9% |

\*ROE of 149.9% is a **leverage artifact**, not profitability. Book value is **$3.22/share** against a $196 price → **P/B = 60.9x**. Equity of ~$334M supporting $20.4B of market cap means ROE carries no information. Use ROIC (20.4%) and ROA (11.5%) instead; I have deliberately de-weighted ROE in the quality score.

**Note:** the peer set is 4 mega-caps ($100B–$325B) vs FTAI at $20B. This is a size-mismatched comp group and no true leasing/aftermarket peers were available. Ranks should be read as directional.

---

## 2. Price Statistics (252-day window, vs SPY)

| Statistic | Value | Read |
|---|---|---|
| Annualized return | **−21.5%** | Underperformed a flat-to-up tape |
| Annualized volatility | **67.7%** | ~2–3x a typical A&D name |
| Beta (vs SPY) | **2.61–2.63** | t ≈ **9.2** → highly significant |
| Alpha (annualized) | **−70.4%** | t ≈ **1.2 → NOT statistically significant** |
| R² | **0.251** | Only 25% of variance is market-explained |
| Systematic vol | ~33.9% | (67.7% × √0.251) |
| **Idiosyncratic vol** | **~58.5%** | 73% of total risk is company-specific |
| Sharpe ratio | **−0.312** | (−0.389 on the vol module's calc) |
| Sortino ratio | **−0.631** | Less negative than Sharpe ⇒ **positive skew** |
| Max drawdown | **−49.9%** | Peak-to-trough halving |
| Implied downside deviation | ~34.1% | vs 67.7% total vol |

**The two most important numbers here:**

- **The −70% alpha is not significant.** With 58.5% annualized residual volatility and only one year of data, the standard error on alpha is roughly ±58%, giving t ≈ 1.2. I cannot reject the null that FTAI has zero alpha. Do **not** cite "−70% alpha" as evidence of skill destruction — cite it as *unmeasurable* destructive return. What *is* statistically solid is the **beta of 2.61** and the **−49.9% drawdown**.
- **Sortino (−0.63) is far better than Sharpe (−0.31) would imply**, meaning downside deviation (~34%) is only half of total volatility (~68%). The return distribution is **strongly positively skewed** — sharp drawdowns punctuated by violent up-days. This is a lottery-like payoff profile, not a smooth compounder. Position sizing should reflect this, not the Sharpe ratio.

---

## 3. Composite Quant Signal: **SELL**

The score is 25/100. Nothing in the factor set is bullish. The stock is simultaneously (a) worst-in-peer on momentum, (b) worst-in-peer on volatility/beta, (c) bottom-quartile on value, and (d) deteriorating on earnings quality. The single offsetting positive — a genuinely improving ROIC (7.2% → 13.3% → 15.7% → **20.4%**) — is real and why this is **Sell, not Strong Sell**. If ROIC holds above 20% and accruals normalize, the picture improves materially.

---

## 4. Key Quant Risk Flags

1. **Earnings-quality deterioration — highest priority.** Accruals ratio **0.186**, the worst in the peer set by a wide margin (next worst: BA at 0.007) and worst in FTAI's own four-year history (0.049 → 0.039 → 0.186). Net income of $501M was booked against **operating cash flow of −$311M**. Piotroski F-Score of **5/9** fails explicitly on **F2 (positive operating CF)** and **F4 (accruals quality)**, plus F7 (dilution) and F8 (gross margin trend). Reported earnings are not being converted to cash.
2. **Momentum reversal risk is largely spent — but not reversed.** −24.6% on 12-1M and a −49.9% drawdown. Note the ceiling caveat: all four A&D peers are *also* negative (−1% to −8%), so a meaningful part of this is **sector-wide de-rating**, not purely idiosyncratic. FTAI is simply the most levered expression of it (β 2.61).
3. **Extreme idiosyncratic risk.** 58.5% residual vol, R² of just 0.25. A market-hedged position in FTAI leaves ~73% of the risk unhedged. This is a single-name event-risk vehicle (engine aftermarket, leasing portfolio, Russia-exposed assets at 8 aircraft / 17 engines per the 2023 disclosure).
4. **Valuation is back-loaded onto thin-coverage estimates.** Forward P/E: 34.4x (2026E $5.70) → 15.2x (2027E $12.87) → 11.2x (2028E $17.54). The entire investment case depends on 2028+ delivery, yet analyst coverage is **1–7 analysts per year** (2025: 1, 2026: 4, 2027: 4, 2028: 7, 2029: 2, 2030: 4). Expect estimate dispersion to be wide and revisions to be violent.
5. **Factor crowding / sample-size caveats.** n=5 peer group, size-mismatched; 1-year price window; the alpha estimate is statistically indistinguishable from zero. Treat all quintile ranks as indicative.

---

## 5. Data Integrity Warning — the "Earnings Revision UPGRADE" is spurious

The revision tool returned **+48.5% (upgrade)** by comparing a **2030-12-31** EPS estimate of $36.48 against a "prior" estimate of **$24.565**. That $24.565 is *exactly* the **2029-12-31** consensus estimate. **The tool has mistaken one year's growth for a revision** — it is differencing adjacent fiscal years, not measuring a change in the same period's estimate. This is a methodology failure, not a signal. Discard it.

The genuine revision evidence runs the other way:

| Date | Broker | Action | Price then |
|---|---|---|---|
| 2026-01-26 | RBC | PT raised 270 → **350** | $289.61 |
| 2026-05-03 | Jefferies | PT raised 375 → **400** | $239.95 |
| 2026-08-21 | Morgan Stanley | PT raised 319 → 360 | $197.81 |
| 2026-08-02 | Jefferies | PT **cut** 400 → 325 | $206.00 |
| 2026-09-15 | Barclays | PT **cut** 350 → 310 | $176.44 |
| 2026-10-16 | Morgan Stanley | PT **cut** 360 → 310 | $168.56 |
| 2026-10-16 | Macquarie | Initiated Outperform, PT 305 | $168.56 |

The 2026 trajectory is a clear rollover: targets peaked at $400 in May and have been **cut sequentially to $305–310**, a ~20% reduction in six months, with the cuts accelerating in Q3–Q4. Consensus PT of ~$306 implies ~56% upside to $196.01 — but **downgrade momentum in targets typically leads EPS downgrades**, not the reverse. This is what the earnings-revision factor should score as negative. I assigned 30/100.

---

### Bottom line
Statistically defensible facts: **β 2.61 (t≈9.2)**, **−49.9% drawdown**, **67.7% vol**, **accruals 0.186**, **ROIC 20.4% and rising**, **12-1M momentum −24.6% (worst in peer set)**. Not statistically defensible: the −70% alpha figure (t≈1.2), and the +48.5% "upgrade" (a tool artifact). **SELL** — the quality of the earnings, the direction of analyst targets, and the risk profile all point the same way, and only the ROIC trend argues otherwise.
