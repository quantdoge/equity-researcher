# Portfolio Strategist

- Symbol: TEM
- Elapsed: 46.4s

---
# PORTFOLIO CONSTRUCTION RECOMMENDATION — TEMPUS AI (NASDAQ: TEM)

**Price $78.48 | Market cap $13.68B | EV $14.25B | Beta 2.45 (252d) / 3.61 (5-yr) | Ann. vol 80.3% | 252d max DD −38.6% | P/B 27.8x | GAAP P/E n.m. (loss) | FY26E EV/Sales ~8.9x | Street PT median ≈ $78**

A note on what I did with my budget: I re-pulled price, multiples, beta, volatility and sector correlations to sanity-check the agents. Multiples and risk stats confirmed their figures. Correlations are new information and change the portfolio-fit view materially (Section 4).

---

## 1. Agent Conviction Summary Table

| Agent | View | Conviction | Key Finding |
|---|---|---|---|
| **Sector Researcher** | Constructive (sector "Attractive w/ high dispersion") | **Medium-High** | Best-in-class oncology data moat + fastest GM expansion in cohort (+22pts since FY22), but 62.7% GM sits *below* dx-peer median and headline growth is M&A-inflated; organic ~22–23% |
| **Growth Researcher** | **BUY** (3–5yr) | **High** | >$550M data-licensing bookings YTD vs ~$430M segment run-rate; GM +24pts in 4 yrs; 5-for-5 beats avg +66%; 8.9x FY26 sales vs peers at ~17–21x |
| **Value Researcher** | **SELL / AVOID** | **High** | Base-case intrinsic value **$43–45** (DCF and sum-of-parts converge); probability-weighted **$54**; price is 45% above value; zero ROIC-above-WACC year ever; negative tangible book |
| **Short Analyst** | **SHORT** (moderate, not strong) | **Medium** | Not a fraud case — an earnings-quality/valuation case. Growth collapsed 85%→23%; DSO 65→92 days; Q3 "FCF inflection" was **100% working capital**; Adj. EBITDA flatters ~$210M/yr SBC |
| **Fin Risk Analyst** | **HIGH financial risk** | **Medium-High** | Sub-investment-grade profile; interest coverage −3.1x; tangible equity −$334M; 4-yr cumulative FCF **−$892M**; 0.75% converts due 2030 = no near-term cliff (the key mitigant) |
| **Non-Fin Risk Analyst** | **HIGH** | **High** | 30:1 Class B votes; CEO+Chair+controlling holder; Nevada reincorporation; audit-chair pedigree; **~$97M CEO selling, ZERO insider buying in 12 months**; unresolved EDNY CID/Ohio AG subpoena status |
| **Geo Legal Researcher** | **MEDIUM risk** | **Medium** | Almost no foreign/geopolitical/sanctions exposure — but the *Farrier* GIPA class action attacks the legal premise of the highest-margin revenue line, and CMS algorithm-test reclassification is a live rule |
| **ESG Analyst** | **ESG RISK / negative overlay** | **Medium-High** | Governance 3/10; GIPA statutory damages $2,500–$15,000/violation → theoretical $1.25–7.5B; **"do not initiate or add ahead of a ruling on the motion to dismiss"** |
| **Quant Analyst** | **NEUTRAL** (momentum-tilted) | **Medium** | Top-decile momentum (+95.7% 12-1) against bottom-quintile value, quality and low-vol; alpha +19.7% but **R² 0.16** and <2yr sample — not statistically robust |
| **Alt Data Analyst** | **NEUTRAL, negative tilt** | **Low-Medium** | Revenue beat magnitude compressing each quarter (+1.3→0.8→0.7→0.5%); search interest −60% y/y vs Natera flat; earnings-day volume −35%; **"good news is priced"** |
| **Macro Researcher** | **UNFAVOURABLE** | **Medium-High** | 10Y at 5.13%, **real** yields +40bp to 2.60%, Fed *hiking* (Sept +25bp, held Oct); CAPM implied required return ~21% vs a 224x EV/Adj-EBITDA asset financed partly by convertibles |

---

## 2. Consensus Assessment: **SPLIT — but not the way it looks**

**Agreement level: Low on direction, High on facts.** This is the single most useful observation in the file, and it changes how the disagreement should be resolved.

The eleven agents are not actually fighting over what is happening at Tempus. They agree on almost every fact:

- Revenue is real and compounding (23% organic; $411.5M in Q3'26).
- Gross margin has genuinely expanded ~2,400bp in four years.
- Adjusted EBITDA turned positive a year or two ahead of schedule.
- Data & Applications is growing 33% at ~71% gross margin on >$550M of YTD bookings.
- The company has **never** produced a year of positive FCF (four-year cumulative −$892M) or positive ROIC.
- The balance sheet has negative tangible equity and $1.33B of debt.
- The *Farrier* GIPA suit directly imperils the de-identified data-licensing model.
- Governance is effectively closed to outside shareholders, and insiders have sold without buying.

**Where they actually split is on price.** The bulls (Growth, plus momentum from Quant/Short-term flows) are making a *fundamental trajectory* argument. The bears (Value, Macro, Risk, ESG) are making a *price-versus-risk* argument. Those are not competing claims — they can both be true simultaneously, and I believe both are.

**How I resolve it:**

1. **The fraud hypothesis loses.** Short Analyst explicitly de-weights it, and I agree: negative accruals, three of eight Beneish indices favourable, improving GM, $755M cash. Anyone shorting TEM on "cooking the books" has a low-probability bet.
2. **The GIPA/injunction risk takes precedence over the growth thesis.** This is the rule in my framework — when a forensic/legal flag threatens the *revenue model itself*, it outranks a growth narrative. *Farrier* does not allege a bad quarter; it alleges the de-identified-genetic-data premise is invalid. Every dollar of the 71%-margin segment rests on that premise.
3. **The valuation conflict resolves against the stock.** Value's DCF ($43) and sum-of-the-parts ($44) converge from independent methods — that convergence is the most credible single output in the entire file. Growth's rebuttal (8.9x forward sales vs NTRA ~21x / GH ~17x) is directionally fair but uses **trailing and estimate-blend multiples for loss-making comps**, not a clean consensus feed, and it prices TEM as if it carried no model risk and no governance discount.
4. **Two data conflicts I am resolving explicitly, at the portfolio level:**
   - **Q3'26 gross margin is ~64.8%, not 72.3%.** The 72.3% appears only in the raw income-statement cost-of-revenue line; the company's own release says 64.8%. This simultaneously deletes Short Analyst's "unexplained 790bp jump" red flag *and* deletes Growth's most aggressive margin data point. Net: both the bull and bear cases get a little weaker.
   - **Q3'26 cash-flow statement is corrupted** (net income +$120.3M in the CF feed vs −$14.9M in the P&L, inverted signs on D&A/SBC). I will not build any conclusion on it. Short Analyst's read — that positive Q3 FCF was ~100% working-capital release — is the only internally consistent interpretation and I weight it.
   - **Beta: use 2.5–3.6.** 252d regression gives 2.45; the 5-yr profile gives 3.61. A <2-year IPO sample cannot settle this; size for the higher number.

**Where the consensus is genuinely bullish and I credit it:** the operating trajectory. This is not a broken company. It is a company whose *equity* is priced for an outcome it has not yet earned.

---

## 3. Position Sizing Recommendation: **0% new capital (Pass). Ceiling of 1.0% if a mandate requires exposure.**

**Kelly criterion is unambiguously negative at $78.48.** Using the scenario weights that the evidence best supports:

| Scenario | Value/sh | Prob. | Return from $78.48 |
|---|---|---|---|
| Bull (data flywheel converts, GIPA benign, policy pivots) | $95–97 | 25–30% | **+21% to +24%** |
| Base (20%+ growth, FCF positive 2028, multiple holds) | $55–60 | 35–40% | **−24% to −30%** |
| Bear (reimbursement cut, GIPA adverse/consent re-papering, or rate shock) | $35–40 | 30–35% | **−49% to −55%** |
| **Probability-weighted** | **≈ $58–62** | | **≈ −22%** |

Kelly: p = 0.40, b = 22/32 = 0.69 → f\* = 0.40 − (0.60/0.69) = **−0.47**. Negative edge → **f\* = 0**.

Even granting the *most* bullish reading available — 25% weight on Growth's $97 bull case against a $50 downside — f\* is still deeply negative. **There is no set of probabilities derivable from these eleven reports that justifies a long position at $78.48.** The only way to own TEM here is with a *technical/momentum* edge (Quant's +95.7% 12-1 signal), which is a trading mandate, not a fundamental portfolio mandate.

**Sizing ladder, if the firm's mandate forces participation:**

| Situation | Max weight | Rationale |
|---|---|---|
| **Current price ($78.48)** | **0%** — Pass | Negative Kelly; price = street consensus median; 45% above convergence intrinsic value |
| If forced to hold for benchmark/coverage reasons | **≤0.75%** | At 80% vol, a 0.75% position contributes ~0.60% of portfolio annualised vol and a 2.45–3.61 beta-adjusted market-risk contribution of ~1.8–2.7% of portfolio equity risk |
| Price < $58 **and** Feb-2027 print clean | **0.5% starter** | Approaching probability-weighted value; still a venture-risk sizing |
| Price < $48 **and** GIPA MTD resolved favourably | **1.5%** | First point at which Value's base case ($43–45) is essentially the price |
| Fundamental proof (2 quarters FCF-positive ex-WC, SBC <8% rev, organic >28%) | **2.5–3.0%** | Evidence-based re-rate, not price-based |

**Why the ceiling is so low even in the best case:** 80.3% annualised volatility means a 2% position has a one-sigma annual P&L swing of ±1.6% of the entire portfolio. A 3% position in TEM is the risk-equivalent of a 7–9% position in a normal-volatility healthcare name. Sizing must be done on risk contribution, not on conviction.

---

## 4. Portfolio Fit Analysis

**Sector concentration — the newly measured constraint.** TEM correlates **0.52 with NTRA, 0.52 with GH, 0.53 with ILMN** (252d), against 0.40 with SPY. That correlation *is the whole argument*: if the portfolio already owns Natera, Guardant, Illumina, Exact Sciences or any broad genomics/diagnostics bucket, TEM does **not** add a new idea — it adds a levered second unit of the same factor. Effective sector exposure would rise roughly 1.7–1.9x the nominal position weight. The medical-diagnostics/AI-healthcare sleeve should be capped at **5–6% of portfolio** in aggregate; TEM, at 0.52 correlation to three of its neighbours, should not be the marginal dollar added to an already-populated sleeve.

*(Caveat: EXAS returned −0.24 correlation to TEM and −0.19 to SPY — a sign-flipped result that is almost certainly a data artifact. I exclude EXAS from any diversification argument.)*

**Factor exposure — TEM is a one-factor bet wearing three labels.**
- **+ Momentum** (top decile, +95.7%)
- **− Value** (bottom quintile)
- **− Quality** (negative ROE, negative ROIC, F-Score 5/9, negative tangible book)
- **− Low-vol** (80% vol, bottom decile)
- **+ Size-agnostic, 84% idiosyncratic** (R² 0.16)

Adding TEM to a portfolio is adding *crowded growth-momentum beta with negative quality*. That is defensible in a high-liquidity, falling-real-yield tape. Macro says we are in the opposite tape. **TEM consumes a disproportionate share of the portfolio's rate-sensitivity and drawdown budget** — a portfolio-level rate/duration risk budget already strained at a 5.13% 10-year should not be allocated to a 224x EV/EBITDA long-duration asset.

**Correlation / diversification verdict:** genuinely useful only if the portfolio is *empty* of diagnostics and *underweight* momentum. If it holds NTRA or GH, TEM is redundant and inferior — NTRA is the MRD leader (25x TEM's test volume, per Growth), and GH's balance sheet doesn't carry a GIPA suit against its core model.

**Idiosyncratic-event budget.** Beyond factor risk, TEM carries at least five discrete binaries the portfolio would be underwriting: (i) *Farrier* MTD/class-cert ruling; (ii) CMS algorithm-test final rule + PAMA 2026 cycle; (iii) Personalis shareholder vote (HSR already pulled-and-refiled — a staff-scrutiny tell); (iv) EDNY CID / Ohio AG status, which is *unknown*; (v) Feb 23, 2027 print. Five unresolved binaries is a lot of event risk for a sub-1% position.

---

## 5. Entry Strategy: **Do not buy at $78.48. Build a conditional scale-in ladder.**

**Current setup is the worst of both worlds.** The stock sits at $78.48 against a street target median of ~$78 (range $66–$92; two recent *Neutral* initiations at GS $75 and UBS $70). It has run **+92% off the July 2026 low of $40.77**, is +11% on the Q3 pop, and did so on **17.0M shares vs 26.1M on the prior print** — a low-conviction rally on thinning participation, with Google search interest −60% y/y and revenue beats compressing toward zero. No insider bought at $42; none has bought at $78. **Buying here is buying the only price at which nobody else wants to sell.**

**Ladder (fund from cash, not from selling better risk-adjusted names):**
1. **Now:** 0%.
2. **< $58:** 0.5% — but *only* after (a) the *Farrier* motion-to-dismiss ruling, and (b) the Feb 23, 2027 print confirms organic growth ≥25% and Q4 EBITDA ≥ the ~$34M implied step-up.
3. **< $48:** add to 1.0–1.5%, conditioned on no adverse CMS rule and no pharma partner pausing data licences.
4. **Post-proof (FCF positive ex-working-capital for two consecutive quarters, SBC <8% of revenue):** accelerate to 2.5–3.0% at *any* reasonable multiple — the thesis will then have changed from narrative to arithmetic.

**Explicitly do not buy ahead of: the Personalis vote, the GIPA MTD ruling, or the February print.** Three of the five binaries resolve within roughly one quarter. Patience is free here; the stock has already given back a 60% drawdown once and can do it again.

---

## 6. Risk Management Rules

**Stop-loss — price stops are nearly useless at 80% volatility.** One-month sigma is ~23%. A −25% stop would be triggered by ordinary noise on this name. Use fundamentals, not ticks.

- If a position is held: **do not use a tight price stop.** Cap the size (Section 3) and use a **−35% trailing stop only as a catastrophic backstop**; anything tighter is a coin flip.

**Thesis invalidation — exit immediately, full position, no averaging down, on any of:**
1. **Adverse ruling on *Farrier*** — denial of the motion to dismiss, or class certification, on the "genetic data cannot be de-identified" theory. This is the model-level kill switch; it invalidates the 71%-margin segment, not just a quarter. **Exit at market.**
2. **Any pharma counterparty (AZ, BMS, Merck, GSK, Pfizer) pausing, renegotiating or narrowing a data-licence** citing consent risk. Customer behaviour is a faster and more honest tell than the docket — ESG flags this correctly.
3. **EDNY U.S. Attorney CID or Ohio AG subpoena escalating** to a formal investigation, or confirmed still-open at the next 10-K. Currently unknown, which I treat as unresolved downside.
4. **Two consecutive quarters of organic growth below 18%** — the deceleration path (36%→22%→23%) has no valuation support below that level.
5. **FY2027 FCF still negative with a new equity or convertible issuance** — that converts a solvency cushion into a dilution event at whatever price the market offers.
6. **Headline gross margin reverting below 64%** — confirming the 72.3% line was an artifact and the mix-shift story stalled.
7. **Governance escalation:** a new related-party transaction with Pathos/SoftBank-type entities on undisclosed terms, or further meaningful insider selling with still-zero open-market buying.

**Trim trigger — this is the one rule I would enforce hardest.**
- **$85–90 (top of street range / ~110% of probability-weighted value): trim 50%.** At that point you are being paid the bull case in full.
- **$95+ (Value's bull case): exit entirely.** No fundamental support remains.
- **Any Personalis-close-related pop of >15% in the absence of operating news: trim 50%** — that is dilution being celebrated, not value being created.

**Monitoring cadence:** quarterly on (a) DSO (91.8 days is the canary — receivables +106.7% vs revenue +83.4% in FY25), (b) bookings-to-revenue conversion of the >$550M data backlog, (c) Form 4 flow (first open-market insider purchase would be a genuine positive signal), (d) any CMS/PAMA publication.

---

## 7. Final Portfolio Action: **PASS**

**Do not initiate. If already held, Reduce to ≤0.75% or exit.**

**Rationale in one paragraph:** Tempus is a genuinely improving, category-leading precision-oncology and data business — the sector, growth and alt-data agents all confirm the operating trajectory is real, and I credit that. But the portfolio question is not "is this a good company," it is "does this equity pay me for the risk it adds?" On these eleven reports the answer is no: probability-weighted value is ~$58–62 against a $78.48 price; two independent valuation methods converge at $43–45; the Kelly fraction is negative under every probability set the evidence supports; the stock is already at street consensus; 84% of its return variance is idiosyncratic; it adds 0.52-correlated redundancy to any existing diagnostics exposure; it consumes rate-sensitivity budget in a rising-real-yield regime; and it carries a live class action that attacks the legal premise of its highest-margin revenue line, alongside 30:1 founder voting control with ~$97M of insider sales and zero purchases.

**What would change the call — in order of importance:**
1. **A favourable *Farrier* ruling**, which removes the model-level tail and would justify re-underwriting the data segment on a normal risk premium.
2. **A price below ~$58** (approaching probability-weighted value) or **below ~$48** (at Value's base case), whichever the fundamentals deliver first.
3. **Two quarters of SBC-adjusted FCF-positive results with a clean gross-margin explanation** — at which point the debate moves from multiple to earnings and I would size 2.5–3.0% regardless of a higher price.

Until one of those three arrives, the correct number of shares of TEM in the portfolio is **zero**, and the correct action is to keep it on the watchlist with the invalidation triggers above pre-committed.

---

**Gaps disclosed honestly:** portfolio composition was not supplied, so fit analysis is stated conditionally on holdings; no formal credit rating or debt-maturity/covenant schedule exists; the EDNY/Ohio AG investigation status is unknown and unresolvable within budget; related-party and round-tripping allegations originate with Spruce Point's May-2025 report rather than a verified FY25 10-K; the Q3'26 cash-flow statement
