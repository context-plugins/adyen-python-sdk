from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type35(str, Enum):
    """**masterpass**"""

    MASTERPASS = "masterpass"

    __str__ = str.__str__


Type35OrStr: TypeAlias = Annotated[Type35 | str, open_enum_validator(Type35)]
