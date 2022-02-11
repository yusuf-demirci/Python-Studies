import requests
from datetime import datetime

USER_NAME = "Your User Name"
TOKEN = "Your Token"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

data_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
current_date = datetime.now().strftime("%Y%m%d")

data_parameters = {
    "date": current_date,
    "quantity": "4.5"
}

# response = requests.post(url=data_endpoint, json=data_parameters, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/20211130"
update_params = {
    "quantity": "7.0"
}

# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{current_date}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
