# Quant Analyst

- Symbol: UBER
- Elapsed: 50.0s

---
## UBER — Quantitative Factor & Risk Assessment

**Data note upfront:** two material data-integrity issues. (1) FMP classifies UBER as "Technology / Software – Application"; its `get_sector_peers` output is mega-cap semiconductors (NVDA, AAPL, MSFT), which are **not economically comparable**. I substituted a hand-built platform/ride-share/travel peer set (LYFT, DASH, ABNB, BKNG) for all cross-sectional ranks. (2) The factor/risk tool suite appears computed on an **earlier data vintage** (~late-2025) than the price history (through 2026-04-30) and the analyst-target feed (through 2026-10). Where they conflict, I report both and say which I trust.

### 1. Factor Scores Table

| Factor | Score | Sector Rank (true peers) | Signal |
|---|---|---|---|
| **Value** | +1.0 | **2 of 5** — EV/EBITDA 22.0x; 2nd cheapest after BKNG (14.6x); ahead of ABNB 36.8x, DASH 47.9x, LYFT 62.9x | Attractive |
| **Momentum (12-1)** | **−1.5** | **4 of 4** — UBER −5.2% vs ABNB +13.2%, DASH +0.3%, LYFT −4.1% | Negative (worst in group) |
| **Quality** | +1.5 | **2 of 4** — signal "high"; ABNB marginally better | Attractive |
| **Low Vol** | 0.0 | Mixed — see below | Neutral |
| **Earnings Revision** | 0.0 | N/A | **Unreliable — see caveat** |

**Factor detail**

- **Value** — P/E 14.87 (on diluted EPS $4.73), P/B 5.31, EV/EBITDA 21.98, P/FCF 15.27, no dividend. Cheap on earnings and FCF, expensive on book (BVPS $13.25). **Critical caveat:** trailing P/E is flattered — FY2025 net income of $10.05B sits on EBIT of only $6.24B, i.e. ~$3.8B of non-operating/tax benefit. On consensus: FY26E EPS $3.36 → **22.2x**, FY27E $4.44 → **16.8x**. EV/EBITDA 22x is the honest multiple, and it is mid-pack, not cheap.
- **Momentum** — 252-day ex-last-21 return **−5.18%**. From raw series: peak close $100.10 (2025-10-06) → trough $69.18 (2026-03-27) = **−30.9%**; 6-month return −22.7%. The only bullish print is the **last month: +6.7%** ($69.91 → $74.61) — a nascent reversal, not yet a trend.
- **Quality** — ROE 35.8%, ROA 16.3%, **ROIC 13.86%** (up from 4.53% FY23 and 8.25% FY24 — genuine operating improvement). Gross profit/assets 0.3346 (Novy-Marx). **Accruals ratio −0.0007 — essentially zero**, a clean earnings-quality reading (FY24 was +0.0531, so this is an improvement). Piotroski F-Score **7/9** (fails: ROA improvement, asset-turnover improvement). Note ROE is also inflated by buybacks ($6.52B repurchased in FY25 shrinking the equity base) and SBC of $1.83B (3.5% of revenue).
- **Low Vol** — Annualised vol **35.3%** (high in absolute terms), regression **beta 0.773** vs SPY, max drawdown 22.82% (tool) / **30.9%** (computed from raw series — I trust the latter). Genuinely favourable: **correlation with SPY of only 0.288**, the lowest of the four peers (LYFT 0.382, ABNB 0.388, DASH 0.391) — real diversification value. Peer correlations 0.53–0.57, so it is a sector-risk taker, not a diversifier within its own group.
- **Earnings Revision** — tool reports **+12.55% "upgrade"**. **Do not use this number.** It compares FY2030 EPS of $7.295 against the FY2029 estimate of $6.48177 — that is the *implied growth rate between two different periods*, not a same-period revision. It is mechanically a growth rate. Only 11 analysts cover FY2030. Genuine revision evidence is mixed: PTs cluster constructively (BMO $119, Mizuho $112, Jefferies $110, Scotiabank $100, BTIG $100, Roth $100, median ≈$100 = **+34% implied upside** vs $74.61) but Wells Fargo & Susquehanna sit at $89–92 and Arete *downgraded* to Neutral. Dispersion is wide: FY2028 EPS range $3.73–$7.76 (±39% around the $5.58 mean).

### 2. Price Statistics

| Metric | 252-day | 126-day |
|---|---|---|
| Annualised return | **−17.12%** | +7.57% |
| Annualised vol | 35.78% | 37.04% |
| **Sharpe** | **−0.478** | +0.204 |
| **Sortino** | **−0.873** | +0.368 |
| **Alpha (ann., vs SPY)** | **−30.31%** | **−14.60%** |
| **Beta** | 0.777 | 0.591 |
| **R²** | **0.0835** | **0.0393** |
| Max drawdown | 22.82% (tool) / 30.9% (raw series) | — |

The sign flip between windows is the whole story: the 252-day window captures the Oct-2025→Mar-2026 de-rating; the 126-day window captures the partial recovery off the $69 low. Note the `calculate_price_volatility` Sharpe (−0.544) disagrees with `calculate_sharpe_sortino` (−0.478) for the identical window — differing vol/return conventions in the two tools; I report the dedicated Sharpe/Sortino tool as primary.

**Statistical significance warning:** R² of 0.084 means only ~8% of UBER's variance is market-explained. The beta of 0.777 has a wide standard error and the −30.3% alpha is correspondingly imprecise — treat "alpha" here as "negative idiosyncratic performance," not a precisely estimated −30%. Beta also conflicts with the company-profile field (1.265, 5Y monthly), so the two estimates bracket a wide range.

### 3. Composite Quant Signal: **NEUTRAL**

Score = (Value +1.0, Quality +1.5, Momentum −1.5, Low-Vol 0.0, Revision 0.0) → mean **+0.2**.

The value and quality factors genuinely support the name — ROIC has tripled in two years, accruals are nil, FCF is $9.76B (P/FCF 15.3), and it is the cheapest EBITDA multiple in its peer group bar BKNG. But it carries the **worst momentum in the peer set, the deepest drawdown, and the most negative alpha**. Two of five factors are unavailable or non-credible. A stock that is cheap-and-high-quality but de-rating with negative alpha is a **watchlist candidate with a catalyst requirement, not a buy**. Upgrade to Buy requires 12-1 momentum to turn positive; downgrade to Sell on a break below the $69.18 March low.

### 4. Key Quant Risk Flags

1. **Momentum reversal / downtrend intact** — 4th of 4 peers, −30.9% peak-to-trough, still below the 200-day trend. The +6.7% one-month bounce is unconfirmed.
2. **Earnings-quality illusion on P/E** — $10.05B net income vs $6.24B EBIT. The 14.9x headline P/E understates the real multiple by ~50%; forward P/E is 22.2x. Anything citing "UBER trades at 15x" is using a distorted denominator.
3. **Tool-level data integrity** — the revision factor is a cross-period artifact (+12.55% is 2029→2030 growth); sector classification and peer set are wrong; PT timestamps post-date the price series; vol-tool and Sharpe-tool disagree; max-drawdown understated by ~8pp. Quant outputs on this name should be re-derived from raw statements.
4. **Factor-model validity** — R² = 0.084. Beta and alpha from this regression are near-uninformative; do not use a 0.77 beta to size a hedge without widening the band (profile beta says 1.265).
5. **Sell-side dispersion / thin long-horizon coverage** — FY2028 EPS ±39%; only 11 analysts on FY2030. Wide-dispersion estimates are a low-reliability revision signal.
6. **SBC dilution offset** — $1.83B SBC (3.5% of revenue) against $6.52B of buybacks; GAAP ROE of 35.8% is partly a shrinking-equity artifact. Not crowded or illiquid (ADV ~15–20M shares), so crowding and liquidity flags are **not** triggered.
