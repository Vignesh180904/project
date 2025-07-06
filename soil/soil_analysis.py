import joblib
import numpy as np

model = joblib.load("soil_model.pkl")

def analyze_soil(data):
    features = np.array([[
        data["N"], data["P"], data["K"],
        data["temperature"], data["humidity"], data["ph"]
    ]])
    viability = int(model.predict(features)[0])  # Now safe, returns numeric

    recs = []
    if data["N"] < 50:
        recs.append("Add nitrogen-rich fertilizer or compost.")
    if data["P"] < 50:
        recs.append("Add bone meal or rock phosphate.")
    if data["K"] < 50:
        recs.append("Add potash or banana peel compost.")
    if data["ph"] < 6.0:
        recs.append("Use lime to raise the soil pH.")
    elif data["ph"] > 7.5:
        recs.append("Add elemental sulfur to lower the pH.")

    return viability, recs
