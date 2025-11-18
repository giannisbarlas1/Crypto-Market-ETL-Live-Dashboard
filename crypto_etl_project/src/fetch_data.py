# src/fetch_data.py
import requests
import pandas as pd

def fetch_market_data(coins):
    """
    Φέρνει δεδομένα αγοράς για τα νομίσματα.
    Επιστρέφει pandas DataFrame.
    """
    API_URL = "https://min-api.cryptocompare.com/data/pricemultifull"
    params = {"fsyms": ",".join(coins), "tsyms": "USD"}

    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    data = response.json()

    rows = []
    for coin, info in data.get("RAW", {}).items():
        usd_data = info.get("USD", {})
        rows.append({
            "coin": coin,
            "price": usd_data.get("PRICE"),
            "market_cap": usd_data.get("MKTCAP"),
            "volume_24h": usd_data.get("VOLUME24HOUR"),
            "change_24h": usd_data.get("CHANGE24HOUR")
        })

    df = pd.DataFrame(rows)
    return df
