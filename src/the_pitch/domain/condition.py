from typing import List, Optional
from . import EntrySettings, AbstractRule, Position
import numpy as np
from .enums import Side
import pandas as pd


class Condition(object):
    def __init__(self, settings: EntrySettings, rules: List[AbstractRule] = []):
        self.settings = settings
        self.rules = rules

    @property
    def side(self) -> Side:
        return self.settings.side

    def is_valid(self, frame: pd.DataFrame, active_position: Optional[Position] = None, **kwargs) -> bool:
        parameters = dict(
            kwargs,
            df=frame.loc[self.settings.symbol],
            settings=self.settings,
            active_position=active_position
        )

        output = np.all([
            rule.is_valid(**parameters)
            for rule in self.rules
        ])

        if output:

            if self.side == Side.Sell and active_position is None:
                ## cant sell with no active positions
                return False

            if self.side == Side.Buy and active_position is not None:
                ## no buying with positions still active
                return False

        return output
