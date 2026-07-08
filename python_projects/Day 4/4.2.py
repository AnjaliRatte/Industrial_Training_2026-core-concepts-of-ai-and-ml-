# 6. Question:
# Fetch the list of all countries and extract details about their official languages.
# Create a dictionary where:
#
# Key = Language Name
# Value = List of Countries where the language is spoken
#
# Task: Print the dictionary.

import requests


response = requests.get(
    "https://api.restcountries.com/countries/v5?limit=100&pretty=1",
    headers = {
        "Authorization" : "Bearer rc_live_ead02b60371441b9888fbb28757ed6c2"
    }
)

data = response.json()

print(data)

languages = []
for info in data["data"]["objects"]:
    for i in info["languages"] :
        languages.append(i["name"])


print(languages)
cd = {}
for lan in languages :
    c = []
    for info in data["data"]["objects"]:
        lang = info["languages"]
        for i in range(len(lang)):
            if lan == info["languages"][i]["name"]:
                c.append(info["names"]["common"])
    cd[lan]=c

print(cd)

