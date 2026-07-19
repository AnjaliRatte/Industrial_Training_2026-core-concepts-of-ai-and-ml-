# https://www.amazon.in/s?k=iphone&crid=3C6WQC5WJM8YA&sprefix=iphone+13%2Caps%2C350&ref=nb_sb_noss_2
#
# Product Name
# Rating
# Rating count
# Price
# Get it by
# About this item


from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
url = "https://www.amazon.in/s?k=iphone&crid=3C6WQC5WJM8YA&sprefix=iphone+13%2Caps%2C350&ref=nb_sb_noss_2"

driver.get(url)
time.sleep(5)

soup = BeautifulSoup(driver.page_source,"html.parser")
p = soup.find_all("a",{"class":"a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal"})

products_link = []
for i in p:
    products_link.append("https://www.amazon.in/"+i.get("href"))


result = []
for link in products_link:
    print(link)
    driver.get(link)
    time.sleep(5)

    sp = BeautifulSoup(driver.page_source,"html.parser")
    title = sp.find("span",{"class":"a-size-large product-title-word-break"})
    price = sp.find("span",{"class":"a-price-whole"})
    about = sp.find("div",{"class":"a-section a-spacing-medium a-spacing-top-small"})
    ratings = sp.find("span",{"class":"a-size-small a-color-base"})
    rating_count = sp.find("span", {"class": "a-size-small","id":"acrCustomerReviewText"})
    gib = sp.find("span",{"data-csa-c-delivery-type":"delivery"}).text.replace("Details","")
    print([
        title.text if title else None,
        price.text if price else None,
        about.text if about else None,
        ratings.text if ratings else None,
        rating_count.text if rating_count else None,
        gib if gib else None,

    ])
# print(result)

    # break
