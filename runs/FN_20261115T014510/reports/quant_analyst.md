# Quant Analyst

- Symbol: FN
- Elapsed: 63.4s

---
# FN — Fabrinet: Quantitative Factor Report

**Price used: $327.98** (FMP quote; third-party quotes show $348.52 — see Data Integrity note). Market cap $11.90B, EV $11.03B, **net cash ~$871M**, no dividend. Fiscal year ends late June; FY2026 (ended 2026-06-26) is the latest reported annual period.

---

## 1. Factor Scores

| Factor | Score / Raw | Sector Rank* | Signal |
|---|---|---|---|
| **Value** | P/E 25.1x, EV/EBITDA 17.7x, P/B 4.84x, **P/FCF 3,910x** (FCF $3.0M) | 2 of 5 (cheapest on P/E) | **Neutral–Positive** (mechanical score wrecked by P/FCF) |
| **Momentum** | **−33.2%** 12-1 return; −56% from $746 peak | 5 of 5 | **Strong Negative** |
| **Quality** | ROE 19.3%, ROIC 18.8%, GP/A 14.2%, accruals **+5.5%**, F-Score **5/9** | 3 of 5 | **Neutral** (tool: "low") |
| **Low Vol** | 85.3% ann. vol (1Y), beta **3.03**, max DD **60.8%** | 5 of 5 | **Strong Negative** |
| **Earnings Revision** | Tool: **+19.25%** — *artefact, see below*; true revision trend positive | n/a (thin coverage) | **Positive, low confidence in tool output** |

\* Rank vs optical/EMS comparables (JBL, COHR, ANET, LITE). FMP's "Technology" sector is dominated by software/semi mega-caps (AAPL, NVDA, MSFT) and is not a valid peer set for an optical contract manufacturer.

**Peer multiple cross-check — FN is the cheapest profitable name in the group:**

| | FN | JBL | COHR | ANET | LITE |
|---|---|---|---|---|---|
| P/E | **25.1** | 26.1 | 53.0 | 71.7 | n/m (loss) |
| EV/EBITDA | **17.7** | 14.1 | 28.3 | 55.7 | n/m |
| P/B | 4.84 | 16.8 | 3.79 | 20.3 | 9.58 |
| P/FCF | 3,910 | 19.8 | neg | 59.2 | 148 |

**Forward curve (consensus, 4 analysts FY27):** Fwd P/E **16.6x** on FY27E EPS $19.71; **13.7x** FY28E $23.99; **11.0x** FY29E; EV/EBITDA **12.8x** FY27E, **10.4x** FY28E. On forward numbers FN is materially cheaper than every peer despite 35–50% growth — a genuine value signal that the trailing P/FCF completely obscures.

---

## 2. Price Statistics (2-year window, 504d, vs SPY)

| Metric | Value |
|---|---|
| Annualised alpha | **−6.51%** |
| Beta (regression) | **3.02** (R² = **0.276**) |
| Annualised return | +51.4% |
| Annualised volatility | 73.4% (1Y: 85.3%) |
| Sharpe | **0.695** (1Y: −0.226) |
| Sortino | **0.992** |
| Max drawdown | **−60.8%** (close-basis: −56.1%, $746.47 → $327.98) |

**Critical read:** the 51% annualised return came with a beta of 3. A beta-3 stock needs ~58% to beat SPY; FN delivered 51%, hence negative alpha. **High beta without compensation** — the classic signature of a crowded, de-rating momentum name. R² of 0.276 means 72% of variance is idiosyncratic: this is not a market proxy, it is a single-theme bet.

---

## 3. Composite Quant Signal: **NEUTRAL**

Three of five factors (momentum, low vol, alpha) are outright negative and one is a data artefact. The offsetting case is real but forward-looking: 16.6x FY27 earnings for +40% growth, 18.8% and rising ROIC, $871M net cash, and fundamental estimate revisions that are genuinely upward (FQ1 FY27 revenue $1,474.5M, **+51% y/y**, non-GAAP EPS $4.34, Q2 guide $1.60–1.65B **above consensus**). The stock is falling on multiple compression, not on deteriorating numbers. That is a valuation opportunity for a 12-month holder and a falling knife for a momentum holder. **Neutral; upgrade to Buy on price stabilisation plus one quarter of gross-margin confirmation.**

---

## 4. Key Quant Risk Flags

1. **Momentum reversal already realised, not pending.** −33% 12-1, −56% from the May-2026 peak, 60.8% drawdown. Trend-following and vol-targeting flows are still sellers.
2. **Earnings-revision tool output is not trustworthy.** The +19.25% "upgrade" compares the **FY2030** estimate ($35.47, **n = 1 analyst**) against $29.74 — which is *exactly* the FY2029 consensus in the same table. It is a rolling-period artefact, not a revision. I have discounted it and substituted the actual fundamental trend (positive) and price-target trend (**negative**: B.Riley $598 → $431 → $364; consensus ~$549–586 across 19 analysts, ~+68% implied).
3. **FCF collapse / capex cycle.** FCF fell to **$3.0M** from $206.5M (FY25) and $365.6M (FY24): capex $253.7M plus a $259.9M working-capital drain. Any value screen using P/FCF will reject FN outright until this normalises.
4. **Earnings quality deteriorating.** Accruals ratio +5.53% ("warning") vs +0.15% prior year; gross margin compressed for four straight years (12.71% → 12.35% → 12.09% → **12.00%**); F-Score 5/9, failing on accruals, leverage, margin and asset-turnover.
5. **Beta instability.** Regression beta 3.02 vs profile beta 1.368 (5Y). With R² = 0.276 the beta estimate carries a wide standard error; do not size a hedge off 3.0.
6. **Crowding / theme risk.** Press coverage attributes weakness to customer concentration and slowing NVIDIA-linked transceiver demand. I could not verify concentration figures from the data provided — **unverified, treat as a qualitative overlay**.
7. **Liquidity is adequate** (~700k–1.0M shares/day, ~$300M+ notional; spikes to 7M on earnings) — not a constraint, but gap risk around prints is high (multiple ±10% days in the sample).

**Sample-size caveats:** FY2027 estimates rest on 4 analysts (tight range $19.53–$19.87, reasonable confidence); FY2029 on 2; FY2030 on 1 (not usable). Regression window 504 days is adequate, but a 2-year window on a stock that tripled and halved captures one regime, not a cycle.

**Data integrity note:** the price-history feed terminates 2026-07-15 ($486.65) while the quote ($327.98) and analyst notes (Oct–Nov 2026, prices $315–$385) imply a further ~30% decline. All price statistics above are consistent with the current quote, and the 60.8% drawdown corroborates it; the raw series is simply truncated. Third-party quotes show $348.52, so treat the exact level as $328–$349 (±6%).
