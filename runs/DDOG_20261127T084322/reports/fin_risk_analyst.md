# Fin Risk Analyst

- Symbol: DDOG
- Elapsed: 47.5s

---
## DDOG — Financial Risk Assessment
*Data through Q3 FY2026 (quarter ended 2026-09-30); latest audited balance sheet 2025-12-31. Market data as of latest close ($158.25, mkt cap ≈$57.1B).*

### 1. Credit Risk Assessment: **INVESTMENT GRADE (balance-sheet equivalent; unrated)**
Datadog carries **$1.54B total debt against $4.47B cash & short-term investments → net cash of ~$2.94B** (net debt/EBITDA of **−15.2x**, per `calculate_leverage_ratios`). The debt stack is dominated by a **$1.0B 0.00% convertible senior note due Dec 1, 2029** (upsized offering, Dec 2024), i.e. zero coupon, ~3 years to maturity, and fully covered ~4.5x by cash on hand. There is **no refinancing cliff**. The reported "interest coverage of −4.01x" is an artifact of FY2025 GAAP operating income being **−$44.4M** (SBC of $750.7M); on a TTM basis EBIT coverage is **~6.2x** and EBITDA coverage **~24x**, and cash interest is immaterial ($15.7M TTM, mostly lease/imputed).

### 2. Key Financial Risk Metrics

| Metric | Value | Read |
|---|---|---|
| Total debt / equity | 0.41x (23% of assets) | Low |
| Net debt / EBITDA | **−15.2x (net cash $2.94B)** | Strong |
| Interest coverage (FY25 op. income / int.) | −4.01x → **TTM 6.2x; EBITDA 24x** | Improving |
| Current / quick / cash ratio | **3.38 / 3.38 / 2.81** | Very strong |
| Working capital | **$3.79B**; cash/liabilities 1.54 | Very strong |
| Altman Z-Score | **2.07 — Grey zone** | Caveat: tool uses *book* equity (x4=1.28). At market cap $57.1B, x4≈19.6 → Z would be **>10, deep safe zone** |
| Piotroski F-Score | **6/9 — Moderate** | Loses points on ROA decline, dilution, GM trend |
| FCF (TTM) | **$1.17B, 27.4% margin** | Strong but decelerating |
| FCF yield | **1.74–2.05%** (~13.3x TTM sales) | Low absolute yield — valuation, not solvency, risk |

**FCF track record:** $354M (2022) → $632M (2023) → $836M (2024) → $1,001M (2025) → **$1,171M TTM**. Growth is intact (+17% y/y) but **FCF margin has rolled over: 31.1% → 29.2% → 27.4%**, with capex up ~3x y/y ($96.7M TTM) and working capital a drag in 3 of the last 4 quarters. Notably, Q3'26 FCF fell to $250.6M (20.9% margin) on record revenue.

### 3. Market Risk Profile — **HIGH (the dominant risk here)**
- **Annualised volatility 60.2%** (756d) vs SPY
- **Beta 1.30** (tool, vs SPY); company-reported beta 1.51 — equity amplifies market drawdowns ~1.3–1.5x
- **Max drawdown 48.6%** over 3 years
- **Sharpe ≈ 0.53** (0% rf) — mediocre risk-adjusted return; Sortino not available (**data gap**)
- Acute event risk: Q3'26 revenue beat by 4.6% (+35.2% y/y to $1.20B) yet **the stock fell ~16%** on Q4 guidance implying flattish sequential growth. Consumption/usage-based pricing gives the model high downside torque to customer optimization.

### 4. Downside Scenario: revenue −20%
TTM base: revenue $4,278M, gross margin 79.6%, opex $3,308M (77.3% of revenue), op. income $97M, FCF $1,171M.

| Case (rev −20% → $3,423M) | Opex action | Op. income | FCF est. |
|---|---|---|---|
| A. Partial flex | −10% ($2,977M), GM 77% | **−$341M** | **−$300M to −$200M** |
| B. Aggressive cost-out | −20% ($2,646M) | **−$10M** | **$0 to +$150M** (WC release) |
| C. Severe: rev −30% | −15% | **−$506M** | **−$450M** |

**Survivability: effectively unimpaired.** Even the severe case burns ~$450M/yr against $4.47B cash + $3.79B working capital — **~10 years of runway with zero capital access**, and the 2029 converts can be retired from cash. Covenant breach risk: none identified (no financial maintenance covenants disclosed; converts are unsecured). Equity holders, however, face multiple compression: at 13.3x sales, a de-rating to peer-growth multiples could compound the earnings hit — a 20% revenue cut plausibly implies a 40–55% equity decline (consistent with the observed 48.6% max drawdown).

### 5. Overall Financial Risk Rating: **MODERATE**
Solvency and liquidity risk: **Low**. Market/valuation risk: **High**. Blended: Moderate. This is a net-cash, high-FCF-margin business whose risk is entirely in the equity multiple and in SBC-driven dilution — not in the capital structure.

### 6. Key Red Flags
1. **GAAP operating losses at scale**: FY2025 operating income **−$44M** (−1.3% margin) on $3.43B revenue, a reversal from +$54M in FY2024.
2. **SBC = 20.1% of revenue** ($859.7M TTM). FCF ex-SBC is only **$311M (7.3% margin)** — the headline 27% FCF margin is substantially a non-cash comp artifact.
3. **Persistent dilution**: diluted shares 315M (2022) → 375M (Q3'26), ~4.5%/yr; Piotroski F7 = 0, no buyback.
4. **FCF margin erosion** (31.1% → 27.4%) plus 3x capex step-up — watch FY2026 FCF trajectory.
5. **Growth deceleration shock**: stock −16% post-Q3'26 on flat sequential Q4 guide; usage-based model cuts both ways.
6. Gross margin drifting down (80.8% → 79.6%), Piotroski F8 = 0.

**Data gaps flagged:** no S&P/Moody's rating or CDS spread accessible (appears unrated); Sortino ratio and 52-week price series not retrieved; composition of the ~$0.5B non-convert debt (assumed leases) and full maturity schedule unverified; no covenant documentation reviewed. The 2029 note price quote (negative implied yield on Public.com) is unreliable and not used.
