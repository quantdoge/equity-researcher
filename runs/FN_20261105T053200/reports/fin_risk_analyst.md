# Fin Risk Analyst

- Symbol: FN
- Elapsed: 100.3s

---
# FABRINET (FN) — FINANCIAL RISK ASSESSMENT
*Data through FY2026 10-K (FYE 26-Jun-2026), Q1 FY2027 (26-Sep-2026), and market data to 30-Sep-2026*

---

## 1. Credit Risk Assessment

**Rating: Investment-Grade equivalent (net cash, effectively debt-free) — but unrated, so scorecard-based, not agency-based.**

| Metric | FY2026 | Read |
|---|---|---|
| Total debt | $4.0M (Q1 FY27: $78.3M) | Trivial; the $78M is the first debt drawdown in years |
| Cash + ST investments | $875.1M (Q1 FY27: $755.8M) | Net cash ~$871M; ~$678M on latest quarter |
| Net debt / EBITDA | **−1.4x** (net cash) | Negative leverage — no refinancing cliff |
| Debt / equity | ~0.00x (0.03x latest qtr) | Zero covenant-breach risk in any realistic scenario |
| Interest coverage (EBIT/interest) | **5,510x** | Statutory, not economically meaningful — no interest burden |
| Altman Z-Score | **4.12 — Safe zone** | Well above the 2.99 threshold; x4 uses book equity, so market-cap-based Z would be higher still |
| Piotroski F-Score | **5 / 9 — Moderate** | Fails on accruals quality, leverage direction, gross-margin trend, asset turnover |

**Conclusion:** This is a solvency-risk story with essentially no solvency risk. There is no maturity wall, no leverage covenant exposure, and no meaningful refinancing need. The credit risk that *does* exist is entirely of the "operational/pricing" variety (customer concentration, margin compression), not the "balance-sheet" variety.

**Weak Piotroski components (the informative part):** accruals quality (F4 = 0, because CFO/NI fell to 0.54x), leverage trend (F5 = 0, liabilities +71% y/y), gross margin (F8 = 0), and asset turnover (F9 = 0). Three of those four are the same signal: **balance sheet and cost base are growing faster than profit.**

---

## 2. Key Financial Risk Metrics

| Metric | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | Q1 FY27 |
|---|---|---|---|---|---|---|
| Revenue ($M) | 2,262 | 2,645 | 2,883 | 3,419 | **4,641** | 1,475 |
| Gross margin | 12.3% | 12.7% | 12.4% | 12.1% | **12.0%** | **11.8%** |
| Operating margin | 9.0% | 9.5% | 9.6% | 9.5% | **10.0%** | 9.9% |
| Net margin | 8.9% | 9.4% | 10.3% | 9.7% | **10.2%** | 7.0% |
| Capex ($M) | 90.6 | 62.3 | 47.5 | 121.8 | **253.7** | **158.7** |
| Capex / revenue | 4.0% | 2.4% | 1.6% | 3.6% | **5.5%** | 10.8% |
| Operating cash flow ($M) | 124.2 | 213.3 | 413.1 | 328.4 | **256.7** | **21.3** |
| **Free cash flow ($M)** | 33.7 | 151.0 | 365.6 | 206.5 | **3.0** | **−137.4** |
| FCF / net income | 0.17x | 0.61x | 1.23x | 0.62x | **0.01x** | negative |
| FCF yield | — | — | — | — | **0.02%** | neg. |
| Working-capital drag ($M) | −145.2 | −104.1 | +41.3 | −89.2 | **−259.9** | **−149.3** |
| Inventory days | 102 | 82 | 67 | 71 | **91** | ~95+ |
| DSO (days) | 73 | 73 | 75 | 81 | **80** | ~80 |
| Current ratio | — | — | — | — | **2.25x** | 2.04x |
| Quick ratio | — | — | — | — | **1.52x** | 1.34x |
| Cash ratio | — | — | — | — | **0.62x** | 0.45x |
| Working capital ($M) | — | — | — | — | **1,757** | 1,744 |
| Equity / assets | 68% | 74% | 75% | 70% | **63%** | 58% |

**Liquidity read:** Strong on a level basis ($1.76B working capital, $756M cash vs. $78M debt), but *directionally deteriorating* — quick ratio 1.52 → 1.34, cash ratio 0.62 → 0.45 in one quarter, equity/assets 75% → 58% over two years. Growth is being funded by the balance sheet, not by cash generation.

**FCF sustainability — this is the weak link.** FY2026 free cash flow was $3.0M on $473M of net income. Over the last five reported quarters, cumulative FCF is **≈ −$134M**. Two distinct causes, with different risk weights:
- **Capex:** $254M in FY26 and $159M in Q1 FY27 alone (10.8% of quarterly revenue). This is *discretionary growth capex* — deferrable under stress. Medium risk.
- **Working capital:** inventory +76% y/y against revenue +36%, inventory days 71 → 91. This is *partly* pre-build for ramping programs, but a 21-day inventory extension in fast-rotating optical/AI hardware is the classic obsolescence setup. Higher risk, and much harder to reverse quickly.

---

## 3. Market Risk Profile

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility (2y) | **70.2%** | ~4.5x a typical large-cap; extreme even for semis |
| Beta vs SPY (2y) | **2.15** | A 10% market drawdown implies ~21% for FN (profile reports 1.345 on a longer window — the 2y regime is far hotter) |
| Max drawdown (tool, 2y window) | **−57.8%** | See cross-check below |
| Max drawdown (my price series, close-to-close) | **−49.9%** — peak close $746.47 (14-May-26) → intraday low $373.70 (15-Sep-26) | Confirms a genuine ~50%+ peak-to-trough |
| Sharpe ratio (2y, rf = 0%) | **0.59** | Poor compensation for 70% vol; Sortino not available from tool |
| Position vs. peak (30-Sep-26 close $424.27) | **−43%** | Deep drawdown, not yet recovered |

**Interpretation:** FN is a high-beta, high-volatility instrument where the *market* risk dominates the *financial* risk. The equity has already demonstrated a 50%+ drawdown in the last twelve months while the business posted record revenue — i.e., **the stock de-rates on sentiment/multiple compression irrespective of fundamentals.** For a risk officer, position sizing and drawdown tolerance matter more here than any credit metric.

---

## 4. Downside Scenario Analysis

Methodology: FY2026 cost base decomposed into variable COGS (84% of revenue), fixed COGS (4%, incl. depreciation), and SG&A ($93.5M, ~80% fixed). Revenue shock applied; management cuts capex to maintenance (~$80M).

| Scenario | Revenue | Gross margin | Operating income | EBITDA | Net income | FCF | Net cash |
|---|---|---|---|---|---|---|---|
| **Base (FY26A)** | $4,641M | 12.0% | $463M | $624M | $473M | $3M | +$871M |
| **−20% revenue** | $3,713M | 11.0% | **$318M (−31%)** | $387M | ~$250M | **+$250–400M** (WC release, capex cut) | +$1.0B+ |
| **−35% (AI/data-center digestion + share loss)** | $3,017M | 9.8% | **$210M (−55%)** | $278M | ~$160M | +$500M+ | +$1.2B+ |
| **−50% severe** | $2,321M | 8.0% | **$101M (−78%)** | $170M | ~$70M | +$600M+ | +$1.3B+ |

**What the scenario math shows:**
- A 20% revenue decline cuts operating income ~31% and net income ~47% — a serious *earnings* event, driven by operating leverage on a 12%-gross-margin base (each 100bp of gross margin ≈ $46M of operating income).
- It is **not a liquidity or solvency event.** Net cash position, no debt maturities, and a revenue contraction *releases* working capital (inventory + receivables of $2.35B at Q1 FY27 would free $600–800M under a 35% contraction) instead of consuming it.
- The severe tail case (−50%) still leaves the company profitable and net-cash. **The company can survive a prolonged downturn with room to spare.** The damage would be to the multiple, not the balance sheet.
- **The real tail risk is inventory marks, not leverage:** at a 91-day inventory holding period, an abrupt order cut from a 20%-of-revenue customer could force write-downs that hit gross margin directly, compounding the volume hit.

---

## 5. Overall Financial Risk Rating

# LOW

*(Balance-sheet/solvency/liquidity risk: LOW. Market risk: HIGH. Blended: LOW-to-MODERATE.)*

Justification: net cash of ~$678–871M, net debt/EBITDA of −1.4x, Z-score of 4.12 in the safe zone, current ratio 2.25x, and no refinancing exposure put the company in the least risky decile of the technology hardware universe on credit fundamentals. The sub-investment-grade traits (negative FCF, working-capital build, 70% volatility, 2.15 beta, ~57% max drawdown) are real but are **equity-risk and working-capital-quality issues, not survival issues.**

---

## 6. Key Red Flags

1. **Free cash flow has effectively gone to zero and turned negative.** FY26 FCF $3.0M on $473M net income (0.6% conversion); cumulative FCF across the last five quarters ≈ −$134M. Three consecutive negative-FCF quarters. Cash conversion, not profitability, is the deteriorating variable.
2. **Inventory ballooning.** $1,021M → $1,193M in one quarter; +76% y/y vs. +36% revenue growth; inventory days 71 → 91 → ~95. Obsolescence exposure in a product cycle this fast is material and would show up as gross-margin impairment, not covenant breach.
3. **Extreme customer concentration.** FY2026: Cisco 20%, NVIDIA 16%, Nokia 11%, plus a fourth customer ≥10% — top four ≈ 57% of revenue. Two customers were already 45.8% in FY2025 (10-K). A single program loss at Cisco or NVIDIA is a ~16–20% revenue event, exactly the −20% scenario above.
4. **Single-theme revenue mix.** Data center products 47.9% of FY2026 revenue (up from 46.2%), communications infrastructure 33.3% (up from 30.7%) — ~81% tied to one capex cycle. The concentration is *increasing*.
5. **Structural gross-margin erosion.** 12.7% (FY23) → 12.0% (FY26) → 11.8% (Q1 FY27). In an EMS model with concentrated, price-setting customers, this is a persistent, not cyclical, headwind — and operating leverage works in reverse on it.
6. **Earnings quality.** FY2026 net income ($473M) *exceeded* operating income ($463M) because ~$92M (~20% of pre-tax profit) was interest income on the cash pile. Normalised, tax-effected operating margin is closer to ~8%, not the headline 10.2%. Piotroski's accruals component (F4) already flags this.
7. **First debt drawdown coincides with negative FCF.** Total debt went from $4.0M to $78.3M in Q1 FY27 while FCF was −$137M. Immaterial in size, but the *direction* (borrowing while burning cash) is the pattern to monitor each quarter.
8. **High-beta drawdown risk.** Beta 2.15, vol 70%, −43% from the May-2026 peak already. Under a market drawdown, FN's equity behaves as a 2x levered AI-capex proxy.
9. **Geographic/regulatory concentration.** Manufacturing concentrated in Thailand; KY-domiciled; exposed to export controls, tariffs, and FX (a $3.2M FX loss in the Dec-2025 quarter, down from $7.1M a year earlier).

---

## Data Gaps (explicitly flagged)

- **No credit rating or CDS spread available** — credit assessment is scorecard/solvency-based only; FN carries no agency rating in the data set.
- **No debt facility / covenant detail** (revolver size, terms) available from the tools; the $78.3M drawn balance is not corroborated against a facility agreement.
- **No sortino ratio** or longer-window volatility from the tool.
- **Peer benchmarking not possible:** the sector-peer tool returned only mega-caps (AAPL, NVDA, MSFT, TSM, AVGO, SK Hynix, MU, AMD), none of which are valid comparables for a 12%-gross-margin contract manufacturer. True EMS/optical comps (Jabil, Flex, Celestica, Coherent, Lumentum, Sanmina) were unavailable — **leverage and margin comparisons to peers are therefore not made.**
- **Price inconsistency:** the company profile shows $341.64 while the last close in the price history is $424.27 (30-Sep-2026). Market cap ($12.24B) is computed off the stale figure; at $424.27 it is ~$15.2B. FCF yield of 0.02% is directionally right either way.
- **Max drawdown discrepancy:** the tool reports −57.8% for a 730-day window; my raw price series shows −49.9% (close-to-close) and −50.1% (peak close to intraday low). The tool's figure may use a longer or later window. Both confirm a ~50%+ drawdown; treat −50% as the confirmed floor of the estimate.
- **TTM FCF is an approximation** — Q1 FY2026 cash flow was not retrieved, so the five-quarter cumulative (−$134M) is used in place of a strict TTM figure.
