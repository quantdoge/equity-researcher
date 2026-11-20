# Short Analyst

- Symbol: AMD
- Elapsed: 78.7s

---
## FORENSIC SHORT ANALYSIS — ADVANCED MICRO DEVICES (AMD)

**Price $534.06 (13-Nov-2026) | Mkt cap ≈$880B | TTM rev $45.4B | TTM EPS $4.60 | P/E 116x | Beta 2.49**

---

### 1. Earnings Quality Assessment: **HIGH**

I went looking for a fraud and did not find one. The accounting is clean by every standard test I ran. Reported FY2025 (ended 27-Dec-2025):

| Test | Result | Read |
|---|---|---|
| Beneish M-Score | **−2.761** | Low risk (threshold −1.78) |
| Accruals ratio | **−4.4%** | Negative accruals = cash-backed earnings |
| OCF / Net income | **1.78x** | Exceptional |
| FCF / Net income | **1.55x** | Exceptional |
| Piotroski F-Score | **8/9** | Only leverage fails |
| Altman Z | **3.74** | Safe (net cash position) |
| Composite quality | 46/100 | The one dissonant reading |

Revenue quality *improved* markedly: DSO fell from 98 days (FY24) to **67 days** (FY25), and receivables actually **declined 8.9%** while revenue rose 34.3%. That is the opposite of channel stuffing. The FY23/FY24 red flags (AR +30% on −4% revenue) have resolved.

**Verdict: this is not an accounting short.** Anyone pitching AMD as a fraud story is wrong and will lose money. The composite 46/100 looks like a scaling artifact — every underlying cash metric is elite.

---

### 2. Key Red Flags Found

**Red Flag #1 — The OpenAI warrant: revenue purchased with equity (material).**
AMD issued OpenAI a warrant for **up to 160 million shares at $0.01** — roughly **10% of the company**, vesting on GPU purchase milestones against a 6 GW commitment. At today's price that is **~$85 billion of consideration** — nearly **2x TTM revenue** and **11x TTM net income** — handed to a single customer to induce purchases.

This is vendor financing wearing a new costume. It is structurally similar to Lucent/Nortel's customer loans in 1999-2001, except the currency is equity rather than debt, so it bypasses the income statement. If booked as consideration payable to a customer under ASC 606, the warrant's fair value must be recorded as a **contra-revenue** charge over the supply period — meaning headline revenue growth in FY27-28 may be materially overstated relative to economic reality, and the charge may be excluded from the non-GAAP EPS that the sell-side is capitalising. **This is the accounting event to watch in the next two 10-Ks.**

**Red Flag #2 — ~10% dilution that buybacks cannot offset.**
AMD repurchased $1.32B in FY25 (~2.5M shares at current prices). Offsetting 160M warrant shares at that pace takes **~60 years**. SBC of $1.64B (4.7% of revenue, **38% of net income**) is already being neutralised by buybacks; the warrant is a permanent, unhedged claim on ~10% of future earnings.

**Red Flag #3 — Inventory days: 106 → 130 → 160 → 165.**
Inventory is up 38% ($5.73B → $7.92B) and days outstanding have risen ~56% in three years. On TTM COGS the figure moderates to ~138 days, but **this exact pattern preceded AMD's 2022-23 collapse** (160 days into a PC air-pocket; the stock fell 66% from $160 to $55). Management is building inventory into an AI ramp that depends on one counterparty's financing.

**Red Flag #4 — Estimate dispersion is a confession.**
FY2028 revenue consensus is $137.2B — but the range is **$106.7B to $207.2B**. A ~2x spread on a two-year-out number is not a forecast; it is an admission that nobody knows. Consensus requires revenue to reach ~$243B by FY2030 — **5.3x TTM**, implying ~52% CAGR.

**Red Flag #5 — Insider filing cluster at the high.**
**25 Form 4 filings in six weeks**, including **13 in the week of 17-Nov-2026**, clustered at $534-585 — just off the $658 all-time high. *Honest limitation: the filing feed returned dates only, not transaction direction. I cannot confirm these are sales, and RSU vesting looks identical in the metadata. Flagged for verification, not asserted as a conclusion.*

**Red Flag #6 — Goodwill is 54% of assets.** $41.8B of goodwill/intangibles (mostly Xilinx) against tangible equity of **$21.2B**. AMD trades at **41x tangible book**. Impairment risk is live if the Embedded/Client cycle rolls over.

---

### 3. Beneish & Accruals — Detail

The only elevated Beneish sub-index is **SGI 1.343** (sales growth index), which flags manipulation risk in high-growth companies as a statistical artifact. The forensic indices that matter point the other way: **DSRI 0.678** (receivables falling relative to sales — the opposite of channel stuffing) and **TATA −0.044** (negative total accruals). GMI 0.997 shows gross margin essentially flat-to-up.

One genuine blemish: **FY2025 operating cash flow of $7.71B absorbed a $2.38B working-capital outflow**. Ex-working-capital OCF would have been ~$10.1B. Cash conversion looks perfect today but is being flattered by payables and the inventory build — it mean-reverts if growth decelerates.

---

### 4. Competitive Threat Assessment

- **Gross margin is expanding, not contracting**: 46.1% (FY23) → 49.4% (FY24) → 49.5% (FY25) → **~53.7% TTM**. Pricing power is intact. Any short thesis built on margin erosion is currently wrong.
- **The real moat problem is direction of travel**: AMD is the *challenger*, not the incumbent. Nvidia's CUDA software ecosystem remains the switching cost that keeps AMD's share of AI accelerators well below its silicon capability. ROCm is the entire bull case and it is a software problem, not a fab problem.
- **Single-point foundry dependency**: leading-edge wafers come from TSMC. AMD has no manufacturing hedge and no pricing power over its most critical input.
- **Customer concentration is now existential, not diversified**: the growth algorithm rests on OpenAI — a loss-making counterparty dependent on external capital to fund its own commitments. AMD has already paid it ~$85B in equity *before* collecting the revenue. That is a circular financing loop, and circular loops are what bubble peaks look like.

---

### 5. Management Red Flags

Lisa Su's team is not promotional in the way frauds are — guidance has been met, and the SOX 302 certification in the 4-Nov-2026 10-Q is unqualified. But two governance concerns stand out: (a) the willingness to pay ~10% of the company to a customer to secure revenue is an aggressive use of the balance sheet that boards typically resist until cycles get late; and (b) the warrant structure means management's growth targets and shareholder dilution are now linked to a third party's capital-raising ability. **No auditor changes or related-party self-dealing found.**

---

### 6. Short Thesis Summary — Is There a Credible Bear Case?

**Yes, but it is a valuation-and-structure short, not a fraud short.**

The arithmetic: sub-1% FCF yield ($6.7B FCF on $880B cap), 116x TTM earnings, 41x tangible book. The bull case requires executing a 5.3x revenue ramp to $243B by 2030 with near-perfect conversion. Consensus FY2028 EPS of $26.38 gives a 20x forward multiple — meaning **the entire 116x trailing multiple is a bet that 2028 estimates are met**.

**Bear scenario:** AI capex digests; FY2028 revenue lands at the *low* end of the analyst range ($106.7B) on an 18% net margin → EPS ~$11.50 → 25-30x = **$290-345/share, −35% to −46%**. A harsher outcome ($80B revenue, 15% margin, $7.20 EPS, 25x) = **~$180, −66%**.

**Bull scenario (and it is currently winning):** FY2028 revenue at the *high* end ($207B), 25% net margin → EPS ~$31 → 35x = **~$1,085, +103%**. Revenue is accelerating (YoY +34.1% → +37.9% → +50.1% → **+44.7%**), gross margin is expanding, and the OpenAI deal provides multi-year volume visibility. Structurally, AMD has already round-tripped **−39% in a month** (peak $658.52 on 6-Oct → $402.10 on 5-Nov) and then rebounded **+45%** in five sessions. That is a tape that gorges and purges on narrative, not fundamentals.

**Where I give ground:** there is no accounting manipulation, no balance-sheet stress ($10.5B cash, $4.5B debt), no margin deterioration and no decelerating revenue. Every "quality" short signal I own says stand down.

**Where I press:** the ~$85B equity-for-revenue payment is a genuine, under-modelled transfer of shareholder value to a single customer, and it will show up as either contra-revenue or dilution — not as a line the sell-side currently models. Combined with 165 inventory days into a one-counterparty ramp, the downside when the AI capex narrative cracks is far larger than a normal multiple compression.

---

### 7. Contrarian Rating: **SHORT** (valuation-driven, not fraud-driven)

*Downgraded from "Strong Short" specifically because earnings quality is High and fundamental momentum is accelerating — shorting clean, accelerating compounders on multiple alone is a low-win-rate trade.*

**Recommended expression:** not a naked short. A $880B, 2.49-beta, ~60%-realised-vol name will produce violent squeezes (see the +45% in five days). Better structures: put spreads 12-18 months out struck at $400/$300; or a pairs trade short AMD / long a lower-multiple cash-generative semi (MU, AVGO) to isolate the AMD-specific premium.

**Catalysts to monitor:** (1) first disclosure of warrant accounting — contra-revenue or not; (2) OpenAI's ability to fund its 1 GW MI450 tranche in H2 FY27; (3) inventory days crossing ~180; (4) any gross-margin tick down below 51%; (5) confirmation of Form 4 transaction direction.

**Kill criteria — cover if:** DSO and inventory days both fall sequentially for two quarters while FY2028 revenue estimates are *raised*, or if the warrant is disclosed as a non-dilutive equity issuance with no P&L charge. That would remove the structural leg of the thesis and leave only multiple risk, which is not shortable against this momentum.

---

*Data gaps, stated plainly: no 10-K text was retrievable (the tool returned "No 10-K found"); the 10-Q excerpt returned only the SOX certification, not risk factors, so customer-concentration percentages are unverified from filings. Form 4 direction was unavailable. Vault/borrow cost and short interest were not obtainable.*
