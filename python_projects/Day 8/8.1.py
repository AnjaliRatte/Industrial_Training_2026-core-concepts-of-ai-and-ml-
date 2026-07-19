# https://in.puma.com/in/en/collections/collections-football/collections-football-manchester-city-fc
# create list of lists
# product_name, price, product_description

import requests
from bs4 import BeautifulSoup

url = "https://in.puma.com/in/en/collections/collections-football/collections-football-manchester-city-fc"
data = requests.get(url).content

soup = BeautifulSoup(data,"html.parser")

item = soup.find_all("a",class_="tw-4m0ihd tw-hlsw0v cursor-pointer absolute inset-0 z-[1] focus:outline-none focus:ring-2 focus:ring-puma-black")
# i=0
links = []
for h in item :
    l=h.get("href")
    links.append("https://in.puma.com"+l)
    # i+=1

result = []
for link in links :
    row = []
    dt = requests.get(link).content
    sp = BeautifulSoup(dt,"html.parser")
    name = sp.find("h1").text
    row.append(name)
    try:
        price = sp.find("span",class_="whitespace-nowrap text-base text-red font-bold override:text-xl override:md:text-2xl").text
        row.append(price)
        # print(price.text)
    except:
        price = sp.find("span",class_="whitespace-nowrap text-base font-bold override:md:text-2xl").text
        row.append(price)
    prod_des = sp.find("div",class_="tw-1rgvuf0 tw-1igwn51 tw-dynr3h tw-l8cie8 pb-4")
    row.append(prod_des.text)
    result.append(row)
print(result)

