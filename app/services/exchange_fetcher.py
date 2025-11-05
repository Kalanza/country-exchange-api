import requests
from app.config import settings

EXCHANGE_URL = f"https://open.er-api.com/v6/latest/{settings.BASE_CURRENCY}"

def fetch_exchange_rates():
    """
    Fetch exchange rates for base currency (e.g., USD)
    Returns dict of rates or None if API fails
    """
    try:
        response = requests.get(EXCHANGE_URL, timeout=10)

        if response.status_code != 200:
            return None

        data = response.json()
        return data.get("rates", {})

    except Exception:
        return None
