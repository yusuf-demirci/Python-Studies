
from datetime import datetime
import smtplib
import pandas
import random

today = (datetime.now().month, datetime.now().day)
dates = pandas.read_csv("birthdays.csv")

my_email = "python.trial09@gmail.com"
password = "*********"

for row in dates.itertuples():
    if today == (row.month, row.day):
        
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as data:
            letter = data.read()
            letter = letter.replace("[NAME]", row.name)
            
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row.email,
                msg=f"Subject:Happy Birthday!\n\n{letter}"
            )
        
            
        
        



