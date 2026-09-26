"""
Equity Research MCP Server.

Single FastMCP server that registers every tool with role-based tags.
Agents receive only the subset of tools matching their role tag — enforcement
happens in agent_factory.py by filtering the tool list before each Claude call.

Run standalone:
    fastmcp run equity_mcp/server.py

Inspect all tools and their tags:
    fastmcp inspect equity_mcp/server.py
"""

from __future__ import annotations

from dotenv import load_dotenv

load_dotenv()

from fastmcp import FastMCP

from equity_mcp.roles import (
    ALT_DATA, ESG, FIN_RISK, GEO_LEGAL, GROWTH,
    MACRO, NONFIN_RISK, PORTFOLIO, QUANT, SECTOR, SHARED, SHORT, VALUE,
)

# ── Tool implementations ──────────────────────────────────────────────────────
from equity_mcp.tools.db import (
    get_analyst_estimates,
    get_balance_sheet,
    get_cash_flow,
    get_company_profile,
    get_dividends,
    get_earnings_calendar,
    get_income_statement,
    get_price_history,
    get_price_targets,
    get_research_universe,
    get_sector_financials,
    get_sector_peers,
)
from equity_mcp.tools.web import fetch_page, web_search
from equity_mcp.tools.calculations.valuation import (
    calculate_gross_margin_trend,
    calculate_intrinsic_value_dcf,
    calculate_owner_earnings,
    calculate_return_on_capital,
    calculate_revenue_growth_rates,
    calculate_rule_of_40,
    calculate_valuation_ratios,
    compare_peer_valuations,
)
from equity_mcp.tools.calculations.risk import (
    calculate_altman_z_score,
    calculate_fcf_yield,
    calculate_leverage_ratios,
    calculate_liquidity_ratios,
    calculate_piotroski_f_score,
    calculate_price_volatility,
)
from equity_mcp.tools.calculations.quant import (
    calculate_alpha_beta,
    calculate_earnings_revision_score,
    calculate_low_vol_score,
    calculate_momentum_score,
    calculate_quality_factor_score,
    calculate_sharpe_sortino,
    calculate_value_factor_score,
    calculate_correlation_matrix,
    rank_universe_by_factor,
)
from equity_mcp.tools.calculations.forensics import (
    calculate_accruals_ratio,
    calculate_beneish_m_score,
    calculate_earnings_quality_score,
    calculate_inventory_days_trend,
    calculate_receivables_growth_vs_revenue,
    detect_revenue_deceleration,
)
from equity_mcp.tools.external.fred import (
    fetch_inflation_data,
    fetch_macro_series,
    fetch_yield_curve,
)
from equity_mcp.tools.external.sec_edgar import (
    fetch_company_facts,
    fetch_filing_text,
    fetch_insider_trading_filings,
    search_regulatory_actions,
)
from equity_mcp.tools.external.news import (
    fetch_esg_controversy_news,
    fetch_geopolitical_news,
    fetch_news,
    fetch_news_sentiment_score,
    fetch_regulatory_news,
)
from equity_mcp.tools.external.alt_data import (
    calculate_earnings_surprise_history,
    fetch_google_trends,
    fetch_job_postings_trend,
    fetch_patent_filing_trend,
    fetch_social_sentiment,
    fetch_web_traffic_trend,
)

# ── Create the MCP server ─────────────────────────────────────────────────────

mcp = FastMCP(
    name="equity-research-mcp",
    instructions=(
        "Equity Research MCP server. Tools are tagged by agent role. "
        "Agents only receive tools matching their role tag."
    ),
)

# =============================================================================
# SHARED TOOLS — visible to every agent
# =============================================================================

mcp.tool(tags=SHARED)(get_price_history)
mcp.tool(tags=SHARED)(get_company_profile)
mcp.tool(tags=SHARED)(get_sector_peers)
mcp.tool(tags=SHARED)(web_search)
mcp.tool(tags=SHARED)(fetch_page)
mcp.tool(tags=SHARED)(get_research_universe)

# =============================================================================
# DATABASE — fundamental & event data (multi-agent)
# =============================================================================

mcp.tool(tags=VALUE | GROWTH | FIN_RISK | SHORT | QUANT | SECTOR | PORTFOLIO)(get_income_statement)
mcp.tool(tags=VALUE | FIN_RISK | SHORT | QUANT | PORTFOLIO)(get_balance_sheet)
mcp.tool(tags=VALUE | GROWTH | FIN_RISK | SHORT | QUANT | PORTFOLIO)(get_cash_flow)
mcp.tool(tags=VALUE | GROWTH | ALT_DATA | PORTFOLIO)(get_earnings_calendar)
mcp.tool(tags=VALUE | GROWTH | PORTFOLIO)(get_dividends)
mcp.tool(tags=GROWTH | QUANT | SHORT | PORTFOLIO)(get_analyst_estimates)
mcp.tool(tags=GROWTH | QUANT | VALUE | PORTFOLIO)(get_price_targets)
mcp.tool(tags=SECTOR)(get_sector_financials)

# =============================================================================
# VALUATION TOOLS — Value Researcher primary, Growth/Portfolio secondary
# =============================================================================

mcp.tool(tags=VALUE | GROWTH | QUANT | PORTFOLIO)(calculate_valuation_ratios)
mcp.tool(tags=VALUE)(calculate_owner_earnings)
mcp.tool(tags=VALUE | QUANT | PORTFOLIO)(calculate_return_on_capital)
mcp.tool(tags=VALUE)(calculate_intrinsic_value_dcf)
mcp.tool(tags=VALUE | PORTFOLIO)(compare_peer_valuations)
mcp.tool(tags=VALUE | GROWTH | SECTOR)(calculate_revenue_growth_rates)
mcp.tool(tags=VALUE | GROWTH | SECTOR)(calculate_gross_margin_trend)
mcp.tool(tags=GROWTH)(calculate_rule_of_40)

# =============================================================================
# RISK TOOLS — Financial Risk Analyst primary
# =============================================================================

mcp.tool(tags=FIN_RISK | PORTFOLIO)(calculate_leverage_ratios)
mcp.tool(tags=FIN_RISK)(calculate_liquidity_ratios)
mcp.tool(tags=FIN_RISK | SHORT)(calculate_altman_z_score)
mcp.tool(tags=FIN_RISK | SHORT | QUANT)(calculate_piotroski_f_score)
mcp.tool(tags=FIN_RISK | QUANT | PORTFOLIO)(calculate_price_volatility)
mcp.tool(tags=FIN_RISK | VALUE | PORTFOLIO)(calculate_fcf_yield)

# =============================================================================
# QUANTITATIVE TOOLS — Quant Analyst primary
# =============================================================================

mcp.tool(tags=QUANT | PORTFOLIO)(calculate_momentum_score)
mcp.tool(tags=QUANT)(calculate_value_factor_score)
mcp.tool(tags=QUANT)(calculate_quality_factor_score)
mcp.tool(tags=QUANT)(calculate_low_vol_score)
mcp.tool(tags=QUANT | GROWTH)(calculate_earnings_revision_score)
mcp.tool(tags=QUANT | PORTFOLIO)(calculate_alpha_beta)
mcp.tool(tags=QUANT | PORTFOLIO)(calculate_sharpe_sortino)
mcp.tool(tags=QUANT | PORTFOLIO)(calculate_correlation_matrix)
# NOTE: not exposed to HEAD_OF_RESEARCH — a single call fans out over up to 100
# symbols x ~7 DB helpers, each opening its own connection (see tools/calculations/quant.py).
mcp.tool(tags=QUANT)(rank_universe_by_factor)

# =============================================================================
# FORENSIC / SHORT TOOLS — Short Analyst primary
# =============================================================================

mcp.tool(tags=SHORT)(calculate_beneish_m_score)
mcp.tool(tags=SHORT | QUANT)(calculate_accruals_ratio)
mcp.tool(tags=SHORT)(calculate_earnings_quality_score)
mcp.tool(tags=SHORT)(detect_revenue_deceleration)
mcp.tool(tags=SHORT)(calculate_receivables_growth_vs_revenue)
mcp.tool(tags=SHORT)(calculate_inventory_days_trend)

# =============================================================================
# MACRO TOOLS — Macro Researcher primary
# =============================================================================

mcp.tool(tags=MACRO)(fetch_macro_series)
mcp.tool(tags=MACRO | FIN_RISK | PORTFOLIO)(fetch_yield_curve)
mcp.tool(tags=MACRO | GEO_LEGAL)(fetch_inflation_data)

# =============================================================================
# SEC EDGAR TOOLS — multiple agents
# =============================================================================

mcp.tool(tags=VALUE | GEO_LEGAL | NONFIN_RISK | SHORT)(fetch_company_facts)
mcp.tool(tags=VALUE | GEO_LEGAL | NONFIN_RISK | SHORT | ESG)(fetch_filing_text)
mcp.tool(tags=NONFIN_RISK | SHORT)(fetch_insider_trading_filings)
mcp.tool(tags=NONFIN_RISK)(search_regulatory_actions)

# =============================================================================
# NEWS TOOLS — multiple agents
# =============================================================================

mcp.tool(tags=SECTOR | GEO_LEGAL | MACRO | NONFIN_RISK | ESG | ALT_DATA)(fetch_news)
mcp.tool(tags=ALT_DATA | PORTFOLIO)(fetch_news_sentiment_score)
mcp.tool(tags=GEO_LEGAL | MACRO)(fetch_geopolitical_news)
mcp.tool(tags=ESG)(fetch_esg_controversy_news)
mcp.tool(tags=NONFIN_RISK)(fetch_regulatory_news)

# =============================================================================
# ALTERNATIVE DATA TOOLS — Alt Data Analyst primary
# =============================================================================

mcp.tool(tags=ALT_DATA | GROWTH)(fetch_google_trends)
mcp.tool(tags=ALT_DATA)(fetch_patent_filing_trend)
mcp.tool(tags=ALT_DATA | GROWTH)(calculate_earnings_surprise_history)
mcp.tool(tags=ALT_DATA | GROWTH)(fetch_job_postings_trend)
mcp.tool(tags=ALT_DATA)(fetch_social_sentiment)
mcp.tool(tags=ALT_DATA)(fetch_web_traffic_trend)
