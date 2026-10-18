"""Fetch the daily rainfall forecast for one location from Open-Meteo."""
import requests

# The web address of the Open-Meteo forecast service
API_URL = "https://api.open-meteo.com/v1/forecast"

# The location we want the forecast for (replace with the numbers you copied from Google Maps)
LATITUDE = -29.00
LONGITUDE = 29.88

# Makes the dates match South African time instead of GMT
TIMEZONE = "Africa/Johannesburg"


# The "question" we send to the weather service
params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "daily": "precipitation_sum",  # total rain per day, in millimetres
    "timezone": TIMEZONE,
}

# Send the request and store the service's reply
response = requests.get(API_URL, params=params)

# 200 means the request worked
print(response.status_code)