# skyroute-places-mcp

Places MCP server for the SkyRoute travel assistant. Phase 1: a single
placeholder `search_places(city)` tool returning a fixed mock response — no
external APIs or databases.

## Requirements

- Python 3.10+

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # adjust MCP_HOST / MCP_PORT if needed
```

## Run

```bash
python server.py
```

The server listens on `http://127.0.0.1:8002/mcp` (streamable HTTP) by default.

## Tools

| Tool            | Input         | Output                                    |
| --------------- | ------------- | ----------------------------------------- |
| `search_places` | `city` (str)  | Mock list of places/attractions in `city` |

## Logging

Each tool invocation logs the tool name, input arguments, and the returned
result (or error) at `INFO` level to stdout.
