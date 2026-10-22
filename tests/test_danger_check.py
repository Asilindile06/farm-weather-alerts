"""Tests for the danger check."""

from danger_check import is_heavy_rain, find_dangerous_days


def test_rain_above_limit_is_dangerous():
    # 60 mm is more than a 50 mm limit, so it should be flagged
    assert is_heavy_rain(60, limit=50) is True