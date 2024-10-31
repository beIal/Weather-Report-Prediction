from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel 
from model import load_model, predict
import pandas as pd

app = FastAPI() 

model = load_model()  

classification_model, regression_model = load_model()

class predictionInput(BaseModel): 
    temperature: float 
    humidity: float
 
@app.post("/predict/classification")
async def classify(input_data, predictionInput): 
    try:  
        data = [[input_data.temperature, input_data.humidity]]
        prediction = predict(classification_model, input_data, model_type='classification')
        return {"prediction": prediction}
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e)) 
    
@app.post("/predict/regression")
async def classify(input_data, predictionInput): 
    try:  
        data = [[input_data.temperature, input_data.humidity]]
        prediction = predict(classification_model, input_data, model_type='regression')
        return {"prediction": prediction}
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))