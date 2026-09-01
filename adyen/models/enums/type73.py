from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type73(str, Enum):
    """The type of the transfer event. Possible values: **accounting**, **tracking**."""

    ACCOUNTING = "accounting"
    TRACING = "tracing"
    TRACKING = "tracking"

    __str__ = str.__str__


Type73OrStr: TypeAlias = Annotated[Type73 | str, open_enum_validator(Type73)]
