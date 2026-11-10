# Portfolio Strategist

- Symbol: AKAM
- Elapsed: 38.5s

---
# AKAM — Portfolio Construction Recommendation

**Verified reference data (Nov 9, 2026 close): $80.29.** Market cap ~$11.6B (144.2M sh). 52-wk range **$77.37–$165.45** (high May 13, 2026). Realised 252d vol **68.3%**, beta vs SPY **1.49**, max drawdown **51.7%**, Sharpe **−0.02**, 12-1 momentum **−11.75%**. I re-verified the price series directly — the Short Analyst's ~$122 quote is stale (that was the Sep 25 level) and the Quant Analyst's "re-based 37% vol" is wrong; the raw OHLC series (eight >10% single-day moves in 12 months, incl. +26.6% on 5/8 and −16.7% on 4/10) confirms the 68%/52% figures. **Every conclusion below uses $80.29.**

---

## 1. Agent Conviction Summary Table

| Agent | View | Conviction | Key Finding |
|---|---|---|---|
| **Value** | Sell / Avoid | **High** | IV $45–65 (base $55) vs $80.29. ROIC 5.3% < WACC for 3 straight yrs. SBC $526M > net income. ~$4B of buybacks destroyed. |
| **Fin Risk** | High risk | **High** | Net debt/EBITDA 4.26x → **6.70x**; FY26E FCF **−$2.0B**; Altman Z 1.71 (distress boundary); lender cut secured basket 10%→3.5%. |
| **Non-Fin Risk** | High risk | Med-High | Single-counterparty concentration; **zero insider buys through a 53% drawdown**; Anthropic MSA DPA unexecuted at signing; no CEO succession. |
| **Short** | Short (not strong) | Medium | **No fraud** (Beneish −2.80, accruals −0.093). Business-model/capital-allocation problem. *Uses stale $122 price — bear case overstated relative to spot.* |
| **Growth** | Hold | Med-High | $14B signed CIS book vs $11.6B cap; **+80% bull / −30% bear**. Needs Q4'26 capex landing + CIS ≥$275M/qtr to become Buy. |
| **Quant** | Neutral, tilt Sell | Medium | "Cheap and broken." #1 of 3 on value (13x EV/EBITDA), **#3 on momentum and quality**. Value-trap signature. |
| **Sector** | Neutral | Medium | Slowest grower (−9.1pp vs peer median) and lowest GM (−24.1pp) in the competitive set, though one of few GAAP-profitable. |
| **Geo/Legal** | Medium risk | Medium | Clean litigation, no Russia/China, no country >10%. Risk is *direction of travel*: EU CADA, BB+ downgrade, $11.6B single counterparty + 5% warrant. |
| **Macro** | Neutral (mild −) | Medium | ~**80% idiosyncratic**, 20% macro. FX −3.2% USD, 5.13% 10Y caps multiple. Bull = disinflation → $100–110. |
| **Alt Data** | Neutral/bearish | Medium | Trends −32% QoQ, Stocktwits −67%; contracts intact but *narrative has fully unwound*. Market stopped paying for beats (Q3 beat, −9.4%). |
| **ESG** | Average, neg. momentum | Low-Med | Carbon intensity **+37%**, clean-energy share −7pp, PUE 1.48 → 2030 target regressing 47%→42%. Neutral to the thesis. |
| **Sector/Consensus** | **Split** | — | Unanimous on *facts*; split on *price implication*. |

---

## 2. Consensus Assessment: **SPLIT** — but the split is shallower than it looks

**High agreement on the facts (10 of 11 agents):** gross margin 63.3%→54.7%; ROIC 9.0%→5.3%; FCF +$699M (FY25) → **−$2.0B (FY26E)**; net debt ~$8.3B; S&P **BB+**; SBC ~12% of revenue; delivery shrinking 3–7%/yr; the growth plan rests on one counterparty.

**The genuine disagreement is narrow and resolvable:**
- *Bear camp* (Value, Short, Fin Risk, Quant): the deterioration is structural and the price still doesn't discount it.
- *Bull camp* (Growth, Macro bull scenario, Alt Data's "contracts intact"): the market assigns ~zero value to a $14B signed book; 3.6x EV/2027E revenue is an option, not a valuation.

**Conflict resolutions I am imposing:**
1. **Value over Growth on intrinsic value.** Growth's $145 requires *both* flawless execution *and* a 15x re-rating. Value's $55 base expenses SBC and prices Anthropic at cost of capital — management itself concedes this deal carries the **lowest-return pricing in the book (~15% ROIC)**. The default valuation is Value's; Growth's number is the option payoff, not the base case.
2. **Short Analyst down-weighted on price.** Its bear multiple math (37x FCF, 108x owner earnings) was struck at $122. At $80.29 EV is ~$19–20B, i.e. **~28x FY25 FCF and ~83x owner earnings** — still unacceptable, but roughly 30% of the bear case has *already been paid out*. This is the single biggest correction in the file.
3. **Quant's risk statistics corrected upward, not downward.** 68% vol / 1.49 beta / 52% drawdown are real. This *tightens* sizing.
4. **Macro deferred.** A disinflation-driven multiple re-rating is a market call, not an AKAM edge. We do not size a single-name position on a Fed forecast.
5. **Non-Fin Risk's DPA finding escalated.** An $11.6B AI-workload MSA effective with privacy terms *still to be negotiated* is a live GDPR/CCPA and enterprise-contract exposure that no agent elsewhere flagged.

**Net: conviction on the fundamentals is HIGH and bearish; conviction on the price path is LOW. Under the framework, that combination is a sizing problem, not a buy signal.**

---

## 3. Position Sizing Recommendation: **0% — PASS at $80.29**

**Kelly check (base-case probabilities: 25% bull $145 / 45% grind ~$85 / 30% bear $55):**
- At **$80.29**: EV = 0.25(+81%) + 0.45(+6%) + 0.30(−32%) = **+8.5%**, with 68% vol and a 2.4:1 payoff. Kelly f* = (pb−q)/b = (0.25×2.53 − 0.75)/2.53 = **−0.05 → negative. Zero allocation.**
- At **$65**: EV = 0.25(+123%) + 0.45(+31%) + 0.30(−15%) = **+40%**; Kelly f* ≈ 0.16 → quarter-Kelly ≈ **4%**. Full 2–3% starter justified.

**Therefore the sizing ladder is price-and-proof conditional:**

| Condition | Position |
|---|---|
| **Today, $80.29** | **0%** |
| Mandate *requires* AI-infra/AKAM tracking exposure | **0.25–0.50%** maximum, hard-stopped, treated as a tracking position not an investment |
| Price ≤ **$65** *with* Q4'26 capex inside guidance and no new equity raise | **1.5%** |
| Price ≤ $65 **and** CIS ≥$275M in a quarter **and** GM stabilised ≥54% | **2.5–3.0%** |
| Price ≤ $55 (base-case IV) with credit outlook stable | **3.5–4.0%** |
| Q4'26 (Feb 18, 2027) delivers capex ≤$3.66B, CIS on track, margin trough confirmed | **1.0–1.5%** even at $85–95 — pay up for de-risked evidence, not for narrative |

**Why not even a small position now:** the sizing framework says "low conviction or multiple risk flags → 0.5–1% or pass." AKAM has **four independent HIGH-risk ratings** (Financial, Non-Financial, credit, and 68% realised vol). At a 68% vol / 1.49 beta, a 1% position contributes **0.68% of standalone portfolio volatility** and roughly **0.6x the risk budget of a 2% position in a normal 35%-vol tech name**. Limited partners are not paid for a 0.25% position in a junk-rated single-counterparty capex vehicle; the research cost is sunk either way, and optionality is better acquired *after* the Feb 2027 print when the binary resolves.

---

## 4. Portfolio Fit Analysis

**Measured correlations (252d, verified):** SPY **0.31** · XLK **0.42** · MSFT **0.16** · NET **0.29** · FSLY **0.55**.

- **Sector concentration:** *Neutral-to-positive.* AKAM is Technology, but its 0.42 correlation to XLK and 0.16 to MSFT mean it is **not redundant tech beta**. It would not materially increase a book's effective tech factor exposure.
- **Correlation:** *Positive.* Lowest-correlation positioning in a year where R² vs SPY is only ~0.10 — ~90% idiosyncratic. Genuine diversification of *return source*.
- **Factor exposure:** *Negative.* AKAM loads **positively on value** (13x EV/EBITDA, #1 in peer set) and **deeply negatively on momentum (−11.75%, #3 of 3) and quality (ROIC 5.3%, #3 of 3)**. Adding it tilts the book toward "cheap and deteriorating." If the portfolio already holds value/contrarian or cyclical-recovery names, this **compounds an existing factor bet** — the highest-risk form of concentration.
- **Hidden factor: it is a credit instrument in equity clothing.** ~$9.5–11B gross debt, BB+, negative FCF, one counterparty. With IG OAS at **93bp** (tight: 74bp in June), AKAM is a **short-volatility/short-credit-spread position**. Credit widening hits it far harder than equity beta implies. Any portfolio already carrying AI-capex or leveraged-infrastructure exposure is doubling that bet.
- **Liquidity:** ~1.5M sh/day, ~$130M notional — no capacity constraint, but note the *exit* liquidity is asymmetric: 16.2M shares traded on Nov 9 (10x normal) on a −3% day.

**Verdict: acceptable diversifier on correlation alone; unacceptable on factor and credit-fit given it adds a leveraged AI-capex bet with negative momentum and negative quality at a price with no margin of safety.**

---

## 5. Entry Strategy: **Scale-in only — never all at once**

The stock has eight >10% single-day moves in twelve months and gapped −9.4% on a *beat*. Market-order execution is a donation. **Do not initiate at $80.29.** The pre-committed plan:

- **Tranche 1 (0.75%):** only at **≤$65** *or* after Feb 18, 2027 if capex lands ≤$3.66B AND no equity raise AND CIS ≥$275M annualised run-rate.
- **Tranche 2 (0.75–1.0%):** GM stabilises ≥54% for two consecutive quarters with CIS still ≥30% growth.
- **Tranche 3 (1.0%):** credit stabilises — outlook revised from negative, or net debt/EBITDA <5.0x.
- Use limit orders across 3–5 sessions; avoid the two weeks bracketing an earnings date.
- **If neither the price nor the proof condition triggers by Q1 2028, close the watchlist item.** Do not let a "potential" position drift into a narrative holding.

---

## 6. Risk Management Rules

**Hard stop (price):** closing basis **$68.00** — ~15% below spot and just under the 12-month closing low of $71.97. Given 4.3% daily σ, intraday stops are noise; use weekly closes.

**Thesis invalidation (any one → exit regardless of price):**
1. **Q4'26 capex outside $3.46–3.66B, or any equity/common issuance** (converts at distressed terms count).
2. **Any Anthropic deferral, capacity re-pricing, or renegotiation disclosure** — this alone is ~100% of the growth story and the ~$5.5B of purpose-built capex.
3. **CIS revenue below $250M in any quarter of 2027** (vs the $275–325M/qtr needed for the $1.1–1.3B guide).
4. **Second downgrade (B+ or below) or a further secured-basket cut.**
5. **Gross margin below 53%** — the floor has not yet been found and this is the cleanest read on whether the pivot is margin-dilutive or margin-accretive.
6. **Security revenue growth below +5%** — the last durable franchise funding the build.

**Trim trigger:** reduce by half at **$110** and exit entirely at **$120–130**. That band is ~11x 2029 bull-case EBITDA and 2.2–2.4x base-case IV. On a name we cannot underwrite, capture the option value rather than riding a narrative we don't believe.

**Monitoring (quarterly):** net debt/EBITDA (currently 6.70x, target <5.0x); FCF (currently −$2.0B annualising); the unexecuted Anthropic DPA; any insider open-market **purchase** (zero in 12 months, 12 sales ~$8.2M — a single CFO or CEO buy through this drawdown would be a genuine signal).

---

## 7. Final Portfolio Action: **PASS**

**No position at $80.29.** Place AKAM on the watchlist with a pre-committed, written entry ladder at **≤$65 or post-Q4'26 proof**, and a hard invalidation checklist.

**The one-paragraph case:** AKAM is a narrow-moat, formerly asset-light CDN/security business that has become a **junk-rated (BB+), negative-free-cash-flow, single-counterparty AI datacenter landlord** — funded with $5.5B of debt and a 5% equity warrant — while its legacy delivery business shrinks 3–7% a year and ROIC (5.3%) sits below its cost of capital for a third consecutive year. That is a genuine business-model problem, not a fraud, and markets can tolerate those far longer than the bears expect. The offsetting truth is equally real: **$14B of signed contractual commitments against an $11.6B market cap and 3.6x 2027E revenue means the market is paying almost nothing for the option**, and a fast disinflation could re-rate the multiple 25% on an unchanged fundamental story. But you cannot size a position on a macro call for a company with one customer, no free cash flow, and three downgrades — and at $80.29 the Kelly arithmetic is *negative*. The asymmetry becomes payable at $65, and the proof arrives on **February 18, 2027**. We wait for one or the other. **Patience is the position; capital is preserved for the point where conviction and price agree.**

---

**Data gaps to disclose in the memo:** (1) Net debt/EV is contested across agents — $8.30B net debt (Q3'26) vs Growth's $16–17B EV and Quant's $17.5B EV; I use **~$19–20B EV** to include the Nov 2026 converts, and flag a $16–20B range. (2) Convertible issuance is reported inconsistently ($2.2B Nov 2026 vs $3.5B May 2026 vs $2.6B upsized) — confirm against the 10-K. (3) No peer valuation multiples exist in the toolkit (FMP sector endpoint returned mega-caps only), so all relative-value work is peer-median growth/margin construction, not multiples. (4) Sortino, CDS spreads, and full debt-maturity ladder unavailable. (5) 10-K risk factors and DEF 14A text returned 403s across three agents; chair/CEO separation is unconfirmed.
