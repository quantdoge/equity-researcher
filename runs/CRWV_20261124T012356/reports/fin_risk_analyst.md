# Fin Risk Analyst

- Symbol: CRWV
- Elapsed: 38.0s

---
I have what I need. Writing the assessment now.

---

# CRWV — CoreWeave, Inc. | Financial Risk Assessment

**Data basis:** LTM through Q3 2026 (period end 2026-09-30, filed 2026-11-12); price/market cap as of latest quote. **Note:** the pre-computed leverage/liquidity/Z-score/F-score tools returned **FY2025 (12/31/2025)** periods and are materially stale — total debt has since risen from $29.8B to $66.2B. I re-derived all key metrics on Q3 2026 data below and label the sources.

---

## 1. Credit Risk Assessment — **Sub-Investment Grade (High-Yield, deteriorating)**

**Ratings:** S&P **'B+' issuer credit rating**, outlook revised to **Positive** from stable; **recovery rating '5'** (indicative 10–30% recovery in a default). Moody's **Ba3** corporate family, **stable**. Moody's **A3** applies only to the **CoreWeave Compute Acquisition SPV** ($8.5B GPU-backed facility closed Mar-2026) — **not** to the parent. That bifurcation is the whole credit story: the lenders are investment-grade-protected against specific GPU collateral, while the corporate entity sits beneath them.

| Metric | FY2023 | FY2024 | FY2025 | **LTM Q3'26** |
|---|---|---|---|---|
| Revenue | $229M | $1,915M | $5,131M | **$9,886M** |
| EBITDA | -$427M | $480M | $2,468M | **$5,346M** |
| EBIT | -$530M | -$383M | $14M | **-$76M** |
| Net income | -$594M | -$863M | -$1,167M | **-$2,527M** |
| Interest expense | $28M | $361M | $1,229M | **$2,410M** |

The critical observation: **EBITDA ($5,346M) is almost entirely D&A ($5,250M).** EBIT is negative. Strip out the depreciation add-back on a GPU fleet whose economic life is the central debate in this name, and the business earns **essentially zero operating profit against $2.4B of cash interest**. Interest expense doubled YoY and is running at **$3.38B annualized** — **~28% of revenue**.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Source / Assessment |
|---|---|---|
| **Total debt** | **$66.2B** | Q3'26. Up from $29.8B at FY25 — **+122% in nine months** |
| Short-term debt | $10.6B | vs. cash $5.6B — refinancing gap this year |
| Net debt | **$60.7B** | 2.26× the entire market cap |
| **Debt / equity (book)** | **16.4×** | Tool (FY25): 8.94× — already extreme, now worse |
| Debt / assets | 72.4% | Equity/assets just **4.4%** |
| **Net debt / EBITDA** | **11.3×** | $60.7B / $5.35B. Flattered — see D&A note |
| **Interest coverage (EBIT)** | **~0.0× (negative)** | Tool (FY25): **-0.04×** |
| Interest coverage (EBITDA) | **2.2× LTM / 2.5× run-rate** | Below the ~3× comfort floor for HY infra |
| **Current ratio** | **0.44×** | Tool (FY25): 0.46× |
| Quick ratio | 0.44× | No inventory — clean read |
| Cash ratio | 0.24× | Cash $5.6B / current liabilities $24.4B |
| **Working capital** | **-$13.6B** | FY25: -$8.95B — widening |
| **Altman Z-Score** | **-0.12 (Distress)** | Tool (FY25): **-0.144**; I re-derived on Q3'26: **-0.12** book, **+0.04** using market cap for X4. Deeply below the 1.81 distress threshold either way |
| **Piotroski F-Score** | **5 / 9 (Moderate)** | FY25. Fails on **ROA (F1), dilution (F7), gross-margin trend (F8), asset turnover (F9)** |
| **FCF yield** | **-76% LTM / -34.5% FY25** | LTM FCF -$20.4B on $26.9B market cap |
| Capex / operating cash flow | **3.8×** | LTM capex $27.6B vs. OCF $7.2B |
| **Cash runway** | **~0.7 quarters (~80 days)** | $5.6B cash / $7.5B quarterly FCF burn |

**Caveats on the model scores:** Altman Z was built for asset-light manufacturers; it mechanically punishes a company mid-buildout (negative X1 from deferred-payable working capital, low X5 asset turnover of 0.11). But its core findings — 4% equity cushion, negative working capital, EBIT ≈ 0 — are corroborated by direct measurement, not artifacts. Similarly, Piotroski's 5/9 overstates health: F5 "lower leverage" scores positive on a book-equity technicality while absolute debt doubled.

---

## 3. Market Risk Profile — **Extreme**

| Metric | Value |
|---|---|
| Annualized volatility (365d) | **102.6%** |
| Beta vs. SPY | **3.62** (tool) — **7.67** per company profile |
| Max drawdown (365d) | **-71.8%** |
| Sharpe ratio | **-0.44** |
| Price / market cap | $48.33 / $26.9B |

This is one of the highest-beta, highest-volatility large-cap profiles in the market: a **~3.6× market beta** means a 20% S&P drawdown plausibly implies a **55–70%+ decline** in CRWV. The -71.8% max drawdown confirms the tail is not theoretical — it has already happened within the past year. **Negative Sharpe (-0.44)** means holders have been paid *less than zero* risk-adjusted return for taking this volatility. Note the **beta discrepancy (3.62 vs 7.67)** — different estimation windows; flagging rather than resolving. Either figure supports "extreme."

Crucially, market risk and credit risk are **positively correlated here**: the stock falls precisely when refinancing conditions tighten, and their equity story is the collateral that supports the debt. That reflexivity is the defining feature of this risk profile.

---

## 4. Downside Scenario: Revenue -20%

Applied to LTM revenue of $9,886M (-$1,977M), assuming cost of revenue is ~40% variable (power/colocation/labor contractually committed) and SG&A fixed:

| Line | Base (LTM) | Scenario | Change |
|---|---|---|---|
| Revenue | $9,886M | $7,909M | -20% |
| Gross profit (66.8% margin) | $6,599M | $5,413M | -18% |
| SG&A | $919M | $919M | flat |
| **EBITDA** | **$5,346M** | **~$4,494M** | **-16%** |
| **Net debt / EBITDA** | **11.3×** | **~13.5×** | Deteriorates |
| **EBITDA / interest (run-rate $3.38B)** | **2.5×** | **~1.33×** | Approaches 1.0× |
| EBIT | -$76M | **~-$790M** | Deeply negative |
| FCF | -$20.4B | **-$22B+** | Capex is committed, not discretionary |

**The break point is not the revenue line — it is financing.** Because capex ($27.6B LTM) is largely committed against signed take-or-pay backlog, a revenue shortfall does **not** reduce the cash outflow; it only reduces the cash inflow. At 1.33× EBITDA/interest the company retains **zero** cushion, and a mere **+100bp** on $66B of largely floating-rate debt adds ~$660M of interest — pushing coverage toward **1.1×** and turning the equity into a pure option on credit availability.

Two escalation paths worth naming:
- **Customer concentration shock.** Top customer was **67% of FY2025 revenue** (Microsoft), reduced to **~36%** by later 2026 — genuine diversification progress, but the top two customers were still 77% of 2024 revenue. A single counterparty renegotiation or failure removes a third of the revenue base while the GPU leases remain.
- **Collateral obsolescence.** Because the SPV lenders (A3) hold first claim on specific GPUs, a scenario where GPU residual values fall below loan balances subordinates the **$87B of corporate liabilities** to the SPV, consistent with S&P's **'5' recovery rating (10–30%)**.

**The equity cushion to absorb this is $4.0B — 4.4% of assets.** The first 6% of asset impairment wipes out book equity entirely.

---

## 5. Overall Financial Risk Rating: **CRITICAL**

Justification: (1) EBITDA ≈ D&A, so EBIT and interest coverage are effectively zero/negative; (2) **~80 days of cash runway** at current burn — solvency depends on continuous, uninterrupted capital-markets access, not on operating cash flow; (3) leverage at 11.3× net debt/EBITDA *rising* to 13.5× on a mild downside; (4) a **$10.6B current-debt wall against $5.6B of cash**; (5) sub-investment-grade corporate ratings with a 10–30% recovery assumption; (6) 103% volatility with a 3.6× beta and a realized -72% drawdown.

**What would change the rating (genuine offsets I am weighing, not dismissing):**
- **$66.8B revenue backlog** as of 12/31/2025 — ~6.8× LTM revenue, largely take-or-pay. This is real contracted demand and the single strongest mitigant.
- **$8.5B GPU-backed facility closed Mar-2026 at A3** — the securitization channel is open and deepening; GPU debt has repriced from private credit toward SOFR+225.
- **S&P outlook revised to Positive**; OCF has turned solidly positive ($7.2B LTM, up from $3.1B FY25) and revenue is compounding at triple digits.
- Customer concentration is measurably improving (67% → 36%).

These make a *liquidity* failure in the next 12 months unlikely. They do **not** make the balance sheet resilient to a genuine AI-capex downturn. The rating is Critical on *resilience*, not on near-term default probability.

---

## 6. Key Red Flags

1. **Debt doubled to $66.2B in nine months** while book equity is $4.0B — 16.4× debt/equity. Leverage is compounding faster than EBITDA.
2. **~80-day cash runway; FCF -$20.4B LTM.** The company is a serial capital raiser, not yet a self-funding business. Any capital-markets closure is existential within one to two quarters.
3. **$10.6B short-term debt vs. $5.6B cash** — a live refinancing wall inside 12 months.
4. **EBITDA is a depreciation artifact.** LTM D&A of $5,250M against EBITDA of $5,346M. If GPU useful lives prove too long relative to the ~2–3 year hardware cadence, true EBITDA is materially lower and *every* leverage ratio above understates risk.
5. **Negative working capital of -$13.6B** and current ratio 0.44× — structurally dependent on supplier/landlord forbearance.
6. **Dilution:** weighted shares 435M (FY25) → 559M (Q3'26), **+28% in nine months**; Piotroski explicitly flags dilution. Equity is being sold into weakness to fund debt service.
7. **Recovery rating '5'** (10–30%) — the market's own pricing of what equity-in-a-default is worth.
8. **Reflexivity:** 3.6× beta equity collateralizing floating-rate debt. A market drawdown raises the cost of the capital that keeps the company solvent.

---

## Data Gaps (explicitly flagged)

- **Debt maturity ladder by year — unavailable.** SEC EDGAR (403 Forbidden) and S&P Global (403 Forbidden) both blocked automated retrieval. I have only: $2.5B revolver due 2029 ($1.45B undrawn at 12/31/25), 2031 9.00% Senior Notes (Feb-2031), and $10.6B current debt. **The 2027–2030 amortization profile is unknown and is the single most important missing input.**
- **$19.3B reconciliation gap:** total debt $66.2B vs. short-term + long-term debt $46.9B. The difference is almost certainly operating/finance lease liabilities not broken out in the available feed. Treat total debt as the true figure.
- **Q3'26 income statement reports D&A = $0** (data error, EBITDA printed equal to EBIT at $220M). I substituted the cash-flow statement's $1,889M to derive LTM EBITDA of $5,346M. This is my estimate, not a reported figure.
- **Beta conflict:** 3.62 (volatility tool, 365d) vs. 7.67 (company profile). Window-dependent; unresolved.
- **Covenant details** (leverage maintenance tests, minimum liquidity) are not available in any accessible source. Given 13.5× stressed leverage, this is a material blind spot — covenant breach risk cannot be quantified from the data available to me.
- Pre-computed ratio tools (leverage, liquidity, Z-score, F-score, FCF yield) are all on **FY2025** and are stale by four quarters against the Q3 2026 balance sheet; where they conflict with my re-derivation, use mine.
