# Fin Risk Analyst

- Symbol: STLA
- Elapsed: 114.2s

---
# STLA — Stellantis N.V. | Complete Financial Risk Assessment

**Sector:** Consumer Cyclical / Auto Manufacturers (Netherlands) | **Price:** $3.92 | **Market cap:** ~$11.4bn | **Employees:** 258,668
**Latest financials:** FY ending 2026-09-30 (€m) | **Rating:** Moody's Baa3 / S&P BBB- (negative) / DBRS BBB

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE (lowest investment grade, rapid deterioration) — on a 12–24 month view the balance sheet is tracking toward high yield.**

The company retains a BBB-/Baa3 label, but every credit metric has deteriorated for three consecutive years, and the qualitative case for investment grade now rests almost entirely on the label rather than on cash generation.

| Year | Revenue (€bn) | EBITDA (€bn) | EBIT (€bn) | Net income (€bn) | Net debt (€bn) | FCF (€bn) |
|---|---|---|---|---|---|---|
| 2023 | 189.5 | 30.5 | 23.0 | +18.6 | ~3.1 (2024) | +0.01 |
| 2024 | 156.9 | 12.7 | 5.4 | +5.5 | 3.1 | −7.1 |
| 2025 | 153.5 | −15.3 | −22.2 | −22.4 | 15.8 | −16.2 |
| **2026** | **119.2** | **6.4** | **1.7** | **+0.2** | **27.0** | **−11.4** |

Revenue is down **37% from the 2023 peak**. Cumulative three-year FCF deficit is **−€34.6bn**, funded almost entirely with debt: net debt has risen **~8.6x in two years** (€3.1bn → €27.0bn). FY2025 produced a **gross loss of €4.2bn** on revenue of €153.5bn — a catastrophic cost-position outcome — followed by a partial recovery to a €12.6bn gross profit (10.6% margin) in FY2026, but not enough to restore cash generation.

Critically, **the two independent solvency screens both fail**: Altman Z-Score of **0.83 (distress zone)** and Piotroski F-Score of **5 (moderate)** — and the F-Score's losses are in the highest-weight items (negative operating cash flow, poor accruals quality, dilution, falling asset turnover).

External validation corroborates the trajectory: Moody's cut to **Baa3**, S&P to **BBB- with negative outlook**, DBRS to BBB (Jan 2026), each step explicitly tied to extended cash burn and a three-year pattern of negative industrial free cash flow.

---

## 2. Key Financial Risk Metrics Table

| Metric | Value | Interpretation |
|---|---|---|
| **Leverage** | | |
| Debt / Equity | 0.91x | Manageable on book, but book is ~75% intangibles |
| Total debt / Assets | 0.26x | Low — asset-heavy OEM + captive finance |
| **Net debt / EBITDA** | **4.11x** | Breach territory for a cyclical; >4x typically HY |
| Gross debt / EBITDA | 8.75x | Elevated; €56.0bn total debt |
| **Coverage** | | |
| EBIT / Interest (operating income €914m) | **0.79x** | **Fails — EBIT does not cover interest** |
| EBIT / Interest (EBIT line €1,662m) | 1.44x | Still below the 2.0x comfort threshold |
| EBITDA / Interest | 5.53x | Only genuinely comfortable metric |
| **Liquidity** | | |
| Current ratio | 1.02x | Razor-thin |
| Quick ratio | 1.02x | *Data artifact — see gaps* |
| Cash ratio | 0.35x | Acceptable |
| Working capital | **€1.52bn** | ~1.3% of revenue — no buffer |
| Cash & ST investments | €29.7bn | Large, but partly captive-finance cash |
| Cash / Short-term debt | 1.94x | Adequate for near-term maturities |
| **Solvency Screens** | | |
| **Altman Z-Score** | **0.833 — DISTRESS** | Adjusted to ~1.21 with reported retained earnings; ~0.6 market-based. All readings < 1.81 |
| **Piotroski F-Score** | **5 / 9 — Moderate** | F2 (op CF) = 0, F4 (accruals) = 0, F7 (dilution) = 0, F9 (turnover) = 0 |
| **Cash Flow** | | |
| FCF (FY2026) | **−€11.37bn** | OCF −€6.82bn, capex €4.55bn |
| **FCF yield** | **−99.5%** (reported); ~−110% FX-consistent | Deeply negative |
| FCF margin | −9.5% | Structural cash destruction |
| Working capital drain (FY2026) | **−€13.2bn** | Single largest cash outflow |

---

## 3. Market Risk Profile

⚠️ *The `calculate_price_volatility` tool failed (FMP `dividend-adjusted` endpoint not on subscription plan). The figures below are **manually derived from the daily OHLCV series** and should be treated as estimates. Beta is taken from the company profile.*

| Metric | Value | Note |
|---|---|---|
| Price (12-Nov-2026) | $3.92–3.93 | All-time low; intraday low $3.87 |
| 1-year return | **−63.3%** | From ~$10.72 |
| 3-year return | **−76.8%** | From ~$16.92 |
| **Max drawdown (3yr)** | **−84.5%** | Peak $25.28 (25-Mar-2024) → $3.93 |
| 52-week range | $3.87 – $12.22 | Current price at the low |
| Annualised volatility | **~48–55% (est.)** | Manual estimate; single-day −23.7% (06-Feb-2026) and +13.0% (28-Oct-2026) |
| Beta vs market | **0.995** (profile) | Understates tail sensitivity — see below |
| Sharpe ratio | **~−0.75 (est.)** | ~−38% annualised return vs ~50% vol |
| Sortino ratio | Worse than Sharpe (est.) | Negative skew, fat left tail |
| Market cap peak-to-now | ~$73bn → **$11.4bn** | −84% |

**Interpretation:** Reported beta of 0.995 is a five-year monthly regression and is misleading. The realised path shows the stock **falling 84% while equity markets broadly rose** — this is idiosyncratic/credit-driven risk, not market beta. Downside participation is effectively uncapped in a way the beta statistic does not capture. Volatility clustering is severe (multi-week 20%+ swings), and the +13%/+7.6% single-day rallies on results dates are classic distressed-equity behaviour — high variance around fundamental news, not the signature of a stable compounder.

**Valuation-as-risk-signal:** price/book is **0.17x** on €61.8bn book equity. Tangible book is only **€15.7bn** (equity less €46.1bn goodwill & intangibles) — a **0.66x** price/tangible-book. The market is explicitly pricing a large write-down of the €46.1bn intangible base.

---

## 4. Downside Scenario Analysis — Revenue −20%

**Base (FY2026A):** Revenue €119.2bn · EBITDA €6.40bn (5.4%) · EBIT €1.66bn · Interest €1.16bn · Net debt €27.0bn · Equity €61.8bn · Cash €29.7bn · FCF −€11.4bn

**Assumption:** 25% decremental margin (OEM fixed-cost absorption; already near break-even, so limited variable-cost flexibility). No tax shield on losses.

| Line item | **Base** | **−10% rev** | **−20% rev** | **−35% (tail / 2008-style)** |
|---|---|---|---|---|
| Revenue | 119.2 | 107.3 | **95.4** | 77.5 |
| EBITDA | 6.40 | 3.42 | **0.44** | **−9.7** |
| EBIT | 1.66 | 0.24 | **−4.30** | **−14.4** |
| **EBITDA / Interest** | 5.5x | 3.0x | **0.4x** | **negative** |
| **EBIT / Interest** | 1.44x | 0.2x | **negative** | **negative** |
| **Net debt / EBITDA** | 4.1x | 7.9x | **~61x (not meaningful)** | **not meaningful** |
| Net debt | 27.0 | 39.8 | **~54** | ~70+ |
| Equity (pre-impairment) | 61.8 | 57.8 | **~53** | ~43 |
| Equity (post goodwill write-down) | 61.8 | ~50 | **~40** | **~20** |
| FCF | −11.4 | −12.8 | **~−14.5** | ~−18 |

**What breaks in the −20% case:**

1. **Interest coverage goes negative.** EBIT of −€4.3bn against €1.16bn of interest. EBITDA of €0.44bn covers only 0.4x of interest — the company would be funding interest from cash reserves.
2. **Leverage becomes unanalysable.** Net debt/EBITDA of ~61x. This is a refinancing-viability question, not a leverage question.
3. **Liquidity is consumed within ~18 months.** Cash of €29.7bn against ~€14.5bn annual burn, while **€15.3bn of debt matures inside 12 months**. On a static basis cash covers short-term debt 1.94x — but that headroom disappears by year two if burn persists.
4. **Refinancing cliff bites.** €38.0bn of long-term debt must be termed out. At BBB-/Baa3 with negative outlook, a 200–300bp spread widening on refinancing costs ~**€0.8–1.1bn of incremental annual interest** — against EBIT of €1.7bn in the base case. That alone could push the company to a net loss.
5. **Equity-raising becomes unavoidable and enormously dilutive.** At 0.17x book, any capital raise transfers value to creditors. A €3–5bn raise at ~$4/share would dilute existing holders 25–45%.
6. **Rating migration to sub-investment grade.** A −20% revenue scenario is inconsistent with retaining BBB-. Fallen-angel status would trigger index-driven selling and forced selling from IG-mandate funds, compounding the −84% drawdown.

**Mitigants:** €29.7bn cash; gross debt/assets only 0.26x (substantial collateral — €47.1bn PP&E, €46.1bn intangibles); captive finance book can be deconsolidated or sold (Stellantis has precedent — Comau, other asset sales); dividend and buybacks are already at zero, preserving ~€4.7bn/yr of prior distributions; brand portfolio (Jeep, Ram, Peugeot) has strategic value to competitors.

---

## 5. Overall Financial Risk Rating: **HIGH** (bordering **CRITICAL** on cash flow)

The balance sheet has not yet reached a liquidity wall — €29.7bn of cash and a still-investment-grade rating provide real runway. But the **cash-generation engine is broken**: three consecutive years of negative FCF totalling −€34.6bn, interest coverage below 1.0x on operating income, an Altman Z-Score of 0.83, and net debt that has multiplied 8.6x in two years. This is a company that is currently **consuming, not producing, capital**.

The distinction between "High" and "Critical" is entirely contingent on whether the FY2026 stabilisation (gross margin back to 10.6%, EBIT back to positive €1.66bn, F-Score 5 rather than 2) is the trough or a pause. A single further year of −20% revenue would move this to Critical. I would not underwrite STLA equity or unsecured debt at current leverage without explicit visibility on the FY2027 operating plan and asset-sale proceeds.

---

## 6. Key Red Flags

1. **Interest coverage of 0.79x on operating income** — EBIT does not cover interest expense. This is the single most serious metric on the page.
2. **Three straight years of negative free cash flow** (−€7.1bn, −€16.2bn, −€11.4bn = −€34.6bn cumulative), financed with debt.
3. **Net debt up 8.6x in two years** (€3.1bn → €27.0bn), with net debt/EBITDA now 4.11x.
4. **Revenue down 37% from peak** (€189.5bn → €119.2bn) with operating margin of just 0.77%.
5. **Altman Z-Score 0.833 — deep distress zone**; market-capitalisation-based Z is ~0.6.
6. **€46.1bn of goodwill and intangibles = 75% of book equity.** Equity is impaired-asset-inflated; tangible book is €15.7bn. A write-down to market-implied value could remove €20–30bn of equity.
7. **Equity declining while debt rises** — €82.1bn (2024) → €61.8bn (2026), −25%, even as total debt rose from €37.2bn to €56.0bn. Classic deleveraging-in-reverse.
8. **Working capital drain of €13.2bn in FY2026** — the largest single cash outflow and a sign of deteriorating receivables/payables discipline.
9. **Ratings one notch from high yield** (Moody's Baa3; S&P BBB- negative) with **€38bn of long-term debt to refinance** into a materially worse spread environment.
10. **Working capital of only €1.52bn on €119bn of revenue** — no liquidity cushion in the operating business.
11. **F-Score weaknesses in the highest-signal components**: negative operating cash flow (F2), poor accruals quality (F4 — net income not backed by cash), dilution (F7), declining asset turnover (F9).
12. **Stock at all-time low, −84.5% from peak**, with single-day −24% gaps — the market is pricing solvency risk, not cyclicality.

---

## 7. Data Gaps & Caveats (explicitly flagged)

| Gap | Impact |
|---|---|
| **`calculate_price_volatility` unavailable** (FMP subscription limit). Vol, beta-consistency, Sharpe, Sortino are **manually estimated** from OHLCV. Beta 0.995 is a profile figure, not independently verified. | Market Risk section is directional, not precise |
| **Inventory reported as €0 for FY2026** (vs €22.2bn in FY2025). This mechanically forces quick ratio = current ratio (1.02x). **True quick ratio is materially lower — likely ~0.65–0.75x.** | Liquidity is overstated in the reported quick ratio |
| **Retained earnings reported as €0 for FY2026** (vs €53.3bn in FY2025). This zeroes Altman's x2 term and **understates the Z-Score**. Adjusted Z ≈ 1.21 — still distress, but the reported 0.833 is pessimistic. | Altman reading is a floor, not a point estimate |
| **FCF yield currency mismatch** — FCF in EUR, market cap in USD. Reported −99.5%; FX-consistent figure ≈ −110%. | Directionally correct either way |
| **FY2026 period ends 2026-09-30** — a non-calendar fiscal year-end, likely a transition period. Year-over-year comparisons to FY2025 (Dec year-end) are **not strictly like-for-like**; D&A fell from €6.98bn to €4.74bn, consistent with prior impairments. | Trend is valid; precise growth rates are approximate |
| **No debt maturity schedule, covenant package, RCF availability, or CDS spread** available from tools. | Refinancing-cliff analysis is inferred from €15.3bn ST / €38.0bn LT split, not a dated ladder |
| **Captive finance is consolidated.** A large portion of €56.0bn debt and €29.7bn cash belongs to the financial-services book and is self-liquidating; industrial net debt is materially lower than €27.0bn. Third-party reports cite ~€2.5bn industrial burn in 2026 vs the €11.4bn consolidated FCF shown here. | Consolidated ratios **overstate** industrial leverage; I have used consolidated figures throughout for consistency and flagged the difference |
| No segment-level (NA vs Europe) breakdown available. | Cannot isolate which region drives the cash burn |

---

### Bottom Line
STLA is a **High** financial risk. It is not yet a liquidity failure — €29.7bn of cash against €15.3bn of near-term maturities buys time — but it is a **cash-flow failure in progress**: negative FCF three years running, interest coverage below 1.0x, a distress-zone Z-Score, and €46bn of intangible-heavy equity that the market values at 17 cents on the dollar. The entire investment case now hinges on whether FY2026 marks the operating trough; a −20% revenue shock from here produces negative EBIT, ~61x leverage, and a fallen
