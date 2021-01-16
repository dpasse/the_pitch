from typing import List
from . import Condition


class StrategyEvaluationResponse(object):

    def __init__(self, buys: List[Condition] = [], sells: List[Condition] = []) -> None:
        self.buys = buys
        self.sells = sells
