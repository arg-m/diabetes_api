from fastapi import FastAPI
from .database import engine
from .models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Diabetes Risk API",
    version="1.0.0",
    description="API for calculating diabetes risk"
)

@app.get("/ping")
def ping():
    return {"message": "API is working"}