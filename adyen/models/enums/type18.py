from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type18(str, Enum):
    """Default payment method details. Common for scheme payment methods, and for simple payment method details."""

    SCHEME = "scheme"

    __str__ = str.__str__


Type18OrStr: TypeAlias = Annotated[Type18 | str, open_enum_validator(Type18)]
