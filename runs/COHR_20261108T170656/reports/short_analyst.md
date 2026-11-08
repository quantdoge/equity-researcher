# Short Analyst

- Symbol: COHR
- Elapsed: 63.3s

---
I have enough to write. Note one data caveat I'll flag: the FY2026 `ppe_net` of $21.29B exceeds total assets of $18.30B, which corrupts the Beneish AQI/DEPI inputs — the M-score is directionally usable but not literally reliable.

---

# COHR — Forensic Short-Seller Analysis
**Price $192.81 | Market cap $37.97B | EV ~$40.4B | Beta 2.23 | FY26 rev $7.12B**

## 1. Earnings Quality Assessment — **LOW**

| Metric | FY2026 | FY2025 | FY2024 |
|---|---|---|---|
| Net income | $805.0M | $49.4M | -$156.2M |
| Operating cash flow | **$79.5M** | $633.6M | $545.7M |
| **Cash conversion (OCF/NI)** | **9.9%** | 1,283% | n/a |
| Capex | **-$1,110M** | -$441M | -$347M |
| **Free cash flow** | **-$1,031M** | $193M | $199M |
| Working-capital drag | **-$1,102M** | -$208M | +$104M |
| Accruals ratio | 0.0396 | -0.0392 | -0.0484 |
| Accruals / revenue | 10.2% | — | — |
| Composite quality score | **22/100** | — | — |

This is the central fact of the thesis. Coherent reported $805M of net income in FY2026 and generated **$79.5M of operating cash**. Roughly **$725M of the year's earnings were non-cash accruals**, overwhelmingly a working-capital build.

And it deteriorated further in **Q1 FY2027** (quarter ended 9/30/26, filed 11/4/26): net income **+$381.6M**, operating cash flow **-$92.7M**, capex **-$775.5M**, free cash flow **-$868.2M**, working-capital drag **-$643.5M in a single quarter**.

Cumulatively, Coherent has consumed roughly **$1.9B of free cash over the last five quarters**. That hole was plugged by Nvidia's $2.0B equity investment (equity rose $2.76B against $805M of net income in FY26).

**That is the circularity worth flagging:** the company's largest strategic customer funded the balance sheet that pays for the capacity build-out that serves that same customer's ecosystem. Vendor-financed demand is not the same as organic demand, and it is the oldest pattern in boom-cycle optical/telecom equipment (JDS Uniphase, Nortel, 2000-01).

Rating: **Low** — but *not* "Fraudulent Risk." Nothing here suggests misrepresentation; the burn is disclosed capex and working capital consistent with a genuine ramp. The problem is that the earnings are economically hollow, not fabricated.

## 2. Key Red Flags

1. **Inventory balloon.** $2.581B vs $1.438B (+79.5%) on revenue growth of 22.5%. Inventory days **211.7 vs 139.8 (+72 days)**. In fast-cycle optical transceivers (800G→1.6T transitions on ~2–3 year product lives), 212 days of stock is an obsolescence wager, not prudent buffer. Trend flagged **"rising."**
2. **Receivables outrunning revenue.** AR +31.7% vs revenue +22.5%; DSO 68.9 vs 64.1 days. Modest, but it is a formal red flag in the screen.
3. **Capex tripling against EBITDA.** FY26 capex $1.11B → Q1 FY27 alone $775M (~$3.1B annualised) versus FY27 consensus EBITDA of $3.25B. **Capex ≈ 100% of EBITDA.** FCF is structurally negative for as long as the expansion lasts.
4. **Share count dilution.** Basic weighted shares 154.8M → 177.3M (**+14.6% y/y**); diluted 195.4M (**+26%**). Plus $186M of annual stock comp (23% of net income). Piotroski F7 (no dilution) = **fail**.
5. **Accruals quality fails Piotroski F4.** Net income materially exceeds operating cash flow — the classic low-quality marker.
6. **Net income exceeding operating profit.** FY26 net income $805M against operating income $902M less $190M interest implies a meaningful non-operating/tax benefit is embedded in the "record" profit.
7. **Goodwill $7.26B (65% of equity)** from the II-VI/Coherent combination — a serial acquirer whose organic ROIC is still unproven.

## 3. Beneish M-Score and Accruals

**M-Score = -1.803** → "moderate risk / possible manipulator" band (−2.22 < −1.78 < threshold).

Component read, *with the caveat that PPE data in the feed is corrupted* (FY26 `ppe_net` $21.29B exceeds total assets $18.30B), so **AQI (−0.887) and DEPI (9.515) are artifacts and must be discarded**:

- **TATA = 0.0396** — the single most predictive Beneish variable, and it is positive and elevated. Consistent with the accruals story. *Reliable.*
- **SGI = 1.225** — 22.5% sales growth. Growth itself mechanically raises manipulation probability in the model; here it reflects real demand.
- **DSRI = 1.075** — receivables slightly outpacing sales. *Reliable.*
- **GMI = 0.944** (gross margin improving — argues *against* manipulation), **LVGI = 0.895** (leverage falling).

Net: the M-score is a **yellow flag, not a red one**, and it is inflated by growth rather than by evidence of manipulation. But TATA + DSRI + the cash conversion data all point the same direction. Earnings quality score of **22/100** is unambiguous.

## 4. Competitive Threat Assessment

**Against the bear case (intellectual honesty):** gross margin has *expanded* — 30.9% → 35.4% → **37.5%**. That is direct refutation of the "commoditising component maker" narrative and the strongest single bull datapoint. Revenue growth is *accelerating*: 17.3% → 17.5% → 20.6% → 33.7% → **49.9%** y/y. The deceleration screen returned **"accelerating."** Vertical integration in indium phosphide (InP) and EML lasers — the real bottleneck at 1.6T — is a genuine structural advantage, and Nvidia's equity stake is third-party validation of it.

**For the bear case:** the moat is a *capacity* moat with a limited half-life. InP capacity is being funded simultaneously by every competitor and by Coherent itself at $3B/yr — capacity that arrives in 2027-28 as supply, not scarcity. Revenue is concentrated in a handful of hyperscalers whose capex is a discretionary board decision, and Chinese vendors (Innolight, EOptolink) have consistently compressed transceiver margins one speed-generation behind the leading edge. Coherent sells into a boom whose *only* independent variable is hyperscaler capex; it has ~zero pricing power over the cycle even if it has some within it.

## 5. Management / Governance Red Flags

- **Insider activity: 30 Form 4s in nine months; ~14 open-market sales totalling ~$9.9M over six months, no disclosed open-market buys.** CFO sold 3,000 shares at $324; a director sold 2,200 shares at ~$268 (Sept 2026). All appear to be Rule 10b5-1 pre-planned sales — a weak signal individually. But **zero insider buying into a 56% drawdown** is itself informative.
- **Dilution and circular financing** as above — customer equity funding the P&L. Legitimate and disclosed, but it flatters the growth optics.
- No auditor-change or related-party flags surfaced in the data available.

## 6. Short Thesis Summary

**The bear case is credible, and it is a cash thesis — not a fraud thesis.**

Coherent has converted itself from a moderately cash-generative compounder (FY24-25 FCF ~$195M/yr on $5B revenue) into a **capital incinerator**: FY26 FCF −$1.03B, Q1 FY27 FCF −$868M, capex at ~100% of forward EBITDA, funded by customer equity and convertible dilution. Reported earnings are ~90% accrual. The balance sheet carries a $2.58B inventory position — 212 days — in a business with 2–3 year product lifecycles, which is precisely the asset that gets written down first when an optical cycle turns (see FY2023: Coherent was loss-making at −$259M as recently as two years ago, on revenue *lower* than FY24's).

**The trigger is not in doubt, only the date:** one quarter of hyperscaler capex caution produces (i) deceleration off a 50% comp, (ii) inventory writedowns against $2.6B of stock, (iii) severe negative operating leverage against a fab base just expanded at $3B/yr, (iv) forced continued dilution at a lower price. With beta 2.23 and a stock that has already shown it can fall 56% in five months ($440 → $170), downside torque is extreme.

**But the other side is strong and I will not understate it:** margins are expanding, growth is accelerating to +50%, guidance is for >60% growth with a first $4B quarter by FY2028, and consensus FY2028 EPS of $15.01 puts the stock at 12.8x. If Coherent delivers that, the current price is not expensive. The market has *already* de-rated the stock 56% from its June 2026 high — much of the multiple compression this thesis predicted has happened.

**Where the thesis wins:** even on consensus FY28 net income of ~$3.08B, if cash conversion normalises to only 50%, OCF is ~$1.5B against a capex run-rate that must be at least $2-3B to sustain that revenue. **The company cannot self-fund its own growth.** That means permanent dilution or permanent leverage — either of which caps the terminal multiple well below 13x, and 10-12x on haircut FY28 EPS of ~$9-11 (after a cycle) is $90-130, i.e. **30-55% downside**.

## 7. Contrarian Rating: **SHORT** (not Strong Short)

Rationale: the earnings-quality evidence is unambiguous — 22/100 quality score, 9.9% cash conversion, negative FCF, 212 inventory days, 15-26% annual dilution — and the capital intensity has crossed from "investment" into "cycle risk." That combination has historically preceded writedowns in optical equipment by 4-6 quarters.

I decline "Strong Short" for three reasons: **(a)** the accruals-driven cash burn is disclosed and fully explainable by a real, accelerating demand ramp — this is not a concealment case; **(b)** gross margin expansion and accelerating revenue directly contradict the moat-erosion leg of the thesis; **(c)** 56% of the de-rating has already occurred, so the risk/reward of initiating here is materially worse than it was at $400, and a beta-2.23 name with consensus estimates rising is a dangerous borrow.

**The bull case is stronger than the average short target's — but it is a bull case about the income statement, while the balance sheet and cash flow statement are quietly voting no.**

---
**Data gaps to note for the memo:** quarterly balance-sheet detail for Q1 FY2027 was unavailable (feed returned annual rows only); FY2026 PPE in the feed is corrupted ($21.3B > total assets), invalidating the AQI/DEPI Beneish components; no short-interest, borrow-cost, or peer-multiple data was retrievable within budget. Q1 FY2027 cash-flow rows were returned scaled ×1,000 — the figures above reflect the normalised (÷1,000) reading, consistent with adjacent quarters.
