import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 10))
GEO_API = os.getenv("GEO_API")
WEATHER_API = os.getenv("WEATHER_API")
FX_API = os.getenv("FX_API")

def get_timestamp():
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
