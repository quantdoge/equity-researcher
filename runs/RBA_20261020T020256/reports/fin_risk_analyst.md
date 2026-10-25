# Fin Risk Analyst

- Symbol: RBA
- Elapsed: 107.9s

---
# RB Global, Inc. (RBA) — Financial Risk Assessment

**Sector:** Industrials / Specialty Business Services (industrial & vehicle auction marketplaces)
**Data basis:** FY2025 annual (period ended 2025-12-31, filed 2026-02-25), FY2021–FY2025 statements, 3-yr price history to 2026-02-27.

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE (high-yield, crossover quality — Ba1 CFR per Moody's)**

RBA sits at the top of the high-yield bucket. Moody's upgraded the corporate family rating to **Ba1** with senior secured at Ba1 and senior unsecured at **Ba2** (source: Investing.com/Moody's coverage — one notch below investment grade on the unsecured line). The company generates genuine, recurring cash: FY2025 operating cash flow of **$995M** and FCF of **$732M** covered cash interest ($195M) roughly **3.7x** on a cash basis.

What keeps it out of investment grade is balance-sheet composition, not cash generation: **59% of assets are goodwill and intangibles** (largely the 2023 IAA acquisition), tangible book equity is **negative $1.06B**, and net leverage of **3.45x** is at the high end of where a Ba1 company typically tolerates. Coverage of 4.2x is adequate but not comfortable for a cyclical, transaction-volume-driven business.

**Leverage trend is deteriorating, not improving:** net debt rose from $4,029M (2024) to $4,810M (2025), **+19%**, while EBITDA was essentially flat (+0.9%, $1,383M → $1,395M). Net debt/EBITDA moved from ~2.9x to 3.45x in one year. Cash interest fell ($234M → $195M) and the Piotroski leverage test passed only because the *ratio* of debt to average assets improved slightly — the absolute debt trajectory is the item to watch.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Read |
|---|---|---|
| Total debt | $5,503M | Short-term $316M + long-term $3,733M = $4,049M; **~$1,454M unreconciled** (likely finance leases) |
| Cash | $694M | |
| Net debt | $4,811M | +19% YoY |
| Net debt / EBITDA | **3.45x** (2.4x on the $4.05B narrower debt figure) | Elevated; rising |
| Debt / equity | 0.91x | |
| Debt / assets | 0.45x | |
| Interest coverage (op. income / interest) | **4.23x** | Tool figure; on EBIT ($740M) it is **3.80x** — use the lower number |
| Current ratio | 1.10x | Thin |
| Quick ratio | 1.02x | Inventory only $140M, so little cushion from inventory |
| Cash ratio | 0.43x | |
| Working capital | $166M = **1.4% of assets** | Structurally thin; drives Z-score down |
| Altman Z-Score | **1.35 — "Distress"** (book-equity version) | **~2.6, grey zone**, if restated with market equity |
| Piotroski F-Score | **7 / 9 — Moderate** | Fails only F7 (share count rose) and F8 (gross margin down) |
| FCF | $732M (15.7% of revenue) | Best-in-five-years |
| FCF yield | 4.91% (on $14.9B mcap) / **~3.9%** on the current $100.27 quote | See data-gap note |

**Altman interpretation:** The "distress" reading is an artifact of (a) book equity instead of market cap and (b) $7.1B of goodwill sitting in total assets. Restating x4 with market equity (~$18.6B / $6.06B liabilities = 3.07) lifts Z to ~2.6 — still **grey zone**, and the underlying drivers (x1 = 1.4% working capital/assets, x5 = 0.39x asset turnover) are genuinely weak. This is not a false signal, only a less alarming one.

**Credit-supportive offsets:** 3.5-year FCF record (2021 $274M → 2025 $732M), ~$694M cash, dividends of $263M covered 2.8x by FCF, and an upgraded rating implying functioning access to capital markets.

---

## 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility (3-yr) | **28.3%** |
| Beta vs SPY | **0.70** (3-yr) / 0.53 (profile, longer window) |
| Max drawdown (3-yr) | **32.6%** (tool) — see note |
| Sharpe ratio | 0.053 (0% risk-free) |
| 3-yr price change (56.09 → 100.27) | **+79%, ~21% annualised** |

**Beta of 0.70 is the most favourable risk fact about this stock** — RBA is only about two-thirds as sensitive as the market to a broad drawdown, and the auction marketplace has some counter-cyclical asset-mix properties (used equipment supply rises in downturns). A 20% market selloff implies a ~14% beta-driven move, before idiosyncratic risk.

**Volatility is event-driven, not systemic.** The price series shows three distinct air-pockets in 12 months:
- **-20.1%** from 118.07 (19-Sep-25) to 94.31 (24-Nov-25)
- **-11.3% in a single session** on 12-Feb-26 (113.10 → 100.30) on 6.1M shares, ~4x average volume — an idiosyncratic shock, not a market beta event
- **-19.4%** from 118.51 (11-Feb-26) to 95.56 (24-Feb-26)

**Two honest flags on this data:**
1. The tool's **32.6% max drawdown** cannot be reconciled with the price series I retrieved, whose worst peak-to-trough is ~20%. The 32.6% figure may come from a longer/differently anchored window. Treat ~20% as the *verified* figure for the past 12 months and 32.6% as the tool's longer-window estimate.
2. The **Sharpe ratio of 0.053 is internally inconsistent** with a +79% / 21%-annualised price move at 28% vol (which implies a Sharpe near 0.75). With a ~4% risk-free rate, the reported figure implies a *negative* excess return. Note as a data-integrity gap; the price return itself is directly observable and is the more reliable input.

**Sortino ratio and CDS spreads: not available** from the toolset — explicit data gaps.

---

## 4. Downside Scenario: Revenue −20%

Revenue $4,671M → **$3,737M** (−$934M). Modelled with two decremental-margin assumptions (RBA has substantial semi-fixed cost — auction sites, technology, 8,350 employees — so 50–65% flow-through is the credible range):

| | Base FY25 | Downside A (−20% rev, 50% decremental) | Downside B (−20% rev, 65% decremental) |
|---|---|---|---|
| Revenue | $4,671M | $3,737M | $3,737M |
| EBITDA | $1,395M | **$928M** | **$788M** |
| D&A (fixed) | $655M | $655M | $655M |
| EBIT | $740M | **$273M** | **$133M** |
| Interest expense | $195M | $195M | $195M |
| **Interest coverage** | 4.23x | **1.40x** | **0.68x — breach** |
| **Net debt / EBITDA** | 3.45x | **5.18x** | **6.10x** (4.26x on narrow debt) |
| FCF (est.) | $732M | **~$450M** | **~$390M** |
| Dividend ($263M) coverage | 2.8x | **1.7x** | **1.5x** |

**The critical insight: cash coverage survives even where accrual coverage fails.** Because D&A is a heavy **14% of revenue** ($655M), EBIT collapses faster than cash flow. In Scenario B, EBIT coverage of 0.68x would trip a typical 2.0–3.0x interest-coverage covenant, yet the company would still produce ~$390M of free cash flow — comfortably covering $195M of *cash* interest and still covering the dividend 1.5x. RBA is **cash-resilient but covenant-fragile** in a severe downturn.

**Net leverage is the binding constraint.** At 5.2x–6.1x, any covenant written at 4.0–4.5x net leverage is breached under either scenario. Absent the actual credit agreement, **I am flagging covenant thresholds as unverified** — this is the single most important missing document.

**Second-order risk in the downside:** a 20% revenue decline in an asset-marketplace model likely reflects falling GTV and *take rates*, exactly the concern that has driven recent drawdowns. Goodwill of $7.1B (59% of assets) against a market cap of ~$18.6B means a sustained GTV decline creates **impairment risk that flows straight through book equity** — already negative on a tangible basis. An impairment would not affect cash or covenants, but would further distort the Z-score and could pressure the rating.

**Liquidity in the downside:** $694M cash plus ~$166M working capital is adequate for 12 months of operations, but with a current ratio of 1.10 and $316M of short-term debt, the **revolver is doing real work here** — and its size and availability are undisclosed in my data.

---

## 5. Overall Financial Risk Rating: **MODERATE**

**Rationale:** Strong and improving free cash generation ($732M, 15.7% margin, best in five years), 4.2x coverage, low beta (0.70), an upgraded Ba1 rating, and a Piotroski score of 7 all argue the company survives a prolonged downturn. Against that: 3.45x and *rising* net leverage, negative tangible equity, a 1.10x current ratio with only 1.4% of assets in working capital, a grey-zone Altman score, and demonstrated 11–20% single-event drawdowns. This is a **moderate-risk credit with high equity volatility** — the equity can be cut 20% without the credit being impaired.

---

## 6. Key Red Flags

1. **Negative tangible book equity (−$1.06B).** Goodwill and intangibles are 58.7% of total assets. Asset coverage for creditors above the lease/finance obligations is effectively nil.
2. **Net leverage is rising into a flat-EBITDA year.** Net debt +19% ($4,029M → $4,811M) with EBITDA +0.9%. Watch for acquisition or finance-lease additions — the cash flow statement shows no acquisitions line, so the $781M increase is **unexplained by the data provided** and needs to be sourced from the 10-K.
3. **Reported gross margin collapse: 48.3% (2023) → 46.8% (2024) → 35.8% (2025).** An 11-point fall in one year is too large to be operational alone and probably reflects cost-of-revenue reclassification, but as reported it fails Piotroski F8 and compresses the buffer for the downside case. **Verify the presentation change.**
4. **Debt components don't reconcile:** total debt $5,503M vs. $4,049M of short+long-term debt — a **$1,454M gap**, almost certainly finance lease obligations. Net leverage of 3.45x is therefore the right number, not the 2.4x the components imply.
5. **Idiosyncratic event risk is real and recurring:** −11.3% in one session (12-Feb-26) on 4x volume; two ~20% drawdowns within twelve months. External coverage also indicates further pressure into mid-2026 around take-rate concerns — i.e., the equity's risk is concentrated in pricing/mix, not in the macro cycle, which is exactly where a 20% revenue shock would originate.
6. **Thin working capital (1.4% of assets) and a 1.10x current ratio** leave almost no liquidity slack; the revolver is load-bearing but undisclosed.
7. **Data-quality flag:** stock-based compensation reported as **$0** for FY2025 (vs. $62.4M in FY2024). This is almost certainly a missing field, not a real change, and it means FCF is modestly overstated.

---

## Data Gaps (explicitly flagged)

- **Debt maturity schedule by year** — not available. With $316M short-term and $3.7B long-term, the refinancing cliff cannot be dated. *Highest-priority gap.*
- **Revolver size, availability, and covenant thresholds** — not available.
- **CDS spreads, Sortino ratio, peer leverage comparison** — not available.
- **Market cap / quote divergence:** company profile shows $79.81 and $14.78B market cap; the price history ends at **$100.27 on 2026-02-27** (implying ~$18.6B). FCF yield is therefore 4.91% or 3.9% depending on which is used. External references to trading near $87 in later 2026 suggest the series is stale relative to the quote — both are reported above rather than resolved.

**Bottom line:** RBA passes the survival test on cash flow and fails it on balance-sheet aesthetics. It is a **Ba1 credit with a levered, goodwill-heavy balance sheet and equity that trades like a high-beta industrial despite a 0.70 measured beta**. In a −20% revenue scenario it remains cash-generative and dividend-covering, but likely breaches a net-leverage covenant at 5–6x — meaning refinancing terms, not solvency, are the transmission mechanism of risk here.
