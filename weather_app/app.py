from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# Using Open-Meteo API (no API key required)
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"
GEOCODING_API_URL = "https://geocoding-api.open-meteo.com/v1/search"


def get_coordinates(city_name):
    """Get latitude and longitude for a city"""
    try:
        params = {
            "name": city_name,
            "count": 1,
            "language": "en",
            "format": "json"
        }
        response = requests.get(GEOCODING_API_URL, params=params)
        data = response.json()
        
        if data.get("results"):
            result = data["results"][0]
            return {
                "latitude": result["latitude"],
                "longitude": result["longitude"],
                "city": result.get("name"),
                "country": result.get("country")
            }
        return None
    except Exception as e:
        print(f"Error getting coordinates: {e}")
        return None


def get_weather(latitude, longitude):
    """Fetch weather data for given coordinates"""
    try:
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m,pressure_msl",
            "timezone": "auto"
        }
        response = requests.get(WEATHER_API_URL, params=params)
        data = response.json()
        
        current = data.get("current", {})
        
        # Weather code interpretation
        weather_descriptions = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Foggy",
            48: "Foggy",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snow",
            73: "Moderate snow",
            75: "Heavy snow",
            80: "Slight rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",
            85: "Slight snow showers",
            86: "Heavy snow showers",
            95: "Thunderstorm",
            96: "Thunderstorm with slight hail",
            99: "Thunderstorm with heavy hail"
        }
        
        weather_code = current.get("weather_code", 0)
        
        return {
            "temperature": current.get("temperature_2m"),
            "humidity": current.get("relative_humidity_2m"),
            "weather_code": weather_code,
            "weather_description": weather_descriptions.get(weather_code, "Unknown"),
            "wind_speed": current.get("wind_speed_10m"),
            "pressure": current.get("pressure_msl"),
            "time": current.get("time")
        }
    except Exception as e:
        print(f"Error getting weather: {e}")
        return None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/weather", methods=["POST"])
def get_weather_data():
    """API endpoint to get weather data"""
    try:
        data = request.get_json()
        city = data.get("city", "London")
        
        # Get coordinates
        coords = get_coordinates(city)
        if not coords:
            return jsonify({"error": "City not found"}), 404
        
        # Get weather
        weather = get_weather(coords["latitude"], coords["longitude"])
        if not weather:
            return jsonify({"error": "Could not fetch weather data"}), 500
        
        return jsonify({
            "success": True,
            "city": coords["city"],
            "country": coords["country"],
            "temperature": weather["temperature"],
            "humidity": weather["humidity"],
            "weather_description": weather["weather_description"],
            "wind_speed": weather["wind_speed"],
            "pressure": weather["pressure"],
            "time": weather["time"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
