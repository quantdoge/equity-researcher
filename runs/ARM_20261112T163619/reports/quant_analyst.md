# Quant Analyst

- Symbol: ARM
- Elapsed: 48.5s

---
## ARM Holdings (ARM) — Quantitative Factor & Risk Report

**Price $202.34 | Mkt cap ~$216bn | Sector: Technology / Semiconductors | IPO 2023-09-14**

---

### 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | 1 / 10 | **5 of 5 (last)** | **Strong Sell** — most expensive in peer set on all four multiples |
| **Momentum** | 3 / 10 | 3 of 4 | **Sell** — negative 12-1 (−10.85%), deteriorating short-term (−16.64%) |
| **Quality** | 5 / 10 | 3 of 5 | Neutral — elite gross margin, but low/falling ROE & ROIC |
| **Low Vol** | 1 / 10 | Bottom decile | **Strong Sell** — 91.2% vol, β 3.81, −62% max DD |
| **Earnings Revision** | 5 / 10 *(unverified)* | n/a | **Neutral, low confidence** — tool output is spurious; see flag #6 |

**Value detail (trailing):** P/E 238.1x · P/B 26.1x · EV/EBITDA 151.5x · P/FCF 220.7x · no dividend.
Peer cross-section (TSM excluded — multiples corrupt, TWD/USD mismatch):

| | ARM | AMD | AVGO | NVDA | MU |
|---|---|---|---|---|---|
| EV/EBITDA | **151.5** | 131.9 | 52.9 | 27.7 | 8.0 |
| P/FCF | **220.7** | 143.4 | 66.4 | 42.0 | 15.4 |
| P/B | **26.1** | 15.3 | 22.0 | 25.8 | 6.6 |

Unanimously last on all four metrics — a clean bottom-quintile value score. Valuation is entirely a bet on out-year delivery: 238x trailing ($0.85 FY26 EPS), 66.8x FY2028E ($3.03), 32.3x FY2030E ($6.26).

**Quality detail:** Gross margin 92.5% (IP-licensing model), gross profit/assets 0.425 (Novy-Marx-positive, 3rd of 5), accruals **−5.79%** (best in peer set — conservative accounting, cash conversion ahead of earnings: OCF $1.52bn vs NI $0.90bn). But capital returns are weak and eroding: ROE 10.91% (FY25 11.58%, FY23 12.94%), ROIC 10.39% (FY25 11.49%, FY23 15.88%). Piotroski **F-Score 6/9** — failed on ROA improvement, gross-margin improvement, and share dilution. Revenue growth is steady (+22.8% FY26, +23.9%, +20.7%) but EPS grew only +13.3%.

**Momentum:** 12-1 return **−10.85%**; 63-day **−16.64%**. Short-horizon is *worse* than long-horizon — classic negative-momentum continuation, not a washout bounce. Trailing 12-month total return is still **+19.96%** ($168.68 → $202.34), so the stock is a former winner now in distribution. Peers: AMD +16.6%, NVDA −0.8%, AVGO −17.5%.

---

### 2. Price Statistics (252-day window, vs SPY)

| Metric | Value |
|---|---|
| Alpha (annualised) | **+68.58%** — *statistically insignificant* (see below) |
| Beta | **3.83** (vol-tool: 3.81) |
| R² | 0.366 |
| Annualised vol | **91.2%** |
| Sharpe (reported, 0% rf, arithmetic) | 1.148 |
| Sortino (reported) | 2.119 |
| **Max drawdown** | **−62.06%** |
| Idiosyncratic risk | 73.2% annualised (63.5% of variance unexplained) |

Max drawdown verified: peak close $439.46 (2026-06-18) → trough $166.72 (2026-11-05) = **−62.06%**. Current price is −53.96% from that peak.

**Two material caveats on the risk ratios:**
1. **Alpha is not significant.** Daily alpha 0.272% vs SE ≈ 0.290% (residual vol 4.61%/day, n=252) → **t ≈ 0.9, p > 0.3**. With R² of only 0.366, the +68.6% alpha is largely a handful of June melt-up days, not a durable edge. Do not allocate on this number.
2. **Sharpe 1.148 / Sortino 2.119 are arithmetic and flattered.** The 105.5% "annualised return" is the arithmetic mean annualised; the *compounded* 12-month return is +19.96%. On a geometric basis Sharpe is **≈0.17** (excess over ~4% rf ÷ 91.2% vol). The gap between 1.15 and 0.17 is pure volatility drag — the single most important number in this report.

---

### 3. Composite Quant Signal

**SELL** (composite 3.0/10; equal-weighted across five factors)

No factor offers support: value is worst-in-class, momentum is negative and decelerating, volatility is maximum, quality is only mid-pack with deteriorating returns on capital. The one genuinely strong attribute — negative accruals and 92% gross margin — is already priced at 221x free cash flow. The verified analyst-flow signal (six of ten recent notes *lowered* targets) contradicts the tool's "upgrade" output.

---

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — active, not hypothetical.** 63-day (−16.6%) underperforming 12-1 (−10.9%) signals continued de-rating. There is no short-term reversal cushion.
2. **Beta amplification.** β 3.83 means a 10% SPY drawdown implies ~38% ARM drawdown. Position sizing must be on *contribution to risk*, not notional.
3. **Valuation compression.** 151x EV/EBITDA / 221x P/FCF requires ~35%+ EPS CAGR through FY2030. A single estimate cut compresses the multiple violently — already demonstrated by the −62% drawdown.
4. **Alpha unreliability / small effective sample.** IPO 2023-09-14 → <3 years of history; 252 obs is adequate for beta but the low R² makes alpha estimates unstable. Longer-window factor stats are unavailable — flagged as a genuine gap.
5. **Analyst dispersion is extreme.** Target range **$160 (Goldman, Sell) to $641 (Raymond James)** — a 4x spread around a $262.50 median (+30% vs spot). Wide dispersion with downward target revisions = rising model uncertainty, and median upside should not be read as conviction.
6. **Data-quality failures (material).** The revision tool compared **FY2031 EPS $10.72 vs FY2030 EPS $6.26**, reporting "same-period" growth as a +71.3% revision — that is a spurious signal, not evidence of upgrades. The consensus FY2026 EPS series ($1.75) also conflicts with reported FY26 diluted EPS ($0.85), suggesting adjusted/unit inconsistency. The revision factor is therefore **unverified and excluded from the composite decision**. TSM peer multiples (P/E 1.24) were corrupt and excluded from ranking.
7. **Liquidity: NOT a concern.** ~5–8m shares/day (~$1.0–1.6bn), deep ADR. No liquidity discount warranted.
8. **Factor crowding: moderate-to-high.** ARM correlates 0.68 with AMD, 0.60 with SPY, 0.55 with AVGO, 0.47 with NVDA. As the highest-beta expression of the AI-semis trade, ARM is the most crowded *and* most fragile vehicle in a sector de-rating.

**Bottom line:** Statistically, the only robust findings here are that ARM is the most expensive and most volatile name in its peer group, with negative and worsening momentum and falling returns on capital. The headline alpha and Sharpe ratios do not survive scrutiny. Sell.
