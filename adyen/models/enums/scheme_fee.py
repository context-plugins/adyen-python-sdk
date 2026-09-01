from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SchemeFee(str, Enum):
    """Deducts the scheme fee from the specified balance account.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**."""

    DEDUCT_FROM_LIABLE_ACCOUNT = "deductFromLiableAccount"
    DEDUCT_FROM_ONE_BALANCE_ACCOUNT = "deductFromOneBalanceAccount"

    __str__ = str.__str__


SchemeFeeOrStr: TypeAlias = Annotated[SchemeFee | str, open_enum_validator(SchemeFee)]
