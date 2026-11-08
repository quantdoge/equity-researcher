# Portfolio Strategist

- Symbol: AMD
- Elapsed: 60.1s

---
# AMD — Portfolio Construction Recommendation

**Price $449.04 | Mkt cap $733B (≈$877B fully diluted incl. warrants) | Beta 1y 3.54 / 3y 2.38 / profile 2.49 | Ann. vol 76.9% | Max DD −63% (3y)**

*Data note: two feeds disagree — valuation/analyst data is Nov-2026 ($449), raw OHLCV terminates Feb-2026 (~$200). All levels below use the Nov-2026 snapshot. ESG agent failed outright (API error, code 502) — a genuine gap in the coverage set, not an omission by this desk.*

---

## 1. Agent Conviction Summary Table

| Agent | View | Conviction | Key Finding |
|---|---|---|---|
| **Sector Researcher** | Attractive sector / Strong position — *priced for perfection* | **High** | EPYC 46.2% x86 server share; FY27 guide >80%; op margin 1.8%→21.2% in 3 yrs. But memory at 80.7% GM = peak-cycle signature |
| **Growth Researcher** | **Strong Buy** | **High** | 25.7x FY27E EPS, 79% EPS CAGR FY26–28E, 7/7 beats, Rule of 40 = 54, median PT $650 |
| **Value Researcher** | **Sell / Avoid** | **High** | Prob-weighted IV **$290** vs $449 (−35%); ROIC 5.47% < WACC ~10% for 4 straight years; 34x tangible book |
| **Fin Risk Analyst** | Moderate (bifurcated) | **High** | **Credit LOW** (net cash, A1/A, Z 3.74, 28–48x coverage). **Equity HIGH** (96x P/E, 0.92% FCF yield vs 5.13% 10Y) |
| **Macro Researcher** | **Unfavourable** (6–12mo) | **High** | Fed *hiking* (3.75–4.00%), CPI 3.72%, HY OAS +82bp to 348bp. Bear path $200–250. "Fundamentals decoupling from the discount rate" |
| **Geo Legal Researcher** | **Medium-High risk** | **High** | China 22.4% of revenue licence-gated; 15% USG revenue share; Taiwan 15% single-source foundry; 25% §232 tariff on MI325X |
| **Nonfin Risk Analyst** | **High risk** | **Med-High** | CEO sold **>$125M** in 2026 at $503–515, zero buys; customer warrants = ~10% of AMD each; FCF fell to ~4% of revenue |
| **Short Analyst** | **Short** (valuation, *not* fraud) | **Med-High** | No fraud found (Beneish −2.761, accruals −4.4%, F-score 8/9). But Q3 cash conversion **0.50x**, inventory **169 days**, 320M warrants = **19.6% dilution** |
| **Quant Analyst** | **Neutral** | **Medium** | Composite 2.8/5: Momentum 1/5, Revisions 1/5 but **Value 4/4 worst, Quality 5/5 worst, Low-Vol 4/5 worst**. Alpha +62% but **t = 1.57 — not significant** |
| **Alt Data Analyst** | Neutral, cautious tilt | **Low-Med** | Hiring bullish, 7/7 beat rate; but Ryzen search −40% YoY, EPYC search −52%, news sentiment 0.91 = crowded-long flag. 3 of 6 sources failed |
| **ESG Analyst** | ❌ **No output** | — | API failure (502). Coverage gap — flag in memo, do not infer a clean ESG profile |

---

## 2. Consensus Assessment: **SPLIT — with strong directional consensus on *why***

This is not a confused split. It is a **clean disagreement about price, not about the business**:

**HIGH-CONVICTION CONSENSUS (7 of 10 reporting agents):**
- **Valuation is the dominant risk, not the franchise.** Value, Fin Risk, Quant, Short, Macro, Sector and Nonfin all independently land on this. At 56x FY26E / 96x TTM EPS with a 0.92% FCF yield against a 5.13% 10-year, the equity is a long-duration claim priced for flawless execution.
- **Operating momentum is genuinely accelerating** — even the Short Analyst concedes gross margin is *expanding* (46.1%→53.9%) and revenue growth is *accelerating*. Nobody disputes the franchise.
- **Beta/volatility is the sizing constraint.** Four agents (Fin Risk, Quant, Macro, Growth) independently say position sizing — not fundamental analysis — is the primary control here.

**CONTESTED:**
- **Growth vs. Value** on intrinsic value: $650+ (Growth, PT median) vs **$290** (Value, DCF prob-weighted). Both are internally coherent; the entire spread is the terminal-value/decade-of-25%-growth assumption. Resolution: **Growth is right about direction; Value is right about the price paid for it.**
- **Cyclicality**: Value and Macro see a late-cycle top (memory at 80.7% GM, revenue +256%); Growth and Sector see a mid-cycle ramp with >$1T 2027 hyperscaler capex. Unresolvable today — which argues for smaller size, not conviction either way.

**RESOLVED IN THE BEAR'S FAVOUR (2 independent agents, high evidentiary quality):**
- **Customer warrant / circular-financing structure.** Short and Nonfin independently flag 320M warrants (~19.6% dilution, $144B notional, $1.097B Q3 non-cash charge). Growth flags it too ("vendor-financed growth — circularity risk"). **Three agents, no rebuttal.** This is a quality-of-revenue discount that must be applied regardless of the growth story.
- **Q3 cash-conversion break (0.50x) + inventory at 169 days.** Short quantifies; Nonfin corroborates ("FCF ~4% of revenue on record earnings"); Value flags working capital −$2.38B. Consensus red flag.

**CRITICAL PRECEDENCE CALL — fraud risk is screened OUT:** Beneish −2.761, accruals negative four years running, F-score 8/9, Z-score 3.74, no restatement, no material weakness, no SEC/DOJ action, receivables *shrank* 8.9% while revenue grew 34.3%. Under my framework, fraud risk would override a bullish value view — **it isn't present.** The bear case is therefore a *multiple-compression* case, which is a sizing decision, not an exclusion decision.

---

## 3. Position Sizing Recommendation

### **0.75% of portfolio (starter). Hard ceiling 2.0%.**

**The Kelly math says pass; the franchise quality says own a little.**

Scenario-weighted expected value (derived from the agent distribution, weighting the six valuation-negative agents against Growth/Sector):
| Scenario | Price | Return | Prob |
|---|---|---|---|
| Bull — FY27 $95B lands, GM ≥55%, re-rate | $625 | +39% | 30% |
| Base — growth lands, multiple compresses to ~30x | $440 | −2% | 40% |
| Bear — capex air-pocket, 50x→25x | $260 | −42% | 30% |

**EV ≈ −1.7%; σ ≈ 34%.** A negative-expected-value, 3.5-beta, 77%-volatility position. Kelly fraction ≈ **0**.

A pure Kelly discipline returns **Pass**. I am overriding to a sub-benchmark starter for three reasons, and I want the override on the record as *deliberate, not analytical drift*:
1. **The bear case is a macro/timing call, not a franchise call.** Macro himself concedes the bull counter-scenario re-rates to $650–700 and calls the Fed's next move — not AMD's next quarter — the swing factor. I do not want zero exposure to a genuine structural share-gainer on a coin-flip macro path.
2. **The 31% drawdown has partially reset the entry.** 25.7x FY27E is not 96x TTM.
3. **Optionality on the Feb 2, 2027 print is asymmetric to the upside** given 7/7 beats and +5.2% average surprise — but only if entered small.

**Sizing derivation:**
- Full-weight for a high-conviction name = 3–5%. AMD fails on **both** axes: conviction is Split (not High), and risk flags number five-plus.
- Standard band would be 0.5–1.0% or pass. I am at the **top of the pass band (0.75%)** because the balance sheet carries zero solvency risk — this cannot be a permanent capital loss on fundamentals (Fin Risk: survives a −40% revenue collapse EBITDA-positive, net-cash).
- **Loss budget check:** a full bear-case drawdown to $260 from $449 = −42%. At a 0.75% weight that is **−32bp of portfolio**. At a 2.0% ceiling it is −84bp. Both tolerable; the ceiling is set by the *correlation* problem below, not by standalone risk.

**Scaling authorization to reach 2.0% requires BOTH:**
- (a) FY27 revenue guide formally quantified at **≥$85B** with gross margin **≥55%**, **AND**
- (b) cash conversion recovering to **≥1.0x** for two consecutive quarters.

Alternatively, price alone at **≤$330** (below value's $290 base plus a growth premium, and near the peer-median-multiple implied $305) justifies scaling to 2.0% on unchanged fundamentals.

---

## 4. Portfolio Fit Analysis

**Sector concentration — the binding constraint.** Semiconductors / AI compute is almost certainly already the portfolio's largest active overweight. AMD adds *no* new theme: it is a second-source derivative of the identical hyperscaler capex pool that funds NVDA, AVGO, MU and TSM. If the book is already >15% AI-semis, **AMD should be funded from an existing semi holding, not from net-new risk budget** — otherwise the firm is doubling down on a position it already owns.

**Correlation — measured, 252-day:**
| | AMD | NVDA | AVGO | MU | TSM | SPY |
|---|---|---|---|---|---|---|
| **AMD** | 1.00 | 0.55 | 0.59 | **0.67** | **0.73** | 0.65 |

AMD–TSM at **0.73** is the highest pair in the group and is the correct lens: AMD is effectively a levered TSMC-allocation bet. AMD–MU 0.67 makes the memory-cost shock a shared factor. **Diversification benefit is approximately nil.** Effective factor exposure of a 0.75% position ≈ 1.3–1.5% of equivalent single-name risk once correlation-adjusted.

**Factor exposure — this is an *additive* tilt, not a neutral one:**
| Factor | AMD Rank (/5, 1=best) | Effect on book |
|---|---|---|
| Momentum (12-1) | **1** | Adds to an already-extended momentum/growth tilt |
| Earnings revision | **1** (proxy only — tool output invalid) | Reinforces |
| Low Volatility | 4 | **β 3.54 (1y) — inflates book beta** |
| Value | 4 of 4 (worst) | **Deepens a growth-over-value skew** |
| Quality | 5 of 5 (worst) | ROE 6.88%, GP/Assets 0.223 — dilutes book quality |

**Beta-multiplication caution:** three estimates — 2.49 (profile), 2.38 (3y), 3.15 (2y), **3.54 (1y)**. The divergence is itself the warning: risk models will mis-scale this position. **Size off the 3.54, not the 2.49.** At the 1-year beta, a 10% market drawdown implies a ~35% AMD drawdown.

**Duration/rate factor:** With the 10Y at 4.84% (5.31% intramonth peak) and the Fed *hiking*, AMD is the portfolio's most rate-sensitive asset per unit of weight. If the book already carries long-duration growth exposure, this position compounds the single largest live macro risk (Macro: Unfavourable).

**Liquidity: no constraint.** $733B cap, 20–250M shares/day. Exitable in one session at a 0.75–2.0% weight.

---

## 5. Entry Strategy: **SCALE IN — three tranches, do not add into the Feb 2 print**

At 77% annualised volatility, monthly σ ≈ 22%. A single slug at $449 is a coin flip on entry price, not an investment decision.

| Tranche | Size | Trigger | Rationale |
|---|---|---|---|
| **T1** | 0.25% | At market ($449) | Secures exposure; 31% drawdown already banked |
| **T2** | 0.25% | Retest of **$400** (−11%) **or** post-Q4 print if guide holds | $402 was the Nov 5 capitulation low — buy the retest, not the bounce |
| **T3** | 0.25% | **$330** (−26%) on unchanged fundamentals, **or** confirmed ≥$85B FY27 guide + ≥55% GM | Value's $290 base + growth premium; the only level where the risk/reward inverts |

**Rules:** No averaging up above $500. **No adds in the 10 sessions before Feb 2, 2027** — that print (consensus $17.01B rev / $2.91 EPS, +27% QoQ) is a binary event at this volatility; hold T1+T2 through it at reduced size rather than sizing up into it. If T2 and T3 both fill, the blended cost is ~$393 — an 12.5% cushion against value's base case rather than a 55% premium to it.

---

## 6. Risk Management Rules

**Hard stop: $300 (−33% from current).** This is not arbitrary — it roughly coincides with (a) Value's probability-weighted IV of $290, (b) the peer-median-multiple-implied $305 (38x FY26E EPS $8.03), and (c) the top of Macro's bear-case range of $200–250. Below $300 the market is telling you the FY27 >80% growth guide is dead. Exit mechanically, do not re-underwrite.

**Fundamental thesis invalidation — exit on any two simultaneously, or immediately on #1:**
1. **FY27 revenue guidance cut below $80B** (from ">80%"), or a Q4 FY26 revenue miss vs. the $17.0B guide. *This is the keystone — the entire 25.7x forward multiple rests on it.*
2. **Gross margin below 53% for two consecutive quarters** (rack-mix/HBM dilution). Growth, Short and Sector all flag this as the highest-probability break.
3. **Cash conversion <0.7x for two more quarters, inventory days >175, or a second write-down** (the ~$800M MI308 charge is the precedent). Short's falsification trigger set — adopt it verbatim.
4. **Any OpenAI/Meta warrant milestone slip or renegotiation**, or new congressional disclosure of non-standard customer-financing terms (Jan-2027 Democratic Congress = subpoena risk).
5. **China: BIS revoking/re-conditioning the MI325X pathway at the July 1, 2026 review, formal Beijing import ban, or reinstatement of the 50%-affiliates rule.** Any single one → cut to 0.25%.
6. **Macro regime break: HY OAS >450bp *and* 10Y >5.5%.** Reduce by half regardless of fundamentals — this is Macro's "debt-funded capex air-pocket," the live path to $200–250.
7. **Taiwan Strait quarantine or blockade → immediate full exit.** Unhedgeable, binary, and the position size does not justify carrying it.

**Trim triggers:**
- **Trim ⅓ at $560** — above the top of the base fair-value band ($450–550) and ~90% of the blended intrinsic range. Take the money.
- **Trim ⅓ at $625** (Growth's bull); **exit remaining above $650** (analyst PT median) unless FY28 revenue visibility has materially improved.
- **Mandatory trim to 0.5% if weight exceeds 2.5% on appreciation alone** — the correlation and beta profile cannot support drift.

**Governance watch (non-trading, escalate to IC):** CEO insider sales >$125M/$781M aggregate with zero offsetting purchases; say-on-pay at 85% vs 92.3% S&P average; combined Chair/CEO with no disclosed succession plan. **Request the warrant accounting memo and customer-financing footnote before any scaling above 0.75%.** Nonfin explicitly escalates items 1–4 to the investment committee — this desk concurs and makes it a precondition on the 2.0% ceiling.

---

## 7. Final Portfolio Action

# **INITIATE — 0.75% starter position, laddered**

**Not a full initiation. Explicitly not a Pass, and explicitly not an Add.**

**The one-line rationale:** AMD is a genuinely elite operating franchise — accelerating revenue, expanding gross margins, net cash, regaining server-CPU share, and *clean accounting* (fraud is screened out, not merely unproven) — trading at a price that already capitalises a decade of near-flawless execution. Six of ten reporting agents independently identify valuation as the dominant risk variable; the probability-weighted outcome is roughly flat to negative with ~34% dispersion. That is a position to **own small, size off the 3.54 beta, fund from existing semi exposure, and let the price come to you** — not a position to underwrite at $449.

**What would change this call:**
- **To ADD (2.0%):** price ≤$330, or FY27 guide quantified ≥$85B with GM ≥55% *and* cash conversion ≥1.0x for two quarters.
- **To PASS (0%):** HY OAS >450bp with 10Y >5.5%, a hyperscaler 2027 capex cut, or the Q4 print missing on gross margin.
- **To EXIT (post-entry):** $300 hard stop, or invalidation triggers #1/#5/#7.

**Memo disclosures I am carrying forward rather than smoothing over:**
1. **ESG agent returned nothing** (API 502). No ESG view was formed. Do not treat the absence as a clean profile — commission a replacement before the IC meeting.
2. **Two data feeds disagree on price** ($449 Nov-2026 vs ~$200 Feb-2026). All multiples in the underlying reports that use the $200 vintage are understated in magnitude but directionally correct.
3. **Quant's earnings-revision score is methodologically invalid** (it returned an FY30/FY29 growth rate, not a 3-month revision). The revision signal above is a price-target proxy only — 10 notes, all dated 2026-11-04/05, so cross-sectional information content is low.
4. **Alt data: 3 of 6 planned sources failed** (patents, web traffic, StockTwits). Confidence low-to-medium.
5. **Peer valuation work is thin** — n=4–5 comparables, TSM value output corrupt. Ranks are indicative, not percentile scores.
