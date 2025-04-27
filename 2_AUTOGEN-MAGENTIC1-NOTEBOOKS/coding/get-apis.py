# Python script to fetch data from the Dogs API

import requests

def fetch_random_dog_image():
    try:
        # API endpoint
        url = "https://dog.ceo/api/breeds/image/random"
        
        # Sending a GET request to the API
        response = requests.get(url)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Extract the image URL
        image_url = data.get("message")
        
        # Display the image URL
        print("Random Dog Image URL:", image_url)
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Call the function to fetch the random dog image
fetch_random_dog_image()