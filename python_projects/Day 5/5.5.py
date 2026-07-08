# 12. Question:
# Write a script that retrieves all country data and calculates the percentage of the world's land area occupied by each country.
# Percentage Formula:
# Country Area Percentage = (Country Area / Total World Area) × 100
# Task: Display the Top 5 Countries by land area percentage in a formatted table.

import requests

response = requests.get(
    "https://api.restcountries.com/countries/v5?limit=100&pretty=1",
    headers = {
        "Authorization" : "Bearer rc_live_ead02b60371441b9888fbb28757ed6c2"
    }
)

data = response.json()

import requests

response = requests.get(
    "https://api.restcountries.com/countries/v5?limit=100&pretty=1",
    headers={
        "Authorization": "Bearer rc_live_ead02b60371441b9888fbb28757ed6c2"
    }
)

data = response.json()

countries = data["data"]["objects"]

# Calculate total world area
total_area = 0

for info in countries:
    area = info.get("area", {}).get("kilometers", 0)
    total_area += area


# Calculate area percentage for each country
result = []

for info in countries:
    name = info["names"]["common"]
    area = info.get("area", {}).get("kilometers", 0)

    if area != 0:
        percentage = (area / total_area) * 100
        result.append([name, percentage])


# Sort countries by area percentage (descending)
result.sort(key=lambda x: x[1], reverse=True)


# Display top 5 countries
print(f"{'Country':30} {'Area Percentage':>15}")
print("-" * 50)

for country in result[:5]:
    print(f"{country[0]:30} {country[1]:>12.2f}%")