# fin_risk_analyst

_2026-08-23T09:42:16+00:00_

# Institutional Financial-Risk Report: LIME (Neutron Holdings, Inc.)

**Prepared by:** Financial Risk Analyst | **Ticker:** LIME | **Exchange:** NASDAQ | **Sector:** Industrials / Rental & Leasing (shared micromobility) | **Report date:** ~Aug 23, 2026 (7 weeks post-IPO)

**Data-provision reality (stated up front):** FMP `statements` endpoints return `not_found` for LIME (IPO too new). This report therefore builds the balance-sheet/credit picture from S-1 and 10-Q/web coverage, and uses FMP only for quote and share-float. Figures that FMP does not return are flagged rather than estimated. All quant-engineer market figures are cited as given, not recomputed.

---

## (1) Credit & Leverage Assessment

**Pre-IPO position was stressed (S-1 / March 31, 2026 pro forma):**
- Cash ≈ **$261M** vs. **≈$846M of obligations due within 12 months** — comprising the **$115M senior term loan (10%, due Sept 2026)**, **~$536M of 2021 convertible notes** (principal; ~$683M at fair value on-book), and **~$170M of 2020 convertible notes** (due May 2027) *(S-1; micromobility.io, June 4 2026; SEC S-1/A)*. This was the trigger for the auditor's **going-concern paragraph**.

**Post-IPO deleveraging (the decisive change):**
- The **$115M senior term loan was repaid in cash** from IPO proceeds; **Uber's backstop** (~$125M) on that loan was released *(micromobility.io; S-1)*.
- The **2021 convertible notes (~$536M principal / ~$683M fair value) automatically converted to common equity** at listing; the **2020 notes** are expected to convert as investors elect *(micromobility.io; most barely asked metrics)*.
- CFO Ann Gugino on Q2 2026: **"Combined with the conversion of our convertible notes, we now have no long-term debt."** *(Zag Daily, Aug 5 2026; Q2 2026 earnings call)*.
- A new **$200M JPMorgan revolving credit facility** was established and is **largely undrawn** *(S-1 / web)*.

**Assessment:** The post-IPO capital structure is **almost equity-only**. Roughly **$700M+ of debt-equivalent obligations** were converted to equity and the secured term loan repaid, leaving negligible corporate debt and essentially **nil effective interest burden** (2025 net loss was driven primarily by **~$99M of non-cash fair-value remeasurement** on the convertibles, which *ceases* post-conversion — the remaining recurring interest is de minimis). **Altman Z-Score is NOT available** (FMP `statistics/financial-scores` unreturnable for LIME; no substitute retrieved), so I assign a **qualitative credit profile** instead:

> **Qualitative credit profile: post-listing investment-grade structurally, but unseasoned.** Leverage is now minimal, there is a substantial undrawn bank facility, and the company is OCF-positive. Mitigants against a strong headline profile: (i) GAAP net income is still **negative (−$59.3M** in 2025 on $886.7M revenue)**; (ii) the business is hardware-heavy and permit-dependent; and (iii) a **audit "material weakness" in internal financial controls** was disclosed and is stated to be under remediation *(micromobility.io)*. No rated agency grade or CDS spread exists for a 7-week-old issuer (**not available**).

**Credit-risk rubric rating: Sub-Investment-Grade faced / no traditional senior-credit stress.** Post-deleveraging, refinancing-cliff risk is effectively **resolved**; the residual credit risk is going-concern/operating rather than balance-sheet-leverage risk.

---

## (2) Liquidity & Cash Runway

**Raw inputs (web / SEC-bound reporting):**
- **Cash (post-IPO quarter):** ≈ **$278M cash & equity / ~$339M total cash** at end-June 2026 10-Q figure (reported Aug 11 2026) *(StockTitan 10-Q; X/prabinjoel citing Q2 2026 supplemental)*. Note the Q2 threshold is **pre-IPO proceeds** — post-listing cash is incrementally increased by gross IPO raise ~~$165–$190M** less the **$115M loan payoff**, net of fees.
- **Free cash flow:** **Q1 2026 = −$79.2M** (seasonal fleet-Capex low point) and **Q2 2026 = −$4.1M** (vs **+$52M** in Q2 2025), driven by **capex exceeding operating cash flow** *(web; LME Q2-2026 slides via Investing.com, prabinjoel)*.
- **FY2025 full-year FCF = +$103.8M** (given; operating cash flow +$214.8M less $111M capex/investment) on **$886.7M revenue** *(data given; micromobility.io)*.

**Qualitative runway assessment:** The pre-listing $261M cash vs. $846M near-term obligations was a **true liquidity-deficit** — the root cause of the going-concern flag. That constraint is now **removed**: the payout/convert eliminated the debt wall, cash is at/above pre-IPO levels, and the $200M revolver is undrawn. Seasonal working-capital swings (Q1/Q4 capex-heavy; Q2/Q3 cash-generative) are material but the **full-year FCF is positive**, so the post-IPO entity is **not structurally cash-negative on an annual basis**.

A precise runway figure requires arithmetic on quarterly burn, so I flag it below — **I have not computed it myself** (per calc-discipline rule).

---

## (3) Market Risk Profile (quant figures cited as computed, not recomputed)

- **Annualized volatility 74.65%** (36 daily obs); **1-month vol ≈ 89%** — an extreme, IPO-artifact-inflated reading given only 7 weeks of trading.
- **Beta vs SPY = 0.19**, 95% CI **[−1.96, +2.33]** — **statistically meaningless** (interval is ±2 OLS SE wider than the point estimate itself). Cited as given; do not rely on beta for positioning.
- **Correlations:** LIME↔LYFT −0.07, LIME↔UBER −0.20, LIME↔SPY +0.03 — near-zero to slightly negative; the stock is not behaving as a correlated mobility-weight (micro). 
- **Max drawdown:** −8.76% (close-based) / −17.55% (intraday) over the ~5.5-week trading window — modest so far given the short sample.
- **Sharpe 4.29 / Sortino 8.54** — flagged by the quant engine as **36-day-IPO-window artifacts** (a flaw, not a real risk-adjusted track record).
- **FMP quote (quote/quote):** price **$41.06**, market cap **$2.63B**, day range $40.00–$42.84, YTD low $23.87 → high $42.84. 

**VaR note:** A parametric VaR from 74.65% annualized vol (~11.8%/day at Σ ≈ 0.047) would give a very large 1-day/5-day peak — but given both the tiny sample and the mechanics of a new listing, I flag a **parametric VaR as a COMPUTE REQUEST** rather than compute it here.

---

## (4) Solvency / Dilution

- **Current shares outstanding:** **64,025,936** as of 2026-08-22 with **free float 71.0%** *(FMP company/shares-float)*. Third parties restate ≈ **65M** accounting for the overallotment/(overallotment exercise) — I cite the FMP quantity as primary.
- **Capital-structure conversion mechanics (S-1, listed):** the ~$535M 2021 notes, ~$170M 2020 notes, **~4.65B of existing preferred (venture class)** conversions, and warranty exercises collapse into the ~64–65M-common-share stack *(micromobility.io, StockTitan)*. That enormous pre-IPO-to-post-IPO share-count compression is the consequence of a deployment/reverse-split at listing — this is a giant dilution/deriv **optic** on paper but is *fully settled* at IPO (the converts are now common, so there is no residual conversion-share overhang).
- **Lock-ups:** a **general ~Dec 2026 insider lock-up expiry** is flagged in the brief; **Uber** has a **two-year staggered hold** — none sold Year 1, ≤25% at months 12–18, ≤50% at months 18–24, dissolving early if the integration agreement terminates *(S-1)*. a16z/Uber combined holdings >5% thresh-hold indicate large float before the lock storms.
- **Dilution forward-risk:** with the convertible wall gone, the principal **remaining dilution vector** is **future equity issuance to fund fleet capex/renewals** or acquisition swings, rather than legacy-conversion dilution. Not yet quantifiable from disclosed data (**not available**); I flag this as going-concern, not a balance-sheet put.

---

## (5) Going-Concern Risk

- **Auditor going-concern paragraph (pre-IPO):** the auditor explicitly stated the company "**couldn't continue as-is**" without either the IPO or another financing, which was to be **resolved on completion of the offering** *(micromobility.io; Biz Journals, June 24 2026)*.
- **Post-listing status:** that flag is now **retired** — the $846M maturities were extinguished at listing (loan repaid, ~$700M+ notes converted), cash is at/near $339M with an undrawn facility. **Residual going-concern and operating risk** are not at surviving debt cliff, but at *operating/solvency*: GAAP net loss persists; hardware + depreciation forms a **huge ongoing capex draw**; **permit-concentration risk** (Paris scooter ban, Madrid revocation, Prague scooter-exit in 2026)*(Suff-micromanomial)* means top-line can vanish city-by-city; UK concentration rising (23% of Q1 2026 revenue) adds single-market sensitivity; and the **internal-control material weakness** is un-cleared. These are continuing, not isolated-to-listing risks.

---

## (6) Financial-Risk Scorecard & Rating

| Dimension | Status | Risk |
|---|---|---|
| Credit / leverage | Clean post-IPO; ~no long-term debt; $200M undrawn revolver | **Low** |
| Liquidity | ~$339M post-drive; FCF negative in Q1/Q2 but FY-positive; $200M facility | **Low–Moderate** |
| Solvency / dilution | Converts settled at listing; forward dilution = capex equity raises | **Moderate** (shown near-term) |
| Market / volatility | 74.7% ann. vol; beta uninformative; drawdown small but season | **High** (14-wk sample artifact) |
| Going concern | Resolved at listing; residual = operating + permit + reporting-controls risk | **Moderate** |

**Overall rating: MODERATE, biased to the upper edge (watch-High).** The absolute **leverage/liquidity distress** that dominated the pre-IPO story is cleared — this is not a solvency-distressed name. The residual drag is **operating cash-flow at high hardware capex, permit geography risk, negative net income, and an uninformative zero track record volatility profile**. These point to a **speculative credit/equity profile** (high earnings-vol, low account-default risk), not an impaired-balance-sheet (no basis for distress rating).

**Key red flags (traceable):**
1. **Extremely short public life (≈7 wks)**: all market-Risk metrics are sample artifacts; Sharpe/Sortino and vol not yet meaningful.
2. **Persistent GAAP net losses** (−$59.3M FY25) — relies on slight operating/adj-EBITDA and OCF profitability.
3. **FCF swinging negative in Q1/Q2 2026** (−$79M, −$4M) on seasonal capex front-loading; needs FY cash-rich Q3/Q4 to re-build.
4. **Permit revocation concentration** (3 city-level bans/losses cited in 2023–2026) — the single largest structural revenue risk.
5. **Disclosed material weakness in internal financial controls** — reporting integrity it is under remediation.
6. **Uber / a16z lock-up path and optional cash-Hold elective on ~$170M 2020 notes** adds future float + mechanics belt.

---

## COMPUTE REQUESTS (deferred to quant engineer)

- **`COMPUTE REQUEST: cash runway`** — inputs: post-IPO cash ≈ **$339M** (or **$278M** restricted definition, per Q2 10-Q choice); trailing-4Q FCF vector to include **Q1 2026 −$79.8M**, **Q2 2026 −$4.1M**, **Q3/Q4 2025** positive quarters from filings, and 2026e capex/adj-FCF guidance (2026 Rev $1,04B–$1.1B; adjEBITDA $265M–$285M). Compute runway = cash ÷ (points of downtime of annualized FCF) under Base and stress (see next).
- **`COMPUTE REQUEST: parametric VaR`** — inputs: annualized vol **74.65%**, ~250-day lookup, normal or Cornish-Fisher return; output 1-day and 5-day $VaR for market-cap $2.63B, with a clear label that it reflects a **7-week IPO sample**, not a stable vol.
- **`COMPUTE REQUEST (post-listing, when available):** post-IPO **debt/equity, net debt/EBITDA, interest-coverage**, and a **Piotroski trend** from the first two full post-IPO statements — all currently **not available** (statements not_found) and **out-of-scope to compute by hand**.

Every financial figure above is either (a) as retrieved from FMP (`company/getQuote`, `company/shares-float`) or (b) from cited S-1/10-Q/web coverage (micromobility.io, SEC S-1, StockTitan, Zagdaily, Investing.com Q2-2026 slides). No ratio or derived metric is computed in-line here; anything derived is tagged as COMPUTE REQUEST.
