# Fin Risk Analyst

- Symbol: MSTR
- Elapsed: 73.8s

---
I have sufficient data. Compiling the assessment.

---

# MSTR (Strategy Inc.) — Financial Risk Assessment

**As of:** mid-November 2026 | **Price:** $96.50 | **Market cap:** ~$38.9B | **Diluted shares:** ~385M | **Last filed period:** FY2025 (12/31/25) audited; Q3 2026 reported

**Structural note up front:** MSTR is not a software company that owns Bitcoin — it is a **3.5× levered, preferred-heavy Bitcoin closed-end fund with a subscale software business attached.** 95.5% of assets ($58.85B of $61.64B) are Bitcoin-classified intangibles. Conventional ratio analysis is therefore misleading in both directions, and I have adjusted for that throughout.

---

## 1. Credit Risk Assessment — **Sub-Investment Grade (CCC-equivalent), Negative Outlook**

| Metric | Reported | Risk Read |
|---|---|---|
| Debt/Equity | 0.16× | **Understated.** Preferred equity ($13.5B) sits *inside* equity. Adjusted senior claims/equity = **0.40×** |
| Debt/Assets | 0.13× | Misleading — assets are marked at Bitcoin fair value, not recoverable cash flow value |
| Net debt | $5.98B | FY25. Convertibles since cut 18% to **$6.7B** (Q2'26) |
| Net debt/EBITDA | −1.1× | **Meaningless** — EBITDA is negative |
| Interest coverage (EBIT) | −0.63× (op. income basis); **−84× (EBIT basis)** | No operating coverage whatsoever |
| **Fixed-charge coverage incl. preferred divs** | **≈ −0.02×** | $(41)M op. income ÷ $(1,668)M of interest + preferred dividends |
| Altman Z-Score | **2.79 — Grey zone** | **Distorted.** x4 = 4.82 on $51B *book* equity; x3 = −0.089 from BTC mark-to-market, not operating losses. Not a valid signal here |
| Piotroski F-Score | **3 / 9 — Weak** | F1, F2, F3, F7, F8, F9 all fail. F7 = 0 (dilution); F2 = 0 (negative operating cash flow) |
| Credit rating / CDS | **Not available — data gap** | Proxy: preferred yielding **12.5% effective**; converts repurchased at 88–92¢ |

**The decisive fact:** the operating business does not cover its financing costs. FY2025 revenue $477M, gross profit $328M, **operating income −$41M**, operating cash flow **−$67M**. Against that sit ~$65M interest and **~$1.6B/yr of preferred dividends** ($400.7M in Q2 2026 alone). Every dollar of the dividend is paid from the balance sheet or new issuance. **This is a structural dependency on capital-markets access, not a cash-generating credit.**

---

## 2. Liquidity Risk — Headline strong, structurally fragile

| Metric | Value | Comment |
|---|---|---|
| Current ratio | 5.62× | 92% of current assets is cash |
| Quick / Cash ratio | 5.62× / 5.05× | No inventory, so quick = current |
| Cash | $2.30B | USD reserve +12% QoQ in Q2'26 |
| Working capital | $2.11B | |
| Assets/Liabilities | 5.82× | |
| **Cash ÷ annual preferred dividends** | **~1.4×** | The real liquidity metric |
| **Cash runway (divs + interest + op. burn)** | **~14–18 months** | Assumes no new issuance, no BTC sales |

**Maturity / refinancing profile.** $6.7B convertibles, laddered 2027–2032, with holder put options in 2027–2028. Much is 0%-coupon, which caps cash interest but **does not cap principal repayment**. The 2030 notes carry a conversion price ~$767 (vs $96.50 spot) — effectively straight debt requiring $2B+ of cash refinancing. Silver lining: 2029 converts at a **$90 conversion price** are struck near spot, so a recovery converts them to equity rather than cash — dilutive, not default-inducing.

**Mitigants:** near-zero short-term debt ($31M); ability to sell BTC; demonstrated access to preferred markets (STRC raised $5.58B in Q1'26); active liability management (repurchasing convertibles at 92¢ and preferred at a 13% discount — sensible, but a classic sign of a stressed borrower managing its stack).

---

## 3. Market Risk Profile — **Extreme**

| Metric | Value |
|---|---|
| Annualised volatility | **85.5%** |
| Beta vs SPY | **2.47** (trailing); 3.61 (5Y, per profile) |
| **Max drawdown (3Y)** | **−82.6%** |
| Sharpe ratio | 0.18 |
| Sortino ratio | **Not available — data gap** |

Risk-adjusted returns are poor: an 85% vol asset delivering a 0.18 Sharpe means the equity is a leveraged Bitcoin beta expression with essentially no compensation for idiosyncratic capital-structure risk. A 2.47 beta means a 20% S&P drawdown mechanically implies a ~50% MSTR move, before Bitcoin's own beta on risk assets.

---

## 4. Downside Scenario Analysis — Bitcoin Decline

Base: 850,364 BTC ≈ **$54.7B** treasury (BTC ~$64,300) + $2.7B cash − $6.7B converts − $13.5B preferred = **$37.2B common NAV ≈ $96.6/share** — i.e., the stock trades at **~1.0× adjusted NAV** (mNAV 0.80× on a gross basis per third-party data).

| BTC scenario | Treasury value | Common NAV | Per share | vs $96.50 |
|---|---|---|---|---|
| Base | $54.7B | $37.2B | $96.6 | 0% |
| **−20%** | $43.8B | $26.3B | $68 | **−29%** |
| **−40%** | $32.8B | $15.3B | $40 | **−59%** |
| **−60%** | $21.9B | $4.4B | $11 | **−88%** |
| **−70%** | $16.4B | −$1.1B | **$0** | **−100%** |
| **−75%** | $13.7B | −$3.8B | $0 | Preferred recovers **~72¢** |

**Key thresholds:**
- **Common equity breakeven: BTC ≈ $20,600 (−68%).** Only ~$17.5B of treasury value stands between today and zero for shareholders, because $20.2B of senior claims ($6.7B debt + $13.5B preferred) precede them.
- **Preferred impairment begins ~BTC $16,000 (−75%).** That the preferred trades at **$64/$100 par** is consistent with the market pricing roughly this recovery band.
- **Revenue −20% scenario is irrelevant** to solvency: a $477M software business with −$41M operating income cannot move a $61B balance sheet either way. The requested revenue stress test is immaterial; **the Bitcoin stress test is the only one that matters.** The software segment's ~$0 EBITDA means it contributes zero debt-service capacity.

**Flywheel break — the underappreciated risk.** Historically MSTR issued equity at 1.5–2.5× NAV, accretively raising BTC-per-share. At **~1.0× adjusted NAV (0.80× gross)**, ATM issuance is **NAV-dilutive**, so the engine that funded the dividends has stalled. Management has correctly pivoted to buying back discounted preferred and converts, but this **removes the funding source for a $1.6B/yr cash dividend while operating cash flow is negative** — a self-reinforcing negative if NAV per share starts declining.

---

## 5. Overall Financial Risk Rating: **HIGH**

Not "Critical" — liquidity is genuinely ample ($2.3B+ cash, 5.6× current ratio), there is no near-term default trigger, and 0% coupons on most converts defer cash interest. But **High** is warranted because: (a) fixed-charge coverage is negative, (b) the dividend obligation is ~24× the software segment's gross profit, (c) 95% of assets are a single 85%-vol, non-cash-flowing asset, and (d) $20.2B of senior claims sit ahead of common on a $54.7B collateral base. Equity is a **deep out-of-the-money call option on Bitcoin with a decaying cash buffer**.

---

## 6. Key Red Flags

1. **Negative fixed-charge coverage (−0.02×)** — $1.6B/yr preferred dividends vs −$41M operating income. Dividends funded by balance sheet, not earnings.
2. **Preferred stack ($13.5B) is now 2× convertible debt ($6.7B)** and trades at **~64% of par** with 12%+ effective yields — the market is pricing impairment risk in the senior-most equity tranche.
3. **Reported leverage badly understates risk.** D/E of 0.16× becomes 0.40× once preferred is correctly treated as a senior claim.
4. **~3× share dilution in three years** (137M → 192M → 294M → ~385M) with Piotroski F7 = 0. BTC-per-share growth is now being achieved despite, not because of, the capital structure.
5. **mNAV premium has collapsed to ~1.0×**, breaking accretive equity issuance — the funding mechanism for the dividend.
6. **Altman Z (2.79) and net debt/EBITDA (−1.1×) are analytically invalid here** due to negative EBITDA and fair-value-marked assets. Any screen relying on them will mis-rate MSTR.
7. **Convertibles repurchased below par (88–92¢) and preferred at a 13% discount** — rational liability management, but a hallmark of a stressed capital structure.
8. **Extreme market risk:** 85.5% vol, 2.47 beta, −82.6% max drawdown, 0.18 Sharpe.

## Data Gaps (explicit)
- **Itemized convertible maturity schedule** (2027–2032 amounts) — company `/debt` page and SEC EDGAR both returned HTTP 403; only the $6.7B aggregate and 2030/$2B detail confirmed.
- **Preferred series-by-series par and coupon** — only the ">$13.5B outstanding" aggregate is confirmed; $13.5B used as estimate.
- **Exact USD reserve balance** and Q3 2026 balance sheet — only "+12% QoQ" disclosed.
- **Credit rating, CDS spreads, Sortino ratio** — unavailable from provided tools.
- **Price conflict:** data feed shows $96.50 / mNAV 0.80×; strategy.com reports $111.62 / mNAV 1.09× (likely different dates). Analysis uses the $96.50 feed value; at $111.62 the common-NAV discount narrows but no conclusion changes.
