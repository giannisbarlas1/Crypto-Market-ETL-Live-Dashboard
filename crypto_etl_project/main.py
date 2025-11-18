from src.fetch_data import fetch_market_data
from src.transform import clean_data
from src.analysis import kpis
from src.visualization import plot_prices
from src.visualization import real_time_plot
from src.visualization import live_plot
def main():
    COINS = ["BTC", "ETH", "SOL"]

    # 1️⃣ Fetch
    df = fetch_market_data(COINS)

    # 2️⃣ Transform
    df = clean_data(df)
    print("\nΔεδομένα Κρυπτονομισμάτων:\n", df)

    # 3️⃣ KPIs
    summary = kpis(df)
    print("\nKPIs:\n", summary)

    # 4️⃣ Στατικό plot
    plot_prices(df)

    # 5️⃣ Live plot (μπλοκάρει μέχρι να το κλείσεις)
    live_plot(COINS, interval=5)

if __name__ == "__main__":
    main()
