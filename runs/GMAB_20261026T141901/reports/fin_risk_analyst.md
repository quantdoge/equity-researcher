# Fin Risk Analyst

- Symbol: GMAB
- Elapsed: 73.9s

---
I have what I need. Writing the assessment now.

---

# GMAB — Genmab A/S: Complete Financial Risk Assessment

**Sector:** Healthcare / Biotechnology (Denmark) · **Price:** $44.83 · **Market Cap:** $27.56B · **Employees:** 3,119

## Executive Summary — The Thesis Has Structurally Changed

Genmab is **no longer a net-cash royalty company**. In December 2025 it closed the ~$8B acquisition of Merus, funded with ~$5.5B of new senior secured debt. Reported leverage, coverage, and solvency metrics therefore reflect a **12-month-old capital structure**, and several tool outputs (interest coverage of 20.5x, Altman "distress" at 1.696) are **materially misleading in opposite directions**. My central finding: the company remains profitable and cash-generative, but its **credit profile has been downgraded to sub-investment grade (BB/BB+)**, tangible book value is **negative**, and run-rate interest coverage is closer to **~3x, not 20x**.

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE**

| Agency | Issuer Rating | Secured Debt | Recovery |
|---|---|---|---|
| Fitch (final, Feb 2026) | **BB**, Outlook Stable | BB+ | RR2 |
| S&P | **BB+** | BB+ | '3' |

The downgrade to BB is the decisive fact. Genmab went from an undebted, net-cash balance sheet to **$5.43B gross debt / $3.71B net debt** in one transaction.

**Debt structure (this is the good news):**
- $1.0B Term Loan A · $2.0B Term Loan B · $1.5B senior secured notes
- **TLB and notes both mature November 2032** — no near-term refinancing cliff
- Only **$273M** classified short-term (5% of debt)

**Critical adjustment — interest coverage:**
The tool reports **20.49x**, computed on FY2025 interest expense of just **$61.0M**, which captures only weeks of the new debt. Actual quarterly interest: Q3'25 $3.0M → Q4'25 $43.9M → Q1'26 $112.4M → Q2'26 $110.0M. Run-rate annualized interest is **~$445M**.

> **Run-rate EBIT / interest ≈ 2.8–3.0x** (2026E operating profit ~$1.2–1.3B ÷ ~$445M). Against LTM interest recognized ($269M) it is ~5.0x. Either way, **coverage has collapsed from >20x to roughly 3x.** This is the single most understated metric in the standard data feed.

**Altman Z-Score correction:** reported 1.696 ("Distress") uses **book** equity ($5.83B) in X4. Substituting market cap ($27.56B / $7.01B liabilities = 3.93 vs 0.83) raises Z by 0.6 × (3.93 − 0.83) = **+1.86 → Z ≈ 3.56, Safe zone**. The "distress" flag is an artifact. However, X3 (EBIT/TA = 0.099) and X5 (Sales/TA = 0.290) are genuinely weak because the asset base ballooned with goodwill.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Assessment |
|---|---|---|
| Total debt / Equity | 0.93x | Moderate; but… |
| Total debt / Assets | 0.42x | Elevated for biotech |
| Net debt / EBITDA | **2.78x** | Moderate, manageable |
| Gross debt / EBITDA | **4.06x** | Sub-IG appropriate, no cushion |
| Interest coverage (reported) | 20.49x | **Misleading — partial-year debt** |
| Interest coverage (run-rate) | **~3.0x** | **Weak; sub-IG profile** |
| Current ratio | 2.02x | Adequate |
| Quick ratio | 2.01x | Adequate (negligible inventory) |
| Cash ratio | 1.20x | Adequate |
| Cash to liabilities | 0.24x | Thin |
| Working capital | $1,454.7M | Positive |
| Altman Z (book equity) | 1.696 Distress | Artifact — see above |
| Altman Z (market equity) | ~3.56 Safe | Indicative |
| Piotroski F-Score | **4 / 9 (Weak)** | Genuine deterioration |
| FCF yield | 4.09% | Reasonable |
| FCF margin | 30.9% | Strong |

**Piotroski detail (4/9):** Fails F5 (leverage rose), F6 (equity change negative), F3 (ROA decline), F8 (gross margin decline), F9 (asset turnover decline). Four of five failures are acquisition mechanics — but **F5 is a real, substantive red flag**, not a technicality.

**The balance-sheet transformation (drawn from statements):**

| | FY2023 (DKK) | FY2024 (DKK) | FY2025 (USD) |
|---|---|---|---|
| Cash & ST inv. | 28,135M | 21,101M | $1,711M |
| Total debt | 770M | 1,029M | **$5,426M** |
| Net debt | −14,097M | −8,829M | **+$3,715M** |
| Goodwill & intangibles | 101M | 14,878M | **$9,456M** |
| Total equity | 31,610M | 36,697M | $5,834M |

**Net cash of ~$1.2B → net debt of $3.7B in one year.** Goodwill/intangibles are now **74% of total assets** ($9.46B / $12.84B) and, critically:

> **Tangible book value = $5,834M − $9,456M = −$3,623M (negative).**

There is **no tangible equity cushion beneath the debt** — recovery depends entirely on cash flows and the acquired IP's value, not assets. This is precisely why Fitch assigns RR2 to the secured debt and why equity sits at the bottom of the waterfall.

*Note: FY2024/2023 reported in DKK, FY2025 in USD — ratios across the boundary are not directly comparable, and the DKK/USD shift (DKK 21,526M ≈ $3.1B vs $3.72B reported) means part of headline "growth" is translational.*

---

## 3. Market Risk Profile

| Metric | Value | Interpretation |
|---|---|---|
| Annualized volatility (252d) | **36.36%** | High — ~2.4x market |
| Beta vs SPY | **0.789** (tool) / 0.645 (reported) | **Deceptively low** |
| Max drawdown | **30.67%** | Material |
| Sharpe (0% rf) | **1.469** | Good on trailing basis |
| Sortino | Not available | **Data gap** |

**Beta understates true risk.** A 0.79 beta implies GMAB is defensive, but that is a historical artifact of the pre-Merus royalty model. The actual risk is **idiosyncratic and binary**: ~64% of revenue is a single royalty stream plus clinical/pipeline catalysts. Biotech drawdowns from pipeline or patent events are uncorrelated with the market — a market-beta framework systematically under-prices this. **36% volatility against 0.79 beta is the signature of concentrated single-asset risk, not diversification.**

The 1.47 Sharpe is respectable but backward-looking; it is computed over a window that includes the pre-leverage royalty-model era.

---

## 4. Downside Scenario Analysis — Revenue −20%

Revenue concentration is the transmission mechanism: **DARZALEX royalties were $2.4B of $3.7B FY2025 revenue (~64%)**, and 2026 guidance is ~$2.7B of ~$4.4B. Royalties carry ~100% incremental margin, so a revenue decline here flows through to profit almost one-for-one.

| | Base 2026E | Revenue −20% | Delta |
|---|---|---|---|
| Revenue | ~$4,400M | $3,520M | −$880M |
| Gross margin | ~91% | ~91% | — |
| Gross profit | $4,004M | $3,203M | −$801M |
| Operating expenses (approx. flat) | ~$2,450M | ~$2,450M | — |
| **Operating income** | **~$1,250M** | **~$370M** | **−70%** |
| Interest expense | $445M | $445M | — |
| **Interest coverage** | **~2.8x** | **~0.83x** | **Fails** |
| EBITDA | ~$1,600M | ~$720M | −55% |
| **Gross debt / EBITDA** | **2.8x** | **6.3x** | Covenant risk |
| **Net debt / EBITDA** | **~2.3x** | **~5.0x** | Covenant risk |
| FCF (approx.) | ~$1,200M | ~$250M | −79% |
| Net income (approx.) | ~$780M | ~$290M | −63% |

**Findings:**
1. **Operating leverage cuts both ways.** A 20% revenue decline produces a ~70% operating profit decline — the business has extremely high fixed-cost intensity relative to its royalty base.
2. **Covenant breach is likely.** At 6.3x gross leverage, a 20% revenue shock would breach a typical ~3.5–4.0x net secured leverage maintenance covenant on the TLA. *Actual covenant thresholds could not be retrieved — flagged as a data gap — so this is a modeled, not confirmed, conclusion.*
3. **Liquidity survives; solvency is tested.** Cash of $1.5B plus ~$250M FCF would still meet $445M interest and $273M of amortization. **This is not a near-term default scenario** — maturities are in 2032. It is a *rating-downgrade and equity-de-rating* scenario, not a liquidity event.
4. **Recovery math favors debt.** With secured debt at BB+/RR2, a stressed scenario transfers value from equity to lenders. Equity has no tangible book support (−$3.6B).

**Rate sensitivity:** $3.0B of TLA/TLB floats at SOFR + 3.0%. **+100bp = +$30M/yr interest (~7%)**, taking run-rate coverage from ~2.8x to ~2.6x.

---

## 5. Overall Financial Risk Rating: **HIGH**

Justification — the rating is driven by *structural change*, not distress:

- **Sub-investment-grade BB/BB+** with only ~3x run-rate interest coverage
- **Negative tangible equity** (−$3.6B) and 74% of assets in goodwill/intangibles
- **64% revenue concentration** in one royalty stream (DARZALEX, facing eventual patent expiry)
- **Piotroski 4/9**, with leverage and asset-turnover deterioration genuine
- **Elevated 36% volatility** with deceptively low beta masking binary risk

**Offsets (why not "Critical"):**
- **Positive FCF of $1.15B (30.9% margin)** — the company services debt from cash generation, not balance-sheet reserves
- **No refinancing cliff** — TLB and notes both due **November 2032**
- **Ample near-term liquidity** — CR 2.02x, cash 1.20x, $1.5B cash vs $273M ST debt
- **Revenue growing 25%** (H1 2026) with guidance raised
- **Fitch Outlook Stable** — no imminent downgrade pressure

---

## 6. Key Red Flags

1. **🔴 Interest coverage of ~3x, not the reported 20.5x.** The database's coverage ratio uses partial-year interest ($61M) and overstates the true burden by ~7x. **Any screen relying on the reported figure would misclassify this credit.**
2. **🔴 Negative tangible book value (−$3.6B).** Goodwill and intangibles ($9.46B) exceed total equity ($5.83B). Recovery value rests on cash flows alone.
3. **🔴 Single-asset concentration.** ~64% of revenue from DARZALEX royalties; ~$2.7B of ~$4.4B 2026E revenue. Patent cliff risk is deferred but not eliminated.
4. **🟠 Operating profit flat despite 25% revenue growth** (H1 2026: $555M vs $548M). The Merus deal's interest and amortization are consuming the entire incremental profit — **growth is not reaching the bottom line.**
5. **🟠 Capital allocation concern:** $430M of buybacks in 2025 executed while simultaneously raising $4.5B of debt to fund M&A — repurchasing equity while levering the balance sheet.
6. **🟠 Goodwill impairment risk.** $9.46B of goodwill/intangibles after a 41%-premium acquisition; any Merus pipeline setback (petosemtamab) triggers a write-down against a thin equity base.
7. **🟡 Floating-rate exposure** on ~$3.0B of term loans.

## Data Gaps & Caveats
- **Covenant thresholds not retrieved** (IR debt page returned 403; modeled at typical BB levels).
- **No rating-agency detail beyond headline levels**; no CDS spreads available.
- **Sortino ratio and 52-week price range unavailable.**
- **TLA maturity not confirmed** (only TLB/notes at Nov-2032).
- FY2024/2023 in DKK vs FY2025 in USD — cross-period ratios approximate.
- Altman Z uses book equity per the tool's methodology; my market-cap-adjusted ~3.56 is indicative, not a literal Altman reading.

**Bottom line:** Genmab is a **profitable, strongly cash-generative business that has just taken on a sub-investment-grade capital structure.** The near-term default risk is low — liquidity is adequate and nothing matures before 2032. But the **cushion is gone**: negative tangible equity, ~3x coverage, and 64% revenue concentration mean a 20% revenue shock would push leverage to ~6x and threaten covenants. For an equity holder the risk is de-rating and dilution, not insolvency; for a credit investor the secured paper (BB+/RR2) is well-protected. **Risk rating: HIGH — acceptable only with position sizing that respects the loss of the net-cash floor.**
