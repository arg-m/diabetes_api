from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from .database import Base

class Risk(Base):
    __tablename__ = "risks"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    bmi = Column(Float, nullable=False)
    glucose = Column(Float, nullable=False)
    activity_level = Column(Integer, nullable=False)
    risk_score = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)