from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

class Property(Base):
    __tablename__ = "properties"
    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id"))
    address = Column(String)
    bedrooms = Column(Integer)
    bathrooms = Column(Float)
    arv = Column(Float)
    repair_cost = Column(Float)
    cash_offer = Column(Float)
    profit_estimate = Column(Float)