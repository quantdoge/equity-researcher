# Fin Risk Analyst

- Symbol: LITE
- Elapsed: 88.9s

---
## Financial Risk Assessment — Lumentum Holdings Inc. (LITE)

**Critical data-integrity note before the analysis:** FY2026 (ended 27-Jun-2026) shows operating income of **+$524.8M** but net income of **−$6.94B**. This is not an operating deterioration. Per the company's FY26 results and 10-K, the loss is driven by a **one-time, non-cash charge (~$7.8B) tied to its US deferred tax asset valuation allowance** (Q4 alone contains −$7.16B). Raw screening outputs — EBITDA of −$6.88B, Altman Z of −2.99, ROA — are **contaminated by this charge and are unusable as reported**. I have rebuilt every ratio below on operating/cash economics.

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE profile**

| Metric | FY2026 | Read |
|---|---|---|
| Total debt | $1,671.2M | ST $1,596.9M + LT $40.5M |
| Cash & ST investments | $2,738.4M | **1.64x total debt** |
| **Net cash** | **+$1,067.2M** | Net *creditor*, not net debtor |
| Interest coverage (EBIT/Int.) | **24.1x** | Q1-FY27 run-rate 147x ($2.4M int.) |
| Gross debt / EBITDA | 2.1x | Net debt/EBITDA negative |
| Debt/equity · Debt/assets | 0.36x · 0.23x | Conservative |
| Equity/assets | 0.64 | Equity $4,643.9M |

The company could retire **100% of its debt from cash on hand** and still hold ~$1.07B. Tangible equity is $3.25B even after stripping $1.40B of goodwill/intangibles (30% of book equity). There is no covenant story, no insolvency story, and no liquidity story here.

### 2. Key Financial Risk Metrics

| Metric | Value | Assessment |
|---|---|---|
| Net debt / EBITDA | **−1.35x** (net cash) | Strong |
| Interest coverage | 24.1x (FY26) | Strong |
| Current / Quick / Cash ratio | 1.68 / 1.40 / 1.10 | Adequate |
| Working capital | +$1,681.4M | Positive |
| Cash / near-term debt | 1.71x | Covered |
| **Altman Z (as reported)** | **−2.99 "Distress"** | **INVALID** (see below) |
| Altman Z (adj., operating EBIT, book equity) | ~0.48 | Distress zone |
| Altman Z (adj., market cap ×4) | ~13.4 | Safe zone |
| **Piotroski F-Score** | **6/9** (as reported) | Moderate |
| Piotroski F-Score (adj.) | **~8/9** | Strong |
| FCF (FY26) | +$300.1M | FCF margin 10.0% |
| FCF yield | **0.48–0.59%** | **Very weak** |
| Capex / revenue | 15.0% | Heavy capacity build |

**Why Altman Z must be discarded:** its two negative drivers are (a) x3, which uses the loss-contaminated EBIT of −$7,151M rather than the true $524.8M operating figure, and (b) x2, retained earnings of **−$7,796M** — an accumulated *accounting* deficit, not a forward cash obligation. Because x4 is equity-denominated, the score swings from 0.48 (book) to 13.4 (market) depending on an arbitrary input. It carries zero informational content for a net-cash company. **Do not use this signal.**

**Why F-Score understates:** F1 (positive ROA) and F3 (ROA improvement) fail *only* because of the tax charge; on operating ROA (7.2%), both pass. The single legitimate failure is **F7 (dilution)** — see red flag #4. Adjusted strength is ~8/9.

### 3. Market Risk Profile — **SEVERE**

| Metric | Value |
|---|---|
| Annualised volatility (3y) | **83.9%** |
| Beta vs SPY | **2.53** (3y daily); 1.64 (profile, 5y) |
| Max drawdown (3y) | **−50.6%** |
| Sharpe (rf = 0%) | 1.87 |
| Implied 1-day 99% VaR | ≈ **−12.3%** |

Volatility of ~84% is roughly **4.5–5x the index**. A beta of 2.53 means a 20% market drawdown implies a **~50% loss** in LITE — precisely the observed max drawdown. The 1.87 Sharpe is respectable, but it is compensation for raw return, not for safety: this is a high-momentum, high-dispersion asset. *Data gap: Sortino ratio and downside deviation were not available; CDS spreads unavailable.*

### 4. Downside Scenario Analysis — Revenue −20%

Assumes 65% of COGS variable ($1,142.8M) / 35% fixed ($615.3M), opex flexed −5%.

| | Base FY26 | −20% revenue | −40% (severe) |
|---|---|---|---|
| Revenue | $3,014.0M | $2,411.2M | $1,808.4M |
| Gross profit | $1,255.9M (41.7%) | $881.7M (36.6%) | $507.4M (28.1%) |
| Operating income | $524.8M (17.4%) | **$187.2M (7.8%)** | **−$136.0M (−7.5%)** |
| EBITDA | $791.8M | $454.2M | $131.0M |
| Interest coverage | 24.1x | 8.6x | 6.0x (EBITDA) |
| Gross debt/EBITDA | 2.1x | 3.7x | 12.8x |
| Est. FCF | +$300.1M | **≈ −$50M** | **≈ −$50M** |
| Cash position | $2,738M | ~$2,700M | ~$2,650M |

**Conclusion: the balance sheet survives even a −40% demand collapse.** At −20%, operating income falls 64% (margin 17.4%→7.8%) and free cash flow turns marginally negative — but the company funds that from a $2.7B cash pile and would still hold net cash. Even the severe case leaves ~$1.6B of debt maturing inside 12 months **fully covered 1.7x by cash**. **The risk in this name is not solvency — it is multiple compression.** At ~20.6x FY26 sales (12.3x annualised Q1-FY27 sales) and a 0.5% FCF yield, a 20% revenue miss would likely trigger a 50–60% equity de-rating even though the company remains financially sound.

*Supporting momentum (mitigant):* Q1 FY2027 revenue $1,262.6M (+136% YoY vs $533.8M), gross margin 51.0%, operating margin 28.0%, diluted EPS $3.54 — the trajectory is currently the opposite of the downside case.

### 5. Overall Financial Risk Rating — **MODERATE**

Weighted by component: **Credit risk LOW · Liquidity risk LOW · FCF sustainability MODERATE (improving) · Market/valuation risk VERY HIGH.** The balance sheet is fortress-grade; the equity is not. Risk is almost entirely transferred from the lender to the shareholder.

### 6. Key Red Flags

1. **Extreme equity volatility (84% ann., beta 2.53, −50.6% max drawdown).** Position sizing, not credit analysis, is the binding constraint. 1-day 99% VaR ≈ −12%.
2. **Valuation-dependent solvency for shareholders.** ~20.6x sales and a **0.5% FCF yield** leave no margin for error; the −20% case impairs equity far more than the business.
3. **Dilution is real and accelerating.** Basic shares 74.6M → **92.5M (+24% YoY)**; June-2026 exchange of $650.4M of 0.50% 2028 converts for ~5M shares. FY26 SBC $170.2M = **5.6% of revenue**. This is the only genuinely failed Piotroski test (F7).
4. **$1,596.9M of debt reclassified to current** (from $10.6M ST in FY25) — a near-term maturity wall. Fully cash-covered today, but it converts a perpetual liability into a refinancing event at a moment of market stress.
5. **Working capital is absorbing cash:** receivables +108% YoY ($250.0M→$520.3M), inventory +47% ($470.1M→$691.6M), WC drag −$292.0M. Growth is being funded, not generated. Watch inventory obsolescence if the AI-datacom cycle inflects.
6. **Capex intensity 15.0% of revenue** ($451.3M) and rising — capacity commitments are largely fixed and would not flex down quickly in a downturn, which is why the −20% case goes FCF-negative.
7. **Customer concentration is unquantified (data gap).** Optical component demand is concentrated in a handful of hyperscalers; this is the single largest unmeasured risk to the downside case.
8. **Negative retained earnings of −$7,796M** will keep triggering false "distress" flags in mechanical screens and constrains capital returns.

### Explicit Data Gaps
No public credit ratings or CDS spreads retrieved (I assess credit quality from fundamentals only). Sortino/downside deviation unavailable. R&D expense not broken out in the feed (opex derived as gross profit − operating income = $731.1M). Quarterly D&A is misreported as $0 for Q1-FY27. Reported EBITDA/EBIT fields are net-income-derived and unreliable across all periods — I used operating income + D&A throughout.
