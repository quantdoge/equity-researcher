# Fin Risk Analyst

- Symbol: HUM
- Elapsed: 68.5s

---
I have sufficient data. Writing the assessment now.

---

# HUM — Humana Inc. | Financial Risk Assessment
**Sector:** Healthcare — Managed Care (Medicare Advantage) | **Market cap:** $46.3B | **Price:** $385.71 | **Data through:** Q3 FY2026 (filed 2026-11-06)

---

## 1. Credit Risk Assessment

**Rating: INVESTMENT GRADE — LOWEST TIER (BBB-/Baa2), NEGATIVE OUTLOOK. Sub-investment-grade risk is elevated and rising.**

| Agency | Long-term | Short-term | Note |
|---|---|---|---|
| S&P | BBB | A-2 | Affirmed 13-Oct-2026; **outlook Negative** (lower quality bonus payments pressuring 2026–27) |
| Moody's | Baa2 | P-2 | |
| Fitch | **BBB-** | **F3** | F3 short-term downgraded 15-Dec-2025; BBB- is one notch above junk |
| A.M. Best | BBB | AMB-2 | |

HUM is split-rated at the very bottom of investment grade. Fitch's long-term BBB- and its **F3 short-term rating on a $5B commercial paper programme** mean the company's access to cheap short-dated funding has already been impaired — a classic early credit-deterioration signal.

**Coverage is the binding constraint.** Operating income / interest = **2.30x** in FY2025 and **2.64x** on a trailing-twelve-month (TTM) basis, versus **4.74x for UNH**. EBITDA/interest is 4.3x. At a 1.1–1.3% operating margin, a single adverse medical-loss-ratio (MLR) quarter erases a full year of earnings — as happened in Q4 FY2025 (operating loss of **–$1,025M**) and Q4 FY2024 (**–$899M**). Two consecutive fourth-quarter operating losses is a structural earnings-quality problem, not a one-off.

**Leverage is manageable but the trend is only recently repaired.** Net debt of **$5.57B** at Q3 FY2026 = **1.72x** TTM EBITDA, down sharply from 3.00x at FY2025 year-end after a ~$1.7B debt paydown in Q3 (total debt $14.25B → $12.50B). Debt/equity 0.66x, debt/assets 21.8%.

**Scoring models are unreliable here.** Altman Z-Score of 3.91 ("Safe") is a false signal: x1 is negative (–0.058) and x5 asset turnover (2.66) is inflated by a low-margin premium base. The same model scores UNH — a materially stronger credit — at 2.28 ("Grey"). I therefore **discard the Z-Score** as non-diagnostic for insurance balance sheets. Piotroski F-Score of **6/9 (Moderate)** is more informative; it loses points on ROA improvement, accruals quality and gross-margin improvement.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Basis | Assessment |
|---|---|---|---|
| Total debt | $12.50B | Q3 FY26 | |
| Net debt | $5.57B | Q3 FY26 | |
| **Net debt / EBITDA** | **1.72x** / 3.00x | TTM / FY25 | Moderate, improving |
| Debt / equity | 0.66x / 0.73x | Q3 FY26 / FY25 | Acceptable |
| Debt / assets | 21.8% / 27.0% | Q3 FY26 / FY25 | Acceptable |
| **Op. income / interest** | **2.64x** / 2.30x | TTM / FY25 | **Weak** (UNH 4.74x) |
| EBITDA / interest | 4.3x | TTM | Adequate |
| **Operating margin** | **1.29%** / 1.12% | TTM / FY25 | **Very weak** (UNH 4.24%) |
| Current ratio | 1.65x / 0.72x | Q3 FY26 / FY25 | See note ⚠ |
| Cash (net-debt basis) | $6.94B | Q3 FY26 | |
| Cash + investments | $25.11B | Q3 FY26 | Large buffer |
| Working capital | –$2.84B | FY25 | Structural for insurers |
| Assets / liabilities | 1.57x | FY25 | Thin |
| Goodwill + intangibles | $10.55B | Q3 FY26 | **56% of equity** — impairment risk |
| **Altman Z** | 3.91 "Safe" | FY25 | **Not reliable** (insurer) |
| **Piotroski F** | **6/9** Moderate | FY25 | Neutral |
| **FCF yield** | **0.8%** / ~1.6% | FY25 / TTM | **Poor** |

⚠ **Data-definition flag:** the FY2025 annual balance sheet reports "cash & ST investments" of $4.20B (current ratio 0.72x), while the Q3 FY2026 row reports $25.11B (current ratio 1.65x) — the quarterly field evidently captures total cash *plus* the investment portfolio. I have reconciled net debt consistently within each period (Q3 FY26: $12,504M debt – $6,935M implied cash = $5,569M). The FY2025 current ratio of 0.72x **materially understates** true liquidity; treat the quarterly 1.65x as the better estimate.

---

## 3. Market Risk Profile

| Metric | Value | Read |
|---|---|---|
| Annualised volatility (756d) | **47.6%** | Extreme for a $46B large cap (~3x market) |
| Beta vs SPY (756d daily) | **0.48** | Low systematic sensitivity |
| Beta (company-reported, 5Y monthly) | 0.744 | Moderate |
| Max drawdown (3Y) | **47.7%** | Severe |
| Sharpe ratio (0% rf) | 0.478 | Positive but modest |

**Critical structural insight:** with vol of 47.6% and a beta of 0.48 against ~16% market vol, systematic risk is only ~7.7pp of the 47.6% total — **roughly 97% of HUM's variance is idiosyncratic**. Humana is a *defensive business with a speculative stock*. Low beta does **not** mean low risk here: diversification provides almost no protection, and drawdowns are driven by company-specific events (star ratings, MLR surprises, guidance resets) that hit in single sessions. Position sizing should reflect total vol, not beta.

Sharpe of 0.478 over three years is flattered by the starting point; a 47.7% peak-to-trough decline is a genuine capital-impairment event for a levered holder.

---

## 4. Downside Scenario Analysis — Revenue –20%

**Base (TTM Q4'25–Q3'26):** Revenue $154,185M; gross profit $20,063M (13.0%); operating income $1,989M (1.29%); EBITDA $3,238M; interest $753M; net income $1,245M.

**Assumptions:** medical costs scale with premium (MLR held at ~93.9%, its Q3 FY26 level); 55% of the ~$17.3B cash operating cost base is fixed; D&A $763M held flat.

| Line item | Base TTM | **–20% revenue** | **Severe (–20% rev + 200bp MLR)** |
|---|---|---|---|
| Revenue | $154,185M | $123,348M | $123,348M |
| Gross profit | $20,063M | $16,050M | $13,583M |
| Fixed opex | ~$9,521M | $9,521M | $9,521M |
| Variable opex | ~$7,790M | $6,232M | $6,232M |
| D&A | $763M | $763M | $763M |
| **Operating income** | **$1,989M** | **–$466M** | **–$2,933M** |
| Interest | $753M | $753M | $753M |
| **Net income (21% tax)** | **$1,245M** | **–$963M** | **–$3,084M** |
| EBITDA | $3,238M | $297M | –$1,700M |
| Net debt/EBITDA | 1.72x | **18.8x** | **n.m. (negative)** |
| EBITDA/interest | 4.3x | **0.4x** | **negative** |
| Equity | $18,888M | $17,925M | **$15,804M (–16%)** |

**Interpretation:** a 20% revenue shock pushes the company to a **~$0.5B operating loss before any MLR deterioration**, because the 1.29% operating margin has almost no absorption capacity. With normal utilisation-driven MLR drift (+200bp, worth ~$2.5B on the smaller premium base), the pre-tax loss approaches **$3B** and equity falls ~16%.

**Survivability:** yes, on the balance sheet — $6.94B of cash plus a ~$18B investment portfolio covers a multi-year stress, and equity of $18.9B absorbs a $3B loss. But **credibility with rating agencies breaks long before solvency does**: coverage below 1.0x and leverage above 18x would trigger immediate multi-notch downgrades, a loss of the CP programme, and likely a dividend suspension. This is a *ratings-and-refinancing* downside, not a bankruptcy downside.

**Liquidity runway:** stress cash burn of ~$2.5–3.0B/yr → ~2.3–2.8 years on cash alone; the investment portfolio extends this substantially, though a large share of it backs state-regulated insurance subsidiaries and cannot be freely upstreamed (see gap note).

---

## 5. Overall Financial Risk Rating: **HIGH**

Not Critical — there is no near-term solvency or refinancing wall, leverage is 1.72x, and $25B of cash and investments stands against $12.5B of debt. But **High** is warranted because:

- Operating margin of **1.1–1.3%** leaves zero buffer against MLR volatility, and the company has posted two Q4 operating losses in two years.
- Interest coverage of **2.3–2.6x** is the weakest in the large-cap managed-care peer set (UNH 4.74x).
- FCF has collapsed from $3.45B (FY22) to **$375M (FY25)**, with TTM FCF of only **$747M** — an FCF yield of 0.8–1.6%.
- Ratings sit at the **bottom rung of investment grade** with a negative outlook and an already-downgraded short-term rating.
- Total return volatility of **47.6%** with ~97% idiosyncratic risk.

**Mitigants:** the FY2027 star-ratings improvement (4.17 stars; 95% of MA members in 4★+ plans, +20% y/y), raised FY2026 adjusted EPS guidance to ≥$9.50, Q3 FY2026 medical cost relief, and a $1.7B Q3 debt paydown.

---

## 6. Key Red Flags

1. **Razor-thin margin, fat-tail earnings.** 1.12–1.29% operating margin means a 100bp MLR miss is a ~$1.5B swing — larger than annual operating income. Q4 FY25 operating loss –$1,025M; Q4 FY24 –$899M.
2. **Coverage erosion.** Operating income/interest 2.30x (FY25); interest expense rose **+49% quarter-over-quarter** ($146M → $217M in Q3 FY26) *despite* a $1.7B debt paydown — evidence of refinancing at materially higher coupons.
3. **FCF deterioration.** $3,450M → $2,977M → $2,391M → **$375M** (FY22–FY25). FY2025 dividends of $430M **exceeded** FY2025 FCF of $375M. TTM FCF of $747M covers the $429M dividend only 1.7x — thin.
4. **Extreme cash-flow volatility.** Quarterly operating cash flow: –$1,652M → +$1,254M → –$426M → +$2,163M. Working-capital swings of ±$2B per quarter make FCF unforecastable.
5. **Ratings at the cliff edge.** Fitch BBB-/F3 with the short-term rating already cut; S&P outlook Negative. A downgrade to BB+ would raise funding costs and could force collateral/CP backstop changes.
6. **Earnings quality.** Q3 FY2026 GAAP EPS of $1.33 against an **adjusted loss of $0.70/share** — a ~$2.03/share (~$245M) gap, meaning GAAP results are flattered by non-operating items.
7. **Goodwill/intangibles at $10.55B = 56% of equity** — a large impairment candidate if MA economics deteriorate.
8. **Structural negative working capital** (–$2.84B) — normal for an insurer, but it means liquidity depends on claims-payment timing, not on a current-asset cushion.
9. **Star-ratings fragility.** The ~$3.5B 2026 quality-bonus hit demonstrates revenue/profit dependence on a single regulatory quality metric.

---

## Data Gaps (explicitly flagged)

- **No debt maturity ladder** — cannot assess the refinancing cliff year-by-year; only Q3 FY26 short-term debt ($949M) and long-term debt ($11,555M) are available.
- **No covenant detail** and **no CDS spreads** — credit-market pricing of HUM risk is unobserved here.
- **No insurance-subsidiary RBC ratios or parent-company cash** — critical for judging true holding-company liquidity; the $25.1B cash+investments figure is not all upstreamable.
- **Balance-sheet definition inconsistency** between annual and quarterly "cash" fields (see ⚠ above) — I used net-debt figures as internally reported per period.
- **SG&A fields are zero in Q1 and Q4 quarters**, so the fixed/variable cost split in the downside scenario is an assumption (55% fixed), not a disclosed figure.
- **Peer benchmarking limited to UNH**; CI, ELV and CVS were not retrieved within budget, so peer-relative conclusions rest on a single comparable.
