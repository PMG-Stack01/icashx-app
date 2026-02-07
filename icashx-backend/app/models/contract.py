from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Contract(Base):
    """
    Database model representing a purchase contract for a property.
    This stores all essential data for agreements between sellers and buyers.
    """
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    seller_name = Column(String(150), nullable=False)
    seller_email = Column(String(150), nullable=True)
    buyer_id = Column(Integer, ForeignKey("buyers.id"), nullable=True)
    property_address = Column(String(255), nullable=False)
    legal_description = Column(Text, nullable=True)
    purchase_price = Column(Float, nullable=False)
    repair_cost = Column(Float, nullable=True)
    arv = Column(Float, nullable=True)  # After Repair Value
    closing_date = Column(DateTime(timezone=True), nullable=False)
    contract_status = Column(String(50), default="pending")  # e.g., pending, signed, cancelled
    contract_file_path = Column(String(300), nullable=True)  # path or cloud link to PDF/Docx
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    buyer = relationship("Buyer", backref="contracts")

    def __repr__(self):
        return (
            f"<Contract(id={self.id}, seller={self.seller_name}, "
            f"property='{self.property_address}', price={self.purchase_price})>"
        )