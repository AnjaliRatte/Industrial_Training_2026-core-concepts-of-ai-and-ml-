# Assignment 5: Custom Data Manipulation
# 9. Question:
# Fetch data for all countries and calculate the total population of all island nations (countries having no land borders).
# Task: Print the total population of island nations.

import requests

response = requests.get(
    "https://api.restcountries.com/countries/v5?limit=100&pretty=1",
    headers = {
        "Authorization" : "Bearer rc_live_ead02b60371441b9888fbb28757ed6c2"
    }
)

data = response.json()

# print(data)

total_population = 0

for info in data["data"]["objects"]:
    border = info["borders"]
    if len(border) == 0 :
        pop = info["population"]
        total_population+=pop
print(total_population)