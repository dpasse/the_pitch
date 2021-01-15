from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime

from ..domain.stock_price import StockPrice


@dataclass
class Dataset(object):
    data: List[StockPrice]
    test_data: Dict[datetime, List[StockPrice]]
