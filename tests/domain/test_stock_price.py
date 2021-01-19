import os
import sys
from typing import List
from datetime import datetime
from decimal import Decimal

sys.path.insert(0, os.path.abspath('src'))

from the_pitch.domain import StockPrice

def test_create_many_from_objects():

    item = {
      'symbol': 'TSLA',
      'date': datetime.strptime('2020-01-06', '%Y-%m-%d'),
      'open': 10.0,
      'close': 12.33,
      'high': 20.3,
      'low': 0.5,
      'volume': 10323,
    }

    stock_prices: List[StockPrice] = StockPrice.create_many_from_objects([ item ])

    stock_price = stock_prices[0]

    assert stock_price.symbol == 'TSLA'
    assert stock_price.created_at == datetime.strptime('2020-01-06', '%Y-%m-%d')
    assert stock_price.open == Decimal('10')
    assert stock_price.close == Decimal('12.33')
    assert stock_price.high == Decimal('20.3')
    assert stock_price.low == Decimal('.5')
    assert stock_price.volume == 10323
