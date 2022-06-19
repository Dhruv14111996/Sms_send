from twilio.rest import Client

account_sid = '# add your account sid'
auth_token = '# add your account token'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid=' Write your sid',
    body=' Write your message',
    to='# write number of the person'
)

print(message.sid)
