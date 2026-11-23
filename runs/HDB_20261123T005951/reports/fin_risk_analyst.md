# Fin Risk Analyst

- Symbol: HDB
- Elapsed: 109.8s

---
# HDFC BANK LIMITED (HDB) — Financial Risk Assessment

**Critical framing note:** HDB is a large Indian commercial bank (ADR; 1 ADR = 3 ordinary shares). Standard non-financial credit templates — Altman Z, interest coverage, net debt/EBITDA, FCF yield — are **structurally invalid** for a deposit-funded bank. I report them below for completeness but explicitly mark them as non-diagnostic, and substitute bank-appropriate measures (capital adequacy, asset quality, funding mix, ROA/ROE, tangible leverage).

---

## 1. Credit Risk Assessment — **INVESTMENT GRADE (High quality)**

| Evidence | Reading |
|---|---|
| Capital adequacy (Q2 FY27) | **CAR 18.9%**, CET1 **17.1%** vs regulatory minimum 11.9% — ~700bp of headroom |
| Asset quality (Q2 FY27) | **GNPA 1.11%** (from 1.24% YoY), **NNPA 0.37%**; FY26 GNPA 1.15% |
| Credit cost | **0.44%** of advances — benign |
| Ratings | S&P **BBB** (upgraded Aug-2025 on India sovereign upgrade, stable); Moody's investment grade; domestic **CRISIL AAA / ICRA AAA / IND AAA (Stable)** |
| Profitability | ROA 1.66% (FY26), ROE ~13.4%; annual report cites ROA 1.94% |

No covenant breach, no refinancing cliff. Bank funding is deposit-based (borrowings only ~13.7% of liabilities, all long-term at FY26), so there is no maturity wall in the conventional sense. Capital buffers could absorb a multi-year loss cycle without external capital.

## 2. Key Financial Risk Metrics

| Metric | FY2024 | FY2025 | FY2026 | Latest (Q2 FY27) |
|---|---|---|---|---|
| Net income (₹B) | 622.7 | 673.5 | 800.0 | PAT +4.7% YoY |
| Revenue (₹B) | 3,520.9 | 4,195.0 | 5,213.3 | Total income +9.1% |
| ROA | 1.41% | 1.40% | 1.66% | — |
| **Tangible assets/equity (true bank leverage)** | 9.08x | 8.57x | **8.07x** | — |
| Tangible equity/assets | 11.0% | 11.7% | **12.4%** | — |
| Interest expense / revenue | 43.6% | 43.5% | **37.4%** | — |
| Operating margin | 20.0% | 20.5% | 20.6% | PPOP +6.2% YoY |
| NIM | — | — | — | **3.26%** (12-quarter low) |
| CASA / deposits | — | — | — | **31.6%** |
| Loan/deposit ratio | — | — | — | **~99.8%** |
| CAR / CET1 | — | — | 19.7% | **18.9% / 17.1%** |
| GNPA / NNPA | — | — | 1.15% | **1.11% / 0.37%** |

**Automated scores — reported but NOT diagnostic:**
- **Altman Z = 0.343 ("Distress")** — **invalid.** Built for manufacturers. X1 (working capital/TA) and X2 (retained earnings/TA) are structurally zero/garbage for a bank, and X4 (book equity/total liabilities = 0.14) is normal for any deposit-funded lender. The FY2026 balance-sheet row is also partially unpopulated (zero current liabilities, zero retained earnings), which corrupts the input. **Discard.**
- **Piotroski F = 6** — designed for non-financials. The three failed tests are leverage/dilution artifacts (share count +0.7% on ESOPs, equity change, leverage). Directionally consistent with "moderate, not pristine" momentum, not with credit weakness.
- **FCF yield = 1,222%** — **meaningless.** The ₹1.72T "free cash flow" is bank operating cash flow driven by deposit/borrowing inflows, not distributable earnings. **Discard.**
- **Interest coverage 0.55x / net debt/EBITDA 2.43x** — **invalid.** For a bank, interest expense is cost of goods sold, not a financing charge. The real coverage test is capital adequacy (18.9% vs 11.9%).

## 3. Market Risk Profile — **the actual risk in this name**

| Metric | Value | Source |
|---|---|---|
| Max drawdown (3yr+) | **−39.3%** (close $37.67 on 23-Jul-25 → $22.86 on 28-May-26) | Computed from retrieved OHLCV |
| Annualised volatility | **~26%** (15 quarterly close-to-close returns, Sep-22 → May-26) | Own calc; tool failed |
| Beta (5Y, vs S&P 500) | 0.42 | Profile feed |
| Realised downside capture, 2026 | Stock **−29%** vs Nifty 50 **−11.5%** → downside beta ~2.5x | Press |
| Sharpe / Sortino | **~0.0 / ~0.0** | Own calc |
| Price return, Sep-2022 → current ($27.50 → $27.42) | **≈ 0% over ~4 years** | OHLCV |

**Interpretation:** the 0.42 beta is a benchmark artifact (US-market beta for an Indian ADR). Against its own market the stock is a high-beta, high-drawdown instrument that has delivered *zero* price return over four years despite 15–18% loan growth and ROA near 1.7% — a pure **de-rating**, not an earnings collapse. The ADR also layers on INR/USD currency risk and foreign-flow risk: **FII ownership fell from 52.1% (Sep-23) to 39.4% (Sep-26)**, a persistent supply overhang that has repeatedly dominated fundamentals.

## 4. Downside Scenario Analysis — Revenue −20%

Base FY2026 (₹B): revenue 5,213; interest expense 1,952; opex 2,187; PPOP 1,075; net income 800; equity 5,964; assets 48,109.

| Line | Base | Stress (rev −20%) | Severe (rev −20%, credit cost 3.0%) |
|---|---|---|---|
| Revenue | 5,213 | 4,171 | 4,171 |
| Interest expense (−10%, sticky deposits) | 1,952 | 1,757 | 1,757 |
| Opex (−10%) | 2,187 | 1,968 | 1,968 |
| **PPOP** | **1,075** | **446 (−58%)** | **446** |
| Credit cost | 146 (0.44%) | 663 (2.0%) | 995 (3.0%) |
| PBT | 1,075 | **(217)** | **(549)** |
| Net income | 800 | **(163)** | **(412)** |
| Equity impact | — | **−2.7%** | **−6.9%** |
| CET1 (from 17.1%) | — | **~16.5%** | **~15.9%** |
| ROA | 1.66% | (0.34%) | (0.86%) |

**Conclusion:** even a 20% revenue shock combined with a **4.5x normalisation of credit costs** produces a loss equal to under 3% of equity and leaves CET1 roughly 460bp above the regulatory floor. HDFC Bank **cannot plausibly breach solvency or covenants** in this scenario. The binding constraint is the **dividend and growth capital**, not survival — payout would be cut and loan growth throttled. The real damage in a downturn is to the *equity multiple*, not the balance sheet.

**Liquidity stress:** the genuine vulnerability is the **~99.8% loan/deposit ratio**. There is essentially no surplus deposit funding to absorb a deposit outflow; a deposit run or a growth push would force reliance on wholesale borrowings at higher cost, compressing NIM further. This is a profitability risk, not a solvency risk.

## 5. Overall Financial Risk Rating: **MODERATE**

Split rating: **Credit/solvency risk = LOW. Market & earnings risk = MODERATE-to-HIGH.**

The balance sheet is fortress-grade (CET1 17.1%, GNPA 1.11%, AAA domestic). The risk is entirely in the earnings trajectory and the equity price: NIM at a 12-quarter low, zero four-year price return, −39% peak-to-trough drawdown, and a structural foreign-owner exit.

## 6. Key Red Flags

1. **Pre-provision earnings are contracting.** H1 FY27 operating profit fell **−4.8%** while reported PAT rose 11.4% — the gap was provisions collapsing to ₹8,012cr from ₹19,595cr. Profit growth is being manufactured by a lower provision charge, which is not repeatable. **This is the single most important flag.**
2. **NIM at a 12-quarter low (3.26%)** with CASA down to 31.6% and deposits growing 18.8% vs advances 16.2% — growth is being bought with expensive time deposits.
3. **Loan/deposit ratio ~99.8%** — no liquidity slack; growth is deposit-constrained.
4. **FII ownership −12.7pp since Sep-2023** — a persistent, price-insensitive seller that has overwhelmed fundamentals for three years.
5. **Management/leadership transition** — cited in market commentary as an incremental overhang.
6. **−39% drawdown with ~26% vol and ~0 Sharpe** — poor risk-adjusted compounding; downside beta ~2.5x versus the domestic index.

## Data Gaps & Caveats (explicit)

- **Volatility/beta tool unavailable** (dividend-adjusted endpoint not on subscription). Vol, Sharpe and Sortino are my own estimates from retrieved closes; returns are **not dividend-adjusted**, so total-return Sharpe is modestly understated (HDB yields ~1%).
- **FY2026 income statement looks inflated** (+24% revenue) versus the reported trajectory (Q2 FY27 total income +9.1%, H1 +4.3%) — likely a consolidated-vs-standalone or mapping difference. Bank-disclosed metrics (GNPA, CAR, NIM) were prioritised over feed-derived ones for the rating.
- **FY2026 balance-sheet row is partially unpopulated** (zero current liabilities, zero retained earnings, zero goodwill vs ₹3.0T in FY25), which invalidates the automated Altman/liquidity/leverage outputs. My leverage figures use tangible equity (FY25 equity less ₹3.0T goodwill) for comparability — this reconciles the apparent FY25→FY26 equity "drop" from ₹8.62T to ₹5.96T.
- **Peer set unusable** — `get_sector_peers` returned US ETFs/funds (VTI, VFIAX), not Indian banks. No peer multiples computed.
- **Price/market-cap unit ambiguity** — the feed's $27.42 quote is internally consistent with 5.13B shares and $140.6B market cap (≈15.5x trailing earnings), but an ADR = 3 ordinary shares, so the quoted level may not be the tradable ADR price. All **percentage** risk metrics are scale-invariant and unaffected.
- No CDS spread data available; no deposit-maturity ladder or sector-wise NPA breakdown retrieved.
