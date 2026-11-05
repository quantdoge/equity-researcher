# Short Analyst

- Symbol: LSCC
- Elapsed: 147.8s

---
I have enough to write. One correction to my initial hypothesis: AMI's gross margins are **above 70%** (higher than Lattice standalone), so this acquisition is gross-margin accretive — my margin-dilution thesis was wrong, and I'll report that honestly.

---

# LSCC — Forensic Short-Seller Analysis

**Price $107.25 · Market cap $15.23B · EV ~$16.03B · Beta 1.89 · S&P 'BB' (junk)**

---

## 1. Earnings Quality Assessment — **MEDIUM** (not fraudulent; but low-quality GAAP)

**No fraud signal.** Beneish is clean and accruals are deeply negative. But the headline quality metrics are mechanically flattered by enormous stock-based compensation, and the gap between "adjusted" and GAAP is now the widest in the comp's history.

| Metric | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Revenue | $737.2M | $509.4M | $523.3M |
| Gross margin | 69.8% | 66.8% | 68.2% |
| Operating margin | 28.8% | 6.8% | **2.9%** |
| GAAP net income | $259.1M | $61.1M | **$3.1M** |
| GAAP EPS | $1.85 | $0.44 | **$0.02** |
| **SBC** | $70.2M | $53.0M | **$115.6M** |
| SBC / revenue | 9.5% | 10.4% | **22.1%** |
| SG&A / revenue | 18.6% | 23.0% | **29.4%** |
| Implied R&D / revenue | 22.4% | 37.1% | **35.9%** |

**The critical adjustment the market is not making.** Reported operating cash flow of $175.1M is flattered by the $115.6M SBC add-back. Adjusting for the economic cost of comp:

| Ex-SBC free cash flow | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| OCF − SBC − capex | **$179.3M** | $66.9M | **$17.0M** |

Ex-SBC FCF fell **−90%** from FY2023 to FY2025, while the stock rose ~2x over the same period (from ~$55 in Jan-2025). On true economic FCF, EV/FCF is roughly **900x**. The tool's "quality score 60/100" is the honest read — mediocre, masked by a 56.8x cash-conversion artifact caused by a near-zero denominator.

**Earnings-quality flags I could not explain away:**
- **FY2024 net income ($61.1M) exceeded operating income ($34.5M)** — a ~$27M positive below-the-line item. Q4-FY24 alone: operating income **−$12.2M**, net income **+$16.5M**. Likely a discrete tax benefit/valuation-allowance release; unverified. Either way FY2024's "profitability" was not operational.
- **Q4-FY25**: operating income +$2.2M but GAAP net loss **−$7.6M** (non-operating/tax drag).
- **SG&A +31% and SBC +118% in FY2025 while revenue grew 2.7%.** Management was paid richly through a revenue trough. That is a governance statement, not an accounting one.

---

## 2. Beneish M-Score & Accruals

**M-Score = −3.251 → "Low risk"** (thresholds: >−1.78 possible manipulation, >−2.22 soft warning). This is decisively clean.

| Component | Value | Read |
|---|---|---|
| DSRI | **1.228** | ⚠️ Receivables outpacing sales — the one strongly bearish input |
| GMI | 0.98 | Slight gross-margin *improvement* ✔ |
| AQI | 0.934 | Asset quality improving ✔ |
| SGI | 1.027 | Modest sales growth |
| DEPI | **1.535** | Depreciation rate declining — watch intangible amortization schedules |
| SGAI | **1.279** | ⚠️ SG&A deleveraging |
| LVGI | **1.215** | ⚠️ Leverage rising (will be far worse in FY2026) |
| TATA | **−0.1948** | Strongly negative accruals — dominates the score |

**Accruals ratio:** −0.1948 (FY25), −0.0945 (FY24), −0.0125 (FY23), −0.0750 (FY22). All negative, all benign.

**Two honest caveats on this "clean" verdict:**
1. The negative TATA is *itself* the SBC add-back. Strip SBC from operating cash flow and FY2025 accruals turn **positive**. The model is validating a metric that stock comp is manufacturing.
2. **The M-Score is stale.** It is computed from FY2024→FY2025 balance sheets. The AMI acquisition and $925M of new debt landed in Q3 FY2026 (Oct-2026). The FY2026 10-K — the first to include a fundamentally different balance sheet — has not been scored. LVGI and DEPI will both deteriorate sharply.

**Receivables — flag, but the smoking gun isn't there.** FY2025 AR +26.2% vs revenue +2.7% (DSRI 1.228) is genuine. But DSO improved materially afterwards: 64.5 days (Q4-FY25) → 66.2 → 54.3 → **51.4 days (Q3-FY26)**. The annual flag is largely a base effect off a depressed FY2024. **No channel-stuffing confirmation.**

**Inventory — the tool's "rising" label is unreliable.** Raw days: 193.4 (FY22) → 162.1 (FY23) → 223.3 (FY24) → 195.8 (FY25) → **~116 days (Q3-FY26)**. Rising over the window, sharply *falling* recently. Destocking is complete; this is a **bull** point, not a bear one.

---

## 3. Key Red Flags Found

1. **Balance sheet transformed in one quarter.** Total assets $976M → **$2,610M**; debt $38M → **$925M**; goodwill + intangibles $335M → **$1,929M**. Net cash of +$135M became net debt of **−$797M**.
2. **Tangible book equity is negative ~$512M** against a $15.23B market cap. 74% of assets are goodwill/intangibles.
3. **Altman Z collapses on a book-equity basis.** The reported Z of 3.849 is **pre-acquisition and stale**. Rebuilt on the Q3-FY26 balance sheet (annualised EBIT/sales): Z ≈ **1.53 — distress zone** (<1.81). With market-cap X4 it would be ~7.7, so this is a balance-sheet-quality observation, not a solvency claim. But the transition from "safe" to "distress on book" in one quarter is real.
4. **Interest coverage is thin.** Q3-FY26 EBIT $23.4M vs interest $9.6M = **2.4x** — and that interest figure covers only a partial quarter of the debt. **S&P rates the credit 'BB' (junk).** A $500M-revenue cyclical just levered to ~4x and lost investment grade.
5. **Relentless dilution.** Diluted shares 136.7M (Q4-FY25) → **143.8M (Q3-FY26), +5.2%** in three quarters (AMI equity consideration + SBC). Buybacks ($100M FY25, $80M FY23, $110M FY22) do not offset SBC — shareholders are funding comp indirectly.
6. **Valuation with no room for error.** 29x trailing sales; ~14.6x EV/pro-forma sales; **84x annualised current EBITDA ($192M)**. Consensus requires EBITDA to reach $774M by FY2028 (**4x in ~2.5 years**) and $1.63B by FY2031 at a 50% margin.
7. **Analyst dispersion is a red flag in itself.** FY2029 EPS estimates: low **$2.77**, high **$7.46** — a 2.7x spread across 9 analysts on a three-year-out number. The 2031 estimates ($3.23B revenue, $1.30B net income) rest on **4 analysts**. When a valuation depends on long-dated estimates this dispersed, it is a narrative, not a forecast.
8. **Insiders sold continuously and bought nothing.** 30 Form 4s June–November 2026, with 7-filing clusters on 2026-07-14 and 2026-10-13, plus a filing on **2026-11-04 — the day after an +11% earnings pop**. Critically, through the **40% drawdown from $155 (June) to $93 (Oct-30)**, no insider bought. *(Caveat: the data feed returns filing metadata only, not transaction direction or size. Treat as indicative, and note much of this is likely RSU vesting / 10b5-1.*)
9. **Fixed cost structure + cyclicality.** Revenue −30.9% in FY2024 while opex stayed ~$330M turned a 28.8% operating margin into 2.9%. That same operating leverage now runs against $925M of debt and $1.9B of goodwill. A repeat downcycle means GAAP losses and impairment risk.

---

## 4. Competitive Threat Assessment — **Moderate, with one specific erosion vector**

- **FPGA:** Lattice (~$520M standalone revenue, 1,174 employees, ~$188M R&D) competes with **AMD/Xilinx** ($798B cap) and **Intel/Altera** — R&D budgets 50–100x larger — plus Microchip (PolarFire, a direct low-power competitor) and Chinese entrants (Gowin, Anlogic, Pango, Efinix) in low-cost. Its niche (low-power, small-form-factor, 10-year design cycles, sticky industrial/auto sockets) is a real moat. **Gross margin has held at 67–70% for four years — no pricing-power erosion. This is a genuine bull point and I will not manufacture a bear case against it.**
- **AMI (the new half of the company):** ~$200M revenue, high-teens growth, **>70% gross margin** — genuinely accretive. But its franchise is UEFI/BIOS and BMC firmware, and its most valuable customers (Google, Meta, hyperscalers) are precisely the parties funding **open-source displacement: LinuxBoot, coreboot, OpenBMC**. A 70%-margin BIOS toll booth is structurally attractive *until* the customer base decides to internalise it — and here they have both the motive and the capability. The deal also reframes LSCC as "silicon-neutral firmware," a software market where it has zero track record, and adds a security/trust-anchor liability profile (a firmware vulnerability is existential, not cyclical).
- **China/export controls** remain an unquantified tail risk on FPGA revenue.

**Net: moat stable today, but the acquired half is more erodible than the FPGA half, and the market is capitalising the combination at a software multiple.**

---

## 5. Management Red Flags

No auditor changes, no related-party concerns, no restatements. The flags are behavioural and capital-allocation-based, not fiduciary: **SBC +118% while revenue +2.7%**; a **$1.65B debt-and-equity-funded acquisition closed at peak valuation** ($1.0B cash + $650M stock + $925M debt + $50M cash); issuing equity at ~$140 while buying back stock in prior years; and **selling into strength with zero insider buying through a 40% drawdown**.

---

## 6. Short Thesis Summary — is there a credible bear case?

**Yes — but it is a valuation and capital-structure thesis, not a fraud thesis.** I want to be explicit about what I found *against* the short:

**The bull case is strong and I will not overstate mine:**
- **Organic acceleration is real and pre-dates the deal:** Q1-FY26 +42.2%, Q2-FY26 +62.2% — both quarters closed *before* AMI consolidated. This is the single best argument against the short.
- **Beneish clean (−3.25), accruals negative, F-Score 6, Altman safe pre-deal, no channel stuffing, DSO and inventory days both improving, gross margin intact at 67.4%.**
- **AMI is a good asset** (~$200M rev, high-teens growth, >70% GM) at 8.25x sales — defensible for high-GM, growing software. My initial margin-dilution hypothesis was **wrong**.
- Revenue run-rate crossing **$1B exiting FY2026**; deleveraging from 3–4x is plausible if estimates hold.
- The stock has **already de-rated 40%** ($155 → $93) before the current bounce, so some froth is out.

**The bear case — one sentence:**
> A $15.2B equity (16x EV/sales, ~900x ex-SBC FCF, 84x current EBITDA) rests entirely on FY2028–2031 estimates with a 2.7x spread, for a company that earns **$0.02 of GAAP EPS** because stock comp is 22% of revenue, just levered to 4x with a junk rating and $1.9B of goodwill, and is buying a firmware business into open-source headwinds — leaving no cushion for the next semiconductor downcycle of a business that lost 31% of revenue in FY2024.

**The catalyst is the cycle, not a restatement.** Beta 1.89; revenue −31% in FY2024 with a fixed cost base is the template. Flattening AI capex or an industrial/auto air pocket → operating-margin compression → GAAP losses → impairment review on $1.9B of goodwill → equity raise. That is the path to a 40–50% drawdown, and it requires no accounting irregularity whatsoever.

---

## 7. Contrarian Rating: **SHORT** (moderate conviction — tactical, not structural)

**Not a Strong Short.** A fraud-led short would be wrong here, and grading it as one would be reflexive rather than rigorous. This is a **quality-of-earnings and valuation short** against a genuinely accelerating business, which caps conviction and demands discipline.

**Sizing and risk management:**
- **Half to two-thirds normal short size.** Never a core position.
- **Squeeze risk is elevated and demonstrated:** +11% on a single earnings print (2026-11-03), and the stock rallied 310% off its April-2025 low of $37.84. This is a crowded, momentum-driven, AI-adjacent name with a 1.89 beta.
- **Stop discipline required** — a decisive break above the $155 June high on volume invalidates the thesis.
- **Better expression than a naked short:** the credit (BB, 4x levered, 2.4x interest coverage) offers a cleaner risk/reward than the equity if CDS/bonds are accessible.

**What would make me wrong, and I would cover:** two consecutive quarters of ≥40% organic growth with AMI fully consolidated; net leverage falling below 2.5x faster than guided; blended gross margin proving sustainable above 70% at scale; or any meaningful insider open-market buying.

**What would make me add:** a second consecutive quarter of receivables growth outpacing revenue; the FY2026 10-K showing positive accruals once SBC is included; goodwill impairment disclosure; or an order-pattern break in industrial/auto.

**Data gaps, stated plainly:** AMI segment-level revenue/margin and pro-forma contribution split (acquisition deck returned HTTP 403); insider transaction *direction and size* (feed returns filing metadata only); 2027 consensus estimates (only 2028–2031 available); borrow cost and short interest. Recommendation should be re-underwritten after the FY2026 10-K — the first filing that will properly reflect the new capital structure.
