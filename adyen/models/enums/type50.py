from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type50(str, Enum):
    """**samsungpay**"""

    SAMSUNGPAY = "samsungpay"

    __str__ = str.__str__


Type50OrStr: TypeAlias = Annotated[Type50 | str, open_enum_validator(Type50)]
