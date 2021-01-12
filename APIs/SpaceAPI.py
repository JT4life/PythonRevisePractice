import requests

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)
json_data = response.json()

print(json_data)

# get number of people in space
in_space_count = json_data["number"]