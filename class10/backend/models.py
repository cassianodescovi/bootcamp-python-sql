from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy import func
from database import Base

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    categoria = Column(String)
    email_seller = Column(String, default="americanas@contato.com")
    created_at = Column(DateTime(timezone=True), default=func.now())