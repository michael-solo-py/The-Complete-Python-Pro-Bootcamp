import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self, city_fly_to):
        self.header = {
            "apikey": "kNaRPuTXYPU94lFwVr5gSB8U8xix5Zjc",
            "authorization_token": self.get_authorization_token(),
                       }
        self.search_url = "https://api.tequila.kiwi.com/v2/search"
        self.parameter = {"fly_from ": "WAW",
                          "fly_to": city_fly_to,
                          "date_from": "27/04/2023",
                          "date_to": "10/05/2023",
                          "adults": 3,
                          "selected_cabins": "M",
                          "adult_hold_bag": "1,1,1",
                          "adult_hand_bag": "1,1,1",
                          "curr": "PLN",
                          "select_stop_airport": "NYC,LON"
                          }
        self.response = requests.get(url=self.search_url, params=self.parameter, headers=self.header)

    def check_flights(self):
        try:
            data = self.response.json()["data"][0]
        except IndexError:
            print(f"No flights found.")
            return None

    def prices(self):
        print(self.response.json())

    def get_authorization_token(self):
        url = "https://api.tequila.kiwi.com/manage/create_auth_token"

        header = {
            "content-type": "application/json",
            "apikey": "API_KEY",
        }
        response = requests.post(url, headers=header)

        return response.json()["authorization_token"]
