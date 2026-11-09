# Quant Analyst

- Symbol: SITM
- Elapsed: 27.0s

---
## SITM — Quantitative Factor Report
**SiTime Corp. | Technology / Semiconductors | Price $416.92 | Mkt cap ~$10.4–12.5B (source discrepancy, see flags)**

### 1. Factor Scores

| Factor | Raw Value | Score (0–100) | Sector Rank* | Signal |
|---|---|---|---|---|
| **Value** | P/E −242.4 (n.m.), EV/EBITDA −4,539 (n.m.), P/FCF **300x**, P/B 9.0, FCF yield 0.33% | 15 | **6 / 6** | Strongly Negative |
| **Quality** | ROE **−3.71%**, GP/Assets **0.135**, accruals −0.1005, Piotroski **7/9** | 30 | **6 / 6** | Negative (accruals are the one bright spot, #1 of 6) |
| **Momentum (12-1)** | **+16.01%** | 55 | **4 / 6** | Neutral/Positive |
| **Low Vol** | Vol **94.5%**, beta **3.11**, max DD **60.6%** | 5 | **6 / 6** | Strongly Negative |
| **Earnings Revision** | **+22.82%** (FY28 EPS $20.17 vs $16.42) | 65 | **4 / 5** | Positive (upgrade) |

*Rank = percentile position within semi comp set {NVDA, AVGO, MU, AMD, TSM}, 1 = best. Composite = 0.25·Value + 0.25·Quality + 0.15·LowVol + 0.20·Momentum + 0.15·Revision = **32.8 / 100**.

**Peer cross-section (the reason Value/Quality rank last):** MU trades 9.3x earnings / 13.4x FCF with 61% ROE; NVDA 38x with 76% ROE and 74% GP/assets. SITM has *negative* trailing earnings and 300x FCF while sitting last on every quality level metric.

**Critical valuation nuance:** trailing multiples are noise because earnings ≈ 0. On forward estimates the picture changes materially — FY26E $11.92 (**35.0x**), FY27E $16.42 (**25.4x**), FY28E $20.17 (**20.7x**), vs revenue ramping $327M → $893M → $1,404M → $1,742M (**~75% 3-yr revenue CAGR**). The entire valuation rests on that ramp.

### 2. Price Statistics (252 trading days)

| Metric | Value |
|---|---|
| Alpha (annualized, vs SPY) | **+28.13%** |
| Beta (regression) | **3.12** (profile: 2.91; low-vol tool: 3.11) |
| R² | **0.22** |
| Annualized return | +43.23% |
| Annualized volatility | **93.48%** |
| Sharpe | **0.462** (vol tool's 0.605 uses a different return convention) |
| Sortino | **0.847** |
| Max drawdown | **−60.62%** |

**Statistical significance check on alpha:** residual vol = 93.5% × √(1−0.22) ≈ 82.6% annual ≈ 23.8%/month; monthly alpha ≈ 2.34%; SE = 23.8/√252 = 1.50% → **t ≈ 1.56 (p ≈ 0.12)**. The alpha is *not* significant at conventional levels. R² of 0.22 means 78% of SITM's variance is idiosyncratic — this is a 3.1-beta, single-story stock, not a market proxy. Sortino (0.847) being nearly 2x Sharpe (0.462) confirms the return distribution is driven by a few very large up-months, not consistency.

### 3. Composite Quant Signal: **NEUTRAL** (speculative-growth profile)
Two of five factors are bottom-decile (value, low vol), quality is bottom-decile, and only revisions + momentum carry the score. This is not a factor-compounder; it is a high-beta, estimate-dependent growth bet. Momentum (+16%) and the revision upgrade (+22.8%) prevent a Sell; the 300x P/FCF, −3.7% ROE, and 60% drawdown prevent a Buy. **Higher-conviction data needed before upgrading: sustained FCF inflection.**

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — HIGH.** Analyst notes in May–Aug 2026 carried targets of $800–900 with the stock printing $543–783. At $416.92, price sits ~47% below those prints while the 12-1 momentum window still shows +16%. That configuration (positive trailing momentum, deep live drawdown) is classic late-stage reversal — the 12-1 window is masking recent deterioration. The tool's −60.6% max DD understates the live peak-to-trough.
2. **Revision sample is tiny.** The +22.8% upgrade rests on **4 analysts** for FY28 (6 for revenue). FY27 has 8. This fails significance thresholds; a single analyst move can swing the score. Treat the revision signal as suggestive only.
3. **Factor crowding: none, but the inverse risk.** SITM is the anti-crowding trade — it ranks last on value/quality/low-vol, so it carries no crowding downside but also no defensive support if growth estimates slip.
4. **Earnings quality is actually defensible.** Accruals −0.1005 (2025), −0.132 (2024), −0.093 (2023): cash flow exceeds net income every year (2025 OCF +$87.2M vs net income −$42.9M). Losses are GAAP-driven (heavy SBC/D&A), not cash-burning. Piotroski 7/9 fails only on negative ROA and **share dilution (~+6%/yr: 22.2M → 23.1M → 25.0M shares).** Dilution is the quiet drag on per-share value.
5. **Liquidity/market-cap data conflict.** Profile shows $12.54B cap; valuation module implies $10.41B (24.97M shares × $416.92). Flagging rather than reconciling — use the diluted-share figure for per-share math.

**Data gaps / exclusions:** TSM's value-factor output (P/E 1.13, EV/EBITDA −0.04) is a currency-mismatch artifact and was excluded from value ranks. MU's revision score returned −100% on a zeroed current estimate — unusable, excluded (revision rank is 4 of 5, not 6). Peer revision scores use each stock's own far-dated consensus period, so they are directional, not strictly comparable. No peer-level Sharpe/Sortino computed; returns/risk ratios are SITM standalone vs SPY.
