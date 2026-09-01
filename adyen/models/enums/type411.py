from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type411(str, Enum):
    """**internal**"""

    INTERNAL = "internal"

    __str__ = str.__str__


Type411OrStr: TypeAlias = Annotated[Type411 | str, open_enum_validator(Type411)]
