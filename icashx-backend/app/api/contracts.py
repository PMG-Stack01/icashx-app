from fastapi import APIRouter
from pydantic import BaseModel
from datetime import date

router = APIRouter(prefix="/contracts", tags=["Contracts"])

class ContractData(BaseModel):
    seller_name: str
    property_address: str
    purchase_price: float
    closing_date: date
    email: str

@router.post("/generate")
def generate_contract(data: ContractData):
    # Placeholder for Docx/PDF creation
    file_path = f"/tmp/{data.seller_name}_contract.pdf"
    return {"message": "Contract generated", "file": file_path}

@router.post("/send")
def send_contract(data: ContractData):
    # Placeholder for email/text logic
    return {
        "status": "sent",
        "recipient_email": data.email,
        "property": data.property_address,
        "price": data.purchase_price
    }