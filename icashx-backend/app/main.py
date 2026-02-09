from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import leads, properties, analysis, communications, contracts, buyers

from app import models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="iCashX Backend", version="1.0")


# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(leads.router, prefix="/api/leads", tags=["Leads"])
app.include_router(properties.router, prefix="/api/properties", tags=["Properties"])
app.include_router(analysis.router, prefix="/api/analysis", tags=["Analysis"])
app.include_router(communications.router, prefix="/api/communications", tags=["Communications"])
app.include_router(contracts.router, prefix="/api/contracts", tags=["Contracts"])
app.include_router(buyers.router, prefix="/api/buyers", tags=["Buyers"])

@app.get("/")
async def root():
    return {"message": "Welcome to iCashX Backend API"}