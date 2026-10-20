"""Decide which forecast days are dangerous."""

from config import RAIN_LIMIT_MM


def is_heavy_rain(rain_mm, limit=RAIN_LIMIT_MM):
    """Return True if the rain amount is at or above the danger limit."""
    return rain_mm >= limit