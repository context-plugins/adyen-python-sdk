from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CancellingEntity(str, Enum):
    MERCHANT = "merchant"
    CARDHOLDER = "cardholder"

    __str__ = str.__str__


CancellingEntityOrStr: TypeAlias = Annotated[CancellingEntity | str, open_enum_validator(CancellingEntity)]
