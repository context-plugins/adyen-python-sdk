from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BalanceType(str, Enum):
    """Define the type of balance about which you want to get notified. Possible values:

    * **available**: the balance available for use.

    * **balance**: the sum of transactions that have already been settled.

    * **pending**: the sum of transactions that will be settled in the future.

    * **reserved**: the balance currently held in reserve."""

    BALANCE = "balance"
    AVAILABLE = "available"
    PENDING = "pending"
    RESERVED = "reserved"

    __str__ = str.__str__


BalanceTypeOrStr: TypeAlias = Annotated[BalanceType | str, open_enum_validator(BalanceType)]
