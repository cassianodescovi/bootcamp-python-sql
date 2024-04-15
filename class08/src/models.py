from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from src.db import Base

class Pokemon(Base):
    __tablename__ = 'pokemons'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    weight = Column(Integer)
    created_at = Column(DateTime, default=func.now())