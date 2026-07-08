# 7. Question:
# Create a program that takes a list of country names as input and returns the details (Name, Capital, Population and Area)
# of all neighboring countries sharing borders with the given countries.
# Task: Test the program using the countries Germany and France.
import requests

response = requests.get(
    "https://api.restcountries.com/countries/v5?limit=100&pretty=1",
    headers = {
        "Authorization" : "Bearer rc_live_ead02b60371441b9888fbb28757ed6c2"
    }
)

data = response.json()
print(data)

# c_list = [input("Enter list of countries")]
# print(c_list)
c_list = ["Germany", "France"]
border_c = []
for country in c_list :
    for info in data["data"]["objects"]:
        name = info["names"]["common"]

        # print(info["borders"])
        if country == name :
            border_c.append(info["borders"])
# print(border_c)

ls = []
for i in range(len(border_c)):
    for j in range(len(border_c[i])):
        if border_c[i][j] not in ls :
            ls.append(border_c[i][j])
print(ls)

result = []

for cod in ls :
    for info in data["data"]["objects"]:
        code = info["codes"]["alpha_3"]
        if cod == code :
            row = []
            row.append(info.get("names").get("common"))
            row.append(info.get("population"))
            row.append(info.get("area").get("kilometers"))
            result.append(row)
print(result)

# for info in data["data"]["objects"]:
#     print(info.get("parent").get("alpha_3"))
# AUT', 'CZE', 'DNK', 'FRA', 'NLD', 'POL', 'AND', 'BEL', 'DEU', 'ITA', 'LUX', 'MCO', 'ESP', 'CHE'
