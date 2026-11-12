# Quant Analyst

- Symbol: CRWV
- Elapsed: 64.2s

---
## CRWV (CoreWeave) — Quantitative Factor Report
**Price $58.33 · Mkt cap $25.4B · EV $51.2B · Sector: Technology / Software-Infrastructure · IPO 2025-03-28**

---

### 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | 34/100 | 3rd of 5 on EV/EBITDA (median) | **Negative** — EV/EBITDA 20.75x sits mid-pack (ORCL 14.9x, MSFT 19.2x, NVDA 27.8x, PLTR 258x), but P/E −20.8 and P/FCF −3.5 are unusable. FY25 FCF −$7.25B on $10.3B capex ⇒ **negative FCF yield**. No dividend. |
| **Momentum** | 22/100 | Bottom quintile | **Negative** — 12-1 momentum **−22.5%**, 6-1 **−21.8%**. Price −57.7% below the 05/06/26 close peak of $137.98. |
| **Quality** | 26/100 | Bottom quintile | **Negative** — ROE **−35.0%**, ROIC **−0.14%**, ROA −2.4%, gross-profit/assets 0.075 (weak). Piotroski **F=5/9** (fails: ROA<0, net dilution, GM decline, asset-turnover decline). *Only bright spot:* accruals ratio **−8.6%** — cash conversion is genuinely good (OCF $3.06B vs net loss $1.17B). |
| **Low Vol** | 3/100 | Worst in universe | **Strong Negative** — annualised vol **102.3%**, beta 3.49 (SPY), max drawdown **−68.4%**. Highest-risk profile of any $25B+ cap. |
| **Earnings Revision** | 20/100 (overridden) | Bottom quintile | **Negative** — see flag below. Tool returned **+158.9%**, but for **period 2030-12-31** ($17.99 vs $6.95), not a forward-4Q period. **Not a valid revision signal.** Real evidence contradicts: **7 of 10 recent price targets were cut** (Piper $153→124, UBS $120→105, MS $99→70, Mizuho→68, Stifel→60, DA Davidson→45), 1 reiterated, 0 raised. |

**Composite factor z-score ≈ −1.4σ (bottom decile).** Only one factor of five is not negative, and that one is a data artifact.

---

### 2. Price Statistics

| Metric | 252-day | 126-day |
|---|---|---|
| Alpha (annualised, vs SPY) | **−56.98%** | −102.52% |
| Beta (vs SPY) | **3.51** | 3.62 |
| R² | 0.244 | 0.239 |
| Sharpe | **−0.176** (vol-tool: −0.047) | −0.961 |
| Sortino | **−0.311** | −1.772 |
| Annualised vol | 100.2% | 108.5% |
| Max drawdown | **−68.36%** | — |

**Path:** IPO $40.00 → peak close $183.58 (06/20/25, +359%) → trough close $43.66 (11/05/26, −76% from peak) → $58.33 now (+33.6% off the low; **−68.2% from peak**). Buy-and-hold since IPO: **+45.8%**.

**Correlations (252d):** ORCL **0.65** (tightest — the AI-datacenter/neocloud complex), NVDA 0.51, SPY 0.49, MSFT 0.25, PLTR 0.25.

---

### 3. Composite Quant Signal: **SELL**

Four of five factors are bottom-quintile and the fifth is invalid. 102% vol with a 3.5 beta and −68% drawdown is not a compensated risk profile: **no metric here is statistically distinguishable from noise.**

**Statistical significance — the honest caveat:** with 102% annualised vol, the standard error on a 1-year mean return is ~102%. Alpha t-stat ≈ **−0.65**; return t-stat ≈ **−0.18**. R² of 0.24 means **76% of variance is idiosyncratic**, so the 3.5 beta is itself unstable (the profile's 7.67 beta is not usable). **Nothing in this report is significant at 95%.** Only 411 trading days exist since IPO — one macro regime, and a 126-day window (n≈63 overlapping obs) is below any reasonable threshold. Treat as directional, not inferential.

*Also flag:* tool-reported annualised returns (−17.6% / −104.2%) are **arithmetic** (mean daily × 252) and materially overstate losses for a 100%-vol series. Realised price change 2025-11-12 → 2026-11-12 was **0.0%** ($58.33 → $58.33).

**The bull case the model cannot see:** Q3'26 revenue $3.66B, **+168% YoY**; gross margin 67.7%; TTM revenue $9.9B. This is a hypergrowth story, and factor models structurally penalise pre-profit capex-heavy compounders. The quant verdict is "sell," not "wrong" — but it says nothing about whether the growth option pays off.

---

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — live and violent.** Down 57.7% from the May peak, yet the stock has whipsawed ±30% in three separate 2026 episodes (Aug: 72→108; Oct: 89→44; Nov: 44→61). Both legs of the 12-1 signal disagree with the raw 1-month trend — a classic unstable-reversal tape.
2. **Factor crowding / single-theme correlation.** 0.65 correlation to ORCL and 0.51 to NVDA means CRWV adds **concentration, not diversification**, to any AI-infrastructure book. Beta 3.5 against SPY.
3. **Balance-sheet fragility is the real quant risk.** Net debt **$25.8B** vs $25.4B market cap (≈10x TTM EBITDA). **TTM interest expense $2.41B** vs ~$2.5–3.5B EBITDA — coverage under 1.5x, and interest is compounding faster than EBITDA (+172% YoY vs +~110%). Leverage this high converts a 100%-vol equity into a de facto option on refinancing conditions.
4. **Dilution.** Shares 506M → 559M over four quarters (**+10.5%**), and this is what fails F-score item 7. EPS revisions must outrun the share count.
5. **Liquidity is *not* a concern** — $2–8B daily dollar volume, no constraint. The gap here is *price stability*, not tradeability.
6. **Revision data gap.** No near-term consensus EPS series was retrievable (FMP endpoint unavailable on plan). The revision factor is proxied by analyst price-target direction, which is a weaker, noisier substitute. **Flag this gap in the memo.**

**Data caveats:** Q3'26 income row reports D&A = 0, which understates that quarter's EBITDA ($220M reported vs ~$1.8B on the Q2'26 D&A run-rate) — EV/EBITDA of 20.75x is therefore inconsistent with the quarterly build and should be treated as approximate. Peer set returned by the screener is mega-cap Technology, not neocloud comparables (NBIS, IREN, APLD); true peer multiples were unavailable.
