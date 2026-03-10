from pydantic import BaseModel, Field

class RiskCreate(BaseModel):
    age: int = Field(..., ge=0, le=120)
    bmi: float = Field(..., ge=10, le=60)
    glucose: float = Field(..., ge=50, le=400)

class RiskResponse(BaseModel):
    id: int
    age: int
    bmi: float
    glucose: float
    risk_score: float

    class Config:
        from_attributes = True