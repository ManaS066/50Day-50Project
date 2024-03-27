import requests
from datetime import datetime
mylat = 51.50
mylong = -0.129664
parameters = {
    "lat": mylat,
    "lng": mylong,
    "formatted": 0,  # To get times in UTC
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
# print(data)
print("Sunrise:", sunrise)
print("Sunset:", sunset)
time_now = datetime.now()
print(time_now.hour)
