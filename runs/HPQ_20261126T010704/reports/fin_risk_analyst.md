# Fin Risk Analyst

- Symbol: HPQ
- Elapsed: 69.4s

---
## 1. Credit Risk Assessment

**Rating: INVESTMENT GRADE (lower-medium BBB band).** Confirmed live ratings: **Moody's Baa2 / S&P BBB / Fitch BBB+, all Stable outlook** (HP investor relations).

HPQ is a low-leverage, high-cash-generation business whose apparent "distress" signals are **structural artifacts of the PC/printer working-capital model and a 20-year buyback programme**, not credit deterioration. Leverage is *falling*, coverage is *improving*, and FCF covers the dividend 2.9x.

⚠️ **Critical data-integrity caveat — read before using any tool output.** The FY2026 (period_end 2026-10-31) income statement is corrupted: Q4 revenue is recorded as **–$28,519M**, which summed into a FY2026 revenue of $16,004M and a FY2026 net income of $769M. Verified against three independent sources: (a) the Q4 FY26 press release ($16.0B quarterly, **$60.5B full year**), (b) the cash-flow statement (FY2026 net income **$2,425M**), and (c) the sum of the uncorrupted Q1–Q3 rows ($44,523M revenue, $1,656M net income). **Consequently the `calculate_leverage_ratios`, `altman_z_score`, and any annual-row metric are materially wrong** (net debt/EBITDA reported 2.83x vs. true ~1.15x; interest coverage returned null; equity/retained-earnings fields zeroed). All figures below are reconstructed from quarterly rows + cash flow + press release.

## 2. Key Financial Risk Metrics Table

| Metric | FY2026 (recon.) | FY2025 | FY2024 | FY2023 | Read |
|---|---|---|---|---|---|
| Revenue | $60.5B | $55.3B | $53.6B | $53.7B | +9.4% |
| EBITDA | ~$4.23B | $4.09B | $4.72B | $4.47B | flat/↓ |
| Total debt | $9,275M | $10,882M | $10,899M | — | deleveraging |
| Cash | $4,394M | $3,690M | $3,238M | — | ↑ |
| Net debt | $4,881M | $7,192M | $7,661M | — | ↓ 36% |
| **Net debt / EBITDA** | **~1.15x** | 1.76x | 1.62x | ~1.6x | **Strong** |
| Total debt / EBITDA | ~2.19x | 2.66x | 2.31x | — | Moderate |
| Debt / assets | 19.5% | 26.0% | 27.3% | — | Low |
| Market leverage (D/(D+E)) | 24.8% | — | — | — | Low |
| **EBIT / interest** | **~8.1x** | 6.3x | 6.4x | 5.3x | **Improving** |
| EBITDA / interest | ~10.4x | 8.1x | 7.8x | 6.5x | Improving |
| Current ratio | 0.81 | 0.77 | 0.72 | — | Sub-1, structural |
| Quick ratio | 0.46 | — | — | — | Weak (inventory-heavy) |
| Working capital | –$6,796M | –$8,805M | –$7,927M | — | Negative, structural |
| Cash / liabilities | 0.09 | — | — | — | Thin buffer |
| Altman Z (book equity) | **0.23 (Distress)** | — | — | — | **Miscalibrated** |
| Altman Z (mkt-cap x4, my calc) | ~1.63 (Distress) | — | — | — | Grey/distress boundary |
| Piotroski F-Score | 6 / 9 (Moderate) | — | — | — | Fair |
| FCF | $3,185M – $3.3B | $2,800M | $3,157M | $2,962M | Stable |
| **FCF yield** | **11.1%** | — | — | — | Very high |
| FCF margin | 5.3% | 5.1% | 5.9% | 5.5% | Flat |
| Gross margin | 19.8% | 20.0% | 22.1% | 21.4% | **Compressing** |

**Peer context (my calc, DELL FY Jan-2026):** net debt/EBITDA 1.69x, interest coverage 5.22x, current ratio 0.91, working capital –$5.7B, equity/assets –2%, D/E –12.75x, FCF yield 4.2%. This proves HPQ's sub-1 current ratio and near-zero/negative equity are **industry-normal**, not idiosyncratic. On every leverage and coverage measure HPQ is **better than DELL**, and its FCF yield is 2.6x higher.

**Z-score caveat:** the 0.23 reading is an artifact — x2 was fed retained earnings = 0 (true ≈ –$1.9B) and x4 uses book equity of $527M. Recomputing with market cap ($28.1B) gives **Z ≈ 1.63**, still technically distress-zone but properly reflecting a structurally asset-light-on-book, payables-funded business. Treat Z as **not decision-useful here**.

## 3. Market Risk Profile

| Measure | 3-Year (756d) | 1-Year (252d) |
|---|---|---|
| Annualised volatility | 42.7% | 51.2% |
| Beta vs SPY | 0.97 | 0.49 |
| Max drawdown | 51.2% | 24.3% |
| Sharpe (0% rf) | 0.19 | 1.66 |

Price $31.15, market cap $28.09B (Nov 25, 2026). Profile beta 1.21.

- **Volatility is high and rising** (~43–51%), well above large-cap hardware norms.
- **Beta is unstable and falling** (1.21 profile → 0.97 3-yr → 0.49 1-yr). Recent evidence: HPQ trades on **idiosyncratic PC/memory-cycle and earnings news, not market direction** — e.g., –9.6% on 30-Oct-2026 and +11.5% on 25-Nov-2026 (Q4 print). Good diversification, poor downside protection in a sector-specific shock.
- **Gap risk is the dominant market risk**, not slow beta drift. The 51% 3-year drawdown dwarfs the 24% 1-year figure — a full half of peak value has been erased within the window.
- ⚠️ **Internal inconsistency flagged:** 1-yr Sharpe of 1.66 with 51% vol implies ~85% return, but the stock rose roughly 25–30% over that period. The 1-yr Sharpe/beta pair is unreliable; I weight the 3-year figures and the profile beta (1.21) more heavily.

## 4. Downside Scenario Analysis — revenue –20% (to ~$48.4B)

| | Base FY2026 | –20% rev (some opex flex) | –20% rev + 10% inventory write-down |
|---|---|---|---|
| Gross profit (19.8% GM) | $11,955M | $9,583M | $9,583M |
| Opex (–10% flexed) | $8,665M | $7,800M | $7,800M |
| Inventory write-down | — | — | –$1,200M |
| EBIT | ~$3,290M | ~$1,783M | **~$583M** |
| EBITDA | ~$4,230M | ~$2,727M | ~$1,527M |
| Net debt / EBITDA | 1.15x | **1.79x** | **3.20x** |
| Debt / EBITDA | 2.19x | 3.40x | 6.07x |
| EBIT / interest | 8.1x | 3.7x | **1.2x** |
| FCF | $3.2–3.3B | ~$1.3B | **~$0** |
| Dividend ($1.15B, just raised) cover | 2.9x | 1.13x | not covered |

**Verdict:** A 20% revenue shock is **survivable at BBB** — net leverage peaks ~1.8x, still inside IG thresholds, and FCF still covers the dividend. But the buyback ($1,225M in FY2026) must be suspended immediately, and ratings would likely go to **negative outlook**. A simultaneous inventory write-down is the true tail: at ~3.2x net leverage and ~1.2x coverage, HPQ would be a **downgrade candidate to BBB-/Ba1** with the dividend cut. Note that a 10% write-down on the $12.3B inventory book equals **50% of FY2026 net income** — the single largest idiosyncratic risk.

## 5. Overall Financial Risk Rating: **MODERATE**

Not Low, because of genuinely thin cushion (0.81 current ratio, $6.8B negative working capital, ~zero book equity, $8.2B negative tangible book) and 43–51% equity vol. Not High, because cash generation is reliable and improving, leverage is falling fast, coverage is 8x and rising, coverage of the dividend is ~3x, refinancing is modest, and the structural features are industry-normal and matched by a weaker-rated-in-practice peer (DELL).

## 6. Key Red Flags

1. **Inventory ballooning +44% y/y to $12,296M** vs. revenue +9.4% — inventory days extended from ~70 to ~92. Largest single risk: a 10% write-down = $1.2B ≈ half of net income. Suggests either pre-buying ahead of memory-cost inflation (cash/liquidity strain) or channel-stuffing (demand risk).
2. **Gross margin compression** 22.1% → 20.0% → 19.8% — component cost inflation not being passed through; contradicts the revenue growth.
3. **Tangible equity of –$8.2B** (goodwill+intangibles $8,724M = 16.6x book equity). Total liabilities $47.0B vs. assets $47.6B — **assets/liabilities = 1.01**. Any material impairment drives equity deeply negative (already –$346M in FY2025).
4. **Structural liquidity dependence**: current ratio has been <1 for years; HPQ relies on continuous supplier credit and receivables factoring. In a credit-market freeze this is a funding risk even with positive FCF.
5. **Refinancing cost step-up**: $1,320M short-term debt plus rollover of legacy low-coupon paper (e.g., 1.45% notes due Jun-2026) into a **4.74% (2Y) / 5.13% (10Y)** curve. Interest expense is falling now ($684M→$506M→~$408M) but will re-accelerate as cheap debt matures.
6. **Capital returns exceed prudence**: dividends $1,095M + buybacks $1,225M = $2,320M = **73% of FCF**, while book equity hovers near zero. Dividend was just increased, reducing flexibility right as the margin outlook is cautious.
7. **Shareholder-return-driven balance sheet** masks leverage: debt/assets (19.5%) looks fine only because assets are inflated by $12.3B inventory.

**Explicit data gaps:** (a) full debt maturity schedule by year — not available from tools; (b) precise FY2026 GAAP operating income and interest expense (reconstructed/estimated from quarterly rows because the annual and Q4 rows are corrupt); (c) covenant terms on the revolver and any securitization facilities; (d) CDS spreads; (e) no reliable peer set — the tool's "Technology" sector list returns software/semiconductor mega-caps (AAPL, MSFT, NVDA, AVGO) that are not meaningful hardware comparables, so I substituted DELL manually.
