# Fin Risk Analyst

- Symbol: INSM
- Elapsed: 74.3s

---
I have sufficient data. The yield curve tool failed twice (I'll flag it), but everything else is covered. Here's the assessment.

---

# INSM — Insmed Incorporated: Financial Risk Assessment

**Company:** Insmed Incorporated (NASDAQ: INSM) · Healthcare / Biotechnology · US
**Market cap:** ~$32.2B · **Price:** $146.93 (Nov 20, 2026 close) · **Employees:** 1,664
**Business:** Commercial-stage biopharma. ARIKAYCE (MAC lung disease) + BRINSUPRI/brensocatib (bronchiectasis, launched 2026) + pipeline (TPIP, PAH).

> **Data vintage note:** The most recent *annual* statements are FY2025 (period-end 2025-12-31). However, *quarterly* statements extend to **Q3 2026 (2026-09-30)**, which is the true "latest" view. I anchor leverage/liquidity commentary on Q3 2026 and TTM figures, not the stale FY2025 annual ratios the tools auto-compute. Where a tool metric is FY2025-only, I flag it.

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE (speculative) — improving, but not investable-grade.**

INSM is a pre-profit, cash-burning commercial biotech, so conventional credit lenses need adjustment. The auto-computed FY2025 metrics look alarming (interest coverage **−14.0x**, Altman Z **−3.96 "Distress"**), but these are **backward-looking and structurally distorted** for a company in launch ramp. The forward-looking picture is materially better:

- **Net cash position, not net debt.** Q3 2026: cash & ST investments **$1,146.6M** vs total debt **$741.2M** → **net cash ~$405M**. The tool's "net debt/EBITDA 0.56" is an artifact of near-zero/negative EBITDA; on a net basis INSM holds net cash.
- **Losses are collapsing fast.** Operating loss by quarter: Q4'25 −$249.7M → Q1'26 −$200.3M → Q2'26 −$1.5M → Q3'26 −$89.4M. Revenue over the same quarters: $263.8M → $306.0M → $425.5M → $524.4M. TTM revenue ~$1.52B vs FY2025 $606M — roughly **2.5x growth in a year**.
- **Interest coverage is negative but small relative to cash.** TTM EBIT −$540.9M / TTM interest $81.4M = **−6.6x**. Interest expense (~$81M/yr) is comfortably covered by the $1.15B cash balance and rising gross profit — cash interest is not a solvency threat.
- **Debt structure:** ~$569.5M of **0.75% convertible senior notes due 2028** (initial conversion ~$32.50/share — deeply in-the-money at $147, so likely equity-settled → dilution, not default) plus ~$172M other debt. **No near-term (2026–27) maturity cliff**; the 2028 convert is the only meaningful refinancing date and is ~2 years out.

**Verdict:** The **credit/solvency risk is moderate, not distress.** The Altman "Distress" reading is a false signal driven by negative retained earnings (−$5.9B cumulative) — expected for a company that has funded R&D with equity. The genuine credit question is *dilution*, not default.

---

## 2. Key Financial Risk Metrics Table

| Metric | Value | Source / Basis | Read |
|---|---|---|---|
| **Leverage** | | | |
| Debt / Equity | 1.02x | Q3'26 ($741.2M / $726.2M) | Moderate; ~half equity-funded |
| Debt / Assets | 0.33x | Q3'26 | Low |
| Net Debt / EBITDA | **Net cash ~$405M** | Q3'26 (cash $1,146.6M − debt $741.2M) | Net cash — no net leverage |
| **Coverage** | | | |
| Interest Coverage (EBIT/Int) | −6.6x (TTM); −14.0x (FY'25) | TTM EBIT −$540.9M / $81.4M | Negative; improving; cash-covered |
| EBITDA (TTM) | −$493.9M | Q4'25–Q3'26 | Negative but narrowing |
| **Liquidity** | | | |
| Current Ratio | 2.86x | Q3'26 ($1,706.5M / $596.6M) | Strong |
| Quick Ratio | 2.59x | Q3'26 (ex-inventory) | Strong |
| Cash Ratio | 1.92x | Q3'26 | Strong |
| Working Capital | ~$1,110M | Q3'26 | Ample |
| **Cash Runway** | | | |
| Cash & ST investments | $1,146.6M | Q3'26 | — |
| Quarterly FCF | −$42.1M (Q3'26) | Q3'26 | Near breakeven |
| Runway @ Q3'26 burn | ~6.8 yrs | $1,146.6M / ($42.1M×4) | Very comfortable |
| Runway @ TTM burn | ~1.7 yrs | $1,146.6M / $657.6M | Adequate; trend improving |
| **Distress / Strength** | | | |
| Altman Z-Score | −3.96 (**"Distress"**) | FY2025 | **Misleading** — neg. retained earnings |
| Piotroski F-Score | 5 / 9 (**Moderate**) | FY2025 | Penalized for dilution & neg. ROA |
| FCF Yield | −3.08% | TTM FCF −$967.6M / mkt cap | Negative; expected for launch ramp |

**Key nuance:** The F-Score's zeros are F1 (positive ROA), F2 (positive operating CF), F3 (ROA improvement), and **F7 (no dilution)** — the dilution flag is the real, valid negative (shares 164M → 213M → 218M over FY24→FY25→Q3'26).

---

## 3. Market Risk Profile

| Metric | Value | Interpretation |
|---|---|---|
| Annualised Volatility | **57.4%** | Very high — top-decile equity risk |
| Beta vs SPY | **0.61** (tool) / 0.81 (profile) | Low *market* beta — idiosyncratic risk dominates |
| Max Drawdown (3-yr) | **−56.5%** | Severe peak-to-trough; typical biotech tail |
| Sharpe Ratio | **0.85** (0% rf) | Decent — but earned via a 7–8x rally, not downside protection |
| 3-yr Price Path | ~$19 (Jan'23) → ~$147 (Nov'26) | Massive re-rating on pipeline/launch |

**Reading:** The low beta (0.61) is deceptive — INSM's risk is **not** market-driven; it is **binary/catalyst-driven** (clinical, regulatory, launch execution). Volatility of 57% and a 56% max drawdown mean drawdowns are brutal and fast. The Nov 19, 2026 session (+20% on 14.4M shares, ~4x normal volume) exemplifies the gap-risk profile. A −56% drawdown is a *live, recent* possibility, not a historical abstraction.

---

## 4. Downside Scenario Analysis — Revenue −20%

**Assumption:** FY2026 revenue guidance ~$1.81–1.87B (BRINSUPRI $1.35–1.40B + ARIKAYCE $460–470M). A 20% shortfall ≈ **−$360M revenue** (e.g., BRINSUPRI launch stumbles or ARIKAYCE pricing/volume pressure).

| Line item | Base (TTM) | −20% Revenue Case | Δ |
|---|---|---|---|
| Revenue | $1,520M | ~$1,216M | −$304M |
| Gross margin (~84%) | $1,281M | ~$1,022M | −$259M |
| Operating income | −$541M | ~−$800M | −$259M |
| FCF | −$658M | ~−$900M to −$960M | −$250M+ |
| Cash (Q3'26) | $1,147M | $1,147M | — |
| **Runway @ stressed burn** | ~1.7 yrs | **~1.1–1.2 yrs** | Shrinks sharply |

**Consequences:**
- **Solvency:** Survives ~12 months on existing cash but would be forced into a **dilutive equity raise or new debt** within 12–18 months. The $405M net-cash cushion buys time but does not eliminate the need to raise.
- **Equity impact:** At ~21x trailing sales ($32B / $1.5B), a 20% revenue miss would likely trigger a **40–60%+ de-rating** — the market cap is priced for flawless launch execution. The financial risk is "moderate"; the *market* risk is "severe."
- **Convertible overhang:** If the stock falls below the ~$32.50 conversion price, the 2028 notes convert to ~$569.5M of *cash* debt due 2028 — a refinancing cliff, though manageable vs. $1.15B cash.
- **Mitigant:** Gross margin is high (~84%) and opex is largely fixed SG&A; revenue growth is the swing factor. A 20% cut is severe but not existential given the cash cushion.

---

## 5. Overall Financial Risk Rating: **MODERATE** (improving trajectory)

**Rationale:** Despite the "Distress" Altman label and negative FCF, INSM is **not** a credit-risk story. It holds **net cash (~$405M)**, **$1.15B liquidity**, **2.9x current ratio**, **no near-term maturity wall**, and **rapidly narrowing losses** (FCF burn −$294M → −$42M across four quarters). The balance sheet can absorb a significant downturn. The elevated risk is **market/valuation risk** (57% vol, 56% max drawdown, 21x sales) and **dilution risk**, not insolvency.

- **Credit/Solvency risk:** **Moderate** (Sub-Investment Grade, improving)
- **Liquidity risk:** **Low** (strong ratios, multi-year runway)
- **Market risk:** **High** (57% vol, −56% max DD, catalyst-driven)
- **Dilution risk:** **High** (shares +33% since FY24; in-the-money converts)

---

## 6. Key Red Flags

1. **Heavy dilution:** Shares outstanding 164M → 213M → 218M (FY24→FY25→Q3'26), +33%. F-Score F7 = 0. In-the-money 2028 converts ($32.50 strike vs $147) add ~17.5M shares (~8%) if equity-settled.
2. **Valuation risk:** ~21x trailing sales ($32B cap / ~$1.5B revenue) — priced for perfect launch; a miss de-rates violently.
3. **Negative FCF still large in absolute terms:** TTM FCF −$658M; FCF yield −3.1%. Burn is narrowing but not yet positive.
4. **Binary/catalyst volatility:** 57% annualized vol, −56.5% max drawdown, low 0.61 beta (idiosyncratic, not market-driven) — gap risk on clinical/regulatory/launch news.
5. **Altman "Distress" is real but misleading:** −$5.9B accumulated deficit drives Z to −3.96; this reflects equity-funded R&D, not imminent default. Do not over-read it.
6. **Convertible refinancing cliff (2028):** ~$569.5M 0.75% notes due 2028 — low coupon but a refinancing/settlement event if the stock declines.

---

## 7. Data Gaps (explicit)

- **US Treasury yield curve unavailable:** `fetch_yield_curve` failed twice (validation error in the tool). Macro rate context (2Y/10Y spread, inversion signal) could **not** be retrieved — this affects discount-rate/refinancing-cost framing only.
- **Press release PDF unreadable:** The Q3 2026 release returned binary PDF data; exact reported cash/debt/interest figures were reconstructed from the structured financial statements and search snippets rather than the primary release.
- **Debt maturity schedule:** Full contractual maturity ladder (beyond the 2028 convert) not itemized; ~$172M non-convert debt maturity unknown.
- **CDS spreads / credit rating:** Not available via tools — no external rating or CDS signal to corroborate the credit view.
- **Peer benchmarking:** Sector peers returned are mega-cap drug manufacturers (LLY, JNJ, ABBV, MRK) — **not** appropriate comparables for a pre-profit biotech; no clean peer set was available. Absolute metrics used instead.
- **Annual vs. quarterly vintage mismatch:** Annual tools compute on FY2025; I used Q3 2026/TTM for the live view. FY2025 auto-ratios (interest coverage −14.0x, net debt/EBITDA 0.56) are stale and should not be used standalone.

---

**Bottom line:** INSM is a **high-growth, high-volatility, net-cash commercial biotech**. Financial-solvency risk is **moderate and improving** — the balance sheet survives a 20% revenue shock for ~12 months and holds ~$405M net cash. The dominant risks are **market/valuation (High)** and **dilution (High)**, not default. The Altman "Distress" score is an artifact of negative retained earnings and should be discounted for a launch-stage biotech.
