Data = {"countries":[{"countryname":"India","flag":"http:\\wptrafficanalyzer.in\\demo1\\india.png","language":"Hindi","capital":"New Delhi","currency":{"code":"INR","currencyname":"Rupee"}},{"countryname":"Pakistan","flag":"http:\\wptrafficanalyzer.in\\demo1\\pakistan.png","language":"Urdu","capital":"Islamabad","currency":{"code":"PKR","currencyname":"Pakistani Rupee"}},{"countryname":"Sri Lanka","flag":"http:\\wptrafficanalyzer.in\\demo1\\srilanka.png","language":"Sinhala","capital":"Sri Jayawardenapura Kotte","currency":{"code":"SKR","currencyname":"Sri Lankan Rupee"}},{"countryname":"China","flag":"http:\\wptrafficanalyzer.in\\demo1\\china.png","language":"Chinese","capital":"Beijing","currency":{"code":"CNY","currencyname":"Renminbi"}},{"countryname":"Bangladesh","flag":"http:\\wptrafficanalyzer.in\\demo1\\bangladesh.png","language":"Bangla","capital":"Dhaka","currency":{"code":"BDT","currencyname":"Taka"}},{"countryname":"Nepal","flag":"http:\\wptrafficanalyzer.in\\demo1\\nepal.png","language":"Nepal Bhasa","capital":"Kathmandu","currency":{"code":"NPR","currencyname":"Napalese Rupee"}},{"countryname":"Afghanistan","flag":"http:\\wptrafficanalyzer.in\\demo1\\afghanistan.png","language":"Dari Persian","capital":"Kabul","currency":{"code":"AFN","currencyname":"Afghani"}},{"countryname":"North Korea","flag":"http:\\wptrafficanalyzer.in\\demo1\\nkorea.png","language":"Korean","capital":"Pyongyang","currency":{"code":"KPW","currencyname":"North Korean Won"}},{"countryname":"South Korea","flag":"http:\\wptrafficanalyzer.in\\demo1\\skorea.png","language":"Korean","capital":"Seoul","currency":{"code":"KRW","currencyname":"South Korean Won"}},{"countryname":"Japan","flag":"http:\\wptrafficanalyzer.in\\demo1\\japan.png","language":"Japanese","capital":"Tokyo","currency":{"code":"JPY","currencyname":"Yen"}}]}
result = []

for country in Data["countries"]:
    row = [
        country["countryname"],
        country["flag"],
        country["language"],
        country["capital"],
        country["currency"]["code"],
        country["currency"]["currencyname"]
    ]
    result.append(row)

print(result)




