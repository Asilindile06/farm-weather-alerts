"""Decide which forecast days are dangerous."""

from config import RAIN_LIMIT_MM


def is_heavy_rain(rain_mm, limit=RAIN_LIMIT_MM):
    """Return True if the rain amount is at or above the danger limit."""

    # The weather service can send no value (None) for a day, so treat it as safe
    if rain_mm is None:
        return False

    return rain_mm >= limit


