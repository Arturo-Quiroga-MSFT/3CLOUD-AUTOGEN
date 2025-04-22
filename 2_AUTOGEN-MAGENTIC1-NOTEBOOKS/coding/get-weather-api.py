import requests
import json
from datetime import datetime

# Placeholder for the API key and location parameters
API_KEY = "your_api_key_here"  # Replace with your actual API key
LATITUDE = "your_latitude_here"  # Replace with the desired latitude (e.g., "37.7749")
LONGITUDE = "your_longitude_here"  # Replace with the desired longitude (e.g., "-122.4194")

# OpenWeatherMap One Call API endpoint
API_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"

# Parameters for the API request
params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "exclude": "minutely,hourly,alerts",  # Exclude unnecessary sections if needed
    "units": "metric"  # Use metric units for temperature
}

try:
    # Make the API request
    response = requests.get(API_ENDPOINT, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the JSON data from the API response
    weather_data = response.json()

    # Save the data locally as a JSON file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"weather_data_{timestamp}.json"
    with open(filename, "w") as json_file:
        json.dump(weather_data, json_file, indent=4)

    print(f"Weather data successfully saved to {filename}")

except requests.exceptions.RequestException as e:
    print(f"Error while making API request: {e}")

except Exception as e:
    print(f"An error occurred: {e}")