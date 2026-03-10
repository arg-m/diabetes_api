from sqlalchemy.orm import Session
from .schemas import RiskCreate
from . import crud
from .ml_model import calculate_risk

def create_risk_service(db: Session, risk_in: RiskCreate):
    risk_score = calculate_risk(risk_in.age, risk_in.bmi, risk_in.glucose)
    return crud.create_risk(db, risk_in, risk_score)

def get_risk_service(db: Session, risk_id: int):
    return crud.get_risk(db, risk_id)

def get_risks_service(db: Session):
    return crud.get_risks(db)