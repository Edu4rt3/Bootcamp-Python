#workout Tracker

import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 180
AGE = 19

APP_ID = "613f5d3f"
API_KEY = "1589d6c44be5c1ce140de7a49811624f"

SHEETY_ENDPOINT = "https://api.sheety.co/577d9e1dd3eb9d13208ede993a831a11/myWorkouts/workouts"
URL_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

parameters = {
    "query": input("What activity you did today and for which time? "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json"
}

response = requests.post(url=URL_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(
  SHEETY_ENDPOINT, 
  json=sheet_inputs, 
  auth=(
      "Eduarte", 
      "YAB123@*",
  )
)
if sheet_response.status_code == 200:
    print(f"✅ Enviado para a planilha: {exercise['name']}")
else:
    print(f"❌ Erro ao enviar: {sheet_response.text}")


