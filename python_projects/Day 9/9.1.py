# https://www.fazwaz.com/property-for-sale/thailand/bangkok?bedrooms=2+&ownership=3120
#
# Sale Price
# Original Price
# Address
# Project Name
# Unit ID
# Bedrooms
# Bathrooms
# Size
# Price/Sqm
# Floor
# Project Completed
# CAM Fee
# Condo Ownership
# Listed By    Date Listed    Last Updated     Beds     Sold Date    Furniture    View    Ownership

from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
url = "https://www.fazwaz.com/property-for-sale/thailand/bangkok?bedrooms=2+&ownership=3120"

driver.get(url)
time.sleep(5)

soup = BeautifulSoup(driver.page_source,"html.parser")

pr = soup.find_all("a",{"class":"link-unit"})

properties = []
for i in pr:
    properties.append(i.get("href"))

# print(properties)

result=[]
for property in properties:
    driver.get(property)
    time.sleep(5)
    sp = BeautifulSoup(driver.page_source,"html.parser")
    p = {}

    sale_price = sp.find("div",{"class":"price-message"})
    p["sale price "]= " ".join(sale_price.text.split())

    try:
        original_price = sp.find("small",{"class":"gallery-unit-sale-price__price-reduce"})
        p["original price"]= " ".join(original_price.text.split())
    except:
        original_price = sp.find("div", {"class": "price-message"})
        p["original price"]= " ".join(original_price.text.split())
    # sp.find("", {"class": ""})

    address = sp.find("span",{"class":"project-location"})
    p["address"]=" ".join(address.text.split())

    project_name = sp.find("a", {"class": "project-information-info"})
    p["project name "]=" ".join(project_name.text.split())

    unit_id = sp.find("div", {"class": "unit-info-element__item"})
    p["unit id "]=" ".join(unit_id.text.split())

    elements = sp.find_all("div", {"class": "property-info-element"})
    lis = []
    for i in elements:
        j=i.text.split()
        lis.append(" ".join(j))
    bedrooms = lis[0]
    p["bedrooms"]= bedrooms

    bathrooms = lis[1]
    p["bathrooms"]=bathrooms

    size = lis[2]
    p["size"] = size

    floors = lis[3]
    p["floors"]=floors

    project_completed = lis[4]
    p["project completed on "] = project_completed

    a = sp.find_all("span", {"class":"basic-information-info"})
    lis2 = []
    for k in a :
        i=k.text.split()
        lis2.append(" ".join(i))
    listed_date = lis2[0]
    p["date listed"]=listed_date

    last_updated = lis2[1]
    p["last updated"]=last_updated

    price_sqm = lis2[6]
    p["price/sqm"]=price_sqm

    furniture = lis2[9]
    p["furnished"]=furniture

    ownership = lis2[8]
    p["ownership"]= ownership

    cam_fee = lis2[13]
    p["campus fee"]=cam_fee

    listed_by = lis2[14]
    p["listed by"]=listed_by

    view = lis2[10]
    p["view"]=view
    print(p)

    result.append(p)
print(result)




