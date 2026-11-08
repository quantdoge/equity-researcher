# Fin Risk Analyst

- Symbol: SITM
- Elapsed: 83.1s

---
## SITM — SiTime Corporation | Financial Risk Assessment
**Price $416.92 (6-Nov-26) · Market cap $12.54B · EV ≈ $13.53B · Sector: Technology / Semiconductors**

> **Critical context — the balance sheet is not what the annual data shows.** SiTime closed the acquisition of Renesas' timing business (TPD) for $1.5B cash + 3.56M shares in Q3'26, funded by $1.35B of 0% convertible notes (May'26, due June 2031, capped call cap price $1,734.15). Between 31-Mar-26 and 30-Sep-26 the company went from **$496M net cash to $995M net debt**, and goodwill/intangibles rose from $229M to **$4.16B (83% of assets)**. All annual metrics (FY2025) are pre-acquisition and are marked as stale below.

---

### 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE** (unrated; indicative BB–/B+ equivalent)

The credit is not liquid, but it is *solvent-with-a-2031-cliff*. The mitigants are real: the $1.35B of debt is a **single 0% coupon bullet due June 2031** — no cash interest drain, no amortisation, **no refinancing before mid-2031**. The risks are equally real: leverage against *earnings* is extreme (net debt/EBIT 44x), tangible equity is **negative**, and the converts are deeply out of the money, so equity conversion will not happen on current prices — the bullet must be paid or refinanced in cash, against $324M of cash (24% coverage).

| Metric (pro forma Q3'26) | Value | Read |
|---|---|---|
| Total debt / cash | $1,319M / $324M | Net debt $995M |
| Net debt / EBITDA (TTM) | **7.7x** | EBITDA $129M incl. $106.6M D&A |
| Net debt / EBIT (TTM) | **44x** | EBIT only $22.5M |
| EBIT / interest (TTM) | **3.1x** | Thin; interest is non-cash amortisation |
| Debt / equity · Debt / assets | 0.38x · 26.5% | Equity inflated by goodwill |
| **Tangible book equity** | **–$663M** | Equity $3,493M – intangibles $4,156M |
| Altman Z (my pro forma calc) | **1.63 = Distress zone** | vs. tool's FY2025 5.71 (pre-deal) |
| Piotroski F (FY2025) | 7/9 → **est. 4–5 pro forma** | Leverage + turnover tests now fail |
| Cash / convert principal | 24% | $1.35B due 6/2031 |

**Z-score reconciliation (own calculation, flagged as analyst estimate):** X1 0.108, X2 –0.042, X3 0.005, X4 2.35, X5 0.137 → **Z = 1.63 (distress)**. Using market cap for X4 = 8.43 → Z ≈ 5.3. The entire difference is equity valuation: **the balance sheet only passes the solvency test if the market cap holds.**

---

### 2. Key Financial Risk Metrics

| | FY2023 | FY2024 | FY2025 | TTM Q3'26 |
|---|---|---|---|---|
| Revenue ($M) | 144.0 | 202.7 | 326.7 | **683.0** |
| Gross margin | 57.0% | 51.6% | 53.6% | 56.2% |
| Operating income ($M) | –107.2 | –115.2 | –60.4 | **+16.6** |
| Net income ($M) | –80.5 | –93.6 | –42.9 | +26.5 |
| FCF ($M) | –4.2 | –13.0 | +34.7 | **+39.6** |
| SBC ($M, % rev) | 76.8 (53%) | 92.6 (46%) | 103.5 (32%) | **121.2 (17.7%)** |
| Capex ($M) | 12.2 | 36.2 | 52.5 | 50.2 |
| Cash ($M) | 528 | 419 | 808 | **324** |
| Total debt ($M) | 8.0 | 6.2 | 4.7 | **1,319** |

- **Liquidity: strong.** Current 5.56x, quick 4.62x, cash/CL 2.74x, WC +$539M (vs 11.3x current ratio on the stale FY2025 balance sheet).
- **FCF sustainability: poor quality.** TTM FCF of +$39.6M is entirely an SBC add-back: **FCF ex-SBC = –$81.6M**. FCF yield 0.32%. Q3'26 operating cash flow was **–$6.6M** on a $126.5M working-capital build.
- **Earnings quality:** Q3'26 GAAP EPS $0.14 vs. **non-GAAP $4.01** — ~$121M of quarterly adjustments (SBC + acquired-intangible amortisation). D&A annualised at ~$280M post-deal; the acquired business carries a low GAAP operating margin (Q3'26 EBIT margin 2.8%).
- **Cyclicality precedent:** revenue fell **–49%** from FY2022 ($283.6M) to FY2023 ($144.0M). A demand drawdown of this magnitude is not hypothetical for this company.

---

### 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility (3y) | **84.5%** |
| Beta vs SPY | **2.77** (profile: 2.91) |
| Max drawdown (3y) | **–60.6%** |
| Sharpe (rf=0) | 0.997 |
| Sortino | Not provided — **data gap** |
| Current drawdown from 11-May-26 peak ($901.48) | **–53.8%** |
| 1-day moves post-Q3 print | –12.0% (5-Nov), **+17.4%** (6-Nov) |

Beta ~2.8 with 84% vol means a 20% market drawdown mechanically implies a 40–55% equity decline before any idiosyncratic news. The stock is a high-torque, AI-datacenter/communications-timing levered beta; its own 6-month record (–54%) already demonstrates the tail.

---

### 4. Downside Scenario: revenue –20%

Applied to TTM revenue of $683M (–$136.6M), with gross margin compressing 420bps to 52% and OpEx cut 5%:

| | Base TTM | –20% revenue |
|---|---|---|
| Revenue | $683.0M | $546.4M |
| Gross profit (56.2% → 52.0%) | $384.1M | $284.1M |
| OpEx (incl. $106.6M D&A) | $367.5M | $350.0M |
| **EBIT** | **+$16.6M** | **–$65.9M** |
| EBITDA (EBIT + D&A) | $129.1M | $40.7M |
| **Net debt / EBITDA** | 7.7x | **24.4x** |
| FCF (EBITDA – capex – cash interest) | +$39.6M | **≈ –$5M** |
| FCF ex-SBC | –$81.6M | ≈ –$126M |

**What this scenario does and doesn't do.** It does *not* create a liquidity crisis: the coupon is 0%, there is no amortisation, and $324M of cash plus a 5.6x current ratio covers a multi-year burn. It *does* (a) push net leverage to ~24x EBITDA / negative on EBIT, (b) guarantee a goodwill impairment against a $4.16B intangible base that already exceeds book equity — a 25% write-down ($1.04B) would cut book equity 30% to $2.45B and lift debt/equity to 0.54x, and (c) confirm the $1.35B 2031 bullet must be refinanced in cash at a moment when the equity is far below the ~$900 conversion price.

---

### 5. Overall Financial Risk Rating: **HIGH**

Upgraded from what the raw FY2025 statements imply (net cash, Z=5.7) to **High** on the post-acquisition reality: 7.7x net leverage, 44x net debt/EBIT, negative tangible equity, SBC-dependent cash flow, and a 2031 convert wall. **Not Critical**, because there is no maturity, covenant test, or cash-interest obligation inside the next four-plus years and liquidity is genuinely ample.

---

### 6. Key Red Flags

1. **Leverage regime change:** net cash +$804M → net debt $995M in two quarters; net debt/EBIT 44x.
2. **Negative tangible book equity (–$663M)**; goodwill/intangibles 83% of assets — impairment would directly attack the only equity cushion.
3. **FCF is an accounting artefact:** TTM FCF +$39.6M vs. **–$81.6M ex-SBC**; SBC 17.7% of revenue and still rising in dollars.
4. **GAAP/non-GAAP divergence of ~$121M in a single quarter** ($0.14 vs $4.01 EPS) — amortisation and SBC are real economic costs of the acquired business.
5. **Convert structure is a 2031 cliff, not equity:** conversion price ≈$900 vs $417 spot; capped call caps value at $1,734. There is no realistic equity conversion at current prices, and cash covers only 24% of the $1.35B bullet.
6. **Acquisition-integration and pro-forma quality risk:** only one full quarter (Q3'26) of consolidated data; reported EBITDA lines are internally inconsistent (Q3'26 D&A shown as $0 on the income statement vs $69.8M in the cash flow), so my EBITDA/leverage figures are reconstructions.
7. **Extreme market risk:** 84.5% vol, beta 2.77–2.91, –53.8% from peak in six months, ±12–17% earnings-day moves.
8. **Dilution:** shares 26.3M → 30.1M (+14%) from deal consideration, plus latent convert dilution on any recovery.
9. **Valuation leaves no margin of safety:** 18.4x TTM sales / 9.3x annualised Q4 guidance ($331–341M) and ~105x TTM EV/EBITDA — the downside scenario is a de-rating risk as much as a credit risk.

### 7. Data Gaps (flagged)
- **No public credit rating or CDS spread** available; my BB–/B+ equivalent is inferred from ratios.
- **No debt maturity schedule / covenant package** — I assume standard convertible terms: single bullet, no maintenance covenants, no put rights. Unverified.
- **Goodwill vs. intangibles not separable** in the reported balance sheet (combined $4.16B), so impairment sensitivity is directional only.
- **Sortino ratio** not computed by the tool; **quarterly balance sheet history limited to 4 periods**, so no leverage trend before Q1'26.
- **Segmental gross margin** of the acquired TPD business not disclosed in the feed — the 52% downside margin is an assumption.
- FY2025/FY2024 annual metrics (Z-score 5.71, F-score 7) are **stale and should be disregarded** for credit purposes.
