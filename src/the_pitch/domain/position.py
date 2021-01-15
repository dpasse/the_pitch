from . import AssetType
from decimal import Decimal
from datetime import date


class Position(object):
    def __init__(self, strategy_id: str, symbol: str, asset_type: AssetType, quantity: int, purchase_price: Decimal, purchase_date: date) -> None:
        self.strategy_id = strategy_id
        self.symbol = symbol
        self.asset_type = asset_type
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.purchase_date = purchase_date

    def to_obj(self) -> dict:
        return {
          'strategy_id': self.strategy_id,
          'symbol': self.symbol,
          'asset_type': self.asset_type,
          'quantity': self.quantity,
          'purchase_price': self.purchase_price,
          'purchase_date': self.purchase_date
        }
