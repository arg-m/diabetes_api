from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..schemas import RiskCreate, RiskResponse
from .. import services

router = APIRouter(tags=["risk"])

@router.post("/risk", response_model=RiskResponse)
def create_risk_endpoint(risk_in: RiskCreate, db: Session = Depends(get_db)):
    return services.create_risk_service(db, risk_in)

@router.get("/risk/{risk_id}", response_model=RiskResponse)
def get_risk_endpoint(risk_id: int, db: Session = Depends(get_db)):
    risk = services.get_risk_service(db, risk_id)
    if not risk:
        raise HTTPException(status_code=404, detail="Risk not found")
    return risk

@router.get("/risks", response_model=List[RiskResponse])
def list_risks(db: Session = Depends(get_db)):
    return services.get_risks_service(db)