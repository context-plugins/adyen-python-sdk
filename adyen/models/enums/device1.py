from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Device1(str, Enum):
    """Possible values:
    * **CashierDisplay**
    * **CustomerDisplay**
    * **CashierInput**
    * **CustomerInput**"""

    CASHIER_DISPLAY = "CashierDisplay"
    CUSTOMER_DISPLAY = "CustomerDisplay"
    CASHIER_INPUT = "CashierInput"
    CUSTOMER_INPUT = "CustomerInput"

    __str__ = str.__str__


Device1OrStr: TypeAlias = Annotated[Device1 | str, open_enum_validator(Device1)]
