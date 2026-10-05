# Fin Risk Analyst

- Symbol: NBIS
- Elapsed: 238.4s

---
All data gathered. Assembling the final assessment.

---

# NBIS — Nebius Group N.V. — Financial Risk Assessment

**Entity:** Amsterdam-based AI-cloud/GPU-infrastructure builder (ex-Yandex international assets; Nasdaq relisting Oct-2024). Mkt cap ≈ **$56.5B**. **Data caveats:** FY2022–23 statements reflect legacy Yandex N.V. (Russia) and are excluded from the analysis; FY2025 and H1-2026 are the meaningful periods for the current entity. No public credit rating or CDS data exists — this is a **data gap**, and the Z-Score below uses book equity (indicative only).

---

## 1. Credit Risk Assessment — **Sub-Investment Grade (unrated, hybrid profile)**

Structurally FCF-negative, loss-making, and rapidly levering, but **exceptionally well-liquidity-backed** with long-dated, non-amortizing convertible debt. This is a "growth-balance-sheet" credit (high-yield/converts), not an operating credit — cash, not EBITDA, services the obligations.

## 2. Key Financial Risk Metrics

| Metric | FY2024 | FY2025 | Jun-2026 (Q) | Reading |
|---|---|---|---|---|
| Revenue | $117.5M | $529.8M (+351%) | n/a | Massive ramp, tiny base |
| Operating income | -$440.7M | **-$596.2M** | Q2 -$190M | Operating margin **-112.5%** |
| Net income | -$641.4M | +$101.7M | Q1 +$621M / Q2 -$190M | FY25 gain is non-operating |
| Debt / Equity | 0.02x | **1.08x** | 0.97x | Leverage ↑ ~50x in 12 mo |
| Total debt | $49.7M | $5.0B | **$10.06B** | Tripled in 6 months |
| Net debt | **-$2.4B** (net cash) | $1.30B | **$2.01B** | Turned net-debt |
| Net debt / EBITDA | n/m | **2.62x** | ~4x (est.) | From negative to levered |
| Interest coverage (EBIT/Int) | n/m | $90.8M/$57.8M = **1.57x** | deteriorating | New $10B debt → coverage <0 soon |
| Current / Quick / Cash ratio | 9.6 / 9.6 / 9.3 | 3.08 / 3.08 / 2.41 | ~4.0 / ~4.0 / ~3.4 | **Strong liquidity** |
| Cash & ST investments | $2.45B | $3.68B | **$8.04B** | Post-$4.3B raise |
| Altman Z-Score | — | **1.10 (distress zone)** | — | Book-equity artifact; with $56B mkt cap → Z >5. Treat as noise |
| Piotroski F-Score | — | **8/9 (Strong)** | — | Profits, margins, efficiency improving |

**Debt structure (media-verified):** convertible senior notes — $1B due 2030, $1B due 2032 (2025), plus $2.75B due 2030 and $1.75B due 2034 (closed Mar-2026, ~$4.34B). Short-term debt only ~$47M. **No near-term refinancing cliff, but conversion = permanent share-dilution overhang.**

## 3. Market Risk Profile (extreme)

| Metric | Value |
|---|---|
| Annualised volatility (3y) | **113.3%** (top decile of market) |
| Beta vs SPY (3y) | **2.79** (reported beta 1.46) |
| Max drawdown (3y) | **-58.3%** |
| Sharpe (0% Rf, 3y) | 1.68 (driven by parabolic appreciation, not stability) |

Tail risk is severe: a market drawdown amplifies ~2.8x on NBIS, and the stock has already shown it can lose 58% in a cycle. This is a **high-beta, high-vol, momentum-driven** instrument.

## 4. Downside Scenario — Revenue -20% (FY2025 base)

- Revenue $529.8M → **$423.8M**; at 68.6% gross margin, gross profit falls ~$73M to **$290.7M** (opex ~$960M is largely fixed).
- Operating loss widens from -$596M to **≈ -$670M**; EBITDA (adj.) falls ~$73M to ≈ **$422M**.
- **Net debt/EBITDA:** 2.62x → **~3.3–3.8x** at current net debt, and worse on H1-26 leverage (net debt $2.0B → **>4.5x**). Coverage EBIT/interest turns deeply negative.
- **Cash runway:** H1-2026 FCF ≈ -$3.6B (annualized ≈ **-$7B+**, capex run-rate ~$16B). Cash $8.0B ⇒ **~12–14 months runway at current burn** — burden shifts entirely to capital markets. A demand shock + frozen credit = forced dilution or capex cut, idling GPU assets.
- **Mitigants:** strong cash, no near-term maturities, proven ability to raise $6B+ equity+debt in 12 months (Microsoft partnership, Nvidia-linked demand).

## 5. Overall Financial Risk Rating — **High** (Borderline Critical on FCF)

**What saves it from Critical:** $8B cash, negative working-capital needs, long-dated convert-only maturities, rapidly improving gross margins and asset-turnover (F-Score 8), booked revenue growth >350%/yr. **What keeps it High:** structurally negative FCF on a $10B+ debt base, negative operating income, cash runway ≤14 months reliant on open capital markets, and equity-like volatility/beta.

## 6. Key Red Flags

1. **FCF burn is enormous and compounding:** -$3.68B FY25; -$3.6B in H1-26 alone; capex at ~$16B/yr run-rate (PPE $6.5B → $14.9B in 6 months). Every quarter adds more debt/inventory-of-GPUs before revenue catches up.
2. **Leverage inflection:** Total debt $0.05B (FY24) → $5.0B (FY25) → **$10.1B (Jun-26)**; turned from $2.4B net cash to **$2.0B net debt** in 18 months.
3. **Interest coverage ≤1.57x and falling** — EBIT cannot service the current debt stack once 2026 coupons (convert notes, semiannual from Sep-2026) ramp.
4. **H1-26 operating cash flow is inflated by working-capital inflows (+$2.9B)** — likely customer prepayments/deposits; not durable earnings-quality, revertable.
5. **Altman Z (book) in distress zone (1.10)** and **no public credit rating/CDS** — you cannot hedge or price credit risk on this name.
6. **Shareholder overhang:** ~$6B+ of converts outstanding → structural dilution; Yandex legacy governance/complexity (Netherlands-incorporated, share-class structure).
7. **Extreme market risk:** 113% vol, 2.79 beta, 58% prior drawdown — position sizing must be treated as **equity-with-option-characteristics**, not an infra bond.

*Gaps: quarterly revenue/FY26 income statement not retrieved; exact convert coupons and indenture covenants (leverage/cash-flow clauses) not confirmed; no peer set of comparable AI-infra credits (sector peers are megacap semis — not relevant).*
