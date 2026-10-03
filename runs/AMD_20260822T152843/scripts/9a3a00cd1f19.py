
# Save a clean markdown table of the results for the final report
import json

with open('data/amd_computed_metrics.json') as f:
    metrics = json.load(f)

# Group metrics for clean presentation
groups = {
    'Market & Valuation': [k for k in metrics if any(x in k for x in ['Price', 'Market Cap', '52-Week', 'P/E', 'EV/EBITDA', 'P/S', 'P/B', 'P/FCF', 'MA', 'Beta'])],
    'Growth': [k for k in metrics if 'CAGR' in k],
    'Profitability Margins (%)': [k for k in metrics if 'Margin' in k and 'Beneish' not in k],
    'Returns (%)': [k for k in metrics if any(x in k for x in ['ROE', 'ROIC'])],
    'Balance Sheet Health': [k for k in metrics if any(x in k for x in ['Debt/Equity', 'Current Ratio'])],
    'Cash Flow (USD M)': [k for k in metrics if any(x in k for x in ['OCF', 'FCF', 'CapEx'])],
    'Quality & Risk Scores': [k for k in metrics if any(x in k for x in ['Altman', 'Piotroski', 'Accruals', 'Volatility'])],
    'DCF Valuation': [k for k in metrics if 'DCF' in k],
    'Beneish M-Score Inputs': [k for k in metrics if 'Beneish' in k],
}

lines = []
lines.append("# AMD Quantitative Metrics Report\n")
lines.append("**Date:** As of latest available data (price timestamp 2025-08-22)\n")
lines.append("**Ticker:** AMD (NASDAQ)\n")
lines.append("---\n")

for group_name, keys in groups.items():
    lines.append(f"\n## {group_name}\n")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    for k in keys:
        v = metrics[k]
        if v is None:
            v_str = "N/A"
        elif isinstance(v, (int, float)):
            v_str = f"{v:,.2f}" if isinstance(v, float) else str(v)
        else:
            v_str = str(v)
        lines.append(f"| {k} | {v_str} |")

with open('data/amd_metrics_report.md', 'w') as f:
    f.write('\n'.join(lines))

print("Saved report to data/amd_metrics_report.md")
print("\n".join(lines[:30]))
