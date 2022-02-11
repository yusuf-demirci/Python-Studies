import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# iss_location = (data["iss_position"]["latitude"], data["iss_position"]["longitude"])
# print(iss_location)
parameters = {
    "lat": 40.853271,
    "lng": 29.881519,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now().hour

print(sunrise)
print(sunset)
print(time_now)