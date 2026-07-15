import smtplib
import random
my_email = "vyshinigowda@gmail.com"
Password = "iptd rwed gxva nppm"

import datetime as dt

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt","r") as data:
        all_quotes = data.readlines()
        quote = random.choice(all_quotes) 

    
    with  smtplib.SMTP("smtp.gmail.com",587) as connection :
        connection.starttls()
        connection.login(user = my_email,password = Password)
        connection.sendmail(from_addr = my_email,to_addrs = my_email,msg = f"subject :Monday Motivation\n\n{quote}.")
