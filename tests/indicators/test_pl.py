import os
import sys
import pandas as pd
from decimal import Decimal

sys.path.insert(0, os.path.abspath('src'))

from the_pitch.converters import utils
from the_pitch.indicators import PercentLess

def test_pl_calculation():
    df_1 = pd.read_csv('tests/data/dal.csv', converters={'close': utils.decimal_from_value })
    df_2 = PercentLess('close', Decimal('.10')).compute(df_1).dropna()

    expected = [ Decimal('42.3270'), Decimal('41.3280'), Decimal('39.6360'), Decimal('39.2850'), Decimal('39.2940') ]
    values = df_2.tail(n=5)['pl_close_0.10'].tolist()

    for i, value in enumerate(expected):
        assert(value == values[i])
