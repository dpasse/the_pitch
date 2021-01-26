import os
import sys
import pandas as pd
from decimal import Decimal

sys.path.insert(0, os.path.abspath('src'))

from the_pitch.converters import utils
from the_pitch.indicators import Gap

def test_gap_calculation():
    df_1 = pd.read_csv('tests/data/dal.csv', converters={'close': utils.decimal_from_value, 'open': utils.decimal_from_value })
    df_2 = Gap().compute(df_1).dropna()

    expected = [ Decimal('3.75'), Decimal('3.83') ]
    values = df_2.tail(n=2)['gap'].tolist()

    for i, value in enumerate(expected):
        assert(value == values[i])
