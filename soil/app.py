import os
import numpy as np
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Import your custom modules
from soil_analysis import analyze_soil
from crop_recommendation import recommend_crop
from weather_forecast import get_weather_forecast

# Flask setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Load leaf disease model
model = load_model('model/leaf_disease_model.h5')
class_labels = ['Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___healthy']

# ---------------------------
# ROUTE: Home Page
# ---------------------------
@app.route("/")
def home():
    return render_template("home.html")

# ---------------------------
# ROUTE: Leaf Disease Detection
# ---------------------------
@app.route('/index', methods=['GET', 'POST'])
def leaf_disease():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)

            img = load_img(path, target_size=(128, 128))
            img_array = img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            prediction = model.predict(img_array)[0]
            index = np.argmax(prediction)
            disease = class_labels[index]
            confidence = round(100 * prediction[index], 2)

            tips = {
                "Tomato___Bacterial_spot": "Use copper-based bactericides and rotate crops.",
                "Tomato___Early_blight": "Remove infected leaves and apply fungicides.",
                "Tomato___healthy": "Your plant looks healthy!",
            }

            return render_template("index.html", disease=disease, confidence=confidence, tip=tips.get(disease, "No tip available."))
    return render_template("index.html")

# ---------------------------
# ROUTE: Soil Suitability Checker
# ---------------------------
@app.route("/suggestion", methods=["GET", "POST"])
def suggestion():
    if request.method == "POST":
        data = {
            "plant": request.form["plant"],
            "N": float(request.form["nitrogen"]),
            "P": float(request.form["phosphorus"]),
            "K": float(request.form["potassium"]),
            "temperature": float(request.form["temperature"]),
            "humidity": float(request.form["humidity"]),
            "ph": float(request.form["ph"])
        }
        viability, recommendations = analyze_soil(data)
        return render_template("suggestion.html", plant=data["plant"], viability=viability, recommendations=recommendations)
    return render_template("suggestion.html")

# ---------------------------
# ROUTE: Crop Recommendation
# ---------------------------
@app.route("/recommendation", methods=["GET", "POST"])
def recommendation():
    if request.method == "POST":
        data = {
            "N": float(request.form["nitrogen"]),
            "P": float(request.form["phosphorus"]),
            "K": float(request.form["potassium"]),
            "temperature": float(request.form["temperature"]),
            "humidity": float(request.form["humidity"]),
            "ph": float(request.form["ph"]),
            "rainfall": float(request.form["rainfall"])
        }
        crop = recommend_crop(data)
        return render_template("recommendation.html", crop=crop)
    return render_template("recommendation.html")

# ---------------------------
# ROUTE: Weather Forecast
# ---------------------------
@app.route("/weather", methods=["GET", "POST"])
def weather():
    if request.method == "POST":
        location = request.form["location"]
        forecast = get_weather_forecast(location)
        return render_template("weather.html", location=location, forecast=forecast)
    return render_template("weather.html")

# ---------------------------
# Run Flask App
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
