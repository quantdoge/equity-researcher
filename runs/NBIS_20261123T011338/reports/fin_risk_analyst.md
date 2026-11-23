# Fin Risk Analyst

- Symbol: NBIS
- Elapsed: 71.6s

---
# NBIS — Nebius Group N.V. | Complete Financial Risk Assessment

**As of:** 2026-11-20 (last close $81.31; market cap $19.5B) | **Latest financials:** Q3 FY2026 (period ended 2026-09-30, filed 2026-11-12)

> **Framing note:** NBIS is no longer a "software" story in risk terms — it is a **leveraged AI-infrastructure build-out with a captive capital-markets funding model**. The relevant question is not whether the business is growing (revenue +571% y/y) but whether the financing structure survives a funding-market or demand interruption. Every conclusion below is organized around that.

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE** (deep high-yield / CCC-profile; no public agency rating available — see data gaps)

The company is **not near-term insolvent** — it has $7.4B cash, no debt maturities until June 2029, and $38.7B of contracted RPO — but its credit profile is structurally dependent on continuous access to capital markets, and its GAAP operating earnings do *not* cover its interest expense.

| Credit signal | Reading | Verdict |
|---|---|---|
| Cash interest vs. operating EBIT | TTM op. income **−$503.5M** vs. interest **$313.2M** → **−1.6x** | ❌ Operations do not cover interest |
| Best single quarter (Q3'26) | Op. income **+$50.4M** vs. interest **$112.5M** → **0.45x** | ❌ Still not covered even at peak |
| TTM EBITDA / interest | $547.3M / $313.2M = **1.75x** | ⚠️ Thin |
| Q3'26 annualized EBITDA / interest | $1,618M / $450M = **3.6x** | ✅ Improving |
| First maturity | June 2029 (converts) | ✅ No near-term cliff |
| Debt structure | Convertible-heavy, 0.50% (2030) / 4.50% (2034) / 2.00% (2029) / 3.00% (2031) + $775M secured GPU facility | ⚠️ Low coupons, weak covenants |

**The interest-coverage picture in detail.** Tail-twelve-month interest expense is $313M and rising steeply — $42.0M → $63.7M → $95.0M → $112.5M across Q4'25–Q3'26, a **2.7x increase in four quarters** as gross debt went from $4.97B to $16.07B. Q3'26 annualizes to ~$450M of cash interest. GAAP operating income turned positive for the first time in Q3'26 (+$50.4M), so coverage is *inflecting* but remains below 1.0x even in the best quarter on record.

**A critical structural deterioration the market has not fully priced: the convertibles are now deeply out of the money.** The $5.75B raised on 2026-08-24 priced when the stock traded ~$210–$220 (it closed at $223.90 that day). With NBIS at $81.31 — **−71.6% from the June high of $286.69** — the conversion options on roughly **$10.0B of convertible principal** (per company filings: first maturity June 2029) are almost certainly worthless. Debt management can no longer treat this as quasi-equity: **$10B converts will have to be cash-refinanced, not converted.** Refinancing $10B of ~2% coupon paper in 2029 at a high-yield rate of ~7–8% implies **+$500–600M of annual interest** — roughly a tripling of the current run-rate — against a company that has never generated positive operating cash flow at scale.

**Equity-as-currency risk.** The company's funding model has relied on issuing equity-linked paper into a rising stock. A 72% drawdown removes that channel precisely when the funding need is largest. This is a classic reflexive credit deterioration pattern: price fall → higher cost of capital → larger external funding need → further dilution.

**Offsetting strengths (genuine, not cosmetic):**
- **$38.7B RPO** backlog and 2027 revenue guidance of $12–13B. Contracted revenue of ~$38.7B against $16.1B gross debt is the single strongest credit mitigant.
- **Gross margin 77.6%** (Q3'26) — incremental revenue converts to EBITDA at very high rates.
- **Demonstrated capital access** — raised $5.75B in August 2026 and $775M secured GPU financing; lenders including ABN AMRO and Bank of America.
- **Asset base:** $21.5B net PP&E of revenue-generating GPU/data-center capacity, financeable on a secured basis.

---

## 2. Key Financial Risk Metrics Table

**Leverage & Solvency**

| Metric | Q3'26 (latest) | FY2025 | FY2024 | Assessment |
|---|---|---|---|---|
| Total debt | **$16.07B** | $4.97B | $0.05B | 3.2x in nine months |
| Cash & ST inv. | $7.43B | $3.68B | $2.45B | Ample but shrinking |
| Net debt | $8.65B | $1.30B | −$2.40B | ✅ Was net cash in FY24 |
| Debt / equity (book) | **1.31x** | 1.08x | 0.05x | ⚠️ |
| Debt / assets | **41.5%** | 40.0% | 1.4% | ⚠️ |
| Net debt / EBITDA — **TTM (ex-one-offs)** | **15.8x** | n/a (neg.) | n/a | ❌ Severe |
| Net debt / EBITDA — **Q3'26 annualized** | **5.3x** | — | — | ⚠️ Borderline HY |
| Net debt / EBITDA — tool output | — | **2.63x** | — | ⚠️ **Stale — pre-dates $11B of 2026 borrowing. Do not use.** |
| Interest coverage (tool, FY25) | — | **−9.95x** | — | ⚠️ Stale |
| Asset coverage | Assets $38.7B / liabilities $26.4B = 1.47x | 1.59x | 1.20x | ✅ |

**Liquidity**

| Metric | Q3'26 | Tool (FY2025) | Assessment |
|---|---|---|---|
| Current ratio | **5.31x** | 3.08x | ✅ Very strong |
| Quick / cash ratio | 5.31x / 3.00x | 3.08x / 2.41x | ✅ |
| Working capital | **$10.66B** | $3.18B | ✅ |
| Cash / short-term debt | **39.6x** | — | ✅ $0.19B current debt only |
| **Cash runway (cash ÷ quarterly FCF burn)** | **$7.43B ÷ $7.57B = ~1.0 quarter** | — | ❌ **The single most important number in this report** |

*Runway caveat: 1.0 quarter is not a solvency statement — capex is discretionary in timing if not in contract — but it quantifies how completely the company depends on rolling capital raises. Q1'26's near-neutral FCF (−$215M) was flattered by a +$2.1B working-capital inflow, not operations.*

**Distress scoring**

| Score | Value | Zone | Caveat |
|---|---|---|---|
| Altman Z-Score | **1.096** | **DISTRESS** (<1.81) | x4 uses *book* equity ($12.3B). Recomputing with market cap ($19.5B) lifts x4 from 0.59 to 2.49 and Z to **≈2.24 — grey zone, not distress**. Treat 1.10–2.24 as the credible range. |
| Piotroski F-Score | **8 / 9** | **Strong** | ⚠️ **Stale and misleading**: computed on FY2025, before the Q3'26 debt ramp. The lone failure is F5 (leverage rose) — and leverage has since roughly tripled. Reflects the upgrading *operating* story, not the current *capital structure*. |

**FCF sustainability**

| Metric | Q3'26 | Q2'26 | Q1'26 | Q4'25 | FY2025 |
|---|---|---|---|---|---|
| Operating cash flow | **−$273M** | +$2,246M | +$2,258M | +$834M | +$385M |
| Capex | **−$7,300M** | −$5,657M | −$2,473M | −$2,056M | −$4,066M |
| **Free cash flow** | **−$7,573M** | −$3,411M | −$215M | −$1,222M | **−$3,681M** |

- **TTM FCF: −$12.42B.** TTM FCF yield: **−63.7%** on $19.5B market cap (tool's −18.28% is FY2025-based and stale).
- Capex is **compounding ~1.4x per quarter** ($2.5B → $5.7B → $7.3B), with 2027 guidance of **$40–45B** — **5–6x current cash on hand**. These are largely committed GPU/data-center procurement obligations.
- FCF margin: **−772% of Q3 revenue.** OCF turned negative in Q3'26 for the first time in five quarters despite revenue up 571% y/y — a working-capital-driven signal worth watching closely.

---

## 3. Market Risk Profile

| Metric | Value | Interpretation |
|---|---|---|
| Annualised volatility (730d) | **115.1%** | ~6–7x the market; among the highest in large-cap tech |
| **Beta vs SPY (730d)** | **2.97** | A 10% market drawdown implies ~30% NBIS decline. ⚠️ *Company profile shows beta 1.56 — a material divergence (different window/source). The computed 2.97 is the more current and more conservative figure; I would underwrite to ~2.5–3.0.* |
| **Max drawdown (730d)** | **−71.6%** | Peak close $286.69 (2026-06-18) → $81.31 (2026-11-20) |
| Sharpe ratio (0% rf) | 1.207 | Looks acceptable *only* because of the Q2'26 melt-up; it is not a risk-quality signal here |
| Recent velocity | **−47.4% in 7 sessions** ($154.69 on 11-Nov → $81.31 on 20-Nov) | Post-Q3 earnings (12-Nov). Volume 69.5M shares on 12-Nov vs. ~15M average — institutional distribution |

**Market risk read:** a beta of ~3 with 115% vol and a live −72% drawdown means the equity offers essentially no downside protection and cannot serve as acquisition currency or collateral at current levels. The −47% seven-session collapse on the Q3 print (despite revenue beating at $980.8M vs. $907.2M est.) confirms the market is now pricing **capex/funding risk, not growth** — a regime change in how the stock is valued.

---

## 4. Downside Scenario Analysis — Revenue −20%

Base = Q3'26 annualized: revenue $3,923M, gross margin 77.6%, opex held flat.

| Line item | Base | Revenue −20% | Change |
|---|---|---|---|
| Revenue | $3,923M | $3,138M | −$785M |
| Gross profit (77.6%) | $3,044M | $2,259M | −$785M |
| Operating income | +$202M | **−$583M** | Turns negative |
| EBITDA | $1,618M | **$833M** | −49% |
| Interest expense | $450M | $450M | Fixed |
| **EBITDA / interest** | 3.6x | **1.85x** | ⚠️ Approaches 1x |
| **Net debt / EBITDA** | 5.3x | **10.4x** | ❌ |
| FCF (pre-capex-flex) | — | deeply negative | — |

**Second-order effects — where the real damage occurs:**

1. **The funding gap becomes unbridgeable rather than merely large.** A 20% revenue shortfall against a $40–45B 2027 capex plan leaves a ~$30B+ external funding requirement against $7.4B cash and $16.1B of existing debt. At $81/share (equity cap $19.5B), an equity solution is arithmetically impossible without near-total dilution. The company would have to cut capex hard — writing off or deferring committed GPU orders and revenue capacity, which further impairs the RPO delivery schedule. **That is the true tail risk: not interest default, but a forced capex retrenchment that breaks the growth contract underpinning the RPO.**
2. **Net leverage of 10.4x closes the unsecured market.** Refinancing the 2029 converts would require secured, covenant-heavy structures at punitive spreads.
3. **Secured-facility covenants likely bind.** If the $775M GPU-backed facility (and any successor secured facilities) carry DSCR or net-leverage maintenance tests, 10.4x net leverage with 1.85x coverage would breach them. *The specific covenant thresholds are not disclosed — this is a genuine data gap and the most important unknown in the credit.*
4. **Convertible covenants are the shock absorber.** Straight converts carry minimal financial maintenance covenants, so the convert-heavy structure materially reduces mechanical acceleration risk. This is why the rating is **High**, not **Critical**.

**What would make it Critical:** a >30% revenue shortfall, loss of investment-grade-style capital access for two consecutive quarters, or an RPO cancellation by a top customer. None of these are in evidence today.

---

## 5. Overall Financial Risk Rating: **HIGH**

**Rationale.** The balance sheet is large, liquid, and free of near-term maturities — this is not a liquidity crisis. But three conditions must hold simultaneously for NBIS to remain solvent without restructuring: (a) capital markets stay open, (b) revenue compounds on plan toward $12–13B in 2027, and (c) the equity price recovers enough to restore the equity-linked funding channel. Q3'26 showed all three weakening at once: cash fell $600M *even after raising ~$6B net*, OCF turned negative, and the stock lost 47% in seven sessions.

**Scorecard:**
| Dimension | Rating | Driver |
|---|---|---|
| Leverage | **High** | 15.8x TTM / 5.3x annualized net leverage; debt up 3.2x in 9 months |
| Liquidity | **Moderate** | $7.4B cash, 5.3x current ratio, no maturities until 2029 — but 1 quarter of runway at current burn |
| Coverage | **High** | Op. EBIT covers interest 0.0x at best; EBITDA 1.75x TTM |
| Market risk | **Critical** | 115% vol, beta 2.97, −71.6% drawdown, −47% in 7 sessions |
| FCF sustainability | **Critical** | TTM FCF −$12.4B; −63.7% FCF yield; capex compounding 1.4x/quarter |
| Covenant/refinancing | **Moderate** | First maturity June 2029; converts have weak covenants — but the 2029 refinancing will reprice ~2% → ~7–8% |

---

## 6. Key Red Flags

1. **🚩 Cash runway of ~1 quarter at the Q3'26 burn rate ($7.43B ÷ $7.57B).** Capex is now 26x annual operating cash flow. The company is a serial capital raiser by necessity, not by choice.
2. **🚩 Convertibles are now out of the money by ~60–70%.** ~$10.0B of principal due from June 2029 must be cash-settled, not converted. The 2029 refinancing reprices $10B from ~2% to a high-yield coupon — an estimated +$500–600M annual interest burden.
3. **🚩 Accounts receivable exploded to $4,040M at Q3'26 from $289M at Q2'26 — a 14x jump.** That is ~375 days of DSO
