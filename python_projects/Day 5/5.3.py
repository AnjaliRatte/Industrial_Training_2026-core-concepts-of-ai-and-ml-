# 10. Question:
# Write a script that finds the countries with the longest and shortest names (based on character count).
# Task: Display the country names along with the number of characters.

import requests

response = requests.get(
    "https://api.restcountries.com/countries/v5?limit=100&pretty=1",
    headers = {
        "Authorization" : "Bearer rc_live_ead02b60371441b9888fbb28757ed6c2"
    }
)

data = response.json()

first_name = data["data"]["objects"][0]["names"]["common"]

max_c = ""
max_count = 0
min_c = first_name
min_count = 0

for info in data["data"]["objects"]:
    name = info["names"]["common"]
    l = len(name)
    if l > len(max_c):
        max_c = name
        max_count = l
    if l < len(min_c) :
        min_c = name
        min_count = l
print("country with longest name is : ( " , max_c , " , ", max_count, " )")
print("country with shortest name is : ( " , min_c , " , ", min_count, " )")
