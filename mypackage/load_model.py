import os
import joblib

def load_model():
    """Load and return the model."""

    dir_path = os.path.dirname(__file__) 
    model_path = os.path.join(dir_path, 'data', 'model.pkl')
    
    model = joblib.load(model_path)
    return model