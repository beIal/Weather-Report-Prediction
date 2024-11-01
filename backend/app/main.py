from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .model import load_model, predict
import pandas as pd

app = FastAPI()

# Load models
classification_model, regression_model = load_model()

# Define input data schema
class PredictionInput(BaseModel):
    temperature: float
    humidity: float

@app.post("/predict/classification")
async def classify(input_data: PredictionInput):
    try:
        # Prepare data for prediction
        data = [[input_data.temperature, input_data.humidity]]
        # Call the predict function with the classification model
        prediction = predict(classification_model, data, model_type='classification')
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict/regression")
async def regress(input_data: PredictionInput):
    try:
        # Prepare data for prediction
        data = [[input_data.temperature, input_data.humidity]]
        # Call the predict function with the regression model
        prediction = predict(regression_model, data, model_type='regression')
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
