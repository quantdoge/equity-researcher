# Sector Researcher

- Symbol: COHR
- Elapsed: 34.8s

---
I have sufficient data. Writing the brief now.

---

# Sector Brief: Coherent Corp (NYSE: COHR)
### Photonics & Optical Connectivity for AI Data Centres

**Note on scoping:** The sector-peers tool returned mega-cap Technology constituents (AAPL, NVDA, MSFT) which are not meaningful comparables. COHR is a photonics/optical-components supplier, so I built a purpose-specific peer set: Lumentum (LITE), Fabrinet (FN), MKS Instruments (MKSI), Ciena (CIEN), Corning (GLW), Arista (ANET), IPG Photonics (IPGP). The `get_sector_financials` aggregate endpoint returned `company_count: 1` and is unusable — peer metrics below are computed from individual filings.

---

## 1. Sector Overview

Coherent sits in the optical components and photonics layer of the AI data-centre supply chain — InP/GaAs lasers, optical transceivers, high-precision optics and semiconductor capital equipment. The datacom transceiver market was ~$16.5bn in 2025 and is tracking toward ~$26bn in 2026, with 800G-and-above port shipments rising from ~24m units (2025) to ~63m (2026); Coherent itself guides the 800G/1.6T/3.2T transceiver market to a **>40% five-year CAGR**. The sector is capacity-constrained rather than demand-constrained: indium phosphide (InP) laser fab capacity is the binding bottleneck, which is transferring pricing power to suppliers holding qualified capacity. Concentration is moderate-to-high (est. HHI ~1,200–1,500; top-3 share ~40–45%) and rising fast — **Marvell agreed on 2 Nov 2026 to acquire Lumentum for ~$115bn in stock**, removing an independent competitor and validating the strategic scarcity of InP capacity. Barriers to entry are high: multi-year fab lead times, customer qualification cycles of 12–24 months, and deep process IP.

---

## 2. Key Tailwinds

- **AI cluster optical intensity is stepping up per generation.** 800G→1.6T→3.2T transitions raise optical content per accelerator; Ethernet optics sales doubled in 2024 and rose another ~70% in 2025 (LightCounting). COHR's own revenue went $5.81bn→$7.12bn (+22.5%) in FY26, then re-accelerated to **+49.9% YoY in Q1 FY27 ($2.37bn vs $1.58bn)** — with management guiding **>60% revenue growth for FY27**.
- **Pricing power is inflecting on InP scarcity.** COHR gross margin expanded 30.9% (FY24) → 35.4% (FY25) → 37.5% (FY26) → **39.1% (Q1 FY27)**; operating margin 2.6% → 9.5% → 12.7% → **15.9%**. This is operating leverage plus mix, not one-off.
- **Contract-backed visibility and sector consolidation.** A **$20bn five-year PhotonLink agreement** (ramping to ~$250m/quarter by end-2027) converts COHR from spot-priced module sales to contracted scarcity pricing. The Marvell–Lumentum deal compresses the competitive field and raises the strategic value of COHR's remaining independent capacity.

---

## 3. Key Headwinds

- **Extreme valuation volatility / beta 2.23.** COHR peaked near $440 (early June 2026) and closed **$192.81 on 6 Nov 2026 — a ~56% drawdown** despite sequentially *improving* results, including a −14% single-day fall on a beat-and-raise print. The sector is trading on AI-capex sentiment, not near-term earnings.
- **Capital intensity and cash burn ahead of revenue.** COHR is spending heavily to build InP/optical capacity; inventory build and operating cash flow conversion are the key watch items (flagged by sell-side as "the defining number"). Heavy depreciation ($147m/quarter) will pressure margins if growth decelerates.
- **Customer concentration and China exposure.** Hyperscaler concentration is rising, and Chinese transceiver vendors (Innolight, Eoptolink) are scaling aggressively at lower cost. MKSI (+9.6%) and IPGP (+2.7%) show how quickly growth fades for optical names without direct AI-datacom leverage.

---

## 4. Peer Comparison Table

*Latest reported fiscal year; COHR FY ends June.*

| Company | Ticker | Latest FY | Revenue | Rev growth YoY | Gross margin | Operating margin |
|---|---|---|---|---|---|---|
| **Coherent** | **COHR** | **FY26 (Jun-26)** | **$7,118m** | **+22.5%** | **37.5%** | **12.7%** |
| Lumentum | LITE | FY26 (Jun-26) | $3,014m | +83.2% | 41.7% | 17.4% |
| Fabrinet | FN | FY26 (Jun-26) | $4,641m | +35.7% | 12.0% | 10.0% |
| Arista Networks | ANET | FY25 (Dec-25) | $9,006m | +28.6% | 64.1% | 42.8% |
| Corning | GLW | FY25 (Dec-25) | $15,629m | +19.1% | 35.3% | 14.9% |
| Ciena | CIEN | FY25 (Oct-25) | $4,770m | +18.8% | 42.0% | 6.5% |
| MKS Instruments | MKSI | FY25 (Dec-25) | $3,931m | +9.6% | 40.4% | 14.4% |
| IPG Photonics | IPGP | FY25 (Dec-25) | $1,004m | +2.7% | 38.0% | 1.3% |
| **Peer median (8)** | | | | **+20.8%** | **39.2%** | **13.5%** |
| **COHR vs median** | | | | **+1.7 pts** | **−1.7 pts** | **−0.9 pts** |

**Supplements:** COHR market cap $38.0bn. On the most recent quarter COHR's +49.9% (≈+56% pro forma) growth is top-of-group, well ahead of the FY-basis median — i.e. COHR is *gaining* relative momentum. LITE's FY26 net income (−$6.9bn) is distorted by a large non-cash charge and is not comparable; its gross/operating margins are used instead. Peer market caps and forward multiples were not available from the feed and are excluded rather than estimated.

---

## 5. Coherent's Competitive Position: **Strong**

**Rationale:**
- **Share gainer, not share donor.** FY-basis growth of +22.5% sits modestly above median, but the acceleration to ~+50–56% in Q1 FY27 with >60% FY27 guidance places COHR at the top of the group alongside LITE — and COHR is doing it on a $7.1bn base, ~2.4x LITE's.
- **Only vertically integrated player at scale.** COHR owns InP/GaAs epitaxy, laser fab, optics and module assembly — the broadest portfolio in the set (datacom + industrial + semiconductor capex + aerospace/defence). This diversification is why it outgrew MKSI and IPGP, which lack datacom leverage.
- **Margin catch-up is the story, not margin leadership.** At 37.5% GM / 12.7% OM COHR still trails the peer median — a legacy of the II-VI/Coherent merger integration and inventory step-ups. The trajectory (OM 2.6%→15.9% in seven quarters) implies material room to converge on LITE's 17.4% and beyond.
- **Structural advantage from the Marvell–Lumentum tie-up.** With Lumentum absorbed, COHR becomes the largest *independent* merchant supplier of InP laser capacity — a valuable position, though it also faces a better-capitalised, vertically integrated rival.
- **Caveats:** highest beta in the group (2.23), heaviest capital requirements, and a $20bn contract that concentrates customer risk. Fabrinet remains the low-cost manufacturing benchmark (12% GM by design, contract model) — COHR does not compete there.

---

## 6. Sector Rating: **ATTRACTIVE**

**The sector is in a capacity-constrained hypergrowth phase — early-to-mid cycle, not mature.** Demand visibility is contract-backed (>40% five-year transceiver CAGR, 800G volumes more than doubling), pricing power is positive for the first time in years as InP capacity stays sold out, and consolidation is shrinking the competitive field. Supply discipline — not demand — is the swing factor, and capacity additions only land in 2027–28, supporting margins through that window.

**Two qualifications keep this from being unambiguously bullish:** (i) the equity market has already begun de-rating the group violently (−56% for COHR from the June peak on *improving* fundamentals), implying the sector is late in its *valuation* cycle even while early in its *volume* cycle; and (ii) the model is highly levered to a handful of hyperscaler capex budgets, so a single AI-spend digestion quarter could compress multiples and estimate revisions simultaneously. **Attractive on fundamentals; high-volatility with acute drawdown risk on sentiment.**
