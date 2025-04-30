# Python script to fetch data from OpenWeatherMap One Call API 3.0

import requests
import json

# API configuration
API_KEY = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
LATITUDE = '37.7749'  # Example latitude (San Francisco)
LONGITUDE = '-122.4194'  # Example longitude (San Francisco)
OUTPUT_FILE = 'weather_data.json'  # File to save the response
ENDPOINT = f'https://api.openweathermap.org/data/3.0/onecall'

# Parameters for the request
params = {
    'lat': LATITUDE,
    'lon': LONGITUDE,
    'appid': API_KEY
}

try:
    # Make the API call
    print("Contacting OpenWeatherMap API...")
    response = requests.get(ENDPOINT, params=params)
    
    # Validate the response
    if response.status_code == 200:
        print("Data fetched successfully!")
        weather_data = response.json()
        
        # Save the data locally
        with open(OUTPUT_FILE, 'w') as file:
            json.dump(weather_data, file, indent=4)
        print(f"Weather data saved to {OUTPUT_FILE}")
    elif response.status_code == 401:
        print("Error: Unauthorized! Please check your API key.")
    elif response.status_code == 404:
        print("Error: Endpoint not found. Please double-check the URL.")
    else:
        print(f"Error: Unable to fetch data. HTTP Status Code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")