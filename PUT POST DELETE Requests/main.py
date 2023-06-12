import requests
from datetime import datetime


TOKEN = "TOKEN"
USERNAME = "michael23"

pixela_endpoint = "https://pixe.la/v1/users"
# user_params = {
#     "token": "TOKEN",
#     "username": "michael23",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/{TOKEN}/graphs"
graph_config = {
    "id": "graphofmika23",
    "name": "read habit",
    "unit": "pages",
    "type": "int",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=pixela_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph_call = f"{pixela_endpoint}/{USERNAME}/graphs/graphofmika23"

today = datetime.now()
configs = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15",
}

# response = requests.post(url=pixela_endpoint, json=configs, headers=headers)
# print(response.text)
