# Fin Risk Analyst

- Symbol: SITM
- Elapsed: 123.9s

---
I have sufficient data. Writing the assessment now.

---

# SiTime Corporation (SITM) — Financial Risk Assessment

**As of:** Q3 2026 (period ended 30-Sep-2026) · Latest price $378.29 · Market cap ~$11.43B
**Critical context:** The company was transformed on **1-Jul-2026** by the ~$3.0B acquisition of **Renesas' timing business** (≈$1.5B cash + ~3.56M shares), funded by **$1.32B of 0% convertible senior notes due 15-Jun-2031**. All FY2025 and prior-period ratios below are therefore **pre-deal and stale**; I have recomputed the key ones on pro-forma TTM/Q3-26 data.

---

## 1. Credit Risk Assessment

**Rating: Sub-Investment Grade (BB–/B+ equivalent, unrated)** — *not* distress.

The capital structure is now materially levered, but structured in a way that is unusually benign for cash flow:

| Feature | Detail | Risk read |
|---|---|---|
| Instrument | $1.32B 0% convertible senior notes, unsecured | **Zero cash coupon** — no cash interest burden |
| Maturity | 15-Jun-2031 (single bullet, no amortisation) | No near-term refinancing cliff |
| Conversion price | ~$1,040/sh (0.9611 sh per $1,000; **~2.75x** current price) | Effectively debt — must be repaid in cash |
| Covenants | Convertible notes — no financial maintenance covenants typical | No technical default trigger on EBITDA |

The absence of cash interest and maintenance covenants means **default probability over the next 3 years is very low**. The problem is not serviceability — it is that **$1.32B must be found in cash by mid-2031**, and the business does not generate it.

---

## 2. Key Financial Risk Metrics (pro-forma TTM to 30-Sep-2026)

| Metric | Value | Assessment |
|---|---|---|
| Revenue (TTM) | $683.0M | +61% y/y FY25; Q3-26 step-up is acquisition consolidation |
| Gross margin (TTM) | 56.2% (Q3-26: 51.6%) | **Declining** — 64.5% (FY22) → 51.6% (Q3-26); mix dilution from acquired business |
| Operating margin (TTM) | 3.3% | Thin; FY25 was –18.5% |
| Total debt | $1,319.1M (all long-term) | |
| Cash & ST investments | $324.4M | |
| **Net debt** | **$994.8M** | |
| Debt / equity | 0.38x | Looks low only because equity is goodwill-inflated |
| **Net debt / EBITDA (GAAP)** | **7.7x** | High |
| Net debt / "cash EBITDA" | ~2.8x | Adjusts ~$232M est. acquired-intangible amortisation |
| Interest coverage | 3.1x GAAP; **n/a on cash basis (0% coupon)** | GAAP interest is non-cash issuance-cost amortisation |
| Current ratio | 5.56x | Strong |
| Quick ratio | 4.62x | Strong |
| Cash ratio | 2.74x | Strong |
| **Altman Z (post-deal, book equity)** | **1.63 — DISTRESS ZONE** | vs 5.71 reported on stale FY2025 data |
| Altman Z (market-cap equity) | ~4.84 — Safe zone | Huge divergence |
| Piotroski F-Score | 7 (FY2025, pre-deal) | **Stale**; pro-forma ~4–5 (leverage up, dilution, ROA collapse) |
| FCF (TTM) | $39.6M | |
| **FCF ex-SBC** | **–$81.6M** | SBC $121.2M = 17.8% of revenue |
| FCF yield | ~0.35% | Negligible |
| Goodwill & intangibles | $4,155.8M | **83% of assets; 119% of equity** |
| **Tangible book value** | **–$662.5M** | Negative |
| Retained earnings | –$207.6M | Never cumulatively profitable |

**The single most important number:** tangible book value is **negative $663M**. Reported equity of $3.49B exists only because of acquisition goodwill. This is why the book-equity Altman Z (1.63) and market-equity Altman Z (4.84) tell opposite stories.

---

## 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility (3y) | **86.8%** |
| Beta vs SPY | **2.85** (profile: 2.91) |
| Max drawdown (3y) | **–60.6%** (Dec-24 peak $268 → Apr-25 trough $105) |
| Sharpe ratio (0% rf) | 0.854 |
| Sortino ratio | *Not available — data gap* |

This is a **high-beta, high-volatility equity**. At beta 2.85, a 20% S&P drawdown mechanically implies a ~57% SITM drawdown. The stock has already delivered a –60.6% drawdown within the last 18 months, and rallied ~290% off that low to a Feb-2026 peak of $438 before retreating to $378. Volatility of 87% means **±5.5% daily moves are a one-sigma event** — position sizing, not fundamentals, is the dominant risk control here.

**Valuation is the primary downside vector:** 16.7x TTM sales, ~18.2x EV/sales, ~96x EV/GAAP-EBITDA, ~430x TTM earnings. There is essentially no valuation support; the equity is a growth-duration asset that reprices violently on any growth disappointment or rate move (10Y UST at 5.13%, curve positively sloped — a hostile backdrop for long-duration multiples).

---

## 4. Downside Scenario Analysis: Revenue –20%

TTM revenue $683M → $546M. Holding gross margin at ~53% (acquired mix), opex cut 8%:

| Line | Base (TTM) | –20% Revenue |
|---|---|---|
| Revenue | $683.0M | $546.4M |
| Gross profit (53%) | $384.1M | $289.6M |
| Opex | $361.6M | $332.7M |
| EBIT | $22.5M | **–$43.1M** |
| D&A | $106.6M | ~$110M |
| EBITDA (GAAP) | $129.1M | **+$66.9M** |
| Cash interest | $0 | $0 |
| Capex | $50.2M | $40M |
| FCF | $39.6M | **~+$40M to +$60M** |

**Conclusion: a 20% revenue decline does NOT create a liquidity crisis.** With $324M cash, zero cash coupon, and FCF that stays roughly flat (working-capital release offsets EBITDA loss), cash runway is not a binding constraint. Net debt/GAAP-EBITDA would rise to ~15x and cash-EBITDA leverage to ~3.3x — uncomfortable but not a breach, since there are no maintenance covenants.

**What breaks instead:** (a) **goodwill impairment** — the acquired business carries $4.16B of goodwill/intangibles; a sustained miss makes a multi-hundred-million impairment highly likely, which would crush book equity and the book-based Z-score further; (b) **the 2031 refinancing** — at a 20%-lower revenue base with ~$40M FCF, repaying $1.32B is impossible without equity issuance or a dilutive convert. In a –40% stress case (EBITDA → roughly breakeven, FCF ~–$25M), cash burn is ~$25M/qtr against $324M — roughly 3 years of runway, still survivable, but the equity would be deeply impaired.

---

## 5. Overall Financial Risk Rating: **MODERATE**

Split explicitly, because the two halves point in different directions:

- **Liquidity / solvency risk: LOW.** $324M cash, 5.6x current ratio, 2.7x cash ratio, zero cash interest, no covenants, no maturity before 2031, positive operating cash flow (+$89.8M TTM).
- **Balance-sheet quality & equity risk: HIGH.** Negative tangible book, goodwill = 119% of equity, 7.7x GAAP leverage, FCF negative ex-SBC, 87% volatility, 2.85 beta, ~17x sales.

The company will **not** be forced into a liquidity event. It **can** be forced into a dilutive equity raise or a value-destroying impairment.

---

## 6. Key Red Flags

1. **Goodwill-dominated balance sheet.** $4.16B of goodwill/intangibles = 83% of assets and 119% of equity → **tangible book value –$663M**. One quarter of combined results exists to validate this. Impairment is the highest-probability negative credit event.
2. **$1.32B convertible bullet, June 2031.** Conversion price ~$1,040 (2.75x spot) means it is functionally **straight debt**. No amortisation, no sinking fund. Refinancing risk is deferred, not eliminated — and the business cannot self-fund repayment.
3. **FCF is an accounting artefact of stock compensation.** GAAP FCF +$39.6M, but SBC is $121.2M (17.8% of revenue) → **FCF ex-SBC is –$81.6M**. Shareholders are funding the "free" cash flow.
4. **Gross margin erosion.** 64.5% (FY22) → 57.0% (FY23) → 51.6% (FY24) → 53.6% (FY25) → 51.6% (Q3-26). The acquired Renesas business is structurally lower-margin; the blended franchise quality is deteriorating as it scales.
5. **Altman Z of 1.63 (book equity) sits in the distress zone** post-deal. The 5.71 reported by the screener is a pre-acquisition artefact.
6. **Never cumulatively profitable.** Retained earnings –$207.6M after 20+ years of operation.
7. **Extreme market-risk profile.** 86.8% vol, 2.85 beta, –60.6% max drawdown, ~430x earnings, ~17x sales. A 10Y yield at 5.13% is a direct headwind to this multiple.

---

## 7. Data Gaps (flagged)

- **Income statement has no R&D line** — opex analysis uses SG&A only; true operating cost structure is understated.
- **D&A is not split** between depreciation and acquired-intangible amortisation. My "cash EBITDA" (~$361M) and 2.8x leverage figure rest on an **estimated ~$232M intangible amortisation**; treat as directional.
- **Quarterly EBITDA field is corrupt** for Q3-26 (D&A = 0, EBITDA = EBIT = $9.62M). I computed EBITDA manually as EBIT + D&A.
- **Annual balance-sheet `net_debt` field is inconsistent** for FY2025 (–$12.0M vs cash-minus-debt of –$803.7M). Used own calculation throughout.
- **No debt maturity schedule, credit rating, or CDS data** available. No covenant detail beyond the convertible indenture summary.
- **Price history feed ends 20-Feb-2026** while financials and the yield curve run to Nov-2026 — the vol/beta/drawdown metrics may not reflect the most recent 9 months. Sortino ratio unavailable.
- Peer benchmarking not performed: the sector peer list returned mega-caps (NVDA, AVGO, TSM) that are not meaningful comparables for a $11B timing-component specialist.
