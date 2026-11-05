# Fin Risk Analyst

- Symbol: BE
- Elapsed: 54.3s

---
## BLOOM ENERGY CORPORATION (BE) — FINANCIAL RISK ASSESSMENT

**Data as of:** Q3 2026 (period ended 2026-09-30) | Price $200.40 | Market cap $59.2B

⚠️ **Critical framing note:** BE's reported FY2025 annuals (revenue $2.02B, net loss $88M) are badly stale. TTM through Q3 2026 shows revenue of **$3.83B** and net income of **+$518M**. Several automated tool outputs below are computed on FY2025 and materially understate current credit quality. I present both and flag which is which.

---

## 1. Credit Risk Assessment

**Rating: Investment Grade on metrics — but structurally Sub-Investment Grade (unrated)**

The single most important fact is the **capital structure, not the leverage ratio**. Debt is almost entirely long-dated, zero-coupon convertible paper:

- **$2.5B 0% Convertible Senior Notes due Nov 2030**, conversion price **$194.97** (issued/upsized Oct 2025)
- **3.0% Green Convertible Notes due June 2028** — became conversion-eligible Q1 2026 after closing-price condition was met; appears to have largely converted (equity jumped from $948M in Q1'26 to $1,964M in Q3'26)
- Total debt $2,782M; short-term portion only **$45.7M**

Two consequences:
1. **There is no refinancing cliff.** The nearest meaningful maturity is 2030, and it carries a 0% coupon.
2. **Cash ($2,487M) ≈ 89% of total debt, and essentially equals the $2.5B 2030 face.** Even in a total-conversion-failure scenario, BE can retire the notes from the balance sheet. Refinancing risk is close to nil.

The **caveat**: the 2030 notes only delever *if the stock stays above $194.97*. At $200.40 the notes are just **2.8% in the money** — the deleveraging is a stock-price-dependent outcome, not a contractual certainty. A de-rating below $195 leaves $2.5B of debt outstanding indefinitely. Conversion would add only ~12.8M shares (+4.3%), so dilution on conversion is modest — far better than the ~12% dilution already absorbed in 2026.

---

## 2. Key Financial Risk Metrics

| Metric | Q3'26 / TTM | FY2025 (tool basis) | Assessment |
|---|---|---|---|
| Debt / Equity | **1.42x** | 3.77x | Improved sharply via conversion |
| Net Debt / EBITDA | **0.48x** | 26.83x | Very low — strong |
| EBIT / Interest | **15.9x** | 1.35x | Very strong vs prior |
| Debt / Assets | **42.3%** | 68% | Acceptable |
| Current Ratio | **3.74x** | 5.98x | Strong |
| Quick Ratio | **3.07x** | 4.95x | Strong |
| Cash Ratio | **1.79x** | 3.93x | Strong |
| Working Capital | **$3,816M** | $3,107M | Ample |
| Cash / Total Debt | **89%** | 82% | Near-matched |
| Altman Z (book equity, tool) | **0.15 — Distress** | 0.15 | ⚠️ See note |
| Altman Z (market cap basis) | **≈8.5 — Safe** | — | Recomputed by me |
| Piotroski F-Score | **4 — Weak** (tool, FY25) | 4 | ⚠️ Stale |

**On the Z-Score:** the tool's 0.15 is an artifact, not a signal. Altman's X4 (equity/liabilities) collapses to 0.22 when book equity is used, because BE carries a **-$3.47B accumulated deficit** that suppresses book equity to $1.96B against $4.61B of liabilities. Recomputing with market capitalization (X4 = 12.85) yields **Z ≈ 8.5, deep in the safe zone**. The true bankruptcy signal sits between these; the market-cap version is economically meaningful here, and the book version is essentially a proxy for "this company funded itself with converts and losses for a decade." **Neither number should drive the credit view** — the debt maturity profile and $2.49B cash balance do.

**On the F-Score:** the 4/9 (weak) is computed on FY2025 and is obsolete. Three of the five failed tests have since reversed on TTM data: positive ROA (now +13.5% on TTM NI/assets), ROA improvement (yes), and gross-margin improvement (29.7%→32.3%). Only **F7 (no dilution) genuinely still fails** — share count rose from 263.6M to 294.8M, **+11.8% in nine months**. A restated TTM F-score would be roughly 6–7.

**Credit rating:** No public Moody's/S&P issuer rating was retrievable — **flagging as a data gap**. Structurally, unrated + convert-heavy + accumulated deficit argues high-yield; the metrics argue IG. I would not assume an IG rating exists to anchor institutional demand.

---

## 3. Market Risk Profile

| Metric | Value | Read |
|---|---|---|
| Annualized Volatility (756d) | **106.7%** | Extreme — top-decile risk |
| Beta vs SPY (756d, computed) | **2.30** | Amplifies drawdowns ~2.3x |
| Beta (profile, longer window) | **3.64** | ~3.6x — near-triple leverage to market |
| Max Drawdown (3yr) | **52.7%** | Modest *relative to* 107% vol |
| Sharpe (0% rf) | **1.81** | Strong, but backward-looking |

This is the risk category where BE genuinely earns a **Critical** mark. A 106.7% annualized volatility means a one-standard-deviation annual move of roughly ±107% — daily moves of 5–7% are routine. Beta of 2.3–3.6x means a 20% market drawdown plausibly produces a 45–70% BE drawdown. Note the **Sharpe of 1.81 alongside a 52.7% max drawdown** is the signature of a violent uptrend: the stock has run hard enough that even severe air-pockets look small against the trend. That is momentum, not stability — it is not a durable risk-adjusted return characteristic.

Valuation is a first-order market risk in its own right: **EV/EBITDA ≈ 95.8x, P/S ≈ 15.5x, P/E ≈ 114x**. At that multiple, the equity is priced for flawless execution. Fundamentals can be fine and the stock can still halve.

---

## 4. Downside Scenario Analysis

Assumptions: gross margin 32.3% TTM; **incremental/contribution margin ~45%** on lost revenue (high fixed-cost absorption in cost of revenue); SG&A held flat at $435M; implied R&D/other $236M held flat. Operating leverage is extreme in both directions — Q3'26 alone showed revenue +44% QoQ driving operating margin from 9.6% to 18.2%.

| Scenario | Revenue | Gross Profit | EBIT | EBITDA | Net Debt/EBITDA | Interest Cov. | FCF |
|---|---|---|---|---|---|---|---|
| **Base (TTM)** | $3,830M | $1,238M (32.3%) | $567M (14.8%) | $621M | **0.48x** | 15.9x | +$440M |
| **−20% revenue** | $3,064M | $893M (29.2%) | $223M (7.3%) | $277M | **1.07x** | **6.2x** | +$140M |
| **−35% revenue** | $2,489M | $635M (25.5%) | **−$36M** | $18M | **16x** | Negative | −$100M |
| **Revenue break-even** | **≈$2,570M (−33%)** | $671M | $0 | $54M | — | 0x | — |

**Interpretation.** A 20% revenue decline is comfortably survivable: still profitable, still ~$140M FCF-positive, net leverage only 1.07x, coverage 6.2x. **The solvency break-point is roughly a 33% revenue decline** — a very wide cushion for a company that just grew 138% YoY. Even at −35%, with $2,487M of cash against a ~$100M annual burn, **cash runway exceeds 20 years** and the 2030 notes could be repaid from the balance sheet. *This company does not have a solvency problem in any plausible demand scenario.*

**The real downside is equity-holder, not creditor.** At −35% revenue, EBIT is negative and the 2030 converts fall far out of the money — the $2.5B stays as debt, no equity is created by conversion, and a 95.8x EV/EBITDA multiple compresses against collapsing EBITDA. That is a 60–80% equity impairment path that never shows up in any credit ratio.

---

## 5. Overall Financial Risk Rating

### **MODERATE**

Decomposed:

| Risk Dimension | Rating | Driver |
|---|---|---|
| **Credit / Solvency** | **Low** | 0.48x net leverage, 15.9x coverage, no maturity before 2030, cash ≈ total debt |
| **Liquidity** | **Low** | 3.74x current, $2.49B cash, >20yr stress runway |
| **Market / Volatility** | **Critical** | 107% vol, 2.3–3.6x beta, 52.7% max DD |
| **Valuation** | **High** | 95.8x EV/EBITDA, 15.5x sales, 114x earnings |
| **FCF Sustainability** | **Moderate** | 11.5% FCF margin but Q3'26 FCF turned negative on WC + capex |

**The core insight: BE's balance-sheet risk and its equity risk have almost completely decoupled.** The 2025 convert issuance converted what was a genuine credit story (26.8x net leverage, 1.35x coverage) into an equity-duration story in under twelve months. Creditors are well protected. Equity holders carry extraordinary risk — but from volatility and multiple compression, not from leverage.

---

## 6. Key Red Flags

1. **Working capital is deteriorating fast.** Q3'26 operating cash flow was **−$27.1M against net income of +$249.3M** — a ~$276M gap driven by a **−$356M working capital swing**. Inventory is up **44% since YE2025** ($643M→$928M) and receivables +13%. Cash conversion is breaking down precisely as revenue accelerates. If growth stalls, this inventory is a write-down candidate.

2. **Capex is ramping hard.** Q3'26 capex of **$153.5M** in a single quarter vs $26.1M in Q1'26 — annualizing toward ~$600M. TTM FCF of $440M is flattered by an unusually strong Q4'25 (+$398M) and will compress as this capex lands.

3. **~12% dilution in nine months.** Shares 263.6M → 294.8M; diluted 324.3M. The only genuinely still-failing Piotroski test. Convert-driven deleveraging is real but it is being paid for in equity.

4. **Deleveraging is contingent on the share price.** The 2030 notes are only **2.8% above their $194.97 strike**. Below that level, the $2.5B never converts and the "deleveraging" reverses on paper.

5. **Valuation at 95.8x EV/EBITDA / 15.5x sales** leaves no margin for error and is itself a primary risk factor.

6. **Extreme operating and market leverage.** 107% volatility with a cost structure where a 44% revenue swing moves operating margin by ~860bp.

7. **Data quality flags:** (a) goodwill & intangibles of $215.5M at Q2'26 vanishing to $0 at Q3'26 with no stated disposal — unexplained; (b) FY2025 annual shows EBIT of −$30.5M against operating income of +$72.8M — internally inconsistent, likely a non-operating charge in the EBIT line; (c) **no public credit rating retrievable**; (d) **no valid fuel-cell peer set** — the sector tool returned mega-cap Industrials (GE, CAT, RTX, GEV) that are not meaningful comparables for a solid-oxide fuel cell manufacturer; (e) the FCF-yield tool used a stale ~240M share count, understating market cap ($48.2B vs $59.2B) and overstating the yield drag — I have recomputed FCF yield at **0.74%** on TTM FCF of $440M.

---

**Bottom line for the memo:** BE is not a credit risk — it is a valuation and volatility risk wearing a leverage-ratio costume. The company can absorb a one-third revenue collapse without threatening its solvency, has no maturity before 2030, and holds cash roughly equal to its entire debt stack. But at 95.8x EV/EBITDA with 107% realized volatility, 2.3–3.6x beta, and deteriorating working-capital dynamics, the equity's downside is severe and driven almost entirely by multiple compression. Size positions accordingly, and monitor the $194.97 conversion threshold and quarterly cash conversion as the two leading indicators that matter.
