from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubType1(str, Enum):
    ATM_DISPUTE = "atmDispute"
    CANCELLED_GOODS_SERVICES = "cancelledGoodsServices"
    CANCELLED_RECURRING = "cancelledRecurring"
    CREDIT_NOT_PROCESSED = "creditNotProcessed"
    COUNTERFEIT = "counterfeit"
    NOT_AS_DESCRIBED = "notAsDescribed"

    __str__ = str.__str__


SubType1OrStr: TypeAlias = Annotated[SubType1 | str, open_enum_validator(SubType1)]
