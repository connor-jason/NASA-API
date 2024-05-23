import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define API URL and retrieve API key from environment variables
url = "https://api.nasa.gov/planetary/apod"
api_key = os.getenv("API_KEY")

def nasa_APOD():
    # Send request to NASA APOD API with API key as parameter
    response = requests.get(url, params={"api_key": api_key})

    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        hd_url = data["hdurl"]

        # Download and save the HD image
        image_path = "image.png"
        if os.path.exists(image_path):
            os.remove(image_path)

        with open(image_path, "wb") as file:
            response = requests.get(hd_url)
            file.write(response.content)
            
    else:
        print("Failed to fetch data from the API.")
