from enum import Enum

class LogicalOperator(Enum):
    Equal = 1
    NotEqual = 2
    LessThan = 3
    LessThanOrEqual = 4
    GreaterThan = 5
    GreaterThanOrEqual = 6

class ConditionOperator(Enum):
    AND = 1
    OR = 2

class Unit(Enum):
    Price = 1
    Stock = 2
    Percentage = 3

class Side(Enum):
    Buy = 1
    Sell = 2

class AssetType(Enum):
    Equity = 1
