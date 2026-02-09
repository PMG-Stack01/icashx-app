from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.database import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String)
    address = Column(String)
    status = Column(String, default="new")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Buyer(Base):
    __tablename__ = "buyers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    budget = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    property_address = Column(String)
    buyer_id = Column(Integer, ForeignKey("buyers.id"))
    price = Column(Float)
    status = Column(String, default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    buyer = relationship("Buyer")