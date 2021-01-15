from typing import Dict, List
import pandas as pd
from ..indicators import AbstractIndicator
from ..domain import StockPrice, Condition, Strategy, Portfolio


class StockFrame():
    def __init__(self, prices: List[StockPrice], indicators: List[AbstractIndicator] = [], strategies: List[Strategy] = [], **kwargs) -> None:
        self.df = pd.DataFrame(data=[ price.to_obj() for price in prices ]).set_index(keys=StockPrice.index_columns())

        self.indicators = indicators
        self.strategies = strategies

        self._refresh_indicators(**kwargs)

    def add_rows(self, prices: List[StockPrice], active_portfolio: Portfolio, **kwargs) -> Dict[str, List[Condition]]:
        columns = StockPrice.feature_columns()
        for price in prices:
            self.df.loc[price.index, columns] = price.to_list()

        self._refresh_indicators(**kwargs)

        return self._evaluate_strategies(active_portfolio, **kwargs)

    def _refresh_indicators(self, **kwargs) -> None:
        self.df.sort_index(inplace=True)

        for indicator in self.indicators:
            self.df = indicator.compute(self.df, **kwargs)

    def _evaluate_strategies(self, portfolio: Portfolio, **kwargs) -> Dict[str, List[Condition]]:
        evals = {}
        for strategy in self.strategies:
            positions = { p.symbol: p for p in portfolio.get_positions_by_strategy(strategy.id) }
            evals[strategy.id] = strategy.get_valid_conditions(self.df, positions, **kwargs)

        return evals
