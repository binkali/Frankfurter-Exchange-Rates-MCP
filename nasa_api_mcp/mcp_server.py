import json
from fastmcp import FastMCP
from first_wrapper import search_nasa_images, get_nasa_apod

mcp = FastMCP("NASA API Wrapper")

@mcp.tool("get_apod_data", description="Fetch NASA's Astronomy Picture of the Day (APOD) data for a given date.")
def get_apod_data(date: str = None):
    result = get_nasa_apod(date)
    if result:
        return json.dumps(result, indent=4)
    else:
        return {"error": "Failed to fetch APOD data."}

@mcp.tool("search_images_data", description="Search NASA's image library for images matching a query.")
def search_images_data(q: str):
    result = search_nasa_images(q)
    if result:
        return json.dumps(result, indent=4)
    else:
        return {"error": "Failed to fetch image data."}


def main():
    mcp.run()

if __name__ == "__main__":
    mcp.run()