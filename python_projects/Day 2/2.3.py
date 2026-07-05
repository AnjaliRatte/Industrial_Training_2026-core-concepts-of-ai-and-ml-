# https://dummyjson.com/products
#
# Download thumbnail images "thumbnail" for all products in the products folder.
# Task Description:
#
# Fetch product data from the API https://dummyjson.com/products and extract the thumbnail image URL and product title for each product.
# Download each thumbnail image and save it locally using the product title as the image filename


import requests

response = requests.get("https://dummyjson.com/products")

data = response.json()

for item in data["products"] :
    thumbnail = item["thumbnail"]
    url = requests.get(thumbnail)
    fn = item["title"] + ".webp"
    # print(fn," , ",thumbnail)
    with open(fn,"wb") as f:
        f.write(url.content)
        f.close()



