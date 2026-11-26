# Fin Risk Analyst

- Symbol: BSP
- Elapsed: 36.6s

---
I have what I need. Note the tool-level balance sheet is FY2025 (latest available), but 2026 disclosures materially change the leverage picture — I've sourced those and flagged them.

---

# BSP — Bending Spoons S.p.A. | Financial Risk Assessment

**Verdict: HIGH financial risk.** A serial-acquisition roll-up funded with ~9% debt, where reported credit metrics and company-adjusted metrics diverge by a factor of ~2.4x. The business is cash-generative and not near distress today, but the margin for error has been spent on acquisitions.

---

## 1. Credit Risk Assessment — **Sub-Investment Grade**

The company is levered like a high-yield issuer and priced like one: recent dual-currency notes carry **coupons near 9%**, a spread consistent with B/B− territory, not BB. Two views of the same balance sheet tell very different stories:

| Leverage view | Net debt | EBITDA basis | Ratio |
|---|---|---|---|
| FY2025 reported (tool data) | $2.04B | $411M reported | **4.97x** |
| Q3 2026, company "adjusted" | $4.00B | ~$1.9B adjusted | **2.1x** |
| Q3 2026, GAAP EBIT basis (derived) | $4.00B | ~$687M annualised EBIT | **~5.8x** |
| Pro-forma post Miro + Mailchimp | ~$7.0B | ~$2.3–2.5B adj. | **~3.0x** |

The entire gap between 2.1x and ~5x is **adjusted-EBITDA add-backs** — chiefly $189M/quarter of acquired-intangible amortization plus acquisition/integration costs and likely run-rate credits on purchased businesses. Covenant leverage is capped at **4.00x**. On the company's own adjusted definition there is ~1.9x of headroom; on a reported basis there is none. **The covenant is a measurement risk, not just a balance-sheet risk.**

Debt trajectory is the core concern: total debt went **$867M (FY24) → $2.67B (FY25) → $5.02B principal (Q3 26) → ~$7B post-deal**. That is an 8x increase in under two years.

## 2. Key Financial Risk Metrics

| Metric | FY2023 | FY2024 | FY2025 | Flag |
|---|---|---|---|---|
| Revenue ($M) | 387.1 | 671.1 | 1,306.4 | +95% (acquisition-led) |
| Gross margin | 61.1% | 63.9% | 65.6% | Improving ✓ |
| Operating margin | 21.8% | 19.0% | 21.3% | Stable ✓ |
| EBITDA ($M) | 109.6 | 226.6 | 410.8 | ✓ |
| Interest expense ($M) | 17.2 | 32.6 | **142.6** | **+337% YoY** ⚠ |
| Net income ($M) | 160.8 | 89.5 | **−0.1** | Swung to loss ⚠ |
| Total debt ($M) | 389.3 | 867.3 | 2,670.9 | +208% ⚠ |
| **Net debt / EBITDA** | 0.91x | 2.77x | **4.97x** | ⚠ |
| **Interest coverage (EBIT/int.)** | 4.35x | 4.21x | **1.78x** | ⚠ Sharp decay |
| Debt / equity | 1.15x | 1.36x | **2.68x** | ⚠ |
| Debt / assets | 0.42x | 0.46x | **0.56x** | ⚠ |
| Current ratio | 1.33 | 1.09 | **0.82** | ⚠ <1.0 |
| Quick ratio | 1.33 | 1.09 | 0.82 | ⚠ |
| Cash ratio | 1.07 | 0.58 | 0.56 | Adequate |
| Working capital ($M) | +88.1 | +39.0 | **−199.9** | ⚠ |
| Cash / short-term debt | 3.29x | 2.14x | 1.52x | OK ✓ |
| **Altman Z-Score** | — | — | **0.654 (Distress)** | See caveat |
| **Piotroski F-Score** | — | — | **4 / 9 (Weak)** | See caveat |
| Goodwill + intangibles / assets | 34.8% | 64.9% | **73.6%** | ⚠ |
| **Tangible book equity ($M)** | — | — | **−2,506.6** | ⚠ Negative |

**On the Altman Z of 0.654:** the tool explicitly uses *book* equity in x4. Substituting market cap ($29.4B) against total liabilities ($3.76B) raises x4 from 0.26 to ~7.8, lifting Z to **≈3.75 — just inside the safe zone (>2.99)**. The honest read: the Z-score is not evidence of imminent bankruptcy, but its two weakest inputs are real — **negative working capital (x1 = −0.042)** and **weak asset productivity (x3 = 5.3%, diluted by $3.5B of acquired intangibles)**.

**On the Piotroski F of 4:** several failures are *mechanical* for an acquisitive roll-up rather than signs of decay — F5 (leverage rose) and F9 (asset turnover fell) fail because they levered up to buy EBITDA, and F7 (dilution) fails from the $1.3B equity raise. The genuinely concerning failures are **F1 (negative ROA)** and **F3 (ROA deteriorated)**.

**Cash generation is the offsetting strength:** FCF **$55.1M → $204.3M → $290.1M** (FY23–25), with essentially no capex ($0.5M) and FCF/interest of **2.03x**. SBC of $55.5M equals 19% of FCF — a real but manageable dilution cost.

## 3. Market Risk Profile

| Metric | Value | Note |
|---|---|---|
| Annualised volatility | **110.2%** | ⚠ Extremely high |
| Beta vs SPY (regression) | 0.92 | ⚠ Conflicts with reported beta |
| Beta (company-reported) | **1.48** | Trust this; regression window too short |
| Max drawdown | **−40.1%** | Aug 11 $53.44 → Oct 2 $32.03 |
| Sharpe ratio | 0.80 | Post-IPO window only |
| Price range since IPO | $30.11 – $59.50 | Current $46.29 |

**Data caveat, flagged:** BSP IPO'd **July 1, 2026** at $29.00. There are only ~105 trading days of history, so the "252-day" volatility and Sharpe are computed on a truncated window. The 110% vol overstates precision but not direction — this is a genuinely high-beta, high-dispersion equity. The 0.92 regression beta should be **discarded** in favour of the reported 1.48; a 105-day window is too short to estimate beta reliably.

## 4. Downside Scenario — Revenue −20%

Applied to FY2026 guidance of $3.07–3.09B revenue / $1.58–1.60B adjusted operating income, with ~$4.0B net debt today and ~$7.0B post-Mailchimp:

| | Base | −20% revenue |
|---|---|---|
| Revenue | $3.08B | $2.46B |
| Gross profit (65% GM) | $2.00B | $1.60B |
| Adjusted op. income | $1.59B | **~$0.95–1.20B** (partial opex flex) |
| GAAP EBIT (after ~$756M amortisation) | ~$0.69B | **~$0.15–0.45B** |
| Annual interest (~8.3% blended on $5.0B) | ~$415M | ~$415M |
| **GAAP interest coverage** | 1.66x | **0.4x – 1.1x → below 1.0x** |
| FCF | ~$800M | ~$450–550M |
| FCF / interest | ~1.9x | **~1.1–1.3x** |
| Net debt / adj. EBITDA | 2.1x | **~2.9x** |
| Post-deal ($7.0B) / adj. EBITDA | ~3.0x | **~5.0x → COVENANT BREACH vs 4.00x** |

**The critical finding:** a 20% revenue shock is survivable *today* — FCF still covers interest and covenant headroom holds at ~2.9x. But **once Miro and Mailchimp are funded and debt reaches ~$7B, the same shock drives leverage through the 4.00x covenant** and GAAP interest coverage below 1.0x. The equity does not go to zero in this scenario, but the company would be forced to raise equity at a distressed price or halt the acquisition engine — which *is* the business model. Compounding this, **organic growth is only 3%**; the −20% scenario has no organic recovery mechanism.

## 5. Overall Financial Risk Rating: **HIGH**

Not Critical — the company is FCF-positive, has $793M+ cash, no dividend, minimal capex, and interest is covered on a cash basis. But four structural features put it firmly in High:
1. Leverage doubling annually while the acquisition treadmill demands more;
2. A covenant measured on adjusted EBITDA that sits ~2.4x below reported leverage;
3. GAAP interest coverage of 1.78x *before* the 2026 debt ramp and ~9% coupons;
4. A negative tangible equity base of −$2.5B that provides no loss absorption if acquired intangibles impair.

## 6. Key Red Flags

1. **Refinancing/covenant cliff** — debt $867M → $2.67B → $5.02B → ~$7B in ~24 months, against a 4.00x cap. TLB matures 2031, so no near-term maturity wall, but post-deal headroom to covenant is thin (~3.0x vs 4.0x base case).
2. **Adjustment gap** — $189M/quarter of intangible amortisation separates a 54% "adjusted" operating margin from a 22% GAAP margin. Credit quality hinges on whether rating agencies and lenders accept run-rate add-backs. 9% note coupons suggest the market partly discounts them.
3. **Interest burden inflecting** — interest expense +337% to $142.6M in FY25 and on pace for ~$415M annualised; net income already −$0.1M with coverage at 1.78x.
4. **Negative tangible book equity (−$2.51B)**, goodwill/intangibles at 73.6% of assets. Any write-down impairs an already thin $995M equity base.
5. **Liquidity quality** — current ratio 0.82 and negative working capital, though cash covers short-term debt 1.52x and the $1.3B equity raise plus notes have since added liquidity.
6. **Organic growth of 3%** — inorganic growth funds the debt service that inorganic growth requires. A stalled deal pipeline is itself a credit event.
7. **Equity supply overhang** — a lock-up covering **318.5M of ~693M shares (~46%)** is due to release, against a stock with 110% vol and a 40% drawdown already on record.
8. **Governance** — dual-class structure gives founders **82.71% of votes**; minority holders cannot constrain capital allocation. Berkshire's ~4% stake is a validation signal, not a control mechanism.

## Data Gaps (explicit)

- **Balance sheet / income statement data from tools is FY2025 only** (latest annual, filed 2026-07-01). All 2026 figures — Q3 revenue $780.2M, $4.00B net debt, 4.00x covenant, ~$7B post-deal, 9% coupons — are from **secondary sources (company fixed-income materials, SEC filing summaries, research notes)** and are **unaudited within this analysis**. The SEC EDGAR page returned HTTP 403.
- **No credit rating or CDS spread available** from tools; the Sub-Investment Grade call is inferred from ~9% new-issue coupons.
- **Peer benchmarking unavailable** — `get_sector_peers` returned mega-cap Technology names (AAPL, MSFT, NVDA, TSM, AVGO) that share no economic characteristics with an Italian acquisition roll-up. No like-for-like leverage or multiple comparison is possible from this dataset.
- **Volatility, beta, and Sharpe are computed on ~105 trading days** (post-IPO from July 2026), not a full 252-day window. Treat as directionally indicative only.
- **Altman Z-Score (0.654)** uses book equity per the tool's construction; market-cap-adjusted Z is ≈3.75. Both are reported above; neither should be used mechanically.
