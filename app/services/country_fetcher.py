import requests

REST_COUNTRY_URL = "https://restcountries.com/v2/all?fields=name,capital,region,population,flag,currencies"

def fetch_countries():
    """
    Fetch list of countries from REST Countries API
    Returns simplified list of dicts or None if API fails
    """
    try:
        response = requests.get(REST_COUNTRY_URL, timeout=10)

        # If API fails, return None so refresh stops
        if response.status_code != 200:
            return None

        data = response.json()

        countries = []
        for c in data:
            countries.append({
                "name": c["name"],
                "capital": c.get("capital"),
                "region": c.get("region"),
                "population": c.get("population"),
                "flag_url": c.get("flag"),
                "currency_code": c["currencies"][0]["code"] if c.get("currencies") else None,
            })

        return countries

    except Exception:
        return None
