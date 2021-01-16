from typing import List, DefaultDict
from ..engines import PitchEngine
from ..domain import StockPrice, Strategy, Portfolio, Position, Pitch, Side
from ..indicators import AbstractIndicator
from ..managers import PortfolioManager
from collections import defaultdict


class PortfolioWrapper(object):
    def __init__(self, seed_prices: List[StockPrice], indicators: List[AbstractIndicator], strategies: List[Strategy], portfolio_manager: PortfolioManager):
        self.engine = PitchEngine(
            seed_prices=seed_prices,
            indicators=indicators,
            strategies=strategies
        )

        self.portfolio_manager = portfolio_manager

    def run(self, pitch: Pitch) -> List[Position]:
        return self.portfolio_manager.run(
            self.engine.run(pitch, self.portfolio_manager.portfolio)
        )
