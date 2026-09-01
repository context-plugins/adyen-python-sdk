from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type25(str, Enum):
    """**ideal**"""

    IDEAL = "ideal"

    __str__ = str.__str__


Type25OrStr: TypeAlias = Annotated[Type25 | str, open_enum_validator(Type25)]
