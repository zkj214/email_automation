import schedule
import smtplib
import time


MY_EMAIL="pythonexercise214@gmail.com"
APP_PASSWORD="gqee yzcx hqfh yqdy "

# send email every 3 months starting from now


def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, APP_PASSWORD)
        connection.sendmail(MY_EMAIL,
                            "alhaj.ziebhar214@gmail.com",
                            msg="Subject:Requesting Salary Raise\n\nI would like to request a raise for every 3 months. Hoping for your kind consideration.\nThanks.")

    print("The email has been sent to the boss.")


schedule.every(90).days.do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)