# Fin Risk Analyst

- Symbol: CVS
- Elapsed: 82.1s

---
Data gathering is complete. Writing the assessment now.

---

# CVS Health Corp. (CVS) — Financial Risk Assessment

**Sector:** Healthcare / Medical – Healthcare Plans · **Price:** $89.01 · **Market cap:** $113.8bn · **Data as of:** FY2025 audited (period end 2025-12-31); market/credit data current to Nov 2026

---

## 1. Credit Risk Assessment

**Rating: INVESTMENT GRADE — LOW TIER / BORDERLINE** (Baa3 Moody's / BBB Fitch)

| Agency | Rating | Outlook | Source date |
|---|---|---|---|
| Moody's | Baa3 (LT debt), P-3 (ST) | Revised to **Positive** (2026) | 06/30/26 |
| S&P | BBB | Revised to **Stable** from Negative | 2026 |
| Fitch | BBB / F2 | **Negative** | — |

**Interpretation:** CVS sits on the bottom rung of investment grade. Baa3/BBB− is one notch from high-yield, and the consequence of a downgrade is non-trivial: index exclusion, forced selling by IG-only mandates, and materially higher commercial paper roll cost on a business that funds working capital with CP.

**Critical divergence to flag:** Moody's estimates **gross debt/EBITDA ≈ 3.7x at 6/30/26**, versus a peak of 5.0x at YE2024 — i.e. the agencies see meaningful *deleveraging through 2026* that my FY2025 statements do not capture. My tool-derived GAAP leverage of 4.6–7.0x and the agency's 3.7x are not reconcilable without the adjusted-EBITDA bridge. **The FY2025 annuals likely represent the earnings trough, not the current run-rate.** This is the single largest data gap in this report and it cuts *in favor* of the company.

---

## 2. Key Financial Risk Metrics

| Metric | FY2025 | FY2024 | FY2023 | Risk read |
|---|---|---|---|---|
| Revenue ($bn) | 402.07 | 372.81 | 357.78 | Growing +7.8% |
| **Gross margin** | **13.77%** | 13.79% | 15.22% | **Severe compression** |
| Operating income ($bn) | 10.39 | 8.52 | 13.74 | Down 24% vs 2023 |
| Reported EBITDA ($bn) | 9.86 | 13.68 | 18.20 | **−46% in 2 yrs** |
| Net income ($bn) | 1.77 | 4.61 | 8.34 | **−79% vs 2023** |
| Diluted EPS | $1.40 | $3.66 | $6.49 | — |
| Interest expense ($bn) | 3.12 | 2.96 | 2.66 | **+36% in 3 yrs** |
| Total debt ($bn) | 79.95 | 82.92 | 79.39 | Flat |
| Net debt ($bn) | 69.35 | 74.33 | 71.19 | Mildly better |
| **Net debt / EBITDA** | **4.6x – 7.0x** | 5.4x – 6.1x | 3.9x – 5.4x | Range = methodology gap (see note) |
| **Interest coverage (EBIT/int.)** | **3.33x** | 3.08x | 5.20x | **Thin, deteriorating** |
| Coverage on reported EBIT ($5.26bn) | **1.68x** | — | — | Alarming on GAAP EBIT |
| Debt / equity | 1.06x | 1.09x | 1.04x | Stable |
| Debt / assets | 0.32x | 0.33x | 0.32x | Stable |
| **Current ratio** | **0.84** | 0.81 | 0.86 | **Chronically <1.0** |
| Quick ratio | 0.63 | 0.61 | 0.64 | Weak |
| Cash ratio | 0.12 | 0.14 | 0.16 | Thin |
| Working capital | **−$13.98bn** | −$15.96bn | −$11.33bn | Structurally negative |
| Cash ($bn) | 10.60 | 10.99 | 11.46 | Ample absolute |
| Equity / assets | 0.30 | 0.30 | 0.31 | — |
| **Altman Z-Score** | **2.18 (Grey)** | — | — | 0.37 above distress line |
| **Piotroski F-Score** | **4 / 9 (Weak)** | — | — | — |

**Leverage methodology note (important):** the tool computes net debt/EBITDA off the reported EBITDA of $9.861bn → **7.03x**. But reported EBITDA ≠ operating income + D&A ($10.385 + $4.606 = **$14.99bn**), a $5.13bn gap that is *not itemised* in the income statement data (EBIT field of $5.255bn implies ~$5.13bn of below-the-line charges). On an operating-income-based EBITDA the ratio is **4.63x**. The honest answer is that true leverage lies between 4.6x and 7.0x under GAAP, and near 3.7x on the agencies' adjusted basis. **Treat any single leverage figure here as unreliable.**

**Solvency quality:** tangible book value is **deeply negative** — goodwill + intangibles of **$110.99bn** exceed total equity of **$75.38bn** by roughly **$35.6bn**. The entire equity cushion is acquisition goodwill (Signify, Oak Street, Aetna).

---

## 3. Market Risk Profile

| Metric | Value | Context |
|---|---|---|
| Annualised volatility (3y) | **34.03%** | ~1.7x market; elevated for a defensive sector name |
| Beta vs SPY (3y regression) | **0.247** | Very low market sensitivity |
| Beta (profile, 5y) | 0.58 | Range 0.25–0.58 |
| **Max drawdown (3y)** | **−43.98%** | Severe peak-to-trough |
| Sharpe ratio (rf=0) | 0.499 | Mediocre absolute; ok risk-adjusted |
| FCF yield | **6.90%** | Genuinely attractive |

**Profile:** this is a **low-beta, high-idiosyncratic-risk** stock. At beta 0.25–0.58 the market-relative drawdown protection is real, but 34% vol against a 0.25 beta means ~95%+ of the variance is company-specific — medical cost trend, Medicare Advantage rate notices, PBM regulation. **Bullish for a hedged portfolio, hostile for a concentrated one.** A −44% max drawdown inside three years with a 0.25 beta is the signature of policy/earnings-shock risk, not cyclicality. Sharpe of 0.50 is not compensation for that.

---

## 4. Downside Scenario Analysis

**Scenario A — Revenue −20% (mechanical, fixed cost base):**
Revenue $402.07bn → $321.65bn (−$80.4bn). At constant 13.77% gross margin, gross profit falls −$11.07bn against operating income of $10.39bn → **operating income ≈ −$0.69bn**. Interest coverage goes **negative**; net debt/EBITDA becomes meaningless (EBITDA ≈ −$4.7bn ex-D&A add-back). Under this framing CVS is insolvent on an interest-coverage basis. *This overstates reality* — a payer's medical costs are largely variable — but it does quantify how little cushion a 2.6% operating margin provides.

**Scenario B — Revenue −20% (proportional, margin held):**
EBITDA $14.99bn → ~$11.99bn. Net debt/EBITDA → **5.8x** (or ~8.9x on the $9.86bn reported EBITDA base). FCF $7.81bn → ~$6.2bn; dividend of $3.40bn still covered **1.8x**. Survivable, but leverage breaches every agency's 4.0x comfort threshold and the Baa3 rating does not survive it.

**Scenario C — MLR shock (the scenario that actually matters):**
A +200bp medical-loss-ratio deterioration on ~$140bn of Health Care Benefits premium ≈ **$2.8bn pre-tax hit** — 27% of operating income. That single move pushes net debt/EBITDA to ~5.9x, coverage to ~1.9x, and FCF to ~$5.0bn. **This is essentially what happened in 2024–25 and explains the collapse from $6.49 to $1.40 EPS.** It is not a tail scenario; it is the base-case risk.

**Liquidity under stress:** cash $10.60bn against a $3.40bn dividend, $2.83bn capex, and $3.12bn interest = ~$9.35bn of near-fixed cash commitments. Cash alone covers barely one year. **The company is dependent on continuous capital-markets access** — and at a 2Y of 4.74% / 10Y of 5.13% (curve positively sloped, no inversion), refinancing legacy ~3–4% coupons is a permanent earnings headwind: interest expense has already climbed 36% in three years on roughly flat debt.

---

## 5. Overall Financial Risk Rating

# **HIGH** (trajectory improving toward Moderate)

The FY2025 balance sheet earns a High: 4.6–7.0x GAAP leverage, 3.33x coverage, negative tangible equity, a 0.84 current ratio, Altman Z in the grey zone 0.37 above distress, and a 4/9 Piotroski score. Offsetting that: **$7.8bn of FCF, a 6.9% FCF yield, a dividend covered 1.8–2.3x by FCF, and credit agencies actively revising outlooks upward on 2026 deleveraging to ~3.7x gross leverage.** This is a company with a strong cash engine and a weak balance sheet — not a company at risk of failure, but one with very little room for a second medical-cost shock.

---

## 6. Key Red Flags

1. **Negative tangible equity (~−$35.6bn).** Goodwill and intangibles are 147% of equity. Any impairment — Oak Street or Signify are the live candidates — is a direct book-equity hit against an already-thin Altman x4 component.
2. **Gross margin collapse: 16.90% (2022) → 13.77% (2025)** while revenue grew 25%. CVS is buying revenue at deteriorating economics.
3. **Dividend exceeds GAAP earnings 1.9x** ($3.40bn paid vs $1.77bn net income). Covered by FCF, but not by earnings — unsustainable if FCF degrades further.
4. **Interest expense +36% in three years** with $4.07bn short-term debt and 5%+ refinancing rates. A structural, non-operational EPS drag that compounds annually.
5. **One notch from high yield.** Baa3 with Fitch already Negative. A downgrade triggers index exclusion and raises CP costs for a business reliant on short-term funding (current ratio 0.84).
6. **Chronic negative working capital (−$14.0bn)** and current ratio below 1.0 for three straight years — operationally normal for a pharmacy/payer, but it removes a liquidity buffer exactly when one is needed.
7. **Nov 2026 pharmacy separation** — Moody's flagged this as reversing strategic course and *reducing business diversity*, a credit-negative structural change not reflected in any financial statement in this analysis.

## Data Gaps (explicit)

- **FY2026 nine-month results are absent.** All statements are FY2025 annual. Agency commentary implies material 2026 improvement to ~3.7x gross leverage — unreconciled.
- **Debt maturity schedule unavailable.** Only $4.07bn ST debt and isolated notes (e.g. $750mn due 2026, $2.25bn 1.3% due 2027) identified; I cannot construct the refinancing-cliff profile.
- **No CDS spreads, no pension/lease obligations detail, no segment MLR breakdown.**
- **$5.13bn unexplained gap** between operating income ($10.385bn) and the EBIT field ($5.255bn); this materially changes every coverage and leverage ratio.
- Adjusted (non-GAAP) EBITDA bridge not obtainable — the difference between 3.7x and 7.0x leverage.
