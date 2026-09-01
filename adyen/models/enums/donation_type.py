from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DonationType(str, Enum):
    ROUNDUP = "roundup"
    FIXED_AMOUNTS = "fixedAmounts"
    FIXED_AMOUNTS_ROUNDUP = "fixedAmountsRoundup"

    __str__ = str.__str__


DonationTypeOrStr: TypeAlias = Annotated[DonationType | str, open_enum_validator(DonationType)]
