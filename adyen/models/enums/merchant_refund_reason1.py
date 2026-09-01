from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MerchantRefundReason1(str, Enum):
    """Your reason for the refund request."""

    FRAUD = "FRAUD"
    CUSTOMER_REQUEST = "CUSTOMER REQUEST"
    RETURN = "RETURN"
    DUPLICATE = "DUPLICATE"
    OTHER = "OTHER"

    __str__ = str.__str__


MerchantRefundReason1OrStr: TypeAlias = Annotated[
    MerchantRefundReason1 | str, open_enum_validator(MerchantRefundReason1)
]
