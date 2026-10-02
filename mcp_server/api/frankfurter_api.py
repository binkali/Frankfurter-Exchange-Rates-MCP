import os
import requests
from dotenv import load_dotenv
from typing import Optional, Dict

load_dotenv()

FRANKFURTER_API_KEY = os.getenv("FRANKFURTER_API_KEY")


def make_api_call(url: str, params: dict, timeout: int = 10) -> Optional[Dict]:
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error when calling API: {e}")
        return None


def get_current_rates(base: str = "EUR") -> Optional[Dict]:
    url = "https://api.frankfurter.dev/v1/latest"
    params = {
        "base": base,
    }
    return make_api_call(url, params)


if __name__ == "__main__":
    rates = get_current_rates()
    print(rates)