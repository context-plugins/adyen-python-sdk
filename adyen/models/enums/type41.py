from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type41(str, Enum):
    """**payto**"""

    PAYTO = "payto"

    __str__ = str.__str__


Type41OrStr: TypeAlias = Annotated[Type41 | str, open_enum_validator(Type41)]
