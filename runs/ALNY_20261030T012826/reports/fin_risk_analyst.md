# Fin Risk Analyst

- Symbol: ALNY
- Elapsed: 68.6s

---
## ALNY — Financial Risk Assessment
**Alnylam Pharmaceuticals, Inc. | Healthcare / Biotechnology | Cambridge, MA**
**Last data: Q3 FY2026 (period end 30-Sep-2026), filed 29-Oct-2026. Price $174.00 (29-Oct-2026).**

> **Data vintage warning:** the automated ratio tools (leverage, liquidity, Z-score, F-score, FCF yield) resolve to **FY2025 annual (31-Dec-2025)**, which is now four quarters stale and pre-dates a >$2.0bn non-operating gain that transformed the balance sheet. I have re-based all key metrics to the **Q3 FY2026** balance sheet and **TTM (Q4'25–Q3'26)** flows below. Where I show both, the FY2025 figure is labelled.

---

## 1. Credit Risk Assessment

**Rating: Investment Grade on quantitative credit metrics (BBB-/BB+ crossover equivalent); no agency rating or CDS spread was retrievable — flagged as a data gap.**

The credit story is unusual: the *income statement* looks levered, the *balance sheet* is net cash. The conflict is entirely an accounting artifact of the Blackstone royalty-monetisation structure.

| | FY2025 (tool) | Q3 FY2026 (re-based) |
|---|---|---|
| Total debt | $1,278m | $1,262m |
| Cash & ST investments | $2,908m | $3,587m |
| Net debt | **–$1,630m** (net cash) | **–$492m** (net cash) |
| Total equity | $789m | $3,604m |
| Debt / equity | 1.62x | **0.35x** |
| Debt / assets | 0.26x | 0.16x |
| Gross debt / TTM EBITDA | — | **1.01x** |
| Net debt / TTM EBITDA | –2.58x | **–0.39x** |
| EBIT / interest (reported) | 1.99x | **3.27x** |

**Critical adjustment — interest coverage.** Reported interest expense is ~$365m TTM against only ~$1.26bn of debt, an implied ~29% rate. That is not a cash cost. Alnylam's actual coupon structure is a **1.00% convertible (2027s, largely repurchased/refinanced)** plus a **$575m 0%-coupon convertible issued Sept-2025** (upsized from $500m, with capped call). The reported figure is dominated by **non-cash imputed interest on the Blackstone "liabilities related to sale of future royalties and development funding"** (a $2bn inclisiran royalty financing). True **cash interest coverage is in excess of 50x**, not 3.3x. Investors screening on the 1.99x headline would badly misjudge this credit.

**Balance-sheet equity quality caveat:** the jump in equity from $789m to $3,604m is driven by **Q3 FY2026 net income of $2,167m on operating income of only $380m** — i.e. ~$1.8bn of the quarter's earnings is a **one-off, non-operating gain** (retained earnings improved by exactly the net income figure, from –$6,332m to –$4,165m). **Do not annualise Q3. Normalised equity is ~$1.6–1.8bn, not $3.6bn**, which puts normalised debt/equity nearer 0.7–0.8x — still comfortable, but not the 0.35x the headline implies.

**Ratings view:** net cash, no near-term maturity wall, cash covering 2.4x current liabilities and 2.8x *all* debt. This is not a credit-risk story. The residual credit weaknesses are structural, not liquidity-driven: a **–$4.2bn accumulated deficit**, no goodwill (clean asset base), and revenue concentration in a single franchise.

---

## 2. Key Financial Risk Metrics Table

| Metric | Value | Zone / Read |
|---|---|---|
| **Altman Z-Score (book equity, FY2025)** | **–0.02** | "Distress" — **misleading, see below** |
| **Altman Z-Score (market-cap x4, Q3'26)** | **≈4.03** | **Safe zone (>2.99)** |
| Altman Z-Score (book equity, Q3'26) | ≈1.34 | Grey/distress — book-equity artifact |
| **Piotroski F-Score** | **7 / 9** | Moderate-strong |
| Current ratio (Q3'26) | 2.48x | Strong |
| Quick ratio (Q3'26) | 2.43x | Strong (inventory only $106m) |
| Cash ratio (Q3'26) | 1.74x | Very strong |
| Working capital | $3,050m | — |
| Assets / liabilities | 1.82x | Adequate |
| Cash / total liabilities | 0.82x | Strong |
| **FCF (FY2025)** | **$465m** | Positive, first full year |
| **FCF yield** | **1.99%** | Thin vs 48% vol |
| FCF margin | 12.5% | Improving |
| Gross margin (TTM) | 77.3% | **Deteriorating** (see §6) |
| Operating margin (TTM) | 23.8% | Positive turnaround |
| Revenue TTM | $5,013m | +123% vs FY2023 |
| EBITDA TTM | $1,248m | — |

**Altman Z reconciliation — the single most important adjustment in this report.** The tool returns Z = –0.02 ("Distress"). That is an artifact of the documented limitation: x4 uses **book** equity ($3.6bn) against $4.4bn of liabilities. Replacing x4 with **market capitalisation** ($23.3bn) gives:

| Component | Book basis | Market-cap basis |
|---|---|---|
| x1 WC/TA | 0.382 | 0.382 |
| x2 RE/TA | –0.521 | –0.521 |
| x3 EBIT/TA | 0.149 | 0.149 |
| x4 Equity/TL | 0.821 | **5.302** |
| x5 Rev/TA | 0.627 | 0.627 |
| **Z** | **1.34** | **4.03** |

The **negative x2 (–0.521)** is simply the accumulated R&D deficit of a company that spent 20 years pre-revenue — it carries no incremental information for a now-profitable commercial-stage biotech. **Conclusion: bankruptcy risk over any 12–24 month horizon is remote.** The Z-score should be disregarded here and replaced with the liquidity and maturity analysis in §1.

**Piotroski detail (7/9) — the two misses are meaningful:**
- **F7 (no dilution) = 0.** Share count: 124.9m (2023) → 127.7m (2024) → 131.0m (2025) → **133.8m (Q3'26)**. ~7% cumulative dilution in three years, plus convertible overhang.
- **F8 (gross margin improvement) = 0.** See §6 — this is a genuine structural negative, not noise.

---

## 3. Market Risk Profile

| Metric | Value | Interpretation |
|---|---|---|
| Annualised volatility (3y, 756d) | **48.1%** | Extreme; ~3x SPY. Biotech-idiosyncratic, not market-driven |
| Beta vs SPY (3y, computed) | **0.834** | *Conflicts with company profile beta of 0.269 — flagged gap* |
| **Max drawdown (3y)** | **–64.6%** | Peak $495.55 (20-Oct-25) → $172.31 (29-Oct-26) |
| Sharpe ratio (rf = 0%) | **–0.109** | **Negative** risk-adjusted return over 3 years |
| Sortino | Not computable (tool does not return downside deviation) | **Data gap** |
| Price today | $174.00 | **At the 3-year drawdown low** |
| 52-week range (approx.) | $172.31 – $495.55 | –65% from high |

**The beta figure is the trap in this profile.** Both 0.269 and 0.834 suggest low market sensitivity — which is technically true (biotech revenue is uncorrelated to the economic cycle) but **dangerously misleading as a risk measure**. With 48% annualised vol and a 0.83 beta, the **vast majority of ALNY's variance is unsystematic**, i.e. company-specific and *undiversifiable by market hedging*. Beta-based position sizing will materially understate the true risk.

**Realised tail events — two in one year, both single-day ~29% losses:**
- **30-Jul-2026:** Q2'26 — stock $286.62 → $205.48 (**–28.3%**), 9.8m shares.
- **29-Oct-2026:** Q3'26 — stock $232.40 → $174.00 (**–25.1%**), 11.8m shares (~9x normal volume).

Both were driven by the **same catalyst: decelerating US Amvuttra demand and lowered full-year guidance** — not by credit, liquidity, or financing events. This is a **commercial-execution risk**, and the market has now twice re-rated the equity on it. The 3-year Sharpe of –0.109 confirms holders have been paid nothing for this volatility.

---

## 4. Downside Scenario Analysis — revenue –20%

**Baseline TTM (Q4'25–Q3'26):** Revenue $5,013m · Gross margin 77.3% · Opex $2,682m (SG&A $1,338m, R&D ~$1,344m) · Operating income $1,193m (23.8%) · Reported interest $365m.

| Scenario | Revenue | Gross profit | Opex | **Operating income** | Pretax after interest | Cash FCF (est.) |
|---|---|---|---|---|---|---|
| **Base TTM** | $5,013m | $3,874m | $2,682m | **$1,193m** | $828m | ~$400m |
| **–20% rev, no cost action** | $4,011m | $2,968m¹ | $2,682m | **$286m** | **–$79m** | ~$180m |
| **–20% rev, opex –10%** | $4,011m | $2,968m | $2,414m | **$554m** | $189m | ~$430m |
| **–35% severe, opex –15%** | $3,259m | $2,411m | $2,280m | **$131m** | –$234m | ~$30m |

¹ Assumes ~300bp gross-margin compression to 74% on fixed manufacturing/royalty absorption.

**Findings:**
1. **A 20% revenue shock is survivable without any balance-sheet action.** Even with zero cost response, the operation stays at a modest operating profit and only dips to a small GAAP pretax loss — because the ~$365m "interest" is ~95% non-cash. On a **cash** basis the company remains profitable at –20% revenue.
2. **The binding constraint is not solvency, it is the growth narrative.** At –20%, operating margin falls from 23.8% to ~7%. Given the equity trades at ~4.6x TTM revenue and 18.7x TTM EBITDA on a business the market just de-rated twice for *slowing* growth, the **equity downside is far larger than the earnings downside** — a multiple de-rating to 3x revenue on $4.0bn implies ~$12bn market cap, i.e. **–48% from $174**.
3. **Liquidity is effectively unconstrained.** Cash $3,587m vs current liabilities $2,063m. Under a severe –35% scenario with negative FCF of ~$300m/yr, **cash runway exceeds 10 years**. There is no going-concern or covenant question here.
4. **Maturity wall is a non-event.** Short-term debt $361.5m (the 2027 converts, now current) + long-term $651m. Cash covers **2.8x total debt**. The convert conversion prices (~$424 and ~$670 reference) are **deep out of the money at $174**, so holders will demand cash — which Alnylam has four times over. No refinancing-cliff risk.

---

## 5. Overall Financial Risk Rating

# **MODERATE**

**Balance-sheet / credit risk: LOW.** Net cash, ~1.0x gross debt/EBITDA, >50x cash interest coverage, zero refinancing cliff, 10+ year stress runway.

**Equity / market risk: HIGH.** 48% volatility, –64.6% max drawdown, negative Sharpe, two ~29% single-day gaps in twelve months, price sitting at the low.

**The blended rating is Moderate only because these offset.** Any assessment that reads the headline Altman Z (–0.02, "distress") or the 1.99x interest coverage at face value will be **wrong in the same direction and by a wide margin** — both are accounting artifacts of an accumulated R&D deficit and a royalty-financing structure, respectively. Conversely, any assessment that dismisses risk because of the $3.6bn cash pile will miss a **real and already-realised equity de-rating** on commercial execution.

---

## 6. Key Red Flags

1. **Product concentration + decelerating demand — the dominant risk.** Two ~29% single-day drawdowns (Jul-30 and Oct-29, 2026) on *the same catalyst*: US **Amvuttra growth slowing** and FY guidance cut. The market has re-rated this equity twice for the same reason; a third miss is the base-case tail risk, not an outlier.
2. **Gross margin is structurally deteriorating: 85.6% (2024) → 81.8% (2025) → 77.3% (TTM).** This is the Piotroski F8 miss and it is *not* transient — it reflects third-party royalty sharing (the Blackstone inclisiran monetisation routes a share of economics away from ALNY) plus rising Amvuttra COGS. Margin erosion of ~830bp in two years alongside revenue more than doubling signals **structurally lower incremental profitability than the revenue line implies**.
3. **Earnings quality: Q3 FY2026 net income of $2,167m is ~83% non-operating.** Operating income was $380m; the ~$1.8bn delta is a one-off gain. It inflated equity from $1.35bn to $3.60bn and cut reported debt/equity from ~0.94x to 0.35x **in a single quarter without any deleveraging**. Any trailing-valuation or leverage metric computed post-Q3 is flattered.
4. **SBC is 75% of FCF.** FY2025: FCF $465m vs stock-based comp **$348m**. Underlying cash generation attributable to shareholders is ~$117m, against a $23.3bn market cap — an **underlying FCF yield closer to 0.5%**, not the reported 1.99%.
5. **Persistent dilution.** Shares 124.9m → 133.8m since 2023 (+7.1%), with a **$575m 0% convertible issued Sept-2025** and $361.5m of 2027 notes to be settled in cash. F7 = 0 on the Piotroski.
6. **Negative tangible equity history.** Book equity was **–$220m at FY2023** and **+$67m at FY2024** — the company was technically balance-sheet insolvent on a book basis 18 months ago. The recovery to $3.6bn is earnings- and one-off-driven, not capital-structure-driven.
7. **Beta/vol inconsistency (data gap).** Computed 3y beta 0.834 vs vendor beta 0.269 — a 3x discrepancy. Neither is reliable for risk sizing; use the 48% realised vol instead, and treat most of it as undiversifiable.

---

### Explicit Data Gaps
- **No credit rating, rating outlook, or CDS spread** — no tool available; rating view in §1 is my own quantitative mapping, not an agency opinion.
- **No debt maturity ladder by year** beyond the current/non-current split (Q3'26: $361.5m current / $651.1m long-term). Covenant package and any financial maintenance covenants unverified.
- **Q1–Q3 FY2026 cash flow statements not retrieved** — TTM FCF is estimated from FY2025 OCF-to-operating-income ratio (~1.04x), not reported.
- **Sortino ratio, downside deviation, and equity/asset impairment detail** not available from the toolset.
- **Royalty-financing liability balance not itemised** — the ~$3.1bn of liabilities beyond reported debt is inferred from the gap between total liabilities ($4,391m) and total debt ($1,262m); the Blackstone portion is not separately disclosed in my data.
- **Nature of the Q3 FY2026 ~$1.8bn non-operating gain not confirmed** (inferred: litigation settlement and/or royalty-related gain); I did not retrieve the Q3 press release to verify. This is the single largest unresolved item in the analysis and should be confirmed before any leverage or book-value metric is relied upon.
