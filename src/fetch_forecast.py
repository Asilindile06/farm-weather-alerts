"""Fetch the daily rainfall forecast for one location from Open-Meteo."""


# The web address of the Open-Meteo forecast service
API_URL = "https://api.open-meteo.com/v1/forecast"

# The location we want the forecast for (replace with the numbers you copied from Google Maps)
LATITUDE = -29.00
LONGITUDE = 29.88

# Makes the dates match South African time instead of GMT
TIMEZONE = "Africa/Johannesburg"


