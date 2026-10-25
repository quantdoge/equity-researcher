# Fin Risk Analyst

- Symbol: NRG
- Elapsed: 127.7s

---
# NRG Energy, Inc. (NRG) — Financial Risk Assessment

**Sector:** Utilities / Independent Power Producers | **Data through:** FY2025 10-K (filed 2/24/26), Q2 2026 10-Q (filed 8/4/26), last price $177.79 (2/27/26)

---

## 1. Credit Risk Assessment — **SUB-INVESTMENT GRADE** (crossover BB+/BB)

| Agency | Rating | Outlook | Note |
|---|---|---|---|
| Fitch (5/8/26) | **BB+** IDR | Stable | Senior secured **BBB-/RR1**; senior unsecured **BB+/RR4** |
| S&P | **BB** | Revised to Stable from Positive | 'BBB-' issue-level on secured notes |
| Moody's | *Not confirmed* | — | Data gap |

NRG sits at the top of the high-yield band with secured debt rated investment grade — a classic crossover credit. **The single most important fact: Fitch states pro-forma 2026 gross EBITDA leverage rises to ~4.3x, "materially above" its 3.5x downgrade threshold**, and expects a return inside 3.5x only within 24 months of the 1/30/26 LS Power close. S&P similarly projects >4x at close declining to mid-3x. The rating is therefore **stable only on the assumption of successful deleveraging** — execution risk, not current cash flow, is what holds the rating.

**Altman Z-Score: 1.61 — Distress Zone.** The tool flags that x4 uses book equity (0.061), which understates a market-cap-based reading. I recomputed with market equity (~$37B / $35.1B liabilities): **Z ≈ 1.67 — still in the distress zone.** That is the meaningful finding: the distress signal is *robust* to the market-equity adjustment because it is driven by weak EBIT/assets (3.7%) and negative working capital, not by the x4 artifact. Z deteriorated from ~2.22 at FY2025 (grey zone) to 1.67 post-close.

**Piotroski F-Score: 5/9 (Moderate).** Positive ROA and op-cash-flow, no dilution, gross margin improvement. Failing: **higher leverage (F5), negative equity change (F6), ROA deterioration (F3), asset turnover deterioration (F9)** — precisely the deleveraging metrics that matter here.

---

## 2. Key Financial Risk Metrics

| Metric | FY2025 (12/31/25) | Q2'26 / TTM (6/30/26) | Assessment |
|---|---|---|---|
| Total debt | $16,766M | **$23,467M** | +40% on LS Power |
| Cash | $6,927M *(acquisition-earmarked)* | **$162M** | ⚠️ Collapsed |
| Net debt | $9,839M | **$23,305M** | 2.4x increase |
| Debt / Equity | 9.97x | **4.83x** (equity rebuilt to $4,855M) | Extreme |
| Debt / Assets | 0.58 | 0.59 | High |
| Net debt / EBITDA (GAAP) | 3.0x | **7.4x** (TTM EBITDA $3,154M) | ⚠️ |
| Net debt / Adj. EBITDA | 2.4x | **~4.3x** (Fitch pro-forma) | ⚠️ Above 3.5x threshold |
| Interest coverage (EBIT/int.) | 2.4x | **~1.4x** (TTM EBIT $1,483M / int. ~$1,076M) | ⚠️ Thin |
| Coverage on Adj. EBITDA | 5.3x | ~4.5–4.7x | Adequate |
| Current ratio | 1.64 | **0.97** | ⚠️ Below 1.0 |
| Quick ratio | 1.58 | ~0.90 (est.) | Weak |
| Cash ratio | 0.86 | **0.016** | ⚠️ Critical |
| Working capital | +$5,118M | **–$322M** | Turned negative |
| Equity / Assets | 5.8% | 12.2% | Thin |
| **Tangible equity** | — | **–$6,100M** (GW&I $10,955M vs equity $4,855M) | ⚠️ Negative |
| Altman Z | 1.61 | ~1.67 (mkt-adj.) | Distress |
| Piotroski F | 5 | 5 | Moderate |
| FCF (OCF – capex) | $766M | $348M (TTM) | Weak |
| FCF yield | 3.87% *(tool)* → **~2.1%** adjusted | ~0.9% on TTM FCF | Below cost of capital |

**Liquidity caveat:** FY2025's $6.9B cash was bridge/escrow funding for the LS Power close, not operating cushion. Post-close cash is $162M against $9,975M of current liabilities and $1,512M of short-term debt. NRG is now **fully dependent on revolving credit facilities** — this is the most acute risk in the capital structure. TEF low-interest financing ($1.15B across three Texas projects) partially offsets funding needs.

---

## 3. Market Risk Profile

| Metric | 1-Year | 3-Year |
|---|---|---|
| Annualised volatility | **51.0%** | 51.5% |
| Beta vs SPY | 1.25 | **1.53** |
| Max drawdown | 47.9% | 47.9% |
| Sharpe (rf=0%) | **–0.75** | +0.44 |

NRG is trading like a **high-beta, cyclical merchant power name, not a utility** — 51% vol is roughly 3x the utility sector norm and beta of 1.25–1.53 means a market drawdown is amplified. The **negative 1-year Sharpe (–0.75)** is a warning: over the past twelve months investors were not compensated for that volatility. The 47.9% max drawdown is a fair proxy for realistic peak-to-trough pain. Recent price action is highly event-driven (Dec 2025 slide to $148, Jan 2026 low of $142, rebound to $183 in late Feb 2026) — a ~25% round trip in three months.

> **Data integrity flags:** (a) The company profile and `calculate_fcf_yield` use a market cap of ~$19.8–20.9B at a price of $99.38, which is **stale** versus the $177.79 last close (~$37B market cap on ~210M shares). I have adjusted FCF yield accordingly; the tool's 3.87% overstates it by ~1.8pts. (b) Q1 2026 interest expense is reported as **–$285M** (negative), an apparent data error; I normalised TTM interest to ~$1,076M. (c) Price data ends 2/27/26 while financials run to 6/30/26.

---

## 4. Downside Scenario: –20% Revenue (FY2025 base, gross margin % held, SG&A fixed)

| Line item | Base | Stress (–20% rev) | Change |
|---|---|---|---|
| Revenue | $30,710M | $24,568M | –$6,142M |
| Gross profit (21.8%) | $6,710M | $5,368M | –$1,342M |
| SG&A (held) | $4,840M | $4,840M | flat |
| **Operating income** | **$1,850M** | **$528M** | –72% |
| EBITDA | $3,285M | $1,963M | –40% |
| Interest expense | $772M | $772M | fixed |
| **Interest coverage** | **2.4x** | **0.68x** | ⚠️ Breach |
| Net debt / EBITDA (post-deal $23.3B) | ~7.4x | **~11.9x** | Covenant territory |
| FCF | $766M | **~–$577M** | Turns negative |

**Covenant/rating consequence:** coverage falls below 1.0x and adjusted leverage would blow through 6x, well past the 3.5x downgrade threshold — a multi-notch downgrade and loss of the BBB- secured rating is the realistic outcome, raising refinancing cost on the $1.5B of 2026-27 maturities.

**Critically, this downside is not hypothetical.** FY2023 is the historical template: gross margin collapsed to 8.0% (from 13.0%), producing a **GAAP net loss of –$202M, operating cash flow of –$221M, and free cash flow of –$819M** — while still paying $381M of dividends and buying back $1,172M of stock. Gross margin has ranged 8.0%–21.8% over four years. **The margin buffer to a 1.0x coverage breach is only ~3.5 points of gross margin** — and the company has violated that buffer within the last three years.

A milder –10% revenue case yields ~$1,179M EBIT and ~1.5x coverage — strained but survivable.

---

## 5. Overall Financial Risk Rating: **HIGH**

Rationale: the business generates real cash flow (FY2025 adjusted EBITDA $4.1B, FCFbG $2.2B) and has no imminent maturity wall — 2025-26 issuance ($4.9B in Oct 2025; 2031/2033/2034 refinancing in April 2026) pushed out maturities. But the balance sheet carries **negative tangible equity, ~4.3x pro-forma leverage above the rating agency's downgrade trigger, near-zero cash, a sub-1.0 current ratio, and a 51%-vol equity with a bankruptcy-zone Z-score.** Interest coverage on a GAAP basis of 1.4x leaves almost no room for margin error in a business whose margins have historically swung violently.

## 6. Key Red Flags

1. **Leverage bought above the downgrade threshold** — 4.3x pro-forma vs Fitch's 3.5x; rating stability contingent on delivering ~$5.5B+ EBITDA by 2028.
2. **Negative tangible equity of –$6.1B** — $11.0B of goodwill/intangibles exceeds total equity of $4.9B. Book solvency is goodwill-dependent.
3. **Liquidity evaporation** — cash $6,927M → $162M; current ratio 1.64 → 0.97; cash ratio 0.016. Full revolver dependence with $1,512M short-term debt.
4. **GAAP coverage thin and noisy** — 2.4x → ~1.4x TTM; the 4.5x adjusted figure relies on excluding mark-to-market swings that have produced two GAAP loss quarters in the last six (Q2'25, Q1'26).
5. **FCF conversion weak** — TTM FCF $348M against $23.3B net debt (1.5%); capex tripled to $1,147M and growth capex is consuming nearly all operating cash flow.
6. **Shareholder returns ahead of deleveraging** — $1.6B returned in 2025 and $1.13B in H1 2026 (buybacks + dividends) while leverage rose. This prioritises equity holders over credit quality.
7. **Altman Z in distress zone on both book and market equity** — a rare robustness of the signal.
8. **Negative 1-year Sharpe with 51% volatility and 48% max drawdown** — the equity is priced as a merchant-power growth story, leaving it exposed to a sharp re-rating if leverage reduction slips.

**Data gaps:** full contractual debt maturity ladder not retrieved (only confirmed: 2031/2033/2034 notes; $1,512M current maturities); Moody's rating unconfirmed; CDS spreads unavailable; Q1 2026 interest expense is a corrupt data point; market cap/price fields in profile and FCF-yield tool are stale and were manually corrected.
