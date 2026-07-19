# https://www.worldometers.info/geography/flags-of-the-world/
#
# print all country names

import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/geography/flags-of-the-world/"

result = requests.get(url)
# print(result.content)
data = result.content
soup = BeautifulSoup(data , "html.parser")
# print(soup)

country_names = soup.find_all("span",class_ = "font-bold")
for country in country_names:
    print(country.text)
