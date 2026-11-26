# Fin Risk Analyst

- Symbol: NTNX
- Elapsed: 69.2s

---
## NTNX — Financial Risk Assessment
**Nutanix, Inc.** | Technology / Software – Infrastructure | San Jose, CA | FY ends July 31
**Price $46.30 (11/25/26) · Market cap $12.63B · EV ≈ $11.79B**

---

### 1. Credit Risk Assessment → **INVESTMENT GRADE** (on fundamentals; agency-unrated)

NTNX is a **net-cash** business with trivial coupon burden and no near-term maturities. The capital structure is entirely convertible-notes-based, and every note is out to 2027+.

| Debt tranche (reconciled) | Approx. principal | Maturity |
|---|---|---|
| 0.25% convertible senior notes | ~$500M (partially repurchased 2024–25) | 2027 |
| 0.50% convertible senior notes | ~$862M | 2029 |
| Other debt / finance leases | ~$157M | Various |
| **Total debt** | **$1,518.7M** | — |
| Revolver ($500M, inaugural Dec-2024) | Undrawn (inferred) | — |
| Cash + ST investments | **$2,361.5M** | — |
| **Net cash** | **+$842.7M** | — |

- **Interest coverage 31.0x** (EBIT $329.9M / interest $8.98M). Interest expense collapsed from $169.4M (FY24) to $9.0M (FY26) after the convert exchange/refi — a genuine de-risking.
- **Economic** coverage is weaker than reported: the 0.25–0.50% coupons are subsidized by equity optionality. If $1.36B of converts were refinanced at ~5.5–6.0% (10Y UST is 5.13%), cash interest would be ~$82M → coverage ~4.0x. Still comfortably investment grade.
- **No refinancing cliff.** Earliest maturity is 2027 (~$500M), fully pre-fundable from cash.
- Cash is **46.5% of total assets**; cash/liabilities 0.54.

**Caveat:** book equity is thin — $702.6M vs $5.07B assets (equity/assets 13.8%), and that positive figure exists *only* because of the FY26 tax item (see Red Flag #1). Debt/equity 2.16x is a book-equity artifact, not a leverage signal.

---

### 2. Key Financial Risk Metrics

| Metric | FY2026 | FY2025 | FY2024 | Read |
|---|---|---|---|---|
| Revenue ($M) | 2,853.5 | 2,537.9 | 2,148.8 | +12.4% (decel from +18.1%) |
| Gross margin | 86.8% | 86.8% | 84.9% | Stable, high |
| Operating margin | 9.8% | 6.8% | 0.3% | Improving |
| EBITDA ($M) | 400.6 | 292.7 | 141.3 | — |
| **Debt / equity** | 2.16x | n.m. (neg. equity) | n.m. | Artifact of thin book equity |
| **Net debt / EBITDA** | **−2.10x (net cash)** | net cash | ~0x | Strong |
| Gross debt / EBITDA | 3.79x | 5.07x | 4.92x | Includes leases |
| **Interest coverage** | **31.0x** | 11.2x | 0.4x | Excellent |
| **Current ratio** | **1.71x** | 1.72x | 1.06x | Adequate |
| **Quick ratio** | **1.71x** | — | — | No inventory |
| Cash ratio | 1.40x | — | — | — |
| Working capital | $1,188.1M | $1,022.6M | $77.1M | Big improvement |
| **Altman Z** | **0.13 (Distress)** | — | — | See note |
| **Piotroski F** | **6 / 9 (Moderate)** | — | — | Understated — see note |
| FCF ($M) | 840.7 | 750.2 | 597.7 | 3-yr CAGR +59% |
| FCF margin | 29.5% | 29.6% | 27.8% | Stable/strong |
| **FCF yield** | **6.2–6.7%** | — | — | EV/FCF ≈ 14x |
| SBC / revenue | 12.5% | 13.9% | 15.5% | High but improving |
| Cash runway | **n/a — self-funding** (~$210M FCF/qtr) | — | — | No burn |

**Altman Z note:** 0.13 is driven by x2 = −0.73 (retained earnings of **−$3.71B** from growth-era losses) and x4 = 0.16 (book equity). Substituting market cap for book equity: Z ≈ **1.77** — still technically grey/distress-adjacent. The model is structurally biased against a software firm with a large accumulated deficit and asset-light base; it is not corroborated by any cash-flow or coverage measure. **Flagged, but not treated as a live bankruptcy signal.**

**Piotroski note:** the 6/9 understates quality. F4 (accruals) fails *only* because GAAP net income ($1,506.8M) exceeds CFO ($916.7M) due to the non-cash $1,198.9M tax release. F9 (asset turnover) fails *only* because assets were grossed up by the deferred tax asset. F8 is a 1bp rounding artifact. Ex-artifacts, the underlying score is ~8/9.

---

### 3. Market Risk Profile → **HIGH**

| Metric | Value |
|---|---|
| Annualised volatility (756d) | **45.9%** |
| Beta vs SPY | **1.165** (computed) / 0.638 (vendor 5Y) → **data conflict; use ~1.0–1.2** |
| Max drawdown (3y, tool) | **−58.6%** |
| Sharpe (rf=0) | **0.031** — effectively zero risk-adjusted return over 3 years |
| Peak-to-current | $83.07 (5/19/25 close) → $46.30 = **−44.3%** (−48.9% intraday) |
| 12-month return | −21.2% (58.77 → 46.30) |
| Single-day gap events | **2025-11-26: −17.7%** (26.0M sh); **2026-11-25: −15.2%** (13.6M sh, ~4x ADV) |

**Diagnosis:** NTNX is an **idiosyncratic event-risk stock**, not a market-beta stock. Two −15%+ earnings-day repricings inside 12 months, with beta ~1.0–1.2, means drawdowns are company-specific (guidance/management), not macro. A Sharpe of 0.031 over three years means holders have absorbed 46% vol for zero return — poor risk-adjusted quality regardless of business quality. The most recent −15.2% drop was triggered by a **CEO succession announcement** paired with guidance that was merely *maintained* rather than raised — i.e., a governance/execution discount, not a fundamental break.

---

### 4. Downside Scenario: Revenue −20%

Baseline FY26: revenue $2,853.5M; opex $2,198.0M (**77% of revenue** — extreme operating leverage); D&A $70.6M; SBC $357.7M; capex $76.0M.

Revenue −20% → $2,282.8M.

| | Base | −20%, no cost action | −20%, 15% opex cut | −30% stress + WC reversal |
|---|---|---|---|---|
| Revenue | 2,853.5 | 2,282.8 | 2,282.8 | 1,997.5 |
| Gross profit (86.8%) | 2,476.9 | 1,981.5 | 1,981.5 | 1,733.8 |
| Opex | 2,198.0 | 2,198.0 | 1,868.3 | 1,758.4 |
| **Operating income** | 278.9 | **−216.5** | **+113.2** | **−24.6** |
| Operating margin | 9.8% | −9.5% | 5.0% | −1.2% |
| Interest coverage | 31x | 0x (EBIT neg.) | 12.6x | 0x |
| **FCF (approx.)** | 840.7 | **~$60–110M** | **~$300M** | **~$0–60M** |
| Net cash (yr-end, excl. buybacks) | +842.7 | ~+900 | ~+1,140 | ~+900 |

**Findings:**
- **GAAP operating breakeven occurs at only −11.3% revenue** ($2,532M). That is the single most important sensitivity in this analysis: a 20% decline destroys ~$217M of operating income. The business is *not* immune to a demand shock.
- **But solvency is not at risk.** Even in the −30% stress case, FCF stays non-negative, cash is $2.36B, and the earliest debt maturity (2027, ~$500M) is covered 4.7x by cash alone. **No covenant breach, no refinancing cliff, no equity raise required.**
- **Management levers are real and unexercised:** opex is 77% of revenue; a 15% opex reduction fully restores profitability at −20% revenue. SBC ($358M) is a discretionary cushion. Buybacks ($483.5M in FY26) would be suspended immediately — a further ~$480M of annual liquidity.
- **The risk in a downturn is equity valuation, not survival.** With EV/revenue 4.1x and EV/EBITDA 29x (GAAP) / 15.5x (SBC-adjusted), a −20% revenue scenario plausibly halves the equity while creditors remain whole.

---

### 5. Overall Financial Risk Rating: **MODERATE**

Decomposed, because a single label conceals the real picture:

| Dimension | Rating | Basis |
|---|---|---|
| **Credit / solvency risk** | **LOW** | Net cash $843M, 31x coverage, 29.5% FCF margin, no maturity before 2027, undrawn $500M revolver |
| **Liquidity risk** | **LOW** | $2.36B cash (46.5% of assets), current 1.71x, positive FCF every year since FY23, zero burn |
| **FCF sustainability** | **LOW–MODERATE** | 3 yrs of expansion (11%→29.5% margin), but 12.5% of revenue is SBC; SBC-adjusted FCF is $483M (16.9% margin), not $841M |
| **Operating/earnings risk** | **MODERATE–HIGH** | 77% opex ratio; breakeven at −11.3% revenue; growth decelerating 18.1%→12.4% |
| **Market / equity risk** | **HIGH** | 45.9% vol, −58.6% max DD, Sharpe 0.031, two −15%+ gaps/yr |

**This is a financially safe company wrapped in a financially dangerous stock.** Survival risk over a prolonged downturn is genuinely low; drawdown risk is high.

---

### 6. Key Red Flags

1. **Reported profitability is 80% a non-cash tax artifact.** FY26 GAAP net income $1,506.8M includes a **$1,198.9M valuation-allowance release on US deferred tax assets** (confirmed in the Q4 FY26 release). Ex-benefit net income ≈ **$308M** → EPS ~$1.14, not $5.57. Critically, the **positive $702.6M book equity exists only because of this entry** — ex-benefit equity would be **−$496M**. Debt/equity of 2.16x should be read as "equity is thin," and any screen using FY26 EPS or ROE is materially misleading. (Offset: the recognized DTA lowers future *cash* taxes — mildly credit-positive.)
2. **Extreme operating leverage.** Opex is 77% of revenue; GAAP operating breakeven sits only **11.3% below current revenue**. A 20% decline produces a $217M operating loss absent cost action.
3. **Event risk is the dominant return driver, and it just fired again.** −15.2% on 11/25/26 (CEO succession + guidance merely maintained) following −17.7% on 11/26/25. Three-year Sharpe 0.031.
4. **Buyback timing has destroyed value.** ~$923M repurchased across FY24–FY26 ($131M + $308M + $483.5M) at prices mostly in the $50–75 range; the stock is now $46.30. Capital was deployed at an average price well above current levels while converts remain outstanding.
5. **Dilution / near-term convert.** Diluted shares 292.7M vs basic 270.6M (**+8.2%**). ~$500M of 0.25% converts mature in 2027 and appear to be at or near the money at $46.30 — potential share settlement or a ~$500M cash call that competes with buybacks. *(Exact conversion prices not retrieved — see gaps.)*
6. **Growth deceleration.** Revenue +15.3% → +18.1% → **+12.4%** (FY26); Q1 FY27 re-accelerated to +15.2%, but that is the quarter the stock fell 15% on cautious guidance.
7. **Altman Z 0.13 (Distress) / 1.77 market-cap-adjusted** — reported for completeness. Structurally penalized by the −$3.71B accumulated deficit and not corroborated by cash flow, coverage, or liquidity.
8. **Elevated rates.** 10Y at 5.13%, 2Y–10Y +39bp (not inverted). Refinancing the 2029 converts at market would cost ~10x the current 0.50% coupon, and a ~5% discount rate pressures the 4.1x EV/sales multiple.

---

### Data Gaps (explicit)
- **No agency credit rating or CDS spread** available — "Investment Grade" is my fundamental inference, not an agency opinion.
- **Exact conversion prices / principal split** between the 2027 and 2029 convert tranches not retrieved; the ~$500M / ~$862M split is reconciled from press releases and total debt, and should be verified against the 10-Q.
- **Revolver covenant terms unverified** (assumed undrawn with standard net-leverage test; net-cash position makes breach implausible).
- **R&D line item** absent from the income statement feed — opex ($2,198.0M) is derived as gross profit less operating income.
- **Beta conflict:** vendor profile 0.638 vs computed 1.165 (756d vs SPY). I used ~1.0–1.2 conservatively; the discrepancy is un-resolved.
- **Balance-sheet `net_debt` field ($741.4M) is inconsistent** with total debt less cash (−$842.7M). I used **net cash of $842.7M**, which ties to the leverage tool and to the raw balance sheet.
- No peer multiples gathered (budget constraint) — EV/revenue 4.1x and EV/FCF 14.0x are stated without a comparable-set benchmark.
