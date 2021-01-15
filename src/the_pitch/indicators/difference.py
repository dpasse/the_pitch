import pandas as pd
from .abstract_indicator import AbstractIndicator


class Difference(AbstractIndicator):
    def __init__(self, column: str = 'close', period: int = 9):
        super().__init__(f'diff_{period}')

        self.column = column
        self.period = period

    def compute(self, df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        df[self.name] = df[self.column].transform(
            lambda x: x.diff(periods=self.period)
        )

        return df
