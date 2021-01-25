import os
import sys

sys.path.insert(0, os.path.abspath('src'))

from the_pitch.management import risk


def test_risk():
    ## total capital in our account = 20,000
    ## current stock price is 10.00, we want a stop loss at 9.75, = 0.25
    ## want to risk 2% of our total capital
    assert(1600 == risk.get_quantity(20000, 0.02, 0.25))
