from sqlalchemy import Column, Integer, String, Enum
from app.database import Base

class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    address = Column(String)
    status = Column(Enum("new", "analyzing", "offer_sent", "contract_signed", name="lead_status"))