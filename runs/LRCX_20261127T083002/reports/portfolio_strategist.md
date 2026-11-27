# Portfolio Strategist

- Symbol: LRCX
- Elapsed: 48.4s

---
# PORTFOLIO CONSTRUCTION RECOMMENDATION — LRCX
### Lam Research Corporation | Semiconductors / WFE | Price $185.01 (25-Nov-2026) | Mkt cap ~$233B

---

## ⚠️ 0. Cross-Cutting Data Integrity Finding (read before the table)

Three agents built conclusions on a **stale price feed**. I re-verified against raw OHLCV:

| Claim | Agent | Verified |
|---|---|---|
| "Price $185.01 is stale; working ref ~$250" | Value | ❌ **Rejected.** $185.01 is the actual 25-Nov close |
| "Current price $289.89" | Quant | ❌ **Rejected.** That is the 1-Sep close; series ended early |
| "+201% 12-1 momentum, Sharpe +2.5, α +127%" | Quant | ❌ **Invalid.** Re-derived from stale data |
| Beta 3.29 / vol 75.2% / DD −57.7% | Quant, Fin Risk | ✅ **Confirmed** on 252d window |
| $185.01 / 32.1x trailing / FY26 EPS $5.76 | Vendor ratios | ✅ **Confirmed** |

**Consequence: the Quant Analyst's sector-#1 "strong positive momentum" signal is inverted.** True 12-1 momentum is *deeply negative* — the stock is **−57% from its 30-Jun peak of $432.87**. I am reassigning Quant from NEUTRAL to **CAUTIOUS**. Had I accepted the report at face value, this would have been sized as a momentum-confirmed quality compounder. It is the opposite.

---

## 1. Agent Conviction Summary

| Agent | View | Conviction | Key Finding |
|---|---|---|---|
| **Sector Researcher** | Constructive | **Med-High** | Sector ATTRACTIVE, position STRONG; #1 growth in group (+26.0% vs +18.5% median), GM +587bp. But "falling knife for a momentum investor" |
| **Geo Legal** | Negative | **High** | China 33.8% FY26 / **35% of Sep-Q** — highest of US WFE peers. MATCH Act ~65% within 12mo; 56% Greater China revenue, only 6.6% US. Rating **HIGH** |
| **Macro** | Negative | **High** | Fed hiking into 3.3% core PCE; 10Y real +59bp → 2.79%; bear steepener; 25% §232 equipment tariff. Rating **UNFAVOURABLE** |
| **Value** | Quality YES / Price NO | **Med** *(truncated)* | Moat **WIDE & widening** (GM 44.6→50.5%, ROIC 49.4%); "no margin of safety at every price tested" |
| **Growth** | BUY (not Strong Buy) | **Med-High** | 19.2x FY27 / 15.3x FY28 for +52% revenue; 1.8:1 upside:downside; explicitly recommends **half-position + dry powder** |
| **Fin Risk** | Solvency LOW / Mkt HIGH | **High** | Net cash $3.7B, 0.47x gross leverage, Altman 5.40, Piotroski 8/9, S&P 'A' (upgraded). Survives −35% revenue |
| **Nonfin Risk** | Negative | **High** | **$135M insider sales, ZERO purchases**; ~$83M at $335–390 just before the −58% move. $25B buyback at cyclical peak. Rating **HIGH** |
| **Quant** | NEUTRAL → **CAUTIOUS** (revised) | **Low** | Stale-feed artifacts. Verified: β3.29, 75% vol, −57.7% DD, negative trend, worst low-vol score in group |
| **Short Analyst** | **NO EDGE** | **Med-High** | Fraud case **rejected**: Beneish M-score is a false positive (one reversal DSO event), deferred revenue *rising*, inventory days *falling* |
| **ESG** | Leader / tail-risk | **Low relevance** | Carbon <0.1% of revenue; export controls are the only material ESG-adjacent factor, already partly priced |
| **Alt Data** | NEUTRAL | **Medium** | Demand signals intact (hiring steady, NAND +40% q/q); attention collapsed −50%+. **Policy-driven, not demand-driven de-rating** |

---

## 2. Consensus Assessment: **SPLIT — but cleanly separable**

The disagreement is not noise; it splits on a well-defined line:

**Near-unanimous BULLISH on the business:** Sector, Growth, Value (on quality), Fin Risk, Short Analyst, Alt Data. No agent found fraud, accounting irregularity, solvency stress, or competitive erosion. The Short Analyst — whose job was to find fraud — **explicitly rejected the bear case** and called residual short risk/reward poor. That is the single most valuable non-consensus input in the pack.

**Near-unanimous BEARISH on policy, macro and price:** Geo Legal, Nonfin Risk, Macro, ESG — four agents working independently converge on **the same risk: China export controls on ~35% of revenue**. Under my conflict-resolution framework, a risk that four independent specialists confirm outranks a bullish fundamental view. Macro adds a separate but reinforcing channel (discount-rate compression on a 2.0–3.3 beta name).

**Resolution:** Business quality is not in dispute — it is verified and improving. The **downside is policy and multiple, not franchise impairment.** That distinction is what allows a position at all rather than a pass, and simultaneously caps its size.

---

## 3. Position Sizing Recommendation: **1.5% of portfolio** (max 2.5%)

**Not 3–5%**, despite genuine fundamental strength, because:

| Constraint | Evidence |
|---|---|
| Binary policy tail | 65% probability of legislated China restriction on 35% of revenue; ~$2.0–2.5B/yr hit in a 2023-repeat, ~$7–8B in a broad ban |
| Hostile macro | Real yields +59bp; multiple *compressing while estimates rise* |
| Risk budget | 75% vol × 1.5% = **~1.1% portfolio vol contribution ≈ 9% of total risk** for a 12%-vol portfolio. At 3% it becomes ~19% — unacceptable for a name correlating 0.93 with three others |
| Broken signal | Negative 12-1 momentum, insider distribution, β 2.0–3.3 |
| Valuation honest check | **"Cheap" only on peak-cycle EPS.** Normalized mid-cycle (~$8.50 EPS @ 45% GM / 30% OM) at 20x = **~$170** — *below today's price*. The 15.3x FY28E case requires the memory cycle to hold through 2028 |

**Kelly cross-check:** b ≈ 1.8 (upside +57% to $291 / downside −31% to $127), p ≈ 0.50 given the 65% legislative probability → full Kelly ≈ 22%, quarter-Kelly ≈ 5.5%. Kelly says the edge is real; the **fat, unmodelable left tail** and the correlation cluster bind first. **Risk budget governs, not Kelly.**

**Scaled build plan:** 1.5% now → 2.5% ceiling only on catalyst confirmation (§5). This is a **"half-position" in Growth's language, expressed in portfolio terms.**

---

## 4. Portfolio Fit Analysis: **the decisive constraint**

**Correlation matrix (252d) — this is the finding that matters most:**

| | LRCX | AMAT | KLAC | ASML | TSM | NVDA | SPY |
|---|---|---|---|---|---|---|---|
| **LRCX** | 1.00 | **0.933** | **0.901** | **0.878** | 0.803 | 0.553 | 0.699 |

- **LRCX is not a position — it is a duplicate of any WFE holding you already own.** 0.93 with AMAT means buying LRCX alongside AMAT adds ~zero diversification and pure leverage. **If the portfolio already holds AMAT, KLAC, or ASML at target weight, the correct action is PASS or an explicit swap** — not an add.
- **Genuine diversifier only against NVDA** (0.55). A portfolio that is NVDA-heavy and WFE-light is the one book where this fits cleanly.
- **Beta contribution:** 1.5% × ~2.5 = +0.038 to portfolio beta. Modest alone, but it stacks onto an already crowded "AI-capex semiconductor" factor cluster (Sector, Quant, Alt Data all flag this crowding independently).
- **Factor tilts added:** high-beta, high-vol (75%), **negative momentum**, no value support on trailing multiples (32.1x vs peer median 27.3x = 17.7% premium). This is the textbook momentum-crash profile Quant warned about.
- **Sector concentration test:** if semis >25% of the portfolio, cut this to 1.0% or pass.

---

## 5. Entry Strategy: **SCALE IN — 3 tranches. Do not go all at once.**

Two forces point in opposite directions, which is precisely why scaling is correct:
- **For acting now:** −57% from peak, 19.2x FY27E, net cash, a dated catalyst (27-Jan-2027), and Growth's 1.8:1 asymmetry.
- **For waiting:** an **unresolved binary legislative event with a 11-Dec-2026 funding deadline**, price still making lower highs ($221 Nov 9 → $183 Nov 20 → $171.53 intraday Nov 25), and no trend reversal signal.

| Tranche | Size | Trigger |
|---|---|---|
| **1 — now** | 50% of target (0.75%) | At market, $180–190 |
| **2 — policy or price** | 25% (0.375%) | EITHER MATCH Act softened/fails in NDAA **OR** capitulation to $150–165 |
| **3 — confirmation** | 25% (0.375%) | After 27-Jan-2027 print *confirms* the component-shortage catch-up landed |

**Hard rules:** do **not** chase above **$230** without Jan-27 confirmation. Do **not** add into a MATCH Act headline bounce — that is the highest-risk entry in the setup.

---

## 6. Risk Management Rules

**Stop-loss: $144 (−22%)** — volatility-aware, not tight. At 75% annualized vol this name routinely moves 20% in a week; a tighter stop is noise-harvesting. **Position size is the primary risk control here, not the stop.** For a 1.5% weight, a −22% stop costs **33bp of portfolio** — acceptable.

**Thesis invalidation (exit regardless of price):**
1. **MATCH Act (or equivalent) enacted *without* Dutch/Japanese harmonization** → permanent impairment of 10–15pts of China revenue, and unilateral US-only rules put Lam at a disadvantage to TEL/ASML.
2. **March-2027 quarter fails to recover the ~$400M of deferred shipments** → proves the "component shortage" framing was demand deferral. This is the highest-value single data point in the entire thesis.
3. **Two consecutive quarters of falling deferred revenue + rising DSO + gross-margin compression** — Short Analyst's explicit flip-to-short trigger. Currently the opposite is true (deferred revenue $2.43B → $2.66B).
4. **Any BIS subpoena, enforcement action, or license denial naming LRCX** — the single unverified gap across Geo Legal and Nonfin Risk reports (EDGAR 403'd). Escalate to immediate review.
5. **Gross margin fails to hold >48%.**

**Trim triggers:**
- **Trim 1/3 at $265** (~22x FY28E $12.12; ~90% of the low end of intrinsic value)
- **Trim 1/3 at $291** (24x FY28E = 5-yr average forward multiple — the re-rating is complete)
- **Let residual run to $340+** (28x FY28E / consensus PT median ~$352), trailing stop at 15%
- **Fundamental trim:** cut to 0.75% if China revenue mix does not fall below 30% by FY27-end as guided

---

## 7. Final Portfolio Action: **INITIATE — 1.5%, scaled, conditional**

**INITIATE** at **1.5% of portfolio** (0.75% immediately), with a hard **2.5% ceiling** contingent on the 27-Jan-2027 confirmation. **Override to PASS if the portfolio already holds AMAT, KLAC, or ASML at target** (0.88–0.93 correlation — this would be leverage, not diversification).

**Why initiate rather than pass:** the franchise is verified and improving (ROIC 49.4%, GM +590bp in three years, net cash, S&P 'A'), the forensic short case was tested and **rejected**, and at 19.2x FY27E / 15.3x FY28E with consensus PT median ~$352 the asymmetry is genuinely favorable. No specialist found the thing that usually justifies a pass — fraud, solvency risk, or competitive erosion.

**Why not more:** four independent agents converge on a 65%-probability legislative risk to a third of revenue; the macro regime is actively hostile to long-duration high-beta equity; and the stock is **not cheap on mid-cycle earnings** (~$170 normalized value vs $185 price). You are being paid to underwrite a 2–3 year AI capex window with a binary political option written against it.

**The one line:** *own a small amount of an excellent business at a fair price, sized so that being wrong about a Congressional outcome costs 33bp — not a career.*

---

**Open verification items before any add beyond 1.5%:** (1) FY26 10-K Legal Proceedings footnote — confirm no BIS inquiry; (2) Form 4 / 10b5-1 adoption dates for the $83M June–July insider cluster; (3) management's quantified MATCH Act scenario bridge; (4) 13-Dec-2026 NDAA outcome.
