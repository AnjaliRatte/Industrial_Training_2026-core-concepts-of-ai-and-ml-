# https://search.idigbio.org/v2/search/records/?rq={%22data.dwc:dynamicProperties%22:%22nsf_tcn%22}&limit=5
#
#
# family
# county
# countrycode
# lat
# lon

import requests

response = requests.get("https://search.idigbio.org/v2/search/records/?rq={%22data.dwc:dynamicProperties%22:%22nsf_tcn%22}&limit=5")
data = response.json()

result = []

for item in data["items"]:
    row = [
        item["data"]["dwc:family"],
        item["data"]["dwc:county"],
        item["indexTerms"]["countrycode"],
        item["indexTerms"]["geopoint"]["lat"],
        item["indexTerms"]["geopoint"]["lon"]
    ]
    result.append(row)

print(result)
