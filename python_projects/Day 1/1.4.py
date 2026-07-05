# http://makeup-api.herokuapp.com/api/v1/products.json
#
# create a list of lists
# id,brand , name, product_colors colour_name1 ,  product_colors colour_name2, product_colors colour_name3 ----- upto 5


import requests

response = requests.get("http://makeup-api.herokuapp.com/api/v1/products.json")
data = response.json()
# print(data)
# data = list(data.values())

result = []

for item in data:
    prod_colors = []
    for color in item["product_colors"] :
        prod_colors.append(color["colour_name"])

    row = [
        item["id"],
        item["brand"],
        item["name"],
        [i for i in prod_colors[:5]]
    ]

    result.append(row)

print(result)