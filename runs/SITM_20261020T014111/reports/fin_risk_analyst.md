# Fin Risk Analyst

- Symbol: SITM
- Elapsed: 530.3s

---
# SITM (SiTime Corporation) — Financial Risk Assessment
**As of:** October 20, 2026 | **Price:** $495.75 | **Market cap:** $14.85B | **Sector:** Technology / Semiconductors

> **Critical data caveat:** SITM executed a transformational balance-sheet change in Q2 2026 (gross debt went from $2.96M to $1,317.6M in one quarter). The standard ratio tools return **FY2025 year-end data and are stale** — e.g. `debt_to_equity: 0.0` and `net_debt_to_ebitda: 379.8` are both artifacts of a pre-refinancing net-cash position and negative EBITDA. All leverage metrics below are recomputed by me on Q2 2026 (6/30/26) data and trailing-twelve-month (TTM) flows through 6/30/26.

---

## 1. Credit Risk Assessment

**Rating: Investment Grade-equivalent on a net basis — but the gross debt stack is new and unseasoned.**

SITM carries **$1,317.6M gross debt** (all long-term) against **$1,921.1M cash and short-term investments**, for **net cash of $603.6M**. There is no near-term refinancing cliff: short-term debt is $0 and current liabilities are only $109.7M against $1,921M of cash. Default risk over any horizon shorter than three years is negligible.

The important qualification is *why* the debt exists. Total assets jumped $1.21B in one quarter while goodwill rose only ~$0 in tandem and cash rose $1.13B — meaning the proceeds are **parked on the balance sheet, not yet deployed**. Two readings: (a) pre-funding an announced acquisition/transaction, in which case the net-cash cushion evaporates on closing and pro-forma leverage becomes ~1.3x gross debt/equity with acquired EBITDA of unknown quality; or (b) a defensive liquidity raise ahead of a capex/working-capital cycle. **This is the single largest unquantified risk in the name and the available data does not disclose the purpose — flagging as a material data gap.**

Interest coverage is the weak link: **EBIT/TTM interest is negative** (TTM EBIT –$7.8M vs. ~$9.0M annualised interest, i.e. **–0.9x**), while **EBITDA/interest is ~5.7x**. The debt is almost certainly a low-coupon convertible (Q2 2026 interest expense of $2.25M on ~$1.3B implies a ~0.7% coupon), which is why coverage is not yet a covenant concern. A convertible also means dilution risk on conversion rather than cash-refinancing risk.

---

## 2. Key Financial Risk Metrics

| Metric | FY2025 (12/31/25) | Q2'26 / TTM (current) | Assessment |
|---|---|---|---|
| Gross debt / equity | 0.004x | **1.29x** | Newly levered |
| Net debt / EBITDA | Net cash | **–$603.6M net cash** | Strong |
| Debt / total assets | 0.4% | **52.6%** | Materially higher |
| Interest coverage (EBIT) | n/a (no debt) | **–0.9x** | Weak |
| Interest coverage (EBITDA) | n/a | **~5.7x** | Adequate |
| Current ratio | 11.3x | **19.4x** | Exceptional |
| Quick ratio | 10.3x | **18.5x** | Exceptional |
| Cash / current liabilities | 9.6x | **17.5x** | Exceptional |
| Altman Z (book equity) | **5.71 — Safe** | **~1.44 — Distress zone*** | See note |
| Piotroski F-Score | **7 / 9** | ~6–7 (est.) | Moderate |
| Retained earnings | –$224.9M | –$212.0M | Accumulated deficit |

*\*The Z-score collapse is mechanical, not operational. The FY2025 Z of 5.71 was computed when x4 (book equity / total liabilities) was 8.35. On Q2'26 data that same term is 0.69 (equity $1,025M / liabilities $1,480M), which drags Z to ~1.44. Substituting **market cap** for book equity — the literal Altman formulation — gives x4 = 10.0 and **Z ≈ 7.8 (deep safe zone)**. With net cash of $604M, the book-equity Z is not signalling bankruptcy risk; it is signalling that the capital structure was levered up in one quarter. I weight the market-cap version.*

**Piotroski detail (FY2025 = 7):** points lost on negative ROA (F1=0) and share dilution (F7=0) — weighted average shares rose 23.1M → 25.0M → 26.5M. On current data F1 would flip to +1 (positive TTM net income) but F5 (lower leverage) would flip to 0, leaving the score roughly unchanged at ~7. Note that F5 and the Z-score are both now penalising a leverage increase that is 100% offset by cash.

---

## 3. Market Risk Profile

| Metric | Value | Read |
|---|---|---|
| Annualised volatility (252d) | **89.5%** | Extreme — ~5x market |
| Beta vs SPY | **3.08** (profile: 2.885) | Near-3x drawdown amplification |
| Max drawdown (252d, tool) | **–48.7%** | Severe |
| Max drawdown (3yr, close-to-close) | **≈ –54.3%** (Dec-2024 $261.03 → Apr-2025 $119.23) | Severe |
| Current drawdown from May-2026 peak | **–45.0%** ($901.48 → $495.75) | De-rating under way |
| Sharpe (0% rf) | **0.96** | Flattered by a +330% 3-yr run |
| Sortino | **Not available** | Data gap |

This is the dominant risk in SITM, and it is **equity risk, not credit risk**. Fundamentals improved dramatically (revenue +126% YoY in Q2'26), yet the stock is down 45% from its May 2026 high — a textbook high-multiple de-rating. A beta of 3.1 means a 15% S&P drawdown mechanically implies a ~45% SITM drawdown before any idiosyncratic factor. Historical realised drawdowns of –48% and –54% within 18 months confirm that 40–55% peak-to-trough moves are *routine*, not tail, events here.

---

## 4. Downside Scenario Analysis — Revenue –20%

**TTM base:** Revenue $467.9M; gross margin 58.7%; total opex $282.5M (SG&A $146.7M, R&D ~$135.8M); D&A $46.7M; EBITDA $51.7M; FCF $83.6M.

| Scenario | Revenue | Gross profit | Op. income | EBITDA | FCF (est.) | Cash position |
|---|---|---|---|---|---|---|
| Base (TTM) | $467.9M | $274.7M | –$7.8M | +$51.7M | +$83.6M | $1,921M |
| **–20% revenue** | $374.3M | $219.7M | **–$62.8M** | **–$15.8M** | **–$25M to –$45M** | $1,921M |
| –40% (severe) | $280.7M | $164.8M | –$117.7M | –$71.0M | –$90M to –$120M | $1,921M |

**Findings:**
- A 20% revenue decline produces an EBITDA loss and modest cash burn — but with **$1.92B cash and $604M net cash, runway exceeds 20 years even in the severe case.** Liquidity risk is effectively nil.
- **There are no financial maintenance covenants disclosed and no debt maturities inside 12 months**, so a revenue shock cannot trigger a technical default.
- **The real downside transmission channel is valuation, not solvency.** At 31.7x TTM sales, 30.5x EV/sales, 275x EV/EBITDA and a **0.56% FCF yield**, a 20% revenue miss would likely compress the multiple by more than it compresses earnings. A de-rating to 15x sales at –20% revenue implies a market cap near $5.6B — a further ~62% downside from today, with the company still solvent and net-cash.
- **Fixed-cost rigidity is high.** Opex of $282.5M against gross profit of $274.7M means the operating line sits almost exactly at breakeven. Every 1% of revenue change moves operating income by ~$4.7M — hence the violent earnings volatility that the 89% vol and 3.1 beta are discounting.

---

## 5. Overall Financial Risk Rating: **MODERATE**

Split assessment, because a single label misleads here:
- **Credit/default risk: LOW.** Net cash $604M, current ratio 19.4x, no near-term maturities, no dividends or buybacks to fund.
- **Liquidity risk: LOW.** Zero refinancing cliff; cash covers current liabilities 17.5x.
- **Market/valuation risk: HIGH.** Beta 3.1, vol 89.5%, routine 45–55% drawdowns, 0.56% FCF yield, 275x EV/EBITDA.

Blended: **Moderate** financial risk. The company will survive anything short of an accounting fraud; the *stock* may not.

---

## 6. Key Red Flags

1. **The $1.3B debt raise is unexplained and undeployed.** Assets and liabilities both jumped ~$1.2B in one quarter with cash simply accumulating. If this pre-funds an acquisition, pro-forma net cash disappears and consolidated leverage could exceed 2x with unproven acquired EBITDA. **This is the #1 issue to resolve before underwriting.**
2. **EBIT interest coverage is negative (–0.9x).** Only EBITDA covers interest, and only ~5.7x. Any covenant defined on EBIT or on a leverage ratio that excludes the cash pile would be tight.
3. **Equity fell $134M in Q2 2026 despite +$18.2M net income.** A ~$152M non-income hit to equity in a single quarter. Most plausible explanation is a mark-to-market (AOCI) loss on the $1.9B securities portfolio into a rising-rate environment (10Y 4.99%, 30Y 5.37%, curve positively sloped at +34bp). **Not directly disclosed in available data — flag as a data gap and verify the investment portfolio duration.** A 7% mark implies duration risk on a very large portfolio.
4. **Stock-based compensation ($114.0M TTM) exceeds free cash flow ($83.6M).** SBC is 24.4% of revenue and **136% of FCF**. FCF net of SBC is **–$30.4M**. Reported cash generation is entirely an artifact of equity compensation; true economic FCF is negative.
5. **Persistent accumulated deficit (–$212.0M)** and a history of losses: net losses in FY2023 (–$80.5M), FY2024 (–$93.6M), FY2025 (–$42.9M). The current profitability is only two quarters old and unproven across a cycle.
6. **Customer/channel concentration risk** — the company sells through distributors (Taiwan, Hong Kong) into communications/enterprise infrastructure. A one- or two-customer program delay could produce the –20% revenue scenario organically.
7. **Tiny absolute scale, huge multiple.** $468M TTM revenue supporting a $14.85B market cap. Valuation leaves no cushion for execution error.

---

## Data Gaps Flagged
- **Purpose and terms of the $1.32B debt** (coupon, conversion terms, covenants, maturity) — not disclosed in available feeds.
- **Sortino ratio** — not computed by the tool.
- **CDS spreads / credit rating** — unavailable (no public rating; likely unrated).
- **Peer comparison** — `get_sector_peers` returned a mega-cap-only list (NVDA, AAPL, MSFT, TSM, AVGO, MU, SKHY, AMD); none are size-comparable to a $15B timing-device specialist, so **relative valuation is a genuine data gap** and no peer benchmarking is asserted here.
- **Segment/customer concentration and backlog** — not available; would materially sharpen the downside scenario.
- **FY2025 Altman Z, Piotroski F, and leverage/liquidity ratios from the ratio tools are pre-refinancing and should not be used as current** — my recomputed figures above supersede them.
