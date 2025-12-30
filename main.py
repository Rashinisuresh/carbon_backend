from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UsageInput(BaseModel):
    usage: float

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.post("/calculate")
def calculate_carbon(data: UsageInput):
    emission_factor = 0.82
    carbon = data.usage * emission_factor

    return {
        "electricity_usage": data.usage,
        "carbon_emission": carbon,
        "unit": "kg CO2"
    }