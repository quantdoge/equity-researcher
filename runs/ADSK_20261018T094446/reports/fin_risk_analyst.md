# Fin Risk Analyst

- Symbol: ADSK
- Elapsed: 59.2s

---
## ADSK — Financial Risk Assessment
**Autodesk, Inc. | Technology / Software–Application | FY2026 (ended 31-Jan-2026) | Mkt cap ~$50.1B**

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE**

ADSK is a low-leverage, high-margin, strongly cash-generative subscription business. **Net debt of ~$485M against $1.906B EBITDA (0.25x)** is effectively de minimis; the leverage tool's 0.07x uses a broader cash definition (incl. short-term investments) but the conclusion is identical under either method. Gross debt is only $2.734B against $12.467B of assets.

External confirmation: S&P rates ADSK **BBB+ issuer (stable)**, senior unsecured notes **BBB**, citing "very high recurring revenue and minimal financial risk" (S&P, 2025). Debt is a **laddered senior unsecured note stack (~$2.5B principal)**, with the June 2025 $1.0B 10-year (due 2035) refinancing a term loan — leaving **no material maturity before 2029–2031**. This is a genuinely back-ended maturity profile, not a refinancing cliff.

Interest coverage: **data gap.** The income statement reports interest expense of $0 for FY24–FY26, which is not credible against $2.5B of notes. FY2023 (pre-refinancing, $71M) is the last clean reading, and blended coupon on the current stack (~2.4%–5%+ across series) implies ~$85–100M. On that estimate, **EBIT/interest ≈ 18–21x**. Coverage is not a risk at any plausible interest level.

**No covenant risk identified** — investment-grade unsecured notes of this type carry no financial maintenance covenants.

---

### 2. Key Financial Risk Metrics

| Metric | FY2026 | FY2025 | FY2024 | FY2023 | Assessment |
|---|---|---|---|---|---|
| Revenue ($M) | 7,206 | 6,131 | 5,497 | 5,005 | +17.5% YoY; 12.9% 3yr CAGR |
| Gross margin | 92.3% | 90.6% | 90.7% | 90.4% | Best-in-class |
| Operating margin | 21.9% | 22.3% | 20.5% | 19.8% | Stable/expanding |
| EBITDA ($M) | 1,906 | 1,564 | 1,275 | 1,167 | +64% over 3 yrs |
| Net debt / EBITDA | **0.25x** | 0.61x | 0.58x | 0.62x | Deleveraging |
| Debt / equity | 0.90x | 0.98x | 1.42x | 2.33x | Rapidly improving |
| Debt / assets | 0.22x | 0.24x | 0.26x | 0.28x | Low |
| Interest coverage (EBIT) | ~18–21x *(est.)* | n/a *(data gap)* | n/a | 14.3x | Very strong |
| Current ratio | **0.85x** | 0.68x | 0.82x | 0.84x | ⚠️ See note — artifact |
| Quick / cash ratio | 0.85x / 0.45x | — | — | — | Cash-rich |
| Working capital ($M) | **(866)** | (1,669) | (772) | (659)** | Deferred-revenue driven |
| Altman Z (book equity) | **1.01 — "Distress"** | — | — | — | ⚠️ False positive |
| **Altman Z (market cap adj.)** | **~4.00 — Safe** | — | — | — | Corrected reading |
| Piotroski F-Score | **8 / 9 — Strong** | — | — | — | Only miss: ROA trend |
| FCF ($M) | 2,409 | 1,567 | 1,282 | 2,025 | Record year |
| FCF margin | 33.4% | 25.6% | 23.3% | 40.5% | Recovering strongly |
| FCF yield | **4.67%** | — | — | — | Solid |
| FCF / net income | 2.14x | 1.41x | 1.41x | 2.46x | High cash conversion |

**Critical adjustment — Altman Z-Score.** The reported 1.01 ("Distress") is a **methodological false positive**, and I would not present it to an investment committee unadjusted. Three distortions compound:
- **x4 uses book equity ($3.045B) instead of market cap ($50.1B).** Re-running with market cap: x4 = 50.14/9.42 = 5.32, giving **Z ≈ 4.00 — firmly in the safe zone**.
- **Negative retained earnings (−$1.432B)** depress x2 (−0.115). This is the cumulative residue of buybacks, not accumulated losses — the company has been profitable every year.
- **Goodwill/intangibles of $4.762B (38% of assets, 156% of book equity)** compress tangible equity to roughly **−$1.7B**, which the model cannot see through.

**Current ratio of 0.85x is likewise an artifact.** ADSK's current liabilities ($5.808B) are dominated by **deferred revenue** (billings collected up front and recognized over the subscription term) — a non-cash, non-claim liability. Excluding an estimated $3.9–4.2B of current deferred revenue (my estimate; not directly disclosed in the tool output), adjusted current liabilities are ~$1.7–1.9B against $4.942B of current assets, implying an **adjusted current ratio of ~2.6–2.9x**. Liquidity is strong, not weak.

---

### 3. Market Risk Profile

| Measure | Value | Read |
|---|---|---|
| Annualised volatility (3Y) | **33.7%** | High absolute risk; typical for high-beta software |
| Beta vs SPY (computed, 756d) | **0.81** | ⚠️ Conflicts with vendor 5Y beta of **1.33** |
| Max drawdown (3Y) | **−42.6%** | Severe — a real capital-impairment event |
| Sharpe ratio (0% RF) | **0.082** | Very poor risk-adjusted return |

The **beta discrepancy is material and I flag it rather than resolve it**: the regression beta (0.81, likely influenced by idiosyncratic de-rating episodes) and the vendor fundamental beta (1.33) point in opposite directions. For stress-testing I would use **1.3** as the conservative assumption — a market drawdown of −25% would imply roughly −33% for ADSK. The −42.6% realized drawdown confirms the stock is a **high-torque instrument**. Sharpe of 0.082 implies roughly 2.8% annualized return across three years — investors have been paid almost nothing for 34% volatility. This is a **market-risk problem, not a solvency problem**: equity can be halved without threatening the franchise.

---

### 4. Downside Scenario Analysis

**Scenario A — Revenue −20% (−$1,441M to $5,765M).** Assumes COGS ~60% variable, SGA −12%, R&D −12%.

| | Base | −20% Revenue |
|---|---|---|
| Revenue | 7,206 | 5,765 |
| Gross margin | 92.3% | 91.5% |
| Operating income | 1,578 | **~812** (14.1% margin) |
| EBITDA | 1,906 | ~1,140 |
| Interest (est.) | ~90 | ~95 |
| Interest coverage | ~20x | **~8.5x** |
| Net debt / EBITDA | 0.25x | **~0.4x (net cash)** |
| FCF | 2,409 | ~$1.3–1.5B (≈24% margin) |
| Piotroski | 8 | ~6–7 |

**Verdict: easily survivable.** ADSK would still print ~14% operating margins, ~$1.4B of FCF, and net cash. Management could cut buybacks ($1.4B run-rate) to zero and *add* $1.4B of liquidity. No covenant, no maturity wall inside 3 years.

**Scenario B — Severe: Revenue −35% (−$2,522M to $4,684M).** Deeper cost cuts (SGA −20%, R&D −22%).

- Operating income collapses to **~$244M (5.2% margin)**, EBITDA ~$440M
- Interest coverage ~2.6x — thin but positive
- **Net debt/EBITDA ~6.2x** — this is the level that would force a **downgrade to BBB−/BB+** and raise refinancing cost on the 2031/2035 notes
- FCF roughly breakeven to +$600M; buyback would be suspended

**Verdict: still solvent, but credit profile meaningfully impaired.** The path to distress requires bankruptcy, and even at −35% revenue ADSK services its debt from EBITDA. Distress is not a realistic near-term outcome.

---

### 5. Overall Financial Risk Rating: **LOW**

Balance-sheet risk (LOW), liquidity risk (LOW once deferred revenue is normalized), credit risk (LOW — BBB+/0.25x net leverage/laddered maturities), and FCF sustainability (LOW–MODERATE) are all supportive. The dominant risks here are **market/valuation risk (HIGH)** and **earnings-quality items (MODERATE)** — not solvency.

---

### 6. Key Red Flags

1. **SBC is a real, growing economic cost — 11% of revenue.** SBC of $788M (+15% YoY, 32% of OCF) is added back in reported FCF. **SBC-adjusted FCF = ~$1.62B, adjusted FCF yield ~3.2%, not 4.67%.** Of the $1.402B spent on buybacks, roughly $790M simply neutralizes dilution; net share reduction was only ~1% (215M → 213M). Genuine capital return is far smaller than headlines suggest.
2. **Buybacks have consumed the equity cushion.** At $1.4B/yr against $2.4B of FCF (58% payout), retained earnings sit at **−$1.432B** and tangible book equity is **negative (~−$1.7B)**. Goodwill/intangibles at 156% of book equity means any impairment lands on an already thin base.
3. **Altman Z-Score of 1.01 is a false signal** — corrected to ~4.0 on market capitalization. Flagging explicitly so this is not misread in the memo.
4. **Working-capital drag of −$1.161B inside FY26 OCF.** Headline FCF of $2.4B was achieved *despite* a large WC headwind — a positive quality signal, but it also means reported FCF is volatile with billing-model timing (visible in the FY23→FY24 collapse from $2.03B to $1.28B).
5. **Poor realized risk-adjusted returns.** Sharpe 0.082 and a −42.6% max drawdown mean equity holders have absorbed severe volatility for negligible return. Beta ambiguity (0.81 vs 1.33) should be resolved before sizing.
6. **Interest expense reported as $0 across FY24–FY26** despite $2.5B of notes outstanding — an unresolved data-quality issue in the feed.

---

### 7. Data Gaps (explicitly flagged)

- **Interest expense: unavailable for FY24–FY26.** Coverage ratios are estimates (~18–21x) derived from FY2023 actuals and modeled coupons, not reported figures.
- **Deferred revenue split (current vs. non-current): not returned by the tools.** My adjusted current ratio (~2.6–2.9x) is an estimate; confirmation from the 10-K balance sheet would firm this up materially.
- **D&A inconsistency:** the income statement shows FY26 D&A of $98M while the cash flow statement shows $195M. EBITDA of $1.906B (built off the income-statement figure) may be modestly overstated.
- **D&A/FY25 anomaly:** income statement D&A of $180M vs. $230M in cash flow — recurring inconsistency.
- **Peer comparison not meaningful:** the sector screen returned mega-cap semis (NVDA, AAPL, MSFT, TSM, AVGO, MU), which are not valid comps for application software. No peer multiples used.
- **CDS spreads: not available** from the toolset. Credit assessment relies on S&P's BBB+/BBB ratings and internal metrics.
