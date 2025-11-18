import matplotlib.pyplot as plt
from src.fetch_data import fetch_market_data
from src.transform import clean_data
import time

COINS = ["BTC", "ETH", "SOL"]

plt.ion()  # ενεργοποίηση interactive mode
fig, ax = plt.subplots(figsize=(8,5))

try:
    while True:
        # 1️⃣ Φέρνουμε νέα δεδομένα
        df = clean_data(fetch_market_data(COINS))

        # 2️⃣ Καθαρίζουμε το axes
        ax.clear()

        # 3️⃣ Χρωματισμός μπάρων
        colors = ["green" if x >= 0 else "red" for x in df["change_24h"]]

        # 4️⃣ Δημιουργία νέων bars
        ax.bar(df["coin"], df["price"], color=colors)

        # 5️⃣ Labels και τίτλος
        ax.set_ylabel("Τιμή (USD)")
        ax.set_title("Live Τιμές BTC, ETH, SOL (Ανανέωση κάθε 5 δευτ.)")

        # 6️⃣ Εμφάνιση τιμών πάνω στις μπάρες
        for i, price in enumerate(df["price"]):
            ax.text(i, price + max(df["price"])*0.01, f"{price:.2f}", ha='center')

        # 7️⃣ Παύση για ανανέωση
        plt.pause(5)

except KeyboardInterrupt:
    print("Live plot τερματίστηκε από τον χρήστη.")
    plt.ioff()
    plt.show()
