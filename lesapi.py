import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("api_key")

url = (f"https://v6.exchangerate-api.com/{api_key}/latest/EUR")
params ={"appid": api_key}

def get_eur_to_usd_rate(api_key):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "USD" in data["conversion_rates"]:
            return data["conversion_rates"]["USD"]
        else:
            print("Fout: USD wisselkoers niet gevonden.")
        return None
def convert_eur_to_usd(amount, exchange_rate):
    return amount * exchange_rate

eur_amount = float(input("Voer het bedrag in EUR in: ").strip())
exchange_rate = get_eur_to_usd_rate(api_key)
usd_amount = convert_eur_to_usd(eur_amount, exchange_rate)

print(f"{eur_amount} EUR is gelijk aan {usd_amount:.2f} USD (Wisselkoers: 1 EUR = {exchange_rate} USD)")

