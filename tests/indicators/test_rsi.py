import os
import sys
import pandas as pd
from decimal import Decimal

sys.path.insert(0, os.path.abspath('src'))

from the_pitch.converters import utils
from the_pitch.indicators import RSI, Difference

def test_rsi_calculation():
    df_1 = Difference(column='close', period=1).compute(pd.read_csv('tests/data/dal.csv', converters={'close': utils.decimal_from_value }))
    df_2 = RSI(5).compute(df_1).dropna()

    expected = [ Decimal('98.63'), Decimal('97.61'), Decimal('95.13'), Decimal('94.38'), Decimal('94.51') ]
    values = df_2.tail(n=5)['rsi_5'].tolist()

    for i, value in enumerate(expected):
        assert(value == values[i])
