import requests

url = "https://bored-api.appbrewery.com/random"
response = requests.get(url)

print(response.json().get("activity"))

#extract???