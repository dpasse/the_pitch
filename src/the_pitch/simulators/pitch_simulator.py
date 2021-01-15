from typing import Dict, List

from ..indicators import AbstractIndicator
from ..domain import Strategy, Portfolio, Position, SimulationDataset
from ..engines import PitchEngine


class PitchSimulator(object):
    def __init__(self, dataset: SimulationDataset):
        self.data = dataset.data
        self.test_data = dataset.test_data

    def run(self, indicators: List[AbstractIndicator], strategies: List[Strategy], portfolio: Portfolio = Portfolio()):
        engine = PitchEngine(
            self.data,
            indicators,
            strategies
        )

        operations: Dict[str, Dict[str, List[Position]]] = {}
        for _, stock_prices in self.test_data.items():
            response = engine.run(stock_prices, portfolio)

            portfolio.add_positions(response['buys'])
            for position in response['buys']:
                strategy_id = position.strategy_id
                symbol = position.symbol

                if strategy_id not in operations:
                    operations[strategy_id] = {}

                if symbol not in operations[strategy_id]:
                    operations[strategy_id][symbol] = []

                ## record so the transaction can be scored
                operations[strategy_id][symbol].append(position)

            sells: List[Position] = response['sells']
            for position in sells:
                strategy_id = position.strategy_id
                symbol = position.symbol

                ## remove from portfolio ('sold')
                portfolio.remove_position(strategy_id, symbol)

                ## record so the transaction can be scored
                operations[strategy_id][symbol].append(position)

        return operations
