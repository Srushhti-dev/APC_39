class Notification:
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print("Email sent:", message)


class SMSNotification(Notification):
    def send(self, message):
        print("SMS sent:", message)


class PushNotification(Notification):
    def send(self, message):
        print("Push notification sent:", message)


for notification in [EmailNotification(), SMSNotification(), PushNotification()]:
    notification.send("Hello!")
