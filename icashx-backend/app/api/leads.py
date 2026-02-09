from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Lead

router = APIRouter(prefix="/leads", tags=["Leads"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/list")
def list_leads(db: Session = Depends(get_db)):
    return db.query(Lead).all()

@router.post("/add")
def add_lead(lead: Lead, db: Session = Depends(get_db)):
    db.add(lead)
    db.commit()
    db.refresh(lead)
    return lead