# Assignment 6: Data Aggregation
# 11. Question:
# Create a program that groups countries by their Subregion (for example: Southern Asia, Northern Europe, Western Africa).
# For each subregion, calculate the average population of all countries belonging to that subregion.
# Task: Print the subregion along with its average population.

import requests

response = requests.get(
    "https://api.restcountries.com/countries/v5?limit=100&pretty=1",
    headers = {
        "Authorization" : "Bearer rc_live_ead02b60371441b9888fbb28757ed6c2"
    }
)

data = response.json()

def sub(s,info):
    region = info["subregion"]
    if s == region :
        return True
    else :
        return False

# print(data)
sub_regions = []
for info in data["data"]["objects"]:
    sr = info["subregion"]
    if sr not in sub_regions:
        sub_regions.append(sr)
# print(sub_regions)

sr_countries = []
for s in sub_regions:
    row = []
    row.append(s)
    countries = []
    for info in data["data"]["objects"]:
        if sub(s,info) :
            countries.append(info["names"]["common"])

    row.append(countries)
    sr_countries.append(row)
# print(sr_countries)

result = []
for dt in sr_countries :
    row = []
    row.append(dt[0])
    sum = 0
    n = len(dt[1])
    for i in dt[1]:
        for info in data["data"]["objects"]:
            name = info["names"]["common"]
            if name == i :
                sum+= info["population"]
    avg = sum/n
    row.append(avg)
    result.append(row)
print(result)





