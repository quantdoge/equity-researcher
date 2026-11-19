# Quant Analyst

- Symbol: AKAM
- Elapsed: 177.4s

---
## AKAM (Akamai Technologies) — Quantitative Factor Report
**Price $91.70 (last close 2026-11-18) · Mkt cap $13.5B · EV $19.2B · Net debt ~$5.7B**

### ⚠️ Data-integrity flags (read before using the table)
Three tool outputs failed cross-checks against the raw tape. I report both but weight my reconstruction:

1. **Earnings Revision tool is structurally invalid.** It compared the **2030E** EPS ($14.99) against the **2029E** ($12.585) and called +19.11% an "upgrade." That is the 2029→2030 *growth rate*, not a same-period revision. **Discard the +19.11%.** Actual revision evidence is the opposite: of 6 recent notes, **5 were price-target *cuts*** (RBC 85, UBS 90, FBN 120, MSFT-side 149, KeyBanc 175, Evercore 150 reiterated).
2. **Momentum tool (−22.63%) is stale.** Reconstructed from raw prices: 12-month total return **+4.5%** ($87.74 → $91.70); 12-1 momentum **≈ +20.7%** ($74.25 → $89.63). The −22.6% figure matches the **peak-to-current** decline, not 12-1.
3. **Max drawdown (−51.69%) looks overstated.** My close-basis reconstruction gives **−42.4%** ($118.44 on 2026-09-23 → $68.21 on 2025-04-08). Windows I could not sample may reconcile this; treat DD as −42% to −52%.
4. **Beta instability:** factor-tool beta 1.35–1.42 vs company-profile 5-yr beta **0.664**.

### 1. Factor Scores
| Factor | Score | Sector Rank* | Signal |
|---|---|---|---|
| **Value** | **6.5/10** | 1 of 3 (cash-flow basis) | **Attractive** — EV/EBITDA 14.3, P/FCF 19.3, FCF yield 5.19%; P/E 29.9 only in line |
| **Momentum** | **4/10** | 3 of 3 (tool) / 1 of 3 (reconstructed) | **Conflicting / low confidence** — 12-1 ≈ +20.7% but −22.6% off the Sep-2026 peak |
| **Quality** | **3/10** | 3 of 3 | **Weak** — ROE 9.1%, GP/Assets 20.1%; accruals −9.3% is best-in-set; F-Score **5/9** |
| **Low Vol** | **2/10** | 3 of 3 (unverified) | **Poor** — ann. vol 66.5% (1y) / 55.1% (2y), beta 1.42 |
| **Earnings Revision** | **3/10** | n/a | **Negative** — 5 of 6 PT cuts; tool's +19.1% is an artifact |

*\*Rank of only 3 comparables sampled (AKAM, CSCO, MSFT). Not a true sector quintile — a full cross-section was out of budget. Treat as indicative only.*

**Peer comparison (the crux):**
| | P/E | EV/EBITDA | P/FCF | ROE | GP/Assets | Accruals |
|---|---|---|---|---|---|---|
| **AKAM** | 29.9 | **14.3** | **19.3** | **9.1%** | **20.1%** | **−9.3%** |
| CSCO | 29.2 | 20.0 | 30.4 | 26.4% | 31.5% | −0.7% |
| MSFT | 28.3 | 18.5 |
