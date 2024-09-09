import os
import joblib
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import json
import numpy as np


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
        # Prepare the input data as a 2D array
        input_data = np.array([[
            data.gender,
            data.age,
            data.blood_urea_nitrogen,
            data.creatinine,
            data.hemoglobin_a1c,
            data.total_cholesterol,
            data.triglycerides,
            data.hdl_cholesterol,
            data.ldl_cholesterol,
            data.vldl,
            data.bmi
        ]])

        # Make the prediction using the loaded model
        prediction = models['diabetes']['model'].predict(input_data)
        probabilities = models['diabetes']['model'].predict_proba(input_data)

        # Return the prediction and probabilities
        return {
            "prediction": 'Positive' if prediction[0] == 1 else 'Negative',
            'probabilities': probabilities[0].tolist()  # Convert to list for JSON serialization
        }

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
        # Prepare the input data as a 2D array
        input_data = np.array([[
            data.age,
            data.gender,
            data.albumin,
            data.alkaline_phosphatase,
            data.alanine_aminotransferase,
            data.aspartate_aminotransferase,
            data.bilirubin,
            data.cholinesterase,
            data.total_cholesterol,
            data.creatinine,
            data.gamma_glutamyl_transferase,
            data.total_protein
        ]])

        # Make the prediction using the loaded model
        prediction = models['liver_condition']['model'].predict(input_data)
        probabilities = models['liver_condition']['model'].predict_proba(input_data)

        # Return the prediction and probabilities
        return {
            "prediction": 'Healthy' if prediction[0] == 0 
                        else 'Hepatitis' if prediction[0] == 1 
                        else 'Fibrosis' if prediction[0] == 2 
                        else 'Cirrhosis' if prediction[0] == 3 
                        else 'Error',
            'probabilities': probabilities[0].tolist()  # Convert to list for JSON serialization
        }

    except ValueError as e:
        logger.error(f"Value error: {e}")
        raise HTTPException(status_code=422, detail=f"Value error: {e}")
 

@app.get("/register_models/", status_code=200)
def register_models():
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
                'accuracy': metadata.get('accuracy'),
                'precision': metadata.get('precision'),
                'recall': metadata.get('recall'),
                'feature_names': metadata.get('feature_names'),
                'feature_impacts': metadata.get('feature_impacts'),
                'feature_maps': metadata.get('feature_maps'),
                'output_maps': metadata.get('output_maps'),
                'hyperparameters': metadata.get('hyperparameters')
            }
            models_metadata.append(model_data)
        except Exception as e:
            logger.error(f"Failed to process model {model_name}: {e}")
            raise HTTPException(status_code=422, detail=f"Value error: {e}")

    return models_metadata