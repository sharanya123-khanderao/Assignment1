import requests
from utils import REQUEST_TIMEOUT, WEATHER_API

def get_weather(latitude, longitude):
    if latitude is None or longitude is None:
        return None
    weather_url = f"{WEATHER_API}?latitude={latitude}&longitude={longitude}&current_weather=true&windspeed_unit=ms"
    response = requests.get(weather_url, timeout=REQUEST_TIMEOUT)
    data = response.json()
    if data.get("current_weather"):
        cw = data["current_weather"]
        return {
            "temperature_c": cw.get("temperature"),
            "wind_speed_mps": cw.get("windspeed")
        }
    else:
        return None
