class Notification:
    def send(self):
        print("Sending a general notification...")

class EmailNotification(Notification):
    def send(self):
        print("Sending an email notification!")

class SMSNotification(Notification):
    def send(self):
        print("Sending an SMS notification!")


email = EmailNotification()
sms = SMSNotification()


email.send()
sms.send()
