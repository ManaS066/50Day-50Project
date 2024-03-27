import smtplib

my_email = "manasranjanpradhan2004@gmail.com"
code = "qkcf znzf biqp uvyl"
# smtp server of our email provider
# connection = smtplib.SMTP("smtp.gmail.com",587)
# connection.starttls()# transport layer sequrity ,sequre our connection with smtp server
# connection.login(user=my_email,password=code)
# connection.sendmail(from_addr=my_email,
#                     to_addrs="22cse066.manasranjanpradhan@giet.edu",
#                     msg="Subject: Greetings \n\n hello brother this message is send by python")
# # connection.close()

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()  # transport layer sequrity ,sequre our connection with smtp server
    connection.login(user=my_email, password=code)
    for i in range(10):
        connection.sendmail(from_addr=my_email,
                            to_addrs="22cse091.mihirranjansingh@giet.edu",
                            msg=f"Subject: Spam \n\n  This is message no:{i}  ")
