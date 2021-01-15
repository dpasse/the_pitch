from typing import List, Tuple

from ..domain import PandasColumnRuleValue, SingleRule, LogicalOperator
from ..indicators import SMA, AbstractIndicator
from ..domain import Strategy, Condition, EntrySettings, Side
from . import StrategyType


class StrategyFactory(object):

    @staticmethod
    def create(id: str, symbols: List[str], strategy_type: StrategyType) -> Tuple[Strategy, List[AbstractIndicator]]:

        if strategy_type == StrategyType.SMA50_X_SMA200:
            sma_50 = SMA('close', 50)
            sma_200 = SMA('close', 200)

            conditions = []
            for symbol in symbols:
                ## buy when,
                conditions.append(
                    Condition(
                        settings=EntrySettings(
                            symbol=symbol,
                            side=Side.Buy,
                            quantity=1,
                            stopLoss=None
                        ),
                        rules=[
                            SingleRule(
                                PandasColumnRuleValue(sma_50.name),
                                LogicalOperator.LessThan,
                                PandasColumnRuleValue(sma_200.name),
                                time_step=-2,
                            ),
                            SingleRule(
                                PandasColumnRuleValue(sma_50.name),
                                LogicalOperator.GreaterThan,
                                PandasColumnRuleValue(sma_200.name),
                                time_step=-1,
                            ),
                        ]
                    )
                )

                ## sell when,
                conditions.append(
                    Condition(
                        settings=EntrySettings(
                            symbol=symbol,
                            side=Side.Sell,
                            stopLoss=None
                        ),
                        rules=[
                            SingleRule(
                                PandasColumnRuleValue(sma_50.name),
                                LogicalOperator.GreaterThan,
                                PandasColumnRuleValue(sma_200.name),
                                time_step=-2,
                            ),
                            SingleRule(
                                PandasColumnRuleValue(sma_50.name),
                                LogicalOperator.LessThan,
                                PandasColumnRuleValue(sma_200.name),
                                time_step=-1,
                            ),
                        ]
                    )
                )

            strategy = Strategy(
                id,
                description='Buy: SMA 50 goes above SMA 200\nSell: SMA 50 goes below SMA 200',
                conditions=conditions
            )

            return (strategy, [ sma_50, sma_200 ])

        raise NotImplementedError()
