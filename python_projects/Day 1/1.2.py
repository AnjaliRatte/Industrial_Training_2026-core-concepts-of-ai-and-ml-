# https://api.github.com/users/mralexgray/repos
#
# create list of lists
#
# name
# avatar_url
# type
# login
# created_at
# size
# visibility
# language


# import requests module
import requests

# Making a get request
response = requests.get('https://api.github.com/users/mralexgray/repos')

# print json content
data = response.json()

result= []

for user in data:
     row = [
         user["name"],
         user["owner"]["avatar_url"],
         user["owner"]["type"],
         user["owner"]["login"],
         user["created_at"],
         user["size"],
         user["visibility"],
         user["language"]
     ]

     result.append(row)


print(result)