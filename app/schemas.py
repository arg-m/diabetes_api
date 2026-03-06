from pydantic import BaseModel

class RiskCreate(BaseModel):
    age: int
    bmi: float
    glucose: float

class RiskResponse(BaseModel):
    id: int
    age: int
    bmi: float
    glucose: float
    risk_score: float

    class Config:
        from_attributes = True