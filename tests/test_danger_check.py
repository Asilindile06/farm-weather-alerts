"""Tests for the danger check."""

from danger_check import is_heavy_rain, find_dangerous_days


def test_rain_above_limit_is_dangerous():
    # 60 mm is more than a 50 mm limit, so it should be flagged
    assert is_heavy_rain(60, limit=50) is True


def test_rain_below_limit_is_safe():
    # 10 mm is under the 50 mm limit, so no alert
    assert is_heavy_rain(10, limit=50) is False


def test_rain_exactly_at_limit_is_dangerous():
    # The limit itself counts as dangerous (we use >=)
    assert is_heavy_rain(50, limit=50) is True