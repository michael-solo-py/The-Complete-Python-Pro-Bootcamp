from twilio.rest import Client


class NotificationManager(Client):
    def __init__(self):
        super().__init__()
        self.account_sid = 'SID'
        self.auth_token = 'TOKEN'

    def send(self, massage):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages \
            .create(
            body= massage,
            from_='+13235290427',
            to='+380937173333'
        )
        print(message.sid)
