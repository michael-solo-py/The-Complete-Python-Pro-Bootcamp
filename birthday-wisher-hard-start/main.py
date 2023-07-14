import datetime as dt
import random
import smtplib
import pandas

MY_EMAIL = "@gmail.com"
PASSWOR = ""
# ------------------ open .csv file ----------------
# original = pandas.read_csv("birthdays.csv")
# data = original.to_dict(orient="record")
# for i in range(len(data)):
#     name = data[i]["name"]
#     email = data[i]["email"]
#     bd = (data[i]["month"], data[i]["day"])
#     # -------------------------------------------------
#
#     now = dt.datetime.now()
#     today = (now.month, now.day)
#
#     if today == bd:
#         templates = random.randint(1, 3)
#         with open(f"letter_templates/letter_{templates}.txt", 'r') as f:
#             letter = f.readlines()
#
#         for i in letter:
#             persone = i.replace("[NAME]", name)
#             with smtplib.SMTP("smtp.gmail.com") as connection:
#                 connection.starttls()
#                 connection.login(user=MY_EMAIL, password=PASSWOR)
#                 connection.sendmail(from_addr=MY_EMAIL, to_addrs="mikeaisolo23@gmail.com", msg=f"{persone}")

# =================================== Angela solution ========================
now = dt.datetime.now()
today = (now.month, now.day)

original = pandas.read_csv("birthdays.csv")
bd_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in original.iterrows()}

if today in bd_dict:
    birthday_person = bd_dict[today]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as f:
        letter = f.read()
        persone = letter.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWOR)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="@gmail.com", msg=f"{persone}")




