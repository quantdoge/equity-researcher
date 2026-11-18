# Fin Risk Analyst

- Symbol: SPCX
- Elapsed: 57.2s

---
# SPCX — Space Exploration Technologies Corp.
## Complete Financial Risk Assessment
*As of 2026-11-17 | Price $141.70 | Market cap ~$1.867T*

---

## 1. Credit Risk Assessment

**Rating: INVESTMENT GRADE (Baa1 / BBB / BBB+) — Solid IG, low end of the band**

Verified agency ratings: Moody's **Baa1** (stable), S&P **BBB**, Fitch **BBB+**, all assigned at/after the June 2026 IPO.

The balance sheet is genuinely strong and has *improved materially* since FY2025 — the pre-computed ratio tools are stale. On the latest Q3 2026 balance sheet:

| Metric | FY2025 | Q3 2026 |
|---|---|---|
| Total debt | $22.90B | $38.84B |
| Cash & ST investments | $24.75B | **$89.86B** |
| Net debt | -$1.85B | **-$51.0B (net cash)** |
| Debt / equity | 0.55x | **0.22x** |
| Debt / assets | 25.0% | **15.3%** |
| Total equity | $41.3B | **$176.8B** |

Net cash of ~$51B against $38.8B gross debt means the company could retire its entire debt stack from the balance sheet. Short-term debt is only $2.70B (6.9% of total), covered **33x** by cash. There is no refinancing cliff.

**Interest coverage is the one soft spot.** TTM interest expense is $2.541B (Q4'25 $0.573B + Q1'26 $0.664B + Q2'26 $0.629B + Q3'26 $0.675B). Against TTM EBIT of $2.963B that is **1.17x** — thin. But EBITDA/interest is **5.44x**, and TTM EBIT is dragged down by a loss-making H1 2026. On Q3 2026 alone, EBIT/interest is 6.9x. This is a company whose coverage has crossed from negative (FY2025 EBIT coverage **-1.33x**) to comfortably positive within three quarters.

**Altman Z-Score — the tool output is not usable and I am discarding it.** The tool reports **0.166 ("Distress")** using FY2025 book equity. That is an artifact: x4 (equity/liabilities) is meaningless for a company with $1.87T market cap and only $176.8B book equity. Recomputing with the correct public-company x4:

- x1 (WC/TA) = 68.237/254.045 = 0.269
- x2 (RE/TA) = -37.448/254.045 = -0.147
- x3 (EBIT/TA) = 2.963/254.045 = 0.012
- x4 (Mkt cap / TL) = 1,866.8/77.277 = **24.16**
- x5 (Sales/TA) = 32.043/254.045 = 0.126

**Z = 14.8 → safe zone.** Even the book-equity version (x4 = 2.29) gives 1.65, i.e. only marginally in distress — versus the tool's 0.17. This is a $1.7T sensitivity to one input; the "Distress" label should be ignored entirely. The only legitimate signal in it is the **-$37.4B retained earnings deficit**, reflecting cumulative historical losses now being offset by a large paid-in capital base.

**Piotroski F-Score: 5/9 (Moderate), FY2025.** Components: positive operating cash flow ✓, accrual quality ✓, positive equity change ✓, no dilution ✗ (in fact heavy issuance), gross margin improvement ✓; negative ROA ✗, no ROA improvement ✗, higher leverage ✗, lower asset turnover ✗. On a TTM basis the score would improve (H2 2026 turned ROA positive), so 5/9 is a lagging read.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Assessment |
|---|---|---|
| Debt / equity | 0.22x | Very low |
| Debt / assets | 15.3% | Very low |
| Net debt / EBITDA | **Net cash -3.7x** | No leverage |
| Gross debt / EBITDA | 2.81x | Low |
| EBIT / interest | 1.17x (TTM) | **Thin** |
| EBITDA / interest | 5.44x | Adequate |
| Current ratio | 3.08x | Strong |
| Quick ratio | 3.00x | Strong |
| Cash ratio | 2.74x | Strong |
| Cash / short-term debt | 33.3x | No cliff |
| Working capital | $68.2B | Ample |
| Altman Z (market-cap) | ~14.8 | Safe (book version 1.65; tool's 0.17 is invalid) |
| Piotroski F | 5/9 | Moderate |
| FCF yield (TTM) | **-2.1%** | Negative |
| Cash runway | **~2.3 yrs** at current burn | Adequate |

**Cash runway:** $89.86B cash ÷ ~$9.8B quarterly FCF burn = **9.2 quarters**. Q3 2026 burn was $9.96B and capex is accelerating ($19.6B in Q3 alone), so the realistic runway is ~2.0–2.3 years absent new capital. Mitigant: the company raised ~$85B of equity in Q2 2026 (book equity $41.6B → $127.2B), demonstrating deep access to capital markets.

**Note on the FCF yield tool:** it returned -3.37% using a **$414.6B** market cap — a stale FY2025 share count (2.93B) rather than the current ~13.2B shares. Recomputed on the actual $1.867T market cap: TTM FCF of **-$39.27B** (OCF $15.76B less capex $55.03B) gives **-2.10%**.

---

## 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility | **78.9%** |
| Beta vs SPY | **2.42** |
| Max drawdown (close-to-close) | **-46.4%** |
| Max drawdown (intraday peak-to-trough) | **-53.5%** ($225.64 → $104.83) |
| Sharpe ratio | **0.015** (economically zero) |
| Current price vs. peak | -37.2% |

The drawdown is fully verifiable in the price data: closing high $201.80 (2026-06-16) to closing low $108.27 (2026-08-05). The stock has round-tripped violently — down 46% in seven weeks, back to $171 by early October, back down to $141.70 now.

**Beta of 2.42** means a 20% SPY drawdown implies roughly a **48% SPCX decline**. A zero Sharpe ratio means five months of extreme volatility has delivered no risk-adjusted return whatsoever — all volatility has been uncompensated.

**Major caveat:** the public trading history is only ~5.5 months (IPO 2026-06-12). Every statistic in this section is estimated from ~115 daily observations during a lockup-era, post-IPO period. Vol, beta, and drawdown are directionally informative but statistically fragile. Also note the profile feed reports **beta = 0** (missing data); the 2.42 figure is the computed one.

**Rate environment:** the 10Y UST is at 5.13% with a +39bp 2s10s spread (no inversion). Elevated long rates are a material headwind for a long-duration, 58x-sales equity and raise the cost of the $36.1B long-term debt.

---

## 4. Downside Scenario: Revenue -20%

Applied to TTM revenue of $32.04B (a ~$6.4B revenue shock), holding gross margin at the TTM 56.7%:

| Line | Base (TTM) | Stress (-20%) |
|---|---|---|
| Revenue | $32.04B | $25.63B |
| Gross profit | $18.18B | $14.53B |
| EBITDA | $13.81B | **$10.20B** |
| EBIT | $2.96B | **-$0.66B** |
| Interest | $2.54B | $2.54B |
| EBITDA / interest | 5.4x | **4.0x** |
| EBIT / interest | 1.17x | **Negative** |

**Solvency conclusion: the company survives comfortably.** EBITDA coverage of 4.0x still services debt, net cash of $51B and $176.8B of book equity provide an enormous buffer, and no covenant is plausibly tripped by a 20% revenue decline. **This is not a credit event.**

**The real damage is to FCF and valuation.** With capex held at $55B/yr, FCF deteriorates to roughly -$42B and runway compresses to ~2.1 years. Even with a 20% capex cut, FCF is ~-$32B and runway ~2.8 years. At 58x TTM sales and 135x TTM EBITDA, a 20% revenue miss would rationally compress the multiple far more than 20% — a 30–50% equity drawdown is the plausible outcome, well within the 46% drawdown already observed. **The downside scenario is a price event, not a default event.**

---

## 5. Overall Financial Risk Rating

## MODERATE

Split explicitly, because the two halves point in opposite directions:

- **Balance-sheet / credit risk: LOW.** Investment grade (Baa1/BBB/BBB+), net cash, 0.22x D/E, 3.08x current ratio, no refinancing cliff, $89.9B liquidity.
- **Market / valuation risk: HIGH.** 79% volatility, 2.42 beta, zero Sharpe, 58x sales, negative FCF, 2-year cash runway, and a business model dependent on continuous external capital.

The company will not fail. The equity can lose half its value without the company being remotely distressed.

---

## 6. Key Red Flags

1. **Persistent negative free cash flow at scale.** TTM FCF -$39.3B, worsening each quarter in 2026 (Q1 -$9.1B → Q2 -$16.0B → Q3 -$10.0B). Capex of $55.0B TTM against OCF of just $15.8B. Growth is being financed, not generated.
2. **Capital-markets dependency.** ~$85B equity raise in Q2 2026. Runway is ~2.3 years; the model requires repeated access to equity or debt markets. A closed capital market is the true tail risk.
3. **Extreme dilution.** Diluted weighted shares went from 2.93B (FY2025) to **12.48B** (Q3 2026) — roughly 4.3x. Per-share economics are being diluted almost as fast as revenue grows.
4. **Thin EBIT coverage (1.17x)** and $2.54B of annual interest expense that is still growing. Interest now consumes 86% of EBIT.
5. **Goodwill/intangibles ballooned** from $12.9B (Q2 2026) to **$54.8B** (Q3 2026), now 21.6% of assets, following a ~$41.8B acquisition. Material impairment risk and it distorts ROA and asset-turnover comparisons.
6. **Retained earnings deficit of -$37.4B** — a decade-plus of cumulative losses, masked by paid-in capital.
7. **Valuation, not leverage, is the risk.** $1.87T market cap on $32.0B TTM revenue (58x) and $13.8B EBITDA (135x). Any growth deceleration produces violent multiple compression.
8. **Statistically fragile risk metrics** — 5.5 months of price history; beta and vol estimates carry wide error bands.

---

## Data Gaps (explicitly flagged)

- **Debt maturity schedule unavailable** — cannot confirm the term structure of the $36.1B long-term debt. Short-term debt is only $2.7B, so near-term risk is low regardless.
- **Reported net debt does not reconcile.** The Q3 2026 field shows -$12.45B, but cash & ST investments of $89.86B minus total debt of $38.84B = **-$51.0B**. Likely the feed excludes restricted or strategic investments. I used the $51.0B figure throughout; the discrepancy is a ~$39B swing and should be verified against the 10-Q.
- **No segment reporting** (Starlink vs. Launch vs. Starshield). Moody's commentary indicates Starlink is the primary cash generator — a concentration that cannot be quantified from available data.
- **No CDS spreads**; ratings used as the credit-market proxy.
- **Peer comparables not computed.** The sector feed returns legacy Industrials/Aerospace names (GE, RTX, LMT, CAT) at 2–15x earnings multiples; they are not meaningful valuation comps for a 58x-sales growth issuer. I deliberately did not force a comparison.
- **Pre-built ratio tools (leverage, liquidity, Altman, FCF yield) run on FY2025 annual data and are three quarters stale** on a company transforming this fast. All metrics above are recomputed on TTM/Q3 2026 data.
