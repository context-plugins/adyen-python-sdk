from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChargebackCostAllocation(str, Enum):
    """Deducts the chargeback costs from the specified balance account.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**"""

    DEDUCT_FROM_LIABLE_ACCOUNT = "deductFromLiableAccount"
    DEDUCT_FROM_ONE_BALANCE_ACCOUNT = "deductFromOneBalanceAccount"

    __str__ = str.__str__


ChargebackCostAllocationOrStr: TypeAlias = Annotated[
    ChargebackCostAllocation | str, open_enum_validator(ChargebackCostAllocation)
]
