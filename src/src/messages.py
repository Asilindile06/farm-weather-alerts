"""Build the alert messages that farmers will receive."""


def english_alert(place, date, rain_mm):
    """Return the English alert text."""
    return (
        f"WEATHER ALERT for {place}: heavy rain of {rain_mm} mm is expected "
        f"on {date}. Please protect your crops and livestock."
    )

def zulu_alert(place, date, rain_mm):
    """Return the isiZulu alert text."""
    return (
        f"ISEXWAYISO SEMVULA e{place}: kulindeleke imvula enkulu engu-{rain_mm} mm "
        f"ngomhlaka {date}. Sicela uvikele izitshalo nemfuyo yakho."
    )