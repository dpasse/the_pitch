from datetime import datetime, timedelta
import os
import sys

sys.path.insert(0, os.path.abspath('src'))

from the_pitch.managers import ChartManager
from the_pitch.domain import ChartType


def test_next_bar_at_one_min():
    last_bar_timestamp = datetime(2020, 10, 1, 8, 56, 0, 0)
    next_bar = ChartManager(ChartType.OneMinute).get_next_expected_bar(last_bar_timestamp)
    assert(next_bar == datetime(2020, 10, 1, 8, 57, 0, 0))

def test_next_bar_at_five_mins():
    last_bar_timestamp = datetime(2020, 10, 1, 8, 15, 0, 0)
    next_bar = ChartManager(ChartType.FiveMinutes).get_next_expected_bar(last_bar_timestamp)
    assert(next_bar == datetime(2020, 10, 1, 8, 20, 0, 0))

def test_next_bar_at_fifteen_mins():
    last_bar_timestamp = datetime(2020, 10, 1, 8, 15, 0, 0)
    next_bar = ChartManager(ChartType.FifteenMinutes).get_next_expected_bar(last_bar_timestamp)
    assert(next_bar == datetime(2020, 10, 1, 8, 30, 0, 0))

def test_next_bar_at_thrity_mins():
    last_bar_timestamp = datetime(2020, 10, 1, 8, 15, 0, 0)
    next_bar = ChartManager(ChartType.ThrityMinutes).get_next_expected_bar(last_bar_timestamp)
    assert(next_bar == datetime(2020, 10, 1, 8, 45, 0, 0))

def test_next_bar_at_one_day():
    last_bar_timestamp = datetime(2020, 10, 1, 8, 15, 0, 0)
    next_bar = ChartManager(ChartType.OneDay).get_next_expected_bar(last_bar_timestamp)
    assert(next_bar == datetime(2020, 10, 2, 8, 15, 0, 0))

def test_next_bar_at_one_day_when_saturday():
    last_bar_timestamp = datetime(2021, 1, 23, 8, 15, 0, 0)
    next_bar = ChartManager(ChartType.OneDay).get_next_expected_bar(last_bar_timestamp)
    assert(next_bar == datetime(2021, 1, 25, 8, 15, 0, 0))

def test_next_bar_at_one_day_when_sunday():
    last_bar_timestamp = datetime(2021, 1, 24, 8, 15, 0, 0)
    next_bar = ChartManager(ChartType.OneDay).get_next_expected_bar(last_bar_timestamp)
    assert(next_bar == datetime(2021, 1, 25, 8, 15, 0, 0))

def test_get_historical_timeframe():
    delta = 15
    now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    start, end = ChartManager(ChartType.OneDay).get_historical_timeframe(15)

    assert(now > start)
    assert(now - timedelta(delta+1) == end)
