# Fin Risk Analyst

- Symbol: RKLB
- Elapsed: 55.7s

---
# RKLB — Financial Risk Assessment
**Rocket Lab USA, Inc.** | Industrials / Aerospace & Defense | US
*Basis: FY2025 audited + TTM through Q2 2026 (quarter ended 6/30/2026, filed 8/10/2026)*

---

## 1. Credit Risk Assessment

**Rating: Sub-Investment Grade (unrated) — but with a near-zero 3-year default probability**

This is an unusual split verdict, and the split matters. On an *earnings* basis RKLB has no credit support at all: TTM EBIT is **-$198.6M**, TTM EBITDA is **-$122.0M**, and interest coverage is negative. On a *balance-sheet* basis it is one of the most over-capitalized companies in the sector: **$2,302M of cash and short-term investments against $133.7M of total debt** — net cash of **$1,996M**, equal to 57% of total assets and 57% of market cap.

The debt structure is not a risk. The company's 4.250% Convertible Senior Notes due 2029 were largely retired — **only $37.6M remained outstanding as of 3/31/2026**, and reported long-term debt fell to $14.8M at Q2 2026, with the residual balance sheet debt (total $133.7M vs. $14.8M LTD) attributable to finance leases. **There is no refinancing cliff.** Interest expense has collapsed to a ~$3M annual run-rate (Q2'26: $0.58M) against ~$90M+ of annual interest *income* on the cash pile — RKLB is net-interest-income positive.

The decisive credit fact: cash grew from $1,016.6M (12/31/25) to $2,302.2M (6/30/26), and equity from $1,721.9M to $3,492.2M, via roughly **$1.77B of equity issuance plus stock-funded M&A** — not from operations. Credit risk is therefore a function of *capital-markets access*, not cash generation. That access has been excellent, but it is equity-market dependent and it is bought with dilution.

## 2. Key Financial Risk Metrics

| Metric | Value | Read |
|---|---|---|
| Total debt / equity | 3.8% (Q2'26) · 15% (FY25) | Negligible leverage |
| Net debt / EBITDA | **-$1,996M net cash** (FY25 tool: 4.91x) | Ratio meaningless — EBITDA negative; tool value is a false positive |
| Interest coverage (EBIT/int.) | **-8.6x** (FY25) · -26.6x TTM | Negative by construction; absolute interest trivial |
| Debt / assets | 3.2% | Effectively unlevered |
| Current ratio | **5.48x** (Q2'26) · 4.08x (FY25) | Exceptional |
| Quick ratio | 4.98x | Exceptional |
| Cash ratio | **4.36x** | Exceptional |
| Working capital | $2,368M | — |
| Altman Z-Score | **1.61 — "Distress" zone** | Structurally distorted, see note |
| Piotroski F-Score | **5 / 9 — Moderate** | Fails on ROA, OCF, **dilution**, asset turnover |
| FCF yield | **-1.14%** (FY25) · -1.17% TTM | FCF -$321.8M / -$371.1M; trivial vs. $31.8B cap |
| Gross margin | 9.0% → 21.0% → 26.6% → 34.4% → **37.3% TTM** | Consistent 400–500bp/yr expansion |
| Operating margin | **-25.8% TTM** (vs. -38.0% FY25) | Improving |
| SBC / revenue | **10.6% TTM** ($81.6M) | Real, recurring cost |

**Altman Z caveat (important):** the 1.61 score is not a bankruptcy signal here. X2 (-0.435) and X3 (-0.086) are negative because of the accumulated deficit (-$1,106M) and negative EBIT — genuine, but not solvency events for a company holding $2.0B net cash. Meanwhile X4 uses *book* equity (2.86); on market cap ($31.8B / $695M liabilities) X4 would be **~45.7**, producing a Z-score in the mid-20s. The metric is unreliable in both directions for a pre-profit growth company. **I do not rely on it.**

**Piotroski detail:** the lost points are F1 (negative ROA), F2 (negative operating cash flow), **F7 (share issuance — no dilution)**, and F9 (asset turnover). Three of four lost points are capital-structure/scale artifacts, not deterioration. The four earned leverage/efficiency points confirm the balance sheet is strengthening.

## 3. Market Risk Profile

*Computed from RKLB's own daily close series (1/3/2023–2/27/2026, 800 obs) sampled to 37 monthly returns. Tool `calculate_price_volatility` unavailable on this subscription.*

| Metric | Value |
|---|---|
| Annualised volatility | **~110%** (month-end basis; daily-basis implied ~90–100%) |
| Beta vs. market | **2.61** (vendor-supplied — *unverified, see gaps*) |
| Max drawdown (close-to-close, 3yr) | **-40.8%** (10/9/25 $66.42 → 11/20/25 $39.32) |
| Max drawdown (intraday) | **-46.5%** (10/10/25 $73.50 → 11/20/25 $39.32) |
| Current drawdown from 1/16/26 peak ($96.30) | **~-28%** at $69.10; **~-45%** at current profile price of $53.07 |
| Sharpe ratio | **~1.17** (0% rf) |
| Sortino ratio | **~2.26** |
| Downside deviation (annualised) | ~59% |
| 3-year total return | **+1,685%** (3.17yr CAGR ≈ 148%) |
| Realised monthly volatility | 32.8% — i.e. a *typical month* moves ±33% |

**Interpretation:** the risk-adjusted return has been genuinely excellent (Sharpe 1.17, Sortino 2.26) — but that is return *level*, not return *quality*. A 111 percentage-point gap between annualised return and volatility is the signature of a momentum/theme-driven name. The beta of 2.61 means a 20% market drawdown implies a ~50% RKLB drawdown mechanically; the historical max drawdown confirms ~-41% is a *routine* event, not a tail event. **Equity risk is extreme even though credit risk is minimal.**

## 4. Downside Scenario Analysis — Revenue -20%

Applied to TTM revenue of **$769.1M** (→ $615.3M), holding the 37.3% TTM gross margin, with opex of $485.2M (TTM SG&A $197.7M + implied R&D ~$287.5M):

| Line | Base (TTM) | -20% revenue, no cost action | -20% revenue, 15% opex flex |
|---|---|---|---|
| Revenue | $769.1M | $615.3M | $615.3M |
| Gross profit (37.3%) | $286.6M | $229.6M | $229.6M |
| Operating expenses | $485.2M | $485.2M | $412.4M |
| **Operating income** | **-$198.6M** | **-$255.6M** | **-$182.8M** |
| Adj. EBITDA (ex-SBC) | ~-$40.4M | ~-$98M | ~-$61M |
| **Free cash flow** | **-$371.1M** | **~-$390M** | **~-$340M** |
| Cash (Q2'26) | $2,302M | $2,302M | $2,302M |
| **Cash runway at that burn** | — | **~5.9 years** | ~6.8 years |

**Conclusion: the company survives a 20% revenue decline with no financing at all for ~6 years.** There is no covenant to breach (effectively no debt), no maturity wall (2029 converts 85%+ retired), and no dividend or buyback obligation. *Solvency is not the downside case.*

**The downside case is equity-side.** At **~38.7x EV/TTM sales** (EV ≈ $29.8B) with negative EBITDA, a 20% revenue miss is not a 20% stock event — it is a multiple-compression event. History is instructive: revenue grew every quarter through the 2025-26 drawdowns, yet the stock fell 41% in six weeks on no fundamental deterioration. A revenue-driven de-rating of 40–60% is the realistic downside, producing a $12–19B market cap — still above net cash, so **even a severe de-rating does not impair the balance sheet or force distress financing.**

## 5. Overall Financial Risk Rating: **MODERATE**

| Sub-dimension | Rating |
|---|---|
| Credit / solvency risk | **Low** (net cash $2.0B, no maturities) |
| Liquidity risk | **Low** (current 5.48x, cash ratio 4.36x, ~6yr runway) |
| Cash-flow sustainability | **Moderate** (burn widening, but growth-driven) |
| Dilution / capital-structure risk | **High** (+35% share count since 2022) |
| Market / equity risk | **High** (110% vol, beta 2.6, -41% routine DD) |
| **Composite** | **MODERATE** |

The "Moderate" is driven by the equity, not the enterprise. This is a company with an investment-grade-quality balance sheet and a venture-stage P&L — the classic profile where credit analysis says "safe" and price analysis says "fragile."

**One genuinely bullish data point worth flagging:** stripped of SBC, EBITDA has been essentially breakeven for three straight quarters — Q3'25 -$31.3M, Q4'25 -$3.7M, Q1'26 -$2.6M, **Q2'26 -$2.8M**. The $371M FCF burn is ~80% explained by Neutron capex ($148.7M) and a working-capital build (-$168.4M) tied to 28% revenue growth — not by operating losses. Gross margin at 37.3% and rising ~400-500bp/yr supports a credible path to positive FCF.

## 6. Key Red Flags

1. **Dilution is structural, not incidental.** Shares 466.2M (2022) → 629.7M (Q2'26), **+35%**; equity +$1.77B in H1 2026 alone. Piotroski F7 = 0. The balance-sheet strength was purchased with shareholder equity, and the mechanism will be used again if markets permit.
2. **FCF burn is accelerating, not narrowing:** -$153.6M (FY23) → -$116.0M (FY24) → **-$321.8M (FY25) → -$371.1M (TTM)**. FY25 was a 177% YoY worsening. Operating cash flow went -$48.9M → -$165.5M → -$222.5M TTM.
3. **Working-capital quality.** Inventory **+68% in six months** ($158.4M → $266.9M); receivables **+92%** ($123.0M → $235.9M) against ~28% revenue growth. Receivables are growing 3x faster than sales — watch collection and reserve adequacy. WC drag TTM: -$168.4M, with Q2'26 the worst quarter (-$84.0M).
4. **Valuation leaves no margin for error** — ~38.7x EV/TTM sales, negative EBITDA, 1.2% negative FCF yield. The single largest risk to an equity holder is multiple compression, which no amount of balance-sheet strength mitigates.
5. **Goodwill & intangibles up 44% in six months** ($430.5M → $619.5M) from acquisitions — now 18% of equity. Integration/impairment risk on newly acquired businesses is unproven.
6. **Negative interest coverage (-8.6x)** and a "Distress"-zone Altman Z (1.61) will screen poorly in quantitative credit models — be prepared for mechanical forced-selling/algo exclusion even though the underlying risk is low.
7. **Neutron concentration risk** — the capex program is binary and largely explains the burn; a schedule slip extends the burn and likely forces another raise.

## 7. Data Gaps (explicit)

- **No benchmark price data.** The `historical-price-eod` endpoint is unavailable on this subscription for all tick
