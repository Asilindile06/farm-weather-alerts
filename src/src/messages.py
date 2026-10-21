"""Build the alert messages that farmers will receive."""


def english_alert(place, date, rain_mm):
    """Return the English alert text."""
    return (
        f"WEATHER ALERT for {place}: heavy rain of {rain_mm} mm is expected "
        f"on {date}. Please protect your crops and livestock."
    )