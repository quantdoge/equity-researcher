# Value Researcher

- Symbol: NBIS
- Elapsed: 46.4s

---
I have what I need. Writing the analysis.

---

# NEBIVS GROUP N.V. (NBIS) — Value Investment Analysis

**Price (Nov 20, 2026): $81.31** · Down ~72% from the June 2026 high of $286.69
**Market cap:** ~$24B (298M basic shares per Q3'26 10-Q; the $19.5B vendor snapshot uses a stale ~240M count) · **Net debt:** $8.65B · **EV ≈ $33B**

---

## 1. Business Quality Assessment — Moat Rating: **NONE** (nascent, unproven)

Nebius is a GPU-rental "neocloud." It buys NVIDIA silicon, builds data centers, and rents compute by the hour. That is the business.

**Moat test — it fails on every axis:**

| Moat source | Evidence |
|---|---|
| **Switching costs** | None. AI workloads are containerized and portable. Microsoft — Nebius's largest customer — signed a competing deal with Cerebras in 2026 while its $17.4–19.4B Nebius contract runs to 2031. That is a live demonstration of zero lock-in. |
| **Cost advantage** | Negative. Nebius pays the same NVIDIA prices as AWS/Azure/GCP and buys in far smaller volume. Revenue of ~$3B vs. hyperscaler cloud revenue in the tens of billions — no scale economy. |
| **Network effects** | None. |
| **Intangible assets** | ~$688M of goodwill/intangibles on a $38.7B balance sheet. The proprietary AI Cloud software stack is competent engineering, not a protected asset. |
| **Efficient scale** | The one *plausible* future moat: scarce power interconnects and European sovereign-AI positioning. Real, but unproven and replicable with capital. |

**The decisive evidence: ROIC was −6.4% in 2025, −12.1% in 2024, −7.4% in 2023.** A moated business earns returns above its cost of capital *consistently*. Nebius has never done so, and the −6.4% figure is *flattered* by a still-small depreciating asset base (see §2). The five-year moat trend is neither widening nor narrowing — the moat does not yet exist.

**Circle of competence:** I cannot underwrite the terminal economics of hourly GPU rental. The price of compute five years out is set by NVIDIA's roadmap, hyperscaler capex plans, and AI demand elasticity — none of which are knowable. This is the clearest "too hard" pile candidate I have reviewed this year.

---

## 2. Financial Quality Score: **3 / 10**

Growth is genuinely extraordinary. Everything below the revenue line is not.

| Metric | 2023 | 2024 | 2025 | TTM (Q3'26) |
|---|---|---|---|---|
| Revenue | $9.8M | $91.5M | $530M | **$2,190M** |
| Gross margin | −100% | 52% | 69% | **77.6%** (Q3) |
| Operating income | −$286M | −$400M | −$612M | **+$50M** (Q3) |
| Adj. EBITDA | — | — | — | **$466M, 47.5%** (Q3) |
| **Free cash flow** | +$746M* | −$562M | −$3,681M | **−$12,421M** |
| Capex | $83M | $808M | $4,066M | **$17,487M** |

*\*2023 FCF is a pre-spin legacy artifact (Yandex working capital), not operating cash generation.*

**Three findings that override the growth story:**

1. **Cash conversion is catastrophically negative.** TTM FCF of −$12.4B. Q3 2026 alone burned $7.57B. Owner earnings (NI + D&A − maintenance capex) were **−$3.57B in 2025**. The stated FCF/NI conversion standard of >80% is not merely missed; the metric is undefined.

2. **Depreciation is materially understated — the key accounting red flag.** TTM D&A is $1.07B against PP&E of $21.5B, an implied ~17-year life. GPUs have a 5–6 year economic life. As the $21.5B in service, D&A plausibly rises to $4B+/yr, which would collapse the entire EBITDA-to-EBIT bridge. Reported adjusted EBITDA is **not** a proxy for owner earnings here; it is a pre-obsolescence number for an asset class that obsolesces fastest.

3. **The balance sheet has been levered beyond recognition in nine months.** Total debt went from essentially zero (2024) to **$16.1B**; net debt from −$2.4B to +$8.65B. Shares outstanding rose from 251.8M to 298.0M (+18%) in three quarters. Interest expense reached $112.5M/quarter. With 2027 capex guided at **$40–45B** against $6.6B of consensus 2027 EBITDA, Nebius must raise roughly **$35B of external capital in a single year**. Equity holders here are option holders on the credit markets.

---

## 3. Valuation Analysis

**The standard tools do not work, and I will not pretend otherwise.**

- P/E of 246x is meaningless — 2025 net income was manufactured by non-operating gains (Q1'26 alone booked $621M of net income against a $128M operating *loss*).
- P/FCF of −5.5x: undefined.
- The DCF tool returns garbage by construction (it grows a negative FCF base).
- Owner earnings are negative. **There is no defensible intrinsic value from trailing financials.**

**Scenario valuation on forward economics** (EV $33B):

| Scenario | 2030 revenue | EBIT margin | NOPAT | Value @ 18–20x | PV @ 12% | vs. EV |
|---|---|---|---|---|---|---|
| **Bear** — AI capex peaks 2027, rental prices fall 30%, revenue plateaus $15B | $15B | 8% | $0.9B | ~$18B | ~$11B | **−67%** |
| **Base** — $25B revenue, 80% cash GM, opex 15%, D&A 48% of revenue (realistic GPU lives) | $25B | 17% | $3.2B | ~$61B | ~$39B | **+18%** |
| **Bull** — management target achieved, 2030 revenue $40B, 20% EBIT | $40B | 20% | $6.0B | ~$120B | ~$76B | **+130%** |

Even the *base* case — which accepts management's aggressive targets — yields ~$39B against a $33B EV. That is a **18% discount, below the 20–30% margin of safety I require, for a business with no moat, negative owner earnings, and a fat, leverage-amplified left tail.** The 72% drawdown has not created a bargain; it has converted a bubble into a fairly-valued speculation.

On consensus the stock *looks* cheap: 2.6x 2027E revenue and 5.0x 2027E EBITDA. That appearance is the trap. Capex of $40–45B in 2027 implies ~$8–12B of annual D&A arriving by 2028–29 against $13.6B of consensus 2028 EBITDA. **The EBITDA multiple is an illusion; the owner-earnings multiple is negative.**

---

## 4. Management Quality: **6 / 10**

**Strengths.** Arkady Volozh is a genuine founder-operator who built Yandex into one of Europe's best technology companies. He has real skin in the game and has executed the Russia exit and Nebius pivot with remarkable speed. Securing $40B+ of contracted backlog from Microsoft and Meta is an outstanding commercial achievement and evidence of credible technical execution. Q3 beat on both revenue ($981M vs. $907M) and adjusted EPS ($0.30 vs. −$0.72).

**Concerns.** Capital allocation is the whole game here, and the record is one data point long: **spending $40–45B in 2027 to generate $12–13B of revenue.** That is a 3.3x capex-to-revenue ratio — a bet that demand, pricing, and financing all cooperate simultaneously. Shareholders have absorbed 18% dilution in nine months with no buyback or dividend, appropriately, but with no demonstrated discipline at scale. Management also *trimmed* 2026 revenue guidance to $3.0–3.2B while *raising* capex to $27B — the market sold the stock 47% on that combination, and it was right to.

**Verdict on management:** honest, capable, and dangerously aggressive. I would back Volozh at a smaller balance sheet and a lower multiple. Not here.

---

## 5. Investment Verdict: **SELL / AVOID**

This is not a value investment by any definition I recognize:

- **No economic moat** — commodity compute, zero switching costs, Microsoft already diversifying away.
- **No positive owner earnings** — TTM FCF −$12.4B; D&A understated against a 5-year-life asset.
- **ROIC negative** and structurally so at current asset intensity.
- **No margin of safety** — base case implies ~18% upside, bear case ~67% downside, with equity subordinated to $16B of debt and a ~$35B annual financing requirement.
- **Outside the circle of competence** — terminal compute pricing is unforecastable.

A business that fails the moat test, fails the owner-earnings test, and trades at fair value on optimistic assumptions is a **pass**, not a buy. The +72% drawdown from $286 is a de-rating to a fair price, not to a discount.

**If I were forced to own it:** only as a small, explicitly speculative position sized as a venture bet (≤1% of capital), accepting total loss, and only below ~$55–60 (EV ~$25B, ~8–10x 2027E EBITDA with a financing cushion). That is not an investment; it is a call option, and I do not size positions as options.

---

## 6. Key Risks to the Value Thesis

**Risks that could prove me wrong (upside):**
- **$40B+ contracted backlog is real revenue.** Microsoft ($17.4–19.4B through 2031) and Meta provide visibility most growth companies lack. If 2027 revenue hits $13B at 47% EBITDA margins, $6.6B of EBITDA against a $33B EV is 5x — genuinely cheap.
- **Adjusted EBITDA margin of 47.5% already achieved** is far ahead of my model. If that holds at $25B+ revenue, my base case is too conservative.
- **Customer prepayments** reportedly fund much of 2027 capex, materially reducing dilution and financing risk.
- **European sovereign AI** could become a genuine narrow moat via scarce power and political preference.
- Consensus PTs remain $185–$304 (Baird $200, Rosenblatt $304), implying 2–4x upside.

**Risks that confirm the thesis (downside):**
- **Financing accident.** ~$35B of 2027 external capital against $12.3B of equity. A credit-market closure, a customer deferral, or a covenant breach impairs equity permanently.
- **GPU obsolescence.** NVIDIA's annual cadence compresses rental prices for prior generations. Today's 77% gross margin is today's; the depreciation is contractual.
- **Customer concentration and renegotiation.** Microsoft is simultaneously a customer, a competitor (Azure), and an investor in alternatives.
- **Dilution** — 18% in nine months extrapolates badly.
- **Cycle risk.** If AI infrastructure spending normalizes in 2028–29, Nebius is a capital-intensive, undifferentiated, levered provider arriving at the worst moment.

---

**Bottom line:** Nebius is a real company with real revenue, real customers, and a real founder. It is also a capital-intensity machine with no moat, negative owner earnings, and an unquantifiable intrinsic value. **Warren Buffett's rule applies exactly: if you cannot estimate intrinsic value, you cannot know whether you have a margin of safety — and so you do not buy.** Rating: **Avoid.**

*Data gaps noted: no cohort-level utilization or GPU rental-price disclosure; no peer multiples for neoclouds (CoreWeave, Lambda, Crusoe are absent from the sector list, which returns mega-cap Technology only); segment EBITDA not broken out. Cash-flow quarterly figures include customer-prepayment working-capital swings that distort Q1–Q2 2026 operating cash flow upward.*
