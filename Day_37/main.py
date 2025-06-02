import requests
from datetime import datetime

TOKEN =  "oihsadkjsak"
USERNAME = "eduarte"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

users_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=users_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How much hours did you code today? ")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

edit_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20250601"

edit_data = {"quantity":"2.5"}

# response = requests.put(url=edit_endpoint, json=edit_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)