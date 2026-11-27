# Value Researcher

- Symbol: NTNX
- Elapsed: 120.6s

---
I have what I need. Two things were essential to get right: the trailing P/E of 9 is an accounting artifact, and the Nov 25 selloff has a specific cause. Writing the report now.

---

# Nutanix, Inc. (NTNX) — Value Investment Analysis
**Price: $46.30 (Nov 25, 2026) · Market cap $12.63B · EV ≈ $13.4B · FY ends July 31**

## 1. Business Quality Assessment

**Moat rating: NARROW**

Nutanix sells hyperconverged infrastructure (HCI) software — it collapses compute, storage, networking and virtualization into one software-defined stack running on commodity hardware. FY2026 revenue was $2.85B, ~87% gross margin, essentially all subscription. ~30,000 customers, $2.63B ARR, and a Gartner leader in HCI.

*Evidence for a moat:*
- **Switching costs (the real moat).** The platform runs mission-critical datacenter workloads. Rip-and-replace means re-architecting production infrastructure — a multi-quarter, career-risking project for a CIO. This is why gross margins sit at 87% and why retention, not acquisition, drives the model.
- **Cost advantage in the hypervisor.** AHV is bundled free against VMware's now-expensive vSphere licences. Post-Broadcom, this is a genuinely potent wedge.
- **Capital intensity: essentially zero.** Invested capital is *negative* (equity $703M + debt $1.52B − cash $2.36B ≈ −$140M). The business grows on customer prepayments. This is a structurally high-return model.

*Evidence the moat is thinner than the margin suggests:*
- **Net dollar-based retention has fallen to 105%.** Best-in-class infrastructure software expands at 115%+. At 105%, Nutanix has modest pricing power inside its installed base — customers are not meaningfully buying more each year.
- **Bookings fell 2% YoY in Q1 FY27** on ~410 new customers, with management citing delayed large deals and sales-account changes.
- Gross margin is a *software* fact, not a *moat* fact. Real competitive pressure shows up in opex and growth, and growth has decelerated every year: 17.9% (FY23) → 15.4% (FY24) → 18.1% (FY25) → 12.4% (FY26) → **12.3% guided for FY27**.

**Moat direction over five years: widened, but for a non-repeatable reason.** Broadcom's VMware licensing upheaval handed Nutanix a multi-year share gift. That windfall is largely banked; the -2% bookings print suggests the easy displacement phase is maturing. A moat that widens because a competitor mispriced its licences is not a durable moat — it is a harvest.

## 2. Financial Quality Score: **7 / 10**

| Metric | FY23 | FY24 | FY25 | FY26 | FY27E (guide) |
|---|---|---|---|---|---|
| Revenue ($M) | 1,863 | 2,149 | 2,538 | 2,854 | 3,180–3,230 |
| Gross margin | 82.2% | 84.9% | 86.8% | 86.8% | ~87% |
| GAAP op margin | (11.1)% | 0.4% | 6.8% | 9.8% | ~12% |
| Non-GAAP op margin | ~2% | ~13% | ~20% | ~22% | 24.5–25.5% |
| FCF ($M) | 207 | 598 | 750 | 841 | 875–975 |
| SBC ($M) | 312 | 334 | 352 | 358 | ~400 |

**Strengths:** five-year revenue CAGR of 15.4%; gross margin up 710bp in five years; FCF margin of 29.5%; net debt of only $741M against $2.36B cash — under 1x annual FCF; and buybacks exceeding SBC ($484M vs. $358M in FY26), so the share count is actually shrinking net of dilution.

**The two marks against it:**
1. **SBC is 12.5% of revenue.** FCF of $841M is struck after adding back $358M of stock compensation. Owner earnings — FCF less SBC — were ~$483M in FY26, not $841M.
2. **Cash taxes and working capital flatter current FCF.** FY26 GAAP net income of $1.507B included a **one-time $1,208M release of the valuation allowance on U.S. deferred tax assets**. Normalized net income was ~$299M. Nutanix has been consuming NOLs; cash taxes will rise structurally from here, and deferred-revenue growth is a working-capital tailwind that cannot run forever.

**Do not use the headline P/E.** The screen shows 8.97x. That is arithmetic on a tax windfall. Normalized FY26 EPS was ~$1.10 (46x), and FY27 non-GAAP EPS is ~$2.15–2.25 (~21x). The truth for an owner sits closer to 25x, as shown below.

## 3. Valuation Analysis

The DCF tool returned a garbage output (it parsed my WACC as 1000%), so I built the valuation by hand.

**Owner earnings base (FY27E):** FCF guide midpoint $925M − SBC ~$400M = **~$525M**. This is the cash genuinely available to shareholders after paying employees in the currency they are actually paid in.

**Two-stage DCF:** owner earnings growing 13%/12%/11%/10%/9% over years 1–5, tapering to a 4% terminal rate, discounted at 10% (beta 0.64, but I use a 10% hurdle regardless — a business with a departing CEO and 105% NDR does not get a 7% discount rate).

| | Value |
|---|---|
| PV of years 1–5 owner earnings | $2,745M |
| PV of terminal value | $9,514M |
| Enterprise value | $12,259M |
| Less net debt | ($741M) |
| **Equity value** | **$11,518M** |
| Shares (economic, ~285M) | **$40.40 / share** |

**Sensitivity:** 9% WACC → $49; 11% WACC → $34. **Intrinsic value range: $34–49, central estimate ~$42.**

Terminal value is 78% of the total — a long-duration asset where small assumption changes swing the answer widely. That is itself a reason to demand a discount, not to pay full price.

**Cross-check on multiples (FY27E, EV $13.4B):**

| Metric | NTNX | Comment |
|---|---|---|
| EV / Revenue | 4.2x | Reasonable for 87% GM, 12% growth |
| EV / FCF (reported) | 14.5x | Looks cheap — but ignores SBC |
| FCF yield | 7.3% | Flattered by SBC add-back |
| **EV / Owner earnings** | **~25x** | The honest number |
| P/E (normalized GAAP) | ~46x | SBC is real |
| P/E (non-GAAP) | ~21x | What the sell-side quotes |

**What growth is implied by $46.30?** Holding owner earnings in perpetuity at a constant rate, the price implies ~5.8% perpetual growth; on my two-stage model it implies roughly the guided 12–13% for five years, then 4% forever. In other words, **the market is already paying for the company to execute its plan.** There is no payment for error, for a botched CEO search, or for NDR drifting to 100%.

Sell-side targets ($62 BofA, $67 Piper, $70 Rosenblatt, $75 Needham, $100 Guggenheim) cluster 35–115% above the price. They are capitalizing non-GAAP numbers and, in most cases, applying 20–25x to a figure that excludes a $400M real cost. I do not accept that framing.

## 4. Management Quality Assessment

**Rajiv Ramaswami (CEO since 2020): a genuinely good operator, now leaving.** He completed the hardest transition in enterprise software — moving a perpetual-licence business to subscription — while taking gross margin from 79.7% to 86.8%, non-GAAP operating margin from ~1% to ~22%, and FCF from $18M to $841M. Capital allocation has been disciplined: **no empire-building M&A** (goodwill of just $187M on a $2.85B revenue base), ~$800M of buybacks over three years at reasonable prices, no dividend (correct — reinvestment returns exceed the payout).

**Two serious governance concerns:**
1. **A surprise exit with no named successor.** Ramaswami departs by April 30, 2027; the board has retained an external search firm. This is announced at the exact moment management is guiding a "significant" reinvestment in AI and agentic capabilities with *lower* margins. A strategy pivot without a jockey is precisely the situation Buffett warns against.
2. **The reinvestment is unquantified.** "Significant reinvestment" plus "bookings -2%" is a combination that deserves scepticism until there is evidence.

*Data gap:* I could not verify insider ownership or recent insider transactions within budget. That is a real omission for a management assessment and I flag it rather than assume it away.

## 5. Investment Verdict: **HOLD**

*(Not a buy at $46.30. Would become a BUY below ~$34; would be a SELL above ~$55.)*

This is a good business — real switching costs, 87% gross margins, negative invested capital, and $875–975M of guided FCF — that is **fairly priced, not cheaply priced**. My central intrinsic value estimate of ~$42 sits *below* the current $46.30. Buffett's rule is to require a 20–30% discount; here I am being asked to pay a 10% premium to intrinsic value for the privilege of owning an unresolved CEO search.

The 15% one-day drawdown looks dramatic (worst day in two years, 13.6M shares vs. 2.7M average) but it has taken the stock from *expensive* to *fair*, not from *fair* to *cheap*. A stock falling is not the same as a stock being mispriced. Note the 52-week range: $34.01–$75.98. The April 2026 low of $34.01 is almost precisely where a 25% margin of safety to my $42 estimate would begin.

A patient investor should put NTNX on the watchlist with a limit order in the low-to-mid $30s, and use the intervening months to see (a) who the board hires, and (b) whether the FY27 bookings decline is a timing artifact or the start of a deceleration trend.

## 6. Key Risks to the Value Thesis

1. **CEO vacuum + strategy pivot.** No successor named; a margin-compressing AI reinvestment begins under interim or brand-new leadership. Execution risk is elevated, and the outcome is unmodellable today.
2. **Growth deceleration / demand.** Bookings −2% YoY and NDR down to 105% are the two most important numbers in the quarter. If NDR breaks below 100%, the recurring-revenue compounding engine stalls and a 25x owner-earnings multiple is indefensible.
3. **VMware tailwind normalizing.** Broadcom has already extracted its price increases; VMware is stabilizing its installed base. The share-gain gift that drove FY24–FY26 outperformance is fading, which is precisely when the underlying 12% growth rate is exposed.
4. **SBC dilution (~$400M/yr, 12.5% of revenue).** Buybacks currently offset it at a cost of ~$484M/yr. If the stock falls, the same dollar buys more shares — helpful — but if buybacks are curtailed to fund reinvestment, per-share value leakage resumes.
5. **Tax normalization.** With the valuation allowance released, Nutanix will be a cash taxpayer at rising rates. FCF growth will lag operating-income growth for several years.
6. **Long-duration valuation risk.** 78% of intrinsic value sits in the terminal value. A 100bp rise in the discount rate takes fair value from ~$42 to ~$34; a 100bp fall takes it to ~$49. Position sizing should respect this.
7. **Competitive breadth.** Broadcom/VMware, Dell and HPE (who sell HCI on their own hardware), Microsoft Azure Stack HCI, and hyperscaler repatriation offers all press on the same buyer. Nutanix wins on software elegance, not on scale.

---

**Summary:** A narrow-moat, capital-light, cash-generative infrastructure software franchise trading at roughly 25x owner earnings and a ~10% premium to intrinsic value, with an unresolved CEO transition and decelerating net expansion. Quality: high. Price: fair, not cheap. **Hold; buy below $34.**
