from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type54(str, Enum):
    """**vipps**"""

    VIPPS = "vipps"

    __str__ = str.__str__


Type54OrStr: TypeAlias = Annotated[Type54 | str, open_enum_validator(Type54)]
