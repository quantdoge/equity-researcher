# Fin Risk Analyst

- Symbol: NTRA
- Elapsed: 34.2s

---
## Natera, Inc. (NTRA) — Financial Risk Assessment

**Sector:** Healthcare / Medical Diagnostics & Research · **Market cap:** $44.78B · **Price:** $310.67 · **FY end:** 2025-12-31 (10-K filed 2026-02-27)

---

### 1. Credit Risk Assessment — **STRONG (Investment-Grade-quality balance sheet, unrated)**

NTRA carries **$862M of net cash** ($1,076M cash vs. $214M total debt) against a $44.8B market cap. There are **zero long-term debt maturities** — the entire debt stack is $80.3M short-term plus ~$134M of leases/finance obligations. Interest expense has collapsed from $12.6M (2023) to $4.1M (2025) as converts converted to equity, and is now dwarfed by interest income on the $1.08B cash pile.

**Critical caveat on the reported ratio:** the tool returned `net_debt_to_ebitda = 3.91`, which is **materially misleading**. That figure is net debt (−$862M) divided by EBITDA (−$221M) — both negative, so the sign flips positive. Economically, **the leverage multiple is undefined because EBITDA is negative.** On a gross basis debt/EBITDA is ~1.0x and falling. Do not read "3.9x" as leverage.

The same mechanical problem drives `interest_coverage = −76.2x` (EBIT/interest). Coverage is formally negative because EBIT is negative, **not** because debt service is strained — annual interest of $4.1M is an immaterial claim. Similarly, `z_score = 0.819 (Distress)` is an artifact of book-value equity and a $2.78B accumulated deficit (retained earnings/assets = −1.107). Restating x4 at market cap ($44.8B / $796M = 56.3x) produces **Z ≈ 23.6, deep safe zone**. I regard the Altman distress flag as **not economically meaningful** for this company, and I am overriding it — but I am flagging that a screen running on raw Z-score would wrongly exclude NTRA.

No published credit rating or CDS spread is available (**data gap**).

---

### 2. Key Financial Risk Metrics

| Metric | 2025 | 2024 | 2023 | Assessment |
|---|---|---|---|---|
| Revenue ($M) | 2,306.1 | 1,696.9 | 1,082.6 | +35.9% y/y; 41% 3-yr CAGR |
| Gross margin | 64.8% | 60.3% | 45.5% | Sharp structural improvement |
| Operating income ($M) | **−309.9** | −222.3 | −446.2 | Still loss-making at $2.3B revenue |
| Operating margin | −13.4% | −13.1% | −41.2% | Improving but not yet positive |
| Net income ($M) | **−208.2** | −190.4 | −434.8 | Widened in absolute terms |
| SG&A (% rev) | 51.1% | 49.6% | 57.1% | Re-leveraging in 2025 |
| R&D (% rev, derived) | 27.2% | 23.8% | — | Investment ramping |
| Total debt / equity | 0.13x | 0.16x | 0.58x | Deleveraged via conversion |
| Total debt / assets | 0.09x | 0.11x | 0.31x | Low |
| Net debt | **−861.8** (net cash) | −758.5 | −200.1 | Net cash every year |
| Net debt / EBITDA | **n/m** (neg. EBITDA) | n/m | n/m | Ratio meaningless |
| EBIT / interest | negative (n/m) | negative | negative | Interest immaterial ($4.1M) |
| Altman Z (book) | 0.819 | — | — | Distress zone, mechanically |
| Altman Z (mkt-cap x4) | **≈23.6** | — | — | Safe zone |
| Piotroski F-Score | **5 / 9** | — | — | Moderate |
| Current / quick / cash ratio | 3.39 / 3.24 / 2.44 | — | — | Very strong |
| Working capital ($M) | 1,055.7 | — | — | 42.9% of assets in cash |
| Assets / liabilities | 3.15x | 3.57x | 2.13x | Deteriorated on M&A |

**Piotroski detail (5/9):** passes on positive operating cash flow, improving ROA, clean accruals (OCF > net income), rising equity, and gross-margin expansion. **Fails** on negative ROA, rising leverage (the Foresight acquisition), share dilution, and declining asset turnover. This is a genuine "improving but not self-funding" profile.

---

### 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility (756d) | **48.5%** |
| Beta vs SPY (756d calc) | 1.28 |
| Beta (profile field) | 1.534 |
| Max drawdown (3yr) | 28.75% |
| Sharpe (rf = 0%) | 1.105 |
| FCF yield | **0.26%** |
| P/S (FY25) | 19.4x |
| EV/FCF | **~402x** |

Risk-adjusted returns look acceptable on the surface (Sharpe 1.1, max drawdown only 28.8%), but these are **backward-looking and flattered by a stock trading near highs**. At 48.5% volatility and beta 1.28–1.53, a market drawdown of −20% implies a −26% to −31% move in NTRA before any idiosyncratic event. A 1-sigma annual adverse move is roughly −48%. The 28.75% max drawdown is almost certainly understated relative to the true tail — a 48.5%-vol name should have experienced materially deeper troughs, so I treat the drawdown figure as **window-dependent and unreliable**.

The real market risk is **valuation, not volatility**: 19.4x sales and ~402x EV/FCF price in sustained ~30%+ growth *and* margin expansion. There is no valuation cushion to absorb a growth disappointment. **Sortino ratio not available (data gap).**

---

### 4. Downside Scenario Analysis — Revenue −20%

Revenue falls to **$1,845M**. Gross margin compresses ~290bp to 62.0% on lab-utilization deleverage → gross profit **$1,144M**. Opex ($1,805M in 2025, 78.3% of revenue) is cut ~12% via variable comp and discretionary spend → **$1,589M**.

| | Base 2025 | −20% Revenue | Severe (−30%, GM 58%) |
|---|---|---|---|
| Revenue | 2,306 | 1,845 | 1,614 |
| Gross profit | 1,496 | 1,144 | 936 |
| Opex | 1,805 | 1,589 | 1,550 |
| Operating income | (310) | **(445)** | **(614)** |
| SBC (cash add-back) | 354 | ~280 | ~250 |
| Operating cash flow | 215 | ~(122) | ~(320) |
| Capex | (106) | (70) | (60) |
| **Free cash flow** | **109** | **~(192)** | **~(380)** |
| Cash balance | 1,076 | 1,076 | 1,076 |
| **Cash runway** | n/a (FCF+) | **~5.6 yrs** | **~2.8 yrs** |

**Conclusion: the company survives a severe 20–30% revenue decline without refinancing risk.** $1.08B of cash, zero long-term maturities, and $80M of near-term debt mean no covenant breach, no refinancing cliff, and no default scenario inside three years. A severe case would force an equity raise — dilutive, not existential, and NTRA has demonstrated market access (converts in 2023, ATM issuance, shares up 38.9% since 2022).

The vulnerability is **not solvency — it is the equity**. In the −20% case, the stock at 19.4x forward sales would re-rate violently; a 50–60% drawdown is entirely plausible even though the balance sheet is untouched.

---

### 5. Overall Financial Risk Rating: **MODERATE**

Split verdict: **Low credit risk, Low liquidity risk, High market/valuation risk, Moderate earnings-quality risk.** The balance sheet is genuinely fortress-like. The company's *income statement quality* and *shareholder value retention* are the weak links, not its solvency.

---

### 6. Key Red Flags

1. **Stock-based compensation is the entire FCF story.** SBC of **$354M = 15.4% of revenue and 3.2x reported FCF**. Adjusted FCF (FCF − SBC) is **−$245M**, an adjusted FCF yield of **−0.58%**. Reported positive FCF of $109M is essentially an SBC artifact — the cash-flow statement adds back a $354M non-cash charge that is a real economic transfer to employees.
2. **Persistent dilution:** shares outstanding 98.4M (2022) → 136.7M (2025), **+38.9%, ~11.6% CAGR**. Piotroski flags this (F7 = 0). Per-share value creation is materially weaker than headline revenue growth suggests.
3. **Still loss-making at scale:** GAAP operating loss of −$310M and net loss of −$208M on $2.3B of revenue. Opex is growing faster than gross profit (SG&A up 40% y/y vs. gross profit up 46% — narrowing).
4. **Valuation with no margin of safety:** 19.4x P/S, ~402x EV/FCF, 0.26% FCF yield. Any growth deceleration triggers a de-rating, regardless of credit strength.
5. **New $515M goodwill/intangibles (from $0 in 2024)** — driven by the **Foresight Diagnostics acquisition (4 Dec 2025, $141.1M goodwill)**. Asset/liability coverage fell from 3.57x to 3.15x and equity/assets from 72% to 68%. Untested impairment exposure; PPA accounting to be watched.
6. **Reimbursement repricing risk** on the growth engine: the 10-K notes Medicare Part B CLFS rates for Signatera are set from a **volume-weighted median of private payer rates**, leaving revenue per test exposed to payer-mix shifts and rate resets. This is the single biggest threat to the 64.8% gross margin.
7. **Altman Z-score screens as "Distress" (0.819)** — I judge this a false positive driven by a $2.78B accumulated deficit and book-value equity, but any mechanical credit screen will flag NTRA.
8. **Aggressive capex ramp:** $106M (2025) vs. $66M (2024), +60% — consuming FCF as the lab footprint expands.

---

### Data Gaps & Caveats

- **No credit rating or CDS spread available** — credit assessment inferred from balance-sheet ratios only.
- **Peer multiples unavailable:** `get_sector_peers` returned mega-cap pharma (LLY, JNJ, ABBV, MRK, UNH, NVS), not diagnostics comparables. No peer benchmarking performed.
- **Sortino ratio not provided** by the volatility tool.
- **R&D expense derived by subtraction** (gross profit − SG&A − operating income), not directly reported.
- **Total debt ($214M) exceeds short-term + long-term debt ($80M + $0)** by ~$134M, implying leases/finance obligations not broken out.
- **2026 guidance not captured** — the earnings release fetch truncated before the outlook section.
- Reported `net_debt_to_ebitda` (3.91) and `interest_coverage` (−76.2x) are mathematically correct but **economically meaningless** given negative EBITDA; both are overridden in this analysis.
