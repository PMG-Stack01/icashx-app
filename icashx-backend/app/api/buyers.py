from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter(prefix="/buyers", tags=["Buyers"])

class Buyer(BaseModel):
    id: int
    name: str
    email: str
    location: str
    max_budget: float

fake_buyers_db: List[Buyer] = []

@router.post("/add", response_model=Buyer)
def add_buyer(buyer: Buyer):
    fake_buyers_db.append(buyer)
    return buyer

@router.get("/match")
def match_buyers(location: str, budget: float) -> List[Dict]:
    buyers = [b for b in fake_buyers_db if b.location.lower() == location.lower() and b.max_budget >= budget]
    return buyers