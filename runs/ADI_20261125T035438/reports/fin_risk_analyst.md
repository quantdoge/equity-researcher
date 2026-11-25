# Fin Risk Analyst

- Symbol: ADI
- Elapsed: 81.8s

---
I have what I need. The picture is clear: fortress balance sheet, but a high-beta, late-cycle market risk profile — and the stock just fell 17% on a Q4 FY26 earnings beat. Writing the assessment now.

---

# Financial Risk Assessment — Analog Devices, Inc. (ADI)

**Sector:** Technology / Semiconductors · **Market Cap:** $151.6B · **Price:** $312.95 (24-Nov-2026) · **Fiscal year end:** late October

---

## 1. Credit Risk Assessment

**Rating: INVESTMENT GRADE (strong)**

ADI's credit profile is exceptionally solid. FY2026 (ended 31-Oct-2026) gross debt of $11.43B against $33.9B of book equity gives **debt/equity of 0.34x** and **debt/assets of 0.22x**. Net debt is $6.53B. Interest coverage on reported EBIT is **15.8x**; on a corrected EBITDA basis it is **~21x**.

The one caveat is composition. Goodwill and intangibles are **$35.0B — 68% of total assets** — leaving **tangible book equity of negative ~$1.1B**. The equity cushion is essentially acquisition goodwill (Maxim/Linear), not hard assets. This does not impair debt service (cash flow does that), but it means a severe downturn that triggered a goodwill impairment would collapse reported book equity. Market cap of $151.6B vs. $33.9B book equity (P/B ~4.5x) shows the goodwill is well-supported by market value today — but it is the key structural vulnerability.

**Altman Z-Score: 2.30 (Grey zone)** — this is **not** a genuine distress signal. The score is mechanically depressed by two factors: (a) x4 uses *book* equity rather than the $151.6B market cap, and (b) the $35B goodwill inflates total assets, shrinking x1 (0.093) and x5 (0.295). On a market-cap basis ADI would score comfortably in the safe zone. Treat 2.30 as a structural artifact, not a warning.

**Piotroski F-Score: 8/9 (Strong)** — the only failed component is F5 (lower leverage), because gross debt rose from $8.66B to $11.43B (+32%) during FY2026. Profitability (4/4), liquidity/leverage quality (2/3), and operating efficiency (2/2) all pass.

---

## 2. Key Financial Risk Metrics

| Metric | FY2026 | FY2025 | FY2024 | FY2023 | Assessment |
|---|---|---|---|---|---|
| Revenue ($M) | 15,179 | 11,020 | 9,427 | 12,306 | +37.8% YoY; cycle recovery |
| Gross margin | 67.4% | 61.5% | 57.1% | 64.0% | Expanding |
| Operating margin | 38.6% | 26.6% | 21.6% | 31.1% | Peak-cycle |
| Net income ($M) | 4,997 | 2,267 | 1,635 | 3,315 | +120% YoY |
| Diluted EPS | $10.21 | $4.56 | $3.28 | $6.55 | — |
| Total debt ($M) | 11,427 | 8,665 | 7,650 | 7,013 | Rising |
| Cash ($M) | 5,198 | 3,652 | 2,363 | 958 | Rebuilt |
| Net debt ($M) | 6,529 | 6,165 | 5,658 | 6,055 | Stable |
| Debt/Equity | 0.34x | 0.26x | 0.22x | 0.20x | Low |
| **Net debt/EBITDA** | **0.83x** | 1.23x | 1.35x | 0.98x | Very low |
| **Interest coverage (EBIT)** | **15.8x** | 9.2x | 6.5x | 14.6x | Strong |
| Current ratio | 1.84x | 2.19x | 1.84x | 1.37x | Adequate |
| Quick ratio | 1.48x | 1.68x | 1.35x | 0.86x | Adequate |
| Cash ratio | 0.92x | 1.13x | 0.79x | 0.30x | Strong |
| Working capital ($M) | 4,778 | 3,862 | 2,496 | 1,183 | Growing |
| Altman Z | 2.30 | — | — | — | Grey (artifact) |
| Piotroski F | 8 | — | — | — | Strong |

**Note on net debt/EBITDA:** The tool computes 1.06x using FY2026 EBITDA = operating income ($5,858M), because the FY2026 income-statement row carries D&A = 0 (a data error). Adding reported D&A of $1,995M gives true EBITDA of ~$7,854M and **net debt/EBITDA of 0.83x**. Even the more conservative 1.06x is comfortably investment grade.

**Liquidity:** Cash of $5.20B covers short-term debt of $1.68B by **3.1x**. The current ratio of 1.84x and quick ratio of 1.48x indicate no working-capital strain. FCF of $5.45B annually dwarfs any near-term obligation — **cash runway is not a relevant constraint**.

---

## 3. Market Risk Profile

| Measure | Value | Interpretation |
|---|---|---|
| Annualised volatility (756d) | **41.2%** | High — elevated for a semi |
| Beta vs SPY | **1.67** (tool) / 1.25 (5Y profile) | High market sensitivity |
| Max drawdown (756d) | **32.2%** | Severe |
| Sharpe ratio (0% rf) | 0.59 | Modest; **~0.47 at 4.7% rf** |
| Current drawdown from peak | **-29.5%** | $444.13 (22-Jun-26) → $312.95 |
| 52-week range | ~$304 – $444 | At the low end |

**The dominant market-risk event:** On **24-Nov-2026 ADI fell 17.4% in a single session** ($378.75 → $312.95) on 12.8M shares — roughly 4x normal volume. Q4 FY26 EPS actually **beat** consensus ($4.06 vs. $3.90), so this was a "beat but guide down" / peak-cycle de-rating, not a fundamental miss. The stock now sits near its 52-week low.

The Sharpe ratio of 0.59 is quoted at a 0% risk-free rate; with the 2Y at 4.74% and 10Y at 5.13%, the true excess-return Sharpe is **~0.47**, and the 30% drawdown has erased most of the trailing risk-adjusted return. ADI's **FCF yield of 3.56% sits below the 10Y Treasury yield of 5.13%** — investors are paying a premium multiple with no yield cushion, which amplifies drawdown severity.

---

## 4. Downside Scenario Analysis — Revenue −20%

**Base:** FY2026 revenue $15.18B, gross margin 67.4%, operating margin 38.6%, FCF $5.45B.

Modeling a 20% revenue decline to **$12.14B** with gross margin compressing to ~60% (high fixed-cost fabs) and ~90% sticky opex:

| Metric | Base FY2026 | −20% Revenue | Change |
|---|---|---|---|
| Revenue | $15,179M | $12,143M | −20% |
| Gross margin | 67.4% | ~60.0% | −7.4 pts |
| Operating income | $5,858M | ~$3,356M | −43% |
| Operating margin | 38.6% | ~27.6% | −11 pts |
| EBITDA | $7,854M | ~$5,351M | −32% |
| **Net debt/EBITDA** | 0.83x | **~1.22x** | Still IG |
| **Interest coverage** | 15.8x | **~9.0x** | Comfortable |
| Net income | $4,997M | ~$2,540M | −49% |
| FCF | $5,453M | ~$4,000M | −27% |
| Dividend coverage | 2.6x | ~1.9x | Safe |

**Conclusion: no covenant breach, no credit deterioration, no refinancing crisis.** Leverage stays near 1.2x and coverage near 9x. The dividend (~$2.09B) remains ~1.9x covered; buybacks would be the flex.

**This scenario is not hypothetical — ADI already lived it.** In FY2024 revenue fell **−23.4%** ($12.31B → $9.43B), gross margin dropped to 57.1%, operating margin to 21.6%, net income halved to $1.64B, and FCF fell to $3.12B. Through that, ADI still paid **$1.80B of dividends (1.74x covered)**, cut buybacks from $2.96B to $0.62B, kept net debt/EBITDA at **1.35x**, and reduced gross debt. That is the empirical stress test, and ADI passed it comfortably. A harsher −35% scenario would still leave leverage under 2x.

---

## 5. Overall Financial Risk Rating: **LOW**

Balance-sheet risk is genuinely low: sub-1x net leverage, ~16x interest coverage, $5.2B cash, $5.5B annual FCF, and an F-Score of 8. The company could absorb a 20–35% revenue decline without breaching covenants or impairing its dividend. The risk here is **not solvency — it is market risk and cyclicality**. At 41% volatility, 1.67 beta, a 32% drawdown, and a 3.56% FCF yield below the risk-free rate, the equity is exposed to sharp de-rating at cycle peaks — which is precisely what happened on 24-Nov-2026.

---

## 6. Key Red Flags

1. **Negative tangible book equity.** Goodwill + intangibles of $35.0B = 68% of assets; tangible equity is **−$1.1B**. An impairment in a deep downturn would wipe out reported book equity (though not cash flows).
2. **Decelerating sequential growth.** Q1→Q4 FY26 revenue grew +14.7%, +11.0%, +8.7% QoQ — decelerating into the peak. The −17.4% single-day drop on a Q4 beat signals the market is pricing a cycle turn.
3. **High market risk.** Beta 1.67, vol 41.2%, max drawdown 32.2%, currently −29.5% from the June peak. FCF yield (3.56%) below the 10Y (5.13%) offers no valuation cushion.
4. **~99% of FCF paid out.** Dividends ($2.09B) + buybacks ($3.32B) = $5.41B vs. FCF $5.45B. Payout is fully FCF-dependent; buybacks are the flex (cut sharply in FY2024).
5. **Working-capital absorption.** FCF margin slipped from 38.8% to 35.9% despite revenue growth, as WC absorbed $682M — inventory and receivables building into the upcycle. Monitor for overbuild.
6. **Rising leverage.** Gross debt +32% YoY and short-term debt up 3.8x ($0.45B → $1.68B); Piotroski F5 failed. Absolute levels remain low, but the direction warrants monitoring.

---

## Data Gaps & Caveats

- **Debt maturity schedule unavailable** — only the short/long split ($1.68B / $9.74B). No refinancing-cliff analysis possible; mitigated by $5.2B cash and $5.5B FCF.
- **No credit rating or CDS spread** in the dataset. Rating assigned on fundamentals only.
- **FY2026 income statement D&A reported as zero** (EBITDA = operating income). I adjusted EBITDA manually using cash-flow D&A ($1,995M); tool-reported leverage ratios are consequently overstated.
- **Altman Z uses book equity** and is distorted by goodwill — indicative only.
- **Peer comparison unavailable.** The top-10 tech peers returned are mega-cap (NVDA, AVGO, TSM, MU, AMD) — not analog comparables. Direct analog peers (TXN, MCHP, NXPI) were not returned, so no peer-multiple benchmarking is included.
