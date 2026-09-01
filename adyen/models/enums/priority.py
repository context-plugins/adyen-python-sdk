from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Priority(str, Enum):
    """Determines how long it takes for the funds to reach the bank account. Adyen pays out based on the `payout
    frequency <https://docs.adyen.com/account/getting-paid#payout-frequency>`__. Depending on the currencies and banks
    involved in transferring the money, it may take up to three days for the payout funds to arrive in the bank account.

     Possible values:
    * **first**: same day.
    * **urgent**: the next day.
    * **normal**: between 1 and 3 days."""

    FIRST = "first"
    NORMAL = "normal"
    URGENT = "urgent"

    __str__ = str.__str__


PriorityOrStr: TypeAlias = Annotated[Priority | str, open_enum_validator(Priority)]
