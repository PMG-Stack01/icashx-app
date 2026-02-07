from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.database import Base


class Buyer(Base):
    """
    Database model representing a cash buyer or real estate investor.
    This stores details for matching properties and managing contacts.
    """
    __tablename__ = "buyers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, index=True)
    phone = Column(String(20), nullable=True)
    company = Column(String(100), nullable=True)
    location = Column(String(120), nullable=True)  # City or Metro Area
    state = Column(String(50), nullable=True)
    max_budget = Column(Float, nullable=False, default=0.0)
    property_types = Column(String(200), nullable=True)  # e.g., "single_family, duplex"
    investment_strategy = Column(String(100), nullable=True)  # fix_and_flip, rental, etc.
    notes = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return (
            f"<Buyer(id={self.id}, name='{self.name}', email='{self.email}', "
            f"location='{self.location}', max_budget={self.max_budget})>"
        )