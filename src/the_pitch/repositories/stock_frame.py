from typing import List, Optional
import numpy as np
import pandas as pd
from pandas.core.groupby import DataFrameGroupBy
from ..indicators import AbstractIndicator
from ..domain import StockPrice, Portfolio


class StockFrame():
    def __init__(self, **kwargs) -> None:
        if 'prices' in kwargs.keys():
            self.df = pd.DataFrame(data=[ price.to_obj() for price in kwargs['prices'] ]).set_index(keys=StockPrice.index_columns())

        if 'df' in kwargs.keys():
            self.df: pd.DataFrame = kwargs['df'].set_index(keys=StockPrice.index_columns())

        self.cache_path = None
        if 'cache_path' in kwargs:
            self.cache_path: str = kwargs['cache_path']

        self.indicators: List[AbstractIndicator] = kwargs['indicators']
        self._refresh_indicators()

    @property
    def symbol_groups(self) -> DataFrameGroupBy:
        return self.df.groupby(by='symbol', as_index=False, sort=True)

    def add_rows(self, prices: List[StockPrice], active_portfolio: Portfolio, **kwargs) -> None:
        columns = StockPrice.feature_columns()
        for price in prices:
            self.df.loc[price.index, columns] = price.to_list()

        self._refresh_indicators(active_portfolio=active_portfolio, **kwargs)

    def _refresh_indicators(self, **kwargs) -> None:
        self.df.sort_index(inplace=True)

        symbols = np.unique(
            list(map(lambda index: index[0], self.df.index))
        )

        for indicator in self.indicators:

            calc = []
            for symbol in symbols:
                output = indicator.compute(self.df.loc[symbol], **kwargs).reset_index()
                output['symbol'] = symbol

                calc.append(output)

            self.df = pd.concat(calc).set_index(keys=StockPrice.index_columns()).sort_index()

        self._cache()

    def _cache(self):
        if self.cache_path is None:
            return

        self.df.to_csv(self.cache_path)
