# Short Analyst

- Symbol: AKAM
- Elapsed: 75.4s

---
I have enough to write. Two data gaps to note honestly: the 10-K retrieval failed and akamai.com blocked the press release fetch (I used the filed 8-K exhibit and secondary sources instead).

---

# AKAM — Forensic Short-Seller Analysis
**Price $91.70 (18-Nov-2026) · Mkt cap $13.2B · Net debt $8.30B · EV ~$21.5B**

---

## 1. Earnings Quality Assessment: **LOW** (not fraudulent)

No fraud. This is a **capital-allocation and cash-flow quality** problem wearing an earnings-quality costume.

The headline screens look *great* and they are misleading:

| Metric | Value | The catch |
|---|---|---|
| Cash conversion (OCF/NI) | **3.36x** | Not efficiency — it's $526M TTM SBC plus $743M D&A being added back |
| Accruals ratio | **-0.093** | Genuinely clean. Negative accruals are a real strength |
| Beneish M-Score | **-2.80** | Low manipulation risk. Passes |
| Piotroski F-Score | **5 / 9** | Mediocre: fails on ROA improvement, leverage, margins, turnover |
| Composite quality score | **60 / 100** | The weak one — and it's the closest to right |

**The single most important number in this analysis:**
- TTM FCF = **+$211M** (and FY2026 guided to roughly **-$1.1B**)
- TTM SBC = **$526M** = 12.0% of revenue = **136% of TTM net income**
- **True economic FCF = $211M − $526M = −$315M**

AKAM's reported profitability is a stock-compensation artifact. Strip the SBC add-back and the business consumed $315M of economic value over the last twelve months. That is the entire thesis in one line.

## 2. Key Red Flags

**① Capex has gone vertical, with no revenue attached to it**
Q3-26 capex $605M = **53.9% of revenue** (Q3-25: 18.5%). FY26 guidance **$2.445–2.645B**, ~57% of FY26 revenue, versus 19.5% in 2025. They are spending 3x the prior baseline — and the Anthropic deal that justified it explicitly "leaves 2026 revenue guidance unchanged."

**② Free cash flow has already gone negative**
Q3-26 FCF **−$172M**. 9M-26 FCF a thin +$49M. With $1.42–1.62B of Q4 capex still to spend against ~$380M of quarterly OCF, FY26 FCF lands near **−$1.1B**, a swing from +$699M in 2025.

**③ The depreciation cliff is arithmetic, not opinion**
D&A is 17% of revenue; capex is 57%. Capex is running at **3.2x depreciation**. New capex depreciating over ~5 years adds ~$500M/yr of incremental D&A starting 2027. TTM EBITDA is $1.24B. TTM D&A is on track toward **$1.3B+ in 2027 and $1.6B in 2028** — i.e. D&A overtakes EBITDA. GAAP operating income goes negative in 2028 *unless revenue roughly doubles.* That is the whole ballgame.

**④ Gross margin: 860bp of erosion in four years**
63.3% (2021) → 59.4% (2024) → 54.7% (2025) → 55.0% (Q3-26). For a company claiming a security and edge-compute pivot, this is the signature of pricing loss, not mix shift. Cost of revenue grew 50% since 2021 while revenue grew 21.6%.

**⑤ Operating margin collapse, quarter by quarter**
15.7% (Q3-25) → 13.8% → 10.7% → **7.3%** (Q2-26) → 9.7% (Q3-26). From 22.6% in 2021. Net income fell from $140.2M to $117.1M YoY on 6.4% *higher* revenue.

**⑥ DSO deterioration — the one accruals flag that IS firing**
Receivables $958M vs $794M at YE25 (+20.7%) on revenue +6.4%. DSO on quarterly revenue: ~66 days → **~78 days**. Annual screen flagged AR growth 9.07% vs revenue 5.44%. ~$130M of revenue is sitting in receivables that wasn't there a year ago. Could be Q3 timing; on its own it's a yellow flag, in combination with everything else it matters.

**⑦ ROIC has fallen below cost of capital**
NOPAT ≈ $341M on ~$12B invested capital = **~2.8% ROIC vs ~8% WACC.** ROE: 12.4% (2022) → 7.5% (TTM). They are deploying capital at a negative spread and accelerating.

## 3. Beneish M-Score & Accruals Detail

**M-Score −2.796** (threshold −2.22) — clean, comfortably. TATA of −0.0929 is doing all the work and it's legitimate.

But read the *components*, not just the score. **Six of eight indices are above 1.0**, all pointing the same way — mild, systemic deterioration:
- **GMI 1.085** — gross margin deteriorating
- **DSRI 1.034** — receivables outpacing revenue (note: 2026 will push this much higher, toward ~1.14)
- **DEPI 1.131** — depreciation rate *falling* relative to capex, i.e. asset lives lengthening as the asset base balloons
- **AQI 1.030 · SGAI 1.060 · SGI 1.054 · LVGI 1.070**

**Accruals:** −0.077 TTM, negative for four straight years. Verdict: **books are honest; the business economics are not.** Distinguishing these two is the difference between a Chanos short and a Hindenburg short. This is the former.

## 4. Competitive Threat Assessment

This is where the case gets uncomfortable for longs.

- **The CDN core is a melting ice cube.** Hyperscaler edge offerings (CloudFront, Cloudflare, Fastly) have commoditised delivery. AKAM's answer was to pivot into **Cloud Infrastructure Services** — selling GPU compute against AWS, Azure, GCP, CoreWeave and Nebius. That is a brutal, deflationary, capital-devouring business with no structural advantage for a late entrant. A 55% and falling gross margin is the market telling you they're buying share with price.
- **The Anthropic contract is rented, not owned.** The 10-Q's filed MSA (Exhibit 10.1, effective 5-May-2026, AKAM ↔ **Anthropic PBC**) is expressly **non-exclusive (Section 3.2)**. Anthropic — a cash-burning private lab backed by AKAM's own competitors — may procure elsewhere at any time. AKAM is committing ~$5.5B of largely irreversible GPU capex against a contract counterparty that is non-exclusive, may terminate, and whose funding depends on third parties who are also AKAM's competitors. **$5.5B of irreversible cost against cancellable revenue is the definition of a bad risk.** The $2.8B of YTD CIS bookings is real, but multi-year and back-end loaded.
- **Concentration.** One customer's infrastructure decisions now drive the entire capital budget of a $4.4B-revenue company.

## 5. Management & Governance Red Flags

1. **The buyback stopped dead.** $800M in Q4-25, $206M Q1-26, $410M Q2-26, then **$0 in Q3-26** — precisely as the stock fell from $161 to $78. Management repurchased most aggressively near the highs and not at all near the lows. That is not a valuation-support
