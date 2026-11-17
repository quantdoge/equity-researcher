# Fin Risk Analyst

- Symbol: MOH
- Elapsed: 83.2s

---
# MOH — Molina Healthcare, Inc. Financial Risk Assessment
**Sector:** Healthcare / Managed Care (Medicaid, Medicare, Marketplace) | **Mkt cap ≈ $12.2B** | **Employees 19,000**

---

## 1. Credit Risk Assessment — **SUB-INVESTMENT GRADE**

**S&P ICR: 'BB-', stable outlook (lowered from 'BB' on Apr 3, 2026, after outlook cut to negative on Nov 6, 2025).** S&P explicitly cited *"forecast deterioration in capital adequacy"* and financial leverage above desired thresholds. That is a two-notch slide in five months and puts MOH two notches into junk.

The downgrade path is fully corroborated by the reported financials:

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Revenue ($M) | 34,072 | 40,650 | 45,426 |
| Gross margin (= 100% − MCR) | 12.72% | 11.65% | **8.97%** |
| EBIT ($M) | 1,573 | 1,707 | **781** |
| Net income ($M) | 1,091 | 1,179 | **472** |
| Diluted EPS | 18.78 | 20.42 | **8.92** |
| Interest expense ($M) | 109 | 118 | **192** |
| Total debt ($M) | 2,385 | 3,118 | **3,950** |
| Operating cash flow ($M) | 1,662 | 644 | **−535** |

Three facts dominate the credit story:
- **Gross margin has compressed 375bps in two years.** Revenue grew 33% from 2023 to 2025 while EBIT *halved*. This is a medical-cost-ratio problem, not a demand problem.
- **FY2025 net income of $472M badly missed the already-reduced November 2025 guidance of ~$630M** (adjusted EPS ~$14 guided vs. $8.92 GAAP delivered). The shortfall triggered a **−25.5% single-day move on Feb 6, 2026** on 10.3M shares.
- **The debt increase funded buybacks, not the business.** MOH repurchased $1.0B of stock in both 2024 and 2025 — $2.0B over two years — while free cash flow over the same period was only $544M − $636M = **−$92M**. Debt rose $1,565M in two years and cash fell $731M in 2025 alone. Capital return has been financed by the balance sheet during an earnings decline.

**Mitigants:** No short-term debt; nearest material maturity is the $850M 6.500% senior notes due 2031 (S&P also rated $750M of new 2031 notes 'BB'). There is no refinancing cliff. Net cash is positive on a reported basis.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Assessment |
|---|---|---|
| Debt / equity | 0.97x | Up from 0.69x (2024); moderate |
| Debt / assets | 0.25x | Manageable |
| Gross debt / EBITDA | 4.05x (3,950/976) | Elevated for a 1.7%-margin business |
| Net debt / EBITDA | **−4.41x (net cash $4.31B)** | Strong on paper — see caveat below |
| EBIT / interest | **4.07x** | Down from 14.5x (2024). Thin |
| EBITDA / interest | 5.08x | Weak for IG-style leverage |
| Current ratio | 1.69x | Adequate |
| Quick ratio | 1.69x | Adequate (no inventory) |
| Cash ratio | 1.12x | Adequate |
| Working capital | $5,072M | Positive |
| Equity / assets | 0.26x | Adequate |
| Assets / liabilities | 1.35x | Adequate |
| **Altman Z-Score** | **4.01 (Safe)** | ⚠️ *Not meaningful here* — x5 (asset turnover 2.92x) and x1 (WC/TA 0.33) are structurally inflated for an insurer whose "working capital" is claims float. Treat as non-informative rather than reassuring. |
| **Piotroski F-Score** | **3 / 9 (Weak)** | Failed: op. cash flow, ROA trend, accrual quality, leverage trend, equity change, gross margin. Only passed: +ROA, no dilution, asset turnover |
| FCF (FY25) | **−$636M** | Two-year collapse from +$1,578M (2023) |
| FCF yield | **≈ −5.2% to −5.4%** | Negative |
| Days cash / cash burn | N/A — not burning cash at a distressed rate; $8.26B cash & ST investments vs. −$636M FCF ≈ 13x annual burn | Cushion exists |

**Critical caveat on net cash:** The reported $4.31B net cash position (cash & ST investments $8,256M less debt $3,950M) is **not freely available**. For a regulated MCO, most of that cash sits in insurance subsidiaries as statutory capital backing claims reserves. The balance sheet's own narrower net-debt field reads **−$298M**, roughly 14x less generous than the headline. S&P's downgrade was explicitly about **capital adequacy below desired thresholds** — i.e., the regulator-relevant cushion, not the consolidated cash line, is the binding constraint.

---

## 3. Market Risk Profile — **Severely elevated idiosyncratic risk**

| Metric | Value |
|---|---|
| Annualised volatility (756d) | **53.06%** |
| Beta vs SPY (computed) | 0.085 |
| Beta (profile, 5Y monthly) | 0.743 |
| Max drawdown (3Y, tool) | **−65.28%** |
| Peak-to-trough close (Mar 2024 $419.53 → Feb 2026 $122.65) | **−70.8%** |
| Sharpe ratio | **−0.077** |

**Beta discrepancy — flagged.** The two beta estimates disagree by 9x. Neither should be used as a risk-mitigation argument. The computed 0.085 is almost certainly distorted by the extreme idiosyncratic re-rating dominating the regression; the 0.743 profile beta understates realized risk. With **53% annualized volatility vs. ~15–18% for SPY**, MOH has been a ~3x market-risk asset in practice, not a low-beta defensive.

**Gap-risk profile is the真正 concern.** Three discrete, company-specific air pockets in twelve months:
- **Jul 2, 2025:** $306 → $239 (−22%)
- **Oct 23, 2025:** $195 → $161 (−17.5%, 7.8M shares)
- **Feb 6, 2026:** $177 → $132 (−25.5%, 10.3M shares)

A Sharpe of −0.077 with 53% vol and −71% peak drawdown means holders have been paid nothing for a great deal of risk. Price has since recovered to ~$233 (profile), but the drawdown/vol profile is permanently changed.

---

## 4. Downside Scenario Analysis — Revenue −20%

Base FY2025: Revenue $45,426M; medical costs $41,351M (91.03%); SG&A $3,009M (6.62%); EBIT $781M; interest $192M.

| Scenario | Rev −20% treatment | EBIT | EBITDA | EBIT / Int | Net income |
|---|---|---|---|---|---|
| **Base FY2025** | — | $781M | $976M | **4.07x** | $472M |
| **A: MCR flat, SG&A fixed** | Med costs 91.03%, SG&A held at $3,009M | **$251M** | $446M | **1.31x** | ~$47M |
| **B: MCR +150bps (92.53%), SG&A fixed** | reflects utilization/mix worsening with volume loss | **−$295M** | −$100M | **Negative** | ~−$390M |
| **C: MCR +250bps, SG&A cut 10%** | management response, still loss-making | **−$355M** | −$160M | **Negative** | ~−$438M |

**The headline finding: at constant MCR, a revenue decline of only ~21% takes interest coverage to 1.0x** ($35.7B revenue needed for EBIT = $192M). MOH's fixed SG&A base of $3.0B against an 8.97% gross margin means operating leverage is now severely asymmetric. A 20% revenue cut removes $4.08B of gross profit — more than 5x total EBIT.

**Balance-sheet survival:** Even in Scenario C, equity falls only to ~$3.6B (debt/equity ~1.09x) and the consolidated cash pile covers debt comfortably. **MOH survives a 20% revenue shock without a liquidity crisis but not without a further rating downgrade** — Scenario B/C leverage metrics are consistent with 'B' category. Survival is not the question; the rating and equity value are.

**2026 trajectory is adverse, not stabilizing.** Consolidated MCR has re-deteriorated through 2026: **Q1 91.1% → Q2 92.2% → Q3 92.9%**, versus 91.0% for FY2025 and 88.4% for FY2024. The margin recovery implied by the current $233 share price is not yet visible in the reported ratios.

---

## 5. Overall Financial Risk Rating: **HIGH**

Not "Critical" — MOH has positive equity ($4.07B), no near-term maturities, adequate liquidity ratios, and consolidated net cash. But the combination of a **halved EBIT, negative operating cash flow, negative FCF, a buyback program funded by debt, coverage collapsing from 14.5x to 4.1x, and a fresh two-notch downgrade into junk** places this firmly in the High bucket. The business is one more 150bp MCR deterioration away from an operating loss at current revenue.

Investment implication: this is an equity with bond-like sensitivity to a single variable (the medical care ratio) and a rating agency that has already moved twice. Position sizing should reflect a 53%-vol, −71%-drawdown risk profile, not the 0.74 beta the profile screen reports.

---

## 6. Key Red Flags

1. **Operating cash flow turned negative (−$535M) against positive net income ($472M)** — a −$1,007M accrual gap. Working capital swung −$1,289M vs. +$314M in 2023. Verify whether this is claims-reserve development (a leading indicator of adverse prior-period development) or premium receivable timing. *This is the single most important item to diligence.*
2. **$2.0B of buybacks over 2024–25 against −$92M cumulative FCF.** Debt +$1,565M, cash −$731M. Equity fell $427M in 2025 despite $472M of net income. Capital return has been borrowing from future flexibility.
3. **Interest expense +63% (118→192) on debt +27%** — the new 6.500% 2031 notes materially raised the cost of debt at exactly the wrong point in the earnings cycle.
4. **Coverage at 4.07x with only a ~21% revenue buffer to 1.0x.** No maintenance covenant data available, but this is the constraint that matters.
5. **S&P two-notch downgrade to 'BB-' (Apr 2026)** following negative outlook (Nov 2025) on capital adequacy — the rating trajectory is still downward even with a "stable" outlook.
6. **FY25 missed reduced guidance by ~25%** ($472M vs. ~$630M), with a −25.5% single-day equity reaction.
7. **Gross margin down 375bps in two years; 2026 quarterly MCRs trending worse** (91.1% → 92.9%).
8. **Piotroski 3/9** — weak on cash generation, leverage trend, and accrual quality simultaneously. Rarely a benign configuration.

---

## Data Gaps (explicit)

- **Full debt maturity schedule** not retrievable; confirmed only that short-term debt is $0 and the $850M 6.500% notes mature 2031. Items due 2028–2030 unquantified.
- **Covenant terms** not available — MOH's senior notes are likely covenant-lite (no maintenance test), but this is unverified.
- **Restricted vs. unrestricted cash split** unavailable. The $8.26B cash & investments figure almost certainly overstates deployable liquidity; the balance sheet's own net-debt field (−$298M) implies a much narrower definition.
- **Moody's and Fitch ratings** not retrieved — only S&P confirmed.
- **CDS spreads** unavailable.
- **Peer leverage/coverage comparison** not gathered (UNH/ELV/CNC/HUM would be the relevant set).
- **Price basis inconsistency:** company profile shows $233.09 / $12.17B market cap, but the price series available to me ends at $151.00 (2026-02-20). FCF yield is therefore reported as a range (−5.2% to −5.4% on the profile cap; ~−8.0% on the $151 close). The $233 figure is taken as current.
- **Altman Z-Score (4.01, "Safe") is reported for completeness but should be disregarded** — the model is not calibrated for managed-care balance sheets, where claims float inflates both working capital and asset turnover.
