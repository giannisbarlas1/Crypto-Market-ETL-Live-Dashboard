# src/transform.py
def clean_data(df):
    """
    Καθαρίζει και μετατρέπει τύπους.
    """
    df = df.copy()
    df["price"] = df["price"].astype(float).round(2)
    df["market_cap"] = df["market_cap"].astype(float).round(2)
    df["volume_24h"] = df["volume_24h"].astype(float).round(2)
    df["change_24h"] = df["change_24h"].astype(float).round(2)
    return df
