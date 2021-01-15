from decimal import Decimal
import os
import sys
import pandas as pd

sys.path.insert(0, os.path.abspath('src'))

from the_pitch.converters import utils
from the_pitch.indicators import EMA

def test_ema_calculation():
    df_1 = pd.read_csv('tests/data/dal.csv', converters={'close': utils.decimal_from_value })
    df_2 = EMA('close', 5).compute(df_1).dropna()

    expected = [ Decimal('46.39'), Decimal('46.23'), Decimal('45.5'), Decimal('44.88'), Decimal('44.48') ]
    values = df_2.tail(n=5)['ema_close_5'].tolist()

    for i, value in enumerate(expected):
        assert(value == values[i])
