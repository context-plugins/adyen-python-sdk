from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RefundCostAllocation(str, Enum):
    """Deducts the refund costs from the specified balance account.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**"""

    DEDUCT_FROM_LIABLE_ACCOUNT = "deductFromLiableAccount"
    DEDUCT_FROM_ONE_BALANCE_ACCOUNT = "deductFromOneBalanceAccount"

    __str__ = str.__str__


RefundCostAllocationOrStr: TypeAlias = Annotated[RefundCostAllocation | str, open_enum_validator(RefundCostAllocation)]
