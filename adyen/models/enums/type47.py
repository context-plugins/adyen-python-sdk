from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type47(str, Enum):
    """**rakutenpay**"""

    RAKUTENPAY = "rakutenpay"

    __str__ = str.__str__


Type47OrStr: TypeAlias = Annotated[Type47 | str, open_enum_validator(Type47)]
