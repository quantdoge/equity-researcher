# Fin Risk Analyst

- Symbol: ARM
- Elapsed: 61.9s

---
## ARM Holdings plc (ARM) — Financial Risk Assessment

**Company:** Arm Holdings plc ADS · Technology / Semiconductors · UK-domiciled, USD reporting · Market cap **$195.1B** · Price $183.39 · FY ends 31 March (latest annual = FY2026)

⚠️ **Nature of the risk:** ARM is a pure IP licensor with **no meaningful debt and ~$3.1–3.6B net cash**. The financial risk here is **not solvency — it is equity valuation and market risk**, plus a cash-conversion problem driven by enormous stock-based compensation.

---

## 1. Credit Risk Assessment

**Rating: Investment Grade (balance-sheet equivalent)** — *not formally rated in the available data (data gap).*

| Metric | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Total debt | $226M | $356M | $457M |
| Cash & ST inv. | $2,923M | $2,825M | $3,601M |
| Net cash | $1,697M | $1,729M | **~$3,144M** |
| Debt/equity | — | — | **0.06** |
| Net debt/EBITDA | — | — | **-2.24x** |
| Interest expense | $0 | $0 | **$0** |

- **Interest coverage: N/A — effectively infinite.** Interest expense is $0 in all three years; the $457M of "total debt" carries **zero short-term debt and zero long-term debt** on the balance sheet, i.e. it is almost entirely lease liabilities. **No refinancing cliff, no maturity wall, no covenant exposure.**
- **Altman Z-Score: 4.04 (Safe zone)** — comfortably above the 2.99 threshold. Note the tool's caveat: x4 uses *book* equity, so ARM's version is **understated** relative to a market-cap-based reading.
- **Piotroski F-Score: 6/9 (Moderate).** Passes positive ROA, positive operating cash flow, accrual quality, lower leverage, positive equity change, asset-turnover improvement. **Fails three:**
  - F3 ROA improvement = 0
  - F7 no-dilution = 0 (**share count rose 1,050M → 1,061M**, SBC-driven)
  - F8 gross-margin improvement = 0 (**92.8% → 94.9% → 92.5%**, GM peaked in FY25)

**Verdict:** Balance-sheet credit risk is **negligible**. ARM could survive a multi-year downturn without touching external capital. The F-score deductions are all *quality-of-earnings* signals, not solvency signals.

---

## 2. Key Financial Risk Metrics

| Risk Dimension | Metric | Value | Read |
|---|---|---|---|
| Leverage | Debt/equity | 0.06 | Negligible |
| Leverage | Net debt/EBITDA | -2.24x | Net cash |
| Leverage | Debt/assets | 0.04 | Negligible |
| Coverage | EBIT/interest | N/A (no interest) | Infinite |
| Liquidity | Current ratio | **6.00** | Exceptional |
| Liquidity | Quick ratio | 6.00 | Exceptional (no inventory) |
| Liquidity | Cash ratio | 3.46 | Exceptional |
| Liquidity | Working capital | $5,196M | Strong |
| Solvency | Equity/assets | 0.77 | Strong |
| Bankruptcy | Altman Z | **4.04** | Safe |
| Strength | Piotroski F | **6/9** | Moderate |
| Cash gen. | FCF (FY26) | $979M | Positive |
| Cash gen. | **FCF yield** | **0.50%** | **Very thin** |
| Cash gen. | FCF / net income | 1.08x | Adequate on face |
| Profitability | Operating margin | 18.5% (FY26) vs 20.6% (FY25) | **Compressing** |
| Valuation | P/E, EV/EBITDA, P/S | ~216x, ~137x, ~40x | Extreme |

**Working-capital note:** receivables grew $1,898M → $2,466M (+30%) on +23% revenue — receivables outrunning revenue slightly. FY25 saw a **-$1,465M** working-capital drain that crushed OCF to $397M.

---

## 3. Market Risk Profile

| Metric | Value | Interpretation |
|---|---|---|
| Annualised volatility (504d) | **74.2%** | ~3x a typical large-cap |
| Beta vs SPY (calculated, 504d) | **3.33** | Extreme market sensitivity |
| Beta (profile field) | **3.94** | Confirms extreme |
| Max drawdown (504d) | **-62.1%** | Severe |
| Sharpe ratio | 0.71 | Weak for the risk taken |
| Sortino ratio | **Not available** | ⚠️ Data gap |

**The beta is the single most important number in this report.** At beta ~3.3–3.9, a garden-variety **-20% market drawdown implies a ~-66% to -78% ARM drawdown**. The -62% realised max drawdown is consistent with that math — this has already happened once. ARM offers essentially **no defensive characteristics**; it is a high-multiple, high-duration asset that reprices violently with discount rates and AI sentiment.

**Rate sensitivity context:** the 10Y Treasury sits at **5.13%** (curve as of 2026-11-18, 2s10s +39bp, not inverted). A 216x P/E asset is acutely exposed to any further rise in long yields — every 50bp of higher discount rate is a material hit to a 40x-sales multiple.

---

## 4. Downside Scenario Analysis — Revenue -20%

**Base (FY2026):** Revenue $4,920M · Gross margin 92.5% · Opex (implied) $3,642M · Operating income $908M · Net income $904M · FCF $979M

| | Base | -20% rev, **opex flat** | -20% rev, **opex -10%** | -35% rev (deep semis downturn) |
|---|---|---|---|---|
| Revenue | 4,920 | 3,936 | 3,936 | 3,198 |
| Gross profit (92.5%) | 4,550 | 3,641 | 3,641 | 2,959 |
| Opex | 3,642 | 3,642 | 3,278 | 3,642 |
| **Operating income** | **908** | **~0** | **364** | **-683** |
| Interest income (est. 4% on cash) | +144 | +144 | +144 | +144 |
| Pretax | ~1,052 | ~144 | ~508 | -539 |
| **Net income** | **904** | **~124 (-86%)** | **~437 (-52%)** | **~-464** |
| Op margin | 18.5% | 0.0% | 9.2% | -21.4% |
| FCF (as reported) | 979 | ~456 | ~820 | ~-400 |
| **FCF ex-SBC** | **-73** | **~-596** | **~-232** | **~-1,450** |

**Why the revenue hit goes straight to operating income:** gross margin is high but **cost of revenue is only ~7.5% of sales**, so the vast majority of the P&L is fixed R&D/SG&A that cannot flex with revenue. Operating leverage therefore works **hard in reverse**.

**Critical finding — ARM is already at zero operating leverage today.** The company's own trajectory proves the model:
- FY26: revenue **+22.8%**, operating income only **+9.8%** → margin 20.6% → 18.5%
- H1 FY27 (Jun-26 + Sep-26 quarters): revenue **$2,732M**, operating income **$299M = 10.9% margin**
- Q1 FY27 alone: operating income **$98M on $1,289M revenue = 7.6% margin**

So the "-20% revenue, opex flat" column is **not a stress case — it is roughly where the margin structure is already trending.** That is the core risk finding.

**Solvency under stress: never in question.** With ~$3.1B net cash, even the -35% scenario's ~$464M annual loss is absorbed for **6–7 years** with no external funding. **No liquidity risk.**

**The real damage is to the equity:** at ~40x sales, a -35% revenue shock with negative margins could plausibly compress the multiple toward 10x sales → market cap ~$32B, or **~-84%**. That is the downside that matters.

---

## 5. Overall Financial Risk Rating: **MODERATE**

**This is a bifurcated rating and should be read that way:**

| Sub-dimension | Rating | Driver |
|---|---|---|
| Credit / solvency risk | **LOW** | Net cash $3.1B, D/E 0.06, coverage infinite, Z 4.04 |
| Liquidity risk | **LOW** | Current ratio 6.0, cash ratio 3.46, no maturities, cash-flow positive |
| Cash-generation quality | **HIGH** | FCF yield 0.5%, FCF **ex-SBC negative**, SBC $1,052M > net income $904M |
| Market / valuation risk | **HIGH** | 74% vol, beta 3.3–3.9, -62% max DD, 216x P/E |
| **Composite** | **MODERATE** | Pristine balance sheet does not offset extreme equity risk |

---

## 6. Key Red Flags

1. **FCF is an accounting artefact of SBC.** FY26: operating cash flow $1,524M includes a **$1,052M stock-compensation add-back** that is larger than net income ($904M). **FCF net of SBC is -$73M — negative.** SBC is 21% of revenue and rising (FY25: $820M). Share count is being diluted ~1%/yr. For a company trading at 216x earnings, "cash-generative" is not yet true on a fully-loaded basis.
2. **Negative operating leverage has already arrived.** Operating margin 20.6% → 18.5% (FY26) → **10.9% (H1 FY27)** on *growing* revenue. Gross margin also slipped 94.9% → 92.5%. Revenue is growing but profit is not scaling — the F-score flags this (F3, F8 = 0).
3. **FCF yield of 0.50% vs. peer set:** NVDA **2.54%**, AVGO **1.62%**, AMD **0.82%**. ARM is the most expensive cash flow in its peer group by a wide margin — the thinnest cushion if growth decelerates.
4. **Extreme customer concentration: top-5 = ~57% of revenue** (FY26, incl. Arm China and SoftBank Group). **Arm China is roughly 16–20% of revenue** with historically opaque reporting and JV governance risk. A single licensing dispute or export-control change is a material revenue event.
5. **Governance/related-party overhang:** SoftBank Group is both controlling shareholder and a top-5 customer — a structural conflict (per FY26 20-F).
6. **Beta 3.3–3.9 with 74% volatility and a realised -62% drawdown.** Position sizing, not fundamental analysis, is the binding constraint on this name.
7. **No debt maturity risk, no covenants, no dividends/buybacks** — the company returns nothing and repurchases no stock.

---

### Data Gaps Flagged
- **No formal credit rating / CDS spread** available in the toolset.
- **Sortino ratio** not returned by the volatility tool (Sharpe 0.71 only).
- **Net debt discrepancy:** leverage tool reports **-$3,144M**, balance sheet field reports **-$2,294M**. I used the ~$3.1B figure for solvency math; the direction (large net cash) is unambiguous either way.
- **Interest coverage is undefined**, not missing — interest expense is $0.
- Peer **credit metrics** only obtained for AVGO (D/E 0.8, net debt/EBITDA 1.41x, coverage 7.94x) — ARM's balance sheet is materially stronger. Broad peer comparison not completed within budget.
