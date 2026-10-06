# Fin Risk Analyst

- Symbol: NOW
- Elapsed: 226.7s

---
I have sufficient data to complete the assessment. The web search feed failed twice (on retry), so credit rating/CDS details are flagged as a data gap. Here is the full report.

---

# FINANCIAL RISK ASSESSMENT — ServiceNow, Inc. (NOW)
**Sector:** Technology / Software – Application (cloud SaaS) | **HQ:** Santa Clara, CA | **Employees:** ~29,187 | **Market cap:** ~$143B (price ≈ $131–138) | As of FY2025 filings (filed Jan 2026)

---

## 1. Credit Risk Assessment — **INVESTMENT GRADE**

This is a **net-cash, low-leverage franchise with fortress-tier debt service capacity**:
- **Total debt $2.4B** (long-term only $1.5B, zero short-term debt) vs **cash $6.3B** → **net debt is −$3.9B** (net creditor).
- **Net debt/EBITDA = −1.29x** (negative = net cash), D/E 0.19x, debt/assets 0.09x.
- **Interest coverage 79.3x** (operating income $1.82B vs interest expense just $23M) — debt is essentially cosmetic; even under severe stress coverage remains in double digits.
- **Altman Z = 1.675 (tool: "distress zone") — methodological artifact, not true distress.** The score is dragged down by (a) x1 working-capital/assets of 0.0011 (asset-light subscription model, near-zero working capital) and (b) x4 using *book* equity (~0.99x) instead of the $143B market cap. With market-cap-based x4, the score would be far into the safe zone. Treat with skepticism for SaaS balance sheets.
- **Piotroski F-Score: 5/9 (Moderate)** — solid profitability/accruals and deleveraging, but flagged for **dilution (SBC $1.96B > net income $1.75B)**, ROA non-improvement, and flat gross-margin/asset-turnover (AI-era cost creep: gross margin fell ~1.7pts to 77.5%).

## 2. Key Financial Risk Metrics (FY2025)

| Metric | Value | Assessment |
|---|---|---|
| Debt / Equity | 0.19x | Low leverage ✔ |
| Net debt / EBITDA | −1.29x | Net cash ✔ |
| Interest coverage | 79.3x | Excellent ✔ |
| Debt / Assets | 0.09x | Minimal ✔ |
| Current ratio | 1.0x | Adequate (thin buffer) |
| Quick ratio | 1.0x | Adequate |
| Cash ratio | 0.6x | Cash = 60% of current liabilities |
| Working capital | $28M | ~zero (SaaS float model) |
| Cash & ST investments | $6.28B | Strong absolute war chest |
| Altman Z / Piotroski F | 1.675 / 5 | Artifact / Moderate |
| FCF / FCF yield | $4.58B / 3.16% | Growing, but yield is thin |
| Revenue / EBITDA / NI | $13.28B / $3.00B / $1.75B | Strong growth, 22.5% rev CAGR '21–'25 |
| Operating margin | 13.7% (from 4.9% in '22) | Improving ✔ |
| Interest expense | $23M | Trivial |

**Liquidity view:** No short-term debt, no dividend, buybacks discretionary. Cash covers >4× total debt and ~1.2× FY25 FCF. Current liabilities ($10.4B) are dominated by deferred revenue/prepayments — a "good" liability. **No refinancing cliff**: only $1.5B LT debt vs $6.3B cash. Debt-maturity schedule and revolving-facility access were not retrievable from tooling (data gap), but the quantum is immaterial at this leverage.

## 3. Market Risk Profile (252-day window, SPY benchmark)

| Measure | Value | Reading |
|---|---|---|
| Annualised volatility | **63.1%** | Very high for a ~$143B mega-cap |
| Beta vs SPY | 0.574 | Below-market systemic sensitivity ✔ |
| Max drawdown (3-yr) | **−46.3%** | Severe tail risk |
| Sharpe (0% RF) | 0.083 | ~zero risk-adjusted return |

**Narrative:** 3-year path $77 (Jan '23) → peak ~$234 (Jan '25) → ~$131 (mid-Jan '26) = **~−44% off peak**, including a −11.6% single-day drop on 12/15/2025 on a 148M-share volume spike (likely a major block/secondary or earnings-event dislocation) and a 48M-share print on 11/19/25. Beta is defensive, but **idiosyncratic volatility is the story here** — this stock carries equity-market tail risk that is NOT hedged by its balance sheet. Yield-curve backdrop: 2Y 4.65% / 10Y 4.99% (+34bp, not inverted) — expensive debt, irrelevant to a net-creditor.

## 4. Downside Scenario — Revenue −20% ($13.28B → $10.62B)

Assumptions: SaaS cost base (COGS $3.0B, SGA $5.5B, D&A $0.7B) largely fixed; assume management recovers ~half the revenue hit via SGA cuts.

| Metric | Base | −20% revenue (w/ cost actions) |
|---|---|---|
| EBIT (est.) | $1.82B | ≈ +$0.5B (no-cost-action case: ≈ −$0.8B) |
| Interest coverage | 79.3x | ~21x — still investment grade |
| Net debt / EBITDA | −1.29x | ≈ −2.3x (still net cash) |
| FCF | $4.58B | ≈ $3.2–3.5B (still strongly positive) |
| Cash | $6.28B | Unchanged — >6-yr runway even at a $1B/yr cash burn |
| Z-score | 1.675 | Deteriorates further on paper (artifact persists) |

**Verdict: ServiceNow survives a 20–30% revenue drawdown without covenant, refinancing, or solvency stress.** The genuine downside is **equity-market**: at a 3.16% FCF yield, a growth-or-AI-disappointment episode compresses the multiple fast (cf. the −46% drawdown already recorded). This is an asset-allocation risk, not a credit event.

## 5. Overall Financial Risk Rating: **MODERATE**
**Decomposition: Credit risk LOW | Liquidity risk LOW | Market risk HIGH | FCF sustainability LOW-MODERATE.**
The balance sheet is investment-grade and controversially defensive (net cash, ~80x coverage, 22% revenue CAGR, 34.5% FCF margin improving). The rating is held up to Moderate by **market risk** (63% vol, 46% drawdown, ~0 Sharpe, thin 3.16% FCF yield) and by **earnings-quality leaks** (SBC exceeds net income; buyback consumes 40% of FCF). Nothing in the credit profile supports High or Critical.

## 6. Key Red Flags
1. **Earnings-quality split:** Stock-based comp ($1.96B) > net income ($1.75B); ~2%/yr shareholder dilution — F-Score penalizes (dilution flag).
2. **Tool-flagged Altman Z in distress zone (1.675)** — argued above as an asset-light/book-equity artifact, but it must be monitored and re-derived with market-capitalized x4 before any credit decision relies on it.
3. **Extreme idiosyncratic volatility:** 63% annualized, −46% max drawdown, 12/15/25 −11.6% / 148M-share dislocation — investigate block trades, ownership concentration, and guidance risk.
4. **Zero working capital / current ratio exactly 1.0:** no balance-sheet buffer in the classic sense; resilience depends on ongoing renewal float (deferred revenue), not on stored working capital.
5. **Valuation-rich:** 3.16% FCF yield — modest for a large-cap software franchise; multiple-compression risk is the dominant tail.
6. **Data gaps:** (a) agency credit rating / CDS spreads — web feed timed out twice, not retrievable (implied by metrics: strong IG equivalent); (b) **debt maturity schedule & credit-facility access not available** in tooling; (c) sector-peer tool returned semiconductor mega-caps, not software comparables — I substituted Salesforce: NOW is markedly better positioned (CRM net debt/EBITDA +0.58x vs NOW −1.29x; NOW coverage 79x vs CRM 27.5x).
