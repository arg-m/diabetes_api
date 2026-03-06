from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, get_db
from .models import Base, Risk
from .schemas import RiskCreate, RiskResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Diabetes Risk API",
    version="1.0.0",
    description="API for calculating diabetes risk",
)


@app.get("/ping")
def ping():
    return {"message": "API is working"}

@app.post("/risk", response_model=RiskResponse)
def create_risk(risk_in: RiskCreate, db: Session=Depends(get_db)):
    risk_score = calculate_risk(risk_in.age, risk_in.bmi, risk_in.glucose)

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

# заменить на ml модель
def calculate_risk(age: int, bmi: float, glucose: float) -> float:
    risk = 0.3 * bmi + 0.5 * glucose + 0.2 * age
    return min(risk / 100, 1.00)
