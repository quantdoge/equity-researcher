# Fin Risk Analyst

- Symbol: PLTR
- Elapsed: 89.5s

---
I have everything I need. All core computations returned successfully (the only gaps: no public credit rating/CDS, and Sortino not provided by the volatility tool). Writing the final assessment now.

---

# Financial Risk Assessment — Palantir Technologies Inc. (PLTR)

**Sector:** Technology / Software-Infrastructure (AI & data platform) | **HQ:** Denver, CO | **Market cap:** ~$433–484B | **Employees:** ~4,400

**Executive summary:** PLTR is a zero-leverage, net-cash fortress with a rapidly improving cash engine — credit and liquidity risk are essentially **non-issues**. The exposure is entirely on the **valuation/market side**: a 0.4% FCF yield, 63% volatility and 1.6 beta mean a modest growth disappointment converts directly into a 40%+ drawdown. Balance-sheet risk: minimal. Equity tail risk: high.

---

## 1. Credit Risk Assessment: **INVESTMENT GRADE** (implicit — see data gaps)

- **No funded debt.** Total debt is only **$229M** (lease-type obligations); short- and long-term funded debt = **$0**; interest expense = **$0** for FY2025. The sole facility is a **$500M revolving credit line, fully undrawn, maturing March 2027** (per 10-K) — no refinancing cliff, no covenant exposure.
- **Net debtor is impossible today:** cash & short-term investments of **$7.18B** vs. total liabilities of **$1.41B** → net cash ≈ **+$5.8B even before EBITDA**. Net debt/EBITDA = **−4.1x**.
- **Debt-servicing capacity is undefined because there is no debt to service** — PLTR does not depend on credit markets for survival; it is a lender to the Treasury (net interest income), not a borrower.
- **Bond-like safety is counterintuitive but real:** the balance sheet could fund ~3 years of zero-revenue operations from cash alone.

## 2. Key Financial Risk Metrics (FY2025)

| Metric | Value | Reading |
|---|---|---|
| Debt/Equity | **0.03x** | Negligible leverage |
| Debt/Assets | **0.03x** | Negligible leverage |
| Net Debt/EBITDA | **−4.1x** | Deeply net-cash-positive |
| Interest coverage | **∞ / N/A** | No interest expense |
| Current ratio | **7.1x** | Fortress liquidity |
| Quick ratio | **7.1x** | Fortress liquidity |
| Cash ratio | **6.1x** | Fortress liquidity |
| Assets/Liabilities | **6.3x** | Deep solvency cushion |
| Altman Z-Score | **4.71** | Safe zone (» 2.99) |
| Piotroski F-Score | **8 / 9** | Strong (only fail: F7 dilution) |
| FCF yield | **0.43%** | ⚠ Extremely rich valuation |
| Operating margin | **31.6%** | Excellent, improving |
| Gross margin | **82.4%** | High-margin software |

**Leverage caution:** none. If anything, the "risk" is *negative* leverage — an idle $7.2B cash pile (≈35% of market... no, ~1.7% of market cap) earning interest income that now **contributes meaningfully to net income** (NI $1.63B vs EBIT $1.66B implies interest income is masking most of the tax bill). Falling rates would dent reported earnings momentum, a minor reputational rather than solvency concern.

## 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility (252d) | **63.1%** |
| Beta vs SPY | **1.63** |
| Max drawdown (window) | **−43.2%** |
| Sharpe (0% rf) | **~0.30** |
| Sortino | Not provided (data gap) |

- **Tail risk is the real story here.** At beta 1.63, a 30% S&P 500 drawdown implies a ~**49% PLTR decline** (CAPM). The 43% historical max drawdown is likely to repeat — and worsened — in any growth scare.
- **Risk-adjusted return quality is mediocre:** ~0.30 Sharpe on a 60%+ vol name means the equity risk premium per unit of risk is thin; the stock is pricing as a landmine option, not a compounder.
- **Revenue multiple ≈ 97–108x** (mkt cap / FY25 revenue); **Price/FCF ≈ 200x+**. The market is capitalizing FY26–27 hypergrowth (FCF roughly doubled YoY: $697M → $1,141M → $2,101M → **$2.09B in H1-FY26 alone**). Any deceleration is a markdown event.

## 4. Downside Scenario Analysis (−20% revenue, modeled off FY2025)

| Line item | Base FY25 ($M) | Stress ($M) | Notes |
|---|---|---|---|
| Revenue | 4,475 | 3,580 | e.g., defense/intel budget shock, contract losses |
| COGS (scales ~90%) | 789 | ~640 | Variable |
| Gross profit | 3,687 | ~2,940 | 82% margin mostly preserved |
| SG&A (sticky, ~98% fixed) | 1,714 | ~1,680 | Headcount-heavy |
| **EBIT / EBITDA** | **1,657 / 1,683** | **~1,260 / ~1,286** | Margin falls ~5pts, still strongly positive |
| Net income | 1,625 | ~1,150–1,400 | Partially cushioned by interest income |
| FCF | 2,101 | **~1,250–1,500** | Still hugely positive |

**Post-stress solvency read:** net debt/EBITDA ≈ **−5.4x** (improves in relative terms — the cash fortress is untouched), D/E ~3%, current ratio ~6.5x, cash cover of liabilities ~5x. **The −20% scenario cripples earnings *growth*, not the balance sheet.** Even a **−50% revenue shock** (Rev $2.24B) still yields EBITDA ≈ +$185M and roughly breakeven net income — the gross-margin cushion converts revenue losses at a ~82% contribution rate, and there is no debt service to default on. **Conclusion: no distress pathway through revenue alone.** The only way this company fails financially is if growth stalls *and* equity holders reprice the multiple — that is the risk, and it is precisely the 43%-drawdown scenario.

## 5. Overall Financial Risk Rating: **MODERATE**

Decomposition (the score is bimodal, so read it as a vector):
- **Credit risk: LOW** (Investment Grade — fortress net cash, zero debt service)
- **Liquidity risk: LOW** (7x current ratio, ~$7.2B cash, undrawn $500M revolver)
- **Market/valuation risk: HIGH** (0.43% FCF yield, 63% vol, β=1.63, 43% historical drawdown)
- The binding constraint is the **equity tail**, not corporate solvency.

## 6. Key Red Flags

1. ⚠ **Valuation is the stress test** — 0.43% FCF yield means the stock carries ~200x FCF; even a mild guidance miss is a 30–45% markdown. Historical precedent is already on the tape (−43%).
2. ⚠ **Persistent dilution via stock-based comp:** SBC of **$684M ≈ 33% of FY25 FCF**; Piotroski's only failed check (F7) is dilution. Shares outstanding up ~23% (2021→2025). Real per-share economics lag reported growth.
3. ⚠ **Customer/segment concentration:** intelligence, defense and government procurement (US/UK/international) — budget-cycle exposure, procurement scandals, and contract resets are idiosyncratic threats to the hypergrowth premise.
4. ⚠ **Market beta of 1.6 with 63% vol:** in a broad risk-off tape PLTR is a high-beta amplifier, not a hedge.
5. ⚠ **Earnings partly interest-income-dependent:** ~$7.2B cash earns ~4–5%; if the curve (2Y currently 4.65%, not inverted) normalizes lower, the "beat-and-raise" net-income cadence softens even with operating momentum intact.
6. **Mitigants that cap the downside:** zero debt, >$7B cash, FCF-margin 47% and rising, Gross margin 82%, FY26 H1 FCF already ≈ whole-FY25. This is the *only* scenario class in this portfolio where the company itself is not the risk.

**Data gaps (flagged):**
- **No public corporate credit rating or CDS spreads** — PLTR issues no public bonds; Investment Grade is an *implicit* fundamental assessment, not an agency rating. Unrated status means no market-observable credit signal.
- **Debt maturity schedule:** immaterial — only the undrawn $500M revolver matures Mar-2027; no funded maturities exist.
- **Sortino ratio:** not returned by the volatility tool; Sharpe (~0.30) shown instead. Peer-ratio comparison (NVDA/MSFT/ORCL/CRWD) not pulled this pass — recommend as follow-up if relative FCF multiples are needed.
