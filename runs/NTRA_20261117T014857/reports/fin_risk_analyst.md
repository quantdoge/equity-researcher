# Fin Risk Analyst

- Symbol: NTRA
- Elapsed: 71.4s

---
# NTRA — Natera, Inc. | Financial Risk Assessment
**As of:** 2026-11-17 (price $288.48; market cap ~$41.8B) | **Sector:** Healthcare — Medical Diagnostics & Research
**Current drawdown:** −33.8% from the 2026-10-29 high of $436.00 (attained over 12 trading days)

---

## 1. Credit Risk Assessment — **INVESTMENT GRADE (balance-sheet basis)**

This is the most important finding, and it cuts against the surface-level numbers: **Natera has essentially no debt.**

- Total debt of only **$80.3M**, disclosed by management as a **UBS line-of-credit draw** inclusive of accrued interest (per Q3 2026 results). **No convertible notes remain outstanding** — the $287.5M 2.25% 2027 converts referred to in older filings are no longer part of the capital structure.
- The data vendor's `total_debt` figure of **$238.8M** does not reconcile with either `short_term_debt` ($80.3M) or `long_term_debt` ($0.0). The ~$158.5M residual is almost certainly lease obligations, not funded debt. **Flagged as a data-composition gap** — but the company's own disclosure ($80.3M) is the reliable number.
- **Net cash of $858.4M** (cash & ST investments $1,097.2M less $238.8M gross debt) — approximately **2.1% of market cap on a strict basis, 12.3% of adjusted EBITDA** — i.e., they could extinguish all debt from cash this quarter.
- **Debt/equity 0.13, debt/assets 0.09** — very low absolute leverage.
- **No refinancing cliff.** The only maturity is a revolver; there is no bond wall, no convert wall, no covenant-Driven forced equity raise.
- **Interest coverage is negative on GAAP EBIT** (EBIT −$216.9M TTM / interest $9.8M = **−22x**; the tool's −76x uses FY25). This is a *headline* failure only: cash interest is trivial. On an ex-SBC basis, adjusted EBITDA covers interest **~26x**.

**The correct interpretation:** Natera's credit risk is *not* solvency risk — it is **earnings-quality risk**. The company loses money on a GAAP basis not because of leverage, but because of $397M of annual stock-based compensation and a still-subscale operating structure. That is an equity risk, not a default risk.

- **Altman Z-Score = 1.004 ("Distress")** — I regard this as a **measurement artifact** and explicitly discount it. The book-equity variant delivers X2 = −1.16 (retained-earnings deficit of $2.99B from cumulative losses) and X3 = −0.08. Recomputing X4 at market value ($41.83B equity / $878.9M liabilities = 47.6) gives **Z ≈ 28.3 — deep in the safe zone**. The book Z-score is being driven by the accumulated-loss history of a growth company, not by balance-sheet weakness. This is exactly where a mechanical screen would generate a false credit alarm.
- **Piotroski F-Score = 5/9 (Moderate).** Passes: positive operating cash flow, ROA improvement, accruals quality, positive equity change, gross-margin improvement. Fails: positive ROA, lower leverage, **no dilution (F7)**, asset-turnover improvement.

**Credit rating:** Not rated / no public CDS spread — **data gap**. But on fundamentals this balance sheet would support an investment-grade profile.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Read |
|---|---|---|
| Revenue (TTM to 9/30/26) | **$2,908.9M** | +34.1% y/y (Q3'26 $794.0M) |
| FY26 guidance (raised) | **$3.005–3.035B** | +$140M at midpoint |
| Gross margin (TTM) | **65.2%** | Rising: 64.8% FY25 → 60.3% FY24 → 45.5% FY23 ✅ |
| Operating margin (TTM) | **−7.5%** | Improving from −41.2% (FY23) but still negative ⚠️ |
| Net income (TTM) | **−$164.7M** | Q3'26 loss $59.9M vs consensus −$0.17/sh (actual −$0.39) ⚠️ |
| EBITDA (TTM, GAAP) | **−$139.5M** | Ex-SBC adj. EBITDA ≈ **+$257M (~8.8% margin)** |
| Stock-based comp (TTM) | **$396.9M** | **13.6% of revenue** — the core earnings-quality issue |
| Debt/Equity / Debt/Assets | **0.13 / 0.09** | ✅ |
| Net debt / EBITDA | **Net cash $858M** | Tool's "3.91x" is a sign artifact (net cash ÷ negative EBITDA) — disregard |
| Interest coverage | **−22x (GAAP) / ~26x (adj.)** | Trivial $9.8M cash interest |
| Current ratio / Quick / Cash ratio | **2.81 / 2.66 / 1.79** | ✅ Strong (Q3'26 balance sheet) |
| Working capital | **$1,109.7M** | ✅ |
| Altman Z (book) | **1.00 — Distress** | Artifact; market-cap Z ≈ **28.3 — Safe** |
| Piotroski F | **5/9 — Moderate** | Dilution + negative ROA are the misses |
| FCF yield (TTM $52.5M / $41.8B) | **0.13%** | ✅ negligible return of cash (vendor shows 0.28% on FY25 FCF) |
| Receivables / DSO | **$471.4M / 59.2 days** | Up from 46.9 days at FY25 ⚠️ |
| Goodwill & intangibles / assets | **$494.1M / 18.0%** | Modest, no impairment overhang concern |

---

## 3. Market Risk Profile — **HIGH**

| Metric | Value |
|---|---|
| Annualised volatility (756d) | **48.98%** — very high for a $42B healthcare name |
| Beta vs SPY | **1.315** (vendor profile: 1.515) — amplified market sensitivity |
| Max drawdown (3y) | **−33.83% — occurring right now** (Oct 29 → Nov 16) |
| Sharpe (0% rf, tool) | 1.052; on the actual **4.74% 2Y / 5.13% 10Y** risk-free rate ≈ **0.96** |
| Sortino | **Not provided — data gap** |

**The drawdown deserves separate comment.** The stock is at its worst 3-year drawdown *as of today*: −14.6% on Nov 6 (volume 5.78M, ~3x normal), then a further **−9.6% on Nov 16** with no identified catalyst in my sources. This is a classic high-multiple growth equity in de-rating mode: Q3'26 delivered a **revenue beat and a guidance raise** yet still fell ~20% intraday because the GAAP loss was 2.3x consensus. The market has repriced the company from "growth at a premium" toward "show me the earnings."

**Rate-sensitivity overlay:** with the 10Y at **5.13%** and 30Y at **5.47%** (2s10s +39bp, no inversion), a stock at **~13.9x FY26 revenue with negative GAAP earnings** is a long-duration asset. Every 50bp of upward rate pressure is a direct multiple headwind. This is the mechanism most likely to extend the drawdown toward −50%.

---

## 4. Downside Scenario: Revenue −20% (my base downside)

Applied to TTM revenue of $2,908.9M → **$2,327.1M**

| Line | Base TTM | −20% Revenue (200bp GM compression, 12% opex cut) |
|---|---|---|
| Revenue | $2,908.9M | $2,327.1M |
| Gross profit (65.2% → 63.2%) | $1,896.9M | $1,470.7M |
| Opex (SGA $1,280M + R&D ~$834M) | $2,113.8M | $1,860.1M |
| **EBIT** | **−$216.9M** | **−$389.4M** |
| EBITDA | −$139.5M | −$311.9M |
| Adj. EBITDA (ex-SBC) | +$257M | **+$85M (still positive)** |
| **FCF** | **+$52.5M** | **≈ −$3M to −$80M** |
| Cash | $1,097.2M | $1,097.2M |
| Debt due | $80.3M revolver | $80.3M revolver |

**Assessment: the company survives comfortably.** Even at −20% revenue with *no* opex cuts and *no* working-capital release, FCF burn would be roughly −$150M, implying **7+ years of runway against $1.1B of cash and no funded debt**. A severe −40% scenario (a Signatera reimbursement shock) yields ~−$300M annual burn and still ~3.5 years of runway with zero capital-raise requirement. **There is no liquidity or solvency cliff in any plausible downside.** The risk transfer is entirely to the equity: at 13.9x sales, a −20% revenue reset plausibly compresses the multiple to 6–8x, implying a 45–60% equity decline even though the *business* remains solvent. That is the asymmetry to flag.

---

## 5. FCF Sustainability — **WEAK / DETERIORATING**

This is the most under-appreciated risk in the name.

- TTM FCF **$52.5M** vs FY2025 **$109.1M** — **down 52%** despite revenue up ~34%. FCF margin compressed from **4.7% → 1.8%**.
- Driver: capex **$160.3M TTM vs $106.2M FY25 (+51%)** — capex is now 5.5% of revenue and rising (PP&E $483.4M, up from $349.7M).
- **FCF is entirely an artifact of non-cash compensation.** TTM FCF of $52.5M versus TTM SBC of $396.9M: if SBC were settled in cash, the business consumed **~$345M**. Operating cash flow of $212.8M is manufactured almost precisely by adding back SBC. **FCF yield of 0.13% is the honest number** — investors are receiving essentially no cash return for a $41.8B enterprise.
- Working capital is turning: Q3'26 inventory $91.7M vs $70.7M (+30% q/q on +5.5% revenue growth), receivables +11.7% q/q on +5.5% revenue, and Q3 working capital was a **−$38.1M drag** on OCF. Two consecutive quarters of receivables growing faster than revenue.
- **Mitigant:** gross margin is genuinely expanding (45.5% → 65.2% over three years) and operating leverage is real. Adj. EBITDA is positive and would remain positive in a −20% revenue scenario. The trajectory is right; the *level* of cash generation is not yet sufficient to support the valuation.

---

## 6. Overall Financial Risk Rating: **MODERATE**

- **Balance-sheet / solvency risk: LOW.** $1.1B cash, $80.3M revolver, net cash $858M, current ratio 2.81, no converts, no maturity wall, trivial interest burden.
- **Earnings-quality risk: HIGH.** GAAP loss of $165M TTM, negative operating margin, $397M SBC, dilution of 5.4% y/y (shares 139.7M → 144.3M).
- **Market / valuation risk: HIGH.** 49% vol, beta 1.32, a live −34% drawdown, 13.9x forward revenue, 5.13% 10Y discount rate.
- **Liquidity risk: LOW.** Multiple years of runway in every modeled scenario.

Net: a **solvent, fast-growing, cash-generative-on-an-adjusted-basis business whose equity is priced for a perfection that its GAAP P&L does not yet deliver.** Not a credit story — a duration and earnings-proof story.

---

## 7. Key Red Flags

1. **Q3'26 EPS loss of $0.39 vs $0.17 consensus (−129%)** — revenue beat and guidance raise were overwhelmed by cost/margin reality. Prompted a 14.6–19.7% single-day collapse on 3x volume.
2. **FCF halved** ($109.1M → $52.5M) while revenue grew 34% — capex ramp is outrunning cash generation.
3. **FCF is 100% SBC-manufactured** — $396.9M of non-cash comp vs $52.5M of "free" cash flow. Treat reported FCF as economically immaterial.
4. **Persistent dilution** — shares +5.4% y/y; Piotroski F7 failure. GAAP loss per share will stay elevated even as losses narrow in dollars.
5. **Working-capital deterioration** — inventory +30% and receivables +12% q/q against +5.5% revenue; working capital a −$38.1M OCF drag in Q3.
6. **Live −33.8% drawdown with a −9.6% down day on Nov 16 lacking an identified catalyst** — evidence of fragile, headline-sensitive positioning.
7. **Altman Z of 1.00 will screen as "distress"** — expect mechanical/screening-driven selling that is not grounded in the actual capital structure. Be prepared to explain it.
8. **Valuation has no margin of safety:** ~13.9x FY26 revenue against a −7.5% operating margin.

## 8. Explicit Data Gaps

- **Peer comparables unusable.** `get_sector_peers` returned LLY, JNJ, ABBV, UNH, MRK, NVS — mega-cap pharma, not diagnostics. No valid multiples comparison (EXAS, GH, TXG, ILMN, CRL would be the right set). **Not obtained within budget.**
- **Debt composition unresolved.** Vendor `total_debt` ($238.8M) ≠ short-term ($80.3M) + long-term ($0.0). Management states $80.3M of debt. The gap is presumed to be leases but is unverified.
- **Credit rating and CDS spreads not available** — company appears unrated; no public CDS.
- **Covenant terms on the UBS facility not disclosed** in available data. Assume standard financial covenants; with $1.1B cash, immaterial.
- **Sortino ratio not provided** by the volatility tool.**
- **SBC-buyback offset** not disclosed (no repurchases in the data — consistent with pure dilution).
- **Payer/customer concentration** (Signatera reimbursement, Medicare/Medicaid mix) not quantifiable from the tools — this is the single largest unmodeled idiosyncratic risk.
