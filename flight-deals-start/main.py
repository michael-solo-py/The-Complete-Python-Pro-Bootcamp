# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()

for i in data_manager.get_response_sheety():
    city_iata = ""
    if i["iataCode"] == '':
        flight_data = FlightData(i['city'])
        city_iata = flight_data.return_iata()
        data_manager.put_response_sheety(i["id"], city_iata)

    flight_search = FlightSearch(city_iata)
    flight_search.prices()

    # notification = NotImplemented()
    # massage = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."


def sheety_users():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    email_1 = str(input("What is your email?  "))
    email_2 = str(input("Type your email again.  "))

    if email_1 == email_2:
        print("You are in the club")
        data_manager.users(first_name, last_name, email_2)


sheety_users()
