import os
import joblib
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Load models
models = {}
model_files = {
    'diabetes': './models/diabetis_predictor.pkl',
    'liver_condition': './models/liver_condition_predictor.pkl'
}

for model_name, model_path in model_files.items():
    try:
        models[model_name] = joblib.load(model_path)
        logger.info(f"{model_name} model loaded successfully.")
    except Exception as e:
        logger.error(f"Failed to load {model_name} model: {e}")
        raise RuntimeError(f"Failed to load model: {e}")

class DiabetesInput(BaseModel):
    gender: float
    age: float
    blood_urea_nitrogen: float
    creatinine: float
    hemoglobin_a1c: float
    total_cholesterol: float
    triglycerides: float
    hdl_cholesterol: float
    ldl_cholesterol: float
    vldl: float
    bmi: float

@app.post("/diabetes/", status_code=200)
def predict_diabetes(data: DiabetesInput):
    try:
        input_data = {
            'Gender': data.gender,
            'AGE': data.age,
            'Blood Urea Nitrogen': data.blood_urea_nitrogen,
            'Creatinine': data.creatinine,
            'Hemoglobin A1c': data.hemoglobin_a1c,
            'Total Cholesterol': data.total_cholesterol,
            'Triglycerides': data.triglycerides,
            'HDL Cholesterol': data.hdl_cholesterol,
            'LDL Cholesterol': data.ldl_cholesterol,
            'Very Low-Density Lipoprotein': data.vldl,
            'BMI': data.bmi
        }
        
        prediction = models['diabetes']['model'].predict(input_data)
        probabilities = models['diabetes']['model'].predict_proba(input_data)
        return {"prediction": 'Positive' if prediction[0] == 1 else 'Negative',
                'probabilities': probabilities[0]}
    
    except ValueError as e:
        logger.error(f"Value error: {e}")
        raise HTTPException(status_code=422, detail=f"Value error: {e}")


class LiverConditionInput(BaseModel):
    age: float
    gender: float
    albumin: float
    alkaline_phosphatase: float
    alanine_aminotransferase: float
    aspartate_aminotransferase: float
    bilirubin: float
    cholinesterase: float
    total_cholesterol: float
    creatinine: float
    gamma_glutamyl_transferase: float
    total_protein: float

@app.post("/liver_condition/", status_code=200)
def predict_liver_condition(data: LiverConditionInput):
    try:
        input_data = {
            'Age': data.age,
            'Gender': data.gender,
            'Albumin': data.albumin,
            'Alkaline Phosphatase': data.alkaline_phosphatase,
            'Alanine Aminotransferase': data.alanine_aminotransferase,
            'Aspartate Aminotransferase': data.aspartate_aminotransferase,
            'Bilirubin': data.bilirubin,
            'Cholinesterase': data.cholinesterase,
            'Total Cholesterol': data.total_cholesterol,
            'Creatinine': data.creatinine,
            'Gamma-Glutamyl Transferase': data.gamma_glutamyl_transferase,
            'Total Protein': data.total_protein
        }
        
        prediction = models['liver_condition']['model'].predict(input_data)
        probabilities = models['liver_condition']['model'].predict_proba(input_data)
        
        return {
            "prediction": 'Healthy' if prediction[0] == 0 
                        else 'Hepatitis' if prediction[0] == 1 
                        else 'Fibrosis' if prediction[0] == 2 
                        else 'Cirrhosis' if prediction[0] == 3 
                        else 'Error',
            'probabilities': probabilities[0]
        }
    
    except ValueError as e:
        logger.error(f"Value error: {e}")
        raise HTTPException(status_code=422, detail=f"Value error: {e}")
    

@app.post("/register_models/", status_code=200)
def register_models():
    logger.info(request.data)
    models_metadata = []
    for model_name, model in models.items():
        try:
            metadata = model.get('metadata', {})           
            model_data = {
                'id': metadata.get('id'),
                'name': metadata.get('name'),
                'version': metadata.get('version'),
                'algorithm': metadata.get('algorithm'),
                'framework': metadata.get('framework'),
                'accuracy': metadata.get('Accuracy'),
                'precision': metadata.get('Precision'),
                'recall': metadata.get('Recall'),
                'f1_score': metadata.get('F1 Score'),
                'hyperparameters': json.dumps(model['model'].get_params())
            }
            models_metadata.append(model_data)
        except Exception as e:
            logger.error(f"Failed to process model {model_name}: {e}")
            continue

    return models_metadata
    


