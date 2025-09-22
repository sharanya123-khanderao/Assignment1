import requests
from utils import REQUEST_TIMEOUT, GEO_API

def get_Geolocation(city, country_code):
    loc_url = f"{GEO_API}?name={city}&country={country_code}&count=1"
    response = requests.get(loc_url, timeout=REQUEST_TIMEOUT)
    data = response.json()
    if data.get("results"):
        location = data["results"][0]
        return {"latitude": location.get("latitude"), "longitude": location.get("longitude")}
    else:
        return None
