"""Check every farmer's area and print bilingual alerts."""

import json
from pathlib import Path

# Our own files: the farm locations, the danger check, the forecast and the messages
from config import LOCATIONS
from danger_check import find_dangerous_days
from fetch_forecast import get_rain_forecast
from messages import bilingual_alert

# Work out where data/farmers.json is, starting from this file's own location
FARMERS_FILE = Path(__file__).resolve().parent.parent / "data" / "farmers.json"


def load_farmers(path=FARMERS_FILE):
    """Read the farmers list from the JSON file and return it."""

    # Open the file as UTF-8 so isiZulu letters and symbols are read correctly
    with open(path, encoding="utf-8") as file:
        # Turn the JSON text into a Python list of dictionaries
        return json.load(file)


def find_location(name):
    """Return the location (with coordinates) that matches a name, or None."""

    # Look through our known locations for one with the same name
    for location in LOCATIONS:
        if location["name"] == name:
            return location

    # No match found
    return None


# This block only runs when we run this file directly (not when imported)
if __name__ == "__main__":
    # Go through every farmer and check the forecast for their area
    for farmer in load_farmers():
        location = find_location(farmer["location"])

        # Skip farmers whose area is not in our config, and say why
        if location is None:
            print(f"Unknown location for {farmer['name']}: {farmer['location']}")
            continue

        # Fetch the rain forecast for this farmer's area
        forecast = get_rain_forecast(location["latitude"], location["longitude"])

        # If the forecast could not be fetched, move on to the next farmer
        if not forecast:
            continue

        # Print one bilingual alert for each dangerous day
        for date, rain_mm in find_dangerous_days(forecast):
            print(f"To: {farmer['name']} <{farmer['email']}>")
            print(bilingual_alert(location["name"], date, rain_mm))
            print("-" * 40)