from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
url = "https://www.jiomart.com/sections/large-appliances"

driver.get(url)
time.sleep(20)
x = 0
y = 500
for i in range(5):
    driver.execute_script("window.scrollTo("+str(x)+", "+str(y)+");")
    x = y
    y = y + 500

    time.sleep(3)
soup = BeautifulSoup(driver.page_source,"html.parser")
title = soup.find_all("h3",class_="productCard__productTitle")
price = soup.find_all("span",class_="PriceContainer__currentPrice")
print(len(title),len(price))

result = []

for t,p in list(zip(title,price))[:100]:
    result.append([t.get_text(strip=True), p.get_text(strip=True)])
print(result)
print(len(result))



