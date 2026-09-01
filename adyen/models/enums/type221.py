from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type221(str, Enum):
    """The type of transfer instrument.

    Possible value: **bankAccount**."""

    BANK_ACCOUNT = "bankAccount"
    RECURRING_DETAIL = "recurringDetail"

    __str__ = str.__str__


Type221OrStr: TypeAlias = Annotated[Type221 | str, open_enum_validator(Type221)]
