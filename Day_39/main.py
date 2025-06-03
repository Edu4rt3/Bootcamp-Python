import requests

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

AMADEUS_KEY = "ok023KC6G6xu6CVeKVMHG1vMY9gD28vj"
AMADEUS_SECRET = "bUZgws0qB7Hywf1l"

amadeus_url = "https://test.api.amadeus.com/v1/security/oauth2/token"

payload = {
    'grant_type': 'client_credentials',
    'client_id': AMADEUS_KEY,
    'client_secret': AMADEUS_SECRET
}

response = requests.post(amadeus_url, data=payload)

# Verificando e imprimindo o resultado
if response.status_code == 200:
    access_token = response.json()['access_token']
    print("✅ Access token gerado com sucesso:")
    print(access_token)