# Short Analyst

- Symbol: CHTR
- Elapsed: 55.1s

---
I have enough. Two fetches returned junk (site nav, a 401(k) exhibit) — I'll note those as gaps rather than retry.

---

# CHTR — Forensic Short-Seller Workup

**Charter Communications | Price $111.49 (30-Oct-26), ~167M sh, mkt cap ~$18.6B, net debt ~$104B, EV ~$123B**

*Note: the profile feed quoted $138.39; that is stale. The $18.65B market cap it reports only reconciles to the $111.49 close on the post-Cox ~167M share count, so $111.49 is the live mark.*

---

## 1. Earnings Quality Assessment — **MEDIUM**

The headline quality scores are genuinely decent, and I want to be straight about that before I make the bear case.

| Metric | FY25 | Read |
|---|---|---|
| Accruals ratio | **−0.0719** | Negative accruals → conservative, cash-backed |
| Cash conversion (OCF/NI) | **3.22x** | Inflated by $8.7B D&A but real |
| FCF conversion (FCF/NI) | **0.886** | Below 1.0 — the weak link |
| Beneish M-Score | **−2.65** | "Low risk" — well inside threshold |
| Piotroski F | **7/9** | Fails F3 (ROA trend) and F9 (asset turnover) |

**This is not a fraud.** Accruals are negative, cash conversion is strong, and Beneish shows no manipulation signature. Anyone pitching CHTR as an accounting short is wrong. The deterioration here is *structural and honestly reported*, which is a harder — and in some ways less tradeable — problem.

Two genuine blemishes:

**(a) Gross margin "expansion" is a reclassification artifact, not pricing power.** FY23 COGS $33.34B / SG&A $8.77B → FY24 COGS $29.76B / SG&A $12.08B. Roughly $3.6B moved from COGS to SG&A. Reported gross margin jumped 38.9% → 45.5% on flat revenue. Piotroski awarded a point for it (F8=1). It's an artifact of line-item shuffling — and the 2022→2023 period shuffled the other direction. **Gross margin is not comparable across years for this company.** The clean metric is EBITDA margin, which has gone 38.3% → 38.7% → 38.0% → 38.9% → 38.7% (2021→2025): **five years, zero operating leverage.**

**(b) Income statement vs. cash flow net income disagree.** FY25 IS shows $4.987B; the cash flow statement shows $5.766B — a $779M gap (NCI/Liberty Broadband consolidation). Not sinister, but it means unadjusted NI-based ratios need care.

## 2. Key Red Flags Found

**1. Free cash flow has structurally halved, and capex is the cause.**

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Capex | $7.56B | $8.82B | $10.94B | $11.27B | **$11.66B** |
| Capex/Rev | 14.6% | 16.3% | 20.0% | 20.5% | **21.3%** |
| **FCF** | **$8.68B** | $6.10B | $3.49B | $3.16B | **$4.42B** |

Capex +54% in four years while revenue compounded **1.2%**. Charter is spending vastly more each year just to stand still. That is textbook unit-economic deterioration, and management is now cutting capex for cash-flow reasons rather than because the network build is finished — which borrows from future competitiveness.

**2. Receivables outgrew a shrinking top line — the single loudest flag.** Revenue **−0.56%** vs. accounts receivable **+18.82%** in FY25. DSO: 19.8 → 20.5 → **24.5 days**. Beneish DSRI 1.195 confirms it. Part of this is plausibly Spectrum Mobile handset installment receivables (legitimate, growing), but a ~20% jump in DSO against negative revenue growth is not something to wave away. *I could not read the XBRL receivables note — the 10-Q fetch returned an Exhibit 4.2 401(k) plan document instead of the financials. This is my biggest unresolved gap and I flag it as such rather than pretend to have closed it.*

**3. Revenue is now organically negative, and Q3 "acceleration" is M&A noise.** Quarterly YoY: +1.57% (Q4-24) → +0.41% → +0.59% → −0.89% → **−2.33% (Q4-25)** → −1.00% → −1.74% → **+9.14% (Q3-26)**. That last print is the Cox close on 20-Aug-26, not a turnaround. The screening tool labeled this trend "accelerating" — that is exactly the naive read a forensic analyst exists to correct. Strip Cox and the underlying trend is −1% to −2% and worsening.

**4. Balance sheet is levered to the eyeballs with a negative tangible book.** Goodwill + intangibles **$97.6B = 63% of total assets** against total equity of $20.5B → **tangible equity ≈ −$77B**. Current ratio **0.39** ($5.14B CA vs $13.31B CL). Retained earnings −$5.39B. **Altman Z = 0.602, deep distress zone** (book-equity based, so indicative — but even swapping in the $18.6B market cap barely moves it).

**5. They paid $34.5B for a business that was already shrinking.** Cox lost 103,000 broadband customers in Q2-26 *before* Charter owned it. Pro forma Q3-26 internet losses: **233,000** (77,000 legacy Charter). Charter's own Q1-26 loss was 120,000. The acquisition added scale, a declining subscriber base, and ~$12B of debt.

**6. The $35B buyback was the decade's real capital-allocation story — and it was value-destructive.** Repurchases: $15.43B (2021) + $10.28B (2022) + $3.22B (2023) + $1.21B (2024) + $5.13B (2025) = **$35.3B**, at average prices in the $300–500 range. Today the entire market cap is $18.6B. They spent nearly **1.9× the current market value of the company on their own stock** — and FY25's $5.13B buyback *exceeded* FCF of $4.42B, funded with debt. Share count fell 219.5M (2019) to 135.2M (2025), then the Cox deal and Liberty Broadband merger re-diluted to ~167M. **A six-year shrink-to-grow exercise, largely undone by M&A.**

**7. Interest is now the biggest single claim on cash.** Post-Cox: $109B principal, 5.3% cost of debt, **$5.8B annualized cash interest**, net leverage 3.93x — versus standalone FCF that never cleared $4.5B.

## 3. Beneish & Accruals Detail

M-Score **−2.65** — *low risk*, comfortably below both the −2.22 soft and −1.78 hard thresholds. Component indices: DSRI 1.195 (the one elevated flag — receivables), GMI 0.993, AQI 0.970, SGI 0.994, DEPI 1.065, SGAI 1.001, LVGI 0.998, TATA **−0.0719**. Only the receivables index is out of line, and it corroborates flag #2. Accruals were negative in all four years examined (−0.072, −0.062, −0.067, −0.068) — consistent, conservative, and the opposite of what an earnings-manipulation short needs.

**Verdict: the accounting is clean. The business is not.**

## 4. Competitive Threat Assessment — **Severe and structural**

- **Fixed wireless (T-Mobile, Verizon)** absorbed essentially the entire U.S. broadband net-add pool from 2022–2025. It's capacity-limited but it has permanently reset price expectations at the low end.
- **Fiber overbuild** — AT&T Fiber, Verizon/Frontier, Brightspeed, and municipals — is taking share in Charter's own footprint, where Charter has no fiber upgrade path short of more capex it is now cutting.
- **The convergence strategy is a rented moat.** Spectrum Mobile is a Verizon MVNO. It grows subscribers and reduces churn optics, but generates thin margins and builds no proprietary infrastructure advantage. It is a defensive bundling tool marketed as a growth engine.
- **Management has effectively conceded on retention.** The CEO publicly admitted the retention strategy was "too aggressive" (July 2026) — promotional pricing suppressed reported churn, and unwinding it means more churn now. That is an admission that prior subscriber metrics were flattered.
- Video is in terminal structural decline; wireline voice likewise.

## 5. Management Red Flags — **Moderate to Serious**

| Flag | Evidence |
|---|---|
| **Capital misallocation at scale** | $35.3B of buybacks 2021–25 at ~$400 avg vs $111 today |
| **Buyback funded with debt** | FY25 repurchases $5.13B vs FCF $4.42B |
| **Strategic reversal on leverage** | Target cut from 4.0–4.5x to **~3.5x** — *after* levering up for Cox |
| **Admitted aggressive retention** | CEO concession that churn was being bought |
| **Promotional language vs. delivery** | "$3B cost-cutting turnaround" and "new operating model" announced the same quarter as a $2.1B pro forma net loss |
| **Impairment already taken** | Q3-26 pro forma net loss $2.1–2.4B despite a $1.4B gain; write-down on a $97.6B goodwill balance that is 63% of assets |

**Insider activity — data gap, stated honestly:** I retrieved 30 Form 4 filing dates in 2026, clustered heavily around 21–24 Aug 2026 (immediately post-Cox). The available metadata gives **filing dates only, not transaction direction or size** — the filing URLs resolve to a generic EDGAR browse page. I cannot compute a net insider buy/sell, so I will not assert one. What I can say is that I see no evidence of *open-market insider buying* into an 87% drawdown, which, if confirmed, would be a mild negative — but it is unconfirmed and I treat it as unresolved.

## 6. Short Thesis Summary — is there a credible bear case?

**Yes, and it is structurally correct.** But it is also, by now, largely *told*.

**The bear case in one line:** Charter is a shrinking, capital-hungry, ex-monopoly utility with 63% of assets in goodwill, negative tangible equity, $5.8B of annual cash interest, and a dead buyback — where the equity is a thin 15% slice of a $123B enterprise value, so a 10% EBITDA decline destroys ~40%+ of equity value at a constant multiple. The FY26 consensus EPS of **$15.12 vs. $36.21 in FY25 (−58%)** is the market already marking the model.

**Why I will not pound the table on the short:**

1. **The stock is down ~87% from its ~$825 peak.** At ~4.6x EV/EBITDA it is the cheapest large-cap cable/telecom asset versus VZ ~7x, T ~7x, CMCSA ~6x, TMUS ~10x.
2. **The forensic case for fraud does not exist.** Beneish −2.65, negative accruals, strong cash conversion. This removes the most violent catalyst (restatement, SEC action).
3. **The earnings-estimate dispersion is a warning, not just a red flag.** FY28 EPS range **$26.40 to $93.55** — a 3.5× spread across analysts. When nobody knows, the stock is driven by flows and sentiment, not fundamentals — bad terrain for a fundamental short.
4. **The bull case is measurable and near-term.** Pro forma Q3-26 capex *fell* to $3.2B from $3.6B. If capex intensity normalizes from 21% toward 18% on a $26B+ EBITDA base, FCF inflects hard off a trough. Simultaneously, deleveraging toward 3.5x is a visible, dated equity-value unlock. On 6.6× leverage, that re-rating is violent *upward*.
5. **The squeeze setup is live.** The stock traded $160 → $102 → $111 within five months, with 13M-share volume spikes on 24-Apr and 12.6M on 29-Jun. Heavily shorted, high-beta-to-news, low float after years of buybacks. This is precisely where crowded shorts die.

**Where the bear case becomes compelling again (falsifiable triggers):**
- Q4-26 internet losses worse than 233k *pro forma*, i.e., legacy Charter + Cox combined deterioration
- Management quietly abandons or "extends the timeline" on the 3.5x leverage target
- A second goodwill impairment (the $97.6B balance is 63% of assets on a shrinking business — the Q3 charge was likely not the last)
- Capex guidance re-accelerates for DOCSIS 4.0 / fiber, breaking the FCF inflection thesis
- DSO keeps climbing (24.5 → 27+ days), confirming the receivables flag is collections, not mobile handsets

## 7. Contrarian Rating: **NO EDGE** (reject the outright short; bear case correct but fully discounted)

I want to be precise about what I'm saying. The **analytical** bear case is validated on every count except fraud: declining organic revenue, accelerating subscriber losses, a structurally higher capex burden, negative tangible equity, Altman distress, a broken buyback, and a $35B record of destroying shareholder capital. Charter in 2021 was an excellent short. **Charter at $111 in late 2026 is a broken business at a broken-business price.**

The honest short-seller's conclusion is that the edge has migrated — from shorting the equity outright to **shorting the credit and hedging the equity**. At 3.93x net leverage with $5.8B of cash interest against ~$4.4B of standalone FCF and a management team that just publicly cut its leverage target, the **bonds** carry the asymmetry, not the equity. The equity's downside requires an EBITDA collapse to be realized; the debt's downside requires only that the deleveraging promise slips.

**If forced to express a view on the stock:** I would not initiate a fresh outright short here. I would pair it — long VZ/T (higher multiple, lower leverage, actual FCF) against short CHTR — capturing the relative-decline thesis without carrying the squeeze risk of a 6.6×-levered stub trading at 4.6x trough-cycle EBITDA. **Re-establish the outright short only above ~6.5x EV/EBITDA or on
