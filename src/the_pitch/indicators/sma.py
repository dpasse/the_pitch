import pandas as pd
from .abstract_indicator import AbstractIndicator


class SMA(AbstractIndicator):
    def __init__(self, column: str = 'close', period: int = 20):
        super().__init__(f'sma_{column}_{period}')

        self.period = period
        self.column = column

    def compute(self, df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        df[self.name] = df[self.column].transform(
            lambda x: round(x.rolling(window=self.period).mean(), 2)
        )

        return df
