# https://dummyjson.com/carts
#
# get
# cartId
# products in each cart id
# total quality
# total price value of cart

import requests

response = requests.get("https://dummyjson.com/carts")
data = response.json()

result = []
for item in data["carts"] :
    total_quantity = 0
    total_cost = 0
    prod_ids = []

    for products in item["products"] :
        prod_ids.append(products["id"])
        total_cost = total_cost + products["discountedTotal"]
        total_quantity = total_quantity + products["quantity"]


    row = [
        item["id"],
        prod_ids,
        total_quantity,
        total_cost
    ]


    result.append(row)

print(result)



