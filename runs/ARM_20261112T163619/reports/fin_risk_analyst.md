# Fin Risk Analyst

- Symbol: ARM
- Elapsed: 83.2s

---
# ARM Holdings plc (NASDAQ: ARM) — Financial Risk Assessment
*Data as of latest available: price 12-Nov-2026 ($202.34; profile $201.57), market cap ≈ $215.7bn, FY26 10-K (31-Mar-2026), latest balance sheet 30-Sep-2026. All figures USD.*

## 1. Credit Risk Assessment — **Investment Grade (in substance) / technically unrated**

ARM carries essentially **no funded debt**. Reported "total debt" of $500m (Sep-26) is consistent with lease liabilities (feed shows short-term debt $0 and long-term debt $0 in every period). Interest expense is **$0** in all reported periods; FY26 EBIT ($1,157m) actually *exceeds* operating income ($908m) by ~$249m, i.e. net interest income, not expense. There is no refinancing cliff, no maturity wall, and no covenant exposure. Net cash of roughly **$3.1bn** (cash + ST investments $3,621m less $500m leases), ~1.4% of market cap.

Conclusion: default/refinancing risk is negligible. The credit story is boringly safe; **all of ARM's financial risk sits in the equity/valuation layer, not the liability layer.**

## 2. Key Financial Risk Metrics

| Metric | Value | Period | Read |
|---|---|---|---|
| Debt / equity | 0.06x (0.055x on Sep-26 BS) | FY26 | Negligible |
| Net debt / EBITDA | **-2.24x** (net cash) | FY26 | Fortress |
| Interest coverage (EBIT/interest) | **N/M — interest expense = 0** | FY26 | No debt service burden (data gap: metric null; treat as unlimited) |
| Debt / assets | 0.04x | FY26 | — |
| Current ratio | 6.00x (6.35x Sep-26) | FY26 | Very strong |
| Quick ratio / cash ratio | 6.00x / 3.46x | FY26 | Inventory-free model; quality of current assets = receivables |
| Working capital | $5,196m | FY26 | — |
| Altman Z-Score | **4.04 — Safe zone** (X1 .49, X2 .42, X3 .11, X4 3.43, X5 .46) | FY26 | Note: X4 uses book equity; indicative only |
| Piotroski F-Score | **6 / 9 — Moderate** | FY26 | Fails: ROA improvement, gross-margin improvement, no-dilution |
| FCF yield | **0.45%** | FY26 | $979m FCF vs $216bn cap |
| FCF (TTM Sep-26) | $1,175m | TTM | CFO $1,734m – capex $559m |
| **FCF ex-SBC (TTM)** | **-$90m** | TTM | SBC $1,265m > 100% of FCF |
| SBC / revenue | 23.2% (FY26: 21.4%) | TTM/FY26 | Core red flag |
| Operating margin | 18.5% FY26; 17.0% TTM; 7.6% (Q1 FY27), 13.9% (Q3 FY27) | — | Compressing despite 27–31% growth |
| ROA | 8.4% FY26 (8.9% FY25) | — | Slight deterioration |
| Receivable days | ~156 (Sep-26) vs ~127 (FY24) | — | Working-capital drag (Q3 FY27 WC –$461m) |

**Revenue/earnings trajectory:** FY23 $2,679m → FY24 $3,233m → FY25 $4,007m → FY26 $4,920m (+23%), TTM $5,464m (+~31% H1 FY27 YoY). Growth is real, but opex (+22% in FY26; SG&A $866m and heavy SBC/engineering build-out) is absorbing gross profit: FY26 gross profit +$749m vs opex +$668m, and in H1 FY27 operating income was flat ($299m vs $270m) on +19% revenue.

## 3. Market Risk Profile — **High**

| Metric | Value |
|---|---|
| Annualised volatility (504d) | **73.8%** |
| Beta vs SPY (504d) | **3.32** (profile: 3.94) |
| Max drawdown (3-yr window) | **-62.1%** (close peak $439.46 on 18-Jun-26 → $166.72 on 5-Nov-26) |
| Sharpe (rf = 0%) | 0.744 |
| Sortino | **Not available** (data gap) |
| 52-wk range (observed) | $100.02 (5-Feb-26) – $452.70 (18-Jun-26) |
| Price now vs high / low | **-55% / +102%** |

Largest single-day moves observed: -13% on 5-Nov-26 (post-Q2 FY27 despite revenue/EPS beats), -8.1% on 29-Jul-26, -5.4% on 17-Dec-25. A beta of 3.3–3.9 implies a **-20% market drawdown translates into roughly -66% to -78% for ARM**. Risk here is valuation convexity: ~230x TTM P/E ($936m TTM NI) and 0.45% FCF yield mean the share price discounts a decade of royalty/own-silicon optionality, so modest guidance disappointment produces double-digit gap risk (already twice in four months).

## 4. Downside Scenario Analysis (20% revenue decline)

Base = TTM Sep-26: revenue $5,464m, gross margin 92.5% (annual-statement basis), opex ~$4,125m, EBIT $930m, EBITDA $1,298m, net income $936m.

| Scenario | Revenue | Gross profit | EBIT | EBITDA | Interest income | Net income | FCF ex-SBC |
|---|---|---|---|---|---|---|---|
| Base (TTM) | 5,464 | 5,055 | 930 | 1,298 | ~160 | 936 | -90 |
| -10% | 4,918 | 4,549 | 424 | 714 | ~160 | ~490 | ~-150 |
| **-20%** | **4,371** | **4,043** | **-82** | **+208** | **~160** | **~+65** | ~-250 |
| -35% (AI-capex bust) | 3,552 | 3,286 | -839 | -549 | ~160 | ~-570 | ~-400 |

Key findings:
- **Operating break-even lands at roughly a 18–19% revenue decline** (break-even revenue ≈ $4,460m = opex ÷ 92.5% GM). The cost base is nearly all fixed people cost — revenue leverage cuts both ways.
- At -20%, EBIT turns slightly negative but net income stays positive thanks to ~$160m of interest income on $3.6bn cash. **No solvency stress**: net cash/EBITDA stays deeply negative, Z-score remains comfortably above 2.99, and cash covers 6+ years of even the -35% cash burn.
- The binding constraint is **not liquidity but equity valuation**: a -20% revenue scenario collapses EPS toward zero and would likely compress the multiple simultaneously (a "double whammy" of -60%+ on the stock, consistent with the observed -62% drawdown).
- Further downside levers: opex is partially discretionary (non-GAAP opex guidance ~$780m/qtr ≈ $3.1bn/yr, i.e. ~$1bn below GAAP opex once SBC/amortisation are stripped), so management can defend margins by slowing the own-silicon investment — but that is the growth narrative itself.

## 5. Overall Financial Risk Rating: **MODERATE**
*(Credit/liquidity risk: **Low**. Market/valuation risk: **High**.)*

Balance-sheet integrity is best-in-class among large-cap semis: net cash $3.1bn, current ratio 6.3x, Z-score 4.04, zero interest expense, no maturities. The company cannot be described as financially fragile. What is fragile is the **price**: 74% vol, beta ~3.3, a 62% drawdown in five months, 0.45% FCF yield, and cash flow that is **negative once stock compensation is treated as a real cost**.

## 6. Key Red Flags

1. **Stock-based compensation = 23% of revenue ($1,265m TTM)**, exceeding free cash flow. FCF ex-SBC is **-$90m TTM** (-$73m FY26). Reported "FCF positive" is an SBC-adjusted illusion; dilution is real (weighted shares 1,026m FY23 → 1,069m, and the F-score's no-dilution test fails).
2. **Margin compression despite hyper-growth:** GAAP operating margin 18.5% FY26 → 7.6% (Q1 FY27) → 13.9% (Q3 FY27) as investment/SBC ramps. Gross margin also slipped (94.9% FY25 → 92.5% FY26).
3. **Customer concentration:** top five customers ≈ **57% of FY26 net revenue**, including **Arm China and SoftBank Group** (related party/controller). Qualcomm ≈9% of FY26 revenue and is in **active federal licensing litigation** — an adverse royalty reset is a direct revenue risk.
4. **Working capital deterioration:** DSO ~156 days; FY26 operating cash flow dragged -$602m by WC, Q3 FY27 -$461m. Cash conversion quality is weakening.
5. **Controlled company / overhang:** SoftBank (Kronos II LLC) control; short public history (IPO Sep-2023) means no through-cycle credit or trading record.
6. **Valuation as a risk factor:** ~230x TTM earnings, 0.45% FCF yield — the equity has no margin of safety and exhibits repeated double-digit gap risk on in-line results.
7. **Geopolitical exposure:** China revenue/export-control sensitivity (Arm China is both a top customer and a licensing-structure risk).

## 7. Data Gaps (flagged)
- **Credit rating / CDS:** not available in the data feed — the "Investment Grade" label is my analytical judgement based on the unlevered balance sheet, not a rating action.
- **Interest coverage:** tool returned null (interest expense = $0); coverage is effectively infinite, not "missing."
- **Sortino ratio:** not provided; only Sharpe (0.744).
- **R&D line item:** not disclosed separately in the feed (only "SG&A"); the opex decomposition relies on gross-profit-minus-operating-income.
- **Cost-of-revenue inconsistency:** quarterly COGS ($36–103m) does not reconcile to annual COGS ($370m FY26); gross-margin trend therefore taken from annual statements only.
- **Net debt definition conflict:** leverage tool shows -$3,144m vs balance-sheet field -$2,294m (the latter likely excludes short-term investments); I use the cash+ST-investments definition (~-$3.1bn).
- No quarterly cash-flow/BS data before FY26, so multi-year cash-conversion trends are limited to three annual points.
