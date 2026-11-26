# Fin Risk Analyst

- Symbol: ASTS
- Elapsed: 84.1s

---
I have enough to assess. Two data caveats up front: the volatility tool is unavailable on this plan (I reconstructed market risk manually), and the price feed ends 2026-06-30 while the company is now reporting Q3 2026 — so I've bridged the gap with the 52-week range and Q3 filings.

---

# AST SpaceMobile, Inc. (ASTS) — Financial Risk Assessment
**As of:** Q3 2026 (period ended 2026-09-30, filed 2026-11-09) | **Price:** ~$26 | **Market cap:** ~$9.2–10.7B | **Shares out:** ~300.7M

**Business context:** Pre-profit satellite-direct-to-cell operator. TTM revenue $142.9M against $6.77B of total assets. This is a capital-project company, not an operating-ratio company — so I weight liquidity, funding access and maturity structure more heavily than margin analysis. The standard ratio toolkit is partly structurally biased here, and I flag where that matters.

---

## 1. Credit Risk Assessment

### Rating: **Sub-Investment Grade (CCC-equivalent profile)** — liquidity-masked, trajectory deteriorating

The company is **not** in near-term payment distress — it holds $2.80B of cash and short-term investments against only $8.8M of short-term debt. But the *credit* is impaired: EBITDA is negative (−$655M TTM), interest coverage is negative, and the debt load has nearly doubled in a year. The balance sheet is propped up by repeated capital raises, not by cash generation. That is a CCC-style structure: ample liquidity today, wholly dependent on capital-market access to remain solvent past 2027.

**Critical structural point:** at ~$26/share, the entire $4.1B convertible stack is deep out of the money (conversion prices ~$79.57 and ~$149.20). Converts that don't convert must be repaid in **cash**. So the maturity schedule is not a soft, equity-settled event — it is a hard cash obligation of ~$4.1B layered into 2031–2036.

---

## 2. Key Financial Risk Metrics

| Metric | Q3 2026 | FY2025 | FY2024 | Read |
|---|---|---|---|---|
| Total debt | $4,118.7M | $2,239.5M | $173.0M | **+84% YoY**; 23.8× in 2 yrs |
| Net debt | **+$1,320.0M** | −$97.1M | −$392.0M | Flipped from net cash to net debt |
| Debt / equity (book) | **1.90** | 0.94 | 0.26 | Doubling; rising fast |
| Debt / assets | **0.61** | 0.45 | 0.18 | — |
| Net debt / EBITDA | **n.m.** (EBITDA −$655M) | 0.26 | n.m. | Ratio meaningless — negative EBITDA |
| Interest coverage (EBIT/int.) | **−8.8×** | −7.98× | −13.0× | **Cannot service from operations** |
| Interest expense (TTM) | **$83.3M** | $36.1M | $18.7M | Q4'25 $2.7M → Q3'26 $30.3M (~11× in 4 qtrs) |
| Current ratio | **13.65** | 16.35 | 7.9 | Exceptional |
| Quick ratio | **13.30** | 16.27 | — | Exceptional |
| Cash ratio | **12.42** | 15.54 | — | Exceptional |
| Working capital | $2,851.3M | $2,308.2M | $524.3M | — |
| **Altman Z-Score** | **0.16** (computed) | 0.605 | — | **Distress zone** (<1.81) |
| **Piotroski F-Score** | n/a | **5 / 9** | — | Moderate |
| Equity / assets | 0.32 | 0.48 | 0.70 | Eroding |
| FCF (TTM) | **−$1,799.4M** | −$1,136.3M | −$300.3M | Burn up 6× in 2 yrs |
| FCF yield | **≈ −16.9%** | −10.7% | — | Deeply negative |

**Z-Score recomputed for Q3 2026** (tool only covers FY2025): X1 0.421, X2 −0.205, X3 −0.109, X4 0.469, X5 0.021 → **Z = 0.16**. Every component except working capital is negative. Note the Z-score is structurally harsh on a company that intentionally runs negative EBIT while building a constellation — but the direction (0.605 → 0.16) is a genuine deterioration signal, not just model bias.

**F-Score detail (FY2025, 5/9):** Positive ROA ✗ | Positive operating CF ✗ | ROA improvement ✓ | Accruals quality ✓ | Lower leverage ✗ | Positive equity change ✓ | No dilution ✗ | Gross margin improvement ✓ | Asset turnover improvement ✓. The two failures that matter most — **no positive operating cash flow** and **ongoing dilution** — are both still failing in 2026.

**Gross margin trend (the one clear positive):** Q1'26 24.9% → Q2'26 25.2% → Q3'26 40.2%. Sequentially improving as revenue scales against a fixed cost base.

---

## 3. Market Risk Profile

*The `calculate_price_volatility` tool is unavailable on this subscription (FMP endpoint restriction). Figures below are computed manually from 209 trading days of OHLC data (2025-09-02 → 2026-06-30), plus the reported 52-week range.*

| Metric | Value |
|---|---|
| **Annualised volatility** | **~70–75%** (est., manual) |
| **Beta** | **2.85** (reported) |
| **Max drawdown (52-wk)** | **−83.2%** ($133.86 → $22.50) |
| Max drawdown (in-window) | −50.7% (May 28 → Jun 25, 2026) |
| Sharpe (Sep'25–Jun'26 window) | ~+1.4 (annualised, 0% rf) |
| Sharpe incl. Jul–Nov'26 collapse | **materially negative** |

**Interpretation.** Beta of 2.85 means a 20% market drawdown implies roughly a **−57%** move in ASTS — and the realized record is worse than that implies. The stock round-tripped from $133.86 to $22.50 in six months. The "positive Sharpe" in my price window is a momentum artifact: it measures the run *up* and excludes the collapse that followed, because the feed stops at 2026-06-30. On a trailing basis through today the risk-adjusted return is deeply negative.

This is the single most important market-risk fact for the credit: **the equity has lost 83% of its value, and equity issuance is this company's primary funding mechanism.** The asset that backs the funding model has been repriced downward by more than 80%. Volatility at 70%+ is not a trading statistic here — it is a *refinancing* statistic.

---

## 4. Downside Scenario Analysis

### Scenario A: Revenue −20% (the standard test)
TTM revenue $142.9M → $114.3M. At ~40% gross margin, gross profit falls ~$11.4M. **Impact on FCF: roughly −$11M against a −$1,799M base — i.e., under 1%.**

**Conclusion: a 20% revenue shock is essentially immaterial to solvency.** Revenue is too small relative to the cost base to be the binding constraint. Anyone stress-testing this company on revenue is testing the wrong variable.

### Scenario B: The scenario that actually matters — capital-market closure
If the equity stays at ~$26 or falls further and new equity/convert issuance becomes unavailable:
- Cash $2,798.9M ÷ Q3'26 annualised burn ($1,856M) = **~1.5 years**
- Cash ÷ TTM burn ($1,799M) = **~1.6 years**
- Debt/equity at **market** (~$9.2B equity) = 0.45 — but book equity is only $2.16B, so **book** leverage is 1.90 and rising
- Result: **solvency pressure becomes acute in roughly 2028**, well before the 2031+ convertible maturities — the gap is funded only by continued issuance.

### Scenario C: Convert stack does not convert
$4.1B of notes at $26 vs conversion prices of $79.57 / $149.20. Deep out of the money. If the stock does not recover ~3× from here, the entire stack must be **cash-settled**. That is a ~$4.1B obligation against a business generating negative EBITDA — a genuine refinancing cliff, just a long-dated one.

### Liquidity buffer (the offset)
No maturities before 2031. Short-term debt $8.8M. Working capital $2.85B. **There is no 2026–2027 wall.** The company has bought time — roughly 18–24 months — and is using it to build the constellation. That is a legitimate, deliberately-chosen risk profile, not a hidden one.

---

## 5. Overall Financial Risk Rating: **HIGH**

*(Not Critical — the $2.8B cash pile and absence of near-term maturities rule that out. But firmly High, and trending toward Critical if capital access stays impaired.)*

**Why High and not Moderate:** the company fails on every earnings-based credit metric (negative EBITDA, negative coverage, Z-score 0.16, F-score 5 with no positive operating cash flow). It passes only on liquidity — and that liquidity is a *stock*, not a *flow*. It is being consumed at ~$1.8B/year and must be replenished from the capital markets.

**Why not Critical:** the maturity ladder is genuinely long-dated (2031+), the cash position is real and large, and gross margins are improving sequentially. The company is not facing a 2026 or 2027 payment default under any plausible scenario.

---

## 6. Key Red Flags

1. **Funding model is circular and now impaired.** Solvency depends on equity/convert issuance; the equity is down 83% from its peak. The cheaper the stock gets, the more dilutive each raise — and the more likely the next raise is debt-funded, which worsens leverage.
2. **Interest expense up ~11× in four quarters** ($2.7M → $30.3M). Annualising Q3 gives ~$121M/yr. Coverage is −8.8× and will not turn positive until EBITDA does.
3. **Net debt flipped from −$97M to +$1.32B in nine months.** Debt up 84% YoY to $4.12B. Leverage is being added at the worst point in the cycle.
4. **Altman Z-Score 0.16, deep in the distress zone** and down from 0.605 — deterioration in every component except working capital.
5. **$4.1B convert stack is deep out of the money** at $26 vs ~$79.57/~$149.20 conversion prices. Converts that don't convert become cash repayments — a 2031–2036 cliff.
6. **Continued dilution.** 10M Class A shares issued to Firefly for a rocket engine license; share issuances used to repurchase 2032 2.375% converts. Share count 256M (2025 avg) → 300M (Q3'26) → ~300.7M now. F-score "no dilution" test fails.
7. **Revenue immateriality.** $142.9M TTM revenue vs $6.77B assets and $4.12B debt. The P&L provides no meaningful debt-service capacity whatsoever.
8. **Asset quality.** $2.38B PP&E (satellites) and $322M goodwill/intangibles — hard to liquidate and, for satellites, subject to launch failure and obsolescence risk. Book equity of $2.16B is not a reliable recovery cushion.

---

## 7. Data Gaps (explicit)

- **`calculate_price_volatility` failed** — FMP endpoint not in subscription. Vol/beta/drawdown/Sharpe computed manually from raw OHLC; volatility (~70–75%) is an estimate, not a model output.
- **Price feed ends 2026-06-30**, but the company now reports Q3 2026. The −83% drawdown ($133.86 → $22.50) is taken from the reported 52-week range, **not** from the feed. Jul–Nov 2026 daily returns are unavailable, so realized vol is likely *understated*.
- **No 3-year drawdown computable** from available data.
- **Market cap inconsistency:** `calculate_fcf_yield` used ~$6.67B; current market cap is ~$9.2–10.7B per multiple sources. I report FCF yield on the current cap (≈ −16.9%) and flag the tool's figure as stale.
- **Convertible maturity conflict:** the $1.0B 1.625% notes (issued July 2026) are described as maturing **2031** in one source and **2034** in another. Not resolved. Also a 2.25% convert due 2036 (Feb 2026) and a 2032 2.375% convert being repurchased.
- **No credit rating or CDS spread available** — the "Sub-Investment Grade" designation is my own mapping from the ratio profile, not an agency rating.
- **Statement inconsistencies:** cash-flow-statement net income differs from income-statement net income (e.g., Q3'26 −$171.8M vs −$132.4M); FY2025 cost of revenue implies negative COGS in some quarters (Q4'25 gross margin −68% vs FY 53.4%). Treat margin trend data with caution.
- **Peer comparison not attempted** — no viable set of listed direct-to-cell satellite operators at scale; `get_sector_peers` would return terrestrial telecoms with non-comparable economics.

---

### Bottom line
ASTS is a **well-capitalised but fundamentally unprofitable** capital project whose credit profile rests entirely on continued access to capital markets — access that has just been sharply repriced by an 83% equity drawdown. The 18–24 month liquidity cushion is real and the maturity ladder is genuinely long, so this is not a near-term default story. But the trajectory is wrong on every flow metric: burn up 6× in two years, interest cost up 11× in four quarters, leverage doubling, and dilution accelerating. **Revenue downside is not the risk; funding-market downside is.** Monitor cash balance, quarterly FCF, and convertible conversion prices as the three tripwires.
