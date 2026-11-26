# Short Analyst

- Symbol: ASTS
- Elapsed: 85.7s

---
I have sufficient data. Writing the report.

---

# AST SPACEMOBILE (ASTS) — Forensic Short-Seller Analysis

**Price $26.02 | Market cap $10.66B | TTM revenue $142.9M | Net debt $1.32B | EV ≈ $11.98B**
**Chart: $133.09 peak (28-May-26) → $23.27 (20-Nov-26) = −82%. Already a worked short.**

---

## 1. Earnings Quality Assessment

**Rating: LOW (but *not* Fraudulent Risk)**

The distinction matters. I went looking for manipulation and largely did not find it. I found something different and in some ways more actionable: a business whose reported numbers are *honest but economically hollow*, where the gap between the narrative and the cash flow is structural rather than accounting-driven.

| Metric | Value | Read |
|---|---|---|
| Earnings Quality Score | **14 / 100** | Bottom decile |
| Cash conversion (OCF/NI) | **0.21** | Poor — but distorted by D&A-heavy asset base |
| Accruals ratio (2025) | −0.054 | **Negative = conservative** |
| Accruals ratio (2024) | −0.182 | **Negative = conservative** |
| Piotroski F-Score | 5 / 9 | Weak-moderate; fails positive ROA, positive OCF, dilution |
| Altman Z-Score | **0.605 — Distress zone** | x2 (retained earnings/TA) = −0.166; x3 (EBIT/TA) = −0.084 |

**The honest verdict on accounting:** accruals are *negative* in both 2024 and 2025, meaning reported losses are actually **worse** than cash earnings before investment. This is the opposite of a channel-stuffing or revenue-pulling-forward profile. ASTS is not Enron. Anyone shorting this on an accounting-fraud thesis is going to have a bad time — the 10-Q CEO certification I reviewed is clean, and there is no auditor-change or restatement signal I could find.

**What is genuinely broken is capital intensity and unit economics:**
- TTM operating cash flow: **−$249.5M**
- TTM capex: **−$1,549.9M**
- **TTM free cash flow: −$1,799.4M**
- Cash on hand: **$2,798.9M** → roughly **18 months of runway at the current burn rate**, before any further raises.

---

## 2. Key Red Flags Found

**Red Flag #1 — Revenue quality: DSO of 224 days.** This is the single most interesting number on the tape. Receivables rose from $37.7M (Dec-25) to $104.1M (Sep-26), while quarterly revenue was only $42.3M. Receivables now equal **73% of TTM revenue**. Days sales outstanding:

| Quarter | Receivables | Revenue | DSO |
|---|---|---|---|
| Dec-25 | $37.7M | $54.3M | 63 |
| Mar-26 | $27.5M | $14.7M | 171 |
| Jun-26 | $79.3M | $31.5M | 230 |
| Sep-26 | $104.1M | $42.3M | **224** |

A 3.5x expansion in collection period alongside a revenue inflection is textbook "revenue recognized, cash not collected." The benign explanation — carrier revenue-share settlements (AT&T, Verizon, Vodafone) and government milestone payments with long payment cycles — is plausible. But at 224 days, ASTS is *financing its customers*, and the "revenue acceleration" headline is partly a receivable on the balance sheet rather than money in the bank.

**Red Flag #2 — Inventory days tripled in one quarter.** $28.4M (Jun-26) → $79.0M (Sep-26), a 178% jump against a 34% revenue increase. Inventory days: 110 → **285**. For a satellite builder this is defensible (satellite components awaiting launch), but it is also *exactly* what demand weakness looks like in a normal company. It deserves watching: if the 2027 launch cadence slips again, this inventory ages and impairs.

**Red Flag #3 — Gross margin was negative 11 months ago and is still sub-scale.** Q4-25 COGS of $91.3M against $54.3M revenue produced a **−68% gross margin**, then "recovered" to 24.9% → 25.2% → 40.2% across 2026. The trajectory is genuine progress — but the volatility reveals that cost recognition is lumpy and that at 40% GM, this is a *worse* structural margin than a terrestrial telco, in a business that must fund $1.5B/yr of satellites.

**Red Flag #4 — The debt is compounding faster than the constellation.** Total debt: $2.24B (Dec-25) → **$4.12B** (Sep-26). That is roughly **$1.88B of new debt in nine months**, via a $1.0B convertible and a further $1.15B convertible (July 2026). Interest expense went from $2.65M (Q4-25) to **$30.34M** (Q3-26) — annualising to **~$121M**, or **85% of TTM revenue**.

**Red Flag #5 — Dilution is relentless.** Weighted average shares: 199.2M (Q4-24) → 300.1M (Q3-26), **+50.6% in seven quarters (~26% annualised)**. Piotroski F7 "no dilution" = **0**. And $4.12B of convertibles sits *behind* the 300M share count.

**Red Flag #6 — Stock comp is 130% of revenue.** TTM SBC: $186.3M against TTM revenue of $142.9M. Every "adjusted EBITDA" figure management presents is adding back a cost larger than the entire top line.

**Red Flag #7 — Altman Z of 0.605.** Negative EBIT/assets, negative retained earnings (−$1.39B), and $4.61B of liabilities against $2.16B of book equity. This is a structural distress reading that only the $10.66B market cap disguises.

---

## 3. Beneish M-Score and Accruals Analysis

**Beneish M-Score: 30.13 ("HIGH RISK — likely manipulator").**

**I do not believe this is a valid data point, and I will not lean on it.** The model has completely decomposed on a pre-scale growth company:

| Index | Value | Why it's invalid |
|---|---|---|
| SGI | **16.05** | Revenue grew 1,505% — pure base effect, not manipulation |
| GMI | **−24.97** | Prior-period gross margin near zero destroys the index |
| AQI | **82.29** | Asset quality inflated by genuinely new satellite assets |
| DEPI | 4.39 | D&A rose because assets were *actually bought* |
| SGAI | 0.04 | Fine |

Three of the eight inputs are outside any range the model was calibrated on. The one input that survives scrutiny is **TATA = −0.0539**, i.e. total accruals to total assets is *negative* — meaning earnings are **understated relative to cash flow**, a hallmark of a conservative, not aggressive, reporter.

**Conclusion: the M-Score is a false positive. Do not build a short on it.** The real accruals story is the receivable/inventory working-capital drain, which shows up in cash flow, not in accruals manipulation.

---

## 4. Competitive Threat Assessment

This is where the bear case is strongest and where I think the market is still under-appreciating the problem.

**The scale gap is not closeable on any relevant horizon:**

| | Constellation |
|---|---|
| SpaceX Starlink (active satellites) | **~9,821** |
| AST SpaceMobile | **~7** |

The 45-satellite deployment target was **pushed from late 2026 to early 2027** — and this is a company that has missed essentially every deployment milestone it has ever set. Even at 45-60 satellites, ASTS operates at roughly **0.5% of Starlink's orbital scale**.

**Three further competitive dynamics:**
1. **Commoditisation risk on the technology edge.** ASTS's original thesis was that its large-aperture BlueBird phased arrays delivered superior link budget to standard phones. Starlink's direct-to-cell iterative deployment is compressing that performance differential each quarter. The moat that justified the entire premium is being arbitraged away.
2. **Distribution dependency.** ASTS does not own customers. It sells wholesale to AT&T, Verizon, Vodafone, Rakuten — parties who can and will dual-source with Starlink. ASTS holds no pricing power in that relationship; the carriers do.
3. **Adoption is slower than narrative.** Scotiabank's Jan-2026 downgrade to Sell cited not just Starlink but *evidence of slow user adoption in the US and Japan*. That is a demand-side crack, which is worse than a supply-side one.

**Counterpoint, fairly stated:** the TAM is real, ASTS holds meaningful spectrum and patents, has FCC direct-to-device approval in hand, and the carrier partnerships create genuine strategic lock-in (Google and the carriers are both partners and shareholders). A 2027-2028 successful deployment is not science fiction.

---

## 5. Management & Governance Red Flags

- **Insider selling: persistent and one-directional.** I reviewed 40 consecutive Form 4 filings (Apr-2026 through Nov-2026). There are **zero open-market purchases** in the sample. Selling is heavily clustered — **12 filings on 18-19 Aug 2026 alone**, with large clusters in June and May 2026. Many will be 10b5-1 plans (the defense management will offer), but a 7-month, 40-filing window with no offsetting buys is a signal about where insiders perceive value.
- **Founder control.** Abel Avellan is simultaneously **Chairman and CEO** and is registered as a **10% owner**. Concentrated founder control in a SPAC-origin company with repeated timeline slippage is a structural governance concern — the board has limited practical ability to discipline the executive who *is* the story.
- **Litigation:** An active securities fraud class action alleges the company **"overstated the durability of AST's competitive position."** This is the exact allegation my own competitive analysis independently supports — that management guided investors to believe a moat that Starlink was already breaching. This is a narrative-integrity problem, not a numbers problem.
- **SPAC heritage** (New Providence, 2019/2021) historically correlates with promotional guidance and shareholder-unfriendly structures.

**Gap disclosure:** I was unable to retrieve the 10-K (no 10-K returned; only the 10-Q CEO certification and exhibit). I therefore **could not independently verify the related-party transaction note** — a material omission I am flagging rather than papering over. The SPAC provenance and founder-ownership structure make this the single most valuable item for a follow-up.

---

## 6. Short Thesis Summary — Is There a Credible Bear Case?

**Yes. But the easy money has been made, and the setup is now dangerous.**

**The core bear case, quantified:**

The company trades at **74.6x TTM revenue** (83.8x EV/revenue). Consensus — the *bulls'* own numbers — projects 2028 revenue of **$1.52B** and 2029 EBITDA of **$1.32B** (4 analysts). Now value that like the business it will actually be: a capital-intensive satellite operator.

- Iridium trades at roughly **6-7x EBITDA**. Grant ASTS a generous **8x** on 2029's $1.32B = **$10.6B EV**.
- Subtract net debt. Debt is already $4.12B and growth capex is $1.5B/yr; funding a 45→90 satellite constellation requires **several billion more**. Call it $5B net debt by 2029.
- **Implied equity value ≈ $5.6B → ~$14/share**, or **−47% from $26**.

The bear case does not require a catastrophe. It requires only that ASTS *succeeds on consensus* and gets valued like its peers. **Even the bull forecast, at a fair multiple, implies the stock is roughly half of today's price.** That is an unusually clean short argument.

Secondary bear supports:
- Debt compounding at $1.88B/9 months with interest now 85% of revenue.
- 26% annualised dilution mechanically capping per-share upside.
- Timeline slippage is habitual, and each slip costs another raise.
- 2030 estimates carry **1 analyst** — the long-dated "path to profitability" is essentially unaudited fiction.

**The other side — and it is substantial:**

**Short interest is 71.45M shares, or 23.15% of float** (13-Nov-26), up from 65.87M on 15-Oct. This is a *crowded* short in a $10.66B story stock with heavy retail ownership, a 2.85 beta, and a demonstrated capacity to run from $17 to $133 in under a year. The historical precedent is brutal: the stock rallied ~400% in 2025 *while* the fundamentals deteriorated. Squeeze mechanics here can inflict 50-100% losses on a short that is directionally correct.

Additionally: $2.8B of cash and $10.66B of market access to capital means **bankruptcy is not on the table** in the next three years. This is not a zero. D2D satellite connectivity is a real, large, strategically vital market with genuine government tailwinds.

---

## 7. Contrarian Rating

### **SHORT — but with strict risk discipline. Not a Strong Short.**

My rating is capped below "Strong Short" for reasons of position mechanics, not of thesis quality. The fundamentals are as bad as I can find in a $10B company: negative FCF of $1.8B, distended receivables, tripling inventory days, interest expense at 85% of revenue, 26% annual dilution, sub-scale gross margins, and a competitor with 1,400x the satellite count. The consensus bull forecast valued at peer multiples implies halving.

But a 23%-of-float short in a high-beta retail favourite that already fell 82% is a bad *trade* even when it's a good *thesis*. You are late and you are in crowded company.

**Recommendation:**
- **Direction: Short**, sized small (0.5-1.0% NAV risk budget, not a core position).
- **Entry discipline:** only on strength into the $35-45 zone or a launch-catalyst spike. Do **not** initiate at $26 in the hole.
- **Hard stop:** a close above ~$55 (the July-2026 breakdown level), which would invalidate the downtrend.
- **Catalyst path:** Q4-26/Q1-27 results, the next convertible raise (the most reliable bear catalyst — each raise has marked a local top), and 45-satellite launch slips into H2-27.
- **What would make me cover:** a Tier-1 carrier committing to a *minimum revenue guarantee* with a take-or-pay structure, gross margin sustainably >55% with DSO back under 90 days, or a funded constellation plan that does not require further equity.

**Bottom line: this is a structurally weak, aggressively-financed, sub-scale business with a shrinking moat and a habit of missing deadlines — not a fraud.** Short the valuation and the execution, not the accounting. And respect the squeeze.
