from typing import Dict, List
from ..indicators import AbstractIndicator
from ..domain import Strategy, Portfolio, Position, AssetType, Side, SimulationDataset
from ..repositories import StockFrame


class PitchSimulator(object):

    def __init__(self, dataset: SimulationDataset):
        self.data = dataset.data
        self.test_data = dataset.test_data

    def run(self, indicators: List[AbstractIndicator], strategies: List[Strategy], portfolio: Portfolio = Portfolio()):
        stock_frame = StockFrame(
            prices=self.data,
            indicators=indicators,
            strategies=strategies
        )

        operations: Dict[str, Dict[str, List[Position]]] = {}
        for _, stock_prices in self.test_data.items():
            output = stock_frame.add_rows(
                stock_prices,
                portfolio
            )

            stock_price_lookup = { sp.symbol: sp for sp in stock_prices }
            for strategy_id in output.keys():
                conditions = output[strategy_id]

                if strategy_id not in operations:
                    operations[strategy_id] = {}

                for condition in conditions:
                    symbol = condition.settings.symbol
                    if symbol not in operations[strategy_id]:
                        operations[strategy_id][symbol] = []

                    trigger_price = stock_price_lookup[symbol]
                    position = Position(
                        strategy_id,
                        symbol,
                        AssetType.Equity,
                        condition.settings.quantity,
                        trigger_price.close,
                        trigger_price.created_at
                    )

                    if condition.side == Side.Buy:
                        portfolio.add_positions(position)
                    else:
                        portfolio.remove_position(strategy_id, symbol)

                    operations[strategy_id][symbol].append(position)

        return operations




