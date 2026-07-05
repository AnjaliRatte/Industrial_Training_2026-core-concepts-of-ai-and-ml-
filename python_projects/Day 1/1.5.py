import requests

response = requests.get("http://makeup-api.herokuapp.com/api/v1/products.json")
data = response.json()
#print(data)

result = []
for item in data :
    row = [
        item["id"],
        item["brand"],
        item["name"]
    ]

    colors = item.get("product_colors", [])

    for color in colors[:5] :
        row.append(color.get("colour_name"))

    while(len(row)<8):
        row.append("none")

    result.append(row)

print(result)


