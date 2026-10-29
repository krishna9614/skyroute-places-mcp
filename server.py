"""SkyRoute Places MCP server.

Phase 1 placeholder server that exposes a single mock ``search_places`` tool
over streamable HTTP. Real places APIs are intentionally out of scope.
"""

import logging
import os
from typing import Any

from dotenv import load_dotenv
from mcp.server.mcpserver import MCPServer

load_dotenv()

logger = logging.getLogger("skyroute.places_mcp")

HOST = os.getenv("MCP_HOST", "127.0.0.1")
PORT = int(os.getenv("MCP_PORT", "8002"))

mcp_server = MCPServer(
    name="skyroute-places-mcp",
    description="Mock places tools for the SkyRoute travel assistant.",
)


@mcp_server.tool(
    name="search_places",
    description="Search for notable places and attractions in a given city.",
)
def search_places(city: str) -> dict[str, Any]:
    """Return a fixed mock list of places for ``city``."""
    logger.info("tool call: name=search_places args=%s", {"city": city})
    try:
        result = {
            "city": city,
            "places": [
                {
                    "name": f"{city} Old Town",
                    "category": "sightseeing",
                    "rating": 4.7,
                },
                {
                    "name": f"{city} Central Museum",
                    "category": "museum",
                    "rating": 4.5,
                },
                {
                    "name": f"{city} Riverside Park",
                    "category": "park",
                    "rating": 4.6,
                },
            ],
            "source": "mock",
        }
        logger.info("tool result: name=search_places result=%s", result)
        return result
    except Exception as exc:
        logger.exception("tool error: name=search_places error=%s", exc)
        raise


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    logger.info(
        "starting skyroute-places-mcp on http://%s:%s/mcp (transport=streamable-http)",
        HOST,
        PORT,
    )
    mcp_server.run(
        transport="streamable-http",
        host=HOST,
        port=PORT,
    )


if __name__ == "__main__":
    main()
