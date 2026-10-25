# Portfolio Strategist

- Symbol: NRG
- Elapsed: 96.9s

---
# NRG Energy (NYSE: NRG) — Portfolio Construction Recommendation
**Price $99.38 (Oct 19, 2026 close, verified) | Mkt cap ~$19.8B | EV ~$43B | 52-wk range $93.36–$188.72**

---

## 0. Data Reconciliation (must be settled before any sizing decision)

Two upstream agents declared the $99.38 price "stale" and restated everything to **$178**. That restatement is **wrong**, and it inverts their conclusions. I pulled the OHLCV series directly: it runs through **2026-10-19 and closes at $99.38**. The $178 figure was simply a feed truncated at Feb 2026. **$99.38 is live.** The Quant analyst's "+77% return / +1.9 Sharpe / 44x P/E / 13.8x EV-EBITDA" corrections must be discarded in full; the Fin Risk analyst's FCF-yield restatement likewise.

Two reconciliations that *do* change the numbers materially:

| Item | Conflicting inputs | Resolution |
|---|---|---|
| **Post-deal net debt** | Value $15.5–17.0B; Fin Risk $23.3B; tool $9.84B (FY25, pre-deal) | **Use $23.3B** (Q2'26 10-Q: debt $23.467B, cash $162M). Tool data is pre-LS Power. **EV ≈ $43.1B, not $29.6B/$37.5B** |
| **Consensus EBITDA** | $4.13B (2026E) vs guidance $5.33–5.83B | Consensus series is **stale/pre-deal; discard**. Anchor on guidance |
| **Price** | $99.38 vs $178 | **$99.38 live.** Down 47% from Feb-26 high — the drawdown is real |

**The consequence:** at the correct EV, NRG trades **7.7x 2026E adj. EBITDA** ($43.1B / $5.575B) and **14.1x 2026E FCFbG** — not the 6.7x and "14.5% yield on market cap" the Value report implied. On enterprise value, free cash generation is roughly **7.1%**, versus a marginal cost of debt of ~7.0–7.5% for a BB credit. *The enterprise earns approximately its cost of debt; equity value rests almost entirely on the growth pipeline.* That is the single most important number in this file.

---

## 1. Agent Conviction Summary

| Agent | View | Conviction | Key Finding |
|---|---|---|---|
| **Sector Researcher** | Positive (relative) | **Medium-High** | Attractive cycle; NRG ~11x FY26E vs VST ~14x / CEG ~21x. Integrated gen+retail is a real moat. But **lowest gross margin in peer set (21.9% vs 32.3%)**, op margin 6.0% vs 11.5%, negative 3-yr revenue CAGR |
| **Geo Legal** | Medium risk | Medium | US-only, no sanctions/EM/FX. But **46% of FY25 EBITDA in one state market**; FERC rejected most of PJM's large-load package **Oct 9, 2026** → BYOP reverts to state-by-state. Uri litigation extinguished (material positive) |
| **Macro** | **Unfavourable near-term** → Neutral 12–24m | Medium | 10Y 5.09–5.24% (5.34% = highest since 2002), Fed hiked in Sep. ~2x levered equity: **100bp on the 10Y ≈ 10–15% of equity value**. Demand backdrop excellent; discount rate is the binding constraint |
| **Value Researcher** | Fully valued | Medium | IV **$100–105** vs $99.38 — *no margin of safety*. Negative tangible book **−$5.7B**. 5/10 quality, 5/10 management. $1.4B buyback in 2025 at ~$130 avg |
| **Growth Researcher** | **HOLD** | Medium | Rule of 40 ≈ 23. ~4.5% revenue CAGR; ~18% EPS CAGR must come from margin + buyback. **Two consecutive misses (Q1 −16.4%, Q2 −11.8%), both interest/D&A-driven.** Upgrades on Q3 beat + signed BYOP |
| **Fin Risk** | **HIGH** | **High** | Pro-forma **4.3x vs Fitch's 3.5x downgrade trigger**. Z-score 1.67 (distress, robust to market-equity adj.). **Cash $162M, current ratio 0.97, GAAP coverage ~1.4x.** Margin buffer to a 1.0x coverage breach ≈ 3.5pts of gross margin — and FY23 already breached it |
| **Nonfin Risk** | **HIGH** | **High** | 3 CEOs in ~24 months; combined Chair/CEO through the deal window. **Net insider selling, zero open-market buys into a 47% decline.** LS Power exited 67% at $164. Single-counterparty $3.2B bet |
| **Quant** | Neutral | **Low** (its own data error) | Quality + momentum ranked 1 of 4 in peer set; **low-vol worst in sector (σ 51%, β 1.25, DD 48%)**. Conclusions rest on a mis-restated price — treat as unreliable |
| **Short Analyst** | **SHORT**, low-moderate | Medium | **Not a fraud** (M-score −2.75, accruals −3.6%, cash conversion 2.21x). "Leverage story dressed as growth." Consensus now below the guidance floor. 6.5x EBITDA → **$74**; 6.0x → **$61** |
| **ESG** | Average, deteriorating | Low-Medium | $71m NY PSC ESCO settlement (Apr-26); gas fleet doubled to ~25GW; **no SLB covenants → no cost-of-capital penalty**. Regulatory tail concentrated in the highest-value retail segment |
| **Alt Data** | **Bearish into Nov 5** | Medium | Q3 consensus **$3.24 = +17.8% YoY** against a **−33% H1**. Beat rate 42.9%. Parent-brand search at 12-mo lows. Reliant brand +27% YoY vs Texas rate-shopping −50% YoY |
| **Portfolio Strategist (me)** | **PASS / defer** | Medium-High | Absolute valuation gives zero cushion; EV-level FCF ≈ cost of debt; binary print in 11 trading days |

---

## 2. Consensus Assessment: **SPLIT, negatively skewed**

**Where agents AGREE (high confidence):**
1. **The asset base is genuinely good and cannot be quickly replicated.** Buying 13GW of dispatchable gas at ~$920/kW vs $1,500–2,000/kW replacement cost is sound. Unanimous.
2. **Leverage, not demand, is the constraint.** Macro, Value, Growth, Fin Risk, Nonfin Risk, Short all independently locate the problem in interest expense, D&A and the balance sheet — not the revenue line (revenue has beaten in 6 of 7 quarters).
3. **The equity sits at fair value, not at a discount.** Value's IV $100–105 vs spot $99.38 = 95% of base case. The stock is *above* any 90%-of-IV trim threshold. Even the bullish Sector Researcher's case is **relative** (11x vs 14–21x), not absolute.
4. **Nov 5 is a binary event** and the near-term setup is poor (Macro, Growth, Alt Data, Short all converge here).

**Where agents CONFLICT:**
- **Sector (buy the discount) vs Value (no margin of safety).** Resolved in Value's favour on the absolute test: relative cheapness is an argument for owning the *sector*, not for owning a 51%-vol, 4.3x-levered stub.
- **Quant vs Short.** Quant's "quality + momentum leadership" was computed off a truncated price series and is void. Short's leverage thesis survives.
- **Growth (upgrade on confirmation) vs Short (consensus below guidance floor).** These are compatible: both say *wait for the print*.

**Rule applied per my framework:** where the Short analyst and Fin Risk analyst flag solvency-grade risks (negative tangible equity, 4.3x leverage above the downgrade trigger, $162M cash, 1.4x GAAP coverage), those risks **override** the value/sector case for cheapness. Fraud risk is absent — but balance-sheet risk is not, and it ranks ahead of multiple compression.

**One finding of my own that sharpens the risk:** FY26 guidance midpoint ($8.90) requires **H2'26 adj. EPS of ~$5.92** (Q3 consensus $3.24 + Q4 ~$2.68) against **H1 actual of $2.98** and **H2'25 of ~$3.78**. That is a **+57% YoY second half** immediately after a −33% first half, with Q4 required to more than double last year
