"""Check every farmer's area and print bilingual alerts."""

import json
from pathlib import Path

# Work out where data/farmers.json is, starting from this file's own location
FARMERS_FILE = Path(__file__).resolve().parent.parent / "data" / "farmers.json"


def load_farmers(path=FARMERS_FILE):
    """Read the farmers list from the JSON file and return it."""
    with open(path, encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    for farmer in load_farmers():
        print(farmer["name"], "-", farmer["location"])