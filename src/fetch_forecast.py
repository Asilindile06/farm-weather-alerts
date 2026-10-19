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

    try:
        # Send the request; give up after 10 seconds so we never wait forever
        response = requests.get(API_URL, params=params, timeout=10)

        # Turn bad replies (like 404 or 500) into errors we can catch below
        response.raise_for_status()

        # Pull the "daily" section out of the reply
        daily = response.json()["daily"]

    except requests.exceptions.RequestException as error:
        # Covers no internet, timeouts and bad status codes
        print(f"Could not fetch forecast: {error}")
        return None

    except KeyError:
        # The reply arrived but did not have the "daily" section we expected
        print("Unexpected reply from the weather service.")
        return None

    # Pair each date with its rainfall and return them as a list
    return list(zip(daily["time"], daily["precipitation_sum"]))
