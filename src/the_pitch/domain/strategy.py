from typing import Dict, List
from . import Condition, Position

import pandas as pd


class Strategy(object):
    """ By combining various entry and exit conditions, we get a strategy. """
    def __init__(self,
                id: str,
                description: str,
                conditions: List[Condition] = []):
        self.id = id
        self.description = description
        self.conditions = conditions

    def get_valid_conditions(self, frame: pd.DataFrame, active_positions: Dict[str, List[Position]], **kwargs) -> List[Condition]:
        return [
            condition
            for condition in self.conditions
            if condition.is_valid(frame, active_positions[condition.settings.symbol] if condition.settings.symbol in active_positions else [], **kwargs)
        ]

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id
