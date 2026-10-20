# Danger limit: a day with this much forecast rain (in mm) or more triggers an alert.
# This is a starting value; adjust it and note your reasoning in the README.
RAIN_LIMIT_MM = 50

# The farm areas we check; each has a name and coordinates
LOCATIONS = [
    {"name": "Colenso", "latitude": -28.00, "longitude": 29.00},
    {"name": "Estcourt", "latitude": -29.00, "longitude": 29.00},
]