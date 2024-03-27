import requests
API_KEY="c7aad8abb93fab804a7a3bfd3667e3db"
from twilio.rest import Client

account_sid = 'ACe515033498b7964d8305b308d0446824'
auth_token = '1092becb238daecbee944cdd61d14162'
client = Client(account_sid, auth_token)

weather_parames ={
    "lat":19.075464,
    "lon":83.812828,
    "appid":API_KEY,
    "cnt":4
}
end_point= ("https://api.openweathermap.org/data/2.5/forecast")
response  = requests.get(end_point,params=weather_parames)
response.raise_for_status()
data=response.json()
data=data["list"]
for hour_data in data :
    precp=hour_data["weather"][0]["id"]
if int(precp)<=600 and int(precp)>=500:
    message = client.messages.create(
        from_='+15043157922',
        body='Its going to be raining plesse take you umbrella ☔along with you  -- Your personal asistant !!',
        to='+918984398009'
    )
    print(message.status)
else:
    print("good to go")
