import requests
from twilio.rest import Client
import smtplib

TWILIO_SID = ""
TWILIO_TOKEN = ""

MY_EMAIL = "rishitwt1804@gmail.com"
PASSWORD = ""

class NotificationManager:
    
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send_message(self, message):
        message = self.client.messages.create(
        body=message,
        from_="+13612735690",
        to="+919600191653"
        )
        print(message.sid)


    def send_emails(self, to_email, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_email, msg=f"Subject: Flight Deal!\n\n{message}".encode('utf-8'))