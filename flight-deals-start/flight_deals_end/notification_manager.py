from twilio.rest import Client
import smtplib


TWILIO_SID = 'ACf82f6b0e3902a5c3dbdc5492bdf30a17'
TWILIO_AUTH_TOKEN = '500a2b3d3f6ebfec18d7857a0710a809'
TWILIO_VIRTUAL_NUMBER = '+13235290427'
TWILIO_VERIFIED_NUMBER = '+380937173273'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )