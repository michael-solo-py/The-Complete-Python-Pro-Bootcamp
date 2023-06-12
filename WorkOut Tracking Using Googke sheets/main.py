import os
import json
import requests
from datetime import datetime

GENDER = "MAN"
WEIGHT_KG = 64
HEIGHT_CM = 174
AGE = 19

header_id = os.environ['HEADER_ID']
header_key = os.environ['HEADER_KEY']
header = {
    'x-app-id': header_id,
    'x-app-key': header_key
}

body = {
    "query": "ran 3 miles",
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

exercise_text = "i made 100 push-ups and ran 2 miles for a hour"  # input("Tell me which exercise you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}




response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=header)
information = response.json()
print(information)

sheets_url = "https://api.sheety.co/6484b395d67b0fda680a68cea27027c8/myWorkouts/workouts"

basic_auth_name = os.environ['BASIC_AUTH_NAME']
basic_auth_pass = os.environ['BASIC_AUTH_PASS']
basic_auth = (basic_auth_name, basic_auth_pass)

headers_s = {'Content-Type': 'application/json'}

date = datetime.now()

body_add = {
    "workout": {
        "date": date.strftime("%Y/%m/%d"),
        "time": date.strftime("%H:%M:%S"),
        "exercise": information['exercises'][0]["name"],
        "duration": information['exercises'][0]['duration_min'],
        "calories": information['exercises'][0]['nf_calories'],
        "id": 2
        }
  }
myWebsite = "https://docs.google.com/spreadsheets/d/17XmjwBgG1B3VuhDx8j20hw6jfj1TFXUoeaqM0bfURc8/edit#gid=0"
response_sheet = requests.post(url= sheets_url, data=json.dumps(body_add), auth=basic_auth, headers=headers_s)
print(response_sheet.text)
