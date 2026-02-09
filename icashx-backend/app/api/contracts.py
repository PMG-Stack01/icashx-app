from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Contract

router = APIRouter(prefix="/contracts", tags=["Contracts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/list")
def list_contracts(db: Session = Depends(get_db)):
    return db.query(Contract).all()

@router.post("/add")
def add_contract(contract: Contract, db: Session = Depends(get_db)):
    db.add(contract)
    db.commit()
    db.refresh(contract)
    return contract