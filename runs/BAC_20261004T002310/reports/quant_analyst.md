# Quant Analyst

- Symbol: BAC
- Elapsed: 45.2s

---
All quantitative legs are in. The `rank_universe_by_factor` tool's `universe` parameter is broken (rejects both string and list forms), so exact sector percentile ranks are unavailable — I note that gap and use the peer correlation matrix plus raw factor values for cohort positioning instead.

---

# BAC — Bank of America Corporation | Quant Factor Report

**As of price $53.75 · Mkt cap ≈ $381bn · Financial Services / Banks-Diversified**
*Analysis window: 252 trading days (~1yr). All ratios vs. SPY unless noted.*

## 1. Factor Scores Table

| Factor | Score (0–5) | Metrics | Signal |
|--------|-------------|---------|--------|
| **Value** | 2.5 / 5 | P/E 14.1 · P/B **1.34** (cheap for cohort) · P/FCF 32.2 · Div yield 2.16% · EV/EBITDA −4.8 (meaningless for banks — negative EV from financing liabilities) | **Neutral / mildly positive** |
| **Momentum** | 3.5 / 5 | 12-1m return **+9.2%** (positive) | **Positive** |
| **Quality** | 2.5 / 5 | ROE 10.1% · gross profit/assets 3.2% · accruals 0.52% (OK) · Piotroski **6/9 (moderate)** · ROIC 5.6% | **Moderate** |
| **Low Vol** | 3.5 / 5 | Ann. vol 22.7% · **beta vs SPY 0.71** (below-market, good) | **Positive** |
| **Earnings Revision** | 4.5 / 5 | Forward FY29 EPS **$6.82 vs prior $5.89 → +15.8% upgrade**; consensus ladder rises monotonically FY26 $4.58 → FY27 $5.24 → FY28 $5.89 → FY29 $6.82 | **Strong positive** |

*Sector rank:* **Not computable** — `rank_universe_by_factor` failed (universe param rejects both list and string) and `get_sector_peers` returned Vanguard index funds/ETFs (Asset Management), not bank comparables. Cohort context below is from raw factor values and a hand-built mega-bank correlation matrix.

## 2. Price Statistics (252d vs SPY)

| Stat | Value | Read |
|------|-------|------|
| Alpha (ann.) | **−12.7%** | Deeply negative |
| Beta | **0.72** (regression); 0.71 low-vol tool | Below-market sensitivity |
| R² | **0.17** | Market explains little — alpha estimate is **low-confidence (small effective sample)** |
| Sharpe | **−0.13** | Negative |
| Sortino | **−0.17** | Negative |
| Ann. return / vol | −2.9% / 22.8% | |
| Max drawdown | **−17.9%** | Material |
| Peer corr. (252d) | WFC **0.80** · JPM **0.80** · C 0.73 · MS 0.66 · GS 0.57 (avg ≈ 0.71) | Tightly clustered with JPM/WFC |

## 3. Composite Quant Signal: **BUY** (moderate conviction)

**Why not Strong Buy:** trailing realized returns are negative (Sharpe −0.13, Sortino −0.17), alpha is deeply negative (−12.7%, albeit R²=0.17 makes it unstable), and the quality factor is only moderate.
**Why not Neutral:** the four pillars that matter most for forward returns — earnings revisions (+15.8%, monotonic 4-year ladder), book-value valuation (P/B 1.34), price momentum (+9.2%), and below-market beta (0.71) — are all constructive. Consensus EPS is expected to compound ~14%/yr FY26→FY29.

## 4. Key Quant Risk Flags

- **Momentum reversal risk — HIGH.** 12-1m momentum is +9.2%, yet the full 252d return is −2.9%. The last ~21 trading days have given back roughly 10–12 points — the most recent month is sharply negative. Recent sell-side color is consistent: Evercore **lowered its target to $62 from $67** (Oct), the newest of four targets (UBS $70, Argus $70, Truist $65 all raised earlier). Targets still imply +15–30% upside from $53.75, but the direction of the latest revision is a trim.
- **Factor crowding.** Corr 0.80 with WFC and JPM — if big-bank beta reprices (rate/credit cycle), BAC moves with it regardless of idiosyncratic merit. Low alpha + high peer corr = little standalone alpha source.
- **Beta estimate mismatch.** Fundamental/profile beta lists 1.16; regression beta is 0.72. The 0.72 figure rests on R²=0.17 — treat beta/alpha as noisy.
- **Small sample flags.** FY29 EPS estimate rests on **n=4 analysts** (FY28 has n=10); R²=0.17 for the return model. Both underpower the strong-upgrade and alpha conclusions.
- **Not a liquidity issue** (mega-cap, $381bn), but P/FCF 32x and negative EV/EBITDA mean standard value screens mis-price banks — P/B 1.34 is the reliable value anchor here.

**Bottom line:** Constructive setup on revisions, valuation, and low-beta profile; the market has not yet paid for it (negative trailing alpha/Sharpe) and the last month rolled over. Position for continued estimate-revision upside but watch the near-term momentum reversal — any further slide below ~$53 makes the Buy thesis data-dependent rather than conviction-based.
