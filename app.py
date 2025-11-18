# app.py
import streamlit as st
import pandas as pd
from src.fetch_data import fetch_market_data
from src.transform import clean_data
from src.analysis import kpis
import time

# Ρυθμίσεις
COINS = ["BTC", "ETH", "SOL"]
DEFAULT_INTERVAL = 5  # δευτερόλεπτα

# Τίτλος
st.set_page_config(page_title="Crypto Market Dashboard", layout="wide")
st.title("💰 Crypto Market Dashboard")
st.markdown("Live tracking των τιμών BTC, ETH, SOL με KPIs και visualization.")

# Sidebar
st.sidebar.header("Ρυθμίσεις")
interval = st.sidebar.slider("Ανανέωση (δευτ.)", min_value=1, max_value=60, value=DEFAULT_INTERVAL)

# Placeholder για live updates
live_area = st.empty()

try:
    while True:
        # 1️⃣ Fetch & clean
        df = clean_data(fetch_market_data(COINS))

        # 2️⃣ KPIs
        summary = kpis(df)

        # Αν summary είναι dict, μετατρέπουμε σε DataFrame για .style
        if isinstance(summary, dict):
            summary = pd.DataFrame(summary, index=[0])

        # 3️⃣ Ενημέρωση dashboard
        with live_area.container():
            # Τιμές
            st.subheader("📊 Τιμές Κρυπτονομισμάτων")
            st.dataframe(df.style.format({"price": "{:,.2f}",
                                          "market_cap": "{:,.0f}",
                                          "volume_24h": "{:,.0f}",
                                          "change_24h": "{:+,.2f}"}))

            # KPIs
            st.subheader("📈 KPIs")
            st.dataframe(summary.style.format("{:,.2f}"))

            # Bar Chart
            st.subheader("💹 Live Τιμές")
            chart_data = df.set_index("coin")["price"]
            st.bar_chart(chart_data)

        time.sleep(interval)

except KeyboardInterrupt:
    st.warning("Το live dashboard τερματίστηκε.")
