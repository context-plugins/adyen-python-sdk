from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Direction(str, Enum):
    """The direction of the transfer.

    Possible values: **incoming**, **outgoing**."""

    INCOMING = "incoming"
    OUTGOING = "outgoing"

    __str__ = str.__str__


DirectionOrStr: TypeAlias = Annotated[Direction | str, open_enum_validator(Direction)]
