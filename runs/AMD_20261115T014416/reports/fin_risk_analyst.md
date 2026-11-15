# Fin Risk Analyst

- Symbol: AMD
- Elapsed: 57.6s

---
I have enough to write a complete assessment. Note: the ratio tools are computed on **FY2025 annual** data, which is now three quarters stale — the Q3 FY2026 balance sheet shows a material change, so I use the latest quarter for the risk read.

---

# AMD — Financial Risk Assessment

**Price $534.06 · Market cap $875.9B · Semiconductors · FY2026 Q3 (ended 2026-09-26) latest**

## 1. Credit Risk Assessment

**Rating: INVESTMENT GRADE (AAA-equivalent balance sheet). Solvency risk is not a live concern.**

- Total debt $8.92B vs. cash & ST investments **$15.78B**. Net debt **+$1.51B** — net *cash* position deteriorated but leverage remains trivial.
- Net debt / TTM EBITDA ≈ **0.13x** (EBITDA TTM $11.1B). Debt/assets 9.4%; debt/equity 0.13.
- Interest coverage ≈ **47x** on TTM operating income of $8.05B vs. $0.17B interest expense. (FY25 tool reading: 28.2x.)
- Altman Z-Score **3.74 — "Safe" zone**, and this is *conservative*: x4 uses book equity ($63.0B). Using the $876B market cap, x4 would be ~14x, pushing Z far higher.
- Moody's senior unsecured **A1** (upgraded from A2 per Moody's ratings news) — consistent with a net-cash balance sheet, though I could not independently verify via the ratings portal.
- Piotroski F-Score **8/9 (Strong)**. The single failure is **F5 (leverage not reduced)** — and on the latest quarter it would still fail, since debt *rose* $4.6B QoQ.

**Verdict: the company can comfortably survive a multi-year downturn. Credit is a non-issue.**

## 2. Key Financial Risk Metrics

| Metric | Value | Read |
|---|---|---|
| Net debt / EBITDA | 0.13x (Q3'26) | Very low |
| Debt / equity | 0.13 | Very low |
| Interest coverage | ~47x TTM | Exceptional |
| Current ratio | 2.72 | Strong |
| Quick ratio | 1.93 | Strong |
| Cash ratio | 1.09 | Strong |
| Working capital | $25.0B | Ample |
| Altman Z | 3.74 | Safe |
| Piotroski F | 8/9 | Strong |
| Goodwill + intangibles | **$40.57B** | 59% of equity |
| FCF yield (TTM) | **~0.81%** | Extremely thin |
| P/E (TTM EPS $4.60) | **~116x** | Extreme |
| P/Tangible book ($17.0/sh) | **~31x** | Extreme |

## 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility | **65.5%** |
| Beta vs SPY | **2.44** (profile: 2.49) |
| Max drawdown (3y) | **−54.7%** |
| Sharpe (approx., 0% rf) | 1.20 |
| Sharpe, risk-free adjusted (rf 4.74%) | **~1.13** |
| Sortino | *Not available — data gap* |

- A 20% S&P drawdown implies roughly **−49% for AMD** at beta 2.44, before any idiosyncratic shock.
- Realised 65.5% vol against ~116x earnings means the volatility is *structural*, not transient.
- Macro: 10Y at 5.13%, 2Y at 4.74%, curve +39bp (normal). Elevated discount rates are a direct headwind to a long-duration, high-multiple equity.

## 4. Downside Scenario Analysis (base: TTM revenue $45.4B, GM 53.7%, opex $16.4B)

| Scenario | Revenue | Gross margin | EBIT | EBITDA | Net debt/EBITDA | Interest cov. | FCF | Equity value risk |
|---|---|---|---|---|---|---|---|---|
| Base | $45.4B | 53.7% | $8.05B | $11.1B | 0.13x | ~47x | $7.1B | — |
| **−20%** | $36.4B | 47% | ~$2.7B | ~$5.7B | 0.26x | ~11x | ~$3.5B | Stock −45% to −65% |
| **−35%** | $29.5B | 40% | ~−$2.2B | ~$0.9B | 1.7x | negligible | ~−$0.5B | Stock −70% to −85% |

**Critical distinction:** in the −20% case AMD remains solidly investment grade, cash-rich, and FCF-positive. The *credit* absorbs the shock cleanly. The *equity* does not — at 116x trailing earnings, a −20% revenue decline with even moderate multiple compression (to 35–45x) implies a share price of roughly $50–$115 versus $534 today. **The downside is almost entirely a valuation-multiple event, not a balance-sheet event.**

At −35%, cash of $15.8B against a ~$0.5B annual burn gives effectively unlimited runway; debt is repaid from the balance sheet, not refinanced.

## 5. Overall Financial Risk Rating

**MODERATE**

Credit risk is **Low**; liquidity risk is **Low**; market/valuation risk is **Critical**. The composite is Moderate only because the solvency pillars are so strong — but investors should understand that the risk here is *not* whether AMD survives, it is what the market is paying for that survival.

## 6. Key Red Flags

1. **Free cash flow is deteriorating fast while revenue accelerates.** Quarterly FCF margin: Q1'26 **25.0%** → Q2 **13.5%** → Q3 **4.1%**. Q3 net income was $2.43B but FCF only $554M. Earnings are not converting to cash.
2. **Working capital explosion.** Q3 alone consumed **−$3.36B** of operating cash flow. Inventory +35% QoQ ($8.47B → $11.46B); DIO up from ~165 to ~199 days. Receivables +26% QoQ. This is the classic late-cycle semiconductor build — it precedes either a demand pull-forward or a writedown. **Single biggest fundamental warning.**
3. **Debt more than doubled in one quarter** ($4.28B → $8.92B) with total liabilities up $9.2B QoQ. Why a net-cash, A1-rated company raises $4.6B abruptly is unexplained in the data — a question for management.
4. **Goodwill $40.6B = 59% of equity, 43% of assets.** A sustained 20–35% revenue decline puts impairment risk on the table. Non-cash, but it would hit book equity — and the Piotroski/A2 leverage reads.
5. **Valuation is the dominant risk:** 116x TTM P/E, 0.81% FCF yield, 31x tangible book, beta 2.44, 3-year max drawdown of −54.7%.
6. **Stock-based comp $2.01B TTM (~4.4% of revenue, ~28% of FCF)** — dilution is real, partly offset by buybacks.

## Data Gaps (explicit)

- **The ratio toolkit (leverage, liquidity, Altman, Piotroski, FCF yield) is computed on FY2025 annual data, ended 2025-12-27 — three quarters stale.** All current-period figures above are my own calculations from Q3 FY2026 statements. The tools' FY25 net-debt figure (−$6.08B) also conflicts with the FY25 balance sheet (−$1.07B), likely differing treatment of long-term investments.
- Quarterly `ebit`/`ebitda` fields are internally **inconsistent** with operating income + D&A (e.g., Q3'26 EBITDA $2.71B *below* operating income $2.83B). I used operating income + D&A instead.
- **No CDS spread, no debt maturity schedule beyond current/non-current split** (ST debt $0 at Q3'26 — no near-term cliff), no covenant detail, no revolving-facility size.
- **Sortino ratio unavailable.**
- **Peer multiples not retrieved** — only market caps (NVDA $3.92T, AVGO $1.66T, TSM $2.07T). No relative valuation work done.
- No segment-level disclosure, which would be needed to separate the AI/data-center ramp from the cyclical client and gaming businesses.
