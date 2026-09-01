from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type2(str, Enum):
    """**afterpay_default**"""

    AFTERPAY_DEFAULT = "afterpay_default"
    AFTERPAYTOUCH = "afterpaytouch"
    AFTERPAY_B2B = "afterpay_b2b"
    CLEARPAY = "clearpay"

    __str__ = str.__str__


Type2OrStr: TypeAlias = Annotated[Type2 | str, open_enum_validator(Type2)]
