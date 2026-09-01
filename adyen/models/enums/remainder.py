from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Remainder(str, Enum):
    """Books the amount left over after currency conversion to the specified balance account.

    Possible values: **addToLiableAccount**, **addToOneBalanceAccount**."""

    ADD_TO_LIABLE_ACCOUNT = "addToLiableAccount"
    ADD_TO_ONE_BALANCE_ACCOUNT = "addToOneBalanceAccount"

    __str__ = str.__str__


RemainderOrStr: TypeAlias = Annotated[Remainder | str, open_enum_validator(Remainder)]
