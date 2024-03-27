import requests
from datetime import datetime
import smtplib
import time

mylat = 51.50
mylong = -0.129664

my_email = "manasranjanpradhan2004@gmail.com"
code = "qkcf znzf biqp uvyl"


def is_night():
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
    time_now = datetime.now().hour
    hour = time_now.hour
    if time_now >= sunset or time_now <= sunrise:
        return True


def is_iss_overhead():
    response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
    response1.raise_for_status()

    data = response1.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if mylat - 5 <= latitude <= mylat + 5 and mylong - 5 <= longitude <= mylong + 5:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, password=code)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg="subject : Look up to sky \n\n The ISS is above your head")
