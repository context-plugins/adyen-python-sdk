from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type37(str, Enum):
    """**mobilepay**"""

    MOBILEPAY = "mobilepay"

    __str__ = str.__str__


Type37OrStr: TypeAlias = Annotated[Type37 | str, open_enum_validator(Type37)]
