from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type201(str, Enum):
    """The type of the webhook you are configuring. Set to **balance**."""

    BALANCE = "balance"

    __str__ = str.__str__


Type201OrStr: TypeAlias = Annotated[Type201 | str, open_enum_validator(Type201)]
