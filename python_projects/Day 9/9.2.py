# https://restaurantguru.com/restaurant-Portugal-t1
#
#
# ["Restaurant Name", "Restaurant Category", "Restaurant Address", "Restaurant P.Number", "Restaurant Website",
#           "Restaurant lat/long", "Source"]

from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
url = "https://restaurantguru.com/restaurant-Portugal-t1"

driver.get(url)
time.sleep(20)

soup = BeautifulSoup(driver.page_source,"html.parser")

# pr = soup.find_all("a",{"class":"link-unit"})
links = soup.find_all("a",class_="notranslate title_url link link--secondary rest-card__link")
ls = []
for link in links:
    ls.append(link.get("href"))

result = []

for l in ls:
    driver.get(l)
    time.sleep(5)
    print(l)
    sp = BeautifulSoup(driver.page_source,"html.parser")
    result.append([sp.find("h1",class_="notranslate").text.replace("\n",""),sp.find("div",class_="cuisine_hidden").text.replace("\n","").replace(" ",""),sp.find("div",class_="address").text.replace("\n","").replace("Address","").replace("                            "," ")])
    print(result)

print(result)
#unavailable