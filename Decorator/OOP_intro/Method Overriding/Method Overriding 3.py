class Notification:
    def send(self):
        print("Sending a general notification...")

class EmailNotification(Notification):
    def send(self):
        print("Sending an email notification!")

class SMSNotification(Notification):
    def send(self):
        print("Sending an SMS notification!")


def notify_all(notifications):
    for note in notifications:
        note.send()  


email = EmailNotification()
sms = SMSNotification()


notifications = [email, sms]


notify_all(notifications)
