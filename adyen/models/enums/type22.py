from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type22(str, Enum):
    """**directdebit_AU**"""

    DIRECTDEBIT_AU = "directdebit_AU"

    __str__ = str.__str__


Type22OrStr: TypeAlias = Annotated[Type22 | str, open_enum_validator(Type22)]
