from fastapi import FastAPI
from pydantic import BaseModel
import joblib, os, numpy as np

app = FastAPI()

model = None
label_encoder = None

class CropInput(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

@app.post("/recommend_crop")
def recommend_crop(data: CropInput):
    global model, label_encoder
    if model is None or label_encoder is None:
        model = joblib.load("models/crop_model.pkl")
        label_encoder = joblib.load("models/label_encoder.pkl")

    X = np.array([[data.N, data.P, data.K, data.temperature, data.humidity, data.ph, data.rainfall]])
    crop = model.predict(X)
    name = label_encoder.inverse_transform(crop)[0]
    return {"recommended_crop": name}

@app.get("/")
def ping():
    return {"status": "Running"}
