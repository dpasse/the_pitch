import os
import sys
import pandas as pd
from decimal import Decimal

sys.path.insert(0, os.path.abspath('src'))

from the_pitch.converters import utils
from the_pitch.indicators import SMA

def test_sma_calculation():
    df_1 = pd.read_csv('tests/data/dal.csv', converters={'close': utils.decimal_from_value })
    df_2 = SMA('close', 5).compute(df_1).dropna()

    expected = [ Decimal('46.16'), Decimal('46.01'), Decimal('45.81'), Decimal('45.4'), Decimal('44.86') ]
    values = df_2.tail(n=5)['sma_close_5'].tolist()

    for i, value in enumerate(expected):
        assert(value == values[i])
