# Fin Risk Analyst

- Symbol: AKAM
- Elapsed: 51.6s

---
## AKAM — Financial Risk Assessment
**Akamai Technologies | Technology / Software-Infrastructure | FY2025 (period ended 2025-12-31)**
Last close $97.15 (2026-01-30); market cap ~$13.2bn

---

### 1. Credit Risk Assessment — **SUB-INVESTMENT GRADE (crossover, deteriorating)**

AKAM is a **fallen angel**. S&P lowered AKAM to **BB+ from BBB-** and Moody's cut one notch to **Baa3** (lowest investment-grade rung) in 2026, citing a **debt-funded AI infrastructure buildout**; S&P notes a **negative outlook and two downgrades in 2026** prior to the Anthropic transaction. Ratings were BBB+/Baa2 stable as recently as 2023–24 — a three-notch deterioration in the cycle. Leverage per the reported balance sheet is already 4.26x net debt/EBITDA, and gross debt rose **+49% in FY2025 alone** ($4.63bn → $6.91bn) and **+52% since FY2023**.

### 2. Key Financial Risk Metrics

| Metric | FY2025 | FY2024 | FY2023 | Read |
|---|---|---|---|---|
| Total debt | $6,909m | $4,635m | $4,536m | +49% y/y; $2.3bn raised in one year |
| Cash & ST inv. | $1,187m | $1,597m | $864m | Cash −26% y/y |
| Net debt/EBITDA | **4.26x** | 3.26x | 3.26x | Deteriorating; breaches 4.0x type thresholds |
| Debt/equity | 1.39x | 0.95x | 0.99x | Leverage doubled vs equity base |
| Debt/assets | 0.60x | 0.45x | 0.46x | — |
| Interest coverage (reported) | 20.4x | 22.7x | 37.9x | **Misleading — see red flag #3** |
| EBIT / est. gross interest | ~2.4x | n/a | n/a | Analyst estimate, see note |
| Current ratio | 2.29x | 1.23x | 2.16x | Adequate on reported basis |
| Quick / cash ratio | 2.29x / 1.23x | — | — | No inventory; clean |
| Working capital | $1,249m | $487m | $969m | — |
| Altman Z-Score | **1.56 (Distress)** | — | — | See note |
| Debt/EBITDA (Altman x3: EBIT/Assets) | 5.5% | — | — | Low asset productivity |
| Piotroski F-Score | **5 / 9 (Moderate)** | — | — | Fails on ROA trend, leverage, GM, turnover |
| FCF yield | 5.19% ($699m FCF) | 6.20% | — | But see SBC adjustment |
| SBC-adjusted FCF yield | **~1.8%** ($240m) | — | — | FCF − SBC $459m |
| Tangible book equity | **$1,157m** | $1,000m | — | vs $5.9bn net debt; goodwill+intangibles = 77% of equity |

**Z-Score note:** the 1.556 "distress" reading uses *book* equity for x4 (0.77). Substituting market cap ($13.2bn) lifts x4 to 2.03 and Z to **~2.32 — still grey zone**, not safe. AKAM fails on genuine fundamentals: x3 (EBIT/assets) of 5.5% and x5 (asset turnover) of 0.37 are structurally weak for a company with $3.8bn of PP&E and $3.8bn of goodwill. This is not merely a book-vs-market artifact.

**Interest coverage note:** reported interest expense is **$30.8m on $6.9bn of debt (0.45% effective rate)** — economically implausible and indicative of heavy **interest capitalisation** into the network/PP&E build. Estimated gross interest at a ~4.5% blended coupon on ~$5.8bn average debt is **~$260m**, implying **EBIT/gross interest ≈ 2.4x** and EBITDA/gross interest ≈ 5.2x. Against ($1,342m EBITDA − $820m capex) = $522m, gross interest consumes ~50% of post-capex cash generation. *This is an estimate — AKAM does not disclose capitalised interest in the data provided.*

### 3. Market Risk Profile

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility | **52.5%** (tool) | ⚠️ Inconsistent with observed series; I estimate **~30–35%** from daily closes |
| Beta vs SPY | **1.226** (tool) vs **0.664** (company profile) | ⚠️ Conflict — see note |
| Max drawdown (3y) | **−51.7%** (tool) / **−46.8%** computed close-to-close ($128.32 → $68.21, Feb-24 → Apr-25) | Severe |
| Sharpe ratio | **0.17** | Poor risk-adjusted return |
| 3-year price return | +14% total (~+4.5%/yr) | vs S&P far higher |

**Data-quality flag:** the two vol/beta measures disagree. Interpretation: AKAM's risk is now **event-driven/idiosyncratic** rather than market-sensitive. Gap days were brutal and repeated: **−22.7% (2025-02-21), −14.5% (2024-11-08), −11.3% (2024-05-10), −8.7% (2025-05-09), +14.7% (2025-11-07)**. A single-digit beta understates tail risk enormously — drawdowns are driven by guidance and AI-capex financing news, not market direction. I would underwrite this as **high-30s vol with fat left tail**, not as a defensive 0.66-beta name.

### 4. Downside Scenario — Revenue −20% (to $3,366m, −$842m)

Assumptions: 65% contribution margin on lost revenue (media delivery/security has low incremental cost but the compute-heavy mix is more fixed); $150m of discretionary cost cuts; capex cut to a $600m maintenance level; gross interest ~$260m.

| Line | Base FY2025 | Stress (−20% rev) |
|---|---|---|
| Revenue | $4,208m | $3,366m |
| EBITDA | $1,342m | **~$945m** |
| EBIT | $633m | **~$236m** |
| Net debt/EBITDA | 4.26x | **~6.3x** |
| EBIT / gross interest | ~2.4x | **~0.9x (fails)** |
| FCF (pre-buyback) | $699m | **~$35m** |
| Buyback capacity | $800m | **$0 — must be suspended** |

**Assessment:** survivable but *not* self-funding. At −20% revenue AKAM services interest from operating cash but cannot cover capex, and EBIT would not cover cash interest. The mitigant is the **$11.6bn / 7-year Anthropic contract** (~$1.66bn/yr), which backstops the revenue line — but it is a **single, private, loss-making counterparty**, requires the capex to be spent *ahead* of the revenue, and creates acute concentration risk.

### 5. Overall Financial Risk Rating: **HIGH**

Not Critical — $1.19bn cash, 2.29x current ratio, $1.28bn revolver-era liquidity, 5.4% revenue growth, 16.6% FCF margin and a $11.6bn contracted backlog all argue against near-term default. But the combination of 4.26x net leverage and rising, a sub-investment-grade rating, negative FCF after buybacks, and a multi-billion convertible-dependent refinancing ladder makes this a **structurally higher-risk credit than at any point in AKAM's history**. FY2025 was the year AKAM stopped being a cash-generative CDN compounder and became a leveraged AI-infrastructure lessor.

### 6. Key Red Flags

1. **Fallen angel / negative momentum:** S&P BB+ (two cuts in 2026), Moody's Baa3. Losing IG status triggers index exclusion and forced selling by IG-only mandates — a mechanical, non-fundamental overhang.
2. **Leverage trajectory, not level, is the problem:** net debt/EBITDA 3.26x → 4.26x in 12 months; gross debt +49%. Post-balance-sheet 2026 convertible issuance (**~$2.5bn across 2028/2031 converts**, refinancing the $1.15bn 0.375% notes due 2027) implies **pro forma gross debt of ~$8–9bn** and leverage materially above the reported 4.26x. *(Sequence unverified; balance sheet does not reflect it.)*
3. **Reported 20.4x interest coverage is not real.** $30.8m of interest expense on $6.9bn of debt means interest is being capitalised into the build. True coverage is likely under 3x on EBIT. Do not underwrite the reported number.
4. **Buybacks ($800m) exceeded FCF ($699m)** — shareholder returns debt-funded while the rating was being cut. A clear capital-allocation red flag.
5. **Low-quality FCF:** SBC of $459m is 66% of reported FCF and 10.9% of revenue (2.1x 2022 levels). Economic FCF is ~$240m — a 1.8% yield, not 5.2%.
6. **Gross margin compression:** 59.4% → 54.7% (−470bps) as mix shifts to capital-intensive compute delivery. Structural, not cyclical.
7. **Capex intensity doubling:** $458m (2022, 12.7% of rev) → $820m (2025, 19.5% of rev); FCF margin 22.6% → 16.6%. The business is consuming more capital per dollar of revenue every year.
8. **Thin tangible equity:** $1.16bn against $5.9bn net debt; 77% of book equity is goodwill/intangibles from an acquisition-led strategy. Recovery value for unsecured creditors is heavily reliant on PP&E ($3.8bn) with limited alternative use.
9. **Counterparty concentration:** the $11.6bn Anthropic commitment is transformative in both directions — it is simultaneously the key mitigant and the key single-name risk.
10. **Rating/refinancing cliff:** convertibles maturing 2027, 2028, 2031 — the company is now dependent on continued access to convertible markets at IG-adjacent cost of capital while it is rated sub-investment-grade.

### Data Gaps (explicit)
- No **CDS spreads** or bond-level pricing — cannot quantify market-implied default probability.
- **Revolver size, drawn balance and covenant terms** not available (critical: at 6.3x stressed leverage a 4.0x maintenance covenant would be breached if drawn).
- **Quarterly debt maturity ladder** not disclosed in tool data; maturities inferred from press releases.
- **Capitalised interest** not broken out — gross-interest coverage is my estimate.
- **No peer comparables** pulled (sector peer set available but not retrieved within budget).
- Volatility/beta tool output conflicts with both the price series and the company profile — treated as unreliable.
- Profile price ($91.70) and price-history close ($97.15) differ; market cap/valuation ratios carry ~6% uncertainty.
