# Fin Risk Analyst

- Symbol: NTSK
- Elapsed: 84.0s

---
I have sufficient data. Writing the assessment now.

---

# NTSK (Netskope, Inc.) — Financial Risk Assessment

**Company:** Netskope — cloud security / SSE platform ("Netskope One"). IPO 2025-09-18 (Nasdaq). Market cap ≈ **$4.9B** at $11.89 (Feb 13, 2026). *Note: the profile's $9.8B market cap is stale (based on the $23.99 IPO-era price); actual shares ≈ 409M × $11.89 ≈ $4.86B, consistent with the FCF tool's ~$5.1B.*

---

## 1. Credit Risk Assessment — **Sub-Investment Grade (unrated), LOW near-term default risk**

Netskope is a **net-cash, cash-generative-on-FCF, but GAAP-unprofitable** growth SaaS issuer. The credit picture is bifurcated:

- **Solvency is not the issue.** Cash & ST investments of **$1,158M** against **$755M total debt** = **~$403M net cash**. FY26 (ended 1/31/26) delivered the company's **first positive free cash flow (+$15.2M)** and positive operating cash flow (+$38.1M).
- **The GAAP losses are largely an IPO artifact.** FY26 operating margin of **-92.0%** looks alarming, but **SBC was $516.2M (73% of revenue)** — an IPO-triggered RSU vesting spike. **Ex-SBC, operating margin is ~-19%** and ex-SBC EBITDA ≈ **-$90.5M**. This is a normal pre-scale SaaS profile, not a distress one.
- **Debt is a single convert, extended and PIK-capable.** The long-term debt is principally **3.75% Convertible Senior PIK-Toggle Notes**, originally due 2027 and **amended to 2028**. The PIK toggle lets Netskope defer cash interest (explaining the $0 interest-expense line — a reporting artifact, not zero economic cost). Holders can convert ~9 months post-IPO; the company can call the notes ~1 year post-IPO. **IPO net proceeds (~$992M) were explicitly raised partly to retire this CB.** With $1.16B cash, a 2028 repayment of ~$744M is affordable (would consume ~64% of liquidity) — **no refinancing cliff.**
- **No maintenance covenants of consequence** on a convertible; the real "covenant" is liquidity, which is ample.

**Rating rationale:** Unrated, implied **BB-/B+ high-yield profile** on the negative retained earnings (-$2.63B) and GAAP losses, but upgraded in practical terms by net cash, positive FCF, and improving gross margins. **Default probability over 12–24 months: low.**

---

## 2. Key Financial Risk Metrics Table

| Metric | Value | Read |
|---|---|---|
| Revenue (FY26) | $709.0M (+31.7% YoY) | Strong, consistent ~32% growth |
| Gross margin | 68.1% (FY25 64.6%, FY24 59.8%) | **Expanding** +350/+480 bps — quality signal |
| Operating margin (GAAP) | **-92.0%** | Distorted by $516M SBC |
| Operating margin (ex-SBC) | **~-19.2%** | True underlying economics |
| SBC / revenue | **72.8%** | Extreme — IPO vesting spike; major dilution flag |
| EBITDA | -$606.7M (adj. ex-SBC ≈ -$90.5M) | Negative → **leverage multiples not meaningful** |
| Debt / Equity | **3.88x** | High, but artifact of thin book equity ($195M) |
| Debt / Assets | 0.43x | Moderate |
| Net Debt | **-$403M (net cash)** | Balance-sheet strength |
| Net Debt / EBITDA | 0.66x (tool) | **Not meaningful** (negative EBITDA) |
| Interest coverage | n/a (interest exp = $0 reported) | **Data gap** — convert coupon ~$28M/yr, PIK-deferrable |
| Current ratio | **2.13x** | Strong |
| Quick ratio | 2.12x | Strong (asset-light, no inventory) |
| Cash ratio | **1.70x** | Very strong |
| Working capital | $767.4M | Ample |
| Cash | $1,158.2M | Fortress liquidity |
| Equity / Assets | **11.0%** | Thin — losses have eroded book equity |
| **Altman Z-Score** | **-2.30 (Distress)** | Driven by negative EBIT (x3) & retained earnings (x2); market-cap-adjusted ≈ -0.5 — still weak but Z poorly suited to high-growth SaaS |
| **Piotroski F-Score** | **6 / 9 (Moderate)** | +OCF, improving ROA, lower leverage, GM expansion; **fails on dilution (F7) & asset turnover** |
| FCF (FY26) | +$15.2M (FY25 -$151.1M) | **Inflection to positive** |
| FCF yield | **0.3%** | Low (just turned positive; ~$4.9B cap) |

---

## 3. Market Risk Profile — **HIGH**

| Metric | Value | Comment |
|---|---|---|
| Annualized volatility | **75.9%** | Extreme (>2x broad market) |
| Beta vs SPY | **1.76** (tool) / **2.99** (FMP profile) | High market sensitivity — **discrepancy flagged**; both imply amplified drawdown exposure |
| Max drawdown | **70.0%** (tool) | My close-to-close check: peak $25.79 (9/22/25) → $11.49 (2/12/26) ≈ **-55%**; intraday peak $27.99 → $11.28 ≈ **-60%**. Tool's 70% likely uses a different reference — directionally correct: severe. |
| Sharpe ratio | 0.458 (tool) | **Unreliable** — only ~100 trading days of history; inconsistent with a -47% price move. Do not rely on it. |

**Market-risk read:** As a recent, unprofitable, high-multiple SaaS IPO, NTSK carries **very high equity risk**. Stock is **-47% from its $22.49 IPO close** and down ~58% from its intraday peak in under five months. Beta ~1.8–3.0 means a 20% market drawdown plausibly translates to a 35–60% drawdown here. *Data gap: <5 months of trading history — vol, beta, Sharpe and max-drawdown are statistically immature estimates.*

---

## 4. Downside Scenario Analysis — Revenue −20%

**Assumptions:** Gross margin holds ~68% (COGS partly variable cloud infra); non-SBC opex cut ~10% (limited by vesting rigidity/restructuring lag); SBC does not flex.

| Line | Base (FY26) | Stress (-20% rev) | Δ |
|---|---|---|---|
| Revenue | $709.0M | **$567.2M** | -$141.8M |
| Gross profit (68% GM) | $482.7M | $386.0M | **-$96.7M** |
| Non-SBC opex | $619M | $557M (-10%) | -$62M |
| **Adj. operating income (ex-SBC)** | **-$136M** | **~-$171M** | **-$35M** |
| GAAP operating income | -$652.6M | ~-$690M | wider |
| **FCF** | **+$15.2M** | **~-$50M to -$90M** | swing to burn |

**Liquidity through the downside:**
- Cash burn of ~$70M/yr against **$1,158M cash → ~16 years runway**; even a severe $200M/yr burn gives **~5.8 years**. **No liquidity or going-concern risk.**
- Convertible due **2028 (~$744M)**: repayable from cash even in stress (would consume ~64% of liquidity, leaving ~$400M+). The **PIK toggle** provides further optionality to defer cash interest. **No refinancing cliff.**
- Gross margin is the swing factor — if a 20% revenue drop forced price concessions (GM to ~62%), the FCF hit roughly doubles, but the balance sheet still absorbs it comfortably.

**Conclusion:** A 20% revenue decline is a **P&L and equity-valuation event, not a solvency event.** The company survives a prolonged downturn on its cash and now-positive FCF; the risk transfers to valuation/dilution, not default.

---

## 5. Overall Financial Risk Rating: **MODERATE (leaning elevated) — bifurcated**

- **Liquidity / solvency risk: LOW** — net cash $403M, current ratio 2.13x, cash ratio 1.70x, 5–16 yr stress runway, no 2026–27 maturities.
- **Profitability / dilution risk: HIGH** — GAAP operating margin -92%, SBC 73% of revenue, shares up from ~97.5M to ~214M WA (IPO + converts), Piotroski fails on dilution, equity only 11% of assets.
- **Market risk: HIGH** — 76% vol, beta 1.8–3.0, -47% since IPO, ~60–70% peak drawdown.

**Bottom line:** Not a credit/distress story — this is a **well-capitalized, FCF-inflecting growth company whose risk is concentrated in equity volatility and shareholder dilution, not balance-sheet solvency.** Altman's "Distress" reading is a false positive for this business model (negative retained earnings by design; Z's x4 uses book not market equity).

---

## 6. Key Red Flags

1. **SBC = 72.8% of revenue ($516M)** — massive IPO-triggered dilution; GAAP-to-economic gap is enormous. Watch whether this normalizes post-lockup or persists.
2. **Share count roughly doubled** (97.5M → 214M WA shares); Piotroski dilution flag (F7=0) confirms.
3. **Thin book equity (11% of assets); retained deficit -$2.63B** — little loss-absorption cushion on a book basis.
4. **Convertible overhang (~$744M, 3.75%, 2028)** — PIK toggle can *grow* principal if exercised; conversion/call windows open ~mid-2026 to ~Sept 2026, a potential equity-supply event. Reported $0 interest expense is a **data misstatement**, not true zero cost.
5. **Extreme equity volatility / deep drawdown** — recent-IPO with limited price history; beta 1.8–3.0 amplifies market stress.
6. **Valuation risk** — FCF yield just 0.3%; the equity is priced on growth durability, and the -47% post-IPO slide shows how violently sentiment can reprice.

## Data Gaps (explicitly flagged)
- **Credit rating & CDS spreads:** not available (unrated recent IPO).
- **Interest expense reported as $0** despite $755M of 3.75% convertibles — actual cash interest (~$28M/yr) is obscured by PIK/reporting; interest coverage **not computable**.
- **Debt maturity schedule detail** beyond the 2028 convert not provided by tools (inferred from SEC 8-K / press).
- **Peer multiples:** sector tool returned only mega-caps (AAPL, MSFT, NVDA) — **not meaningful comps** for a $5B newly-public SaaS; relative valuation unassessed.
- **Price-derived metrics (vol, beta, Sharpe, max DD) rest on <5 months of data** — statistically immature; Sharpe figure appears internally inconsistent and was not relied upon.
- **Yield curve data dated 2026-11-20** (future-dated vs price data) — treated as indicative only (10Y ~5.13%, 2s10s +39bps, not inverted).
