# loading a image from a url

url = "https://assets.farmsanctuary.org/content/uploads/2021/12/28124545/2021_04-28_FSNY_Rad_Dobie_Milo_and_Macka_ducks_DSC_3972_CREDIT_Farm_Sanctuary-1600x1068.jpg"


import requests

response = requests.get(url)

print(response)

fn = "img.jpg"

with open(fn,"wb") as f:
    f.write(response.content)
    f.close()