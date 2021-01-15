from collections import defaultdict
from typing import Dict, List

from . import Position


class Portfolio(object):
    def __init__(self) -> None:
        self.active_positions: Dict[str, List[Position]] = defaultdict(list)

    def add_positions(self, new_positions: List[Position]) -> None:
        for position in new_positions:
            self.active_positions[position.strategy_id].append(position)

    def remove_position(self, strategy_id: str, symbol: str) -> None:
        if symbol in self.active_positions.keys():
            self.active_positions[strategy_id] = filter(
              lambda p: p.symbol != symbol,
              self.active_positions[strategy_id],
            )

    def get_positions_by_strategy(self, strategy_id: str) -> List[Position]:
        return self.active_positions[strategy_id]

    def get_positions(self, strategy_id: str, symbol: str) -> List[Position]:
        return filter(
          lambda p: p.symbol == symbol,
          self.get_positions_by_strategy(strategy_id)
        )
