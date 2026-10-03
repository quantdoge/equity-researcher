# quant_engineer

_2026-08-23T09:23:54+00:00_

# CMG Peer Cross-Sectional & Fundamental Computation — Attributed Report

**Execution constraint disclosed up front:** this run's `fmp_call` budget was exhausted after 10 calls (annual income statements for all 8 symbols + balance sheets for CMG and CAVA). The endpoint then refused all further calls. I compensated with (a) files a **prior agent had already saved to this same run workspace** (CMG cashflow FY2016–25, CMG key-metrics and metrics-ratios FY2016–25, CMG as-reported statements, CMG prices through 2026‑08‑21, TXRH/CMG growth files) and (b) web sources for the earnings-surprise history. **Not retrievable and therefore absent:** `key-metrics-ttm`, `metrics-ratios(-ttm)`, `financial-scores` for the symbols, balance sheets/cashflows for the 6 non-CMG/CAVA peers, and FMP's `calendar/earnings-company`. Every gap is flagged below; nothing was proxied silently.

**Data date context:** "today" ≈ 2026‑08‑23. All 8 companies have Dec‑2025 fiscal year-ends and filed FY2025 10‑Ks in Feb 2026, so **FY2025 = TTM through each company's FY2025 year-end**. TTM through Q2 2026 (CMG reported 7/29/2026) is *not* in FMP annual data on disk — flagged where relevant.

---

## 1. FY2025 Cross-Sectional Table (8 symbols)

**Source:** `statements/income-statement` (annual, FY2025 & FY2024 rows, pulled this run). **Formulas:** gross margin = `grossProfit/revenue`; operating margin = `operatingIncome/revenue`; net margin = `netIncome/revenue`; growth = `revenue_FY25/revenue_FY24 − 1`. All values FMP-reported USD.

| Symbol | FY end | Rev FY25 ($M) | Rev growth YoY | Gross margin | Op margin | EBIT margin* | Net margin | Net margin (TTM=FY25) |
|---|---|---|---|---|---|---|---|---|
| CMG | 12/31 | 11,925.6 | **+5.41%** | 25.38% | 16.88% | 16.88% | 12.88% | 12.88% |
| CAVA | 12/28 | 1,179.7 | +22.41% | 18.38% | 6.73% | 6.00% | 5.40% | 5.40% |
| SHAK | 12/31 | 1,445.3 | +15.38% | 17.98% | 5.93% | 5.17% | 3.16% | 3.16% |
| WING | 12/27 | 696.9 | +11.35% | 82.62% | 27.58% | 39.17% | 25.01% | 25.01% |
| TXRH | 12/30 | 5,878.1 | +9.39% | 12.42% | 8.55% | 8.18% | 6.90% | 6.90% |
| MCD | 12/31 | 26,885.0 | +3.72% | 57.41% | 46.10% | 46.42% | 31.85% | 31.85% |
| YUM | 12/31 | 8,214.0 | +8.81% | 46.17% | 30.80% | 31.37% | 18.98% | 18.98% |
| DPZ | 12/28 | 4,940.0 | +4.96% | 39.95% | 19.31% | 19.56% | 12.18% | 12.18% |
| **Median (all 8)** | | | **9.10%** | **32.66%** | **18.09%** | | **12.53%** | **12.53%** |
| Median (ex-CMG) | | | 9.39% | 39.95% | 19.31% | | 12.18% | 12.18% |

\*EBIT margin (`ebit/revenue`) shown because FMP's `operatingIncome` embeds non-operating items for some peers: WING −$80.8M charge (impairment/refranchising), TXRH +$21.8M gains, CAVA +$8.5M, SHAK +$11.0M. CMG is unaffected (`operatingIncome` = `ebit` = $2,012.8M). **Context (not a computed figure):** MCD/YUM/DPZ/WING are substantially franchised, which structurally inflates margins on their reported (net) revenue vs. company-operated models like CMG.

**CMG rank within the 8** (1 = best; higher is better on margins/growth):
- Gross margin: **5th** (order: WING, MCD, YUM, DPZ, **CMG**, CAVA, SHAK, TXRH)
- Operating margin: **5th** (MCD, YUM, WING, DPZ, **CMG**, TXRH, CAVA, SHAK)
- Net margin: **4th** (MCD, WING, YUM, **CMG**, DPZ, TXRH, CAVA, SHAK)
- Revenue growth: **6th** (CAVA, SHAK, WING, TXRH, YUM, **CMG**, DPZ, MCD)
- TTM net margin: same as net margin, **4th** (all 8 have Dec‑2025 FYEs and filed FY2025 10‑Ks, so TTM = FY2025; `key-metrics-ttm` itself was not retrievable)

**Latest-TTM multiples & ROIC — CMG only** (TTM = FY2025, through 2025‑12‑31). Sources: `statements/key-metrics` and `statements/metrics-ratios` (FY2025 rows, prior-agent files), computed cross-checks from `statements/balance-sheet-statement` + income statement + `chart` EOD prices:

| Metric | FMP-published (FY2025) | My computed cross-check |
|---|---|---|
| EV/EBITDA | **24.84×** (`evToEBITDA`; EV $58.98B / EBITDA $2,374.2M) | 22.54× lease-inclusive (EV $53.51B); 20.30× classic no-leases (EV $48.20B) — see caveat † |
| P/E | **32.17×** (`priceToEarningsRatio`) | Verified: $37.00 close 12/31/25 ÷ $1.15 basic EPS = 32.17 (diluted: 32.46). At 8/21/26 close $36.90 ÷ FY25 diluted $1.14 = 32.37 (mixed-period). External: TradingKey TTM P/E 33.65× (TTM EPS thru Q2'26 ≈ $1.10) |
| ROIC | **18.97%** (`returnOnInvestedCapital`; FMP investedCapital $7,443.1M) | 23.22% end-of-IC / 24.55% average-IC, lease-inclusive (formula below) |
| ROCE (suppl.) | 25.78% | — |
| TTM net margin | **12.88%** (`netProfitMargin`) | Matches `netIncome/revenue` exactly |

† **FMP data-quality finding:** FMP's FY2025 `totalDebt` ($9,849.2M) **double-counts CMG's operating-lease liabilities** — `longTermDebt` ($4,773.4M) is identical to `capitalLeaseObligationsNonCurrent`, plus `shortTermDebt` $302.4M; FY2025 interest expense is $0, confirming no borrowings. True lease liabilities = **$5,075.8M**. FMP's EV = market cap $49.48B + netDebt $9.50B → hence the inflated 24.84×. My variants: EV_leaseInclusive = mktCap + leases − cash&STI; EV_classic = mktCap − cash&STI − LT investments. My ROIC = NOPAT/IC where NOPAT = EBIT × (1 − `incomeTaxExpense/incomeBeforeTax`) = $2,012.8M × (1 − 23.58%) = $1,538.3M; IC = equity + leases − cash&STI − LT investments ($6,624.8M FY25, $5,905.2M FY24). Ex-lease IC ($1,549.0M) yields a degenerate 99.3% — not meaningful for a debt-free operator; leases are the operative capital. FMP's own ROIC formula (IC $7,443.1M) could not be reverse-engineered exactly — noted, not guessed.

**Peer EV/EBITDA, P/E, ROIC and their medians: NOT COMPUTABLE this run** — missing inputs: peer market caps/prices (screener file on disk does not contain these symbols) and peer balance sheets (`key-metrics-ttm`/`metrics-ratios-ttm` not pulled). One supplementary computed figure: **CAVA ROIC = 7.47%** (NOPAT $63.7M / IC $852.9M, same formula, from `bs_cava.json` + `is_cava.json`).

**Verification passed:** CMG & TXRH growth match FMP's own `financial-statement-growth` (5.41%) and `income-statement-growth` (9.39%) files; CMG margins match `metrics-ratios` to the decimal.

---

## 2. CMG Margin Trendline FY2021–FY2025

**Source:** `statements/income-statement` (CMG, annual; identical to FMP `metrics-ratios` margins every year — cross-checked).

| FY | Revenue ($M) | Gross margin | Operating margin | Net margin |
|---|---|---|---|---|
| 2021 | 7,547.1 | 22.62% | 10.67% | 8.65% |
| 2022 | 8,634.7 | 23.88% | 13.44% | 10.41% |
| 2023 | 9,871.6 | 26.20% | 15.78% | 12.45% |
| 2024 | 11,313.9 | 26.67% | 16.94% | 13.56% |
| 2025 | 11,925.6 | 25.38% | 16.88% | 12.88% |

Read: margins expanded ~440–630 bps from FY2021 to a FY2024 peak, then rolled back ~130–70 bps in FY2025 (comps decelerated).

## 3. CMG Revenue CAGR & $11.93B Reconciliation

- **CAGR 2019–2025** = (11,925.601/5,586.405)^(1/6) − 1 = **13.47%** (FY2019 and FY2025 revenue from `statements/income-statement`).
- **FY2025 vs FY2024 growth** = 11,925.601/11,313.853 − 1 = **+5.41%** (matches FMP `financial-statement-growth` exactly).
- **Reconciliation vs company-reported $11.93B:** FMP FY2025 revenue = **$11,925.6M**, i.e. **−$4.4M (−0.037%)** vs $11,930M — a rounding-level difference; $11,925.6M rounds to $11.93B. **No material discrepancy.** Externally corroborated: TradingKey's CMG page shows revenue 11.93B / +5.41%.
- **One vendor nuance flagged:** FMP's *as-reported* (XBRL) view (`as-reported-income-statements`) tags `revenues` = $11,679.4M for FY2025 ($11,111.7M FY2024) — $246.2M ($202.2M) below the standardized total, consistent with the tag capturing food & beverage revenue and excluding delivery-service revenue (my inference from the residual; the standardized statement used throughout includes it and matches the company total).

## 4. CMG "Rule of 40"

**Source:** `statements/cashflow-statement` (CMG, FY2025 row, prior-agent file) + income statement. **Formula:** FCF = `operatingCashFlow` − |`capitalExpenditure`|; FCF margin = FCF/revenue; Rule of 40 = revenue growth % + FCF margin %. Annual FY2025 used (available; it is also the TTM through 2025‑12‑31 — TTM through Q2 2026 is not on disk).

| Component | FY2025 | (FY2024 context) |
|---|---|---|
| Revenue growth | +5.41% | +14.61% |
| Operating cash flow | $2,113.9M | $2,105.1M |
| Capex | $666.3M | $593.6M |
| FCF | $1,447.6M | $1,511.5M |
| FCF margin | 12.14% | 13.36% |
| **Rule of 40** | **17.55** | **27.97** |

(FMP's own `freeCashFlow` field matches my OCF−capex arithmetic to the dollar both years.) Note: Rule of 40 is a software-sector heuristic, reported here as specified; on this metric CMG fell from ~28 to ~17.5 as growth decelerated.

## 5. CMG AUV

**Formula:** FY2025 revenue ÷ 4,056 company-operated units (unit count **user-supplied**, not an FMP field) = $11,925,601,000 / 4,056 = **$2.94M per unit** ($2,940,237). Caveat: this simple division spreads *total* revenue across all year-end units including those opened during 2025; a company-defined AUV (restaurants open ≥12 full months) will be higher — the two are not the same measure.

## 6. CMG Earnings Surprise Aggregation (last ~11 quarters)

**FMP `calendar/earnings-company` could not be pulled (call budget exhausted).** Fallback: web retrieval (Zacks-syndicated articles via Yahoo Finance/TradingView/TraderFox/Globes/public.com, and TradingKey's earnings-history table). Surprise % = (actual − estimate)/|estimate| as published by each source; percentages are invariant to CMG's June‑2024 50:1 split. **Vendors disagree on recent quarters** (Zacks uses adjusted EPS; TradingKey appears to use GAAP vs a different consensus) — both shown, primary = Zacks where available.

| Quarter | EPS surprise | Rev surprise | Source (primary) |
|---|---|---|---|
| Q4 2023 | +6.47% | +0.98% | Zacks (via Globes) |
| Q1 2024 | +14.96% | +1.01% | Zacks |
| Q2 2024 | **n/a** (beat both, magnitude not retrievable) | n/a | Benzinga headline via Wedbush, Zacks blog 7/24/24 |
| Q3 2024 | +12.33% | −0.81% | TradingKey |
| Q4 2024 | −0.52% | −0.09% | TradingKey |
| Q1 2025 | +1.52% | −2.51% | TradingKey |
| Q2 2025 | −0.45% | −1.55% | TradingKey |
| Q3 2025 | +3.57% (TK alt +0.01%) | −0.48% (TK alt −0.71%) | Zacks / TradingKey |
| Q4 2025 | +4.65% (TK alt +5.16%) | +0.60% (TK alt +0.64%) | Zacks / TradingKey |
| Q1 2026 | −1.11% (TK alt −2.23%) | +0.41% (TK alt +0.63%) | Zacks / TradingKey |
| Q2 2026 | +3.13% (adj EPS $0.33 vs est $0.32; TK alt −1.02% on GAAP $0.32) | +0.81% (TK alt +0.52%) | Zacks ×3 sources / TradingKey |

**Aggregation (primary series, 10 quarters with quantitative data; computed in script):**
- **EPS beat rate: 7/10 (70%)**; including Q2 2024's known beat → **8/11 (72.7%)**
- **Revenue beat rate: 5/10 (50%)**; including Q2 2024 → **6/11 (54.5%)**
- **Mean EPS surprise: +4.46% | Median EPS surprise: +3.35%**; revenue mean −0.16%, median +0.16%
- *Sensitivity (pure TradingKey series, 8 quarters):* EPS mean +1.85%, median −0.22%, beat 4/8; revenue mean −0.48%, median −0.40%, beat 3/8. The two series disagree mainly on Q3'25–Q2'26 (adjusted-vs-GAAP EPS).

**Reproduce:** scripts `scripts/33342cdcf281.py` (cross-section, trend, CAGR, Rule of 40, AUV, multiples), `scripts/10f59436aefc.py` (balance-sheet decomposition), `scripts/8401b0d2fbbf.py` (EV/ROIC variants + surprise aggregation), `scripts/ee68194f0e90.py` (workspace inventory); data in `data/is_*.json`, `data/bs_cmg.json`, `data/bs_cava.json`, `data/statements_{cashflow-statement,key-metrics,metrics-ratios,balance-sheet-statement}.json`, `data/cmg_eod_full.json`.

**Caveats (complete list):** (1) `key-metrics-ttm`, `metrics-ratios(-ttm)`, `financial-scores` for all 8 symbols and FMP `earnings-company` were not retrievable — TTM figures are TTM-through-FY2025, and peer multiples/ROIC ranks/medians are unavailable; (2) balance sheets exist only for CMG and CAVA (ROIC computed for those two only); (3) peer cash flows not pulled (Rule of 40 computed for CMG only, as asked); (4) FMP's CMG `totalDebt` double-counts leases, inflating its published EV/EBITDA (corrected variants provided); (5) surprise history is web-sourced, not FMP, with vendor conflicts and one magnitude gap (Q2 2024); (6) 4,056 units is user-supplied; (7) several peers use 52/53-week December calendars (CAVA/WING/DPZ/TXRH), a minor comparability wrinkle in YoY growth.
