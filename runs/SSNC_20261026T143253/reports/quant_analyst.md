# Quant Analyst

- Symbol: SSNC
- Elapsed: 22.4s

---
I have a complete quantitative picture. Note: FI returned insufficient price history (excluded), leaving a 4-name comparable set (SSNC, FIS, JKHY, TYL). Writing the report now.

---

# SSNC — Quantitative Factor Report
**SS&C Technologies Holdings, Inc.** | Technology / Software–Application | Price ~$83.09 | Mkt Cap ~$19.5B

## 1. Factor Scores Table

*(Sector rank = 1 best of 4 in a hand-built financial-software comparable set: SSNC, FIS, JKHY, TYL. The vendor "Technology" sector returns mega-cap semis/hardware — not true comparables — so I substituted vertical financial-software peers.)*

| Factor | Score (0–100) | Sector Rank | Signal |
|--------|--------------|-------------|--------|
| **Value** | 68 | **2 / 4** | **Attractive** — EV/EBITDA 11.9×, P/FCF 12.6×, P/E 26.4×. Cheaper than JKHY (14.4× EV/EBITDA) and TYL (30.2×); only FIS cheaper on EV/EBITDA (11.1×) but FIS has 49.9× P/E and collapsing earnings |
| **Momentum** | 70 | **1 / 4** | **Positive** — 12-1m return **+12.5%**, best of group (FIS −17.2%, JKHY −2.2%, TYL +1.4%) |
| **Quality** | 40 | **3 / 4** | **Weak** — ROE 11.5%, GP/assets 0.146 (JKHY 0.342), F-score 5/9. Only accruals strong (−4.6% = clean earnings). Tool flags quality "low" |
| **Low Vol** | 35 | **3 / 4** | **Mixed/unfavorable** — β 0.44 (low) *but* total vol **31.7%** and Sharpe 0.09; heavy idiosyncratic risk |
| **Earnings Revision** | 60* | n/a | **Upgrade** — forward EPS +9.4% (9.05→9.90) over 3m, *but see caveat* |

\* **Revision caveat:** the +9.4% revision is on the **FY2030** estimate, which has **only 1 analyst** covering it (2029 also 1 analyst; 2027/2028 have 6/5). The MAGNITUDE is directionally bullish but **statistically unreliable** — a single-analyst move, not a broad revision breadth signal.

## 2. Price Statistics (1yr daily vs SPY)

| Metric | Value |
|--------|-------|
| Alpha (annualized) | **−3.00%** |
| Beta (daily vs SPY) | **0.44** |
| R² | **0.033** (very low — 97% idiosyncratic) |
| Annualized return | +2.89% |
| Annualized volatility | 32.1% |
| **Sharpe ratio** | **0.09** |
| **Sortino ratio** | **0.118** |
| Max drawdown | **−27.2%** |

**Beta conflict flag:** vendor profile beta = **1.089**, but 1-yr daily regression vs SPY = **0.44**. The profile beta is likely a 5-yr monthly measure. R² of 0.033 means the regression beta is unstable and of limited explanatory value — treat SSNC as largely idiosyncratic relative to the index.

## 3. Composite Quant Signal

**NEUTRAL** (composite ≈ 56/100)

Weighted: Value 25% (68) + Momentum 25% (70) + Quality 25% (40) + Low-Vol 15% (35) + Revisions 10% (60).

The setup has genuine positives — cheapish cash-flow multiples and best-in-class relative momentum — offset by weak profitability/quality, poor risk-adjusted returns (Sharpe 0.09, Sortino 0.12), and **negative alpha**. A value+momentum pairing that is *not* confirmed by quality or revisions breadth is a "show-me" rather than a conviction buy.

## 4. Key Quant Risk Flags

1. **Negative alpha (−3.0%) & R² 0.033** — no evidence of index-outperformance; returns are a coin-flip on idiosyncratic factors, not a repeatable market-relative edge.
2. **Poor risk-adjusted performance** — Sharpe 0.09 and Sortino 0.12 mean the +12.5% momentum was earned with >30% vol; risk-adjusted return is near zero.
3. **Momentum reversal risk** — momentum is the single strongest positive; with 31.7% idiosyncratic vol, a sharp reversal would erase the 12-1m gain quickly.
4. **Quality deficit** — ROE 11.5%, GP/assets 0.146, F-score 5/9, only accruals clean. No quality cushion if the cycle turns.
5. **Revision signal is a single-analyst artifact** — do not treat the +9.4% as a broad-based upgrade cycle.
6. **Beta/concentration** — daily beta 0.44 vs profile beta 1.09; regression beta unreliable (R² 0.033). Large drawdown capacity (−27.2% observed). Liquidity is ample (large-cap), so no liquidity flag.

**Bottom line:** Cheap-ish, momentum-strong, but quality-thin and alpha-negative with poor Sharpe — statistically a **Neutral** for a factor portfolio. Not a Strong Buy on the numbers; only justified as a value/momentum tactical with tight risk controls.
