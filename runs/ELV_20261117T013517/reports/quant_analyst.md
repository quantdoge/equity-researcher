# Quant Analyst

- Symbol: ELV
- Elapsed: 83.9s

---
## ELV (Elevance Health) — Quantitative Factor Report

### 0. Data Integrity Note (read first)
Two price anchors exist and both are valid but measure different things:
- **FY2025 close (2025-12-31): $345.49** — last row of the daily series I pulled.
- **Current price used by the ratio/factor engine: $446.28** (mkt cap $98.98B, 221.8M sh) — implies a ~+29% move since year-end. This reconciles the otherwise contradictory stats: 12-1 momentum of **+9.62%** and a **+41.33% annualised return** are only possible from a base in the $270–345 range, i.e. the trailing 252-day window ends *after* 2025-12-31. Ratios below are on the $446.28 basis.
- **Contradiction to flag:** the trailing-window series I retrieved shows a peak-to-trough of **–39.1%** (Apr-3-2025 $439.52 → Aug-1-2025 $267.84), yet the vol module reports max drawdown of only **–19.37%**. The reported drawdown is therefore window-dependent, not lifetime. Do not use 19.4% as "worst case this name can do."

---

### 1. Factor Scores Table

| Factor | Score / Raw | Sector Rank* | Signal |
|---|---|---|---|
| **Value** | P/E 17.8 (fwd 15.4), EV/EBITDA 12.7, P/B 2.25, FCF yield 3.2% | **3 of 6** (~50th pct) | Neutral |
| **Momentum** | 12-1 return **+9.62%** | **1 of 6** (best) | **Bullish** |
| **Quality** | ROE 12.9%, GP/assets 0.419, accruals +0.0113 | **2 of 6** | Buy (deteriorating trend) |
| **Low Vol** | Vol 32.5%, beta 0.13, max DD –19.4% | **3 of 6** (~45th pct) | Neutral |
| **Earnings Revision** | +16.06% vs 3-mo prior | n/a — no peer data | Bullish but **unreliable (n=1)** |

\*Peer set = managed-care comps (UNH, CI, HUM, CNC, MOH). Note the `get_sector_peers` tool returns pharma names (LLY, JNJ, ABBV, MRK) because it keys on "Healthcare"; ranking against pharma would be economically wrong, so I substituted the true industry cohort.

**Peer detail — Value (lower = better)**

| | P/E | EV/EBITDA | P/FCF |
|---|---|---|---|
| ELV | 17.8 | 12.7 | 31.2 |
| CI | 13.5 | 8.8 | 9.5 |
| UNH | 31.1 | 18.4 | 23.3 |
| MOH | 26.1 | 7.7 | neg |
| HUM | 46.9 | 22.2 | 148.6 |
| CNC | neg | neg | 8.5 |

ELV is the **2nd cheapest on P/E** (ex-CNC's meaningless negative) but only **3rd/6 on EV/EBITDA and P/FCF**. The gap is the tell: EV/EBITDA and P/FCF rank worse than P/E because ELV converts earnings to cash poorly — **P/FCF of 31.2x vs a 17.8x P/E**.

**Peer detail — Quality**

| | ROE | GP/Assets | Accruals |
|---|---|---|---|
| ELV | 12.9% (2nd) | **0.419 (1st)** | +0.0113 (**5th**) |
| CI | 14.2% | 0.165 | –0.0231 |
| UNH | 11.9% | 0.268 | –0.0247 |
| MOH | 11.6% | 0.262 | +0.0647 |
| HUM | 6.7% | 0.387 | +0.0055 |
| CNC | –33.3% | 0.311 | –0.153 (distorted by loss) |

Top-quartile ROE and best-in-class gross-profit/assets, but **bottom-2 accruals** — the single weakest quality leg.

---

### 2. Price Statistics

| Metric | Value |
|---|---|
| Annualised return | **+41.33%** |
| Annualised volatility | 32.5–32.7% |
| **Beta vs SPY** | **0.131** |
| **Alpha (annualised)** | **+46.02%** |
| **R²** | **0.0034** |
| **Sharpe** | **1.264** |
| **Sortino** | **1.868** |
| Max drawdown (trailing) | –19.37% |
| Max drawdown (FY2025 series, verified) | **–39.1%** |

**Critical statistical flag on alpha/beta:** R² of 0.0034 means the market explains **0.34%** of ELV's variance. Implied t-stat on beta ≈ 0.92 (n=252) — **beta is statistically indistinguishable from zero**. Consequently:
- The 0.131 beta is **not a usable risk input**. The company profile reports beta **0.711**; the 252-day regression is dominated by an idiosyncratic re-rating event, not market sensitivity. Use 0.65–0.75 for cost of equity.
- The **+46% alpha is almost entirely unexplained idiosyncratic return**, not market-relative skill. It is a realised outcome, not an ex-ante signal. Idiosyncratic vol = 32.46% × √(1–0.0034) ≈ **32.4%** — ~99.7% of total risk is stock-specific.
- Sortino/Sharpe = 1.48x, so downside deviation is well-controlled relative to total vol — but this is a 252-day window that no longer contains the July-2025 event.

---

### 3. Supporting Fundamental / Quality Checks

**Piotroski F-Score: 6/9 (Moderate)** — failing on precisely the three legs that matter:
- F3 ROA improvement = **0**
- F4 accruals quality = **0**
- F8 gross margin improvement = **0**
Passing: positive ROA, positive OCF, lower leverage, positive equity change, no dilution, asset-turnover improvement.

**Return on capital — a four-year monotonic decay (the most important number here):**

| | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| ROIC | 13.60% | 13.24% | 11.99% | **10.50%** |
| ROE | 16.22% | 15.19% | 14.44% | **12.86%** |
| ROA | 5.74% | 5.50% | 5.12% | **4.66%** |

**Cash conversion is breaking down:**

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| Revenue ($B) | 171.3 | 176.8 | **199.1** (+12.6%) |
| Operating income ($B) | 8.745 | 8.888 | **8.112** (–8.7%) |
| Net income ($B) | 5.987 | 5.980 | **5.662** |
| Diluted EPS | $25.22 | $25.68 | **$25.12** (–2.2%) |
| Free cash flow ($B) | 6.765 | 4.552 | **3.174** (–30% y/y) |
| Accruals ratio | –0.019 | +0.0015 | **+0.0113** |

Revenue grew 12.6% while operating income fell 8.7% and FCF fell 30% — pure margin/MLR compression. Net income exceeds operating cash flow by $1.37B, with working capital a $3.28B drag. This is why the value factor's EV/EBITDA and P/FCF ranks lag its P/E rank.

**Forward estimates (13 analysts, FY2026):** EPS $29.05 → forward P/E **15.4x**; FY2027E $30.25 → 14.8x. Growth decelerates sharply after 2026 (+15.7% in 2026, then **+4.1%** in 2027).
**Earnings revision caveat:** the +16.06% upgrade is measured on the **FY2030** estimate with **num_analysts = 1**. The 2029 period also carries n=1. Sample is far too small for significance — I would not weight this leg above 0 in the composite.

**Balance sheet:** Net debt ≈ $23.75B; net debt/EBITDA **2.46x**; EBIT/interest **5.8x**. Dividend $6.87 (1.5% yield), 27% payout — secure but modest.

---

### 4. Composite Quant Signal: **BUY** (not Strong Buy)

Weighted: Momentum (best-in-cohort, +) and Quality (2nd-in-cohort on ROE and GP/assets, +) carry the score; Value is mid-pack (+) and Low Vol is mid-pack (0). Deductions for the four-year ROIC decay, the FCF/accruals deterioration, and the unreliable revision signal cap it below Strong Buy.

A genuine top-quintile-on-all-three stock would show ROIC *expanding* alongside cheap multiples. ELV is cheap-and-improving-on-price but **de-rated on fundamentals** — the price factor and the quality factor point in opposite directions, and the quality factor is trending down, not up.

### 5. Key Quant Risk Flags

1. **Alpha/beta not statistically valid.** R² = 0.0034, beta t-stat ≈ 0.9. Do not size ELV as a low-beta hedge; 99.7% of risk is idiosyncratic. A 0.13 beta assumption would badly understate portfolio VaR contribution.
2. **Drawdown asymmetry.** The engine's –19.4% understates the real event: –39.1% in under four months in 2025. Position sizing should use the latter.
3. **Earnings-quality decay (highest-conviction negative).** Four consecutive years of ROIC decline (13.6%→10.5%), FCF down 53% from 2023 peak, accruals flipping from –0.019 to +0.0113. F-Score 6/9 with all three deterioration legs failing.
4. **Value trap signature.** P/FCF 31.2x and EV/EBITDA 12.7x against a 17.8x P/E means the "cheap" multiple is an earnings multiple, not a cash multiple. Medical-cost trend is compressing exactly the conversion ELV needs to justify the price.
5. **Revision signal is statistically empty.** +16.06% is computed on FY2030 with a single contributing analyst. Zero inferential weight.
6. **Factor crowding / momentum reversal risk.** ELV is the cohort's #1 momentum name (+9.62%) in an industry that just delivered a 39% drawdown. Managed care is a policy-headline sector (Medicare Advantage rate notices, MLR rules) — momentum here is event-fragile, and the +41% trailing return is precisely the setup for reversal.
7. **Decelerating growth cliff.** FY2027E growth of +4.1% after +15.7% in FY2026 means the forward multiple is not as cheap as 15.4x implies once the 2026 step-up laps.
8. **Sector-rank bucket is tiny.** Ranks are computed against 5 peers (n=6 cohort). That is directional context, not a statistically robust quintile. No P/B data was obtainable for comps, so the book-value leg of the value factor is single-name only.
