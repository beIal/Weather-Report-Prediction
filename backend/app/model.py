import pickle 

def load_model(): 
    classifcation_model_path = r"C:\Users\cucum\Downloads\COS30049\assignment 2\Classification.py" 
    regression_model_path = r"C:\Users\cucum\Downloads\COS30049\assignment 2\Regression.py"  
    classification_model = pickle.load(open(classifcation_model_path, 'rb')) 
    regression_model = pickle.load(open(regression_model_path, 'rb')) 
    return classification_model, regression_model 

def predict(model, data, model_type): 
    if model_type == 'classification':
        return model.predict(data)[0]
    elif model_type == 'regression':
        return model.predict(data)[0]