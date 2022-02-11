import smtplib
import datetime as dt
import random

my_email = "python.trial09@gmail.com"
password = "# pythontrial"

current_date = dt.datetime.now()
    
if current_date.isoweekday() == 6:
    with open("quotes.txt") as file:
        data = file.readlines()
        quote = random.choice(data)

    with smtplib.SMTP("smtp.gmail.com") as connection: 
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="python.trial09@yahoo.com", 
            msg=f"Subject:Hello\n\n{quote}")

