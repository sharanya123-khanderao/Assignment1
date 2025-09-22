import csv, json
from geolocation import get_Geolocation
from weather import get_weather
from fxrate import get_fx_conversion
from utils import get_timestamp

input_file = "expenses.csv"
output_file = "enriched_expenses.json"

results = []

with open(input_file, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        city = row["city"]
        country_code = row["country_code"]
        local_currency = row["local_currency"]
        amount_local = row["amount"]

        location = get_Geolocation(city, country_code)
        weather = get_weather(location["latitude"], location["longitude"]) if location else {}
        fx = get_fx_conversion(local_currency, amount_local)

        enriched = {
            "city": city,
            "country_code": country_code,
            "local_currency": local_currency,
            "amount_local": float(amount_local),
            "fx_rate_to_usd": fx["fx_rate_to_usd"] if fx else None,
            "amount_usd": fx["amount_usd"] if fx else None,
            "latitude": location["latitude"] if location else None,
            "longitude": location["longitude"] if location else None,
            "temperature_c": weather["temperature_c"] if weather else None,
            "wind_speed_mps": weather["wind_speed_mps"] if weather else None,
            "retrieved_at": get_timestamp()
        }

        results.append(enriched)

with open(output_file, "w", encoding="utf-8") as jsonfile:
    json.dump(results, jsonfile, indent=4)
