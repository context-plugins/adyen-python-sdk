from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Interchange(str, Enum):
    """Deducts the interchange fee from specified balance account.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**."""

    DEDUCT_FROM_LIABLE_ACCOUNT = "deductFromLiableAccount"
    DEDUCT_FROM_ONE_BALANCE_ACCOUNT = "deductFromOneBalanceAccount"

    __str__ = str.__str__


InterchangeOrStr: TypeAlias = Annotated[Interchange | str, open_enum_validator(Interchange)]
