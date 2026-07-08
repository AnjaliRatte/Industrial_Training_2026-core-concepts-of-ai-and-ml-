# 8. Question:
# Write a script that fetches currency information for all countries and groups countries according to the currency they use.
# Task: Display the currency name along with the corresponding countries.

import requests

response = requests.get(
    "https://api.restcountries.com/countries/v5?limit=100&pretty=1",
    headers = {
        "Authorization" : "Bearer rc_live_ead02b60371441b9888fbb28757ed6c2"
    }
)

data = response.json()

def get_currency(info,c):
    cr = info["currencies"]
    # print(cr)
    for i in cr :
        # print(i["name"])
        if i["name"] == c :
            return True
        else :
            return False
        # for j in i :
        #     if j["name"] == c :
        #         return True
        #     else :
        #         return False


# print(data)
currency = []

for info in data["data"]["objects"]:
    cr = info["currencies"]
    if cr not in currency:
        currency.append(cr)
# print(currency)

c_names = []
for i in currency :
    for j in i :
        if j["name"] not in c_names:
            c_names.append(j["name"])
# print(c_names)
# print(len(c_names))

result = []
for c in c_names:
    row = []
    countries = []
    row.append(c)
    for info in data["data"]["objects"]:

        if get_currency(info, c) :
            countries.append(info["names"]["common"])
            # print(info["names"]["common"])

    row.append(countries)
    result.append(row)
print(result)

