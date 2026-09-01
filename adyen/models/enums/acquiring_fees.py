from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AcquiringFees(str, Enum):
    """Deducts the acquiring fees (the aggregated amount of interchange and scheme fee) from the specified balance
    account.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**."""

    DEDUCT_FROM_LIABLE_ACCOUNT = "deductFromLiableAccount"
    DEDUCT_FROM_ONE_BALANCE_ACCOUNT = "deductFromOneBalanceAccount"

    __str__ = str.__str__


AcquiringFeesOrStr: TypeAlias = Annotated[AcquiringFees | str, open_enum_validator(AcquiringFees)]
