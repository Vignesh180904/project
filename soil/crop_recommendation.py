# crop_recommendation.py – Used by app.py to predict crop

import joblib
import numpy as np

# Load the trained crop model
model = joblib.load("crop_model.pkl")

def recommend_crop(data):
    features = np.array([[
        data["N"], data["P"], data["K"],
        data["temperature"], data["humidity"],
        data["ph"], data["rainfall"]
    ]])
    crop = model.predict(features)[0]
    return crop
