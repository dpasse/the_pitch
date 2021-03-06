from typing import List
from ..managers import PlayMoneyPortfolioManager
from ..indicators import AbstractIndicator
from ..domain import Strategy, Portfolio, SimulationDataset, Pitch
from ..engines import PortfolioWrapper
from ..repositories import StockFrame


class PitchSimulator(object):
    def __init__(self, dataset: SimulationDataset):
        self.data = dataset.data
        self.test_data = dataset.test_data

    def run(self, indicators: List[AbstractIndicator], strategies: List[Strategy]):
        portfolio_manager = PlayMoneyPortfolioManager(Portfolio())

        stock_frame = StockFrame(
            prices=self.data,
            indicators=indicators
        )

        engine = PortfolioWrapper(
            stock_frame,
            strategies,
            portfolio_manager
        )

        for _, stock_prices in self.test_data.items():
            engine.run(Pitch(stock_prices))

        return portfolio_manager.strategy_operations
