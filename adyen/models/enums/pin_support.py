from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PinSupport(str, Enum):
    """PIN Support. For ecommerce, PIN is required."""

    PIN = "PIN"
    NO_PIN = "NO PIN"

    __str__ = str.__str__


PinSupportOrStr: TypeAlias = Annotated[PinSupport | str, open_enum_validator(PinSupport)]
