import pickle 

def load_model(): 
    with open('path/to/your/model.pkl', 'rb') as f: 
        model = pickle.load(f) 
    return model 

def predict_weather(model, input_data): 
    input_values = [[input_data.temperature, input_data.humidity]] 
    prediction = model.predict(input_values) 
    return prediction[0]