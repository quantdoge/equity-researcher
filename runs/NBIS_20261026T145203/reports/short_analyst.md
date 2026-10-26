# Short Analyst

- Symbol: NBIS
- Elapsed: 312.4s

---
## FORENSIC SHORT-SELLER ANALYSIS — Nebius Group N.V. (NBIS)

**Snapshot:** Price $159.24 · Market cap $38.2B (240M basic) / ~$49B fully diluted (309M incl. converts) · Total assets $27.96B · Debt $10.06B · Cash $8.04B · TTM revenue ~$1.36B. Stock peaked ~$265 (Aug–Oct 2026) and is ~40% off that high. Dutch-domiciled foreign private issuer (files 20-F/6-K — no 10-Qs, materially thinner interim disclosure than a US issuer).

---

### 1. Earnings Quality Assessment — **LOW** (aggressive, not fraudulent)

I want to be precise here: I found **no evidence of fraud**. What I found is a *presentation architecture* that systematically flatters the operating reality on four separate axes. That distinction matters — it changes the trade from "fraud short" to "re-rating short."

**Axis 1 — Depreciation is excluded from cost of revenue.** Reported Q2 2026 gross margin is 77.1% ($448.7M on $582.3M). But D&A in that quarter was $259.7M — the cost of the GPUs that *are the product*. Fully loaded, gross profit is ~$189M, or **32.5%**. For FY2025 the math is worse: gross profit $363.6M against D&A $468.5M → **fully-loaded gross margin of −20%**. The product's cost of goods does not include the cost of the product. This is the single most important number in this report.

**Axis 2 — Reported EBITDA/EBIT contain non-operating gains.** FY2025: operating loss −$596.2M, D&A $468.5M → EBITDA should be ≈ −$128M. Reported EBITDA: **+$559.3M**. The ~$687M gap is investment gains. Q1 2026 is starker: operating loss −$128.0M, reported EBIT **+$679.1M**, reported EBITDA **+$920.9M** — ~$807M of non-operating income sitting inside "EBIT." Anyone screening NBIS on reported EBITDA is looking at a number that has nothing to do with operations. Only Q2 2026 ($83.8M) is genuinely operating-derived — and after $102.5M of SBC it is **−$18.7M**.

**Axis 3 — Net income is positive 3 of 4 years on non-operating items.** FY2025 NI +$101.7M vs operating loss −$596.2M (+$698M non-operating). Q2 2025 NI +$584.4M vs operating loss −$111.2M. Q1 2026 NI +$621.2M vs operating loss −$128.0M. The profits are mark-to-market/asset-sale gains (legacy Yandex-era stakes, ClickHouse-type holdings). Non-cash, non-recurring, and optically masquerading as earnings.

**Axis 4 — Operating cash flow is prepayment and balance-sheet driven.** Q1 2026 OCF $2.258B and Q2 2026 OCF $2.246B, against quarterly revenue of $399M and $582M respectively. Working capital contributed +$2.122B and +$0.811B. That is customer money arriving in advance (deferred revenue — a *liability*), plus a ~$1.24B receivables unwind. Real economics, but not repeatable earnings power. Meanwhile **FCF was −$3.41B in Q2 2026 alone** and cumulative FCF is roughly **−$6.6B over six reported quarters**.

**The tool composite says 60/100 — I think that overstates it.** The "cash conversion ratio" of 378% and "accruals ratio" of −0.023 both pass only because the numerator (NI) and denominator (OCF) are each distorted by the same one-offs in opposite directions. Passing a test for the wrong reason is not quality.

---

### 2. Key Red Flags Found

| # | Red flag | Supporting data |
|---|---|---|
| 1 | **Depreciation lagging asset base** | PP&E $8.40B → $14.90B in one quarter (+78%), but D&A only $241.8M → $259.7M (+7%). Annualized D&A of ~$1.04B against $14.9B PP&E implies ~14-year blended life — while press reports say NBIS depreciates GPUs over ~4 years. The two cannot both be true unless a large share of PP&E is not yet in service. **Either way, a depreciation cliff is contracted, not hypothetical.** |
| 2 | **Receivables balloon** | FY2025 revenue +479% vs AR **+1,823%** (DSRI 3.32). DSO: 588 days (FY2025) → 348 days (Q1 2026) → 45 days (Q2 2026). The spike was severe; it then reversed violently. |
| 3 | **Leverage index 7.57** | Total debt $187.8M (Q1 2025) → **$10.06B** (Q2 2026), ~53x in five quarters. Net debt swung from −$1.26B (net cash) to **+$2.01B**. |
| 4 | **Extreme capital intensity** | Altman X5 (revenue/total assets) = **0.0426** — about 4 cents of revenue per dollar of assets. Q2 2026 capex $5.66B = ~9.7x that quarter's revenue. |
| 5 | **Dilution** | Shares 238M → 280M (+17.6%) in five quarters; diluted Q1 2026 count 309M vs 258M basic (+19.6% potential). SBC $102.5M in Q2 2026 alone (~17% of annualized revenue). Note: the Piotroski F-score scored "no dilution" as **passing** — that component is simply wrong here. |
| 6 | **Customer concentration** | Three customers ≈ **59% of revenue** in Q2. Microsoft ($17.4B, expandable to $19.4B) and Meta (~$3B/5yr) dominate. Microsoft is also a direct competitor (Azure) and the deal is **back-end loaded** — revenue arrives late while depreciation runs from day one. |
| 7 | **Insider distribution into strength** | COO Ophir Nave sold 48,845 shares at **$234.21** (Oct 5); director Ryan Charles E sold 50,000 at **~$265** (Aug 14); director John Boynton IV sold at $164.80/$188.77 (Oct 15). 25 Form 4s in ~4 months. Stock now $159. Insiders sold 30–40% above today's price. |
| 8 | **Vendor circularity** | Nvidia disclosed a **9.3% stake** (~$2B at $94.94, March 2026). The supplier is funding the customer's capex to buy the supplier's product, which generates the revenue being celebrated as demand. That is a self-referential demand signal — and it gives Nvidia allocation and pricing power over NBIS. |

**Beneish M-Score = 2.469 ("HIGH RISK").** I'll be straight with you: this score is **partly mechanical**. SGI 5.79 and LVGI 7.57 are what a hypergrowth, debt-funded buildout produces by construction — Beneish was built for mature manufacturers, and it false-positives on this profile. The components that are *genuinely* diagnostic are **DSRI 3.32** (receivables outrunning revenue — real, though it unwound in Q2) and **DEPI 1.304** (depreciation lagging the asset base — real and unresolved). TATA is negative (fine), GMI 0.761 shows margin improvement (not a flag), SGAI 0.256 (not a flag). So: high-risk label, but the honest read is "aggressive capitalisation and presentation," not "cooked books."

---

### 3. Accru
