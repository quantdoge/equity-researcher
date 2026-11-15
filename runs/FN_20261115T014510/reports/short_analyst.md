# Short Analyst

- Symbol: FN
- Elapsed: 114.4s

---
# Forensic Short-Seller Analysis — Fabrinet (FN)

**Price $327.98 · Market cap $11.71B · Net cash $314M · EV ~$11.40B · Data through Q1 FY2027 (qtr ended 9/25/26, filed 11/3/26)**

Note on context: FN is **down ~56% from its April 2026 peak of $748.89** and ~44% from the May high. This is not a crowded "peak-multiple" short anymore — the air has partly come out. My job here is to determine whether the *business quality* deterioration justifies further downside, and it does, though with important caveats.

---

## 1. Earnings Quality Assessment: **LOW** (not Fraudulent)

Composite quality score **41/100**. The reporting is not fraudulent in my judgement — the balance sheet is clean ($2.3M goodwill, no off-balance-sheet games, Altman Z 4.12) — but **reported earnings have materially decoupled from cash generation**, and three of the four levers driving margin expansion are non-repeatable.

| Metric | FY2024 | FY2025 | FY2026 | Q1 FY2027 | TTM |
|---|---|---|---|---|---|
| Cash conversion (OCF/NI) | 139% | 99% | **54%** | **21%** | **36%** |
| Free cash flow | +$365.6M | +$206.5M | **+$3.0M** | **–$137.4M** | **–$191.7M** |
| Accruals ratio | –5.0% | 0.2% | **+5.5%** | — | — |
| Gross margin | 12.35% | 12.09% | 11.99% | **11.79%** | — |
| SG&A % of revenue | 2.71% | 2.56% | 2.01% | **1.81%** | — |

**The central finding: FN has produced four consecutive quarters of negative free cash flow while reporting record profits.** Revenue is accelerating beautifully (+50.7% YoY in Q1 FY27) — and that is precisely the problem. Growth is consuming cash, not generating it.

---

## 2. Key Red Flags Found

**Red Flag #1 — The tax-rate illusion (the most underappreciated item).**
FY2026 net income of $473.0M was **102% of operating income** of $462.9M, implying an effective tax rate of roughly **zero**. Quarterly NI/OpInc: 99%, 98%, 108%, 103%. In Q1 FY2027 that ratio collapsed to **71%** — a ~29% tax rate. Consequence: **Q1 FY27 revenue grew +50.7% while net income grew only +11.3%** ($103.5M vs $93.0M). Fabrinet's Thai BOI tax holidays are expiring structurally; this is a permanent EPS headwind of roughly $1.40/share per 10 percentage points of tax rate on a $500M pre-tax base. Anyone modeling earnings off FY2024–26 net margin (10.2%) is over-earning by ~30%.

**Red Flag #2 — Depreciation wave not yet in the P&L.**
Capex: $47.5M (FY24) → $121.8M (FY25) → $253.7M (FY26) → **$158.7M in Q1 FY27 alone** (annualizing >$630M). TTM capex $367M, or 7.1% of sales. Yet D&A is only **$21.7M/quarter** — capex is running at **7.3x D&A**. Net PP&E rose 26% in a single quarter ($619M → $782M). Depreciation *must* step up hard as this capacity enters service. Every 100bp of gross margin is worth ~$66M of pre-tax income at a $6.6B revenue run-rate; a doubling of D&A to $43M/qtr alone is ~150bp. Beneish **DEPI of 1.221** independently confirms the falling depreciation rate.

**Red Flag #3 — Inventory building faster than revenue.**
Inventory days: 66.9 (FY24) → 70.5 (FY25) → **91.3 (FY26)** → 83.7 (Q1 FY27). Inventory dollars grew **+65% YoY** in Q1 FY27 ($722M → $1,193M) against revenue growth of +50.7%. Some of this is legitimate ramp-prefunding for a 50%-growth business, but ~25% higher inventory days than FY24 is a demand-quality question, and it is a direct cash cost.

**Red Flag #4 — Unexplained ~$62M non-operating income in Q4 FY26 that reversed.**
FY2026 "EBIT" of $555.2M exceeds operating income of $462.9M by $92M — with $61.9M of that landing in Q4 alone. In Q1 FY27 the gap flipped to **–$16.3M**. That is a ~$78M swing in other income, roughly 13% of FY26 net income. Most plausibly Thai baht FX and interest income. FX is a real, ongoing margin exposure given the Thailand cost base — not a one-off.

**Red Flag #5 — $116M jump in non-current "other assets."**
Non-current non-PP&E assets went from $16.2M to $132.2M in FY26. This is what drives the Beneish AQI of 5.91. I cannot identify the composition from available data — **this needs a look at the 10-K notes.** It is not evidence of malfeasance, but a 7x jump in an opaque asset bucket is exactly the line item I want explained.

**Red Flag #6 — Cash has declined four straight quarters** from $968.8M to $755.8M (–22%) despite $473M of reported FY26 net income. FN also took on its first meaningful debt in years ($4.0M → $78.3M) — immaterial in size, but a directional signal.

**Red Flag #7 — Buyback collapsed to nearly zero.** $125.7M (FY25) → $5.2M (FY26). Management stopped buying its own stock just as it fell 50%. Weak conviction signal on capital allocation.

**Confirmed: severe customer concentration.** Cisco, NVIDIA, Nokia and Amazon together accounted for **~58% of FY2026 revenue**; NVIDIA is the largest customer. This is the single most important fact in the file.

---

## 3. Beneish M-Score & Accruals Analysis

**M-Score: +0.059** — nominally "HIGH RISK — likely manipulator."

I will not overclaim here. **Decomposing the score, roughly half the signal is a growth artefact, and I want to be honest about that:**

| Index | Value | My read |
|---|---|---|
| DSRI | 0.988 | **Clean** — receivables are *not* outrunning revenue. This is the big manipulation tell, and it's absent. |
| GMI | 1.008 | Slight gross-margin deterioration. Real. |
| AQI | 5.914 | **Artefact** — driven by a spike off a 0.6% base, but worth investigating (see #5) |
| SGI | 1.357 | **Artefact** — this is genuine 36% growth. Beneish systematically false-positives on hyper-growth. |
| DEPI | 1.221 | **Genuine flag** — depreciation rate falling |
| SGAI | 0.788 | **Genuine flag** — SG&A intensity collapsed |
| LVGI | 1.241 | Trivial (leverage from a near-zero base) |
| TATA | 0.0553 | **Genuine flag** — high total accruals to assets |

**Verdict: not a fraud signal.** Removals of AQI and SGI put FN comfortably in normal territory. But the trio that remains — high accruals (TATA 5.53%), falling depreciation rate (DEPI 1.22), and collapsing SG&A intensity (SGAI 0.79) — describes precisely the mechanism by which this company has manufactured operating-margin expansion (9.49% → 9.97%) on *falling gross margins* (12.09% → 11.99%). **Margin expansion is coming from cost deferral and opex leverage, not from pricing power or value capture.**

---

## 4. Competitive Threat Assessment: **Structurally Weak Moat**

Gross margin has declined in **every one of the last four fiscal years** — 12.71% → 12.35% → 12.09% → 11.99% → 11.79%. That is the clearest possible statement of zero pricing power. FN is a contract manufacturer renting out Thai factory capacity; the value capture sits with NVIDIA, Cisco and the transceiver vendors, not FN.

- **Customer concentration is the moat's inverse.** With 58% of revenue in four customers, FN has no negotiating leverage on price. Each customer is fully capable of dual-sourcing or in-sourcing.
- **Co-packaged optics (CPO) is the structural existential risk.** FN's core datacom franchise is pluggable optical transceivers. Every major AI networking roadmap trends toward co-packaged/on-board optics, which compresses the pluggable module TAM over a multi-year horizon. FN is a component assembler in a market where the architecture is being redefined by its single largest customer.
- **The Aug 18, 2026 reaction is diagnostic.** FN **beat every estimate** — non-GAAP EPS $4.10 vs $3.81 consensus, record $1.316B revenue, above guidance — and the stock still fell ~19% over two sessions on 3.2M shares. The market punished non-GAAP gross margin slipping 30bp to 12.2% and a capex surge. **This is the market beginning to price "growth without margin"; that re-rating has room to run.**

---

## 5. Management Red Flags

- **Dense Form 4 clusters**: 17 filings across four different filing agents between Aug 13 and Sep 3, 2026, plus a five-filing cluster on Dec 12, 2025. The Aug cluster lands immediately adjacent to the Aug 18 earnings collapse. **Direction unconfirmed** — the tool returns filing metadata, not transaction direction — so I flag this as *unresolved* rather than as a proven insider-selling signal. It is worth confirming directly.
- **Guidance/GAAP gap widening**: Q1 FY2027 GAAP diluted EPS was **$2.86**; the Q2 FY2027 non-GAAP guide is **$4.77–$4.92** — a 67–72% sequential jump. Reconciling that requires either a near-doubling of revenue QoQ or a non-GAAP definition that excludes the tax normalization. Either explanation is an earnings-quality problem, and I could not obtain the non-GAAP reconciliation to settle it. **This is the largest unresolved item in my file.**
- No related-party transactions, no auditor changes, no restatements found. Language is measured, not promotional.

---

## 6. Short Thesis Summary

**There is a credible, differentiated bear case — and it is a cash-flow and consensus-math case, not a fraud case.**

**The thesis:** The market is valuing FN on non-GAAP EPS that requires margins FN has never earned and cannot earn.
- TTM GAAP EPS ≈ $13.34 → **24.6x**; EV/Sales 2.2x. On **TTM free cash flow of –$192M, the multiple is undefined.** EV/FCF on FY26's $3.0M is ~3,800x.
- Consensus FY2027 EPS of **$19.71** on revenue of $6.59B implies a **10.8% net margin** — versus **7.0% actually delivered in Q1 FY27** and a full-year tax rate that has already normalized to ~29%. At current 11.8% gross margin, $6.6B of revenue yields roughly **$12.70** of EPS, not $19.71. **The forward "16.6x" is really ~26x on run-rate economics.** Note: I flag that the consensus data feed is internally inconsistent (net income $712M vs EBITDA $863M), so treat the precise figures with caution — but the *direction* of the gap is corroborated by the GAAP-to-non-GAAP spread in company guidance itself.
- Meanwhile the true earnings headwinds are: (a) tax rate +29pp, (b) depreciation normalizing from 7x under-earned, (c) SG&A already at 1.81% of sales with nowhere left to go, (d) gross margin eroding ~25bp/yr, (e) an inventory+capex cash sink.
- Catalysts: Q2 FY27 print (first test of the $4.77–$4.92 guide), any NVIDIA program share loss or CPO roadmap announcement, further gross-margin slippage, and continued negative FCF requiring the first real debt raise.

**The other side — and it is genuinely strong:**
1. **Revenue is accelerating, not decelerating** (+50.7%, four straight quarters of acceleration). This kills the classic "deceleration short."
2. **Balance sheet is pristine**: $756M cash, $314M net cash, Altman Z 4.12 "Safe," $2.3M goodwill, Piotroski 5. There is no solvency trade here.
3. **The cash burn is discretionary growth capex**, not operational deterioration. Capex is $367M TTM on $5.1B of revenue. If management simply stopped building, FCF turns positive immediately. Shorting a company that is voluntarily investing itself into negative FCF is a well-known way to lose money.
4. **DSO is improving** (72 days vs 80) — receivables growth is *not* outrunning revenue. The channel-stuffing tell is absent, and that materially lowers my fraud conviction.
5. **Beneish M-score is largely a false positive** on growth (SGI) and a small-base asset bucket (AQI). I will not dress it up as more than it is.
6. FN has a genuine, hard-to-replicate role as the leading independent optical packaging house with 21,500 employees in Thailand — a real asset in a supply chain diversifying away from China.

---

## 7. Contrarian Rating: **SHORT** (moderate conviction — not a Strong Short, and emphatically not a fraud short)

The bear case is real and quantitative, but the setup is not the clean kill a Strong Short requires. Three things cap my conviction: an accelerating top line, a net-cash balance sheet with no solvency risk, and a stock that has already surrendered 56% from its high — much of the multiple compression I would be shorting has occurred.

What keeps me short rather than neutral is the **consensus math**: FY2027 EPS expectations sit ~55% above what the current gross margin structure and a normalized tax rate can produce, and the company itself is now guiding to a non-GAAP number nearly 70% above its GAAP run-rate. Combine that with four quarters of negative free cash flow, a depreciation wave that has not yet hit the income statement, 58% customer concentration, and a 25bp/yr gross-margin bleed in a business whose architecture (pluggable optics) is being redesigned by its largest customer — and the risk/reward on the equity remains skewed down. **I would size this modestly and pair it against the optical complex rather than run it naked.**

**Monitoring triggers that would flip me long:** gross margin stabilizing above 12.5%, FCF turning positive for two consecutive quarters, non-GAAP-to-GAAP reconciliation showing a durable low tax rate, or evidence that FN is winning CPO-era packaging content.

**Data gaps I could not close:** 10-K risk factors and customer-concentration notes (the filing tool returned no 10-K); insider transaction *direction*; and the non-GAAP tax reconciliation behind the Q2 FY27 guide. Each of these could materially move the thesis — the tax reconciliation most of all.
