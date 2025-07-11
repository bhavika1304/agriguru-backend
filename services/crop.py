import joblib
import os
import numpy as np

model = None
label_encoder = None

def get_crop_recommendation(data: dict):
    global model, label_encoder

    if model is None or label_encoder is None:
        model = joblib.load(os.path.join("models", "crop_model.pkl"))
        label_encoder = joblib.load(os.path.join("models", "label_encoder.pkl"))

    input_data = [float(data.get(key, 0)) for key in ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    prediction = model.predict(np.array(input_data).reshape(1, -1))
    crop_label = label_encoder.inverse_transform(prediction)[0]

    return {"recommended_crop": crop_label}
