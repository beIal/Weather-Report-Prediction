from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel 
from model import load_model, predict_weather 
from schemas import weatherInput

app = FastAPI() 

model = load_model() 

async def get_prediction(input_data, WeatherInput): 
    try:  
        # Validate and predict
        prediction = predict_weather(model, input_data)
        return {"prediction": prediction}
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))