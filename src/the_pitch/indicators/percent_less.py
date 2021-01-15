import pandas as pd
from decimal import Decimal
from .abstract_indicator import AbstractIndicator


class PercentLess(AbstractIndicator):
    def __init__(self, column: str = 'close', percent: Decimal = .10):
        super().__init__(f'pl_{column}_{percent}')

        self.column = column
        self.percent = percent

    def compute(self, df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        df[self.name] = round(df[self.column] - (df[self.column] * self.percent), 2)

        return df
