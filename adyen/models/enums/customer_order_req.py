from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CustomerOrderReq(str, Enum):
    OPEN = "Open"
    CLOSED = "Closed"
    BOTH = "Both"

    __str__ = str.__str__


CustomerOrderReqOrStr: TypeAlias = Annotated[CustomerOrderReq | str, open_enum_validator(CustomerOrderReq)]
