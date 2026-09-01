from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Surcharge3(str, Enum):
    """Books the surcharge amount to the specified balance account.

    Possible values: **addToLiableAccount**, **addToOneBalanceAccount**"""

    ADD_TO_LIABLE_ACCOUNT = "addToLiableAccount"
    ADD_TO_ONE_BALANCE_ACCOUNT = "addToOneBalanceAccount"

    __str__ = str.__str__


Surcharge3OrStr: TypeAlias = Annotated[Surcharge3 | str, open_enum_validator(Surcharge3)]
