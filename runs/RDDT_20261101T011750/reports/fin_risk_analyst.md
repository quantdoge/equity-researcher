# Fin Risk Analyst

- Symbol: RDDT
- Elapsed: 67.5s

---
## RDDT — Financial Risk Assessment
**Reddit, Inc. | Communication Services / Internet Content & Information | Price $91.73 (last close 2026‑10‑30) | Mkt cap $17.64bn**

**Data currency note:** FY2025 annual statements (filed 2026‑02‑06) plus quarterly data through Q3 2026 (filed 2026‑10‑30). Latest balance sheet available is 2025‑12‑31 — nine months stale and therefore *conservative* on cash, since TTM FCF of ~$1.2bn accrued after that date.

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE (effectively AAA-like solvency)**

Reddit is, financially, an almost debt-free company.

| Metric | Value | Read |
|---|---|---|
| Total debt | **$23.2M** (all lease-related; $0 short-term, $0 long-term funded debt) | Negligible |
| Debt / equity | 0.01 | ~Nil |
| Debt / assets | 0.01 | ~Nil |
| Net debt / EBITDA | **−4.51x** (net cash) | Net cash position |
| Net cash | **$2.45bn** (cash & ST inv. $2.477bn − debt $23.2M) | 13.9% of market cap |
| Interest coverage (EBIT/interest) | **N/A — interest expense $0.00** in FY25 and all six reported quarters | No debt service burden exists |
| Altman Z‑Score | **7.66 → Safe zone** (threshold 2.99) | Bankruptcy probability de minimis |
| Piotroski F‑Score | **7 / 9 → Moderate-strong** | |

**Z‑Score composition:** 1.2(x1 0.884) + 1.4(x2 **−0.207**) + 3.3(x3 0.163) + 0.6(x4 9.444) + 1.0(x5 0.680) = 7.66. The score is driven by x4 (book equity / total liabilities = 9.44x — liabilities are only $310M) and by working capital (x1). *Caveat: x2 is negative because retained earnings are −$671M — an accumulated deficit built from the SBC-heavy loss years (2023 equity was **negative** $413M). This is an accounting artifact of a 2024 IPO, not a solvency signal. x4 uses book rather than market equity, so the score is flattered; but with no funded debt the conclusion holds regardless.*

**Credit ratings / CDS:** none exist. Reddit carries no public rating or traded credit protection, so there is no market-based credit deterioration signal available. **This is a genuine data gap, not a hidden red flag.**

---

### 2. Key Financial Risk Metrics

| Metric | FY2023 | FY2024 | FY2025 | **TTM (Q4'25–Q3'26)** |
|---|---|---|---|---|
| Revenue | $804.0M | $1,300.2M | $2,202.5M | **$3,088.9M** |
| Gross margin | 86.2% | 90.5% | 91.2% | **91.5%** |
| Operating income | −$140.2M | −$560.6M | +$442.0M | **+$908.0M (29.4%)** |
| Net income | −$90.8M | −$484.3M | +$529.7M | **+$991.7M** |
| EBITDA | −$73.3M | −$469.6M | $544.6M | **$1,023.3M** |
| Operating cash flow | −$75.1M | $222.1M | $690.9M | **$1,200.8M** |
| **Free cash flow** | **−$84.8M** | **$215.8M** | **$684.2M** | **$1,198.1M (38.8% margin)** |
| Capex | $9.7M | $6.2M | $6.7M | ~$4.5M |

**Liquidity (2025‑12‑31):** current ratio **11.56x**; quick ratio **11.56x** (no inventory — asset-light); cash ratio **9.13x**; working capital **$2.865bn**; assets/liabilities **10.44x**; cash/liabilities **7.99x**.

**Cash runway:** there is no burn to run out of. Q3'26 total operating expense was $557.6M/quarter; cash alone covers **4.4 quarters of the entire cost base against zero revenue**. With FCF generating $362.6M/quarter, runway is indefinite. **No refinancing cliff exists — there is no funded debt to refinance.** (Lease maturity ladder not disclosed in the retrieved data — minor gap.)

**FCF sustainability:** FCF margin expanded 16.6% → 31.1% → 38.8% TTM. FCF yield **6.79%** on TTM FCF ($1,198M / $17.64bn) versus the tool's 3.69% on the FY2025 base — the gap is purely the growth between periods. Capital intensity is trivially low (capex 0.15% of revenue), so cash conversion is structural, not deferred maintenance.

**Critical adjustment:** TTM SBC was ~$386M ($131.3M in Q3'26 alone). Because SBC is added back in FCF, the headline FCF is overstated. **SBC-adjusted FCF ≈ $812M (26.3% margin, 4.6% yield).** Buybacks of $340M YTD 2026 partially offset dilution, but share count still rose ~3.4% YoY — Piotroski F7 (no dilution) fails.

**Valuation context:** EV = $17.64bn − $2.45bn net cash = **$15.18bn** → 4.9x TTM revenue, 14.8x TTM EBITDA, 17.8x TTM earnings.

---

### 3. Market Risk Profile — **EXTREME**

| Metric | 252-day | 90-day |
|---|---|---|
| Annualised volatility | **78.5%** | **85.7%** |
| Beta vs SPY | **2.24** | **2.59** |
| Max drawdown | **−58.1%** | −54.9% |
| Sharpe (rf = 0%) | **−1.03** | **−2.30** |

Beta is *rising* (2.05 company-reported → 2.24 trailing year → 2.59 trailing quarter). This is the signature of a stock whose risk is becoming more systematic, not less. Volatility of ~80% means a 1-sigma daily move of ~5%; 2-sigma days of ±10% are routine.

**Realised tail events — five single-day drops ≥7% in 19 months of trading:**

| Date | Move | Catalyst |
|---|---|---|
| **2026‑10‑30** | **−29.2%** ($129.60 → $91.73, 33.4M shares) | Q3 beat (rev $895M, +53% YoY, EPS $1.40 vs $1.35) **but weak Q4 guidance + announced test of a login requirement as Google search traffic shrinks** |
| 2026‑07‑31 | −21.0% ($178.04 → $140.67) | Q2 print |
| 2025‑03‑10 | −19.9% ($133.98 → $107.29) | Post-lockup / growth scare |
| 2025‑10‑01 | −11.9% ($229.99 → $202.60) | Google traffic concerns |
| 2026‑02‑06 | −7.4% (intraday −16.6%) | Q4'25 print |

Peak-to-current: **−62.8% from the $246.50 close (Aug 2025)** and −66.1% from the $270.71 close (Sep 2025). Risk-adjusted return since IPO is **negative** — Sharpe of −1.03 means an investor has been paid nothing for 78% volatility. Sortino is not returned directly by the tool; given the Sharpe and the fat left tail, the downside deviation ratio would be materially worse than −1.03 (**approximation, flagged**).

---

### 4. Downside Scenario Analysis — Revenue −20%

Applied to the TTM run-rate of $3,088.9M (revenue falls $617.8M to $2,471.1M), holding gross margin at 91.5% and total opex at the TTM level of $1,919.8M:

| Line | Base (TTM) | **−20% revenue, opex flat** | −20% rev, opex −10% | −20% rev, opex +5% (no flex) |
|---|---|---|---|---|
| Revenue | $3,088.9M | **$2,471.1M** | $2,471.1M | $2,471.1M |
| Gross profit | $2,827.8M | **$2,261.1M** | $2,261.1M | $2,261.1M |
| Opex | $1,919.8M | **$1,919.8M** | $1,727.8M | $2,015.8M |
| Operating income | $908.0M | **$341.3M (13.8%)** | $533.3M (21.6%) | $245.3M (9.9%) |
| EBITDA | $1,023.3M | **~$358M** | ~$550M | ~$262M |
| Interest expense | $0 | **$0** | $0 | $0 |
| FCF (post-SBC) | ~$812M | **~$250–330M** | ~$430M | ~$180–250M |
| Altman Z | 7.66 | **~7.0 (still Safe)** | ~7.2 | ~6.9 |

**Survivability: total.** Even a 20% revenue shock leaves positive EBITDA, positive FCF, zero debt service, and $2.45bn of cash. There is **no covenant to breach** (no credit agreement) and **no maturity to refinance**. Extending to a −40% revenue scenario: revenue $1,853M, gross profit ~$1,690M, opex flat $1,920M → operating loss of ~−$230M and FCF of roughly −$150M to −$200M — cash would fund that for over a decade.

**The risk is entirely in the equity, not the enterprise.** At current price, EV/EBITDA is 14.8x. In the −20% scenario, EBITDA falls to ~$358M. If the market re-rates a de-growing ad platform to 12–15x EBITDA:

> Equity value = $2,454M net cash + ($358M × 12–15x) = **$6.75bn–$7.83bn → $35–$41/share → −55% to −62%**

That is the honest downside case: **a balance-sheet-fortress business with a valuation that has no cushion if growth stalls.** The −29% reaction on 2026‑10‑30 is the market beginning to price exactly this.

---

### 5. Overall Financial Risk Rating: **MODERATE**

Decomposed because a single word obscures the two very different risk profiles here:

| Risk axis | Rating | Basis |
|---|---|---|
| **Solvency / credit risk** | **LOW** | $2.45bn net cash, $23.2M total debt, Z = 7.66, zero interest expense |
| **Liquidity risk** | **LOW** | Current ratio 11.6x, cash ratio 9.1x, no maturities, positive FCF |
| **FCF sustainability** | **MODERATE** | 38.8% FCF margin but 32% of it is SBC add-back; revenue rests on one distribution channel |
| **Market / equity risk** | **CRITICAL** | 78–86% vol, beta 2.24–2.59, −58% drawdown, Sharpe −1.03, −29% single-day gap |

**Net: MODERATE overall — with the explicit caveat that this company will not fail, but its stock can lose another 50%+ without any deterioration in solvency.** Do not confuse the two.

---

### 6. Key Red Flags

1. **Google search traffic dependency — the single largest risk.** The −29% crash was explicitly attributed to shrinking Google referral traffic and a defensive login-requirement test. Reddit's growth engine sits inside a competitor's (GOOG's) AI-answer rollout. This is a *structural, exogenous, non-diversifiable* revenue risk, and it is the one thing the balance sheet cannot protect against.
2. **Guidance deceleration despite a 53% growth quarter.** Revenue beat ($895M vs $877M consensus) and EPS beat ($1.40 vs $1.35) yet the stock fell 29%. When beats get punished this hard, the market is repricing the *terminal growth rate*, not the quarter.
3. **Beta is rising, not falling** (2.05 → 2.24 → 2.59). Early-stage volatility should decay with scale; here it is intensifying, meaning the risk is becoming market-correlated (AI/ad-tech cyclicality) rather than idiosyncratic.
4. **SBC distorting both FCF and F-Score.** $386M TTM SBC = 12.5% of revenue. F-Score's F7 (no dilution) fails — diluted shares up ~3.4% YoY (186.4M → 192.6M weighted). Headline 38.8% FCF margin overstates distributable cash by roughly a third.
5. **Stale cash figure / no post-crash balance sheet.** Latest balance sheet is 2025‑12‑31. Post-Q3 cash, the $340M 2026 buyback, and any credit facility are unverified (**data gap**).
6. **Inconsistent net-debt field.** The balance-sheet feed reports net_debt of −$930.4M, which does not reconcile with cash $2,476.8M less debt $23.2M = −$2,453.6M. I have used the $2.45bn figure, which reconciles to the reported cash line and to the leverage tool. Flagged as a **feed integrity issue**.
7. **Accumulated deficit of −$671M and 2023 negative equity ($413M)** — resolved by IPO proceeds, but it means book equity (which underpins the Z-Score's x4) is a thin, recent construct.
8. **Controlled company.** Advance Publications' control constrains shareholder recourse in a governance event.
9. **No credit rating, no CDS, no peer-multiple comparison.** The sector peers returned (GOOG, META, NFLX, DIS, VZ, TMUS) are $150bn–$3.4tn incumbents with different economics — **no genuine comparable set was obtainable from the tools.** Relative valuation is therefore asserted from absolute multiples only, not verified against peers.

---

**Bottom line for the memo:** Reddit's balance sheet is about as safe as a newly public company's can be — net cash of $2.45bn, no funded debt, no maturities, a Safe-zone Z-Score, and 38.8% FCF margins. The financial risk is not in the enterprise value; it is in the equity price, which trades at 14.8x EBITDA on a growth rate the company just told the market is decelerating, in a business whose customer acquisition runs through a competitor's search results page. **Solvency risk: Low. Equity impairment risk: High.**
