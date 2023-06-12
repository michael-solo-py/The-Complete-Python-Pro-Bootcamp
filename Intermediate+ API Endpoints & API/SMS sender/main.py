import os
from twilio.rest import Client

account_sid = os.environ['ACf82f6b0e3902a5c3dbdc5492bdf30a17']
auth_token = os.environ['500a2b3d3f6ebfec18d7857a0710a809']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="It's me, Misha. This is testing massage. I sent it using Python",
                     from_='+13235290427',
                     to='+380937173333'
                 )

print(message.sid)
