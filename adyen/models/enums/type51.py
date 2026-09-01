from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type51(str, Enum):
    """**sepadirectdebit**"""

    SEPADIRECTDEBIT = "sepadirectdebit"
    SEPADIRECTDEBIT_AMAZONPAY = "sepadirectdebit_amazonpay"

    __str__ = str.__str__


Type51OrStr: TypeAlias = Annotated[Type51 | str, open_enum_validator(Type51)]
