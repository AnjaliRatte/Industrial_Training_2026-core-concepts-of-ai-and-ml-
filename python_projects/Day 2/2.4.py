# Download all images whose width is less than 400 and save them in a folder named "small images"
#
# https://api.imgflip.com/get_memes

import requests
import os

folder = "small images"
os.makedirs(folder, exist_ok=True)

response = requests.get("https://api.imgflip.com/get_memes")

data = response.json()

for info in data["data"]["memes"]:
    if info["width"] < 400 :
        img = info["url"]
        r = requests.get(img)
        fn = info["id"] + ".jpg"
        file_path = os.path.join(folder,fn)
        with open(file_path,"wb") as f :
            f.write(r.content)
            f.close()
