# http://quotes.toscrape.com/
#
# get
# quote and author name

import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
data = requests.get(url).content
# data = result.content
# print(data)
# print(data)
soup = BeautifulSoup(data,"html.parser")
# print(soup)
quotes = soup.find_all("span",class_ = "text")
authors = soup.find_all("small",class_ = "author")
result = []
for quote,author in zip(quotes,authors):
    row = []
    # print(i.text)
    row.append(quote.text)
    row.append(author.text)
    result.append(row)
print(result)
