# Fin Risk Analyst

- Symbol: ZM
- Elapsed: 57.0s

---
## ZM — Zoom Communications, Inc. | Financial Risk Assessment
*Fiscal year ends Jan 31. Latest balance sheet: 31-Jan-2026 (FY26 10-K). Latest quarter: Q2 FY27, period ended 31-Jul-2026.*

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE (effectively AAA-profile, unrated)**

ZM is a **net-cash company with no financial leverage**. Total debt is $58.5M (operating leases; LT debt = $0.0), against $7.82B of cash and short-term investments — **net cash of $7.76B, i.e. ~28% of market cap**. Interest expense is **$0**, so interest coverage is mathematically undefined (infinite); there are **no covenants, no credit facilities drawn, and no refinancing cliff**. The only "credit risk" here is counterparty/custodial risk on the $7.8B cash and short-duration investment portfolio.

| Test | Reading | Interpretation |
|---|---|---|
| Debt/Equity | 0.01 (0.6%) | Leverage is immaterial |
| Net debt / EBITDA | **−3.04x** (tool, on reported EBITDA) / **−6.2x** on clean operating EBITDA of $1.26B | Net cash |
| Interest coverage | **N/A — interest expense $0** | No debt service burden |
| Altman Z-Score | **5.15 "Safe"** (book-equity basis); ~10x if market cap used for x4 | Bankruptcy risk de minimis |
| Piotroski F-Score | **8 / 9 "Strong"** (only F9 asset-turnover improvement fails) | Improving fundamentals |
| Equity / Assets | 0.82; assets/liabilities 5.56 | Fortress balance sheet |
| Goodwill + intangibles | $472M = 3.9% of assets | Low impairment exposure |

---

### 2. Key Financial Risk Metrics

| Metric | FY2023 | FY2024 | FY2025 | FY2026 | Trend |
|---|---|---|---|---|---|
| Revenue ($M) | 4,392.9 | 4,527.2 | 4,665.4 | 4,868.8 | +3.0%, +3.1%, +4.4% — slow but re-accelerating (Q1 FY27 +5.5% per company release; Q2 FY27 +8.7% y/y vs Q1 FY26) |
| Gross margin | 74.9% | 76.2% | 75.8% | **77.0%** | Expanding |
| Operating margin | 5.6% | 11.6% | 17.4% | **23.1%** | Strong expansion — but see ⚠️ |
| FCF ($M) | 1,175 | 1,472 | 1,809 | **1,924** | FCF margin **39.5%** |
| FCF yield | — | — | — | **7.5%** (tool, $25.7B cap) / **6.9%** at $96.07 close | Healthy |
| SBC ($M) | 1,286 | 1,057 | 931 | **761 (15.6% of rev)** | Falling but still large |
| SBC-adj. FCF ($M) | — | — | — | **~1,163** (23.9% margin, ~4.2% yield) | True economic cash yield |
| Cash & ST inv. ($M) | 5,413 | 6,962 | 7,792 | **7,817** | |
| Total debt ($M) | 96.5 | 73.0 | 64.4 | **58.5** | Deleveraging to zero |
| Current ratio | — | — | — | **4.33** | |
| Quick ratio | — | — | — | **4.33** | No inventory |
| Cash ratio | — | — | — | **3.91** | |
| Working capital ($M) | — | — | — | **6,659** | |

**Liquidity:** cash alone covers current liabilities **3.9x** and total liabilities **3.6x**. Cash runway is not a meaningful constraint: even a scenario burning $300M/yr would take **26 years** to exhaust the cash pile. Receivables $497M = ~37 DSO; current liabilities of $2.0B are dominated by deferred revenue — i.e. **customers prepay ZM**, a structurally negative-working-capital model.

**FCF sustainability:** capex is trivial ($65M, 1.3% of revenue), so FCF tracks OCF almost 1:1. FY26 buybacks of **$1.62B exceeded SBC-adjusted FCF of $1.16B by ~$460M**, funded out of interest income on the cash pile — sustainable for years, but not indefinitely, and it means reported FCF overstates distributable cash by the SBC drag.

---

### 3. Market Risk Profile

| Measure | Value | Read |
|---|---|---|
| Annualised volatility (756d) | **39.6%** | Very high for a net-cash software name — ~2.5x market |
| Beta vs SPY (756d) | **0.95** (profile beta 1.018) | Low *systematic* risk; the risk is idiosyncratic |
| Max drawdown (756d) | **−25.9%** | Observed in-window: $111.88 (1-Jun-26) → $84.11 (23-Jul-26) = **−24.8% in 7 weeks** |
| Sharpe (0% rf) | **0.44** | Mediocre risk-adjusted return |
| 52-wk (observed) range | **$69.15 – $114.74** | Last close **$96.07**, ~16% below high, +39% above low |

Beta ~0.95 understates the risk: the danger is **earnings-gap risk**, not market beta. Observed single-day moves: **+14.7%** (22-Aug-25), **−11.7%** (26-Feb-26), **+9.2%** (22-May-26), **+9.9%** (1-Jun-26). Any position carries a realistic ±10–15% overnight gap each quarter. *Sortino ratio and downside deviation unavailable from tooling — data gap.*

---

### 4. Downside Scenario Analysis — Revenue −20% (FY26 base $4.869B → $3.895B)

Assumes COGS fully variable (gross margin holds at 77%) and opex ($845M R&D + $1,781M SGA = $2,626M) held flat:

| Line | Base FY26 | −20% revenue, no cost action | −20% revenue + 10% opex cut |
|---|---|---|---|
| Revenue | 4,869 | 3,895 | 3,895 |
| Gross profit | 3,750 | 3,000 | 3,000 |
| Opex | 2,626 | 2,626 | 2,363 |
| **Operating income** | **1,124** | **374** (−67%) | **637** (−43%) |
| Operating margin | 23.1% | 9.6% | 16.4% |
| Est. FCF | 1,924 | ~$860–975M (22–25% margin) | ~$1.0–1.1B |
| Cash + ST inv. | 7,817 | 7,817 + ~$270M interest income | same |

**Conclusion: ZM survives a −20% revenue shock with positive operating income, positive FCF, and ~$7.8B net cash untouched.** Stress it to **−35% revenue** ($3.16B): gross profit $2,437M vs flat opex $2,626M = **−$189M operating loss**, which a 15% opex cut eliminates entirely. Even then, the loss is <2.5% of the cash balance per year. **There is no plausible demand scenario in which ZM faces a liquidity or solvency event.** The 20% revenue decline would compress EV/FCF from ~10.5x to ~21x on my market-cap estimate — a valuation risk, not a survival risk.

---

### 5. Overall Financial Risk Rating: **LOW**

Balance-sheet risk is essentially nil (net cash, no debt, 4.3x current ratio, Z-score 5.1, F-score 8/9, 39.5% FCF margin). The rating is **LOW on solvency/liquidity**, but the **equity carries HIGH market risk**: 40% annualized vol, ±10–15% earnings gaps, decelerating-then-recovering top line, and a GAAP earnings base inflated by non-recurring items. Do not conflate the two — this is a low-credit-risk, high-equity-volatility asset.

---

### 6. Key Red Flags

1. **Quality of earnings — the biggest issue.** Reported net income is dominated by non-operating items: FY26 net income $1,900M vs operating income $1,124M (**$1,299M** gap), and Q2 FY27 net income $1,542M vs operating income $314M (**$1,681M** gap; the tool's EBIT of $1,995M vs operating income of $314M confirms the classification). This is almost certainly a **deferred-tax-asset valuation allowance release** (discrete, non-recurring). Consequence: GAAP EPS of $6.32 and the implied ~15x P/E are **illusory**; clean EPS is closer to ~$3.0, implying a **~28–30x clean multiple**. *(Inferred from data; no filing text fetched — confirm against the FY26 10-K tax footnote.)*
2. **SBC drag of $761M (15.6% of revenue).** Reported FCF of $1.92B overstates economic cash generation by ~40%; SBC-adjusted FCF is ~$1.16B (4.2% yield). Buybacks of $1.62B are running **ahead** of economic FCF.
3. **Margin expansion may be peaking.** Q2 FY27 operating margin 24.6% vs 26.4% in Q1 FY26 despite +8.7% revenue — COGS +6.8% and SGA +3% outgrew the top line. AI-related investment is compressing incremental margins.
4. **Structurally low organic growth (~4–6%)** against bundled competition (Microsoft Teams, Google Meet) and AI-native entrants — the −20% scenario is not a tail fantasy, it is a competitive-share-loss scenario.
5. **Volatility/gap risk:** 39.6% vol with ±10–15% earnings-day gaps on a stock whose balance sheet suggests bond-like risk. Position sizing must reflect equity risk, not credit risk.
6. **Capital allocation:** $1.62B buyback + rising goodwill (+$106M, to $472M) means M&A and repurchases, not the core, drive per-share outcomes.

### Data Gaps (explicit)
- **No quarterly cash-flow statement** — TTM FCF derived from FY26 annual only.
- **No deferred revenue / billings / RPO detail**, no customer count, NRR, or segment concentration — critical for judging the durability of the 77% gross margin.
- **No credit rating or CDS spread** — immaterial here (debt $58.5M), but unverified.
- **No Sortino/downside deviation**; max drawdown flagged on a 756-day window only.
- **Price/market-cap inconsistency in the feed:** profile price $83.28 → $24.30B cap, vs last close $96.07 (31-Jul-26) → ~$28.0B. All yields above are presented on both bases (6.9%–7.5%).
- **No peer benchmarking** performed (budget); leverage and margin comparisons are absolute, not relative.
