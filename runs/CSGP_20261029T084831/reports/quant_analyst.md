# Quant Analyst

- Symbol: CSGP
- Elapsed: 38.6s

---
I have enough to write the report. Two things need flagging prominently: (1) the terminal "current price" of $27.54 is corrupted and has poisoned the return-based tools; (2) the earnings-revision print rests on a single analyst's 2030 estimate. Numbers below reconcile the clean daily series against the tool outputs.

---

# CSGP — Quantitative Factor Report
**CoStar Group, Inc. | Real Estate — Real Estate Services | Price $27.54 (printed; see data caveat) | Mkt cap ~$11.6B**

## ⚠️ Critical Data-Integrity Flag
The daily price series is clean and trades **$68–96 through 2025, last close $68.80 (2025‑11‑28)**. The provider's "current price" field (**$27.54**) and derived market cap ($11.6B) are **inconsistent** with that series (a $68.80 price implies ~$29B cap on 421M shares). That stale/erroneous terminal price injects a phantom −95% return into every *return-based* tool (`alpha −95.2%`, `beta 0.004`, `vol 51%`, `Sharpe −1.83`, `maxDD −59%`). **Those five figures are garbage and are discarded below.** Momentum, valuation and quality tools read from clean fundamentals/discrete prices and are usable.

## 1. Factor Scores Table
*(Sector rank = among the 4 large-cap Real Estate comps pulled: EQIX, PLD, SPG, CSGP; 1 = best of 4)*

| Factor | Raw Score | Sector Rank | Signal |
|--------|-----------|-------------|--------|
| **Value** | P/E 1659×, EV/EBITDA 37.5×, P/FCF 282×, P/B 1.39× | **4 / 4 (worst)** | **Strong Sell** — expensive on every earnings multiple; only P/B looks cheap |
| **Momentum** (12‑1) | −3.86% | **1 / 4 (best)** | Neutral-negative — least-bad in a weak sector; but breakdown since Aug |
| **Quality** | ROE 0.08%, ROIC **−0.76%**, GP/Assets 0.232 (best), accruals −0.040 (good) | **3 / 4** | **Sell** — earnings ~breakeven, negative ROIC; but high GP/asset & low accruals help |
| **Low Vol** | Realized vol 51% / beta 0.004 (corrupted); profile beta 0.80 | 4 / 4 (corrupt) | Weak — est. true vol ~30%, elevated |
| **Earnings Revision** | +23.2% (2030 EPS est.), **n = 1 analyst** | n/a | Weak positive — statistically insignificant |

Peer context: SPG best value (P/E 14.9×, EV/EBITDA 12.3×) & quality (ROE 68.8%); EQIX & PLD mid; **CSGP is bottom of the group on value and near-bottom on quality.** All four names have negative momentum (sector-wide derating).

## 2. Price Statistics
Tool outputs **rejected** (corrupted). Reconstructed from clean series (Sep‑2024 → Nov‑2025, ~310 trading days):

| Metric | Tool Output (corrupt) | Reconstructed estimate |
|--------|----------------------|------------------------|
| Annualized return | −94.5% ❌ | ≈ **−7% to −9%** (price only; no dividend) |
| Beta vs SPY | 0.004 ❌ | ≈ **0.80** (profile beta 0.796) |
| Alpha (ann.) | −95.2% ❌ | **Large negative** (~−20 to −30% vs SPY's strong advance) |
| Volatility (ann.) | 51.1% ❌ | ≈ **28–32%** |
| Sharpe | −1.83 ❌ | ≈ **−0.25** |
| Sortino | −2.48 ❌ | ≈ **−0.30** |
| Max drawdown | −59.3% ❌ | ≈ **−33%** ($97 peak Aug‑2025 → $65 Nov‑2025) |

Real picture: **negative absolute return, negative alpha, moderate-high vol, negative risk-adjusted ratios, deep ~33% drawdown, now in a downtrend (−10% single-day drop 2025‑10‑29).**

## 3. Composite Quant Signal: **NEUTRAL (with Sell bias)**
The current-factor vector is genuinely poor — bottom-quartile **value** (absurd trailing multiples), negative **quality** (ROIC −0.76%, ROE ~0%), elevated **volatility**, and negative **alpha**. The only offsets are (a) best-in-sector **momentum** (−3.86% vs −10 to −13% peers) and (b) an improving **forward EPS trajectory** (2025 $0.84 → 2026 $1.38 → 2027 $1.74 → 2030 $3.48), which would normalize the value multiples if delivered. On a pure screen this is a Sell; the forward inflection story pulls it back to Neutral. **Not a quant buy.**

## 4. Key Quant Risk Flags
- **🔴 Data integrity:** terminal price ($27.54) contradicts the daily series — **verify the actual quote before acting**; all return/risk stats here are estimates, not tool outputs.
- **🔴 Earnings-revision significance:** the +23% upgrade compares a **2030 estimate built by a single analyst (n=1)** vs 3 months prior — not statistically meaningful. Treat as noise.
- **🟠 Momentum reversal / breakdown risk:** stock peaked $97 (Aug‑2025), fell ~33% to $65, with a −10% single-session gap (2025‑10‑29, 15M shares). Trend is down; the "best momentum" ranking is relative, not absolute.
- **🟠 Quality/value-trap:** cheap P/B (1.39×) masks near-zero earnings and negative ROIC — a classic value-trap signature unless Homes.com margins inflect.
- **🟠 Size/coverage:** long-range estimates carry 1–4 analysts; thin coverage → low estimate reliability.
- **🟡 Factor exposure:** high-multiple growth-services profile makes it rate- and growth-disappointment-sensitive.

**Bottom line:** Quantitatively this is a **pass (Neutral/Sell-biased)** — deep value and quality failures are only partially offset by relative momentum and a plausible but unproven forward EPS recovery. Recommend re-running return-based stats once the price feed is corrected.
