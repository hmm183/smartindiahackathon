from twilio.rest import Client

account_sid = ''
auth_token = ''#use ur own
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+13642048913',
  body='hello im undoor the wtoor,help me pls',
  to='+917893217500'
)

print(message.sid)
