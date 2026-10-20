"""Decide which forecast days are dangerous."""

from config import RAIN_LIMIT_MM


def is_heavy_rain(rain_mm, limit=RAIN_LIMIT_MM):
    """Return True if the rain amount is at or above the danger limit."""

    # The weather service can send no value (None) for a day, so treat it as safe
    if rain_mm is None:
        return False

    return rain_mm >= limit

def find_dangerous_days(forecast, limit=RAIN_LIMIT_MM):
    """Take a list of (date, rain_mm) pairs and return only the dangerous ones."""

    dangerous = []

    # Check each day and keep the ones that cross the limit
    for date, rain_mm in forecast:
        if is_heavy_rain(rain_mm, limit):
            dangerous.append((date, rain_mm))

    return dangerous
