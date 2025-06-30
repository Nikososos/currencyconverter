import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("api_key")

url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR"
params ={"appid": api_key}

print("API KEY: " , api_key)

if api_key is None:
    raise ValueError("API key niet gevonden? Gaat dit wel goed?")

def get_eur_to_usd_rate():
    response = requests.get(url)
    data = response.json()
    # print("Status code:", response.status_code)  
    # try:
    #     data = response.json()
    #     print("Full API response:\n", data)       
    # except ValueError:
    #     print(" Response is not valid JSON.")
    #     return None

    if response.status_code == 200 and "conversion_rates" in data:
        if "USD" in data["conversion_rates"]:
            return data["conversion_rates"]["USD"]
        else:
            print(" USD rate not found in conversion_rates.")
    else:
        print(" Unexpected API response format or error.")
    return None

def convert_eur_to_usd(amount, exchange_rate):
    return amount * exchange_rate

eur_amount = float(input("Voer het bedrag in EUR in: ").strip())
exchange_rate = get_eur_to_usd_rate()
usd_amount = convert_eur_to_usd(eur_amount, exchange_rate)

print(f"{eur_amount} EUR is gelijk aan {usd_amount:.2f} USD (Wisselkoers: 1 EUR = {exchange_rate} USD)")

