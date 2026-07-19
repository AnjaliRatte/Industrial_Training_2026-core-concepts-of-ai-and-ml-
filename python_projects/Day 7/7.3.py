# https://www.worldometers.info/geography/flags-of-the-world/
#
# make a folder of country names and download their images in that folder

import requests
from bs4 import BeautifulSoup
import os
import shutil

url = "https://www.worldometers.info/geography/flags-of-the-world/"

result = requests.get(url)
# print(result.content)
data = result.content
soup = BeautifulSoup(data , "html.parser")
# print(soup)

c_names = soup.find_all("span",class_ = "font-bold")
c_flags = soup.find_all("img")
c_flags.pop(0)
country_names = []
for i in c_names:
    country_names.append(i.text)
country_flags = []
for j in c_flags:
    country_flags.append(j.get("src"))

# print(len(country_flags))
# for i in country_flags:
#     print(i.get("src"))
print(country_flags,country_names)


for country,flag in zip(country_names,country_flags):
    flag = "https://www.worldometers.info" + flag
    print(flag)
    country = country.replace(" ","")
    path = os.path.join(os.getcwd(),country)
    os.mkdir(path)
    img = requests.get(flag)
    img_path = os.path.join(path,country+".webp")
    with open(img_path, "wb") as f:
        f.write(img.content)


