from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DonationType1(str, Enum):
    """The type of donation to collect from the shopper. Possible values:

    - **roundup**: Round up the transaction amount.

    - **fixedAmounts**: Choose a fixed amount.

    - **fixedAmountsRoundup**: Round up, or choose a fixed amount."""

    ROUNDUP = "roundup"
    FIXED_AMOUNTS = "fixedAmounts"
    FIXED_AMOUNTS_ROUNDUP = "fixedAmountsRoundup"

    __str__ = str.__str__


DonationType1OrStr: TypeAlias = Annotated[DonationType1 | str, open_enum_validator(DonationType1)]
