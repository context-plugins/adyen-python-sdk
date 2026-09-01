from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CancellingEntity1(str, Enum):
    """The party that initiated the cancellation of the transaction.

    Possible values: **merchant**, **cardholder**."""

    MERCHANT = "merchant"
    CARDHOLDER = "cardholder"

    __str__ = str.__str__


CancellingEntity1OrStr: TypeAlias = Annotated[CancellingEntity1 | str, open_enum_validator(CancellingEntity1)]
