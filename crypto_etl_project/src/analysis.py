# src/analysis.py
def kpis(df):
    """
    Υπολογίζει βασικά KPIs.
    """
    summary = {
        "avg_price": df["price"].mean(),
        "max_price": df["price"].max(),
        "min_price": df["price"].min(),
        "total_market_cap": df["market_cap"].sum()
    }
    return summary
