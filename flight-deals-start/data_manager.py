import requests
from pprint import pprint

SHEETY_URL = "https://api.sheety.co/6484b395d67b0fda680a68cea27027c8/flightDeals/prices"
HEADER = {"Authorization": "Bearer oNONONSASOononfaowqwszfdnoweoIOoWESMDFNonomOIWfsodn"}


class DataManager:
    def get_response_sheety(self):
        response = requests.get(SHEETY_URL, headers=HEADER)
        response.raise_for_status()

        # pprint(response.json())
        return response.json()["prices"]

    def put_response_sheety(self, id: int, iata):
        body = {
            'price': {
                'iataCode': iata
            }
        }
        response = requests.put(f"{SHEETY_URL}/{id}", headers=HEADER, json=body)
        response.raise_for_status()

        # pprint(response.json())

    def users(self, first_name, last_name, email):
        url_post = "https://api.sheety.co/6484b395d67b0fda680a68cea27027c8/flightDeals/users"
        body = {"user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            }
        }
        response = requests.post(url=url_post, json=body)
        pprint(response.json())



