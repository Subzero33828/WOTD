# from twilioConfig import amount_sid, auth_token, from_num, to_num
# from twilio.rest import Client

# account_sid = 'ACe0513e604e5c2e3e7af87582486a1253'
# auth_token = 'ecc19521ddac85ffc83a139b576f5df0'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
    
#     #'+ton_twilio_numero',#
#     from_= '+1 844 459 0221',
    
#     body="Le mot du jour d'aujourd'hui est : [Merci!]Réfléchissez à la manière dont vous pouvez appliquer ce nouvel outil.", 
    
#     # +leur_phone_numer
#     to='+1 215 501 3351')
    
# print(message.sid)



# from twilio.rest import Client
# account_sid = 'ACe0513e604e5c2e3e7af87582486a1253'
# auth_token = '[AuthToken]'
# client = Client(account_sid, auth_token)
# message = client.messages.create(
#   from='+18444590221',
#   body='Le mot du jour d'aujourd'hui est : [votre mot',
#   to='+18777804236'
# )
# print(message.sid)
#code sameple from website [https://console.twilio.com/us1/develop/sms/try-it-out/send-an-sms]

# https://www.youtube.com/watch?v=ENHnfQ3cBQM
# https://youtu.be/Hd7n2J5mZ7o?si=STp_9cC-rQfp1cT6





#gpt

from twilio.rest import Client

# Replace these with your actual Twilio credentials
account_sid = 'ACe0513e604e5c2e3e7af87582486a1253'
auth_token = 'ecc19521ddac85ffc83a139b576f5df0'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='18444590221',  # Your Twilio number
    body="Le mot du jour d'aujourd'hui est : [Merci!] Réfléchissez à la manière dont vous pouvez appliquer ce nouvel outil.",
    to='12155013351'  # Recipient's phone number
)

print(message.sid)
