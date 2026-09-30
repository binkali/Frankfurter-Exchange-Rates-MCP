import os
from dotenv import load_dotenv
import requests
from typing import Optional, Dict

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY") or "DEMO_KEY"

def make_api_req(url: str, params: dict, timeout: int=10) -> Optional[Dict]:
    """Return a JSON object, or ``None`` when the request or response is invalid."""
    try:
        response = requests.get(url, params=params, timeout=timeout)
    except requests.exceptions.Timeout as error:
        print("Request timed out: ", error)
    except requests.exceptions.ConnectionError as error:
        print("Connection failed: ", error)
    except requests.exceptions.HTTPError as error:
        print("HTTP error: ", error)
    except requests.exceptions.JSONDecodeError as error:
        print("Invalid JSON response: ", error)
    except requests.exceptions.RequestException as error:
        print("Request failed: ", error)
    except (TypeError, ValueError) as error:
        print("Invalid request or response: ", error)
    return None

def get_nasa_apod(api_key=NASA_API_KEY, date: Optional[str] = None):
    """Fetch NASA's Astronomy Picture of the Day, optionally for a date."""
    base_url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": api_key
    }
    if date:
        params["date"] = date

    return make_api_req(base_url, params, timeout=10)

def search_nasa_images(query: str,
                       size: int = 3) -> Optional[Dict]:
    """Search NASA's image library for up to ``size`` images matching query."""
    base_url = "https://images-api.nasa.gov/search"

    params = {
        "q": query,
        "mediatype": "image", 
        "page": 1,
        "page_size": size
    }

    return make_api_req(base_url, params, timeout=15)
### API's
#GET https://science.nasa.gov/wp-json/wp/v2/apod-basic
#GET https://images-api.nasa.gov






































