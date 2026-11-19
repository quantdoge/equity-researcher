# Short Analyst

- Symbol: OKTA
- Elapsed: 49.3s

---
## Forensic Short-Seller Analysis — OKTA (Okta, Inc.)
**Price $194.02 | Mkt cap ~$34B | EV ~$31B | FY26 revenue $2.92B | FY ends Jan 31**

---

### 1. Earnings Quality Assessment — **MEDIUM** (not fraudulent; structured to flatter)

I went looking for fraud and did not find it. What I found is a company whose GAAP profitability inflection is thinner and more manufactured than the narrative suggests.

| Metric | FY24 | FY25 | FY26 | TTM Q2FY27 |
|---|---|---|---|---|
| Revenue | 2,263 | 2,610 | 2,919 | ~3,073 |
| GAAP op margin | -22.8% | -2.8% | 5.1% | 7.6% |
| SBC | 684 | 565 | 544 | ~560 |
| SBC % of revenue | 30.2% | 21.6% | 18.6% | ~18% |
| FCF | 488 | 730 | 863 | ~875 |
| **FCF ex-SBC** | **-196** | **165** | **319** | **~315** |

The headline is "Okta is now profitable, generating $863M of free cash flow." Economic reality: **FCF excluding stock compensation is ~$315M — 10.9% margin, not 29.6%.** SBC at 18.6% of revenue is not a rounding error; it is essentially the entire non-GAAP earnings base. Consensus FY28 non-GAAP EPS of $4.34 is roughly the same magnitude as annual per-share SBC (~$3.20). Management is effectively reporting compensation as a non-expense.

Two further quality tells in the FY26 profit:
- **~$110M of FY26's $259M pre-tax income was interest income** on the $2.5B cash pile, not operations. Roughly 40% of the first-ever GAAP profit came from the treasury portfolio.
- **Effective tax rate ~9%** (FY26: $24M tax on $259M). NOL and windfall benefits are masking the normalized rate. At a 21% rate, FY26 net income would be ~$205M, not $235M.

**Rating: Medium.** Cash is real, collections are real, and accruals are genuinely conservative. But the P&L is engineered to look better than the business.

---

### 2. Key Red Flags Found

1. **Cost of revenue declined in absolute dollars while revenue grew 11%.** Q2 FY27: CoR $164M vs $168M a year ago, revenue $805M vs $728M. Gross margin jumped ~270bp to 79.6% in a single quarter. No cloud infrastructure business — especially one now selling AI-inference-adjacent workloads — cuts hosting cost in absolute terms without mix shift, capitalization, or one-timers. This is the single most important thing on the tape and nobody is asking about it.
2. **D&A halved in one quarter:** $24M → $12M Q2 FY27, against $117M of net PP&E and $5.6B of intangibles. Half the operating-income beat ($107M vs $41M) is explained by a step-down in depreciation. Either assets fully depreciated (margin tailwind is temporary) or something was reclassified.
3. **Revenue growth has decelerated for five straight years:** +42.9% → +21.8% → +15.3% → +11.8% → ~10.6% latest quarter. Eight-quarter YoY series: 13.9% → 12.7% → 11.5% → 12.7% → 11.6% → 11.6% → 11.2% → 10.6%. The trend is a sawtooth lower.
4. **Goodwill $5.58B = 80% of equity and 57% of total assets.** Tangible equity is only ~$1.4B. Auth0 was bought for $6.5B in 2021; at 10% growth the DCF supporting that carrying value gets thinner every year. A $2B impairment would erase three years of retained earnings progress.
5. **The entire re-rating is narrative, not revenue.** The stock went $62.93 (Apr 2026) → $232.13 (Oct 9 2026), +269%, on an "AI agent identity" TAM story that contributes approximately zero revenue today.
6. **Net income ≠ operating profit:** ~29% of TTM pre-tax income is still non-operating interest.

**What I explicitly did NOT find:** no receivables inflation (AR +10.6% vs revenue +11.8%), no channel stuffing, no inventory issue (asset-light), no auditor change, no related-party red flags in the data.

---

### 3. Beneish M-Score and Accruals Analysis — **CLEAN**

| Test | Result | Read |
|---|---|---|
| Beneish M-Score (FY26) | **-2.65** | Below the -2.22 soft threshold and -1.78 hard threshold → low manipulation probability |
| DSRI | 0.989 | Receivables not outrunning sales |
| GMI | 0.987 | Gross margin *improving* (this is the one index that flags margin deterioration) |
| AQI | 1.010 | No aggressive asset capitalization signal |
| SGI | 1.118 | Modest growth, low manipulation incentive |
| TATA | -0.0668 | Negative total accruals — conservative |
| LVGI | 0.869 | Deleveraging |
| Accruals ratio (FY26) | **-0.0668** | Strongly negative = high quality |
| Cash conversion (OCF/NI) | **376%** | Distorted upward by SBC-depressed net income |
| Earnings quality score | 60/100 | Pulled down by FCF-conversion-vs-SBC, not by accounting games |

**Verdict: this is not Enron.** Okta converts revenue to cash reliably. Anyone shorting OKTA on an accounting-fraud thesis is wrong, and the negative accruals trend across four consecutive years (-0.097 → -0.068) is a real positive for the bull case.

---

### 4. Competitive Threat Assessment — **SEVERE, and under-appreciated**

- **Microsoft Entra ID is the structural problem.** Entra is bundled free-ish inside E3/E5, and any CIO already paying Microsoft gets SSO/MFA/Conditional Access at marginal cost. Okta's core SSO product is commoditised; its 4.6-star Gartner rating versus Microsoft's 4.4 is a preference, not a moat.
- **The growth has to come from adjacent, more crowded markets.** With SSO saturated, Okta's incremental revenue must come from Identity Governance (SailPoint, Saviynt), PAM/non-human identity (CyberArk — now Palo Alto, Delinea), and AI agent identity (Descope, WorkOS, Auth0 challengers, plus Microsoft again). Okta is a challenger, not the incumbent, in every one of those.
- **Pricing model exposure:** Okta's seat/headcount-based pricing means every corporate hiring freeze and every AI-driven headcount reduction is a revenue headwind, while AI agent identities (which is the bull thesis) are priced at a fraction of human seats.
- **Brand scar tissue:** the 2023 support-system breach remains a procurement objection in security-conscious enterprises. Okta is the identity vendor whose own identity was compromised.

---

### 5. Management Red Flags — **MODERATE**

- **Insider selling is heavy and clustered into strength.** CEO Todd McKinnon sold 140,307 shares (~$21.5M) between Dec 2025 and Sep 2026, including **48,822 shares for $9.45M on Sept 22, 2026** — within 13% of the all-time high. At least ten Form 4s were filed by multiple insiders between Sept 15–24, 2026, right as the stock went vertical. Executives sold into the AI narrative, not into the drawdown.
- **Mitigant (in fairness):** all sales are described as Rule 10b5-1 pre-arranged plans. This is programmatic compensation monetization, not opportunistic dumping. It is a sentiment signal, not evidence of insider knowledge. I would not weight it heavily.
- **Promotional framing:** "accelerating cRPO" and "AI agent identity market could surpass traditional IAM" is forward-looking language doing heavy lifting against 10.6% revenue growth. Watch the gap between RPO growth (+17%) and revenue growth (+11%) — if RPO growth is duration-driven or a handful of large deals, the backlog signal is illusory.
- **Positive governance note:** net cash position (~$2.4B cash vs $422M debt), debt paid down from $2.37B to $422M in two years, and a $73M buyback initiated. Capital allocation discipline has genuinely improved.

---

### 6. Short Thesis Summary — is there a credible bear case?

**Yes, but it is a valuation thesis, not a forensic one.**

The bear case: Okta is a 10–11% grower trading at ~10x EV/sales, ~45x FY28 consensus non-GAAP EPS, and ~98x FCF excluding SBC. Its GAAP operating margin of 7.6% is flattered by a one-quarter depreciation step-down and an absolute decline in cost of revenue that cannot persist. Strip out interest income and SBC, and the business earns roughly $315M of economic free cash flow on a $31B enterprise value — a 1.0% economic FCF yield. The AI-agent identity narrative that drove +269% off the April low has no revenue attached to it, and the CEO and at least nine other insiders sold into it. If growth prints 8% instead of 11% in FY28 — entirely plausible given five years of deceleration and Entra bundling — the multiple compresses toward 6–7x sales, implying **$115–135, or -30% to -40%**.

**The bull case is stronger than most bears admit, and I must say so:**
- **RPO +17% vs revenue +11%** is genuine backlog acceleration, and cRPO is described as accelerating. That is not what a company losing to Microsoft looks like.
- Gross margin is expanding, not contracting (69.5% FY22 → 77.4% FY26). Pricing power is holding.
- Beneish -2.65, negative accruals, receivables in line, cash conversion >100%. The accounting is clean.
- GAAP profitable, ~$2.4B net cash, FCF margin ~30%, Rule of 40 score of ~40. Deleveraged from $2.37B to $422M of debt in two years.
- Diluted share count has flattened (179.3M → 178.8M) and a buyback has begun — dilution is being addressed.
- **Timing risk is brutal:** the stock has already fallen 19% from $232 to $194 in four sessions. Shorting a freshly cracked momentum name into an earnings cycle with 17% RPO growth is how shorts get carried out.

---

### 7. Contrarian Rating: **NO EDGE** (reject the forensic short thesis)

**Reasoning:** I was hired to find fraud and manipulation. **There isn't any.** Beneish -2.65, accruals -0.067, receivables tracking revenue, and four years of improving cash conversion make OKTA one of the cleaner mid-cap software P&Ls I could construct a short against. The bear case that remains is a multiple-compression argument that was far better expressed at $232 (or $80) than at $194 after a 19% drawdown, and it is directly contradicted by RPO growing 17% against 11% revenue.

**Where I would change my mind, and what to monitor:**
1. **Cost of revenue resuming growth faster than revenue** in Q3 FY27 — if last quarter's absolute CoR decline was a one-timer, the margin story unwinds instantly. *This is the key tell.*
2. **RPO growth decelerating below 13%**, which would break the "backlog inflecting" pillar of the bull case.
3. **Depreciation normalizing** — if D&A snaps back to $24M/quarter, Q2's operating margin halves.
4. **A goodwill impairment or Auth0-related write-down** of any size.
5. Growth guided below 9% for FY28.

**If forced to express a view:** a small, tight-stopped **Short** is defensible purely as a mean-reversion trade against a 269% narrative-driven re-rating, with the thesis invalidated above ~$235. But it is a trade, not a forensic conviction short — and the accounting forensics argue for the long side. **Honest verdict: No Edge on fraud; the bear case has been largely de-risked by the fundamentals and mostly de-rated by nothing at all.**
