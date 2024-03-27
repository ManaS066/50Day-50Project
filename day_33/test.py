# API = Aplication progarming interface
#iss location

import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# #output :<Response [200]> it is response code of the request
# response code and their meaning
# 1XX :hold on
# 2XX: Here you go
# 3XX :go away
# 4XX : not found
# 5XX website error

# status code exception
# if response.status_code == 404:
#     raise Exception("That resource doesnot exit")
# elif response.status_code == 401:
#     raise Exception("you are not authorised ")

# We can use request module for doing this
response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude,latitude)
print(iss_position)


