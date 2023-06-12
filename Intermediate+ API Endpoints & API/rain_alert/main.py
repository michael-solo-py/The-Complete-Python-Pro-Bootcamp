import requests
import os
from twilio.rest import Client


account_sid = os.environ['ACf82f6b0e3902a5c3dbdc5492bdf30a17']
auth_token = os.environ['500a2b3d3f6ebfec18d7857a0710a809']

api_key = "aec32c9ec74e10567ced23bb1d071ae8"
parameters = {
    "lat": 50.133883,
    "lon": 30.598706,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()["hourly"][0:12]


will_rain = False

for hour in data:
    hourly_weather_status = hour["weather"][0]["id"]
    if int(hourly_weather_status) < 700:
        will_rain = True


if will_rain:

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's me, Misha. This is testing massage. I sent it using Python",
        from_='+13235290427',
        to='+3809371733333'
    )

    print(message.sid)
