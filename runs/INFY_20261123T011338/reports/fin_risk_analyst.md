# Fin Risk Analyst

- Symbol: INFY
- Elapsed: 55.1s

---
# INFOSYS LIMITED (INFY) — FINANCIAL RISK ASSESSMENT

**Company:** Infosys Ltd. | Technology — IT Services | India (ADR, USD-reported) | Market cap ≈ $48.8B | FY ends 31-Mar
**Data basis:** FY2026 (ended 31-Mar-2026) latest annual; price data through 31-Mar-2026

---

## 1. Credit Risk Assessment

**Rating: INVESTMENT GRADE (fortress balance sheet) — no meaningful default risk**

Infosys is a net-cash company with essentially no financial leverage. The capital structure is not a risk factor at any plausible operating scenario.

| Metric | Value | Read |
|---|---|---|
| Total debt | $967M | ~0.6% of assets; predominantly lease liabilities |
| Cash & ST investments | $3,752M | **Net cash ≈ $2.79B** |
| Net debt / EBITDA | **−0.55x** | Negative → net cash position |
| Debt / equity | 0.10x | Very low |
| Debt / assets | 0.06x | Very low |
| EBIT / interest | **86.9x** (4,085 / 47) | EBIT-based coverage ≈ 97x. Effectively no debt service burden |
| Altman Z-Score | **4.57** (Safe; >2.99) | Distress threshold is 1.81 — 2.5x headroom. Using market cap instead of book equity for x4, Z rises to ~13.5 |
| Piotroski F-Score | **6 / 9** (Moderate) | Strong profitability (4/4); weak points are all capital-allocation, not solvency |

**Z-score components:** x1 0.328, x2 0.818, x3 0.277, x4 1.490, x5 1.226 — high retained earnings (x2) and asset turnover (x5) do the work; leverage contributes almost nothing to the score either way.

**F-Score diagnosis:** F1–F4 all pass (positive ROA, positive operating cash flow, ROA improvement, clean accruals). The three misses are **F5 (leverage not lower), F6 (equity declined), F8 (gross margin not improved)** — all downstream of returning more cash than was earned (dividends $2,133M + buyback $2,006M = $4,139M vs FCF $3,733M), which shrank book equity from $11.26B to $9.84B. This is a shareholder-returns signal, **not** a credit deterioration signal.

**No credit rating or CDS spread data was available from the tools — flagged as a data gap.** Based on leverage alone, a high investment-grade profile is implied.

---

## 2. Key Financial Risk Metrics

| Metric | FY2026 | FY2025 | FY2024 | Trend |
|---|---|---|---|---|
| Revenue ($M) | 20,158 | 19,277 | 18,562 | +4.6% YoY (decelerating) |
| Gross margin | 30.2% | 30.5% | 30.1% | Flat, slight dip |
| Operating margin | 20.3% | 21.1% | 20.7% | −80bp YoY |
| EBITDA ($M) | 5,105 | 5,066 | 4,967 | Stable |
| Net income ($M) | 3,313 | 3,162 | 3,167 | +4.8% |
| Operating cash flow ($M) | 4,039 | 4,351 | 3,148 | −7% YoY |
| Capex ($M) | 306 | 263 | 266 | 1.5% of revenue (asset-light) |
| **FCF ($M)** | **3,733** | 4,088 | 2,882 | −8.7% YoY |
| **FCF margin** | **18.5%** | 21.2% | 15.5% | Volatile but healthy |
| **FCF yield** | **7.77%** | — | — | Attractive; well above 10Y UST 5.13% |
| Current ratio | 1.98x | 2.27x | 2.31x | Declining (cash drawdown) |
| Quick ratio | 1.98x | — | — | No inventory — clean |
| Cash ratio | 0.68x | — | — | Adequate |
| Working capital ($M) | 5,396 | 6,347 | 6,071 | −15% YoY |
| Cash / liabilities | 0.57x | — | — | — |
| Equity / assets | 0.60x | 0.65x | 0.64x | Falling via buybacks |
| Dividends + buyback / FCF | **111%** | 59% | 62% | **Over-distributing** |

**Liquidity verdict:** No refinancing cliff — short-term debt is reported as $0 and the entire $967M debt load is covered ~3.9x by cash on hand. Cash runway on a zero-revenue basis is not meaningful; on a stressed cash-burn basis (see §4) the company still generates positive FCF. The 12% decline in cash ($4,509M → $3,752M) and falling current ratio reflect deliberate capital returns, not liquidity strain.

---

## 3. Market Risk Profile

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility | **34.2%** | High for a large-cap IT services name; reflects ADR + INR/EM overlay |
| Beta vs SPY | **0.513** | Low market sensitivity (profile reports 0.131 — see data gaps) |
| Max drawdown (3Y) | **52.9%** | Contaminated by a bad print — see below |
| Sharpe (rf = 0%) | **−0.56** | Negative: the stock lost money over the window |

**Interpretation:** This is the weakest part of the INFY story, and it is a *price* problem, not a *solvency* problem. The ADR has de-rated from ~$21 (Jul-2024 peak) to $12.93 (31-Mar-2026) — roughly **−40%** peak-to-trough, and down from ~$16 in Sep-2022. With fundamentals essentially flat (revenue +4.6%, EBITDA flat), the entire drawdown is multiple compression: the market is repricing long-term growth/terminal-value risk for offshore IT services, plausibly on AI-driven disruption of the labor-arbitrage model.

**Data integrity caveat:** the 52.87% max-drawdown figure is almost certainly inflated by an anomalous print on 2025-12-19 (intraday high $28.71 vs close $19.35 on 118.7M shares). On closing prices the peak-to-trough is ≈ −41%. Volatility of 34.2% also looks inflated relative to a 0.51 beta — I would treat the vol estimate as an upper bound. The **negative Sharpe is directionally real** regardless of the bad tick.

**Risk read:** low *systematic* risk (beta ~0.5, defensive contracted revenue, net cash), but high *idiosyncratic/de-rating* risk. INFY will underperform in a market drawdown less than the index, but has been destroying risk-adjusted return through sector-specific de-rating.

---

## 4. Downside Scenario Analysis — Revenue −20%

Model: 85% of COGS variable (offshore headcount is the swing factor), SG&A 10% variable, working capital releases modestly, capex held at $306M.

| Line item | Base FY2026 | **−20% Revenue** | Change |
|---|---|---|---|
| Revenue | 20,158 | **16,126** | −4,032 |
| Gross profit | 6,079 | 4,440 | margin 30.2% → **27.5%** |
| Operating income | 4,085 | **2,646** | margin 20.3% → **16.4%** (−390bp) |
| EBITDA | 5,105 | 3,198 | −37% |
| EBIT / interest | 86.9x | **56x** | Still no coverage issue |
| Net income | 3,313 | ~1,923 | −42% |
| Operating cash flow | 4,039 | ~2,675 | Working capital release cushions |
| **FCF** | 3,733 | **~2,369** | FCF margin 18.5% → 14.7% |
| Net debt / EBITDA | −0.55x | **≈ −0.9x** (net cash grows) | Still net cash |
| Dividends + buyback ($4,139M) vs FCF | 111% | **175%** | **$1.77B shortfall** |

**Conclusion:** A 20% revenue shock is absorbed without any debt issuance. The company ends the year still in net cash, with coverage above 50x. The *only* genuine consequence is that the current capital-return policy ($4.1B/yr) becomes unfundable from FCF and would have to be cut or drawn from the cash pile — which would exhaust ~$1.8B of a $3.75B buffer per year of stress.

**Severe stress (−30% revenue, operating margin to ~10%):** EBIT ≈ $1.7B, coverage ~37x, FCF ≈ $1.4B, net cash still positive. **No distress zone reached even here.** To breach a covenant-style threshold (net debt/EBITDA > 2.0x) revenue would have to fall >50% *and* margins go negative simultaneously — not a realistic scenario for a contracted, diversified services book.

---

## 5. Overall Financial Risk Rating: **LOW**

Balance-sheet risk is close to as low as it gets in public equities: net cash, 87x interest coverage, Z-score 4.57, no near-term maturities, 1.98x current ratio, and a business that converts ~18.5% of revenue into FCF with 1.5% capex intensity. There are **no covenant, refinancing, or liquidity risks** at any plausible operating outcome.

The risk that matters for INFY is **equity/valuation risk, not financial risk**: −40% peak-to-trough de-rating on flat fundamentals, a negative 3-year Sharpe, and a shareholder-return policy running at 111% of FCF.

---

## 6. Key Red Flags

1. **Capital returns exceed free cash flow (111% of FCF).** $4.14B returned vs $3.73B generated, funded by drawing cash from $4.51B → $3.75B. Sustainable in normal years, but leaves no cushion for a downturn without a dividend/buyback cut. Directly explains the 3 F-Score misses and the 12% equity decline.
2. **Margin erosion.** Operating margin −80bp YoY (21.1% → 20.3%) and gross margin down 30bp, on only 4.6% revenue growth — pricing pressure is visible even before any demand shock.
3. **FCF and OCF deteriorating.** OCF −7% and FCF −8.7% YoY despite higher revenue and net income; working capital drag of −$259M. Watch receivables ($6.19B = 31% of revenue, DSO ~112 days).
4. **Growth deceleration.** Revenue growth 6.3% (FY24) → 3.9% (FY25) → 4.6% (FY26) in USD — the core driver of the de-rating. Structural (AI/automation) risk to the labor-arbitrage model is the single biggest threat to the *equity*, not the *creditor*.
5. **Negative risk-adjusted returns.** 3Y Sharpe −0.56, −41% peak-to-trough on closes. Beta 0.51 means this is idiosyncratic sector risk, not market risk — it will not be diversified away by market exposure.

**Data gaps flagged:**
- **No credit rating or CDS spread** retrievable from tools — cannot confirm agency ratings.
- **Debt maturity schedule unavailable.** Balance sheet reports `short_term_debt: 0` and `long_term_debt: 0` yet `total_debt: $967M`, and `net_debt: −$1,374M` conflicts with cash ($3,752M) − debt ($967M) = **−$2,785M** (the figure the leverage tool uses). I have used −$2,785M; the internal inconsistency means the maturity profile cannot be verified.
- **Beta conflict:** profile beta 0.131 vs calculated 0.513 vs SPY (756d). Likely different lookbacks; both indicate low market sensitivity.
- **Price series contamination:** 2025-12-19 print (high $28.71, close $19.35, 118M shares) distorts max drawdown and volatility. Profile price ($12.03) also differs from the last close in history ($12.93) — staleness.
- **Peer comparables unusable:** the sector-peer tool returned AAPL, MSFT, NVDA, TSM, AVGO, ANT — mega-cap US hardware/software, not IT-services comparables (no CTSH/ACN/WIT/TCS). No peer-relative leverage benchmarking is possible.
- **Yield curve as-of 2026-11-23** (2Y 4.74%, 10Y 5.13%, 30Y 5.47%, 2s10s +39bp, no inversion) is dated *after* the price series end. Elevated long rates raise the discount-rate headwind on long-duration growth equities — relevant to the de-rating — but INFY faces no refinancing exposure to it.
