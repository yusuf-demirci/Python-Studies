import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 40.853271 # Your latitude
MY_LONG = 29.881519 # Your longitude
MY_EMAIL = "python.trial09@gmail.com"
PASSWORD = "# pythontrial"


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    
    print(iss_latitude, iss_longitude)
    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    #If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.

    
    print(time_now.hour)
    print(sunrise, sunset)


    if time_now.hour < sunrise or time_now.hour > sunset:
        return True

while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="ydemirci7@gmail.com",
                msg="Subject:Attention!\n\nInternational Space System is approaching!"
            )

