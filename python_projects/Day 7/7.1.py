# web scraping

import requests

url = "https://en.wikipedia.org/wiki/Flag_of_India"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)
data = result.content

from bs4 import BeautifulSoup

soup = BeautifulSoup(data, 'html.parser')

heading = soup.find("h1")
print(heading.text)


sh = soup.find_all("h2")

for h in sh:
    print(h.text)
