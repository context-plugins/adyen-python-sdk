from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type91(str, Enum):
    BACK = "BACK"
    FRONT = "FRONT"
    UNDEFINED = "UNDEFINED"

    __str__ = str.__str__


Type91OrStr: TypeAlias = Annotated[Type91 | str, open_enum_validator(Type91)]
