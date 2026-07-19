# https://www.ajio.com/s/caps-and-hats-4461-75481
#
# name
# price
# brand
# MRP
# product details

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.ajio.com/s/caps-and-hats-4461-75481"
driver.get(url)
time.sleep(5)
soup = BeautifulSoup(driver.page_source,"html.parser")
# print(soup)
products = soup.find_all("a",{"class":"rilrtl-products-list__link desktop"})
items = []
for p in products:
    items.append("https://www.ajio.com"+p.get("href"))

result = []

for item in items:
    driver.get(item)
    time.sleep(5)
    sp = BeautifulSoup(driver.page_source,"html.parser")
    result.append([sp.find("h1",class_="prod-name").text,sp.find("div",class_="prod-sp").text,sp.find("h2",class_="brand-name").text,sp.find("span",class_="prod-cp").text,sp.find("section",class_="prod-desc")])

print(result)
##access denied