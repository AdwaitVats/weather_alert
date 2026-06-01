# Latitude and Longitude for Devanahalli
MY_LAT=13.241715
MY_LONG=77.713730
ENDPOINT="https://api.openweathermap.org/data/2.5/forecast"
from twilio.rest import Client
import os
api_key=os.environ["OWM_API_KEY"]
ACCOUNT_SID = os.environ["TWILIO_SID"]
AUTH_TOKEN = os.environ["TWILIO_TOKEN"]
parameters={
    "lat":MY_LAT,
    "lon":MY_LONG,
    "cnt":4,
    "appid":api_key,
}
import requests
response=requests.get(ENDPOINT,params=parameters)
response.raise_for_status()
weather_data=response.json()
conditions_12hours=[]
for num in range(0,4):
    condition_code=weather_data["list"][num]["weather"][0]["id"]
    conditions_12hours.append(condition_code)
if any(condition < 700 for condition in conditions_12hours):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message=client.messages.create(
    body="Carry an ☂️. It is going to rain today.",
    from_=os.environ["TWILIO_FROM"],
    to=os.environ["MY_PHONE"],)
        print(message.status)


