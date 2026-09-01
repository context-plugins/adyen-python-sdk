from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type36(str, Enum):
    """**mbway**"""

    MBWAY = "mbway"

    __str__ = str.__str__


Type36OrStr: TypeAlias = Annotated[Type36 | str, open_enum_validator(Type36)]
