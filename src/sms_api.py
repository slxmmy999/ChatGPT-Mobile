import smtplib
from setup import gmail_password, email, carrier
from log import AppLogger

class MessageService:
    def __init__(self):
        self.logger = AppLogger()

        self.EMAIL = email
        self.PASSWORD = gmail_password

        auth = (self.EMAIL, self.PASSWORD)
    
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(auth[0], auth[1])
    
    def send_message(self, phone_number, message):
        self.logger.SMS_LOG_EVENT("Preparing to send SMS", "info")
        recipient = phone_number + carrier
    
        self.server.sendmail(self.EMAIL, recipient, message)
        self.logger.SMS_LOG_EVENT("SMS sent", "info")