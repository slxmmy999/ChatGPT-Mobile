import smtplib
from api_keys import gmail_password, email, carrier

EMAIL = email
PASSWORD = gmail_password
 
def send_message(phone_number, message):
    recipient = phone_number + carrier
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, message)