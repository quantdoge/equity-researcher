# Fin Risk Analyst

- Symbol: VSAT
- Elapsed: 58.5s

---
Both fetch attempts failed (403s and a binary PDF). I have sufficient data from the structured feed plus rating snippets to complete the assessment. Writing the report now.

---

# VSAT — Viasat, Inc. | Financial Risk Assessment

**Sector:** Technology / Communication Equipment · **Price:** $74.37 · **Market cap:** $10.24B · **FYE:** March 31
**Latest balance sheet:** 2026-09-30 (Q2 FY2027) · **Latest full year:** FY2026 (ended 2026-03-31)

## 1. Credit Risk Assessment

**Rating: Sub-Investment Grade (high-yield, deep tier).** S&P has moved VSAT to **'B+' and then a further notch lower to 'B'** (negative outlook); Fitch carries **'B'** (stable, Jan-2025 action); Moody's rates the secured term loan **Ba3**. This is 3–5 notches below investment grade. *Source: web search snippets — S&P/Fitch pages themselves returned HTTP 403, so the exact effective dates and current notch could not be independently verified.*

The paradox is that headline leverage looks moderate while earnings-based coverage is alarming:

- **Net debt / EBITDA: 2.83x** on the reported $1,835M EBITDA — but that EBITDA is propped up by a ~$372M non-operating gain (EBIT $480M vs GAAP operating income of only $108M). On an operating-income basis, EBITDA is ~$1,463M and **net leverage is 3.55x**.
- **Interest coverage is the core weakness: 0.30x** on operating income (GAAP operating income $108.1M vs interest expense $360.3M). Even on the flattered EBIT figure it is only **1.33x**. VSAT does not cover interest from operations — it relies on EBITDA-before-capex, and **capex of $993M consumes 54% of EBITDA**, leaving (EBITDA − capex) / interest of just **1.3–2.3x**.
- **Altman Z-Score 0.79 — Distress zone** (< 1.81). Because the tool uses book equity, I re-ran it with market cap ($10.24B / $10.50B liabilities → x4 ≈ 0.98): **Z ≈ 1.11, still firmly in distress territory.** This is not a book-equity artifact.
- **Piotroski F-Score 6/9 (Moderate)** — but the failures are the forward-looking ones: negative ROA, **share count growth 130.2M → 134.7M → 138.6M (dilution)**, and **gross margin deterioration**.

## 2. Key Financial Risk Metrics

| Metric | Value | Assessment |
|---|---|---|
| Total debt | $6,867M (Q2 FY27) | — |
| Cash & ST investments | $1,759M | Strong absolute buffer |
| Net debt | $5,109M | — |
| Net debt / EBITDA | **2.83x** reported / **3.55x** operating-basis | Elevated |
| Gross debt / EBITDA | 3.78x / 4.74x | Elevated |
| Debt / equity | 1.47x | High |
| Debt / assets | 0.46x | High |
| Total liabilities / assets | 69.5% | High |
| **Interest coverage (op. income)** | **0.30x** | **Severe** |
| Interest coverage (EBIT / EBITDA) | 1.33x / 5.09x | Weak / adequate |
| Current ratio | 2.41x (FY26) → **1.65x (Q2 FY27)** | Deteriorating |
| Quick ratio | 2.19x → 1.49x | Deteriorating |
| Cash ratio | 1.35x → 0.93x | Adequate |
| Working capital | $1,827M → $1,238M | Shrinking |
| Cash to liabilities | 0.17x | Thin vs total obligations |
| Altman Z-Score | 0.79 (mkt-cap adj. ≈ 1.11) | **Distress zone** |
| Piotroski F-Score | 6 / 9 | Moderate |
| FCF yield | 5.96% ($597M FCF) | Genuine inflection |

**Liquidity — the current ratio collapse is mechanical, not operational.** Short-term debt jumped from $57.8M (Mar-26) to **$659.1M (Sep-26)** as the **$400M 5.625% 2027 notes reclassified into current liabilities**. Cash of $1,759M covers that maturity ~4.4x over, so there is **no near-term refinancing cliff** — but it does mean VSAT must tap capital markets in a 'B' credit within 12 months.

**FCF — the single genuine bright spot.** FCF went **−$796M (FY23) → −$851M (FY24) → −$122M (FY25) → +$597M (FY26)** as capex fell from $1,539M to $993M with the satellite build cycle completing. This is a real, structural improvement and it is what keeps the risk rating off "Critical."

## 3. Market Risk Profile

| Metric | Value | Assessment |
|---|---|---|
| Annualised volatility (3y) | **88.0%** | Extreme — ~5.5x market |
| Beta vs SPY | **2.18** (profile: 1.76) | Very high |
| Max drawdown (3y) | **−49.7%** | Severe |
| Sharpe ratio | 1.33 | See caveat |

**Caveat on Sharpe:** a 1.33 Sharpe alongside 88% volatility implies roughly a +117% annualised return over the window. The Sharpe is driven by a **single enormous rally**, not by risk control — the stock's max drawdown of nearly 50% shows the downside is fully live. Beta of 2.18 means a 20% market drawdown implies a **~40%+ hit to VSAT**. Note the **beta discrepancy (2.18 computed vs 1.76 in profile)** — treat 2.18 as the more conservative, recent-window estimate.

## 4. Downside Scenario: Revenue −20%

Applied to FY2026 revenue of $4,640M (≈ −$928M), with ~27–32% blended gross margin and limited fixed-cost flex:

| | Base (FY26) | −20% Revenue |
|---|---|---|
| Revenue | $4,640M | $3,712M |
| Operating income | $108M | **≈ −$170M** |
| EBITDA (operating basis) | $1,463M | **≈ $1,185M** |
| Net debt / EBITDA | 3.55x | **≈ 4.4x** |
| Interest coverage (op. income) | 0.30x | **Negative** |
| EBITDA / interest | 4.06x | ≈ 3.3x |
| FCF | +$597M | **≈ +$290M to +$490M** |

**Interpretation:** a 20% revenue decline pushes operating income deeply negative and leverage to ~4.4x — the level at which a 'B' credit typically faces downgrade pressure and constricted market access. The company would **not** breach liquidity (cash $1.76B covers ~3–4 years of the resulting burn), and FCF plausibly stays positive if capex is trimmed. **The risk is not insolvency — it is a refinancing failure at the 2027/2029 maturities forcing distressed exchange or dilutive equity issuance.** A 30%+ decline is where this turns genuinely critical.

## 5. Overall Financial Risk Rating: **HIGH**

Not "Critical" because: $1.76B cash, positive and improving FCF, no maturity wall inside 12 months that cash cannot cover, and net leverage of 2.8–3.6x is high but not unmanageable. Not "Moderate" because: interest is not covered by operating income (0.30x), the Altman Z-Score sits in the distress zone on both book and market equity, and the credit is rated 'B' with negative momentum.

## 6. Key Red Flags

1. **Interest coverage of 0.30x on operating income.** VSAT earns $108M of operating income against $360M of interest. The business does not service its debt from operations; it services it from EBITDA that capex then consumes.
2. **Altman Z in the distress zone even using market cap (≈1.11).** Bankruptcy-risk signal, not an accounting artifact.
3. **Sub-investment-grade ratings in downgrade motion** — S&P has cut VSAT at least twice, the second time to 'B', with a negative outlook.
4. **Quarterly deterioration in FY2027.** Operating income fell $47.3M → $7.1M (Jun→Sep 2026); net loss widened −$51.7M → −$128.7M; **interest expense rose to $102.0M/quarter**, annualising to ~$408M vs $360M in FY26.
5. **Goodwill & intangibles fell $4,060M → $3,491M (−$569M) in six months**, with a $504M drop in the Sep-26 quarter alone — consistent with a **goodwill impairment** (I could not confirm the charge from the filings; SEC/investor pages were 403-blocked). Goodwill is still $3.5B, **76% of total equity** — further impairment would directly erode the covenant and equity cushion.
6. **Gross margin compression:** 33.0% (FY25) → 27.4% (FY26); quarterly 35.7% → 32.1%. Core pricing power is weakening — the S&P downgrade rationale cited competitive pressure.
7. **Refinancing dependence:** $400M 2027 notes due within 12 months, then ~$1.4B in 2029 (2029 notes + term loan). A 'B' issuer must refinance into a market it does not control.
8. **Dilution:** share count up 6.4% over two years (130.2M → 138.6M) and still rising — equity is being used to plug the funding gap.
9. **88% volatility / 2.18 beta** — position sizing risk is as significant as balance-sheet risk here.

## Data Gaps (explicit)
- **S&P and Fitch rating pages returned HTTP 403**; ratings, outlooks and dates are from search snippets only and could not be verified at source. Two distinct S&P actions were found ('B+' and 'B'), so the current notch is uncertain but is at best 'B+'.
- **Debt maturity ladder is partial** — assembled from search snippets and a third-party credit study, not from the primary 10-K note. Figures: 2027 notes $400M; 2029 notes ~$733M (one source cites a $1.25B issue due 2029 — possibly partially retired); term loans due 2029 ~$677M and 2030 ~$604M; 2031 notes ~$553M. **Covenant terms, revolver capacity and the EXIM facility size are unknown.**
- **No quarterly cash-flow statement available**, so Q2 FY27 operating cash flow and true cash burn are inferred from balance-sheet movements.
- **CDS spreads and peer-multiple benchmarking were not obtained** — sector-relative credit positioning is unassessed.
- Downside scenario uses blended-margin assumptions; segment-level contribution margins (Satellite Services vs Commercial Networks) were not modeled and would sharpen the result.
