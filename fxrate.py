import os
import requests
from utils import REQUEST_TIMEOUT, FX_API

FX_API_KEY = os.getenv("FX_API_KEY", "").strip()

def get_fx_conversion(from_currency, amount):
    if from_currency.upper() == 'USD':
        return {"fx_rate_to_usd": 1.0, "amount_usd": float(amount)}
        
    fx_url = f"https://api.exchangerate.host/convert?from={from_currency}&to=USD&amount={amount}&access_key={FX_API_KEY}"
    response = requests.get(fx_url)
    data = response.json()
    if data.get('success'):
        rate = None
        if 'info' in data and isinstance(data['info'], dict) and 'quote' in data['info']:
            rate = data['info']['quote']
        
        return {
            "amount_usd": data.get('result'),
            "fx_rate_to_usd": rate
        }
    else:
        return None