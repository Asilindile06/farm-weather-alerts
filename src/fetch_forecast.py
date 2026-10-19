"""Fetch the daily rainfall forecast for one location from Open-Meteo."""

import requests

# The web address of the Open-Meteo forecast service
API_URL = "https://api.open-meteo.com/v1/forecast"

# The location we want the forecast for
LATITUDE = -29.00
LONGITUDE = 29.88

# Makes the dates match South African time instead of GMT
TIMEZONE = "Africa/Johannesburg"


def get_rain_forecast(latitude, longitude):
    """Return a list of (date, rain_mm) pairs, or None if the request fails."""

    # The "question" we send to the weather service
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "precipitation_sum",  # total rain per day, in millimetres
        "timezone": TIMEZONE,
    }