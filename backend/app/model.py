import pickle 

def load_model(): 
    # Updates paths to find point to the picke files 
    classifcation_model_path = r"C:\Users\cucum\Downloads\COS30049\assignment 2\classification_model.pkl" 
    regression_model_path = r"C:\Users\cucum\Downloads\COS30049\assignment 2\regression_model.pk1"  
    
    # Load Models
    classification_model = pickle.load(open(classifcation_model_path, 'rb')) 
    regression_model = pickle.load(open(regression_model_path, 'rb'))  
    
    return classification_model, regression_model 

def predict(model, data, model_type): 
    if model_type == 'classification':
        return model.predict(data)[0]
    elif model_type == 'regression':
        return model.predict(data)[0]