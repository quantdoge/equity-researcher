# Quant Analyst

- Symbol: ANT
- Elapsed: 32.4s

---
# Quantitative Factor Analysis — ANT (Anthropic PBC)

## ⚠️ Critical Data Integrity Note
ANT is a **recently-IPO'd entity (first trading day 2026-11-19)**. The price history contains **exactly 2 trading days**. Every time-series statistic requested — momentum, low-vol, alpha/beta, Sharpe, Sortino, drawdown, correlation — **cannot be computed with statistical validity** (n=2). I report them as unavailable rather than fabricate values. Fundamentals (FY2023–FY2025) are available and used where possible.

---

## 1. Factor Scores Table

| Factor | Score / Raw Value | Sector Rank | Signal |
|--------|-------------------|-------------|--------|
| **Value** | P/E −3.74; EV/EBITDA −4.26; P/FCF −56.66; P/B **n/a** (BVPS −$11.39) | **n/a** | **Not meaningful** — all multiples negative on negative earnings/EBITDA/FCF/book. No valuation floor exists. |
| **Momentum** | n/a — 2 trading days | **n/a** | **Insufficient data** (day-2 return −11.4%) |
| **Quality** | Gross profit/assets −0.111; accruals ratio −1.595; ROE +202% (distorted by negative equity) | **n/a** | **Low / Negative** — negative gross margin, negative equity |
| **Low Vol** | n/a — 2 trading days | **n/a** | **Insufficient data** |
| **Earnings Revision** | FY2030 EPS est. $2.41 vs $2.565 prior = **−6.04%** | **n/a** | **Downgrade** (⚠️ n=1 analyst — statistically void) |

---

## 2. Price Statistics

| Metric | Value | Note |
|--------|-------|------|
| Alpha (vs SPY, ann.) | **n/a** | 2 observations |
| Beta (vs SPY) | **n/a** | Provider reports `beta: 0` — a placeholder, not a real estimate |
| Sharpe ratio | **n/a** | Insufficient history |
| Sortino ratio | **n/a** | Insufficient history |
| Max drawdown | **−11.38%** | Peak (D1 close $97.17) → D2 close $86.12. Only 2 points; not a valid drawdown series |
| Annualised volatility | **n/a** | Undefined on 2 returns |
| Day-1 → Day-2 return | **−11.38%** | Open $111.50 → close $86.12 = **−22.8%** intraday-to-now |

---

## 3. Composite Quant Signal

### **NEUTRAL → SELL (provisional, low confidence)**

A rigorous composite is **not computable**: 3 of 5 factors are undefined (n=2 price history) and the 2 that resolve (Value, Quality) are **both negative**. There is **no factor in the dataset that scores positively**:

- **Value:** uninvestable on multiples — negative EPS, EBITDA, FCF, and book.
- **Quality:** weak — Piotroski **F-Score 4/9 (Weak)**; negative gross profit; liabilities ($45.4B) exceed assets ($24.7B); equity **−$20.7B**.
- **Revision:** downward, but on a single analyst.
- **Growth (unscored but material):** revenue $41M → $386M → $4,585M (2023→2025), consensus ~$53.9B FY2026 — genuine hypergrowth, the one bullish datapoint, offset by gross margin still negative.

Directionally the fundamental factors tilt **cautious**, but with zero trading history I will not issue a conviction rating. **The correct institutional call is "Not Rated — awaiting price history."**

---

## 4. Key Quant Risk Flags

1. **⛔ Sample size (dominant risk):** 2 trading days. Any volatility, beta, Sharpe, or momentum figure would be noise. Re-evaluate after ≥60 trading days (~3 months).
2. **⛔ Negative shareholders' equity (−$20.7B):** ROE of +202% is an artifact of dividing by negative book — ignore it. P/B is undefined.
3. **⛔ Leverage:** Total debt **$41.8B**, net debt **$24.4B**, against $20.3B cash. Debt/equity undefined (negative equity).
4. **⛔ Accounting anomaly:** FY2025 net loss **−$42.0B** vs operating loss **−$8.1B** — a ~$34B non-operating charge (not SBC, which was $1.2B). Source unexplained; verify before trusting any bottom-line metric.
5. **⚠️ Data inconsistency:** Market cap reported **$1.13T** (profile) vs **$156.8B** (1.821B diluted shares × $86.12). A ~7x discrepancy — resolve share count before sizing any position.
6. **⚠️ Coverage:** Forward estimates rest on **1–2 analysts**. Revision signal (−6.04%) is not statistically meaningful.
7. **⚠️ Factor crowding / lockup:** $86 price is 11% below the IPO-day close and 23% below the day-1 open — post-IPO supply overhang; **lockup expiry** is the key unfactored catalyst. Liquidity itself is high (146M shares traded day 2).

**Bottom line:** Fundamentals describe a hypergrowth but deeply loss-making, negatively-equitied AI company with no valuation support; quantitative price statistics are **impossible to compute** at this stage. Recommend **Not Rated** until sufficient trading history accrues.
