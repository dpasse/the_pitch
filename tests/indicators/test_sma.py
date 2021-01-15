import os
import sys
import pandas as pd

sys.path.insert(0, os.path.abspath('src'))

from the_pitch.indicators import SMA

def test_sma_calculation():

    df_1 = pd.read_csv('tests/data/dal.csv')
    df_2 = SMA('close', 5).compute(df_1).dropna()

    expected = [ 46.16, 46.01, 45.81, 45.40, 44.86 ]
    values = df_2.tail(n=5)['sma_close_5'].tolist()

    for i, value in enumerate(expected):
        assert(value == values[i])
