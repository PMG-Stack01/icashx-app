from fastapi import APIRouter
from pydantic import BaseModel
import os
from twilio.rest import Client

router = APIRouter(prefix="/communications", tags=["Communications"])

class TextMessage(BaseModel):
    to: str
    body: str

class PhoneCall(BaseModel):
    to: str
    message: str

@router.post("/text")
def send_text(msg: TextMessage):
    # Twilio credentials from environment
    sid = os.getenv("TWILIO_SID")
    token = os.getenv("TWILIO_AUTH_TOKEN")
    from_num = os.getenv("TWILIO_FROM_NUMBER", "+15555555555")

    if not (sid and token):
        return {"status": "error", "message": "Twilio credentials not set"}

    client = Client(sid, token)
    client.messages.create(body=msg.body, from_=from_num, to=msg.to)
    return {"status": "sent", "to": msg.to, "body": msg.body}

@router.post("/call")
def start_call(call: PhoneCall):
    # Placeholder for AI voice call logic
    return {
        "status": "initiated",
        "to": call.to,
        "message": call.message
    }