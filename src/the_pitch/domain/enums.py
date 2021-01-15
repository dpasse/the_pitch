from enum import Enum


class LogicalOperator(Enum):
    Equal = 1
    NotEqual = 2
    LessThan = 3
    LessThanOrEqual = 4
    GreaterThan = 5
    GreaterThanOrEqual = 6

    def as_int(self):
        return self.value

class ConditionOperator(Enum):
    AND = 1
    OR = 2

    def as_int(self):
        return self.value

class Unit(Enum):
    Price = 1
    Stock = 2
    Percentage = 3

    def as_int(self):
        return self.value

class Side(Enum):
    Buy = 1
    Sell = 2

    def as_int(self):
        return self.value

class AssetType(Enum):
    Equity = 1

    def as_int(self):
        return self.value
