import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758

def return_true():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= MY_LAT <= MY_LAT + 5 and MY_LONG - 5 <= MY_LONG <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


def function():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="@gmail.com", password="")
        connection.sendmail(from_addr="@gmail.com", to_addrs="@gmail.com",
                            msg="look up")


if __name__ == "__main__":
    while True:
        time.sleep(60)
        if return_true() and is_night():
                function()

