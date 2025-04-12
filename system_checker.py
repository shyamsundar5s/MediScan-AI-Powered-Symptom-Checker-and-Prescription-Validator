from fastapi import APIRouter
import pickle
from app.utils.nlp import process_symptoms

router = APIRouter()

# Load the pre-trained model
model_path = "ml-models/symptom_checker_model/model.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

@router.post("/")
async def analyze_symptoms(symptoms: str):
    processed_symptoms = process_symptoms(symptoms)
    prediction = model.predict([processed_symptoms])
    return {"possible_conditions": prediction}
