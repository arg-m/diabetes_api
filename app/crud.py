from sqlalchemy.orm import Session
from .models import Risk
from .schemas import RiskCreate


def create_risk(db: Session, risk_in: RiskCreate, risk_score: float):
    db_risk = Risk(
        age=risk_in.age, 
        bmi=risk_in.bmi, 
        glucose = risk_in.glucose,
        activity_level=1,
        risk_score=risk_score)
    
    db.add(db_risk)
    db.commit()
    db.refresh(db_risk)

    return db_risk

def get_risk(db: Session, risk_id: int):
    return db.query(Risk).filter(Risk.id == risk_id).first()

def get_risks(db:Session):
    return db.query(Risk).all()