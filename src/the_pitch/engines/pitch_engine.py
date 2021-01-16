from typing import List
from ..domain import Strategy, StockPrice, Portfolio, Position, Side, StrategyEvaluationResponse, Pitch, StrategyPayload
from ..indicators import AbstractIndicator
from ..repositories import StockFrame


class PitchEngine(object):
    def __init__(self, seed_prices: List[StockPrice], indicators: List[AbstractIndicator], strategies: List[Strategy]):
        self.stock_frame = StockFrame(
            prices=seed_prices,
            indicators=indicators
        )

        self.strategies = strategies

    def run(self, pitch: Pitch, portfolio: Portfolio) -> StrategyEvaluationResponse:
        self.stock_frame.add_rows(pitch.prices, portfolio)

        return self._evaluate_strategies(pitch, portfolio)

    def _get_valid_conditions(self, portfolio: Portfolio) -> dict:
        evals = {}

        for strategy in self.strategies:
            strategy_payload = StrategyPayload(
                strategy.id,
                self.stock_frame.df,
                active_positions = { p.symbol: p for p in portfolio.get_positions_by_strategy(strategy.id) }
            )

            evals[strategy.id] = strategy.get_valid_conditions(strategy_payload)

        return evals


    def _evaluate_strategies(self, pitch: Pitch, portfolio: Portfolio) -> StrategyEvaluationResponse:
        buys = []
        sells = []

        evals = self._get_valid_conditions(portfolio)

        if len(evals.keys()):
            price_by_symbol = { price.symbol: price for price in pitch.prices }
            for strategy_id, conditions in evals.items():
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
                        trigger_price.created_at,
                        condition.side
                    )

                    if condition.side == Side.Buy:
                        buys.append(position)
                    else:
                        sells.append(position)

        return StrategyEvaluationResponse(buys, sells)
