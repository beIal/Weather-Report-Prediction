from pydantic import BaseModel 

class weatherInput(BaseModel): 
    temperature: float
    humidity: float