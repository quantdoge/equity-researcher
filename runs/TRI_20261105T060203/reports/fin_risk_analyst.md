# Fin Risk Analyst

- Symbol: TRI
- Elapsed: 47.5s

---
# Financial Risk Assessment — Thomson Reuters Corporation (TRI)

**As of:** 2026-11-05 | Price $117.23 | Market cap $50.8bn | TTM through Q3-2026 (quarter ended 2026-09-30)

**Critical framing up front:** TRI presents a two-speed risk profile. Its *credit* is among the strongest in the market (A-, net leverage under 1x). Its *equity* has just repriced ~46% from its July-2025 peak ($218.42 → ~$117) on AI-disruption fears. The balance sheet is not the risk here — the terminal value of the franchise is. This distinction drives every rating below.

---

## 1. Credit Risk Assessment — **INVESTMENT GRADE (A-)**

| Evidence | Reading |
|---|---|
| Fitch IDR | **A-**, upgraded Sep-2025, Outlook Stable |
| S&P ICR | **A-**, upgraded from BBB+ |
| Debt structure | ~$1.9bn fixed-rate unsecured notes at the upgrade date; **no secured debt, no financial covenants of consequence, maturities laddered 2026–2043** |
| Net debt / EBITDA (TTM) | **0.77x** |
| EBIT / interest (TTM) | **11.7x** |
| EBITDA / interest (TTM) | 17.0x |

TRI has *investment-grade-grade* coverage and leverage with a fully unsecured, long-dated, fixed-rate stack. A 200bp rise in rates would not touch interest cost on existing notes. Two agencies upgraded the name *into* the equity collapse — the credit and the equity are telling different stories, and the credit is right.

**Caveat on the tool output:** `calculate_leverage_ratios` returned net debt/EBITDA 0.50x and interest coverage 10.87x — both on the **stale FY2025 (2025-12-31)** balance sheet, before the 2026 releveraging. I have restated to the Q3-2026 balance sheet. The FY2025 figure *understates* current leverage by ~0.27x.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Assessment |
|---|---|---|
| Total debt | $3,812m (Q3-26) vs $2,119m (FY25) | **+$1.69bn in 9 months** ⚠️ |
| Net debt | $2,418m (Q3-26) vs $1,608m (FY25) | +50% ⚠️ |
| Net debt / EBITDA (TTM) | 0.77x | Strong |
| Debt / equity | 34.0% | Strong |
| Debt / assets | 20.2% | Strong |
| EBIT / interest | 11.7x | Strong |
| Current ratio | 0.64x (FY25) → **1.08x (Q3-26)** | Improving |
| Quick ratio | 0.64x | Structurally low (deferred revenue) |
| Cash / short-term debt | **2.47x** ($1,394m / $565m) | Adequate |
| Working capital | –$1,233m (FY25) → **+$268m (Q3-26)** | Recovered |
| Altman Z (as reported) | 2.629 — **Grey zone** | **Misleading — see below** |
| Altman Z (market-cap x4) | **~5.4 — Safe zone** | Corrected reading |
| Piotroski F-Score | **7 / 9 — Moderate** | Solid |
| FCF yield (TTM) | **4.14%** ($2,102m / $50.8bn) | Moderate |
| FCF margin | 26.7% TTM vs 27.5% FY25 | Mildly deteriorating |
| Goodwill + intangibles / equity | **112%** | **Negative tangible book (~–$1.3bn)** ⚠️ |

**Z-score note:** the tool's 2.629 uses *book* equity (its own stated caveat). Substituting market cap ($50.8bn) for x4 lifts Z to ~5.4. TRI is not near distress on a solvency basis. I am overriding the tool's "Grey" label.

**Piotroski detail:** the two lost points are ROA improvement and positive equity change — the latter is *caused by buybacks* (equity fell $11,850m → $11,224m), not by losses. That is a governance/capital-allocation signal, not a deterioration signal.

---

## 3. Market Risk Profile — **the real problem area**

| Metric | Value | Interpretation |
|---|---|---|
| Annualised volatility (756d) | **39.7%** | Very high for a subscription-information business |
| Beta vs SPY | **0.33** | Low |
| Max drawdown (3y) | **–63.5%** | Severe |
| Sharpe ratio | **–0.20** | Negative; implies ~–8% annualised mean return over the window |
| Sortino | *Not available from tools* | **DATA GAP** |
| CDS spread | *Not available* | **DATA GAP** |

**The beta/vol divergence is the single most important market-risk finding.** A 0.33 beta alongside 39.7% volatility and a –63.5% drawdown means TRI's risk is overwhelmingly **idiosyncratic, not market-driven**. Practical consequences:

1. **Beta-based risk models and market-neutral hedging understate TRI's true risk** by a wide margin. A beta-hedge would have provided almost no protection through this drawdown.
2. **Diversification does not mitigate this exposure.** Position sizing must be driven by total volatility (39.7%), not beta-adjusted contribution.
3. **Driver identified:** the selloff is AI-disruption repricing of the legal-information franchise — specifically Anthropic's Claude Cowork legal plugins (contract review, NDA triage, compliance workflows) triggering a re-rating of legal data incumbents, compounded by Q3-2026 profit pressure from **higher AI spend in the Legal division** and a plan to cut up to 500 positions.
4. **Confirmed operating evidence:** Q3-2026 revenue grew only **+2.9% YoY** ($1,833m vs $1,782m) while operating income fell **–32%** ($402m vs $593m). Growth stalling *and* margins compressing simultaneously is the worst combination for a multiple.

---

## 4. Downside Scenario Analysis — Revenue –20%

Assumptions: TTM revenue $7,883m, EBIT $2,143m (27.2% margin), D&A $987m, ~45% of the $5,740m cost base variable (content/tech largely fixed), interest $184m, 25% tax, capex held at ~$700m.

| Line | Base (TTM) | –20% revenue | –30% revenue (stress) |
|---|---|---|---|
| Revenue | $7,883m | $6,306m | $5,518m |
| EBIT | $2,143m | **$1,083m** (–49%) | **$553m** (–74%) |
| EBIT margin | 27.2% | 17.2% | 10.0% |
| EBITDA | $3,130m | $2,070m | $1,540m |
| Interest coverage | 11.7x | **5.9x** | **3.0x** |
| Net debt / EBITDA | 0.77x | **1.17x** | **1.57x** |
| FCF (post-capex) | $2,102m | **~$960m** | **~$440m** |
| Dividend coverage ($1,086m) | 1.94x | **0.88x** | **0.41x** |

**Verdict: TRI survives a 20% revenue decline with credit intact** — leverage peaks at 1.17x and coverage holds at 5.9x, comfortably investment grade. Even at –30%, net leverage of 1.57x and 3.0x coverage remain IG-compatible.

**The binding constraint is the dividend, not solvency.** At –20% revenue the dividend is uncovered (0.88x) and at –30% it requires a cut. Mitigant: management can suspend the **$1,520m TTM buyback** immediately, which restores full dividend coverage at –20% and most of it at –30%. The realistic downside path is **dividend growth halted + buyback eliminated**, not a covenant breach or refinancing crisis.

**Refinancing risk is minimal:** $565m short-term debt against $1,394m cash (2.47x), notes laddered to 2043, and no near-term cliff.

---

## 5. Overall Financial Risk Rating: **MODERATE**

| Dimension | Rating |
|---|---|
| Credit / solvency risk | **LOW** (A-, 0.77x net leverage, 11.7x coverage) |
| Liquidity risk | **LOW** (2.47x cash/ST debt, positive FCF, laddered maturities) |
| FCF sustainability | **MODERATE** (26.7% margin, but flat FCF on rising revenue; returns exceed FCF) |
| Market / equity risk | **HIGH** (39.7% vol, –63.5% drawdown, negative Sharpe, idiosyncratic) |
| **Blended** | **MODERATE** |

**Bottom line:** this is a **solvency-safe, equity-fragile** name. The financial risk is not "will they default" (they will not) but "what is the franchise worth if AI compresses legal-information pricing." Investors are being paid a 4.14% FCF yield and a ~2.0% dividend yield to underwrite that question. Leverage is a non-issue; **multiple and terminal value are the entire debate.**

---

## 6. Key Red Flags

1. **⚠️ Aggressive releveraging into a collapsing share price.** Debt rose $2,119m → $3,812m in nine months while the equity fell ~46%. TTM shareholder returns of **$2,606m** (buybacks $1,520m + dividends $1,086m) equal **124% of TTM FCF** ($2,102m). The $504m shortfall was debt-funded. Buying back stock at $200+ with borrowed money ahead of an AI-driven repricing is a serious capital-allocation error and destroys management credibility on capital discipline.
2. **⚠️ Negative tangible book value.** Goodwill + intangibles of $12,555m are **112% of total equity**. Equity is entirely acquisition-accounting residue; tangible book is ~–$1.3bn. Any impairment cycle (Casetext, SafeSend, legal assets) hits book equity directly.
3. **⚠️ Growth/margin pincer.** Q3-2026: revenue +2.9%, operating income –32%. AI spend is hitting the P&L *before* any AI revenue arrives.
4. **⚠️ FCF stagnation despite revenue growth.** TTM FCF $2,102m vs FY2025 $2,052m on +5.4% revenue — conversion is slipping, and capex is climbing (8.4% of revenue).
5. **Structural negative working capital** (current ratio 0.64x in FY25) — benign for a prepaid subscription model but it removes a liquidity buffer in a downturn. Improved to 1.08x in Q3-26.
6. **Idiosyncratic risk is un-hedgeable via beta** — 0.33 beta materially understates a 39.7%-vol, –63.5%-drawdown stock.

## Data Gaps (explicit)

- **No valid peer benchmarking.** `get_sector_peers` returned mega-cap *industrials* (GE, CAT, RTX, BA, UNP) — GICS classifies TRI as "Specialty Business Services," so the peer set is not comparable. True comps (RELX, Wolters Kluwer, Verisk, FactSet, MSCI) were unavailable. **All ratio assessments above are absolute, not relative.**
- **Sortino ratio and CDS spreads unavailable** from the toolset.
- **Fitch report body blocked** (JavaScript-gated); rating, outlook, and maturity range sourced from search metadata, not the full document.
- **Quarterly cost classification is inconsistent** — Q3-2026 reports cost_of_revenue $1,431m with SG&A of $0, while Q3-2025 splits $430m/$674m. Gross-margin trend analysis is therefore unreliable at quarterly granularity; I used operating income instead.
- **Altman Z reported by tool is not the market-cap version** and was manually corrected (2.63 → ~5.4).
- **Balance-sheet-derived metrics in `calculate_leverage_ratios` are stale (FY2025)** and were restated to Q3-2026 by hand.
