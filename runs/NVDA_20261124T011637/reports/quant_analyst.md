# Quant Analyst

- Symbol: NVDA
- Elapsed: 80.4s

---
Data now reconciles. The profile price ($165.05) is current (2026‑11‑23); the earlier history call simply truncated at Feb 2026. Critically, **NVDA crashed −47.5% between 6 Oct and 20 Nov 2026**, then rebounded +31.5% in one session.

---

# NVIDIA (NVDA) — Quantitative Factor Report
**Price $165.05 (23‑Nov‑2026) | Mkt cap $4.05T | Technology / Semiconductors | 24.51B diluted sh**

## 1. Factor Scores

| Factor | Score /100 | Raw Metric | Sector Rank (6 semis) | Signal |
|---|---|---|---|---|
| **Value** | **74** | P/E 33.7 · EV/EBITDA 27.6 · P/FCF 41.9 · P/B 25.7 · FCF yld 2.39% · Fwd P/E FY27 17.2x | **2 / 5** | **Attractive** |
| **Momentum** | **30** | 12‑1 = −3.96% (tool); −21.8% trailing 1M; −47.5% peak‑to‑trough | **3 / 6** (but last on risk‑adj) | **Negative** |
| **Quality** | **85** | ROE 76.3% · ROIC 77.3% · GP/Assets 0.742 · Accruals 0.084 | **1 / 6** (profitability) / **6 / 6** (accruals) | **Strong, deteriorating** |
| **Low Vol** | **12** | Vol 56.25% · β 2.442 · MaxDD 47.5% | **4 / 6** vol, **6 / 6** drawdown | **Poor** |
| **Earnings Revision** | **50** | +25.85% "revision" — **see flag, likely artifact** | n/a | **Neutral / low confidence** |

**Value detail.** Cheapest large‑cap semi only after Micron (P/E 9.5). Peer P/E: MU 9.5 · **NVDA 33.7** · ASML 56.0 · AVGO 65.7 · AMD 171.1. On forward FY2027 EPS of $9.62, NVDA trades **17.2x**; FY2028 ($16.59) → **9.9x**. PEG ≈ 0.18. Note P/B of 25.7x is the outlier — book value is meaningless here given 76% ROE.

**Quality detail.** Gross profit/assets of 0.742 is ~1.35x the next best (MU 0.549) and ~3.3x AMD. Piotroski **F‑Score 5/9** (Moderate): fails ROA improvement, gross‑margin improvement, asset‑turnover improvement, and accruals quality. That is the textbook signature of a business decelerating from a hyper‑growth base.

**⚠ Earnings Revision flag.** The tool's +25.85% is **FY2031 estimate ($33.19) ÷ FY2030 estimate ($26.37) − 1** — a fiscal‑period roll, *not* a 3‑month revision for a fixed forward period. I do not treat this as evidence of upward revision. The genuine revision evidence is the 18‑Nov price‑target actions, which are **mixed‑to-negative**: JPM raised to $230, but UBS cut 240→220, Piper cut to 230, TD Cowen cut to 200, CLSA downgraded to Outperform. **EPS path rising while targets are trimmed = multiple compression.**

## 2. Price Statistics

| Metric | 1‑Year (252d) | 2‑Year (504d) |
|---|---|---|
| Annualised return | ~ −7.5% (my calc) / ~0% (tool) | **+19.52%** |
| Annualised volatility | **56.25%** | 46.65–47.01% |
| Beta vs SPY | **2.442** | **2.276** |
| **Alpha (annualised)** | n/a | **−13.29%** |
| R² vs SPY | n/a | 0.458 |
| **Sharpe (rf=0)** | **0.006** | **0.415** |
| **Sortino** | n/a | **0.693** |
| **Max drawdown** | **−47.53%** | −47.53% |

**Drawdown anatomy:** peak **$239.24 (6‑Oct‑26)** → trough **$125.53 (20‑Nov‑26)**, exactly −47.53%. Rebound to $165.05 on 772M shares (+31.5% in one session). **Still −31.0% below the peak.**

**Risk‑adjusted verdict.** Over two years NVDA delivered 19.5% annualised — but with β 2.28 that is *below* its beta‑implied return; alpha is **−13.3%/yr**. Over the last twelve months Sharpe is **0.006** — zero risk‑adjusted return. NVDA ranks **last of six** semis on 1‑year Sharpe (AMD 1.717 · MU 1.264 · TSM 0.258 · ASML 0.207 · AVGO 0.115 · **NVDA 0.006**). You are being paid nothing for 56% vol.

## 3. Composite Quant Signal

**Weighting:** Value 20% · Momentum 25% · Quality 25% · Low‑Vol 10% · Revisions 20%

> 0.20(74) + 0.25(30) + 0.25(85) + 0.10(12) + 0.20(50) = **54.8**

# → NEUTRAL (54.8 / 100)

**Rationale.** Two top‑decile factors (Quality 85, Value 74) are offset by two bottom‑decile factors (Low‑Vol 12, Momentum 30), and the revision signal — the factor that would normally break the tie — is **methodologically unreliable**. Elite fundamentals priced at a reasonable forward multiple, but the trend is broken, alpha is negative, and risk‑adjusted returns are nil. High conviction in the *quality*, low conviction in the *timing*.

*Analyst PT cross‑check:* median **$227.5**, mean $225.9 (n=14, range $170–$293, CV 16%) → **+36.9% upside** vs $165.05. Wide dispersion = genuine disagreement on the AI capex cycle, not consensus comfort.

## 4. Key Quant Risk Flags

1. **Momentum reversal — REALISED, not prospective.** −47.5% in six weeks, −21.8% in one month, worst drawdown in the peer group. Momentum crashes in crowded high‑beta names typically see failed rallies; the +31.5% single‑day bounce on 772M shares (3–4x normal volume) is a **volatility signature, not a confirmed reversal**.
2. **Negative alpha at maximum beta.** 2‑yr alpha −13.29% with β 2.276. High R² is absent (0.458) — **54% of variance is idiosyncratic**, so index hedges only remove ~46% of risk. This is an expensive position to hedge.
3. **Accruals deterioration is monotonic and material.** 0.0839 (FY26) → 0.0788 (FY25) → 0.0254 (FY24) → −0.0309 (FY23). FY26 net income $120.07B vs. operating cash flow $102.72B = **$17.35B non‑cash gap**. Earnings quality is decaying as growth normalises. Flagged "warning" in both of the last two years.
4. **Factor crowding.** NVDA is the single most crowded AI‑momentum holding in the market. Beta 2.44 with only 0.458 R² means it *behaves* like high beta in selloffs but does not track the index — the worst combination for a crowded unwind.
5. **Earnings‑revision factor is contaminated** (period‑roll artifact). Do not size a position on the +25.85% figure. The independent evidence (PT cuts on 18‑Nov, CLSA downgrade) leans negative.
6. **Growth deceleration risk embedded in estimates.** FY27 EPS +96% → FY28 +72% → FY29 +32% → FY30 +21%. Any shortfall in the first two years compresses the entire terminal path; the 17.2x forward multiple is only cheap *if* $9.62 is achieved.
7. **Peer‑data integrity:** TSM value multiples are unusable (P/E 1.1, EV/EBITDA −0.06 — ADR currency mismatch). TSM excluded from value ranking; ranks are therefore out of 5, not 6.

**Not a concern:** liquidity. 772M shares on the rebound day, ~$125B notional. Zero execution risk.

**Sample size:** 252d/504d windows are adequate (n≈252/504) for vol, beta and Sharpe. **Alpha (R² 0.458) and Sortino are statistically fragile** — alpha's standard error is wide given the unexplained variance, and Sortino rests on few downside observations clustered in Apr‑2025 and Nov‑2026. Treat the −13.29% alpha as directional, not precise.

**Bottom line:** exceptional business (ROE 76%, GP/assets 0.74, ROIC 77%) at a defensible forward multiple, but the quantitative tape says the de‑rating is already in motion. **Neutral — wait for either (a) a stabilised 1‑month momentum base or (b) accruals reverting below 0.05 before adding.**
