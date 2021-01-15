from datetime import datetime
from decimal import Decimal
from dataclasses import dataclass
from typing import Tuple
import pandas as pd


@dataclass
class StockPrice(object):
    symbol: str
    created_at: datetime
    open: Decimal
    close: Decimal
    high: Decimal
    low: Decimal
    volume: int

    @property
    def index(self) -> Tuple[str, datetime]:
        return (self.symbol, self.created_at)

    @staticmethod
    def index_columns():
        return ['symbol', 'datetime']

    @staticmethod
    def feature_columns():
        return [ 'open', 'close', 'high', 'low', 'volume' ]

    def to_obj(self) -> dict:
        return {
          'symbol': self.symbol,
          'datetime': self.created_at,
          'open': self.open,
          'close': self.close,
          'high': self.high,
          'low': self.low,
          'volume': self.volume,
        }

    def to_list(self, include_indexes: bool = False) -> list:
        if include_indexes:
            return [ self.symbol, self.created_at, self.open, self.close, self.high, self.low, self.volume ]

        return [ self.open, self.close, self.high, self.low, self.volume ]

    @staticmethod
    def create_many(df: pd.DataFrame):
        prices = []
        for _, row in df.iterrows():
            prices.append(
                StockPrice(
                    row['symbol'],
                    row['date'],
                    Decimal(str(round(row['open'], 2))),
                    Decimal(str(round(row['close'], 2))),
                    Decimal(str(round(row['high'], 2))),
                    Decimal(str(round(row['low'], 2))),
                    int(row['volume'])
                )
            )

        return prices
