
from flask import Flask, render_template, request
from soil_analysis import analyze_soil
from crop_recommendation import recommend_crop
from weather_forecast import get_weather_forecast

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

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

@app.route("/weather", methods=["GET", "POST"])
def weather():
    if request.method == "POST":
        location = request.form["location"]
        forecast = get_weather_forecast(location)
        return render_template("weather.html", location=location, forecast=forecast)
    return render_template("weather.html")

if __name__ == "__main__":
    app.run(debug=True)
