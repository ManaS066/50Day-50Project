# import smtplib
# my_email = "manasranjanpradhan2004@gmail.com"
# code = "qkcf znzf biqp uvyl"
# # smtp server of our email provider
# # connection = smtplib.SMTP("smtp.gmail.com",587)
# # connection.starttls()# transport layer sequrity ,sequre our connection with smtp server
# # connection.login(user=my_email,password=code)
# # connection.sendmail(from_addr=my_email,
# #                     to_addrs="22cse066.manasranjanpradhan@giet.edu",
# #                     msg="Subject: Greetings \n\n hello brother this message is send by python")
# # # connection.close()
#
# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#     connection.starttls()# transport layer sequrity ,sequre our connection with smtp server
#     connection.login(user=my_email,password=code)
#     connection.sendmail(from_addr=my_email,
#                             to_addrs="mp382107@gmail.com",
#                             msg=f"Subject: Spam \n\n  This is message no: {i} ")




import datetime as dt
import smtplib
import random

my_email = "manasranjanpradhan2004@gmail.com"
code = "qkcf znzf biqp uvyl"
now = dt.datetime.now()
send_day = 3
day_of_week = now.weekday()
if send_day == day_of_week:
    with open(file="quotes.txt") as quote:
        all_quote = quote.readlines()
        quot = random.choice(all_quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # transport layer security ,secure our connection with smtp server
        connection.login(user=my_email, password=code)
        connection.sendmail(from_addr=my_email,
                            to_addrs="parshuramsahoo57@gmail.com",
                            msg=f"Subject : Motivational Quote \n\n {quot}")
