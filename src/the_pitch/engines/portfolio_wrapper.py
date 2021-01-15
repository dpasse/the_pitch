from typing import List, Dict
from the_pitch.engines.pitch_engine import PitchEngine
from ..domain import StockPrice, Strategy, Portfolio, Position
from ..indicators import AbstractIndicator
from collections import defaultdict


class PortfolioWrapper(object):
    def __init__(self, seed_prices: List[StockPrice], indicators: List[AbstractIndicator], strategies: List[Strategy], portfolio: Portfolio = Portfolio(), paper_money: bool = True):
        self.engine = PitchEngine(
            seed_prices=seed_prices,
            indicators=indicators,
            strategies=strategies
        )

        self.portfolio = portfolio
        self.paper_money = paper_money

        ## history
        self.strategy_operations = defaultdict(lambda: defaultdict(list))

    def run(self, prices: List[StockPrice]) -> dict:
        self.portfolio.reload()
        response = self.engine.run(prices, self.portfolio)

        if self.paper_money:
            self.portfolio.add_positions(response['buys'])
            self.portfolio.remove_positions(response['sells'])

        for position in response['buys']:
            self.strategy_operations[position.strategy_id][position.symbol].append(position)

        for position in response['sells']:
            self.strategy_operations[position.strategy_id][position.symbol].append(position)

        return response


