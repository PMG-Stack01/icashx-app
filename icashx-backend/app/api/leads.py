from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/leads", tags=["Leads"])

class Lead(BaseModel):
    id: int
    name: str
    phone: str
    address: str
    status: str = "new"

fake_leads_db: List[Lead] = []

@router.post("/create", response_model=Lead)
def create_lead(lead: Lead):
    fake_leads_db.append(lead)
    return lead

@router.get("/list", response_model=List[Lead])
def list_leads():
    return fake_leads_db

@router.get("/lead/{lead_id}", response_model=Lead)
def get_lead(lead_id: int):
    lead = next((l for l in fake_leads_db if l.id == lead_id), None)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead