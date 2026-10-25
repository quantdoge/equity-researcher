# Fin Risk Analyst

- Symbol: BSP
- Elapsed: 222.6s

---
Both S&P and Forbes blocked automated fetch (403) — I'll rely on the search snippets, which gave the key facts, and flag the rest as gaps. I have enough to complete the assessment.

---

# BENDING SPOONS S.p.A. (BSP) — Financial Risk Assessment

**Price $47.07 | Market cap $29.90bn | Sector: Technology / Software-Application | Domicile: Italy | IPO: 2026-07-01**

**Critical framing note:** BSP's fiscal 2025 statements are *not representative* of the current business. Revenue doubled via the AOL (~$1.43bn, closed Oct 2025), Vimeo and Eventbrite acquisitions, and total debt nearly doubled again in H1 2026 ($2.67bn → $4.96bn). Tool-computed ratios on FY2025 data are therefore stale. I have rebuilt all metrics on a **TTM (Q3'25–Q2'26)** basis alongside the reported figures.

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE — S&P 'BB-' (upgraded from 'B+', stable outlook)**

BSP is a leveraged serial acquirer, not a net-cash software company. The credit is genuinely improving (S&P upgrade, EBITDA +41.9% margin) but the balance sheet is structurally thin: **78.2% of assets are goodwill and intangibles, and tangible book equity is −$5.04bn.**

| Metric | FY2024 | FY2025 | TTM Q2'26 | Assessment |
|---|---|---|---|---|
| Revenue ($M) | 671.1 | 1,306.4 | 2,041.8 | Acquisitive, not organic |
| EBITDA ($M) | 226.6 | 410.8 | 854.5 | Strong margin (41.9%) |
| EBIT ($M) | 137.4 | 253.8 | 542.3 | 26.6% margin |
| Net income ($M) | 89.5 | **−0.1** | 251.1 | Recovered in H1'26 |
| Interest expense ($M) | 32.6 | 142.6 | 288.7 | **+786% in 2 yrs** |
| **EBIT / interest** | 4.22x | **1.78x** | **1.88x** | Thin |
| **EBITDA / interest** | 6.95x | 2.88x | 2.96x | Adequate |
| Net debt / EBITDA | 2.77x | 4.97x | **4.87x** | Elevated |
| Gross debt / EBITDA | 3.83x | 6.50x | **5.80x** | Elevated |

**Run-rate interest is the key under-appreciation.** Q2'26 interest was $107.99M → **~$432M annualized**, versus TTM EBIT of $542M. On the $5.7bn gross debt S&P projects by YE2026, interest approaches ~$456M against forward EBIT of ~$721M (H1'26 annualized) → **forward EBIT coverage only ~1.6x**. FY2025's 1.95x (operating income basis) is flattered by partial-year debt. Interest has grown 6.6x faster than EBIT since 2024 — the defining trend.

**Altman Z-Score is misleading here and must be read two ways:**
- Book-equity basis (tool, FY2025): **0.654 — Distress zone**
- Rebuilt on Q2'26 TTM: **0.57 — Distress zone**
- Market-cap basis (x4 = 4.40x): **Z ≈ 3.09 — just above the 2.99 safe threshold**

The entire gap is the market's 23.8x premium to book equity and the negative tangible book. The *insolvency* signal is largely an artefact of acquisition accounting, but the *leverage* signal is real.

**Piotroski F-Score: 4/9 (Weak)** — failing on negative FY2025 ROA, rising leverage, dilution (587M → 620M shares), and declining asset turnover (0.356 → 0.275 as assets tripled). Directionally improving into 2026 but still below investment-grade norms.

---

## 2. Key Financial Risk Metrics (Q2'26 / TTM basis)

| Metric | Value | Threshold | Verdict |
|---|---|---|---|
| Net debt / EBITDA | **4.87x** | >4.0x = high | ✗ High |
| Gross debt / EBITDA | **5.80x** | >5.0x = high | ✗ High |
| Debt / equity | **3.94x** | >2.0x | ✗ High |
| Debt / assets | **61.5%** | >50% | ✗ High |
| EBIT / interest | **1.88x** | <2.0x weak | ✗ Weak |
| EBITDA / interest | **2.96x** | <3.0x weak | ⚠ Borderline |
| Altman Z (book) | **0.57** | <1.81 distress | ✗ Distress |
| Altman Z (market cap) | **3.09** | >2.99 safe | ⚠ Boundary |
| Piotroski F | **4/9** | <4 weak | ⚠ Weak |
| Current ratio | **0.64x** | <1.0 | ✗ High |
| Quick ratio | **0.64x** | <1.0 | ✗ High |
| Cash ratio | **0.375x** | <0.5 | ✗ High |
| Working capital | **−$761M** | Negative | ✗ High |
| Cash / short-term debt | **0.98x** | <1.0 | ⚠ Tight |
| Tangible book equity | **−$5.04bn** | Negative | ✗ High |
| Goodwill+intangibles / assets | **78.2%** | >50% | ✗ High |
| FCF yield | **~1.0–1.3%** | <2% | ✗ Thin |
| Net debt / FCF | **~11x** | >5x | ✗ High |

**Liquidity:** No cash-burn problem — FCF is positive (H1'26: $202.3M, ~$100M/quarter). But the current ratio of 0.64x and a $761M working-capital deficit mean the company runs on revolving access, not balance-sheet liquidity. Cash of $793M covers short-term debt of $807M at 0.98x — **zero headroom on the nearest maturity wall.** Q2'26 also saw a −$138.8M working-capital outflow, the second consecutive large drag.

**FCF sustainability:** Ample and improving in absolute terms, but low-yielding. Capex is negligible (<$5M/yr) because the business model capitalizes acquisitions as intangibles rather than investing in PP&E — so reported FCF is structurally flattered by excluding the real "capex," which is M&A. At ~$380M TTM FCF against $4.17bn net debt, **deleveraging organically takes ~11 years.** The credit depends on EBITDA growth and continued capital-markets access, not on debt repayment.

---

## 3. Market Risk Profile

| Metric | Value | Comment |
|---|---|---|
| Annualized volatility | **121.3%** | Extraordinary; ~6–8x an index |
| Beta vs SPY | **0.175** | **Not statistically reliable** (see below) |
| Max drawdown | **40.1%** | $53.44 (Aug 11) → $32.03 (Oct 2), **7.5 weeks** |
| Sharpe ratio | 0.96 (0% RF, tool) | ~0.47 restated with 2Y RF 4.65% |

**Data integrity warning:** BSP listed 2026-07-01, so the requested 756-day window silently truncated to **76 trading days**. The 3-year drawdown asked for is not computable. Beta of 0.175 is an artefact of a tiny, wildly idiosyncratic sample — the R² is near zero, so **beta here carries no information and must not be read as downside protection.** With 121% volatility and 76 observations, the standard error on beta swamps the estimate.

What the tape actually shows is **event-driven, gap-risk behaviour**: +41.2% on Oct 14, +24.2% on Oct 7, +25.1% on Aug 5, and −16.2% on Oct 13, −15.6% on Oct 16. (The Oct 14–15 spike plausibly tracks the S&P upgrade to BB-, though I could not verify the date — flagged as unconfirmed.) Singular daily moves of this size mean stop-losses and risk models will not protect a position.

**The dominant market risk is valuation, not volatility.** EV = $29.90bn + $4.17bn = **$34.07bn**, against TTM EBITDA of $854.5M → **EV/EBITDA 39.9x**, EV/EBIT 62.8x, P/S 14.6x. The equity is priced as a high-growth compounder while the capital structure is that of a leveraged buyout roll-up. A de-rating to a still-generous 20x EV/EBITDA implies EV of $17.1bn → **equity ≈ $12.9bn, a −57% drawdown**, with no change in operating performance. That single channel is larger than the credit-driven downside.

---

## 4. Downside Scenario Analysis — Revenue −20%

Applied to TTM revenue of $2,041.8M (severe but not implausible: AOL, Vimeo and Eventbrite are structurally declining legacy assets, and AI-driven substitution is a live threat to consumer software). Cost of revenue treated as variable at 33.5%; fixed opex of $815.4M held flat, then flexed for BSP's aggressive cost-cut playbook.

| | Base (TTM) | −20% revenue, no action | −20% revenue, 12% fixed-cost cut |
|---|---|---|---|
| Revenue | $2,041.8M | $1,633.5M | $1,633.5M |
| Gross profit (66.5%) | $1,357.6M | $1,086.1M | $1,086.1M |
| Fixed opex | $815.4M | $815.4M | $717.5M |
| **EBIT** | $542.3M | **$270.7M** | **$368.5M** |
| EBITDA | $854.5M | $550.9M | $648.7M |
| Interest (run-rate) | $432M | $432M | $432M |
| **EBIT / interest** | 1.26x | **0.63x — fails** | **0.85x — fails** |
| **EBITDA / interest** | 1.98x | 1.28x | 1.50x |
| **Net debt / EBITDA** | 4.87x | **~8.9x — breach** | **~7.6x — breach** |
| FCF | ~$380M | **~$100M** | **~$200M** |
| FCF / interest | 0.88x | 0.23x | 0.46x |

**The finding that matters: a 20% revenue decline breaks EBIT interest coverage outright (0.63x), and even a 12% fixed-cost reduction leaves it at 0.85x.** Only EBITDA covers interest, and no plausible cost action restores an investment-grade cushion. Net leverage goes to 7.6–8.9x — a covenant breach under any conventional 5.0–5.5x maintenance test, which would freeze revolver access precisely when the $761M working-capital deficit needs it most.

**−35% severe case:** EBITDA falls to ~$347M against $432M of interest — **interest is no longer covered by cash generation at all.** Cash of $793M buys roughly 5 years of burn, but the equity would be functionally impaired given −$5.0bn tangible book. This is the true tail: not liquidity failure, but a leverage spiral and a valuation collapse.

**Mitigants:** subscription revenue with high retention; a 66.5% gross margin; demonstrated ability to harvest acquired assets by aggressive cost-cutting; recent and repeated access to capital ($4bn raised in 2025, $2.8bn in Oct 2025, plus the July 2026 IPO); S&P upgrade trajectory; no dividend and no buyback, so all FCF is retained. The yield curve is **not** inverted (2s10s +34bp), so no imminent recession signal — but at 4.65%–5.37% across the curve, refinancing $5.7bn of BB- debt will be expensive.

---

## 5. Overall Financial Risk Rating: **HIGH**

Boundary: credit risk is **High but not Critical** — coverage and liquidity are adequate at current operating levels, and the rating trajectory is positive. Market/valuation risk is **Critical**. Weighted together the equity carries high financial risk with a genuine tail.

---

## 6. Key Red Flags

1. **Leverage is rising, not falling.** Gross debt $2.67bn → $4.96bn in six months; S&P projects **~$5.7bn by YE2026**. The model consumes debt to buy growth — deleveraging is not the plan.
2. **Interest cost compounding far faster than earnings.** +786% since FY2024 vs EBIT +295%. Coverage is 1.88x TTM and ~1.6x on forward run-rate.
3. **−$5.04bn tangible book / 78.2% goodwill.** A single impairment round wipes out the entire $1.26bn of book equity and would likely force a rating downgrade.
4. **Liquidity is revolver-dependent.** Current ratio 0.64x, working capital −$761M, cash covers short-term debt at 0.98x — no buffer.
5. **Thin pro-forma profitability.** Pro forma 2025 net income was only ~$22.4M on a ~$2.9bn revenue base (Forbes); FY2025 net income was effectively zero.
6. **Serial-acquisition opacity.** Revenue doubled through M&A; organic growth is not separable in the reported data, so the durability of the 41.9% EBITDA margin is unverifiable. The acquired assets (AOL, Vimeo, Eventbrite) are structurally challenged.
7. **Valuation risk dominates.** 39.9x EV/EBITDA and 62.8x EV/EBIT on a BB- capital structure — a multiple normalization alone is a −50%+ event.
8. **Gap risk.** Four single-day moves >15% in 76 sessions; max drawdown 40.1% in 7.5 weeks. Beta of 0.175 should be ignored.

---

## Data Gaps (explicitly flagged)

- **Debt maturity ladder unavailable** from tools — cannot assess the refinancing cliff, the single most important credit variable here.
- **Covenant package not disclosed** — I have assumed market-standard 5.0–5.5x maintenance leverage; unverified.
- **3-year price history does not exist** (IPO 2026-07-01). Vol/beta/drawdown rest on **76 trading days**; beta is statistically meaningless.
- **S&P and Forbes pages returned 403**; rating ('BB-', stable, upgraded from 'B+'; ~$5.7bn gross debt YE2026; pro forma net income $22.4M) is sourced from search-result snippets only — one retry attempted, then abandoned.
- No CDS spread or bond-price data; no organic-vs-acquired revenue split; no segment disclosure.
- FY2025 annual ratios (net debt/EBITDA 4.97x, Altman 0.654, F-score 4) are retained for reference but are **superseded** by the TTM/Q2'26 rebuild.
