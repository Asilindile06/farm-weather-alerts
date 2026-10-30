"""AWS Lambda: check the rain forecast and email bilingual alerts via SNS."""

import json
import os
import urllib.parse
import urllib.request

import boto3

API_URL = "https://api.open-meteo.com/v1/forecast"
TIMEZONE = "Africa/Johannesburg"

# Settings come from Lambda environment variables, so they can change without editing code
RAIN_LIMIT_MM = float(os.environ.get("RAIN_LIMIT_MM", "50"))
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")

# Farm areas to check (use your real coordinates from config.py)
LOCATIONS = [
    {"name": "Colenso", "latitude": -28.00, "longitude": 29.00},
    {"name": "Estcourt", "latitude": -29.00, "longitude": 29.00},
]


def get_rain_forecast(latitude, longitude):
    """Return a list of (date, rain_mm) pairs, or an empty list if the request fails."""
    query = urllib.parse.urlencode({
        "latitude": latitude,
        "longitude": longitude,
        "daily": "precipitation_sum",
        "timezone": TIMEZONE,
    })
    try:
        # Ask the weather service, giving up after 10 seconds
        with urllib.request.urlopen(f"{API_URL}?{query}", timeout=10) as response:
            daily = json.loads(response.read())["daily"]
        return list(zip(daily["time"], daily["precipitation_sum"]))
    except Exception as error:
        print(f"Could not fetch forecast: {error}")
        return []


def bilingual_alert(place, date, rain_mm):
    """Return the isiZulu alert followed by the English alert."""
    zulu = (
        f"ISEXWAYISO SEMVULA e{place}: kulindeleke imvula enkulu engu-{rain_mm} mm "
        f"ngomhlaka {date}. Sicela uvikele izitshalo nemfuyo yakho."
    )
    english = (
        f"WEATHER ALERT for {place}: heavy rain of {rain_mm} mm is expected "
        f"on {date}. Please protect your crops and livestock."
    )
    return zulu + "\n\n" + english


def lambda_handler(event, context):
    """Entry point: AWS calls this each time the timer fires."""
    sns = boto3.client("sns")
    alerts_sent = 0

    for location in LOCATIONS:
        forecast = get_rain_forecast(location["latitude"], location["longitude"])

        for date, rain_mm in forecast:
            # Skip days with no value, and days under the danger limit
            if rain_mm is None or rain_mm < RAIN_LIMIT_MM:
                continue

            message = bilingual_alert(location["name"], date, rain_mm)

            if SNS_TOPIC_ARN:
                sns.publish(
                    TopicArn=SNS_TOPIC_ARN,
                    Subject=f"Weather alert: {location['name']}",
                    Message=message,
                )
            else:
                print(message)  # no topic set: just log it
            alerts_sent += 1

    return {"statusCode": 200, "alerts_sent": alerts_sent}