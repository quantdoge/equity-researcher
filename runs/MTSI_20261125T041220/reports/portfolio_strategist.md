# Portfolio Strategist

- Symbol: MTSI
- Elapsed: 84.0s

---
# PORTFOLIO CONSTRUCTION RECOMMENDATION — MTSI (MACOM Technology Solutions)
**Price $200.20 (24-Nov-26 close) · Mkt cap $15.56B · EV $15.14B · No dividend**
**Peak $409.68 (26-May-26) → −51.1% · 52-wk low $186.59 (5-Nov-26) · Currently 7% off the low**

*Verification pass performed against tool data before synthesis. Three reported claims were corrected (see §0).*

---

## §0. Data Verification Notes (corrections to agent inputs)

| Item | Agent claim | Verified | Consequence |
|---|---|---|---|
| **12-1 momentum** | Quant: **+53.2%** | **−21.9%** (252d, ex-last-21d) | Major. Momentum is *outright negative*, not merely decelerating. Removes the last support for initiating. |
| **Beta** | Profile 1.83 / FinRisk 2.17 / Quant 2.65 | **3.05** (252d vs SPY); vol **79.7%**, max DD **−53.5%**, Sharpe 252d **0.07** | Sizing must use ~3.0, not 1.8. |
| **Customer concentration** | NonFin: "no customer ≥10%"; Short: "Customer A = 20% of FY26, 26% in Q3" | **Unresolved conflict** | I take the conservative read (Short). Highest-priority diligence item. |
| **Macro** | Empty report | **Filled by tool**: 2Y 4.74 / 10Y **5.13** / 30Y 5.47, +39bp, no inversion | High absolute rates = headwind for a 53x-FCF long-duration name. |
| **Valuation confirmed** | — | P/E 46.45, P/B 9.17, EV/EBITDA 33.0, **P/FCF 53.2**, peer median P/E 27.6 → **+68% premium** | Value agent's arithmetic confirmed. |
| **Correlation (252d)** | — | COHR **0.78**, ADI **0.73**, LITE **0.72**, MRVL 0.67, SPY 0.61, AVGO 0.58, NVDA 0.57 | MTSI is an AI-optics **substitute**, not a diversifier. |

---

## §1. Agent Conviction Summary Table

| # | Agent | View | Conviction | Key Finding |
|---|---|---|---|---|
| 1 | **Sector Researcher** | Attractive (narrow) | **Med-High** | DC optics +74% to $509.7M; I&D +27.8%; adj GM 61.3% (from 57.1%); B2B 1.4x. Bifurcated end-market. |
| 2 | **Geo Legal** | **Risk: HIGH** | **High** | China 37.7% of rev (+930bp), 25% §232 tariff with no drawback, Jan-2027 Ga/Ge suspension cliff. Litigation clean. |
| 3 | **Macro Researcher** | *No report* | *n/a* | **Gap.** Backfilled: 10Y 5.13% — a 1.3–1.9% SBC-adj FCF yield is negative-spread to risk-free. |
| 4 | **Value Researcher** | **SELL** | **High** | IV $90–160 (**mid $125**) vs $200. 53x FCF, 33x EV/EBITDA; ROIC only 14.8% *at peak*. Buy zone $95–115. |
| 5 | **Growth Researcher** | **BUY** | **High (12m) / Med (durability)** | FY27 +46% rev, adj EPS $9.80 → **20.4x fwd**, PEG 0.46, Rule of 40 = 59. |
| 6 | **Fin Risk** | **Moderate** | **High** | Credit LOW (net cash $421M, 48x interest, Z 3.23, F 8/9). **Equity risk HIGH.** −20% rev → EBITDA −52%. |
| 7 | **Nonfin Risk** | **Risk: HIGH** | **Med-High** | CEO/Chair duality; **~$355M insider sales, zero open-market buys**; $328.8M purchase commitments ($301.7M ≤12m). |
| 8 | **Quant** | **Neutral 45/100** | **High** | Value 25, Quality 70, LowVol **5/100** (worst in peer set). R² 0.31 → 69% idiosyncratic. Alpha t-stat ≈ 0.4 (insignificant). |
| 9 | **Short Analyst** | **NO EDGE — do not short** | **High** | No fraud: DSRI 1.03, negative accruals, M-score warning is *growth-mechanical*. Bear case = margin reversion → **$87–112**. |
| 10 | **ESG** | **Average** | **Medium** | Clean E/S, G 6/10; no exclusion trigger. China concentration is the real (badly-scored) risk. |
| 11 | **Alt Data** | **Bullish** | **Medium** (3 of 6 feeds failed) | Record backlog, 7% in-quarter turns, +12.9% open reqs, 7-for-7 beats with widening surprise. |
| 12 | **Portfolio Strategist** | **PASS (no new capital)** | **High** | See below. |

---

## §2. Consensus Assessment — **SPLIT on price; UNANIMOUS on risk**

**High agreement (business quality):** #1, #5, #6, #9 all independently confirm the improvement is **real and organic** — goodwill *fell* ($414.9M→$393.6M), accruals negative every year, cash conversion 1.07x, DSO improved 7 days, inventory days fell 13. **The fraud/short case is rejected unanimously.** This matters because it removes the "value-bull vs fraud-flag" scenario where risk would override everything: quality is not the issue.

**Split (the only live debate — and it is the whole debate):** Value says IV $125; Growth says 20x FY27E is cheap. Both are internally correct; they disagree on **whether 60%+ gross margins are permanent or cyclical rent in a 1.6T bottleneck**. That is unresolvable with current data — and Growth itself concedes FY28 consensus decelerates to +19%.

**Unanimous negative (the signal that governs sizing):** **four independent risk agents land on HIGH risk** — Geo (HIGH), Nonfin (HIGH), Fin (equity HIGH), Quant (LowVol 5/100, beta 3.0, −53.5% DD). No risk agent dissents. Simultaneously, the only two bullish agents (#5, #11) both explicitly flag **position-sizing** as the constraint, with Alt Data capping itself at *Medium* confidence on 3-of-6 failed feeds.

**Resolution rule I apply:** when quality passes but four risk agents independently flag high risk and one valuation agent prices a 38% downside to intrinsic value, the risk and price findings govern *entry*, and the growth finding governs only the *watchlist*. Confidence in the demand story ≠ license to pay any price.

**Scenario-weighted expected value (my construction):**

| Case | Prob | FY27 delivery | Multiple | Value | vs $200 |
|---|---|---|---|---|---|
| Bear — capex digestion, GM →54% | 30% | $1.6B rev, ~$4.25 EPS | 25x | **$100** | −50% |
| Value-base — margins partially revert, FCF-anchored | 45% | $1.9B rev, $9.20 EPS | ~19x | **$175** | −13% |
| Bull — everything delivered | 25% | $2.3B (FY28), $11.7 EPS | 25x | **$290** | +45% |

**EV ≈ $181 → −9.5% vs spot**, with a −50%/+45% dispersion at **80% realized volatility**. Kelly fraction on a negative edge = **0%**. You are not being paid for the variance.

---

## §3. Position Sizing Recommendation: **0.0% now — PASS**

| Candidate size | Framework test | Verdict |
|---|---|---|
| 3–5% (high conviction, low risk) | Conviction is *split*; risk is HIGH on four independent tests | **Fails** |
| 1–3% (medium conviction / elevated risk) | EV is negative at spot; momentum negative; 80% vol | **Fails at $200** |
| 0.5–1% "starter" | Would require an entry edge. Price is 60% above Value's IV midpoint | **No edge → no size** |

**Hard sizing ceiling if/when re-underwritten: 3.0% max**, not 5%. Math: at 3% × 80% vol the position contributes **2.4% of standalone portfolio volatility**; at beta 3.0 it imports **0.09 beta units** — the systematic risk of a **9% S&P index position held in a 3% slot**. A 5% position would import 0.15 beta units and 4% standalone vol. That is a portfolio-level risk decision, not a stock decision.

---

## §4. Portfolio Fit Analysis — **Poor, and worse than it looks**

- **Sector/factor concentration:** MTSI's correlation to COHR (0.78), ADI (0.73) and LITE (0.72) means it is a **substitute for AI-optics exposure already held, not a diversifier**. If the book owns any of NVDA/AVGO/MRVL/ADI/LITE/COHR, adding MTSI *increases* the single largest factor exposure in most current equity books (AI datacenter capex) at a moment when that factor just de-rated 8.3% in a session.
- **The correlation trap:** SPY correlation is only 0.61, which screens as "diversifying." It is not. R² = 0.31 → **69% idiosyncratic variance at 80% annualized vol**. That is uncompensated single-stock risk, not diversification — you get the volatility without the offsetting benefit.
- **Factor tilts added:** high beta (+3.0), **negative momentum (−21.9%)**, bottom-quartile value (25/100), worst-decile low-vol (5/100). The only positive contribution is Quality (70/100) — i.e., "expensive quality in a momentum downtrend," the quadrant with the weakest forward 12-month return profile per the Quant agent.
- **Rate/duration:** with the 10Y at **5.13%**, a 1.3% SBC-adjusted FCF yield is a deeply negative spread to risk-free. This name is long-duration; the macro regime is actively hostile to that.
- **Correlated-risk stacking (the non-obvious one):** 37.7% China revenue, 20–26% Customer A, and 38–44% data-centre concentration may all be **the same node** (Short's inference: Customer A is a China-based module vendor shipping to US hyperscalers). If true, a single BIS action or one sourcing change impairs ~a quarter of revenue *and* the growth engine simultaneously. That correlation is not visible in any return matrix.

---

## §5. Entry Strategy — **Wait, then ladder. Do not scale in now.**

Do **not** use a scale-in to average into a name whose expected value is *below* spot; scale-in is a tool for volatile names with a positive edge, and this has neither. Two independent entry paths, whichever triggers first:

**Path A — Valuation ladder (preferred).** Enter only where the good-execution case gets a discount rather than a premium:
- **$145** → initiate **1.0%** (≈15x FY27E, ~2.8% SBC-adj FCF yield)
- **$122** → add to **2.0%** (Value's IV midpoint)
- **$98** → add to **3.0% cap** (Value's stated buy zone, ~4% SBC-adj FCF yield)
- **Do not add on the way down without a fundamental print.** Each tranche requires the prior quarter's data-centre sequential growth ≥5% and GM guide ≥58%.

**Path B — Catalyst entry (priced for optionality).** Post **Q1 FY27 print, 4-Feb-27**. If DC revenue grows ≥20% QoQ (vs ~15% guided) **and** adj GM ≥60% **and** price is ≤$230 → initiate **1.0%**. That converts Alt Data's "tracking above" into a verified fact and buys the durability proof rather than assuming it.

**Explicitly rejected:** buying the 51% drawdown as a mean-reversion trade. Verified 12-1 momentum is **negative**, the stock closed at $200.20 on the last data point after a −13.5% session and printed a lower low at $186.59 nine sessions earlier. There is no technical or valuation floor under this. "Down 51%" is not a thesis.

---

## §6. Risk Management Rules

**Stop-loss (if a position is ever initiated):**
- **Price stop: −20% from entry**, hard. At 80% annualized vol a −20% stop is ~1.6 monthly sigma — it filters noise without tolerating a re-rating to the bear case ($100).
- **Structural stop:** weekly close below **$186.59** (52-wk low) on >1.5x average volume → exit without discretion. Break of the low invalidates the "multiple compression is over" premise.

**Thesis invalidation (exit regardless of price — these fire before the stop):**
1. **Data-centre sequential growth <5% for two consecutive quarters** (the Q4 +37%→Q1 ~+15% deceleration is the template; a second step down ends the story).
2. **Adjusted gross-margin guidance below 58%.** This is the single cleanest tell: 62–63% guided GM with 1,600bp of peer spread leaves zero cushion, and management guided margins *up*.
3. **Any BIS action touching Chinese optical-module customers**, or confirmation that **Customer A is China-domiciled at >20%** — converts a valuation debate into a structural impairment.
4. **Book-to-bill <1.1x** (currently 1.4x Q4 / 1.5x FY26) — the highest-quality forward indicator in the file.
5. **The trio:** purchase commitments rising *while* inventory days tick up *and* DSO extends. Any two of three → cut to zero.
6. **Jan-2027 gallium/germanium suspension lapsing** without replacement → re-underwrite input cost and continuity.

**Trim trigger:** trim 50% at **$228** (≈1.3× my $175 base case; also 30x FY27E); **exit fully above $285–290** unless gross margin has proven durable ≥60% through a full FY28 cycle — that is precisely the level at which the Short analyst re-engages, i.e., the price at which the risk/reward inverts.
**Add-on-confirmation:** a first open-market insider purchase, or a buyback reinstated against the $88M SBC load, would be a genuine positive tell (zero buys currently exist).

---

## §7. FINAL PORTFOLIO ACTION

# **PASS** — do not initiate. For existing holders: **REDUCE / trim into strength.**

**For new capital (0.0%):** The business is genuinely better than the price action suggests — organic growth, real margin expansion, fortress balance sheet, no accounting fraud (unanimously confirmed). But I am asked to construct a *portfolio*, not to admire a franchise. At $200.20 the stock carries a **−9.5% expected value with a −50% left tail**, **verified negative 12-1 momentum**, **80% volatility / beta 3.0**, **four independent HIGH-risk ratings**, a **68% P/E premium to peers**, a **53x P/FCF** against a **5.13% risk-free rate**, and **37.7% China concentration that may be the same node as its largest customer and its fastest-growing segment**. Every one of those is a reason to require a discount; none is a reason to require a premium.

**For existing holders (~1–2% positions):** **Reduce to ≤1.0%** on any rally above $228, and exit above $285–290. Hold the residual only against the explicit invalidation triggers in §6, and hold it knowing the credit is fine — the enterprise does not break; the *equity* does.

**Re-engagement plan:** MTSI goes to the top of the **AI-optics watchlist** with two live triggers — **≤$145 (Path A)** or **Q1 FY27 confirmation at ≤$230 (Path B)** — max **3.0%** on full ladder completion. Review date **4-Feb-2027**.

**What would prove this PASS wrong:** FY27 delivered at ≥$1.94B revenue with adjusted GM ≥60%, data-centre growth ~80%, and the multiple holding 25x forward — that is ≈$245 (+22%). It is a real outcome and I may well forgo it. But it requires the demand curve, the margin peak, the China channel, and the multiple to *all* hold simultaneously, and I am being asked to pay for all four today with a stop that sits only 20% away and a bear case 50% below. **Passing on a 22% upside to avoid a 50% downside, with no momentum support and a negative expected value, is the sizing decision — not a view on MACOM's technology.**

---
*Gaps declared: Macro specialist report was empty (10Y 5.13% backfilled from tool). Customer A identity and the 10-K customer-concentration language conflict unresolved. Convertible-note indenture/capped-call terms unavailable. Net-debt figure inconsistent across sources ($259.2M reported vs −$421.2M computed; I use net cash, corroborated by the leverage tool). Insider-sale dollar totals are third-party aggregates, not reconciled to Form 4 line items. FY29–30 consensus rests on a single analyst.*
