from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Buyer

router = APIRouter(prefix="/buyers", tags=["Buyers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/list")
def list_buyers(db: Session = Depends(get_db)):
    return db.query(Buyer).order_by(Buyer.created_at.desc()).all()

@router.post("/add")
def add_buyer(buyer: Buyer, db: Session = Depends(get_db)):
    db.add(buyer)
    db.commit()
    db.refresh(buyer)
    return buyer