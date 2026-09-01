from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RateType1(str, Enum):
    SPLIT_PAYMENT = "splitPayment"
    BALANCE_CONVERSION = "balanceConversion"
    TRANSFER = "transfer"
    SPLIT_REFUND = "splitRefund"

    __str__ = str.__str__


RateType1OrStr: TypeAlias = Annotated[RateType1 | str, open_enum_validator(RateType1)]
