import requests
from datetime import datetime as dt

MY_LATITUDE = 51.2115
MY_LONGITUDE = 24.7077

parameters = {
    "lat": MY_LATITUDE,
    "lgt": MY_LONGITUDE,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

now = dt.now()
print(sunset)
