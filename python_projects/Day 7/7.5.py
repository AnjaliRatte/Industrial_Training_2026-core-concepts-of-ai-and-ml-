# https://realpython.github.io/fake-jobs/
#
# get
#
# Job Title
# company name
# address
# date

import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
data = requests.get(url).content

soup = BeautifulSoup(data,"html.parser")
job_title = soup.find_all("h2", class_="title is-5")
company_name = soup.find_all("h3",class_="subtitle is-6 company")
address = soup.find_all("p",class_="location")
date = soup.find_all("time")

result = []
for jt,cn,a,d in zip(job_title,company_name,address,date):
    row = {}
    row["job title"]=jt.text
    row["company name"]=cn.text
    row["address"]=a.text.strip()
    row["date posted"]=d.text
    # row.append(jt.text)
    # row.append(cn.text)
    # row.append(a.text)
    # row.append(d.text)
    result.append(row)

for i in result:
    print(i)
