import json
import urllib.parse
import urllib.request

city = input("Enter city name: ").strip()

try:
    url = "https://geocoding-api.open-meteo.com/v1/search?" + urllib.parse.urlencode({
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    })

    with urllib.request.urlopen(url, timeout=20) as response:
        data = json.loads(response.read().decode())

    if not data.get("results"):
        print("City not found!")
    else:
        place = data["results"][0]
        lat = place["latitude"]
        lon = place["longitude"]

        weather_url = (
            "https://api.open-meteo.com/v1/forecast?"
            + urllib.parse.urlencode({
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m",
                "timezone": "auto"
            })
        )

        with urllib.request.urlopen(weather_url, timeout=20) as response:
            weather = json.loads(response.read().decode())["current"]

        print("\n--- WEATHER REPORT ---")
        print("City:", place["name"])
        print("Temperature:", weather["temperature_2m"], "°C")
        print("Feels like:", weather["apparent_temperature"], "°C")
        print("Humidity:", weather["relative_humidity_2m"], "%")
        print("Wind speed:", weather["wind_speed_10m"], "km/h")

except Exception as e:
    print("Unable to fetch weather data.")
    print("Error:", e)