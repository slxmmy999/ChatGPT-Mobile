import smtplib
from log import AppLogger

class MessageService:
    def __init__(self, email, password, carrier):
        self.logger = AppLogger()

        self.EMAIL = email
        self.PASSWORD = password
        self.carrier = carrier

        self.auth = (self.EMAIL, self.PASSWORD)
    
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(self.auth[0], self.auth[1])
    
    def send_message(self, phone_number, message) -> bool:
        try:
            self.logger.SMS_LOG_EVENT("Preparing to send SMS", "info")
            recipient = phone_number + self.carrier
        
            self.server.sendmail(self.EMAIL, recipient, message)
            self.logger.SMS_LOG_EVENT("SMS sent", "info")
            return True
        except Exception as e:
            self.logger.SMS_LOG_EVENT(f"SMS failed to send: {e}", "error")
            return False
        
    def reload(self, email: str = None, password: str = None, carrier: str = None):
        self.__init__(email or self.EMAIL, password or self.PASSWORD, carrier or self.carrier)