from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type53(str, Enum):
    """The payment method type."""

    TWINT = "twint"

    __str__ = str.__str__


Type53OrStr: TypeAlias = Annotated[Type53 | str, open_enum_validator(Type53)]
