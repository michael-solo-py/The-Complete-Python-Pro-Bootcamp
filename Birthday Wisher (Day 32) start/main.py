import smtplib
import datetime as dt
import random

now = dt.datetime.now()
CURRENT_DAY = now.weekday()


def massage():
    with open("quotes.txt", "r") as motivation:
        ms = motivation.readlines()
    return random.choice(ms)


def email(massage):
    my_email = "@gmail.com"
    password = "PASS"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="@gmail.com", msg=f"{massage}")


if __name__ == "__main__":
    if CURRENT_DAY == 2:
        email(massage())
