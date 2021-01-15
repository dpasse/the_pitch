import pandas as pd
from .abstract_indicator import AbstractIndicator


class EMA(AbstractIndicator):
    def __init__(self, column: str = 'close', period: int = 20):
        super().__init__(f'ema_{column}_{period}')

        self.column = column
        self.period = period

    def compute(self, df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        df[self.name] = df[self.column].transform(
            lambda x: round(x.ewm(span=self.period).mean(), 2)
        )

        return df
