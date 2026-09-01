from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type44(str, Enum):
    """The payment method type."""

    PIX = "pix"

    __str__ = str.__str__


Type44OrStr: TypeAlias = Annotated[Type44 | str, open_enum_validator(Type44)]
