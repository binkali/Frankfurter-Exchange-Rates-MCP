import json
from fastmcp import FastMCP
from api.frankfurter_api import get_current_rates

mcp = FastMCP("Best Server Ever")

all_quotes = [
    "AUD", "BRL", "CAD", "CHF", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD",
    "HUF", "IDR", "ILS", "INR", "ISK", "JPY", "KRW", "MXN", "MYR", "NOK",
    "NZD", "PHP", "PLN", "RON", "SEK", "SGD", "THB", "TRY", "USD", "ZAR",
    "EUR"
]
filtered_results = []

@mcp.tool()
def get_parsed_rates(quotes: list = None, base: str = 'EUR'):
    """Return the current exchange rates for a base currency.

    Args:
        quotes: Optional list of quote currencies to inspect. If omitted, the full
            API response for the selected base currency is returned.
            Following quotes are possible:
                "AUD", "BRL", "CAD", "CHF", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD",
                "HUF", "IDR", "ILS", "INR", "ISK", "JPY", "KRW", "MXN", "MYR", "NOK",
                "NZD", "PHP", "PLN", "RON", "SEK", "SGD", "THB", "TRY", "USD", "ZAR",
                "EUR"
        base: Base currency code used for the exchange-rate lookup. Defaults to "EUR".

    Returns:
        A JSON string containing the current exchange rates for the given base
        currency, or None if a filtered quote list is requested.
    """
    json_response = json.dumps(get_current_rates(base))
    loaded_json = json.loads(json_response)
    if not quotes:
        response = get_current_rates(base)
        return response
    else:
        if base in quotes:
            #print("Dont you dare use the base as a quote! It's too much work for me.(The default base is EUR)")
            filtered_results.append(base + ": 1")
            quotes.remove(base)
            return None
        quotes =  quotes.upper()
        for i in range(len(quotes)):
            quote = quotes[i]
            result = f"{quote}: {loaded_json["rates"][quote]}"
            filtered_results.append(result)
        return filtered_results
    


if __name__ == "__main__":
    mcp.run()