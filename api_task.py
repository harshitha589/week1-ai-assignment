import requests
response = requests.get("https://zenquotes.io/api/random")
data = response.json()
print("Quote of the Day:")
print(data[0]["q"])
print("- " + data[0]["a"])