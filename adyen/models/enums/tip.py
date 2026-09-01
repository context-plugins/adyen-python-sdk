from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Tip(str, Enum):
    """Books the tips (gratuity) to the specified balance account.

    Possible values: **addToLiableAccount**, **addToOneBalanceAccount**."""

    ADD_TO_LIABLE_ACCOUNT = "addToLiableAccount"
    ADD_TO_ONE_BALANCE_ACCOUNT = "addToOneBalanceAccount"

    __str__ = str.__str__


TipOrStr: TypeAlias = Annotated[Tip | str, open_enum_validator(Tip)]
