from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdyenFees(str, Enum):
    """Deducts the fees due to Adyen (markup or commission) from the specified balance account.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**."""

    DEDUCT_FROM_LIABLE_ACCOUNT = "deductFromLiableAccount"
    DEDUCT_FROM_ONE_BALANCE_ACCOUNT = "deductFromOneBalanceAccount"

    __str__ = str.__str__


AdyenFeesOrStr: TypeAlias = Annotated[AdyenFees | str, open_enum_validator(AdyenFees)]
