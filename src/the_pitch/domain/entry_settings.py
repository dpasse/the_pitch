from typing import Optional
from .order_target import OrderTarget
from .enums import Side


class EntrySettings(object):
    def __init__(self,
                symbol: str,
                side: Side,
                quantity: int = 1,
                stopLoss: Optional[OrderTarget] = None):
        self.symbol = symbol
        self.side = side
        self.quantity = quantity
        self.stopLoss = stopLoss
