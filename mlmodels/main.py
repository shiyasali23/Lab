import os
import joblib
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Load models
models = {}
base_model_dir = './models'  

model_files = {
    'diabetes': 'diabetis_predictor.pkl',
    'liver_condition': 'liver_condition_predictor.pkl',
    'disease': 'disease_predictor.pkl'
}

for model_name, model_filename in model_files.items():
    try:
        model_path = os.path.join(base_model_dir, model_filename)
        models[model_name] = joblib.load(model_path)
        logger.info(f"{model_name} model loaded successfully from {model_path}.")
    except Exception as e:
        logger.error(f"Failed to load {model_name} model: {e}")
        raise RuntimeError(f"Failed to load model: {e}")

# Define input models
class DiabetesInput(BaseModel):
    features: List[float]

class LiverConditionInput(BaseModel):
    features: List[float]

class DiseaseInput(BaseModel):
    features: List[float]

# Prediction endpoint for diabetes
@app.post(f"/predict/diabetes", status_code=200)
def predict_diabetes(data: DiabetesInput):
    try:
        input_data = np.array([data.features], dtype=float)
        prediction = models['diabetes'].predict(input_data)
        probabilities = models['diabetes'].predict_proba(input_data)

        return {
            "prediction": int(prediction[0]),  # Convert to int
            'probabilities': probabilities[0].tolist()  # Convert to list
        }

    except ValueError as e:
        logger.error(f"Value error: {e}")
        raise HTTPException(status_code=422, detail=f"Value error: {e}")

# Prediction endpoint for liver condition
@app.post(f"/predict/liver_condition", status_code=200)
def predict_liver_condition(data: LiverConditionInput):
    try:
        input_data = np.array([data.features], dtype=float)
        prediction = models['liver_condition'].predict(input_data)
        probabilities = models['liver_condition'].predict_proba(input_data)

        return {
            "prediction": int(prediction[0]),  # Convert to int
            'probabilities': probabilities[0].tolist()  # Convert to list
        }

    except ValueError as e:
        logger.error(f"Value error: {e}")
        raise HTTPException(status_code=422, detail=f"Value error: {e}")

# Prediction endpoint for disease
@app.post(f"/predict/disease", status_code=200)
def predict_disease(data: DiseaseInput):
    try:
        input_data = np.array([data.features], dtype=float)
        prediction = models['disease'].predict(input_data)
        probabilities = models['disease'].predict_proba(input_data)

        return {
            "prediction": int(prediction[0]),  # Convert to int
            'probabilities': probabilities[0].tolist()  # Convert to list
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
                'id': metadata.get('id', None),
                'name': metadata.get('name', None),
                'version': metadata.get('version', None),
                'algorithm': metadata.get('algorithm', None),
                'framework': metadata.get('framework', None),
                'accuracy': metadata.get('accuracy', None),
                'precision': metadata.get('precision', None),
                'recall': metadata.get('recall'),
                'feature_names': metadata.get('feature_names', None),
                'feature_impacts': metadata.get('feature_impacts', None),
                'feature_maps': metadata.get('feature_maps', None),
                'output_maps': metadata.get('output_maps', None),
                'hyperparameters': metadata.get('hyperparameters', None)
            }
            models_metadata.append(model_data)
        except Exception as e:
            logger.error(f"Failed to process model {model_name}: {e}")
            raise HTTPException(status_code=422, detail=f"Value error: {e}")

    return models_metadata
