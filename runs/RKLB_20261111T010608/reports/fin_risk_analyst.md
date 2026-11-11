# Fin Risk Analyst

- Symbol: RKLB
- Elapsed: 110.1s

---
## RKLB — Financial Risk Assessment
**Rocket Lab USA, Inc.** | Industrials / Aerospace & Defense | Price ~$70.86 (2026-02-20 close), Market cap ~$37.5B

---

### 1. Credit Risk Assessment

**Rating: Sub-Investment Grade (speculative) — but with a LOW near-term default probability.**

This is a deliberately split verdict, because standard credit metrics point in opposite directions for Rocket Lab.

RKLB is a **pre-profit, cash-consuming growth company with a fortress balance sheet**. It carries $254.0M of total debt against $1,016.6M of cash — a **net cash position of $762.6M**. Debt/assets is 0.11 and debt/equity is 0.15. That is not a leveraged company; that is a well-funded one.

But it has **no interest coverage and no positive EBITDA**. FY2025 EBIT was –$199.4M against $26.5M of interest expense, giving interest coverage of **–8.6x**. Reported net debt/EBITDA of 4.91x is a **sign/formatting artifact** of dividing a negative net-debt figure by negative EBITDA — it carries no economic meaning and should be ignored. There is no credit rating and no CDS market for this name (data gap).

The $26.5M interest charge is explained by **$355.0M principal of convertible senior notes at 4.25%** outstanding as of Sept 30, 2025 (per 10-Q), versus a $254.0M *carrying* value at year-end — the gap is the equity component/reclassification, not a repayment. These are unsecured obligations with no meaningful near-term maturity cliff: **$0 short-term debt, $154.1M of long-term debt**.

**Verdict:** default risk over the next 24 months is low — liquidity covers it many times over. The actual credit risk is *refinancing-conditioned-on-equity-prices*, since the company's access to capital depends on a $37.5B market cap holding up.

---

### 2. Key Financial Risk Metrics

| Metric | FY2025 | FY2024 | FY2023 | Read |
|---|---|---|---|---|
| Revenue | $601.8M | $436.2M | $244.6M | +38% YoY; 41.8% 3-yr CAGR |
| Gross margin | **34.4%** | 26.6% | 21.0% | Genuine, sustained improvement |
| Operating margin | –38.0% | –43.5% | –72.7% | Improving but deeply negative |
| EBITDA | –$155.5M | –$151.8M | –$144.9M | **Essentially flat for 3 years** |
| Net income | –$198.2M | –$190.2M | –$182.6M | Losses not narrowing |
| Total debt | $254.0M | $468.4M | $176.7M | Deleveraged in 2025 |
| Cash & ST inv. | $1,016.6M | $419.0M | $244.8M | Raised heavily in 2025 |
| Net cash | **+$762.6M** | –$197.4M | –$14.2M | Flip to net cash |
| Debt/equity | 0.15 | 1.22 | 0.32 | Low |
| Interest coverage | **–8.6x** | –46.9x | –41.1x | No coverage |
| Current ratio | **4.08** | 2.04 | 2.13 | Very strong |
| Quick ratio | 3.61 | — | — | Very strong |
| Cash ratio | 3.04 | — | — | Very strong |
| Altman Z-Score | **1.61 (Distress)** | — | — | **See caveat — meaningless here** |
| Piotroski F-Score | **5 / 9 (Moderate)** | — | — | Mixed |
| FCF | –$321.8M | –$116.0M | –$153.6M | Deteriorated sharply |
| FCF margin | **–53.5%** | –26.6% | –62.8% | Worsened on Neutron capex |
| FCF yield | **–0.86%** | — | — | EV ~$36.8B → EV/Sales ~61x |

**On the Altman Z-Score (1.61, "Distress"): discard it.** The tool's own note flags that x4 uses book equity ($1.72B) rather than market cap. Substituting market cap of $37.5B makes x4 ≈ 62 and the Z-score ≈ **37**, an absurd "ultra-safe" reading. With a 21.8x price-to-book, the equity term dominates and the model has **zero information content** for RKLB. Do not let this number drive a credit decision.

**On the Piotroski F-Score (5/9):** the two failures that matter are F1 (negative ROA) and F2 (negative operating cash flow), plus F7 (**dilution**). Shares outstanding grew from 466.2M (2022) to 530.7M (2025), **+13.8%**. The offsetting positives — lower leverage, improving gross margin, improving ROA, no accruals games — are real but are "turnaround" points, not "quality" points.

---

### 3. Market Risk Profile

*The FMP volatility/beta endpoint is unavailable on this subscription tier (`historical-price-eod/dividend-adjusted` returned an error). All figures below are computed manually from the daily OHLC provided.*

| Metric | Value | Source |
|---|---|---|
| Annualised volatility | **~90%** (range 78–112%) | Monthly log-return derived; 38 months of data |
| Beta vs S&P 500 | **2.61** | FMP company profile |
| Max drawdown (3-yr, close basis) | **–55.5%** | $7.93 (Jul-2023) → $3.53 (Apr-2024) |
| Max drawdown (3-yr, intraday) | **–56.9%** | $8.05 → $3.47 |
| Recent drawdown | –33.7% | $96.30 (Jan-2026) → $63.87 (Feb-2026) |
| 3-yr total return | **+1,731%** | $3.87 → $70.86 |
| Sharpe ratio | **~1.2–1.7** | Method-sensitive; 0% rf |
| Calendar 2023 / 2024 / 2025 | +42.9% / +360.6% / +173.9% | Annual close-to-close |

Three points of interpretation matter far more than the numbers:

1. **The Sharpe ratio is a trap.** A ~1.5 Sharpe on 90% volatility is not evidence of quality risk-adjusted return — it is evidence of unprecedented multiple expansion. Price-to-sales went from roughly **3.7x in 2023 to ~62x today**, on revenue that grew 2.8x. The return is overwhelmingly re-rating, not cash generation. This is the single most fragile part of the profile: the same mechanism that produced +360% in 2024 can produce –50% in a de-rating.

2. **Beta of 2.61 understates drawdown risk.** In a market-wide risk-off event, a 2.6-beta, unprofitable, long-duration asset with 61x EV/Sales is likely to see far more than 2.6× the index decline. The observed history includes three separate drawdowns of 34–57% in three years.

3. **Zero negative calendar years is a small-sample artifact.** Three years of uninterrupted positive returns is a survivorship illusion; do not extrapolate. Sortino is not separately computable meaningfully with n=3 annual observations.

---

### 4. Downside Scenario Analysis: Revenue –20%

Base FY2025 cost structure: gross profit $207.2M; total opex $436.0M (SG&A $165.3M + implied R&D ~$270.7M); D&A $43.9M; capex $156.3M.

| Scenario | Revenue | GM | Op. loss | EBITDA | Est. FCF | Cash runway |
|---|---|---|---|---|---|---|
| **Base (actual)** | $601.8M | 34.4% | –$228.8M | –$155.5M | –$321.8M | **3.2 yrs** |
| **A: Rev –20%, opex flat, capex trimmed to $130M** | $481.4M | 34.4% | –$270.3M | –$226.4M | ~–$376M | **2.7 yrs** |
| **B: Rev –20%, opex cut 10%, capex $130M** | $481.4M | 34.4% | –$226.7M | –$182.8M | ~–$313M | **3.2 yrs** |
| **C: Severe — Rev –35%, GM compresses to 22%, Neutron delayed** | $391.2M | 22.0% | –$306.3M | –$262.4M | ~–$382M | **2.7 yrs** |

**The critical finding: RKLB survives a 20% revenue decline without a solvency event.** Even in the severe case, $1.02B of cash funds ~2.7 years of operations at elevated burn, and the company retains the opex lever (Scenario B shows a 10% opex cut almost fully offsets a 20% revenue hit).

**What actually breaks in the downside is the equity, not the balance sheet.** At 61x EV/Sales, a 20% revenue miss would almost certainly compress the multiple to 25–30x — a **50–60% drawdown in market cap**, from ~$37.5B toward $15–18B. That cascades into:
- **Cost of capital shock:** with the stock down 55%, an equity raise that would have cost ~2% dilution now costs ~5%. The convertible market closes to a sub-$15B unprofitable issuer. This is the real refinancing cliff — it is *equity-market-dependent*, not maturity-schedule-dependent.
- **Interest coverage deteriorates** to roughly –10x in Scenario A, but cash interest of ~$26M against $1B of cash is trivially serviceable from the balance sheet.
- **Asset impairment risk:** $430.5M of goodwill and intangibles (25% of equity) is at risk of write-down if growth expectations reset — a non-cash but equity-damaging event.
- **Neutron funding:** capex of $156.3M/yr is the largest discretionary line. In a downturn, delaying Neutron extends the burn but destroys the growth narrative that justifies the multiple — a genuine no-win.

**Liquidity conclusion:** no debt maturity wall, no covenant trigger evident, no going-concern risk. **Liquidity risk: LOW.**

---

### 5. Overall Financial Risk Rating: **HIGH**

Not because Rocket Lab might fail — it very likely will not over a 2–3 year horizon. The rating is **High** because of a specific and unusual risk composition:

| Risk type | Rating | Rationale |
|---|---|---|
| **Credit risk** | **Low–Moderate** | Net cash $762.6M, D/E 0.15, no near-term maturities. Offset by negative EBITDA and no coverage. |
| **Liquidity risk** | **Low** | 4.08 current ratio, 3.0 cash ratio, 3.2-yr runway, $0 short-term debt. |
| **Market risk** | **Critical** | ~90% vol, beta 2.61, three 34–57% drawdowns in three years, 61x EV/Sales. |
| **Dilution risk** | **High** | Negative FCF for four straight years; shares +13.8% in 3 yrs; SBC $71.1M = 11.8% of revenue. |
| **FCF sustainability** | **High risk** | FCF worsened from –$116M to –$322M as capex nearly doubled. Gross margin improving, but EBITDA flat for three years. |

The distinguishing feature of RKLB's risk is that **its balance sheet is safe and its valuation is not**. An investor is not underwriting default risk; they are underwriting a 61x sales multiple on a company whose EBITDA has not moved in three years.

---

### 6. Key Red Flags

1. **EBITDA has been flat at ~–$150M for three consecutive years** (–$144.9M → –$151.8M → –$155.5M) while revenue nearly tripled. Gross margin improvement is being entirely consumed by opex growth. Scale is not producing operating leverage yet.

2. **Free cash flow is deteriorating, not improving:** –$116.0M (2024) → –$321.8M (2025), a 2.8x worsening. Capex rose from $67.1M to $156.3M. FCF margin of –53.5% means the company burns $0.54 for every $1 of revenue.

3. **Valuation is the dominant risk factor.** 62x trailing sales, 61x EV/Sales, 21.8x book, negative FCF yield. Any growth disappointment transmits almost mechanically into a 50%+ drawdown and a materially higher cost of capital.

4. **Heavy reliance on equity markets rather than internal cash generation.** The 2025 balance sheet transformation (cash $419M → $1,017M) came predominantly from capital raising, not operations. This is a structural dependency, not a one-off.

5. **Dilution is recurring and material:** Piotroski failure on F7; shares +13.8% over three years; SBC running at 11.8% of revenue. Per-share value creation is meaningfully lower than enterprise value creation.

6. **$430.5M of goodwill and intangibles** — 25% of book equity and 1.8x FY2025 gross profit — carry impairment risk in a growth reset.

### Data Gaps (explicitly flagged)
- **Volatility/beta tool unavailable** on current subscription; all volatility and drawdown figures computed manually from daily OHLC. Beta (2.61) is FMP-reported, unaudited here.
- **Altman Z-Score is not interpretable** for this company (book-equity x4 artifact); market-cap-adjusted Z is ~37. Do not use 1.61 as a distress signal.
- **Net debt figures conflict between tools:** balance sheet reports –$574.7M, leverage tool –$762.6M. The latter reconciles arithmetically ($254.0M debt – $1,016.6M cash) and is used throughout.
- **Debt maturity schedule, covenant terms, and revolver availability not obtainable** from available tools. Convertible principal ($355.0M, 4.25%) is sourced from a Sept-2025 10-Q and may not reflect year-end 2025.
- **No credit rating or CDS spread exists/available.**
- **Peer set is unusable:** the sector tool returned SpaceX, GE Aerospace, RTX, Caterpillar, GE Vernova, Deere — $180B–$1.9T cap industrial conglomerates. No valid comparables for a pre-profit launch provider; relative valuation is not assessable.
- Quarterly granularity not retrieved (budget constraint); runway estimated from annual FY2025 burn and may understate current-quarter intensity given the Neutron capex ramp.
