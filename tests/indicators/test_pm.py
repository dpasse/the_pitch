import os
import sys
import pandas as pd
from decimal import Decimal

sys.path.insert(0, os.path.abspath('src'))

from the_pitch.converters import utils
from the_pitch.indicators import PercentMore

def test_pm_calculation():
    df_1 = pd.read_csv('tests/data/dal.csv', converters={'close': utils.decimal_from_value })
    df_2 = PercentMore('close', Decimal('.10')).compute(df_1).dropna()

    expected = [ Decimal('51.7330'), Decimal('50.5120'), Decimal('48.4440'), Decimal('48.0150'), Decimal('48.0260') ]
    values = df_2.tail(n=5)['pm_close_0.10'].tolist()

    for i, value in enumerate(expected):
        assert(value == values[i])
