# Fin Risk Analyst

- Symbol: WCN
- Elapsed: 83.8s

---
## Waste Connections, Inc. (WCN) — Financial Risk Assessment
*Data as of FY2025 audited (period end 2025-12-31) and TTM through Q3 2026 (quarter ended 2026-09-30). Price $181.50, market cap ~$45.4B. Yield curve as of 2026-11-18.*

### 1. Credit Risk Assessment — **INVESTMENT GRADE** (A-/A3/BBB+)

WCN carries a mid-single-A profile confirmed by all three agencies: **Fitch 'A-'** (rated 2026-05-03 on proposed senior unsecured notes), **Moody's A3** (recently upgraded), **S&P 'BBB+'**. This is a full notch or two better than the underlying metrics alone would justify, reflecting the contractual, recession-resistant nature of the revenue base (~85–90% subscription/collection-based, non-deferrable service).

Leverage is elevated but deliberate and stable: **net debt/EBITDA 3.15x** FY2025, **3.02x TTM** (net debt $9,662M / TTM EBITDA $3,201M). That sits inside the 3.0–3.5x management band and is *lower* than Waste Management (4.48x) and only modestly above Republic (2.69x). Interest coverage of **5.1x EBIT** (8.8x EBITDA/interest) is comfortable and in line with both peers (WM 5.05x, RSG 5.75x).

**Critical nuance on the Altman Z-Score:** the tool reports **1.39 — "Distress" zone**, but this is a measurement artifact, not a solvency signal. The model substitutes *book* equity for market equity in x4 (0.633 vs. liabilities), which structurally penalizes any acquisitive roll-up with large goodwill. Recomputing x4 at the actual **market capitalization of $45.4B** (45.4/13.0 = 3.49) gives:

> **Z = 1.2(−0.038) + 1.4(0.245) + 3.3(0.082) + 0.6(3.49) + 1.0(0.446) = 3.11 → SAFE ZONE**

The book-basis x1 of −0.038 (negative working capital) also drives the low reading — again structural, driven by accrued landfill closure/post-closure liabilities and deferred revenue, not by liquidity strain.

### 2. Key Financial Risk Metrics

| Metric | WCN (FY25) | WCN (TTM Q3'26) | WM | RSG | Assessment |
|---|---|---|---|---|---|
| Net debt / EBITDA | 3.15x | **3.02x** | 4.48x | 2.69x | Moderate, in-band |
| Total debt / equity | 1.14x | 1.24x | 2.29x | 1.15x | Moderate |
| Debt / assets | 0.44x | 0.45x | 0.50x | 0.40x | Moderate |
| EBIT / interest | 5.11x | 5.21x | 5.05x | 5.75x | Adequate |
| EBITDA / interest | 8.9x | 8.8x | — | — | Adequate |
| Current ratio | 0.62x | **0.67x** | — | — | Weak (structural) |
| Quick ratio | 0.58x | — | — | — | Weak |
| Cash / current liabilities | 0.02x | 0.04x | — | — | Very thin |
| Working capital | −$811M | −$718M | — | — | Negative |
| Assets / liabilities | 1.63x | 1.58x | — | — | OK |
| **Altman Z** | **1.39 book / 3.11 market-adj.** | — | — | — | Book-basis overstated risk |
| **Piotroski F-Score** | **7 / 9** | — | — | — | Moderate-strong |
| FCF yield | 2.64% | ~2.75% | 2.87% | 3.05% | Slightly low |
| FCF margin | 13.0% | 12.6% | — | — | Stable |

**F-Score detail (7/9):** passes profitability (4/4), accruals quality, equity issuance and gross-margin improvement. Fails **F5 (leverage increased — D/E 0.97→1.14)** and **F9 (asset turnover declined 0.450→0.446)**. Both failures are the direct arithmetic consequence of debt-funded M&A and buybacks, not of operating deterioration.

**FCF sustainability:** TTM operating cash flow $2,528M, capex $1,278M (12.9% of revenue), **FCF $1,250M**. FCF is up every year since 2021 ($954M → $1,250M), a 6.9% CAGR, with a stable 12–15% FCF margin. Cash conversion is high quality — D&A ($1,232M) exceeds net income ($1,077M), which is exactly what you want to see in a capital-intensive, goodwill-heavy business.

### 3. Market Risk Profile

| Metric | WCN | Read-through |
|---|---|---|
| Annualised volatility (3y, 756d) | **22.65%** | Below broad market; defensive |
| Beta vs SPY (3y regression) | **0.144** | Implausibly low — see flag |
| Beta (vendor profile) | 0.481 | More credible; still low-beta |
| Max drawdown (3y) | **−24.75%** | Shallow vs. market drawdowns |
| Sharpe ratio (0% rf) | **0.16** | Poor risk-adjusted return |

The low 22.65% volatility and 24.75% peak-to-trough decline confirm WCN behaves as a defensive compounder. The **Sharpe of 0.16 is the weak spot**: over the measurement window shareholders earned roughly 3–4% annualised against 22.65% vol. Combined with a 2.64% FCF yield and a market cap that implies a rich multiple, the stock is priced for consistency and offers little cushion — the risk here is **valuation/multiple compression, not balance-sheet failure**. Note the two beta estimates diverge sharply (0.144 vs 0.481); the regression beta is likely distorted by the rolling window, so I would underwrite to ~0.5, meaning a 20% market drawdown costs roughly 10% in WCN.

### 4. Downside Scenario Analysis — Revenue −20%

Assumptions: −30% of the revenue base proves cyclical (industrial/construction roll-off volumes, E&P waste, special waste, and commodity-linked recycling); ~45% decremental EBITDA margin (variable disposal, fuel, hourly labour, third-party hauling offset by fixed landfill and fleet costs). Interest held at the TTM run-rate of $365M; capex flexed down toward maintenance (~$900M); buybacks suspended.

| Line item | Base (TTM) | −20% revenue | −30% revenue (tail) |
|---|---|---|---|
| Revenue | $9,944M | $7,955M | $6,961M |
| EBITDA | $3,201M | **$2,306M** (23.2% mgn) | $1,859M (26.7% mgn) |
| D&A (largely fixed) | $1,299M | $1,300M | $1,300M |
| EBIT | $1,902M | **$1,006M** | $559M |
| Interest | $365M | $365M | $365M |
| **EBIT / interest** | 5.21x | **2.76x** | **1.53x** |
| **Net debt / EBITDA** | 3.02x | **4.19x** | **5.20x** |
| FCF (capex cut to $900M) | $1,250M | **~$890M** | ~$600M |
| Dividend cover ($355M) | 3.5x | **2.5x** | 1.7x |
| Z-score (market-adj.) | 3.11 | ~2.3 (grey) | ~1.8 (grey/distress edge) |

**Findings:** A 20% revenue shock is *survivable without a liquidity event* — FCF stays positive at ~$890M and dividends remain covered 2.5x. But leverage breaks 4.0x, which sits above the 3.0–3.5x management target and would almost certainly cost one notch of rating (A- → BBB+/Baa1), raising the marginal cost of the $9.8B debt stack. **The true stress point is −25% to −30% revenue**, where EBIT/interest falls to ~1.5x and the company would need to cut the dividend and halt buybacks.

**Headroom math:** EBITDA can fall to $2,416M before breaching 4.0x leverage — an **EBITDA cushion of $785M, equivalent to roughly a 17.6% revenue decline**. That is a meaningful but not unlimited buffer.

**Refinancing risk is genuinely low.** Per Fitch, the **next maturity is only $500M of notes due December 2028**, with a well-spread ladder running through 2052, and WCN priced $600M of 4.800% notes due 2036 in March 2026. There is no 2026–2027 cliff. The offsetting factor is the rate environment: with the **10Y at 5.13% and 30Y at 5.47%** (2s10s +39bp, no inversion), refinancing legacy low-coupon paper will push interest expense higher — TTM interest is already up 9% YoY and 82% since FY2022. Each $1B refinanced at +150bp costs ~$15M pre-tax, or ~1% of EBIT. Manageable, but it is a slow structural drag on coverage.

### 5. Overall Financial Risk Rating: **MODERATE**

Credit risk: **Low** (investment grade, no near-term maturities, 5.2x coverage, 3.0x leverage). Liquidity risk: **Moderate** (thin absolute cash, negative working capital, but $2.5B annual operating cash flow and an undrawn revolver make this a reporting artifact rather than a funding risk). Market/valuation risk: **Moderate-High** (Sharpe 0.16, 2.6% FCF yield, priced for perfection). Downside risk: **Moderate** (17.6% revenue cushion before leverage target breach).

### 6. Key Red Flags

1. **Negative tangible book equity — −$2.50B.** Goodwill and intangibles are $10.38B, or **48.3% of total assets**. Equity of $7.88B is entirely goodwill-dependent. Any acquisition write-down or landfill impairment flows straight into book equity and the rating agencies' adjusted metrics. This is the single largest structural risk.
2. **Capital returns exceeded free cash flow.** TTM dividends ($355M) + buybacks ($1,008M) = **$1,363M vs. FCF of $1,250M — 109% payout**. Total debt has risen from $8,393M (FY24) to $9,758M (Q3'26), a **+$1,365M increase in 21 months** funding buybacks plus M&A. Leverage is being managed, but the buyback is debt-funded at the margin. This is the clearest path to deterioration if FCF stalls.
3. **Liquidity buffer is minimal.** Cash of $95.7M equals **4.4% of current liabilities**; the current ratio of 0.67x and negative working capital mean WCN runs on its revolver and commercial paper. Fine in normal markets — a genuine vulnerability if credit markets seize while ~$500M of notes approach maturity.
4. **FY2024 margin break.** Operating income *fell* 14% ($1,236M → $1,068M) on 11% revenue growth, dropping operating margin from 15.4% to 12.0% before recovering to 18.1% in FY2025. That volatility in a supposedly predictable business warrants scrutiny of the FY2024 charge composition — the tool data does not decompose it.
5. **Interest expense compounding.** Up 82% since FY2022 ($201M → $365M) versus EBIT +50%. Coverage has been flat at ~5.2x only because margins expanded; that offset is now largely exhausted.
6. **Piotroski F5 and F9 both fail** — leverage up and asset turnover down. Consistent with a company buying growth rather than generating it organically.

**Data gaps to flag:** (a) no year-by-year debt maturity ladder or covenant detail was retrievable — maturity commentary relies on Fitch's public note (next maturity $500M, Dec 2028); (b) no CDS spread data; (c) the sector-peer tool returned generic Industrials mega-caps (GE, RTX, CAT) rather than waste comps, so WM and RSG were pulled individually for benchmarking; (d) no intraday price series was pulled, so max drawdown (−24.75%) and Sharpe (0.16) are taken from the volatility tool's 756-day window; (e) the two beta estimates (0.144 regression vs. 0.481 vendor) conflict and I recommend underwriting to ~0.5.
