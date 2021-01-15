import os
import sys
import pandas as pd

sys.path.insert(0, os.path.abspath('src'))

from the_pitch.indicators import PercentMore

def test_pm_calculation():

    df_1 = pd.read_csv('tests/data/dal.csv')
    df_2 = PercentMore('close', .10).compute(df_1).dropna()

    expected = [ 51.73, 50.51, 48.44, 48.02, 48.03 ]
    values = df_2.tail(n=5)['pl_close_0.1'].tolist()

    for i, value in enumerate(expected):
        assert(value == values[i])
