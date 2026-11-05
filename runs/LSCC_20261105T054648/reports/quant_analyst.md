# Quant Analyst

- Symbol: LSCC
- Elapsed: 22.4s

---
# LSCC — Quantitative Factor Report
**Lattice Semiconductor Corp. | Technology / Semiconductors | Price $107.25 | Mkt Cap $15.23B**

---

## 1. Factor Scores Table

| Factor | Score (0–100) | Sector Rank* | Signal |
|---|---|---|---|
| **Value** | **8** | 6 of 6 (worst) | **Strong Sell** |
| **Momentum** | **55** | 3 of 6 | **Neutral** |
| **Quality** | **30** | 5 of 6 | **Sell** |
| **Low Vol** | **5** | 6 of 6 (worst) | **Strong Sell** |
| **Earnings Revision** | **62** | 3 of 4 | **Buy (low confidence)** |
| **Composite (weighted)** | **33** | — | **Sell (mechanical)** |

\*Rank vs. hand-built semi peer set n=6: MRVL, MPWR, TXN, AMD, ON, LSCC. Full-sector rank unavailable — flagging as a sample limitation, not a full cross-section.

**Raw factor inputs:**

| Metric | LSCC | MRVL | MPWR | TXN | AMD | ON |
|---|---|---|---|---|---|---|
| P/E | **4,809x** | 52.1 | 98.9 | 57.2 | 184.5 | 245.7 |
| EV/EBITDA | **264.0x** | 31.1 | 72.9 | 35.7 | 109.1 | 34.1 |
| P/FCF | 111.8x | 99.5 | 91.5 | 109.3 | 118.7 | 20.7 |
| P/B | **20.7x** | — | — | — | — | — |
| ROE | **0.43%** | 18.7% | 17.4% | 30.7% | 6.9% | 1.6% |
| 12-1 Momentum | +9.1% | +63.2% | +11.4% | — | +42.1% | −2.2% |
| EPS Revision (fwd) | +24.3% | +52.5% | +7.2% | — | — | +32.1% |

**Quality detail:** gross profit/assets 0.404 (strong, Novy-Marx positive), accruals ratio **−0.195** (excellent — cash earnings far exceed book earnings), Piotroski **F=6/9** (moderate). But ROIC 1.93% vs 29.5% in FY2023. **The quality factor is internally contradictory and this is the crux of the stock.**

**Valuation is not computable on trailing earnings.** FY2025 (ended 2026-01-03): revenue $523.3M, operating income $15.3M, net income **$3.1M**, diluted EPS $0.02. Revenue fell 29% from the FY2023 peak ($737M) and has only just stabilized (+2.7% yoy). SG&A jumped to $153.6M from $116.9M — restructuring plus heavy stock comp. P/E of 4,809x and ROE of 0.43% are **artifacts of cycle-trough earnings, not business deterioration in the franchise**. Gross margin actually *expanded* to 68.2% (from 66.8%), which is top-decile for semis. On the forward curve the picture inverts: consensus EPS $2.51 (FY2027) → 42.7x, $4.39 (FY2028) → 24.4x, $5.89 (FY2029) → 18.2x.

---

## 2. Price Statistics

| Metric | 252-day | 504-day |
|---|---|---|
| Annualised volatility | **67.4%** | 58.5% |
| Beta vs SPY | **3.27** | 2.77 |
| Alpha (annualised) | — | **+14.72%** |
| R² vs SPY | — | **0.336** |
| Sharpe ratio | 0.78 | **1.332** |
| Sortino ratio | — | **2.028** |
| Annualised return | — | +77.9% |
| **Max drawdown** | **−40.1%** | −40.1% |

*(Price-vol tool reports Sharpe 1.178 on the 504d window using a slightly different return convention; I use the Sharpe/Sortino module's 1.332 as primary. Difference is immaterial to the conclusion.)*

**Critical statistical caveat — the alpha is not significant.** With R² = 0.336, residual volatility = 58.5% × √(1−0.336) = 47.7%. Standard error of the annualised alpha over 2.0 years ≈ 47.7% / √2 = **33.7%**. That gives **t ≈ 0.44**. The +14.7% "alpha" is statistically indistinguishable from zero. Decomposed: beta 2.77 × SPY's ~15%/yr delivered roughly 42% of the 77.9% return; the remaining 35 points carry an error band wider than the estimate itself. **Do not underwrite LSCC on its measured alpha.** Also note profile beta of 1.894 disagrees with computed 2.77–3.27 — trust the regression.

---

## 3. Composite Quant Signal: **NEUTRAL** (mechanical score: Sell, 33/100)

The weighted composite (Value 25%, Momentum 25%, Quality 25%, Low Vol 10%, Revision 15%) computes to 33, which screens **Sell**. I am overriding to **Neutral** for one defensible reason, and only one: **the value and quality factors are structurally broken at a cyclical trough.** P/E of 4,809x and ROE of 0.43% measure the cycle, not the company. The non-broken evidence is genuinely positive — 68.2% gross margin, accruals of −0.195, $175M operating cash flow against $3M of net income, and an implied net-cash balance sheet (EV $14.77B ≈ market cap $14.83B). Meanwhile the broken factors (momentum mid-pack, revision positive) do not support a Sell either.

**Verdict: Neutral, with a negative near-term tilt.** This is a 2.8-beta cyclical recovery option trading at 24x two-years-forward earnings, where the recovery must materialize on schedule. It is not a value stock, not a quality stock at this point in the cycle, and not a low-vol stock. The bull case is entirely a forward-estimate case, and the forward estimates are the least statistically reliable input in the model.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal / relative decay — HIGH.** Absolute 12-1 momentum is +9.1%, but peer median is ~+26% (MRVL +63%, AMD +42%). Relative momentum is decaying while the group runs. The −40.1% max drawdown inside the trailing year shows how violently this name mean-reverts. A beta-2.8 stock with fading relative momentum is the classic setup for a momentum-reversal drawdown.

2. **Earnings-revision signal is statistically weak — DO NOT OVERWEIGHT.** The +24.27% revision is measured on the **FY2031 estimate with only 4 analysts** (range $8.45–$9.74), not the standard 3-month near-forward revision. n=4 is below any reasonable significance threshold. Peer revisions are also far-dated and at *different* horizons (2030 vs 2031), so the cross-sectional comparison is indicative only.

3. **Earnings-quality distortion masking true profitability — MEDIUM.** Net income $3.1M vs operating cash flow $175.1M is a $172M gap driven by D&A ($42.3M) and a large stock-comp/restructuring load. Accruals of −0.195 is flatteringly good *because* earnings are depressed. Any screen ranking LSCC on accruals will rank it top-decile for the wrong reason.

4. **Factor crowding in the high-beta semi trade — MEDIUM.** LSCC is not crowded on value or quality (it scores at the bottom of both), but beta 2.77 and 58–67% vol place it firmly inside the crowded "AI-adjacent semiconductor" risk bucket. In a sector-wide de-rating, correlation goes to 1 and the low-vol cushion is zero.

5. **Low explanatory power / idiosyncratic risk — HIGH.** R² of 0.336 means two-thirds of LSCC's variance is company-specific and unhedgeable with index exposure. Position sizing must reflect a 47.7% residual volatility, not the 58.5% total.

6. **Liquidity — LOW RISK.** $15.2B market cap, 138M diluted shares, no liquidity constraint. This is the only one of the six flags that is clean.

7. **Sample-size disclosure.** Peer ranks rest on n=6 semis and the revision score on n=4 analysts. Sector-relative ranks in this report should be read as directional, not as true cross-sectional quintiles. Full-universe factor ranking was not available within budget.
