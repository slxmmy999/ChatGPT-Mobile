import smtplib
from setup import gmail_password, email, carrier
from log import AppLogger

logger = AppLogger()

EMAIL = email
PASSWORD = gmail_password
 
def send_message(phone_number, message):
    logger.SMS_LOG_EVENT("Preparing to send SMS", "info")
    recipient = phone_number + carrier
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, message)
    logger.SMS_LOG_EVENT("SMS sent", "info")