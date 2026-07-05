# Below is an API that provides details about different Pokémon.
#
# Extract the name and URL of each Pokémon.
# Retrieve the URL for each Pokémon and download its image if its weight is less than 80 kg.
# The image can be found in the "sprites" section under the key "front_default".
#
# https://pokeapi.co/api/v2/pokemon?limit=1000&offset=0

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1000&offset=0")
data = response.json()
print("pokemons with weight less than 80 kg are : ")
for item in data["results"]:
    url = item["url"]
    name = item["name"]
    dino_info = requests.get(url)
    dino_data = dino_info.json()
    # print(dino_data["weight"])
    if dino_data["weight"] < 80 :
        print(name,url)
        img = requests.get(dino_data["sprites"]["front_default"])
        fn = name + ".png"
        with open(fn,"wb") as f :
            f.write(img.content)
            f.close()






