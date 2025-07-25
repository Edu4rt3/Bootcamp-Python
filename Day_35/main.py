#SMS rain alert

import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = ""
auth_token = ""

parameters = {
    "lat": -19.912998,
    "lon": -43.940933,
    "cnt": 4,
    "appid": ""
}

will_rain = False
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain, bring a umbrella.",
        from_="+",
        to="+Your number"
    )
    print(message.status)