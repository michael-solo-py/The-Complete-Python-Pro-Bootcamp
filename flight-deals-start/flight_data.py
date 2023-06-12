import requests


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, city):
        self.header = {"apikey": "KEY", }
        self.search_url = "https://tequila-api.kiwi.com/locations/query"
        self.parameter = {"term": city}
        self.response = requests.get(url=self.search_url, params=self.parameter, headers=self.header)

    def return_iata(self):
        return self.response.json()["locations"][0]["code"]
