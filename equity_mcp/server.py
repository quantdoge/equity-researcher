"""
Equity Research MCP Server.

Six tools, tagged by agent role. Data access is uniform — every agent discovers
and queries Financial Modeling Prep through the same two tools — so tags now gate
only one thing that genuinely differs by role: who is allowed to execute code.

Run standalone:
    fastmcp run equity_mcp/server.py

Inspect all tools and their tags:
    fastmcp inspect equity_mcp/server.py
"""

from __future__ import annotations

from dotenv import load_dotenv

# Before the tool imports: fmp.py reads FMP_API_KEY at call time, but loading
# early keeps a bare `fastmcp run` behaving the same as the orchestrator.
load_dotenv()

from fastmcp import FastMCP

from equity_mcp.roles import QUANT_ENGINEER, SHARED
from equity_mcp.tools.code_exec import list_workspace, run_python
from equity_mcp.tools.fmp import fmp_call, fmp_catalog
from equity_mcp.tools.web import fetch_page, web_search

mcp = FastMCP(
    name="equity-research-mcp",
    instructions=(
        "Equity Research MCP server. Financial data comes from Financial "
        "Modeling Prep: call fmp_catalog to discover the available tools and "
        "endpoints, then fmp_call to fetch. Large payloads are saved to the run "
        "workspace and computed over with run_python."
    ),
)

# ── Data and web — every agent ────────────────────────────────────────────────

mcp.tool(tags=SHARED)(fmp_catalog)
mcp.tool(tags=SHARED)(fmp_call)
mcp.tool(tags=SHARED)(web_search)
mcp.tool(tags=SHARED)(fetch_page)

# ── Computation — the quant engineer only ─────────────────────────────────────
# Widening these to SHARED would give every specialist its own execution loop;
# keeping them here means code runs in exactly one place per run.

mcp.tool(tags=QUANT_ENGINEER)(run_python)
mcp.tool(tags=QUANT_ENGINEER)(list_workspace)
