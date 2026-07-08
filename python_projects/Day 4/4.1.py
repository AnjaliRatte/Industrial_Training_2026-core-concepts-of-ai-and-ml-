# API Endpoint
# https://api.restcountries.com/countries/v5?limit=250&pretty=1
#
# const data = await response.json();
# Note: Replace YOUR_API_TOKEN with the API token provided by your instructor.

# Assignment 3: Complex Data Extraction
# 5. Question:
# Write a script that retrieves data from the API and finds the country with the highest Population Density.
# Population Density = Population ÷ Area
# Task: Display the country name and its population density.

import requests

response = requests.get(
    "https://api.restcountries.com/countries/v5?limit=100&pretty=1",
    headers = {
        "Authorization" : "Bearer rc_live_ead02b60371441b9888fbb28757ed6c2"
    }
)

data = response.json()

# c_d = {}
max_density = 0
name = ""
for info in data["data"]["objects"]:
    popu = info.get("population")
    area = info.get("area").get("kilometers")
    density = popu/area
    if density > max_density:
        max_density = density
        name = info.get("names", {}).get("common", "N/A")
print(name,max_density)
