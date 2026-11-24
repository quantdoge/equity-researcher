# Short Analyst

- Symbol: CRWV
- Elapsed: 50.4s

---
# CRWV — Forensic Short-Seller Analysis
**CoreWeave, Inc.** | Technology / Software-Infrastructure | Price $39.51–48.33 (Nov 20, 2026) | Mkt cap ~$22–27B

---

## 1. Earnings Quality Assessment

**Rating: LOW — Aggressive but Not Fraudulent**

The forensic scores flag loudly, but the arithmetic needs human interpretation:

| Score | Value | Read |
|---|---|---|
| Beneish M-Score | **+0.003** (threshold −1.78) | Extreme "manipulator" signal |
| Accruals ratio | −0.0857 | "OK" — but only because NI is negative |
| Earnings quality score | **0 / 100** | Bottom of scale |
| Piotroski F-Score | 5 / 9 | Moderate (fails dilution, margins, turnover) |
| Altman Z | **−0.14 → Distress** | Recomputing with market cap still gives ~0.06 |

**Important honesty caveat:** the Beneish model is *mis-calibrated* for a hyper-growth recent IPO. SGI (2.68) and SGAI (2.17) trigger mechanically on any company doubling revenue, and the FY2024 SG&A base of $137M looks like an IPO-year reclassification artifact. **I do not believe this is a Beneish fraud case.** But two components are genuinely diagnostic and cannot be dismissed: **DSRI 2.779** and **TATA** masking.

The earnings-quality score of 0 and the "ok" accruals ratio are both *artifacts of negative net income*. The real forensic problem is not accruals — it is **cost classification**.

### The headline finding: true gross margin is ~16%, not 68%

CoreWeave reports cost of revenue **excluding depreciation**; GPU depreciation sits in a separate opex line. In Q3 2026:

| | Q3'25 | Q1'26 | Q2'26 | Q3'26 |
|---|---|---|---|---|
| Reported gross margin | 73.0% | 65.5% | 65.9% | **67.7%** |
| Depreciation ($M) | 630 | 1,147 | 1,393 | **1,889** |
| **True gross margin (incl. D&A)** | 26.8% | 10.3% | 11.8% | **16.1%** |

True gross margin collapsed from ~28% (2025) to 10–16% (2026). The 68% number is a presentation choice that makes CRWV look like a software company. **It is a capital-intensive hardware lessor earning a mid-teens gross margin, before SG&A and before $846M/quarter of interest.**

---

## 2. Key Red Flags

**(1) Receivables — the single hardest red flag.**
- AR grew **+644% vs revenue +168%** in FY2025 (DSRI 2.78).
- DSO: 81 days (FY24) → **225 days** (FY25) → 158 days (TTM). Even after "improvement," 158 days of uncollected revenue is ~3–5x what a hyperscaler-billed GPU contract should require.
- **Re-accelerating:** Q3 2026 AR rose +68% QoQ ($2,541M → $4,280M) against revenue +42%. AR is again outrunning billings. Classic channel-stuffing/recognition-timing signature.

**(2) Depreciation materially understated — the core thesis.**
- TTM D&A $5.25B on ~$86B estimated gross PP&E = **~6% of cost per year**, versus the **16.7%** implied by management's stated 6-year life. Depreciation is running at ~⅓ of schedule because the fleet was bought in the last 12–18 months.
- At steady state on the current asset base, D&A must roughly **double to ~$14B/yr** — a **~$6–7B annual headwind still to arrive**, unmodelled in consensus.
- Sensitivity: a 4-year life (the economically honest number for AI accelerators) adds ~$6B/yr pre-tax ≈ **~$10.7/share** — roughly a quarter of the entire current share price.
- Michael Burry has publicly accused hyperscalers of understating depreciation by $176B (2026–28). CRWV is the purest, most levered expression of that trade.

**(3) OCF quality is flattered by customer prepayments and possibly capitalised interest.**
TTM OCF $7.20B *exceeds* TTM EBITDA of $5.17B by ~$2.0B — structurally odd, since OCF should sit *below* EBITDA after cash interest. Working-capital inflows (+$1.56B TTM) and SBC (+$635M) explain part. The residual points to customer prepayment/deferred-revenue timing, and to **interest capitalisation into construction-in-progress** — which would mean reported interest expense *understates* the true economic cost. **Verify cash interest paid and capitalised interest in the 10-Q; this is my single biggest unresolved gap.**

**(4) Insolvency-adjacent balance sheet.**
- Total debt **$66.2B** (from $29.8B nine months earlier), net debt $60.7B against $4.0B book equity (~16x).
- **Current ratio 0.44** ($10.8B current assets vs $24.4B current liabilities). Working capital negative $13.6B.
- Interest expense TTM **$2.41B**, growing **+66% YoY**; FY2025 $1.23B. Q3'26 interest of $846M = **23% of revenue** and **4.1x operating income**.

**(5) The cash burn is the whole story.**
TTM capex **$27.6B** vs $7.2B OCF → **FCF −$20.4B**. Cumulative FCF 2023→Q3'26 ≈ **−$32B**. Funded by debt and dilution: shares 192M (2023) → 218M (2024) → 435M (2025) → **559M** (Q3'26). Piotroski flags dilution (F7=0) and failing asset turnover. This is a capital-consuming machine being valued on revenue.

**(6) Customer concentration remains existential despite headline "diversification."**
Microsoft was **67% of FY2025 revenue** (10-K). Q3 2026: two unnamed customers at **30% and 24%** (54% combined). The FT reported **Microsoft withdrew from some agreements over delivery issues and missed deadlines** — CRWV denies it. The **$132.5B backlog (+138% YoY)** is a marketing number until it converts; a large share rests on counterparties (hyperscalers with in-house alternatives; OpenAI, a loss-making entity dependent on continuous external fundraising) whose ability *and willingness* to pay is unproven.

---

## 3. Beneish & Accruals Detailing

- **M-Score +0.003**: driven by DSRI 2.78 (real red flag), SGI 2.68 and SGAI 2.17 (growth artifacts — discounted), AQI 0.775 (favorable), LVGI 0.911 (artifact — total debt nearly tripled; the vendor formula uses a narrow leverage ratio).
- **Accruals ratio −0.0857** is *mechanically* flattered by negative earnings plus $5.2B of non-cash D&A. It carries no information here. The earnings-quality composite of **0/100** is the more honest signal: FCF conversion is deeply negative and cash conversion is meaningless when NI < 0.
- **The correct accruals test for this business is the D&A/capex gap, not the balance-sheet accrual.** D&A of $5.2B against $27.6B of capex means reported earnings will be progressively punished for the next several years regardless of operating performance.

---

## 4. Competitive Threat Assessment

**Moat: weak and eroding. This is a commodity capacity lessor with a financing advantage, not a technology moat.**

- **Gross margin** (ex-D&A) fell from 75.6% (Q4'24) to 65.5% (Q1'26) — a ~1,000bp compression — before partially recovering to 67.7%. That is the direct financial signature of pricing-power loss as GPU supply loosened.
- **Zero switching costs**: NVIDIA GPUs are fungible; Nebius, IREN, Crusoe, Lambda, Together and Nscale all rent the same silicon.
- **Supplier/customer squeeze from both sides**: NVIDIA captures the economics upstream (and has backstopped CRWV capacity — a circular vendor-finance structure where NVIDIA invests in AI labs that buy CRWV compute that CRWV buys with NVIDIA chips). Hyperscalers capture them downstream by building in-house and by squeezing vendors on delivery.
- **The only durable asset is contracted power (4.6 GW)** — real, but replicable with capital, and the capital is now expensive.
- **The 2029 A100 contract** cited bulls are correct that accounting life ≠ commercial life. But one contract is an anecdote, not a fleet-wide curve.

---

## 5. Management & Governance Red Flags

1. **Insider selling at extraordinary scale**: ~**$9.06B of shares sold in 24 months** (MarketBeat aggregate). CEO Michael Intrator sold 307,692 shares at ~$88.60 (Aug/Sep 2026); **Magnetar** (the 10% owner that incubated the company) has been a persistent seller. **No meaningful offsetting insider buying** appears in the record.
2. **Promotional timing pattern**: Intrator **cancelled a planned share sale** after the August 2026 earnings beat/guidance raise, then sold weeks later. Behaviour that manages optics around news flow is a governance tell.
3. **Aggressive narrative management**: the CEO publicly calls the GPU depreciation debate **"nonsense"** — the single issue on which the entire equity value hinges. Dismissiveness on the one question that matters is not reassuring.
4. **Structural complexity**: $66B of debt layered through SPV/equipment-financing vehicles with GPU collateral; a fresh ~$4B equipment-backed loan under discussion in Nov 2026. Complexity plus leverage plus a depreciating collateral base is the classic failure architecture.
5. **Dual-class control** — insiders retain voting control with a minority of the economics, and 20 Form 4 filings in Oct–Nov 2026 alone.

---

## 6. Short Thesis Summary — Is There a Credible Bear Case?

**Yes, but it is a solvency/accounting-duration thesis, not a fraud thesis.**

The bear case in one line: *CRWV is a capital-intensive hardware lessor with ~16% true gross margin, $66B of debt at rising rates, a 158-day receivable cycle, customer concentration that is still ~54% in two names, and depreciation that must roughly double from here — being valued at ~$85B enterprise value on a 68% gross margin that excludes the depreciation of the very machines generating the revenue.*

Three falsifiable triggers to watch:
1. **Depreciation life extension or further capex ramp** without matching D&A guidance.
2. **Continued AR-outpacing-revenue** (Q3 2026 already re-broke this) — the cleanest tell for recognition stress.
3. **Any Microsoft/OpenAI backlog renegotiation** or a failed/costlier refinancing of the $66B stack.

### The other side — and it is strong

I must be explicit: **the bull case is materially better than most shorts acknowledge.**
- Revenue is genuinely **re-accelerating**: +168% YoY in Q3 2026, sequential +42%, and 2026 guidance raised to **$13.0–13.3B**.
- EBITDA margin ~52%; **interest coverage has improved to ~2.1x** — not deteriorating, as the bear case requires.
- Backlog $132.5B (+138%), 4.6 GW of contracted power.
- Concentration is *improving* (top customer 30% vs 67% a year ago).
- The stock is **already down 79% from its $187 June 2025 peak and below its $40 IPO price**. A great deal of the bear case
