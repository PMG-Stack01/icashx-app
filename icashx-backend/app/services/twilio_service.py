from twilio.rest import Client

# Use environment vars for credentials
ACCOUNT_SID = "TWILIO_SID"
AUTH_TOKEN = "TWILIO_AUTH_TOKEN"
FROM_NUMBER = "+15555555555"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_text(to: str, body: str):
    message = client.messages.create(body=body, from_=FROM_NUMBER, to=to)
    return message.sid