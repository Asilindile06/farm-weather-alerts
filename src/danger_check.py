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

# This block only runs when we run this file directly
if __name__ == "__main__":
    from fetch_forecast import get_rain_forecast, LATITUDE, LONGITUDE

    forecast = get_rain_forecast(LATITUDE, LONGITUDE)

    if forecast:
        dangerous_days = find_dangerous_days(forecast)

        if dangerous_days:
            for date, rain_mm in dangerous_days:
                print(f"WARNING: {rain_mm} mm of rain expected on {date}")
        else:
            print("No dangerous rainfall in the forecast.")
