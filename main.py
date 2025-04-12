from fastapi import FastAPI
from app.routers import symptom_checker, prescription_validator, chatbot, doctor_connect

app = FastAPI(
    title="MediScan API",
    description="An API for AI-Powered Symptom Checker and Prescription Validator",
    version="1.0.0"
)

# Include routers
app.include_router(symptom_checker.router, prefix="/symptom-checker", tags=["Symptom Checker"])
app.include_router(prescription_validator.router, prefix="/prescription-validator", tags=["Prescription Validator"])
app.include_router(chatbot.router, prefix="/chatbot", tags=["Chatbot"])
app.include_router(doctor_connect.router, prefix="/doctor-connect", tags=["Doctor Connect"])

@app.get("/")
def root():
    return {"message": "Welcome to MediScan API"}
