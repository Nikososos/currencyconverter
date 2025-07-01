import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("api_key")

# print("API KEY: " , api_key)

if api_key is None:
    raise ValueError("API key niet gevonden? Gaat dit wel goed?")

def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    # print("Status code:", response.status_code)  
    # try:
    #     data = response.json()
    #     print("Full API response:\n", data)       
    # except ValueError:
    #     print(" Response is not valid JSON.")
    #     return None

    if response.status_code == 200 and data.get("result") == "success":
        rate = data["conversion_rates"].get(target_currency.upper())
        if rate:
            return rate
        else:
            raise ValueError(f"Currency '{target_currency}' niet gevonden in de exchange.")
    else:
        print("Er is een ander probleem met je programma, check je api response met de uitgecommende code bovenin")

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

base_currency = input("Van welke valuta wil je omrekenen? (bijv. EUR): ").strip().upper()
target = input("Naar welke valuta wil je omrekenen? (bijv. USD): ").strip().upper()
amount = float(input(f"Voer het bedrag in {base_currency} in: ").strip())
exchange_rate = get_exchange_rate(base_currency, target)
converted = convert_currency(amount, exchange_rate)

print(f"{amount} {base_currency} = {converted:.2f} {target} (Wisselkoers: 1 {base_currency} = {exchange_rate} {target})")

