from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import numpy as np
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and encoders
with open("backend/model/branch_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("backend/model/caste_encoder.pkl", "rb") as f:
    caste_encoder = pickle.load(f)
with open("backend/model/branch_encoder.pkl", "rb") as f:
    branch_encoder = pickle.load(f)

# Input schema
class StudentData(BaseModel):
    tenth_cgpa: float
    puc_cgpa: float
    caste: str  # General, OBC, SC, ST

# Predict route
@app.post("/predict_branch")
def predict_branch(data: StudentData):
    try:
        caste_encoded = caste_encoder.transform([data.caste])[0]
    except ValueError:
        return {"error": "Invalid caste. Choose from General, OBC, SC, ST."}

    features = np.array([[data.tenth_cgpa, data.puc_cgpa, caste_encoded]])
    pred = model.predict(features)[0]
    branch = branch_encoder.inverse_transform([pred])[0]

    return {"predicted_branch": branch}
