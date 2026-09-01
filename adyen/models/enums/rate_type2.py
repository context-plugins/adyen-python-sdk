from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RateType2(str, Enum):
    """The type of transaction. Possible values:
    * **splitPayment**: for payments
    * **splitRefund**: for refunds"""

    SPLIT_PAYMENT = "splitPayment"
    BALANCE_CONVERSION = "balanceConversion"
    TRANSFER = "transfer"
    SPLIT_REFUND = "splitRefund"

    __str__ = str.__str__


RateType2OrStr: TypeAlias = Annotated[RateType2 | str, open_enum_validator(RateType2)]
