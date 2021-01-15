from collections import defaultdict
from typing import Dict, List

from . import Position


class Portfolio(object):
    def __init__(self) -> None:
        self.by_positions: Dict[str, List[Position]] = defaultdict(list)

    def add_positions(self, new_positions: List[Position]) -> None:
        for position in new_positions:
            self.by_positions[position.strategy_id].append(position)

    def remove_position(self, strategy_id: str, symbol: str) -> None:
        if symbol in self.by_positions.keys():
            self.by_positions[strategy_id] = filter(
              lambda p: p.symbol != symbol,
              self.by_positions[strategy_id],
            )

    def get_positions_by_strategy(self, strategy_id: str) -> List[Position]:
        return self.by_positions[strategy_id]

    def get_positions(self, strategy_id: str, symbol: str) -> List[Position]:
        return filter(
          lambda p: p.symbol == symbol,
          self.get_positions_by_strategy(strategy_id)
        )
