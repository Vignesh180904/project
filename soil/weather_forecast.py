import datetime
import random
def get_weather_forecast(location):
    today = datetime.date.today()
    forecast = []
    for i in range(3):  
        forecast_date = today + datetime.timedelta(days=i)
        date_str = forecast_date.strftime("%d-%m-%Y")
        month = forecast_date.month
        base_rainfall = {
            1: 5, 2: 7, 3: 15, 4: 20, 5: 35, 6: 75,
            7: 120, 8: 130, 9: 90, 10: 60, 11: 40, 12: 20
        }.get(month, 20)
        rain = round(base_rainfall + random.uniform(-10, 10), 2)
        temp = random.randint(24, 32)
        forecast.append({
            "date": date_str,
            "rainfall": f"{rain} mm",
            "temperature": f"{temp}°C"
        })
    return forecast