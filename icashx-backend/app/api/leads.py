from fastapi import APIRouter

router = APIRouter(prefix="/leads", tags=["Leads"])

@router.get("/")
def get_leads():
    return {"message": "List of leads"}