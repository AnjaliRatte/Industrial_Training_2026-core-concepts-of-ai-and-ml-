# https://api.shopstyle.com/api/v2/products?pid=Uid5396-41944086-79&fts=WHITE%20color%20%20Blouse&offset=0&limit=10
#
#
# Append the image URL to the list of lists of all products
# Small
# XLarge
# Medium
# Large

import requests

response = requests.get("https://api.shopstyle.com/api/v2/products?pid=Uid5396-41944086-79&fts=WHITE%20color%20%20Blouse&offset=0&limit=10")
data = response.json()

print(data)

result = []

for product in data["products"]:
    sizes = product.get("image", {}).get("sizes", {})

    row = [
        sizes.get("Small", {}).get("url"),
        sizes.get("Medium", {}).get("url"),
        sizes.get("Large", {}).get("url"),
        sizes.get("XLarge", {}).get("url")
    ]

    result.append(row)

print(result)