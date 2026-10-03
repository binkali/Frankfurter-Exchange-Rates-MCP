# MCP-Server – Frankfurter Exchange Rates

An [MCP](https://modelcontextprotocol.io) server that wraps the free [Frankfurter API](https://frankfurter.dev) and exposes current exchange rates as tools for LLM clients like Claude Desktop.

The server fetches the latest rates published by the European Central Bank, parses the response and returns only the currencies you ask for. No API key required.

## Features

-  Current exchange rates for any supported base currency (default: `EUR`)
-  Filter the response down to specific quote currencies
-  Input validation (unknown currencies, base used as quote)
-  No API key, no account – Frankfurter is free and open

## Tools

### `get_parsed_rates`

Returns the current exchange rates for a base currency.

| Parameter | Type        | Default | Description                                                  |
|-----------|-------------|---------|--------------------------------------------------------------|
| `quotes`  | `list[str]` | `None`  | Quote currencies to return. If omitted, all rates are returned. |
| `base`    | `str`       | `"EUR"` | Base currency for the lookup.                                |

**Example call**

```json
{ "quotes": ["USD", "GBP", "CHF"], "base": "EUR" }
```

**Example response**

```json
{
  "base": "EUR",
  "date": "2026-10-02",
  "rates": {
    "USD": 1.1225,
    "GBP": 0.85033,
    "CHF": 0.9279
  }
}
```

**Errors** are returned as `{"error": "..."}`, e.g. when the API is unreachable, a currency code is unknown, or the base currency is also listed as a quote.

## Installation

Requires Python 3.10+.

```bash
git clone https://github.com/fr3d0m/MCP-Server.git
cd MCP-Server

python -m venv .venv
source .venv/bin/activate

pip install fastmcp python-dotenv requests
```

## Usage

### Run locally

```bash
python mcp_server.py
```

To inspect and test the tools in the browser, use the MCP Inspector:

```bash
mcp dev mcp_server.py
```

### Connect to Claude Desktop

Add the server to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "exchange-rates": {
      "command": "/absolute/path/to/MCP-Server/.venv/bin/python",
      "args": ["/absolute/path/to/MCP-Server/server.py"]
    }
  }
}
```

Restart Claude Desktop afterwards. You can then ask things like:

> *"What's the current EUR to USD rate?"*
> *"Show me the exchange rates for GBP, JPY and CHF with USD as base."*

## Project structure

```
MCP-Server/
├── api.py        # HTTP calls to the Frankfurter API
├── server.py     # MCP server and tool definitions
└── README.md
```

## Notes

- Rates come from the **European Central Bank** and are updated once per working day (around 16:00 CET). Weekends and holidays return the last published rates.
- I used UV as the project interpreter but because the majority of people just uses python or python3 i wrote the instructions all with the python command
- Expect updates soon

## Credits

Exchange rate data provided by [Frankfurter](https://frankfurter.dev), based on reference rates from the European Central Bank.
