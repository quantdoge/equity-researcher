# Quant Analyst

- Symbol: RIVN
- Elapsed: 25.3s

---
## RIVN — Quantitative Factor Report
**Rivian Automotive, Inc.** | Consumer Cyclical / Auto Manufacturers | Price $13.19 | Mkt cap ~$19.0B | F-Score **4/9 (Weak)**

---

### 1. Factor Scores

| Factor | Score / Raw Value | Peer Rank (of 6) | Signal |
|---|---|---|---|
| **Value** | P/E **-4.3**, EV/EBITDA **-6.33**, P/FCF **-6.28**, P/B **3.41** | 4th (bottom tercile) | **Negative** — all earnings-based multiples undefined/unusable; only P/B is readable at 3.41x, which is *expensive* for -79% ROE |
| **Momentum** | 12-1 return **-7.83%** | 3rd (median) | **Neutral/Negative** — underperforms in absolute terms, mid-pack cross-sectionally |
| **Quality** | ROE **-79.4%**, ROIC **-31.9%**, GrossProfit/Assets **0.97%**, Accruals **-19.3%** | 5th | **Negative** — only LCID is worse; accruals the one bright spot (cash burn < accounting loss) |
| **Low Vol** | Annualised vol **66.4%**, beta **1.90** (1yr) / **1.74** (2yr), Max DD **-43.3%** | 6th (worst) | **Strong Negative** — highest-volatility name in the comp set |
| **Earnings Revision** | FY2030 EPS est. **+$0.625** vs **-$0.255** prior → **+344.7%** | 1st | **Positive but low confidence** — 4 analysts only, 4+ years out |

**Comp set used:** TSLA, GM, F, NIO, LCID, RIVN (the provider's "Consumer Cyclical" sector is 60% mega-cap retail — AMZN, HD, MCD — so I built a native auto/EV peer group instead).

**Peer factor detail:**
| | 12-1 Momentum | GrossProfit/Assets | ROE | Accruals |
|---|---|---|---|---|
| TSLA | **+20.99%** | 12.40% | +4.58% | -7.95% |
| GM | -2.72% | 7.14% | +4.27% | -8.59% |
| **RIVN** | **-7.83%** | **0.97%** | **-79.36%** | **-19.29%** |
| F | -14.56% | 7.89% | -22.74% | -10.19% |
| NIO | -23.83% | — | — | — |
| LCID | -33.81% | **-14.98%** | -376.15% | +3.12% |

RIVN scores **top-quintile on nothing except the revision metric** — which rests on a 4-analyst sample.

---

### 2. Price Statistics

| Metric | 1-Year (252d) | 2-Year (504d) |
|---|---|---|
| Annualised return | — | **+8.38%** |
| Annualised volatility | **66.37%** | 63.59% |
| Beta vs SPY | **1.90** | **1.743** |
| Alpha (annualised) | — | **-26.55%** |
| R² vs SPY | — | **0.1125** |
| Sharpe (rf=0) | **-0.022** | **0.132** |
| Sortino (rf=0) | — | **0.235** |
| Max drawdown | **-43.25%** | — |

**Critical caveat on alpha:** R² of **0.11** means ~89% of RIVN's variance is idiosyncratic. The -26.6% alpha carries a very wide standard error — with 504 observations and this residual dispersion, alpha is not statistically distinguishable from zero at conventional thresholds. Treat beta (1.7–1.9) as robust; treat alpha as directional only.

Note the **Sharpe divergence**: 2-yr Sharpe is +0.132 while 1-yr is -0.022. The 2-year figure is a legacy of the Oct 2025–Dec 2025 melt-up ($14.68 → $22.45); it is not representative of the current regime.

**Actual peak-to-trough, Dec 2025 → Oct 2026:** $22.64 → $11.45 = **-49.4%**, materially worse than the reported 43% window max DD.

---

### 3. Composite Quant Signal: **SELL**

Four of five factors are negative, and the one positive is the least reliable:

1. **No valuation floor.** -$3.07 EPS, negative EBITDA and negative FCF mean no multiple-based support. At 3.41x book and -79% ROE, you pay a growth premium for a business destroying 24.5% of assets annually.
2. **Negative and unstable momentum.** -7.83% 12-1, with a full round-trip from $22.45 to $13.19 — a broken trend, not a base.
3. **Bottom-of-cohort quality.** Gross profit/assets of 0.97% vs TSLA 12.4%, GM 7.1%, F 7.9%. ROIC of -31.9% means capital is being consumed, not compounded.
4. **Worst risk profile in the group.** 66% vol, 1.9 beta, Sortino 0.235 — you are paid almost nothing per unit of downside.
5. **Only offset:** margins inflected (gross profit +$144M in 2025 vs -$1.2B in 2024) and FY2030 consensus flipped to profit — but that is a 2030 datapoint from 4 analysts, i.e. narrative, not evidence.

**What would upgrade this:** two consecutive quarters of positive operating cash flow plus upward revision in the *FY2026–27* consensus (currently -$2.12 / -$1.88), not the FY2030 number.

---

### 4. Key Quant Risk Flags

- **Thin estimate coverage (highest priority).** The +344.7% revision score uses **4 analysts on FY2030**; revenue has 15–19 contributors near-term. This is a long-horizon extrapolation being reported as revision momentum. Do not size on it.
- **Beta instability / high market sensitivity.** Beta ranges 1.62 (provider), 1.74 (2yr OLS), 1.90 (1yr). Rising beta into a declining price is the classic signature of a de-rating high-beta name.
- **Momentum reversal risk is symmetric and violent.** Single-day moves of +11.4% (2025-11-05) and +8.4% (2026-02-13) on 3–4x normal volume. Short interest and options-driven gaps make any negative signal unreliable for tight-stop implementation.
- **Dilution is a persistent drag, not a one-off.** Shares 913M → 947M → 1,013M → **1,186M (+30% in 3 yrs, +17% in 2025 alone)**. F-Score component F7 (no dilution) scores **0**. Per-share value is being diluted faster than operating losses narrow.
- **Factor crowding: not a concern.** With 89% idiosyncratic variance, RIVN is a single-name thesis, not a factor exposure.
- **Liquidity: adequate.** ADV ~35–50M shares (~$500M+); no liquidity constraint.
- **Data integrity caveats.** (a) Provider market cap $19.0B at $13.19 implies ~1.44B shares vs 1.186B diluted in the valuation file — a ~20% discrepancy that likely reflects post-period dilution or stale share count. (b) Enterprise value $16.2B implies only ~$0.57B net debt, which is inconsistent with Rivian's cash position; treat EV/EBITDA magnitude as unreliable. Directional conclusions are unaffected since both revisions worsen the picture, not improve it.

---

### 5. Context: analyst targets vs. the model

Ten recent PTs span **$14–$22**, median **~$16.75** → ~+27% implied upside vs $13.19. But note the pattern: through Jul-2026 targets were being *raised* (RBC 14→16, MS 13→14, WF 15→16, UBS 16→17, Piper upgrade to OW) while the stock traded $15–18. On **2026-10-30**, with the stock at $11.45, Cantor and Needham both **cut** to $16/$18. The sell-side is following price down. That is negative revision momentum in the *rating* channel even as the long-dated EPS line moves up — and the quant evidence sides with the ratings.
