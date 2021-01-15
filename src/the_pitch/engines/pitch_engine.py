from typing import List

from the_pitch.domain import strategy
from ..domain import Strategy, StockPrice, Portfolio, Position, Side
from ..indicators import AbstractIndicator
from ..repositories import StockFrame


class PitchEngine(object):
    def __init__(self, seed_prices: List[StockPrice], indicators: List[AbstractIndicator], strategies: List[Strategy]):
        self.stock_frame = StockFrame(
            prices=seed_prices,
            indicators=indicators,
            strategies=strategies
        )

    def run(self, prices: List[StockPrice], portfolio: Portfolio) -> dict:
        response = {
            'buys': [],
            'sells': [],
        }

        output = self.stock_frame.add_rows(prices, portfolio)

        if len(output.keys()):
            price_by_symbol = { price.symbol: price for price in prices }
            for strategy_id, conditions in output.items():
                for condition in conditions:
                    symbol = condition.settings.symbol
                    quantity = condition.settings.quantity
                    assert_type = condition.settings.asset_type

                    trigger_price = price_by_symbol[symbol]
                    position = Position(
                        strategy_id,
                        symbol,
                        assert_type,
                        quantity,
                        trigger_price.close,
                        trigger_price.created_at
                    )

                    if condition.side == Side.Buy:
                        response['buys'].append(position)
                    else:
                        response['sells'].append(position)

        return response
