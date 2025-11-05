from fastapi import FastAPI, Depends, HTTPException
from .model import HousingFeatures, Model, get_model

app = FastAPI(
    title="California Housing Price Predictor",
    description="A pro-level API to predict housing prices, built with Docker and FastAPI.",
    version="0.1.0"
)

@app.on_event("startup")
async def startup_event():
    # Simple check to make sure model is loaded on startup
    if get_model() is None:
        raise RuntimeError("Model could not be loaded. Exiting.")

@app.get("/")
async def root():
    return {"message": "Welcome. Go to /docs for the API documentation."}

@app.post("/predict/")
async def predict_price(
    features: HousingFeatures, 
    model: Model = Depends(get_model)
):
    """
    Predict the median house value for a district based on its features.
    """
    if model is None:
         raise HTTPException(
            status_code=500, 
            detail="Model is not loaded. Please check server logs."
        )
            
    try:
        # Get prediction from our model logic
        prediction = model.predict(features)
        return {"predicted_median_house_value": prediction}
    except Exception as e:
        # Catch any errors during prediction
        raise HTTPException(
            status_code=500, 
            detail=f"Error during prediction: {str(e)}"
        )
        