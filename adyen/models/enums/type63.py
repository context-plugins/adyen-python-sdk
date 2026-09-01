from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type63(str, Enum):
    """**platformPayment**"""

    PLATFORM_PAYMENT = "platformPayment"

    __str__ = str.__str__


Type63OrStr: TypeAlias = Annotated[Type63 | str, open_enum_validator(Type63)]
