# Fin Risk Analyst

- Symbol: ALNY
- Elapsed: 64.1s

---
## ALNY — Financial Risk Assessment
*Data as of: FY2025 (10-K, filed 2026-02-12) for financials; Q3 2026 (10-Q) for interim trends; market data through 2026-11-20.*

### 1. Credit Risk Assessment — **Sub-Investment Grade (BB-equivalent), Stable-to-Weakening**

Alnylam is **not a leveraged credit story — it is a single-franchise business-risk story**. The balance sheet is net cash and liquidity is abundant, but the *quality* of the credit rests almost entirely on one product line that just broke its growth narrative.

| Signal | Reading | Interpretation |
|---|---|---|
| Net debt / EBITDA | **−2.58x** (net cash $1,630m) | Undeniable positive |
| Interest coverage (EBIT/int.) | **1.99x** FY25; ~**2.8x** TTM | Thin for a "net cash" company — see red flag #3 |
| Debt / equity (book) | 1.62x | Distorted by −$6.70bn accumulated deficit |
| Debt / assets | 0.26x | Conservative |
| Altman Z | **−0.02 (Distress)**; **~2.77 (Grey)** using market cap for X4 | Book-equity version is meaningless here (X2 = −1.35 from the deficit). Market-cap adjusted, ALNY sits mid-grey zone |
| Piotroski F | **7 / 9** | Genuine improvement: positive ROA, positive OCF, lower leverage, positive equity change |
| FCF (FY25) | **+$465m** (first real inflection; −$613m in FY22) | Real, but see SBC caveat |

**Verdict:** Solvency risk over a 2–3 year horizon is **low**; *credit deterioration* risk is real because the model was priced as a self-funding growth compounder and that assumption has now been challenged by management's own guidance.

### 2. Key Financial Risk Metrics

| Metric | FY2022 | FY2023 | FY2024 | FY2025 | Q3'26 / TTM |
|---|---|---|---|---|---|
| Revenue ($m) | 1,037 | 1,828 | 2,248 | 3,714 | **5,013 TTM** (+52% y/y in Q3) |
| Gross margin | 83.7% | 83.0% | 85.6% | 81.8% | ~77% (Q3'26 75.2%) — **compressing** |
| EBIT ($m) | (971) | (312) | (236) | **+576** | **+1,012 TTM** |
| EBITDA ($m) | (927) | (258) | (179) | +631 | +1,248 TTM |
| Interest expense ($m) | 156 | 121 | 142 | **253** | **365 TTM** |
| Total debt ($m) | 1,320 | 1,305 | 1,296 | 1,278 | ~1,278 (YE25) |
| Cash + ST inv. ($m) | 2,192 | 2,439 | 2,695 | **2,908** | n/a (gap) |
| Net debt ($m) | +454 | +493 | +330 | **(1,630)** | net cash |
| Book equity ($m) | (158) | (221) | 67 | 789 | materially higher post one-off |
| FCF ($m) | (613) | +42 | (43) | **+465** | likely higher TTM |
| Current ratio | — | — | — | **2.76** | — |
| Quick ratio | — | — | — | **2.71** | — |
| Cash ratio | — | — | — | **1.98** | — |
| Working capital ($m) | — | — | — | 2,584 | — |

**Liquidity:** No concern. $2.9bn cash/securities vs $1.28bn debt; working capital $2.58bn. Against FY25 cash burn of ~nil, runway is effectively indefinite at current run-rate.

**FCF quality (the caveat):** FY25 OCF of $524m includes a **$348m stock-comp add-back** (9.4% of revenue) and absorbed a **−$445m working-capital drag**. SBC-adjusted FCF is only ~**$117m** — i.e., a 0.6% FCF yield, not the reported 2.29%. Receivables rose 92% to $778m vs revenue +65% (DSO 76 days vs 66 in FY24) — worth monitoring for channel/collectability stress.

**Debt structure (from filings/search, partial):** $362.8m of 1.00% converts due **Sept 15, 2027** (now current), $661m of 0.00% converts due **2028**, plus ~$575m 2028 notes — roughly **$1.3bn maturing inside ~24 months**. With the stock at $150 (vs conversion prices set far higher), these will be **cash-settled, not converted** — a ~$1.3bn cash call against a ~$2.9bn cushion. Manageable, but it consumes most of the downside buffer if revenue stalls. *Note the tool reported $0 short-term debt at YE25; the 2027 convert has since been reclassified current.*

### 3. Market Risk Profile — **Severe**

| Metric | Value |
|---|---|
| Annualised volatility (3y) | **48.7%** |
| Beta vs SPY (756d) | 0.84 (profile beta: 0.27) |
| Max drawdown (3y) | **−69.9%** |
| Sharpe ratio | **−0.31** |
| Sortino | Not provided (gap); with Sharpe < 0, downside deviation has overwhelmed returns |

**Verified drawdown anatomy (from daily data):** peak **$495.55 (Oct 20, 2025)** → trough **$147.82 (Nov 19, 2026)** = **−70.2%**, matching the computed −69.9%.

- **Jul 30, 2026:** −28% in one session (Amvuttra Q2 miss) — $286.62 → $205.48
- **Oct 29, 2026:** −25% in one session (Q3 miss + 2026 TTR guidance cut) — $232.40 → $174.00
- *Preceded by:* Jun 24, 2024 +35% in one day ($165.70 → $222.90) on positive ATTR data.

This is a **binary-event equity**: extreme single-day gap risk in both directions, fat tails, and negative risk-adjusted return over three years. The low 0.84 beta is *not* reassurance — it is an artifact of massive idiosyncratic (not market) risk. For portfolio construction purposes, treat ALNY as a high-vol, single-catalyst credit-linked equity with ~50% annualised vol and realistic 1-day tail of −25% to −30%.

### 4. Downside Scenario: Revenue −20% (no cost response)

TTM revenue $5,013m → **$4,010m**; gross margin ~77% → gross profit $3,088m → **$2,470m**. Operating cost base is sticky (TTM SG&A $1,338m + derived R&D ~$1,525m = **$2,862m**; R&D is relatively fixed in biotech).

| Line | Base (TTM) | −20% revenue |
|---|---|---|
| Gross profit | $3,864m | $3,088m → $2,470m |
| Opex (held flat) | $2,862m | $2,862m |
| **EBIT** | **+$1,012m** | **≈ −$392m** |
| EBITDA | +$1,248m | ≈ −$336m |
| Interest coverage | 2.8x | **negative** |
| Net debt/EBITDA | net cash | still net cash, but burning |

**Interpretation:** a 20% revenue decline flips ALNY from ~$1.0bn of EBIT to a ~$390m EBIT loss — a **$1.4bn EBIT swing**, illustrating extreme operating leverage. Combined annual cash need ≈ $390m pre-interest + $365m interest ≈ **$755m/yr**, against ~$1.6bn net cash → **~2-year runway** before external financing, absent R&D cuts. A 25% R&D reduction (~$380m) would roughly restore breakeven — that is the likely management lever, and it is exactly what impairs the long-term pipeline.

**Compounding risk in this scenario:** a 20% revenue miss likely re-rates the equity well below current $150, keeping the 2027/2028 converts deeply out of the money → ~$1.3bn repaid in cash rather than converted. That, plus burn, would move ALNY from net cash to **material net debt within ~24 months**. This is the specific path from "Low solvency risk" to "High."

### 5. Overall Financial Risk Rating: **MODERATE**
*(Balance-sheet risk: Low. Business-model / equity risk: High. Blended: Moderate, on a deteriorating trend.)*

Rationale: net cash, 2.8x TTM coverage, positive FCF, 7/9 Piotroski and $2.9bn liquidity justify **not** calling this elevated or critical. But concentration, guidance cuts, compressing gross margin, SBC-heavy cash conversion and a ~$1.3bn convert wall mean the cushion is thinner than headline net cash implies — and it is shrinking.

### 6. Key Red Flags

1. **Single-franchise concentration.** TTR (Amvuttra) is ~79% of Q3'26 revenue ($1,150m of $1,458m) and the entirety of 2026 guidance ($4.2bn TTR). One product, one indication set, one competitor (Ionis' donidalorsen) driving the demand shift that triggered both 2026 guidance cuts. This is the dominant credit and equity risk.
2. **Interest expense is inconsistent with reported debt.** $365m TTM interest on ~$1.28bn of *0%–1% coupon* converts implies an effective cost near 28%. Either the reported debt figure is incomplete, or there are substantial **debt-like obligations outside "total debt"** (note: ~$1.7bn of non-current liabilities sit beyond current liabilities + LT debt on the YE25 balance sheet, consistent with royalty monetization). **Treat my 2.8x coverage — and possibly my net-cash figure — as optimistic until the full debt footnote is reviewed.** This is the single largest analytical gap in this report.
3. **Refinancing cliff inside 24 months.** ~$1.3bn of converts mature 2027–2028 and are all out-of-the-money at $150 → cash settlement, not equity. Consumes ~80% of the cash cushion.
4. **Guidance credibility / growth durability.** Two guidance-related −25%+ single-day collapses in six months (Jul & Oct 2026); TTR guidance cut. Management's forward numbers now warrant a discount.
5. **Earnings quality.** Q3'26 "net income" of $2,167m was inflated by a **$1,871m non-cash income-tax benefit** (deferred-tax valuation-allowance release), not operations — operating income was only $380m. Book equity improvement is largely accounting, **and is reversible as a non-cash charge if profitability expectations fall again** post-guidance-cut.
6. **FCF quality.** 67% of FY25 operating cash flow ($348m of $524m) is non-cash stock compensation; SBC-adjusted FCF yield is ~0.6%. Reported FCF yield of 2.29% overstates cash generation.
7. **Gross margin compression** (85.6% FY24 → 81.8% FY25 → 75.2% Q3'26) — mix shift and price/rebate pressure worth tracking.
8. **Dilution.** Shares 121.7m → 134.0m (+10%) since FY22; Piotroski F7 fails on equity issuance.

### Data Gaps (explicit)
- **No debt maturity schedule, covenant detail, or revolver availability** from the data feeds — maturity data is partial, from press releases/search only.
- **No credit rating or CDS spread** available; "BB-equivalent" is my inference from net-cash/coverage, not an agency view.
- **No cash/investment balance at Q3 2026** — all liquidity ratios are as of 2025-12-31 and are now ~11 months stale.
- **R&D expense line not supplied** by the feed; derived as a residual (≈$1,525m TTM) — scenario outputs are approximate.
- **Sortino ratio** not computable from available tools.
- Peer comparison not meaningful: the peer set returned is large-cap diversified pharma (LLY, JNJ, ABBV, MRK), not commercial-stage biotech comparables. No peer multiples computed.
