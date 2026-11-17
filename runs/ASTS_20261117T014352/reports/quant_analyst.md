# Quant Analyst

- Symbol: ASTS
- Elapsed: 47.5s

---
# ASTS — Quantitative Factor & Risk Analysis

**AST SpaceMobile, Inc.** | Communication Services · Telecommunications Services | Market cap ~$11.7B | Live price ~$28.58 (see data caveat)

---

## 1. Factor Scores Table

| Factor | Score | Sector Rank* | Signal |
|---|---|---|---|
| **Value** | P/E **−21.3**, EV/EBITDA **−19.5**, P/FCF **−6.4** — all negative (no earnings/FCF) | **4 / 4 (last)** | **Strongly Unattractive** (not meaningful — see caveat) |
| **Momentum** | **−41.8%** (12‑1m, 252d); **−30.2%** (6‑1m, 126d) | **4 / 4 (last)** | **Strongly Negative** |
| **Quality** | ROE **−14.3%**, GP/Assets **0.0076**, accruals **−0.0539**; Piotroski **F=5** | **4 / 4 (last)** | **Low** (only accruals is a plus) |
| **Low Vol** | Ann. vol **105.6%**, beta **3.73**, max DD **78.5%** | **4 / 4 (last)** | **Very High Risk** |
| **Earnings Revision** | FY2030 EPS $3.65 vs $1.82 prior = **+100%** | n/a (single analyst) | **Upgrade — but statistically void** |

*Peer set: ASTS vs VZ, TMUS, T (nearest large-cap telecom comps). ASTS ranks dead last on every measurable factor.

**Peer comparison detail**

| | ASTS | VZ | TMUS | T |
|---|---|---|---|---|
| P/E | **−21.3** | 11.4 | 17.5 | 7.4 |
| EV/EBITDA | **−19.5** | 7.5 | 9.9 | 5.8 |
| ROE | **−14.3%** | 16.2% | 18.6% | 17.1% |
| GP/Assets | **0.008** | 0.156 | 0.192 | 0.178 |
| Momentum (12‑1) | **−41.8%** | −4.7% | −11.4% | −1.4% |
| Ann. vol | **105.6%** | 25.8% | 37.8% | 30.4% |
| Beta vs SPY | **3.73** | −0.34 | −0.35 | −0.35 |
| Max DD | **−78.5%** | −17.8% | −33.1% | −28.9% |

**Caveat on Value:** with negative EPS/EBITDA/FCF, the value factor's multiples invert sign and are economically uninterpretable. The correct statement is not "expensive" — it is *"no earnings-based valuation anchor exists."* The only usable valuation datum is **EV/Sales ≈ 163x** ($11.57B EV on $70.9M TTM revenue) and **P/B ≈ 4.9x** ($11.67B / $2.39B equity). At 163x trailing sales, the market is discounting a multi-year revenue ramp (consensus: $167M FY26 → $558M FY27 → $1.52B FY28).

---

## 2. Price Statistics

| Metric | 252-day | 126-day |
|---|---|---|
| Alpha (annualised, vs SPY) | **−148.3%** | **−204.3%** |
| Beta | **3.75** | **4.00** |
| R² | 0.261 | 0.329 |
| Ann. return | −89.3% | −166.8% |
| Ann. volatility | 105.7% | 99.2% |
| **Sharpe** | **−0.845** | **−1.681** |
| **Sortino** | **−1.486** | **−2.800** |
| Max drawdown | **−78.5%** | −67.8% |

**Interpretation.**
- **Beta ~3.7–4.0** is extreme, not merely "high beta." Only ~26–33% of variance is market-explained; **~70% is idiosyncratic** — this is a single-thesis event bet, not a factor exposure.
- **Alpha of −148% to −204%** is the signature of a de-rating, not operational deterioration matching the index. Note that alpha and beta are unstable across windows (sign-stable, magnitude unstable) — evidence the model is poorly specified for a jump-driven series.
- **Sortino (−1.49 / −2.80) materially worse than Sharpe (−0.85 / −1.68)** means downside volatility dominates total volatility: losses arrive in fat left-tail clusters. Risk-managed sizing must use the Sortino, not the Sharpe.
- The 126-day deterioration is the key read: **all four risk metrics are worse in the recent window**. This is a *deteriorating*, not stabilizing, risk profile.

**Ranks:** 4th of 4 on every factor; 1st of 4 on correlation to SPY (0.51 vs −0.11 to −0.19 for VZ/T/TMUS) — i.e., it is the only name in the set that actually behaves like an equity beta instrument.

**Correlation structure:** ASTS–VZ **−0.14**, ASTS–TMUS **−0.15**, ASTS–T **−0.11**. ASTS has *negative* correlation to the very peers it is classified with. It offers almost no diversification benefit within telecom — it is a standalone speculative position, and its 0.51 SPY correlation means it does **not** hedge equity drawdowns.

---

## 3. Composite Quant Signal

# STRONG SELL
**Composite rank: bottom quintile of the Communication Services universe on 4 of 5 factors.**

Weighted factor z-score is dominated by momentum (−41.8%), low-vol (105.6% vol, beta 3.73), and quality (negative ROE, GP/Assets of 0.8%) all sitting at the worst end of their distributions. The single positive reading — a +100% FY2030 EPS revision — rests on **one analyst** and a **four-year-forward** period, which fails any significance test.

**Important qualifier the numbers force me to state:** the value and quality factors are structurally miscalibrated for pre-profit ramps. A model built on P/E and ROE will *always* rank a pre-revenue capital-intensive business last, regardless of whether the satellite constellation succeeds. So the Strong Sell is an accurate statement about **factor exposure and realized price behaviour**, and a weak statement about **business viability**. Both facts belong in the memo.

**Analyst targets (for the qualitative desk, not my factor model):** recent PTs $65 (Oct-2) → $54 (Oct-13) → $55.70 (Oct-23) → $45 (Nov-10) → **$43 (Nov-10)**. The *direction* is unambiguously down even as levels sit ~50–120% above spot. **Target revision momentum is negative** — this contradicts the FY2030 revision "upgrade" and is the higher-signal of the two, since near-dated targets track the freshest information.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal / trend persistence (SEVERE).** −41.8% 12‑1m and −30.2% 6‑1m. Negative momentum in a name at 4x beta does not mean-revert on the schedule it does for low-beta names; losses compound.
2. **Beta 3.73–4.00 (SEVERE).** A 10% SPY drawdown implies a ~37–40% move. R² of 0.26–0.33 means this beta is an unstable estimate — realized sensitivity can spike.
3. **Drawdown 78.5% with no valuation floor (SEVERE).** With negative EBITDA and 163x EV/Sales, there is no multiple support level. Drawdowns terminate on narrative, not arithmetic.
4. **Dilution (HIGH, hard evidence).** Diluted shares **154.5M → 256.0M (+66% y/y)**; Piotroski F7 = 0. Equity rose via issuance, not earnings. Per-share value is being structurally diluted to fund capex — this is why EPS estimates remain negative through FY2028 despite revenue growth.
5. **Factor crowding — LOW concern.** Negative correlation to all telecom peers means this is *not* a crowded factor trade. The crowding risk here is retail/narrative positioning, not institutional factor overlap (cannot be measured with available tools).
6. **Liquidity — acceptable.** ADV ~10M shares / ~$300M+ notional; no liquidity constraint. But note volume spikes to 30–43M on news days — gap risk, not slippage risk.
7. **Earnings quality — mixed.** Accruals −0.0539 (conservative, "ok"), improved from −0.18 in FY24 and +0.28 in FY22. Cash burn is real: **OCF −$71.5M** vs net income −$341.9M. Cash $2.34B against $2.24B debt (net debt −$97M) — funded, not distressed.
8. **DATA INTEGRITY (must disclose).** The OHLCV endpoint lags (Feb-2026, $80.20) while the factor engine and company profile use the live ~$28.58 price — consistent with the Nov-2026 analyst PTs ($33–37 posted prices) and with the 78.5% peak-to-trough drawdown from the Jan-2026 highs (~$122 close). **All factor and risk statistics above are internally consistent with the live price and should be used; the raw OHLCV series should not.** Two further limits: the earnings-revision score is built on **n=1 analyst at FY2030** and is not statistically meaningful; and ASTS is absent from the top-10 Communication Services peer list by market cap, so "sector rank" is measured against the four-name telecom comp set, not the full sector.

---

**Bottom line:** Every measurable quant factor lands in the bottom decile: worst momentum, worst volatility, worst quality, no valuation anchor, negative alpha of −148% to −204%, and a Sortino of −1.49 to −2.80 confirming clustered downside. The only offsets are a funded balance sheet, improving accruals, and analyst targets well above spot on a falling trajectory. **On the numbers alone: Strong Sell. The bull case is a binary operational event that no factor in this framework can price — it must be underwritten qualitatively, sized against the Sortino, and never held as a beta or telecom-diversification position.**
