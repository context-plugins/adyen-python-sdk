from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type310(str, Enum):
    """**bank**"""

    BANK = "bank"

    __str__ = str.__str__


Type310OrStr: TypeAlias = Annotated[Type310 | str, open_enum_validator(Type310)]
