# https://www.scrapingcourse.com/ecommerce/
# create list of lists
#
# title
# price
# image url
# Description
# SKU
# Category

import requests
from bs4 import BeautifulSoup

url = "https://www.scrapingcourse.com/ecommerce/"
data = requests.get(url).content
soup = BeautifulSoup(data,"html.parser")
result = []
# print(soup.find("main",class_="site-main"))
page_links = []
for i in soup.find_all("a",class_="page-numbers"):
    page_links.append(i.get("href"))
# print(page_links)

for link in page_links:
    response= requests.get(link).content
    sp = BeautifulSoup(response,"html.parser")
    products = sp.find_all("a",class_="woocommerce-LoopProduct-link woocommerce-loop-product__link")
    for i in products :
        row = []
        product_link = i.get("href")
        product = requests.get(product_link).content
        sp2 = BeautifulSoup(product,"html.parser")

        title = sp2.find("h1",class_="product_title entry-title")
        row.append(title.text)

        price = sp2.find("bdi")
        row.append(price.text)

        img = sp2.find("img")
        row.append(img.get("src"))

        des = sp2.find("div",class_="woocommerce-Tabs-panel woocommerce-Tabs-panel--description panel entry-content wc-tab")
        row.append(des.text)

        sku = sp2.find("span",class_="sku_wrapper")
        row.append(sku.text)

        cat = sp2.find("span",class_="posted_in")
        row.append(cat.text)

        result.append(row)
    break

print(result)
        # break
    # break
