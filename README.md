# MediScan-AI-Powered-Symptom-Checker-and-Prescription-Validator
MediScan is an innovative AI-powered solution designed to assist patients and pharmacists in under-resourced areas. It helps users understand their symptoms, verify prescriptions, and improve healthcare access and accuracy through cutting-edge technology.

## Features
### 1. AI Symptom Checker
- **Input:** User-entered symptoms in natural language.
- **Output:**
  - Possible medical conditions.
  - Urgency level (e.g., emergency, see GP, treat at home).
  - Recommended actions.
- **Tech:** Trained on datasets like MedQuAD or SymCAT using NLP models (spaCy, Hugging Face Transformers).

### 2. Prescription Validator
- **Input:** Upload a handwritten prescription image.
- **Output:**
  - Medicine correctness based on symptoms/conditions.
  - Dosage safety verification.
  - Drug interaction checks using databases like DrugBank.
- **Tech:** OCR (Tesseract or Google Vision API) + ML models.

### 3. Multilingual Chatbot Interface
- Conversational AI in English, Hindi, and Marathi.
- Voice support using Google Speech-to-Text and TTS for better accessibility.

### 4. Doctor Connect (Optional)
- Integrated video call functionality for high-risk cases to connect with certified doctors.

### Bonus Features
- PDF export of analyzed prescriptions.
- Health record storage for follow-ups.
- Medication reminders via SMS (Twilio).

## Tech Stack
### Frontend
- **Frameworks:** React.js / Flutter (web and mobile compatibility)
- **Hosting:** Vercel

### Backend
- **Frameworks:** FastAPI / Flask
- **Hosting:** Render / Railway.app
- **Database:** Firebase / PostgreSQL

### AI & Machine Learning
- **Symptom Checker:** Trained NLP models (e.g., Hugging Face Transformers).
- **Prescription Validator:** OCR (Tesseract) + ML models.
- **Drug Interactions:** DrugBank database integration.

### Deployment
- **Frontend:** Vercel
- **Backend:** Render or full-stack deployment on Railway.app
- **ML Model Hosting:** Hugging Face Spaces or AWS SageMaker

## How to Run Locally
### Prerequisites
- Node.js and npm (for frontend)
- Python 3.8+ (for backend)
- PostgreSQL or Firebase (for database)
- Tesseract OCR installed locally (for prescription validation)
### Clone the Repository
```bash
git clone https://github.com/codebyjyotsna/MediScan.git
cd MediScan
```
### Start Backend
1. Navigate to the backend folder:
   ```bash
   cd backend
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv env
   source env/bin/activate  # For Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run the backend:
   ```bash
   uvicorn app.main:app --reload
   ```
### Start Frontend
1. Navigate to the frontend folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the frontend:
   ```bash
   npm start
   ```
### Access the Application
- Frontend: `http://localhost:3000/`
- Backend: `http://localhost:8000/`

## Datasets Used
- **MedQuAD**: For symptom and condition mapping.
- **SymCAT**: Symptom analysis and conditions.
- **DrugBank**: Drug interaction and safety checks.

## Future Enhancements
- Expand chatbot support to additional regional languages.
- Improve ML model accuracy with larger datasets.
- Integrate medication refill tracking and reminders.
- Add blockchain-based health record storage for security.

