# Short Analyst

- Symbol: GMAB
- Elapsed: 100.5s

---
Data gathering complete (two SEC fetch attempts blocked — noted as gaps). Writing the analysis.

---

# GMAB (Genmab A/S) — Forensic Short-Seller Review
*Price ref: $35.67 (30-Sep-2026 ADR close) · ~614M shares · mkt cap ~$21.9bn · net debt $3.71bn · EV ~$25.6bn*
*(Vendor profile also carries $44.83 / $27.6bn — a later or stale mark. Both are used in sensitivity below.)*

## 1. Earnings Quality Assessment: **MEDIUM**

The accounting is clean. The *business* is not durable. Those are different things and the market is pricing the first as if it were the second.

- **Accruals ratio −0.017** (2025); −0.086 (2023); +0.052 (2022) — no accrual build.
- **Cash conversion 123% · FCF conversion 119%** — earnings are cash-backed.
- **Beneish M-Score −3.224 "low risk"** — but see §3, this score is invalid.
- **Receivables vs revenue: no channel-stuffing signal** (2024: AR +35.3% vs revenue +30.7%).

**Rating rationale:** no manipulation. But cash conversion of 123% is *structurally* flattered — DARZALEX royalties arrive from J&J as pure cash with zero COGS and zero working capital. A high cash-conversion ratio here measures the *form* of the revenue (a royalty coupon), not the *quality or durability* of it. That is the trap.

## 2. Key Red Flags

**R1 — Single-asset concentration with a dated, company-admitted cliff.** 2026 guidance: revenue ~$4.4bn, of which **DARZALEX royalties ~$2.83bn = 64%**. Genmab's own SEC filing states royalties "**will begin to decline materially in 2029 following expiration of our U.S. patent rights on daratumumab**." Street work puts royalties near zero by ~2032. Genmab does not control this asset — J&J does, and J&J also sells competing bispecifics that can cannibalise it.

**R2 — The non-DARZALEX business does not cover its own cost base.** 2025 derived R&D $1,560M + SG&A $602M = **~$2,163M opex**. 2026 "other" revenue (ex-DARZALEX) ≈ $4.4bn − $2.83bn = **$1.57bn**. Even at ~90% gross margin, the ex-DARZALEX enterprise runs roughly **−$0.8 to −$0.9bn at the EBITDA line**. Current-year GAAP profitability is *entirely* a function of one royalty line with a 2029 expiry.

**R3 — Balance sheet transformed by an $8bn debt-funded acquisition.** Goodwill + intangibles $9,456M = **74% of total assets**. Total equity $5,834M → **tangible book equity is NEGATIVE ~$3.6bn**. Total debt went from DKK 1,029M (~$0.15bn) to **$5,426M**; net cash of ~$1.2bn became **net debt $3.71bn**. Liabilities grew ~5.5x in one year.

**R4 — Interest is now eating operating profit.** Q1-26 interest expense **$112.4M**; Q2-26 **$110.2M** → ~$445M/yr on $5.4bn ≈ **8.2% blended cost of debt**. Q1-26 EBIT $226M vs interest $112M = **2.0x coverage**; Q2-26 3.7x. Q1-26 net income collapsed to **$53M on $899M revenue (5.9% net margin)** vs 26% for FY2025.

**R5 — Internally inconsistent capital allocation.** Buying back stock ($430M in 2025; DKK 564M in 2023) *while* issuing $5.5bn of ~8% debt to fund a 41%-premium all-cash deal for a pre-commercial asset. You do not simultaneously believe your equity is cheap and your debt is the right currency at 8%.

**R6 — Segment economics mean the cliff is a cliff, not a slope.** Because the royalty line carries ~100% incremental margin, losing it is not a 64% revenue problem — it is close to a 100% *profit* problem. Operating margin 34% (2025) rests on that line.

## 3. Beneish M-Score & Accruals — Why the Model Is Lying

**Beneish −3.224 ("low risk") is not usable. Discard the headline.**

GMAB switched reporting currency from DKK to USD in FY2025. The model compared USD 2025 line items against DKK 2024 line items, producing nonsense indices:

| Index | Value | Verdict |
|---|---|---|
| SGI | **0.173** | Impossible — implies revenue fell 83%. Pure DKK/USD unit artifact. |
| DSRI | **0.993** | Also unit-corrupted; cannot be read. |
| TATA | −0.017 | Real, benign. |
| **LVGI** | **2.743** | **Genuine and severe** — leverage genuinely ~2.7x'd. |
| **AQI** | **1.953** | **Genuine** — goodwill/intangible bloat + PP&E step-up. |
| DEPI | 3.009 | Mixed; deal-related asset step-up. |

Of the eight inputs, **three are destroyed by the currency switch** and the two that remain fully interpretable — leverage and asset quality — **deteriorated violently**. The "low risk" output is an artifact. This is itself an investable insight: the DKK→USD transition (defensible on its own terms — J&J, peers and debt are USD) has silently broken third-party forensic screens and consensus comparability across the whole Street.

**Accruals: clean.** Balance-sheet accruals −0.017; no income-inflating accrual build. Whatever else is wrong here, it is not accounting fabrication. I want to be explicit: **there is no fraud case against GMAB.**

**Piotroski F-Score: 4/9 (weak).** Failed: leverage (F5), equity change (F6, buybacks + deal), gross margin (F8), asset turnover (F9 — revenue/assets fell from ~0.47 to 0.29 on the goodwill bloat). Passed on profitability and accruals.

**Altman Z: 1.696 ("distress").** Be honest — this is partly a book-equity artifact. X4 uses book equity ($5.83bn) not market cap; substituting ~$21.9bn gives Z ≈ 3.07 (safe). **GMAB is not a solvency story.** It is a leverage-and-return-of-capital story.

**Data-integrity caveat:** income-statement net income and cash-flow-statement net income disagree for FY2021–2023 (e.g., FY2023: DKK 4,352M vs 5,637M). Almost certainly a vendor line-item mismatch, not a filing discrepancy — but it is a reason to distrust any screen that ingests these feeds unadjusted.

## 4. Competitive Threat Assessment

- **DARZALEX:** still compounding (+22% YoY to $4,207M in Q2-26), but US composition-of-matter runs off 2029 with biosimilar entry thereafter. Royalty *tiers step down*, so Genmab's royalty growth already lags underlying drug growth.
- **Kesimpta (ofatumumab, Novartis):** another partner-controlled royalty; MS franchise faces BTKi and next-gen competition.
- **Epkinly (epcoritamab):** crowded DLBCL/follicular space against CAR-T and J&J's own teclistamab; AbbVie partnership splits economics.
- **Merus / petosemtamab (the $8bn bet):** first-in-class EGFR×LGR5 in head & neck, but Phase 3, pre-revenue, and the entire impairment thesis on $9.5bn of intangibles rests on it. Genmab paid a 41% premium to consensus for the privilege.
- **Moat verdict: eroding by calendar.** The moat was never Genmab's — it was a patent estate licensed to a counterparty that controls commercial strategy.

## 5. Management & Governance Red Flags

- **Insider activity — unresolved gap.** Only 4 Form 4s on file, all clustered **18–30 Dec 2025**, immediately around the Merus close. The filing metadata does not expose direction, so I cannot assert net selling. Treat as an open question, not evidence.
- **Auditor changes:** no evidence obtainable in budget — gap.
- Management tone is promotional relative to the disclosed cliff: guidance *raised* ~460bp to $4.4bn in Q2-26 while the same documents concede material royalty decline from 2029. Both can be true, but the market is trading the raise and ignoring the calendar.
- Reporting-currency change mid-stream: legitimate, but it removed the clean comparable series exactly when comparability mattered most.

## 6. Short Thesis Summary — Is There a Credible Bear Case?

**Yes, and it is a valuation/durability case, not a fraud case.**

Rough NAV: after-tax PV of the DARZALEX royalty stream (2026–2032 run-off, 8% discount) ≈ **$9.5–11.4bn**. Against a market cap of **$21.9bn** ($27.6bn on the profile mark), the market is capitalising **$10–16bn** of value in an ex-DARZALEX enterprise that today generates ~$1.57bn of revenue against a ~$2.2–2.3bn cost base — i.e. **negative EBITDA** — plus an $8bn, 8%-coupon bet on a Phase 3 asset. Roughly *half to two-thirds of the equity value depends on pipeline assets that do not yet earn money.*

**The bull case, stated fairly (and it is currently winning):**
- DARZALEX is still growing 22%; 2026 guidance was *raised*.
- Consensus sees revenue $5.35bn (2027) → $6.65bn (2028) → $7.65bn (2030) and net income $1.07bn → $1.66bn → $1.94bn. At $35.67 that is **20.5x 2027E and 13.2x 2028E** — not an expensive multiple if the post-cliff franchise materialises.
- Earnings are genuinely cash-backed (123% conversion); there is no accounting fraud.
- The stock has nearly **doubled off the $17.98 April-2025 low** and sits at the top of its two-year range ($17.98–$35.91). Momentum, estimate revisions and the royalty tailwind are all against a short right now.
- The 2029 cliff is **disclosed, widely known, and therefore partly discounted.**

**Where I think consensus is wrong:** it is treating the 2027–2028 EPS ramp as the valuation anchor and treating 2030 revenue of $7.65bn as a base case rather than a *financing-dependent option*. The Street is also under-modelling that the debt taken on to buy the replacement asset consumes ~$445M/yr of the very cash flow it is meant to replace, at 8.2% — a negative carry that widens every year the pipeline slips.

**Timing is the weak point.** There is no near-term catalyst. The cliff bites in 2029; the Merus readouts are 2027+. This is a slow-burn short, not an event short, and it will bleed carry against a rising stock.

## 7. Contrarian Rating: **SHORT** *(structural / medium-term — not a near-term trade)*

**Conviction: medium.** No fraud, moat erosion rather than moat collapse, and a leveraged balance sheet that is uncomfortable rather than distressed.

**What would make me wrong (and I'd cover):** (a) petosemtamab Phase 3 data decisively beats in head & neck; (b) Epkinly establishes itself as a multi-billion franchise; (c) management refinances the 8.2% debt materially lower, removing the interest drag; (d) DARZALEX litigation extends US protection beyond 2029. Any of these converts a negative-carry story into a credible post-cliff franchise.

**What would make me add:** Q1-26-style quarters becoming the norm (net margin <10%), any goodwill impairment on the $9.5bn intangible base, clarity that net insider selling occurred around the Merus close, or 2027 consensus revenue starting to roll over while the stock holds its high.

**Practical expression:** small, longer-dated, and paired — long the royalty cash flow via a peer, short GMAB — rather than an outright directional short into a stock making two-year highs on raised guidance.

---

### Gaps & caveats (declared, not hidden)
- Two SEC fetches (20-F risk factors, Q1-26 interim report) returned 403/not-found; retried once, abandoned. Risk-factor language quoted is from Genmab's own SEC filing as surfaced via search, plus IR releases.
- Form 4 **direction** (buy vs sell) not available from the tool — insider conclusion left explicitly unresolved rather than asserted.
- FY2025 vs prior-year comparisons are unit-mixed (DKK→USD); where I quote growth I have normalised at ~7.0 DKK/USD and flagged it.
- `detect_revenue_deceleration` returned "accelerating" — an artifact of a corrupted Q1-25 revenue print ($105M). The underlying trend (2022 +72%, 2023 +13.6%, 2024 +30.7%, 2025 ~+22%, 2026E +18%) shows **no** clean deceleration. I have not used that output.
- No auditor-change or related-party data obtainable in budget.
