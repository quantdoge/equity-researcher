# Fin Risk Analyst

- Symbol: SOFI
- Elapsed: 78.4s

---
# SOFI — Financial Risk Assessment
**As of 2026-02-20 | Price $19.02 | Market cap ≈$21.2bn | FY2025 (period end 2025-12-31)**

## ⚠️ Critical Framework Note
SOFI is a **bank holding company** (SoFi Bank, N.A. — a Utah-chartered national bank). Several of the tool's ratios are **structurally inapplicable** and would produce false conclusions if read literally. I flag each one and substitute bank-appropriate metrics below.

---

## 1. Credit Risk Assessment — **INVESTMENT GRADE (bank-adjusted)**

| Metric | Value | Read |
|---|---|---|
| SoFi Bank CET1 risk-based | **16.4%** ($5,790M) | vs 7.0% min incl. buffer → **2.3x** |
| Total risk-based capital | ~16.6–17.5% | vs 10.5% min |
| Regulatory standing | "Well capitalized under **all** definitions" | ✅ |
| Equity / assets | 20.7% (FY24: 18.0%) | Rising, ~4x typical bank |
| Tangible equity / assets | 16.8% | Excl. $2.0bn goodwill |
| Net charge-offs | 3.7%, **−70bps y/y** | Improving |
| Personal-loan NCO | 2.80% annualized (**+20bps QoQ**) | ⚠️ Rising |
| ROA (avg assets) | 1.11% | Above ~1.0% bank benchmark |
| ROE (avg equity) | 5.66% | Low — capital-heavy |

**Reverse stress test:** CET1 capital of $5,790M against RWA of ~$35.3bn means SOFI can absorb **~$3.3bn of losses (~10.4% of the loan book, ~6.9 years of FY25 earnings)** before breaching the 7.0% requirement. Half the $10.5bn consolidated equity sits at the unregulated parent and can be downstreamed. **Solvency is not the risk.**

---

## 2. Key Financial Risk Metrics

| Metric | Reported | Bank-Adjusted Read |
|---|---|---|
| Debt/equity | 0.18x | 0.10x on tangible equity |
| Total borrowings | $1,934.6M (**−64% since 2023**) | Only 3.8% of assets |
| Net cash position | **+$5,426M** | Cash $7,360M vs debt $1,935M |
| **Interest coverage** | **0.45x** | ❌ **INVALID** — funding cost sits inside revenue for a bank |
| Current ratio | **0.24x** | ❌ **INVALID** — deposits ($38.2bn) are "current liabilities" |
| Working capital | −$29,286M | ❌ Artificial: deposit-funded balance sheet |
| **Altman Z-Score** | **−0.431 "Distress"** | ❌ **INVALID** — X1 (−0.578) driven by deposit classification. **Disregard.** |
| **Piotroski F-Score** | **4/9 "Weak"** | Partly valid — but F2 & F4 are bank artifacts |
| FCF / FCF yield | −$3,985M / **−19.4%** | ❌ **INVALID** — −$4,438M "working capital" = loan growth |
| **Core cash earnings** | **+$696M** vs NI $481M (1.45x) | ✅ Ex-loan-growth, conversion is healthy |

**Piotroski detail:** genuine deductions are F7 no-dilution (share count +9.5%), F3 ROA decline, F9 asset turnover. F2/F4 failures are artifacts.

---

## 3. Market Risk Profile — **HIGH**

| Metric | Value |
|---|---|
| Annualized volatility | **54.2%** (~4x SPY) |
| Beta vs SPY | **2.42** (profile: 2.33) |
| Max drawdown (252d, reported) | **45.5%** |
| Peak-to-current | **−41.9%** ($32.73 → $19.02, Nov 2025 → Feb 2026) |
| Sharpe (reported) | −0.784 ⚠️ |
| 12-month price return | **+22.2%** ($15.56 → $19.02) |
| 3-year price return | +323% ($4.50 → $19.02) |
| P/E (diluted EPS $0.39) | **48.8x** |
| P/Tangible book ($7.38/sh) | **2.58x** |

⚠️ **Data inconsistency:** the tool's Sharpe of −0.784 is irreconcilable with the observed +22% to +32% trailing-12-month return on 54% vol (implying ~+0.4 to +0.6). I computed returns directly from price history and treat Sharpe as unreliable. Sortino unavailable (no daily return series returned).

A beta of 2.42 means a −20% S&P drawdown implies roughly **−45% to −50%** for SOFI.

---

## 4. Downside Scenario: Revenue −20%

Base: revenue $4,769.6M, operating income $525.9M (11.0%). Cost base $4,243.7M, assumed 65% variable / 35% fixed.

| | Base | Revenue −20% | Severe: −35% + NCO 6.5% |
|---|---|---|---|
| Revenue | $4,770M | $3,816M | $3,100M |
| Operating income | $526M | **$124M** (−76%) | −$178M |
| Incremental provision | — | −$480M (+150bps) | −$896M (+280bps) |
| Pre-tax income | $526M | **−$356M** | −$1,074M |
| Net income | $481M | **≈−$280M** | ≈−$838M |
| Equity after | $10,490M | $10,212M | $9,652M |
| Equity/assets | 20.7% | 19.7% | 18.6% |
| CET1 (est.) | 16.4% | ~15.5% | ~14.6% |
| **Capital breach?** | No | **No** | **No** |

**Conclusion:** a 20% revenue decline plus a 150bp credit shock produces a GAAP loss but leaves equity/assets at ~19.7% and CET1 at ~15.5% — still **2.2x** the regulatory minimum. **No covenant breach, no refinancing cliff, no going-concern question.** Borrowings of $486M short-term are covered **15x** by cash. The pain in a downturn is entirely borne by the equity holder via the multiple and EPS, not by the balance sheet.

---

## 5. Overall Financial Risk Rating

# **MODERATE**
*(Balance-sheet risk: LOW. Equity/market risk: HIGH. Blended: Moderate.)*

The company is **far safer than its -0.431 Z-score, 0.24 current ratio, and -19.4% FCF yield suggest** — those are artifacts of bank accounting. Capital and liquidity are genuinely fortress-like and improving. The risk is **valuation and earnings volatility**, not solvency.

---

## 6. Key Red Flags

1. **Extreme market risk** — beta 2.42, 54% vol, −41.9% drawdown in 14 weeks. The Nov 2025 high of $32.73 is 72% above spot.
2. **Relentless dilution** — shares 900.9M → 1,150.1M (+27.7% in 3 years); ~$3.3bn equity raise in FY2025 (~10% of market cap); SBC $262M/yr.
3. **Rising personal-loan charge-offs** — 2.80% annualized, +20bps QoQ. This is the single best leading indicator of consumer credit stress and the most important number to monitor.
4. **Valuation offers no margin of safety** — 48.8x earnings, 2.58x tangible book, priced for 25%+ growth to persist indefinitely.
5. **Goodwill/intangibles $2.0bn = 19.1% of equity** (Galileo/Technisys) — impairment risk if the Tech Platform segment underperforms.
6. **Earnings-quality caveat** — net income *fell* y/y ($499M → $481M) despite revenue +28.8%; FY2024 net income exceeded operating income by ~$265M, implying a large non-operating tax benefit. The underlying trend (operating income +125%) is far better than the headline.
7. **Accumulated deficit still −$824M** — never earned its way to positive retained earnings; 14 years of cumulative losses.
8. **Deposit franchise is unproven through a stress cycle** — online-only, rate-sensitive deposits carry higher runoff risk than a branch network (partially offset by $7.36bn cash = 14.5% of assets).

**Mitigants:** borrowings cut 64% since 2023 with no maturity wall; net cash of $5.4bn; SBC intensity down from 17.4% (2022) to 5.5% of revenue; net charge-offs improving y/y; equity/assets rising to 20.7%.

---

## Data Gaps (Explicit)
- **Peer comparison: UNAVAILABLE.** `get_sector_peers` returned only Vanguard index funds/ETFs — no valid bank comparables. All relative-valuation conclusions are unsupported.
- **Deposit balance, loan composition (LHFI vs. held-for-sale), uninsured-deposit %, NIM, provision/ACL coverage ratios** — not returned by any available tool. Deposit figures above are **derived** (total liabilities less borrowings) and approximate.
- **Credit ratings / CDS spreads** — unavailable.
- **Sortino ratio** — not computable (no daily return series returned).
- **Sharpe ratio** — reported value appears erroneous; flagged, not used.
- **SEC EDGAR direct fetch returned HTTP 403**; capital ratios sourced from search excerpts of the FY2025 10-K and annual report, not primary retrieval.
- **Altman Z, current ratio, quick ratio, interest coverage, FCF, and FCF yield are reported above only to document that they were computed and rejected** — do not carry them into a valuation or credit conclusion.
