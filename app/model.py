import joblib
import pandas as pd
import numpy as np
from pydantic import BaseModel
from pathlib import Path

# This is the path *inside* the Docker container
MODEL_PATH = Path("/app/model/housing_model.pkl")

# Define the input data schema using Pydantic
# This ensures we get valid data types
class HousingFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

    # This is an example for the API docs
    class Config:
        json_schema_extra = {
            "example": {
                "MedInc": 8.3252,
                "HouseAge": 41.0,
                "AveRooms": 6.984127,
                "AveBedrms": 1.02381,
                "Population": 322.0,
                "AveOccup": 2.555556,
                "Latitude": 37.88,
                "Longitude": -122.23
            }
        }

class Model:
    def __init__(self, model_path: Path):
        self.model = joblib.load(model_path)

    def predict(self, features: HousingFeatures) -> float:
        # 1. Convert Pydantic model to DataFrame
        data_df = pd.DataFrame([features.model_dump()])
        
        # 2. Make prediction (returns a numpy array)
        prediction_array = self.model.predict(data_df)
        
        # 3. Extract the single prediction
        prediction = prediction_array[0]
        
        return float(prediction)

# Load the model once when the app starts
# This is efficient; we don't reload it for every request
try:
    model = Model(MODEL_PATH)
except FileNotFoundError:
    print(f"Warning: Model file not found at {MODEL_PATH}")
    model = None

def get_model():
    return model