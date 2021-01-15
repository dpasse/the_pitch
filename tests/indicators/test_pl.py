import os
import sys
import pandas as pd

sys.path.insert(0, os.path.abspath('src'))

from the_pitch.indicators import PercentLess

def test_pl_calculation():

    df_1 = pd.read_csv('tests/data/dal.csv')
    df_2 = PercentLess('close', .10).compute(df_1).dropna()

    expected = [ 42.33, 41.33, 39.64, 39.28, 39.29 ]
    values = df_2.tail(n=5)['pl_close_0.1'].tolist()

    for i, value in enumerate(expected):
        assert(value == values[i])
