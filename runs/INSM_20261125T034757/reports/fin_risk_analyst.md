# Fin Risk Analyst

- Symbol: INSM
- Elapsed: 87.0s

---
## INSM — Insmed Incorporated: Financial Risk Assessment

**Critical note on data vintage:** The financial statement feed runs through **Q3 2026** (period end 2026-09-30, filed 2026-10-29). The pre-computed ratio tools (`calculate_leverage_ratios`, `calculate_liquidity_ratios`, `calculate_altman_z_score`, `calculate_piotroski_f_score`, `calculate_fcf_yield`) all return **FY2025 (2025-12-31)** figures. FY2025 is now materially stale — revenue has roughly tripled on a quarterly basis since. I present both, and anchor conclusions on TTM (Q4'25–Q3'26) figures I computed directly from the statements.

---

### 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE (unrated / high-yield profile) — but with a strongly improving trajectory.**

Insmed is an unrated, loss-making commercial-stage biotech carrying a term loan. On a *static* credit screen it looks impaired: negative EBIT, negative FCF, an Altman Z of **−3.955 ("Distress")**, and an accumulated deficit of **$5.91B** against book equity of only $726M. On a *forward* view the picture is very different, and the static screen is misleading here.

Key facts:
- **Interest coverage (TTM):** EBIT of −$540.9M against interest expense of $81.4M → **−6.6x**. This is a genuine deficit, but a marked improvement from FY2025's **−14.0x** (EBIT −$1,187.9M / $84.8M). The trend is the story, not the level.
- **Leverage:** Total debt $741.2M vs. cash & short-term investments $1,146.6M → the company is in a **net cash position of roughly $405M** (computed as debt less cash). Debt/equity 1.02x book; debt/assets 0.33x. On market capitalisation ($37.3B) leverage is negligible at 2.0%.
- **Maturity profile — no cliff:** The 0.75% Convertible Senior Notes due 2028 ($569.5M) were **redeemed in June 2025**. The remaining debt is a **term loan extended to a February 1, 2028 maturity** under an amended & restated loan agreement. Short-term debt is only **$10.2M**. There is **no refinancing requirement before 2028** — this is the single most important mitigant to the credit story.
- **Cost of debt:** ~8% effective on the average 2025 balance ($1.04B average debt, $83.8M interest) — expensive, consistent with an unrated, pre-profit issuer.

**Conclusion:** Not a distress credit in any cash-flow sense. The Altman "Distress" classification is an artefact of accumulated losses and a book-equity denominator, not a liquidity signal. The real credit risk is **execution risk on the Brinsupri launch**, not solvency.

---

### 2. Key Financial Risk Metrics

| Metric | FY2025 (tool output) | TTM to Q3'26 (computed) | Assessment |
|---|---|---|---|
| Revenue | $606.4M | **$1,519.7M** | +151% vs FY25; Q3'26 alone $524.4M (+268% YoY) |
| Gross margin | 79.4% | **84.3%** | Improving — strong pricing |
| EBITDA | −$1,171.5M | **−$493.9M** | Still negative, but <½ the loss |
| EBIT / operating income | −$1,187.9M | **−$540.9M** | Q2'26 was **+$8.9M** — first positive quarter |
| Net income | −$1,276.8M | **−$605.6M** | Q3'26 loss narrowed to −$100.3M |
| Debt / equity | 1.04x | 1.02x | Moderate; book equity thin |
| Net debt / EBITDA | 0.56x (net cash) | Net cash ~$405M | N/M — negative EBITDA |
| Interest coverage | **−14.04x** | **−6.6x** | Improving but negative |
| Current ratio | 3.83x | **2.86x** | Strong |
| Quick ratio | 3.54x | **2.59x** | Strong |
| Cash ratio | 3.05x | **1.92x** | Strong |
| Working capital | $1,325.3M | $1,110.0M | Ample |
| **Altman Z-Score** | **−3.955 — Distress** | — | **Not reliable for this issuer (see caveat)** |
| **Piotroski F-Score** | **5 / 9 — Moderate** | — | F1/F2/F3/F7 all score 0 |
| FCF yield | −2.66% | −1.76% | Negative |
| Equity / assets | 0.33 | 0.33 | Thin |

**Altman Z caveat:** The model's x4 uses book equity ($726M) rather than the $37.3B market cap. Substituting market cap would swing the score from −3.96 to roughly +10 — the output is dominated by an input that is economically meaningless for a company with a $5.9B accumulated deficit and a 50x book-to-market ratio. The components that *are* informative: **x2 (retained earnings/assets) = −2.49** and **x3 (EBIT/assets) = −0.52**. Both correctly say "this company has never earned money." The Z-score should be treated as a flag on cumulative profitability, not on bankruptcy probability.

**Piotroski detail:** 5/9 reflects negative ROA (0), negative operating cash flow (0), worsening ROA (0), and dilution (0) — offset by accruals quality (1), lower leverage (1), positive equity change (1), gross margin improvement (1), and asset turnover improvement (1). Note that on a *TTM* basis F1/F2/F3 would all flip positive; the FY2025 score understates current momentum.

---

### 3. Market Risk Profile

| Metric | 756-day (3Y) | 252-day (1Y) | Read |
|---|---|---|---|
| Annualised volatility | **58.4%** | **72.9%** | Extreme — 3–4x a broad index |
| Beta vs SPY | 0.62 | 0.44 | Low, but **misleading** |
| Max drawdown | **−56.5%** | **−44.3%** | Severe |
| Sharpe ratio | 0.96 | 0.56 | Decent 3Y, deteriorating 1Y |

**The beta is a trap.** At 0.44–0.62, INSM screens as *less* risky than the market. That is an artefact of idiosyncratic, launch-driven price action that is uncorrelated with SPY. The economically relevant risk is **72.9% annualised volatility and a 44% drawdown within the last twelve months** — the stock moved 15%+ on a single earnings day (2026-02-19: open $153.78, close $161.00, +16% on the Brinsupri Q4 beat). Market risk here is **event/binary risk**, not systematic risk. Beta-based position sizing would materially understate exposure.

---

### 4. Downside Scenario Analysis — Revenue −20%

Applied to the TTM base ($1,519.7M revenue, 84.3% gross margin, SG&A $960.3M, R&D ~$861.2M, interest $81.4M):

| Line | Base TTM | −20% Revenue, no cost action | −20% Revenue, 20% opex cut |
|---|---|---|---|
| Revenue | $1,519.7M | $1,215.8M | $1,215.8M |
| Gross profit (84.3%) | $1,280.6M | $1,024.8M | $1,024.8M |
| SG&A | $960.3M | $960.3M | $768.2M |
| R&D | $861.2M | $861.2M | $689.0M |
| **EBIT** | **−$540.9M** | **−$796.7M** | **−$432.4M** |
| Interest | $81.4M | $81.4M | $81.4M |
| **Net loss** | **−$605.6M** | **−$861.5M** | **−$497.2M** |
| **FCF** | **−$657.6M** | **~−$910M** | **~−$550M** |

**Findings:**

1. **A 20% revenue shock does not threaten solvency — it threatens the profitability timeline.** Even with a 20% cost cut, EBIT stays at −$432M. The company is not yet at breakeven, so a demand shock pushes the inflection point out roughly 12–18 months rather than triggering a default.
2. **Cash runway remains adequate in the stress case.** Against $1,146.6M of cash, a −$550M to −$910M FCF year implies **1.3 to 2.1 years of runway** — past the February 2028 term loan maturity only in the milder case. In the harsher case, Insmed would need to raise capital in 2027, likely dilutive.
3. **Breakeven revenue is approximately $2.16B** (fixed cost base of ~$1.82B at 84.3% gross margin). TTM revenue is $1.52B; Q3'26 annualised revenue is ~$2.10B. **The company is within ~3% of breakeven on current run-rate** — which is why the launch trajectory, not the debt, is the whole risk story.
4. **The genuine tail risk is not a 20% revenue dip — it is a launch stall.** A 20% haircut is survivable. A scenario where Brinsupri growth flattens near $1.5B and R&D cannot be cut fast enough (the pipeline is the reason for the valuation) would produce a multi-year −$500M+ burn against a 2028 maturity.

---

### 5. Overall Financial Risk Rating: **MODERATE**

*(Down from what would have been "High" on FY2025 data alone.)*

**Why not High:** ~$1.15B cash, a **net cash position**, current ratio 2.86x, **no debt maturity until February 2028**, revenue up 268% YoY in the latest quarter, gross margin expanding to 85%, and a first positive EBIT quarter in Q2'26. Liquidity risk is genuinely low and the trend is strongly positive.

**Why not Low:** The company is still loss-making, FCF is negative, coverage is negative, book equity is thin ($726M) against $1.50B of liabilities, and volatility is 73%. There is no margin of safety if the launch disappoints.

---

### 6. Key Red Flags

1. **Persistent negative FCF despite a 268% revenue acceleration** — TTM FCF −$657.6M. Cash burn has not yet inflected even as revenue has. Q3'26 FCF was −$42.1M, so it is close, but not there.
2. **Negative interest coverage (−6.6x)** — the company services $81M of annual interest entirely from its balance sheet, not from operations. This is sustainable only while cash lasts.
3. **Cumulative losses of $5.91B** — retained earnings/assets of −2.49 means the business has consumed roughly eight times its current book equity over its life.
4. **Dilution** — Piotroski F7 scores 0; diluted shares rose from 123.0M (2022) to 218.8M (Q3'26), **+78% in under four years**. Continued funding needs imply more.
5. **Single-name, launch-dependent valuation** — ~24.6x TTM revenue on $37.3B market cap. Any Brinsupri prescription-trend miss is a double hit: earnings downgrade *and* multiple compression.
6. **Concentrated debt maturity** — while 2028 is distant, essentially all $691M of long-term debt matures at once in February 2028. Refinancing will need to happen either from operating cash flow or from a market window that may not be open.

---

### Data Gaps (explicit)

- **No credit rating or CDS spread available.** Insmed is unrated; the "Sub-Investment Grade" label is my inference from leverage, coverage, and cost of debt, not a published rating.
- **Net debt field inconsistent in quarterly balance sheet feed.** The feed reports net debt of $344.6M at 2026-09-30 and $35.1M at 2026-06-30, which do not reconcile to total debt less cash ($741.2M − $1,146.6M = −$405.4M). The FY2025 figure reconciles correctly. I used the computed net cash figure throughout and flag the feed as unreliable for this field.
- **Q4'25 stock-based compensation reported as $0** in the quarterly cash flow feed, versus FY2025 SBC of $152.7M — almost certainly a data error. TTM SBC of $128.2M is therefore understated.
- **No detailed debt maturity ladder by year** — maturity confirmed as February 2028 via SEC filing reference, but the year-by-year schedule was not retrieved.
- **Peer comparison not performed** — the sector peer list returned large-cap pharma (LLY, JNJ, ABBV, MRK) with no commercial-stage biotech comparables. Ratio benchmarking against those names would be misleading, so I omitted it rather than present a false comparison.
