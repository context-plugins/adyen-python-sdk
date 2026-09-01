from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubType11(str, Enum):
    """The specific category of **other** dispute that you are raising.

    Possible values: **atmDispute**, **cancelledGoodsServices**, **cancelledRecurring**, **counterfeit**,
    **creditNotProcessed**, **notAsDescribed**."""

    ATM_DISPUTE = "atmDispute"
    CANCELLED_GOODS_SERVICES = "cancelledGoodsServices"
    CANCELLED_RECURRING = "cancelledRecurring"
    CREDIT_NOT_PROCESSED = "creditNotProcessed"
    COUNTERFEIT = "counterfeit"
    NOT_AS_DESCRIBED = "notAsDescribed"

    __str__ = str.__str__


SubType11OrStr: TypeAlias = Annotated[SubType11 | str, open_enum_validator(SubType11)]
