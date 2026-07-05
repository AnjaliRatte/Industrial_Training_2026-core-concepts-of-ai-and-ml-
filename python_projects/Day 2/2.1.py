# https://open.er-api.com/v6/latest/USD
#
#
# Display:
#
# Base Currency
# Selected Currency
# Exchange Rate
# Last Updated Time
# API Status
#
#
# Example
# Input
# Target Currency : INR
#
# Output
# Base Currency : USD
#
# Target Currency : INR
#
# Exchange Rate : 94.65

import requests

response = requests.get("https://open.er-api.com/v6/latest/USD")
data = response.json()

target_currency = input("Enter Target currency : ")

base_currency = data["base_code"]

exchange_rate = data["rates"][target_currency]
print("Base Currency : ", base_currency)
print("Target Currency : ", target_currency)
print("Exchange Rate : ",exchange_rate )



