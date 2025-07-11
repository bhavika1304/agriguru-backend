from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from services.crop import get_crop_recommendation
from services.weather import get_weather
# from services.market import get_market_price
# from services.disease import detect_disease
# from services.assistant import process_query

app = FastAPI()

class CropInput(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

@app.get("/")
def root():
    return {"status": "AgriGuru backend running"}

@app.post("/recommend_crop")
def recommend_crop(data: CropInput):
    print(data)
    return get_crop_recommendation(data.dict())

@app.get("/weather")
def weather(city: str):
    return get_weather(city)

"""
@app.get("/market_price")
def market_price(crop: str):
    return get_market_price(crop)

@app.post("/detect_disease")
async def detect(file: UploadFile = File(...)):
    return await detect_disease(file)

@app.post("/assistant")
def assistant(data: dict):
    return process_query(data["text"], data["language"])
"""
