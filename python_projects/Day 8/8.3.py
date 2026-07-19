# https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&otracker=nmenu_sub_Electronics_0_Mi&page=1
# create list of lists
# title , ratings , price
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

url = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&otracker=nmenu_sub_Electronics_0_Mi&page=1"

# data =  driver.get("https://google.com")
driver.get(url)
time.sleep(5)

soup = BeautifulSoup(driver.page_source,"html.parser")
# driver.quit()
# print(soup)

pro = soup.find_all("a",{"class":"k7wcnx"})
products = []
for p in pro :
    products.append("https://www.flipkart.com"+p.get("href"))
# print(products)
# print(len(pro))

# for pr in products :
#     print(repr(pr))

products_data = []
for link in products:
    driver.get(link)
    time.sleep(5)
    sp2 = BeautifulSoup(driver.page_source,"html.parser")
    title = sp2.find("h1", class_="v1zwn21l v1zwn26 _1psv1zeb9 _1psv1ze0")
    price = sp2.find("div", class_="v1zwn21l v1zwn20 _1psv1zeb9 _1psv1ze0")
    rating = sp2.find("div", class_="css-146c3p1")
    products_data.append([
        title.text if title else None,
        rating.text if rating else None,
        price.text if price else None
    ])
    # break

    print(products_data)
    # print(sp2.text)

driver.quit()