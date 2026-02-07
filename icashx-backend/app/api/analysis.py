from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import random
import openai
import os

router = APIRouter(prefix="/analysis", tags=["Property Analysis"])

# Set your OpenAI key from environment (configured in Render)
openai.api_key = os.getenv("OPENAI_API_KEY")

class AnalysisRequest(BaseModel):
    address: str
    bedrooms: int | None = None
    bathrooms: float | None = None
    sqft: int | None = None
    description: str | None = None

@router.post("/run", response_model=Dict[str, Any])
def run_analysis(request: AnalysisRequest):
    """
    Runs automated property analysis.
    1. Calls OpenAI to estimate ARV/repair cost if key present.
    2. Falls back to randomized values if running without API key.
    """
    try:
        # === When OpenAI key configured ===
        if openai.api_key:
            prompt = (
                f"Estimate the after-repair value (ARV), repair cost, and fair cash offer "
                f"for a house located at {request.address}. "
                f"Include fields: arv, repair_cost, cash_offer, profit_estimate."
            )
            completion = openai.ChatCompletion.create(
                model="gpt-5",  # or "gpt-4-turbo" if unavailable
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
            )
            text = completion.choices[0].message["content"]

            # Basic fallback parser (you could structure via JSON mode for accuracy)
            return {"address": request.address, "analysis": text}
        else:
            # === Simulated values if no OpenAI key found ===
            arv = random.randint(150000, 350000)
            repair_cost = random.randint(15000, 50000)
            cash_offer = arv - repair_cost - random.randint(10000, 30000)
            profit = arv - (repair_cost + cash_offer)
            return {
                "address": request.address,
                "arv": arv,
                "repair_cost": repair_cost,
                "cash_offer": cash_offer,
                "profit_estimate": profit,
            }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error running analysis: {e}")

@router.get("/status")
def status_check():
    """Simple health check endpoint."""
    return {"status": "analysis service active"}