import json
from fastmcp import FastMCP
from mcp_server.frankfurter_api.py import get_current_rates

mcp = FastMCP("Best Server Ever")

all_rates = [
    "AUD", "BRL", "CAD", "CHF", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD",
    "HUF", "IDR", "ILS", "INR", "ISK", "JPY", "KRW", "MXN", "MYR", "NOK",
    "NZD", "PHP", "PLN", "RON", "SEK", "SGD", "THB", "TRY", "USD", "ZAR",
]

@mcp.tool()
def get_parsed_rates(quotes: list = None, base: str = 'EUR', rates: list = all_rates):
    #"""If you want to filter by quotes: seperate each quote with a comma. E.g. you want to filter by AUD and CAD than quotes would be 'aud,cad'"""
    json_response = get_current_rates(base)
    loaded_json = json.loads(json_response)
    if not quotes:
        


if __name__ == "__main__":
    mcp.run()