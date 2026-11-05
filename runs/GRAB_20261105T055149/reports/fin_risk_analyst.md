# Fin Risk Analyst

- Symbol: GRAB
- Elapsed: 41.2s

---
# GRAB — Financial Risk Assessment
**Grab Holdings Limited** | Technology / Software-Application | Singapore | Market cap ≈ $13.35bn | Price $3.36 | Latest data: Q3'26 (filed 2026-11-03)

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE (BB) — but with an unusually fortress-like balance sheet for the rating band.**

S&P upgraded Grab to **'BB'** on improving credit metrics (source: S&P Global Ratings, *"Grab Holdings Ltd. Upgraded To 'BB' On Improving..."*), placing it two notches below investment grade at the top of the BB bucket. Bloomberg also reports Grab **prepaid $600M of debt ahead of a 2026 maturity** using excess cash — an explicit signal of voluntary deleveraging, not distress-driven refinancing.

The balance sheet does not look like a BB credit. Gross debt is only **$2.07bn** against **$5.66bn** of cash and short-term investments — a **net cash position of roughly $3.6bn** (≈27% of market cap). Debt/assets is **0.17** and debt/equity **0.30**. The rating is capped by earnings volatility, not leverage.

⚠️ **Vendor data conflict (flagged):** the leverage tool reports net debt of **−$4.75bn** (YE25, cash $6.80bn less debt $2.05bn), while the balance sheet `net_debt` field shows **−$1.38bn** (YE25) and **−$0.78bn** (Q3'26). The two definitions differ by ~$2.8bn (likely restricted cash / deposits / investment netting). I use the conservative gross-cash-minus-gross-debt convention throughout and disclose both.

⚠️ **Coverage definition conflict (flagged):** the tool's interest coverage of **3.13x** divides *operating income* ($222M) by interest ($71M); the income statement's *EBIT* line is $340M, implying **4.8x**. Both are shown below.

---

## 2. Key Financial Risk Metrics

| Metric | YE2023 | YE2024 | YE2025 | TTM (Q4'25–Q3'26) |
|---|---|---|---|---|
| Revenue ($M) | 2,359 | 2,797 | 3,370 | **3,970** |
| EBITDA ($M) | (222) | 93 | 517 | **828** |
| EBITDA margin | neg | 3.3% | 15.3% | **20.9%** |
| EBIT ($M) | (367) | (54) | 340 | **604** |
| Net income ($M) | (434) | (105) | 268 | **586** |
| Interest expense ($M) | 99 | 41 | 71 | **116** |
| **Interest coverage (EBIT)** | neg | neg | **4.8x** | **5.2x** |
| Interest coverage (op. income basis) | neg | neg | **3.1x** | — |
| Total debt ($M) | 793 | 364 | 2,053 | **2,070** |
| Cash & ST inv. ($M) | 5,043 | 5,629 | 6,804 | **5,658** |
| **Net cash ($M)** | 2,345 | 2,600 | **4,751** | **3,588** |
| Debt/equity | 0.12 | 0.06 | **0.30** | **0.29** |
| Debt/assets | 0.09 | 0.04 | **0.17** | **0.15** |
| Current ratio | 3.90 | 2.53 | **1.75** | **1.38** |
| Quick ratio | — | — | **1.73** | **1.37** |
| Cash ratio | — | — | **1.47** | **0.99** |
| Working capital ($M) | — | — | 3,453 | **2,206** |
| **Altman Z-Score** | — | — | **−0.545 (Distress)** | — |
| **Piotroski F-Score** | — | — | **5 / 9 (Moderate)** | — |
| FCF ($M) | 15 | 775 | 134 | **156** |
| FCF yield | — | — | **0.95%** | **~1.17%** |

**Altman Z-Score decomposition (YE25):** x1 0.288, **x2 −1.458**, x3 0.028, x4 1.293 (book equity), x5 0.281 → **−0.545**.

**This score is a structural artifact, not a bankruptcy signal.** x2 (retained earnings / total assets) is −1.458 because Grab carries **−$17.5bn of accumulated losses** from its 2021–2023 cash-burn era. Sensitising x4 to *market* value (mkt cap $13.35bn / liabilities $5.23bn = 2.56) lifts Z only to **+0.21** — still "distress." A company with $3.6bn net cash, positive EBIT and positive FCF is not a bankruptcy candidate; the model simply cannot digest a post-SPAC loss history. **Weight the Z-score at near zero here; weight liquidity and coverage at full value.**

**Piotroski F-Score = 5:** points for positive ROA, positive operating cash flow, ROA improvement, positive equity change, gross-margin improvement. Fails on **accruals quality** (CFO $252M < net income $586M TTM), **leverage** (debt up 5.6x since 2024), **no dilution** (share count 3.995bn → 4.092bn) and **asset turnover** (0.301 → 0.281).

---

## 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility (756d) | **46.4%** |
| Beta vs SPY (computed, 756d) | **1.314** |
| Beta (vendor profile field) | 0.833 ⚠️ conflict |
| Max drawdown (3yr) | **−57.98%** |
| Sharpe ratio | **0.234** (weak) |
| Sortino ratio | **Not available — data gap** |
| Risk-free reference (UST) | 2Y 4.74% / 10Y 5.13% / 30Y 5.47%; 2s10s +39bp (no inversion) |

GRAB is a **high-beta, high-volatility equity** — 46% annualised vol, ~1.3x market sensitivity, and a **58% peak-to-trough drawdown** in three years. A Sharpe of 0.234 on a 0% risk-free assumption is **negative on a true risk-free basis** (46% vol vs 4.7% cash yields). Note the 1.314 computed beta contradicts the 0.833 profile field — I trust the computed regression; the stock is a drawdown amplifier, not a defensive.

**Critically, this is equity risk, not credit risk.** The 58% drawdown occurred while the balance sheet was net-cash and improving. Investors are being paid no premium for a sub-1% FCF yield while absorbing 46% vol.

---

## 4. Downside Scenario Analysis — Revenue −20%

Base: TTM revenue $3,970M, gross margin 44.4%, SG&A $925M, EBITDA $828M, interest $116M.

| Line item | Base TTM | −20% revenue (with 15% SG&A flex) | −35% severe stress |
|---|---|---|---|
| Revenue | 3,970 | 3,176 | 2,581 |
| Gross profit (44.4%) | 1,763 | 1,410 | 1,146 |
| SG&A | 925 | 786 | 740 |
| **EBITDA** | **828** | **624 (−25%)** | **~406 (−51%)** |
| D&A | 224 | 224 | 224 |
| **EBIT** | **604** | **400** | **~182** |
| Interest | 116 | 116 | 116 |
| **Interest coverage** | **5.2x** | **3.4x** | **~1.6x** |
| Gross debt/EBITDA | 2.5x | 3.3x | 5.1x |
| **FCF** | **156** | **~+340** | **~−50** |
| Net cash | 3,588 | ~3,300 | ~2,700 |

**Conclusion: a 20% revenue shock is entirely survivable.** EBITDA falls ~25% to $624M but stays strongly positive; interest coverage holds at 3.4x; free cash flow remains *positive* (because the base case is already depressed by working capital, not by cash burn). Even at −35% revenue, coverage is ~1.6x and the company retains **$2.7bn of net cash** — roughly **50+ years of runway** at that burn rate. There is **no plausible demand-shock path to a liquidity or covenant event.**

The real downside transmission channel is **not solvency — it is the multiple**: with FCF yield already <1.2%, a revenue shock that compresses the growth narrative would hit the equity far harder than the balance sheet. A 58% drawdown on this name is a demonstrated, not hypothetical, outcome.

---

## 5. Overall Financial Risk Rating: **MODERATE**

**Split verdict:**
- **Solvency / liquidity / credit risk: LOW.** Net cash ~$3.6bn, current ratio 1.38, cash ratio ~1.0, coverage 5.2x, debt/assets 0.15, voluntary debt prepayment, S&P upgrade to BB.
- **Earnings quality / momentum risk: HIGH.** Q3'26 margin collapse, receivables ballooning, negative accruals, sub-1% FCF yield.
- **Market / equity risk: HIGH.** 46% vol, 1.31 beta, −58% max drawdown.

Blended: **Moderate**, with the explicit caveat that the risk here is *valuation and earnings durability*, not *survival*.

---

## 6. Key Red Flags

1. **🔴 Q3'26 profitability breakdown.** EBITDA margin fell from **27.6% (Q2'26) to 9.3% (Q3'26)**; EBITDA $275M → $103M; net income $252M → **$27M**. Quarterly interest coverage collapsed to **1.27x** (EBIT $38M / interest $30M). This is the single most important data point in the file and directly contradicts the TTM picture — the trailing averages are flattered by a strong Q4'25–Q2'26.

2. **🔴 Acquisition-driven balance sheet expansion.** Goodwill + intangibles rose from **$1,051M (Q1'26) to $2,208M (Q3'26)** — roughly **$1.16bn of acquisitions closed in two quarters**, now **30% of book equity**. Total debt rose in lockstep and interest expense stepped from $12M (Q2'25) to $30M (Q3'26). The Q3 margin compression is almost certainly consolidation of lower-margin acquired revenue. **Impairment risk on $2.2bn of goodwill is now a live balance-sheet exposure.**

3. **🟠 Cash pile is being drawn down while debt rises.** Cash $6,804M (YE25) → $5,658M (Q3'26), a **$1.15bn decline in nine months**, while total debt ticked up to $2.07bn. Net cash fell from $4.75bn to $3.59bn.

4. **🟠 Buybacks exceed free cash flow.** $574M repurchased in 2026 YTD ($400M Q1'26, $174M Q3'26) plus $274M in 2025 — against **TTM FCF of only $156M**. Capital returns are being funded from the balance sheet, not from cash generation. Shareholder-friendly, but it erodes the very liquidity cushion that underpins the credit story.

5. **🟠 Working capital / receivables deterioration.** TTM change in working capital is **−$656M**. Receivables went from **$1,000M (YE25) to $1,956M (Q3'26)** — up 96% while revenue grew ~19%. Receivables now equal **49% of TTM revenue** vs 30% a year ago. Partly fintech lending book, but this is the driver of the **negative accruals signal** in the F-Score (CFO $252M vs net income $586M) and deserves scrutiny on collection quality and credit-loss provisioning.

6. **🟠 Short-term debt concentration.** **$1,618M of $2,070M total debt (78%) is current** — a refinancing wall inside 12 months. Mitigant: $5.66bn of cash covers it **3.5x**, and the $600M prepayment shows active management. Low risk, high monitoring priority.

7. **🟡 Altman Z-Score −0.545 (Distress)** — model artifact from −$17.5bn retained earnings; market-value-adjusted Z is +0.21, still "distress." **Do not use as a bankruptcy probability here.**

8. **🟡 FCF yield 0.95%** (1.17% on TTM FCF/market cap) — minimal cash return to owners for 46% volatility.

---

## Data Gaps & Caveats (explicit)

- **Peer benchmarking unavailable.** `get_sector_peers` returns US mega-cap Technology (AAPL, NVDA, MSFT, TSM, AVGO, SKHY) — not comparable to a SE Asian super-app. No Sea Ltd / Uber / DoorDash / GoTo comparison was obtainable. **All ratio analysis above is absolute, not relative.**
- **Stock-based compensation reported as $0** in all 2026 quarterly cash-flow rows — clearly a feed error, given $241M in FY25 and $412M in FY22. SBC is a real economic cost; FCF is overstated on a fully-loaded basis by roughly $240M+/yr.
- **Moody's rating not obtained** — only the S&P 'BB' upgrade was confirmed.
- **No Sortino ratio, no CDS spread, no covenant detail, no explicit debt maturity ladder** (only current/non-current split) available from the toolset.
- Balance-sheet `net_debt` field and leverage-tool `net_debt` disagree by ~$2.8bn; annual `operating_income` ($222M) and `EBIT` ($340M) disagree within the same filing. Both disclosed rather than resolved.

**Bottom line for the investment memo:** GRAB is a **balance-sheet-fortress, income-statement-fragile** story. Solvency risk is close to nil — $3.6bn net cash and positive FCF through a 35% revenue shock. But the Q3'26 margin collapse, a $1.16bn goodwill build, receivables nearly doubling, buybacks outrunning free cash flow, and a sub-1% FCF yield mean the *financial risk that matters* is earnings quality and equity drawdown, not default. Watch Q4'26 for whether the Q3 margin is acquisition-dilution or a genuine cost inflection.
